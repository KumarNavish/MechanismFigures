# GraphCast — Keep the natural geometry on screen

Lam et al. · Science 2023 · Figure 1

[Publication](https://www.science.org/doi/10.1126/science.adi2336) · [Original image source](https://docs.nvidia.com/physicsnemo/25.11/_images/graphcast_architecture.png)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/7b9f9e1b-graphcast.png) — SHA-256 `f3ad9f38ed289af2215b198693b839e62b6054f09ffe08606088fcb4feb32784`. The supplied guide's published architecture figure, reproduced in NVIDIA documentation. The original paper and author manuscript are linked separately; NVIDIA is the image host, not the paper's publisher.

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** Computation acts on a physical surface, spatial graph or multiscale substrate.

## See the mechanism

1. Find the same globe at input and forecast output.
2. In d and f, trace grid points into mesh nodes and back again.
3. In g, compare short and long mesh edges: different spatial reaches belong to one processor.

**Mechanism:** A graph network maps weather fields onto a spherical multimesh, exchanges information, and decodes the next weather state.

**Visual construction:** Keep Earth as the common surface; enlarge grid-to-mesh and mesh-to-grid transfers and expose the hierarchy of edge lengths.

**What the eye understands:** Information changes representation and spatial reach, while remaining attached to the same physical world.

**Why an ordinary plot is weaker:** A forecast score hides the computation's spatial organization. These linked geometries show where and across what scales information is exchanged.

## Learn this visual style, then adapt it

**Observe:** Earth remains visible through grid, mesh and output. Enlargements expose the transfers; the lower mesh row makes scale differences directly comparable.

**Apply:** Anchor computation to the real spatial substrate. Use one consistent viewpoint and local magnifications to reveal representation changes; reserve strong color for active transfer or communication paths.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Earth → your physical domain; grid → observations; mesh → computation graph; mesh levels → interaction scales.

**Keep the relationship:** Distinguish measured grid, computational mesh and predicted field. Keep their spatial correspondence visible.

1. Use one physical domain as the anchor across input, computation and output.
2. Enlarge one transfer between representations so the mapping is explicit.
3. Reveal how different edge lengths or scales extend communication across that domain.

**Acceptance test:** Can the reader locate where information enters, travels and returns? Verify the actual graph adjacency and coordinate transforms.

**Do not copy literally:** Do not replace an arbitrary latent graph with a globe unless its geometry is genuinely spatial.

**Scientific boundary:** The graph depicts learned communication, not literal atmospheric transport. Forecast validity requires separate evaluation.

## Attribution and rights

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Approved published figure included for source-specific critical visual study. Original author/publisher rights remain; the repository MIT license does not license this image or grant further republication rights. A broadly reusable image license has not been established.
