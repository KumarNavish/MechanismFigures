# Grokking / modular addition: Draw the mathematical operation itself

Nanda et al. · ICLR 2023 · Figure 1

[Publication](https://arxiv.org/abs/2301.05217) · [Original asset](https://arxiv.org/pdf/2301.05217)

**Use when:** A computation has a precise geometric interpretation such as rotation, projection, composition or alignment.

## Look in this order

1. Read bottom to top: a and b become angles on the circle.
2. At the middle circle, the two rotations compose to a + b.
3. At the top, subtracting candidate c reveals which phase aligns with the answer.

## Mechanism → construction → immediate insight

**Mechanism:** The studied transformer computes modular addition using Fourier features and trigonometric composition.

**Construction:** Translate features into rotations on circles; carry those rotations through composition and candidate readout.

**The eye sees:** The answer is an alignment operation: the correct candidate cancels the combined phase.

**Why not an ordinary plot:** A grokking curve says when generalization appears. These circles show what computation supports it.

## Recreate the explanatory operation

**Replace the objects:** Token values → your input variables; rotations → an established algebraic representation; alignment → the readout criterion.

**Preserve:** Preserve the mapping between algebraic value and geometric position through every stage.

1. Identify an exact or empirically established operation, not a metaphor chosen for appearance.
2. Apply it visibly to one small worked example.
3. Put the corresponding model stage or equation beside the operation.

**Acceptance test:** Can a reader perform the toy computation by following the picture? Test several inputs and the boundary cases.

**Do not copy literally:** A pleasing circle is not evidence that the learned algorithm is rotational.

**Transfer example (proposal, not a finding):** For a projection algorithm, show the actual vector, feasible subspace and projected vector rather than a box labeled projection.

**Scientific boundary:** This explains a specific modular-addition setting. The figure is a mechanistic summary; separate analyses and ablations support it.

## Actual images and rights

Source-link-only: open the original figure above. No image is bundled, and no generated substitute is used. A text description does not count as image inspection.

Status: source-link-only. No broadly redistributable figure license verified; the paper and original asset are linked, not bundled.

License: not verified for redistribution. [Permission basis](https://arxiv.org/abs/2301.05217).

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.
