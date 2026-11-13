# GraphCast

**The world stays visible while the representation changes.**

Lam et al.. *Learning skillful medium-range global weather forecasting*. Science 2023, Figure 1. [Publication](https://www.science.org/doi/10.1126/science.adi2336)

**View:** 3D · **Moves:** Block diagram, Field on geometry, Fixed-camera sequence, Layer stack

## Open the image

- [`assets/calibration/7b9f9e1b-graphcast.png`](../../assets/calibration/7b9f9e1b-graphcast.png): focused. The supplied guide's published architecture figure, reproduced in NVIDIA documentation. The original paper and author manuscript are linked separately; NVIDIA is the image host, not the paper's publisher.

Look at the image file. This text does not replace the look.

## Mechanism

A graph network maps weather fields onto a spherical multimesh, exchanges information, and decodes the next weather state.

## Where to look

1. Find the same globe at input and forecast output.
2. In d and f, trace grid points into mesh nodes and back again.
3. In g, compare short and long mesh edges: different spatial reaches belong to one processor.

## Why it works

Earth remains visible through grid, mesh and output. Enlargements expose the transfers; the lower mesh row makes scale differences directly comparable.

## Take this

Keep the physical substrate visible when it explains the graph and its interactions.

## Test your figure

Can the reader locate where information enters, travels and returns? Verify the actual graph adjacency and coordinate transforms.

## Do not copy

Do not replace an arbitrary latent graph with a globe unless its geometry is genuinely spatial.

## Limit

The graph depicts learned communication, not literal atmospheric transport. Forecast validity requires separate evaluation.

## Rights

Approved published figure included for source-specific critical visual study. Original author/publisher rights remain; the repository MIT license does not license this image or grant further republication rights. A broadly reusable image license has not been established. Status: `reference-excerpt`.
Selection: retained by the user on 2026-10-08.
