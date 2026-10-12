# Construction kit

The kit is original MechanismFigures code. It supplies primitives and checks, not predesigned scientific figures. The current published gallery remains the visual calibration authority.

| Module | Provides | Does not provide |
|---|---|---|
| `kit/geometry.py` | Explicit orthographic camera, uniform frame fitting, affine transformations. | Physical meaning for latent axes, perspective rendering, collision/visibility proof. |
| `kit/scene.py` | Stable mark IDs, evidence tags, circles/polygons, owned anchors, routed arrows, physically sized labels, SVG and scene record. | Scientific model, automatic layout, complete text measurement or a quality verdict. |
| `kit/motion.mjs` | Deterministic time, pure `stateAt(t)` → rendering, pause/seek, visibility suspension and reduced motion. | A new scientific state update, WebGL, historical inference or independently authored readout values. |

## Use existing project tools when they are stronger

A complex volume, physical assembly or differentiable renderer should use the project's established implementation. Do not approximate its scientific geometry with these few primitives just to satisfy a toolkit preference. Bind its output to the same contract and inspect it with the same review.

## SVG API

Add the installed skill directory to the Python import path, then `from kit import Scene`. Supply `title`, `description`, physical width/height and a minimum text size. Each scientific mark requires `meaning`, `evidence=[...]` and `status` (`formal`, `measured`, `inferred`, `simulated`, or `schematic`). Evidence IDs must also exist in the project contract; the kit does not resolve publications for you.

- `scene.circle(id, (x,y), radius, ...)` and `scene.polygon(id, points, ...)` create identity-bearing geometry.
- `scene.anchor(name, (x,y), owner_id)` identifies an attachment location; it must be inside the owner's declared bounds. This is a bounded diagnostic, not an exact interface-intersection proof.
- `scene.route(id, start_anchor, end_anchor, via=..., ...)` draws from those exact endpoints. Intermediates are explicit; there is no hidden auto-routing.
- `scene.label(id, (x,y), text, for_mark=..., font_pt=8)` ties annotation to a known scientific mark and preserves the physical font size.
- `scene.audit()` reports out-of-frame geometry and invalid anchors, together with what it has not checked.
- `scene.save('figure.svg')` writes editable SVG and `figure.scene.json`, refusing to overwrite existing outputs. Choose a new revision path or explicitly manage the prior revision in project code.

World coordinates are in `units_per_mm`, default 6. All geometry, label positions and widths use those declared units; `font_pt` uses physical points. The palette's names are semantic conveniences; they do not infer scientific categories. Record color mappings in `figure.json`.

## Minimal data flow, not a universal drawing template

Read actual data or compute the justified formal state → derive coordinates and visual channels → draw named scientific objects → attach truthful labels → save source/data/vector → capture → inspect. A test fixture using two circles is useful for verifying the API; it is not a valid substitute for a reference-calibrated scientific construction.

Read [craft.md](craft.md) before implementing and [verify.md](verify.md) before delivering.
