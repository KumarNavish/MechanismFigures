# DreamFusion — Return the update to its object

Poole, Jain, Barron & Mildenhall · ICLR 2023 · Figure 3

[Publication](https://openreview.net/forum?id=FjNys5c7VyY) · [Original image source](https://docs.nvidia.com/nemo-framework/user-guide/24.12/_images/dreamfusion_model_overview1.png)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/f022cea5-dreamfusion.png) — SHA-256 `4a0b4f5506ac8a206733a22b4a0ca7e53a52a37f1fe6ba9145d834fea22d022f`. The supplied guide's Figure 3, reproduced in NVIDIA documentation. The author project and OpenReview publication are linked separately.

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** A fixed evaluator, model or physical test produces a signal that iteratively changes another object.

## See the mechanism

1. Follow the peacock from density and albedo to a shaded camera rendering.
2. Follow the noisy image through the locked, frozen diffusion model.
3. Follow the bottom arrow back to the NeRF weights: this is the object being optimized.

**Mechanism:** A pretrained 2D diffusion model supplies a score-distillation update for a rendered, trainable 3D representation.

**Visual construction:** Reuse the same object across intermediate representations; show frozen-model locks and an explicit return path to the NeRF weights.

**What the eye understands:** A fixed image prior can guide changes in a different representation through its differentiable rendering.

**Why an ordinary plot is weaker:** A loss curve cannot show what is fixed, what changes, or how a 2D signal reaches a 3D object.

## Learn this visual style, then adapt it

**Observe:** The peacock persists through density, appearance, rendering, noise and feedback. Large grouped regions and the returning arrow distinguish trainable state from a frozen evaluator.

**Apply:** Keep one recognizable object across views and route feedback back to its exact mutable state. Use grouping and annotation to distinguish fixed versus trainable parts; do not draw an empty generic feedback loop.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** NeRF → your mutable state; rendering → observable prediction; frozen prior → evaluator; residual → update signal.

**Keep the relationship:** Distinguish mutable state from fixed evaluator. Preserve the identity of the object across views.

1. Place the mutable object on the left and its observation above the loop.
2. Show the actual discrepancy or feedback at the right, not a box labeled loss.
3. Route the update back to the precise parameters or parts that change.

**Acceptance test:** Can the reader identify what changes and what remains frozen? Verify that the displayed feedback is the implemented update.

**Do not copy literally:** A circular arrow alone does not explain an optimization mechanism.

**Scientific boundary:** The returned signal is not a ground-truth 3D measurement. The picture does not establish that the result is unique or geometrically correct.

## Attribution and rights

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Approved published figure included for source-specific critical visual study. Original author/publisher rights remain; the repository MIT license does not license this image or grant further republication rights. A broadly reusable image license has not been established.
