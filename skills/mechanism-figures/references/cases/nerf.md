# NeRF — Keep one trace through every representation

Mildenhall et al. · ECCV 2020 · Figure 2

[Publication](https://www.matthewtancik.com/nerf) · [Original image source](https://arxiv.org/pdf/2003.08934)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/14900912-nerf.png) — SHA-256 `e5e5b4b304623b24eb3da07837a767a639c67291b650b045216ebee7c03215b9`. Actual Figure 2 rasterized from the authors' arXiv manuscript.

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** A physical or computational signal passes through several representations before producing an observation.

## See the mechanism

1. Choose one camera ray in a.
2. Follow its sampled locations into color and density in b, then the depth profile in c.
3. Find the corresponding pixel comparison in d: the chain ends in an observable residual.

**Mechanism:** A learned field supplies density and view-dependent color; volume rendering accumulates these along camera rays.

**Visual construction:** Carry identifiable rays from a 3D scene into depth profiles and finally into pixel-color comparisons.

**What the eye understands:** A pixel is an accumulation through space—not a color emitted by an unexplained network box.

**Why an ordinary plot is weaker:** A pipeline names the stages. Following the ray exposes the physical meaning of the intermediate quantities.

## Learn this visual style, then adapt it

**Observe:** The same rays connect a physical scene to sampled density/color, depth profiles and a pixel residual. Small labels describe the quantity at each transformation.

**Apply:** Carry one traceable query through the representation changes. Place intermediate values and the observable consequence along its route, rather than separating a pipeline from its physical meaning.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Ray → your traceable query; samples → local states; accumulation → actual reduction; pixel → observable output.

**Keep the relationship:** Retain one trace identity through every panel, even when the representation changes.

1. Pick one representative query and reveal its inputs in context.
2. Carry its intermediate quantities into the actual aggregation.
3. Attach the output and measured residual at the end of the same trace.

**Acceptance test:** Can every stage's output be matched to the next stage's input? Verify the actual reduction, units and weighting.

**Do not copy literally:** A pipeline of named boxes does not show what is being transformed.

**Scientific boundary:** This explains image formation and optimization. It does not imply that reconstructed scene geometry is unique.

## Attribution and rights

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Approved published figure included for source-specific critical visual study. Original author/publisher rights remain; the repository MIT license does not license this image or grant further republication rights. A broadly reusable image license has not been established.
