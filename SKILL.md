---
name: mechanism-figures
description: Use when a figure must show HOW something works. Applies to scientific and technical mechanism figures, paper figure 1, method and architecture figures, 3D schematics, cutaways, exploded views, anatomy of a device, molecule, model or algorithm, and to the repair of a figure that looks like boxes and arrows. Strong bias for rendered 3D. Gives a reference atlas of real published figures, a 3D stage with a renderer, and a look-critique-repair loop. Not for routine chart styling.
license: MIT for code and text. Third-party reference figures keep the licences recorded in THIRD_PARTY.md.
compatibility: The agent must be able to view images. The 3D stage needs Node 22 or later and an installed Chrome or Chromium. Reference lookup needs Python 3.9 or later. No network, model service or GPU is necessary.
metadata:
  author: Navish Kumar
  version: "1.0.1"
---

# MechanismFigures

**A mechanism figure passes one test: a reader who sees only the picture can predict what the system does next.**

A list of parts fails this test. A pipeline of boxes fails this test. A plot of the result fails this test. The picture must show an object, the operation on that object, and the consequence.

This skill gives you three tools:

1. **An atlas** of real published figures that pass the test. You look at them before you draw.
2. **Fifteen visual moves** that make an operation visible. Most of them are three-dimensional.
3. **A 3D stage** that renders your figure, and a loop in which you look at the render and repair it.

## Think in 3D first

Most mechanisms occur in space. Parts enclose other parts. Layers lie on layers. Rays cross volumes. Surfaces fold. A flat diagram deletes these relations and puts arrows in their place. Thus your first proposal must be a 3D construction. Go to a flat construction only when a test below tells you to.

| Use 3D when | Stay flat when |
|---|---|
| The operation occurs inside something. Use a cutaway. | The claim is an exact quantity that the reader must read from an axis. |
| Parts touch, stack, nest or interlock. Use an exploded view or a layer stack. | The structure is a sequence or a graph with no spatial meaning. |
| Something moves, folds, rotates or flows through space. | Depth has no variable and no spatial relation to carry. |
| A quantity lives on a surface or in a volume. | A fair comparison needs equal lengths, and foreshortening can change them. |
| The data has three state variables, or a manifold has a shape. | |
| An abstract object becomes clear as a physical object: a tensor as a block, a landscape as a surface. | |

3D must carry meaning. Each axis has a name or a spatial sense. Do not make 3D bars, 3D pies or bevelled boxes. If the reader must read a number, put a flat panel adjacent to the 3D view and link the two with a shared object.

## The loop

Do the six steps in sequence. Do not start with step 5.

### 1. Write the mechanism sentence

> The reader must see that **[consequence]** occurs because **[operation]** acts on **[object]**.

Then write the prediction test: "If I remove or change **X**, the reader can tell from the picture that **Y** changes." If you cannot write these two sentences from the project material, find the mechanism first. Read the code, the equations and the data. Do not draw a topic.

### 2. Name the cast

Write three lists.

- **The persistent object.** One thing that the eye follows through the full figure: a ray, a residue pair, a cell, a sheet, a weight vector. It keeps its colour and its identity in each panel.
- **The operation.** The one event that carries the explanation. It gets the strongest colour and the most space.
- **The context.** All other items. They are pale, thin and quiet. Use the pale cool context colour of the palette. Do not use grey.

For each item, record its status: **measured**, **simulated**, **derived from an equation**, or **schematic**. You will show this status in the figure. See [truth.md](references/truth.md).

### 3. Look at real figures

Run `python3 scripts/refs.py <words>` with words from your mechanism, for example `refs.py cutaway rotation` or `refs.py layers field`. The command prints the best matches and the absolute paths of their images. A move name such as `cutaway` or `rays` matches best. With no words it prints the full atlas. [atlas.md](references/atlas.md) has the same data in a table.

**Open two or more of the image files and look at them.** A filename or a caption is not a look. For each image, write down four facts:

- the move: how the operation becomes visible,
- the camera: its angle, and what faces the viewer,
- the depth cues: what makes near and far clear,
- the labels: where they are, how many, and what they name.

Each reference has a case file in `references/cases/` that tells you where to look and what to take. Take the move. Do not copy the domain objects.

### 4. Choose the move

Select from the table. Then describe two different constructions in one sentence each. Select the one that tells the truth with the least decoding. A different palette is not a different construction.

