# AlphaDev — Make the eliminated work visible

Mankowitz et al. · Nature 2023 · Figure 3

[Publication](https://www.nature.com/articles/s41586-023-06004-9) · [Original image source](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41586-023-06004-9/MediaObjects/41586_2023_6004_Fig3_HTML.png)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/c243c8d0-alphadev.png) — SHA-256 `90a4613920c0676036626105b11f2803f3dd8ee390145e9a7e2fdac76194de3f`. Publisher-hosted Figure 3, replacing the supplied guide's third-party blog image URL. The scientific figure is the same; this source replacement is explicit.

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** A local invariant allows an algorithm to omit or simplify an operation.

## See the mechanism

1. Locate the circled comparators in a and the ordering established before them.
2. Compare matching lines in b and c; the removed instruction leaves a visible gap.
3. Read the changed expressions: the optimization uses an existing ordering relation, not a different sorting task.

**Mechanism:** An ordering relation established earlier permits a simplification while retaining the required sorting behavior.

**Visual construction:** Keep before/after instructions aligned and connect the local sorting-network structure to the changed expressions.

**What the eye understands:** The missing line is justified by information the program already has—not by quietly changing the task.

**Why an ordinary plot is weaker:** A speedup bar reports a consequence. The paired structure and code expose the redundancy that permits the saving.

## Learn this visual style, then adapt it

**Observe:** Before/after code is line-aligned beside the comparator structure. Deleted instructions leave visible gaps; only the altered expressions receive emphasis.

**Apply:** Use matched structure and implementation views. Preserve positions, expose the precondition beside the removed work, and highlight only the actual change—not the entire proposed method.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Comparator → your local operation; ordering invariant → precondition; paired code → before/after implementation; missing line → saved work.

**Keep the relationship:** Hold the input/output contract fixed. Show the precondition that makes the missing work redundant.

1. Draw the local dependency or invariant beside the baseline code.
2. Align the modified code line for line, leaving omissions visible.
3. Connect the changed expression to a correctness check and a separate cost measurement.

**Acceptance test:** Can the reader state why the removed operation is unnecessary? Verify equivalence under the stated precondition, and measure runtime separately.

**Do not copy literally:** Fewer displayed instructions do not automatically establish lower runtime on every machine.

**Scientific boundary:** The figure explains specific transformations, not a universal optimality or speed claim. Correctness and hardware-dependent cost require separate checks.

## Attribution and rights

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Article Rights and permissions states CC BY 4.0; reviewed figure credit lines contain no separate restriction. Original and focused assets are separately labeled.

[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
