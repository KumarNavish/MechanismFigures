# Critique and repair

You must look at the rendered files. Open `figure.png` after each render. Open each detail tile and the grayscale copy after pass C and after the last repair. A critique of the source code is not a critique of the figure.

## The seven questions

Ask them in this sequence. Stop at the first failure, repair it, render and start again from question 1.

| # | Question | Test |
|---|---|---|
| 1 | **Truth** | Each mark has a status and evidence. See [truth.md](truth.md). |
| 2 | **Mechanism** | Hide the labels in your mind. Can you see the operation? Answer the prediction test from the picture alone. |
| 3 | **Entry** | Squint, or look at the grayscale copy for one second. The first thing that you see is the operation. |
| 4 | **Depth** | For each pair of adjacent parts, you know which is in front. No part floats without a reason. Nothing important is hidden. |
| 5 | **Identity** | The persistent object has one colour and one shape rule in all states. Each state uses the same camera. |
| 6 | **Words** | Each label is adjacent to its thing. No label collides. No text is below 6.5 pt. The title is the claim. |
| 7 | **Finish** | Edges align. Gaps are equal. Line weights are consistent. Shadows are soft and light. Nothing touches the frame. |

Questions 1 and 2 are about the science. Do not spend time on question 7 while question 2 fails.

## Compare with the references

Put your render adjacent to the two reference images that you studied. Ask:

- Is the operation as easy to see as in the reference?
- Does my figure have more labels, more colours or more parts than the reference for the same quantity of explanation?
- Which thing does the reference do that my figure does not?

Write one sentence for each answer. Then repair the largest difference.

## Defects and repairs

| You see | Cause | Repair |
|---|---|---|
| The figure is a row of labelled boxes | No construction | Go back to step 4. Draw the object that the first box operates on. |
| Everything has a strong colour | No cast list | Give all context the pale context colour. Give strong colour to two things only. |
| The eye goes to a shadow | Shadow too dark or too large | Lower `shadow` in the view, or set `shadow: false` on that part. |
| Cells or data surfaces have uneven tones | A shadow falls on them | Set `receive: false` on those parts. |
| Low values of a field look grey or dirty | Shading darkens the data colour | Set `unlit: true` on the surface. |
| The figure looks grey | Grey context colours or a custom grey | Use `palette.context` and `palette.quiet`. Do not set a grey. |
| Parts merge into one shape | Same tone, no outline, aligned edges | Change the azimuth by 5 to 10 degrees. Change the tone of one part. Keep the outlines. |
| The operation is hidden inside | No access | Cut the body, or make it a ghost. |
| The cut looks like a missing piece, not a section | Cap has the tone of the skin | Give the cap a darker tone. Align the plane with an axis. |
| An exploded part looks lost | No tether, too far | Reduce the offset. Keep the tether. |
| The fog of many ghosts | More than two transparent layers | Make one layer solid and cut it. |
| States look different for no reason | Camera or frame changed | Build the states in one scene with `S.right`. For beats, set `view.frame`. |
| Label leaders cross | Labels on the wrong side | Put each label on the side of its anchor. Sort labels by height. |
| A label points to nothing | Anchor hidden or in space | Move the anchor to a visible surface point. Read the report. |
| The 3D view gives no numbers | 3D used for a quantity | Add a flat panel for the quantity. Link it with colour. |
| The figure is correct but dull | The operation is small | Give the operation half of the area. Remove context. |
| The figure is busy | Too many parts | Remove each part that does not change the prediction. Show one instance. |
| Small text | The figure holds too much | Remove words. Do not go below 6.5 pt. |
| The surface looks like plastic | Gloss | Set `roughness: 0.8`. Do not add metal. |

## When to change the construction

If two repairs in sequence do not improve question 2, the move is wrong. Typical changes:

- From a pipeline to **one object that goes through the pipeline**.
- From a full system to **one unit and a linked zoom**.
- From an outside view to **a cutaway**.
- From a single state to **a fixed-camera sequence with a counterfactual**.
- From a 3D view that the reader must measure to **a 3D view with a flat partner**.

Keep the rejected version in a folder. Tell the user that you changed the construction and why.

## Stop rule

Stop when the seven questions pass and the side-by-side comparison finds no large difference. Then give the handoff. If you cannot reach this state, give the best version, name the question that fails and say what you need: evidence, real geometry, or a decision from the user. Do not say that a figure is finished when question 1 or 2 fails.
