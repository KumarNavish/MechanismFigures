# Truth

A clear figure that is false is worse than no figure. Apply these checks before you build and again before the handoff.

## Status of each mark

Each object, field and arrow in the figure has one status. Decide it in step 2 of the loop.

| Status | Meaning | How to show it |
|---|---|---|
| **Measured** | From an experiment or an observation | Solid. Give a scale bar or units. Do not smooth or recolour. |
| **Simulated** | From a model run | Solid. Name the model in the caption. |
| **Derived** | From an equation or an exact construction | Solid. Geometry computed in the source file, not drawn by eye. |
| **Schematic** | An illustration of an idea, not to scale | Simpler shapes, and the word "schematic" in the caption or on the panel. |
| **Hypothesis** | Not established | Dashed lines, a question mark, or a lighter tone. |

Do not mix statuses in one style. A reader must be able to tell a measured surface from a drawn one.

## What a picture must not imply

- **Cause from sequence.** An arrow from A to B says that A produces B. If the evidence is a correlation, draw the two things adjacent, with no arrow.
- **History from a snapshot.** Do not draw a trajectory through points that were measured at one time, unless a model infers it. Then the status is "simulated" or "hypothesis".
- **Topology from a projection.** A 2D or 3D embedding of high-dimensional data distorts distances and neighbours. Do not let the reader measure in it. Say what the embedding keeps.
- **The typical from the selected.** If the example is the best case, say so. Prefer a median case.
- **Speed or cost from the number of drawn steps.** Three boxes are not three operations of equal cost.
- **Precision from smoothness.** A smooth rendered surface looks exact. If the data is coarse, show the samples.

## Risks that are special to 3D

- **Foreshortening.** Lengths along the view direction look short. Do not ask the reader to compare lengths in different directions. Use an orthographic camera, and put quantities in a flat panel.
- **Shading changes colour.** Light makes one data value look like many. For a field that the reader must read exactly, add the flat map.
- **Occlusion hides data.** If the hidden side matters, cut the object, make the front a ghost, or show a second view.
- **Invented geometry.** Do not give an abstract thing a detailed physical shape that suggests knowledge that you do not have. A loss landscape drawn by hand is a schematic.
- **Exaggeration.** Write each scale factor on the figure.
- **Perspective.** It changes relative sizes. Use it only for a scene that a camera sees.

## Comparisons

- Use the same camera, scale, light, colour ramp and sampling for all states.
- Change one thing. Say what stayed fixed.
- Use the strongest fair baseline.
- A colour ramp has the same range in each panel that the reader compares.

## Before the handoff

1. Read the mechanism sentence. Does the project evidence support it? If it supports only a part, draw only that part.
2. For each arrow: what is the source, what is the target, what is the relation, and what is the evidence?
3. For each number or scale: where does it come from?
4. Could an expert in the field look at the geometry and say "it does not look like that"? If yes, get the real geometry or simplify until the shape makes no claim.
5. Does the caption state the status of the content and each exaggeration?

If the evidence is not sufficient for a mechanism figure, say so. Offer a figure that shows the competing explanations, or the observation alone. Do not invent a mechanism to complete the task.
