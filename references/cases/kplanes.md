# K-Planes

**A point in space and time is read from six planes.**

Fridovich-Keil, Meanti et al.. *K-Planes: Explicit Radiance Fields in Space, Time, and Appearance*. CVPR 2023, Method overview figure. [Publication](https://arxiv.org/abs/2301.10241)

**View:** 3D · **Moves:** Ray trace, Layer stack, Index to geometry

## Open the image

- [`assets/calibration/kplanes.png`](../../assets/calibration/kplanes.png): full figure. Raster at 2800 pixels wide of the vector file figures/triplane6_small.pdf in the arXiv source. Not redrawn.

Look at the image file. This text does not replace the look.

## Mechanism

A 4D field factorises into six planes: three for space and three that pair one space axis with time. A sample is projected onto each plane, read by bilinear interpolation at several scales, and the six readings are multiplied.

## Where to look

1. Find the sample q on the ray from the camera.
2. Follow q to its projections on the three space planes xy, xz, yz and on the three space-time planes.
3. Panel b: on each plane, the four grid values round the projection are blended at two scales. Panel c multiplies the six results.

## Why it works

The planes stand in 3D in their real orientation, thus the factorisation is a visible fact and not only an equation. The same point q appears on each plane with the same mark.

## Take this

When a method factorises a volume, draw the factors as planes or lines in their real orientation and project one sample onto each.

## Test your figure

Does one sample appear on each factor with the same mark?

## Limit

The two triads of planes overlap and are dense. Read the image at full size.

## Rights

The arXiv abstract page states CC BY 4.0. The image is a raster of the vector figure in the arXiv source. Status: `bundled`, [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
Selection: curator selection of 2026-11-13, not yet reviewed by the user.
