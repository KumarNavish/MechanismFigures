# GNNExplainer: Subtract routes without changing the world

Ying et al. · NeurIPS 2019 · Figure 2

[Publication](https://proceedings.neurips.cc/paper_files/paper/2019/hash/d80b7040b773199015de6d3b4293c8ff-Abstract.html) · [Original asset](https://proceedings.neurips.cc/paper_files/paper/2019/file/d80b7040b773199015de6d3b4293c8ff-Paper.pdf)

**Use when:** An explanation selects dependencies or features from a larger relational structure.

## Look in this order

1. Locate the red target node in both panels.
2. Compare the same neighborhood with and without highlighted message routes.
3. Inspect the crossed-out feature entries: the explanation selects information as well as edges.

## Mechanism → construction → immediate insight

**Mechanism:** An explanation selects graph structure and node-feature information relevant to a model's prediction.

**Construction:** Repeat the same graph layout. Retain the explanatory routes; hollow out other nodes and mask feature dimensions.

**The eye sees:** The proposed explanation is a specific pathway through a specific neighborhood—not a list of important variables.

**Why not an ordinary plot:** A feature ranking discards connectivity. Fixed-layout subtraction exposes both relational and feature selection.

## Recreate the explanatory operation

**Replace the objects:** Target node → prediction of interest; edges → allowable dependencies; mask → proposed explanatory subset.

**Preserve:** Fix graph positions and target identity before and after selection. Distinguish selected importance from established causality.

1. Render the original relational structure with its target clearly identified.
2. Repeat that structure without re-layout.
3. Remove or mute the excluded routes and feature entries, retaining enough context to compare.

**Acceptance test:** Can the reader trace the retained pathway? Test prediction fidelity and any causal claim separately.

**Do not copy literally:** Re-layout after filtering makes selection look like structural change.

**Transfer example (proposal, not a finding):** For a dependency audit, keep a fixed software-call graph and reveal the subset actually exercised by one failure.

**Scientific boundary:** This schematic illustrates a learned explanation. Relevance masks are not automatically causal interventions or ground-truth mechanisms.

## Actual images and rights

Source-link-only: open the original figure above. No image is bundled, and no generated substitute is used. A text description does not count as image inspection.

Status: source-link-only. No broadly redistributable figure license verified; the paper and original asset are linked, not bundled.

License: not verified for redistribution. [Permission basis](https://proceedings.neurips.cc/paper_files/paper/2019/hash/d80b7040b773199015de6d3b4293c8ff-Abstract.html).

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.
