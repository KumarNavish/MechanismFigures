# AlphaFold / triangle updates: Unfold indices into relationships

Jumper et al. · Nature 2021 · Figure 3b–c

[Publication](https://www.nature.com/articles/s41586-021-03819-2/figures/3) · [Original asset](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41586-021-03819-2/MediaObjects/41586_2021_3819_Fig3_HTML.png)

**Use when:** Tensor indices, pairwise constraints or higher-order interactions hide which entities exchange information.

## Look in this order

1. In panel b, match selected matrix entries to edges between residues i, j and k.
2. In panel c, follow the blue edges through the third residue.
3. In the full figure, relate these local updates to the structure module and its explicit residue frames.

## Mechanism → construction → immediate insight

**Mechanism:** Updating a residue-pair representation incorporates information involving a third residue.

**Construction:** Unfold indexed tensor entries into a graph triangle; keep edge orientation visible across update variants.

**The eye sees:** The i–j relation can be informed by relations passing through k. Index notation becomes a route.

**Why not an ordinary plot:** A matrix or module diagram hides the three-way dependency. The triangle lets the reader trace it.

## Recreate the explanatory operation

**Replace the objects:** Residues → your entities; pair entries → relational state; triangle routes → the actual dependencies in the update equation.

**Preserve:** Use the same entity labels and edge orientation in the equation, matrix and geometric view.

1. Select one output relation and the smallest set of inputs needed to update it.
2. Expand its indices into entities arranged so each dependency is traceable.
3. Place the algebra next to those same routes; emphasize only the active terms.

**Acceptance test:** Can every highlighted edge be matched to a term in the update? Do not imply physical transport or causation when it is only computation.

**Do not copy literally:** Do not draw triangles merely because the method contains three modules.

**Transfer example (proposal, not a finding):** For a Gram-matrix update, draw the vectors and the inner products that actually determine one entry; do not draw arbitrary networking arrows.

**Scientific boundary:** These arrows describe computation, not experimental causal evidence or a guarantee that every geometric constraint is satisfied.

## Actual images and rights

- [focused figure](../../assets/calibration/94866d7c-alphafold.png) — Publisher Figure 3; panels b–c cropped together. Full figure available in the viewer.
- [full figure](../../assets/calibration/82942714-alphafold.png) — Full published figure

Status: bundled. Article Rights and permissions states CC BY 4.0; reviewed figure credit lines contain no separate restriction. Original and focused assets are separately labeled.

License: CC-BY-4.0. [Permission basis](https://www.nature.com/articles/s41586-021-03819-2).

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.
