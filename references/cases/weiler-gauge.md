# Coordinate-independent convolution

**Move a kernel along two paths: on a plane it agrees, on a sphere it rotates, on a Möbius strip it flips.**

Weiler, Forré, Verlinde and Welling. *Coordinate Independent Convolutional Networks: Isometry and Gauge Equivariant Convolutions on Riemannian Manifolds*. arXiv 2021, Figures 3, 27 and 23. [Publication](https://arxiv.org/abs/2106.06020)

**View:** 3D · **Moves:** Matched counterfactual, Unroll pair, Field on geometry

## Open the image

- [`assets/calibration/weiler-gauge-paths.png`](../../assets/calibration/weiler-gauge-paths.png): Figure 3. Raster at 2800 pixels wide of the vector file figures/intro_transport_ambiguity.pdf in the arXiv source. Not redrawn.
- [`assets/calibration/weiler-gauge-mobius.png`](../../assets/calibration/weiler-gauge-mobius.png): Figure 27. Raster of figures/mobius_conv_gauges.pdf in the arXiv source. Not redrawn.
- [`assets/calibration/weiler-gauge-pullback.png`](../../assets/calibration/weiler-gauge-pullback.png): Figure 23. Raster of figures/pullback_field_exp_TpM.pdf in the arXiv source. Not redrawn.

Look at the image file. This text does not replace the look.

## Mechanism

On a curved or non-orientable surface, the alignment of a convolution kernel depends on the path along which it moves. Thus the network must give the same result for each choice of local frame.

## Where to look

1. Figure 3: on each surface, follow the red path and the green path from the same start kernel to the same end point.
2. Compare the two kernels that arrive, in the row at the bottom: identity, rotation, flip.
3. Figure 27: the Möbius strip is cut into two charts and unrolled. Find where the charts agree (id) and where they differ (flip).

## Why it works

A matched counterfactual on three surfaces: only the surface changes. The kernel is a small image with a frame, so its orientation is readable at once. Soft grey surfaces with contact shadows keep all attention on the coloured paths. The lizard and the butterfly in figures 23 and 27 are asymmetric motifs, so a flip or a rotation is obvious.

## Take this

To show that a space changes an operation, do the same operation on three spaces with the same camera. Use an asymmetric motif when orientation matters. Unroll the surface when the reader must see its charts.

## Test your figure

Would the reader see the difference if the motif were symmetric? If not, change the motif.

## Limit

The notation in figures 23 and 27 is dense for a reader outside the field. The figures are formal illustrations and are not data.

## Rights

The arXiv abstract page states CC BY 4.0. The images are rasters of vector figures in the arXiv source. Status: `bundled`, [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
Selection: curator selection of 2026-11-13, not yet reviewed by the user.
