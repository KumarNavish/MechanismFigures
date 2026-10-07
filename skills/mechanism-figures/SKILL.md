---
name: mechanism-figures
description: Design, implement, and rigorously critique scientific figures that reveal mechanisms through geometry, dynamics, correspondence, or structure. Use for explanatory research figures, not routine chart styling or decorative infographics.
license: MIT; third-party calibration images retain their stated licenses in THIRD_PARTY.md
compatibility: Requires an agent able to inspect images and edit files. Optional deterministic helpers use Python 3.9+ standard library. No model service, GPU, network, or plotting dependency is required by the skill itself.
metadata:
  author: Navish Kumar
  version: "0.3.0"
---

# MechanismFigures

**Learn from the approved real published figures. Make the mechanism visible at that standard, then test whether the picture tells the truth.**

The [approved gallery](assets/gallery.html) is the visual calibration authority: all 20 published references and 29 actual figure assets are included. Never replace them with self-generated examples or generic diagrams. This is a reasoning-and-review workflow, not a plot theme. An agent supplies scientific judgment and implementation. The scripts never generate research claims, call a model, or certify aesthetic quality.

An optional [60-second visual walkthrough](assets/motion.html) shows how this workflow uses the actual approved figures. It is an authored explanation, not a live run, generated scientific result, or substitute for the required image inspections.

## Enter with four inputs

Read the supplied **project context**, **result/mechanism**, **data/evidence**, and **output constraints**. Use the project's existing sources and tools before seeking more. Do not change the scientific objective to fit a reference.

Initialize one isolated figure folder with `python scripts/mf.py init /path/to/figure-work`. Paths below are relative to this installed skill; invoke scripts using their resolved absolute path when working elsewhere. The generated `figure.json` is the persistent contract. Fill it from the four inputs; do not ask the user to fill all its fields.

Before drawing anything, read [references/style-calibration.md](references/style-calibration.md), open at least **two actual approved reference images**, and record their composition, encoding, visual style and planned application. Read [references/choose.md](references/choose.md) and [references/critique.md](references/critique.md). Load [references/fidelity.md](references/fidelity.md) when evidence, causation, geometry, or uncertainty needs clarification; load [references/construct.md](references/construct.md) before implementation. Select **two** relevant cases through [references/calibration-index.md](references/calibration-index.md). Do not load the entire atlas into context.

## The execution loop

| Stage | Required decision / artifact | Advance only when |
|---|---|---|
| 1. Understand | Fill `inputs` and `analysis` in `figure.json`: state variables, units, update/relationship, assumptions, claim boundary, comparator, falsifier. | The proposed relationship has support, or is explicitly a hypothesis/schematic. |
| 2. Isolate | Write one sentence: **“The reader should see that ___ because ___.”** State one predicted change under one intervention. | It names a relationship, not a topic, score, or list of modules. |
| 3. Choose | Propose two genuinely different constructions. Record gain, distortion, and required evidence for each; choose by fidelity first. | The selected construction exposes something a scalar plot or box inventory would hide. |
| 4. Calibrate | Visually inspect at least two approved published figures; record image paths/hashes and concrete composition, encoding, annotation/style, and project-transfer observations. | Both actual images have been viewed. Text descriptions, invented images, or a self-generated example cannot substitute. |
| 5. Map | Fill an encoding table: scientific entity/quantity → visible object/channel → units/status → evidence IDs. Plan a captionless prediction probe. | Every meaningful position, width, arrow, join, and transformation has an explicit meaning. |
| 6. Compose | Draw a rough, unstyled construction using the actual relationship and smallest sufficient worked instance. | The mechanism survives without decoration. The same entities and controls stay traceable. |
| 7. Implement | Produce editable vector, actual-size preview, caption, source, and reproducible inputs. Use existing project tooling. | The source regenerates the outputs; no synthetic illustration is mislabeled as an experimental result. |
| 8. Critique | Inspect the rendered preview, compare with the two references, record evidence-linked scores and hard gates in a fresh `review.json`. | Review is tied to the exact contract and output hashes. |
| 9. Repair | Fix the highest-impact defect; render again; record change and effect in `revisions.jsonl`; create a new review. | Every hard gate passes, every dimension is ≥4/5, fidelity is 5/5, and weighted score is ≥90/100. |

**Meaning precedes polish.** Repair order: scientific error → hidden mechanism → false or missing comparison → unreadable encoding → composition → typography/color/detail. Never improve the score by merely changing its justification.

## Non-negotiable rules

- Keep the scientific object visible. Generic boxes may locate peripheral stages; they must not replace the decisive operation.
- Use literal geometry or a defined transformation before using metaphor. A metaphor is admissible only if its mapping and limits are stated.
- Preserve entity identity, coordinates, scales, time alignment, and experimental controls across comparisons. Declare any difference.
- Distinguish **measured**, **inferred**, **simulated**, **formal**, and **schematic** content. Arrows encode specified dependencies or transitions; they are not automatic causal proof.
- Attach evidence to the event or object it actually concerns. Check identity/time joins, normalization, uncertainty, and representative-example selection.
- Show the smallest complete mechanism, not the whole project. Keep background, benchmarks, and literature that do not change the figure's reading outside the figure.
- Originality means a precise adaptation to this problem, not novelty for its own sake. Reuse a fitting visual operation; do not copy the reference's domain objects or visual signature without reason.
- Do not infer topology from projection, history from snapshots, global behavior from one example, or algorithm speed from a count of drawn steps.
- If the evidence supports only an association, draw the association or a labeled competing-mechanisms figure. Do not manufacture a causal story to satisfy this skill.

## Review procedure and stopping rule

Use `python scripts/mf.py preflight /path/to/figure-work/figure.json` for deterministic file/SVG checks. Then `python scripts/mf.py review-init /path/to/figure-work/figure.json --out /path/to/figure-work/review-r1.json` binds a blank review to current artifacts. **It does not score them.** Inspect the files and complete the review. Run `python scripts/mf.py gate /path/to/figure-work/figure.json /path/to/figure-work/review-r1.json`.

Test the captionless image against the frozen question and intervention prediction. Record actual reader responses; a creator's imagined response is a **self-review**, never a timed user test. Inspect at output dimensions, grayscale, and enlargement. Compare the mechanism region to the same actual calibration images at matched readable scale, not whole-page thumbnails. Record `composition_match`, `encoding_match`, `style_match`, and `remaining_gap` for each reference. A generic box diagram or decorated plot does not pass merely because its files are valid.

The rubric's thresholds are a demanding policy, not empirically validated probabilities of publication success. A gate may report `self_review_pass`; it may report `independent_review_pass` only with an additional, named independent review of the same hashes using `--require-independent`. Neither authenticates a reviewer's honesty or guarantees universal quality.

Revise while meaningful progress is possible. After two iterations without a mechanistic/fidelity improvement, change the construction rather than polishing it; keep the rejected variant. After two failed construction families or the user's budget limit, return `needs_revision`, `needs_evidence`, or `needs_independent_review` with the best inspected artifact and one precise unresolved decision. **Never lower the threshold, fabricate evidence, loop indefinitely, or call a subthreshold figure finished.** Resume from the same contract and revision history.

## Handoff

Return the vector, rendered preview, caption, generating source/data, contract, all review records, and revision log. Lead with the mechanism the figure makes visible, the actual gate status, and remaining limits. Report actual costs where available, unknown costs as unknown. Do not claim superiority to the calibration set without a matched, independently rated comparison.

An agent with no image-viewing capability may prepare the contract and source, but must return `needs_visual_review`, not a visual pass. Host permissions, data policy, protected evidence, and user-specified tools override any procedural default here.
