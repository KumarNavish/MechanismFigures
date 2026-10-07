"""Evidence-linked review records. Scores are supplied by reviewers, never inferred."""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List
from _contract import SKILL, ValidationError, digest, load_json, local_file, positive, preflight, snapshot, text


def rubric():
    result = load_json(SKILL / 'assets/rubric.json')
    if sum(d['weight'] for d in result['dimensions']) != 100:
        raise ValidationError('Rubric weights must sum to 100')
    return result


def blank_review(contract_path: Path) -> Dict[str, Any]:
    c = load_json(contract_path)
    check = preflight(contract_path)
    if check['errors']:
        raise ValidationError('Preflight must pass before review: ' + '; '.join(check['errors']))
    r = rubric()
    return {
        'schema_version': 1, 'rubric_version': r['version'],
        'reviewer': {'id': c['creator_id'], 'mode': 'self'},
        'snapshot': snapshot(contract_path),
        'observations': {
            'viewed_files': [],
            'final_size': {'width_mm': c['inputs']['output_constraints']['width_mm'],
                           'height_mm': c['inputs']['output_constraints']['height_mm'], 'notes': ''},
            'captionless': {'response': '', 'prediction': '', 'matches_contract': None,
                            'justification': '', 'timing': 'not_measured'},
            'grayscale': {'inspected': False, 'notes': ''},
            'reference_comparison': [],
            'response_record': None
        },
        'gates': {g: {'status': 'unknown', 'evidence': '', 'files': []} for g in r['hard_gates']},
        'scores': {d['id']: {'score': None, 'evidence': '', 'residual_issue': ''} for d in r['dimensions']},
        'adverse_observation': '', 'next_action': ''
    }


