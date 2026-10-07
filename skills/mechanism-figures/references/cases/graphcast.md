# GraphCast: Keep the natural geometry on screen

Lam et al. · Science 2023 · Figure 1

[Publication](https://www.science.org/doi/10.1126/science.adi2336) · [Original asset](https://docs.nvidia.com/physicsnemo/25.11/_images/graphcast_architecture.png)

**Use when:** Computation acts on a physical surface, spatial graph or multiscale substrate.

## Look in this order

1. Find the same globe at input and forecast output.
2. In d and f, trace grid points into mesh nodes and back again.
3. In g, compare short and long mesh edges: different spatial reaches belong to one processor.

## Mechanism → construction → immediate insight

**Mechanism:** A graph network maps weather fields onto a spherical multimesh, exchanges information, and decodes the next weather state.

**Construction:** Keep Earth as the common surface; enlarge grid-to-mesh and mesh-to-grid transfers and expose the hierarchy of edge lengths.

**The eye sees:** Information changes representation and spatial reach, while remaining attached to the same physical world.

**Why not an ordinary plot:** A forecast score hides the computation's spatial organization. These linked geometries show where and across what scales information is exchanged.

## Recreate the explanatory operation

**Replace the objects:** Earth → your physical domain; grid → observations; mesh → computation graph; mesh levels → interaction scales.

**Preserve:** Distinguish measured grid, computational mesh and predicted field. Keep their spatial correspondence visible.

1. Use one physical domain as the anchor across input, computation and output.
2. Enlarge one transfer between representations so the mapping is explicit.
3. Reveal how different edge lengths or scales extend communication across that domain.

**Acceptance test:** Can the reader locate where information enters, travels and returns? Verify the actual graph adjacency and coordinate transforms.

**Do not copy literally:** Do not replace an arbitrary latent graph with a globe unless its geometry is genuinely spatial.

**Transfer example (proposal, not a finding):** For a tissue model, keep the tissue geometry visible while measurements map to a cell graph, propagate, and return as a predicted field.

**Scientific boundary:** The graph depicts learned communication, not literal atmospheric transport. Forecast validity requires separate evaluation.

## Actual images and rights

Source-link-only: open the original figure above. No image is bundled, and no generated substitute is used. A text description does not count as image inspection.

Status: source-link-only. No broadly redistributable figure license verified; the paper and original asset are linked, not bundled.

License: not verified for redistribution. [Permission basis](https://www.science.org/doi/10.1126/science.adi2336).

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.
