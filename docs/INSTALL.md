# Install once, then use in any local project

## Standard Agent Skills installation

```sh
npx skills add KumarNavish/MechanismFigures -g -a codex
```

The repository now has one `SKILL.md` at its root, like the supplied Anatomy standard. Use `-a claude-code` or `-a opencode` for other hosts, or several `-a` flags. Omit `-g` for a project installation. The standard CLI is third-party software and requires network access; its checked 1.7.2 release requires Node ≥22.20. Set `DISABLE_TELEMETRY=1` to disable its telemetry. A direct Git clone into an **unused** skill folder or the complete standalone ZIP is also valid.

Choose one installation owner. Never overwrite an existing managed/Git/CLI installation with another installer. Root-relative resources stay portable. Old public gallery and motion URLs redirect to their new asset paths.

## Optional conservative Python installer

```bash
git clone https://github.com/KumarNavish/MechanismFigures.git
cd MechanismFigures
python3 install.py --global --agents all
python3 install.py --doctor
```

Python 3.9+ standard library only. For this Python route: no package installation, API key, model execution, subscription, administrator privileges, or modification of unrelated configuration is required. For a fixed release, clone with `--branch v0.5.0`.

**Global means one operating-system user on this machine, across local projects.** It does not mean all users, remote machines, web/mobile accounts, all cloud workers, or guaranteed automatic invocation in every message.

## What is written

The complete skill lives at `~/.agents/skills/mechanism-figures/`. Modern shared-directory hosts read that same copy. Claude Code and legacy Windsurf receive user-level adapters at `~/.claude/skills/mechanism-figures` and `~/.codeium/windsurf/skills/mechanism-figures`.

Adapters are symlinks by default. `--adapter-mode copy` uses verified owned copies; `auto` falls back to a copy when directory symlinks cannot be created, for example on restricted Windows setups. Updates include previously managed copied adapters so they cannot quietly retain an old version.

Receipts, locks, staging and previous versions stay under `~/.agents/mechanism-figures-state/`, outside directories scanned for skills. Existing `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, provider settings, account permissions and other skills remain untouched. A preexisting unmanaged or modified skill is a conflict, never silently replaced.

## Plan, install, update, verify

| Command | Result |
|---|---|
| `python3 install.py --global --agents all --dry-run` | Resolves exact host paths and reports conflicts; writes nothing. |
| `python3 install.py --global --agents all` | Installs a new or identical version. A different managed version requires `--update`. |
| `python3 install.py --global --agents all --update` | Replaces only hash-verified managed files; retains the previous version. |
| `python3 install.py --doctor` | Checks canonical and adapter file hashes; reports account and activation limits. Does not run agents. |
| `python3 install.py --recover` | Reconciles and rolls back a stopped incomplete transaction; refuses changed targets or a still-running owner. |

`--agents codex,claude,gemini` selects specific documented hosts. The `all` alias is the finite supported registry in `tools/agent_hosts.json`, not a claim about every agent product in existence. `--home` supports isolated tests or an explicitly chosen user home; no administrator impersonation is performed.

A source checkout can also be installed project-locally with the legacy narrow helper: `python3 tools/install.py --dest /path/to/project/.agents/skills`. Do not combine multiple copies of the same named skill in one host unless you intentionally want separate scopes.

## Make the host actually use it

Refresh its skill list or start a new session after installation. Select the skill once using the host's documented UI or invocation, then provide the four project inputs. Ask it to open two real calibration files and report the actual paths before drawing. A host may require consent, may cap its initial discovery list, or may have policy disabling skills.

The installer intentionally does **not** append an always-on instruction to every global prompt. That would consume unrelated-chat context, interfere with existing rules, and still would not install a cloud account capability. The front-loaded skill description routes scientific figure tasks; explicit invocation is the reliable fallback. [Host-by-host scope and invocation](HOSTS.md).

## Interrupted or conflicting installs

A transaction is journaled before target changes; completed replacements are hash-verified and the old version is retained. Ordinary exceptions attempt rollback. After a killed process or disconnect, inspect `--doctor` and the retained journal before doing anything else. `--recover` checks actual paths and hashes, then reverses only its exact owned targets. It never replays a model call or overwrites a post-failure user edit.

If a skill has local edits, preserve and review them rather than forcing an update. The installer does not include a force-overwrite switch. If an old installation lock exists without a recoverable journal, inspect its process and state manually; the program does not assume that a long-running owner is dead.

## Web, mobile and remote environments

These have their own installation scope. The repository includes a plugin ZIP build route using the root manifest as packaging metadata, but an account/workspace must still install or publish the package through its supported flow. A local filesystem install is not that action. Details and primary documentation are in [HOSTS.md](HOSTS.md).