def evaluate_review(contract_path: Path, review: Dict[str, Any]) -> Dict[str, Any]:
    contract_path = Path(contract_path).resolve()
    c, r = load_json(contract_path), rubric()
    errors: List[str] = []
    def require(value, message):
        if not value: errors.append(message)
    require(review.get('schema_version') == 1 and type(review.get('schema_version')) is int, 'Unsupported review schema')
    require(review.get('rubric_version') == r['version'], 'Rubric version mismatch')
    require(review.get('snapshot') == snapshot(contract_path), 'Stale or incorrect snapshot: contract/output/evidence changed')
    reviewer = review.get('reviewer', {})
    if not isinstance(reviewer, dict): reviewer = {}
    mode, reviewer_id = reviewer.get('mode'), reviewer.get('id')
    require(mode in {'self', 'independent'}, 'Reviewer mode must be self or independent')
    require(text(reviewer_id), 'Reviewer identity is missing')
    if mode == 'self': require(reviewer_id == c['creator_id'], 'Self-review must identify the figure creator')
    if mode == 'independent': require(reviewer_id != c['creator_id'], 'The creator cannot count as an independent reviewer')
    obs = review.get('observations', {})
    if not isinstance(obs, dict): obs = {}
    viewed = obs.get('viewed_files', [])
    require(isinstance(viewed, list), 'viewed_files must be a list')
    if not isinstance(viewed, list): viewed = []
    for key in ['vector', 'preview']:
        require(c['outputs'][key] in viewed, 'Actual ' + key + ' inspection not recorded')
    valid_files = set(snapshot(contract_path)['artifacts']) | {contract_path.name}
    require(all(isinstance(n, str) and n in valid_files for n in viewed), 'Viewed file is not a bound artifact')
    fs = obs.get('final_size', {})
    if not isinstance(fs, dict): fs = {}
    for k in ['width_mm', 'height_mm']:
        actual, expected = fs.get(k), c['inputs']['output_constraints'][k]
        require(positive(actual) and abs(actual - expected) < 0.01, 'Final-size inspection mismatches ' + k)
    require(text(fs.get('notes')), 'Final-size inspection needs an observation')
    cold = obs.get('captionless', {})
    if not isinstance(cold, dict): cold = {}
    for key in ['response', 'prediction', 'justification']:
        require(text(cold.get(key)), 'Captionless ' + key + ' is missing')
    require(cold.get('matches_contract') is True, 'Captionless mechanism/prediction did not match the frozen contract')
    require(cold.get('timing') == 'not_measured' or positive(cold.get('timing')), 'Timing must be measured positive seconds or not_measured')
    gray = obs.get('grayscale', {})
    if not isinstance(gray, dict): gray = {}
    require(gray.get('inspected') is True and text(gray.get('notes')), 'Grayscale inspection and concrete observation required')
    comparisons = obs.get('reference_comparison', [])
    if not isinstance(comparisons, list): comparisons = []
    planned = {x['id'] for x in c['design']['reference_readings']}
    compared = set()
    for item in comparisons:
        if not isinstance(item, dict): errors.append('Invalid reference comparison'); continue
        rid = item.get('id')
        require(isinstance(rid, str) and rid in planned and text(item.get('observation')), 'Reference comparison must identify a planned reference and visible relationship')
        if isinstance(rid, str): compared.add(rid)
    require(len(compared) >= 2, 'Compare the result to two selected reference constructions')
    if mode == 'independent':
        record = obs.get('response_record')
        if not isinstance(record, dict): errors.append('Independent review requires a preserved captionless response record')
        else:
            try:
                p = local_file(contract_path.parent, record.get('path'))
                require(digest(p) == record.get('sha256'), 'Independent response record hash mismatch')
            except ValidationError as exc: errors.append(str(exc))
    gates = review.get('gates', {})
    if not isinstance(gates, dict): gates = {}
    require(set(gates) == set(r['hard_gates']), 'Exactly the canonical hard gates are required')
    for name in r['hard_gates']:
        item = gates.get(name, {})
        if not isinstance(item, dict): item = {}
        require(item.get('status') == 'pass', 'Hard gate not passed: ' + name)
        require(text(item.get('evidence')), 'Gate lacks inspection evidence: ' + name)
        files = item.get('files', [])
        require(isinstance(files, list) and bool(files) and all(isinstance(n, str) and n in valid_files for n in files), 'Gate lacks a bound artifact pointer: ' + name)
    scores = review.get('scores', {})
    if not isinstance(scores, dict): scores = {}
    require(set(scores) == {d['id'] for d in r['dimensions']}, 'Exactly ten canonical dimension scores are required')
    weighted, dimensions = 0.0, {}
    for d in r['dimensions']:
        name = d['id']; item = scores.get(name, {})
        if not isinstance(item, dict): item = {}
        score = item.get('score')
        valid = type(score) is int and 0 <= score <= 5
        require(valid, 'Score must be an integer 0–5: ' + name)
        if valid:
            weighted += d['weight'] * score / 5
            dimensions[name] = score
            require(score >= r['acceptance']['dimension_minimum'], 'Dimension below threshold: ' + name)
            if name == 'scientific_fidelity': require(score == 5, 'Scientific fidelity must be 5/5')
        require(text(item.get('evidence')), 'Score needs a concrete visible observation: ' + name)
        require(text(item.get('residual_issue')), 'State a remaining limit, even for a score of 5: ' + name)
    weighted = round(weighted, 6)
    require(weighted >= r['acceptance']['weighted_minimum'], 'Weighted score below 90/100')
    require(text(review.get('adverse_observation')), 'Keep the strongest adverse observation')
    require(text(review.get('next_action')), 'State the review consequence or next action')
    return {'passed': not errors, 'reviewer': reviewer_id, 'mode': mode, 'weighted_score': weighted,
            'dimensions': dimensions, 'errors': errors}


def gate(contract_path: Path, review_paths: List[Path], require_independent=False):
    check = preflight(contract_path)
    if check['errors']:
        return {'status': check['status'], 'accepted': False, 'preflight': check, 'reviews': []}
    results = [evaluate_review(contract_path, load_json(p)) for p in review_paths]
    all_pass = bool(results) and all(x['passed'] for x in results)
    self_pass = any(x['passed'] and x['mode'] == 'self' for x in results)
    independent = any(x['passed'] and x['mode'] == 'independent' for x in results)
    if not all_pass or not self_pass:
        status, accepted = 'needs_revision', False
    elif require_independent and not independent:
        status, accepted = 'needs_independent_review', False
    elif independent:
        status, accepted = 'independent_review_pass', True
    else:
        status, accepted = 'self_review_pass', True
    return {'status': status, 'accepted': accepted, 'reviews': results, 'preflight': check,
            'notice': 'Recorded review policy only. Reviewer identity, observations, and scientific truth are attestations, not authenticated by this tool.'}
