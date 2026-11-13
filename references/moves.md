# The fifteen moves

A move is a construction that makes an operation visible. Select the move from the operation, not from the look that you like. Each entry gives the purpose, the construction, the stage calls, the usual failures and the references to study. Reference IDs are in [atlas.md](atlas.md).

## 1. Cutaway

**Shows** an operation inside a closed body.

**Build.** Model the full body. Remove the part between the viewer and the operation with one plane, or with two planes for a quarter cut. Cap the section so that solid material looks solid. Keep the hidden operation in a strong colour and the body in grey.

```js
const body = S.solid(geometry, {color: P.context});
S.cut(body, point, normalTowardRemovedSide);                 // capped section
S.cut([body], p2, n2);                                       // second plane makes a quarter cut
```

**Failures.** The cut removes the thing that it must show. The section face has the same tone as the outer surface, so the reader cannot tell cut from skin: give the cap a darker or hatched tone. The cut plane is at a random angle: align it with a symmetry plane or an axis.

**Study.** `kent-hopfion`, `t3ss-needle`, `tokamak`, `scutoids`, `flagellar-stator`, `piezo-dome`.

## 2. Exploded view

**Shows** how parts join, and the sequence of an assembly.

**Build.** Move each part along the axis on which it assembles. Move it only far enough to show the interface. Draw a tether from each part to its home position. Keep all parts in one camera.

```js
S.explode(part, [0, 0, 0.8]);          // offset plus a dashed tether
```

**Failures.** Parts move in random directions. The distance is so large that the reader cannot tell which part goes where. Tethers are missing.

**Study.** `photonic-braids`, `alphatensor`.

## 3. Layer stack

**Shows** a sequence of layers: a device, a tissue, a set of representations, a network.

**Build.** Draw each layer as a thin slab. Separate the slabs on one axis by equal gaps. Link corresponding points in adjacent layers with thin vertical lines. Give each layer one role and one label at its edge.

**Failures.** The gaps are different, and the reader thinks that the gap has a meaning. The top layer hides the layers below: use a lower elevation, make the top layer a ghost, or cut a corner.

**Study.** `photonic-braids`, `genomnimatte`, `kplanes`, `kent-hopfion`.

## 4. Ghost and focus

**Shows** one active part in a large assembly.

**Build.** Draw the context at 15 to 30 percent opacity with a thin outline. Draw the active part solid and in colour. The ghost gives location. It does not compete.

```js
S.solid(contextGeometry, {color: P.context, opacity: 0.2});
S.solid(activeGeometry, {color: P.focus});
```

**Failures.** Three or more transparent layers overlap, and the result is fog. The ghost is so faint that the location is lost.

**Study.** `loterie-vam`, `frenzel-chiral`, `birch-skyrmion`, `rfdiffusion`, `myosin-stroke`.

## 5. Fixed-camera sequence

**Shows** a change of state, a deformation, or time.

**Build.** Put copies of the object side by side. The orthographic camera shows each copy from the same angle. Change one thing between adjacent copies. Keep the persistent object in one colour. Put the state name below each copy. Use three to five states. Use flat overlay arrows between states.

```js
for (let k = 0; k < 4; k++) build(k).position.add(S.right(k * 2.4));   // same view of each state
S.link(anchorA, anchorB, {text: 'stretch'});
```

**Failures.** The camera or the scale changes between states. Two things change at once. There are so many states that each one is too small.

**Study.** `kennaway-growth`, `christoffersen-lake`, `cohesin-ratchet`, `myosin-stroke`, `kirigami`, `diffusive-machines`.

## 6. Unroll pair

**Shows** the logic of a curved surface: periodic boundaries, winding, a map.

**Build.** Draw the surface in 3D. Draw its flat map adjacent to it, at the same scale if possible. Draw the same path, the same seams and the same field on the two views. Colour each seam, so that the eye can glue the flat map together again.

**Failures.** The two views have different colours or orientations. The seams have no marks.

**Study.** `weiler-gauge`, `torus`, `hulse-compass`. The template `kit/template.mjs` uses this move.

## 7. Ray trace

**Shows** sampling, projection, imaging or transport through a volume.

**Build.** Draw the source, the volume and the receiver as solid objects. Draw a small number of rays, three to seven, as thin tubes or lines. Mark the sample points on one ray. Show what one sample reads and what the receiver gets.

```js
S.curve([source, hit], {color: P.act, width: 0.4});
S.sphere(samplePoint, 0.03, {color: P.act, outline: false});
```

**Failures.** There are too many rays. The rays do not start and stop on surfaces. The figure does not show what occurs at a sample.

**Study.** `nerf`, `plenoxels`, `caustics`, `loterie-vam`, `wolf-tomography`.

## 8. Field on geometry

**Shows** a scalar or vector quantity that lives on a surface or in a volume.

