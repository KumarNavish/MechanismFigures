# Neural Congealing — Use a transported probe to show correspondence

Ofri-Amar et al. · CVPR 2023 · Figure 1

[Publication](https://openaccess.thecvf.com/content/CVPR2023/html/Ofri-Amar_Neural_Congealing_Aligning_Images_to_a_Joint_Semantic_Atlas_CVPR_2023_paper.html) · [Original image source](https://arxiv.org/pdf/2302.03956)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/afe52f89-congealing.jpg) — SHA-256 `7f1a954b19683a9e783005bd1f39bcc4b3a5e76c0e33a50983e35f4e75ea537a`. Actual Figure 1 from the authors' March 2023 arXiv manuscript; butterfly examples retained in their original order.

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** The claim is alignment, semantic identity or equivariance across deformation and viewpoint.

## See the mechanism

1. Read one column from original butterfly to aligned butterfly.
2. Read across the aligned row: corresponding parts occupy common coordinates.
3. Inspect the transferred edit below: it follows the corresponding part back into each original pose.

**Mechanism:** A shared atlas maps corresponding semantic parts into common coordinates despite pose and appearance changes.

**Visual construction:** Align real objects, then propagate one localized edit back through their different shapes and viewpoints.

**What the eye understands:** The edit stays attached to the corresponding part rather than to a fixed image location.

**Why an ordinary plot is weaker:** An average matching score hides what was matched. A transported edit makes the correspondence inspectable.

## Learn this visual style, then adapt it

**Observe:** Original, aligned and edited images form consistent rows with each specimen in the same column. A localized edit visibly follows the corresponding semantic part.

**Apply:** Keep specimen order fixed and use actual input images. Compare transformations vertically, then transport one localized probe back to every original; let repeated correspondence organize the composition.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Butterfly part → your persistent feature; atlas → reference coordinates; edit → localized test probe; inverse warp → transfer back.

**Keep the relationship:** Use the same localized probe across cases. Keep the original examples visible so alignment is not mistaken for identical inputs.

1. Show diverse unaligned inputs in a fixed order.
2. Place their transformed versions directly underneath.
3. Apply one probe in common coordinates and display its return to every input.

**Acceptance test:** Does the probe remain attached to the intended feature? Include failures and cases outside the fitted regime.

**Do not copy literally:** Consistent coloring alone is not proof of a correct correspondence.

**Scientific boundary:** Selected successes demonstrate correspondence qualitatively; they do not establish reliability over all inputs.

## Attribution and rights

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Author manuscript license link is CC BY 4.0. Actual paper figure crop, not a reconstruction; figure-specific treatment is recorded below.

[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
