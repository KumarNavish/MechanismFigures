# From encoding to composition

## Make the encoding contract explicit

For each meaningful mark record `scientific`, `visual`, `units`, `status`, and `evidence_ids`. For example: transition probability → edge width under a stated linear mapping → dimensionless → inferred → E2. A narrative arrow with no quantitative width uses a fixed stroke. Never let incidental area, perspective, opacity, or distance imply a quantity unintentionally.

Choose one persistent object to carry the reading. Its identifier must survive each change of representation. A matrix cell can become an edge, then a local geometric operation; the same indices must appear in all three. In a controlled contrast, reuse the exact object coordinates, camera, scale, and sampling choices; only the intervention changes. Freeze these layout coordinates in code rather than independently optimizing each panel.

## Plan the reading path

Write three ordered eye actions, each using an observable verb: **find, follow, compare, align, cross, separate, rotate, expand**. Avoid “understand” as an action. The first action locates the scientific object; the second performs the decisive operation; the third sees its consequence. Put labels where each action occurs, not in a distant legend.

Use one main explanatory region. Add an inset only if a local-to-global link or a scale change is essential. Distinguish a schematic enlargement from a different measured scale. A second panel must answer a different necessary question: typically counterfactual, observable consequence, or validity limit. Panels that repeat the prose without exposing another relation are removed.

## Specific layout operations

- **Shared substrate:** draw one physical domain or reference coordinate system repeatedly; link actual corresponding landmarks, not whole panels with generic arrows.
- **Exploded unit:** pull a component only far enough to expose its interface; retain a tether or ghost position showing where it belongs.
- **Matched contrast:** anchor identical structures at identical coordinates. Align operations; preserve blank space left by deleted work.
- **Dynamics:** share time samples and scales. Attach arrowheads to known time direction. A density movie is not a set of tracked-particle paths.
- **Invariant:** show both where variation is allowed and where it is constrained. State the preserved observable and tolerance.
- **Evidence join:** attach source snippets to the exact entity and event; compare equal units only. Use separate local axes when modalities differ.

## Typography, whitespace and annotation have jobs

Set physical dimensions before drawing. Defaults for an unconstrained 180 mm-wide figure are 8–9 pt primary labels, ≥7 pt secondary labels, and 10–12 pt panel headings. These are editable project defaults, not universal journal rules. The true size is `font_size_in_viewBox_units × width_mm / viewBox_width × 72 / 25.4`; shrinking the final figure shrinks its text. Do not solve overflow by lowering the minimum text size.

Use one text family with mathematical symbols rendered consistently. Direct labels belong beside the relevant mark; a leader is added only when it resolves a genuine collision. Keep leaders out of the mechanism's movement paths. Use explanation annotations to name the **change** (“same center, larger support”), not to repeat the section title (“our method”).

Reserve whitespace around the decisive interaction so incident edges, contact surfaces, or the intervention can be distinguished. Start with one label-line height between unrelated text and roughly two between distinct reasoning steps; tighten only after final-size inspection. Whitespace is not a license for a huge title that pushes the scientific object away.

A small working hierarchy is usually enough: high-contrast active objects, quieter unchanged context, and restrained annotation. Test by hiding the title: the mechanism region should still be the obvious entry point. If an empty decorative frame becomes the most salient element, delete it.

## Color is a semantic mapping

Start with neutral context plus one focal color; add a second only for an intervention, opposing regime, or independent quantity. A multivariate scientific encoding may need more colors; record each mapping instead of applying an arbitrary color-count cap. Preserve categorical identities between panels. Signed values need a visible zero/reference; magnitude requires a defined scale. Continuous maps must be consistent across comparisons.

Redundant non-color signals carry essential distinctions: solid/dashed for evidence status, outline/fill for control/intervention, direct labels for identities. Grayscale checks detect lost distinctions; a color-blind simulation may supplement but does not replace them. Never recolor or enhance experimental imagery selectively to strengthen a claim.

## Implement with the project's best deterministic tool

Use SVG/TikZ/vector primitives for exact geometry and relations; plotting code for data-dependent geometry; a proper renderer for physical scenes. The skill does not mandate a library. SciencePlots can style an accompanying quantitative panel; it cannot choose the explanatory construction.

Keep data processing separate from layout. Seed random choices, retain data filters, freeze transformations and normalizations, record renderer versions, and use portable paths. Include editable labels plus a rendered preview, not just a flattened screenshot. No synthetic visual substitutes for missing measurements. Generative tools may explore illustration only when authorized and clearly non-evidential; numerical geometry and reported evidence must remain data- or equation-driven.

Generate vector, actual-size PNG preview, caption, source, and reproducible local evidence. Inspect the vector in its intended export path and its raster preview, because font fallback and clipping can differ. For PDF output use the host's PDF workflow and verify the resulting PDF, not an assumed conversion. Never distribute font binaries without permission.