**Build.** Paint a scalar on the real surface with one colour ramp. For a vector field, draw arrows on a regular lattice or draw stream tubes. In a volume, show the field on two or three slice planes and on one isosurface. Give the ramp a legend with units. Use the diverging ramp only when zero has a meaning.

```js
S.surface((u, v) => point(u, v), {value: (u, v, p) => field(p), range: [lo, hi], ramp: ramps.viridis});
```

**Failures.** A rainbow ramp. Too many arrows. Light and shadow change the apparent value: for exact reading, add a flat panel of the same field.

**Study.** `zheng-hopfion`, `birch-skyrmion`, `graphcast`, `kennaway-growth`, `bioprint4d`.

## 9. Linked zoom

**Shows** a local rule that gives a global result.

**Build.** Draw the whole. Mark a small region. Draw that region large, adjacent to the whole, and link the two with two thin lines from the corners of the mark. The enlarged view shows the rule: one unit cell, one neighbourhood, one update.

**Failures.** The zoom has a different orientation from the region. The link is missing. The zoom shows a different instance from the marked one.

**Study.** `plenoxels`, `frenzel-chiral`, `tokamak`, `flagellar-stator`, `cellrank`, `scutoids`.

## 10. State-space geometry

**Shows** dynamics, optimisation, invariance or the structure of a representation.

**Build.** Give each axis a name. Draw the manifold or landscape as a surface. Draw trajectories on it as tubes with a start mark and an arrowhead. Draw a constraint set as a plane or a curve. To compare two systems, draw two surfaces in the same axes.

**Failures.** The axes have no names. The surface is an invention: say "schematic", or compute it. A 3D embedding of high-dimensional data gets a geometric reading that the projection cannot support.

**Study.** `fip`, `torus`, `safaie-dynamics`, `cohen-untangling`, `cellrank`.

## 11. Index to geometry

**Shows** what an index, a tensor or a matrix entry refers to.

**Build.** Draw the algebraic object as a block or a grid. Draw the things that the indices name. Use one colour for one entry in the two views. Highlight only the active terms.

**Cells and slabs.** Draw a tensor as slabs of unit cells with a gap between slabs. Make each cell a thin box with crease lines. Give colour only to the cells that take part. Set `receive: false` on all cells, because a shadow on a cell looks like a different value.

```js
for (let c = 0; c < 3; c++) for (let i = 0; i < 6; i++) for (let j = 0; j < 6; j++)
  S.box([i, j, c * 0.9], [1, 1, 0.18], {color: inPatch(i, j) ? P.focus : P.paper, receive: false, outline: false});
```

**Failures.** The link between entry and object is by position only. Give it a colour and a label.

**Study.** `alphatensor`, `kplanes`, `hulse-compass`, `alphafold`.

## 12. Target, program, structure, consequence

**Shows** an inverse design: a desired result fixes the local instructions.

**Build.** Four states in a row. The target: what you want. The program: the local quantity that the method computes. The structure: the thing that is built. The consequence: the measured result, which the reader compares with the target. The first and last states must look alike, and that likeness is the proof.

**Failures.** The consequence is missing. The program is a box with a name in it.

**Study.** `caustics`, `bioprint4d`, `mechanical`.

## 13. Matched counterfactual

**Shows** the effect of one intervention.

**Build.** Two or three copies with the same camera, scale, light and layout. One element changes, and it has the intervention colour. Where a part is removed, leave its space empty or leave a ghost.

**Failures.** The layout changes also. The baseline is weaker than the fair one.

**Study.** `flagellar-stator`, `weiler-gauge`, `kent-hopfion`, `kennaway-growth`, `genomnimatte`.

## 14. Block diagram

**Shows** a process in a landscape, a tissue or a medium: surface above, section below.

**Build.** Cut a rectangular block from the world. The top face shows the surface. The two front faces show the vertical section. Draw the process across the faces as arrows and numbered events. State the vertical exaggeration.

**Failures.** The side faces are empty. The depth scale is absent. Question marks and certain facts look the same: give uncertain items a different style.

**Study.** `azores-dike`, `christoffersen-lake`, `graphcast`.

## 15. Loop through one object

**Shows** a feedback cycle: training, control, an iterative algorithm, a molecular cycle.

**Build.** Select one object and carry it round the cycle: it is observed, evaluated and updated. Draw the stations of the cycle in a ring or a row with a return path. The object keeps its colour at each station. Give the return path its own style, because it carries the update.

**Failures.** The cycle is a ring of boxes with no object in it. The return arrow has no label, so the reader does not know what goes back.

**Study.** `cohesin-ratchet`, `dreamfusion`, `nerf`.

## Combine moves with care

A strong figure uses one primary move and at most two helper moves. `graphcast` uses a block diagram, a field on geometry and a fixed-camera sequence. `kent-hopfion` uses a cutaway, a layer stack and a matched counterfactual. Name your primary move before you build. If you cannot name it, the figure has no construction yet.
