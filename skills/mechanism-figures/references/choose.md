# Choose the construction, not the chart

## Diagnose the explanatory gap

Read the equations, experimental intervention, data-generation process, or documented operational rule. Write: **same ___, changed ___, therefore ___ through ___**. For a non-interventional result, replace “therefore” with the defensible relation (“is associated with”, “is inferred from”, “is constrained by”).

Distinguish three questions: **what was observed**, **which mechanism could explain it**, and **what evidence separates that mechanism from alternatives**. The figure may answer one, but must not silently claim all three. If the mechanism is not identified, show the discriminating experiment or competing explanations, not an invented certainty.

Select the narrowest scene in which the essential relationship is visible. A scene can be a physical system, a legitimate state space, one indexed update, an event history, or matched objects. It is not necessarily a 3D illustration.

## Decision table

| Hidden relationship | Required support | Construct this | Calibration | Reject when |
|---|---|---|---|---|
| Extent changes the measurement | Defined support and integration/aggregation | Same center, different footprints; show the field being averaged | mipnerf | Blob size has no unit or definition |
| Local geometry creates global shape | Actual interface, packing or deformation relation | Extract one decisive unit from its assembled context | dna, kirigami | Parts are merely an inventory |
| Algebra is difficult to follow | Established operator and coordinate mapping | Apply the operator to a visible object; align terms with geometry | grokking, alphafold | A circle/triangle is only thematic |
| Information changes representation | Actual input/output correspondence | Carry one traceable query through each representation | nerf, graphcast | Intermediate objects cannot be matched |
| Feedback changes a state | Fixed evaluator, update rule, mutable target | Forward observation and distinct return path to the changed object | dreamfusion | Loop omits the discrepancy or updates the wrong object |
| A scalar conflates direction/history | Joint state variables and valid dynamics | Phase plane; oriented arms; equal-coordinate states with different futures | scvelo | Curve alone is used as evidence of time or a cycle |
| Local transitions produce global outcomes | Transition model; normalized probabilities | One enlarged neighborhood → same system coarse-grained → outcomes | cellrank | Projection distance is substituted for the actual transition rule |
| Outcomes depend on when work occurs | Matched intermediate states and compute | Aligned state sequences plus budget-limited consequence | flow | Cherry-picked or unmatched time/compute columns |
| Identity survives transformation | Correspondence/known symmetry/defined tolerance | Transport a localized probe, or connect changing and invariant spaces | congealing, fip, torus | Shared color substitutes for tested correspondence |
| An intervention removes work or error | Fixed task and explicit precondition | Aligned before/after; leave deletion or repair spatially traceable | alphadev, gaussian, gnn | Layout, target or task changes with the intervention |
| Multiple modalities explain one event | Verified entity/time/provenance joins | Use the main question as the host; attach the other evidence at the event | aardvark, mega | Visually adjacent evidence belongs to different events |
| A construction preserves an invariant | Defined invariant and allowed transformations | Show the operation and the constraint it must preserve at each step | topomap | Attractive layout hides what is actually preserved |

An ordinary plot is not forbidden by its type. A phase portrait can be exactly right. Reject a plot when it only measures an outcome while hiding the mechanism the reader needs. For a pure ranking question, ordinary plotting is the appropriate task; do not force this skill onto it.

## Compare exactly two candidates

For each write four compact fields in `design.candidates`: **construction**, **visible_gain**, **distortion_risk**, **evidence_needed**. They must differ in representation, not just palette or arrangement. A candidate must preserve all claim-critical relations. Choose lexicographically: fidelity first, then exposed mechanism, then decoding burden, then implementation cost. Do not pick a beautiful but unsupported representation.

Visually inspect two related references and one source of likely confusion. Use `python scripts/mf.py references --group dynamics` to locate cases, then `python scripts/mf.py reference cellrank` to retrieve just that case and its image paths. Both chosen references must be actual approved images, opened at readable size, with their registered file paths and hashes recorded. All twenty references now include image files. Use the reference-specific visual-style observations in each case; no self-generated or text-only replacement is acceptable.

## Test before polish

Draw the minimal world with neutral strokes and direct labels. Freeze a question with a correct answer and a counterfactual: “Which part changes?”, “What happens if this input doubles?”, “Which route becomes impossible?” Answer from the intended science, not by looking at the draft. If the picture cannot support that answer, change the encoding before adding color.

Allowed additions must do one of three jobs: establish the mechanism, define an otherwise ambiguous encoding, or bound the claim. Everything else belongs outside the figure. Broad literature review, new experiments, model redesign, and website design are out of scope unless a concrete figure-critical uncertainty requires them.
