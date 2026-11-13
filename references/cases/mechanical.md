# Mechanical Characters

**Let the mechanism grow inside the same object.**

Coros, Thomaszewski, Noris et al.. *Computational Design of Mechanical Characters*. SIGGRAPH / ACM TOG 2013, Figures 2 and 3. [Publication](https://cdl.ethz.ch/publications/computational-design-of-mechanical-characters/)

**View:** 3D · **Moves:** Target to consequence, Ghost and focus

## Open the image

- [`assets/calibration/mechanical-figure.png`](../../assets/calibration/mechanical-figure.png): focused. Actual published primary figure, rasterized from the author/proceedings PDF with MuPDF 1.26.0. Extraction: {"source": "mechanical.pdf", "page_zero_based": 1, "crop_fraction_top_left": [0.083, 0.067, 0.918, 0.185], "output": "mechanical-fig2.png", "width": 2601, "height": 477, "sha256": "5c374fdc1a4a9daa5e56b8b722308c92559fb5dd18d036ac39db1c4384781e36", "bytes": 1087374, "renderer": "MuPDF 1.26.0; actual published figure rasterization, no redraw"}
- [`assets/calibration/mechanical-context.png`](../../assets/calibration/mechanical-context.png): related. Actual published related figure, rasterized from the author/proceedings PDF with MuPDF 1.26.0. Extraction: {"source": "mechanical.pdf", "page_zero_based": 2, "crop_fraction_top_left": [0.083, 0.063, 0.918, 0.2], "output": "mechanical-fig3.png", "width": 2601, "height": 553, "sha256": "3cf04e6076b4ccfa246e4a3dc5b041c72e9eb16ce60a03450427d6ce9603d1ec", "bytes": 931168, "renderer": "MuPDF 1.26.0; actual published figure rasterization, no redraw"}

Look at the image file. This text does not replace the look.

## Mechanism

A desired cyclic motion is converted into constrained linkages, then connected through a gear train so one actuator drives the character.

## Where to look

1. Follow the same character from a to f; its foot path is the persistent target.
2. In b–d, trace the red motion curve into a linkage, then follow the gears connecting the drives.
3. Compare e with the fabricated object in f; inspect related Figure 3 to see which paths different mechanisms can trace.

## Why it works

The character silhouette and red actuation curve persist while yellow and green gears accumulate. The visual sequence introduces physical complexity without changing the reader’s coordinate frame.

## Take this

Grow the implementing structure around one persistent scientific object; use color to distinguish target behavior from the parts that realize it.

## Test your figure

Can a reader point from one segment of the desired motion to the component that constrains it?

## Do not copy

Do not put decorative gears behind a non-mechanical process or infer accuracy merely because a mechanism can be drawn.

## Limit

The paper targets cyclic motions and a constrained library of assemblies. The overview is not a universal synthesis guarantee; fabrication and fit require separate validation.

## Rights

Actual published figure excerpt included with source-specific critical study. No general redistribution license is asserted by this repository. Original authors/publishers retain rights; inspect the source terms and any third-party image credits before further reuse. Status: `reference-excerpt`.
Selection: curator selection of 2026-10-08.
