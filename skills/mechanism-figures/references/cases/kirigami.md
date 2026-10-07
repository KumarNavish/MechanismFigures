# Shape-morphing kirigami — Align the geometric input with its deformation

Hong et al. · Nature Communications 2022 · Figure 1a–f

[Publication](https://www.nature.com/articles/s41467-022-28187-x/figures/1) · [Original image source](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41467-022-28187-x/MediaObjects/41467_2022_28187_Fig1_HTML.png)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/fc3c6acf-kirigami.jpg) — SHA-256 `96741301d6c48c2a7960ca4eec72757c3f6d2e05a3880d4054f2e6dcc951eae1`. Publisher Figure 1; panels a–f cropped together. Force–displacement panel excluded from the focused view.
- [full figure](../../assets/calibration/f4bfe551-kirigami.png) — SHA-256 `530129726a7ecb50e65ab33771218081b2c7f0ba891282bf876c826167919cc7`. Full published figure

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** A design parameter changes the qualitative shape of a mechanical response.

## See the mechanism

1. Read each flat cut boundary on the left.
2. Follow its row to the stretched three-dimensional object.
3. Compare outward, straight and inward boundaries with the different curvature types.

**Mechanism:** The cut boundary constrains deformation, guiding a stretched sheet toward different out-of-plane morphologies.

**Visual construction:** Pair flat precursors with their stretched forms; align positive, zero, and negative curvature cases vertically.

**What the eye understands:** The boundary is a design input: outward curvature, straightness, and inward curvature correspond to distinct 3D shapes.

**Why an ordinary plot is weaker:** A force curve measures response. The matched objects show which geometric choice changes the kind of response.

## Learn this visual style, then adapt it

**Observe:** Each flat precursor is aligned with its resulting 3D shape. The boundary geometries themselves—not just numeric parameter labels—organize the alternatives.

**Apply:** Show design geometry and deformation in matched rows with stated loading. Let changing curvature create the visual distinction; do not imply a controlled comparison when the strains differ.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Cut boundary → your design geometry; stretch → loading condition; final surface → response mode.

**Keep the relationship:** Align input and output by specimen. State loading conditions: the published examples do not use identical strain.

1. Show the actual design geometry instead of only naming a parameter.
2. Place its deformation directly beside it under a stated loading condition.
3. Arrange alternatives by the geometric relation whose change explains the response.

**Acceptance test:** Can the reader predict the response type from the geometry? Separate changed geometry from changed loading in validation.

**Do not copy literally:** Do not call unmatched loading conditions a controlled counterfactual.

**Scientific boundary:** The shown strains differ: 0.30, 0.65 and 1.47. These are not same-strain counterfactuals, nor a universal rule for every cut pattern.

## Attribution and rights

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Article Rights and permissions states CC BY 4.0; reviewed figure credit lines contain no separate restriction. Original and focused assets are separately labeled.

[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
