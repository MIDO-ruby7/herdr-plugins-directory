# herdr plugins by purpose

[🇯🇵 日本語](README.md) · 🇺🇸 English · [🇨🇳 中文](README.zh.md)

**A link collection for finding [herdr](https://herdr.dev/) plugins by what you want to get done.**

- **921** plugins indexed / last updated **2026-09-02 04:33 UTC** (auto-refreshed every 6 hours)
- Source: GitHub repositories tagged [`herdr-plugin`](https://github.com/topics/herdr-plugin) — the same population as the official [herdr.dev/plugins](https://herdr.dev/plugins/) marketplace
- Categories are auto-inferred from each repo's description and topics. If one looks wrong, fix it with a PR to [`data/overrides.json`](data/overrides.json)
- Install: `herdr plugin install owner/repo` — [official docs](https://herdr.dev/docs/plugins/)

> [!WARNING]
> This is an auto-collected index, not a vetted catalog. Plugins are code that runs directly on your machine, so check the manifest and the commands it runs before installing.

<a id="purposes"></a>

## Browse by purpose

- [**🆕 Recently added**](#cat-new) (112) — Plugins that joined this list in the last 7 days.
- [**Notifications & Alerts**](#cat-notify) (35) — I want to know when an agent finishes or gets stuck waiting for input, even when I'm away from my desk
- [**Mobile & Remote Control**](#cat-remote) (39) — I want to monitor agents from my phone or while away, and just send back approvals
- [**Agent Orchestration**](#cat-agents) (131) — I want to launch, split up, and manage multiple AI agents together
- [**Git Worktrees & Branches**](#cat-worktree) (48) — I want to spin up a worktree for each piece of work, and have the cleanup handled automatically too
- [**Code Review & Diffs**](#cat-review) (39) — I want to read the diff an agent wrote and send comments back on it
- [**GitHub & Issue Trackers**](#cat-forge) (32) — I want to kick off work from an issue or PR, and track PR status
- [**Workspaces & Layouts**](#cat-layout) (34) — When I open a project, I want tabs, panes, and startup commands all set up in one shot
- [**Pane Navigation & Keys**](#cat-navigate) (112) — I want to move and resize between panes and workspaces using the same keys as my editor
- [**File Viewers & Editors**](#cat-files) (57) — I want to open a file tree inside a pane, or keep it in sync with my editor
- [**Tokens & Cost**](#cat-cost) (24) — I want to see how much an agent is spending, and cut down on usage
- [**Monitoring & Dashboards**](#cat-monitor) (68) — I want an at-a-glance overview of agent and machine status
- [**Fuzzy Finders & Palettes**](#cat-finder) (84) — I want to invoke commands or projects even when I only half-remember their names
- [**Automation, Hooks & Schedules**](#cat-automation) (49) — I want a fixed set of steps to run automatically on worktree creation or at a chosen time
- [**Session State & Restore**](#cat-session) (33) — I want to close my work and later resume from exactly the same state
- [**Titles, Naming & Looks**](#cat-naming) (53) — I want tab names and terminal titles to be automatically clear, or want to change how things look
- [**Text & URL Grabbing**](#cat-text) (23) — I want to grab strings, paths, or URLs shown on screen without touching the mouse
- [**Plugin Management & Authoring**](#cat-meta) (9) — I want to manage plugins themselves, or build my own
- [**Other & Utilities**](#cat-other) (51) — Handy things that don't fit any of the categories above

<a id="cat-new"></a>

## 🆕 Recently added

> Plugins that joined this list in the last 7 days.

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**🆕 herdr-claude-lifecycle**](https://github.com/daocoding/herdr-claude-lifecycle)<br><sub>daocoding</sub> | Hook-first Claude Code lifecycle for herdr + Omarchy: working/blocked/idle from Claude's own hooks, verify after every Claude Code update | `claude-code` `omarchy` `python` | 0 | 2026-09-02 |
| [**🆕 herdr-dia**](https://github.com/rewt/herdr-dia)<br><sub>rewt</sub> | Turn a GitHub PR you're reading in the Dia browser into a Herdr coding-agent review or update — from a side panel. | `ai-agents` `browser-extension` `code-review` `dia` `native-messaging` | 0 | 2026-09-02 |
| [**🆕 herdr-git-dirty**](https://github.com/viko16/herdr-git-dirty)<br><sub>viko16</sub> | A lightweight Herdr plugin that shows uncommitted Git file counts in each Space. | `git` `shell` | 0 | 2026-09-02 |
| [**🆕 herdr-tab-jump**](https://github.com/cyperx84/herdr-tab-jump)<br><sub>cyperx84</sub> | Focus herdr tab N by position, from any keybinding — split your number row between tabs and workspaces | `shell` | 1 | 2026-09-01 |
| [**🆕 herdr-claude-usage**](https://github.com/anyaachan/herdr-claude-usage)<br><sub>anyaachan</sub> | Global Claude Code plan usage in Herdr: tab-bar summary + popup dashboard. statusLine-powered, multi-account aware. | `claude` `claude-code` `cli` `terminal` `shell` | 0 | 2026-09-01 |
| [**🆕 herdr-tab-command**](https://github.com/asermax/herdr-tab-command)<br><sub>asermax</sub> | Starts an agent or runs a command in a new tab, based on the name you give the tab | `typescript` | 0 | 2026-08-31 |
| [**🆕 herdr-agent-numbers**](https://github.com/DillonWall/herdr-agent-numbers)<br><sub>DillonWall</sub> | Number herdr's agents panel to match focus_agent (prefix+1..9). | `terminal-multiplexer` `shell` | 0 | 2026-09-01 |
| [**🆕 herdr-hitl**](https://github.com/huketo/herdr-hitl)<br><sub>huketo</sub> | Block a Herdr coding agent on a human decision, delivered to your phone over Telegram or Discord | `agent-skill` `ai-agents` `cli` `discord-bot` `go` | 0 | 2026-09-01 |
| [**🆕 herdr-pane-mark**](https://github.com/jovylle/herdr-pane-mark)<br><sub>jovylle</sub> | Herdr plugin — custom $mark under Agents via palette/popup (no fork) | `terminal` `shell` | 0 | 2026-09-01 |
| [**🆕 herdr-jump**](https://github.com/lancodev/herdr-jump)<br><sub>lancodev</sub> | Two-pane fuzzy switcher for herdr workspaces and agents, with vim keys | `fzf` `tui` `shell` | 0 | 2026-09-01 |
| [**🆕 lasso**](https://github.com/skellleks/lasso)<br><sub>skellleks</sub> | Review pane for herdr: per-agent diffs with syntax highlighting and inline comments sent back to the agent | `ai-agents` `claude-code` `code-review` `git-diff` `ratatui` | 0 | 2026-08-31 |
| [**🆕 herdr-jump**](https://github.com/solidsnakedev/herdr-jump)<br><sub>solidsnakedev</sub> | Fuzzy workspace, pane and tab pickers for herdr, plus a last-workspace toggle | `shell` | 0 | 2026-09-01 |
| [**🆕 herdr-pane-tools**](https://github.com/solidsnakedev/herdr-pane-tools)<br><sub>solidsnakedev</sub> | Vim-aware pane navigation, aerospace-style pane moves and tmux-style rotation for herdr | `shell` | 0 | 2026-09-01 |
| [**🆕 herdweb**](https://github.com/zlxlabs/herdweb)<br><sub>zlxlabs</sub> | Monitor and drive your coding agents from your phone.Voice Input, Paste Image, webhook notification, multi devices server support.. | `typescript` | 5 | 2026-09-01 |
| [**🆕 herdr-mission-control**](https://github.com/vjeantet/herdr-mission-control)<br><sub>vjeantet</sub> | Mission Control for herdr: one key, every pane of the workspace as a live tile grid grouped by tab; pick one to switch to it | `expose` `mission-control` `terminal` `tui` `rust` | 3 | 2026-09-01 |
| [**🆕 herdr-pets**](https://github.com/abhishek944/herdr-pets)<br><sub>abhishek944</sub> | A transparent desktop village for live Herdr agents | `typescript` | 2 | 2026-08-31 |
| [**🆕 herdr-codex-bridge**](https://github.com/ardasevinc/herdr-codex-bridge)<br><sub>ardasevinc</sub> | Native Herdr pane identity for Codex sessions using a centralized app-server | `ai-agents` `codex` `terminal` `go` | 2 | 2026-09-01 |
| [**🆕 herdr-composer**](https://github.com/danieljvdm/herdr-composer)<br><sub>danieljvdm</sub> | Compose tasks, attach context, and launch coding agents in isolated Herdr workspaces | `coding-agents` `git-worktree` `rust` | 1 | 2026-09-01 |
| [**🆕 herdr-mobile-app**](https://github.com/teasec4/herdr-mobile-app)<br><sub>teasec4</sub> | herdr mobile plugin | `herdr-integration` `herdr-mobile` `dart` | 1 | 2026-08-31 |
| [**🆕 herdr-hyprland**](https://github.com/aorumbayev/herdr-hyprland)<br><sub>aorumbayev</sub> | Hyprland inspired controls for herdr | `ai-agents` `developer-tools` `golang` `hyprland` `keybindings` | 0 | 2026-08-31 |
| [**🆕 herdr-sheep**](https://github.com/huketo/herdr-sheep)<br><sub>huketo</sub> | Watch your Herdr coding agents as a flock of animated ASCII sheep | `ascii-art` `rust` `tui` | 0 | 2026-08-31 |
| [**🆕 herdr-tab-titles**](https://github.com/kewah/herdr-tab-titles)<br><sub>kewah</sub> | Herdr plugin that names panes and tabs after the first coding-agent prompt. | `javascript` | 0 | 2026-09-01 |
| [**🆕 precc-herdr-plugin**](https://github.com/peria-ai/precc-herdr-plugin)<br><sub>peria-ai</sub> | PRECC plugin for herdr: cross-agent token-savings telemetry + one-touch PRECC setup | `claude-code` `precc` `shell` | 0 | 2026-09-01 |
| [**🆕 provider-usage**](https://github.com/ryus1234/provider-usage)<br><sub>ryus1234</sub> | Provider usage and quota bar for Herdr | `ai-usage` `quota-monitor` `rust` | 0 | 2026-08-31 |
| [**🆕 herdr-tab-new**](https://github.com/softwarecrafts/herdr-tab-new)<br><sub>softwarecrafts</sub> | Resume or start an agent session in the herdr workspace for this project — a herdr plugin, and a CLI for terminals outside herdr | `typescript` | 0 | 2026-08-31 |
| [**🆕 herdr-grid**](https://github.com/WillHeather/herdr-grid)<br><sub>WillHeather</sub> | Tile a herdr workspace's agent panes into a screen-sized grid, and put them back. | `python` | 0 | 2026-08-31 |
| [**🆕 herdr-updater**](https://github.com/diegopzz/herdr-updater)<br><sub>diegopzz</sub> | Keep Herdr and its plugins current across a whole fleet, safely | `rust` `updater` | 7 | 2026-09-01 |
| [**🆕 herdr-grid**](https://github.com/thuanlm215/herdr-grid)<br><sub>thuanlm215</sub> | Visual Herdr pane layout editor with drag-and-drop, new shells, balanced splits, fixed presets, and safe workspace creation. | `layout-presets` `pane-layout` `productivity` `ratatui` `rust` | 6 | 2026-09-01 |
| [**🆕 herdr-arrange**](https://github.com/crierr/herdr-arrange)<br><sub>crierr</sub> | Interactive popup UI for herdr pane move / swap / re-split / layout | `go` | 4 | 2026-08-31 |
| [**🆕 agent-keep-awake**](https://github.com/happyeric77/agent-keep-awake)<br><sub>happyeric77</sub> | Prevent macOS sleep while Herdr agents are working | `javascript` | 1 | 2026-08-12 |
| [**🆕 herdr-plugins**](https://github.com/narumiruna/herdr-plugins)<br><sub>narumiruna</sub> | _(no description)_ | `rust` | 1 | 2026-08-08 |
| [**🆕 herdr-tournament**](https://github.com/neospeed83/herdr-tournament)<br><sub>neospeed83</sub> | Adversarial multi-agent code reviews for Herdr | `rust` | 1 | 2026-08-29 |
| [**🆕 herdr-undo-close**](https://github.com/pedroloch/herdr-undo-close)<br><sub>pedroloch</sub> | Reopen a closed tab in herdr, like Cmd+Shift+T in a browser - restores the label, the split tree with its ratios, each pane's cwd, and the tab's position. | `python` | 1 | 2026-07-30 |
| [**🆕 herdr-copy-hints**](https://github.com/rotemb-wond/herdr-copy-hints)<br><sub>rotemb-wond</sub> | tmux-fingers-style keyboard copy hints for Herdr: paths, Git SHAs, URLs, and more | `clipboard` `developer-tools` `keyboard-navigation` `productivity` `terminal` | 1 | 2026-07-23 |
| [**🆕 herdr-rovo-dev**](https://github.com/usrivastava92/herdr-rovo-dev)<br><sub>usrivastava92</sub> | Herdr plugin that detects Rovo Dev CLI sessions and reports them as live agents in Herdr | `ai-agent` `rovo` `rovo-dev` `shell` | 1 | 2026-07-19 |
| [**🆕 reasonix-herdr**](https://github.com/uuie/reasonix-herdr)<br><sub>uuie</sub> | Native Reasonix plugin with live lifecycle reporting and workspace control inside Herdr. | `reasonix` `python` | 1 | 2026-07-10 |
| [**🆕 herdr-activity-age**](https://github.com/1Morganmore/herdr-activity-age)<br><sub>1Morganmore</sub> | Windows Herdr plugin that shows time since each agent's last status change | `powershell` `windows` | 0 | 2026-08-30 |
| [**🆕 herdr-dynamic-workflow**](https://github.com/andthezhang/herdr-dynamic-workflow)<br><sub>andthezhang</sub> | JavaScript workflows for orchestrating coding-agent CLIs in Herdr. | `agent-fleet` `agent-orchestration` `agent-swarm` `agentic-ai` `agents` | 0 | 2026-08-30 |
| [**🆕 herdr-jetbrains**](https://github.com/chenyao0910/herdr-jetbrains)<br><sub>chenyao0910</sub> | Open the active Herdr workspace or worktree in Rider, WebStorm, IntelliJ IDEA, or GoLand. | `developer-tools` `git-worktree` `goland` `intellij-idea` `jetbrains` | 0 | 2026-08-30 |
| [**🆕 herdr-keybinds**](https://github.com/gwelican/herdr-keybinds)<br><sub>gwelican</sub> | Herdr plugin for listing/searching all keybinds, including plugins | `python` | 0 | 2026-08-31 |
| [**🆕 herdr-positional-tabs**](https://github.com/juezhong/herdr-positional-tabs)<br><sub>juezhong</sub> | Stable positional tab labels and Alt-number navigation for Herdr. | `rust` `terminal` | 0 | 2026-08-30 |
| [**🆕 herd**](https://github.com/orrgal1/herd)<br><sub>orrgal1</sub> | Issue-driven multi-agent setup for omp on herdr: a lead that files issues, workers that poll, claim, and ship them | `shell` | 0 | 2026-09-01 |
| [**🆕 herdr-worktree-guard**](https://github.com/takeaship/herdr-worktree-guard)<br><sub>takeaship</sub> | A safety-focused Herdr plugin for tracking and cleaning up agent worktrees | `coding-agents` `git-worktree` | 0 | 2026-08-30 |
| [**🆕 cbds**](https://github.com/zqkra/cbds)<br><sub>zqkra</sub> | Reliable multi-agent orchestration for the Herdr herd. Durable tasks, authoritative worker reports, and a wait that cannot hang. | `agents` `cli` `multi-agent` `orchestration` `javascript` | 0 | 2026-08-31 |
| [**🆕 dotfiles**](https://github.com/tifandotme/dotfiles)<br><sub>tifandotme</sub> | ~/.* | `aerospace` `chezmoi` `cmux` `dotfiles` `ghostty` | 3 | 2026-09-01 |
| [**🆕 herdr-world**](https://github.com/IvoryHeart/herdr-world)<br><sub>IvoryHeart</sub> | Herdr World — a multi-surface web experience for Herdr | `multi-agent` `observability` `pixel-art` `react` `rust` | 2 | 2026-09-01 |
| [**🆕 herdr-code-board**](https://github.com/sazardev/herdr-code-board)<br><sub>sazardev</sub> | Kanban queue for agentic prompts inside Herdr: cards dispatch real agents into panes, worktrees and workspaces, with rules that chain one card to the next. | `ai-agents` `kanban` `rust` `tui` | 2 | 2026-08-30 |
| [**🆕 harbr**](https://github.com/dev-town/harbr)<br><sub>dev-town</sub> | Harbour TUI | `typescript` | 1 | 2026-08-31 |
| [**🆕 herdr-plugin-atomic-workflows**](https://github.com/caner-akca/herdr-plugin-atomic-workflows)<br><sub>caner-akca</sub> | Herdr plugin: launch and monitor isolated Atomic workflow tasks — campaign board, sidebar tokens, run ledger, and an optional Telegram cockpit | `javascript` | 0 | 2026-09-01 |
| [**🆕 herdr-pane-agent-unread**](https://github.com/NachoPal/herdr-pane-agent-unread)<br><sub>NachoPal</sub> | Per-pane 'unread' notifier + sidebar badge for herdr - surfaces agents that finish or need input in panes you aren't viewing (herdr tracks 'seen' per tab, not… | `python` | 0 | 2026-09-01 |
| [**🆕 herdr-bot**](https://github.com/Phoobobo/herdr-bot)<br><sub>Phoobobo</sub> | _(no description)_ | `tui` `typescript` | 0 | 2026-08-31 |
| [**🆕 herdr-cmd-agent-plugin**](https://github.com/thesimonharms/herdr-cmd-agent-plugin)<br><sub>thesimonharms</sub> | Herdr plugin to recognize CommandCode (cmd) as an agent — idle/working/blocked detection via screen manifest + cmd mod | `cmd` `commandcode` `shell` | 0 | 2026-08-31 |
| [**🆕 herdr-space-groups**](https://github.com/yojahny55/herdr-space-groups)<br><sub>yojahny55</sub> | Herdr plugin: group Spaces into named, colored groups — picker popup (mouse + keyboard), sidebar group headers, automatic ordering | `javascript` | 0 | 2026-08-29 |
| [**🆕 herdr-ferry**](https://github.com/wavrin/herdr-ferry)<br><sub>wavrin</sub> | Move files and clipboard between the Herdr box and your laptop over SSH — no cloud bucket | `rust` | 2 | 2026-08-29 |
| [**🆕 hermes-herdr-auto-reconcile**](https://github.com/chris-yyau/hermes-herdr-auto-reconcile)<br><sub>chris-yyau</sub> | Gateway liveness plugin for Hermes supervisors watching Herdr panes | `automation` `hermes-agent` `multi-agent` `python` | 1 | 2026-08-28 |
| [**🆕 herdr-overview**](https://github.com/iamgp/herdr-overview)<br><sub>iamgp</sub> | Mission Control / Exposé for Herdr — a live tiled overview of every space | `terminal` `tui` `javascript` | 1 | 2026-08-28 |
| [**🆕 herdr-session-sync**](https://github.com/nengqi/herdr-session-sync)<br><sub>nengqi</sub> | Auto-sync Claude Code, Codex & Agent session names across Herdr pane labels, PTY window titles, and mobile companion apps (Heeler) | `agent` `claude-code` `codex` `heeler` `terminal-multiplexer` | 1 | 2026-08-28 |
| [**🆕 herdr-plugin-env-sync**](https://github.com/DecampsRenan/herdr-plugin-env-sync)<br><sub>DecampsRenan</sub> | Herdr plugins: env-sync sets up new Git worktrees (.env copy, remote branch tracking, setup commands) with a live status panel | `developer-tools` `git-worktree` `shell` | 0 | 2026-08-28 |
| [**🆕 herdr-session-title-name**](https://github.com/jovylle/herdr-session-title-name)<br><sub>jovylle</sub> | Herdr plugin: terminal_title_stripped → tab persistence (session_title alone on top, tab keeps it after close) | `sidebar` `terminal` `html` | 0 | 2026-08-28 |
| [**🆕 herdr-nvim**](https://github.com/jtnovellis/herdr-nvim)<br><sub>jtnovellis</sub> | Neovim inside Herdr: a per-tab full-height sidebar, and a real round trip with your coding agent — ask about the code you're looking at, read the answer withou… | `ai-agents` `claude-code` `developer-tools` `lua` `neovim` | 0 | 2026-08-31 |
| [**🆕 herdr-ccs**](https://github.com/KennethWKZ/herdr-ccs)<br><sub>KennethWKZ</sub> | Make `ccs claude` behave like native Claude Code in Herdr: pane detection + launcher-aware restore through ccs. | `shell` | 0 | 2026-08-29 |
| [**🆕 herdr-rich-notifications**](https://github.com/liamwh/herdr-rich-notifications)<br><sub>liamwh</sub> | Rich native desktop notifications for herdr agent-status changes: zero-LLM context enrichment, click-to-focus (herdr agent focus + Niri window targeting). Fork… | `notifications` `rust` | 0 | 2026-08-28 |
| [**🆕 herdr-gh-issue-label**](https://github.com/polidog/herdr-gh-issue-label)<br><sub>polidog</sub> | ブランチに対応する GitHub issue の番号とタイトルを Herdr のスペースに表示するプラグイン | `github-issues` `shell` | 0 | 2026-08-28 |
| [**🆕 herdr-git-stack**](https://github.com/ubuntudroid/herdr-git-stack)<br><sub>ubuntudroid</sub> | Herdr plugin: shows each space's position in its git branch stack in the spaces sidebar, flags branches whose parent has moved, and keeps stacks contiguous. Lo… | `bash` `developer-tools` `git` `stacked-branches` `shell` | 0 | 2026-08-29 |
| [**🆕 herdr-annotate**](https://github.com/plannotator/herdr-annotate)<br><sub>plannotator</sub> | Annotate terminal text, review documents and agent replies in Herdr, and send the feedback straight back to the agent. | `annotation` `multiplexer` `rust` | 311 | 2026-08-31 |
| [**🆕 agys**](https://github.com/quaywin/agys)<br><sub>quaywin</sub> | Effortless multi-profile isolation & real-time quota tracking for Antigravity CLI in Herdr via zero-pollution sandboxing. | `ai-agents` `antigravity` `cli` `context-window` `developer-tools` | 9 | 2026-08-31 |
| [**🆕 herdr-palette**](https://github.com/vjeantet/herdr-palette)<br><sub>vjeantet</sub> | Command palette for herdr, à la Sublime Text / VS Code — built-in operations, plugin actions and your own commands behind one key | `command-palette` `fuzzy-search` `terminal` `tui` `rust` | 7 | 2026-08-31 |
| [**🆕 herdr-lazydocker**](https://github.com/sudoeren/herdr-lazydocker)<br><sub>sudoeren</sub> | Run lazydocker in a herdr split pane or its own tab. | `docker` `lazydocker` `shell` | 6 | 2026-08-27 |
| [**🆕 herdr-flash**](https://github.com/youguanxinqing/herdr-flash)<br><sub>youguanxinqing</sub> | flash.nvim-style search, select, and yank for Herdr panes | `rust` `terminal` | 3 | 2026-09-02 |
| [**🆕 herdr-dwm-layout**](https://github.com/42lizard/herdr-dwm-layout)<br><sub>42lizard</sub> | DWM-style master/stack layouts for Herdr | `dwm` `fzf` `rust` `shell` `tiling` | 1 | 2026-08-28 |
| [**🆕 herdr-sessionizer**](https://github.com/42lizard/herdr-sessionizer)<br><sub>42lizard</sub> | tmux-sessionizer style plugin for herdr | `fzf` `shell` | 1 | 2026-08-28 |
| [**🆕 herdr-spinner**](https://github.com/hasuwini77/herdr-spinner)<br><sub>hasuwini77</sub> | Animated braille spinner for Herdr panes in the working state, via display-only pane metadata | `spinner` `terminal` `tui` `javascript` | 1 | 2026-08-27 |
| [**🆕 herdr-tunnel**](https://github.com/ivorpad/herdr-tunnel)<br><sub>ivorpad</sub> | Herdr plugin: put a local port on the public internet, copy the URL, take it down again | `tui` `python` | 1 | 2026-08-27 |
| [**🆕 herdr-wsl-notify**](https://github.com/tkmct/herdr-wsl-notify)<br><sub>tkmct</sub> | A Herdr plugin that shows a Windows desktop toast when an agent (Claude Code, etc.) running under WSL2 becomes done (finished) or blocked (waiting for approval… | `javascript` | 1 | 2026-08-27 |
| [**🆕 herdr-notes**](https://github.com/0xfelixli/herdr-notes)<br><sub>0xfelixli</sub> | Annotate selected terminal text in a Rust popup textbox — herdr plugin | `rust` `terminal` | 0 | 2026-08-27 |
| [**🆕 workspace-basename**](https://github.com/42lizard/workspace-basename)<br><sub>42lizard</sub> | herdr plugin to set the workspace name based on the basename of the cwd the workspace was created | `shell` | 0 | 2026-08-27 |
| [**🆕 herdr-tab-git**](https://github.com/hasuwini77/herdr-tab-git)<br><sub>hasuwini77</sub> | Git branch and status in the Herdr Spaces sidebar that follow the active tab instead of the first one | `git` `terminal` `tui` `javascript` | 0 | 2026-08-28 |
| [**🆕 herdr-go**](https://github.com/herdr-go/herdr-go)<br><sub>herdr-go</sub> | Control your herdr coding agents from anywhere — private, P2P, EasyTier-secured. | `dart` | 0 | 2026-09-01 |
| [**🆕 herdr-ports**](https://github.com/ivorpad/herdr-ports)<br><sub>ivorpad</sub> | Herdr plugin: a popup that lists listening ports, names the project behind each one, and kills or opens it | `tui` `python` | 0 | 2026-08-27 |
| [**🆕 herdr-reap**](https://github.com/ivorpad/herdr-reap)<br><sub>ivorpad</sub> | Herdr plugin: every agent's lifecycle state, and one keystroke to close the finished ones | `tui` `python` | 0 | 2026-08-27 |
| [**🆕 herdr-worktree-setup**](https://github.com/jtnovellis/herdr-worktree-setup)<br><sub>jtnovellis</sub> | herdr plugin: make a new git worktree immediately usable — copy .env & dev state, clone dependency caches (APFS/reflink), mise trust, direnv allow, install dep… | `git-worktree` `rust` | 0 | 2026-08-29 |
| [**🆕 herdr-ai-memory**](https://github.com/MarlonPassos-git/herdr-ai-memory)<br><sub>MarlonPassos-git</sub> | Herdr popup for checkout-local AI Memory workstreams | `ai-memory` `python` | 0 | 2026-08-27 |
| [**🆕 herdr-equalize-panes**](https://github.com/ponko2/herdr-equalize-panes)<br><sub>ponko2</sub> | Automatically keeps panes in each tab evenly sized as panes are created, closed, moved, or exited. | `rust` | 0 | 2026-08-30 |
| [**🆕 herdr-claude-context-meter**](https://github.com/tmastalirsch/herdr-claude-context-meter)<br><sub>tmastalirsch</sub> | herdr plugin: Claude Code context usage as a bar — in the status line and in a herdr pane | `claude-code` `context-window` `statusline` `shell` | 0 | 2026-08-27 |
| [**🆕 herdr-claude-safe-compact**](https://github.com/tmastalirsch/herdr-claude-safe-compact)<br><sub>tmastalirsch</sub> | herdr plugin: compacts idle Claude Code panes, but only once a handoff is safely on disk | `claude-code` `compaction` `shell` | 0 | 2026-08-31 |
| [**🆕 herdr-workspace-board**](https://github.com/tmastalirsch/herdr-workspace-board)<br><sub>tmastalirsch</sub> | herdr plugin: one line per git repository with unfinished work, ranked by how likely it is to be forgotten | `git` `productivity` `workspace` `shell` | 0 | 2026-08-27 |
| [**🆕 herdr-auto-title**](https://github.com/kryptamine/herdr-auto-title)<br><sub>kryptamine</sub> | Tab titles that automatically follow the work in each tab. Keep your tabs organized and instantly know what you're working on with Herdr. | `go` | 47 | 2026-08-30 |
| [**🆕 sheep**](https://github.com/gokay-ai/sheep)<br><sub>gokay-ai</sub> | Undo for AI coding agents. Every agent turn becomes a restorable checkpoint. | `git` `rust` `tui` `undo` | 5 | 2026-08-28 |
| [**🆕 herdr-palette**](https://github.com/cesarferreira/herdr-palette)<br><sub>cesarferreira</sub> | Popup command palette for Herdr. | `typescript` | 3 | 2026-08-14 |
| [**🆕 herdr-pet**](https://github.com/nikok6/herdr-pet)<br><sub>nikok6</sub> | Tiny desk pet on your herdr panes: types, waits, and celebrates with your agent. Works with any Codex pet. | `rust` | 3 | 2026-08-26 |
| [**🆕 herdr-standup**](https://github.com/neospeed83/herdr-standup)<br><sub>neospeed83</sub> | Evidence-backed daily standups from Git activity and Herdr context. | `developer-tools` `standup` `rust` | 2 | 2026-08-31 |
| [**🆕 scp-explorer**](https://github.com/TinocoAI/scp-explorer)<br><sub>TinocoAI</sub> | MobaXterm-style SCP file explorer herdr plugin (cross-platform macOS/Linux/Windows) | `curses` `file-manager` `scp` `python` | 2 | 2026-08-31 |
| [**🆕 herdr-glance**](https://github.com/arvmaan/herdr-glance)<br><sub>arvmaan</sub> | desktop widget to view the status of your agents | `rust` | 1 | 2026-08-26 |
| [**🆕 herdr-replay**](https://github.com/neospeed83/herdr-replay)<br><sub>neospeed83</sub> | Record and replay multi-agent Herdr coding sessions as interactive timelines. | `ai-agents` `developer-tools` `terminal-recording` `rust` | 1 | 2026-08-29 |
| [**🆕 herdr-awake**](https://github.com/susomejias/herdr-awake)<br><sub>susomejias</sub> | Herdr plugin: keep the machine awake while Herdr agents are busy | `shell` | 1 | 2026-08-26 |
| [**🆕 herdr-pr**](https://github.com/yelsed/herdr-pr)<br><sub>yelsed</sub> | A Todo of the pull requests waiting on you, in a herdr pane. Reads everything through the gh CLI. | `rust` | 1 | 2026-08-29 |
| [**🆕 multitrunk-herdr-plugin**](https://github.com/yoyoyeti/multitrunk-herdr-plugin)<br><sub>yoyoyeti</sub> | Herdr plugin for multitrunk task workspaces | `git` `multitrunk` `rust` | 1 | 2026-08-31 |
| [**🆕 unblock**](https://github.com/aneym/unblock)<br><sub>aneym</sub> | One queue for everything your agents need from you. Blockers need an action, grills need a judgement; secrets never enter the model's context. | `agents` `human-in-the-loop` `mcp` `javascript` | 0 | 2026-08-28 |
| [**🆕 herdr-quick-prompt**](https://github.com/astwys/herdr-quick-prompt)<br><sub>astwys</sub> | A Herdr plugin to send predefined prompts to an agent pane | `shell` | 0 | 2026-08-24 |
| [**🆕 herdr-command-palette**](https://github.com/barnuri/herdr-command-palette)<br><sub>barnuri</sub> | F1-style command palette for herdr — fuzzy-search and run every action from every installed plugin. Zero dependencies. | `command-palette` `terminal` `javascript` | 0 | 2026-09-01 |
| [**🆕 herdr-spotify**](https://github.com/DeepRuparel/herdr-spotify)<br><sub>DeepRuparel</sub> | Spotify for Herdr — Go, zero-setup local controls + gated search/queue/save via PKCE | `spotify` `go` | 0 | 2026-08-28 |
| [**🆕 herdr-context-locator**](https://github.com/Dimon94/herdr-context-locator)<br><sub>Dimon94</sub> | Copy a self-describing locator for a Herdr agent's canonical native session context | `python` | 0 | 2026-08-26 |
| [**🆕 herdr-llm-summary-header**](https://github.com/dnf0/herdr-llm-summary-header)<br><sub>dnf0</sub> | Herdr plugin: LLM one-line summary written to the pane title when an agent finishes | `javascript` | 0 | 2026-08-03 |
| [**🆕 herdr-claude-title-hook**](https://github.com/eduardoborges/herdr-claude-title-hook)<br><sub>eduardoborges</sub> | Claude Code plugin that syncs the session title to the Herdr tab title | `shell` | 0 | 2026-08-26 |
| [**🆕 herdr-looper**](https://github.com/gurronen/herdr-looper)<br><sub>gurronen</sub> | Launch repeatable machine-local Pi jobs in fresh Herdr workspaces and worktrees | `automation` `rust` `terminal` | 0 | 2026-08-26 |
| [**🆕 herdr-desktop-switcher**](https://github.com/gustavocaiano/herdr-desktop-switcher)<br><sub>gustavocaiano</sub> | Experimental macOS desktop switcher for Herdr | `rust` | 0 | 2026-08-26 |
| [**🆕 herdr-plugin-agent-quota**](https://github.com/kwanwooi25/herdr-plugin-agent-quota)<br><sub>kwanwooi25</sub> | Agent quota for Herdr — token & cost dashboard, sidebar quota gauges, and tab bar summary for Claude Code, Codex, and Grok | `javascript` | 0 | 2026-08-30 |
| [**🆕 herdr-browser**](https://github.com/redsquiggle/herdr-browser)<br><sub>redsquiggle</sub> | Keep Chromium tab groups aligned with Herdr workspaces | `chromium` `ratatui` `rust` | 0 | 2026-07-28 |
| [**🆕 herdr-status-ui-bar**](https://github.com/speardragon/herdr-status-ui-bar)<br><sub>speardragon</sub> | AI agent plan-usage gauges (Claude Code / Codex / Grok) in the herdr tab bar | `claude-code` `shell` | 0 | 2026-08-28 |
| [**🆕 herdr-context-display**](https://github.com/TheBrunoPetkovic/herdr-context-display)<br><sub>TheBrunoPetkovic</sub> | Colour-coded context window usage on every Claude Code agent row in herdr | `claude-code` `terminal` `typescript` | 0 | 2026-08-26 |
| [**🆕 herdr-coder-sessions**](https://github.com/ubuntudroid/herdr-coder-sessions)<br><sub>ubuntudroid</sub> | Browse running Coder agent sessions in herdr and open each as its own workspace: agentty on the session, its changes mirrored into a local worktree for review | `agentapi` `coder` `coding-agents` `python` | 0 | 2026-09-01 |
| [**🆕 pi-agent-usage**](https://github.com/w784415/pi-agent-usage)<br><sub>w784415</sub> | Pi extension that displays OpenAI Codex quota and reset times, with Herdr plugin support. | `openai-codex` `pi-extension` `pi-package` `quota` `typescript` | 0 | 2026-08-26 |

[⬆ Back to purposes](#purposes)

<a id="cat-notify"></a>

## Notifications & Alerts

> I want to know when an agent finishes or gets stuck waiting for input, even when I'm away from my desk

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-focus-notify**](https://github.com/yankewei/herdr-focus-notify)<br><sub>yankewei</sub> | Clickable macOS notifications for Herdr agents. Sends a native toast when an agent becomes blocked or done; clicking it brings the terminal forward and focuses… | `alerter` `macos` `notifications` `productivity` `rust` | 17 | 🔄 2026-08-18 |
| [**herdr-pings**](https://github.com/joelhooks/herdr-pings)<br><sub>joelhooks</sub> | Turn-level wake events for AI agents in herdr panes — pi extension, wait CLI, crash bridge, and Discworld callsigns for your workers | `ai-agents` `pi` `typescript` | 9 | 2026-08-09 |
| [**herdr-ntfy**](https://github.com/horn553/herdr-ntfy)<br><sub>horn553</sub> | Minimal dependencies: jq, curl, and sh — send ntfy notifications when Herdr agents finish or get blocked. | `shell` | 7 | 2026-08-01 |
| [**herdr-ntfy-notify**](https://github.com/zom-2018/herdr-ntfy-notify)<br><sub>zom-2018</sub> | Real-time ntfy push notifications for Herdr terminal agents | `agent` `ntfy` `push-notifications` `tui` `javascript` | 7 | 2026-06-23 |
| [**herdr-terminal-notifier**](https://github.com/dot/herdr-terminal-notifier)<br><sub>dot</sub> | Customizable macOS notifications for herdr agent state changes via terminal-notifier | `macos` `terminal-notifier` `shell` | 6 | 2026-07-14 |
| [**herdr-hail**](https://github.com/natori-hrj/herdr-hail)<br><sub>natori-hrj</sub> | Two-way Slack & Discord bridge for herdr — get pinged when an agent blocks, reply/tap to unblock. No tunnel. | `discord` `slack` `typescript` | 6 | 2026-07-19 |
| [**herdr-notify-windows**](https://github.com/aclima01/herdr-notify-windows)<br><sub>aclima01</sub> | Windows 11 toast notifications for herdr agents (turn finished / needs input) | `powershell` | 4 | 2026-07-23 |
| [**herdr-telegram-bridge**](https://github.com/cokekitten/herdr-telegram-bridge)<br><sub>cokekitten</sub> | Get a Telegram push when a herdr agent finishes or blocks — reply to it to send text or files straight back into that agent. No server, no tunnel, no app. | `ai-agents` `chatops` `claude-code` `developer-tools` `notifications` | 4 | 2026-08-06 |
| [**herdr-telegram-plugin**](https://github.com/mvallebr/herdr-telegram-plugin)<br><sub>mvallebr</sub> | Telegram bot companion for herdr — remote control any agent via Telegram forum topics, zero LLM in the path. | `typescript` | 4 | 🔄 2026-08-31 |
| [**herdr-announcer**](https://github.com/nhclink16/herdr-announcer)<br><sub>nhclink16</sub> | Herdr plugin: speaks a one-sentence LLM summary when an agent finishes or needs input — local TTS, ElevenLabs, or any custom command | `tts` `python` | 3 | 🔄 2026-08-20 |
| [**herdr-discord-presence**](https://github.com/revanp/herdr-discord-presence)<br><sub>revanp</sub> | Herdr plugin: show your Herdr session and agent status as Discord Rich Presence | `typescript` | 3 | 2026-08-14 |
| [**herdr-agent-notify**](https://github.com/A1exthegreat/herdr-agent-notify)<br><sub>A1exthegreat</sub> | Herdr plugin: desktop notifications when agents finish working, need confirmation, or go idle | `javascript` | 2 | 2026-08-15 |
| [**herdr-cache-alert**](https://github.com/AltanS/herdr-cache-alert)<br><sub>AltanS</sub> | Herdr plugin: prompt-cache countdown on every agent pane, with every cache rule sourced and dated | `ai-agents` `ai-coding` `ai-tools` `claude-code` `multiplexing` | 2 | 🔄 2026-09-01 |
| [**buzzr**](https://github.com/candypoets/buzzr)<br><sub>candypoets</sub> | Mirror live Herdr spaces and agents into Buzz channels with Nostr identities and mention routing. | `agents` `buzz` `nostr` `rust` | 2 | 2026-08-14 |
| [**agent-webhook-notify**](https://github.com/happyeric77/agent-webhook-notify)<br><sub>happyeric77</sub> | Send webhook notifications when Herdr agents finish or get blocked | `javascript` | 2 | 2026-08-12 |
| [**herdr-guard**](https://github.com/StructuPath/herdr-guard)<br><sub>StructuPath</sub> | Cross-agent command policy for Herdr: audit, alert, and interrupt dangerous shell commands | `ai-agents` `command-policy` `security` `terminal` `javascript` | 2 | 🔄 2026-08-23 |
| [**herdr-prayer-times**](https://github.com/bayoudhi/herdr-prayer-times)<br><sub>bayoudhi</sub> | Next Islamic prayer and countdown in the Herdr sidebar, with a timetable popup and notifications | `rust` | 1 | 2026-08-13 |
| [**session-sounds**](https://github.com/ChrisPachulski/session-sounds)<br><sub>ChrisPachulski</sub> | Distinct per-agent completion and attention sounds for Herdr on macOS and Linux. | `coding-agents` `notifications` `rust` | 1 | 2026-07-19 |
| [**herdr-notify-wsl**](https://github.com/saeedrahimi/herdr-notify-wsl)<br><sub>saeedrahimi</sub> | Windows 11 toast notifications for herdr agents running inside WSL. Based on aclima01/herdr-notify-windows. | `powershell` | 1 | 2026-07-23 |
| [**🆕 herdr-wsl-notify**](https://github.com/tkmct/herdr-wsl-notify)<br><sub>tkmct</sub> | A Herdr plugin that shows a Windows desktop toast when an agent (Claude Code, etc.) running under WSL2 becomes done (finished) or blocked (waiting for approval… | `javascript` | 1 | 🔄 2026-08-27 |
| [**herdr-telegram-notifications**](https://github.com/barnuri/herdr-telegram-notifications)<br><sub>barnuri</sub> | herdr plugin: Telegram notifications when an agent goes idle, gets blocked, or finishes | `telegram` `javascript` | 0 | 🔄 2026-09-01 |
| [**herdr-prompt-reply**](https://github.com/cedrus-8864/herdr-prompt-reply)<br><sub>cedrus-8864</sub> | Answer herdr agent permission prompts straight from a macOS notification — real answer buttons, single Swift binary, nothing waiting in the background | `ai-agents` `claude-code` `macos` `macos-notifications` `notifications` | 0 | 🔄 2026-08-19 |
| [**herdr-telegram-notify**](https://github.com/elkraps/herdr-telegram-notify)<br><sub>elkraps</sub> | Customizable Telegram notifications for Herdr agent state changes, with status filters, templates, multi-chat delivery, deduplication, Codex approval buttons,… | `ai-agents` `automation` `developer-tools` `javascript` `nodejs` | 0 | 🔄 2026-08-27 |
| [**herdr-random-sounds**](https://github.com/gridness/herdr-random-sounds)<br><sub>gridness</sub> | play random notification sounds per agent status in herdr on macOS | `herdr-integration` `macos` `notification` `notifications` `python` | 0 | 🔄 2026-08-23 |
| [**🆕 herdr-hitl**](https://github.com/huketo/herdr-hitl)<br><sub>huketo</sub> | Block a Herdr coding agent on a human decision, delivered to your phone over Telegram or Discord | `agent-skill` `ai-agents` `cli` `discord-bot` `go` | 0 | 🔄 2026-09-01 |
| [**herdr-slack-notify**](https://github.com/juninaba/herdr-slack-notify)<br><sub>juninaba</sub> | Send Slack notifications when Herdr agents finish or get blocked. | `javascript` | 0 | 2026-07-07 |
| [**drover-notify**](https://github.com/keinstn/drover-notify)<br><sub>keinstn</sub> | Herdr plugin that sends Drover push notifications when an agent becomes blocked | `javascript` | 0 | 2026-08-01 |
| [**🆕 herdr-rich-notifications**](https://github.com/liamwh/herdr-rich-notifications)<br><sub>liamwh</sub> | Rich native desktop notifications for herdr agent-status changes: zero-LLM context enrichment, click-to-focus (herdr agent focus + Niri window targeting). Fork… | `notifications` `rust` | 0 | 🔄 2026-08-28 |
| [**herdr-telegram-slack-bridge**](https://github.com/lsisoft/herdr-telegram-slack-bridge)<br><sub>lsisoft</sub> | Bidirectional Telegram and Slack bot bridge for Herdr agent sessions, routing blocked-agent alerts and chat replies back to Herdr or tmux panes | `ai-agents` `slack-bot` `telegram-bot` `tmux` `python` | 0 | 2026-07-28 |
| [**🆕 herdr-pane-agent-unread**](https://github.com/NachoPal/herdr-pane-agent-unread)<br><sub>NachoPal</sub> | Per-pane 'unread' notifier + sidebar badge for herdr - surfaces agents that finish or need input in panes you aren't viewing (herdr tracks 'seen' per tab, not… | `python` | 0 | 🔄 2026-09-01 |
| [**herdr-plugin-telegram-notify**](https://github.com/OiAnthony/herdr-plugin-telegram-notify)<br><sub>OiAnthony</sub> | Standalone Herdr plugin that sends Telegram notifications when an agent is done or blocked. | `javascript` | 0 | 2026-07-16 |
| [**herdr-apple-music-plugin**](https://github.com/perlporter/herdr-apple-music-plugin)<br><sub>perlporter</sub> | Shows a toast in herdr when the currently playing track changes in Apple Music (macOS) | `shell` | 0 | 2026-07-28 |
| [**herdr-plugin-call-me**](https://github.com/radres/herdr-plugin-call-me)<br><sub>radres</sub> | Ring your real phone when a herdr agent is blocked, answer by voice, and your answer becomes the keypress the agent was waiting for. | `ai-agents` `claude-code` `codex` `developer-tools` `notifications` | 0 | 🔄 2026-08-25 |
| [**herdr-notify-center**](https://github.com/ram4-dev/herdr-notify-center)<br><sub>ram4-dev</sub> | Server-wide agent notifications with a durable popup inbox for Herdr | `notifications` `typescript` | 0 | 2026-08-14 |
| [**herdr-cc-mac-notify**](https://github.com/y-hirakaw/herdr-cc-mac-notify)<br><sub>y-hirakaw</sub> | macOS notifications for Claude Code — shows the agent's real last message, not just "done" | `claude-code` `macos` `notifications` `python` | 0 | 2026-07-17 |

<details><summary>Also relevant to this purpose</summary>

- [donghaolicd/herdr-teams-notify](https://github.com/donghaolicd/herdr-teams-notify) — Herdr plugin for bounded Microsoft Teams agent lifecycle notifications

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-remote"></a>

## Mobile & Remote Control

> I want to monitor agents from my phone or while away, and just send back approvals

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**collie**](https://github.com/AltanS/collie)<br><sub>AltanS</sub> | PWA to manage 🐑 herdr on the go. Tailnet accessible, push notifications, quick actions and more. | `agent-orchestration` `ai` `ai-agents` `ai-coding` `ai-tools` | 613 | 🔄 2026-09-01 |
| [**herdr-remote**](https://github.com/dcolinmorgan/herdr-remote)<br><sub>dcolinmorgan</sub> | Monitor and drive your herdr agents from menu bar, phone, or Telegram. Zero config locally. Free tunnel for remote. No Tailscale needed. | `macos` `mobile` `python` | 308 | 🔄 2026-09-01 |
| [**herdr-mobile-relay**](https://github.com/0cv/herdr-mobile-relay)<br><sub>0cv</sub> | Approve and monitor Herdr agents remotely from your phone, a mobile web app for Android/iOS smartphones with push notifications, QR setup, and multi-computer r… | `android` `approvals` `cloudflare` `ios` `mobile` | 155 | 🔄 2026-08-29 |
| [**herdr-watch**](https://github.com/Unayung/herdr-watch)<br><sub>Unayung</sub> | Agent status from herdr on an Apple Watch | `javascript` | 25 | 2026-08-14 |
| [**herdr-plugin-mobile-relay**](https://github.com/benkraus/herdr-plugin-mobile-relay)<br><sub>benkraus</sub> | _(no description)_ | `typescript` | 11 | 2026-08-12 |
| [**herdr-connect**](https://github.com/Tomyail/herdr-connect)<br><sub>Tomyail</sub> | Monitor and control your Herdr AI coding agents from your iPhone with this mobile companion app — read output, send follow-ups, and get notified when jobs fini… | `agent` `mobile-app` `react-native` `typescript` | 11 | 🔄 2026-09-01 |
| [**herdr-push**](https://github.com/dcolinmorgan/herdr-push)<br><sub>dcolinmorgan</sub> | herdr plugin: zero-dep event push to herdr-remote for mobile monitoring and one-tap approval | `shell` | 10 | 2026-07-09 |
| [**paddock**](https://github.com/lntvan166/paddock)<br><sub>lntvan166</sub> | A mobile-first dashboard for herdr — reads its unix socket. Run on your phone without any configuration. | `agent-orchestration` `coding-agents` `herdr-mobile` `paddock` `pwa` | 7 | 🔄 2026-09-01 |
| [**merino**](https://github.com/LoneExile/merino)<br><sub>LoneExile</sub> | Merino 🐑 — remote tunnel dashboard for Herdr agents | `go` `macos` `menubar` `react` `wails` | 6 | 🔄 2026-08-23 |
| [**herdr-call**](https://github.com/eliasstravik/herdr-call)<br><sub>eliasstravik</sub> | Voice control for Herdr | `elevenlabs` `tailscale` `voice` `typescript` | 5 | 2026-08-07 |
| [**herdr-web**](https://github.com/eyalev/herdr-web)<br><sub>eyalev</sub> | Mobile-first web UI for the herdr agent multiplexer — drive your coding agents from a phone | `claude-code` `mobile` `pwa` `terminal` `javascript` | 5 | 2026-07-29 |
| [**herdr-tether**](https://github.com/moneycaringcoder/herdr-tether)<br><sub>moneycaringcoder</sub> | Keep local and remote terminal workloads running after their Herdr view closes. | `remote-development` `rust` `ssh` `terminal` `tmux` | 5 | 🔄 2026-09-01 |
| [**muqun-gateway**](https://github.com/osuki-dev/muqun-gateway)<br><sub>osuki-dev</sub> | The program that lets Muqun reach a terminal on your own computer. It runs on your machine, talks to tmux or to Herdr, and answers your phone directly — there… | `rust` | 5 | 🔄 2026-08-20 |
| [**herdr-remote-panes**](https://github.com/Poor-Plebs/herdr-remote-panes)<br><sub>Poor-Plebs</sub> | Work on other machines from one Herdr: pick a machine from a menu, get a terminal on it. Optional experimental two-way mirroring. | `golang` `ssh` `terminal` `go` | 5 | 🔄 2026-09-01 |
| [**🆕 herdweb**](https://github.com/zlxlabs/herdweb)<br><sub>zlxlabs</sub> | Monitor and drive your coding agents from your phone.Voice Input, Paste Image, webhook notification, multi devices server support.. | `typescript` | 5 | 🔄 2026-09-01 |
| [**herdr-web**](https://github.com/barnuri/herdr-web)<br><sub>barnuri</sub> | Mobile-first web UI plugin for herdr — drive your coding agents from a phone, with notifications | `pwa` `typescript` | 4 | 🔄 2026-09-01 |
| [**herdr-portfwd**](https://github.com/miko-misa/herdr-portfwd)<br><sub>miko-misa</sub> | Automatic SSH port forwarding for coding agents on remote machines: Ctrl+click the localhost URL your agent printed and the page opens on your machine, same po… | `ai-agents` `claude-code` `cli` `coding-agents` `developer-tools` | 4 | 2026-08-11 |
| [**herdr-whistle**](https://github.com/amurru/herdr-whistle)<br><sub>amurru</sub> | Herdr plugin for remote agent management | `golang` `telegrambot` `go` | 3 | 2026-08-06 |
| [**herdr-mobile**](https://github.com/bsorescu/herdr-mobile)<br><sub>bsorescu</sub> | Phone-friendly TUI for controlling Herdr coding agents over SSH | `mobile` `ssh` `textual` `tui` `python` | 3 | 🔄 2026-08-25 |
| [**herdr-aws-ssm**](https://github.com/maayanyosef/herdr-aws-ssm)<br><sub>maayanyosef</sub> | Pick an EC2 instance and connect over AWS SSM in a herdr --remote session - no bastion or public IP. | `aws-ssm` `terminal` `shell` | 3 | 2026-07-01 |
| [**herdr-farm**](https://github.com/mejiasd3v/herdr-farm)<br><sub>mejiasd3v</sub> | Herdr plugin: 3D farm that visualizes your Herdr workspaces and agents as livestock (three.js webapp) | `threejs` `javascript` | 3 | 2026-07-28 |
| [**herdr-devup**](https://github.com/alon-z/herdr-devup)<br><sub>alon-z</sub> | Herdr plugin: per-project dev layouts from .herdr/dev.toml with tunnel-URL env sync | `typescript` | 2 | 2026-06-22 |
| [**herdr-topbar**](https://github.com/bigbug16/herdr-topbar)<br><sub>bigbug16</sub> | macOS menu bar icon for herdr — jump back to your session, open a project, and see which agent is waiting for input. | `macos` `menubar` `swift` | 2 | 🔄 2026-08-24 |
| [**herdr-telegram-gate**](https://github.com/hkdom/herdr-telegram-gate)<br><sub>hkdom</sub> | Telegram approval inbox + risk-tiered auto-approval for your herdr AI agent fleet — blocked agents surface as Telegram cards with Approve/Deny buttons (zero-de… | `approval-gate` `telegram` `javascript` | 2 | 2026-08-06 |
| [**herdr-remotedownloder**](https://github.com/kosuketut/herdr-remotedownloder)<br><sub>kosuketut</sub> | Download files from a remote Herdr pane to the connected Mac. | `rust` | 2 | 🔄 2026-08-24 |
| [**herdr-phone**](https://github.com/matheus3301/herdr-phone)<br><sub>matheus3301</sub> | Mobile remote console for Herdr over Cloudflare Tunnel and Access | `cloudflare-tunnel` `coding-agents` `developer-tools` `golang` `mobile` | 2 | 2026-08-14 |
| [**vscode-devcontainers-herdr**](https://github.com/scott-the-programmer/vscode-devcontainers-herdr)<br><sub>scott-the-programmer</sub> | Herdr relay for agents running inside a dev container | `container` `devcontainer` `rust` | 2 | 🔄 2026-08-28 |
| [**herdr-hub**](https://github.com/alex-devdone/herdr-hub)<br><sub>alex-devdone</sub> | Describe a herdr session of remote-attach panes as a portable manifest, and rebuild it on any machine | `python` | 1 | 🔄 2026-08-23 |
| [**herdrchat**](https://github.com/cobanov/herdrchat)<br><sub>cobanov</sub> | HerdrChat — control your herdr coding agents from your phone (iOS + Android) | `herdr-client` `herdr-integration` `herdr-mobile` `typescript` | 1 | 🔄 2026-08-27 |
| [**🆕 herdr-tunnel**](https://github.com/ivorpad/herdr-tunnel)<br><sub>ivorpad</sub> | Herdr plugin: put a local port on the public internet, copy the URL, take it down again | `tui` `python` | 1 | 🔄 2026-08-27 |
| [**🆕 herdr-mobile-app**](https://github.com/teasec4/herdr-mobile-app)<br><sub>teasec4</sub> | herdr mobile plugin | `herdr-integration` `herdr-mobile` `dart` | 1 | 🔄 2026-08-31 |
| [**herdr-web-tui**](https://github.com/tigorlazuardi/herdr-web-tui)<br><sub>tigorlazuardi</sub> | Daemon-first browser/PWA frontend for Herdr with an optional plugin launcher | `go` | 1 | 🔄 2026-08-29 |
| [**setnet**](https://github.com/chano-gpt/setnet)<br><sub>chano-gpt</sub> | Herd multi-harness coding agents from your phone — a Herdr plugin | `typescript` | 0 | 🔄 2026-08-29 |
| [**herdr-slack**](https://github.com/egemenyildiz/herdr-slack)<br><sub>egemenyildiz</sub> | Drive your local herdr agents from Slack — browse, prompt, and launch from your phone. No tunnel. | `slack` `typescript` | 0 | 🔄 2026-08-27 |
| [**🆕 herdr-go**](https://github.com/herdr-go/herdr-go)<br><sub>herdr-go</sub> | Control your herdr coding agents from anywhere — private, P2P, EasyTier-secured. | `dart` | 0 | 🔄 2026-09-01 |
| [**herdr-approval-gate**](https://github.com/Javamomma/herdr-approval-gate)<br><sub>Javamomma</sub> | Human sign-off gate for agent actions in herdr — run a task in a dedicated pane, verdict-check its transcript, block until a human types APPROVE <initials>. | `shell` | 0 | 2026-07-15 |
| [**herdr-wechat-plugin**](https://github.com/LuYanFCP/herdr-wechat-plugin)<br><sub>LuYanFCP</sub> | A Herdr plugin for wechat remote control | `rust` | 0 | 2026-07-17 |
| [**herdr-agents-bridge**](https://github.com/maedana/herdr-agents-bridge)<br><sub>maedana</sub> | Monitor and interact with your coding agents from your phone via a local mobile-friendly web UI — connect by scanning a QR code. | `rust` | 0 | 2026-07-22 |
| [**herdview**](https://github.com/Orchard-Robotics/herdview)<br><sub>Orchard-Robotics</sub> | View your herd from the web | `html` | 0 | 2026-07-17 |

<details><summary>Also relevant to this purpose</summary>

- [huketo/herdr-hitl](https://github.com/huketo/herdr-hitl) — Block a Herdr coding agent on a human decision, delivered to your phone over Telegram or Discord
- [radres/herdr-plugin-call-me](https://github.com/radres/herdr-plugin-call-me) — Ring your real phone when a herdr agent is blocked, answer by voice, and your answer becomes the keypress the…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-agents"></a>

## Agent Orchestration

> I want to launch, split up, and manage multiple AI agents together

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**oh-my-opencode-slim**](https://github.com/alvinunreal/oh-my-opencode-slim)<br><sub>alvinunreal</sub> | Lean, fine tuned Opencode multi agent suite · Mix any models · Auto delegate tasks | `agentic-ai` `antigravity` `cerebras` `oh-my-opencode` `opencode` | 8574 | 🔄 2026-09-01 |
| [**agentbox**](https://github.com/madarco/agentbox)<br><sub>madarco</sub> | Run multiple agents in parallel sandboxed VMs, with a single command, on your PC or in the cloud | `claude` `claude-code` `cli` `cmux` `codex` | 381 | 🔄 2026-09-01 |
| [**pi-workflows**](https://github.com/osolmaz/pi-workflows)<br><sub>osolmaz</sub> | Workflow engine, JSON control-flow tool, and live terminal viewer for the pi coding agent | `typescript` | 252 | 🔄 2026-09-02 |
| [**pi-extensible-workflows**](https://github.com/vekexasia/pi-extensible-workflows)<br><sub>vekexasia</sub> | Deterministic multi-agent workflow orchestration for Pi | `pi` `workflow` `workflows` `typescript` | 200 | 🔄 2026-08-31 |
| [**herdr-board**](https://github.com/nelsonPires5/herdr-board)<br><sub>nelsonPires5</sub> | Kanban board for herdr — cards are prompts dispatched to AI agents in visible panes | `board` `kanban` `kanban-board` `tui` `rust` | 83 | 🔄 2026-08-23 |
| [**herdr-dagr**](https://github.com/aemrebarut/herdr-dagr)<br><sub>aemrebarut</sub> | Your agent swarm as a live DAG: an orchestration graph with attempts, review gates, and evidence, in a herdr split pane. | `agents` `dag` `multi-agent` `orchestration` `rust` | 58 | 🔄 2026-08-23 |
| [**herdr-file-annotator**](https://github.com/JonasBaeumer/herdr-file-annotator)<br><sub>JonasBaeumer</sub> | A plugin for herdr to maximize agentic development without losing touch with the actual codebase | `rust` | 44 | 🔄 2026-09-01 |
| [**agentbox-herdr-plugin**](https://github.com/madarco/agentbox-herdr-plugin)<br><sub>madarco</sub> | Run multiple agents in parallel sandboxed VMs, with a single command, on your PC or in the cloud | `claude-code` `codex-cli` `opencode` `sandbox` `shell` | 29 | 2026-06-24 |
| [**herdmates**](https://github.com/caioniehues/herdmates)<br><sub>caioniehues</sub> | Claude Code agent teams, native in herdr — teammux shim, mission-control board, focus pane | `agent-teams` `claude-code` `rust` `tui` | 21 | 🔄 2026-08-21 |
| [**pi-herd**](https://github.com/ribbons-digital/pi-herd)<br><sub>ribbons-digital</sub> | Visible Pi session orchestration with Herdr panes and git worktrees | `typescript` | 17 | 2026-07-06 |
| [**PromptPilot**](https://github.com/ivanarama/PromptPilot)<br><sub>ivanarama</sub> | Background task queue for Claude Code and other AI CLIs — web UI + Telegram bot | `ai-agents` `claude-code` `telegram-bot` `python` | 14 | 🔄 2026-09-02 |
| [**herdr-vercel-sandbox-plugin**](https://github.com/vercel-labs/herdr-vercel-sandbox-plugin)<br><sub>vercel-labs</sub> | Run terminal-based coding agents in isolated Vercel Sandboxes from Herdr. | `javascript` | 13 | 2026-08-09 |
| [**herdr-agent-handoff**](https://github.com/sanirudh17/herdr-agent-handoff)<br><sub>sanirudh17</sub> | Herdr plugin that hands an in-progress agent session to a fresh session of another installed coding agent, carrying the complete session inside the prompt - no… | `agent-handoff` `claude-code` `codex` `coding-agents` `developer-tools` | 12 | 2026-08-14 |
| [**herdr-browser**](https://github.com/StructuPath/herdr-browser)<br><sub>StructuPath</sub> | Drivable agent-browser pane for Herdr with live streaming, real interaction, adaptive rendering, console/page errors, recording, and localhost routing | `terminal` `javascript` | 11 | 🔄 2026-08-23 |
| [**herdr-social-glass**](https://github.com/ythx-101/herdr-social-glass)<br><sub>ythx-101</sub> | Screenshot-friendly Social Glass theme and workflow plugin for Herdr on macOS. | `macos` `multi-agent` `terminal-theme` `shell` | 11 | 🔄 2026-08-21 |
| [**vibetty**](https://github.com/second-state/vibetty)<br><sub>second-state</sub> | Share a live AI agent terminal to smart hardware (vibekeys, vibewatch, etc.) over MQTT; can also be used as a Herdr plugin. | `claude-code` `codex` `vibecoding` `rust` | 10 | 2026-08-17 |
| [**🆕 agys**](https://github.com/quaywin/agys)<br><sub>quaywin</sub> | Effortless multi-profile isolation & real-time quota tracking for Antigravity CLI in Herdr via zero-pollution sandboxing. | `ai-agents` `antigravity` `cli` `context-window` `developer-tools` | 9 | 🔄 2026-08-31 |
| [**herdr-helpr**](https://github.com/sohanemon/herdr-helpr)<br><sub>sohanemon</sub> | Prompt-driven workspace and pane management for herdr. | `ai-agents` `bun` `cli` `developer-tools` `ink` | 8 | 2026-07-16 |
| [**herdr-catchup**](https://github.com/wilbeibi/herdr-catchup)<br><sub>wilbeibi</sub> | Cross-agent coding-session handoff for herdr: from a live pane, summarize, fork, or hand a Claude Code, Codex, Cursor, Cline, or OpenCode session to another ag… | `ai-agents` `claude-code` `codex` `coding-agents` `context-handoff` | 8 | 🔄 2026-08-28 |
| [**herdr-agent-messenger**](https://github.com/aashishd/herdr-agent-messenger)<br><sub>aashishd</sub> | Send focused, self-contained messages between AI agents running in live Herdr panes, so one agent can coordinate work with another without sharing its full con… | `python` | 6 | 2026-08-02 |
| [**pier**](https://github.com/July24/pier)<br><sub>July24</sub> | Pi is the coding-agent carrier; Herdr is a terminal workspace manager. pier adds the two capabilities pi deliberately leaves out — a todo list loop and interac… | `pi-coding-agent` `typescript` | 6 | 🔄 2026-09-01 |
| [**herdr-triage**](https://github.com/natori-hrj/herdr-triage)<br><sub>natori-hrj</sub> | Attention triage for herdr — ranks your agents by who needs you most; a long-blocked agent rises to the top. | `ai-agents` `triage` `rust` | 6 | 2026-07-23 |
| [**herdr-space-scoped-agents**](https://github.com/ShankyJS/herdr-space-scoped-agents)<br><sub>ShankyJS</sub> | herdr plugin that scopes the agent panel to the space you're focused on | `coding-agents` `terminal` `go` | 6 | 2026-07-23 |
| [**herdr-swarm**](https://github.com/StructuPath/herdr-swarm)<br><sub>StructuPath</sub> | Parallel coding agents on one repo, safely: worktree-per-agent fan-out, live change visibility, and review-first harvest for Herdr | `terminal` `javascript` | 6 | 🔄 2026-08-24 |
| [**herdr-gamepad**](https://github.com/htlin222/herdr-gamepad)<br><sub>htlin222</sub> | Drive Herdr with a game controller. Patrol your AI agents, split panes and switch workspaces from the couch — any gamepad, mapped by you in 60 seconds. | `ai-agents` `gamepad` `macos` `swift` `terminal-multiplexer` | 5 | 2026-08-08 |
| [**herdr-insight**](https://github.com/0x5c0f/herdr-insight)<br><sub>0x5c0f</sub> | Agent State Timeline Panel | `rust` | 4 | 2026-06-23 |
| [**shepherdr**](https://github.com/afogel/shepherdr)<br><sub>afogel</sub> | Shepherd delegated coding agents into visible, auditable herdr panes you can watch, resume, and take over — a herdr plugin. | `ai-agents` `claude-code` `codex` `cursor` `rust` | 4 | 2026-07-24 |
| [**herdr-scuttlebutt**](https://github.com/andybarilla/herdr-scuttlebutt)<br><sub>andybarilla</sub> | A herdr plugin that gives the agents in a herdr session a shared chat room | `rust` | 4 | 🔄 2026-08-31 |
| [**herdr-orchestrate**](https://github.com/darjss/herdr-orchestrate)<br><sub>darjss</sub> | Pi-native orchestration for visible Herdr worker sessions — a run board, durable prompts/reports/state, isolated git worktrees, and explicit model routing. | `pi-package` `typescript` | 4 | 2026-07-13 |
| [**herdr-devcontainer**](https://github.com/gambtho/herdr-devcontainer)<br><sub>gambtho</sub> | Herdr plugin for opening shells and coding agents inside a repo's Dev Container via the official Dev Containers CLI. | `coding-agents` `containers` `devcontainers` `developer-tools` `development-environment` | 4 | 2026-08-13 |
| [**herdr-espresso**](https://github.com/Hanyang-Li/herdr-espresso)<br><sub>Hanyang-Li</sub> | Keeps your MacBook awake even when the lid closed when agent is running | `rust` | 4 | 2026-07-25 |
| [**herdr-fleet**](https://github.com/Northern-Lighthouse/herdr-fleet)<br><sub>Northern-Lighthouse</sub> | Manage a fleet of herdr machines over Tailscale: dashboard plugin, auto-discovery, capacity-aware agent dispatch, diskless workspaces | `ai-agents` `tailscale` `python` | 4 | 2026-08-14 |
| [**herdr-theos-settler**](https://github.com/calebcauthon/herdr-theos-settler)<br><sub>calebcauthon</sub> | Settle Herdr agent tabs and workspaces below active work to get finished work out of the way. Theo's idea. | `rust` | 3 | 2026-07-23 |
| [**herdr-a2a**](https://github.com/IsaiasZc/herdr-a2a)<br><sub>IsaiasZc</sub> | Reliable agent-to-agent delegation layer for Herdr via A2A | `typescript` | 3 | 🔄 2026-08-27 |
| [**herdr-walkietalkie**](https://github.com/jeffory/herdr-walkietalkie)<br><sub>jeffory</sub> | Herdr plugin: token-efficient cross-agent delegation (wt) — orchestrator agents spawn Claude/OpenCode/Antigravity workers in tabs or worktrees | `shell` | 3 | 2026-08-12 |
| [**herdr-prompt-library**](https://github.com/jwkicklighter/herdr-prompt-library)<br><sub>jwkicklighter</sub> | A Herdr plugin for browsing, managing, and inserting reusable local or global Markdown prompts into the focused pane. | `go` `golang` `prompting` `snippets` `tui` | 3 | 🔄 2026-09-01 |
| [**herdr-worker-orchestrator**](https://github.com/anhnd3005-infinity/herdr-worker-orchestrator)<br><sub>anhnd3005-infinity</sub> | Dispatch tasks to CLI agent workers (agy, codex, ...) via Herdr-managed panes with stateful task tracking, worktree isolation & diff-based review. Dual plugin… | `html` | 2 | 🔄 2026-08-25 |
| [**herdr-blaxel-sandbox-plugin**](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin)<br><sub>blaxel-ai</sub> | Run coding agents in persistent Blaxel sandboxes from Herdr. | `blaxel` `claude-code` `codex` `coding-agents` `opencode` | 2 | 🔄 2026-08-18 |
| [**herdr-birdseye**](https://github.com/calebcauthon/herdr-birdseye)<br><sub>calebcauthon</sub> | Birds Eye View of your agents in herdr | `rust` | 2 | 2026-07-24 |
| [**herdr-loop**](https://github.com/cyperx84/herdr-loop)<br><sub>cyperx84</sub> | Declarative, event-driven loop and graph orchestration for herdr — run Claude Code, Codex, opencode and pi together until the work converges | `ai-agents` `golang` `orchestration` `go` | 2 | 2026-08-12 |
| [**herdr-openclaw**](https://github.com/gejiliang/herdr-openclaw)<br><sub>gejiliang</sub> | herdr plugin: manage OpenClaw TUI panes as first-class herdr agents | `openclaw` `terminal` `javascript` | 2 | 2026-08-13 |
| [**herdr-amphetamine-macos**](https://github.com/gw31415/herdr-amphetamine-macos)<br><sub>gw31415</sub> | herdr plugin that tops up Amphetamine while agents work | `python` | 2 | 2026-07-09 |
| [**🆕 herdr-world**](https://github.com/IvoryHeart/herdr-world)<br><sub>IvoryHeart</sub> | Herdr World — a multi-surface web experience for Herdr | `multi-agent` `observability` `pixel-art` `react` `rust` | 2 | 🔄 2026-09-01 |
| [**herdr-newtab-plus**](https://github.com/jeffarese/herdr-newtab-plus)<br><sub>jeffarese</sub> | A Herdr new tab that asks which folder and which agent: completes real paths, remembers where you work, and starts an agent for you. | `python` | 2 | 2026-07-26 |
| [**herdr-shame-report**](https://github.com/JYasha11/herdr-shame-report)<br><sub>JYasha11</sub> | Keeps a permanent ledger of how long you've left your AI agents waiting. The sheep remember. | `javascript` | 2 | 2026-07-10 |
| [**herdr-orchestrator**](https://github.com/kylezk777/herdr-orchestrator)<br><sub>kylezk777</sub> | Herdr-orch is a file-based agent orchestration tool that runs on top of Herdr. | `agent-orchestration` `orchestrator` `rust` | 2 | 2026-07-26 |
| [**herdr-agents-status**](https://github.com/maedana/herdr-agents-status)<br><sub>maedana</sub> | Always-on-top transparent overlay showing Herdr agent status — a spiritual successor to claudeye, built for Herdr instead of tmux. | `rust` | 2 | 2026-08-15 |
| [**chatter**](https://github.com/marcvermeeren/chatter)<br><sub>marcvermeeren</sub> | Chatter is an experiment in cross-harness agent collaboration: a shared group chat and context layer for agents working on the same Git repository in Herdr. | `agent-collaboration` `agentic-ai` `agentic-workflow` `ai-agents` `group-chat` | 2 | 🔄 2026-08-18 |
| [**herdr-agent-profiles**](https://github.com/mikeyobrien/herdr-agent-profiles)<br><sub>mikeyobrien</sub> | Data-driven CLI harness and model profiles for Herdr | `ai-agents` `terminal` `python` | 2 | 2026-08-10 |
| [**herdr-redact**](https://github.com/moneycaringcoder/herdr-redact)<br><sub>moneycaringcoder</sub> | Warns you when an agent pane has printed a credential — before you screenshot it, stream it, or paste it into a chat window. | `rust` `secret-detection` `security` `terminal` | 2 | 🔄 2026-09-01 |
| [**herdr-approve-all**](https://github.com/RenKoya1/herdr-approve-all)<br><sub>RenKoya1</sub> | herdr plugin: approve every blocked agent at once (one keystroke, all pending permission prompts) | `shell` | 2 | 2026-08-16 |
| [**🆕 herdr-code-board**](https://github.com/sazardev/herdr-code-board)<br><sub>sazardev</sub> | Kanban queue for agentic prompts inside Herdr: cards dispatch real agents into panes, worktrees and workspaces, with rules that chain one card to the next. | `ai-agents` `kanban` `rust` `tui` | 2 | 🔄 2026-08-30 |
| [**herdr-agents-history**](https://github.com/speardragon/herdr-agents-history)<br><sub>speardragon</sub> | See what your AI coding agents are actually doing — a live, keyboard-driven herdr TUI streaming every tool call across all your agents (Claude Code & Codex). | `ai-agents` `claude-code` `codex` `tui` `typescript` | 2 | 2026-07-19 |
| [**herdr-conductor**](https://github.com/StructuPath/herdr-conductor)<br><sub>StructuPath</sub> | Orchestrate a feature-delivery team as visible Herdr agent panes — the Conductor plugin | `orchestration` `javascript` | 2 | 🔄 2026-08-23 |
| [**herdr-agent-office**](https://github.com/suisya-systems/herdr-agent-office)<br><sub>suisya-systems</sub> | Your agent fleet as a pixel-art office - a herdr plugin. See who's working, who's stuck, and jump to them. | `python` | 2 | 2026-07-25 |
| [**herdr-wakeup**](https://github.com/usrivastava92/herdr-wakeup)<br><sub>usrivastava92</sub> | Herdr plugin that keeps macOS or Linux awake while Herdr-managed agents are working | `power-management` `sleep-prevention` `wakeup` `rust` | 2 | 2026-07-17 |
| [**herdr-agent-timer**](https://github.com/Yemeni/herdr-agent-timer)<br><sub>Yemeni</sub> | A Herdr plugin that alternates each agent's status label with its elapsed time | `shell` | 2 | 2026-08-14 |
| [**herdr-pouch**](https://github.com/AltanS/herdr-pouch)<br><sub>AltanS</sub> | Herdr plugin: stash prompts for an agent ahead of time and insert them when it's ready | `ai-agents` `ai-coding` `ai-tools` `multiplexing` `typescript` | 1 | 🔄 2026-08-24 |
| [**herdr-pi-reloader**](https://github.com/anrunt/herdr-pi-reloader)<br><sub>anrunt</sub> | Reload or restart idle Pi agent sessions from a Herdr overlay TUI. | `rust` | 1 | 2026-07-18 |
| [**herdr-pane-topic-sync**](https://github.com/danbuhler/herdr-pane-topic-sync)<br><sub>danbuhler</sub> | herdr plugin: auto-name panes & tabs after each agent's live topic (Claude Code, Codex, …) instead of 1, 2, 3. | `ai-agents` `claude-code` `terminal` `tmux-alternative` `javascript` | 1 | 2026-08-04 |
| [**herdr-handoff**](https://github.com/devops-fj/herdr-handoff)<br><sub>devops-fj</sub> | Preview and securely hand off local working context between Herdr coding agents. | `ai-agents` `coding-agents` `go` | 1 | 🔄 2026-08-21 |
| [**herdr-agent-team**](https://github.com/gdli6177/herdr-agent-team)<br><sub>gdli6177</sub> | A Herdr plugin for Markdown-defined agent teams | `javascript` | 1 | 2026-08-16 |
| [**herdr-prompt-bucket**](https://github.com/GNURub/herdr-prompt-bucket)<br><sub>GNURub</sub> | A durable, ordered prompt bucket for coding agents running in Herdr | `claude-code` `codex` `coding-agents` `opencode` `typescript` | 1 | 🔄 2026-08-19 |
| [**LunaCrab**](https://github.com/GranamyrBR/LunaCrab)<br><sub>GranamyrBR</sub> | Reserved for a separate project | `agents` `developer-tools` `multi-agent` `observability` `rust` | 1 | 2026-08-10 |
| [**🆕 agent-keep-awake**](https://github.com/happyeric77/agent-keep-awake)<br><sub>happyeric77</sub> | Prevent macOS sleep while Herdr agents are working | `javascript` | 1 | 2026-08-12 |
| [**herdr-dispatch**](https://github.com/husniadil/herdr-dispatch)<br><sub>husniadil</sub> | Dispatcher for the herdr-tasks board - a worker agent pane per ready task, the goal delivered, the worker tracked, and a stop at review, in one Go binary. | `agent-orchestration` `ai-agents` `dispatcher` `mcp-server` `go` | 1 | 🔄 2026-08-31 |
| [**herdr-annotations**](https://github.com/IgorWarzocha/herdr-annotations)<br><sub>IgorWarzocha</sub> | Collect annotations on terminal selections and stage them into Herdr agents | `ai-agents` `annotations` `terminal` `javascript` | 1 | 2026-07-18 |
| [**herdr-plan-approve**](https://github.com/jerryfane/herdr-plan-approve)<br><sub>jerryfane</sub> | Auto-approve Claude Code plan-mode dialogs in herdr — agents plan, then execute, without a keypress. | `claude-code` `shell` | 1 | 🔄 2026-08-25 |
| [**corral**](https://github.com/jirathip-dev/corral)<br><sub>jirathip-dev</sub> | See every agent. Steer the fleet. | `agent-orchestration` `ai-agents` `coding-agents` `control-plane` `devtools` | 1 | 🔄 2026-09-02 |
| [**herdr-watcher**](https://github.com/joshka0/herdr-watcher)<br><sub>joshka0</sub> | Durable continuations and detached worker callbacks for Herdr agents | `rust` | 1 | 2026-08-02 |
| [**herdr-turn-coordinator**](https://github.com/KarthusLorin/herdr-turn-coordinator)<br><sub>KarthusLorin</sub> | Preserve interactive Herdr agent TUIs without model-driven status polling | `ai-agents` `python` | 1 | 🔄 2026-09-02 |
| [**herdr-island**](https://github.com/kay-ws/herdr-island)<br><sub>kay-ws</sub> | Find the agents that are waiting on you — shows why each herdr agent stopped, and filters the Agents panel down to just those. | `shell` | 1 | 2026-08-04 |
| [**herdr-link**](https://github.com/LZHcode1986/herdr-link)<br><sub>LZHcode1986</sub> | Faster, token-efficient, and zero-reasoning cross-agent interoperability for Herdr sessions. Replaces heavyweight skills with a unified contract for peer disco… | `typescript` | 1 | 🔄 2026-09-01 |
| [**sheprd**](https://github.com/m-mohamed/sheprd)<br><sub>m-mohamed</sub> | Keep Pi, Codex, Claude Code, and OpenCode in one visible, isolated Herdr Flok. | `agent-tools` `claude-code` `cli` `codex` `coding-agents` | 1 | 🔄 2026-08-25 |
| [**herdr-agents-preview**](https://github.com/maedana/herdr-agents-preview)<br><sub>maedana</sub> | Multi-agent terminal preview dashboard for Herdr: all running agents shown at once, with the selected agent taking most of the width. | `rust` | 1 | 2026-08-14 |
| [**herdr-standup**](https://github.com/natori-hrj/herdr-standup)<br><sub>natori-hrj</sub> | Agent standup for herdr — a per-agent digest of commits and uncommitted work across your agents' repos. | `ai-agents` `git` `standup` `rust` | 1 | 2026-07-23 |
| [**🆕 herdr-replay**](https://github.com/neospeed83/herdr-replay)<br><sub>neospeed83</sub> | Record and replay multi-agent Herdr coding sessions as interactive timelines. | `ai-agents` `developer-tools` `terminal-recording` `rust` | 1 | 🔄 2026-08-29 |
| [**🆕 herdr-tournament**](https://github.com/neospeed83/herdr-tournament)<br><sub>neospeed83</sub> | Adversarial multi-agent code reviews for Herdr | `rust` | 1 | 🔄 2026-08-29 |
| [**herdr-caffeinate**](https://github.com/nwarwick/herdr-caffeinate)<br><sub>nwarwick</sub> | Prevent macOS system sleep while Herdr agents are working | `caffeinate` `coding-agents` `macos` `shell` | 1 | 2026-07-29 |
| [**herdr-spawn**](https://github.com/nytafar/herdr-spawn)<br><sub>nytafar</sub> | One MCP tool that hands a prompt from a chat to a real Claude Code session on one of your hosts, with Remote Control on. | `python` | 1 | 🔄 2026-08-21 |
| [**herdr-imebox**](https://github.com/Sawakee/herdr-imebox)<br><sub>Sawakee</sub> | IME-friendly pop-up text box for typing Japanese/CJK into AI agent panes in herdr | `cjk` `ime` `input-method` `japanese` `ratatui` | 1 | 2026-07-17 |
| [**🆕 herdr-awake**](https://github.com/susomejias/herdr-awake)<br><sub>susomejias</sub> | Herdr plugin: keep the machine awake while Herdr agents are busy | `shell` | 1 | 🔄 2026-08-26 |
| [**herdr-traex**](https://github.com/szrenwei/herdr-traex)<br><sub>szrenwei</sub> | Herdr Marketplace integration for TraeX agent lifecycle and metadata | `traex` `python` | 1 | 2026-08-04 |
| [**herdr-orc**](https://github.com/tamdogood/herdr-orc)<br><sub>tamdogood</sub> | A minimal, profile-driven custom orchestrator for Herdr | `ai-agents` `multi-agent` `orchestrator` `javascript` | 1 | 2026-08-11 |
| [**tinysend-herdr**](https://github.com/tiny-send/tinysend-herdr)<br><sub>tiny-send</sub> | herdr plugin: email yourself when an agent blocks/finishes, reply to unblock it. Powered by tinysend. | `ai-agents` `tinysend` `javascript` | 1 | 2026-06-26 |
| [**🆕 herdr-rovo-dev**](https://github.com/usrivastava92/herdr-rovo-dev)<br><sub>usrivastava92</sub> | Herdr plugin that detects Rovo Dev CLI sessions and reports them as live agents in Herdr | `ai-agent` `rovo` `rovo-dev` `shell` | 1 | 2026-07-19 |
| [**herdr-polyglot**](https://github.com/wazum/herdr-polyglot)<br><sub>wazum</sub> | Write coding-agent prompts in your own language — DeepL or Google Cloud Translate translates them to English and delivers them into Claude Code, Codex or any h… | `ai-agents` `bubbletea` `bubbletea-tui` `claude-code` `codex` | 1 | 🔄 2026-09-01 |
| [**herdr-auto-yes-sir**](https://github.com/xlinx/herdr-auto-yes-sir)<br><sub>xlinx</sub> | herdr-auto-yes-sir for non blocked running when agent ask for approve; like codex. | `javascript` | 1 | 🔄 2026-08-20 |
| [**herdr-cadence**](https://github.com/zhenyufu/herdr-cadence)<br><sub>zhenyufu</sub> | Light agent orchestrator with one Lead and a fleet of agents | `rust` | 1 | 🔄 2026-08-25 |
| [**herdr-simple-prompts**](https://github.com/AlexSamarsky/herdr-simple-prompts)<br><sub>AlexSamarsky</sub> | Only your prompts and the final answers from Codex or Claude, with a working composer | `rust` | 0 | 🔄 2026-08-31 |
| [**🆕 herdr-dynamic-workflow**](https://github.com/andthezhang/herdr-dynamic-workflow)<br><sub>andthezhang</sub> | JavaScript workflows for orchestrating coding-agent CLIs in Herdr. | `agent-fleet` `agent-orchestration` `agent-swarm` `agentic-ai` `agents` | 0 | 🔄 2026-08-30 |
| [**🆕 unblock**](https://github.com/aneym/unblock)<br><sub>aneym</sub> | One queue for everything your agents need from you. Blockers need an action, grills need a judgement; secrets never enter the model's context. | `agents` `human-in-the-loop` `mcp` `javascript` | 0 | 🔄 2026-08-28 |
| [**hird**](https://github.com/aoprisan/hird)<br><sub>aoprisan</sub> | Cross-harness agent work queue and shared assertion memory, backed by one local SQLite database | `ai-agents` `claude-code` `cli` `mcp` `rust` | 0 | 🔄 2026-08-22 |
| [**🆕 herdr-quick-prompt**](https://github.com/astwys/herdr-quick-prompt)<br><sub>astwys</sub> | A Herdr plugin to send predefined prompts to an agent pane | `shell` | 0 | 🔄 2026-08-24 |
| [**otito-herdr-plugin**](https://github.com/BASHBOP/otito-herdr-plugin)<br><sub>BASHBOP</sub> | Run Otito context and deterministic merge evidence inside Herdr agent workspaces. | `ai-agents` `developer-tools` `merge-safety` `otito` `javascript` | 0 | 🔄 2026-08-21 |
| [**herdr-agent-manager**](https://github.com/bleedingfight/herdr-agent-manager)<br><sub>bleedingfight</sub> | 一个基于fzf的模糊搜索workspace、tab、pane、agent工具 | `python` | 0 | 🔄 2026-08-27 |
| [**herdr-warp**](https://github.com/cdpath/herdr-warp)<br><sub>cdpath</sub> | Herdr plugin that drives the interactive Warp Agent CLI (warp) in Herdr panes: open/send/status/wait/read/approve/deny/new/stop/exit, with screen-scraped idle/… | `shell` | 0 | 2026-08-13 |
| [**clawsouls-herdr-plugin**](https://github.com/clawsouls/clawsouls-herdr-plugin)<br><sub>clawsouls</sub> | _(no description)_ | `ai-agents` `persona` `shell` | 0 | 2026-08-11 |
| [**herdr-tuple-plugin**](https://github.com/doggyfish/herdr-tuple-plugin)<br><sub>doggyfish</sub> | A herdr plugin that pairs two coding agents side by side in one tab and moves text between them | `javascript` | 0 | 2026-08-08 |
| [**herdr-chat**](https://github.com/eliasstravik/herdr-chat)<br><sub>eliasstravik</sub> | A live structured chat view for agents running inside Herdr. | `typescript` | 0 | 🔄 2026-08-24 |
| [**herdr-nudge**](https://github.com/EricBois/herdr-nudge)<br><sub>EricBois</sub> | Arm a continue-nudge on a herdr agent — fire at a set time, or when it goes idle/blocked | `shell` | 0 | 2026-07-17 |
| [**herdr-cursor**](https://github.com/gabriel-laet/herdr-cursor)<br><sub>gabriel-laet</sub> | Cursor cloud agents as first-class herdr panes | `typescript` | 0 | 🔄 2026-08-21 |
| [**ezdras-herdr**](https://github.com/GranamyrBR/ezdras-herdr)<br><sub>GranamyrBR</sub> | Live multi-agent observability and pane controls for Herdr | `rust` | 0 | 2026-08-10 |
| [**herdr-mail**](https://github.com/husniadil/herdr-mail)<br><sub>husniadil</sub> | Async mail between coding agents on Herdr - a store-authoritative mailbox, a one-line pane marker as the hint, and ask/reply with a tracked obligation, in one… | `ai-agents` `mail` `mcp-server` `sqlite` `go` | 0 | 🔄 2026-08-30 |
| [**herdr-ai-memory**](https://github.com/iagogfe/herdr-ai-memory)<br><sub>iagogfe</sub> | Herdr plugin: launch coding agents through ai-memory managed workstreams - cross-agent session continuity | `ai-agents` `ai-memory` `terminal` `javascript` | 0 | 2026-07-24 |
| [**herdr-pane-id**](https://github.com/imtim/herdr-pane-id)<br><sub>imtim</sub> | herdr plugin: label panes with their ID and agent name, plus tab and workspace id labels — so you and your agents can address any pane or agent by id. Works be… | `ai-agents` `coding-agents` `developer-tools` `terminal-multiplexer` `tui` | 0 | 🔄 2026-08-24 |
| [**herdr-spawn**](https://github.com/JLighter/herdr-spawn)<br><sub>JLighter</sub> | Herdr plugin: launch a coding agent with a prompt — one git worktree per agent | `shell` | 0 | 2026-08-03 |
| [**herdr-suffix-agent-filter**](https://github.com/kazimshah39/herdr-suffix-agent-filter)<br><sub>kazimshah39</sub> | Toggle Herdr’s Agents sidebar between exact Space-suffix groups and the default view. | `coding-agents` `developer-tools` `terminal` `javascript` | 0 | 🔄 2026-08-27 |
| [**herdr-kit**](https://github.com/kevinWangSheng/herdr-kit)<br><sub>kevinWangSheng</sub> | Declarative layouts, an event watcher, plugins and a socket client for Herdr — the parts the herdr CLI does not expose | `coding-agents` `terminal-multiplexer` `python` | 0 | 2026-08-14 |
| [**led-agent-status**](https://github.com/lfsmoura/led-agent-status)<br><sub>lfsmoura</sub> | herdr plugin: show your AI agents' status on a BLE LED strip — blue working, blinking red blocked, green done | `ble` `led` `swift` | 0 | 2026-08-10 |
| [**herdr-claude-launcher**](https://github.com/lucasleon2107/herdr-claude-launcher)<br><sub>lucasleon2107</sub> | herdr plugin: open a new tab with Claude Code already running | `ai-agents` `claude-code` `terminal` `tmux` `shell` | 0 | 2026-08-03 |
| [**herdr-alias-setter**](https://github.com/m2selfA/herdr-alias-setter)<br><sub>m2selfA</sub> | Herdr plugin: set pane name + agent alias (quick type-in or full menu) | `powershell` | 0 | 🔄 2026-08-21 |
| [**quickTUI**](https://github.com/marcjfj-vmlyr/quickTUI)<br><sub>marcjfj-vmlyr</sub> | Snap-together primitives for building terminal UIs fast, on top of OpenTUI. Ships as a Herdr plugin that gives coding agents the /quicktui skill. | `bun` `opentui` `terminal` `tui` `typescript` | 0 | 2026-08-13 |
| [**herdr-agent-dash**](https://github.com/MartinBspheroid/herdr-agent-dash)<br><sub>MartinBspheroid</sub> | Herdr Agent Board: a local, keyboard-first plugin for scanning active coding agents, their state, working directory, and Git context at a glance. | `typescript` | 0 | 2026-07-21 |
| [**herdr-green**](https://github.com/natori-hrj/herdr-green)<br><sub>natori-hrj</sub> | Per-agent test status for herdr — run a project's tests when its agent finishes and show pass/fail. | `ai-agents` `ci` `tests` `rust` | 0 | 2026-07-23 |
| [**agentic-box**](https://github.com/nicoRomeroCuruchet/agentic-box)<br><sub>nicoRomeroCuruchet</sub> | An isolated box where Claude Code drives local model agents. | `agent-orchestration` `agentic` `agentic-workflow` `docker` `ornith-1-0-35b` | 0 | 2026-08-17 |
| [**herdr-plugin-aos**](https://github.com/noctaIO/herdr-plugin-aos)<br><sub>noctaIO</sub> | Spawn Agentic OS-enabled Claude Code agents in a herdr pane from any workspace. Non-invasive herdr plugin. | `shell` | 0 | 2026-07-11 |
| [**herdr-prompts**](https://github.com/oppenheimor/herdr-prompts)<br><sub>oppenheimor</sub> | Save, search, fill, and reuse prompt templates across coding agents in Herdr. Inspired by my friend: bingguanqi | `typescript` | 0 | 🔄 2026-08-19 |
| [**🆕 herd**](https://github.com/orrgal1/herd)<br><sub>orrgal1</sub> | Issue-driven multi-agent setup for omp on herdr: a lead that files issues, workers that poll, claim, and ship them | `shell` | 0 | 🔄 2026-09-01 |
| [**herdr-sidekick**](https://github.com/qapquiz/herdr-sidekick)<br><sub>qapquiz</sub> | Toggleable sidekick AI-agent pane for Herdr — paste code selections into the agent's composer without submitting. Pairs with qapquiz/herdr-sidekick.nvim. | `neovim` `terminal` `shell` | 0 | 2026-08-15 |
| [**ocean-herdr**](https://github.com/Risingtides-dev/ocean-herdr)<br><sub>Risingtides-dev</sub> | Ocean agent integration for Herdr | `coding-agent` `ocean` `rust` | 0 | 2026-07-17 |
| [**herdr-want-to-sleep**](https://github.com/scheron/herdr-want-to-sleep)<br><sub>scheron</sub> | A herdr plugin that puts your Mac to sleep once no coding agent is working any more. Arm it before bed and it waits for every agent to settle, then journals wh… | `coding-agents` `macos` `shell` | 0 | 2026-07-28 |
| [**herdr-achievements**](https://github.com/SerHappy/herdr-achievements)<br><sub>SerHappy</sub> | Achievements and tiny celebrations for your Herdr AI agent herd | `achievements` `ai-agents` `developer-tools` `gamification` `go` | 0 | 2026-07-30 |
| [**herdr-ask**](https://github.com/TaylorFinklea/herdr-ask)<br><sub>TaylorFinklea</sub> | Lightweight command generation and terminal chat for Herdr and any terminal | `cli` `rust` `terminal` `tui` | 0 | 2026-07-21 |
| [**herdr-restart-always**](https://github.com/terafin/herdr-restart-always)<br><sub>terafin</sub> | Supervise herdr agent panes and always restart whatever the pane is running (claude, hermes, codex, pi, opencode, ...) whenever the agent dies. | `python` | 0 | 2026-08-15 |
| [**herdr-group-chat**](https://github.com/terry-li-hm/herdr-group-chat)<br><sub>terry-li-hm</sub> | A shared local Herdr room for Pi, Claude Code, Codex, and Grok Build. | `ai-agents` `claude-code` `codex` `grok` `multi-agent` | 0 | 🔄 2026-08-31 |
| [**herdr-cline-plugin**](https://github.com/TheMetalStorm/herdr-cline-plugin)<br><sub>TheMetalStorm</sub> | Herdr plugin that makes a plain Cline CLI launched from any pane look like a native Herdr agent. | `cli` `cline` `herdr-integration` `shell` | 0 | 2026-07-31 |
| [**🆕 herdr-cmd-agent-plugin**](https://github.com/thesimonharms/herdr-cmd-agent-plugin)<br><sub>thesimonharms</sub> | Herdr plugin to recognize CommandCode (cmd) as an agent — idle/working/blocked detection via screen manifest + cmd mod | `cmd` `commandcode` `shell` | 0 | 🔄 2026-08-31 |
| [**herdr-agent-notes**](https://github.com/timjonez/herdr-agent-notes)<br><sub>timjonez</sub> | Herdr plugin: sticky notes on agents so you can see why one is idle. | `python` | 0 | 🔄 2026-08-20 |
| [**herdr-agent-topic**](https://github.com/wynemo/herdr-agent-topic)<br><sub>wynemo</sub> | Herdr plugin: show your latest user prompt in each agent card | `go` | 0 | 🔄 2026-08-20 |
| [**🆕 cbds**](https://github.com/zqkra/cbds)<br><sub>zqkra</sub> | Reliable multi-agent orchestration for the Herdr herd. Durable tasks, authoritative worker reports, and a wait that cannot hang. | `agents` `cli` `multi-agent` `orchestration` `javascript` | 0 | 🔄 2026-08-31 |

<details><summary>Also relevant to this purpose</summary>

- [AltanS/collie](https://github.com/AltanS/collie) — PWA to manage 🐑 herdr on the go. Tailnet accessible, push notifications, quick actions and more.
- [a2u/herdr-jira](https://github.com/a2u/herdr-jira) — Jira TUI plugin for herdr — browse issues with configurable JQL filters, search, change statuses, and delegat…
- [walcew/herdr-assist](https://github.com/walcew/herdr-assist) — Physical desk panel for Herdr, the terminal multiplexer for AI coding agents — shows session state in color a…
- [e2b-dev/herdr-e2b-sandbox](https://github.com/e2b-dev/herdr-e2b-sandbox) — herdr plugin that mirrors a git worktree into an E2B sandbox — one box or a branch-per-agent fleet, with a TU…
- [miko-misa/herdr-portfwd](https://github.com/miko-misa/herdr-portfwd) — Automatic SSH port forwarding for coding agents on remote machines: Ctrl+click the localhost URL your agent p…
- [JefeLabs/herdr-web-broker](https://github.com/JefeLabs/herdr-web-broker) — Self-hosted REST/WS API for herdr: spawn and steer coding agents from anywhere — tokens, multi-user session o…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-worktree"></a>

## Git Worktrees & Branches

> I want to spin up a worktree for each piece of work, and have the cleanup handled automatically too

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-worktrunk**](https://github.com/devashish2203/herdr-worktrunk)<br><sub>devashish2203</sub> | Herdr Plugin to integrate worktrunk for git worktree management | `shell` | 119 | 🔄 2026-08-27 |
| [**herdr-plugin-jj-workspace**](https://github.com/NathanFlurry/herdr-plugin-jj-workspace)<br><sub>NathanFlurry</sub> | Create and remove Jujutsu (jj) workspaces as Herdr workspaces | `jujutsu` `rust` | 47 | 🔄 2026-09-02 |
| [**herdkit**](https://github.com/briankeegan1/herdkit)<br><sub>briankeegan1</sub> | Governance and parallelism for herdr-based agent workflows — a coordinator drains your backlog into isolated worktree builders (Claude Code, Codex, Grok, or Cu… | `shell` | 12 | 🔄 2026-09-02 |
| [**herdr-plugin-renamer**](https://github.com/wyattjoh/herdr-plugin-renamer)<br><sub>wyattjoh</sub> | Renames an auto-generated herdr worktree branch and workspace from the agent's first prompt, via on-device Apple FoundationModels or Codex. | `rust` | 11 | 2026-08-17 |
| [**jj-waltz**](https://github.com/EzraCerpac/jj-waltz)<br><sub>EzraCerpac</sub> | A Jujutsu workspace switcher inspired by Worktrunk | `cli` `jj` `jujitsu` `utility` `workspace` | 7 | 🔄 2026-08-21 |
| [**herdr-e2b-sandbox**](https://github.com/e2b-dev/herdr-e2b-sandbox)<br><sub>e2b-dev</sub> | herdr plugin that mirrors a git worktree into an E2B sandbox — one box or a branch-per-agent fleet, with a TUI dashboard | `cli` `cloud-dev` `e2b` `git-worktree` `sandbox` | 6 | 🔄 2026-08-29 |
| [**herdr-plugin-git-worktree-hooks**](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks)<br><sub>freethinkel</sub> | Run shell commands when a git worktree is created/removed — one YAML config for all projects, living outside any repo. | `git-worktree` `javascript` | 6 | 2026-07-06 |
| [**herdr-worktree-from-pr**](https://github.com/tdi/herdr-worktree-from-pr)<br><sub>tdi</sub> | Create a git worktree from a GitHub PR and open it as a herdr workspace | `javascript` | 6 | 2026-07-20 |
| [**herdr-worktree-seed**](https://github.com/jlimas/herdr-worktree-seed)<br><sub>jlimas</sub> | Herdr plugin that seeds new worktrees with copy-on-write node_modules and configurable local dotfiles | `developer-tools` `dotfiles` `git-worktree` `nodejs` `typescript` | 5 | 2026-07-28 |
| [**herdr-symlink-worktree**](https://github.com/hmu332233/herdr-symlink-worktree)<br><sub>hmu332233</sub> | A herdr plugin that symlinks shared local files from your main repo into new worktrees. | `shell` | 4 | 2026-07-16 |
| [**herdr-fresh-worktree**](https://github.com/persiyanov/herdr-fresh-worktree)<br><sub>persiyanov</sub> | Reset a newly created herdr worktree to the latest origin default branch. | `javascript` | 4 | 2026-06-25 |
| [**herdr-worktreeinclude**](https://github.com/tanshio/herdr-worktreeinclude)<br><sub>tanshio</sub> | Herdr plugin: copy gitignored files matching .worktreeinclude into newly created worktrees | `worktree` `worktreeiclude` `shell` | 4 | 2026-07-11 |
| [**herdr-worktree-hooks**](https://github.com/timofey-TK/herdr-worktree-hooks)<br><sub>timofey-TK</sub> | herdr plugin: run custom setup/teardown commands when a git worktree is created, opened, or removed | `developer-tools` `git-worktree` `worktree` `python` | 4 | 2026-07-17 |
| [**herdr-remote-worktrunk**](https://github.com/ditwrd/herdr-remote-worktrunk)<br><sub>ditwrd</sub> | Herdr remote worktrunk workspace | `shell` | 3 | 2026-07-10 |
| [**herdr-branch-cleanup**](https://github.com/osolmaz/herdr-branch-cleanup)<br><sub>osolmaz</sub> | Checkout the default branch when a pane's branch is merged or deleted on GitHub | `git` `github` `rust` | 3 | 2026-07-26 |
| [**herdr-worktree-lifecycle**](https://github.com/qdentity/herdr-worktree-lifecycle)<br><sub>qdentity</sub> | Herdr plugin: dispatch worktree lifecycle events to repo-owned setup/teardown wrappers | `rust` | 3 | 2026-06-29 |
| [**herdr-multirepo**](https://github.com/jattento/herdr-multirepo)<br><sub>jattento</sub> | One feature branch across many repositories, in one Herdr workspace | `git-worktree` `python` | 2 | 2026-08-03 |
| [**herdr-shear**](https://github.com/moneycaringcoder/herdr-shear)<br><sub>moneycaringcoder</sub> | Find the git worktrees that are safe to delete, and delete those. A worktree janitor for herdr. | `cleanup` `git-worktree` `rust` `terminal` | 2 | 🔄 2026-09-01 |
| [**herdr-jj-status**](https://github.com/mroth/herdr-jj-status)<br><sub>mroth</sub> | herdr plugin: show the Jujutsu bookmark/status for jj workspaces in the spaces sidebar | `shell` | 2 | 2026-07-28 |
| [**herdr-jj**](https://github.com/OliverGilan/herdr-jj)<br><sub>OliverGilan</sub> | Jujutsu workspace support for Herdr | `jujutsu` `rust` | 2 | 2026-08-12 |
| [**herdr-worktreeinclude**](https://github.com/serhii-chernenko/herdr-worktreeinclude)<br><sub>serhii-chernenko</sub> | Allow custom path for new worktrees and respects `.worktreeinclude` file like Claude CLI does | `worktree` `shell` | 2 | 2026-07-23 |
| [**herdr-corral**](https://github.com/bfreed/herdr-corral)<br><sub>bfreed</sub> | Herd your Git worktrees in Herdr: env files, dependencies, agent/shell/server tabs, and merge-safe cleanup. A workmux replacement for Herdr. | `git-worktree` `workmux` `python` | 1 | 2026-08-14 |
| [**herdr-worktree-copy**](https://github.com/crexi/herdr-worktree-copy)<br><sub>crexi</sub> | Herdr plugin that copies and symlinks worktree-local files from a .worktree-copy manifest | `git-worktree` `shell` | 1 | 2026-07-28 |
| [**herdr-deck**](https://github.com/ctbaum/herdr-deck)<br><sub>ctbaum</sub> | The companion workspace launcher for herdr-agents.nvim: open or resume Claude and Codex in a ready-made Neovim, agent, shell, and lazygit deck. | `claude-code` `codex` `coding-agents` `git-worktree` `neovim` | 1 | 🔄 2026-08-24 |
| [**🆕 herdr-composer**](https://github.com/danieljvdm/herdr-composer)<br><sub>danieljvdm</sub> | Compose tasks, attach context, and launch coding agents in isolated Herdr workspaces | `coding-agents` `git-worktree` `rust` | 1 | 🔄 2026-09-01 |
| [**trunkr**](https://github.com/disintegrator/trunkr)<br><sub>disintegrator</sub> | Herdr 🤝 Worktrunk | `go` | 1 | 2026-08-12 |
| [**herdr-allow**](https://github.com/Feasy01/herdr-allow)<br><sub>Feasy01</sub> | herdr plugin: copy gitignored files (.env, secrets, local configs) into every new worktree via a .herdr-allow allowlist | `shell` | 1 | 2026-07-02 |
| [**herdr-plugin-gwm**](https://github.com/kbrdn1/herdr-plugin-gwm)<br><sub>kbrdn1</sub> | herdr plugin that drives gwm for git worktree management — gwm stays the source of truth, herdr adopts. | `bash` `cli` `git-worktree` `gwm` `worktree` | 1 | 2026-07-27 |
| [**herdr-collide**](https://github.com/moneycaringcoder/herdr-collide)<br><sub>moneycaringcoder</sub> | Warns when agents working in different git worktrees of one repo are about to collide — and whether their edits merely overlap or will actually conflict. | `conflict-detection` `git-worktree` `rust` `terminal` | 1 | 🔄 2026-09-01 |
| [**herdr-standup**](https://github.com/moneycaringcoder/herdr-standup)<br><sub>moneycaringcoder</sub> | A digest of what your agents actually did. One command, one readable summary of every Herdr workspace over a time window — commits, change volume, branch, and… | `git` `rust` `standup` `terminal` | 1 | 🔄 2026-09-01 |
| [**herdr-worktree-nav**](https://github.com/ShoMasegi/herdr-worktree-nav)<br><sub>ShoMasegi</sub> | _(no description)_ | `terminal` `rust` | 1 | 🔄 2026-08-23 |
| [**herdr-plugin-pr-board**](https://github.com/0xthc/herdr-plugin-pr-board)<br><sub>0xthc</sub> | GitHub PRs for the current repo inside herdr: browse them in a pane, check one out as a worktree workspace, and safely collect merged ones. | `shell` | 0 | 🔄 2026-08-20 |
| [**herdr-plugin-worktree-bootstrap**](https://github.com/0xthc/herdr-plugin-worktree-bootstrap)<br><sub>0xthc</sub> | Seed new herdr worktrees with .env files and node_modules the moment they open | `shell` | 0 | 🔄 2026-08-22 |
| [**herdr**](https://github.com/AgentTeamsRun/herdr)<br><sub>AgentTeamsRun</sub> | Report herdr worktree lifecycle events to the AgentTeams registry | — | 0 | 🔄 2026-08-19 |
| [**herdr-worktree-provisioner**](https://github.com/arjenblokzijl/herdr-worktree-provisioner)<br><sub>arjenblokzijl</sub> | Runs per-repo setup in a new worktree's own visible pane — composable and guard-free. | `bootstrap` `git-worktree` `worktree` `shell` | 0 | 2026-07-08 |
| [**🆕 herdr-plugin-env-sync**](https://github.com/DecampsRenan/herdr-plugin-env-sync)<br><sub>DecampsRenan</sub> | Herdr plugins: env-sync sets up new Git worktrees (.env copy, remote branch tracking, setup commands) with a live status panel | `developer-tools` `git-worktree` `shell` | 0 | 🔄 2026-08-28 |
| [**herdr-worktreeinclude**](https://github.com/eightHundreds/herdr-worktreeinclude)<br><sub>eightHundreds</sub> | Herdr plugin: copy .worktreeinclude-selected gitignored files into new worktrees | `worktree` `rust` | 0 | 2026-07-28 |
| [**herdr-title**](https://github.com/filoozom/herdr-title)<br><sub>filoozom</sub> | A Herdr plugin that shows the selected worktree and agent activity in your terminal tab title. | `rust` | 0 | 2026-07-24 |
| [**herdr-hub-worktrees**](https://github.com/klukacin/herdr-hub-worktrees)<br><sub>klukacin</sub> | Herdr plugin: mirror a hub worktree into every nested sub-repo clone | `git-worktree` `monorepo` `terminal-multiplexer` `shell` | 0 | 2026-08-12 |
| [**gren-herdr**](https://github.com/langtind/gren-herdr)<br><sub>langtind</sub> | A herdr plugin for creating, switching, and removing git worktrees via gren — with gren's post-create setup. | `git-worktree` `gren` `shell` | 0 | 🔄 2026-09-01 |
| [**herdr-worktree-hooks-plugin**](https://github.com/m1sk9/herdr-worktree-hooks-plugin)<br><sub>m1sk9</sub> | A plugin that adds customizable hooks to Herdr's Worktree | `rust` | 0 | 🔄 2026-09-01 |
| [**herdr-worktree-include**](https://github.com/scoussens-nthplusio/herdr-worktree-include)<br><sub>scoussens-nthplusio</sub> | Copy gitignored files such as .env into new Herdr worktrees, using the repository's .worktreeinclude — the same file and rules Claude Code uses. | `dotenv` `git-worktree` `shell` | 0 | 🔄 2026-08-27 |
| [**herdr-jira-worktree**](https://github.com/spiritsack/herdr-jira-worktree)<br><sub>spiritsack</sub> | herdr plugin: prompt for a Jira ticket, open/reuse a matching git worktree, and prefill it into a fresh Claude Code session | `shell` | 0 | 🔄 2026-08-24 |
| [**🆕 herdr-worktree-guard**](https://github.com/takeaship/herdr-worktree-guard)<br><sub>takeaship</sub> | A safety-focused Herdr plugin for tracking and cleaning up agent worktrees | `coding-agents` `git-worktree` | 0 | 🔄 2026-08-30 |
| [**herdr-worktree**](https://github.com/tjg184/herdr-worktree)<br><sub>tjg184</sub> | Herdr worktree plugin that works with worktrunk and native worktrees | `rust` | 0 | 2026-08-13 |
| [**🆕 herdr-coder-sessions**](https://github.com/ubuntudroid/herdr-coder-sessions)<br><sub>ubuntudroid</sub> | Browse running Coder agent sessions in herdr and open each as its own workspace: agentty on the session, its changes mirrored into a local worktree for review | `agentapi` `coder` `coding-agents` `python` | 0 | 🔄 2026-09-01 |
| [**🆕 herdr-git-stack**](https://github.com/ubuntudroid/herdr-git-stack)<br><sub>ubuntudroid</sub> | Herdr plugin: shows each space's position in its git branch stack in the spaces sidebar, flags branches whose parent has moved, and keeps stacks contiguous. Lo… | `bash` `developer-tools` `git` `stacked-branches` `shell` | 0 | 🔄 2026-08-29 |
| [**herdr-plugin-worktree-bootstrap**](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap)<br><sub>zerodice0</sub> | Safely copy ignored local files and run setup commands in new Herdr Git worktrees | `python` | 0 | 2026-08-03 |

<details><summary>Also relevant to this purpose</summary>

- [tdi/herdr-worktree-from-linear](https://github.com/tdi/herdr-worktree-from-linear) — Create a git worktree from a Linear issue and open it as a herdr workspace
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — Automatically bootstrap Herdr worktrees for JavaScript and TypeScript with lockfile-aware installs and safe e…
- [tomasvarga/herdr-e2b](https://github.com/tomasvarga/herdr-e2b) — Mirror a git worktree into a fresh E2B cloud sandbox on demand — a snapshot upload (uncommitted changes and a…
- [JLighter/herdr-spawn](https://github.com/JLighter/herdr-spawn) — Herdr plugin: launch a coding agent with a prompt — one git worktree per agent
- [jtnovellis/herdr-worktree-setup](https://github.com/jtnovellis/herdr-worktree-setup) — herdr plugin: make a new git worktree immediately usable — copy .env & dev state, clone dependency caches (AP…
- [snics/herdr-worktree-from-gitlab](https://github.com/snics/herdr-worktree-from-gitlab) — herdr plugin: create a git worktree + workspace from a GitLab issue (via glab)
- [untalfranfernandez/herdr-worktreeinclude](https://github.com/untalfranfernandez/herdr-worktreeinclude) — Herdr plugin that populates every new git worktree with the gitignored local files it needs — .env, settings.…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-review"></a>

## Code Review & Diffs

> I want to read the diff an agent wrote and send comments back on it

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**crabbox**](https://github.com/openclaw/crabbox)<br><sub>openclaw</sub> | Crabbox: warm a box, sync the diff, run the suite. | `agent-skills` `remote-test-runner` `go` | 1353 | 🔄 2026-09-02 |
| [**herdr-reviewr**](https://github.com/persiyanov/herdr-reviewr)<br><sub>persiyanov</sub> | A code-review + file-viewer sidebar for herdr — comment on an agent's diff, send it back. Plus a read-only view of the PR, its checks, and comments. | `code-review` `rust` `tui` | 577 | 🔄 2026-08-29 |
| [**🆕 herdr-annotate**](https://github.com/plannotator/herdr-annotate)<br><sub>plannotator</sub> | Annotate terminal text, review documents and agent replies in Herdr, and send the feedback straight back to the agent. | `annotation` `multiplexer` `rust` | 311 | 🔄 2026-08-31 |
| [**herdr-hunk-diff**](https://github.com/jhochenbaum/herdr-hunk-diff)<br><sub>jhochenbaum</sub> | Review agent-authored changes in hunk from herdr and send inline comments back to the responsible agent. | `code-review` `hunk` `typescript` | 102 | 🔄 2026-08-26 |
| [**herdr-plannotator**](https://github.com/plannotator/herdr-plannotator)<br><sub>plannotator</sub> | Open Plannotator reviews inside Herdr Browser panes. | `plannotator` `typescript` | 20 | 2026-07-29 |
| [**herdr-plugin-hunk**](https://github.com/edmundmiller/herdr-plugin-hunk)<br><sub>edmundmiller</sub> | Herdr plugin for opening Hunk diffs in split panes or tabs | `python` | 15 | 2026-06-23 |
| [**herdr-pickr**](https://github.com/tomasvarga/herdr-pickr)<br><sub>tomasvarga</sub> | A PR review router for herdr — Ctrl+click a GitHub PR / GitLab MR link and pick a reviewer (tuicr · hunk · diff · browser · or your own tool), with an optional… | `cli` `code-review` `pull-request` `tui` `shell` | 14 | 2026-07-13 |
| [**herdr-gitview**](https://github.com/ChmaraX/herdr-gitview)<br><sub>ChmaraX</sub> | Git status/diff panel for herdr - review changes, edit in nvim, stage/commit/discard, all from the terminal | `git` `git-diff` `git-tui` `neovim` `rust` | 9 | 🔄 2026-09-01 |
| [**herdr-plugin-hunk-autodiff**](https://github.com/scott306lr/herdr-plugin-hunk-autodiff)<br><sub>scott306lr</sub> | Herdr plugin: auto-open a hunk diff split when a coding agent finishes with uncommitted changes | `claude-code` `hunk` `python` | 5 | 2026-07-05 |
| [**herdr-extensions**](https://github.com/vonzelle-vzt/herdr-extensions)<br><sub>vonzelle-vzt</sub> | Tiny VS Code for herdr: a real editor with LSP diagnostics, autocomplete, rename and go-to-definition — plus source control, search, problems, tests, a debugge… | `agent-tools` `autocomplete` `claude-code` `cli` `code-review` | 5 | 2026-08-03 |
| [**herdr-progressive-reviewer**](https://github.com/flupke/herdr-progressive-reviewer)<br><sub>flupke</sub> | Turns based diff reviewer inspired by Tidewave | `rust` | 3 | 🔄 2026-09-01 |
| [**herdr-review.nvim**](https://github.com/inferst/herdr-review.nvim)<br><sub>inferst</sub> | Code review UI for Neovim with Git and herdr integration | `lua` | 3 | 2026-08-01 |
| [**easy-review**](https://github.com/VilfredSikker/easy-review)<br><sub>VilfredSikker</sub> | Git diff review for AI-assisted coding. Terminal TUI and Tauri desktop app. | `ai-code-review` `cli` `code-review` `desktop-app` `developer-tools` | 3 | 🔄 2026-09-01 |
| [**herdr-pr-tracker**](https://github.com/jakekroon/herdr-pr-tracker)<br><sub>jakekroon</sub> | Every open pull request you have authored, docked and colour-coded by what needs you. A Herdr plugin. | `bun` `code-review` `developer-tools` `github` `pull-requests` | 2 | 🔄 2026-08-28 |
| [**herdr-scribe**](https://github.com/Javamomma/herdr-scribe)<br><sub>Javamomma</sub> | herdr plugin: live no-recording meeting transcription — mic → RAM-only transcript + live analyst panes; on stop: meeting note, optional policy gate, reviewable… | `macos` `meeting-notes` `privacy` `speech-to-text` `terminal` | 2 | 2026-08-07 |
| [**herdr-review**](https://github.com/quantk/herdr-review)<br><sub>quantk</sub> | Review agent-authored changes in Hunk and send inline feedback back through Herdr | `code-review` `hunk` `javascript` | 2 | 2026-07-28 |
| [**herdr-comments**](https://github.com/shadowfax92/herdr-comments)<br><sub>shadowfax92</sub> | Annotate copied Herdr terminal output, collect per-pane comments, and review them in Neovim. | `ai-agents` `annotations` `neovim` `rust` `terminal` | 2 | 🔄 2026-08-19 |
| [**herdr-hunk**](https://github.com/yuucu/herdr-hunk)<br><sub>yuucu</sub> | herdr plugin: toggle Hunk diff reviews for your agent workspaces | `diff` `hunk` `go` | 2 | 2026-07-20 |
| [**herdr-strays**](https://github.com/aleslanger/herdr-strays)<br><sub>aleslanger</sub> | Terminal UI for herding stray git worktrees — browse projects, see changed files live, read diffs, and prompt Claude without leaving the panel. | `rust` | 1 | 2026-08-12 |
| [**roboherd**](https://github.com/andschneider/roboherd)<br><sub>andschneider</sub> | roborev review status and actions inside your herdr workspace | `rust` `tui` | 1 | 🔄 2026-08-25 |
| [**herdr-agent-diff**](https://github.com/baotran01/herdr-agent-diff)<br><sub>baotran01</sub> | Herdr plugin for inspecting agent filesystem and Git diffs | `rust` | 1 | 2026-08-03 |
| [**herdr-stagr**](https://github.com/brianh20/herdr-stagr)<br><sub>brianh20</sub> | Source Control sidebar for herdr: stage, unstage, and discard with side-by-side diffs | `git` `tui` `rust` | 1 | 2026-08-06 |
| [**herdr-peer-review**](https://github.com/Elio2000/herdr-peer-review)<br><sub>Elio2000</sub> | Open a second coding agent in a herdr pane and have it review your diff — watchable, auto-approve, read-only. Ships a Claude Code skill for the autonomous revi… | `agent-skills` `ai-agents` `claude-code` `code-review` `codex` | 1 | 2026-07-16 |
| [**herdr-tasks**](https://github.com/husniadil/herdr-tasks)<br><sub>husniadil</sub> | Task backlog and notes board for coding agents on Herdr - claims with leases, evidence-backed review, and a human decision gate, in one Go binary. | `ai-agents` `mcp-server` `notes` `sqlite` `task-management` | 1 | 🔄 2026-08-30 |
| [**herdr-git-graph**](https://github.com/jorge-huxley/herdr-git-graph)<br><sub>jorge-huxley</sub> | Read-only git graph TUI plugin for Herdr with colored ASCII lanes, branch filter, search, and on-demand diffs. | `rust` | 1 | 2026-07-17 |
| [**agentflock**](https://github.com/neospark-sol/agentflock)<br><sub>neospark-sol</sub> | AI-coordinated builder and reviewer groups with durable milestone control | `ai-agents` `pair-programming` `typescript` | 1 | 🔄 2026-08-21 |
| [**herdr-hunk-viewer**](https://github.com/tareqmlx/herdr-hunk-viewer)<br><sub>tareqmlx</sub> | _(no description)_ | `code-review` `hunk` `rust` | 1 | 🔄 2026-08-21 |
| [**herdr-lazygit-viewer**](https://github.com/tareqmlx/herdr-lazygit-viewer)<br><sub>tareqmlx</sub> | Opens lazygit at the files, branches, commits, or stash panel, in whichever Herdr surface suits the moment. | `code-review` `lazygit` `rust` | 1 | 2026-08-14 |
| [**herdr-hunk-gh-diff**](https://github.com/Allianaab2m/herdr-hunk-gh-diff)<br><sub>Allianaab2m</sub> | Herdr plugin: open a Hunk diff between the branch checked out in the current pane and the target branch of its GitHub pull request. | `python` | 0 | 2026-07-15 |
| [**herdr-hunk**](https://github.com/cevr/herdr-hunk)<br><sub>cevr</sub> | Send Hunk review notes to the correct Herdr agent pane | `effect-ts` `hunk` `typescript` | 0 | 2026-07-28 |
| [**herdr-hunk**](https://github.com/goofansu/herdr-hunk)<br><sub>goofansu</sub> | Provides quick Herdr review actions that open a temporary Hunk overlay. Quitting Hunk closes the overlay and restores your workspace. | `python` | 0 | 🔄 2026-08-25 |
| [**herdr-implement-review**](https://github.com/Idan-Levin/herdr-implement-review)<br><sub>Idan-Levin</sub> | Herdr workflow for Codex implementation, security scanning, and mother-agent review | `claude-code` `codex` `security-review` `shell` | 0 | 2026-08-10 |
| [**herdr-plan-code-review**](https://github.com/inxx/herdr-plan-code-review)<br><sub>inxx</sub> | herdr plugin: Opus plans, Sonnet codes, Claude+Codex review — one action opens the four agent panes | `claude-code` `codex` `terminal` `shell` | 0 | 2026-07-06 |
| [**herdr-idle-panes**](https://github.com/leonho/herdr-idle-panes)<br><sub>leonho</sub> | herdr plugin: popup checklist to review and close panes sitting at an idle shell | `python` | 0 | 🔄 2026-08-22 |
| [**herdr-roborev**](https://github.com/phin-tech/herdr-roborev)<br><sub>phin-tech</sub> | Open roborev's review TUI in a Herdr pane | `shell` | 0 | 2026-07-21 |
| [**🆕 herdr-dia**](https://github.com/rewt/herdr-dia)<br><sub>rewt</sub> | Turn a GitHub PR you're reading in the Dia browser into a Herdr coding-agent review or update — from a side panel. | `ai-agents` `browser-extension` `code-review` `dia` `native-messaging` | 0 | 🔄 2026-09-02 |
| [**herdr-diff-review.nvim**](https://github.com/rytkmt/herdr-diff-review.nvim)<br><sub>rytkmt</sub> | Review AI agent file changes in Neovim diff mode before applying — approve or deny edits from Claude Code and Kiro CLI with a single command. AIエージェントのファイル変更をN… | `kiro-cli` `neovim` `neovim-plugin` `neovim-plugins` `nvim` | 0 | 🔄 2026-08-18 |
| [**🆕 lasso**](https://github.com/skellleks/lasso)<br><sub>skellleks</sub> | Review pane for herdr: per-agent diffs with syntax highlighting and inline comments sent back to the agent | `ai-agents` `claude-code` `code-review` `git-diff` `ratatui` | 0 | 🔄 2026-08-31 |
| [**herdr-code-review**](https://github.com/txmed82/herdr-code-review)<br><sub>txmed82</sub> | Structured AI code review plugin for Herdr | `code-review` `javascript` | 0 | 🔄 2026-08-19 |

<details><summary>Also relevant to this purpose</summary>

- [briankeegan1/herdkit](https://github.com/briankeegan1/herdkit) — Governance and parallelism for herdr-based agent workflows — a coordinator drains your backlog into isolated…
- [elKei24/herdr-co-review](https://github.com/elKei24/herdr-co-review) — Split-screen PR review in herdr: your agent finds issues, you triage each one next to its code in a TUI, the…
- [itisbryan/herdr-gh-checks](https://github.com/itisbryan/herdr-gh-checks) — Herdr plugin: watch & review the current PR's CI in a pane; CI/merge status on sidebar rows. Go + Bubble Tea.
- [JacquesvanWyk/herdr-hunk](https://github.com/JacquesvanWyk/herdr-hunk) — Interactive fzf picker for hunk diffs in herdr: commits, ranges, stashes, plus auto-open when an agent finish…
- [anhnd3005-infinity/herdr-worker-orchestrator](https://github.com/anhnd3005-infinity/herdr-worker-orchestrator) — Dispatch tasks to CLI agent workers (agy, codex, ...) via Herdr-managed panes with stateful task tracking, wo…
- [tomasvarga/herdr-sniffr](https://github.com/tomasvarga/herdr-sniffr) — An AI sniffs your PR for issues before you review — an agentic first-pass that drops draft comments into tuic…
- [mikhail-angelov/herdr-review-loop](https://github.com/mikhail-angelov/herdr-review-loop) — Automated cross-review between agents in a herdr workspace — one writes, the other reviews, repeat.
- [moneycaringcoder/herdr-collide](https://github.com/moneycaringcoder/herdr-collide) — Warns when agents working in different git worktrees of one repo are about to collide — and whether their edi…
- [neospeed83/herdr-tournament](https://github.com/neospeed83/herdr-tournament) — Adversarial multi-agent code reviews for Herdr
- [krzysztoff1/herdr-cull](https://github.com/krzysztoff1/herdr-cull) — Review and close idle agent panes in herdr — fzf multi-select, nothing closes without confirmation.
- [ubuntudroid/herdr-coder-sessions](https://github.com/ubuntudroid/herdr-coder-sessions) — Browse running Coder agent sessions in herdr and open each as its own workspace: agentty on the session, its…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-forge"></a>

## GitHub & Issue Trackers

> I want to kick off work from an issue or PR, and track PR status

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**ghzinga**](https://github.com/osolmaz/ghzinga)<br><sub>osolmaz</sub> | Easy, clickable TUI to view a single GitHub issue or PR, in Rust | `rust` | 82 | 2026-07-26 |
| [**herdr-plugin-gh-pr**](https://github.com/wyattjoh/herdr-plugin-gh-pr)<br><sub>wyattjoh</sub> | herdr plugin that shows the focused agent pane's branch GitHub PR status in the sidebar | `typescript` | 18 | 2026-07-16 |
| [**herdr-plugin-github-start**](https://github.com/ogulcancelik/herdr-plugin-github-start)<br><sub>ogulcancelik</sub> | Herdr plugin that starts Codex or Claude from a GitHub issue, PR, or discussion | `javascript` | 16 | 🔄 2026-08-31 |
| [**herdr-worktree-from-linear**](https://github.com/tdi/herdr-worktree-from-linear)<br><sub>tdi</sub> | Create a git worktree from a Linear issue and open it as a herdr workspace | `javascript` | 14 | 🔄 2026-08-24 |
| [**herdr-jira**](https://github.com/a2u/herdr-jira)<br><sub>a2u</sub> | Jira TUI plugin for herdr — browse issues with configurable JQL filters, search, change statuses, and delegate issues to AI agents running in your terminal wit… | `ai-agents` `jira` `ratatui` `rust` `tui` | 11 | 2026-07-18 |
| [**herdr-pr-tracker**](https://github.com/Matovidlo/herdr-pr-tracker)<br><sub>Matovidlo</sub> | herdr plugin: track the GitHub PR each Claude Code session produces, with gh state + actions | `claude-code` `shell` | 11 | 2026-08-12 |
| [**herdr-linear**](https://github.com/JacquesvanWyk/herdr-linear)<br><sub>JacquesvanWyk</sub> | fzf-driven Linear panel in a herdr split pane or tab: search issues, drill into projects, create issues, change status | `shell` | 8 | 2026-07-12 |
| [**herdr-git-status**](https://github.com/krystof018/herdr-git-status)<br><sub>krystof018</sub> | Surfaces CI status inside herdr for both GitLab (pipelines + merge requests) and GitHub (Actions + pull requests), auto-detected from the repo's origin. | `bash` `ci-cd` `ci-status` `developer-tools` `github-actions` | 5 | 2026-07-01 |
| [**herdr-plugin-github-dash**](https://github.com/kukv/herdr-plugin-github-dash)<br><sub>kukv</sub> | Herdr plugin for browsing and managing GitHub pull requests and issues | `cli` `github` `go` | 4 | 🔄 2026-08-29 |
| [**herdr-linear**](https://github.com/talent-factory/herdr-linear)<br><sub>talent-factory</sub> | A Linear issues panel for Herdr, with implement-on-Enter. | `rust` | 4 | 🔄 2026-08-21 |
| [**herdr-pr-board**](https://github.com/cdowell09/herdr-pr-board)<br><sub>cdowell09</sub> | Configurable cross-repository GitHub pull request dashboard for Herdr | `github` `tui` `go` | 3 | 🔄 2026-09-02 |
| [**herdr-co-review**](https://github.com/elKei24/herdr-co-review)<br><sub>elKei24</sub> | Split-screen PR review in herdr: your agent finds issues, you triage each one next to its code in a TUI, the agent posts what you approve. | `cli` `code-review` `pull-request` `rust` `tui` | 3 | 🔄 2026-08-20 |
| [**herdr-gh-checks**](https://github.com/itisbryan/herdr-gh-checks)<br><sub>itisbryan</sub> | Herdr plugin: watch & review the current PR's CI in a pane; CI/merge status on sidebar rows. Go + Bubble Tea. | `bubbletea` `ci` `github-actions` `tui` `go` | 3 | 🔄 2026-08-25 |
| [**mergr**](https://github.com/jsmenzies/mergr)<br><sub>jsmenzies</sub> | GitHub pull request status for Herdr Space sidebar rows. | `github-pull-requests` `rust` | 3 | 2026-07-30 |
| [**herdr-plugin-gh-workflow**](https://github.com/kkckkc/herdr-plugin-gh-workflow)<br><sub>kkckkc</sub> | Herdr plugin for GitHub workflow | `javascript` | 3 | 2026-07-03 |
| [**herdr-beads**](https://github.com/hexsprite/herdr-beads)<br><sub>hexsprite</sub> | Ctrl-click a beads issue ID in Herdr to open its details in a split pane | `beads` `issue-tracker` `terminal` `shell` | 2 | 2026-08-07 |
| [**herdr-sniffr**](https://github.com/tomasvarga/herdr-sniffr)<br><sub>tomasvarga</sub> | An AI sniffs your PR for issues before you review — an agentic first-pass that drops draft comments into tuicr. Agent-agnostic (codex/claude/cursor/grok/…). | `ai` `cli` `code-review` `pull-request` `tuicr` | 2 | 2026-07-14 |
| [**herdr-board**](https://github.com/bredebjorhovd/herdr-board)<br><sub>bredebjorhovd</sub> | Where coding agents queue up and run their own work — GitHub issues in, autonomous agents in herdr panes, PR reviews delivered back to the agent that wrote the… | `rust` | 1 | 2026-08-14 |
| [**herdr-dashboard**](https://github.com/chouxcreams/herdr-dashboard)<br><sub>chouxcreams</sub> | PR status dashboard TUI for herdr workspaces — PR state / CI / reviews per pane at a glance | `dashboard` `github` `pull-requests` `ratatui` `rust` | 1 | 2026-07-28 |
| [**herdr-plugin-dotfiles-github-link-preview**](https://github.com/edmundmiller/herdr-plugin-dotfiles-github-link-preview)<br><sub>edmundmiller</sub> | Herdr plugin for previewing GitHub issues and pull requests in a side pane | `python` | 1 | 2026-06-23 |
| [**worktender**](https://github.com/steig/worktender)<br><sub>steig</sub> | One command from a GitHub issue to a coding agent working on it in its own worktree. | `ai-agents` `claude-code` `coding-agents` `git-worktree` `golang` | 1 | 🔄 2026-08-26 |
| [**herdr-github-pr**](https://github.com/woshahua/herdr-github-pr)<br><sub>woshahua</sub> | Herdr plugin that syncs GitHub PR status, checks, reviews, and comments | `github` `javascript` | 1 | 🔄 2026-08-21 |
| [**🆕 herdr-pr**](https://github.com/yelsed/herdr-pr)<br><sub>yelsed</sub> | A Todo of the pull requests waiting on you, in a herdr pane. Reads everything through the gh CLI. | `rust` | 1 | 🔄 2026-08-29 |
| [**herdr-plugin-jira-pr**](https://github.com/abtris/herdr-plugin-jira-pr)<br><sub>abtris</sub> | Herdr plugin: show the Jira issue behind the current branch's PR, and warn when they disagree | `github-pr` `jira` `shell` | 0 | 2026-08-04 |
| [**git-shepherd**](https://github.com/H3xept/git-shepherd)<br><sub>H3xept</sub> | Draft/open/merged/closed pull request state as an icon next to every Herdr Space | `developer-tools` `github-cli` `tui` `javascript` | 0 | 🔄 2026-08-21 |
| [**herdr-spaces-pr-status**](https://github.com/jmarbutt/herdr-spaces-pr-status)<br><sub>jmarbutt</sub> | Show GitHub pull request status on herdr spaces, with a Conductor-style PR board | `github-pull-request` `javascript` | 0 | 2026-08-01 |
| [**herdr-pr-preview**](https://github.com/juninaba/herdr-pr-preview)<br><sub>juninaba</sub> | A Herdr plugin for previewing the current branch's GitHub pull request in a split pane. | `shell` | 0 | 2026-07-08 |
| [**github-issue-herdr-plugin**](https://github.com/nyanyaon/github-issue-herdr-plugin)<br><sub>nyanyaon</sub> | Claude Code plugin for herding GitHub issues | `rust` | 0 | 2026-07-27 |
| [**🆕 herdr-gh-issue-label**](https://github.com/polidog/herdr-gh-issue-label)<br><sub>polidog</sub> | ブランチに対応する GitHub issue の番号とタイトルを Herdr のスペースに表示するプラグイン | `github-issues` `shell` | 0 | 🔄 2026-08-28 |
| [**herdr-pr-tab-renamer**](https://github.com/ralphilius/herdr-pr-tab-renamer)<br><sub>ralphilius</sub> | Herdr plugin that renames tabs with detected pull request numbers. | `javascript` | 0 | 2026-08-03 |
| [**herdr-worktree-from-gitlab**](https://github.com/snics/herdr-worktree-from-gitlab)<br><sub>snics</sub> | herdr plugin: create a git worktree + workspace from a GitLab issue (via glab) | `gitlab` `rust` `worktree` | 0 | 2026-07-09 |
| [**herdr-pr-workflow**](https://github.com/tamdogood/herdr-pr-workflow)<br><sub>tamdogood</sub> | A Herdr action that prompts the focused agent to safely create or merge the current branch's pull request. | `javascript` | 0 | 2026-08-10 |

<details><summary>Also relevant to this purpose</summary>

- [tomasvarga/herdr-pickr](https://github.com/tomasvarga/herdr-pickr) — A PR review router for herdr — Ctrl+click a GitHub PR / GitLab MR link and pick a reviewer (tuicr · hunk · di…
- [tdi/herdr-worktree-from-pr](https://github.com/tdi/herdr-worktree-from-pr) — Create a git worktree from a GitHub PR and open it as a herdr workspace
- [jakekroon/herdr-pr-tracker](https://github.com/jakekroon/herdr-pr-tracker) — Every open pull request you have authored, docked and colour-coded by what needs you. A Herdr plugin.
- [kiitosu/herdr-jira-board](https://github.com/kiitosu/herdr-jira-board) — Jira kanban board inside herdr with Claude Code session launcher
- [ukwhatn/taskherd](https://github.com/ukwhatn/taskherd) — Task board linked to herdr agent sessions, PRs, and Jira tickets
- [0xthc/herdr-plugin-pr-board](https://github.com/0xthc/herdr-plugin-pr-board) — GitHub PRs for the current repo inside herdr: browse them in a pane, check one out as a worktree workspace, a…
- [orrgal1/herd](https://github.com/orrgal1/herd) — Issue-driven multi-agent setup for omp on herdr: a lead that files issues, workers that poll, claim, and ship…
- [spiritsack/herdr-jira-worktree](https://github.com/spiritsack/herdr-jira-worktree) — herdr plugin: prompt for a Jira ticket, open/reuse a matching git worktree, and prefill it into a fresh Claud…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-layout"></a>

## Workspaces & Layouts

> When I open a project, I want tabs, panes, and startup commands all set up in one shot

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-spreader**](https://github.com/yuk1ty/herdr-spreader)<br><sub>yuk1ty</sub> | Spin up your whole herdr workspace layout — tabs, panes, commands, and all — from a single YAML file. | `rust` | 93 | 2026-08-16 |
| [**dotfiles**](https://github.com/lararosekelley/dotfiles)<br><sub>lararosekelley</sub> | My dotfiles, meant for use with a Bash shell | `bash` `bootstrap` `dotfiles` `homebrew` `macos` | 51 | 🔄 2026-08-31 |
| [**herdr-plugin-workspace-manager**](https://github.com/razajamil/herdr-plugin-workspace-manager)<br><sub>razajamil</sub> | Declarative tab/pane layouts with per-workspace defaults applied automatically when a worktree is created. | `rust` | 38 | 🔄 2026-08-23 |
| [**seshagy**](https://github.com/lmilojevicc/seshagy)<br><sub>lmilojevicc</sub> | Agent-aware session manager for tmux & herdr — discover projects, launch sessions, and track your AI agents work. | `bubbletea` `go` `session-management` `session-manager` `terminal` | 14 | 🔄 2026-08-20 |
| [**🆕 herdr-grid**](https://github.com/thuanlm215/herdr-grid)<br><sub>thuanlm215</sub> | Visual Herdr pane layout editor with drag-and-drop, new shells, balanced splits, fixed presets, and safe workspace creation. | `layout-presets` `pane-layout` `productivity` `ratatui` `rust` | 6 | 🔄 2026-09-01 |
| [**herdr-warp**](https://github.com/HexSleeves/herdr-warp)<br><sub>HexSleeves</sub> | Open a Herdr workspace as native Warp panes | `shell` | 4 | 2026-07-25 |
| [**herdr-muster**](https://github.com/marcoskichel/herdr-muster)<br><sub>marcoskichel</sub> | Agent-aware project switcher for herdr | `rust` | 4 | 2026-07-03 |
| [**herdr-layout-tools**](https://github.com/edouard-andrei/herdr-layout-tools)<br><sub>edouard-andrei</sub> | herdr plugin: in-place reshape (main-left + grid) and equalize — same tab id, same pane ids, processes preserved | `javascript` | 3 | 2026-08-06 |
| [**herdr-pane-layouts**](https://github.com/iurysza/herdr-pane-layouts)<br><sub>iurysza</sub> | Seamless tmux-style pane resizing and layouts for Herdr | `pane-layout` `python` `terminal` | 3 | 2026-07-17 |
| [**herdr-setup-bootstrap**](https://github.com/shizlie/herdr-setup-bootstrap)<br><sub>shizlie</sub> | Herdr plugin to bootstrap new worktrees from worktree_init.toml | `shell` | 3 | 2026-06-17 |
| [**dsh-plugin-herdr**](https://github.com/sunny0826/dsh-plugin-herdr)<br><sub>sunny0826</sub> | Herdr control-plane plugin for DeepSeek Harness (DSH): observe and drive Herdr — a terminal workspace manager for AI coding agents — from DSH sessions | `dsh-plugin` `typescript` | 3 | 🔄 2026-08-25 |
| [**herdr-google-gmail**](https://github.com/Tomatio13/herdr-google-gmail)<br><sub>Tomatio13</sub> | herdr-google-gmail is a Gmail integration plugin for herdr, a terminal workspace tool. | `shell` | 3 | 2026-07-22 |
| [**herdr-clone-layout**](https://github.com/danilolucasmd/herdr-clone-layout)<br><sub>danilolucasmd</sub> | Clone your workspace layout onto every new herdr worktree. No templates, no config — the layout you're in is the template. | `shell` | 2 | 🔄 2026-08-27 |
| [**herdr-fork-from-message**](https://github.com/dmangla3/herdr-fork-from-message)<br><sub>dmangla3</sub> | Fork Codex or Claude Code from an earlier message into a new Herdr tab, pane, or workspace | `claude-code` `codex` `developer-tools` `terminal-multiplexer` `python` | 2 | 2026-08-10 |
| [**herdr-compose**](https://github.com/ropali/herdr-compose)<br><sub>ropali</sub> | herdr-compose is a declarative workspace layout manager for Herdr | `layout-manager` `python` | 2 | 2026-07-25 |
| [**herdr-google-calendar**](https://github.com/Tomatio13/herdr-google-calendar)<br><sub>Tomatio13</sub> | herdr-gog-calendar is a Google Calendar integration plugin for herdr, a terminal workspace tool. | `shell` | 2 | 2026-07-22 |
| [**herdr-layout**](https://github.com/3mmdrew/herdr-layout)<br><sub>3mmdrew</sub> | Minimalist workspace layouts for herdr. Lua file in -> workspace out. No deps, no daemon, no YAML. | `lua` `terminal` | 1 | 2026-08-04 |
| [**🆕 herdr-dwm-layout**](https://github.com/42lizard/herdr-dwm-layout)<br><sub>42lizard</sub> | DWM-style master/stack layouts for Herdr | `dwm` `fzf` `rust` `shell` `tiling` | 1 | 🔄 2026-08-28 |
| [**herdr-medieval**](https://github.com/gabrielbarretoo/herdr-medieval)<br><sub>gabrielbarretoo</sub> | A Herdr plugin that shows your workspaces and agents as a hexagonal medieval continent in 3D: each workspace is a fenced camp, each pane an adventurer that tra… | `3d` `hex-grid` `threejs` `javascript` | 1 | 2026-08-06 |
| [**herdr-spinup**](https://github.com/Royal-lobster/herdr-spinup)<br><sub>Royal-lobster</sub> | Start screen for every new herdr tab: pick a tool and it runs in that tab. Tools defined in JSON. | `javascript` | 1 | 2026-08-04 |
| [**🆕 reasonix-herdr**](https://github.com/uuie/reasonix-herdr)<br><sub>uuie</sub> | Native Reasonix plugin with live lifecycle reporting and workspace control inside Herdr. | `reasonix` `python` | 1 | 2026-07-10 |
| [**herdr-sesh**](https://github.com/xheisenbugx/herdr-sesh)<br><sub>xheisenbugx</sub> | A smart herdr workspace manager inspired by sesh | `go` | 1 | 🔄 2026-08-21 |
| [**herdr-workspace**](https://github.com/zackshen/herdr-workspace)<br><sub>zackshen</sub> | Herdr plugin: create a workspace and apply a layout profile from a centered popup | `rust` | 1 | 🔄 2026-08-24 |
| [**🆕 herdr-tab-command**](https://github.com/asermax/herdr-tab-command)<br><sub>asermax</sub> | Starts an agent or runs a command in a new tab, based on the name you give the tab | `typescript` | 0 | 🔄 2026-08-31 |
| [**ccc-herdr-layout**](https://github.com/caoer/ccc-herdr-layout)<br><sub>caoer</sub> | Visual layout picker plugin for herdr — one key, live preview | `go` | 0 | 2026-08-01 |
| [**herdr-yoke**](https://github.com/dgnsrekt/herdr-yoke)<br><sub>dgnsrekt</sub> | get yoked — two tabs side by side, one key. Chrome's split view for herdr. | `split-view` `terminal` `shell` | 0 | 2026-08-09 |
| [**herdr-plugin-dotfiles-dev-layout**](https://github.com/edmundmiller/herdr-plugin-dotfiles-dev-layout)<br><sub>edmundmiller</sub> | Herdr plugin for opening my dotfiles dev workspace layout | `python` | 0 | 2026-06-23 |
| [**herdr-notebook**](https://github.com/goofansu/herdr-notebook)<br><sub>goofansu</sub> | One permanent Markdown notebook per workspace, opened in your editor over the active pane. | `python` | 0 | 🔄 2026-08-20 |
| [**herdr-follow-cwd**](https://github.com/hasuwini77/herdr-follow-cwd)<br><sub>hasuwini77</sub> | Herdr plugin: workspace labels follow the directory their panes actually live in | `javascript` | 0 | 2026-08-13 |
| [**herdr-pane-id-metadata**](https://github.com/limars874/herdr-pane-id-metadata)<br><sub>limars874</sub> | Minimal Herdr plugin for canonical pane IDs and compact tab/pane sidebar metadata | `coding-agents` `terminal` `javascript` | 0 | 2026-08-17 |
| [**herdr-lastfocus**](https://github.com/pedrobarco/herdr-lastfocus)<br><sub>pedrobarco</sub> | tmux-style last-active pane/tab/workspace toggles for herdr, via a focus-event history daemon | `terminal-multiplexer` `tmux` `go` | 0 | 2026-07-25 |
| [**herdr-workspace-description**](https://github.com/rstacruz/herdr-workspace-description)<br><sub>rstacruz</sub> | _(no description)_ | `typescript` | 0 | 2026-08-08 |
| [**herdr-active-agent-jump**](https://github.com/shoaibkhanz/herdr-active-agent-jump)<br><sub>shoaibkhanz</sub> | herdr plugin: cycle focus forward/backward through in-flight (working/blocked) agents in layout order — the vim-motion complement to attention-jump | `javascript` | 0 | 2026-07-12 |
| [**herdr-dev-layout**](https://github.com/simoncrypta/herdr-dev-layout)<br><sub>simoncrypta</sub> | Sticky agent pane for Herdr | `herdr-integration` `shell` | 0 | 🔄 2026-08-20 |

<details><summary>Also relevant to this purpose</summary>

- [andrewchng/herdr-sessionizer](https://github.com/andrewchng/herdr-sessionizer) — Fuzzy-open projects and worktrees, then bootstrap workspaces from declarative TOML layouts — tabs, pane split…
- [fullerzz/herdr-plugin-sesh](https://github.com/fullerzz/herdr-plugin-sesh) — Sesh-style workspace picker TUI for Herdr. Integrates with zoxide to create workspaces from commonly used dir…
- [ntindle/herdr-resurrect](https://github.com/ntindle/herdr-resurrect) — tmux-resurrect for herdr — snapshot workspaces, tabs, panes, cwd, running programs and agents, and restore th…
- [enekos/herdr-quick-actions](https://github.com/enekos/herdr-quick-actions) — fzf picker for herdr's native tab/pane/workspace actions, ranked by usage — stop memorizing keybindings
- [salkhalil/herdr-sessionizer](https://github.com/salkhalil/herdr-sessionizer) — tmux-sessionizer for herdr: fzf over open workspaces and zoxide directories, create-or-focus with template ta…
- [crierr/herdr-arrange](https://github.com/crierr/herdr-arrange) — Interactive popup UI for herdr pane move / swap / re-split / layout
- [aliou/herdr-cast](https://github.com/aliou/herdr-cast) — Personal Herdr plugin for native macOS agent notifications, fuzzy workspace navigation, zoxide-backed workspa…
- [42lizard/herdr-sessionizer](https://github.com/42lizard/herdr-sessionizer) — tmux-sessionizer style plugin for herdr
- [chandrasekharan98/herdr-workspace-save](https://github.com/chandrasekharan98/herdr-workspace-save) — Save a Herdr workspace — layout, cwds, agent sessions, running commands — and reopen it later from an fzf pic…
- [asermax/herdr-suspend-workspace](https://github.com/asermax/herdr-suspend-workspace) — Suspend a herdr workspace (snapshot layout + agents, close it, restore later from a popup picker)
- [willfish/herdr-workspacex](https://github.com/willfish/herdr-workspacex) — Rust-native fuzzy Herdr workspace switcher with zoxide-backed workspace creation

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-navigate"></a>

## Pane Navigation & Keys

> I want to move and resize between panes and workspaces using the same keys as my editor

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**vim-herdr-navigation**](https://github.com/paulbkim-dev/vim-herdr-navigation)<br><sub>paulbkim-dev</sub> | Seamless Ctrl+h/j/k/l navigation across herdr panes and Vim/Neovim splits — vim-tmux-navigator ported to herdr | `neovim` `vim` `shell` | 101 | 🔄 2026-08-23 |
| [**herdr-automatic-rename**](https://github.com/qu8n/herdr-automatic-rename)<br><sub>qu8n</sub> | Navigate herdr faster with smart tab names and 1-9 jump labels for workspaces/tabs/agents | `shell` | 62 | 🔄 2026-08-31 |
| [**herdr-splits.nvim**](https://github.com/lmilojevicc/herdr-splits.nvim)<br><sub>lmilojevicc</sub> | Smart splits navigation and resizing for Herdr and Neovim | `lua` `neovim` `neovim-plugin` `neovim-plugins` `nvim` | 56 | 2026-08-17 |
| [**herdr-floax**](https://github.com/Tyru5/herdr-floax)<br><sub>Tyru5</sub> | Floating scratch shell for herdr — a tmux-floax style toggleable popup, one per workspace, with persistent sessions | `rust` `terminal` `tmux-floax` | 23 | 2026-07-26 |
| [**herdr-nvim-nav**](https://github.com/aimdevlee/herdr-nvim-nav)<br><sub>aimdevlee</sub> | Seamless Ctrl+h/j/k/l across herdr panes and Neovim splits — socket-based, no per-keystroke process | `neovim` `neovim-plugin` `lua` | 18 | 2026-08-02 |
| [**herdr-last-workspace**](https://github.com/third774/herdr-last-workspace)<br><sub>third774</sub> | Plugin for swapping to the last workspace you had focused | `rust` | 17 | 2026-06-22 |
| [**herdr-logbook**](https://github.com/Resetnak/herdr-logbook)<br><sub>Resetnak</sub> | Your terminal's working memory — offline, Markdown-first notes, decisions, and an active-task now.md for Herdr | `adr` `bubbletea` `cli` `go` `markdown` | 12 | 🔄 2026-08-27 |
| [**herdr-pane-mover**](https://github.com/osamahbeig/herdr-pane-mover)<br><sub>osamahbeig</sub> | Clickable overlay menu for herdr: move, re-split, or swap panes across tabs and workspaces | `terminal` `tui` `javascript` | 11 | 2026-07-10 |
| [**herdr-recent-navigator**](https://github.com/beyondlex/herdr-recent-navigator)<br><sub>beyondlex</sub> | A recent workspaces/tabs/panes switcher for Herdr. Opens an popup window listing recently focused workspaces, tabs, panes, and AI agents — fuzzy-searchable and… | `agent` `mru` `navigator` `pane` `popup` | 10 | 2026-07-28 |
| [**herdr-paddock**](https://github.com/neyham/herdr-paddock)<br><sub>neyham</sub> | 🐑 A card-wall feed for your herdr agents — glance over the flock, zoom into one, reply, all over plain SSH | `bubbletea` `go` `ssh` `tui` | 9 | 🔄 2026-08-25 |
| [**herdr-command-center**](https://github.com/speardragon/herdr-command-center)<br><sub>speardragon</sub> | One keybinding for every command — a herdr popup that lists the commands you registered, runs them by arrow key or number, and closes itself before the command… | `command-palette` `nodejs` `terminal` `toml` `tui` | 9 | 🔄 2026-08-19 |
| [**herdr-trail**](https://github.com/catoncat/herdr-trail)<br><sub>catoncat</sub> | Herd-wide shared memos for herdr: agents jot follow-ups, humans manage one global list, every entry jumps back to its source conversation | `javascript` | 8 | 🔄 2026-08-26 |
| [**herdr-toggle-popup**](https://github.com/maro114510/herdr-toggle-popup)<br><sub>maro114510</sub> | One-keybinding overlay popup shell plugin for the Herdr terminal | `go` | 7 | 2026-08-12 |
| [**nvim-herdr-navigation**](https://github.com/bojackduy/nvim-herdr-navigation)<br><sub>bojackduy</sub> | vim-tmux-navigator style ctrl+h/j/k/l navigation between Neovim splits and Herdr panes | `keyboard-shortcuts` `lazyvim` `lua` `navigation` `neovim` | 6 | 2026-07-20 |
| [**herdr-swipe**](https://github.com/husniadil/herdr-swipe)<br><sub>husniadil</sub> | Trackpad gestures for Herdr: move between panes, tabs and spaces, and jump to the agent waiting on you | `cgeventtap` `gestures` `macos` `python` `terminal` | 6 | 🔄 2026-08-20 |
| [**herdr-omnisearch**](https://github.com/dmnkf/herdr-omnisearch)<br><sub>dmnkf</sub> | Fast local search and navigation for Herdr workspaces, panes, and archived agent sessions | `python` | 5 | 🔄 2026-08-31 |
| [**nvim-herdr-navigator**](https://github.com/kaar/nvim-herdr-navigator)<br><sub>kaar</sub> | Seamless navigation between Neovim splits and herdr panes: one set of `ctrl+h/j/k/l` chords moves through vim and herdr panes. | `neovim` `neovim-plugin` `lua` | 5 | 2026-07-29 |
| [**herdr-equalize-panes**](https://github.com/shibayu36/herdr-equalize-panes)<br><sub>shibayu36</sub> | herdr plugin that automatically equalizes pane sizes on split and close (tmux select-layout -E, but automatic) | `terminal` `perl` | 5 | 🔄 2026-08-22 |
| [**herdr-scratch**](https://github.com/AkashJana18/herdr-scratch)<br><sub>AkashJana18</sub> | Persistent scratchpads for Herdr, paving the way for floating utility panes. | `cli` `rust` `scratchpad` | 4 | 🔄 2026-08-30 |
| [**herdr-cliamp**](https://github.com/coryshaw1/herdr-cliamp)<br><sub>coryshaw1</sub> | Floating cliamp for herdr that keeps playing when hidden: the player lives in a detached herdr session, so closing the float only detaches. | `audiobook` `cliamp` `music-player` `podcast` `terminal` | 4 | 🔄 2026-08-24 |
| [**🆕 herdr-arrange**](https://github.com/crierr/herdr-arrange)<br><sub>crierr</sub> | Interactive popup UI for herdr pane move / swap / re-split / layout | `go` | 4 | 🔄 2026-08-31 |
| [**herdr-annotations**](https://github.com/jagzmz/herdr-annotations)<br><sub>jagzmz</sub> | Annotate selected terminal text in Herdr with a fast local-first popup and reusable collections. | `annotations` `cli` `coding-agents` `developer-tools` `local-first` | 4 | 2026-07-16 |
| [**herdr-harpoon**](https://github.com/KonstantinKai/herdr-harpoon)<br><sub>KonstantinKai</sub> | Harpoon for herdr: mark panes and jump by index. Bash-only, zero build. | `bash` `harpoon` `tmux-harpoon` `shell` | 4 | 2026-07-29 |
| [**herdr-last**](https://github.com/lmilojevicc/herdr-last)<br><sub>lmilojevicc</sub> | Toggle back to the previously active workspace or tab in Herdr | `go` `linux` `macos` `productivity` `tabs` | 4 | 2026-08-07 |
| [**herdr-equalize-splits**](https://github.com/markhuot/herdr-equalize-splits)<br><sub>markhuot</sub> | herdr plugin: equalize every split in the current tab to an even share within each row/column (bind to Ctrl+b =) | `terminal` `tmux` `javascript` | 4 | 2026-07-08 |
| [**herdr-attention**](https://github.com/milkyskies/herdr-attention)<br><sub>milkyskies</sub> | A herdr plugin: one keypress jumps focus to the next agent that needs attention (blocked, then done). | `javascript` | 4 | 2026-07-08 |
| [**herdr-navigator**](https://github.com/willfish/herdr-navigator)<br><sub>willfish</sub> | Herdr-side navigation actions for Vim/Neovim-aware pane movement | `navigation` `neovim` `rust` | 4 | 2026-07-07 |
| [**herdr-tmux-layout**](https://github.com/crierr/herdr-tmux-layout)<br><sub>crierr</sub> | tmux-style preset layouts for live Herdr panes: cycle, even-horizontal, even-vertical, main-horizontal, main-vertical, tiled, and balance | `go` | 3 | 🔄 2026-08-30 |
| [**herdr-convo-index**](https://github.com/dzwduan/herdr-convo-index)<br><sub>dzwduan</sub> | Turn index for Claude Code panes in herdr — jump to any past turn and read it in a popup | `python` | 3 | 2026-07-27 |
| [**herdr-popupx**](https://github.com/jeromychu23/herdr-popupx)<br><sub>jeromychu23</sub> | Persistent native floating scratch popups for Herdr. | `rust` `terminal` `tui` | 3 | 2026-07-21 |
| [**herdr-unread-marker**](https://github.com/JoanGil/herdr-unread-marker)<br><sub>JoanGil</sub> | Mark/unmark the focused agent unread with a keybinding, manual only | `shell` | 3 | 2026-07-17 |
| [**herdr-confirm-close-pane**](https://github.com/poweroutlet2/herdr-confirm-close-pane)<br><sub>poweroutlet2</sub> | A herdr plugin that asks for confirmation before closing a pane, like tmux's prefix+x confirm-before. | `shell` | 3 | 2026-07-06 |
| [**herdr-pretty-which**](https://github.com/ramarivera/herdr-pretty-which)<br><sub>ramarivera</sub> | A Rust/Ratatui which-key style keybinding overlay for Herdr. | `ratatui` `rust` `terminal` `tui` `which-key` | 3 | 2026-08-14 |
| [**🆕 herdr-mission-control**](https://github.com/vjeantet/herdr-mission-control)<br><sub>vjeantet</sub> | Mission Control for herdr: one key, every pane of the workspace as a live tile grid grouped by tab; pick one to switch to it | `expose` `mission-control` `terminal` `tui` `rust` | 3 | 🔄 2026-09-01 |
| [**herdr-equalize-vsplit**](https://github.com/devoc09/herdr-equalize-vsplit)<br><sub>devoc09</sub> | A Herdr plugin that splits the current pane to the right and equalizes column widths. | `go` | 2 | 2026-07-15 |
| [**herdr-easymotion**](https://github.com/elliotekj/herdr-easymotion)<br><sub>elliotekj</sub> | 🦘 Jump directly between Herdr panes | `javascript` | 2 | 2026-07-20 |
| [**herdr-break-pane**](https://github.com/iuhoay/herdr-break-pane)<br><sub>iuhoay</sub> | A small Herdr plugin that moves the focused pane into a new tab. | `pane` `javascript` | 2 | 🔄 2026-08-27 |
| [**herdr-prevtab**](https://github.com/joo-was-already-taken/herdr-prevtab)<br><sub>joo-was-already-taken</sub> | Herdr plugin for switching to the previously focused tab | `rust` | 2 | 🔄 2026-09-01 |
| [**herdr-lazytask**](https://github.com/mdetweil/herdr-lazytask)<br><sub>mdetweil</sub> | Lazytask in a herdr split pane (open/focus/toggle) plus Taskwarrior quick actions | `lazytask` `taskwarrior` `terminal` `rust` | 2 | 2026-08-02 |
| [**herdr-float**](https://github.com/meerzulee/herdr-float)<br><sub>meerzulee</sub> | Zellij like ALT+F floating pane | `shell` | 2 | 2026-07-20 |
| [**herdr-quotr**](https://github.com/napalmpapalam/herdr-quotr)<br><sub>napalmpapalam</sub> | Quote your agent's own answer back at it, from a herdr popup. | `claude-code` `rust` `tui` | 2 | 🔄 2026-09-01 |
| [**herdr-pane-mover**](https://github.com/ronly2460/herdr-pane-mover)<br><sub>ronly2460</sub> | Move Herdr panes between workspaces with an interactive arrow-key picker | `terminal` `workspace` `shell` | 2 | 🔄 2026-08-23 |
| [**herdr-pane-orientation-switcher**](https://github.com/sf1tzp/herdr-pane-orientation-switcher)<br><sub>sf1tzp</sub> | Workflow Ergonomics for Split Panes in Herdr | `shell` | 2 | 2026-07-25 |
| [**herdr-ask-inbox**](https://github.com/speardragon/herdr-ask-inbox)<br><sub>speardragon</sub> | Collect blocked Claude AskUserQuestion prompts from every herdr workspace into one popup, answer them in place, and never send an answer to the wrong agent. | `claude-code` `javascript` | 2 | 2026-07-25 |
| [**herdr-unread-jump**](https://github.com/to4iki/herdr-unread-jump)<br><sub>to4iki</sub> | Jump to the next Herdr agent pane that needs attention (blocked, then done). | `agents` `bash` `shell` | 2 | 🔄 2026-08-30 |
| [**herdr-plugin-ide-jump**](https://github.com/agentience/herdr-plugin-ide-jump)<br><sub>agentience</sub> | Get back to your IDE: raise the editor window for the focused pane's project, or pick one from a filterable popup. A Herdr plugin. | `python` | 1 | 🔄 2026-08-24 |
| [**herdr-voice**](https://github.com/aneym/herdr-voice)<br><sub>aneym</sub> | Voice control for herdr — speak to create spaces, split panes, and drive coding agents. OpenAI Realtime + floating HUD with live dictation and transcripts. | `openai-realtime-api` `voice` `javascript` | 1 | 2026-08-01 |
| [**herdr-plugin-tiles**](https://github.com/carsonjones/herdr-plugin-tiles)<br><sub>carsonjones</sub> | simple pane manager for herdr | `python` | 1 | 2026-06-19 |
| [**herdr-notes**](https://github.com/cyperx84/herdr-notes)<br><sub>cyperx84</sub> | Focused per-workspace Markdown scratch notes for Herdr, built in Go | `bubbletea` `golang` `markdown` `notes` `go` | 1 | 2026-08-16 |
| [**🆕 herdr-tab-jump**](https://github.com/cyperx84/herdr-tab-jump)<br><sub>cyperx84</sub> | Focus herdr tab N by position, from any keybinding — split your number row between tabs and workspaces | `shell` | 1 | 🔄 2026-09-01 |
| [**herdr-last-tab**](https://github.com/dantehemerson/herdr-last-tab)<br><sub>dantehemerson</sub> | Plugin for swapping to the last tab you had focused | `rust` | 1 | 2026-08-12 |
| [**herdr-nav-history**](https://github.com/jugyo/herdr-nav-history)<br><sub>jugyo</sub> | Browser-style back/forward navigation over focus history (panes, tabs, workspaces) for herdr | `javascript` | 1 | 2026-07-12 |
| [**herdr-plugin-switcher**](https://github.com/KadenThomp36/herdr-plugin-switcher)<br><sub>KadenThomp36</sub> | Hold Ctrl, tap Tab to cycle herdr panes MRU-style. Arc/Zen-style pane switcher for herdr on macOS. | `swift` | 1 | 🔄 2026-08-21 |
| [**herdr-nvim-aware**](https://github.com/KoalaVim/herdr-nvim-aware)<br><sub>KoalaVim</sub> | Nvim-aware keybindings for herdr: navigation, splits, close, zoom | `rust` | 1 | 🔄 2026-08-20 |
| [**herdr-plugin-last**](https://github.com/m4salah/herdr-plugin-last)<br><sub>m4salah</sub> | tmux-style last-tab and last-workspace navigation for Herdr | `rust` | 1 | 2026-07-30 |
| [**herdr-scratch**](https://github.com/macintacos/herdr-scratch)<br><sub>macintacos</sub> | A scratch shell for herdr, in a popup you toggle with one chord — backed by tmux, so it comes back exactly as you left it | `go` | 1 | 🔄 2026-08-28 |
| [**herdr-normal-mode**](https://github.com/maedana/herdr-normal-mode)<br><sub>maedana</sub> | Vim-style normal mode for the herdr sidebar: j/k rows, h/l tabs, 0-9 panes | `rust` `tui` | 1 | 🔄 2026-08-24 |
| [**herdr-next-agent**](https://github.com/martin-ro/herdr-next-agent)<br><sub>martin-ro</sub> | Herdr plugin: jump to the next agent needing attention, ranked by a configurable status priority | `python` | 1 | 2026-07-15 |
| [**herdr-touchbar**](https://github.com/omerturhan/herdr-touchbar)<br><sub>omerturhan</sub> | Shows working and blocked herdr agents on the MacBook Touch Bar; tap one to jump straight to its tab. | `ai-agents` `macos` `touchbar` `swift` | 1 | 2026-07-30 |
| [**herdr-deck-navigation**](https://github.com/raghu-nandan-bs/herdr-deck-navigation)<br><sub>raghu-nandan-bs</sub> | Replaces herdr's flat workspace/tab/pane navigator with a Deck view built to reach any pane fast without scrolling. | `rust` `terminal` `tui` | 1 | 🔄 2026-08-24 |
| [**herdr-account-switch**](https://github.com/rcosteira79/herdr-account-switch)<br><sub>rcosteira79</sub> | Hot-swap Claude Code / Codex logins without re-authenticating. Overlay picker, cycle-to-next keybinding, and a per-pane account badge ($acct). | `python` | 1 | 🔄 2026-08-28 |
| [**herdr-smartnav**](https://github.com/retroaalto/herdr-smartnav)<br><sub>retroaalto</sub> | Direction-aware pane navigation plugin for Herdr | `go` | 1 | 2026-08-01 |
| [**herdr-edge-nav**](https://github.com/sebcbi1/herdr-edge-nav)<br><sub>sebcbi1</sub> | Herdr plugin for directional pane navigation/resizing that crosses tabs and workspaces at pane edges, with seamless Neovim split awareness. | `lua` | 1 | 2026-08-12 |
| [**herdr-ferry**](https://github.com/shadowfax92/herdr-ferry)<br><sub>shadowfax92</sub> | A native Rust popup for multi-moving live Herdr panes and tabs or merging workspaces. | `productivity` `rust` `terminal` `tui` | 1 | 🔄 2026-08-19 |
| [**herdr-scratch**](https://github.com/shadowfax92/herdr-scratch)<br><sub>shadowfax92</sub> | Persistent per-pane Herdr scratch popups backed by private tmux sessions. | `neovim` `productivity` `rust` `terminal` `tmux` | 1 | 2026-08-04 |
| [**herdr-talon**](https://github.com/shadowfax92/herdr-talon)<br><sub>shadowfax92</sub> | Spatial keyboard hints for visible Herdr terminal targets. | `keyboard-navigation` `productivity` `rust` `terminal` `tmux-fingers` | 1 | 🔄 2026-08-20 |
| [**herdr-nav-plus**](https://github.com/shoaibkhanz/herdr-nav-plus)<br><sub>shoaibkhanz</sub> | Ctrl+h/j/k/l navigation that flows past herdr panes into workspaces — vim-aware, wraps at both ends | `javascript` | 1 | 2026-07-18 |
| [**herdr-hintr**](https://github.com/wraithyy/herdr-hintr)<br><sub>wraithyy</sub> | herdr plugin: whichkey-style keybinding cheatsheet popup — press the key to run it | `shell` | 1 | 2026-08-11 |
| [**🆕 herdr-notes**](https://github.com/0xfelixli/herdr-notes)<br><sub>0xfelixli</sub> | Annotate selected terminal text in a Rust popup textbox — herdr plugin | `rust` `terminal` | 0 | 🔄 2026-08-27 |
| [**herdr-popup**](https://github.com/abelfubu/herdr-popup)<br><sub>abelfubu</sub> | Generic Herdr popup pane plugin for ad-hoc shell commands | `shell` | 0 | 🔄 2026-08-21 |
| [**herdr-layout-cycle**](https://github.com/amiramay/herdr-layout-cycle)<br><sub>amiramay</sub> | herdr plugin: cycle through preset pane layouts, tmux prefix+space style | `javascript` | 0 | 2026-08-08 |
| [**herdr-plugin-echo**](https://github.com/andischerer/herdr-plugin-echo)<br><sub>andischerer</sub> | Herdr Plugin that broadcast keystrokes from one pane to multiple marked panes | `typescript` | 0 | 🔄 2026-08-23 |
| [**🆕 herdr-hyprland**](https://github.com/aorumbayev/herdr-hyprland)<br><sub>aorumbayev</sub> | Hyprland inspired controls for herdr | `ai-agents` `developer-tools` `golang` `hyprland` `keybindings` | 0 | 🔄 2026-08-31 |
| [**gotopr**](https://github.com/asumaran/gotopr)<br><sub>asumaran</sub> | Herdr plugin: jump to your open GitHub PRs across local repos and worktrees | `go` | 0 | 🔄 2026-08-23 |
| [**herdr-confirm-close**](https://github.com/asumaran/herdr-confirm-close)<br><sub>asumaran</sub> | Herdr plugin: close the focused pane, asking first only when a process is running in it | `terminal` `go` | 0 | 🔄 2026-08-23 |
| [**herdr-auto-focus**](https://github.com/calorie/herdr-auto-focus)<br><sub>calorie</sub> | Focus Herdr agents that need attention after macOS input becomes idle. | `golang` `macos` `go` | 0 | 2026-07-27 |
| [**herdr-next-agent**](https://github.com/choplin/herdr-next-agent)<br><sub>choplin</sub> | Move between Herdr agents in configured semantic states. | `go` | 0 | 🔄 2026-08-24 |
| [**herdr-split-pane**](https://github.com/choplin/herdr-split-pane)<br><sub>choplin</sub> | Open a caller-provided command directly in a Herdr split pane. | — | 0 | 🔄 2026-08-24 |
| [**herdr-nav**](https://github.com/codingfragments/herdr-nav)<br><sub>codingfragments</sub> | herdr Workspaces and pane navigation, modern version of herdr-navigation with better preview support and new workspace template handling | `html` | 0 | 🔄 2026-08-27 |
| [**herdr-which-key**](https://github.com/CowboyVang/herdr-which-key)<br><sub>CowboyVang</sub> | A which-key-style keymap overlay for herdr. Press one key, see every binding under your prefix grouped and labelled, press a second key to run it. Deliberately… | `keybindings` `terminal` `which-key` `python` | 0 | 2026-08-02 |
| [**🆕 herdr-agent-numbers**](https://github.com/DillonWall/herdr-agent-numbers)<br><sub>DillonWall</sub> | Number herdr's agents panel to match focus_agent (prefix+1..9). | `terminal-multiplexer` `shell` | 0 | 🔄 2026-09-01 |
| [**herdr-plugin-agents-usage**](https://github.com/gecm0/herdr-plugin-agents-usage)<br><sub>gecm0</sub> | Show provider usage (Claude, Codex, OpenCode Go, Neuralwatt) in a Herdr modal popup | `claude` `codex` `opencode` `terminal` `usage` | 0 | 2026-07-26 |
| [**🆕 herdr-desktop-switcher**](https://github.com/gustavocaiano/herdr-desktop-switcher)<br><sub>gustavocaiano</sub> | Experimental macOS desktop switcher for Herdr | `rust` | 0 | 🔄 2026-08-26 |
| [**herdr-harpoon**](https://github.com/hadeson/herdr-harpoon)<br><sub>hadeson</sub> | Harpoon-style pane marks for herdr: pin panes to slots 1-9 and jump straight to them, across tabs and workspaces. | `harpoon` `pane-navigation` `terminal` `tmux` `python` | 0 | 2026-07-25 |
| [**herdr-counting-sheep**](https://github.com/inonprince/herdr-counting-sheep)<br><sub>inonprince</sub> | Live Space and Agent indexes for Herdr, with shortcuts for jumping to the last tab, Space, or Agent. | `productivity` `terminal` `javascript` | 0 | 2026-08-03 |
| [**herdr-matter-wall**](https://github.com/Javamomma/herdr-matter-wall)<br><sub>Javamomma</sub> | herdr plugin: tile the most-active subdirectories of a project as a live wall of read-only AI status cards | `claude-code` `shell` | 0 | 2026-07-14 |
| [**herdr-nav**](https://github.com/jmarcelomb/herdr-nav)<br><sub>jmarcelomb</sub> | Pane, tab and workspace navigation plugin for herdr. | `rust` | 0 | 2026-07-30 |
| [**🆕 herdr-pane-mark**](https://github.com/jovylle/herdr-pane-mark)<br><sub>jovylle</sub> | Herdr plugin — custom $mark under Agents via palette/popup (no fork) | `terminal` `shell` | 0 | 🔄 2026-09-01 |
| [**🆕 herdr-positional-tabs**](https://github.com/juezhong/herdr-positional-tabs)<br><sub>juezhong</sub> | Stable positional tab labels and Alt-number navigation for Herdr. | `rust` `terminal` | 0 | 🔄 2026-08-30 |
| [**herdr-last-tab**](https://github.com/k-narusawa/herdr-last-tab)<br><sub>k-narusawa</sub> | _(no description)_ | `shell` | 0 | 🔄 2026-08-22 |
| [**herdr-hasr**](https://github.com/KazBrekker1/herdr-hasr)<br><sub>KazBrekker1</sub> | Hasr (حصر — enumeration, a complete tally) — goto-style popup switcher for herdr: switch, rename, delete & create agents, tabs and spaces, with real-time done… | `tui` `go` | 0 | 2026-07-23 |
| [**herdr-cmd-marks**](https://github.com/leonho/herdr-cmd-marks)<br><sub>leonho</sub> | herdr plugin: per-project command bookmarks popup. Run bookmarked commands in a separate shell while your agent is busy (global, project, and smart sections). | `shell` | 0 | 2026-07-18 |
| [**herdr-reshape**](https://github.com/macintacos/herdr-reshape)<br><sub>macintacos</sub> | A herdr plugin that moves the focused pane around its tab and squares the tab up into an even grid | `go` | 0 | 🔄 2026-08-28 |
| [**herdr-pane-balancer**](https://github.com/malone-c/herdr-pane-balancer)<br><sub>malone-c</sub> | Keeps herdr panes evenly sized as they open and close. Splitting halves the focused pane; this rebalances the whole tab. | `python` | 0 | 2026-08-07 |
| [**🆕 herdr-ai-memory**](https://github.com/MarlonPassos-git/herdr-ai-memory)<br><sub>MarlonPassos-git</sub> | Herdr popup for checkout-local AI Memory workstreams | `ai-memory` `python` | 0 | 🔄 2026-08-27 |
| [**herdr-focus-or-tab**](https://github.com/mholtzscher/herdr-focus-or-tab)<br><sub>mholtzscher</sub> | Cycle through Herdr panes across tab boundaries | `terminal-multiplexer` `rust` | 0 | 2026-07-31 |
| [**herdr-plugins**](https://github.com/oullin/herdr-plugins)<br><sub>oullin</sub> | A collection of focused, independently installable plugins for Herdr. | `typescript` | 0 | 2026-08-09 |
| [**🆕 herdr-equalize-panes**](https://github.com/ponko2/herdr-equalize-panes)<br><sub>ponko2</sub> | Automatically keeps panes in each tab evenly sized as panes are created, closed, moved, or exited. | `rust` | 0 | 🔄 2026-08-30 |
| [**herdr-focused-codex-fork**](https://github.com/potatoQi/herdr-focused-codex-fork)<br><sub>potatoQi</sub> | Fork the Codex session in the focused Herdr pane into a right-hand pane. | `shell` | 0 | 2026-08-09 |
| [**herdr-whichkey**](https://github.com/Qu4tro/herdr-whichkey)<br><sub>Qu4tro</sub> | A blezz/which-key-style action menu for herdr: one trigger key, then one keystroke per action — no typing, no Enter. | `rust` | 0 | 2026-07-22 |
| [**herdr-close-other-panes**](https://github.com/reobin/herdr-close-other-panes)<br><sub>reobin</sub> | vim's ctrl-w o for herdr: close every pane except the focused one | `shell` | 0 | 🔄 2026-08-25 |
| [**herdr-pane-equalizer**](https://github.com/shanefully-done/herdr-pane-equalizer)<br><sub>shanefully-done</sub> | Resize herdr panes equally; automatically or manually. | `javascript` | 0 | 🔄 2026-08-20 |
| [**🆕 herdr-pane-tools**](https://github.com/solidsnakedev/herdr-pane-tools)<br><sub>solidsnakedev</sub> | Vim-aware pane navigation, aerospace-style pane moves and tmux-style rotation for herdr | `shell` | 0 | 🔄 2026-09-01 |
| [**herdr-tabpick**](https://github.com/sushidesu/herdr-tabpick)<br><sub>sushidesu</sub> | Pick a herdr tab, most recently used first, with a live pane preview. | `shell` | 0 | 2026-08-15 |
| [**herdr-confirm-close**](https://github.com/tajdien/herdr-confirm-close)<br><sub>tajdien</sub> | herdr plugin: confirmation popup before closing a pane or tab | `shell` | 0 | 2026-08-13 |
| [**herdr-jump**](https://github.com/tp6gw94/herdr-jump)<br><sub>tp6gw94</sub> | Keyboard navigation for Herdr workspaces, tabs, panes, and agents. | `javascript` | 0 | 2026-08-16 |
| [**herdr-focus**](https://github.com/trapple/herdr-focus)<br><sub>trapple</sub> | Focus the next blocked/done agent pane and bring the terminal app to front. Global hotkey included. | `shell` | 0 | 2026-07-19 |
| [**herdr-golden-ratio**](https://github.com/vigneshwerv/herdr-golden-ratio)<br><sub>vigneshwerv</sub> | Resize the focused Herdr pane to the golden ratio (~61.8%) | `go` `terminal` | 0 | 🔄 2026-08-24 |
| [**herdr-balance-panes**](https://github.com/willfish/herdr-balance-panes)<br><sub>willfish</sub> | Evenly size panes in the current Herdr tab (tmux select-layout -E) | `rust` `terminal` `tmux` | 0 | 2026-08-05 |
| [**🆕 herdr-grid**](https://github.com/WillHeather/herdr-grid)<br><sub>WillHeather</sub> | Tile a herdr workspace's agent panes into a screen-sized grid, and put them back. | `python` | 0 | 🔄 2026-08-31 |
| [**herdr-compass**](https://github.com/ycros/herdr-compass)<br><sub>ycros</sub> | Unified directional navigation for Herdr across panes, tabs, and workspaces. | `python` | 0 | 2026-08-07 |
| [**herdr-kakoune-popup**](https://github.com/Yukaii/herdr-kakoune-popup)<br><sub>Yukaii</sub> | Run Kakoune terminal commands in native Herdr popups. | `kakoune` `shell` | 0 | 🔄 2026-08-20 |

<details><summary>Also relevant to this purpose</summary>

- [thanhdat77/herdr-navigator](https://github.com/thanhdat77/herdr-navigator) — Jump to any Herdr workspace, agent, project, session, remote, directory, or action from one fuzzy navigator.
- [speardragon/herdr-plugin-manager](https://github.com/speardragon/herdr-plugin-manager) — Manage herdr plugins from a popup — install, update, enable/disable, uninstall, and browse the herdr-plugin m…
- [jorge07RD/herdr-ssh-manager](https://github.com/jorge07RD/herdr-ssh-manager) — Save SSH hosts and reconnect from a fuzzy popup inside Herdr — Enter hands the popup straight to ssh.
- [bayoudhi/herdr-prayer-times](https://github.com/bayoudhi/herdr-prayer-times) — Next Islamic prayer and countdown in the Herdr sidebar, with a timetable popup and notifications
- [black-atom-industries/helm.herdr](https://github.com/black-atom-industries/helm.herdr) — Jump to any Herdr workspace, agent, project, session, remote, directory, or action from one fuzzy navigator.
- [victor-software-house/herdr-stash](https://github.com/victor-software-house/herdr-stash) — Stash a Herdr workspace: stop its agents, keep its shape and their conversations, and restore it later from a…
- [Joxtacy/herdr-plugin-vault](https://github.com/Joxtacy/herdr-plugin-vault) — Browse past Claude Code sessions in a herdr popup and resume the one you pick in a new tab
- [leonho/herdr-idle-panes](https://github.com/leonho/herdr-idle-panes) — herdr plugin: popup checklist to review and close panes sitting at an idle shell
- [ram4-dev/herdr-notify-center](https://github.com/ram4-dev/herdr-notify-center) — Server-wide agent notifications with a durable popup inbox for Herdr
- [shoaibkhanz/herdr-active-agent-jump](https://github.com/shoaibkhanz/herdr-active-agent-jump) — herdr plugin: cycle focus forward/backward through in-flight (working/blocked) agents in layout order — the v…
- [vgreg/herdr-padio](https://github.com/vgreg/herdr-padio) — Switch PadIO controller modes automatically based on the app running in herdr's focused pane
- [yojahny55/herdr-space-groups](https://github.com/yojahny55/herdr-space-groups) — Herdr plugin: group Spaces into named, colored groups — picker popup (mouse + keyboard), sidebar group header…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-files"></a>

## File Viewers & Editors

> I want to open a file tree inside a pane, or keep it in sync with my editor

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**terminal-code**](https://github.com/zenbu-labs/terminal-code)<br><sub>zenbu-labs</sub> | VS Code in the terminal | `cli` `terminal` `vscode` `typescript` | 1834 | 🔄 2026-08-28 |
| [**herdr-file-viewer**](https://github.com/smarzban/herdr-file-viewer)<br><sub>smarzban</sub> | A git-aware, read-only file viewer for herdr. Mouse friendly, keyboard-driven TUI: tree + content pane with diffs, rendered markdown, and syntax highlighting. | `file-viewer` `git` `ratatui` `rust` `terminal` | 515 | 2026-08-15 |
| [**herdr-sidebar**](https://github.com/alexarthurs/herdr-sidebar)<br><sub>alexarthurs</sub> | VS Code-style sidebar for the herdr: file explorer + git source control in one pane — syntax-highlighted previews, VS Code-style diffs, GitLens-style drawers,… | `git` `ratatui` `rust` `sidebar` `terminal` | 246 | 🔄 2026-09-02 |
| [**herdr-mirror**](https://github.com/nikok6/herdr-mirror)<br><sub>nikok6</sub> | Unify your local and remote sessions in one window: mirror remote herdr servers into your local sidebar and drive them over SSH | `rust` | 210 | 🔄 2026-08-29 |
| [**herdr-nvim**](https://github.com/ChmaraX/herdr-nvim)<br><sub>ChmaraX</sub> | Neovim, fully integrated into your herdr workspace | `lua` `neovim` `nvim` `nvim-plugin` `rust` | 113 | 🔄 2026-09-01 |
| [**dotfiles**](https://github.com/edmundmiller/dotfiles)<br><sub>edmundmiller</sub> | For keeping all my Dotfiles update to date | `dotfiles` `emacs` `nix-dotfiles` `nixos` `nixos-configuration` | 80 | 🔄 2026-09-02 |
| [**herdr-lazygit**](https://github.com/Crokily/herdr-lazygit)<br><sub>Crokily</sub> | Run lazygit in a herdr sidebar pane with AI commit messages — one key to open, one to expand, one to commit | `git` `lazygit` `shell` | 27 | 2026-07-17 |
| [**herdr-yazi**](https://github.com/speardragon/herdr-yazi)<br><sub>speardragon</sub> | Open Yazi in a herdr pane | `shell` | 22 | 🔄 2026-08-19 |
| [**herdr-quicklook**](https://github.com/dwarvesf/herdr-quicklook)<br><sub>dwarvesf</sub> | Quick Look for herdr: pop the clipboard's path in an overlay, escalate to the file-viewer with one key | `terminal` `shell` | 10 | 🔄 2026-08-26 |
| [**herdr-git-status**](https://github.com/ezcorp-org/herdr-git-status)<br><sub>ezcorp-org</sub> | herdr plugin: per-space git working-tree status (staged/modified/untracked/conflicts) in the sidebar, next to the branch | `rust` | 9 | 2026-08-10 |
| [**herdr-context.nvim**](https://github.com/makyinmars/herdr-context.nvim)<br><sub>makyinmars</sub> | From Neovim, select code or stand on a line, choose a live Herdr agent, and stage structured context in that agent’s prompt—without submitting it. | `lua` | 8 | 🔄 2026-08-26 |
| [**herdr-workbench**](https://github.com/azizuysal/herdr-workbench)<br><sub>azizuysal</sub> | A polished project sidebar for Herdr with Explorer, live file and content search, read-only Source Control, rich previews, file icons, and Git decorations. | `rust` | 6 | 2026-08-07 |
| [**herdr-flist**](https://github.com/devskale/herdr-flist)<br><sub>devskale</sub> | herdr - file list plugin | `python` | 5 | 2026-07-10 |
| [**herdr-markdown-viewer**](https://github.com/arvindparmar-me/herdr-markdown-viewer)<br><sub>arvindparmar-me</sub> | Herdr plugin: drag-select a markdown path and press prefix+m to preview it in a right-split pane. | `shell` | 4 | 2026-07-17 |
| [**herdr-fresh**](https://github.com/rvalledorjr/herdr-fresh)<br><sub>rvalledorjr</sub> | A herdr plugin that runs Fresh, the terminal IDE, as a file viewer and editor inside a herdr pane. | `developer-tools` `editor` `fresh` `ide` `terminal` | 4 | 2026-07-17 |
| [**herdr-plugin-mermaid-preview**](https://github.com/Volpestyle/herdr-plugin-mermaid-preview)<br><sub>Volpestyle</sub> | Live Mermaid previews for Claude Code and Codex output in Herdr | `claude-code` `mermaid` `openai-codex` `terminal` `javascript` | 4 | 2026-07-10 |
| [**openloc.nvim**](https://github.com/Zamua/openloc.nvim)<br><sub>Zamua</sub> | Open file references in the Neovim that already belongs to the workspace | `lua` | 4 | 🔄 2026-08-25 |
| [**herdr-wait**](https://github.com/cdc-lst/herdr-wait)<br><sub>cdc-lst</sub> | Configurable herdr plugin that tags an idle agent pane with what it's really doing — e.g. 'waiting: build-api' or 'waiting: codex' — matched from the pane's pr… | `typescript` | 3 | 2026-07-03 |
| [**herdr-file-viewer**](https://github.com/ismaelosuna7824/herdr-file-viewer)<br><sub>ismaelosuna7824</sub> | A keyboard-driven file explorer, code viewer and git client in a single Herdr pane — Go + Bubble Tea. | `bubbletea` `git` `golang` `tui` `go` | 3 | 2026-08-08 |
| [**herdr-lazygit**](https://github.com/JacquesvanWyk/herdr-lazygit)<br><sub>JacquesvanWyk</sub> | Open lazygit in a herdr split pane or tab with smart toggle (open / focus / close) | `lazygit` `shell` | 3 | 2026-07-12 |
| [**herdr-yazi-windows**](https://github.com/Only-Moon/herdr-yazi-windows)<br><sub>Only-Moon</sub> | Windows port of herdr-yazi with native Windows pane spawning support via herdr v0.8+ | `file` `file-manager` `pidotdev` `python` `tui` | 3 | 2026-08-14 |
| [**herdr-x**](https://github.com/playsthisgame/herdr-x)<br><sub>playsthisgame</sub> | Browse x.com in a terminal split inside herdr, and draft posts in $EDITOR to send yourself. | `cli` `terminal` `terminal-browser` `twitter` `shell` | 3 | 🔄 2026-08-20 |
| [**advanced-herdr-file-viewer**](https://github.com/thuanlm215/advanced-herdr-file-viewer)<br><sub>thuanlm215</sub> | Git-aware file viewer for Herdr: full-text and file search (workspace or folder), context actions that open workspaces and panes, Unicode/Nerd icons, independe… | `file-viewer` `ripgrep` `rust` `tui` | 3 | 🔄 2026-08-25 |
| [**🆕 dotfiles**](https://github.com/tifandotme/dotfiles)<br><sub>tifandotme</sub> | ~/.* | `aerospace` `chezmoi` `cmux` `dotfiles` `ghostty` | 3 | 🔄 2026-09-01 |
| [**herdr-open-in-editor**](https://github.com/timofey-TK/herdr-open-in-editor)<br><sub>timofey-TK</sub> | Open local and remote Herdr workspaces in VS Code or Zed | `vscode` `zed` `python` | 3 | 2026-07-30 |
| [**herdr-claude-usage-multi**](https://github.com/iamhouser/herdr-claude-usage-multi)<br><sub>iamhouser</sub> | Claude plan usage gauges in the Herdr sidebar - Session/Week %, color escalation, countdown to reset, multi-account via CLAUDE_CONFIG_DIR profiles | `claude-code` `python` | 2 | 2026-07-25 |
| [**🆕 scp-explorer**](https://github.com/TinocoAI/scp-explorer)<br><sub>TinocoAI</sub> | MobaXterm-style SCP file explorer herdr plugin (cross-platform macOS/Linux/Windows) | `curses` `file-manager` `scp` `python` | 2 | 🔄 2026-08-31 |
| [**herdr-launcher-pane**](https://github.com/y-hirakaw/herdr-launcher-pane)<br><sub>y-hirakaw</sub> | Docked click-to-launch pane for herdr — Finder/Explorer, VS Code, or any command you configure, per workspace | `launcher` `launcher-pane` `productivity` `python` | 2 | 2026-08-10 |
| [**herdr-flutter**](https://github.com/ablause/herdr-flutter)<br><sub>ablause</sub> | A herdr sidebar to watch, hot reload and inspect a running Flutter app beside the coding agent. | `dart` | 1 | 2026-07-27 |
| [**herdr-goto**](https://github.com/asumaran/herdr-goto)<br><sub>asumaran</sub> | Tree-style switcher across herdr repos, worktrees and panes | `go` | 1 | 🔄 2026-08-23 |
| [**herdr-file-viewer**](https://github.com/jomarmontuya/herdr-file-viewer)<br><sub>jomarmontuya</sub> | Right-side Herdr file tree plugin with file tabs, cwd following, git decorations, and clickable links | `go` | 1 | 2026-07-13 |
| [**herdr-yazi-explorer**](https://github.com/pjs-0457/herdr-yazi-explorer)<br><sub>pjs-0457</sub> | Open Yazi in a herdr tab/split, labeled 🗂 yazi, in the workspace you triggered it from; auto-restarts on quit. | `yazi` `shell` | 1 | 2026-08-13 |
| [**herdr-terminal-file-manager**](https://github.com/robert-flo/herdr-terminal-file-manager)<br><sub>robert-flo</sub> | A thin herdr wrapper for the elio file manager. It detects your active directory and launches elio natively, bringing its snappy previews, inline images, and b… | `shell` | 1 | 2026-07-10 |
| [**herdr-numbered-workspaces**](https://github.com/abrose/herdr-numbered-workspaces)<br><sub>abrose</sub> | Puts a number in front of every space in herdr's sidebar, matching the indexed switch_workspace shortcut. | `shell` | 0 | 2026-07-21 |
| [**herdr-cursor-open**](https://github.com/alex-devdone/herdr-cursor-open)<br><sub>alex-devdone</sub> | Open the focused herdr pane in Cursor or VS Code — including panes attached to a remote herdr, over Remote-SSH | `cursor` `vscode` `shell` | 0 | 🔄 2026-08-23 |
| [**herdr-preview**](https://github.com/AlexanderMakarov/herdr-preview)<br><sub>AlexanderMakarov</sub> | Herdr plugin: letter-hint file paths in the visible pane and open them in file-viewer or less | `rust` | 0 | 🔄 2026-08-29 |
| [**herdr_plugin**](https://github.com/Andreslvc/herdr_plugin)<br><sub>Andreslvc</sub> | Herdr plugin: open pane folder in VS Code, copy path, and open a folder as a space. | `python` | 0 | 🔄 2026-08-24 |
| [**herdr-context**](https://github.com/Anthodev/herdr-context)<br><sub>Anthodev</sub> | Project context dock for herdr — file tree with git status and LLM conversation history, always at your agent's side | `git` `jj` `ratatui` `rust` `sidebar` | 0 | 🔄 2026-08-31 |
| [**herdr-ctx**](https://github.com/aorumbayev/herdr-ctx)<br><sub>aorumbayev</sub> | Claude context-window indicator for herdr sidebar panes | `typescript` | 0 | 2026-07-21 |
| [**Renderd**](https://github.com/Brutheron/Renderd)<br><sub>Brutheron</sub> | Live Markdown reader for completed Claude Code and Codex responses in Herdr | `go` | 0 | 2026-08-15 |
| [**herdr-sidebar-plugin**](https://github.com/caoool/herdr-sidebar-plugin)<br><sub>caoool</sub> | _(no description)_ | `typescript` | 0 | 🔄 2026-09-01 |
| [**herdr-sidebar-numbers**](https://github.com/cedrus-8864/herdr-sidebar-numbers)<br><sub>cedrus-8864</sub> | herdr plugin: show workspace and agent position numbers in the sidebar, matching the 1..9 shortcut digits | `ai-agents` `bun` `sidebar` `terminal` `javascript` | 0 | 2026-08-04 |
| [**🆕 herdr-jetbrains**](https://github.com/chenyao0910/herdr-jetbrains)<br><sub>chenyao0910</sub> | Open the active Herdr workspace or worktree in Rider, WebStorm, IntelliJ IDEA, or GoLand. | `developer-tools` `git-worktree` `goland` `intellij-idea` `jetbrains` | 0 | 🔄 2026-08-30 |
| [**herdr-codex-cost**](https://github.com/Coolsik/herdr-codex-cost)<br><sub>Coolsik</sub> | Show estimated Codex session cost in the Herdr sidebar | `codex` `shell` | 0 | 2026-07-31 |
| [**herdr-tab-badges**](https://github.com/CowboyVang/herdr-tab-badges)<br><sub>CowboyVang</sub> | Sidebar badge on herdr spaces that hold more than one tab. | `shell` | 0 | 2026-07-21 |
| [**🆕 herdr-tab-git**](https://github.com/hasuwini77/herdr-tab-git)<br><sub>hasuwini77</sub> | Git branch and status in the Herdr Spaces sidebar that follow the active tab instead of the first one | `git` `terminal` `tui` `javascript` | 0 | 🔄 2026-08-28 |
| [**herdr-plugin-mado**](https://github.com/hidekingerz/herdr-plugin-mado)<br><sub>hidekingerz</sub> | herdr plugins that open agent-written markdown in mado, a TUI viewer, beside the agent writing it | `mado` `markdown` `tui` `shell` | 0 | 🔄 2026-08-24 |
| [**🆕 herdr-nvim**](https://github.com/jtnovellis/herdr-nvim)<br><sub>jtnovellis</sub> | Neovim inside Herdr: a per-tab full-height sidebar, and a real round trip with your coding agent — ask about the code you're looking at, read the answer withou… | `ai-agents` `claude-code` `developer-tools` `lua` `neovim` | 0 | 🔄 2026-08-31 |
| [**herdr-plugin-agent-repo**](https://github.com/khatriafaz/herdr-plugin-agent-repo)<br><sub>khatriafaz</sub> | Herdr plugin that shows agent, repository, and branch names in agent pane headers and the sidebar. | `javascript` | 0 | 2026-07-24 |
| [**herdr-nnn**](https://github.com/linuxing3/herdr-nnn)<br><sub>linuxing3</sub> | open nnn in herder | `shell` | 0 | 2026-08-04 |
| [**herdr-cmux-file-viewer**](https://github.com/linvald/herdr-cmux-file-viewer)<br><sub>linvald</sub> | herdr plugin that syncs cmux's file viewer to the currently focused herdr space | `python` | 0 | 2026-07-23 |
| [**herdr-openmd**](https://github.com/RufusLin/herdr-openmd)<br><sub>RufusLin</sub> | Open selected markdown in openmd — a rich Qt preview from herdr | `shell` | 0 | 2026-07-29 |
| [**herdr-git-detail**](https://github.com/sfroment/herdr-git-detail)<br><sub>sfroment</sub> | herdr plugin: rich git status (modified/staged/untracked/ahead/behind/stash) as a $git_detail sidebar token. | `developer-tools` `git` `shell` `starship` `terminal` | 0 | 2026-08-05 |
| [**herdr-gitui**](https://github.com/Shi1xin/herdr-gitui)<br><sub>Shi1xin</sub> | herdr plugin: gitui in a sidebar pane — open/toggle, expand, light/dark themes | `gitui` `python` | 0 | 2026-07-28 |
| [**meadow**](https://github.com/Tetat-Chulchue/meadow)<br><sub>Tetat-Chulchue</sub> | Mouse-driven file explorer pane for the herdr terminal multiplexer | `python` | 0 | 2026-07-21 |
| [**dotfiles**](https://github.com/Unique-Divine/dotfiles)<br><sub>Unique-Divine</sub> | Dotfiles and other ~ configuration from Unique Divine | `dotfiles` `lua` `neovim` `neovim-dotfiles` `nvim` | 0 | 🔄 2026-08-31 |
| [**herdr-cmux-cwd-sync**](https://github.com/WerrySs/herdr-cmux-cwd-sync)<br><sub>WerrySs</sub> | Non-invasive cmux file explorer sync for the focused HerdR pane | `cmux` `macos` `python` | 0 | 2026-08-14 |

<details><summary>Also relevant to this purpose</summary>

- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) — A code-review + file-viewer sidebar for herdr — comment on an agent's diff, send it back. Plus a read-only vi…
- [ChmaraX/herdr-gitview](https://github.com/ChmaraX/herdr-gitview) — Git status/diff panel for herdr - review changes, edit in nvim, stage/commit/discard, all from the terminal
- [vonzelle-vzt/herdr-extensions](https://github.com/vonzelle-vzt/herdr-extensions) — Tiny VS Code for herdr: a real editor with LSP diagnostics, autocomplete, rename and go-to-definition — plus…
- [jsmenzies/mergr](https://github.com/jsmenzies/mergr) — GitHub pull request status for Herdr Space sidebar rows.
- [maedana/herdr-whereami](https://github.com/maedana/herdr-whereami) — Herdr plugin that automatically renames tabs to show where you are, e.g. repo-name/branch when inside a git r…
- [bayoudhi/herdr-prayer-times](https://github.com/bayoudhi/herdr-prayer-times) — Next Islamic prayer and countdown in the Herdr sidebar, with a timetable popup and notifications
- [brianh20/herdr-stagr](https://github.com/brianh20/herdr-stagr) — Source Control sidebar for herdr: stage, unstage, and discard with side-by-side diffs
- [ctbaum/herdr-deck](https://github.com/ctbaum/herdr-deck) — The companion workspace launcher for herdr-agents.nvim: open or resume Claude and Codex in a ready-made Neovi…
- [ZingerLittleBee/herdr-agent-pins](https://github.com/ZingerLittleBee/herdr-agent-pins) — Persistently pin Herdr agent sessions to the top of the Agents sidebar.
- [caner-akca/herdr-plugin-atomic-workflows](https://github.com/caner-akca/herdr-plugin-atomic-workflows) — Herdr plugin: launch and monitor isolated Atomic workflow tasks — campaign board, sidebar tokens, run ledger,…
- [Gareth-Rouse/herdr-plugin-session-pruner](https://github.com/Gareth-Rouse/herdr-plugin-session-pruner) — Herdr plugin: track workspace last-use, show the age in the Spaces sidebar, and keep cold workspaces out of t…
- [jovylle/herdr-session-title-name](https://github.com/jovylle/herdr-session-title-name) — Herdr plugin: terminal_title_stripped → tab persistence (session_title alone on top, tab keeps it after close)
- [limars874/herdr-pane-id-metadata](https://github.com/limars874/herdr-pane-id-metadata) — Minimal Herdr plugin for canonical pane IDs and compact tab/pane sidebar metadata
- [NachoPal/herdr-pane-agent-unread](https://github.com/NachoPal/herdr-pane-agent-unread) — Per-pane 'unread' notifier + sidebar badge for herdr - surfaces agents that finish or need input in panes you…
- [ubuntudroid/herdr-git-stack](https://github.com/ubuntudroid/herdr-git-stack) — Herdr plugin: shows each space's position in its git branch stack in the spaces sidebar, flags branches whose…
- [yojahny55/herdr-space-groups](https://github.com/yojahny55/herdr-space-groups) — Herdr plugin: group Spaces into named, colored groups — picker popup (mouse + keyboard), sidebar group header…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-cost"></a>

## Tokens & Cost

> I want to see how much an agent is spending, and cut down on usage

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**memex**](https://github.com/nicosuave/memex)<br><sub>nicosuave</sub> | Search Claude Code, Codex, Pi, OpenCode, Github Copilot & Cursor transcripts. Resume sessions. Track tokens. | `bm25` `claude-code` `codex-cli` `hybrid-search` `rag` | 181 | 🔄 2026-09-01 |
| [**llmtrim-herdr**](https://github.com/fkiene/llmtrim-herdr)<br><sub>fkiene</sub> | 💸 Shrink your token bill in herdr: compresses every agent pane's requests (-31% input / -74% output, measured live) and shows the savings on a per-pane badge | `llm-proxy` `llmtrim` `powershell` | 40 | 2026-07-02 |
| [**herdr-agent-usage**](https://github.com/senna-lang/herdr-agent-usage)<br><sub>senna-lang</sub> | Context meters and provider rate limits for agents running in Herdr. | `ai-agents` `claude-code` `codex` `golang` `rate-limiting` | 28 | 🔄 2026-09-01 |
| [**herdr-token-dashboard**](https://github.com/Davidcreador/herdr-token-dashboard)<br><sub>Davidcreador</sub> | Live token spend dashboard and notifications for Herdr agent panes | `ai-agents` `bubbletea` `opencode` `pi-agent` `token-dashboard` | 18 | 2026-08-13 |
| [**herdr-claude-usage**](https://github.com/alejodelosrios/herdr-claude-usage)<br><sub>alejodelosrios</sub> | Stop opening a Claude session just to check your quota. Live Claude plan usage — Session % \| Week % — always visible in your Herdr sidebar, shared across ever… | `claude` `claude-code` `python` | 3 | 2026-07-21 |
| [**herdr-opentab**](https://github.com/hamidi-dev/herdr-opentab)<br><sub>hamidi-dev</sub> | Live per-agent AI spend from OpenTab in the Herdr sidebar. | `ai-agents` `opentab` `terminal` `python` | 3 | 🔄 2026-08-18 |
| [**herdr-gekiatsu-plugin**](https://github.com/yuuta1219/herdr-gekiatsu-plugin)<br><sub>yuuta1219</sub> | herdr plugin: Claude Code usage counter, but it's a pachislot machine. 1/99 jackpot, daily reset at 10:00 JST | `claude` `claude-code` `python` `tui` | 3 | 2026-08-17 |
| [**herdr-api-credit-bar**](https://github.com/CristianPeralta/herdr-api-credit-bar)<br><sub>CristianPeralta</sub> | Herdr plugin: remaining credit for pay-as-you-go API providers, starting with Alibaba Cloud Model Studio | `shell` | 2 | 🔄 2026-08-18 |
| [**herdr-quota**](https://github.com/kvkenyon/herdr-quota)<br><sub>kvkenyon</sub> | See Claude, Codex, Cursor, and Kimi subscription quota at a glance in Herdr. | `ai-tools` `claude-code` `cursor` `developer-tools` `kimi` | 2 | 🔄 2026-08-21 |
| [**herdr-whereami**](https://github.com/maedana/herdr-whereami)<br><sub>maedana</sub> | Herdr plugin that automatically renames tabs to show where you are, e.g. repo-name/branch when inside a git repository. | `rust` | 2 | 2026-08-14 |
| [**scopefuel**](https://github.com/mgh3326/scopefuel)<br><sub>mgh3326</sub> | Scope-aware headroom gauge for AI coding agent plans — what is actually blocked (account/model/group) and when it refills | `ai-agents` `antigravity` `claude-code` `cli` `codex` | 1 | 2026-08-15 |
| [**herdr-usage-bar**](https://github.com/silverwolfdoc/herdr-usage-bar)<br><sub>silverwolfdoc</sub> | Usage limits and context meters for AI agents in Herdr, with a compact bottom usage bar. | `go` | 1 | 🔄 2026-08-27 |
| [**herdr-model-lanes**](https://github.com/terry-li-hm/herdr-model-lanes)<br><sub>terry-li-hm</sub> | Herdr plugin: Codex, Claude Max and Grok quota in the workspace row, plus quota-aware model-class lanes (ag) for new agents | `claude` `codex` `grok` `model-routing` `quota` | 1 | 🔄 2026-08-30 |
| [**herdr-usage**](https://github.com/Efeguclu1/herdr-usage)<br><sub>Efeguclu1</sub> | Compact account-usage marks on Herdr agent tabs for Claude, Codex, Cursor, OpenCode, and Pi | `claude-code` `cursor` `openai` `opencode` `python` | 0 | 🔄 2026-08-22 |
| [**herdr-web-broker**](https://github.com/JefeLabs/herdr-web-broker)<br><sub>JefeLabs</sub> | Self-hosted REST/WS API for herdr: spawn and steer coding agents from anywhere — tokens, multi-user session ownership, git verbs, event streaming, parent↔child… | `typescript` | 0 | 🔄 2026-09-01 |
| [**🆕 herdr-plugin-agent-quota**](https://github.com/kwanwooi25/herdr-plugin-agent-quota)<br><sub>kwanwooi25</sub> | Agent quota for Herdr — token & cost dashboard, sidebar quota gauges, and tab bar summary for Claude Code, Codex, and Grok | `javascript` | 0 | 🔄 2026-08-30 |
| [**🆕 precc-herdr-plugin**](https://github.com/peria-ai/precc-herdr-plugin)<br><sub>peria-ai</sub> | PRECC plugin for herdr: cross-agent token-savings telemetry + one-touch PRECC setup | `claude-code` `precc` `shell` | 0 | 🔄 2026-09-01 |
| [**🆕 provider-usage**](https://github.com/ryus1234/provider-usage)<br><sub>ryus1234</sub> | Provider usage and quota bar for Herdr | `ai-usage` `quota-monitor` `rust` | 0 | 🔄 2026-08-31 |
| [**herdr-burn**](https://github.com/samuelbaldwin05/herdr-burn)<br><sub>samuelbaldwin05</sub> | Live Claude Code cost/quota per pane in the herdr sidebar, with a workspace-total burn overlay. | `python` | 0 | 2026-08-12 |
| [**herdr-model-capacity**](https://github.com/shrivatsas/herdr-model-capacity)<br><sub>shrivatsas</sub> | Herdr pane for account-level Claude, Codex/OpenAI, and OpenRouter capacity | `claude` `codex` `openrouter` `rust` | 0 | 🔄 2026-08-28 |
| [**🆕 herdr-status-ui-bar**](https://github.com/speardragon/herdr-status-ui-bar)<br><sub>speardragon</sub> | AI agent plan-usage gauges (Claude Code / Codex / Grok) in the herdr tab bar | `claude-code` `shell` | 0 | 🔄 2026-08-28 |
| [**🆕 herdr-context-display**](https://github.com/TheBrunoPetkovic/herdr-context-display)<br><sub>TheBrunoPetkovic</sub> | Colour-coded context window usage on every Claude Code agent row in herdr | `claude-code` `terminal` `typescript` | 0 | 🔄 2026-08-26 |
| [**🆕 pi-agent-usage**](https://github.com/w784415/pi-agent-usage)<br><sub>w784415</sub> | Pi extension that displays OpenAI Codex quota and reset times, with Herdr plugin support. | `openai-codex` `pi-extension` `pi-package` `quota` `typescript` | 0 | 🔄 2026-08-26 |
| [**claude-usage**](https://github.com/yuuta1219/claude-usage)<br><sub>yuuta1219</sub> | herdr plugin: Claude Code usage (session % / week %) pinned to the bottom of the sidebar | `claude` `claude-code` `python` `tui` | 0 | 2026-08-01 |

<details><summary>Also relevant to this purpose</summary>

- [levi-qiao/herdr-agent-quota](https://github.com/levi-qiao/herdr-agent-quota) — Credential-scoped AI quota, context, and cache in Herdr for Claude, Codex, Grok, Agy, OpenCode, Pi, and OMP.
- [caner-akca/herdr-plugin-atomic-workflows](https://github.com/caner-akca/herdr-plugin-atomic-workflows) — Herdr plugin: launch and monitor isolated Atomic workflow tasks — campaign board, sidebar tokens, run ledger,…
- [Coolsik/herdr-codex-cost](https://github.com/Coolsik/herdr-codex-cost) — Show estimated Codex session cost in the Herdr sidebar

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-monitor"></a>

## Monitoring & Dashboards

> I want an at-a-glance overview of agent and machine status

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**clauth**](https://github.com/uwuclxdy/clauth)<br><sub>uwuclxdy</sub> | Claude Code multi-account manager, usage monitor (CLI, TUI & MCP cross-account delegation) | `account-manager` `account-switcher` `anthropic` `claude` `claude-code` | 84 | 🔄 2026-09-01 |
| [**herdr-agent-quota**](https://github.com/levi-qiao/herdr-agent-quota)<br><sub>levi-qiao</sub> | Credential-scoped AI quota, context, and cache in Herdr for Claude, Codex, Grok, Agy, OpenCode, Pi, and OMP. | `agent-usage` `agy` `ai-agents` `antigravity` `claude-code` | 48 | 🔄 2026-09-02 |
| [**herdr-beads**](https://github.com/miiraheart/herdr-beads)<br><sub>miiraheart</sub> | A beads (bd) task board for herdr: List, Table, Kanban over your bd issues, docked as a sidebar or floating. | `bd` `beads` `kanban` `rust` `tui` | 15 | 🔄 2026-08-25 |
| [**herdr-pc-ram-and-cpu-usage-overlay**](https://github.com/ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay)<br><sub>ezcorp-org</sub> | herdr plugin: live CPU/RAM usage per space (workspace), as a share of the whole machine | `rust` | 14 | 🔄 2026-08-27 |
| [**herdr-telemetry**](https://github.com/DIodide/herdr-telemetry)<br><sub>DIodide</sub> | Herdr plugin that streams workspace & agent telemetry to an endpoint you control — Go, single binary, privacy-first defaults | `golang` `telemetry` `go` | 11 | 2026-07-10 |
| [**herdr-f1**](https://github.com/hmu332233/herdr-f1)<br><sub>hmu332233</sub> | An F1-style dashboard for your Herdr agents. | `agent-dashboard` `typescript` | 10 | 2026-08-13 |
| [**herdres**](https://github.com/luminexord/herdres)<br><sub>luminexord</sub> | Telegram interface for monitoring and messaging Herdr coding agents, powered by Tendwire. | `coding-agents` `telegram` `python` | 10 | 2026-08-09 |
| [**shepherd**](https://github.com/ryonakae/shepherd)<br><sub>ryonakae</sub> | Worker observability daemon and runtime bridges for Herdr-managed coding agents. | `pi-coding-agent` `pi-extension` `typescript` | 8 | 🔄 2026-08-28 |
| [**herdr-sysmon**](https://github.com/getpipher/herdr-sysmon)<br><sub>getpipher</sub> | System metrics in the Herdr sidebar — CPU, memory, battery, network, disk, clock. A faithful port of a tmux-cpu/tmux-battery/tmux-online-status status bar into… | `battery` `catppuccin` `cpu` `getpipher` `macos` | 7 | 2026-07-26 |
| [**herdr-workboard**](https://github.com/Phoobobo/herdr-workboard)<br><sub>Phoobobo</sub> | Kanban workboard TUI for herdr: boards are workspaces, task states are tabs, task sessions are panes | `kanban` `tui` `typescript` | 7 | 2026-08-10 |
| [**herdr-tally**](https://github.com/jasonrr/herdr-tally)<br><sub>jasonrr</sub> | Project-scoped todos & scratchpads for you and your agents.<br>📝 プロジェクト単位の TODO 管理 | `rust` `todo` | 6 | 🔄 2026-08-30 |
| [**🆕 herdr-lazydocker**](https://github.com/sudoeren/herdr-lazydocker)<br><sub>sudoeren</sub> | Run lazydocker in a herdr split pane or its own tab. | `docker` `lazydocker` `shell` | 6 | 🔄 2026-08-27 |
| [**herdr-kanban**](https://github.com/KokiKono/herdr-kanban)<br><sub>KokiKono</sub> | Terminal Kanban board that links tasks to herdr tabs, persisted in SQLite | `rust` | 5 | 2026-07-10 |
| [**herdr-devserver-status**](https://github.com/Razz21/herdr-devserver-status)<br><sub>Razz21</sub> | Herdr plugin that detects dev servers in panes via pluggable specs and reports lifecycle status. | `astro` `cli` `deamon` `dev-server` `extensible` | 5 | 🔄 2026-08-25 |
| [**herdr-agent-watcher**](https://github.com/winoooops/herdr-agent-watcher)<br><sub>winoooops</sub> | Coding-agent observability for Herdr: live sidebar cards, lifecycle notifications, and a zero-config Claude Code metrics bridge. | `claude-code` `rust` | 5 | 🔄 2026-08-31 |
| [**herdr-shell-progress**](https://github.com/bayoudhi/herdr-shell-progress)<br><sub>bayoudhi</sub> | Herdr plugin: live sidebar progress for slow shell commands, not just coding agents | `rust` | 3 | 2026-08-05 |
| [**adlc-herdr**](https://github.com/voodootikigod/adlc-herdr)<br><sub>voodootikigod</sub> | ADLC herdr plugin — per-pane phase/ticket/gate status, backlog board, gate actions, and adlc-fleet run observability. Auto-synced mirror of voodootikigod/adlc/… | `javascript` | 3 | 🔄 2026-08-31 |
| [**🆕 herdr-codex-bridge**](https://github.com/ardasevinc/herdr-codex-bridge)<br><sub>ardasevinc</sub> | Native Herdr pane identity for Codex sessions using a centralized app-server | `ai-agents` `codex` `terminal` `go` | 2 | 🔄 2026-09-01 |
| [**herdr-agent-dashboard**](https://github.com/carsonjones/herdr-agent-dashboard)<br><sub>carsonjones</sub> | prefix +a show herdr agents | `typescript` | 2 | 2026-07-16 |
| [**herdr-telemetry-bridge**](https://github.com/CodyBontecou/herdr-telemetry-bridge)<br><sub>CodyBontecou</sub> | Herdr plugin that streams local workspace, repo, coding-agent, model, and trace telemetry to external clients. | `coding-agents` `telemetry` `time-md` `javascript` | 2 | 2026-06-26 |
| [**herdr-agentsview**](https://github.com/cpcloud/herdr-agentsview)<br><sub>cpcloud</sub> | AgentsView activity, compressed into one very busy terminal. | `rust` | 2 | 🔄 2026-08-24 |
| [**herdr-mise**](https://github.com/funsaized/herdr-mise)<br><sub>funsaized</sub> | Run the pass, not the prompts 🧑‍🍳 A visualizer for your agents (in herdr) | `agent` `agent-monitoring` `ai-agents` `cli-tool` `developer-tools` | 2 | 🔄 2026-09-01 |
| [**herdr-statusline**](https://github.com/iiii1224/herdr-statusline)<br><sub>iiii1224</sub> | Customizable status line for herdr sessions. | `cli` `statusbar` `statusline` `tmux` `python` | 2 | 2026-08-15 |
| [**shepherd**](https://github.com/jwarykowski/shepherd)<br><sub>jwarykowski</sub> | your todos herded | `cli` `developer-tools` `go-lang` `productivity` `task-management` | 2 | 🔄 2026-08-21 |
| [**herdr-portal**](https://github.com/loofare/herdr-portal)<br><sub>loofare</sub> | Mission-control dashboard for herdr — aggregates every workspace/tab/pane agent into a live TUI kanban (keyboard + mouse) plus a web big-screen: structured pro… | `agent-dashboard` `agent-monitor` `ai-agents` `claude-code` `codex` | 2 | 🔄 2026-08-20 |
| [**herdr-cache-ttl**](https://github.com/nytafar/herdr-cache-ttl)<br><sub>nytafar</sub> | Herdr plugin: live prompt-cache TTL countdown per agent pane | `rust` | 2 | 2026-08-05 |
| [**herdr-slurm**](https://github.com/quan-meng/herdr-slurm)<br><sub>quan-meng</sub> | Create Herdr workspaces and monitored agent tabs for Slurm allocations | `hpc` `slurm` `terminal-multiplexer` `python` | 2 | 2026-08-13 |
| [**herdr-tilt**](https://github.com/the-inconvenience-store/herdr-tilt)<br><sub>the-inconvenience-store</sub> | A keyboard-driven Tilt dashboard for Herdr | `k8s` `kubernetes` `tilt` `rust` | 2 | 🔄 2026-08-24 |
| [**herdr-agent-state**](https://github.com/Tyru5/herdr-agent-state)<br><sub>Tyru5</sub> | Realtime agent status pane for herdr; what each agent in the workspace is working on (in a more human-readable format) | `claude-code` `rust` `terminal` | 2 | 2026-08-05 |
| [**herdr-memex-analytics**](https://github.com/vishnutskumar/herdr-memex-analytics)<br><sub>vishnutskumar</sub> | Herdr plugin: session efficiency analytics and realtime agent guidance, powered by memex history | `rust` | 2 | 🔄 2026-09-01 |
| [**herdr-cache-timer**](https://github.com/ArteenHD/herdr-cache-timer)<br><sub>ArteenHD</sub> | Shows when each agent's prompt cache expires, right in the Herdr sidebar. | `claude-code` `prompt-caching` `terminal` `javascript` | 1 | 2026-08-08 |
| [**🆕 herdr-glance**](https://github.com/arvmaan/herdr-glance)<br><sub>arvmaan</sub> | desktop widget to view the status of your agents | `rust` | 1 | 🔄 2026-08-26 |
| [**herdr-tokscale-dashboard**](https://github.com/astkaasa/herdr-tokscale-dashboard)<br><sub>astkaasa</sub> | Open Tokscale as a local Herdr dashboard pane. | `dashboard` `tokscale` `shell` | 1 | 2026-06-26 |
| [**herdr-plugin-codex-subs**](https://github.com/benkraus/herdr-plugin-codex-subs)<br><sub>benkraus</sub> | Herdr dashboard for CLIProxyAPI Codex subscription quotas and reset credits | `go` | 1 | 2026-07-30 |
| [**🆕 herdr-spinner**](https://github.com/hasuwini77/herdr-spinner)<br><sub>hasuwini77</sub> | Animated braille spinner for Herdr panes in the working state, via display-only pane metadata | `spinner` `terminal` `tui` `javascript` | 1 | 🔄 2026-08-27 |
| [**🆕 herdr-overview**](https://github.com/iamgp/herdr-overview)<br><sub>iamgp</sub> | Mission Control / Exposé for Herdr — a live tiled overview of every space | `terminal` `tui` `javascript` | 1 | 🔄 2026-08-28 |
| [**herdr-jira-board**](https://github.com/kiitosu/herdr-jira-board)<br><sub>kiitosu</sub> | Jira kanban board inside herdr with Claude Code session launcher | `python` | 1 | 🔄 2026-08-30 |
| [**herdr-compose**](https://github.com/mattyan1053/herdr-compose)<br><sub>mattyan1053</sub> | Herdr Plugin for docker compose | `terminal` `tui` `shell` | 1 | 2026-07-24 |
| [**herdr-pulse**](https://github.com/moneycaringcoder/herdr-pulse)<br><sub>moneycaringcoder</sub> | Per-workspace agent activity history for herdr, rendered as a sidebar sparkline. | `monitoring` `rust` `sparkline` `terminal` | 1 | 🔄 2026-09-01 |
| [**herdr-ports**](https://github.com/Numbered-com/herdr-ports)<br><sub>Numbered-com</sub> | Surface active dev servers in herdr: a generic $ports badge on every Space running at least one TCP listener | `pids` `ports` `shell` | 1 | 2026-07-23 |
| [**herdr-readpending**](https://github.com/rcosteira79/herdr-readpending)<br><sub>rcosteira79</sub> | Mark agents you haven't finished reading. Numbered badge ($read) + a reorderable list pane. Auto-clears when you focus the agent. | `python` | 1 | 🔄 2026-08-24 |
| [**herdr-agent-metrics**](https://github.com/szrenwei/herdr-agent-metrics)<br><sub>szrenwei</sub> | Lightweight Herdr context and session usage metrics for Claude Code, Codex, and TraeX. | `claude-code` `openai-codex` `traex` `python` | 1 | 2026-08-04 |
| [**herdr-space-tab-metadata**](https://github.com/szrenwei/herdr-space-tab-metadata)<br><sub>szrenwei</sub> | Show each Herdr Space's active tab in the sidebar | `terminal-ui` `python` | 1 | 2026-08-04 |
| [**taskherd**](https://github.com/ukwhatn/taskherd)<br><sub>ukwhatn</sub> | Task board linked to herdr agent sessions, PRs, and Jira tickets | `claude-code` `kanban` `task-management` `tui` `go` | 1 | 🔄 2026-09-01 |
| [**🆕 herdr-activity-age**](https://github.com/1Morganmore/herdr-activity-age)<br><sub>1Morganmore</sub> | Windows Herdr plugin that shows time since each agent's last status change | `powershell` `windows` | 0 | 🔄 2026-08-30 |
| [**herdr-docker**](https://github.com/abcxff/herdr-docker)<br><sub>abcxff</sub> | Keep track of docker builds like you do with agents for herdr. | `docker` `javascript` | 0 | 2026-08-12 |
| [**🆕 herdr-claude-usage**](https://github.com/anyaachan/herdr-claude-usage)<br><sub>anyaachan</sub> | Global Claude Code plan usage in Herdr: tab-bar summary + popup dashboard. statusLine-powered, multi-account aware. | `claude` `claude-code` `cli` `terminal` `shell` | 0 | 🔄 2026-09-01 |
| [**herdr-ios-build-status-plugin**](https://github.com/atomsbaza/herdr-ios-build-status-plugin)<br><sub>atomsbaza</sub> | On-demand iOS build+test status pane for Herdr, with failure screenshots | `shell` | 0 | 2026-08-06 |
| [**herdr-nodejs-center**](https://github.com/AZenking/herdr-nodejs-center)<br><sub>AZenking</sub> | A Herdr popup for monitoring and focusing local Node.js, Bun, and Deno services | `developer-tools` `nodejs` `javascript` | 0 | 🔄 2026-08-20 |
| [**🆕 herdr-plugin-atomic-workflows**](https://github.com/caner-akca/herdr-plugin-atomic-workflows)<br><sub>caner-akca</sub> | Herdr plugin: launch and monitor isolated Atomic workflow tasks — campaign board, sidebar tokens, run ledger, and an optional Telegram cockpit | `javascript` | 0 | 🔄 2026-09-01 |
| [**herdr-jcode-integration**](https://github.com/capt-marbles/herdr-jcode-integration)<br><sub>capt-marbles</sub> | Herdr plugin for Jcode lifecycle state and session reporting | `jcode` `shell` | 0 | 2026-08-09 |
| [**herdr-dev-servers**](https://github.com/carellano/herdr-dev-servers)<br><sub>carellano</sub> | Discover and safely manage development servers running in Herdr panes. | `developer-tools` `go` `terminal` | 0 | 2026-08-12 |
| [**herdr-agent-metadata**](https://github.com/choplin/herdr-agent-metadata)<br><sub>choplin</sub> | Show when each Herdr agent's semantic state was last observed changing. | `go` | 0 | 🔄 2026-08-26 |
| [**herdr-repository-identity**](https://github.com/choplin/herdr-repository-identity)<br><sub>choplin</sub> | Report each Herdr workspace's shared Git repository identity. | `go` | 0 | 🔄 2026-08-24 |
| [**herdr-process-guard**](https://github.com/Efeguclu1/herdr-process-guard)<br><sub>Efeguclu1</sub> | Explain and safely stop dev servers left running by coding agents. | `claude-code` `codex` `coding-agents` `cursor` `macos` | 0 | 🔄 2026-08-24 |
| [**herdr-vitals**](https://github.com/ericcparsons/herdr-vitals)<br><sub>ericcparsons</sub> | macOS herdr plugin: CPU/RAM per agent and active dev server ports per space, in the sidebar, plus a popup to kill them | `bun` `developer-tools` `terminal` `typescript` | 0 | 2026-07-29 |
| [**herdr-kanban**](https://github.com/hassox/herdr-kanban)<br><sub>hassox</sub> | Workspace panes as a kanban board. | `go` | 0 | 🔄 2026-08-21 |
| [**🆕 herdr-ports**](https://github.com/ivorpad/herdr-ports)<br><sub>ivorpad</sub> | Herdr plugin: a popup that lists listening ports, names the project behind each one, and kills or opens it | `tui` `python` | 0 | 🔄 2026-08-27 |
| [**🆕 herdr-reap**](https://github.com/ivorpad/herdr-reap)<br><sub>ivorpad</sub> | Herdr plugin: every agent's lifecycle state, and one keystroke to close the finished ones | `tui` `python` | 0 | 🔄 2026-08-27 |
| [**herdr-metrics**](https://github.com/jordanhawkes/herdr-metrics)<br><sub>jordanhawkes</sub> | Context, session-token and account-limit metrics for Claude Code, Codex and TraeX in the Herdr sidebar. Maintained continuation of szrenwei/herdr-agent-metrics. | `claude-code` `openai-codex` `traex` `tui` `python` | 0 | 🔄 2026-08-22 |
| [**herdr-last-used**](https://github.com/MorganCollins/herdr-last-used)<br><sub>MorganCollins</sub> | Show when each herdr agent was last active, colour-coded by age, and filter the Agent sidebar by activity. | `terminal` `shell` | 0 | 🔄 2026-08-24 |
| [**herdr-phin-board**](https://github.com/phin-tech/herdr-phin-board)<br><sub>phin-tech</sub> | Herdr plugin: a status board over your spaces — todo, in progress, waiting on someone, done, plus any status you invent. List or kanban. | `bubbletea` `tui` `go` | 0 | 2026-07-29 |
| [**herdr-idle-shell-badge**](https://github.com/rcosteira79/herdr-idle-shell-badge)<br><sub>rcosteira79</sub> | Badges idle agents that still have background shells running | `python` | 0 | 🔄 2026-08-26 |
| [**colloquy**](https://github.com/SoMaCoSF/colloquy)<br><sub>SoMaCoSF</sub> | Self-addressing, ephemerally-cached causal DAG audit logs and telemetry for agent swarms. | `colloquy` `gyst` `javascript` | 0 | 2026-07-29 |
| [**🆕 herdr-claude-context-meter**](https://github.com/tmastalirsch/herdr-claude-context-meter)<br><sub>tmastalirsch</sub> | herdr plugin: Claude Code context usage as a bar — in the status line and in a herdr pane | `claude-code` `context-window` `statusline` `shell` | 0 | 🔄 2026-08-27 |
| [**🆕 herdr-workspace-board**](https://github.com/tmastalirsch/herdr-workspace-board)<br><sub>tmastalirsch</sub> | herdr plugin: one line per git repository with unfinished work, ranked by how likely it is to be forgotten | `git` `productivity` `workspace` `shell` | 0 | 🔄 2026-08-27 |
| [**conflux-herdr**](https://github.com/tumf/conflux-herdr)<br><sub>tumf</sub> | Herdr plugin pane for running the Conflux TUI and reporting its lifecycle state. | `shell` | 0 | 2026-07-26 |
| [**herdr-hud**](https://github.com/zetlen/herdr-hud)<br><sub>zetlen</sub> | Herdr plugin: keybound popup of host, network, agent, and session facts — configurable, extensible via custom script | `bash` `terminal` `shell` | 0 | 2026-08-03 |

<details><summary>Also relevant to this purpose</summary>

- [nelsonPires5/herdr-board](https://github.com/nelsonPires5/herdr-board) — Kanban board for herdr — cards are prompts dispatched to AI agents in visible panes
- [quaywin/agys](https://github.com/quaywin/agys) — Effortless multi-profile isolation & real-time quota tracking for Antigravity CLI in Herdr via zero-pollution…
- [e2b-dev/herdr-e2b-sandbox](https://github.com/e2b-dev/herdr-e2b-sandbox) — herdr plugin that mirrors a git worktree into an E2B sandbox — one box or a branch-per-agent fleet, with a TU…
- [Northern-Lighthouse/herdr-fleet](https://github.com/Northern-Lighthouse/herdr-fleet) — Manage a fleet of herdr machines over Tailscale: dashboard plugin, auto-discovery, capacity-aware agent dispa…
- [cdowell09/herdr-pr-board](https://github.com/cdowell09/herdr-pr-board) — Configurable cross-repository GitHub pull request dashboard for Herdr
- [bengemine/herdr-hibernate](https://github.com/bengemine/herdr-hibernate) — Hibernate idle coding-agent panes in Herdr (Claude Code, Codex, Grok) — free the RAM, press Enter to resume t…
- [IvoryHeart/herdr-world](https://github.com/IvoryHeart/herdr-world) — Herdr World — a multi-surface web experience for Herdr
- [Javamomma/herdr-scribe](https://github.com/Javamomma/herdr-scribe) — herdr plugin: live no-recording meeting transcription — mic → RAM-only transcript + live analyst panes; on st…
- [sazardev/herdr-code-board](https://github.com/sazardev/herdr-code-board) — Kanban queue for agentic prompts inside Herdr: cards dispatch real agents into panes, worktrees and workspace…
- [chouxcreams/herdr-dashboard](https://github.com/chouxcreams/herdr-dashboard) — PR status dashboard TUI for herdr workspaces — PR state / CI / reviews per pane at a glance
- [GranamyrBR/LunaCrab](https://github.com/GranamyrBR/LunaCrab) — Reserved for a separate project
- [maedana/herdr-agents-preview](https://github.com/maedana/herdr-agents-preview) — Multi-agent terminal preview dashboard for Herdr: all running agents shown at once, with the selected agent t…
- [GranamyrBR/ezdras-herdr](https://github.com/GranamyrBR/ezdras-herdr) — Live multi-agent observability and pane controls for Herdr
- [peria-ai/precc-herdr-plugin](https://github.com/peria-ai/precc-herdr-plugin) — PRECC plugin for herdr: cross-agent token-savings telemetry + one-touch PRECC setup
- [ryus1234/provider-usage](https://github.com/ryus1234/provider-usage) — Provider usage and quota bar for Herdr

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-finder"></a>

## Fuzzy Finders & Palettes

> I want to invoke commands or projects even when I only half-remember their names

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-navigator**](https://github.com/thanhdat77/herdr-navigator)<br><sub>thanhdat77</sub> | Jump to any Herdr workspace, agent, project, session, remote, directory, or action from one fuzzy navigator. | `fuzzy-finder` `rust` `terminal` `workspace-manager` | 127 | 🔄 2026-08-25 |
| [**termscope**](https://github.com/iurysza/termscope)<br><sub>iurysza</sub> | Open files and links already visible on your terminal screen in a split. | `python` `television` `terminal` `tmux` | 50 | 🔄 2026-08-19 |
| [**herdr-sessionizer**](https://github.com/andrewchng/herdr-sessionizer)<br><sub>andrewchng</sub> | Fuzzy-open projects and worktrees, then bootstrap workspaces from declarative TOML layouts — tabs, pane splits, commands, and per-repo overrides. | `bun` `fuzzy-finder` `fzf` `git-worktree` `sessionizer` | 44 | 🔄 2026-09-02 |
| [**herdr-plugin-sesh**](https://github.com/fullerzz/herdr-plugin-sesh)<br><sub>fullerzz</sub> | Sesh-style workspace picker TUI for Herdr. Integrates with zoxide to create workspaces from commonly used directories. | `bubbletea` `sesh` `tui` `zoxide` `go` | 36 | 🔄 2026-09-02 |
| [**herdr-command-palette**](https://github.com/JanTvrdik/herdr-command-palette)<br><sub>JanTvrdik</sub> | fzf command palette for herdr — fuzzy-pick and run any plugin action | `shell` | 34 | 2026-06-29 |
| [**herdr-bar**](https://github.com/jeffarese/herdr-bar)<br><sub>jeffarese</sub> | Cmd+K for herdr: fuzzy-jump to any tab, agent, repo or branch. Python stdlib only. | `command-bar` `fuzzy-finder` `python` `terminal` `tui` | 30 | 🔄 2026-08-31 |
| [**herdr-drovr**](https://github.com/AVGVSTVS96/herdr-drovr)<br><sub>AVGVSTVS96</sub> | easily move herdr panes and tabs | `fzf` `terminal` `javascript` | 14 | 2026-08-08 |
| [**herdr-zoxide**](https://github.com/den-tanui/herdr-zoxide)<br><sub>den-tanui</sub> | Herdr plugin to create workspaces, tabs and panes from zoxide directories. | `zoxide` `shell` | 11 | 2026-07-25 |
| [**herdr-palette**](https://github.com/ramarivera/herdr-palette)<br><sub>ramarivera</sub> | A Rust/Ratatui fuzzy command palette for Herdr workspaces. | `command-palette` `ratatui` `rust` `terminal` `tui` | 8 | 2026-08-14 |
| [**🆕 herdr-palette**](https://github.com/vjeantet/herdr-palette)<br><sub>vjeantet</sub> | Command palette for herdr, à la Sublime Text / VS Code — built-in operations, plugin actions and your own commands behind one key | `command-palette` `fuzzy-search` `terminal` `tui` `rust` | 7 | 🔄 2026-08-31 |
| [**herdr-switchboard**](https://github.com/crafts69guy/herdr-switchboard)<br><sub>crafts69guy</sub> | A herdr plugin: fuzzy-switch across running agents, open workspaces, and ghq repositories in one Rust TUI — and open a repo in a new workspace, tab, split, or… | `developer-tools` `ghq` `ratatui` `rust` `terminal` | 5 | 🔄 2026-08-28 |
| [**herdr-quick-actions**](https://github.com/enekos/herdr-quick-actions)<br><sub>enekos</sub> | fzf picker for herdr's native tab/pane/workspace actions, ranked by usage — stop memorizing keybindings | `shell` | 5 | 2026-08-05 |
| [**herdr-sessionizer**](https://github.com/salkhalil/herdr-sessionizer)<br><sub>salkhalil</sub> | tmux-sessionizer for herdr: fzf over open workspaces and zoxide directories, create-or-focus with template tabs | `shell` | 5 | 2026-07-27 |
| [**herdr-pane-navigator**](https://github.com/mr04vv/herdr-pane-navigator)<br><sub>mr04vv</sub> | Navigate Herdr's workspaces, tabs, and panes as one fuzzy tree — led by what each pane is actually doing. | `coding-agents` `fzf` `terminal` `tui` `shell` | 4 | 🔄 2026-08-24 |
| [**herdr-keymap**](https://github.com/The-Dave-Stack/herdr-keymap)<br><sub>The-Dave-Stack</sub> | A herdr plugin: shows every keybinding in an overlay palette and runs the ones with a CLI equivalent | `typescript` | 4 | 2026-08-12 |
| [**herdr-kiosk**](https://github.com/thomasschafer/herdr-kiosk)<br><sub>thomasschafer</sub> | Fuzzy-find Git repos and branches, and open them as worktrees in Herdr | `rust` | 4 | 🔄 2026-08-27 |
| [**herdr-cast**](https://github.com/aliou/herdr-cast)<br><sub>aliou</sub> | Personal Herdr plugin for native macOS agent notifications, fuzzy workspace navigation, zoxide-backed workspace creation, and layout commands. | `developer-tools` `macos` `notifications` `ratatui` `rust` | 3 | 🔄 2026-08-31 |
| [**🆕 herdr-palette**](https://github.com/cesarferreira/herdr-palette)<br><sub>cesarferreira</sub> | Popup command palette for Herdr. | `typescript` | 3 | 2026-08-14 |
| [**herdr-grep-nvim**](https://github.com/cinco/herdr-grep-nvim)<br><sub>cinco</sub> | herdr plugin: live-grep with fzf + ripgrep and open the match in nvim, in a split beside your work | `shell` | 3 | 2026-07-17 |
| [**herdr-spotify**](https://github.com/iikjl/herdr-spotify)<br><sub>iikjl</sub> | Spotify now-playing overlay plugin for herdr — album art, playback controls, and optional search/queue/like via the Spotify Web API | `spotify` `terminal` `go` | 3 | 2026-07-07 |
| [**herdr-hunk**](https://github.com/JacquesvanWyk/herdr-hunk)<br><sub>JacquesvanWyk</sub> | Interactive fzf picker for hunk diffs in herdr: commits, ranges, stashes, plus auto-open when an agent finishes | `fzf` `hunk` `shell` | 3 | 2026-07-12 |
| [**herdr-ssh-manager**](https://github.com/jorge07RD/herdr-ssh-manager)<br><sub>jorge07RD</sub> | Save SSH hosts and reconnect from a fuzzy popup inside Herdr — Enter hands the popup straight to ssh. | `rust` `ssh` `terminal` `tui` | 3 | 🔄 2026-08-24 |
| [**herdr-workspacer**](https://github.com/mcuste/herdr-workspacer)<br><sub>mcuste</sub> | Find projects with zoxide, then switch or create Herdr workspaces | `rust` `tui` `zoxide` | 3 | 🔄 2026-09-01 |
| [**herdr-agent-recency**](https://github.com/ugurtarlig/herdr-agent-recency)<br><sub>ugurtarlig</sub> | Theme-aware Herdr picker sorted by meaningful Codex and Claude activity | `claude-code` `codex` `fzf` `python` | 3 | 2026-07-17 |
| [**herdr-openr**](https://github.com/wraithyy/herdr-openr)<br><sub>wraithyy</sub> | herdr plugin: fuzzy-open files/URLs your terminal or AI agent just mentioned — Claude panes read the session transcript | `shell` | 3 | 2026-08-14 |
| [**herdr-configurable-picker**](https://github.com/yoshiori/herdr-configurable-picker)<br><sub>yoshiori</sub> | Tree-based goto picker for herdr with fully configurable keybindings | `rust` | 3 | 2026-07-05 |
| [**herdr-command-palette**](https://github.com/alon-z/herdr-command-palette)<br><sub>alon-z</sub> | Herdr plugin: fuzzy workspace/directory command palette. | `javascript` | 2 | 2026-06-22 |
| [**herdr-launcher**](https://github.com/arjenblokzijl/herdr-launcher)<br><sub>arjenblokzijl</sub> | Fuzzy-pick a declarative TOML workflow, fill a form, and launch a coding agent in a new herdr space. | `launcher` `ratatui` `rust` `tui` | 2 | 2026-07-10 |
| [**herdr-sesh-bro**](https://github.com/cyperx84/herdr-sesh-bro)<br><sub>cyperx84</sub> | sesh-style fuzzy session picker for Herdr — workspaces, agents, and zoxide dirs in one fzf popup with live previews | `go` | 2 | 2026-08-12 |
| [**herdr-simple-switcher**](https://github.com/haphamdev/herdr-simple-switcher)<br><sub>haphamdev</sub> | Fuzzy searching for workspaces, tabs and AI agents | `shell` | 2 | 2026-08-01 |
| [**herdr-workspace-launcher**](https://github.com/ImArtisann/herdr-workspace-launcher)<br><sub>ImArtisann</sub> | A macOS Herdr plugin for quickly creating focused workspaces with a searchable, keyboard-driven directory picker. | `typescript` | 2 | 2026-07-16 |
| [**herdr-recent-workspaces**](https://github.com/ismaelosuna7824/herdr-recent-workspaces)<br><sub>ismaelosuna7824</sub> | Open Recent for Herdr — a fuzzy-filterable list of the folders you've opened as workspaces. Pick one to open or re-focus that workspace; browse the filesystem… | `go` | 2 | 2026-07-10 |
| [**herdr-ghq-open-agent**](https://github.com/kenchan/herdr-ghq-open-agent)<br><sub>kenchan</sub> | Herdr plugin: incrementally search ghq-managed repositories with fzf and open one in a workspace/tab, starting claude | `fzf` `ghq` `shell` | 2 | 2026-08-03 |
| [**herdr-keybind-search**](https://github.com/malone-c/herdr-keybind-search)<br><sub>malone-c</sub> | Searchable keybind overlay for herdr (fzf). Press a key, fuzzy-search your keybinds. | `shell` | 2 | 2026-07-15 |
| [**herdr-waypoint**](https://github.com/wraithyy/herdr-waypoint)<br><sub>wraithyy</sub> | Save folders with a name, pick one from a fuzzy list, open it as a new herdr workspace. | `shell` | 2 | 2026-08-12 |
| [**🆕 herdr-sessionizer**](https://github.com/42lizard/herdr-sessionizer)<br><sub>42lizard</sub> | tmux-sessionizer style plugin for herdr | `fzf` `shell` | 1 | 🔄 2026-08-28 |
| [**herdr-url-picker**](https://github.com/abrose/herdr-url-picker)<br><sub>abrose</sub> | herdr plugin: pick a URL printed in the current pane with fzf and open it in the default browser | `shell` | 1 | 2026-07-22 |
| [**herdr-jump**](https://github.com/agustinvalencia/herdr-jump)<br><sub>agustinvalencia</sub> | Separate overlay pickers for herdr spaces and agents — jump to any workspace or agent, with live status colours | `go` | 1 | 2026-07-24 |
| [**helm.herdr**](https://github.com/black-atom-industries/helm.herdr)<br><sub>black-atom-industries</sub> | Jump to any Herdr workspace, agent, project, session, remote, directory, or action from one fuzzy navigator. | `rust` | 1 | 🔄 2026-08-29 |
| [**herdr-workspace-save**](https://github.com/chandrasekharan98/herdr-workspace-save)<br><sub>chandrasekharan98</sub> | Save a Herdr workspace — layout, cwds, agent sessions, running commands — and reopen it later from an fzf picker. | `claude-code` `terminal` `tmux` `python` | 1 | 🔄 2026-08-19 |
| [**herdr-url-picker**](https://github.com/chouxcreams/herdr-url-picker)<br><sub>chouxcreams</sub> | Herdr plugin: pick a URL from the focused pane and open it in your browser | `shell` | 1 | 2026-07-22 |
| [**herdr-plugin-command-palette**](https://github.com/haisi/herdr-plugin-command-palette)<br><sub>haisi</sub> | Fuzzy-searchable command palette for herdr, backed by fzf | `fzf` `python` | 1 | 2026-08-17 |
| [**herdr-command-palette**](https://github.com/hota911/herdr-command-palette)<br><sub>hota911</sub> | fzf command palette for herdr's built-in operations — workspaces, tabs, panes, agents | `command-palette` `fzf` `shell` | 1 | 2026-08-16 |
| [**herdr-keys**](https://github.com/JacquesvanWyk/herdr-keys)<br><sub>JacquesvanWyk</sub> | Fuzzy-searchable keybinding cheatsheet for herdr (packs, discovery, personal overrides) | `shell` | 1 | 2026-07-12 |
| [**herdr-fzf-url**](https://github.com/kaar/herdr-fzf-url)<br><sub>kaar</sub> | Fuzzy-find and open URLs from your herdr pane scrollback — a port of tmux-fzf-url | `shell` | 1 | 2026-07-29 |
| [**herdr-hint**](https://github.com/maedana/herdr-hint)<br><sub>maedana</sub> | Vimium-style hint labels for Herdr — press a key to see labels on tabs and agents, then press a label to jump. | `rust` | 1 | 2026-08-11 |
| [**herdr-shortcut**](https://github.com/matheus3301/herdr-shortcut)<br><sub>matheus3301</sub> | Shortcut task picker and coding-agent launcher for Herdr | `bubbletea` `claude-code` `codex` `coding-agents` `developer-tools` | 1 | 2026-07-24 |
| [**herdr-pane-picker**](https://github.com/ugurtarlig/herdr-pane-picker)<br><sub>ugurtarlig</sub> | Pick a Herdr pane by typing its on-pane character hint | `terminal` `wezterm` `python` | 1 | 2026-07-17 |
| [**herdr-bitwarden**](https://github.com/WillowMist/herdr-bitwarden)<br><sub>WillowMist</sub> | Fuzzy-search your Bitwarden vault and paste/copy credentials — a herdr port of tmux-bitwarden | `bitwarden` `fzf` `terminal` `tmux` `shell` | 1 | 2026-08-11 |
| [**herdr-fzf-url**](https://github.com/x0d7x/herdr-fzf-url)<br><sub>x0d7x</sub> | Scan herdr terminal panes for URLs and interactively pick one with fzf | `fzf` `go` `url` | 1 | 2026-06-26 |
| [**herdr-open-local-paths**](https://github.com/yigitkg/herdr-open-local-paths)<br><sub>yigitkg</sub> | Herdr plugin that detects local paths and opens or reveals them through a simple picker on Windows, Linux, and WSL. | `developer-tools` `python` `terminal` `wsl` | 1 | 2026-07-28 |
| [**herdr-agents-picker**](https://github.com/yxhta/herdr-agents-picker)<br><sub>yxhta</sub> | Herdr plugin: workspace-picker-style fuzzy picker for agent panes, with live pane preview (Rust + ratatui) | `rust` | 1 | 2026-07-31 |
| [**herdr-telescope**](https://github.com/zackshen/herdr-telescope)<br><sub>zackshen</sub> | fzf command telescope for herdr: native actions, plugin actions, file finder (@), and live ripgrep search (/) | `fzf` `rust` | 1 | 🔄 2026-08-20 |
| [**herdr-iris**](https://github.com/a-curious-coder/herdr-iris)<br><sub>a-curious-coder</sub> | Iris — a herdr plugin: fuzzy cheatsheet of AI agent skills, scoped to the pane's detected agent | `shell` | 0 | 2026-08-07 |
| [**🆕 herdr-command-palette**](https://github.com/barnuri/herdr-command-palette)<br><sub>barnuri</sub> | F1-style command palette for herdr — fuzzy-search and run every action from every installed plugin. Zero dependencies. | `command-palette` `terminal` `javascript` | 0 | 🔄 2026-09-01 |
| [**herdr-project-manager**](https://github.com/barnuri/herdr-project-manager)<br><sub>barnuri</sub> | Project manager plugin for herdr — glob/manual project discovery, fuzzy picker, open as tab or workspace | `javascript` | 0 | 🔄 2026-08-25 |
| [**herdr-worktree-picker**](https://github.com/BjoernSchotte/herdr-worktree-picker)<br><sub>BjoernSchotte</sub> | Fuzzy Git worktree picker for Herdr — type the branch name instead of worktree-rapid-river-6486. Opens as a grouped workspace or as a split pane. | `bash` `cli` `developer-tools` `fzf` `git-worktree` | 0 | 🔄 2026-08-24 |
| [**herdr-locksmith**](https://github.com/bkarpinos/herdr-locksmith)<br><sub>bkarpinos</sub> | keybinding command palette for herdr | `go` | 0 | 🔄 2026-09-01 |
| [**herdr-picker**](https://github.com/bkarpinos/herdr-picker)<br><sub>bkarpinos</sub> | A fast popup picker for searching and previewing workspaces, agents, and tabs in herdr. | `go` | 0 | 2026-07-25 |
| [**herdr-opencode-sessions**](https://github.com/damianpoole/herdr-opencode-sessions)<br><sub>damianpoole</sub> | A Herdr plugin for fuzzy-searching previous OpenCode sessions by title, project, path, date, or transcript content, with conversation previews and shortcuts to… | `typescript` | 0 | 2026-08-14 |
| [**🆕 herdr-spotify**](https://github.com/DeepRuparel/herdr-spotify)<br><sub>DeepRuparel</sub> | Spotify for Herdr — Go, zero-setup local controls + gated search/queue/save via PKCE | `spotify` `go` | 0 | 🔄 2026-08-28 |
| [**herdr-agents**](https://github.com/dleen/herdr-agents)<br><sub>dleen</sub> | An fzf agent picker for herdr: every agent pane, worst-first, with a session preview and one-key launching. | `coding-agents` `fzf` `python` `terminal` | 0 | 🔄 2026-08-20 |
| [**herdr-command-palette**](https://github.com/fabiogaliano/herdr-command-palette)<br><sub>fabiogaliano</sub> | Fuzzy command palette for Herdr — search every action, see its shortcut, run it. | `command-palette` `fzf` `terminal` `python` | 0 | 2026-08-10 |
| [**🆕 herdr-keybinds**](https://github.com/gwelican/herdr-keybinds)<br><sub>gwelican</sub> | Herdr plugin for listing/searching all keybinds, including plugins | `python` | 0 | 🔄 2026-08-31 |
| [**herdr-control-panel**](https://github.com/iskwyuki/herdr-control-panel)<br><sub>iskwyuki</sub> | One keybinding, one panel for herdr: open a workspace from history or any path, and add your own actions. Pure bash + fzf, no build step. | `bash` `fzf` `terminal` `shell` | 0 | 2026-08-11 |
| [**herdr-turbo-palette**](https://github.com/jackfrancisdalton/herdr-turbo-palette)<br><sub>jackfrancisdalton</sub> | Fuzzy-find any Herdr space, tab, agent or pane and jump straight to it. | `python` | 0 | 🔄 2026-08-22 |
| [**pj-herdr**](https://github.com/josephschmitt/pj-herdr)<br><sub>josephschmitt</sub> | Herdr plugin that uses the PJ picker to open a new workspace | `shell` | 0 | 2026-07-15 |
| [**herdr-finder-reveal**](https://github.com/klukacin/herdr-finder-reveal)<br><sub>klukacin</sub> | Click a local file path in a Herdr pane, get it revealed in Finder (macOS) | `finder` `ghostty` `macos` `terminal-multiplexer` `shell` | 0 | 2026-08-10 |
| [**herdr-cull**](https://github.com/krzysztoff1/herdr-cull)<br><sub>krzysztoff1</sub> | Review and close idle agent panes in herdr — fzf multi-select, nothing closes without confirmation. | `ai-agents` `claude` `codex` `fzf` `terminal` | 0 | 2026-07-20 |
| [**🆕 herdr-jump**](https://github.com/lancodev/herdr-jump)<br><sub>lancodev</sub> | Two-pane fuzzy switcher for herdr workspaces and agents, with vim keys | `fzf` `tui` `shell` | 0 | 🔄 2026-09-01 |
| [**herdr-vscode-tasks**](https://github.com/lurepos/herdr-vscode-tasks)<br><sub>lurepos</sub> | useful herdr picker when dealing with .vscode folder at projects | `typescript` | 0 | 2026-08-12 |
| [**herdr-omarchy-theme-sync**](https://github.com/maxBRT/herdr-omarchy-theme-sync)<br><sub>maxBRT</sub> | Sync Herdr's UI palette with the active Omarchy theme | `linux` `omarchy` `theme` `python` | 0 | 2026-08-15 |
| [**herdr-workspaces**](https://github.com/mikedclarke/herdr-workspaces)<br><sub>mikedclarke</sub> | Directories as workspaces for herdr: register the places you work, fuzzy-pick one, get a named workspace there | `go` `terminal` `tui` `workspaces` | 0 | 2026-08-02 |
| [**herdr-smart-workspace**](https://github.com/nicolasvasquez/herdr-smart-workspace)<br><sub>nicolasvasquez</sub> | Herdr plugin for quickly switching workspaces within a session or creating new ones from zoxide with an overlay fzf picker. | `python` | 0 | 2026-07-02 |
| [**herdr-launcher**](https://github.com/nicolegros/herdr-launcher)<br><sub>nicolegros</sub> | A herdr plugin that provides a fuzzy directory picker for quickly creating or switching to workspaces. | `go` | 0 | 2026-07-15 |
| [**mux-prompter**](https://github.com/phine-apps/mux-prompter)<br><sub>phine-apps</sub> | Fuzzy-pick and inject context-aware prompts into Herdr and tmux panes | `fzf` `prompt-engineering` `terminal-multiplexer` `tmux` `tmux-plugin` | 0 | 🔄 2026-08-31 |
| [**herdr-repo-picker**](https://github.com/princejoogie/herdr-repo-picker)<br><sub>princejoogie</sub> | Open Git repositories as Herdr workspaces from an OpenTUI picker | `git` `opentui` `typescript` | 0 | 2026-08-17 |
| [**herdr-claude-profile**](https://github.com/quinnjr/herdr-claude-profile)<br><sub>quinnjr</sub> | herdr plugin: switch and manage claude-profile profiles from an overlay palette | `typescript` | 0 | 2026-07-20 |
| [**herdr-plugins**](https://github.com/shelken/herdr-plugins)<br><sub>shelken</sub> | Herdr plugins monorepo (auto-pi: open pi by area + session picker) | `python` | 0 | 2026-07-17 |
| [**herdr-file-picker**](https://github.com/shivammehta25/herdr-file-picker)<br><sub>shivammehta25</sub> | Vibecoded port of tmux-file-picker to herdr | `shell` | 0 | 2026-07-29 |
| [**herdr-atuin-plugin**](https://github.com/smanickam01/herdr-atuin-plugin)<br><sub>smanickam01</sub> | Atuin shell history search in a herdr popup — press prefix+a, Enter to run or Tab to edit. Binds itself on install. | `atuin` `macos` `shell-history` `terminal` `zsh` | 0 | 2026-08-17 |
| [**🆕 herdr-jump**](https://github.com/solidsnakedev/herdr-jump)<br><sub>solidsnakedev</sub> | Fuzzy workspace, pane and tab pickers for herdr, plus a last-workspace toggle | `shell` | 0 | 🔄 2026-09-01 |
| [**herdr-workspacex**](https://github.com/willfish/herdr-workspacex)<br><sub>willfish</sub> | Rust-native fuzzy Herdr workspace switcher with zoxide-backed workspace creation | `rust` `workspace-manager` `zoxide` | 0 | 2026-07-07 |
| [**herdr-fzf-url**](https://github.com/willian/herdr-fzf-url)<br><sub>willian</sub> | Pick URLs from the focused pane with `fzf`, then open or copy them. | `fzf` `shell` | 0 | 2026-07-28 |

<details><summary>Also relevant to this purpose</summary>

- [beyondlex/herdr-recent-navigator](https://github.com/beyondlex/herdr-recent-navigator) — A recent workspaces/tabs/panes switcher for Herdr. Opens an popup window listing recently focused workspaces,…
- [JacquesvanWyk/herdr-linear](https://github.com/JacquesvanWyk/herdr-linear) — fzf-driven Linear panel in a herdr split pane or tab: search issues, drill into projects, create issues, chan…
- [42lizard/herdr-dwm-layout](https://github.com/42lizard/herdr-dwm-layout) — DWM-style master/stack layouts for Herdr
- [adamwangxx/herdr-codex-resume](https://github.com/adamwangxx/herdr-codex-resume) — Open the native Codex resume picker in a new Herdr split with live Herdr context.
- [caoer/ccc-herdr-layout](https://github.com/caoer/ccc-herdr-layout) — Visual layout picker plugin for herdr — one key, live preview
- [jovylle/herdr-pane-mark](https://github.com/jovylle/herdr-pane-mark) — Herdr plugin — custom $mark under Agents via palette/popup (no fork)

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-automation"></a>

## Automation, Hooks & Schedules

> I want a fixed set of steps to run automatically on worktree creation or at a chosen time

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-browser**](https://github.com/ogulcancelik/herdr-browser)<br><sub>ogulcancelik</sub> | Render a real Chromium view inside a Herdr pane and drive it over CDP. | `browser` `browser-automation` `cdp` `chromium` `kitty-graphics` | 348 | 🔄 2026-08-22 |
| [**herdr-auto-title**](https://github.com/sh1ma/herdr-auto-title)<br><sub>sh1ma</sub> | Automatically generate titles for herdr tabs from Claude Code and Codex conversations. | `claude-code` `codex` `python` | 53 | 2026-08-13 |
| [**🆕 herdr-auto-title**](https://github.com/kryptamine/herdr-auto-title)<br><sub>kryptamine</sub> | Tab titles that automatically follow the work in each tab. Keep your tabs organized and instantly know what you're working on with Herdr. | `go` | 47 | 🔄 2026-08-30 |
| [**zed-herdr**](https://github.com/ImArtisann/zed-herdr)<br><sub>ImArtisann</sub> | Automatically keeps your active HerdR workspace in sync with your existing Zed session. | `typescript` | 26 | 2026-08-17 |
| [**herdr-worktree-setup**](https://github.com/tdi/herdr-worktree-setup)<br><sub>tdi</sub> | herdr plugin: run per-project setup steps when a worktree is created (copy .env from main, mise trust, direnv allow, install deps) | `javascript` | 23 | 2026-07-20 |
| [**herdr-auto-pilot**](https://github.com/0xGosu/herdr-auto-pilot)<br><sub>0xGosu</sub> | A Herdr plugin that will automatically prompt the running AI Coding CLI on-behalf of you via Herdr API. The plugin has training mode which learn from your acti… | `go` | 18 | 🔄 2026-09-01 |
| [**herdr-workflows**](https://github.com/aorumbayev/herdr-workflows)<br><sub>aorumbayev</sub> | Declarative automation for repetitive steps in herdr | `agentic-ai` `agentic-workflow` `agents` `ai` `claude` | 17 | 🔄 2026-08-31 |
| [**herdr-routines**](https://github.com/mrcndz/herdr-routines)<br><sub>mrcndz</sub> | Herdr plugin that runs scheduled routines: cron or interval schedules that open a tab in a workspace and run a command or launch an agent. | `python` | 10 | 2026-07-18 |
| [**🆕 herdr-updater**](https://github.com/diegopzz/herdr-updater)<br><sub>diegopzz</sub> | Keep Herdr and its plugins current across a whole fleet, safely | `rust` `updater` | 7 | 🔄 2026-09-01 |
| [**herdr-agent-config-manager**](https://github.com/Phoobobo/herdr-agent-config-manager)<br><sub>Phoobobo</sub> | Hybrid CLI + Herdr plugin for detecting and centrally managing agent skills, MCP, plugins, and hooks | `python` | 7 | 🔄 2026-08-18 |
| [**herdr-tab-title**](https://github.com/aarsh21/herdr-tab-title)<br><sub>aarsh21</sub> | Automatic tmux-like tab titles for Herdr | `rust` `terminal` `tmux` | 6 | 2026-07-08 |
| [**herdr-pane-balancer**](https://github.com/jeph/herdr-pane-balancer)<br><sub>jeph</sub> | Automatically balance, equalize, and tile Herdr terminal panes on create, close, and exit. | `python` | 5 | 2026-08-02 |
| [**herdr-automations**](https://github.com/DnzzL/herdr-automations)<br><sub>DnzzL</sub> | Scheduled tasks for your coding agents, in the terminal. A prompt, a cron line, and a fresh git worktree per run — on Herdr. One YAML file, no store, prebuilt… | `ai-agents` `automation` `claude-code` `coding-agents` `cron` | 4 | 🔄 2026-09-01 |
| [**herdr-fwd**](https://github.com/go-min/herdr-fwd)<br><sub>go-min</sub> | Automatic loopback port forwarding for remote Herdr sessions. | `port-forwarding` `ssh` `terminal` `rust` | 3 | 🔄 2026-09-01 |
| [**tendwire**](https://github.com/plotarmordev/tendwire)<br><sub>plotarmordev</sub> | Local API for Herdr: connect coding agents to apps, automations, and any local system. | `agent-api` `local-first` `python` | 3 | 2026-08-10 |
| [**herdr-js-worktree-bootstrap**](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap)<br><sub>LeonardoTrapani</sub> | Automatically bootstrap Herdr worktrees for JavaScript and TypeScript with lockfile-aware installs and safe env restoration | `automation` `bun` `developer-tools` `git-worktree` `javascript` | 2 | 2026-07-15 |
| [**herdr-shepherd**](https://github.com/mikedclarke/herdr-shepherd)<br><sub>mikedclarke</sub> | Scheduled agent sessions for herdr: heartbeats, cron routines, and scripts, launched as visible herdr workspaces. | `coding-agents` `cron` `go` `scheduler` `tui` | 2 | 🔄 2026-08-27 |
| [**herdr-plugin**](https://github.com/ppggff/herdr-plugin)<br><sub>ppggff</sub> | Automatically remember and restore the right macOS input method (ime) for each Herdr pane. | `ime` `input-method` `macos` `python` | 2 | 2026-07-27 |
| [**herdr-labels**](https://github.com/Angel-O/herdr-labels)<br><sub>Angel-O</sub> | Herdr plugin that automatically names and numbers tabs while preserving manual labels | `rust` | 1 | 2026-08-17 |
| [**🆕 hermes-herdr-auto-reconcile**](https://github.com/chris-yyau/hermes-herdr-auto-reconcile)<br><sub>chris-yyau</sub> | Gateway liveness plugin for Hermes supervisors watching Herdr panes | `automation` `hermes-agent` `multi-agent` `python` | 1 | 🔄 2026-08-28 |
| [**herdr-auto-tab-name**](https://github.com/dev-shimada/herdr-auto-tab-name)<br><sub>dev-shimada</sub> | herdr plugin: automatically name tabs after their current directory | `javascript` | 1 | 🔄 2026-08-29 |
| [**herdr-auto-update**](https://github.com/dio16/herdr-auto-update)<br><sub>dio16</sub> | herdr plugin: check installed plugins for newer upstream commits and reinstall them at startup | `rust` | 1 | 2026-08-16 |
| [**herdr-routines**](https://github.com/guidodinello/herdr-routines)<br><sub>guidodinello</sub> | _(no description)_ | `python` | 1 | 🔄 2026-09-01 |
| [**say-hook**](https://github.com/HikaruEgashira/say-hook)<br><sub>HikaruEgashira</sub> | A macOS CLI that reads Claude Code hook events aloud using ElevenLabs text-to-speech. | `typescript` | 1 | 🔄 2026-09-01 |
| [**herdr-sched**](https://github.com/husniadil/herdr-sched)<br><sub>husniadil</sub> | Schedules and triggers for coding agents on Herdr - cron jobs and webhook/file-watcher triggers firing actions into the sibling plugins, each act signed by its… | `ai-agents` `cron` `mcp-server` `scheduler` `webhooks` | 1 | 🔄 2026-08-30 |
| [**herdr-review-loop**](https://github.com/mikhail-angelov/herdr-review-loop)<br><sub>mikhail-angelov</sub> | Automated cross-review between agents in a herdr workspace — one writes, the other reviews, repeat. | `terminal` `go` | 1 | 2026-08-16 |
| [**herdr-automations**](https://github.com/ram4-dev/herdr-automations)<br><sub>ram4-dev</sub> | Declarative cron, interval, and event automations for Herdr | `automation` `bun` `typescript` | 1 | 2026-08-13 |
| [**herdr-nixos-vm**](https://github.com/Slimydog21/herdr-nixos-vm)<br><sub>Slimydog21</sub> | The NixOS VM pane for herdr — boot, stop, watch, and ssh into your Hashimoto-style dev VM. Requires the nixos-vm kit. | `shell` | 1 | 🔄 2026-08-18 |
| [**herdr-agent-title-sync**](https://github.com/winoooops/herdr-agent-title-sync)<br><sub>winoooops</sub> | Automatic Herdr pane title sync for Claude Code, Codex, Kimi Code, OpenCode, and other coding agents. | `developer-tools` `typescript` | 1 | 🔄 2026-08-20 |
| [**herdr-plugin-orbstack**](https://github.com/AsgardMuninn/herdr-plugin-orbstack)<br><sub>AsgardMuninn</sub> | Open OrbStack Linux machines as herdr workspaces (direct shell, SSH fallback, auto-sync) | `python` | 0 | 2026-08-11 |
| [**herdr-auto-update**](https://github.com/barnuri/herdr-auto-update)<br><sub>barnuri</sub> | Keep herdr always up to date — auto patch/minor/major updates with live handoff | `auto-update` `javascript` | 0 | 🔄 2026-08-25 |
| [**bermuda**](https://github.com/bon5co/bermuda)<br><sub>bon5co</sub> | Orchestration under Claude Code on herdr: flows an agent cannot skip, jobs on a clock, threads with claims, and a forum agents search later | `agent-orchestration` `agents` `ai-agents` `automation` `claude-code` | 0 | 🔄 2026-09-01 |
| [**🆕 herdr-claude-lifecycle**](https://github.com/daocoding/herdr-claude-lifecycle)<br><sub>daocoding</sub> | Hook-first Claude Code lifecycle for herdr + Omarchy: working/blocked/idle from Claude's own hooks, verify after every Claude Code update | `claude-code` `omarchy` `python` | 0 | 🔄 2026-09-02 |
| [**herdr-teams-notify**](https://github.com/donghaolicd/herdr-teams-notify)<br><sub>donghaolicd</sub> | Herdr plugin for bounded Microsoft Teams agent lifecycle notifications | `automation` `microsoft-teams` `notifications` `javascript` | 0 | 2026-08-15 |
| [**herdr-context-namer**](https://github.com/eabadim/herdr-context-namer)<br><sub>eabadim</sub> | Auto-name Herdr tabs and workspaces from pane context via OpenCode | `opencode` `python` | 0 | 2026-08-06 |
| [**🆕 herdr-claude-title-hook**](https://github.com/eduardoborges/herdr-claude-title-hook)<br><sub>eduardoborges</sub> | Claude Code plugin that syncs the session title to the Herdr tab title | `shell` | 0 | 🔄 2026-08-26 |
| [**herdr-pane-name**](https://github.com/go-min/herdr-pane-name)<br><sub>go-min</sub> | Herdr plugin that automatically names panes in your terminal sessions. | `pane-naming` `terminal` `terminal-multiplexer` `rust` | 0 | 2026-08-16 |
| [**🆕 herdr-looper**](https://github.com/gurronen/herdr-looper)<br><sub>gurronen</sub> | Launch repeatable machine-local Pi jobs in fresh Herdr workspaces and worktrees | `automation` `rust` `terminal` | 0 | 🔄 2026-08-26 |
| [**🆕 herdr-worktree-setup**](https://github.com/jtnovellis/herdr-worktree-setup)<br><sub>jtnovellis</sub> | herdr plugin: make a new git worktree immediately usable — copy .env & dev state, clone dependency caches (APFS/reflink), mise trust, direnv allow, install dep… | `git-worktree` `rust` | 0 | 🔄 2026-08-29 |
| [**herdr-plugin-auto-rename**](https://github.com/khatriafaz/herdr-plugin-auto-rename)<br><sub>khatriafaz</sub> | Automatically rename fresh Herdr workspaces and Git branches from a Pi session's first prompt. | `typescript` | 0 | 2026-08-14 |
| [**herdr-unrecoverable**](https://github.com/neilwashere/herdr-unrecoverable)<br><sub>neilwashere</sub> | Herdr watchdog that recovers Pi coding-agent sessions from terminal provider errors | `pi-coding-agent` `javascript` | 0 | 2026-08-14 |
| [**herdr-autocontinue**](https://github.com/rcosteira79/herdr-autocontinue)<br><sub>rcosteira79</sub> | Watches agents for usage-limit walls, badges the countdown to the reset ($wall), and re-prompts the agents you armed once the window reopens. | `python` | 0 | 🔄 2026-08-31 |
| [**🆕 herdr-claude-safe-compact**](https://github.com/tmastalirsch/herdr-claude-safe-compact)<br><sub>tmastalirsch</sub> | herdr plugin: compacts idle Claude Code panes, but only once a handoff is safely on disk | `claude-code` `compaction` `shell` | 0 | 🔄 2026-08-31 |
| [**herdr-worktreeinclude**](https://github.com/untalfranfernandez/herdr-worktreeinclude)<br><sub>untalfranfernandez</sub> | Herdr plugin that populates every new git worktree with the gitignored local files it needs — .env, settings.local.json, fixtures. Declare them once in a .work… | `claude-code` `dotenv` `git-worktree` `worktree` | 0 | 2026-07-29 |
| [**herdr-padio**](https://github.com/vgreg/herdr-padio)<br><sub>vgreg</sub> | Switch PadIO controller modes automatically based on the app running in herdr's focused pane | `game-controller` `macos` `padio` `python` | 0 | 2026-08-02 |
| [**🆕 herdr-space-groups**](https://github.com/yojahny55/herdr-space-groups)<br><sub>yojahny55</sub> | Herdr plugin: group Spaces into named, colored groups — picker popup (mouse + keyboard), sidebar group headers, automatic ordering | `javascript` | 0 | 🔄 2026-08-29 |
| [**numberer-manager**](https://github.com/yuritada/numberer-manager)<br><sub>yuritada</sub> | A lightweight Herdr plugin that automatically prefixes workspace and tab labels with their current list position (e.g., 1: space and 1: tab). | `python` | 0 | 2026-07-25 |
| [**herdr-pane-restart**](https://github.com/zap0xfce2/herdr-pane-restart)<br><sub>zap0xfce2</sub> | Run a configured command in named panes on server startup | `python` | 0 | 2026-08-10 |
| [**herdr-booking-task-plugin**](https://github.com/zerodice0/herdr-booking-task-plugin)<br><sub>zerodice0</sub> | Schedule Herdr agent prompts and local CLI commands on macOS and Linux. | `golang` `scheduler` `go` | 0 | 2026-08-03 |

<details><summary>Also relevant to this purpose</summary>

- [qu8n/herdr-automatic-rename](https://github.com/qu8n/herdr-automatic-rename) — Navigate herdr faster with smart tab names and 1-9 jump labels for workspaces/tabs/agents
- [freethinkel/herdr-plugin-git-worktree-hooks](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks) — Run shell commands when a git worktree is created/removed — one YAML config for all projects, living outside…
- [miko-misa/herdr-portfwd](https://github.com/miko-misa/herdr-portfwd) — Automatic SSH port forwarding for coding agents on remote machines: Ctrl+click the localhost URL your agent p…
- [timofey-TK/herdr-worktree-hooks](https://github.com/timofey-TK/herdr-worktree-hooks) — herdr plugin: run custom setup/teardown commands when a git worktree is created, opened, or removed
- [itisbryan/herdr-gh-checks](https://github.com/itisbryan/herdr-gh-checks) — Herdr plugin: watch & review the current PR's CI in a pane; CI/merge status on sidebar rows. Go + Bubble Tea.
- [elkraps/herdr-telegram-notify](https://github.com/elkraps/herdr-telegram-notify) — Customizable Telegram notifications for Herdr agent state changes, with status filters, templates, multi-chat…
- [m1sk9/herdr-worktree-hooks-plugin](https://github.com/m1sk9/herdr-worktree-hooks-plugin) — A plugin that adds customizable hooks to Herdr's Worktree
- [Newt6611/herdr-tab-title](https://github.com/Newt6611/herdr-tab-title) — Herdr Tab Title automatically renames Herdr tabs with clean, workspace-local numbering like 1. Codex, 2. Term…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-session"></a>

## Session State & Restore

> I want to close my work and later resume from exactly the same state

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-resurrect**](https://github.com/ntindle/herdr-resurrect)<br><sub>ntindle</sub> | tmux-resurrect for herdr — snapshot workspaces, tabs, panes, cwd, running programs and agents, and restore them after a crash or reboot. | `crash-recovery` `session-manager` `terminal-multiplexer` `tmux-resurrect` `javascript` | 26 | 🔄 2026-08-24 |
| [**session-digger**](https://github.com/taxueseek/session-digger)<br><sub>taxueseek</sub> | 跨环境会话历史挖掘与知识管理。分析记录。支持 Claude/Grok/Kimi Code/Codex/WorkBuddy/Trae CN 等主流环境 | `claude-code` `conversation-analysis` `jsonl` `knowledge-management` `log-analysis` | 17 | 2026-07-21 |
| [**herdr-notes**](https://github.com/alexarthurs/herdr-notes)<br><sub>alexarthurs</sub> | Persistent markdown notes pane for herdr - one note per workspace, rendered preview + edit mode, autosaves and survives restarts | `markdown` `notes` `ratatui` `rust` `terminal` | 14 | 2026-07-25 |
| [**herdr-claude-auto-retry**](https://github.com/mo-arvan/herdr-claude-auto-retry)<br><sub>mo-arvan</sub> | Wait out Anthropic rate limits and auto-resume Claude Code, herdr-native: no tmux, no shell wrapper. | `javascript` | 14 | 🔄 2026-08-31 |
| [**herdr-session-parker**](https://github.com/iviaxpow3r/herdr-session-parker)<br><sub>iviaxpow3r</sub> | Herdr plugin to park panes/tabs and resume supported agent sessions later | `agent-tools` `python` | 11 | 2026-07-03 |
| [**herdr-agent-inbox**](https://github.com/douglascorrea/herdr-agent-inbox)<br><sub>douglascorrea</sub> | An inbox for your coding agents in herdr — session titles, settle/mark-unread triage, runtimes, workspace rollups, and resumable chat history | `ai-agents` `terminal` `python` | 9 | 2026-07-28 |
| [**herdr-assist**](https://github.com/walcew/herdr-assist)<br><sub>walcew</sub> | Physical desk panel for Herdr, the terminal multiplexer for AI coding agents — shows session state in color and rings a bell when an agent stops to ask for a d… | `ai-agents` `claude-code` `coding-agents` `embedded` `esp-idf` | 8 | 🔄 2026-08-27 |
| [**🆕 sheep**](https://github.com/gokay-ai/sheep)<br><sub>gokay-ai</sub> | Undo for AI coding agents. Every agent turn becomes a restorable checkpoint. | `git` `rust` `tui` `undo` | 5 | 🔄 2026-08-28 |
| [**herdr-oh-my-agent**](https://github.com/GavinTomlins/herdr-oh-my-agent)<br><sub>GavinTomlins</sub> | Mirror every oh-my-openagent subagent delegation into its own Herdr pane or tab — live, with full session state and scrollback | `typescript` | 4 | 2026-07-31 |
| [**herdr-pane-id-labeler**](https://github.com/4Born/herdr-pane-id-labeler)<br><sub>4Born</sub> | Herdr plugin that keeps pane labels synchronized with public pane IDs such as w1:p2. | `developer-tools` `terminal` `javascript` | 2 | 2026-07-26 |
| [**herdr-hibernate**](https://github.com/bengemine/herdr-hibernate)<br><sub>bengemine</sub> | Hibernate idle coding-agent panes in Herdr (Claude Code, Codex, Grok) — free the RAM, press Enter to resume the exact session. | `claude-code` `python` | 2 | 2026-08-03 |
| [**herdr-synchronize-panes**](https://github.com/furuhashin/herdr-synchronize-panes)<br><sub>furuhashin</sub> | Herdr plugin: broadcast one command to every pane in the current tab (tmux synchronize-panes style) | `javascript` | 2 | 2026-07-14 |
| [**herdr_sync**](https://github.com/kamaaina/herdr_sync)<br><sub>kamaaina</sub> | synchronize panes in herdr | `zig` | 2 | 2026-07-01 |
| [**herdr-e2b**](https://github.com/tomasvarga/herdr-e2b)<br><sub>tomasvarga</sub> | Mirror a git worktree into a fresh E2B cloud sandbox on demand — a snapshot upload (uncommitted changes and all), no push or clone. A herdr plugin. | `cli` `cloud-dev` `e2b` `git-worktree` `sandbox` | 2 | 2026-07-18 |
| [**herdr-thread-to-tab**](https://github.com/toyamarinyon/herdr-thread-to-tab)<br><sub>toyamarinyon</sub> | Keep single-pane Herdr tab labels in sync with Claude Code and Codex thread titles. | `rust` | 2 | 2026-08-06 |
| [**herdr-todos-windows**](https://github.com/aclima01/herdr-todos-windows)<br><sub>aclima01</sub> | Live panel mirroring a herdr agent's task list (TaskCreate/TaskUpdate) so you can follow its plan | `powershell` | 1 | 2026-07-22 |
| [**mo-herdr**](https://github.com/momentohq/mo-herdr)<br><sub>momentohq</sub> | Run mo inside herdr panes: session restore after a herdr restart, a launch action, and SIGKILL cleanup | `python` | 1 | 🔄 2026-08-27 |
| [**🆕 herdr-undo-close**](https://github.com/pedroloch/herdr-undo-close)<br><sub>pedroloch</sub> | Reopen a closed tab in herdr, like Cmd+Shift+T in a browser - restores the label, the split tree with its ratios, each pane's cwd, and the tab's position. | `python` | 1 | 2026-07-30 |
| [**attic**](https://github.com/TheThoughtagen/attic)<br><sub>TheThoughtagen</sub> | Auto-closes idle AI coding sessions, but archives each one first so you can restore it. | `claude-code` `developer-tools` `python` `session-management` `tui` | 1 | 2026-08-14 |
| [**herdr-stash**](https://github.com/victor-software-house/herdr-stash)<br><sub>victor-software-house</sub> | Stash a Herdr workspace: stop its agents, keep its shape and their conversations, and restore it later from a clickable two-column popup. | `rust` `terminal` `tui` | 1 | 2026-07-29 |
| [**herdr-agent-pins**](https://github.com/ZingerLittleBee/herdr-agent-pins)<br><sub>ZingerLittleBee</sub> | Persistently pin Herdr agent sessions to the top of the Agents sidebar. | `terminal` `javascript` | 1 | 🔄 2026-08-24 |
| [**herdr-codex-resume**](https://github.com/adamwangxx/herdr-codex-resume)<br><sub>adamwangxx</sub> | Open the native Codex resume picker in a new Herdr split with live Herdr context. | `codex-cli` `terminal` `shell` | 0 | 🔄 2026-08-21 |
| [**herdr-agent-resume**](https://github.com/Angel-O/herdr-agent-resume)<br><sub>Angel-O</sub> | Herdr plugin that inserts or copies resume commands to smoothly resume AI agent sessions | `rust` | 0 | 2026-08-15 |
| [**herdr-suspend-workspace**](https://github.com/asermax/herdr-suspend-workspace)<br><sub>asermax</sub> | Suspend a herdr workspace (snapshot layout + agents, close it, restore later from a popup picker) | `typescript` | 0 | 2026-07-31 |
| [**herdr-plugin-session-pruner**](https://github.com/Gareth-Rouse/herdr-plugin-session-pruner)<br><sub>Gareth-Rouse</sub> | Herdr plugin: track workspace last-use, show the age in the Spaces sidebar, and keep cold workspaces out of the restored session | `terminal-multiplexer` `shell` | 0 | 2026-08-07 |
| [**herdr-flakes**](https://github.com/iQua/herdr-flakes)<br><sub>iQua</sub> | Flakes plugin for Herdr — mirror and steer your Flakes runs in your local Herdr session | `javascript` | 0 | 2026-07-22 |
| [**🆕 herdr-session-title-name**](https://github.com/jovylle/herdr-session-title-name)<br><sub>jovylle</sub> | Herdr plugin: terminal_title_stripped → tab persistence (session_title alone on top, tab keeps it after close) | `sidebar` `terminal` `html` | 0 | 🔄 2026-08-28 |
| [**herdr-plugin-vault**](https://github.com/Joxtacy/herdr-plugin-vault)<br><sub>Joxtacy</sub> | Browse past Claude Code sessions in a herdr popup and resume the one you pick in a new tab | `shell` | 0 | 2026-08-11 |
| [**🆕 herdr-ccs**](https://github.com/KennethWKZ/herdr-ccs)<br><sub>KennethWKZ</sub> | Make `ccs claude` behave like native Claude Code in Herdr: pane detection + launcher-aware restore through ccs. | `shell` | 0 | 🔄 2026-08-29 |
| [**herdr-layout**](https://github.com/noviadi/herdr-layout)<br><sub>noviadi</sub> | Save and replay Herdr pane layouts. A companion plugin (tmux-resurrect-style) for the Herdr terminal multiplexer. | `cli` `terminal` `tmux-resurrect` `shell` | 0 | 2026-08-13 |
| [**🆕 herdr-tab-new**](https://github.com/softwarecrafts/herdr-tab-new)<br><sub>softwarecrafts</sub> | Resume or start an agent session in the herdr workspace for this project — a herdr plugin, and a CLI for terminals outside herdr | `typescript` | 0 | 🔄 2026-08-31 |
| [**herdr-event-log**](https://github.com/waynewu411/herdr-event-log)<br><sub>waynewu411</sub> | Herdr plugin: logs pane.agent_status_changed (and future event types) to a durable, cursor-resumable global log any parent agent can tail. | `shell` | 0 | 🔄 2026-08-24 |
| [**live-sync-panes**](https://github.com/wg1k/live-sync-panes)<br><sub>wg1k</sub> | Herdr plugin: broadcast a command, or live-sync keystrokes, to every pane in a tab | `javascript` | 0 | 2026-08-11 |

<details><summary>Also relevant to this purpose</summary>

- [nicosuave/memex](https://github.com/nicosuave/memex) — Search Claude Code, Codex, Pi, OpenCode, Github Copilot & Cursor transcripts. Resume sessions. Track tokens.
- [KokiKono/herdr-kanban](https://github.com/KokiKono/herdr-kanban) — Terminal Kanban board that links tasks to herdr tabs, persisted in SQLite
- [afogel/shepherdr](https://github.com/afogel/shepherdr) — Shepherd delegated coding agents into visible, auditable herdr panes you can watch, resume, and take over — a…
- [AkashJana18/herdr-scratch](https://github.com/AkashJana18/herdr-scratch) — Persistent scratchpads for Herdr, paving the way for floating utility panes.
- [voodootikigod/adlc-herdr](https://github.com/voodootikigod/adlc-herdr) — ADLC herdr plugin — per-pane phase/ticket/gate status, backlog board, gate actions, and adlc-fleet run observ…
- [blaxel-ai/herdr-blaxel-sandbox-plugin](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin) — Run coding agents in persistent Blaxel sandboxes from Herdr.
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — Automatically bootstrap Herdr worktrees for JavaScript and TypeScript with lockfile-aware installs and safe e…
- [ppggff/herdr-plugin](https://github.com/ppggff/herdr-plugin) — Automatically remember and restore the right macOS input method (ime) for each Herdr pane.
- [shadowfax92/herdr-scratch](https://github.com/shadowfax92/herdr-scratch) — Persistent per-pane Herdr scratch popups backed by private tmux sessions.
- [damianpoole/herdr-opencode-sessions](https://github.com/damianpoole/herdr-opencode-sessions) — A Herdr plugin for fuzzy-searching previous OpenCode sessions by title, project, path, date, or transcript co…
- [goofansu/herdr-hunk](https://github.com/goofansu/herdr-hunk) — Provides quick Herdr review actions that open a temporary Hunk overlay. Quitting Hunk closes the overlay and…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-naming"></a>

## Titles, Naming & Looks

> I want tab names and terminal titles to be automatically clear, or want to change how things look

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-tab-smart-rename**](https://github.com/iurysza/herdr-tab-smart-rename)<br><sub>iurysza</sub> | Generates context-aware workspace and tab names for Herdr. | `ai` `bun` `terminal` `typescript` | 69 | 🔄 2026-08-19 |
| [**herdr-window-title-sync**](https://github.com/rjyo/herdr-window-title-sync)<br><sub>rjyo</sub> | Syncs terminal titles from workspaces, tabs, and agent sessions (use w/ Moshi) | `moshi` `terminal-title` `javascript` | 34 | 2026-06-26 |
| [**herdr-flock**](https://github.com/ragamo/herdr-flock)<br><sub>ragamo</sub> | A herdr plugin that visualizes your AI coding agents as pixel-art sheep living on a top-down farm. | `cli` `ratatui` `rust` `tui` | 30 | 🔄 2026-08-31 |
| [**herdr-claude-session-title**](https://github.com/bcihanc/herdr-claude-session-title)<br><sub>bcihanc</sub> | Herdr plugin: mirrors the Claude Code session title (/rename or auto summary) into the herdr pane metadata title | `shell` | 8 | 2026-07-11 |
| [**herdr-canvas**](https://github.com/aorumbayev/herdr-canvas)<br><sub>aorumbayev</sub> | Mouse-driven ASCII diagram canvas for herdr agents - draw in the TUI, share structured JSON, and let AI edit it. | `agentic-ai` `agents` `ai-agents` `ascii-art` `bubbletea` | 7 | 🔄 2026-08-31 |
| [**herdr-pet**](https://github.com/allmight-ai/herdr-pet)<br><sub>allmight-ai</sub> | Companion V-Pet for Herdr — mirrors your coding agent | `companion` `rust` `v-pet` | 6 | 🔄 2026-08-20 |
| [**herdr-icon-agent-ui**](https://github.com/qintmb/herdr-icon-agent-ui)<br><sub>qintmb</sub> | Renders Agent icon, vertically-aligned monochrome icons in the Herdr sidebar. rendered via a custom font with non-uniform glyph scaling that matches terminal c… | `python` | 5 | 🔄 2026-08-20 |
| [**herdr-ghostty-tab-title**](https://github.com/wjarka/herdr-ghostty-tab-title)<br><sub>wjarka</sub> | herdr plugin: color-coded agent status counts (blocked / done / working / idle) in the Ghostty tab title | `ai-agents` `ghostty` `terminal` `python` | 5 | 2026-08-04 |
| [**herdr-town**](https://github.com/Efeguclu1/herdr-town)<br><sub>Efeguclu1</sub> | Watch your Herdr coding agents as an 8-bit town. Read and answer them without leaving it. | `ai-agents` `pixel-art` `terminal` `tui` `javascript` | 4 | 2026-08-08 |
| [**herdr-in-your-face**](https://github.com/JYasha11/herdr-in-your-face)<br><sub>JYasha11</sub> | A giant ASCII face screams at you when you leave an AI agent blocked. Escalates the longer you ignore it. | `javascript` | 4 | 2026-07-10 |
| [**herdr-auto-namer**](https://github.com/kakigakki/herdr-auto-namer)<br><sub>kakigakki</sub> | ChatGPT-style auto-naming for herdr: agents get their Claude session title, workspaces get their working directory | `claude-code` `python` | 4 | 🔄 2026-08-27 |
| [**herdr-tab-rename**](https://github.com/lmilojevicc/herdr-tab-rename)<br><sub>lmilojevicc</sub> | Auto-rename each Herdr tab to its focused pane's working-directory name. Manually renamed tabs are left alone. | `go` | 4 | 2026-07-31 |
| [**🆕 herdr-pet**](https://github.com/nikok6/herdr-pet)<br><sub>nikok6</sub> | Tiny desk pet on your herdr panes: types, waits, and celebrates with your agent. Works with any Codex pet. | `rust` | 3 | 🔄 2026-08-26 |
| [**herdr-questmancer**](https://github.com/opsydyn/herdr-questmancer)<br><sub>opsydyn</sub> | A cozy 16-bit adventurers' guild for your Herdr coding agents. Working agents delve, blocked agents call for counsel, finished work returns with spoils. | `coding-agents` `pixel-art` `ratatui` `tui` `rust` | 3 | 2026-08-11 |
| [**herdr-theme-picker**](https://github.com/qintmb/herdr-theme-picker)<br><sub>qintmb</sub> | Theme picker for herdr UI based terminalcolors scheme and your customization. | `shell` | 3 | 🔄 2026-08-31 |
| [**herdr-nerd-font-tab-name**](https://github.com/rohankewal/herdr-nerd-font-tab-name)<br><sub>rohankewal</sub> | Nerd Font icons for your herdr tabs — a port of joshmedeski/tmux-nerd-font-window-name | `nerd-fonts` `python` `terminal` `tui` | 3 | 2026-07-31 |
| [**🆕 herdr-pets**](https://github.com/abhishek944/herdr-pets)<br><sub>abhishek944</sub> | A transparent desktop village for live Herdr agents | `typescript` | 2 | 🔄 2026-08-31 |
| [**herdr-titles**](https://github.com/davidolrik/herdr-titles)<br><sub>davidolrik</sub> | Herdr Titles that keep up. – herdr-titles names your tabs and windows after what's actually running; including your AI agents' live session titles — and compos… | `ai-assisted` `go` | 2 | 🔄 2026-08-18 |
| [**herdr-english-coach**](https://github.com/GranamyrBR/herdr-english-coach)<br><sub>GranamyrBR</sub> | herdr plugin: color-coded English corrections board — your coding agent logs grammar + dev-jargon fixes to a live side pane while you work | `english` `language-learning` `shell` | 2 | 2026-07-06 |
| [**herdr-ai-tab-name**](https://github.com/ndom91/herdr-ai-tab-name)<br><sub>ndom91</sub> | Auto-rename your Herdr Tabs with local LLMs | `local-llm` `python` | 2 | 2026-08-05 |
| [**herdr-powershell-title-sync**](https://github.com/aclima01/herdr-powershell-title-sync)<br><sub>aclima01</sub> | Windows/PowerShell port of window-title-sync: sync the terminal title to the focused herdr session | `powershell` | 1 | 2026-07-20 |
| [**herdr-git-tab-name**](https://github.com/blurname/herdr-git-tab-name)<br><sub>blurname</sub> | Herdr plugin that renames tabs to the focused pane's Git branch. | `shell` | 1 | 2026-07-06 |
| [**herdr-hermes-session-title**](https://github.com/btorresgil/herdr-hermes-session-title)<br><sub>btorresgil</sub> | Show Hermes Agent session titles in the Herdr sidebar. | `python` | 1 | 2026-08-07 |
| [**herdr-tab-smart-rename-rs**](https://github.com/EmmetZ/herdr-tab-smart-rename-rs)<br><sub>EmmetZ</sub> | _(no description)_ | `rust` | 1 | 🔄 2026-08-24 |
| [**herdr-tab-title-sync**](https://github.com/lucasleon2107/herdr-tab-title-sync)<br><sub>lucasleon2107</sub> | herdr plugin: rename tabs to the AI agent's conversation title | `ai-agents` `claude-code` `terminal` `tmux` `shell` | 1 | 2026-08-04 |
| [**🆕 herdr-session-sync**](https://github.com/nengqi/herdr-session-sync)<br><sub>nengqi</sub> | Auto-sync Claude Code, Codex & Agent session names across Herdr pane labels, PTY window titles, and mobile companion apps (Heeler) | `agent` `claude-code` `codex` `heeler` `terminal-multiplexer` | 1 | 🔄 2026-08-28 |
| [**herdr-nerd-font-tab-name-windows**](https://github.com/Only-Moon/herdr-nerd-font-tab-name-windows)<br><sub>Only-Moon</sub> | Windows port of herdr-nerd-font-tab-name: Nerd Font icons for herdr tabs with cross-platform support (Windows, macOS, Linux) and folder-based icon resolution | `herdr-windows` `icons` `nerd-fonts` `python` `title` | 1 | 2026-08-10 |
| [**herdr-tab-renamer**](https://github.com/ryanlewis/herdr-tab-renamer)<br><sub>ryanlewis</sub> | herdr plugin: labels tabs after their live content — agent session titles and shell directories | `javascript` | 1 | 2026-08-08 |
| [**herdr-claude-tab-title**](https://github.com/tmn73/herdr-claude-tab-title)<br><sub>tmn73</sub> | Mirrors each Claude Code session title, and its agent state, onto its Herdr tab | `claude-code` `tabs` `terminal` `typescript` | 1 | 🔄 2026-08-27 |
| [**🆕 workspace-basename**](https://github.com/42lizard/workspace-basename)<br><sub>42lizard</sub> | herdr plugin to set the workspace name based on the basename of the cwd the workspace was created | `shell` | 0 | 🔄 2026-08-27 |
| [**herdr-habitat**](https://github.com/chantlong/herdr-habitat)<br><sub>chantlong</sub> | herdr habitat is a living terminal habitat that grows alongside your agents’ work. Nurturing takes time, so no agentmaxxing please. As agents burn tokens in en… | `chill` `cozy` `javascript` | 0 | 2026-08-16 |
| [**herdr-tab-title-from-terminal**](https://github.com/christiangroth/herdr-tab-title-from-terminal)<br><sub>christiangroth</sub> | Name every Herdr tab after the terminal title of the agent inside it. One /rename in Claude Code names your session and the tab. Manually named tabs are left a… | `python` | 0 | 🔄 2026-08-25 |
| [**🆕 herdr-llm-summary-header**](https://github.com/dnf0/herdr-llm-summary-header)<br><sub>dnf0</sub> | Herdr plugin: LLM one-line summary written to the pane title when an agent finishes | `javascript` | 0 | 2026-08-03 |
| [**herdr-smart-rename**](https://github.com/edouard-andrei/herdr-smart-rename)<br><sub>edouard-andrei</sub> | herdr plugin: AI names for tabs and panes from agent transcripts — one keypress, any OpenAI-compatible model | `javascript` | 0 | 🔄 2026-08-20 |
| [**herdr-title-sync**](https://github.com/elKei24/herdr-title-sync)<br><sub>elKei24</sub> | Herdr plugin: mirror each agent's terminal title onto its tab label | `python` | 0 | 🔄 2026-09-01 |
| [**🆕 herdr-sheep**](https://github.com/huketo/herdr-sheep)<br><sub>huketo</sub> | Watch your Herdr coding agents as a flock of animated ASCII sheep | `ascii-art` `rust` `tui` | 0 | 🔄 2026-08-31 |
| [**herdr-tab-session-name-sync**](https://github.com/itayo-m/herdr-tab-session-name-sync)<br><sub>itayo-m</sub> | Syncs agent session name with herdr tabs and panes title | `developer-tools` `github-copilot` `terminal` `javascript` | 0 | 2026-08-03 |
| [**herdr-chromatic-spaces**](https://github.com/jackfrancisdalton/herdr-chromatic-spaces)<br><sub>jackfrancisdalton</sub> | Give every Herdr Space its own colour and emoji: coloured sidebar dots, grouped agents, and optional chrome tint on space switch. | `python` | 0 | 🔄 2026-08-22 |
| [**🆕 herdr-tab-titles**](https://github.com/kewah/herdr-tab-titles)<br><sub>kewah</sub> | Herdr plugin that names panes and tabs after the first coding-agent prompt. | `javascript` | 0 | 🔄 2026-09-01 |
| [**herdr-tab-numbers**](https://github.com/kokatsu/herdr-tab-numbers)<br><sub>kokatsu</sub> | Prefix each tab name with its switch_tab position | `shell` | 0 | 🔄 2026-08-26 |
| [**herdr-window-title**](https://github.com/mackt/herdr-window-title)<br><sub>mackt</sub> | Configurable outer-terminal title for herdr: template-driven, session-aware, with live agent state (blocked/done/working) indicator | `rust` | 0 | 2026-08-03 |
| [**herdr-agent-smart-rename**](https://github.com/malone-c/herdr-agent-smart-rename)<br><sub>malone-c</sub> | Names each herdr agent session from what it is actually doing | `python` | 0 | 2026-08-14 |
| [**herdr-machine-title**](https://github.com/mikevalstar/herdr-machine-title)<br><sub>mikevalstar</sub> | herdr plugin: pin the outer terminal title to herdr@<hostname> · <workspace> | `shell` | 0 | 2026-07-02 |
| [**herdr-tab-title**](https://github.com/Newt6611/herdr-tab-title)<br><sub>Newt6611</sub> | Herdr Tab Title automatically renames Herdr tabs with clean, workspace-local numbering like 1. Codex, 2. Terminal, using a customizable format. | `rust` | 0 | 2026-07-09 |
| [**tab-blank-number**](https://github.com/riq0h/tab-blank-number)<br><sub>riq0h</sub> | herdr plugin that clears herdr's default numeric tab labels (1, 2, 3…) to blank. | `javascript` | 0 | 2026-07-19 |
| [**tab-process-name**](https://github.com/riq0h/tab-process-name)<br><sub>riq0h</sub> | herdr plugin that labels each tab with its foreground process name — tmux's automatic-rename behavior, for herdr. | `javascript` | 0 | 2026-07-19 |
| [**herdr-workspace-renamer**](https://github.com/ryanlewis/herdr-workspace-renamer)<br><sub>ryanlewis</sub> | herdr plugin: syncs agent session names onto workspace labels | `javascript` | 0 | 2026-08-08 |
| [**herdr-codex-session-title**](https://github.com/sergeybataev/herdr-codex-session-title)<br><sub>sergeybataev</sub> | Herdr plugin that mirrors Codex chat titles into agent names | `codex` `python` | 0 | 2026-08-01 |
| [**herdr-title-wrap**](https://github.com/T0mSIlver/herdr-title-wrap)<br><sub>T0mSIlver</sub> | Herdr plugin: wrap Claude Code session titles across multiple sidebar rows, auto-fitting the sidebar width | `python` | 0 | 2026-08-06 |
| [**herdr-agent-session-title**](https://github.com/the-inconvenience-store/herdr-agent-session-title)<br><sub>the-inconvenience-store</sub> | Herdr plugin: mirrors the Claude Code or Codex session title (/rename or auto summary) into the herdr pane metadata title | `python` | 0 | 2026-07-30 |
| [**herdr-ghostty-theme-sync**](https://github.com/themuuln/herdr-ghostty-theme-sync)<br><sub>themuuln</sub> | Adapt herdr's theme and sidebar colors to the active Ghostty theme; keeps sidebar tokens alive across herdr restarts. herdr.dev plugin. | `python` | 0 | 2026-08-12 |
| [**tabby**](https://github.com/yersonargotev/tabby)<br><sub>yersonargotev</sub> | Herdr plugin that labels focused tabs with a Significant Command or Working Directory Basename. | `rust` | 0 | 🔄 2026-08-20 |
| [**herdr-auto-session-title**](https://github.com/zhangzujian/herdr-auto-session-title)<br><sub>zhangzujian</sub> | Generate concise Herdr pane titles and synchronize native Codex thread names. | `javascript` | 0 | 2026-07-30 |

<details><summary>Also relevant to this purpose</summary>

- [qu8n/herdr-automatic-rename](https://github.com/qu8n/herdr-automatic-rename) — Navigate herdr faster with smart tab names and 1-9 jump labels for workspaces/tabs/agents
- [sh1ma/herdr-auto-title](https://github.com/sh1ma/herdr-auto-title) — Automatically generate titles for herdr tabs from Claude Code and Codex conversations.
- [kryptamine/herdr-auto-title](https://github.com/kryptamine/herdr-auto-title) — Tab titles that automatically follow the work in each tab. Keep your tabs organized and instantly know what y…
- [wyattjoh/herdr-plugin-renamer](https://github.com/wyattjoh/herdr-plugin-renamer) — Renames an auto-generated herdr worktree branch and workspace from the agent's first prompt, via on-device Ap…
- [ythx-101/herdr-social-glass](https://github.com/ythx-101/herdr-social-glass) — Screenshot-friendly Social Glass theme and workflow plugin for Herdr on macOS.
- [aarsh21/herdr-tab-title](https://github.com/aarsh21/herdr-tab-title) — Automatic tmux-like tab titles for Herdr
- [funsaized/herdr-mise](https://github.com/funsaized/herdr-mise) — Run the pass, not the prompts 🧑‍🍳 A visualizer for your agents (in herdr)
- [IvoryHeart/herdr-world](https://github.com/IvoryHeart/herdr-world) — Herdr World — a multi-surface web experience for Herdr
- [maedana/herdr-whereami](https://github.com/maedana/herdr-whereami) — Herdr plugin that automatically renames tabs to show where you are, e.g. repo-name/branch when inside a git r…
- [suisya-systems/herdr-agent-office](https://github.com/suisya-systems/herdr-agent-office) — Your agent fleet as a pixel-art office - a herdr plugin. See who's working, who's stuck, and jump to them.
- [dev-shimada/herdr-auto-tab-name](https://github.com/dev-shimada/herdr-auto-tab-name) — herdr plugin: automatically name tabs after their current directory
- [winoooops/herdr-agent-title-sync](https://github.com/winoooops/herdr-agent-title-sync) — Automatic Herdr pane title sync for Claude Code, Codex, Kimi Code, OpenCode, and other coding agents.
- [eduardoborges/herdr-claude-title-hook](https://github.com/eduardoborges/herdr-claude-title-hook) — Claude Code plugin that syncs the session title to the Herdr tab title
- [filoozom/herdr-title](https://github.com/filoozom/herdr-title) — A Herdr plugin that shows the selected worktree and agent activity in your terminal tab title.
- [go-min/herdr-pane-name](https://github.com/go-min/herdr-pane-name) — Herdr plugin that automatically names panes in your terminal sessions.
- [jovylle/herdr-session-title-name](https://github.com/jovylle/herdr-session-title-name) — Herdr plugin: terminal_title_stripped → tab persistence (session_title alone on top, tab keeps it after close)
- [KazBrekker1/herdr-hasr](https://github.com/KazBrekker1/herdr-hasr) — Hasr (حصر — enumeration, a complete tally) — goto-style popup switcher for herdr: switch, rename, delete & cr…
- [khatriafaz/herdr-plugin-auto-rename](https://github.com/khatriafaz/herdr-plugin-auto-rename) — Automatically rename fresh Herdr workspaces and Git branches from a Pi session's first prompt.
- [maxBRT/herdr-omarchy-theme-sync](https://github.com/maxBRT/herdr-omarchy-theme-sync) — Sync Herdr's UI palette with the active Omarchy theme
- [ralphilius/herdr-pr-tab-renamer](https://github.com/ralphilius/herdr-pr-tab-renamer) — Herdr plugin that renames tabs with detected pull request numbers.

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-text"></a>

## Text & URL Grabbing

> I want to grab strings, paths, or URLs shown on screen without touching the mouse

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-pluck**](https://github.com/rmarganti/herdr-pluck)<br><sub>rmarganti</sub> | quickly copy pattern-matched strings from Herdr panes | `rust` | 22 | 2026-08-07 |
| [**herdr-tiny-fingers**](https://github.com/hotchpotch/herdr-tiny-fingers)<br><sub>hotchpotch</sub> | tmux-fingers style visible-screen copy hints for Herdr | `tools` `rust` | 9 | 2026-08-04 |
| [**herdr-scratchpad**](https://github.com/vjeantet/herdr-scratchpad)<br><sub>vjeantet</sub> | One buffer per tab to prepare your prompt, one key to drop it to your agent's input box. | `clipboard` `ratatui` `rust` `scratchpad` `terminal` | 5 | 🔄 2026-08-31 |
| [**herdr-fingers**](https://github.com/hitaishi2222/herdr-fingers)<br><sub>hitaishi2222</sub> | Fingers to clipboard: A smart overlay to pick information from a current pane. | `python` | 4 | 2026-07-16 |
| [**herdr-copy-search**](https://github.com/qq88976321/herdr-copy-search)<br><sub>qq88976321</sub> | regex and copycat pattern search with extrakto token extraction for herdr scrollback, landing in a tmux-style copy mode (OSC 52) | `copy-mode` `rust` `terminal` `tmux` | 3 | 2026-08-04 |
| [**🆕 herdr-flash**](https://github.com/youguanxinqing/herdr-flash)<br><sub>youguanxinqing</sub> | flash.nvim-style search, select, and yank for Herdr panes | `rust` `terminal` | 3 | 🔄 2026-09-02 |
| [**herdr-agent-copy-paste-fork**](https://github.com/calebcauthon/herdr-agent-copy-paste-fork)<br><sub>calebcauthon</sub> | fork by simply copying and pasting, or hotkey the fork into a new pane | `claude-code` `codex` `shell` | 2 | 2026-07-24 |
| [**herdr-paste-image**](https://github.com/ddfonseca/herdr-paste-image)<br><sub>ddfonseca</sub> | Paste clipboard images into herdr panes as file paths — tmux-paste-image, ported to herdr | `shell` | 2 | 2026-07-30 |
| [**herdr-s3-clipboard**](https://github.com/jagzmz/herdr-s3-clipboard)<br><sub>jagzmz</sub> | Publish clipboard images as reusable public or presigned URLs from Herdr using S3-compatible storage. | `aws-s3` `clipboard` `cloudflare-r2` `developer-tools` `image-publishing` | 2 | 2026-07-16 |
| [**🆕 herdr-ferry**](https://github.com/wavrin/herdr-ferry)<br><sub>wavrin</sub> | Move files and clipboard between the Herdr box and your laptop over SSH — no cloud bucket | `rust` | 2 | 🔄 2026-08-29 |
| [**herdr-scrollback-capture**](https://github.com/alexjsp/herdr-scrollback-capture)<br><sub>alexjsp</sub> | Herdr plugin that saves the focused pane's scrollback to your Desktop as HTML or text | `shell` | 1 | 2026-06-30 |
| [**herdr-leap**](https://github.com/RooseveltAdvisors/herdr-leap)<br><sub>RooseveltAdvisors</sub> | EasyMotion/leap-style character jump + select-to-copy for the Herdr terminal multiplexer | `easymotion` `rust` `terminal` `tui` | 1 | 2026-07-24 |
| [**🆕 herdr-copy-hints**](https://github.com/rotemb-wond/herdr-copy-hints)<br><sub>rotemb-wond</sub> | tmux-fingers-style keyboard copy hints for Herdr: paths, Git SHAs, URLs, and more | `clipboard` `developer-tools` `keyboard-navigation` `productivity` `terminal` | 1 | 2026-07-23 |
| [**herdr-translate**](https://github.com/zackshen/herdr-translate)<br><sub>zackshen</sub> | Herdr plugin: translate mouse-selected terminal text in a centered popover | `rust` | 1 | 🔄 2026-08-25 |
| [**herdr-quickselect**](https://github.com/choplin/herdr-quickselect)<br><sub>choplin</sub> | Select visible terminal text and run configurable actions in Herdr. | `go` | 0 | 🔄 2026-08-24 |
| [**herdr-flash**](https://github.com/codingfragments/herdr-flash)<br><sub>codingfragments</sub> | Port of zellij-flash (Zellij plugin) to run as a native Herdr plugin | `rust` | 0 | 🔄 2026-08-26 |
| [**herdr-zextract**](https://github.com/codingfragments/herdr-zextract)<br><sub>codingfragments</sub> | Port of zextract (Zellij plugin) to run as a native Herdr plugin | `rust` | 0 | 🔄 2026-08-18 |
| [**herdr-vaultr**](https://github.com/connerohnesorge/herdr-vaultr)<br><sub>connerohnesorge</sub> | Official herdr plugin for vaultr — copy, show, fork, and search captured agent sessions from the pane they ran in | `vaultr` `shell` | 0 | 2026-08-13 |
| [**🆕 herdr-context-locator**](https://github.com/Dimon94/herdr-context-locator)<br><sub>Dimon94</sub> | Copy a self-describing locator for a Herdr agent's canonical native session context | `python` | 0 | 🔄 2026-08-26 |
| [**herdr-thumbs**](https://github.com/sd2k/herdr-thumbs)<br><sub>sd2k</sub> | tmux-thumbs for Herdr: hint-pick anything on screen, copy it, paste it, or open it | `tmux-thumbs` `shell` | 0 | 🔄 2026-08-21 |
| [**herdr-lens**](https://github.com/VoidAxon/herdr-lens)<br><sub>VoidAxon</sub> | Select text in a Herdr pane, press a key, read it in your own language. Translation, dictionary, identifier lookup and summaries — stdlib-only, zero config. | `ai` `cli` `terminal` `translation` `python` | 0 | 🔄 2026-08-25 |
| [**herdr-translate**](https://github.com/wenPKtalk/herdr-translate)<br><sub>wenPKtalk</sub> | Herdr plugin: translate the selected text in a pane with translate-shell, shown in a floating popup (macOS and Linux) | `translate` `shell` | 0 | 🔄 2026-08-19 |
| [**herdr-copy-pane-id**](https://github.com/wine-fall/herdr-copy-pane-id)<br><sub>wine-fall</sub> | Herdr plugin: copy the focused pane's id to the clipboard, or show every pane's id on its border | `cli` `terminal` `python` | 0 | 🔄 2026-08-24 |

<details><summary>Also relevant to this purpose</summary>

- [nicosuave/memex](https://github.com/nicosuave/memex) — Search Claude Code, Codex, Pi, OpenCode, Github Copilot & Cursor transcripts. Resume sessions. Track tokens.
- [iurysza/termscope](https://github.com/iurysza/termscope) — Open files and links already visible on your terminal screen in a split.
- [jlimas/herdr-worktree-seed](https://github.com/jlimas/herdr-worktree-seed) — Herdr plugin that seeds new worktrees with copy-on-write node_modules and configurable local dotfiles
- [tanshio/herdr-worktreeinclude](https://github.com/tanshio/herdr-worktreeinclude) — Herdr plugin: copy gitignored files matching .worktreeinclude into newly created worktrees
- [shadowfax92/herdr-comments](https://github.com/shadowfax92/herdr-comments) — Annotate copied Herdr terminal output, collect per-pane comments, and review them in Neovim.
- [crexi/herdr-worktree-copy](https://github.com/crexi/herdr-worktree-copy) — Herdr plugin that copies and symlinks worktree-local files from a .worktree-copy manifest
- [Feasy01/herdr-allow](https://github.com/Feasy01/herdr-allow) — herdr plugin: copy gitignored files (.env, secrets, local configs) into every new worktree via a .herdr-allow…
- [Angel-O/herdr-agent-resume](https://github.com/Angel-O/herdr-agent-resume) — Herdr plugin that inserts or copies resume commands to smoothly resume AI agent sessions
- [eightHundreds/herdr-worktreeinclude](https://github.com/eightHundreds/herdr-worktreeinclude) — Herdr plugin: copy .worktreeinclude-selected gitignored files into new worktrees
- [itayo-m/herdr-tab-session-name-sync](https://github.com/itayo-m/herdr-tab-session-name-sync) — Syncs agent session name with herdr tabs and panes title
- [jtnovellis/herdr-worktree-setup](https://github.com/jtnovellis/herdr-worktree-setup) — herdr plugin: make a new git worktree immediately usable — copy .env & dev state, clone dependency caches (AP…
- [scoussens-nthplusio/herdr-worktree-include](https://github.com/scoussens-nthplusio/herdr-worktree-include) — Copy gitignored files such as .env into new Herdr worktrees, using the repository's .worktreeinclude — the sa…
- [willian/herdr-fzf-url](https://github.com/willian/herdr-fzf-url) — Pick URLs from the focused pane with `fzf`, then open or copy them.
- [zerodice0/herdr-plugin-worktree-bootstrap](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap) — Safely copy ignored local files and run setup commands in new Herdr Git worktrees

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-meta"></a>

## Plugin Management & Authoring

> I want to manage plugins themselves, or build my own

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-plus**](https://github.com/cloudmanic/herdr-plus)<br><sub>cloudmanic</sub> | An extension for herdr, built as a first-class herdr plugin — a collection of tools that make it better: Projects and Quick Actions. | `go` | 280 | 🔄 2026-08-28 |
| [**herdr-lazy**](https://github.com/natori-hrj/herdr-lazy)<br><sub>natori-hrj</sub> | Declarative plugin manager and curated distro for herdr — one list, a real lockfile, a manage pane. | `cli` `lockfile` `plugin-manager` `rust` `terminal` | 22 | 🔄 2026-09-01 |
| [**herdr-plugin-manager**](https://github.com/speardragon/herdr-plugin-manager)<br><sub>speardragon</sub> | Manage herdr plugins from a popup — install, update, enable/disable, uninstall, and browse the herdr-plugin marketplace. Recommended key: prefix+p | `plugin-manager` `tui` `shell` | 21 | 🔄 2026-08-19 |
| [**house-of-herdr**](https://github.com/alasano/house-of-herdr)<br><sub>alasano</sub> | A collection of plugins for Herdr, including Codex Micro: agent status lights and controls on the Work Louder Codex Micro | `codex-micro` `work-louder` `typescript` | 4 | 2026-08-13 |
| [**herdr-plugin-rust**](https://github.com/Newt6611/herdr-plugin-rust)<br><sub>Newt6611</sub> | A Rust application framework for building Herdr plugins. | `rust` | 2 | 2026-07-09 |
| [**herdr-plugins**](https://github.com/alastairsounds/herdr-plugins)<br><sub>alastairsounds</sub> | Plugins for herdr | `rust` | 1 | 🔄 2026-08-28 |
| [**herdr-plugins-labs**](https://github.com/hmu332233/herdr-plugins-labs)<br><sub>hmu332233</sub> | Experimental plugins for Herdr — incubated here, graduated to their own repos | `labs` `javascript` | 1 | 🔄 2026-08-24 |
| [**herdr-plugin-manager**](https://github.com/a-curious-coder/herdr-plugin-manager)<br><sub>a-curious-coder</sub> | Manage and discover herdr plugins from a single popup pane — install/uninstall/update, run or bind actions, browse the public registry. | `shell` | 0 | 2026-08-13 |
| [**herdr-plugins**](https://github.com/tyler-jewell/herdr-plugins)<br><sub>tyler-jewell</sub> | Pure-Rust Herdr plugins monorepo (stdlib-first). Install with: herdr plugin install tyler-jewell/herdr-plugins/<subdir> | `rust` `go` | 0 | 2026-08-10 |

<details><summary>Also relevant to this purpose</summary>

- [JefeLabs/herdr-web-broker](https://github.com/JefeLabs/herdr-web-broker) — Self-hosted REST/WS API for herdr: spawn and steer coding agents from anywhere — tokens, multi-user session o…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-other"></a>

## Other & Utilities

> Handy things that don't fit any of the categories above

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**terminal-browser**](https://github.com/zenbu-labs/terminal-browser)<br><sub>zenbu-labs</sub> | A browser inside your terminal | `browser` `claude-code` `claude-skills` `cli` `codex` | 2497 | 🔄 2026-08-31 |
| [**herdr-lantern**](https://github.com/aigorahub/herdr-lantern)<br><sub>aigorahub</sub> | Lantern, by Elves. A Herdr plugin: the herd is in the field; Lantern illuminates who needs you and what they are working toward. | `shell` | 58 | 🔄 2026-08-26 |
| [**herdr-plugins-directory**](https://github.com/MIDO-ruby7/herdr-plugins-directory)<br><sub>MIDO-ruby7</sub> | A link collection for finding herdr plugins by what you want to get done. | `python` | 10 | 🔄 2026-09-01 |
| [**neon-herdr**](https://github.com/neon-solutions/neon-herdr)<br><sub>neon-solutions</sub> | The official Neon Herdr Plugin | `typescript` | 10 | 2026-08-06 |
| [**herdr-commandcode-plugin**](https://github.com/TheMetalStorm/herdr-commandcode-plugin)<br><sub>TheMetalStorm</sub> | Integrates Commandcode into Herdr | `cli` `commandcode` `herdr-integration` `shell` | 7 | 2026-07-30 |
| [**herdr-plugin-cmux**](https://github.com/lachieh/herdr-plugin-cmux)<br><sub>lachieh</sub> | Mirrors every herdr-managed agent into a cmux sidebar as its own live row, with a status pill and a click-to-jump task line. | `javascript` | 6 | 2026-07-01 |
| [**wave-tui**](https://github.com/takemo101/wave-tui)<br><sub>takemo101</sub> | Quiet terminal radio for work sessions | `rust` | 4 | 2026-07-20 |
| [**herdr-memory**](https://github.com/jatingargiitk/herdr-memory)<br><sub>jatingargiitk</sub> | A Herdr plugin that builds a living brain from your coding sessions — progressively learning what works, what failed, and what you decided. | `shell` | 3 | 2026-08-11 |
| [**🆕 herdr-standup**](https://github.com/neospeed83/herdr-standup)<br><sub>neospeed83</sub> | Evidence-backed daily standups from Git activity and Herdr context. | `developer-tools` `standup` `rust` | 2 | 🔄 2026-08-31 |
| [**herdr-streamdeck**](https://github.com/Pimpmuckl/herdr-streamdeck)<br><sub>Pimpmuckl</sub> | Physical control for Herdr on Elgato Stream Deck+ | `typescript` | 2 | 2026-08-15 |
| [**herdr-suite-site**](https://github.com/StructuPath/herdr-suite-site)<br><sub>StructuPath</sub> | Landing page for the StructuPath Herdr Suite — herdr.structupath.ai | `herdr-integration` `html` | 2 | 2026-07-31 |
| [**herdr-freebuff-plugin**](https://github.com/TheMetalStorm/herdr-freebuff-plugin)<br><sub>TheMetalStorm</sub> | Freebuff lifecycle integration plugin for Herdr — reports idle/working/blocked state via file polling and PTY content scraping | `cli` `freebuff` `herdr-integration` `shell` | 2 | 2026-07-22 |
| [**herdr-edit-windows**](https://github.com/aclima01/herdr-edit-windows)<br><sub>aclima01</sub> | A simple text editor that runs in a herdr pane beside your coding agent — file tree, syntax-highlighted editor, and an uncommitted-diff tab. Windows-only. | `rust` | 1 | 2026-07-25 |
| [**herdr-stoplight**](https://github.com/BowlOfSoup/herdr-stoplight)<br><sub>BowlOfSoup</sub> | Drive a physical Arduino traffic-light module from the live status of Herdr | `go` | 1 | 2026-07-11 |
| [**🆕 harbr**](https://github.com/dev-town/harbr)<br><sub>dev-town</sub> | Harbour TUI | `typescript` | 1 | 🔄 2026-08-31 |
| [**herdr-rainfrog**](https://github.com/fraction12/herdr-rainfrog)<br><sub>fraction12</sub> | Open Rainfrog in a managed HerdR pane. | `shell` | 1 | 2026-08-15 |
| [**herdr-openlogi**](https://github.com/giacolees/herdr-openlogi)<br><sub>giacolees</sub> | Logitech mouse → herdr via OpenLogi binding overlay | `ghostty` `logitech-mouse` `macos` `openlogi` `shell` | 1 | 🔄 2026-08-24 |
| [**hrd**](https://github.com/joshuadavidthomas/hrd)<br><sub>joshuadavidthomas</sub> | Manage your herd of sandboxes and the Herdr sessions running on them | `go` | 1 | 🔄 2026-08-28 |
| [**🆕 herdr-plugins**](https://github.com/narumiruna/herdr-plugins)<br><sub>narumiruna</sub> | _(no description)_ | `rust` | 1 | 2026-08-08 |
| [**herdr-phin-util**](https://github.com/phin-tech/herdr-phin-util)<br><sub>phin-tech</sub> | Personal Herdr Utils | `bubbletea` `tui` `go` | 1 | 🔄 2026-08-18 |
| [**herdr-api-client**](https://github.com/playsthisgame/herdr-api-client)<br><sub>playsthisgame</sub> | HTTP/REST API client in a herdr split pane or tab — browse, run and test requests without leaving the terminal | `http-client` `rest-client` `tui` `shell` | 1 | 2026-08-08 |
| [**pixtui**](https://github.com/RizRiyz/pixtui)<br><sub>RizRiyz</sub> | Pixel Art Editor on Terminal | `bohay-module` `editor` `luvus-module` `pixel-art` `termina` | 1 | 2026-08-07 |
| [**herdr-jetbrains**](https://github.com/Soemii/herdr-jetbrains)<br><sub>Soemii</sub> | _(no description)_ | `go` | 1 | 2026-08-09 |
| [**herdr-sidepulse**](https://github.com/third774/herdr-sidepulse)<br><sub>third774</sub> | _(no description)_ | `javascript` | 1 | 2026-08-14 |
| [**herdr-plugin-k8s-context**](https://github.com/tkuchiki/herdr-plugin-k8s-context)<br><sub>tkuchiki</sub> | Open Herdr tabs with isolated Kubernetes contexts and namespaces. | `go` | 1 | 2026-08-15 |
| [**herdr-zen**](https://github.com/y4m3/herdr-zen)<br><sub>y4m3</sub> | Zen mode for Herdr with an adjustable centered pane width | `rust` `terminal` `zen-mode` | 1 | 🔄 2026-08-19 |
| [**🆕 multitrunk-herdr-plugin**](https://github.com/yoyoyeti/multitrunk-herdr-plugin)<br><sub>yoyoyeti</sub> | Herdr plugin for multitrunk task workspaces | `git` `multitrunk` `rust` | 1 | 🔄 2026-08-31 |
| [**herdr-panes**](https://github.com/atm028/herdr-panes)<br><sub>atm028</sub> | _(no description)_ | `python` | 0 | 2026-08-01 |
| [**hrdr-azure-plugin**](https://github.com/gbaeke/hrdr-azure-plugin)<br><sub>gbaeke</sub> | Herdr plugin: browse Azure resource groups and resources; click a resource to open it in the Azure portal | `azure` `javascript` | 0 | 🔄 2026-08-23 |
| [**capslock-herdr-prefix**](https://github.com/GHJQ/capslock-herdr-prefix)<br><sub>GHJQ</sub> | Make Caps Lock the herdr prefix key on macOS | `capslock` `macos` `shell` | 0 | 2026-08-11 |
| [**herdr-attach**](https://github.com/gilvanecesar/herdr-attach)<br><sub>gilvanecesar</sub> | Pick local files from a Herdr popup and send them to the focused coding agent, attaching file context without leaving the terminal. | `javascript` | 0 | 2026-07-26 |
| [**herdr-llama**](https://github.com/hitaishi2222/herdr-llama)<br><sub>hitaishi2222</sub> | Control your llama-server from your fingertips. | `llama-cpp` `local-ai` `python` | 0 | 2026-07-16 |
| [**herdr-pane-update-timestamps**](https://github.com/johnlindquist/herdr-pane-update-timestamps)<br><sub>johnlindquist</sub> | Herdr plugin for timestamped, scrollable pane output observations | `rust` | 0 | 2026-07-29 |
| [**herdr-status**](https://github.com/jrswab/herdr-status)<br><sub>jrswab</sub> | Ambient machine status pane for Herdr on Linux. | `go` | 0 | 2026-07-30 |
| [**herdr-laravel-tinker**](https://github.com/lancodev/herdr-laravel-tinker)<br><sub>lancodev</sub> | Split-style Laravel tinker REPL for herdr — editor beside live results, as a pane or popup | `laravel` `tinker` `php` `repl` | 0 | 2026-07-16 |
| [**herdr-new-task**](https://github.com/leonho/herdr-new-task)<br><sub>leonho</sub> | herdr plugin: one keystroke to pick a project dir and launch claude in a new tab, with noun-first tab labels | `python` | 0 | 2026-07-16 |
| [**herdr-plugin-loopreview**](https://github.com/loopkeep/herdr-plugin-loopreview)<br><sub>loopkeep</sub> | Herdr plugin for loopreview | `rust` | 0 | 2026-07-23 |
| [**strays**](https://github.com/m1sk9/strays)<br><sub>m1sk9</sub> | A TUI for Centralized Management of Claude Code | `claude-code` `llm` `tui` `rust` | 0 | 🔄 2026-08-29 |
| [**herdr-source-control**](https://github.com/mariotmc/herdr-source-control)<br><sub>mariotmc</sub> | _(no description)_ | `go` | 0 | 2026-08-15 |
| [**herdr-brainrot**](https://github.com/marius-se/herdr-brainrot)<br><sub>marius-se</sub> | DOOM in a Herdr pane while your agents cook — brainrot plugin with pluggable apps | `doom` `go` | 0 | 2026-08-06 |
| [**herdr-git-pull**](https://github.com/nimrc/herdr-git-pull)<br><sub>nimrc</sub> | _(no description)_ | `python` | 0 | 2026-08-13 |
| [**ayatsumugi**](https://github.com/nkwork9999/ayatsumugi)<br><sub>nkwork9999</sub> | Local-first React DOM, Fiber, and state graph visualization for Ayatori and Tsumugi | `cmux` `ghostty` `orca` `react-devtools` `javascript` | 0 | 🔄 2026-08-26 |
| [**herdr-action-launcher**](https://github.com/nnexai/herdr-action-launcher)<br><sub>nnexai</sub> | _(no description)_ | `javascript` | 0 | 2026-08-05 |
| [**🆕 herdr-bot**](https://github.com/Phoobobo/herdr-bot)<br><sub>Phoobobo</sub> | _(no description)_ | `tui` `typescript` | 0 | 🔄 2026-08-31 |
| [**herdr-traex-integration**](https://github.com/Phoobobo/herdr-traex-integration)<br><sub>Phoobobo</sub> | Herdr plugin that supports traex integration | `shell` | 0 | 2026-07-02 |
| [**herdr-handsfree**](https://github.com/RanolP/herdr-handsfree)<br><sub>RanolP</sub> | Hands-free herdr plugin: voice dictation (whisper.cpp) + webcam gaze mouse for macOS | `rust` | 0 | 2026-07-30 |
| [**🆕 herdr-browser**](https://github.com/redsquiggle/herdr-browser)<br><sub>redsquiggle</sub> | Keep Chromium tab groups aligned with Herdr workspaces | `chromium` `ratatui` `rust` | 0 | 2026-07-28 |
| [**herdr-cwd-control**](https://github.com/skinp/herdr-cwd-control)<br><sub>skinp</sub> | A herdr plugin for enhanced control over initial working directory for new workspaces, tabs & panes. | `python` | 0 | 2026-08-10 |
| [**herdr-now-playing**](https://github.com/spywhere/herdr-now-playing)<br><sub>spywhere</sub> | Add music player with music control through key bindings to herdr | `shell` | 0 | 🔄 2026-08-22 |
| [**herdr-plugins**](https://github.com/tomaszhanc/herdr-plugins)<br><sub>tomaszhanc</sub> | A personal monorepo of herdr plugins, each living in its own folder with a herdr-plugin.toml manifest and an executable. | — | 0 | 2026-07-16 |
| [**🆕 herdr-git-dirty**](https://github.com/viko16/herdr-git-dirty)<br><sub>viko16</sub> | A lightweight Herdr plugin that shows uncommitted Git file counts in each Space. | `git` `shell` | 0 | 🔄 2026-09-02 |

[⬆ Back to purposes](#purposes)

## Installing

```sh
# pass the owner/repo from any row in the table above
herdr plugin install ogulcancelik/herdr-plugin-github-start
herdr plugin list
```

Plugins that live in a subdirectory use the `owner/repo/subdir` form. See [Plugins](https://herdr.dev/docs/plugins/) and [Marketplace](https://herdr.dev/docs/marketplace/) for details.

## Fixing this list

If a category looks off, you want to add tags, or attach a short note, add an entry to [`data/overrides.json`](data/overrides.json) and send a PR.

```json
{
  "owner/repo": {
    "category": "notify",
    "add_tags": ["macos"],
    "note": "needs ntfy topic configured during setup"
  }
}
```

Category keys: `notify`, `remote`, `agents`, `worktree`, `review`, `forge`, `layout`, `navigate`, `files`, `cost`, `monitor`, `finder`, `automation`, `session`, `naming`, `text`, `meta`, `other`

For repos with no GitHub description, override it with a `description` key (in English; add ja/zh translations to `data/translations.json`).

Listing is fully automatic — any repo gets included as soon as it's tagged with the GitHub topic `herdr-plugin` (no need to submit it here).

---

*README.en.md and `data/plugins.json` are generated by [`scripts/build.py`](scripts/build.py). Please don't edit them directly.*
