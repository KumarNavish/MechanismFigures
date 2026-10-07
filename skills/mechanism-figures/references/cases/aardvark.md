# Aardvark — Make the figure perform the join

D. Lange, Judson-Torres, Zangle & Lex · IEEE VIS / TVCG 2024 · Figure 1

[Publication](https://pmc.ncbi.nlm.nih.gov/articles/PMC12143745/) · [Original image source](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/df01/12143745/4e9f75adbdb2/nihms-2083519-f0001.jpg)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/af521a16-aardvark.jpg) — SHA-256 `68aa01b4f6400d42629784cf8ef55c4af63f6e4330e233df3d5c9dc430e23b8b`. Full Figure 1 from the authors' manuscript deposited in PMC. Presented at VIS 2024; TVCG volume 31(1), January 2025. The conference/journal date distinction is retained.

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** A tree, measurement trace and image all describe the same objects and events.

## See the mechanism

1. In b, the tree provides the structure; the orange trace lives inside each branch's lifetime.
2. The purple cell images are attached to specific points on that trace.
3. Compare c and d: changing the question changes which modality supplies the main layout.

**Mechanism:** Lineage, measured change and microscopy evidence describe the same cells and events but answer different questions.

**Visual construction:** Choose tree, time series or image as the host; nest or overlay matching evidence where the corresponding event occurs.

**What the eye understands:** The reader can connect a change to its ancestry and image evidence without mentally joining separated panels.

**Why an ordinary plot is weaker:** A line alone cannot reveal whether a drop is a biological event or a tracking error. Attached images make that distinction inspectable.

## Learn this visual style, then adapt it

**Observe:** Tree, measurement and image motifs remain identifiable when one becomes the host layout. Repeated colors communicate modality roles; nesting communicates event ownership.

**Apply:** Let the primary scientific question determine the host geometry. Attach evidence at the exact matching event and preserve modality identities; do not scatter related evidence into decorative cards.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Cell identity → event/entity ID; lineage → provenance; attribute trace → measurement; image snippet → primary evidence.

**Keep the relationship:** Use exact identity and time keys to join modalities. A host layout is not proof that all values share the same units.

1. Choose the main question: ancestry, change over time, or movement in space.
2. Let that variable set the layout, then attach the other evidence at the matching event.
3. Show critical transitions by default; reveal secondary detail without moving the host structure.

**Acceptance test:** Can a reader inspect the raw evidence for a suspicious event without searching another panel? Validate every time/entity match.

**Do not copy literally:** Co-location is not enough: a screenshot near a curve must correspond to the same event.

**Scientific boundary:** Figure 1 presents a design grammar, not experimental proof. Different host layouts do not imply that all modalities use one metric coordinate system.

## Attribution and rights

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Approved published figure included for source-specific critical visual study. Original author/publisher rights remain; the repository MIT license does not license this image or grant further republication rights. A broadly reusable image license has not been established.
