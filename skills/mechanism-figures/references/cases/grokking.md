# Grokking / modular addition — Draw the mathematical operation itself

Nanda et al. · ICLR 2023 · Figure 1

[Publication](https://arxiv.org/abs/2301.05217) · [Original image source](https://arxiv.org/pdf/2301.05217)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/436a75eb-grokking.png) — SHA-256 `09a000bcefb948b4c0a422d424d4e465c113f4c4c24a85c0a7c8d137cbc66aad`. Actual Figure 1 rasterized from the authors' arXiv manuscript.

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** A computation has a precise geometric interpretation such as rotation, projection, composition or alignment.

## See the mechanism

1. Read bottom to top: a and b become angles on the circle.
2. At the middle circle, the two rotations compose to a + b.
3. At the top, subtracting candidate c reveals which phase aligns with the answer.

**Mechanism:** The studied transformer computes modular addition using Fourier features and trigonometric composition.

**Visual construction:** Translate features into rotations on circles; carry those rotations through composition and candidate readout.

**What the eye understands:** The answer is an alignment operation: the correct candidate cancels the combined phase.

**Why an ordinary plot is weaker:** A grokking curve says when generalization appears. These circles show what computation supports it.

## Learn this visual style, then adapt it

**Observe:** Aligned model stages, trigonometric expressions and circles describe the same operation. Colored phase arrows preserve the identity of the operands through composition and readout.

**Apply:** Align symbolic, geometric and computational views of the same worked instance. Use color to preserve operand identity and direct labels to connect equations to the visible rotation.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Token values → your input variables; rotations → an established algebraic representation; alignment → the readout criterion.

**Keep the relationship:** Preserve the mapping between algebraic value and geometric position through every stage.

1. Identify an exact or empirically established operation, not a metaphor chosen for appearance.
2. Apply it visibly to one small worked example.
3. Put the corresponding model stage or equation beside the operation.

**Acceptance test:** Can a reader perform the toy computation by following the picture? Test several inputs and the boundary cases.

**Do not copy literally:** A pleasing circle is not evidence that the learned algorithm is rotational.

**Scientific boundary:** This explains a specific modular-addition setting. The figure is a mechanistic summary; separate analyses and ablations support it.

## Attribution and rights

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Approved published figure included for source-specific critical visual study. Original author/publisher rights remain; the repository MIT license does not license this image or grant further republication rights. A broadly reusable image license has not been established.
