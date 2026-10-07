"""Deterministic contract, provenance and SVG preflight checks. No scientific scoring."""
from __future__ import annotations

import hashlib
import base64
import binascii
import json
import math
from pathlib import Path
import re
import struct
from typing import Any, Dict, List, Tuple
import xml.etree.ElementTree as ET

SKILL = Path(__file__).resolve().parents[1]
EVIDENCE_KINDS = {'measured', 'inferred', 'simulated', 'formal', 'schematic'}
PLACEHOLDERS = {'', 'TODO', 'TBD', 'REPLACE_ME'}


class ValidationError(ValueError):
    """A malformed or unsafe input that cannot be evaluated."""


def _pairs(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValidationError('Duplicate JSON key: ' + key)
        obj[key] = value
    return obj


def load_json(path: Path) -> Dict[str, Any]:
    def reject_constant(value):
        raise ValidationError('Non-finite JSON number: ' + value)
    try:
        obj = json.loads(Path(path).read_text(encoding='utf-8'),
                         object_pairs_hook=_pairs, parse_constant=reject_constant)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValidationError(str(exc)) from exc
    if not isinstance(obj, dict):
        raise ValidationError('Expected a JSON object: ' + str(path))
    return obj


def text(value: Any) -> bool:
    return isinstance(value, str) and value.strip() not in PLACEHOLDERS


def positive(value: Any) -> bool:
    return type(value) in (int, float) and math.isfinite(value) and value > 0


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def local_file(base: Path, name: Any, must_exist: bool = True) -> Path:
    """Resolve a project-relative file without following escape paths or symlinks."""
    if not isinstance(name, str) or not name or '\\' in name or '\x00' in name:
        raise ValidationError('Invalid local path: ' + repr(name))
    rel = Path(name)
    if rel.is_absolute() or '..' in rel.parts or name.startswith(('http:', 'https:')):
        raise ValidationError('Expected a contained relative path: ' + name)
    base = base.resolve()
    candidate = base / rel
    cursor = base
    for part in rel.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise ValidationError('Symlink paths are not accepted: ' + name)
    try:
        candidate.resolve().relative_to(base)
    except ValueError as exc:
        raise ValidationError('Path escapes work directory: ' + name) from exc
    if must_exist and (not candidate.is_file() or candidate.stat().st_size == 0):
        raise ValidationError('Missing or empty file: ' + name)
    return candidate


def _section(parent: Any, key: str, errors: List[str]) -> Dict[str, Any]:
    value = parent.get(key) if isinstance(parent, dict) else None
    if not isinstance(value, dict):
        errors.append(key + ': expected object')
        return {}
    return value


def _strings(parent, keys, prefix, errors):
    for key in keys:
        if not text(parent.get(key)):
            errors.append(prefix + '.' + key + ': required non-placeholder text')


def _list(parent, key, prefix, errors, minimum=0):
    value = parent.get(key)
    if not isinstance(value, list) or len(value) < minimum:
        errors.append(prefix + '.' + key + ': expected list with >= ' + str(minimum) + ' entries')
        return []
    return value


def validate_contract(contract: Dict[str, Any], stage: str = 'plan') -> List[str]:
    """Validate declared structure. Does not check whether scientific statements are true."""
    errors: List[str] = []
    if contract.get('schema_version') != 1 or isinstance(contract.get('schema_version'), bool):
        errors.append('schema_version must be integer 1')
    known = {'schema_version', 'id', 'creator_id', 'inputs', 'analysis', 'design', 'outputs', 'reproduction'}
    if set(contract) - known:
        errors.append('Unknown top-level fields: ' + ', '.join(sorted(set(contract) - known)))
    _strings(contract, ['id', 'creator_id'], 'contract', errors)
    inputs = _section(contract, 'inputs', errors)
    _strings(inputs, ['project_context', 'mechanism'], 'inputs', errors)
    constraints = _section(inputs, 'output_constraints', errors)
    _strings(constraints, ['audience', 'accessibility'], 'output_constraints', errors)
    for key in ['width_mm', 'height_mm', 'min_font_pt']:
        if not positive(constraints.get(key)):
            errors.append('output_constraints.' + key + ': expected finite positive number')
    formats = _list(constraints, 'formats', 'output_constraints', errors, 1)
    if any(x not in {'svg', 'png', 'pdf'} for x in formats):
        errors.append('output_constraints.formats: supported checked formats are svg, png, pdf')
    evidence = _list(inputs, 'evidence', 'inputs', errors, 1)
    evidence_ids = set()
    for i, item in enumerate(evidence):
        prefix = 'evidence[' + str(i) + ']'
        if not isinstance(item, dict):
            errors.append(prefix + ': expected object'); continue
        _strings(item, ['id', 'source', 'supports', 'does_not_support'], prefix, errors)
        if item.get('kind') not in EVIDENCE_KINDS:
            errors.append(prefix + '.kind: unknown evidence type')
        eid = item.get('id')
        if isinstance(eid, str):
            if eid in evidence_ids:
                errors.append('Duplicate evidence id: ' + eid)
            evidence_ids.add(eid)
    if stage == 'inputs':
        return errors
    analysis = _section(contract, 'analysis', errors)
    _strings(analysis, ['insight', 'update_rule', 'claim_boundary', 'falsifier'], 'analysis', errors)
    entities = _list(analysis, 'entities', 'analysis', errors, 1)
    entity_ids = set()
    for entity in entities:
        if not isinstance(entity, dict):
            errors.append('entities: expected objects'); continue
        _strings(entity, ['id', 'meaning', 'units'], 'entity', errors)
        eid = entity.get('id')
        if isinstance(eid, str):
            if eid in entity_ids:
                errors.append('Duplicate entity id: ' + eid)
            entity_ids.add(eid)
    assumptions = _list(analysis, 'assumptions', 'analysis', errors, 1)
    if any(not text(s) for s in assumptions):
        errors.append('assumptions: each assumption must be explicit text')
    comp = _section(analysis, 'comparison', errors)
    _strings(comp, ['baseline', 'intervention', 'budget'], 'comparison', errors)
    fixed = _list(comp, 'held_fixed', 'comparison', errors, 1)
    if any(not text(s) for s in fixed):
        errors.append('comparison.held_fixed: nonempty text required')
    unknowns = _list(analysis, 'unknowns', 'analysis', errors)
    for item in unknowns:
        if not isinstance(item, dict) or item.get('impact') not in {'blocking', 'background'} or type(item.get('resolved')) is not bool:
            errors.append('unknowns: require impact blocking/background and boolean resolved'); continue
        if item['impact'] == 'blocking' and not item['resolved']:
            errors.append('Unresolved figure-critical unknown: ' + str(item.get('id', '?')))
    design = _section(contract, 'design', errors)
    candidates = _list(design, 'candidates', 'design', errors, 2)
    if len(candidates) != 2:
        errors.append('Use exactly two distinct construction candidates')
    candidate_ids, constructions = set(), set()
    for candidate in candidates:
        if not isinstance(candidate, dict):
            errors.append('candidate: expected object'); continue
        _strings(candidate, ['id', 'construction', 'visible_gain', 'distortion_risk', 'evidence_needed'], 'candidate', errors)
        if isinstance(candidate.get('id'), str): candidate_ids.add(candidate['id'])
        if isinstance(candidate.get('construction'), str): constructions.add(candidate['construction'].lower().strip())
    if len(candidate_ids) != 2 or len(constructions) != 2:
        errors.append('Candidates must have distinct IDs and constructions, not just new colors')
    if design.get('selected') not in candidate_ids:
        errors.append('design.selected must identify one candidate')
    encoding = _list(design, 'encoding', 'design', errors, 1)
    for item in encoding:
        if not isinstance(item, dict):
            errors.append('encoding: expected object'); continue
        _strings(item, ['scientific', 'visual', 'units'], 'encoding', errors)
        if item.get('status') not in EVIDENCE_KINDS:
            errors.append('encoding.status must define evidence type')
        ids = item.get('evidence_ids')
        if not isinstance(ids, list) or not ids or any(not isinstance(eid, str) or eid not in evidence_ids for eid in ids):
            errors.append('encoding.evidence_ids must point to existing evidence')
    registry = {r['id']: r for r in load_json(SKILL / 'assets/calibration.json')['references']}
    readings = _list(design, 'reference_readings', 'design', errors, 2)
    seen_ids, visually_seen = set(), 0
    for item in readings:
        if not isinstance(item, dict):
            errors.append('reference_readings: expected objects'); continue
        _strings(item, ['id', 'insight', 'do_not_copy', 'composition_observation', 'encoding_observation', 'style_observation', 'planned_application'], 'reference_reading', errors)
        rid = item.get('id')
        if not isinstance(rid, str) or rid not in registry:
            errors.append('reference_reading.id: unknown calibration reference')
        elif rid in seen_ids:
            errors.append('Duplicate reference reading: ' + rid)
        else: seen_ids.add(rid)
        if type(item.get('image_observed')) is not bool:
            errors.append('reference_reading.image_observed must be boolean')
        elif item['image_observed']:
            visually_seen += 1
            observed = item.get('asset_seen')
            if not text(observed):
                errors.append('Visually inspected reference requires asset_seen path or URL')
            elif isinstance(rid, str) and rid in registry:
                ref = registry[rid]
                registered = {a['path']: a for a in ref['assets']}
                if observed not in registered:
                    errors.append('Reference inspection must name an actual installed approved image: ' + rid)
                else:
                    selected_asset = registered[observed]
                    if item.get('asset_sha256') != selected_asset['sha256']:
                        errors.append('Reference image hash missing or does not match approved asset: ' + rid)
                    try:
                        actual_asset = local_file(SKILL, observed)
                        if digest(actual_asset) != selected_asset['sha256']:
                            errors.append('Approved calibration image bytes were modified: ' + rid)
                    except ValidationError as exc: errors.append(str(exc))
        else:
            errors.append('Every selected reference must be visually inspected; no text-only substitute')
    if visually_seen < 2:
        errors.append('At least two actual approved reference images must be inspected before drawing')
    path = _list(design, 'reading_path', 'design', errors, 3)
    if len(path) != 3 or any(not text(s) for s in path):
        errors.append('design.reading_path requires exactly three concrete eye actions')
    for key in ['prediction_probe', 'counterfactual_probe']:
        probe = _section(design, key, errors)
        _strings(probe, ['question', 'expected'], key, errors)
    outputs = _section(contract, 'outputs', errors)
    _strings(outputs, ['vector', 'preview', 'caption', 'source'], 'outputs', errors)
    _list(outputs, 'additional', 'outputs', errors)
    reproduction = _section(contract, 'reproduction', errors)
    _strings(reproduction, ['command', 'environment'], 'reproduction', errors)
    return errors


def artifact_names(contract):
    outputs = contract.get('outputs', {})
    names = [outputs.get(k) for k in ['vector', 'preview', 'caption', 'source']]
    names += outputs.get('additional', []) if isinstance(outputs.get('additional'), list) else []
    for item in contract.get('inputs', {}).get('evidence', []):
        if isinstance(item, dict) and item.get('local_path'):
            names.append(item['local_path'])
    return list(dict.fromkeys(n for n in names if isinstance(n, str)))


def svg_checks(path: Path, constraints: Dict[str, Any]) -> Tuple[List[str], List[str]]:
    errors, warnings = [], []
    raw = path.read_text(encoding='utf-8')
    if re.search(r'<!DOCTYPE|<!ENTITY', raw, re.I):
        return ['SVG document types/entities are not accepted'], warnings
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as exc:
        return ['SVG parse error: ' + str(exc)], warnings
    if root.tag.split('}')[-1] != 'svg':
        return ['Vector file is not an SVG root'], warnings
    for el in root.iter():
        if el.tag.split('}')[-1].lower() in {'script', 'foreignobject'}:
            errors.append('SVG contains executable or foreign markup')
        for key, value in el.attrib.items():
            if key.split('}')[-1].lower().startswith('on'):
                errors.append('SVG contains an event handler')
            if key.split('}')[-1] == 'href' and not value.startswith('#'):
                # Actual scientific images may remain raster data inside an editable SVG.
                # Permit only inert, explicitly encoded PNG/JPEG bytes; never external URLs.
                image = re.fullmatch(r'data:image/(png|jpeg);base64,([A-Za-z0-9+/=\r\n]+)', value)
                if el.tag.split('}')[-1] != 'image' or image is None:
                    errors.append('SVG external or active embedded resource is not permitted')
                else:
                    try:
                        if len(image[2]) > 55_000_000: raise ValueError('Embedded image exceeds safety limit')
                        payload = base64.b64decode(image[2].replace('\n','').replace('\r',''), validate=True)
                        valid = payload.startswith(b'\x89PNG\r\n\x1a\n') if image[1] == 'png' else payload.startswith(b'\xff\xd8') and payload.endswith(b'\xff\xd9')
                        if not valid: errors.append('SVG embedded image signature does not match its MIME type')
                    except (ValueError, binascii.Error):
                        errors.append('SVG embedded image is malformed or too large')
    urls = re.findall(r'url\(([^)]*)\)', raw, re.I)
    # Quotes and whitespace around a local fragment do not make it external.
    if re.search(r'@import|@font-face', raw, re.I) or any(not value.strip().strip(chr(34)+chr(39)).startswith('#') for value in urls):
        errors.append('SVG external CSS/font/resource reference is not permitted')
    title = next((e for e in root.iter() if e.tag.split('}')[-1] == 'title'), None)
    desc = next((e for e in root.iter() if e.tag.split('}')[-1] == 'desc'), None)
    if title is None or not text(title.text): errors.append('SVG requires a meaningful title')
    if desc is None or not text(desc.text): errors.append('SVG requires an accessible description')
    dims = {}
    for key in ['width', 'height']:
        m = re.fullmatch(r'\s*([0-9.]+)mm\s*', root.get(key, ''))
        if not m:
            errors.append('SVG ' + key + ' must be explicit in mm'); continue
        try: dims[key] = float(m.group(1))
        except ValueError: errors.append('Malformed SVG dimension'); continue
        expected = constraints.get(key + '_mm')
        if not positive(dims[key]) or not positive(expected) or abs(dims[key] - expected) > 0.01:
            errors.append('SVG ' + key + ' does not match output constraints')
    try:
        vb = [float(x) for x in re.split(r'[\s,]+', root.get('viewBox', '').strip())]
        if len(vb) != 4 or not all(math.isfinite(v) for v in vb) or vb[2] <= 0 or vb[3] <= 0: raise ValueError()
    except ValueError:
        errors.append('SVG requires a finite positive viewBox'); vb = None
    if vb and 'width' in dims and 'height' in dims:
        if abs(dims['width'] / dims['height'] - vb[2] / vb[3]) > 0.01:
            errors.append('SVG physical and viewBox aspect ratios disagree')
        for e in root.iter():
            if e.tag.split('}')[-1] != 'text': continue
            font = e.get('font-size')
            if not font:
                warnings.append('Inherited/CSS font size needs rendered final-size inspection'); continue
            try:
                f = float(font)
                pt = f * dims['width'] / vb[2] * 72 / 25.4
                if pt < constraints.get('min_font_pt', 7) - 0.01:
                    errors.append('SVG label below physical minimum: {:.2f} pt'.format(pt))
            except ValueError:
                warnings.append('Non-numeric font size requires rendered inspection')
    if any('transform' in e.attrib for e in root.iter()):
        warnings.append('Transforms may change effective text size; manual inspection required')
    warnings.append('Geometry checks do not prove no clipping, correct science, or visual quality')
    return sorted(set(errors)), sorted(set(warnings))


def preflight(path: Path) -> Dict[str, Any]:
    path = Path(path).resolve()
    contract = load_json(path)
    errors = validate_contract(contract)
    warnings: List[str] = []
    if errors:
        return {'status': 'needs_contract', 'errors': errors, 'warnings': warnings}
    base = path.parent
    outputs = contract['outputs']
    for name in artifact_names(contract):
        try: local_file(base, name)
        except ValidationError as exc: errors.append(str(exc))
    if len(set(outputs[k] for k in ['vector', 'preview', 'caption', 'source'])) != 4:
        errors.append('Source, vector, preview, and caption must be distinct artifacts')
    available = {Path(n).suffix.lower().lstrip('.') for n in [outputs['vector'], outputs['preview']] + outputs['additional'] if isinstance(n, str)}
    for fmt in contract['inputs']['output_constraints']['formats']:
        if fmt not in available: errors.append('Requested export format is missing: ' + fmt)
    if not errors:
        vector = local_file(base, outputs['vector'])
        if vector.suffix.lower() != '.svg': errors.append('Editable vector must be SVG; include PDF as an additional export')
        else:
            ve, vw = svg_checks(vector, contract['inputs']['output_constraints'])
            errors.extend(ve); warnings.extend(vw)
        for name in [outputs['preview']] + outputs['additional']:
            f = local_file(base, name)
            b = f.read_bytes()[:32]
            if f.suffix.lower() == '.png':
                if len(b) < 24 or b[:8] != b'\x89PNG\r\n\x1a\n' or b[12:16] != b'IHDR':
                    errors.append('Invalid PNG signature: ' + name)
                elif min(struct.unpack('>II', b[16:24])) == 0:
                    errors.append('Invalid PNG dimensions: ' + name)
            if f.suffix.lower() == '.pdf' and not b.startswith(b'%PDF-'):
                errors.append('Invalid PDF signature: ' + name)
        if Path(outputs['preview']).suffix.lower() != '.png': errors.append('Preview must be a rendered PNG')
    return {'status': 'preflight_pass' if not errors else 'needs_revision', 'errors': errors, 'warnings': warnings,
            'notice': 'File checks only. No aesthetic, scientific, or reproducibility claim is certified.'}


def snapshot(path: Path) -> Dict[str, Any]:
    path = Path(path).resolve()
    contract = load_json(path)
    return {'contract_sha256': digest(path), 'rubric_sha256': digest(SKILL / 'assets/rubric.json'),
            'calibration_sha256': digest(SKILL / 'assets/calibration.json'),
            'artifacts': {name: digest(local_file(path.parent, name)) for name in sorted(artifact_names(contract))}}
