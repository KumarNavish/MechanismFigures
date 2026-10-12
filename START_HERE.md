# Start here

## Install the standard skill

```sh
npx skills add KumarNavish/MechanismFigures -g -a codex
```

Use `-a claude-code` or `-a opencode` for those hosts. Then request `$mechanism-figures` in Codex, `/mechanism-figures` in Claude Code, or use the host’s skill picker.

The repository **is** the skill: one root [SKILL.md](SKILL.md), with the kit, references, assets and scripts beside it. Direct Git clone and ZIP installation also work. Existing Python-managed users should use the explicit safe update path in [INSTALL.md](docs/INSTALL.md), not overwrite their folder with a different installer.

## Give the agent four inputs

```text
Use mechanism-figures.
Project context: …
Mechanism or result: …
Data and evidence: …
Output constraints: …
```

The agent follows [SKILL.md](SKILL.md), opens two actual published figures, identifies the visual world and parts, implements from evidence, inspects the real render at 1× and 4×, and repairs it before review.

[Gallery](assets/gallery.html) · [Motion walkthrough](assets/motion.html) · [Craft](references/craft.md) · [Quality gate](references/critique.md).

## Scope

Global means this local user across projects, not every cloud account or guaranteed automatic invocation in every chat. The standalone skill and optional generated plugin archive have separate installation routes. [Host boundaries](docs/HOSTS.md).

## Maintain

[Repository standards adapted from Anatomy](docs/ANATOMY_STANDARD.md) · [Maintainer guide](docs/MAINTAINING.md) · [Evaluation protocol](benchmarks/PROTOCOL.md).
