# NeRF: Keep one trace through every representation

Mildenhall et al. · ECCV 2020 · Figure 2

[Publication](https://www.matthewtancik.com/nerf) · [Original asset](https://arxiv.org/pdf/2003.08934)

**Use when:** A physical or computational signal passes through several representations before producing an observation.

## Look in this order

1. Choose one camera ray in a.
2. Follow its sampled locations into color and density in b, then the depth profile in c.
3. Find the corresponding pixel comparison in d: the chain ends in an observable residual.

## Mechanism → construction → immediate insight

**Mechanism:** A learned field supplies density and view-dependent color; volume rendering accumulates these along camera rays.

**Construction:** Carry identifiable rays from a 3D scene into depth profiles and finally into pixel-color comparisons.

**The eye sees:** A pixel is an accumulation through space—not a color emitted by an unexplained network box.

**Why not an ordinary plot:** A pipeline names the stages. Following the ray exposes the physical meaning of the intermediate quantities.

## Recreate the explanatory operation

**Replace the objects:** Ray → your traceable query; samples → local states; accumulation → actual reduction; pixel → observable output.

**Preserve:** Retain one trace identity through every panel, even when the representation changes.

1. Pick one representative query and reveal its inputs in context.
2. Carry its intermediate quantities into the actual aggregation.
3. Attach the output and measured residual at the end of the same trace.

**Acceptance test:** Can every stage's output be matched to the next stage's input? Verify the actual reduction, units and weighting.

**Do not copy literally:** A pipeline of named boxes does not show what is being transformed.

**Transfer example (proposal, not a finding):** For transport, trace one inlet packet through local interactions into a measured outlet response.

**Scientific boundary:** This explains image formation and optimization. It does not imply that reconstructed scene geometry is unique.

## Actual images and rights

Source-link-only: open the original figure above. No image is bundled, and no generated substitute is used. A text description does not count as image inspection.

Status: source-link-only. No broadly redistributable figure license verified; the paper and original asset are linked, not bundled.

License: not verified for redistribution. [Permission basis](https://www.matthewtancik.com/nerf).

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.
