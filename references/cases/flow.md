# Multisample Flow Matching

**Show when structure forms—and what a coarse solver misses.**

Pooladian et al.. *Multisample Flow Matching: Straightening Flows with Minibatch Couplings*. ICML 2023, Figure 2. [Publication](https://proceedings.mlr.press/v202/pooladian23a.html)

**View:** Flat · **Moves:** Matched counterfactual, Fixed-camera sequence

## Open the image

- [`assets/calibration/e65934cc-flow.jpg`](../../assets/calibration/e65934cc-flow.jpg): focused. Actual Figure 2 rasterized from the PMLR proceedings PDF.

Look at the image file. This text does not replace the look.

## Mechanism

The coupling changes the intermediate probability path and how well a coarse numerical solver reaches the target.

## Where to look

1. Read density evolution from left to right using the common time columns.
2. Compare when the checkerboard structure begins forming in different rows.
3. Move to the right-hand solver outputs: inspect what survives at a small number of function evaluations.

## Why it works

All methods share the same time columns and spatial domain; budget-limited outputs are attached to the corresponding row.

## Take this

If timing explains an outcome, align intermediate states and place the budget-limited consequence immediately beside them.

## Test your figure

Is the claimed mechanism visible before the endpoint? Match compute and inspect whether the intermediate difference predicts the result.

## Do not copy

Do not choose different favorable timesteps for different methods.

## Limit

These are density snapshots, not individual trajectories. The 2D example does not establish universal low-step performance.

## Rights

Approved published figure included for source-specific critical visual study. Original author/publisher rights remain; the repository MIT license does not license this image or grant further republication rights. A broadly reusable image license has not been established. Status: `reference-excerpt`.
Selection: retained by the user on 2026-10-08.
