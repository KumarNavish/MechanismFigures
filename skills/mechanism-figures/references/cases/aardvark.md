# Aardvark: Make the figure perform the join

D. Lange, Judson-Torres, Zangle & Lex · IEEE VIS / TVCG 2024 · Figure 1

[Publication](https://pmc.ncbi.nlm.nih.gov/articles/PMC12143745/) · [Original asset](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/df01/12143745/4e9f75adbdb2/nihms-2083519-f0001.jpg)

**Use when:** A tree, measurement trace and image all describe the same objects and events.

## Look in this order

1. In b, the tree provides the structure; the orange trace lives inside each branch's lifetime.
2. The purple cell images are attached to specific points on that trace.
3. Compare c and d: changing the question changes which modality supplies the main layout.

## Mechanism → construction → immediate insight

**Mechanism:** Lineage, measured change and microscopy evidence describe the same cells and events but answer different questions.

**Construction:** Choose tree, time series or image as the host; nest or overlay matching evidence where the corresponding event occurs.

**The eye sees:** The reader can connect a change to its ancestry and image evidence without mentally joining separated panels.

**Why not an ordinary plot:** A line alone cannot reveal whether a drop is a biological event or a tracking error. Attached images make that distinction inspectable.

## Recreate the explanatory operation

**Replace the objects:** Cell identity → event/entity ID; lineage → provenance; attribute trace → measurement; image snippet → primary evidence.

**Preserve:** Use exact identity and time keys to join modalities. A host layout is not proof that all values share the same units.

1. Choose the main question: ancestry, change over time, or movement in space.
2. Let that variable set the layout, then attach the other evidence at the matching event.
3. Show critical transitions by default; reveal secondary detail without moving the host structure.

**Acceptance test:** Can a reader inspect the raw evidence for a suspicious event without searching another panel? Validate every time/entity match.

**Do not copy literally:** Co-location is not enough: a screenshot near a curve must correspond to the same event.

**Transfer example (proposal, not a finding):** For an agent experiment, nest performance traces and the exact tool-output snapshot inside the corresponding branch of the execution history.

**Scientific boundary:** Figure 1 presents a design grammar, not experimental proof. Different host layouts do not imply that all modalities use one metric coordinate system.

## Actual images and rights

Source-link-only: open the original figure above. No image is bundled, and no generated substitute is used. A text description does not count as image inspection.

Status: source-link-only. No broadly redistributable figure license verified; the paper and original asset are linked, not bundled.

License: not verified for redistribution. [Permission basis](https://pmc.ncbi.nlm.nih.gov/articles/PMC12143745/).

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.
