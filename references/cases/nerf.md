# NeRF

**Follow one ray all the way to one pixel.**

Mildenhall et al.. *NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis*. ECCV 2020, Figure 2. [Publication](https://www.matthewtancik.com/nerf)

**View:** 3D · **Moves:** Ray trace, Loop through one object

## Open the image

- [`assets/calibration/14900912-nerf.png`](../../assets/calibration/14900912-nerf.png): focused. Actual Figure 2 rasterized from the authors' arXiv manuscript.

Look at the image file. This text does not replace the look.

## Mechanism

A learned field supplies density and view-dependent color; volume rendering accumulates these along camera rays.

## Where to look

1. Choose one camera ray in a.
2. Follow its sampled locations into color and density in b, then the depth profile in c.
3. Find the corresponding pixel comparison in d: the chain ends in an observable residual.

## Why it works

The same rays connect a physical scene to sampled density/color, depth profiles and a pixel residual. Small labels describe the quantity at each transformation.

## Take this

Choose one traceable object and preserve its identity across every change of representation.

## Test your figure

Can every stage's output be matched to the next stage's input? Verify the actual reduction, units and weighting.

## Do not copy

A pipeline of named boxes does not show what is being transformed.

## Limit

This explains image formation and optimization. It does not imply that reconstructed scene geometry is unique.

## Rights

Approved published figure included for source-specific critical visual study. Original author/publisher rights remain; the repository MIT license does not license this image or grant further republication rights. A broadly reusable image license has not been established. Status: `reference-excerpt`.
Selection: retained by the user on 2026-10-08.
