# Mechanical Characters — Let the mechanism grow inside the same object.

Coros, Thomaszewski, Noris et al. · SIGGRAPH / ACM TOG 2013 · Figures 2 and 3

[Publication](https://cdl.ethz.ch/publications/computational-design-of-mechanical-characters/) · [Original image source](https://s3-us-west-1.amazonaws.com/disneyresearch/wp-content/uploads/20140804211255/CDMC1.pdf)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/mechanical-figure.png) — SHA-256 `5c374fdc1a4a9daa5e56b8b722308c92559fb5dd18d036ac39db1c4384781e36`. Actual published primary figure, rasterized from the author/proceedings PDF with MuPDF 1.26.0. Extraction: {"source": "mechanical.pdf", "page_zero_based": 1, "crop_fraction_top_left": [0.083, 0.067, 0.918, 0.185], "output": "mechanical-fig2.png", "width": 2601, "height": 477, "sha256": "5c374fdc1a4a9daa5e56b8b722308c92559fb5dd18d036ac39db1c4384781e36", "bytes": 1087374, "renderer": "MuPDF 1.26.0; actual published figure rasterization, no redraw"}
- [related figure](../../assets/calibration/mechanical-context.png) — SHA-256 `3cf04e6076b4ccfa246e4a3dc5b041c72e9eb16ce60a03450427d6ce9603d1ec`. Actual published related figure, rasterized from the author/proceedings PDF with MuPDF 1.26.0. Extraction: {"source": "mechanical.pdf", "page_zero_based": 2, "crop_fraction_top_left": [0.083, 0.063, 0.918, 0.2], "output": "mechanical-fig3.png", "width": 2601, "height": 553, "sha256": "3cf04e6076b4ccfa246e4a3dc5b041c72e9eb16ce60a03450427d6ce9603d1ec", "bytes": 931168, "renderer": "MuPDF 1.26.0; actual published figure rasterization, no redraw"}

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** Replaces a code-dominated aligned diff with a visible behavior-to-structure transformation and a fabricated consequence.

## See the mechanism

1. Follow the same character from a to f; its foot path is the persistent target.
2. In b–d, trace the red motion curve into a linkage, then follow the gears connecting the drives.
3. Compare e with the fabricated object in f; inspect related Figure 3 to see which paths different mechanisms can trace.

**Mechanism:** A desired cyclic motion is converted into constrained linkages, then connected through a gear train so one actuator drives the character.

**Visual construction:** Let the mechanism grow inside the same object.

**What the eye understands:** The sketched path becomes a linkage; the linkage becomes a connected, physically fabricated mechanism.

**Why an ordinary plot is weaker:** A motion-error curve reports fit. Keeping the character and its actuation points in place exposes which physical structures make the movement possible.

## Learn this visual style, then adapt it

**Observe:** The character silhouette and red actuation curve persist while yellow and green gears accumulate. The visual sequence introduces physical complexity without changing the reader’s coordinate frame.

**Apply:** Grow the implementing structure around one persistent scientific object; use color to distinguish target behavior from the parts that realize it.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Replace the character with the project object, its motion curve with the desired behavior, and linkages with the actual constraints or operators that realize it.

**Keep the relationship:** Keep the target object, actuation point, motion phase and intended path identifiable at every step.

1. Show the desired behavior directly on the object rather than in a separate specification box.
2. Add only the parts that implement that behavior; expose their connections in the same coordinates.
3. Finish with the realized object and a matched behavior check, distinguishing rendering from fabrication.

**Acceptance test:** Can a reader point from one segment of the desired motion to the component that constrains it?

**Do not copy literally:** Do not put decorative gears behind a non-mechanical process or infer accuracy merely because a mechanism can be drawn.

**Scientific boundary:** The paper targets cyclic motions and a constrained library of assemblies. The overview is not a universal synthesis guarantee; fabrication and fit require separate validation.

## Attribution and rights

MechanismFigures editorial reading of the cited publication. Replacement selected after the user retired the previous image on 2026-10-08; not an author endorsement or a new empirical result.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Actual published figure excerpt included with source-specific critical study. No general redistribution license is asserted by this repository. Original authors/publishers retain rights; inspect the source terms and any third-party image credits before further reuse.
