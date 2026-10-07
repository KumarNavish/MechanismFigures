# Required visual calibration: the approved published figures

**This is the quality standard for every figure task. Do not substitute a self-generated example, a remembered diagram, or a generic plotting template.**

The complete [approved gallery](../assets/gallery.html) contains twenty real published references and twenty-nine figure assets. Its original six anchors are AlphaFold, CellRank, GraphCast, DreamFusion, AlphaDev, and Aardvark. The remaining fourteen are the already-approved grand gallery, not a new selection. Source credits and scientific limitations remain attached to each image.

## 1. Look before drawing

After understanding the project, select at least two relevant references from [the index](calibration-index.md). Use one to calibrate the mechanism's visual encoding and one to calibrate the composition and visual finish; one image may serve both roles, but two actual images are still required.

Open the real files at readable size. Inspect the complete figure to understand its hierarchy, then a relevant panel at native size to see the actual geometry and annotation. Do not base a claim of inspection on an image filename, caption, search snippet, text summary, or a tiny thumbnail. All approved image files ship with the skill, so a broken remote host is no reason to replace the image with prose.

Run `python scripts/mf.py reference graphcast --json`, for example, to obtain that reference's actual asset paths and SHA-256 hashes. Record the path and hash of the file you viewed. If the host cannot view images, report `needs_visual_review`; do not pretend the style has been learned.

## 2. Record what is physically visible

For each reference, fill these fields in `design.reference_readings`:

| Field | Record something concrete |
|---|---|
| `id`, `asset_seen`, `asset_sha256` | Approved reference ID, installed image path, exact image hash. |
| `image_observed` | `true` only after the actual image was opened. Both selected references must be observed. |
| `composition_observation` | The actual placement and hierarchy: e.g. a physical domain anchors the main view; an enlarged local mapping sits directly below it. |
| `encoding_observation` | Which spatial relationship reveals the mechanism: e.g. the same indexed tensor entries become edges in a triangle. |
| `style_observation` | How annotation, typography, line weights, color roles and whitespace support the reading: e.g. only active edges are saturated; stable identifiers sit beside the edges they name. |
| `planned_application` | Exactly how this composition and visual grammar will appear in the current project. Name the project's real objects and operations. |
| `insight`, `do_not_copy` | What the construction explains, and which domain-specific facts, shapes, or assumptions do not transfer. |

“Clean,” “minimal,” “beautiful,” “use blue,” and “professional style” are not sufficient observations. Point to a panel or visible relation and state what it does for the reader.

## 3. Transfer the visual grammar, not just the subject labels

**AlphaFold:** align mathematical entities with actual geometric relations; preserve indices across matrix, graph and update views. Do not copy its triangle just because your system has three modules.

**CellRank:** keep one scientific state traceable from local evidence to global behavior; expose the intermediate transition rule. Do not turn inferred transitions into observed causal lineages.

**GraphCast:** preserve the natural spatial substrate across representations; show exactly where and at what scale information moves. Do not replace it with generic network boxes or introduce a globe into a non-spatial problem.

**DreamFusion:** retain a recognizable object through transformations and return feedback to the actual mutable state. Group fixed and trainable parts distinctly. A circular arrow around unnamed boxes is not an equivalent construction.

**AlphaDev:** align before and after, leave eliminated work visible as an omission, and place the enabling invariant beside it. Do not claim speed from fewer drawn steps alone.

**Aardvark:** make the layout join related evidence at the same entity and event. Preserve the roles of each modality; mere proximity does not establish a valid data join.

The other approved cases supply additional visual grammars for support, dynamics, correspondence, invariance, density evolution, spatial history and geometry-preserving construction. Select the one that matches the science. The common standard is a tangible scientific object, an inspectable operation, disciplined visual hierarchy, concise local annotations, controlled emphasis and substantial information without irrelevant decoration.

## 4. Compare the actual output back to the same images

After rendering, reopen the two references at comparable readable scale and inspect the candidate beside them. For each item in `observations.reference_comparison`, record:

- `composition_match`: which hierarchy, correspondence or layout operation the candidate carries over.
- `encoding_match`: which scientific relationship is now comparably visible.
- `style_match`: how annotation placement, line treatment, color roles, typography and whitespace match the reference's explanatory discipline.
- `remaining_gap`: the strongest visible shortfall or adaptation limit; do not write an invented claim of superiority.

The review gate rejects absent image inspection, unregistered images, wrong hashes, missing visual observations and missing output-to-reference comparisons. These records cannot prove an agent actually looked or guarantee aesthetics; they make omissions and self-generated substitutes explicit and auditable.

If the result has become a generic flowchart, a decorated standard plot, or a sparse toy diagram whose simplicity erases the real mechanism, it has not met this reference standard—even when its code and file checks pass. Return to the chosen images, identify the missing visual operation, and rebuild that part before polishing or accepting the result.
