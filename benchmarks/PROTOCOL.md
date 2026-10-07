# Measuring transfer and reliability

## Status

**No cross-agent outcome study has been run for v0.2.0.** The shipped unit tests test engineering behavior, and the complete approved gallery supplies visual calibration. Neither establishes that this skill reliably outperforms a capable agent or reaches publication-defining quality across domains. The rubric thresholds are design policy pending empirical calibration.

## Primary outcome

For a frozen task, agent, seed and total budget: **fraction of outputs that pass the fidelity hard gates and the ≥90/100 reference-calibrated rubric under independent review**. A beautiful unsupported explanation counts as a failure. Refusal to invent causation is correct behavior for the association-only task; evaluate that task's honest figure or `needs_evidence` decision separately from finished-figure pass rate.

Secondary outcomes: correct captionless mechanism identification and intervention prediction; score dispersion within and between agents; iterations and changes of construction; false causal/physical/history claims; missing provenance; total wall time, agent tokens, tool calls, rendering time and external compute. Unknown costs remain unknown, never zero. Record all failed and unfinished attempts.

## Matched comparison

Compare the same capable agent under two conditions:

- **Baseline:** project context, mechanism/result, evidence, output constraints, and a competent request for a scientifically faithful, readable publication figure. The same tools and rendering libraries are available; SciencePlots may be available in both conditions for genuine quantitative panels.
- **Skill:** the exact same four-input task packet, tools and budget, plus this versioned skill. Reference reading and critique consume the same total budget, not free extra time.

A style-only bar-chart prompt is not a fair baseline. Match data access, resolution, reference-access policy, tool permissions, model settings and all compute limits. Randomize condition order; isolate work directories; prevent one attempt seeing another's draft. Freeze input packet SHA-256, skill commit, agent/version, seed and budget before dispatch. Do not run paid models or extra agents without explicit authority.

## Calibration, evaluation and holdout separation

The 20 published references are **training/calibration material**. `tasks.json` contains eight public diagnostic tasks, not a held-out test set. A claim about general transfer requires new domain/project packets withheld from skill development; nominate their owner and fix their hashes before evaluating. Never quietly replace failed tasks or tune the rubric after seeing the outcomes.

Start with at least two agent systems and three independent runs per condition/task for a diagnostic study, then determine the larger sample from the precision actually needed. That small initial design is not sufficient evidence of universal reliability. Report task-level outcomes and raw sample sizes; bootstrap or model uncertainty at the independent project level rather than treating every panel or repeated score as an independent study.

## Review protocol

Use at least two domain-competent, non-author reviewers. Blind condition and agent identity; show the actual-size image before its caption or method rationale. Preserve the responses to the frozen comprehension and counterfactual questions, including any measured timing. Then reveal caption/evidence and use the anchored rubric. Record disagreements before adjudication; report raw agreement and an appropriate reliability statistic rather than only a reconciled score.

For each output save its contract, data/source snapshots, image/vector, caption, creator self-review, independent review records, exact hashes, and revision log. The CLI's `--require-independent` checks recorded structure and differing identities; it cannot authenticate identity or observation. A different persona of the creating agent is not independent review.

## Records and reporting

A `runs.jsonl` row contains `task`, `agent`, `seed`, `condition` (baseline/skill), `input_packet_sha256`, `budget`, `contract`, `reviews`, and `costs` (`tokens`, `wall_seconds`, `tool_calls`, `compute_seconds`; null when unknown). File paths are relative to that JSONL file's directory. Store actual artifacts, not scores copied from a chat summary.

Run `python tools/benchmark_report.py path/to/runs.jsonl`. It checks the recorded gates and matched packet/budget pairs, preserves failures and missing cost counts, and reports descriptive pass-rate differences. It does not run agents, adjudicate science, invent missing reviews, compute unsupported significance, or turn a missing run into a successful trial.

An empty/missing dataset is reported as **not_run**, not 0% success and not evidence of failure. Synthetic unit-test reviews are explicitly excluded from empirical claims. Publish results with the exact skill commit and all non-sensitive failures; redact protected data without disguising missing evidence.

## Adoption criterion

Retain the skill only if matched independent trials improve fidelity-gated pass rate or reduce total cost at matched quality, without increasing false mechanistic claims. If gains are limited to certain domains, publish that boundary and route unsupported tasks differently. A higher creator self-score alone is not an improvement.
