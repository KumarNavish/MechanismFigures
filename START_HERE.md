# Start here

## Install once

```bash
python3 install.py --global --agents all
python3 install.py --doctor
```

Updating an existing managed installation: `python3 install.py --global --agents all --update`.

This installs one user-level skill and the required host adapters. It does not modify global prompts, launch agents, or upload to web/mobile accounts. [Exact scope, supported hosts and recovery](docs/INSTALL.md).

## Use it in a scientific project

```text
Use mechanism-figures for this figure.
Context: …
Mechanism/result: …
Evidence/data: …
Output constraints: …
```

The agent starts at [SKILL.md](skills/mechanism-figures/SKILL.md), opens two actual images, states a project-specific visual mapping, builds, inspects and revises. [Gallery](skills/mechanism-figures/assets/gallery.html) · [60-second walkthrough](skills/mechanism-figures/assets/motion.html).

## Distribute across products

The repository is a portable skill **and** a minimal Agent Plugins package. [Account/cloud setup](docs/HOSTS.md) explains what a local installation cannot do. GitHub publication is not a universal plugin-directory listing.

## Maintain or evaluate

[Architecture and sources of truth](docs/MAINTAINING.md) · [Curation decisions](docs/CURATION.md) · [Independent evaluation protocol](benchmarks/PROTOCOL.md).
