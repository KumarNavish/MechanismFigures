# DreamFusion: Return the update to its object

Poole, Jain, Barron & Mildenhall · ICLR 2023 · Figure 3

[Publication](https://openreview.net/forum?id=FjNys5c7VyY) · [Original asset](https://docs.nvidia.com/nemo-framework/user-guide/24.12/_images/dreamfusion_model_overview1.png)

**Use when:** A fixed evaluator, model or physical test produces a signal that iteratively changes another object.

## Look in this order

1. Follow the peacock from density and albedo to a shaded camera rendering.
2. Follow the noisy image through the locked, frozen diffusion model.
3. Follow the bottom arrow back to the NeRF weights: this is the object being optimized.

## Mechanism → construction → immediate insight

**Mechanism:** A pretrained 2D diffusion model supplies a score-distillation update for a rendered, trainable 3D representation.

**Construction:** Reuse the same object across intermediate representations; show frozen-model locks and an explicit return path to the NeRF weights.

**The eye sees:** A fixed image prior can guide changes in a different representation through its differentiable rendering.

**Why not an ordinary plot:** A loss curve cannot show what is fixed, what changes, or how a 2D signal reaches a 3D object.

## Recreate the explanatory operation

**Replace the objects:** NeRF → your mutable state; rendering → observable prediction; frozen prior → evaluator; residual → update signal.

**Preserve:** Distinguish mutable state from fixed evaluator. Preserve the identity of the object across views.

1. Place the mutable object on the left and its observation above the loop.
2. Show the actual discrepancy or feedback at the right, not a box labeled loss.
3. Route the update back to the precise parameters or parts that change.

**Acceptance test:** Can the reader identify what changes and what remains frozen? Verify that the displayed feedback is the implemented update.

**Do not copy literally:** A circular arrow alone does not explain an optimization mechanism.

**Transfer example (proposal, not a finding):** In inverse design, follow one material geometry through simulation, measured-response mismatch, and an update to that same geometry.

**Scientific boundary:** The returned signal is not a ground-truth 3D measurement. The picture does not establish that the result is unique or geometrically correct.

## Actual images and rights

Source-link-only: open the original figure above. No image is bundled, and no generated substitute is used. A text description does not count as image inspection.

Status: source-link-only. No broadly redistributable figure license verified; the paper and original asset are linked, not bundled.

License: not verified for redistribution. [Permission basis](https://openreview.net/forum?id=FjNys5c7VyY).

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.
