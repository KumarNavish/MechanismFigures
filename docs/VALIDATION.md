# Validation evidence and what it does not establish

## Engineering

The regression suite exercises contract completeness; missing and contradictory fields; evidence references; output-format and physical-size checks; unsafe paths, symlinks and active SVGs; score bounds; weighted and per-dimension floors; unknown gates; stale contract/source/evidence/output hashes; creator-versus-independent review; preserved response records; and clean, idempotent, non-destructive installation.

Synthetic reviews in tests are explicitly fixtures. Their scores do not represent a reader study or a figure-quality result. Repository CI runs the same no-network standard-library checks on Python 3.9 and 3.12.

## Analytical examples

The projection source checks feasibility, preserved tangent, idempotence and nearest-point inequalities against a fixed comparison grid. The lag source checks the closed-form solution against the differential equation and verifies two equal slow readouts with opposite derivatives. These are exact toy checks, not novel research.

Creator visual inspection of the first renders found an annotation crossing the projection's dashed vector, a lag-state label touching its trajectory, and inadequate separation between a tick and axis title. Those first drafts are retained under each example's `history/`. The source was revised and previews re-rendered. This shows an actual inspect–repair loop, not just a passing schema.

Calibration inspection also revealed that Quartz/PDFKit had dropped portions of transparent Gaussian splats in an earlier PDF crop. Rendering the same page with MuPDF restored the complete primitives. The public asset registry records the corrected image hash, source, crop and renderer. No scientific content was redrawn.

## Review status

Example review files, where present, are **creator self-reviews**, not independent validation. The contracts document the worked constructions, and the response fields are retrospective self-assessment rather than timed or blind comprehension tests. `--require-independent` must therefore withhold independent acceptance. Do not use these examples as evidence that a generic agent has achieved the calibration quality bar.

## Not established

Cross-agent pass rates, inter-rater reliability, superiority to SciencePlots or an unassisted capable agent, measured time/token savings, generalization to held-out scientific projects, and universal publication-quality output have not been established. The protocol in `benchmarks/PROTOCOL.md` defines how to measure those outcomes without replacing science with schema success.
