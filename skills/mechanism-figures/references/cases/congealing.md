# Neural Congealing: Use a transported probe to show correspondence

Ofri-Amar et al. · CVPR 2023 · Figure 1

[Publication](https://openaccess.thecvf.com/content/CVPR2023/html/Ofri-Amar_Neural_Congealing_Aligning_Images_to_a_Joint_Semantic_Atlas_CVPR_2023_paper.html) · [Original asset](https://arxiv.org/pdf/2302.03956)

**Use when:** The claim is alignment, semantic identity or equivariance across deformation and viewpoint.

## Look in this order

1. Read one column from original butterfly to aligned butterfly.
2. Read across the aligned row: corresponding parts occupy common coordinates.
3. Inspect the transferred edit below: it follows the corresponding part back into each original pose.

## Mechanism → construction → immediate insight

**Mechanism:** A shared atlas maps corresponding semantic parts into common coordinates despite pose and appearance changes.

**Construction:** Align real objects, then propagate one localized edit back through their different shapes and viewpoints.

**The eye sees:** The edit stays attached to the corresponding part rather than to a fixed image location.

**Why not an ordinary plot:** An average matching score hides what was matched. A transported edit makes the correspondence inspectable.

## Recreate the explanatory operation

**Replace the objects:** Butterfly part → your persistent feature; atlas → reference coordinates; edit → localized test probe; inverse warp → transfer back.

**Preserve:** Use the same localized probe across cases. Keep the original examples visible so alignment is not mistaken for identical inputs.

1. Show diverse unaligned inputs in a fixed order.
2. Place their transformed versions directly underneath.
3. Apply one probe in common coordinates and display its return to every input.

**Acceptance test:** Does the probe remain attached to the intended feature? Include failures and cases outside the fitted regime.

**Do not copy literally:** Consistent coloring alone is not proof of a correct correspondence.

**Transfer example (proposal, not a finding):** For robot manipulation, transport the same contact target across differently posed objects and inspect where it lands.

**Scientific boundary:** Selected successes demonstrate correspondence qualitatively; they do not establish reliability over all inputs.

## Actual images and rights

- [focused figure](../../assets/calibration/afe52f89-congealing.jpg) — Actual Figure 1 from the authors' March 2023 arXiv manuscript; butterfly examples retained in their original order.

Status: bundled. Author manuscript license link is CC BY 4.0. Actual paper figure crop, not a reconstruction; figure-specific treatment is recorded below.

License: CC-BY-4.0. [Permission basis](https://arxiv.org/abs/2302.03956v2).

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.
