# Plenoxels

**A ray crosses a voxel grid, and each sample blends the eight corners of its voxel.**

Fridovich-Keil, Yu et al.. *Plenoxels: Radiance Fields without Neural Networks*. CVPR 2022, Method overview figure. [Publication](https://arxiv.org/abs/2112.05131)

**View:** 3D · **Moves:** Ray trace, Linked zoom

## Open the image

- [`assets/calibration/plenoxels.png`](../../assets/calibration/plenoxels.png): full figure. Raster at 2800 pixels wide of the vector file figures/overview.pdf in the arXiv source. Not redrawn.

Look at the image file. This text does not replace the look.

## Mechanism

A scene is a sparse grid of voxels. Each grid corner stores a density and spherical-harmonic coefficients. A sample on a camera ray reads a trilinear blend of the eight corners round it, and the samples on the ray integrate to one pixel colour.

## Where to look

1. Panel a: follow the ray from the camera through the training image into the sparse grid. One voxel is solid blue.
2. Panel b: that voxel, enlarged. The orange arrows bring the values of the eight corners to the sample on the ray.
3. Panel c: the samples on the ray become a density curve and one predicted colour.

## Why it works

One ray is the persistent object. It keeps its direction and its style from the scene, to the enlarged voxel, to the plot. The zoom is a blue cone that starts at the marked voxel. The grid is dots and dashes, so it gives structure and no clutter.

## Take this

Carry one sample through the full method. Keep its line in the same direction in each panel. Enlarge the one cell where the operation occurs, and join the two views with a cone.

## Test your figure

Can the reader follow one line from the input to the output with no break?

## Limit

The right third is flat and holds a formula. The figure shows one ray. The optimisation over all rays is one line of text.

## Rights

The arXiv abstract page states CC BY 4.0. The image is a raster of the vector figure in the arXiv source. Status: `bundled`, [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
Selection: curator selection of 2026-11-13, not yet reviewed by the user.
