# RFdiffusion

**Keep the constraint visible while structure emerges.**

Watson et al.. *De novo design of protein structure and function with RFdiffusion*. Nature 2023, Figure 1. [Publication](https://www.nature.com/articles/s41586-023-06415-8)

**View:** 3D · **Moves:** Fixed-camera sequence, Ghost and focus

## Open the image

- [`assets/calibration/rfdiffusion-figure.png`](../../assets/calibration/rfdiffusion-figure.png): focused. Unmodified publisher-hosted Figure 1.

Look at the image file. This text does not replace the look.

## Mechanism

Iterative denoising constructs protein backbones; conditioning supplies symmetry, a binding target or a fixed motif that constrains what the trajectory can become.

## Where to look

1. Read the noising/reverse-generative sequence in a, then identify the fixed conditioning object in each row of b.
2. Follow each row’s persistent motif or symmetry through the intermediate structures into the final backbone.
3. Compare the noisy input row with the clean-structure prediction row at matched denoising steps in c.

## Why it works

Rows are organized by a visible conditioning object; restrained, persistent colors distinguish fixed motifs from evolving structure. Matched temporal columns turn a complicated model into an inspectable transformation.

## Take this

Use aligned state sequences in which the protected or conditioning object remains recognizable throughout the update.

## Test your figure

Can a reader identify the unchanged constraint and distinguish the current state from its clean-state prediction?

## Do not copy

Do not copy protein imagery for a non-structural problem or imply that a smooth denoising sequence alone validates a designed function.

## Limit

The figure describes model construction and examples. Structural plausibility and predicted designability are not equivalent to experimental confirmation of binding or activity.

## Rights

Actual published figure excerpt included with source-specific critical study. No general redistribution license is asserted by this repository. Original authors/publishers retain rights; inspect the source terms and any third-party image credits before further reuse. Status: `reference-excerpt`.
Selection: curator selection of 2026-10-08.
