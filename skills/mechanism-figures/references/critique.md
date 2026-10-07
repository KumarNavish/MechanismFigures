# Quality-control loop

The canonical weights and hard gates are in `assets/rubric.json`. These are **design-policy thresholds**, not calibrated probabilities of quality. Scripts check records and integrity; the reviewer must actually inspect the figure and its evidence.

## Anchor scale

0 = missing or false; 1 = substantially misleading/unusable; 2 = partly present but the reader must reconstruct the argument; 3 = competent ordinary figure; 4 = reference-level explanatory performance for the stated audience; 5 = unusually direct and precise, supported by a concrete observation/test. Use integers and the lower anchor when uncertain. Never score from intent, code, or the author's caption alone.

| Dimension (weight) | 3: ordinary competent | 4: demanding threshold | 5: exceptional evidence |
|---|---|---|---|
| Mechanistic insight (18) | Names stages; relation needs prose | The operative relation can be traced visually | A correct counterfactual is predictable from the construction |
| Scientific fidelity (20) | Mostly accurate, some assumptions/encodings implicit | Claim, units and encodings trace to evidence; limits explicit | Critical geometry, controls and invariants are checked; no unsupported implied claim |
| Visual intuition (12) | Requires repeated legend/caption decoding | Objects and transformation read directly | A worked instance can be mentally executed with minimal decoding |
| Information hierarchy (8) | Main region exists but competes with detail | Entry point, operation and consequence read in order | Removing any remaining major element would lose a necessary reasoning step |
| Encoding originality (6) | Familiar diagram fitted to labels | Representation is specifically adapted to the actual relation | The adaptation reveals an otherwise hidden distinction; novelty is not decoration |
| Compositional clarity (8) | Alignment/spacing acceptable | Comparison, correspondence and grouping are unambiguous | Position and negative space perform part of the explanation without false metric implications |
| Annotation quality (6) | Mostly readable; labels define terms | Labels define exact objects/changes beside the relevant marks | No nontrivial lookup is needed on the critical path; qualification stays concise |
| Aesthetic refinement (8) | Clean but generic or slightly inconsistent | Coherent typography, strokes and restrained semantic color | No visible spacing, clipping or style defect distracts at the intended size |
| Publication readiness (8) | Preview works; production/provenance incomplete | Required formats, readable labels, credits and source are complete | Exact outputs regenerate; target-format and final-size checks are recorded |
| Immediate comprehensibility (6) | Topic is recognizable, relation uncertain | The frozen captionless question receives the correct answer | Correct mechanism and intervention prediction are reported, without prompting from the caption |

Weighted score = sum(weight × score / 5), maximum 100. **Accept only ≥90; all ten scores ≥4; fidelity =5; all hard gates pass.** No average may compensate for a false claim. Every score needs a figure-local evidence statement and a tested or inspected observation. Scores below 5 need a concrete residual limitation, not inflated praise.

## Hard gates

`truthful_claims`, `defined_encoding`, `matched_comparison`, `evidence_status`, `reference_inspected`, `captionless_probe`, `final_size`, `no_clipping`, `reproducible`, `output_constraints`.

Each is pass/fail/unknown plus evidence and a pointer to an inspected file. Unknown blocks acceptance. A comparison that is scientifically inapplicable may pass only with a precise reason and the relevant alternative validity check, not “N/A”. Gates are review attestations; the CLI does not determine whether their prose is true.

## Conduct four passes

**1. Cold read.** Show only the image at the intended size. Ask the contract's frozen question and intervention prediction before showing its answer or caption. Preserve the actual response. For self-review, explicitly label the response self-assessed; it is not a blind reader study. Record elapsed time only when measured. The “five-second test” is a useful test condition, not an excuse to invent timing or to penalize every complex scientific figure.

**2. Adversarial science.** Try to falsify the visual implication. Follow an arrow backwards. Check a boundary case, equal input with different support, an unmatched loading condition, or a projection artifact. Compare against raw evidence and stated equations. Ask whether an informed reader could infer a stronger claim than supported.

**3. Reference calibration.** Inspect two actual reference images at comparable readable scale. For each, name a specific operation ours matches, improves, or fails to match. Do not compare domain complexity or treat a large journal label as a score. Both selected references must be visually observed with their registered paths/hashes and explicit readings. Record composition_match, encoding_match, style_match and remaining_gap for each. A self-generated example cannot serve as a calibration reference.

**4. Production inspection.** View at physical output size, grayscale, and enlargement. Inspect labels, leader crossings, clipping, aspect ratio, layout correspondence and source/preview agreement. Verify the requested export formats. Captionless intuition and production polish cannot substitute for scientific checks.

## Repair, do not rationalize

Record one defect as: **location → mistaken reading → cause → edit → expected improvement**. Prioritize scientific fidelity, mechanism and intuition before polish. After editing, rerender and create a new review bound to the new hashes; preserve the old review. Raise a score only when a new visible observation supports it. Keep the strongest adverse observation in the final record.

Two consecutive non-improving iterations trigger a different construction. Two failed construction families or an explicit budget boundary trigger an honest non-final handoff; do not lower the acceptance threshold. A reviewer who authored the figure is a self-reviewer even when instructed to adopt a different persona.

## Independent review and claims

A completed self-review meeting policy earns `self_review_pass`, not certification. Publication-level independent status requires another named reviewer who did not create that revision, the same artifact snapshot, a captionless response record, and a passing rubric. Use `gate ... --require-independent` to enforce the recorded distinction. Reviewer identity and truthfulness remain externally auditable attestations, not cryptographic proof.

Report what was actually tested. Repository unit tests validate the tooling, not figure quality. Empirical claims about reduced agent-to-agent variance require matched cross-agent trials; see the repository's `benchmarks/PROTOCOL.md` before making such claims.
