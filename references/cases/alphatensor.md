# AlphaTensor

**Matrix multiplication is a 3D block of ones and zeros.**

Fawzi et al.. *Discovering faster matrix multiplication algorithms with reinforcement learning*. Nature 2022, Figure 1, panel a. [Publication](https://www.nature.com/articles/s41586-022-05172-4)

**View:** 3D · **Moves:** Index to geometry, Exploded view

## Open the image

- [`assets/calibration/alphatensor-block.png`](../../assets/calibration/alphatensor-block.png): crop of panel a. Crop of panel a from the publisher file of Figure 1. No other change.
- [`assets/calibration/alphatensor-full.png`](../../assets/calibration/alphatensor-full.png): full figure. Publisher file of Figure 1, not changed.

Look at the image file. This text does not replace the look.

## Mechanism

The product of two 2 by 2 matrices is a 4 by 4 by 4 tensor of zeros and ones. An algorithm for the product is a decomposition of this tensor into rank-one terms, and fewer terms mean fewer multiplications.

## Where to look

1. Top: the product of two 2 by 2 matrices.
2. Below: a block of 4 by 4 by 4 cells, drawn as four separate slices. The axes are the entries of a, b and c.
3. A purple cube at (a, b, c) means that the product of that a and that b contributes to that c.

## Why it works

An abstract tensor becomes a physical block. The slices are pulled apart, so each cell is visible. Only the non-zero cells are solid.

## Take this

Draw a tensor as a block of cells. Separate the slices. Fill only the cells that carry information.

## Test your figure

Can the reader read one cell and say what it means?

## Limit

The block shows a structure and not a process. The crop is 572 pixels wide.

## Rights

The article page and the Crossref record state CC BY 4.0. Figure captions were not checked for third-party exceptions. Status: `bundled`, [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
Selection: curator selection of 2026-11-13, not yet reviewed by the user.
