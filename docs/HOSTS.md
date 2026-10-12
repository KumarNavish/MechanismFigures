# Agent hosts and account boundaries

Verified against primary host documentation on **8 October 2026**. The machine-readable registry is `tools/agent_hosts.json`. File routes can change; keep the verification date and sources with any update.

| Host | User-global local discovery | Invocation / important boundary |
|---|---|---|
| Codex CLI / IDE / desktop skill environment | `~/.agents/skills` | `$mechanism-figures` or the skill picker. Metadata can trigger relevant tasks; cloud workers need their own environment. [OpenAI documentation](https://learn.chatgpt.com/docs/build-skills). |
| Claude Code | `~/.claude/skills` adapter | `/mechanism-figures` or request the skill. Local files do not upload to account skills. Do not alter `skills/synced`. [Claude documentation](https://code.claude.com/docs/en/skills). |
| Cursor | `~/.agents/skills` | Select/use the skill in a supported client. Cloud skill sync is separate; this installer does not enable it or create a duplicate native skill. [Cursor documentation](https://cursor.com/help/customization/skills). |
| Gemini CLI | `~/.agents/skills` | Request the skill and honor activation consent. [Gemini documentation](https://geminicli.com/docs/cli/skills/). |
| OpenCode | `~/.agents/skills` | The skill tool loads the named skill; existing permission policy still applies. [OpenCode documentation](https://opencode.ai/docs/skills/). |
| GitHub Copilot local skill clients | `~/.agents/skills` | User-global local discovery is distinct from hosted coding-agent environments. [GitHub documentation](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills). |
| Windsurf / Devin Desktop | Legacy `~/.codeium/windsurf/skills` adapter; current shared discovery | Supports the documented legacy path while retaining the shared canonical copy. No provider sync setting changes. [Devin documentation](https://docs.devin.ai/desktop/cascade/skills). |
| OpenClaw local agents | `~/.agents/skills` | Shared personal discovery in the default state only; custom `OPENCLAW_STATE_DIR` deployments need their own configured installation. Eligibility and agent configuration still apply. [OpenClaw documentation](https://docs.openclaw.ai/tools/skills). |

## ChatGPT on desktop versus web/mobile

OpenAI documents standalone skills for the ChatGPT desktop app and Codex local clients, and plugin-bundled skills for Chat/Work across web, desktop and mobile. The portable package at this repository's root exposes `skills/mechanism-figures`; it needs no MCP server or model API. [Skill scope](https://learn.chatgpt.com/docs/build-skills) · [Plugin packaging and local marketplaces](https://developers.openai.com/plugins/build/plugins).

The root repository is now a standard **skill**, not a directly installable local marketplace. The optional plugin ZIP builder places the same payload under `skills/mechanism-figures` inside a separate plugin package. Use that generated archive only through a supported account/workspace flow. The root `plugin.json` is maintainer packaging metadata; no marketplace or account is silently enabled.

GitHub publication and a portable ZIP are not a public plugin-directory listing or account-wide installation. No account activation is claimed without provider confirmation. Local CLI/Git discovery and account installation remain separate.

## Claude account skills and other cloud clients

Claude's account skill management and synchronization are separate from local authoring. Upload the standalone skill ZIP through the supported account UI where available; do not assume a local `~/.claude/skills` adapter pushes it to web or Cowork. Similarly, a remote development machine, container, workspace or hosted agent needs access to its own installed package.

## Any other capable agent

Use the standard `skills/mechanism-figures/` folder in that host's supported personal-skill location, or explicitly tell it to read `SKILL.md` and open the referenced images. No undocumented global search path is invented. An agent without image-viewing/file capabilities must report that missing capability; a text-only summary cannot be certified as visual calibration.

## What “always learn from the style” means

On every scientific-figure task handled by this skill: choose two current reference images, open the files, record the exact hashes and concrete visual observations, transfer the operation, and compare the rendered result to those same images. It does not mean copying a palette, silently injecting the whole gallery into unrelated chats, overriding system instructions, or bypassing user permissions.
