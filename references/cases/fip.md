# Functionally invariant paths — Separate the space that changes from the space that stays fixed

Raghavan et al. · Nature Machine Intelligence 2024 · Figure 1a

[Publication](https://www.nature.com/articles/s42256-024-00902-x) · [Original image source](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs42256-024-00902-x/MediaObjects/42256_2024_902_Fig1_HTML.png)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/c1bbd0b1-fip.png) — SHA-256 `8cf5139aa2fb353d9d12aa0493aa5f2eacb6b6a5a997e5e1d145a18dfd41d313`. Publisher Figure 1, panel a cropped. Full figure available in the viewer.
- [full figure](../../assets/calibration/58b095f5-fip.png) — SHA-256 `e6279162f5dc5eb6e1b8f5545f60b6921e8a941ef8abda554a3860d21d74ea79`. Full published figure

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** Large internal changes can preserve a specified external behavior.

## See the mechanism

1. Find the different parameter points on the weight-space surface.
2. Follow their relationship to the compact group in output space.
3. Notice the contrast: internal movement and task-output movement have different magnitudes.

**Mechanism:** Parameters may change substantially while task behavior is approximately preserved, allowing other properties to be adjusted.

**Visual construction:** Separate weight space from output space. Show an extended set in one mapping to a compact set in the other.

**What the eye understands:** Movement in parameters need not mean comparable movement in behavior.

**Why an ordinary plot is weaker:** An accuracy curve reports preservation. The paired spaces explain which freedom preservation can leave available.

## Learn this visual style, then adapt it

**Observe:** An extended set of weight-space states maps to a compact task-output set. The two spaces are kept distinct so internal change and output preservation can be compared.

**Apply:** Give changing and preserved quantities their own explicitly labeled spaces. Connect corresponding states and show a defined tolerance; do not mistake a conceptual surface for measured manifold geometry.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Weights → your internal state; surface → feasible behavior-preserving set; output cluster → the specified invariance criterion.

**Keep the relationship:** Define the preserved behavior and tolerance. Do not present conceptual surface geometry as measured structure.

1. Draw the changing representation and the preserved representation in separate aligned spaces.
2. Connect corresponding states between the spaces.
3. Show the size of allowed output change using actual measurements where available.

**Acceptance test:** Is preservation verified on the intended inputs, not just one illustrated example? Label approximate versus exact invariance.

**Do not copy literally:** Equal task accuracy is not identical function behavior on every input.

**Scientific boundary:** The surface is schematic, not a measured 3D manifold or proof of exact global functional invariance.

## Attribution and rights

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Approved published figure included for source-specific critical visual study. Original author/publisher rights remain; the repository MIT license does not license this image or grant further republication rights. Publisher permits noncommercial unadapted redistribution; the original license remains applicable; check source-specific permissions for further use.

[CC-BY-NC-ND-4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
