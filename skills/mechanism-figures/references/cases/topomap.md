# TopoMap: Show construction under an invariant

Doraiswamy et al. · IEEE VIS / TVCG 2020 · Figure 4; alternate Figure 2

[Publication](https://virtual.ieeevis.org/year/2020/paper_f-scivis-1049.html) · [Original asset](https://arxiv.org/pdf/2009.01512)

**Use when:** An algorithm transforms a representation while preserving a precisely defined structure.

## Look in this order

1. Track the colored components as complete groups, not independent points.
2. Watch the groups rotate and translate before the next connection.
3. In the related ball-growth view, see that each joining event occurs at a particular distance threshold.

## Mechanism → construction → immediate insight

**Mechanism:** The projection preserves the connected-component merge structure associated with increasing distance thresholds.

**Construction:** Move whole components while controlling the next joining distance. The alternate figure makes thresholds into growing balls.

**The eye sees:** Placement is constrained by the next merge event, not chosen merely to make an appealing cluster map.

**Why not an ordinary plot:** A finished embedding hides what it preserves. Showing its construction makes the invariant inspectable.

## Recreate the explanatory operation

**Replace the objects:** Component → your preserved group; merge event → invariant relation; placement → allowed transformation; gap → constraint.

**Preserve:** Define the invariant narrowly: this example concerns connected-component persistence, not all topology or distances.

1. Show the pre-transformation objects with stable identity.
2. Depict each allowed move and the condition it must preserve.
3. Expose the next critical event so the reader can inspect why the move remains valid.

**Acceptance test:** Can each step be checked against the invariant? Compute the preserved quantity before and after, including edge cases.

**Do not copy literally:** A visually similar endpoint is not proof of invariant preservation.

**Transfer example (proposal, not a finding):** For constrained optimization, show feasible moves and the constraint boundary that prevents an invalid shortcut.

**Scientific boundary:** The guarantee concerns 0-dimensional persistence: connected components. It does not preserve all distances, loops, or higher-dimensional topology.

## Actual images and rights

Source-link-only: open the original figure above. No image is bundled, and no generated substitute is used. A text description does not count as image inspection.

Status: source-link-only. No broadly redistributable figure license verified; the paper and original asset are linked, not bundled.

License: not verified for redistribution. [Permission basis](https://virtual.ieeevis.org/year/2020/paper_f-scivis-1049.html).

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.
