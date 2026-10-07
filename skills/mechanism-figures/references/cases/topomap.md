# TopoMap — Show construction under an invariant

Doraiswamy et al. · IEEE VIS / TVCG 2020 · Figure 4; alternate Figure 2

[Publication](https://virtual.ieeevis.org/year/2020/paper_f-scivis-1049.html) · [Original image source](https://arxiv.org/pdf/2009.01512)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/627981ba-topomap.png) — SHA-256 `d847c7821776b04fc47f34e9337a3437f2e095cf169e3e4e4fcbecb54be2c410`. Actual figures from the authors' arXiv manuscript. Presented at VIS 2020; TVCG journal issue 2021.
- [related figure](../../assets/calibration/9b9fbfab-topomap-balls.png) — SHA-256 `5d47814af89651a5f2008afad235ee56ee10f684d476296c9ecfe4cd49c31488`. Figure 2 · growth and merge events

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** An algorithm transforms a representation while preserving a precisely defined structure.

## See the mechanism

1. Track the colored components as complete groups, not independent points.
2. Watch the groups rotate and translate before the next connection.
3. In the related ball-growth view, see that each joining event occurs at a particular distance threshold.

**Mechanism:** The projection preserves the connected-component merge structure associated with increasing distance thresholds.

**Visual construction:** Move whole components while controlling the next joining distance. The alternate figure makes thresholds into growing balls.

**What the eye understands:** Placement is constrained by the next merge event, not chosen merely to make an appealing cluster map.

**Why an ordinary plot is weaker:** A finished embedding hides what it preserves. Showing its construction makes the invariant inspectable.

## Learn this visual style, then adapt it

**Observe:** The same components and point identities remain visible while they move, rotate and merge at controlled distances.

**Apply:** Show the permitted transformations and the specific invariant they preserve. Keep identities consistent through steps and make the next merge event visibly determine placement.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Component → your preserved group; merge event → invariant relation; placement → allowed transformation; gap → constraint.

**Keep the relationship:** Define the invariant narrowly: this example concerns connected-component persistence, not all topology or distances.

1. Show the pre-transformation objects with stable identity.
2. Depict each allowed move and the condition it must preserve.
3. Expose the next critical event so the reader can inspect why the move remains valid.

**Acceptance test:** Can each step be checked against the invariant? Compute the preserved quantity before and after, including edge cases.

**Do not copy literally:** A visually similar endpoint is not proof of invariant preservation.

**Scientific boundary:** The guarantee concerns 0-dimensional persistence: connected components. It does not preserve all distances, loops, or higher-dimensional topology.

## Attribution and rights

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Approved published figure included for source-specific critical visual study. Original author/publisher rights remain; the repository MIT license does not license this image or grant further republication rights. A broadly reusable image license has not been established.
