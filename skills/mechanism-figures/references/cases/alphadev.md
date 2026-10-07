# AlphaDev: Make the eliminated work visible

Mankowitz et al. · Nature 2023 · Figure 3

[Publication](https://www.nature.com/articles/s41586-023-06004-9) · [Original asset](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41586-023-06004-9/MediaObjects/41586_2023_6004_Fig3_HTML.png)

**Use when:** A local invariant allows an algorithm to omit or simplify an operation.

## Look in this order

1. Locate the circled comparators in a and the ordering established before them.
2. Compare matching lines in b and c; the removed instruction leaves a visible gap.
3. Read the changed expressions: the optimization uses an existing ordering relation, not a different sorting task.

## Mechanism → construction → immediate insight

**Mechanism:** An ordering relation established earlier permits a simplification while retaining the required sorting behavior.

**Construction:** Keep before/after instructions aligned and connect the local sorting-network structure to the changed expressions.

**The eye sees:** The missing line is justified by information the program already has—not by quietly changing the task.

**Why not an ordinary plot:** A speedup bar reports a consequence. The paired structure and code expose the redundancy that permits the saving.

## Recreate the explanatory operation

**Replace the objects:** Comparator → your local operation; ordering invariant → precondition; paired code → before/after implementation; missing line → saved work.

**Preserve:** Hold the input/output contract fixed. Show the precondition that makes the missing work redundant.

1. Draw the local dependency or invariant beside the baseline code.
2. Align the modified code line for line, leaving omissions visible.
3. Connect the changed expression to a correctness check and a separate cost measurement.

**Acceptance test:** Can the reader state why the removed operation is unnecessary? Verify equivalence under the stated precondition, and measure runtime separately.

**Do not copy literally:** Fewer displayed instructions do not automatically establish lower runtime on every machine.

**Transfer example (proposal, not a finding):** For a caching method, align the two execution traces and remove only recomputation whose inputs are demonstrably unchanged.

**Scientific boundary:** The figure explains specific transformations, not a universal optimality or speed claim. Correctness and hardware-dependent cost require separate checks.

## Actual images and rights

- [focused figure](../../assets/calibration/c243c8d0-alphadev.png) — Publisher-hosted Figure 3, replacing the supplied guide's third-party blog image URL. The scientific figure is the same; this source replacement is explicit.

Status: bundled. Article Rights and permissions states CC BY 4.0; reviewed figure credit lines contain no separate restriction. Original and focused assets are separately labeled.

License: CC-BY-4.0. [Permission basis](https://www.nature.com/articles/s41586-023-06004-9).

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.
