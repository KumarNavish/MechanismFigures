# Scientific motion

Motion must explain an update, trajectory, transformation, intervention or correspondence. It is not evidence merely because it moves.

## One source of truth

Implement a pure `stateAt(t)` from the real data, exact rule or explicitly labeled illustration. Geometry, labels, legends and readouts consume the same returned state. Interpolation between independent snapshots must be labeled as interpolation; do not pretend it is a tracked physical path. Preserve entity identity, sampling time and comparison budget.

`kit/motion.mjs` supplies `createPlayback({duration, stateAt, draw, element, autoplay})`. It does not infer dynamics. `play`, `pause`, `seek` and `dispose` are explicit, playback stops at the end, and hidden/offscreen views pause. With reduced motion, the drawing remains still and manual seek can show selected states.

## Controls must belong to the experiment

Use a control for a meaningful intervention, parameter, time or viewpoint. Label its units and allowable regime. Show what stays fixed. Support keyboard operation through native buttons and ranges; do not rely on hover alone. Do not silently restart motion after a user pauses it. If changing the camera hides the decisive interface, the view is not an acceptable explanatory default.

## Verify a sequence, not just its best frame

Inspect start, a representative intermediate state, every transition, boundary cases and final state. Check for discontinuities, occlusion errors, inconsistent readouts, moving labels that change meaning, and dropped object identity. Validate exact values against the state model. Check reduced motion, keyboard use, background suspension and a readable static fallback.

Only claim a performance measurement after recording the device, viewport, renderer, workload and actual timing. Fewer animated steps do not demonstrate a faster algorithm. The existing website walkthrough is an editorial reference reading—not an execution trace of a scientific project or a claim that this skill generated the published figures.
