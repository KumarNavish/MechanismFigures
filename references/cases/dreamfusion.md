# DreamFusion

**The feedback returns to the object that changes.**

Poole, Jain, Barron & Mildenhall. *DreamFusion: Text-to-3D using 2D Diffusion*. ICLR 2023, Figure 3. [Publication](https://openreview.net/forum?id=FjNys5c7VyY)

**View:** 3D · **Moves:** Loop through one object, Ray trace

## Open the image

- [`assets/calibration/f022cea5-dreamfusion.png`](../../assets/calibration/f022cea5-dreamfusion.png): focused. The supplied guide's Figure 3, reproduced in NVIDIA documentation. The author project and OpenReview publication are linked separately.

Look at the image file. This text does not replace the look.

## Mechanism

A pretrained 2D diffusion model supplies a score-distillation update for a rendered, trainable 3D representation.

## Where to look

1. Follow the peacock from density and albedo to a shaded camera rendering.
2. Follow the noisy image through the locked, frozen diffusion model.
3. Follow the bottom arrow back to the NeRF weights: this is the object being optimized.

## Why it works

The peacock persists through density, appearance, rendering, noise and feedback. Large grouped regions and the returning arrow distinguish trainable state from a frozen evaluator.

## Take this

Expose both the forward observation and the exact return path of the update.

## Test your figure

Can the reader identify what changes and what remains frozen? Verify that the displayed feedback is the implemented update.

## Do not copy

A circular arrow alone does not explain an optimization mechanism.

## Limit

The returned signal is not a ground-truth 3D measurement. The picture does not establish that the result is unique or geometrically correct.

## Rights

Approved published figure included for source-specific critical visual study. Original author/publisher rights remain; the repository MIT license does not license this image or grant further republication rights. A broadly reusable image license has not been established. Status: `reference-excerpt`.
Selection: retained by the user on 2026-10-08.
