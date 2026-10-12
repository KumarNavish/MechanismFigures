# Rendered verification: read the images, not just the report

This is the concrete inspection pass before the [scoring review](critique.md). It complements scientific checks; it does not replace them.

## Capture safely

```sh
node scripts/capture.mjs figure.svg --out-dir review-r1 --selector svg
```

The directory must not already exist. The tool captures a full 1× view and a 2×2 grid of 4× detail tiles, then writes source/capture hashes and bounded browser diagnostics. Change `--tiles` up to 4 for dense material. `--width` and `--height` set the viewport, not the scientific scale. Physical SVG dimensions are preserved in CSS units; a digital capture is not a physical print test.

For an authored HTML page, inspect its source first and pass `--allow-active`. Select the mechanism region, not the entire UI. For the bundled walkthrough, `--time 27 --selector .construction-paper` captures a deterministic teaching state. General project interaction states must be exposed by the project renderer, not invented by the capture script.

Use an already installed Chrome/Chromium or `CHROME_PATH`. Network resources are blocked and no sandbox-disabling flags are supplied. A host that cannot run the browser returns a blocker; move the verification to an authorized environment or use its approved browser tool. Do not weaken global security settings.

## Inspect every output

1. **1×:** identify the entry object, follow the operation, predict the stated consequence. Read actual label sizes and controlled comparisons. Hide the caption for the frozen question.
2. **4×:** inspect all decisive junctions, boundaries, overlap ordering, line endings, contact points, annotations, source-image crops and correspondence. A crop that misses the mechanism is not sufficient coverage.
3. **Science:** evaluate one normal case, a boundary case and a counterexample or falsifier from the underlying evidence/model. Watch for an inference stronger than the data supports.
4. **Sequence, when applicable:** inspect initial/intermediate/final states and each intervention. Check values, identity, keyboard interaction and reduced motion.
5. **Reference comparison:** reopen the same two real published figures at readable scale and name the remaining gaps in encoding, composition and finish.

The tool may flag a label outside the target bounds or an image that did not decode. These are diagnostics, not comprehensive detection: it does not prove all text is legible, all routes are collision-free, or the mechanism is correct. Read the PNGs even when the diagnostics are empty.

## Bind the critique to the result

Add the scene record and the decisive capture files to `outputs.additional` in the figure contract. Run preflight, then create a new hash-bound review. Record the wrong reading, its location and cause, and the repair. Preserve old revisions. The creator's cold-read attempt is a self-review, not a timed or blind independent experiment.

A missing renderer, unavailable evidence or failed reference-level reading is an explicit non-final state. Neither a passing file check nor a beautifully rendered wrong figure satisfies the skill.
