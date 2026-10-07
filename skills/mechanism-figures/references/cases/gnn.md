# GNNExplainer — Subtract routes without changing the world

Ying et al. · NeurIPS 2019 · Figure 2

[Publication](https://proceedings.neurips.cc/paper_files/paper/2019/hash/d80b7040b773199015de6d3b4293c8ff-Abstract.html) · [Original image source](https://proceedings.neurips.cc/paper_files/paper/2019/file/d80b7040b773199015de6d3b4293c8ff-Paper.pdf)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/4b618381-gnn.png) — SHA-256 `ca1d59b567be2a10e4a6a78196f7816fdc62d6eda205623f6d52d1e46e679067`. Actual Figure 2 rasterized from the NeurIPS proceedings PDF.

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** An explanation selects dependencies or features from a larger relational structure.

## See the mechanism

1. Locate the red target node in both panels.
2. Compare the same neighborhood with and without highlighted message routes.
3. Inspect the crossed-out feature entries: the explanation selects information as well as edges.

**Mechanism:** An explanation selects graph structure and node-feature information relevant to a model's prediction.

**Visual construction:** Repeat the same graph layout. Retain the explanatory routes; hollow out other nodes and mask feature dimensions.

**What the eye understands:** The proposed explanation is a specific pathway through a specific neighborhood—not a list of important variables.

**Why an ordinary plot is weaker:** A feature ranking discards connectivity. Fixed-layout subtraction exposes both relational and feature selection.

## Learn this visual style, then adapt it

**Observe:** The target node and graph positions stay fixed while unselected routes become quiet and feature entries are crossed out.

**Apply:** Use fixed-layout subtraction. Keep the original neighborhood recognizable while selectively revealing which edges and features explain the prediction; never re-layout to make selection look like structural change.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Target node → prediction of interest; edges → allowable dependencies; mask → proposed explanatory subset.

**Keep the relationship:** Fix graph positions and target identity before and after selection. Distinguish selected importance from established causality.

1. Render the original relational structure with its target clearly identified.
2. Repeat that structure without re-layout.
3. Remove or mute the excluded routes and feature entries, retaining enough context to compare.

**Acceptance test:** Can the reader trace the retained pathway? Test prediction fidelity and any causal claim separately.

**Do not copy literally:** Re-layout after filtering makes selection look like structural change.

**Scientific boundary:** This schematic illustrates a learned explanation. Relevance masks are not automatically causal interventions or ground-truth mechanisms.

## Attribution and rights

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Approved published figure included for source-specific critical visual study. Original author/publisher rights remain; the repository MIT license does not license this image or grant further republication rights. A broadly reusable image license has not been established.
