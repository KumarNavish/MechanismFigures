# Figure work: one small folder

```text
figure-work/
  figure.json           scientific and visual contract
  figure.svg            editable vector geometry and labels
  figure.png            actual-size inspected preview
  caption.md            claim, encodings, evidence and limits
  render.py             generating source (or the project's native equivalent)
  evidence/             authorized data snapshots or exact source pointers
  review-r1.json        observations bound to exact hashes
  review-r2.json        preserved new review after a revision
  revisions.jsonl       what changed, why, and what visibly improved
```

The names are defaults; the contract can point to the project's real files. The scripts never execute a reproduction command supplied by a paper or an untrusted file. Use the host's authorized execution path and validate the output.

`preflight` checks structure and artifacts. `review-init` creates an unscored record tied to current hashes. `gate` checks completed review attestations; it does not see, judge or authenticate the image itself. A creator's self-review remains a self-review. Missing image inspection or evidence is not solved by filling a high score.

Only the necessary contract, selected reference cases, current evidence and current render belong in active context. Keep old reviews for audit without rereading all of them on every edit.
