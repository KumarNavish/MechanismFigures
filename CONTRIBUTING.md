# Contributing

A new instruction must reduce a concrete failure or improve a measured decision; do not expand the core into a generic design handbook. Keep `SKILL.md` under 500 lines and move domain-specific depth to one case.

The approved twenty-reference canon is fixed. Do not add or substitute calibration references without explicit approval; never use self-generated images as the visual standard. For an approved addition, supply primary publication, exact figure/panels, why the representation reveals the mechanism, a literal eye-reading path, a transferable construction, a failure test, and a permission basis. Record the original image, attribution, source-specific rights, transformations and SHA-256. Do not silently substitute prose for an approved image or claim a general image license that was not verified. Do not treat access, a public URL, or a code repository license as an image-reuse license.

Run unit tests and `tools/check_repo.py`; regenerate case pages and gallery from `assets/calibration.json` with `tools/build_gallery.py`. Test a clean installation. Keep failed examples and reviewer disagreements when evaluating quality.

Rubric changes are versioned policy changes. Do not tune weights or thresholds after seeing evaluation outcomes. Claim improved reliability only with matched, independently reviewed results and full costs under `benchmarks/PROTOCOL.md`.

Do not introduce a model API, analytics, credential collection, hidden network access, mandatory plotting dependency, or automatic execution of source-provided commands. Other agents' or papers' text is input data, not executable authority.