| The reader must see | Move | Study |
|---|---|---|
| An operation inside a body | **Cutaway** with a capped section | `kent-hopfion`, `t3ss-needle`, `tokamak` |
| How parts join or stack | **Exploded view** with tethers; **layer stack** | `photonic-braids`, `alphatensor`, `kplanes` |
| One part in action in a large assembly | **Ghost and focus** | `loterie-vam`, `frenzel-chiral`, `birch-skyrmion` |
| A change of state or shape | **Fixed-camera sequence** | `kennaway-growth`, `christoffersen-lake`, `myosin-stroke` |
| The logic of a curved surface | **Unroll pair**: the surface and its flat map | `weiler-gauge`, `torus` |
| Sampling, projection or transport through a volume | **Ray trace** | `plenoxels`, `nerf`, `wolf-tomography` |
| A quantity on a surface or in a volume | **Field on geometry** | `zheng-hopfion`, `kent-hopfion`, `graphcast` |
| A local rule that gives a global result | **Linked zoom**: unit cell to lattice | `plenoxels`, `frenzel-chiral`, `flagellar-stator` |
| Dynamics, optimisation or invariance | **State-space geometry** | `safaie-dynamics`, `cohen-untangling`, `torus` |
| What an index or tensor refers to | **Index to geometry** | `alphatensor`, `hulse-compass`, `alphafold` |
| An inverse design | **Target, program, structure, consequence** | `caustics`, `bioprint4d`, `mechanical` |
| The effect of one intervention | **Matched counterfactual** | `flagellar-stator`, `weiler-gauge`, `kent-hopfion` |
| A feedback or training cycle | **Loop through one object** | `cohesin-ratchet`, `dreamfusion` |
| A process in a landscape or a medium | **Block diagram** with a cut front face | `azores-dike`, `christoffersen-lake` |

[moves.md](references/moves.md) gives the construction, the stage calls and the failure modes for each move. The atlas lists more references for each move. Read the entry for your move before you build.

### 5. Build in three passes

Use the stage unless the project has a better renderer for its own data. Read [stage.md](references/stage.md) once. If the host has no Node or Chrome, stage.md gives the artifact route.

```js
// figure.mjs
export const view = {width: 180, height: 100, azim: -50, elev: 28};   // millimetres and degrees
export default function build(S, THREE) {
  const P = S.palette;
  const shell = S.solid(new THREE.SphereGeometry(1, 64, 40), {color: P.context, id: 'shell'});
  S.sphere([0, 0, 0], 0.45, {color: P.act, id: 'core'});
  S.cut(shell, [0, 0, 0], [0.2, -1, 0.15]);            // remove the near side and cap the section
  S.label([0, 0, 0.45], 'core', {dx: 5, dy: -14});
}
```

```bash
node scripts/render.mjs figure.mjs --out out
```

The renderer writes `figure.png`, `figure.svg` with editable labels, four detail tiles, a grayscale copy and a report.

- **Pass A, blockout.** Primitives in the one pale context colour only. No strong colour, no labels. Set the camera. Render and look. The operation must be visible from shape alone. If it is not, change the construction or the camera. Do not continue.
- **Pass B, meaning.** Give the persistent object and the operation their colours. Add ghosts, cuts, tethers, arrows and fields. Render and look.
- **Pass C, words.** Add labels, panel letters and the minimum text. Render and look.

[craft.md](references/craft.md) has the rules for the camera, depth cues, light, colour, labels and composition. Read it before pass A.

### 6. Look, find the defect, repair

After each render, **open the PNG.** After pass C and after your last repair, open each detail tile and the grayscale copy also. The report finds hidden label anchors, small text and text collisions only. It cannot see.

Ask these questions in sequence. Repair the first one that fails, then render again.

1. **Truth.** Does the picture show something that is false or that has no evidence?
2. **Mechanism.** Cover the labels. Is the operation visible? Can you answer the prediction test?
3. **Entry.** Squint. Does the eye go first to the operation? If it goes to a frame, a title or a shadow, repair the hierarchy.
4. **Depth.** Is each near-far relation clear? Does a part float? Does a hidden part matter?
5. **Identity.** Does the persistent object keep its colour, shape and position rule in each state?
6. **Words.** Does each label name a visible thing at the place of that thing? Is each text 6.5 pt or larger at print size?
7. **Finish.** Alignment, spacing, line weights, collisions.

[critique.md](references/critique.md) gives the full checklist and a table of defects with their repairs.

Stop when all seven questions pass and the figure is as clear as the references that you opened. Compare them side by side. If two repairs in sequence do not improve question 2, the construction is wrong. Go back to step 4 and select a different move. Keep the rejected version.

## Rules that do not bend

- **Orthographic camera by default.** Parallel lines stay parallel and equal lengths stay equal in one direction. Use perspective only for a scene that a camera or an eye sees, and say so.
- **One colour, one meaning, in all panels.** Context is pale and cool, not grey. A colour that carries a value is `unlit`. Do not add a colour that has no entry in your cast list.
- **Same camera for all states that the reader compares.** Change one thing only.
- **Geometry from the source.** Use the real equation, coordinates or data when they exist. If you draw a schematic shape, label it as a schematic.
- **Arrows have types.** A solid 3D arrow is a physical vector: a force, a flow, a ray. A flat overlay arrow is narrative: "then" or "becomes". Do not mix the two types in one style.
- **Show the evidence status.** Measured, simulated, derived and schematic content must look different or have a label.
- **No invented data.** Do not draw a result that the project does not have. Do not smooth, recolour or exaggerate data to help the story. If you exaggerate a scale for visibility, write the factor on the figure.
- **The smallest full mechanism.** One worked instance is better than the full system. Remove each part that does not change the prediction.
- **Labels are vector text.** Do not put text in the 3D raster.

## Handoff

Give the user `figure.svg`, `figure.png`, the `figure.mjs` source and a caption. The caption states the mechanism sentence, the status of the content and each exaggeration. Tell the user which reference figures you studied and what is not verified. If you cannot view images, say that the figure has no visual review.
