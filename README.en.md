# herdr plugins by purpose

[🇯🇵 日本語](README.md) · 🇺🇸 English · [🇨🇳 中文](README.zh.md)

**A link collection for finding [herdr](https://herdr.dev/) plugins by what you want to get done.**

- **461** plugins indexed / last updated **2026-08-02 13:53 UTC** (auto-refreshed every 6 hours)
- Source: GitHub repositories tagged [`herdr-plugin`](https://github.com/topics/herdr-plugin) — the same population as the official [herdr.dev/plugins](https://herdr.dev/plugins/) marketplace
- Categories are auto-inferred from each repo's description and topics. If one looks wrong, fix it with a PR to [`data/overrides.json`](data/overrides.json)
- Install: `herdr plugin install owner/repo` — [official docs](https://herdr.dev/docs/plugins/)

> [!WARNING]
> This is an auto-collected index, not a vetted catalog. Plugins are code that runs directly on your machine, so check the manifest and the commands it runs before installing.

<a id="purposes"></a>

## Browse by purpose

- [**Notifications & Alerts**](#cat-notify) (21) — I want to know when an agent finishes or gets stuck waiting for input, even when I'm away from my desk
- [**Mobile & Remote Control**](#cat-remote) (18) — I want to monitor agents from my phone or while away, and just send back approvals
- [**Agent Orchestration**](#cat-agents) (53) — I want to launch, split up, and manage multiple AI agents together
- [**Git Worktrees & Branches**](#cat-worktree) (27) — I want to spin up a worktree for each piece of work, and have the cleanup handled automatically too
- [**Code Review & Diffs**](#cat-review) (22) — I want to read the diff an agent wrote and send comments back on it
- [**GitHub & Issue Trackers**](#cat-forge) (19) — I want to kick off work from an issue or PR, and track PR status
- [**Workspaces & Layouts**](#cat-layout) (21) — When I open a project, I want tabs, panes, and startup commands all set up in one shot
- [**Pane Navigation & Keys**](#cat-navigate) (56) — I want to move and resize between panes and workspaces using the same keys as my editor
- [**File Viewers & Editors**](#cat-files) (37) — I want to open a file tree inside a pane, or keep it in sync with my editor
- [**Tokens & Cost**](#cat-cost) (6) — I want to see how much an agent is spending, and cut down on usage
- [**Monitoring & Dashboards**](#cat-monitor) (24) — I want an at-a-glance overview of agent and machine status
- [**Fuzzy Finders & Palettes**](#cat-finder) (48) — I want to invoke commands or projects even when I only half-remember their names
- [**Automation, Hooks & Schedules**](#cat-automation) (25) — I want a fixed set of steps to run automatically on worktree creation or at a chosen time
- [**Session State & Restore**](#cat-session) (20) — I want to close my work and later resume from exactly the same state
- [**Titles, Naming & Looks**](#cat-naming) (22) — I want tab names and terminal titles to be automatically clear, or want to change how things look
- [**Text & URL Grabbing**](#cat-text) (10) — I want to grab strings, paths, or URLs shown on screen without touching the mouse
- [**Plugin Management & Authoring**](#cat-meta) (6) — I want to manage plugins themselves, or build my own
- [**Other & Utilities**](#cat-other) (26) — Handy things that don't fit any of the categories above

<a id="cat-notify"></a>

## Notifications & Alerts

> I want to know when an agent finishes or gets stuck waiting for input, even when I'm away from my desk

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-focus-notify**](https://github.com/yankewei/herdr-focus-notify)<br><sub>yankewei</sub> | Clickable macOS notifications for Herdr agents. Sends a native toast when an agent becomes blocked or done; clicking it brings the terminal forward and focuses… | `alerter` `macos` `notifications` `productivity` `rust` | 8 | 🆕 2026-07-24 |
| [**herdr-ntfy-notify**](https://github.com/zom-2018/herdr-ntfy-notify)<br><sub>zom-2018</sub> | Real-time ntfy push notifications for Herdr terminal agents | `agent` `ntfy` `push-notifications` `tui` `javascript` | 6 | 2026-06-23 |
| [**herdr-terminal-notifier**](https://github.com/dot/herdr-terminal-notifier)<br><sub>dot</sub> | Customizable macOS notifications for herdr agent state changes via terminal-notifier | `macos` `terminal-notifier` `shell` | 5 | 2026-07-14 |
| [**herdr-pings**](https://github.com/joelhooks/herdr-pings)<br><sub>joelhooks</sub> | Turn-level wake events for AI agents in herdr panes — pi extension, wait CLI, crash bridge, and Discworld callsigns for your workers | `ai-agents` `pi` `typescript` | 5 | 🆕 2026-07-24 |
| [**herdr-ntfy**](https://github.com/horn553/herdr-ntfy)<br><sub>horn553</sub> | Minimal dependencies: jq, curl, and sh — send ntfy notifications when Herdr agents finish or get blocked. | `shell` | 4 | 🆕 2026-08-01 |
| [**herdr-notify-windows**](https://github.com/aclima01/herdr-notify-windows)<br><sub>aclima01</sub> | Windows 11 toast notifications for herdr agents (turn finished / needs input) | `powershell` | 3 | 🆕 2026-07-23 |
| [**herdr-telegram-plugin**](https://github.com/mvallebr/herdr-telegram-plugin)<br><sub>mvallebr</sub> | Telegram bot companion for herdr — remote control any agent via Telegram forum topics, zero LLM in the path. | `typescript` | 3 | 🆕 2026-07-31 |
| [**herdr-hail**](https://github.com/natori-hrj/herdr-hail)<br><sub>natori-hrj</sub> | Two-way Slack & Discord bridge for herdr — get pinged when an agent blocks, reply/tap to unblock. No tunnel. | `discord` `slack` `typescript` | 2 | 🆕 2026-07-19 |
| [**herdr-guard**](https://github.com/StructuPath/herdr-guard)<br><sub>StructuPath</sub> | Cross-agent command policy for Herdr: audit, alert, and interrupt dangerous shell commands | `ai-agents` `command-policy` `security` `terminal` `javascript` | 2 | 🆕 2026-07-28 |
| [**session-sounds**](https://github.com/ChrisPachulski/session-sounds)<br><sub>ChrisPachulski</sub> | Distinct per-agent completion and attention sounds for Herdr on macOS and Linux. | `coding-agents` `notifications` `rust` | 1 | 🆕 2026-07-19 |
| [**herdr-telegram-bridge**](https://github.com/cokekitten/herdr-telegram-bridge)<br><sub>cokekitten</sub> | Get a Telegram push when a herdr agent finishes or blocks — reply to it to send text or files straight back into that agent. No server, no tunnel, no app. | `ai-agents` `chatops` `claude-code` `developer-tools` `notifications` | 1 | 🆕 2026-07-26 |
| [**herdr-announcer**](https://github.com/nhclink16/herdr-announcer)<br><sub>nhclink16</sub> | Herdr plugin: speaks a one-sentence LLM summary when an agent finishes or needs input — local TTS, ElevenLabs, or any custom command | `tts` `python` | 1 | 🆕 2026-07-30 |
| [**herdr-notify-back**](https://github.com/vjbee/herdr-notify-back)<br><sub>vjbee</sub> | Clickable macOS notifications for Herdr that jump you back to the agent pane that needs you | `macos` `notifications` `terminal` `python` | 1 | 🆕 2026-07-30 |
| [**herdr-prompt-reply**](https://github.com/cedrus-8864/herdr-prompt-reply)<br><sub>cedrus-8864</sub> | Answer herdr agent permission prompts straight from a macOS notification — real answer buttons, single Swift binary, nothing waiting in the background | `ai-agents` `claude-code` `macos` `macos-notifications` `notifications` | 0 | 🆕 2026-07-28 |
| [**herdr-slack-notify**](https://github.com/juninaba/herdr-slack-notify)<br><sub>juninaba</sub> | Send Slack notifications when Herdr agents finish or get blocked. | `javascript` | 0 | 2026-07-07 |
| [**drover-notify**](https://github.com/keinstn/drover-notify)<br><sub>keinstn</sub> | Herdr plugin that sends Drover push notifications when an agent becomes blocked | `javascript` | 0 | 🆕 2026-08-01 |
| [**herdr-telegram-slack-bridge**](https://github.com/lsisoft/herdr-telegram-slack-bridge)<br><sub>lsisoft</sub> | Bidirectional Telegram and Slack bot bridge for Herdr agent sessions, routing blocked-agent alerts and chat replies back to Herdr or tmux panes | `ai-agents` `slack-bot` `telegram-bot` `tmux` `python` | 0 | 🆕 2026-07-28 |
| [**herdr-plugin-telegram-notify**](https://github.com/OiAnthony/herdr-plugin-telegram-notify)<br><sub>OiAnthony</sub> | Standalone Herdr plugin that sends Telegram notifications when an agent is done or blocked. | `javascript` | 0 | 2026-07-16 |
| [**herdr-apple-music-plugin**](https://github.com/perlporter/herdr-apple-music-plugin)<br><sub>perlporter</sub> | Shows a toast in herdr when the currently playing track changes in Apple Music (macOS) | `shell` | 0 | 🆕 2026-07-28 |
| [**herdr-notify-wsl**](https://github.com/saeedrahimi/herdr-notify-wsl)<br><sub>saeedrahimi</sub> | Windows 11 toast notifications for herdr agents running inside WSL. Based on aclima01/herdr-notify-windows. | `powershell` | 0 | 🆕 2026-07-23 |
| [**herdr-cc-mac-notify**](https://github.com/y-hirakaw/herdr-cc-mac-notify)<br><sub>y-hirakaw</sub> | macOS notifications for Claude Code — shows the agent's real last message, not just "done" | `claude-code` `macos` `notifications` `python` | 0 | 2026-07-17 |

[⬆ Back to purposes](#purposes)

<a id="cat-remote"></a>

## Mobile & Remote Control

> I want to monitor agents from my phone or while away, and just send back approvals

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**collie**](https://github.com/AltanS/collie)<br><sub>AltanS</sub> | PWA to manage 🐑 herdr on the go. Tailnet accessible, push notifications, quick actions and more. | `typescript` | 220 | 🆕 2026-07-30 |
| [**herdr-remote**](https://github.com/dcolinmorgan/herdr-remote)<br><sub>dcolinmorgan</sub> | Monitor and drive your herdr agents from menu bar, phone, or Telegram. Zero config locally. Free tunnel for remote. No Tailscale needed. | `macos` `mobile` `python` | 170 | 🆕 2026-07-31 |
| [**herdr-mobile-relay**](https://github.com/0cv/herdr-mobile-relay)<br><sub>0cv</sub> | Approve and monitor Herdr agents remotely from your phone — a mobile web app for Android/iOS smartphones with push notifications, QR setup, and multi-computer… | `android` `approvals` `cloudflare` `ios` `mobile` | 23 | 🆕 2026-08-01 |
| [**herdr-push**](https://github.com/dcolinmorgan/herdr-push)<br><sub>dcolinmorgan</sub> | herdr plugin: zero-dep event push to herdr-remote for mobile monitoring and one-tap approval | `shell` | 6 | 2026-07-09 |
| [**herdr-tether**](https://github.com/moneycaringcoder/herdr-tether)<br><sub>moneycaringcoder</sub> | Keep local and remote terminal workloads running after their Herdr view closes. | `remote-development` `rust` `ssh` `terminal` `tmux` | 5 | 🆕 2026-07-28 |
| [**merino**](https://github.com/LoneExile/merino)<br><sub>LoneExile</sub> | Merino 🐑 — remote tunnel dashboard for Herdr agents | `go` `macos` `menubar` `react` `wails` | 3 | 🆕 2026-08-02 |
| [**herdr-aws-ssm**](https://github.com/maayanyosef/herdr-aws-ssm)<br><sub>maayanyosef</sub> | Pick an EC2 instance and connect over AWS SSM in a herdr --remote session - no bastion or public IP. | `aws-ssm` `terminal` `shell` | 3 | 2026-07-01 |
| [**herdr-devup**](https://github.com/alon-z/herdr-devup)<br><sub>alon-z</sub> | Herdr plugin: per-project dev layouts from .herdr/dev.toml with tunnel-URL env sync | `typescript` | 2 | 2026-06-22 |
| [**herdr-whistle**](https://github.com/amurru/herdr-whistle)<br><sub>amurru</sub> | Herdr plugin for remote agent management | `golang` `telegrambot` `go` | 2 | 2026-07-04 |
| [**herdr-web**](https://github.com/eyalev/herdr-web)<br><sub>eyalev</sub> | Mobile-first web UI for the herdr agent multiplexer — drive your coding agents from a phone | `claude-code` `mobile` `pwa` `terminal` `javascript` | 2 | 🆕 2026-07-29 |
| [**herdr-phone**](https://github.com/matheus3301/herdr-phone)<br><sub>matheus3301</sub> | Mobile remote console for Herdr over Cloudflare Tunnel and Access | `cloudflare-tunnel` `coding-agents` `developer-tools` `golang` `mobile` | 2 | 🆕 2026-07-29 |
| [**herdr-farm**](https://github.com/mejiasd3v/herdr-farm)<br><sub>mejiasd3v</sub> | Herdr plugin: 3D farm that visualizes your Herdr workspaces and agents as livestock (three.js webapp) | `threejs` `javascript` | 2 | 🆕 2026-07-28 |
| [**sheperd-ssh-app**](https://github.com/kojunseo/sheperd-ssh-app)<br><sub>kojunseo</sub> | Mobile companion site for persistent Herdr sessions over SSH | `android` `github-pages` `herdr-mobile` `ios` `ssh-client` | 1 | 🆕 2026-08-02 |
| [**herdr-approval-gate**](https://github.com/Javamomma/herdr-approval-gate)<br><sub>Javamomma</sub> | Human sign-off gate for agent actions in herdr — run a task in a dedicated pane, verdict-check its transcript, block until a human types APPROVE <initials>. | `shell` | 0 | 2026-07-15 |
| [**herdr-remotedownloder**](https://github.com/kosuketut/herdr-remotedownloder)<br><sub>kosuketut</sub> | Download files from a remote Herdr pane to the connected Mac. | `rust` | 0 | 🆕 2026-08-01 |
| [**herdr-wechat-plugin**](https://github.com/LuYanFCP/herdr-wechat-plugin)<br><sub>LuYanFCP</sub> | A Herdr plugin for wechat remote control | `rust` | 0 | 2026-07-17 |
| [**herdview**](https://github.com/Orchard-Robotics/herdview)<br><sub>Orchard-Robotics</sub> | View your herd from the web | `html` | 0 | 2026-07-17 |
| [**herdr-web-tui**](https://github.com/tigorlazuardi/herdr-web-tui)<br><sub>tigorlazuardi</sub> | Daemon-first browser/PWA frontend for Herdr with an optional plugin launcher | `go` | 0 | 🆕 2026-07-31 |

[⬆ Back to purposes](#purposes)

<a id="cat-agents"></a>

## Agent Orchestration

> I want to launch, split up, and manage multiple AI agents together

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**agentbox**](https://github.com/madarco/agentbox)<br><sub>madarco</sub> | Run multiple agents in parallel sandboxed VMs, with a single command, on your PC or in the cloud | `claude` `claude-code` `cli` `cmux` `codex` | 332 | 🆕 2026-08-01 |
| [**agentbox-herdr-plugin**](https://github.com/madarco/agentbox-herdr-plugin)<br><sub>madarco</sub> | Run multiple agents in parallel sandboxed VMs, with a single command, on your PC or in the cloud | `claude-code` `codex-cli` `opencode` `sandbox` `shell` | 19 | 2026-06-24 |
| [**herdmates**](https://github.com/caioniehues/herdmates)<br><sub>caioniehues</sub> | Claude Code agent teams, native in herdr — teammux shim, mission-control board, focus pane | `agent-teams` `claude-code` `rust` `tui` | 13 | 2026-07-17 |
| [**pi-herd**](https://github.com/ribbons-digital/pi-herd)<br><sub>ribbons-digital</sub> | Visible Pi session orchestration with Herdr panes and git worktrees | `typescript` | 12 | 2026-07-06 |
| [**herdr-board**](https://github.com/nelsonPires5/herdr-board)<br><sub>nelsonPires5</sub> | Kanban board for herdr — cards are prompts dispatched to AI agents in visible panes | `board` `kanban` `kanban-board` `tui` `rust` | 11 | 🆕 2026-07-30 |
| [**vibetty**](https://github.com/second-state/vibetty)<br><sub>second-state</sub> | Share a live AI agent terminal to smart hardware (vibekeys, vibewatch, etc.) over MQTT; can also be used as a Herdr plugin. | `claude-code` `codex` `vibecoding` `rust` | 8 | 🆕 2026-07-31 |
| [**herdr-helpr**](https://github.com/sohanemon/herdr-helpr)<br><sub>sohanemon</sub> | Prompt-driven workspace and pane management for herdr. | `ai-agents` `bun` `cli` `developer-tools` `ink` | 7 | 2026-07-16 |
| [**herdr-browser**](https://github.com/StructuPath/herdr-browser)<br><sub>StructuPath</sub> | Drivable agent-browser pane for Herdr with live streaming, real interaction, adaptive rendering, console/page errors, recording, and localhost routing | `terminal` `javascript` | 7 | 🆕 2026-07-28 |
| [**herdr-agent-handoff**](https://github.com/sanirudh17/herdr-agent-handoff)<br><sub>sanirudh17</sub> | Herdr plugin that hands an in-progress agent session to a fresh session of another installed coding agent, carrying the complete session inside the prompt - no… | `agent-handoff` `claude-code` `codex` `coding-agents` `developer-tools` | 5 | 🆕 2026-08-02 |
| [**herdr-insight**](https://github.com/0x5c0f/herdr-insight)<br><sub>0x5c0f</sub> | Agent State Timeline Panel | `rust` | 4 | 2026-06-23 |
| [**shepherdr**](https://github.com/afogel/shepherdr)<br><sub>afogel</sub> | Shepherd delegated coding agents into visible, auditable herdr panes you can watch, resume, and take over — a herdr plugin. | `ai-agents` `claude-code` `codex` `cursor` `rust` | 4 | 🆕 2026-07-24 |
| [**herdr-triage**](https://github.com/natori-hrj/herdr-triage)<br><sub>natori-hrj</sub> | Attention triage for herdr — ranks your agents by who needs you most; a long-blocked agent rises to the top. | `ai-agents` `triage` `rust` | 4 | 🆕 2026-07-23 |
| [**herdr-catchup**](https://github.com/wilbeibi/herdr-catchup)<br><sub>wilbeibi</sub> | Cross-agent coding-session handoff for herdr: from a live pane, summarize, fork, or hand a Claude Code, Codex, Cursor, Cline, or OpenCode session to another ag… | `ai-agents` `claude-code` `codex` `coding-agents` `context-handoff` | 4 | 🆕 2026-07-27 |
| [**herdr-theos-settler**](https://github.com/calebcauthon/herdr-theos-settler)<br><sub>calebcauthon</sub> | Settle Herdr agent tabs and workspaces below active work to get finished work out of the way. Theo's idea. | `rust` | 3 | 🆕 2026-07-23 |
| [**herdr-espresso**](https://github.com/Hanyang-Li/herdr-espresso)<br><sub>Hanyang-Li</sub> | Keeps your MacBook awake even when the lid closed when agent is running | `rust` | 3 | 🆕 2026-07-25 |
| [**herdr-space-scoped-agents**](https://github.com/ShankyJS/herdr-space-scoped-agents)<br><sub>ShankyJS</sub> | herdr plugin that scopes the agent panel to the space you're focused on | `coding-agents` `terminal` `go` | 3 | 🆕 2026-07-23 |
| [**herdr-swarm**](https://github.com/StructuPath/herdr-swarm)<br><sub>StructuPath</sub> | Parallel coding agents on one repo, safely: worktree-per-agent fan-out, live change visibility, and review-first harvest for Herdr | `terminal` `javascript` | 3 | 🆕 2026-07-28 |
| [**herdr-agent-messenger**](https://github.com/aashishd/herdr-agent-messenger)<br><sub>aashishd</sub> | Send focused, self-contained messages between AI agents running in live Herdr panes, so one agent can coordinate work with another without sharing its full con… | `python` | 2 | 2026-07-10 |
| [**herdr-birdseye**](https://github.com/calebcauthon/herdr-birdseye)<br><sub>calebcauthon</sub> | Birds Eye View of your agents in herdr | `rust` | 2 | 🆕 2026-07-24 |
| [**herdr-orchestrate**](https://github.com/darjss/herdr-orchestrate)<br><sub>darjss</sub> | Pi-native orchestration for visible Herdr worker sessions — a run board, durable prompts/reports/state, isolated git worktrees, and explicit model routing. | `pi-package` `typescript` | 2 | 2026-07-13 |
| [**herdr-shame-report**](https://github.com/JYasha11/herdr-shame-report)<br><sub>JYasha11</sub> | Keeps a permanent ledger of how long you've left your AI agents waiting. The sheep remember. | `javascript` | 2 | 2026-07-10 |
| [**herdr-wakeup**](https://github.com/usrivastava92/herdr-wakeup)<br><sub>usrivastava92</sub> | Herdr plugin that keeps macOS or Linux awake while Herdr-managed agents are working | `power-management` `sleep-prevention` `wakeup` `rust` | 2 | 2026-07-17 |
| [**herdr-agent-timer**](https://github.com/Yemeni/herdr-agent-timer)<br><sub>Yemeni</sub> | A Herdr plugin that alternates each agent's status label with its elapsed time | `shell` | 2 | 🆕 2026-07-29 |
| [**herdr-pi-reloader**](https://github.com/anrunt/herdr-pi-reloader)<br><sub>anrunt</sub> | Reload or restart idle Pi agent sessions from a Herdr overlay TUI. | `rust` | 1 | 🆕 2026-07-18 |
| [**herdr-pane-topic-sync**](https://github.com/danbuhler/herdr-pane-topic-sync)<br><sub>danbuhler</sub> | herdr plugin: auto-name panes & tabs after each agent's live topic (Claude Code, Codex, …) instead of 1, 2, 3. | `ai-agents` `claude-code` `terminal` `tmux-alternative` `javascript` | 1 | 2026-07-17 |
| [**herdr-amphetamine-macos**](https://github.com/gw31415/herdr-amphetamine-macos)<br><sub>gw31415</sub> | herdr plugin that tops up Amphetamine while agents work | `python` | 1 | 2026-07-09 |
| [**herdr-newtab-plus**](https://github.com/jeffarese/herdr-newtab-plus)<br><sub>jeffarese</sub> | A Herdr new tab that asks which folder and which agent: completes real paths, remembers where you work, and starts an agent for you. | `python` | 1 | 🆕 2026-07-26 |
| [**herdr-agents-status**](https://github.com/maedana/herdr-agents-status)<br><sub>maedana</sub> | Always-on-top transparent overlay showing Herdr agent status — a spiritual successor to claudeye, built for Herdr instead of tmux. | `rust` | 1 | 🆕 2026-07-22 |
| [**herdr-imebox**](https://github.com/Sawakee/herdr-imebox)<br><sub>Sawakee</sub> | IME-friendly pop-up text box for typing Japanese/CJK into AI agent panes in herdr | `cjk` `ime` `input-method` `japanese` `ratatui` | 1 | 2026-07-17 |
| [**herdr-agents-history**](https://github.com/speardragon/herdr-agents-history)<br><sub>speardragon</sub> | See what your AI coding agents are actually doing — a live, keyboard-driven herdr TUI streaming every tool call across all your agents (Claude Code & Codex). | `ai-agents` `claude-code` `codex` `tui` `typescript` | 1 | 🆕 2026-07-19 |
| [**herdr-conductor**](https://github.com/StructuPath/herdr-conductor)<br><sub>StructuPath</sub> | Orchestrate a feature-delivery team as visible Herdr agent panes — the Conductor plugin | `orchestration` `javascript` | 1 | 🆕 2026-07-31 |
| [**herdr-agent-office**](https://github.com/suisya-systems/herdr-agent-office)<br><sub>suisya-systems</sub> | Your agent fleet as a pixel-art office - a herdr plugin. See who's working, who's stuck, and jump to them. | `python` | 1 | 🆕 2026-07-25 |
| [**tinysend-herdr**](https://github.com/tiny-send/tinysend-herdr)<br><sub>tiny-send</sub> | herdr plugin: email yourself when an agent blocks/finishes, reply to unblock it. Powered by tinysend. | `ai-agents` `tinysend` `javascript` | 1 | 2026-06-26 |
| [**herdr-rovo-dev**](https://github.com/usrivastava92/herdr-rovo-dev)<br><sub>usrivastava92</sub> | Herdr plugin that detects Rovo Dev CLI sessions and reports them as live agents in Herdr | `ai-agent` `rovo` `rovo-dev` `shell` | 1 | 🆕 2026-07-19 |
| [**herdr-nudge**](https://github.com/EricBois/herdr-nudge)<br><sub>EricBois</sub> | Arm a continue-nudge on a herdr agent — fire at a set time, or when it goes idle/blocked | `shell` | 0 | 2026-07-17 |
| [**herdr-ai-memory**](https://github.com/iagogfe/herdr-ai-memory)<br><sub>iagogfe</sub> | Herdr plugin: launch coding agents through ai-memory managed workstreams - cross-agent session continuity | `ai-agents` `ai-memory` `terminal` `javascript` | 0 | 🆕 2026-07-24 |
| [**herdr-annotations**](https://github.com/IgorWarzocha/herdr-annotations)<br><sub>IgorWarzocha</sub> | Collect annotations on terminal selections and stage them into Herdr agents | `ai-agents` `annotations` `terminal` `javascript` | 0 | 🆕 2026-07-18 |
| [**herdr-watcher**](https://github.com/joshka0/herdr-watcher)<br><sub>joshka0</sub> | Durable continuations and detached worker callbacks for Herdr agents | `rust` | 0 | 🆕 2026-08-02 |
| [**herdr-orchestrator**](https://github.com/kylezk777/herdr-orchestrator)<br><sub>kylezk777</sub> | Herdr-orch is a file-based agent orchestration tool that runs on top of Herdr. | `agent-orchestration` `orchestrator` `rust` | 0 | 🆕 2026-07-26 |
| [**herdr-claude-launcher**](https://github.com/lucasleon2107/herdr-claude-launcher)<br><sub>lucasleon2107</sub> | herdr plugin: open a new tab with Claude Code already running | `ai-agents` `claude-code` `terminal` `tmux` `shell` | 0 | 🆕 2026-07-31 |
| [**sheprd**](https://github.com/m-mohamed/sheprd)<br><sub>m-mohamed</sub> | Keep Pi, Codex, Claude Code, and OpenCode in one visible, isolated Herdr Flok. | `agent-tools` `claude-code` `cli` `codex` `coding-agents` | 0 | 🆕 2026-07-31 |
| [**herdr-alias-setter**](https://github.com/m2selfA/herdr-alias-setter)<br><sub>m2selfA</sub> | Herdr plugin: set pane name + agent alias (quick type-in or full menu) | `powershell` | 0 | 🆕 2026-07-28 |
| [**herdr-agents-bridge**](https://github.com/maedana/herdr-agents-bridge)<br><sub>maedana</sub> | Monitor and interact with your coding agents from your phone via a local mobile-friendly web UI — connect by scanning a QR code. | `rust` | 0 | 🆕 2026-07-22 |
| [**herdr-agent-dash**](https://github.com/MartinBspheroid/herdr-agent-dash)<br><sub>MartinBspheroid</sub> | Herdr Agent Board: a local, keyboard-first plugin for scanning active coding agents, their state, working directory, and Git context at a glance. | `typescript` | 0 | 🆕 2026-07-21 |
| [**herdr-green**](https://github.com/natori-hrj/herdr-green)<br><sub>natori-hrj</sub> | Per-agent test status for herdr — run a project's tests when its agent finishes and show pass/fail. | `ai-agents` `ci` `tests` `rust` | 0 | 🆕 2026-07-23 |
| [**herdr-standup**](https://github.com/natori-hrj/herdr-standup)<br><sub>natori-hrj</sub> | Agent standup for herdr — a per-agent digest of commits and uncommitted work across your agents' repos. | `ai-agents` `git` `standup` `rust` | 0 | 🆕 2026-07-23 |
| [**herdr-plugin-aos**](https://github.com/noctaIO/herdr-plugin-aos)<br><sub>noctaIO</sub> | Spawn Agentic OS-enabled Claude Code agents in a herdr pane from any workspace. Non-invasive herdr plugin. | `shell` | 0 | 2026-07-11 |
| [**herdr-caffeinate**](https://github.com/nwarwick/herdr-caffeinate)<br><sub>nwarwick</sub> | Prevent macOS system sleep while Herdr agents are working | `caffeinate` `coding-agents` `macos` `shell` | 0 | 🆕 2026-07-29 |
| [**ocean-herdr**](https://github.com/Risingtides-dev/ocean-herdr)<br><sub>Risingtides-dev</sub> | Ocean agent integration for Herdr | `coding-agent` `ocean` `rust` | 0 | 2026-07-17 |
| [**herdr-want-to-sleep**](https://github.com/scheron/herdr-want-to-sleep)<br><sub>scheron</sub> | A herdr plugin that puts your Mac to sleep once no coding agent is working any more. Arm it before bed and it waits for every agent to settle, then journals wh… | `coding-agents` `macos` `shell` | 0 | 🆕 2026-07-28 |
| [**herdr-achievements**](https://github.com/SerHappy/herdr-achievements)<br><sub>SerHappy</sub> | Achievements and tiny celebrations for your Herdr AI agent herd | `achievements` `ai-agents` `developer-tools` `gamification` `go` | 0 | 🆕 2026-07-30 |
| [**herdr-ask**](https://github.com/TaylorFinklea/herdr-ask)<br><sub>TaylorFinklea</sub> | Lightweight command generation and terminal chat for Herdr and any terminal | `cli` `rust` `terminal` `tui` | 0 | 🆕 2026-07-21 |
| [**herdr-cline-plugin**](https://github.com/TheMetalStorm/herdr-cline-plugin)<br><sub>TheMetalStorm</sub> | Herdr plugin that makes a plain Cline CLI launched from any pane look like a native Herdr agent. | `cli` `cline` `herdr-integration` `shell` | 0 | 🆕 2026-07-31 |

<details><summary>Also relevant to this purpose</summary>

- [a2u/herdr-jira](https://github.com/a2u/herdr-jira) — Jira TUI plugin for herdr — browse issues with configurable JQL filters, search, change statuses, and delegat…
- [steig/worktender](https://github.com/steig/worktender) — Drive git worktrees as herdr workspaces: list, adopt, staff and tear down worktrees with their workspace and…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-worktree"></a>

## Git Worktrees & Branches

> I want to spin up a worktree for each piece of work, and have the cleanup handled automatically too

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-worktrunk**](https://github.com/devashish2203/herdr-worktrunk)<br><sub>devashish2203</sub> | Herdr Plugin to integrate worktrunk for git worktree management | `shell` | 74 | 🆕 2026-07-24 |
| [**herdr-plugin-jj-workspace**](https://github.com/NathanFlurry/herdr-plugin-jj-workspace)<br><sub>NathanFlurry</sub> | Create and remove Jujutsu (jj) workspaces as Herdr workspaces | `jujutsu` `rust` | 37 | 2026-07-08 |
| [**herdr-worktree-from-pr**](https://github.com/tdi/herdr-worktree-from-pr)<br><sub>tdi</sub> | Create a git worktree from a GitHub PR and open it as a herdr workspace | `javascript` | 6 | 🆕 2026-07-20 |
| [**herdr-plugin-renamer**](https://github.com/wyattjoh/herdr-plugin-renamer)<br><sub>wyattjoh</sub> | Renames an auto-generated herdr worktree branch and workspace from the agent's first prompt, via on-device Apple FoundationModels or Codex. | `rust` | 6 | 🆕 2026-07-29 |
| [**jj-waltz**](https://github.com/EzraCerpac/jj-waltz)<br><sub>EzraCerpac</sub> | A Jujutsu workspace switcher inspired by Worktrunk | `cli` `jj` `jujitsu` `utility` `workspace` | 4 | 🆕 2026-07-28 |
| [**herdr-symlink-worktree**](https://github.com/hmu332233/herdr-symlink-worktree)<br><sub>hmu332233</sub> | A herdr plugin that symlinks shared local files from your main repo into new worktrees. | `shell` | 4 | 2026-07-16 |
| [**herdr-fresh-worktree**](https://github.com/persiyanov/herdr-fresh-worktree)<br><sub>persiyanov</sub> | Reset a newly created herdr worktree to the latest origin default branch. | `javascript` | 4 | 2026-06-25 |
| [**herdr-worktreeinclude**](https://github.com/tanshio/herdr-worktreeinclude)<br><sub>tanshio</sub> | Herdr plugin: copy gitignored files matching .worktreeinclude into newly created worktrees | `worktree` `worktreeiclude` `shell` | 4 | 2026-07-11 |
| [**herdr-plugin-git-worktree-hooks**](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks)<br><sub>freethinkel</sub> | Run shell commands when a git worktree is created/removed — one YAML config for all projects, living outside any repo. | `git-worktree` `javascript` | 3 | 2026-07-06 |
| [**herdr-worktree-seed**](https://github.com/jlimas/herdr-worktree-seed)<br><sub>jlimas</sub> | Herdr plugin that seeds new worktrees with copy-on-write node_modules and configurable local dotfiles | `developer-tools` `dotfiles` `git-worktree` `nodejs` `typescript` | 3 | 🆕 2026-07-28 |
| [**herdr-branch-cleanup**](https://github.com/osolmaz/herdr-branch-cleanup)<br><sub>osolmaz</sub> | Checkout the default branch when a pane's branch is merged or deleted on GitHub | `git` `github` `rust` | 3 | 🆕 2026-07-26 |
| [**herdr-worktree-lifecycle**](https://github.com/qdentity/herdr-worktree-lifecycle)<br><sub>qdentity</sub> | Herdr plugin: dispatch worktree lifecycle events to repo-owned setup/teardown wrappers | `rust` | 3 | 2026-06-29 |
| [**herdr-worktree-hooks**](https://github.com/timofey-TK/herdr-worktree-hooks)<br><sub>timofey-TK</sub> | herdr plugin: run custom setup/teardown commands when a git worktree is created, opened, or removed | `developer-tools` `git-worktree` `worktree` `python` | 3 | 2026-07-17 |
| [**herdr-remote-worktrunk**](https://github.com/ditwrd/herdr-remote-worktrunk)<br><sub>ditwrd</sub> | Herdr remote worktrunk workspace | `shell` | 2 | 2026-07-10 |
| [**herdr-worktreeinclude**](https://github.com/serhii-chernenko/herdr-worktreeinclude)<br><sub>serhii-chernenko</sub> | Allow custom path for new worktrees and respects `.worktreeinclude` file like Claude CLI does | `worktree` `shell` | 2 | 🆕 2026-07-23 |
| [**herdr-worktree-copy**](https://github.com/crexi/herdr-worktree-copy)<br><sub>crexi</sub> | Herdr plugin that copies and symlinks worktree-local files from a .worktree-copy manifest | `git-worktree` `shell` | 1 | 🆕 2026-07-28 |
| [**herdr-allow**](https://github.com/Feasy01/herdr-allow)<br><sub>Feasy01</sub> | herdr plugin: copy gitignored files (.env, secrets, local configs) into every new worktree via a .herdr-allow allowlist | `shell` | 1 | 2026-07-02 |
| [**herdr-plugin-gwm**](https://github.com/kbrdn1/herdr-plugin-gwm)<br><sub>kbrdn1</sub> | herdr plugin that drives gwm for git worktree management — gwm stays the source of truth, herdr adopts. | `bash` `cli` `git-worktree` `gwm` `worktree` | 1 | 🆕 2026-07-27 |
| [**worktender**](https://github.com/steig/worktender)<br><sub>steig</sub> | Drive git worktrees as herdr workspaces: list, adopt, staff and tear down worktrees with their workspace and agent state in one view. | `ai-agents` `claude-code` `coding-agents` `git-worktree` `golang` | 1 | 🆕 2026-08-02 |
| [**herdr-worktree-provisioner**](https://github.com/arjenblokzijl/herdr-worktree-provisioner)<br><sub>arjenblokzijl</sub> | Runs per-repo setup in a new worktree's own visible pane — composable and guard-free. | `bootstrap` `git-worktree` `worktree` `shell` | 0 | 2026-07-08 |
| [**herdr-deck**](https://github.com/ctbaum/herdr-deck)<br><sub>ctbaum</sub> | The companion workspace launcher for herdr-agents.nvim: open or resume Claude and Codex in a ready-made Neovim, agent, shell, and lazygit deck. | `claude-code` `codex` `coding-agents` `git-worktree` `neovim` | 0 | 🆕 2026-08-01 |
| [**trunkr**](https://github.com/disintegrator/trunkr)<br><sub>disintegrator</sub> | Herdr 🤝 Worktrunk | `go` | 0 | 🆕 2026-07-28 |
| [**herdr-worktreeinclude**](https://github.com/eightHundreds/herdr-worktreeinclude)<br><sub>eightHundreds</sub> | Herdr plugin: copy .worktreeinclude-selected gitignored files into new worktrees | `worktree` `rust` | 0 | 🆕 2026-07-28 |
| [**herdr-title**](https://github.com/filoozom/herdr-title)<br><sub>filoozom</sub> | A Herdr plugin that shows the selected worktree and agent activity in your terminal tab title. | `rust` | 0 | 🆕 2026-07-24 |
| [**gren-herdr**](https://github.com/langtind/gren-herdr)<br><sub>langtind</sub> | A herdr plugin for creating, switching, and removing git worktrees via gren — with gren's post-create setup. | `git-worktree` `gren` `shell` | 0 | 🆕 2026-07-31 |
| [**herdr-jj-status**](https://github.com/mroth/herdr-jj-status)<br><sub>mroth</sub> | herdr plugin: show the Jujutsu bookmark/status for jj workspaces in the spaces sidebar | `shell` | 0 | 🆕 2026-07-28 |
| [**herdr-plugin-worktree-bootstrap**](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap)<br><sub>zerodice0</sub> | Safely copy ignored local files and run setup commands in new Herdr Git worktrees | `python` | 0 | 🆕 2026-08-02 |

<details><summary>Also relevant to this purpose</summary>

- [tdi/herdr-worktree-from-linear](https://github.com/tdi/herdr-worktree-from-linear) — Create a git worktree from a Linear issue and open it as a herdr workspace
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — Automatically bootstrap Herdr worktrees for JavaScript and TypeScript with lockfile-aware installs and safe e…
- [tomasvarga/herdr-e2b](https://github.com/tomasvarga/herdr-e2b) — Mirror a git worktree into a fresh E2B cloud sandbox on demand — a snapshot upload (uncommitted changes and a…
- [snics/herdr-worktree-from-gitlab](https://github.com/snics/herdr-worktree-from-gitlab) — herdr plugin: create a git worktree + workspace from a GitLab issue (via glab)
- [untalfranfernandez/herdr-worktreeinclude](https://github.com/untalfranfernandez/herdr-worktreeinclude) — Herdr plugin that populates every new git worktree with the gitignored local files it needs — .env, settings.…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-review"></a>

## Code Review & Diffs

> I want to read the diff an agent wrote and send comments back on it

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**crabbox**](https://github.com/openclaw/crabbox)<br><sub>openclaw</sub> | Crabbox: warm a box, sync the diff, run the suite. | `agent-skills` `remote-test-runner` `go` | 1247 | 🆕 2026-08-02 |
| [**herdr-reviewr**](https://github.com/persiyanov/herdr-reviewr)<br><sub>persiyanov</sub> | A code-review + file-viewer sidebar for herdr — comment on an agent's diff, send it back. Plus a read-only view of the PR, its checks, and comments. | `code-review` `rust` `tui` | 307 | 🆕 2026-08-01 |
| [**herdr-pickr**](https://github.com/tomasvarga/herdr-pickr)<br><sub>tomasvarga</sub> | A PR review router for herdr — Ctrl+click a GitHub PR / GitLab MR link and pick a reviewer (tuicr · hunk · diff · browser · or your own tool), with an optional… | `cli` `code-review` `pull-request` `tui` `shell` | 11 | 2026-07-13 |
| [**herdr-plugin-hunk**](https://github.com/edmundmiller/herdr-plugin-hunk)<br><sub>edmundmiller</sub> | Herdr plugin for opening Hunk diffs in split panes or tabs | `python` | 10 | 2026-06-23 |
| [**herdr-plannotator**](https://github.com/plannotator/herdr-plannotator)<br><sub>plannotator</sub> | Open Plannotator reviews inside Herdr Browser panes. | `plannotator` `typescript` | 8 | 🆕 2026-07-29 |
| [**herdr-plugin-hunk-autodiff**](https://github.com/scott306lr/herdr-plugin-hunk-autodiff)<br><sub>scott306lr</sub> | Herdr plugin: auto-open a hunk diff split when a coding agent finishes with uncommitted changes | `claude-code` `hunk` `python` | 4 | 2026-07-05 |
| [**herdr-extensions**](https://github.com/vonzelle-vzt/herdr-extensions)<br><sub>vonzelle-vzt</sub> | Tiny VS Code for herdr: a real editor with LSP diagnostics, autocomplete, rename and go-to-definition — plus source control, search, problems, tests, a debugge… | `agent-tools` `autocomplete` `claude-code` `cli` `code-review` | 2 | 🆕 2026-08-01 |
| [**herdr-hunk**](https://github.com/yuucu/herdr-hunk)<br><sub>yuucu</sub> | herdr plugin: toggle Hunk diff reviews for your agent workspaces | `diff` `hunk` `go` | 2 | 🆕 2026-07-20 |
| [**herdr-strays**](https://github.com/aleslanger/herdr-strays)<br><sub>aleslanger</sub> | Terminal UI for herding stray git worktrees — browse projects, see changed files live, read diffs, and prompt Claude without leaving the panel. | `rust` | 1 | 🆕 2026-07-31 |
| [**herdr-peer-review**](https://github.com/Elio2000/herdr-peer-review)<br><sub>Elio2000</sub> | Open a second coding agent in a herdr pane and have it review your diff — watchable, auto-approve, read-only. Ships a Claude Code skill for the autonomous revi… | `agent-skills` `ai-agents` `claude-code` `code-review` `codex` | 1 | 2026-07-16 |
| [**herdr-git-graph**](https://github.com/jorge-huxley/herdr-git-graph)<br><sub>jorge-huxley</sub> | Read-only git graph TUI plugin for Herdr with colored ASCII lanes, branch filter, search, and on-demand diffs. | `rust` | 1 | 2026-07-17 |
| [**herdr-review**](https://github.com/quantk/herdr-review)<br><sub>quantk</sub> | Review agent-authored changes in Hunk and send inline feedback back through Herdr | `code-review` `hunk` `javascript` | 1 | 🆕 2026-07-28 |
| [**herdr-hunk-gh-diff**](https://github.com/Allianaab2m/herdr-hunk-gh-diff)<br><sub>Allianaab2m</sub> | Herdr plugin: open a Hunk diff between the branch checked out in the current pane and the target branch of its GitHub pull request. | `python` | 0 | 2026-07-15 |
| [**herdr-agent-diff**](https://github.com/baotran01/herdr-agent-diff)<br><sub>baotran01</sub> | Herdr plugin for inspecting agent filesystem and Git diffs | `rust` | 0 | 🆕 2026-08-01 |
| [**herdr-stagr**](https://github.com/brianh20/herdr-stagr)<br><sub>brianh20</sub> | Source Control sidebar for herdr: stage, unstage, and discard with side-by-side diffs | `git` `tui` `rust` | 0 | 🆕 2026-07-30 |
| [**herdr-hunk**](https://github.com/cevr/herdr-hunk)<br><sub>cevr</sub> | Send Hunk review notes to the correct Herdr agent pane | `effect-ts` `hunk` `typescript` | 0 | 🆕 2026-07-28 |
| [**herdr-gitview**](https://github.com/ChmaraX/herdr-gitview)<br><sub>ChmaraX</sub> | Git status/diff panel for herdr - review changes, edit in nvim, stage/commit/discard, all from the terminal | `git` `git-diff` `git-tui` `neovim` `rust` | 0 | 🆕 2026-08-01 |
| [**herdr-plan-code-review**](https://github.com/inxx/herdr-plan-code-review)<br><sub>inxx</sub> | herdr plugin: Opus plans, Sonnet codes, Claude+Codex review — one action opens the four agent panes | `claude-code` `codex` `terminal` `shell` | 0 | 2026-07-06 |
| [**herdr-scribe**](https://github.com/Javamomma/herdr-scribe)<br><sub>Javamomma</sub> | herdr plugin: live no-recording meeting transcription — mic → RAM-only transcript + live analyst panes; on stop: meeting note, optional policy gate, reviewable… | `python` | 0 | 🆕 2026-07-31 |
| [**herdr-idle-panes**](https://github.com/leonho/herdr-idle-panes)<br><sub>leonho</sub> | herdr plugin: popup checklist to review and close panes sitting at an idle shell | `python` | 0 | 2026-07-18 |
| [**herdr-roborev**](https://github.com/phin-tech/herdr-roborev)<br><sub>phin-tech</sub> | Open roborev's review TUI in a Herdr pane | `shell` | 0 | 🆕 2026-07-21 |
| [**herdr-comments**](https://github.com/shadowfax92/herdr-comments)<br><sub>shadowfax92</sub> | Annotate copied Herdr terminal output, collect per-pane comments, and review them in Neovim. | `ai-agents` `annotations` `neovim` `rust` `terminal` | 0 | 🆕 2026-08-01 |

<details><summary>Also relevant to this purpose</summary>

- [JacquesvanWyk/herdr-hunk](https://github.com/JacquesvanWyk/herdr-hunk) — Interactive fzf picker for hunk diffs in herdr: commits, ranges, stashes, plus auto-open when an agent finish…
- [tomasvarga/herdr-sniffr](https://github.com/tomasvarga/herdr-sniffr) — An AI sniffs your PR for issues before you review — an agentic first-pass that drops draft comments into tuic…
- [krzysztoff1/herdr-cull](https://github.com/krzysztoff1/herdr-cull) — Review and close idle agent panes in herdr — fzf multi-select, nothing closes without confirmation.

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-forge"></a>

## GitHub & Issue Trackers

> I want to kick off work from an issue or PR, and track PR status

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**ghzinga**](https://github.com/osolmaz/ghzinga)<br><sub>osolmaz</sub> | Easy, clickable TUI to view a single GitHub issue or PR, in Rust | `rust` | 68 | 🆕 2026-07-26 |
| [**herdr-plugin-github-start**](https://github.com/ogulcancelik/herdr-plugin-github-start)<br><sub>ogulcancelik</sub> | Herdr plugin that starts Codex or Claude from a GitHub issue, PR, or discussion | `javascript` | 15 | 2026-06-30 |
| [**herdr-plugin-gh-pr**](https://github.com/wyattjoh/herdr-plugin-gh-pr)<br><sub>wyattjoh</sub> | herdr plugin that shows the focused agent pane's branch GitHub PR status in the sidebar | `typescript` | 14 | 2026-07-16 |
| [**herdr-worktree-from-linear**](https://github.com/tdi/herdr-worktree-from-linear)<br><sub>tdi</sub> | Create a git worktree from a Linear issue and open it as a herdr workspace | `javascript` | 11 | 🆕 2026-07-22 |
| [**herdr-pr-tracker**](https://github.com/Matovidlo/herdr-pr-tracker)<br><sub>Matovidlo</sub> | herdr plugin: track the GitHub PR each Claude Code session produces, with gh state + actions | `claude-code` `shell` | 10 | 🆕 2026-07-21 |
| [**herdr-jira**](https://github.com/a2u/herdr-jira)<br><sub>a2u</sub> | Jira TUI plugin for herdr — browse issues with configurable JQL filters, search, change statuses, and delegate issues to AI agents running in your terminal wit… | `ai-agents` `jira` `ratatui` `rust` `tui` | 7 | 🆕 2026-07-18 |
| [**herdr-linear**](https://github.com/JacquesvanWyk/herdr-linear)<br><sub>JacquesvanWyk</sub> | fzf-driven Linear panel in a herdr split pane or tab: search issues, drill into projects, create issues, change status | `shell` | 6 | 2026-07-12 |
| [**herdr-plugin-github-dash**](https://github.com/kukv/herdr-plugin-github-dash)<br><sub>kukv</sub> | Herdr plugin for browsing and managing GitHub pull requests and issues | `cli` `github` `go` | 4 | 🆕 2026-07-31 |
| [**herdr-plugin-gh-workflow**](https://github.com/kkckkc/herdr-plugin-gh-workflow)<br><sub>kkckkc</sub> | Herdr plugin for GitHub workflow | `javascript` | 3 | 2026-07-03 |
| [**herdr-git-status**](https://github.com/krystof018/herdr-git-status)<br><sub>krystof018</sub> | Surfaces CI status inside herdr for both GitLab (pipelines + merge requests) and GitHub (Actions + pull requests), auto-detected from the repo's origin. | `bash` `ci-cd` `ci-status` `developer-tools` `github-actions` | 3 | 2026-07-01 |
| [**mergr**](https://github.com/jsmenzies/mergr)<br><sub>jsmenzies</sub> | GitHub pull request status for Herdr Space sidebar rows. | `github-pull-requests` `rust` | 2 | 🆕 2026-07-30 |
| [**herdr-dashboard**](https://github.com/chouxcreams/herdr-dashboard)<br><sub>chouxcreams</sub> | PR status dashboard TUI for herdr workspaces — PR state / CI / reviews per pane at a glance | `dashboard` `github` `pull-requests` `ratatui` `rust` | 1 | 🆕 2026-07-28 |
| [**herdr-plugin-dotfiles-github-link-preview**](https://github.com/edmundmiller/herdr-plugin-dotfiles-github-link-preview)<br><sub>edmundmiller</sub> | Herdr plugin for previewing GitHub issues and pull requests in a side pane | `python` | 1 | 2026-06-23 |
| [**herdr-sniffr**](https://github.com/tomasvarga/herdr-sniffr)<br><sub>tomasvarga</sub> | An AI sniffs your PR for issues before you review — an agentic first-pass that drops draft comments into tuicr. Agent-agnostic (codex/claude/cursor/grok/…). | `ai` `cli` `code-review` `pull-request` `tuicr` | 1 | 2026-07-14 |
| [**herdr-browser**](https://github.com/Epsomsaltskerosinelamp950/herdr-browser)<br><sub>Epsomsaltskerosinelamp950</sub> | Render a live, interactive Chromium view within Herdr panes for real-time automation monitoring and control using Chrome DevTools Protocol. | `codex` `coding-agents` `developer-tools` `diff` `file-viewer` | 0 | 🆕 2026-07-30 |
| [**herdr-spaces-pr-status**](https://github.com/jmarbutt/herdr-spaces-pr-status)<br><sub>jmarbutt</sub> | Show GitHub pull request status on herdr spaces, with a Conductor-style PR board | `github-pull-request` `javascript` | 0 | 🆕 2026-08-01 |
| [**herdr-pr-preview**](https://github.com/juninaba/herdr-pr-preview)<br><sub>juninaba</sub> | A Herdr plugin for previewing the current branch's GitHub pull request in a split pane. | `shell` | 0 | 2026-07-08 |
| [**github-issue-herdr-plugin**](https://github.com/nyanyaon/github-issue-herdr-plugin)<br><sub>nyanyaon</sub> | Claude Code plugin for herding GitHub issues | `rust` | 0 | 🆕 2026-07-27 |
| [**herdr-worktree-from-gitlab**](https://github.com/snics/herdr-worktree-from-gitlab)<br><sub>snics</sub> | herdr plugin: create a git worktree + workspace from a GitLab issue (via glab) | `gitlab` `rust` `worktree` | 0 | 2026-07-09 |

<details><summary>Also relevant to this purpose</summary>

- [tomasvarga/herdr-pickr](https://github.com/tomasvarga/herdr-pickr) — A PR review router for herdr — Ctrl+click a GitHub PR / GitLab MR link and pick a reviewer (tuicr · hunk · di…
- [tdi/herdr-worktree-from-pr](https://github.com/tdi/herdr-worktree-from-pr) — Create a git worktree from a GitHub PR and open it as a herdr workspace

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-layout"></a>

## Workspaces & Layouts

> When I open a project, I want tabs, panes, and startup commands all set up in one shot

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-spreader**](https://github.com/yuk1ty/herdr-spreader)<br><sub>yuk1ty</sub> | Spin up your whole herdr workspace layout — tabs, panes, commands, and all — from a single YAML file. | `rust` | 59 | 2026-07-16 |
| [**dotfiles**](https://github.com/lararosekelley/dotfiles)<br><sub>lararosekelley</sub> | My dotfiles, meant for use with a Bash shell | `bash` `bootstrap` `dotfiles` `homebrew` `macos` | 49 | 🆕 2026-08-02 |
| [**herdr-plugin-workspace-manager**](https://github.com/razajamil/herdr-plugin-workspace-manager)<br><sub>razajamil</sub> | Declarative tab/pane layouts with per-workspace defaults applied automatically when a worktree is created. | `rust` | 24 | 🆕 2026-07-25 |
| [**seshagy**](https://github.com/lmilojevicc/seshagy)<br><sub>lmilojevicc</sub> | Agent-aware session manager for tmux & herdr — discover projects, launch sessions, and track your AI agents work. | `bubbletea` `go` `session-management` `session-manager` `terminal` | 8 | 🆕 2026-07-31 |
| [**herdr-muster**](https://github.com/marcoskichel/herdr-muster)<br><sub>marcoskichel</sub> | Agent-aware project switcher for herdr | `rust` | 4 | 2026-07-03 |
| [**herdr-setup-bootstrap**](https://github.com/shizlie/herdr-setup-bootstrap)<br><sub>shizlie</sub> | Herdr plugin to bootstrap new worktrees from worktree_init.toml | `shell` | 3 | 2026-06-17 |
| [**herdr-clone-layout**](https://github.com/danilolucasmd/herdr-clone-layout)<br><sub>danilolucasmd</sub> | Clone your workspace layout onto every new herdr worktree. No templates, no config — the layout you're in is the template. | `shell` | 2 | 🆕 2026-08-01 |
| [**herdr-warp**](https://github.com/HexSleeves/herdr-warp)<br><sub>HexSleeves</sub> | Open a Herdr workspace as native Warp panes | `shell` | 2 | 🆕 2026-07-25 |
| [**herdr-pane-layouts**](https://github.com/iurysza/herdr-pane-layouts)<br><sub>iurysza</sub> | Seamless tmux-style pane resizing and layouts for Herdr | `pane-layout` `python` `terminal` | 2 | 2026-07-17 |
| [**herdr-layout-tools**](https://github.com/edouard-andrei/herdr-layout-tools)<br><sub>edouard-andrei</sub> | herdr plugin: in-place reshape (main-left + grid) and equalize — same tab id, same pane ids, processes preserved | `javascript` | 1 | 2026-07-08 |
| [**herdr-compose**](https://github.com/ropali/herdr-compose)<br><sub>ropali</sub> | herdr-compose is a declarative workspace layout manager for Herdr | `layout-manager` `python` | 1 | 🆕 2026-07-25 |
| [**herdr-google-calendar**](https://github.com/Tomatio13/herdr-google-calendar)<br><sub>Tomatio13</sub> | herdr-gog-calendar is a Google Calendar integration plugin for herdr, a terminal workspace tool. | `shell` | 1 | 🆕 2026-07-22 |
| [**herdr-google-gmail**](https://github.com/Tomatio13/herdr-google-gmail)<br><sub>Tomatio13</sub> | herdr-google-gmail is a Gmail integration plugin for herdr, a terminal workspace tool. | `shell` | 1 | 🆕 2026-07-22 |
| [**herdr-layout**](https://github.com/3mmdrew/herdr-layout)<br><sub>3mmdrew</sub> | Minimalist workspace layouts for herdr. Lua file in -> workspace out. No deps, no daemon, no YAML. | `lua` `terminal` | 0 | 🆕 2026-08-01 |
| [**ccc-herdr-layout**](https://github.com/caoer/ccc-herdr-layout)<br><sub>caoer</sub> | Visual layout picker plugin for herdr — one key, live preview | `go` | 0 | 🆕 2026-08-01 |
| [**herdr-plugin-dotfiles-dev-layout**](https://github.com/edmundmiller/herdr-plugin-dotfiles-dev-layout)<br><sub>edmundmiller</sub> | Herdr plugin for opening my dotfiles dev workspace layout | `python` | 0 | 2026-06-23 |
| [**herdr-gateway**](https://github.com/osuki-dev/herdr-gateway)<br><sub>osuki-dev</sub> | Herdr Gateway exposes a small HTTP API for reading Herdr workspaces, tabs, panes, agents, pane output, and sending pane input. It talks to the local Herdr sock… | `rust` | 0 | 🆕 2026-07-29 |
| [**herdr-lastfocus**](https://github.com/pedrobarco/herdr-lastfocus)<br><sub>pedrobarco</sub> | tmux-style last-active pane/tab/workspace toggles for herdr, via a focus-event history daemon | `terminal-multiplexer` `tmux` `go` | 0 | 🆕 2026-07-25 |
| [**herdr-active-agent-jump**](https://github.com/shoaibkhanz/herdr-active-agent-jump)<br><sub>shoaibkhanz</sub> | herdr plugin: cycle focus forward/backward through in-flight (working/blocked) agents in layout order — the vim-motion complement to attention-jump | `javascript` | 0 | 2026-07-12 |
| [**herdr-dev-layout**](https://github.com/simoncrypta/herdr-dev-layout)<br><sub>simoncrypta</sub> | Sticky agent pane for Herdr | `herdr-integration` `shell` | 0 | 🆕 2026-07-28 |
| [**reasonix-herdr**](https://github.com/uuie/reasonix-herdr)<br><sub>uuie</sub> | Native Reasonix plugin with live lifecycle reporting and workspace control inside Herdr. | `reasonix` `python` | 0 | 2026-07-10 |

<details><summary>Also relevant to this purpose</summary>

- [andrewchng/herdr-sessionizer](https://github.com/andrewchng/herdr-sessionizer) — Fuzzy-open projects and worktrees, then bootstrap workspaces from declarative TOML layouts — tabs, pane split…
- [fullerzz/herdr-plugin-sesh](https://github.com/fullerzz/herdr-plugin-sesh) — Sesh-style workspace picker TUI for Herdr. Integrates with zoxide to create workspaces from commonly used dir…
- [ntindle/herdr-resurrect](https://github.com/ntindle/herdr-resurrect) — tmux-resurrect for herdr — snapshot workspaces, tabs, panes, cwd, running programs and agents, and restore th…
- [salkhalil/herdr-sessionizer](https://github.com/salkhalil/herdr-sessionizer) — tmux-sessionizer for herdr: fzf over open workspaces and zoxide directories, create-or-focus with template ta…
- [aliou/herdr-cast](https://github.com/aliou/herdr-cast) — Personal Herdr plugin for native macOS agent notifications, fuzzy workspace navigation, zoxide-backed workspa…
- [asermax/herdr-suspend-workspace](https://github.com/asermax/herdr-suspend-workspace) — Suspend a herdr workspace (snapshot layout + agents, close it, restore later from a popup picker)
- [willfish/herdr-workspacex](https://github.com/willfish/herdr-workspacex) — Rust-native fuzzy Herdr workspace switcher with zoxide-backed workspace creation

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-navigate"></a>

## Pane Navigation & Keys

> I want to move and resize between panes and workspaces using the same keys as my editor

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**vim-herdr-navigation**](https://github.com/paulbkim-dev/vim-herdr-navigation)<br><sub>paulbkim-dev</sub> | Seamless Ctrl+h/j/k/l navigation across herdr panes and Vim/Neovim splits — vim-tmux-navigator ported to herdr | `neovim` `vim` `shell` | 65 | 🆕 2026-08-02 |
| [**herdr-splits.nvim**](https://github.com/lmilojevicc/herdr-splits.nvim)<br><sub>lmilojevicc</sub> | Smart splits navigation and resizing for Herdr and Neovim | `lua` `neovim` `neovim-plugin` `neovim-plugins` `nvim` | 36 | 🆕 2026-08-02 |
| [**herdr-floax**](https://github.com/Tyru5/herdr-floax)<br><sub>Tyru5</sub> | Floating scratch shell for herdr — a tmux-floax style toggleable popup, one per workspace, with persistent sessions | `rust` `terminal` `tmux-floax` | 17 | 🆕 2026-07-26 |
| [**herdr-last-workspace**](https://github.com/third774/herdr-last-workspace)<br><sub>third774</sub> | Plugin for swapping to the last workspace you had focused | `rust` | 14 | 2026-06-22 |
| [**herdr-pane-mover**](https://github.com/osamahbeig/herdr-pane-mover)<br><sub>osamahbeig</sub> | Clickable overlay menu for herdr: move, re-split, or swap panes across tabs and workspaces | `terminal` `tui` `javascript` | 7 | 2026-07-10 |
| [**herdr-recent-navigator**](https://github.com/beyondlex/herdr-recent-navigator)<br><sub>beyondlex</sub> | A recent workspaces/tabs/panes switcher for Herdr. Opens an popup window listing recently focused workspaces, tabs, panes, and AI agents — fuzzy-searchable and… | `agent` `mru` `navigator` `pane` `popup` | 6 | 🆕 2026-07-28 |
| [**herdr-toggle-popup**](https://github.com/maro114510/herdr-toggle-popup)<br><sub>maro114510</sub> | One-keybinding overlay popup shell plugin for the Herdr terminal | `go` | 5 | 🆕 2026-07-28 |
| [**herdr-logbook**](https://github.com/Resetnak/herdr-logbook)<br><sub>Resetnak</sub> | Your terminal's working memory — offline, Markdown-first notes, decisions, and an active-task now.md for Herdr | `adr` `bubbletea` `cli` `go` `markdown` | 5 | 🆕 2026-07-31 |
| [**herdr-command-center**](https://github.com/speardragon/herdr-command-center)<br><sub>speardragon</sub> | One keybinding for every command — a herdr popup that lists the commands you registered, runs them by arrow key or number, and closes itself before the command… | `command-palette` `nodejs` `terminal` `toml` `tui` | 4 | 🆕 2026-07-29 |
| [**herdr-scratch**](https://github.com/AkashJana18/herdr-scratch)<br><sub>AkashJana18</sub> | Persistent scratchpads for Herdr, paving the way for floating utility panes. | `cli` `rust` `scratchpad` | 3 | 2026-07-06 |
| [**herdr-annotations**](https://github.com/jagzmz/herdr-annotations)<br><sub>jagzmz</sub> | Annotate selected terminal text in Herdr with a fast local-first popup and reusable collections. | `annotations` `cli` `coding-agents` `developer-tools` `local-first` | 3 | 2026-07-16 |
| [**nvim-herdr-navigator**](https://github.com/kaar/nvim-herdr-navigator)<br><sub>kaar</sub> | Seamless navigation between Neovim splits and herdr panes: one set of `ctrl+h/j/k/l` chords moves through vim and herdr panes. | `neovim` `neovim-plugin` `lua` | 3 | 🆕 2026-07-29 |
| [**herdr-harpoon**](https://github.com/KonstantinKai/herdr-harpoon)<br><sub>KonstantinKai</sub> | Harpoon for herdr: mark panes and jump by index. Bash-only, zero build. | `bash` `harpoon` `tmux-harpoon` `shell` | 3 | 🆕 2026-07-29 |
| [**herdr-equalize-splits**](https://github.com/markhuot/herdr-equalize-splits)<br><sub>markhuot</sub> | herdr plugin: equalize every split in the current tab to an even share within each row/column (bind to Ctrl+b =) | `terminal` `tmux` `javascript` | 3 | 2026-07-08 |
| [**herdr-equalize-vsplit**](https://github.com/devoc09/herdr-equalize-vsplit)<br><sub>devoc09</sub> | A Herdr plugin that splits the current pane to the right and equalizes column widths. | `go` | 2 | 2026-07-15 |
| [**herdr-omnisearch**](https://github.com/dmnkf/herdr-omnisearch)<br><sub>dmnkf</sub> | Fast local search and navigation for Herdr workspaces, panes, and archived agent sessions | `python` | 2 | 🆕 2026-07-30 |
| [**herdr-convo-index**](https://github.com/dzwduan/herdr-convo-index)<br><sub>dzwduan</sub> | Turn index for Claude Code panes in herdr — jump to any past turn and read it in a popup | `python` | 2 | 🆕 2026-07-27 |
| [**herdr-unread-marker**](https://github.com/JoanGil/herdr-unread-marker)<br><sub>JoanGil</sub> | Mark/unmark the focused agent unread with a keybinding, manual only | `shell` | 2 | 2026-07-17 |
| [**herdr-float**](https://github.com/meerzulee/herdr-float)<br><sub>meerzulee</sub> | Zellij like ALT+F floating pane | `shell` | 2 | 🆕 2026-07-20 |
| [**herdr-attention**](https://github.com/milkyskies/herdr-attention)<br><sub>milkyskies</sub> | A herdr plugin: one keypress jumps focus to the next agent that needs attention (blocked, then done). | `javascript` | 2 | 2026-07-08 |
| [**herdr-navigator**](https://github.com/willfish/herdr-navigator)<br><sub>willfish</sub> | Herdr-side navigation actions for Vim/Neovim-aware pane movement | `navigation` `neovim` `rust` | 2 | 2026-07-07 |
| [**nvim-herdr-navigation**](https://github.com/bojackduy/nvim-herdr-navigation)<br><sub>bojackduy</sub> | vim-tmux-navigator style ctrl+h/j/k/l navigation between Neovim splits and Herdr panes | `keyboard-shortcuts` `lazyvim` `lua` `navigation` `neovim` | 1 | 🆕 2026-07-20 |
| [**herdr-plugin-tiles**](https://github.com/carsonjones/herdr-plugin-tiles)<br><sub>carsonjones</sub> | simple pane manager for herdr | `python` | 1 | 2026-06-19 |
| [**herdr-last-tab**](https://github.com/dantehemerson/herdr-last-tab)<br><sub>dantehemerson</sub> | Plugin for swapping to the last tab you had focused | `rust` | 1 | 🆕 2026-08-01 |
| [**herdr-easymotion**](https://github.com/elliotekj/herdr-easymotion)<br><sub>elliotekj</sub> | 🦘 Jump directly between Herdr panes | `javascript` | 1 | 🆕 2026-07-20 |
| [**herdr-break-pane**](https://github.com/iuhoay/herdr-break-pane)<br><sub>iuhoay</sub> | A small Herdr plugin that moves the focused pane into a new tab. | `pane` `javascript` | 1 | 🆕 2026-07-27 |
| [**herdr-popupx**](https://github.com/jeromychu23/herdr-popupx)<br><sub>jeromychu23</sub> | Persistent native floating scratch popups for Herdr. | `rust` `terminal` `tui` | 1 | 🆕 2026-07-21 |
| [**herdr-nav-history**](https://github.com/jugyo/herdr-nav-history)<br><sub>jugyo</sub> | Browser-style back/forward navigation over focus history (panes, tabs, workspaces) for herdr | `javascript` | 1 | 2026-07-12 |
| [**herdr-pretty-which**](https://github.com/ramarivera/herdr-pretty-which)<br><sub>ramarivera</sub> | A Rust/Ratatui which-key style keybinding overlay for Herdr. | `ratatui` `rust` `terminal` `tui` `which-key` | 1 | 🆕 2026-07-24 |
| [**herdr-nav-plus**](https://github.com/shoaibkhanz/herdr-nav-plus)<br><sub>shoaibkhanz</sub> | Ctrl+h/j/k/l navigation that flows past herdr panes into workspaces — vim-aware, wraps at both ends | `javascript` | 1 | 2026-07-18 |
| [**herdr-ask-inbox**](https://github.com/speardragon/herdr-ask-inbox)<br><sub>speardragon</sub> | Collect blocked Claude AskUserQuestion prompts from every herdr workspace into one popup, answer them in place, and never send an answer to the wrong agent. | `claude-code` `javascript` | 1 | 🆕 2026-07-25 |
| [**herdr-unread-jump**](https://github.com/to4iki/herdr-unread-jump)<br><sub>to4iki</sub> | Jump to the next Herdr agent pane that needs attention (blocked, then done). | `agents` `bash` `shell` | 1 | 🆕 2026-07-22 |
| [**herdr-nvim-nav**](https://github.com/aimdevlee/herdr-nvim-nav)<br><sub>aimdevlee</sub> | Seamless Ctrl+h/j/k/l across herdr panes and Neovim splits — socket-based, no per-keystroke process | `neovim` `c` | 0 | 🆕 2026-08-02 |
| [**herdr-voice**](https://github.com/aneym/herdr-voice)<br><sub>aneym</sub> | Voice control for herdr — speak to create spaces, split panes, and drive coding agents. OpenAI Realtime + floating HUD with live dictation and transcripts. | `openai-realtime-api` `voice` `javascript` | 0 | 🆕 2026-08-01 |
| [**gotopr**](https://github.com/asumaran/gotopr)<br><sub>asumaran</sub> | Herdr plugin: jump to your open GitHub PRs across local repos and worktrees | `go` | 0 | 🆕 2026-08-01 |
| [**herdr-auto-focus**](https://github.com/calorie/herdr-auto-focus)<br><sub>calorie</sub> | Focus Herdr agents that need attention after macOS input becomes idle. | `golang` `macos` `go` | 0 | 🆕 2026-07-27 |
| [**herdr-which-key**](https://github.com/CowboyVang/herdr-which-key)<br><sub>CowboyVang</sub> | A which-key-style keymap overlay for herdr. Press one key, see every binding under your prefix grouped and labelled, press a second key to run it. Deliberately… | `keybindings` `terminal` `which-key` `python` | 0 | 🆕 2026-07-30 |
| [**herdr-plugin-agents-usage**](https://github.com/gecm0/herdr-plugin-agents-usage)<br><sub>gecm0</sub> | Show provider usage (Claude, Codex, OpenCode Go, Neuralwatt) in a Herdr modal popup | `claude` `codex` `opencode` `terminal` `usage` | 0 | 🆕 2026-07-26 |
| [**herdr-harpoon**](https://github.com/hadeson/herdr-harpoon)<br><sub>hadeson</sub> | Harpoon-style pane marks for herdr: pin panes to slots 1-9 and jump straight to them, across tabs and workspaces. | `harpoon` `pane-navigation` `terminal` `tmux` `python` | 0 | 🆕 2026-07-25 |
| [**herdr-matter-wall**](https://github.com/Javamomma/herdr-matter-wall)<br><sub>Javamomma</sub> | herdr plugin: tile the most-active subdirectories of a project as a live wall of read-only AI status cards | `claude-code` `shell` | 0 | 2026-07-14 |
| [**herdr-nav**](https://github.com/jmarcelomb/herdr-nav)<br><sub>jmarcelomb</sub> | Pane, tab and workspace navigation plugin for herdr. | `rust` | 0 | 🆕 2026-07-30 |
| [**herdr-hasr**](https://github.com/KazBrekker1/herdr-hasr)<br><sub>KazBrekker1</sub> | Hasr (حصر — enumeration, a complete tally) — goto-style popup switcher for herdr: switch, rename, delete & create agents, tabs and spaces, with real-time done… | `tui` `go` | 0 | 🆕 2026-07-23 |
| [**herdr-cmd-marks**](https://github.com/leonho/herdr-cmd-marks)<br><sub>leonho</sub> | herdr plugin: per-project command bookmarks popup. Run bookmarked commands in a separate shell while your agent is busy (global, project, and smart sections). | `shell` | 0 | 2026-07-18 |
| [**herdr-plugin-last**](https://github.com/m4salah/herdr-plugin-last)<br><sub>m4salah</sub> | tmux-style last-tab and last-workspace navigation for Herdr | `rust` | 0 | 🆕 2026-07-30 |
| [**herdr-next-agent**](https://github.com/martin-ro/herdr-next-agent)<br><sub>martin-ro</sub> | Herdr plugin: jump to the next agent needing attention, ranked by a configurable status priority | `python` | 0 | 2026-07-15 |
| [**herdr-focus-or-tab**](https://github.com/mholtzscher/herdr-focus-or-tab)<br><sub>mholtzscher</sub> | Cycle through Herdr panes across tab boundaries | `terminal-multiplexer` `rust` | 0 | 🆕 2026-07-31 |
| [**herdr-touchbar**](https://github.com/omerturhan/herdr-touchbar)<br><sub>omerturhan</sub> | Shows working and blocked herdr agents on the MacBook Touch Bar; tap one to jump straight to its tab. | `ai-agents` `macos` `touchbar` `swift` | 0 | 🆕 2026-07-30 |
| [**herdr-plugins**](https://github.com/oullin/herdr-plugins)<br><sub>oullin</sub> | A collection of focused, independently installable plugins for Herdr. | `typescript` | 0 | 🆕 2026-07-22 |
| [**herdr-confirm-close-pane**](https://github.com/poweroutlet2/herdr-confirm-close-pane)<br><sub>poweroutlet2</sub> | A herdr plugin that asks for confirmation before closing a pane, like tmux's prefix+x confirm-before. | `shell` | 0 | 2026-07-06 |
| [**herdr-whichkey**](https://github.com/Qu4tro/herdr-whichkey)<br><sub>Qu4tro</sub> | A blezz/which-key-style action menu for herdr: one trigger key, then one keystroke per action — no typing, no Enter. | `rust` | 0 | 🆕 2026-07-22 |
| [**herdr-deck-navigation**](https://github.com/raghu-nandan-bs/herdr-deck-navigation)<br><sub>raghu-nandan-bs</sub> | Replaces herdr's flat workspace/tab/pane navigator with a Deck view built to reach any pane fast without scrolling. | `rust` `terminal` `tui` | 0 | 🆕 2026-07-21 |
| [**herdr-smartnav**](https://github.com/retroaalto/herdr-smartnav)<br><sub>retroaalto</sub> | Direction-aware pane navigation plugin for Herdr | `go` | 0 | 🆕 2026-08-01 |
| [**herdr-scratch**](https://github.com/shadowfax92/herdr-scratch)<br><sub>shadowfax92</sub> | Persistent per-pane Herdr scratch popups backed by private tmux sessions. | `neovim` `productivity` `rust` `terminal` `tmux` | 0 | 🆕 2026-07-31 |
| [**herdr-talon**](https://github.com/shadowfax92/herdr-talon)<br><sub>shadowfax92</sub> | Spatial keyboard hints for visible Herdr terminal targets. | `keyboard-navigation` `productivity` `rust` `terminal` `tmux-fingers` | 0 | 🆕 2026-08-01 |
| [**herdr-focus**](https://github.com/trapple/herdr-focus)<br><sub>trapple</sub> | Focus the next blocked/done agent pane and bring the terminal app to front. Global hotkey included. | `shell` | 0 | 🆕 2026-07-19 |
| [**herdr-compass**](https://github.com/ycros/herdr-compass)<br><sub>ycros</sub> | Unified directional navigation for Herdr across panes, tabs, and workspaces. | `python` | 0 | 2026-07-05 |

<details><summary>Also relevant to this purpose</summary>

- [thanhdat77/herdr-navigator](https://github.com/thanhdat77/herdr-navigator) — Jump to any Herdr workspace, agent, project, session, remote, directory, or action from one fuzzy navigator.
- [qu8n/herdr-automatic-rename](https://github.com/qu8n/herdr-automatic-rename) — Auto-renaming of herdr tabs in tmux style & 1-9 jump-key numbering for spaces/tabs/agents
- [speardragon/herdr-plugin-manager](https://github.com/speardragon/herdr-plugin-manager) — Manage herdr plugins from a popup — install, update, enable/disable, uninstall, and browse the herdr-plugin m…
- [leonho/herdr-idle-panes](https://github.com/leonho/herdr-idle-panes) — herdr plugin: popup checklist to review and close panes sitting at an idle shell
- [shoaibkhanz/herdr-active-agent-jump](https://github.com/shoaibkhanz/herdr-active-agent-jump) — herdr plugin: cycle focus forward/backward through in-flight (working/blocked) agents in layout order — the v…
- [vgreg/herdr-padio](https://github.com/vgreg/herdr-padio) — Switch PadIO controller modes automatically based on the app running in herdr's focused pane
- [victor-software-house/herdr-stash](https://github.com/victor-software-house/herdr-stash) — Stash a Herdr workspace: stop its agents, keep its shape and their conversations, and restore it later from a…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-files"></a>

## File Viewers & Editors

> I want to open a file tree inside a pane, or keep it in sync with my editor

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-file-viewer**](https://github.com/smarzban/herdr-file-viewer)<br><sub>smarzban</sub> | A git-aware, read-only file viewer for herdr. Mouse friendly, keyboard-driven TUI: tree + content pane with diffs, rendered markdown, and syntax highlighting. | `file-viewer` `git` `ratatui` `rust` `terminal` | 322 | 🆕 2026-08-02 |
| [**herdr-mirror**](https://github.com/nikok6/herdr-mirror)<br><sub>nikok6</sub> | Unify your local and remote sessions in one window: mirror remote herdr servers into your local sidebar and drive them over SSH | `rust` | 87 | 🆕 2026-07-31 |
| [**dotfiles**](https://github.com/edmundmiller/dotfiles)<br><sub>edmundmiller</sub> | For keeping all my Dotfiles update to date | `dotfiles` `emacs` `nix-dotfiles` `nixos` `nixos-configuration` | 77 | 🆕 2026-08-02 |
| [**herdr-sidebar**](https://github.com/alexarthurs/herdr-sidebar)<br><sub>alexarthurs</sub> | VS Code-style sidebar for the herdr: file explorer + git source control in one pane — syntax-highlighted previews, VS Code-style diffs, GitLens-style drawers,… | `git` `ratatui` `rust` `sidebar` `terminal` | 18 | 🆕 2026-07-25 |
| [**herdr-lazygit**](https://github.com/Crokily/herdr-lazygit)<br><sub>Crokily</sub> | Run lazygit in a herdr sidebar pane with AI commit messages — one key to open, one to expand, one to commit | `git` `lazygit` `shell` | 12 | 2026-07-17 |
| [**herdr-yazi**](https://github.com/speardragon/herdr-yazi)<br><sub>speardragon</sub> | Open Yazi in a herdr pane | `shell` | 12 | 2026-07-09 |
| [**herdr-nvim**](https://github.com/ChmaraX/herdr-nvim)<br><sub>ChmaraX</sub> | Neovim, fully integrated into your herdr workspace | `lua` `neovim` `nvim` `nvim-plugin` `rust` | 8 | 🆕 2026-08-01 |
| [**herdr-quicklook**](https://github.com/dwarvesf/herdr-quicklook)<br><sub>dwarvesf</sub> | Quick Look for herdr: pop the clipboard's path in an overlay, escalate to the file-viewer with one key | `terminal` `shell` | 7 | 🆕 2026-07-27 |
| [**herdr-git-status**](https://github.com/ezcorp-org/herdr-git-status)<br><sub>ezcorp-org</sub> | herdr plugin: per-space git working-tree status (staged/modified/untracked/conflicts) in the sidebar, next to the branch | `rust` | 6 | 🆕 2026-07-30 |
| [**herdr-flist**](https://github.com/devskale/herdr-flist)<br><sub>devskale</sub> | herdr - file list plugin | `python` | 5 | 2026-07-10 |
| [**herdr-context.nvim**](https://github.com/makyinmars/herdr-context.nvim)<br><sub>makyinmars</sub> | From Neovim, select code or stand on a line, choose a live Herdr agent, and stage structured context in that agent’s prompt—without submitting it. | `lua` | 5 | 🆕 2026-07-26 |
| [**herdr-file-viewer**](https://github.com/ismaelosuna7824/herdr-file-viewer)<br><sub>ismaelosuna7824</sub> | A keyboard-driven file explorer, code viewer and git client in a single Herdr pane — Go + Bubble Tea. | `bubbletea` `git` `golang` `tui` `go` | 3 | 2026-07-15 |
| [**herdr-lazygit**](https://github.com/JacquesvanWyk/herdr-lazygit)<br><sub>JacquesvanWyk</sub> | Open lazygit in a herdr split pane or tab with smart toggle (open / focus / close) | `lazygit` `shell` | 3 | 2026-07-12 |
| [**herdr-markdown-viewer**](https://github.com/arvindparmar-me/herdr-markdown-viewer)<br><sub>arvindparmar-me</sub> | Herdr plugin: drag-select a markdown path and press prefix+m to preview it in a right-split pane. | `shell` | 2 | 2026-07-17 |
| [**herdr-file-viewer**](https://github.com/jomarmontuya/herdr-file-viewer)<br><sub>jomarmontuya</sub> | Right-side Herdr file tree plugin with file tabs, cwd following, git decorations, and clickable links | `go` | 2 | 2026-07-13 |
| [**herdr-fresh**](https://github.com/rvalledorjr/herdr-fresh)<br><sub>rvalledorjr</sub> | A herdr plugin that runs Fresh, the terminal IDE, as a file viewer and editor inside a herdr pane. | `developer-tools` `editor` `fresh` `ide` `terminal` | 2 | 2026-07-17 |
| [**herdr-plugin-mermaid-preview**](https://github.com/Volpestyle/herdr-plugin-mermaid-preview)<br><sub>Volpestyle</sub> | Live Mermaid previews for Claude Code and Codex output in Herdr | `claude-code` `mermaid` `openai-codex` `terminal` `javascript` | 2 | 2026-07-10 |
| [**herdr-goto**](https://github.com/asumaran/herdr-goto)<br><sub>asumaran</sub> | Tree-style switcher across herdr repos, worktrees and panes | `go` | 1 | 🆕 2026-07-28 |
| [**herdr-wait**](https://github.com/cdc-lst/herdr-wait)<br><sub>cdc-lst</sub> | Configurable herdr plugin that tags an idle agent pane with what it's really doing — e.g. 'waiting: build-api' or 'waiting: codex' — matched from the pane's pr… | `typescript` | 1 | 2026-07-03 |
| [**herdr-claude-usage-multi**](https://github.com/iamhouser/herdr-claude-usage-multi)<br><sub>iamhouser</sub> | Claude plan usage gauges in the Herdr sidebar - Session/Week %, color escalation, countdown to reset, multi-account via CLAUDE_CONFIG_DIR profiles | `claude-code` `python` | 1 | 🆕 2026-07-25 |
| [**herdr-terminal-file-manager**](https://github.com/robert-flo/herdr-terminal-file-manager)<br><sub>robert-flo</sub> | A thin herdr wrapper for the elio file manager. It detects your active directory and launches elio natively, bringing its snappy previews, inline images, and b… | `shell` | 1 | 2026-07-10 |
| [**advanced-herdr-file-viewer**](https://github.com/thuanlm215/advanced-herdr-file-viewer)<br><sub>thuanlm215</sub> | Advanced, git-aware file viewer for herdr with fast file and full-text search, rich Unicode icons, independent tree scrolling, context actions, Git diffs, Mark… | `rust` | 1 | 🆕 2026-08-01 |
| [**herdr-open-in-editor**](https://github.com/timofey-TK/herdr-open-in-editor)<br><sub>timofey-TK</sub> | Open local and remote Herdr workspaces in VS Code or Zed | `vscode` `zed` `python` | 1 | 🆕 2026-07-30 |
| [**herdr-flutter**](https://github.com/ablause/herdr-flutter)<br><sub>ablause</sub> | A herdr sidebar to watch, hot reload and inspect a running Flutter app beside the coding agent. | `dart` | 0 | 🆕 2026-07-27 |
| [**herdr-numbered-workspaces**](https://github.com/abrose/herdr-numbered-workspaces)<br><sub>abrose</sub> | Puts a number in front of every space in herdr's sidebar, matching the indexed switch_workspace shortcut. | `shell` | 0 | 🆕 2026-07-21 |
| [**herdr-ctx**](https://github.com/aorumbayev/herdr-ctx)<br><sub>aorumbayev</sub> | Claude context-window indicator for herdr sidebar panes | `typescript` | 0 | 🆕 2026-07-21 |
| [**herdr-workbench**](https://github.com/azizuysal/herdr-workbench)<br><sub>azizuysal</sub> | A polished project sidebar for Herdr with Explorer, live file and content search, read-only Source Control, rich previews, file icons, and Git decorations. | `rust` | 0 | 🆕 2026-07-29 |
| [**herdr-sidebar-numbers**](https://github.com/cedrus-8864/herdr-sidebar-numbers)<br><sub>cedrus-8864</sub> | herdr plugin: show workspace and agent position numbers in the sidebar, matching the 1..9 shortcut digits | `ai-agents` `bun` `sidebar` `terminal` `javascript` | 0 | 🆕 2026-07-31 |
| [**herdr-codex-cost**](https://github.com/Coolsik/herdr-codex-cost)<br><sub>Coolsik</sub> | Show estimated Codex session cost in the Herdr sidebar | `codex` `shell` | 0 | 🆕 2026-07-31 |
| [**herdr-tab-badges**](https://github.com/CowboyVang/herdr-tab-badges)<br><sub>CowboyVang</sub> | Sidebar badge on herdr spaces that hold more than one tab. | `shell` | 0 | 🆕 2026-07-21 |
| [**herdr-plugin-agent-repo**](https://github.com/khatriafaz/herdr-plugin-agent-repo)<br><sub>khatriafaz</sub> | Herdr plugin that shows agent, repository, and branch names in agent pane headers and the sidebar. | `javascript` | 0 | 🆕 2026-07-24 |
| [**herdr-cmux-file-viewer**](https://github.com/linvald/herdr-cmux-file-viewer)<br><sub>linvald</sub> | herdr plugin that syncs cmux's file viewer to the currently focused herdr space | `python` | 0 | 🆕 2026-07-23 |
| [**herdr-agents-preview**](https://github.com/maedana/herdr-agents-preview)<br><sub>maedana</sub> | Multi-agent terminal preview dashboard for Herdr: all running agents shown at once, with the selected agent taking most of the width. | `rust` | 0 | 2026-07-17 |
| [**herdr-openmd**](https://github.com/RufusLin/herdr-openmd)<br><sub>RufusLin</sub> | Open selected markdown in openmd — a rich Qt preview from herdr | `shell` | 0 | 🆕 2026-07-29 |
| [**herdr-gitui**](https://github.com/Shi1xin/herdr-gitui)<br><sub>Shi1xin</sub> | herdr plugin: gitui in a sidebar pane — open/toggle, expand, light/dark themes | `gitui` `python` | 0 | 🆕 2026-07-28 |
| [**meadow**](https://github.com/Tetat-Chulchue/meadow)<br><sub>Tetat-Chulchue</sub> | Mouse-driven file explorer pane for the herdr terminal multiplexer | `python` | 0 | 🆕 2026-07-21 |
| [**herdr-launcher-pane**](https://github.com/y-hirakaw/herdr-launcher-pane)<br><sub>y-hirakaw</sub> | Docked click-to-launch pane for herdr — Finder/Explorer, VS Code, or any command you configure, per workspace | `launcher` `launcher-pane` `productivity` `python` | 0 | 🆕 2026-07-20 |

<details><summary>Also relevant to this purpose</summary>

- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) — A code-review + file-viewer sidebar for herdr — comment on an agent's diff, send it back. Plus a read-only vi…
- [jsmenzies/mergr](https://github.com/jsmenzies/mergr) — GitHub pull request status for Herdr Space sidebar rows.
- [vonzelle-vzt/herdr-extensions](https://github.com/vonzelle-vzt/herdr-extensions) — Tiny VS Code for herdr: a real editor with LSP diagnostics, autocomplete, rename and go-to-definition — plus…
- [brianh20/herdr-stagr](https://github.com/brianh20/herdr-stagr) — Source Control sidebar for herdr: stage, unstage, and discard with side-by-side diffs
- [ChmaraX/herdr-gitview](https://github.com/ChmaraX/herdr-gitview) — Git status/diff panel for herdr - review changes, edit in nvim, stage/commit/discard, all from the terminal
- [ctbaum/herdr-deck](https://github.com/ctbaum/herdr-deck) — The companion workspace launcher for herdr-agents.nvim: open or resume Claude and Codex in a ready-made Neovi…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-cost"></a>

## Tokens & Cost

> I want to see how much an agent is spending, and cut down on usage

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**llmtrim-herdr**](https://github.com/fkiene/llmtrim-herdr)<br><sub>fkiene</sub> | 💸 Shrink your token bill in herdr: compresses every agent pane's requests (-31% input / -74% output, measured live) and shows the savings on a per-pane badge | `llm-proxy` `llmtrim` `powershell` | 28 | 2026-07-02 |
| [**herdr-token-dashboard**](https://github.com/Davidcreador/herdr-token-dashboard)<br><sub>Davidcreador</sub> | Live token spend dashboard and notifications for Herdr agent panes | `ai-agents` `bubbletea` `opencode` `pi-agent` `token-dashboard` | 14 | 2026-07-15 |
| [**herdr-agent-usage**](https://github.com/senna-lang/herdr-agent-usage)<br><sub>senna-lang</sub> | Context meters and provider rate limits for agents running in Herdr. | `ai-agents` `claude-code` `codex` `golang` `rate-limiting` | 11 | 🆕 2026-08-01 |
| [**herdr-claude-usage**](https://github.com/alejodelosrios/herdr-claude-usage)<br><sub>alejodelosrios</sub> | Stop opening a Claude session just to check your quota. Live Claude plan usage — Session % \| Week % — always visible in your Herdr sidebar, shared across ever… | `claude` `claude-code` `python` | 1 | 🆕 2026-07-21 |
| [**scopefuel**](https://github.com/mgh3326/scopefuel)<br><sub>mgh3326</sub> | Scope-aware headroom gauge for AI coding agent plans — what is actually blocked (account/model/group) and when it refills | `ai-agents` `antigravity` `claude-code` `cli` `codex` | 0 | 🆕 2026-08-02 |
| [**herdr-usage-bar**](https://github.com/silverwolfdoc/herdr-usage-bar)<br><sub>silverwolfdoc</sub> | Usage limits and context meters for AI agents in Herdr, with a compact bottom usage bar. | `go` | 0 | 🆕 2026-07-30 |

<details><summary>Also relevant to this purpose</summary>

- [Coolsik/herdr-codex-cost](https://github.com/Coolsik/herdr-codex-cost) — Show estimated Codex session cost in the Herdr sidebar

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-monitor"></a>

## Monitoring & Dashboards

> I want an at-a-glance overview of agent and machine status

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-telemetry**](https://github.com/DIodide/herdr-telemetry)<br><sub>DIodide</sub> | Herdr plugin that streams workspace & agent telemetry to an endpoint you control — Go, single binary, privacy-first defaults | `golang` `telemetry` `go` | 9 | 2026-07-10 |
| [**herdr-pc-ram-and-cpu-usage-overlay**](https://github.com/ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay)<br><sub>ezcorp-org</sub> | herdr plugin: live CPU/RAM usage per space (workspace), as a share of the whole machine | `rust` | 8 | 🆕 2026-07-30 |
| [**herdres**](https://github.com/luminexord/herdres)<br><sub>luminexord</sub> | Telegram interface for monitoring and messaging Herdr coding agents, powered by Tendwire. | `coding-agents` `telegram` `python` | 7 | 🆕 2026-08-02 |
| [**herdr-beads**](https://github.com/miiraheart/herdr-beads)<br><sub>miiraheart</sub> | A beads (bd) task board for herdr: List, Table, Kanban over your bd issues, docked as a sidebar or floating. | `bd` `beads` `kanban` `rust` `tui` | 5 | 🆕 2026-07-24 |
| [**herdr-f1**](https://github.com/hmu332233/herdr-f1)<br><sub>hmu332233</sub> | An F1-style dashboard for your Herdr agents. | `agent-dashboard` `typescript` | 4 | 🆕 2026-07-29 |
| [**herdr-kanban**](https://github.com/KokiKono/herdr-kanban)<br><sub>KokiKono</sub> | Terminal Kanban board that links tasks to herdr tabs, persisted in SQLite | `rust` | 4 | 2026-07-10 |
| [**shepherd**](https://github.com/ryonakae/shepherd)<br><sub>ryonakae</sub> | Worker observability daemon and runtime bridges for Herdr-managed coding agents. | `pi-coding-agent` `pi-extension` `typescript` | 4 | 🆕 2026-07-22 |
| [**herdr-tally**](https://github.com/jasonrr/herdr-tally)<br><sub>jasonrr</sub> | Project-scoped todos & scratchpads for you and your agents.<br>📝 プロジェクト単位の TODO 管理 | `rust` `todo` | 3 | 🆕 2026-07-30 |
| [**herdr-workboard**](https://github.com/Phoobobo/herdr-workboard)<br><sub>Phoobobo</sub> | Kanban workboard TUI for herdr: boards are workspaces, task states are tabs, task sessions are panes | `kanban` `tui` `typescript` | 3 | 🆕 2026-07-30 |
| [**herdr-agent-dashboard**](https://github.com/carsonjones/herdr-agent-dashboard)<br><sub>carsonjones</sub> | prefix +a show herdr agents | `typescript` | 2 | 2026-07-16 |
| [**herdr-sysmon**](https://github.com/getpipher/herdr-sysmon)<br><sub>getpipher</sub> | System metrics in the Herdr sidebar — CPU, memory, battery, network, disk, clock. A faithful port of a tmux-cpu/tmux-battery/tmux-online-status status bar into… | `battery` `catppuccin` `cpu` `getpipher` `macos` | 2 | 🆕 2026-07-26 |
| [**shepherd**](https://github.com/jwarykowski/shepherd)<br><sub>jwarykowski</sub> | your todos herded | `cli` `developer-tools` `go-lang` `productivity` `task-management` | 2 | 🆕 2026-07-29 |
| [**herdr-tokscale-dashboard**](https://github.com/astkaasa/herdr-tokscale-dashboard)<br><sub>astkaasa</sub> | Open Tokscale as a local Herdr dashboard pane. | `dashboard` `tokscale` `shell` | 1 | 2026-06-26 |
| [**herdr-telemetry-bridge**](https://github.com/CodyBontecou/herdr-telemetry-bridge)<br><sub>CodyBontecou</sub> | Herdr plugin that streams local workspace, repo, coding-agent, model, and trace telemetry to external clients. | `coding-agents` `telemetry` `time-md` `javascript` | 1 | 2026-06-26 |
| [**herdr-compose**](https://github.com/mattyan1053/herdr-compose)<br><sub>mattyan1053</sub> | Herdr Plugin for docker compose | `terminal` `tui` `shell` | 1 | 🆕 2026-07-24 |
| [**herdr-ports**](https://github.com/Numbered-com/herdr-ports)<br><sub>Numbered-com</sub> | Surface active dev servers in herdr: a generic $ports badge on every Space running at least one TCP listener | `pids` `ports` `shell` | 1 | 🆕 2026-07-23 |
| [**herdr-slurm**](https://github.com/quan-meng/herdr-slurm)<br><sub>quan-meng</sub> | Create Herdr workspaces and monitored agent tabs for Slurm allocations | `hpc` `slurm` `terminal-multiplexer` `python` | 1 | 🆕 2026-07-24 |
| [**herdr-plugin-codex-subs**](https://github.com/benkraus/herdr-plugin-codex-subs)<br><sub>benkraus</sub> | Herdr dashboard for CLIProxyAPI Codex subscription quotas and reset credits | `go` | 0 | 🆕 2026-07-30 |
| [**herdr-vitals**](https://github.com/ericcparsons/herdr-vitals)<br><sub>ericcparsons</sub> | macOS herdr plugin: CPU/RAM per agent and active dev server ports per space, in the sidebar, plus a popup to kill them | `bun` `developer-tools` `terminal` `typescript` | 0 | 🆕 2026-07-29 |
| [**herdr-statusline**](https://github.com/iiii1224/herdr-statusline)<br><sub>iiii1224</sub> | Customizable status line for herdr sessions. | `python` | 0 | 🆕 2026-07-31 |
| [**herdr-phin-board**](https://github.com/phin-tech/herdr-phin-board)<br><sub>phin-tech</sub> | Herdr plugin: a status board over your spaces — todo, in progress, waiting on someone, done, plus any status you invent. List or kanban. | `bubbletea` `tui` `go` | 0 | 🆕 2026-07-29 |
| [**colloquy**](https://github.com/SoMaCoSF/colloquy)<br><sub>SoMaCoSF</sub> | Self-addressing, ephemerally-cached causal DAG audit logs and telemetry for agent swarms. | `colloquy` `gyst` `javascript` | 0 | 🆕 2026-07-29 |
| [**conflux-herdr**](https://github.com/tumf/conflux-herdr)<br><sub>tumf</sub> | Herdr plugin pane for running the Conflux TUI and reporting its lifecycle state. | `shell` | 0 | 🆕 2026-07-26 |
| [**adlc-herdr**](https://github.com/voodootikigod/adlc-herdr)<br><sub>voodootikigod</sub> | ADLC herdr plugin — per-pane phase/ticket/gate status, backlog board, gate actions, and adlc-fleet run observability. Auto-synced mirror of voodootikigod/adlc/… | `javascript` | 0 | 🆕 2026-07-29 |

<details><summary>Also relevant to this purpose</summary>

- [nelsonPires5/herdr-board](https://github.com/nelsonPires5/herdr-board) — Kanban board for herdr — cards are prompts dispatched to AI agents in visible panes
- [chouxcreams/herdr-dashboard](https://github.com/chouxcreams/herdr-dashboard) — PR status dashboard TUI for herdr workspaces — PR state / CI / reviews per pane at a glance
- [bengemine/herdr-hibernate](https://github.com/bengemine/herdr-hibernate) — Hibernate idle coding-agent panes in Herdr (Claude Code, Codex, Grok) — free the RAM, press Enter to resume t…
- [Javamomma/herdr-scribe](https://github.com/Javamomma/herdr-scribe) — herdr plugin: live no-recording meeting transcription — mic → RAM-only transcript + live analyst panes; on st…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-finder"></a>

## Fuzzy Finders & Palettes

> I want to invoke commands or projects even when I only half-remember their names

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-navigator**](https://github.com/thanhdat77/herdr-navigator)<br><sub>thanhdat77</sub> | Jump to any Herdr workspace, agent, project, session, remote, directory, or action from one fuzzy navigator. | `fuzzy-finder` `rust` `terminal` `workspace-manager` | 43 | 🆕 2026-08-02 |
| [**termscope**](https://github.com/iurysza/termscope)<br><sub>iurysza</sub> | Open files and links already visible on your terminal screen in a split. | `python` `television` `terminal` `tmux` | 35 | 2026-07-18 |
| [**herdr-sessionizer**](https://github.com/andrewchng/herdr-sessionizer)<br><sub>andrewchng</sub> | Fuzzy-open projects and worktrees, then bootstrap workspaces from declarative TOML layouts — tabs, pane splits, commands, and per-repo overrides. | `bun` `fuzzy-finder` `fzf` `git-worktree` `sessionizer` | 24 | 🆕 2026-08-02 |
| [**herdr-command-palette**](https://github.com/JanTvrdik/herdr-command-palette)<br><sub>JanTvrdik</sub> | fzf command palette for herdr — fuzzy-pick and run any plugin action | `shell` | 23 | 2026-06-29 |
| [**herdr-plugin-sesh**](https://github.com/fullerzz/herdr-plugin-sesh)<br><sub>fullerzz</sub> | Sesh-style workspace picker TUI for Herdr. Integrates with zoxide to create workspaces from commonly used directories. | `bubbletea` `sesh` `tui` `zoxide` `go` | 19 | 🆕 2026-08-02 |
| [**herdr-zoxide**](https://github.com/den-tanui/herdr-zoxide)<br><sub>den-tanui</sub> | Herdr plugin to create workspaces, tabs and panes from zoxide directories. | `zoxide` `shell` | 9 | 🆕 2026-07-25 |
| [**herdr-bar**](https://github.com/jeffarese/herdr-bar)<br><sub>jeffarese</sub> | Cmd+K for herdr: fuzzy-jump to any tab, agent, repo or branch. Python stdlib only. | `command-bar` `fuzzy-finder` `python` `terminal` `tui` | 8 | 🆕 2026-07-25 |
| [**herdr-drovr**](https://github.com/AVGVSTVS96/herdr-drovr)<br><sub>AVGVSTVS96</sub> | easily move Herdr tabs to other workspaces | `fzf` `terminal` `javascript` | 6 | 🆕 2026-08-02 |
| [**herdr-ghq**](https://github.com/crafts69guy/herdr-ghq)<br><sub>crafts69guy</sub> | A herdr plugin: fuzzy-switch across running agents, open workspaces, and ghq repositories in one Rust TUI — and open a repo in a new workspace, tab, split, or… | `developer-tools` `ghq` `ratatui` `rust` `terminal` | 4 | 🆕 2026-07-22 |
| [**herdr-grep-nvim**](https://github.com/cinco/herdr-grep-nvim)<br><sub>cinco</sub> | herdr plugin: live-grep with fzf + ripgrep and open the match in nvim, in a split beside your work | `shell` | 3 | 2026-07-17 |
| [**herdr-palette**](https://github.com/ramarivera/herdr-palette)<br><sub>ramarivera</sub> | A Rust/Ratatui fuzzy command palette for Herdr workspaces. | `command-palette` `ratatui` `rust` `terminal` `tui` | 3 | 🆕 2026-07-24 |
| [**herdr-sessionizer**](https://github.com/salkhalil/herdr-sessionizer)<br><sub>salkhalil</sub> | tmux-sessionizer for herdr: fzf over open workspaces and zoxide directories, create-or-focus with template tabs | `shell` | 3 | 🆕 2026-07-27 |
| [**herdr-agent-recency**](https://github.com/ugurtarlig/herdr-agent-recency)<br><sub>ugurtarlig</sub> | Theme-aware Herdr picker sorted by meaningful Codex and Claude activity | `claude-code` `codex` `fzf` `python` | 3 | 2026-07-17 |
| [**herdr-configurable-picker**](https://github.com/yoshiori/herdr-configurable-picker)<br><sub>yoshiori</sub> | Tree-based goto picker for herdr with fully configurable keybindings | `rust` | 3 | 2026-07-05 |
| [**herdr-launcher**](https://github.com/arjenblokzijl/herdr-launcher)<br><sub>arjenblokzijl</sub> | Fuzzy-pick a declarative TOML workflow, fill a form, and launch a coding agent in a new herdr space. | `launcher` `ratatui` `rust` `tui` | 2 | 2026-07-10 |
| [**herdr-spotify**](https://github.com/iikjl/herdr-spotify)<br><sub>iikjl</sub> | Spotify now-playing overlay plugin for herdr — album art, playback controls, and optional search/queue/like via the Spotify Web API | `spotify` `terminal` `go` | 2 | 2026-07-07 |
| [**herdr-recent-workspaces**](https://github.com/ismaelosuna7824/herdr-recent-workspaces)<br><sub>ismaelosuna7824</sub> | Open Recent for Herdr — a fuzzy-filterable list of the folders you've opened as workspaces. Pick one to open or re-focus that workspace; browse the filesystem… | `go` | 2 | 2026-07-10 |
| [**herdr-hunk**](https://github.com/JacquesvanWyk/herdr-hunk)<br><sub>JacquesvanWyk</sub> | Interactive fzf picker for hunk diffs in herdr: commits, ranges, stashes, plus auto-open when an agent finishes | `fzf` `hunk` `shell` | 2 | 2026-07-12 |
| [**herdr-keybind-search**](https://github.com/malone-c/herdr-keybind-search)<br><sub>malone-c</sub> | Searchable keybind overlay for herdr (fzf). Press a key, fuzzy-search your keybinds. | `shell` | 2 | 2026-07-15 |
| [**herdr-keymap**](https://github.com/The-Dave-Stack/herdr-keymap)<br><sub>The-Dave-Stack</sub> | A herdr plugin: shows every keybinding in an overlay palette and runs the ones with a CLI equivalent | `typescript` | 2 | 2026-07-17 |
| [**herdr-url-picker**](https://github.com/abrose/herdr-url-picker)<br><sub>abrose</sub> | herdr plugin: pick a URL printed in the current pane with fzf and open it in the default browser | `shell` | 1 | 🆕 2026-07-22 |
| [**herdr-jump**](https://github.com/agustinvalencia/herdr-jump)<br><sub>agustinvalencia</sub> | Separate overlay pickers for herdr spaces and agents — jump to any workspace or agent, with live status colours | `go` | 1 | 🆕 2026-07-24 |
| [**herdr-cast**](https://github.com/aliou/herdr-cast)<br><sub>aliou</sub> | Personal Herdr plugin for native macOS agent notifications, fuzzy workspace navigation, zoxide-backed workspace creation, and layout commands. | `developer-tools` `macos` `notifications` `ratatui` `rust` | 1 | 🆕 2026-08-01 |
| [**herdr-command-palette**](https://github.com/alon-z/herdr-command-palette)<br><sub>alon-z</sub> | Herdr plugin: fuzzy workspace/directory command palette. | `javascript` | 1 | 2026-06-22 |
| [**herdr-url-picker**](https://github.com/chouxcreams/herdr-url-picker)<br><sub>chouxcreams</sub> | Herdr plugin: pick a URL from the focused pane and open it in your browser | `shell` | 1 | 🆕 2026-07-22 |
| [**herdr-simple-switcher**](https://github.com/haphamdev/herdr-simple-switcher)<br><sub>haphamdev</sub> | Fuzzy searching for workspaces, tabs and AI agents | `shell` | 1 | 🆕 2026-08-01 |
| [**herdr-workspace-launcher**](https://github.com/ImArtisann/herdr-workspace-launcher)<br><sub>ImArtisann</sub> | A macOS Herdr plugin for quickly creating focused workspaces with a searchable, keyboard-driven directory picker. | `typescript` | 1 | 2026-07-16 |
| [**herdr-keys**](https://github.com/JacquesvanWyk/herdr-keys)<br><sub>JacquesvanWyk</sub> | Fuzzy-searchable keybinding cheatsheet for herdr (packs, discovery, personal overrides) | `shell` | 1 | 2026-07-12 |
| [**herdr-fzf-url**](https://github.com/kaar/herdr-fzf-url)<br><sub>kaar</sub> | Fuzzy-find and open URLs from your herdr pane scrollback — a port of tmux-fzf-url | `shell` | 1 | 🆕 2026-07-29 |
| [**herdr-kiosk**](https://github.com/thomasschafer/herdr-kiosk)<br><sub>thomasschafer</sub> | Fuzzy-find Git repos and branches, and open them as worktrees in Herdr | `rust` | 1 | 🆕 2026-07-30 |
| [**herdr-pane-picker**](https://github.com/ugurtarlig/herdr-pane-picker)<br><sub>ugurtarlig</sub> | Pick a Herdr pane by typing its on-pane character hint | `terminal` `wezterm` `python` | 1 | 2026-07-17 |
| [**herdr-fzf-url**](https://github.com/x0d7x/herdr-fzf-url)<br><sub>x0d7x</sub> | Scan herdr terminal panes for URLs and interactively pick one with fzf | `fzf` `go` `url` | 1 | 2026-06-26 |
| [**herdr-open-local-paths**](https://github.com/yigitkg/herdr-open-local-paths)<br><sub>yigitkg</sub> | Herdr plugin that detects local paths and opens or reveals them through a simple picker on Windows, Linux, and WSL. | `developer-tools` `python` `terminal` `wsl` | 1 | 🆕 2026-07-28 |
| [**herdr-agents-picker**](https://github.com/yxhta/herdr-agents-picker)<br><sub>yxhta</sub> | Herdr plugin: workspace-picker-style fuzzy picker for agent panes, with live pane preview (Rust + ratatui) | `rust` | 1 | 🆕 2026-07-31 |
| [**herdr-picker**](https://github.com/bkarpinos/herdr-picker)<br><sub>bkarpinos</sub> | A fast popup picker for searching and previewing workspaces, agents, and tabs in herdr. | `go` | 0 | 🆕 2026-07-25 |
| [**herdr-control-panel**](https://github.com/iskwyuki/herdr-control-panel)<br><sub>iskwyuki</sub> | One keybinding, one panel for herdr: open a workspace from history or any path, and add your own actions. Pure bash + fzf, no build step. | `bash` `fzf` `terminal` `shell` | 0 | 🆕 2026-08-01 |
| [**pj-herdr**](https://github.com/josephschmitt/pj-herdr)<br><sub>josephschmitt</sub> | Herdr plugin that uses the PJ picker to open a new workspace | `shell` | 0 | 2026-07-15 |
| [**herdr-cull**](https://github.com/krzysztoff1/herdr-cull)<br><sub>krzysztoff1</sub> | Review and close idle agent panes in herdr — fzf multi-select, nothing closes without confirmation. | `ai-agents` `claude` `codex` `fzf` `terminal` | 0 | 🆕 2026-07-20 |
| [**herdr-shortcut**](https://github.com/matheus3301/herdr-shortcut)<br><sub>matheus3301</sub> | Shortcut task picker and coding-agent launcher for Herdr | `bubbletea` `claude-code` `codex` `coding-agents` `developer-tools` | 0 | 🆕 2026-07-24 |
| [**herdr-omarchy-theme-sync**](https://github.com/maxBRT/herdr-omarchy-theme-sync)<br><sub>maxBRT</sub> | Sync Herdr's UI palette with the active Omarchy theme | `linux` `omarchy` `theme` `python` | 0 | 🆕 2026-07-28 |
| [**herdr-smart-workspace**](https://github.com/nicolasvasquez/herdr-smart-workspace)<br><sub>nicolasvasquez</sub> | Herdr plugin for quickly switching workspaces within a session or creating new ones from zoxide with an overlay fzf picker. | `python` | 0 | 2026-07-02 |
| [**herdr-launcher**](https://github.com/nicolegros/herdr-launcher)<br><sub>nicolegros</sub> | A herdr plugin that provides a fuzzy directory picker for quickly creating or switching to workspaces. | `go` | 0 | 2026-07-15 |
| [**mux-prompter**](https://github.com/phine-apps/mux-prompter)<br><sub>phine-apps</sub> | Fuzzy-pick and inject context-aware prompts into Herdr panes | `fzf` `prompt-engineering` `terminal-multiplexer` `shell` | 0 | 🆕 2026-07-20 |
| [**herdr-claude-profile**](https://github.com/quinnjr/herdr-claude-profile)<br><sub>quinnjr</sub> | herdr plugin: switch and manage claude-profile profiles from an overlay palette | `typescript` | 0 | 🆕 2026-07-20 |
| [**herdr-plugins**](https://github.com/shelken/herdr-plugins)<br><sub>shelken</sub> | Herdr plugins monorepo (auto-pi: open pi by area + session picker) | `python` | 0 | 2026-07-17 |
| [**herdr-file-picker**](https://github.com/shivammehta25/herdr-file-picker)<br><sub>shivammehta25</sub> | Vibecoded port of tmux-file-picker to herdr | `shell` | 0 | 🆕 2026-07-29 |
| [**herdr-workspacex**](https://github.com/willfish/herdr-workspacex)<br><sub>willfish</sub> | Rust-native fuzzy Herdr workspace switcher with zoxide-backed workspace creation | `rust` `workspace-manager` `zoxide` | 0 | 2026-07-07 |
| [**herdr-fzf-url**](https://github.com/willian/herdr-fzf-url)<br><sub>willian</sub> | Pick URLs from the focused pane with `fzf`, then open or copy them. | `fzf` `shell` | 0 | 🆕 2026-07-28 |

<details><summary>Also relevant to this purpose</summary>

- [beyondlex/herdr-recent-navigator](https://github.com/beyondlex/herdr-recent-navigator) — A recent workspaces/tabs/panes switcher for Herdr. Opens an popup window listing recently focused workspaces,…
- [JacquesvanWyk/herdr-linear](https://github.com/JacquesvanWyk/herdr-linear) — fzf-driven Linear panel in a herdr split pane or tab: search issues, drill into projects, create issues, chan…
- [caoer/ccc-herdr-layout](https://github.com/caoer/ccc-herdr-layout) — Visual layout picker plugin for herdr — one key, live preview

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-automation"></a>

## Automation, Hooks & Schedules

> I want a fixed set of steps to run automatically on worktree creation or at a chosen time

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-browser**](https://github.com/ogulcancelik/herdr-browser)<br><sub>ogulcancelik</sub> | Render a real Chromium view inside a Herdr pane and drive it over CDP. | `browser` `browser-automation` `cdp` `chromium` `kitty-graphics` | 237 | 🆕 2026-07-28 |
| [**zed-herdr**](https://github.com/ImArtisann/zed-herdr)<br><sub>ImArtisann</sub> | Automatically keeps your active HerdR workspace in sync with your existing Zed session. | `typescript` | 16 | 2026-07-16 |
| [**herdr-worktree-setup**](https://github.com/tdi/herdr-worktree-setup)<br><sub>tdi</sub> | herdr plugin: run per-project setup steps when a worktree is created (copy .env from main, mise trust, direnv allow, install deps) | `javascript` | 16 | 🆕 2026-07-20 |
| [**herdr-automatic-rename**](https://github.com/qu8n/herdr-automatic-rename)<br><sub>qu8n</sub> | Auto-renaming of herdr tabs in tmux style & 1-9 jump-key numbering for spaces/tabs/agents | `shell` | 11 | 🆕 2026-07-30 |
| [**herdr-routines**](https://github.com/mrcndz/herdr-routines)<br><sub>mrcndz</sub> | Herdr plugin that runs scheduled routines: cron or interval schedules that open a tab in a workspace and run a command or launch an agent. | `python` | 8 | 🆕 2026-07-18 |
| [**herdr-auto-pilot**](https://github.com/0xGosu/herdr-auto-pilot)<br><sub>0xGosu</sub> | A Herdr plugin that will automatically prompt the running AI Coding CLI on-behalf of you via Herdr API. The plugin has training mode which learn from your acti… | `go` | 5 | 🆕 2026-08-02 |
| [**herdr-tab-title**](https://github.com/aarsh21/herdr-tab-title)<br><sub>aarsh21</sub> | Automatic tmux-like tab titles for Herdr | `rust` `terminal` `tmux` | 5 | 2026-07-08 |
| [**herdr-workflows**](https://github.com/aorumbayev/herdr-workflows)<br><sub>aorumbayev</sub> | Declarative automation for repetitive steps in herdr | `agentic-ai` `agentic-workflow` `agents` `ai` `claude` | 3 | 🆕 2026-08-02 |
| [**herdr-agent-config-manager**](https://github.com/Phoobobo/herdr-agent-config-manager)<br><sub>Phoobobo</sub> | Hybrid CLI + Herdr plugin for detecting and centrally managing agent skills, MCP, plugins, and hooks | `python` | 3 | 2026-07-06 |
| [**herdr-js-worktree-bootstrap**](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap)<br><sub>LeonardoTrapani</sub> | Automatically bootstrap Herdr worktrees for JavaScript and TypeScript with lockfile-aware installs and safe env restoration | `automation` `bun` `developer-tools` `git-worktree` `javascript` | 2 | 2026-07-15 |
| [**bermuda**](https://github.com/bon5co/bermuda)<br><sub>bon5co</sub> | An agent harness: schedules work and runs each job as an interactive herdr agent | `agents` `golang` `tui` `go` | 1 | 🆕 2026-08-01 |
| [**herdr-fwd**](https://github.com/go-min/herdr-fwd)<br><sub>go-min</sub> | Automatic loopback port forwarding for remote Herdr sessions. | `port-forwarding` `ssh` `terminal` `rust` | 1 | 🆕 2026-08-01 |
| [**say-hook**](https://github.com/HikaruEgashira/say-hook)<br><sub>HikaruEgashira</sub> | A macOS CLI that reads Claude Code hook events aloud using ElevenLabs text-to-speech. | `typescript` | 1 | 🆕 2026-08-01 |
| [**herdr-pane-balancer**](https://github.com/jeph/herdr-pane-balancer)<br><sub>jeph</sub> | Automatically balance, equalize, and tile Herdr terminal panes on create, close, and exit. | `python` | 1 | 🆕 2026-08-02 |
| [**tendwire**](https://github.com/plotarmordev/tendwire)<br><sub>plotarmordev</sub> | Local API for Herdr: connect coding agents to apps, automations, and any local system. | `agent-api` `local-first` `python` | 1 | 🆕 2026-08-02 |
| [**herdr-plugin**](https://github.com/ppggff/herdr-plugin)<br><sub>ppggff</sub> | Automatically remember and restore the right macOS input method (ime) for each Herdr pane. | `ime` `input-method` `macos` `python` | 1 | 🆕 2026-07-27 |
| [**herdr-auto-tab-name**](https://github.com/dev-shimada/herdr-auto-tab-name)<br><sub>dev-shimada</sub> | herdr plugin: automatically name tabs after their current directory | `javascript` | 0 | 🆕 2026-08-01 |
| [**herdr-context-namer**](https://github.com/eabadim/herdr-context-namer)<br><sub>eabadim</sub> | Auto-name Herdr tabs and workspaces from pane context via OpenCode | `opencode` `python` | 0 | 🆕 2026-07-29 |
| [**herdr-pane-name**](https://github.com/go-min/herdr-pane-name)<br><sub>go-min</sub> | Herdr plugin that automatically names panes in your terminal sessions. | `pane-naming` `terminal` `terminal-multiplexer` `rust` | 0 | 🆕 2026-08-02 |
| [**herdr-plugin-auto-rename**](https://github.com/khatriafaz/herdr-plugin-auto-rename)<br><sub>khatriafaz</sub> | Automatically rename fresh Herdr workspaces and Git branches from a Pi session's first prompt. | `typescript` | 0 | 🆕 2026-07-24 |
| [**herdr-shepherd**](https://github.com/mikedclarke/herdr-shepherd)<br><sub>mikedclarke</sub> | Scheduled agent sessions for herdr: heartbeats, cron routines, and scripts, launched as visible herdr workspaces. | `coding-agents` `cron` `go` `scheduler` `tui` | 0 | 🆕 2026-07-31 |
| [**herdr-worktreeinclude**](https://github.com/untalfranfernandez/herdr-worktreeinclude)<br><sub>untalfranfernandez</sub> | Herdr plugin that populates every new git worktree with the gitignored local files it needs — .env, settings.local.json, fixtures. Declare them once in a .work… | `claude-code` `dotenv` `git-worktree` `worktree` | 0 | 🆕 2026-07-29 |
| [**herdr-padio**](https://github.com/vgreg/herdr-padio)<br><sub>vgreg</sub> | Switch PadIO controller modes automatically based on the app running in herdr's focused pane | `game-controller` `macos` `padio` `python` | 0 | 🆕 2026-08-02 |
| [**numberer-manager**](https://github.com/yuritada/numberer-manager)<br><sub>yuritada</sub> | A lightweight Herdr plugin that automatically prefixes workspace and tab labels with their current list position (e.g., 1: space and 1: tab). | `python` | 0 | 🆕 2026-07-25 |
| [**herdr-booking-task-plugin**](https://github.com/zerodice0/herdr-booking-task-plugin)<br><sub>zerodice0</sub> | Schedule Herdr agent prompts and local CLI commands on macOS and Linux. | `golang` `scheduler` `go` | 0 | 🆕 2026-07-31 |

<details><summary>Also relevant to this purpose</summary>

- [freethinkel/herdr-plugin-git-worktree-hooks](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks) — Run shell commands when a git worktree is created/removed — one YAML config for all projects, living outside…
- [timofey-TK/herdr-worktree-hooks](https://github.com/timofey-TK/herdr-worktree-hooks) — herdr plugin: run custom setup/teardown commands when a git worktree is created, opened, or removed
- [Epsomsaltskerosinelamp950/herdr-browser](https://github.com/Epsomsaltskerosinelamp950/herdr-browser) — Render a live, interactive Chromium view within Herdr panes for real-time automation monitoring and control u…
- [Newt6611/herdr-tab-title](https://github.com/Newt6611/herdr-tab-title) — Herdr Tab Title automatically renames Herdr tabs with clean, workspace-local numbering like 1. Codex, 2. Term…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-session"></a>

## Session State & Restore

> I want to close my work and later resume from exactly the same state

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-resurrect**](https://github.com/ntindle/herdr-resurrect)<br><sub>ntindle</sub> | tmux-resurrect for herdr — snapshot workspaces, tabs, panes, cwd, running programs and agents, and restore them after a crash or reboot. | `crash-recovery` `session-manager` `terminal-multiplexer` `tmux-resurrect` `javascript` | 10 | 2026-07-12 |
| [**herdr-session-parker**](https://github.com/iviaxpow3r/herdr-session-parker)<br><sub>iviaxpow3r</sub> | Herdr plugin to park panes/tabs and resume supported agent sessions later | `agent-tools` `python` | 9 | 2026-07-03 |
| [**herdr-agent-inbox**](https://github.com/douglascorrea/herdr-agent-inbox)<br><sub>douglascorrea</sub> | An inbox for your coding agents in herdr — session titles, settle/mark-unread triage, runtimes, workspace rollups, and resumable chat history | `ai-agents` `terminal` `python` | 5 | 🆕 2026-07-28 |
| [**herdr-claude-auto-retry**](https://github.com/mo-arvan/herdr-claude-auto-retry)<br><sub>mo-arvan</sub> | Wait out Anthropic rate limits and auto-resume Claude Code, herdr-native: no tmux, no shell wrapper. | `javascript` | 5 | 2026-07-16 |
| [**session-digger**](https://github.com/taxueseek/session-digger)<br><sub>taxueseek</sub> | 跨环境会话历史挖掘与知识管理。分析记录。支持 Claude/Grok/Kimi Code/Codex/WorkBuddy/Trae CN 等主流环境 | `python` | 4 | 🆕 2026-07-21 |
| [**herdr-notes**](https://github.com/alexarthurs/herdr-notes)<br><sub>alexarthurs</sub> | Persistent markdown notes pane for herdr - one note per workspace, rendered preview + edit mode, autosaves and survives restarts | `markdown` `notes` `ratatui` `rust` `terminal` | 3 | 🆕 2026-07-25 |
| [**herdr-synchronize-panes**](https://github.com/furuhashin/herdr-synchronize-panes)<br><sub>furuhashin</sub> | Herdr plugin: broadcast one command to every pane in the current tab (tmux synchronize-panes style) | `javascript` | 2 | 2026-07-14 |
| [**herdr_sync**](https://github.com/kamaaina/herdr_sync)<br><sub>kamaaina</sub> | synchronize panes in herdr | `zig` | 2 | 2026-07-01 |
| [**herdr-e2b**](https://github.com/tomasvarga/herdr-e2b)<br><sub>tomasvarga</sub> | Mirror a git worktree into a fresh E2B cloud sandbox on demand — a snapshot upload (uncommitted changes and all), no push or clone. A herdr plugin. | `cli` `cloud-dev` `e2b` `git-worktree` `sandbox` | 2 | 🆕 2026-07-18 |
| [**herdr-pane-id-labeler**](https://github.com/4Born/herdr-pane-id-labeler)<br><sub>4Born</sub> | Herdr plugin that keeps pane labels synchronized with public pane IDs such as w1:p2. | `developer-tools` `terminal` `javascript` | 1 | 🆕 2026-07-26 |
| [**herdr-todos-windows**](https://github.com/aclima01/herdr-todos-windows)<br><sub>aclima01</sub> | Live panel mirroring a herdr agent's task list (TaskCreate/TaskUpdate) so you can follow its plan | `powershell` | 1 | 🆕 2026-07-22 |
| [**herdr-oh-my-agent**](https://github.com/GavinTomlins/herdr-oh-my-agent)<br><sub>GavinTomlins</sub> | Mirror every oh-my-openagent subagent delegation into its own Herdr pane or tab — live, with full session state and scrollback | `typescript` | 1 | 🆕 2026-07-31 |
| [**herdr-thread-to-tab**](https://github.com/toyamarinyon/herdr-thread-to-tab)<br><sub>toyamarinyon</sub> | Keep single-pane Herdr tab labels in sync with Claude Code and Codex thread titles. | `rust` | 1 | 🆕 2026-07-24 |
| [**herdr-suspend-workspace**](https://github.com/asermax/herdr-suspend-workspace)<br><sub>asermax</sub> | Suspend a herdr workspace (snapshot layout + agents, close it, restore later from a popup picker) | `typescript` | 0 | 🆕 2026-07-31 |
| [**herdr-hibernate**](https://github.com/bengemine/herdr-hibernate)<br><sub>bengemine</sub> | Hibernate idle coding-agent panes in Herdr (Claude Code, Codex, Grok) — free the RAM, press Enter to resume the exact session. | `claude-code` `python` | 0 | 🆕 2026-07-30 |
| [**herdr-flakes**](https://github.com/iQua/herdr-flakes)<br><sub>iQua</sub> | Flakes plugin for Herdr — mirror and steer your Flakes runs in your local Herdr session | `javascript` | 0 | 🆕 2026-07-22 |
| [**herdr-codex-app**](https://github.com/jievince/herdr-codex-app)<br><sub>jievince</sub> | Turn Herdr into a terminal-first Codex app: sync projects, resume chats. | `codex` `terminal` `javascript` | 0 | 🆕 2026-07-31 |
| [**herdr-undo-close**](https://github.com/pedroloch/herdr-undo-close)<br><sub>pedroloch</sub> | Reopen a closed tab in herdr, like Cmd+Shift+T in a browser - restores the label, the split tree with its ratios, each pane's cwd, and the tab's position. | `python` | 0 | 🆕 2026-07-30 |
| [**herdr-stash**](https://github.com/victor-software-house/herdr-stash)<br><sub>victor-software-house</sub> | Stash a Herdr workspace: stop its agents, keep its shape and their conversations, and restore it later from a clickable two-column popup. | `rust` `terminal` `tui` | 0 | 🆕 2026-07-29 |
| [**live-sync-panes**](https://github.com/wg1k/live-sync-panes)<br><sub>wg1k</sub> | Herdr plugin: broadcast a command, or live-sync keystrokes, to every pane in a tab | `javascript` | 0 | 2026-07-08 |

<details><summary>Also relevant to this purpose</summary>

- [afogel/shepherdr](https://github.com/afogel/shepherdr) — Shepherd delegated coding agents into visible, auditable herdr panes you can watch, resume, and take over — a…
- [KokiKono/herdr-kanban](https://github.com/KokiKono/herdr-kanban) — Terminal Kanban board that links tasks to herdr tabs, persisted in SQLite
- [AkashJana18/herdr-scratch](https://github.com/AkashJana18/herdr-scratch) — Persistent scratchpads for Herdr, paving the way for floating utility panes.
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — Automatically bootstrap Herdr worktrees for JavaScript and TypeScript with lockfile-aware installs and safe e…
- [ppggff/herdr-plugin](https://github.com/ppggff/herdr-plugin) — Automatically remember and restore the right macOS input method (ime) for each Herdr pane.
- [shadowfax92/herdr-scratch](https://github.com/shadowfax92/herdr-scratch) — Persistent per-pane Herdr scratch popups backed by private tmux sessions.
- [voodootikigod/adlc-herdr](https://github.com/voodootikigod/adlc-herdr) — ADLC herdr plugin — per-pane phase/ticket/gate status, backlog board, gate actions, and adlc-fleet run observ…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-naming"></a>

## Titles, Naming & Looks

> I want tab names and terminal titles to be automatically clear, or want to change how things look

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-window-title-sync**](https://github.com/rjyo/herdr-window-title-sync)<br><sub>rjyo</sub> | Syncs terminal titles from workspaces, tabs, and agent sessions (use w/ Moshi) | `moshi` `terminal-title` `javascript` | 24 | 2026-06-26 |
| [**herdr-tab-smart-rename**](https://github.com/iurysza/herdr-tab-smart-rename)<br><sub>iurysza</sub> | Generates context-aware workspace and tab names for Herdr. | `ai` `bun` `terminal` `typescript` | 23 | 🆕 2026-07-30 |
| [**herdr-flock**](https://github.com/ragamo/herdr-flock)<br><sub>ragamo</sub> | A herdr plugin that visualizes your AI coding agents as pixel-art sheep living on a top-down farm. | `cli` `ratatui` `rust` `tui` | 14 | 2026-07-11 |
| [**herdr-auto-namer**](https://github.com/kakigakki/herdr-auto-namer)<br><sub>kakigakki</sub> | ChatGPT-style auto-naming for herdr: agents get their Claude session title, workspaces get their working directory | `claude-code` `python` | 4 | 2026-07-12 |
| [**herdr-claude-session-title**](https://github.com/bcihanc/herdr-claude-session-title)<br><sub>bcihanc</sub> | Herdr plugin: mirrors the Claude Code session title (/rename or auto summary) into the herdr pane metadata title | `shell` | 3 | 2026-07-11 |
| [**herdr-in-your-face**](https://github.com/JYasha11/herdr-in-your-face)<br><sub>JYasha11</sub> | A giant ASCII face screams at you when you leave an AI agent blocked. Escalates the longer you ignore it. | `javascript` | 3 | 2026-07-10 |
| [**herdr-english-coach**](https://github.com/GranamyrBR/herdr-english-coach)<br><sub>GranamyrBR</sub> | herdr plugin: color-coded English corrections board — your coding agent logs grammar + dev-jargon fixes to a live side pane while you work | `english` `language-learning` `shell` | 2 | 2026-07-06 |
| [**herdr-tab-rename**](https://github.com/lmilojevicc/herdr-tab-rename)<br><sub>lmilojevicc</sub> | Auto-rename each Herdr tab to its focused pane's working-directory name. Manually renamed tabs are left alone. | `go` | 2 | 🆕 2026-07-31 |
| [**herdr-nerd-font-tab-name**](https://github.com/rohankewal/herdr-nerd-font-tab-name)<br><sub>rohankewal</sub> | Nerd Font icons for your herdr tabs — a port of joshmedeski/tmux-nerd-font-window-name | `nerd-fonts` `python` `terminal` `tui` | 2 | 🆕 2026-07-31 |
| [**herdr-powershell-title-sync**](https://github.com/aclima01/herdr-powershell-title-sync)<br><sub>aclima01</sub> | Windows/PowerShell port of window-title-sync: sync the terminal title to the focused herdr session | `powershell` | 1 | 🆕 2026-07-20 |
| [**herdr-git-tab-name**](https://github.com/blurname/herdr-git-tab-name)<br><sub>blurname</sub> | Herdr plugin that renames tabs to the focused pane's Git branch. | `shell` | 1 | 2026-07-06 |
| [**herdr-tab-title-sync**](https://github.com/lucasleon2107/herdr-tab-title-sync)<br><sub>lucasleon2107</sub> | herdr plugin: rename tabs to the AI agent's conversation title | `ai-agents` `claude-code` `terminal` `tmux` `shell` | 1 | 🆕 2026-07-31 |
| [**herdr-ai-tab-name**](https://github.com/ndom91/herdr-ai-tab-name)<br><sub>ndom91</sub> | Auto-rename your Herdr Tabs with local LLMs | `local-llm` `python` | 1 | 🆕 2026-08-01 |
| [**herdr-tab-session-name-sync**](https://github.com/itayo-m/herdr-tab-session-name-sync)<br><sub>itayo-m</sub> | Syncs agent session name with herdr tabs and panes title | `developer-tools` `github-copilot` `terminal` `javascript` | 0 | 🆕 2026-08-02 |
| [**herdr-window-title**](https://github.com/mackt/herdr-window-title)<br><sub>mackt</sub> | Configurable outer-terminal title for herdr: template-driven, session-aware, with live agent state (blocked/done/working) indicator | `rust` | 0 | 🆕 2026-07-31 |
| [**herdr-machine-title**](https://github.com/mikevalstar/herdr-machine-title)<br><sub>mikevalstar</sub> | herdr plugin: pin the outer terminal title to herdr@<hostname> · <workspace> | `shell` | 0 | 2026-07-02 |
| [**herdr-tab-title**](https://github.com/Newt6611/herdr-tab-title)<br><sub>Newt6611</sub> | Herdr Tab Title automatically renames Herdr tabs with clean, workspace-local numbering like 1. Codex, 2. Terminal, using a customizable format. | `rust` | 0 | 2026-07-09 |
| [**tab-blank-number**](https://github.com/riq0h/tab-blank-number)<br><sub>riq0h</sub> | herdr plugin that clears herdr's default numeric tab labels (1, 2, 3…) to blank. | `javascript` | 0 | 🆕 2026-07-19 |
| [**tab-process-name**](https://github.com/riq0h/tab-process-name)<br><sub>riq0h</sub> | herdr plugin that labels each tab with its foreground process name — tmux's automatic-rename behavior, for herdr. | `javascript` | 0 | 🆕 2026-07-19 |
| [**herdr-codex-session-title**](https://github.com/sergeybataev/herdr-codex-session-title)<br><sub>sergeybataev</sub> | Herdr plugin that mirrors Codex chat titles into agent names | `codex` `python` | 0 | 🆕 2026-08-01 |
| [**herdr-agent-session-title**](https://github.com/the-inconvenience-store/herdr-agent-session-title)<br><sub>the-inconvenience-store</sub> | Herdr plugin: mirrors the Claude Code or Codex session title (/rename or auto summary) into the herdr pane metadata title | `python` | 0 | 🆕 2026-07-30 |
| [**herdr-auto-session-title**](https://github.com/zhangzujian/herdr-auto-session-title)<br><sub>zhangzujian</sub> | Generate concise Herdr pane titles and synchronize native Codex thread names. | `javascript` | 0 | 🆕 2026-07-30 |

<details><summary>Also relevant to this purpose</summary>

- [qu8n/herdr-automatic-rename](https://github.com/qu8n/herdr-automatic-rename) — Auto-renaming of herdr tabs in tmux style & 1-9 jump-key numbering for spaces/tabs/agents
- [wyattjoh/herdr-plugin-renamer](https://github.com/wyattjoh/herdr-plugin-renamer) — Renames an auto-generated herdr worktree branch and workspace from the agent's first prompt, via on-device Ap…
- [aarsh21/herdr-tab-title](https://github.com/aarsh21/herdr-tab-title) — Automatic tmux-like tab titles for Herdr
- [suisya-systems/herdr-agent-office](https://github.com/suisya-systems/herdr-agent-office) — Your agent fleet as a pixel-art office - a herdr plugin. See who's working, who's stuck, and jump to them.
- [dev-shimada/herdr-auto-tab-name](https://github.com/dev-shimada/herdr-auto-tab-name) — herdr plugin: automatically name tabs after their current directory
- [filoozom/herdr-title](https://github.com/filoozom/herdr-title) — A Herdr plugin that shows the selected worktree and agent activity in your terminal tab title.
- [go-min/herdr-pane-name](https://github.com/go-min/herdr-pane-name) — Herdr plugin that automatically names panes in your terminal sessions.
- [KazBrekker1/herdr-hasr](https://github.com/KazBrekker1/herdr-hasr) — Hasr (حصر — enumeration, a complete tally) — goto-style popup switcher for herdr: switch, rename, delete & cr…
- [khatriafaz/herdr-plugin-auto-rename](https://github.com/khatriafaz/herdr-plugin-auto-rename) — Automatically rename fresh Herdr workspaces and Git branches from a Pi session's first prompt.
- [maxBRT/herdr-omarchy-theme-sync](https://github.com/maxBRT/herdr-omarchy-theme-sync) — Sync Herdr's UI palette with the active Omarchy theme

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-text"></a>

## Text & URL Grabbing

> I want to grab strings, paths, or URLs shown on screen without touching the mouse

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-pluck**](https://github.com/rmarganti/herdr-pluck)<br><sub>rmarganti</sub> | quickly copy pattern-matched strings from Herdr panes | `rust` | 16 | 🆕 2026-07-30 |
| [**herdr-tiny-fingers**](https://github.com/hotchpotch/herdr-tiny-fingers)<br><sub>hotchpotch</sub> | tmux-fingers style visible-screen copy hints for Herdr | `rust` | 5 | 2026-07-10 |
| [**herdr-fingers**](https://github.com/hitaishi2222/herdr-fingers)<br><sub>hitaishi2222</sub> | Fingers to clipboard: A smart overlay to pick information from a current pane. | `python` | 3 | 2026-07-16 |
| [**herdr-agent-copy-paste-fork**](https://github.com/calebcauthon/herdr-agent-copy-paste-fork)<br><sub>calebcauthon</sub> | fork by simply copying and pasting, or hotkey the fork into a new pane | `claude-code` `codex` `shell` | 2 | 🆕 2026-07-24 |
| [**herdr-s3-clipboard**](https://github.com/jagzmz/herdr-s3-clipboard)<br><sub>jagzmz</sub> | Publish clipboard images as reusable public or presigned URLs from Herdr using S3-compatible storage. | `aws-s3` `clipboard` `cloudflare-r2` `developer-tools` `image-publishing` | 2 | 2026-07-16 |
| [**herdr-copy-search**](https://github.com/qq88976321/herdr-copy-search)<br><sub>qq88976321</sub> | regex and copycat pattern search with extrakto token extraction for herdr scrollback, landing in a tmux-style copy mode (OSC 52) | `copy-mode` `rust` `terminal` `tmux` | 2 | 🆕 2026-07-23 |
| [**herdr-scrollback-capture**](https://github.com/alexjsp/herdr-scrollback-capture)<br><sub>alexjsp</sub> | Herdr plugin that saves the focused pane's scrollback to your Desktop as HTML or text | `shell` | 1 | 2026-06-30 |
| [**herdr-leap**](https://github.com/RooseveltAdvisors/herdr-leap)<br><sub>RooseveltAdvisors</sub> | EasyMotion/leap-style character jump + select-to-copy for the Herdr terminal multiplexer | `easymotion` `rust` `terminal` `tui` | 1 | 🆕 2026-07-24 |
| [**herdr-copy-hints**](https://github.com/rotemb-wond/herdr-copy-hints)<br><sub>rotemb-wond</sub> | tmux-fingers-style keyboard copy hints for Herdr: paths, Git SHAs, URLs, and more | `clipboard` `developer-tools` `keyboard-navigation` `productivity` `terminal` | 1 | 🆕 2026-07-23 |
| [**herdr-paste-image**](https://github.com/ddfonseca/herdr-paste-image)<br><sub>ddfonseca</sub> | Paste clipboard images into herdr panes as file paths — tmux-paste-image, ported to herdr | `shell` | 0 | 🆕 2026-07-30 |

<details><summary>Also relevant to this purpose</summary>

- [iurysza/termscope](https://github.com/iurysza/termscope) — Open files and links already visible on your terminal screen in a split.
- [tanshio/herdr-worktreeinclude](https://github.com/tanshio/herdr-worktreeinclude) — Herdr plugin: copy gitignored files matching .worktreeinclude into newly created worktrees
- [jlimas/herdr-worktree-seed](https://github.com/jlimas/herdr-worktree-seed) — Herdr plugin that seeds new worktrees with copy-on-write node_modules and configurable local dotfiles
- [crexi/herdr-worktree-copy](https://github.com/crexi/herdr-worktree-copy) — Herdr plugin that copies and symlinks worktree-local files from a .worktree-copy manifest
- [Feasy01/herdr-allow](https://github.com/Feasy01/herdr-allow) — herdr plugin: copy gitignored files (.env, secrets, local configs) into every new worktree via a .herdr-allow…
- [eightHundreds/herdr-worktreeinclude](https://github.com/eightHundreds/herdr-worktreeinclude) — Herdr plugin: copy .worktreeinclude-selected gitignored files into new worktrees
- [itayo-m/herdr-tab-session-name-sync](https://github.com/itayo-m/herdr-tab-session-name-sync) — Syncs agent session name with herdr tabs and panes title
- [shadowfax92/herdr-comments](https://github.com/shadowfax92/herdr-comments) — Annotate copied Herdr terminal output, collect per-pane comments, and review them in Neovim.
- [willian/herdr-fzf-url](https://github.com/willian/herdr-fzf-url) — Pick URLs from the focused pane with `fzf`, then open or copy them.
- [zerodice0/herdr-plugin-worktree-bootstrap](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap) — Safely copy ignored local files and run setup commands in new Herdr Git worktrees

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-meta"></a>

## Plugin Management & Authoring

> I want to manage plugins themselves, or build my own

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-plus**](https://github.com/cloudmanic/herdr-plus)<br><sub>cloudmanic</sub> | An extension for herdr, built as a first-class herdr plugin — a collection of tools that make it better: Projects and Quick Actions. | `go` | 191 | 🆕 2026-07-23 |
| [**herdr-lazy**](https://github.com/natori-hrj/herdr-lazy)<br><sub>natori-hrj</sub> | Declarative plugin manager and curated distro for herdr — one list, a real lockfile, a manage pane. | `cli` `lockfile` `plugin-manager` `rust` `terminal` | 12 | 🆕 2026-07-31 |
| [**herdr-plugin-manager**](https://github.com/speardragon/herdr-plugin-manager)<br><sub>speardragon</sub> | Manage herdr plugins from a popup — install, update, enable/disable, uninstall, and browse the herdr-plugin marketplace. Recommended key: prefix+p | `plugin-manager` `tui` `shell` | 6 | 🆕 2026-07-22 |
| [**house-of-herdr**](https://github.com/alasano/house-of-herdr)<br><sub>alasano</sub> | A collection of plugins for Herdr, including Codex Micro: agent status lights and controls on the Work Louder Codex Micro | `codex-micro` `work-louder` `typescript` | 2 | 🆕 2026-07-24 |
| [**herdr-plugins-labs**](https://github.com/hmu332233/herdr-plugins-labs)<br><sub>hmu332233</sub> | Experimental plugins for Herdr — incubated here, graduated to their own repos | `labs` `javascript` | 1 | 2026-07-18 |
| [**herdr-plugin-rust**](https://github.com/Newt6611/herdr-plugin-rust)<br><sub>Newt6611</sub> | A Rust application framework for building Herdr plugins. | `rust` | 1 | 2026-07-09 |

[⬆ Back to purposes](#purposes)

<a id="cat-other"></a>

## Other & Utilities

> Handy things that don't fit any of the categories above

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-plugins-directory**](https://github.com/MIDO-ruby7/herdr-plugins-directory)<br><sub>MIDO-ruby7</sub> | A link collection for finding herdr plugins by what you want to get done. | `python` | 6 | 🆕 2026-08-02 |
| [**wave-tui**](https://github.com/takemo101/wave-tui)<br><sub>takemo101</sub> | Quiet terminal radio for work sessions | `rust` | 4 | 🆕 2026-07-20 |
| [**herdr-plugin-cmux**](https://github.com/lachieh/herdr-plugin-cmux)<br><sub>lachieh</sub> | Mirrors every herdr-managed agent into a cmux sidebar as its own live row, with a status pill and a click-to-jump task line. | `javascript` | 3 | 2026-07-01 |
| [**herdr-commandcode-plugin**](https://github.com/TheMetalStorm/herdr-commandcode-plugin)<br><sub>TheMetalStorm</sub> | Integrates Commandcode into Herdr | `cli` `commandcode` `herdr-integration` `shell` | 2 | 🆕 2026-07-30 |
| [**herdr-edit-windows**](https://github.com/aclima01/herdr-edit-windows)<br><sub>aclima01</sub> | A simple text editor that runs in a herdr pane beside your coding agent — file tree, syntax-highlighted editor, and an uncommitted-diff tab. Windows-only. | `rust` | 1 | 🆕 2026-07-25 |
| [**herdr-stoplight**](https://github.com/BowlOfSoup/herdr-stoplight)<br><sub>BowlOfSoup</sub> | Drive a physical Arduino traffic-light module from the live status of Herdr | `go` | 1 | 2026-07-11 |
| [**herdr-suite-site**](https://github.com/StructuPath/herdr-suite-site)<br><sub>StructuPath</sub> | Landing page for the StructuPath Herdr Suite — herdr.structupath.ai | `herdr-integration` `html` | 1 | 🆕 2026-07-31 |
| [**herdr-freebuff-plugin**](https://github.com/TheMetalStorm/herdr-freebuff-plugin)<br><sub>TheMetalStorm</sub> | Freebuff lifecycle integration plugin for Herdr — reports idle/working/blocked state via file polling and PTY content scraping | `cli` `freebuff` `herdr-integration` `shell` | 1 | 🆕 2026-07-22 |
| [**herdr-panes**](https://github.com/atm028/herdr-panes)<br><sub>atm028</sub> | _(no description)_ | `python` | 0 | 🆕 2026-08-01 |
| [**herdr-attach**](https://github.com/gilvanecesar/herdr-attach)<br><sub>gilvanecesar</sub> | Pick local files from a Herdr popup and send them to the focused coding agent, attaching file context without leaving the terminal. | `javascript` | 0 | 🆕 2026-07-26 |
| [**herdr-llama**](https://github.com/hitaishi2222/herdr-llama)<br><sub>hitaishi2222</sub> | Control your llama-server from your fingertips. | `llama-cpp` `local-ai` `python` | 0 | 2026-07-16 |
| [**herdr-pane-update-timestamps**](https://github.com/johnlindquist/herdr-pane-update-timestamps)<br><sub>johnlindquist</sub> | Herdr plugin for timestamped, scrollable pane output observations | `rust` | 0 | 🆕 2026-07-29 |
| [**hrd**](https://github.com/joshuadavidthomas/hrd)<br><sub>joshuadavidthomas</sub> | Manage your herd of sandboxes and the Herdr sessions running on them | `go` | 0 | 🆕 2026-08-01 |
| [**herdr-status**](https://github.com/jrswab/herdr-status)<br><sub>jrswab</sub> | Ambient machine status pane for Herdr on Linux. | `go` | 0 | 🆕 2026-07-30 |
| [**herdr-laravel-tinker**](https://github.com/lancodev/herdr-laravel-tinker)<br><sub>lancodev</sub> | Split-style Laravel tinker REPL for herdr — editor beside live results, as a pane or popup | `laravel` `tinker` `php` `repl` | 0 | 2026-07-16 |
| [**herdr-new-task**](https://github.com/leonho/herdr-new-task)<br><sub>leonho</sub> | herdr plugin: one keystroke to pick a project dir and launch claude in a new tab, with noun-first tab labels | `python` | 0 | 2026-07-16 |
| [**herdr-plugin-loopreview**](https://github.com/loopkeep/herdr-plugin-loopreview)<br><sub>loopkeep</sub> | Herdr plugin for loopreview | `rust` | 0 | 🆕 2026-07-23 |
| [**herdr-hint**](https://github.com/maedana/herdr-hint)<br><sub>maedana</sub> | Vimium-style hint labels for Herdr — press a key to see labels on tabs and agents, then press a label to jump. | `rust` | 0 | 🆕 2026-07-22 |
| [**herdr-whereami**](https://github.com/maedana/herdr-whereami)<br><sub>maedana</sub> | Herdr plugin that automatically renames tabs to show where you are, e.g. repo-name/branch when inside a git repository. | `rust` | 0 | 🆕 2026-07-22 |
| [**herdr-source-control**](https://github.com/mariotmc/herdr-source-control)<br><sub>mariotmc</sub> | _(no description)_ | `go` | 0 | 🆕 2026-07-31 |
| [**herdr-phin-util**](https://github.com/phin-tech/herdr-phin-util)<br><sub>phin-tech</sub> | Personal Herdr Utils | `bubbletea` `tui` `go` | 0 | 🆕 2026-07-29 |
| [**herdr-traex-integration**](https://github.com/Phoobobo/herdr-traex-integration)<br><sub>Phoobobo</sub> | Herdr plugin that supports traex integration | `shell` | 0 | 2026-07-02 |
| [**herdr-handsfree**](https://github.com/RanolP/herdr-handsfree)<br><sub>RanolP</sub> | Hands-free herdr plugin: voice dictation (whisper.cpp) + webcam gaze mouse for macOS | `rust` | 0 | 🆕 2026-07-30 |
| [**herdr-browser**](https://github.com/redsquiggle/herdr-browser)<br><sub>redsquiggle</sub> | Keep Chromium tab groups aligned with Herdr workspaces | `chromium` `ratatui` `rust` | 0 | 🆕 2026-07-28 |
| [**herdr-jetbrains**](https://github.com/Soemii/herdr-jetbrains)<br><sub>Soemii</sub> | _(no description)_ | `go` | 0 | 🆕 2026-07-29 |
| [**herdr-plugins**](https://github.com/tomaszhanc/herdr-plugins)<br><sub>tomaszhanc</sub> | A personal monorepo of herdr plugins, each living in its own folder with a herdr-plugin.toml manifest and an executable. | — | 0 | 2026-07-16 |

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
