# AlphaFold / triangle updates — Unfold indices into relationships

Jumper et al. · Nature 2021 · Figure 3

[Publication](https://www.nature.com/articles/s41586-021-03819-2/figures/3) · [Original image source](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41586-021-03819-2/MediaObjects/41586_2021_3819_Fig3_HTML.png)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/94866d7c-alphafold.png) — SHA-256 `96abc1ce03ee69229283a7ba38769ec011912bd2e644d1ba39624f02c77b1e91`. Publisher Figure 3; panels b–c cropped together. Full figure available in the viewer.
- [full figure](../../assets/calibration/82942714-alphafold.png) — SHA-256 `cc3898ec047291dcfeadaea447fdba928d74174f972b6a75074ffcf8c56bd4fc`. Full published figure

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** Tensor indices, pairwise constraints or higher-order interactions hide which entities exchange information.

## See the mechanism

1. In panel b, match selected matrix entries to edges between residues i, j and k.
2. In panel c, follow the blue edges through the third residue.
3. In the full figure, relate these local updates to the structure module and its explicit residue frames.

**Mechanism:** Updating a residue-pair representation incorporates information involving a third residue.

**Visual construction:** Unfold indexed tensor entries into a graph triangle; keep edge orientation visible across update variants.

**What the eye understands:** The i–j relation can be informed by relations passing through k. Index notation becomes a route.

**Why an ordinary plot is weaker:** A matrix or module diagram hides the three-way dependency. The triangle lets the reader trace it.

## Learn this visual style, then adapt it

**Observe:** The same indices label matrix cells, graph edges and triangle operations. The surrounding architecture stays quieter than the selected local update.

**Apply:** Use an aligned overview-plus-mechanism composition. Let geometry carry the index relationship; repeat identifiers and selectively emphasize the active edges rather than coloring every module.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Residues → your entities; pair entries → relational state; triangle routes → the actual dependencies in the update equation.

**Keep the relationship:** Use the same entity labels and edge orientation in the equation, matrix and geometric view.

1. Select one output relation and the smallest set of inputs needed to update it.
2. Expand its indices into entities arranged so each dependency is traceable.
3. Place the algebra next to those same routes; emphasize only the active terms.

**Acceptance test:** Can every highlighted edge be matched to a term in the update? Do not imply physical transport or causation when it is only computation.

**Do not copy literally:** Do not draw triangles merely because the method contains three modules.

**Scientific boundary:** These arrows describe computation, not experimental causal evidence or a guarantee that every geometric constraint is satisfied.

## Attribution and rights

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Article Rights and permissions states CC BY 4.0; reviewed figure credit lines contain no separate restriction. Original and focused assets are separately labeled.

[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
