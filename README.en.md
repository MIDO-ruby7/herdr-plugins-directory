# herdr plugins by purpose

[🇯🇵 日本語](README.md) · 🇺🇸 English · [🇨🇳 中文](README.zh.md)

**A link collection for finding [herdr](https://herdr.dev/) plugins by what you want to get done.**

- **994** plugins indexed / last updated **2026-10-28 22:34 UTC** (auto-refreshed every 6 hours)
- Source: GitHub repositories tagged [`herdr-plugin`](https://github.com/topics/herdr-plugin) — the same population as the official [herdr.dev/plugins](https://herdr.dev/plugins/) marketplace
- Categories are auto-inferred from each repo's description and topics. If one looks wrong, fix it with a PR to [`data/overrides.json`](data/overrides.json)
- Install: `herdr plugin install owner/repo` — [official docs](https://herdr.dev/docs/plugins/)

> [!WARNING]
> This is an auto-collected index, not a vetted catalog. Plugins are code that runs directly on your machine, so check the manifest and the commands it runs before installing.

<a id="purposes"></a>

## Browse by purpose

- [**🆕 Recently added**](#cat-new) (220) — Plugins that joined this list in the last 7 days.
- [**Notifications & Alerts**](#cat-notify) (35) — I want to know when an agent finishes or gets stuck waiting for input, even when I'm away from my desk
- [**Mobile & Remote Control**](#cat-remote) (59) — I want to monitor agents from my phone or while away, and just send back approvals
- [**Agent Orchestration**](#cat-agents) (176) — I want to launch, split up, and manage multiple AI agents together
- [**Git Worktrees & Branches**](#cat-worktree) (52) — I want to spin up a worktree for each piece of work, and have the cleanup handled automatically too
- [**Code Review & Diffs**](#cat-review) (43) — I want to read the diff an agent wrote and send comments back on it
- [**GitHub & Issue Trackers**](#cat-forge) (49) — I want to kick off work from an issue or PR, and track PR status
- [**Workspaces & Layouts**](#cat-layout) (33) — When I open a project, I want tabs, panes, and startup commands all set up in one shot
- [**Pane Navigation & Keys**](#cat-navigate) (110) — I want to move and resize between panes and workspaces using the same keys as my editor
- [**File Viewers & Editors**](#cat-files) (65) — I want to open a file tree inside a pane, or keep it in sync with my editor
- [**Tokens & Cost**](#cat-cost) (24) — I want to see how much an agent is spending, and cut down on usage
- [**Monitoring & Dashboards**](#cat-monitor) (76) — I want an at-a-glance overview of agent and machine status
- [**Fuzzy Finders & Palettes**](#cat-finder) (75) — I want to invoke commands or projects even when I only half-remember their names
- [**Automation, Hooks & Schedules**](#cat-automation) (48) — I want a fixed set of steps to run automatically on worktree creation or at a chosen time
- [**Session State & Restore**](#cat-session) (26) — I want to close my work and later resume from exactly the same state
- [**Titles, Naming & Looks**](#cat-naming) (44) — I want tab names and terminal titles to be automatically clear, or want to change how things look
- [**Text & URL Grabbing**](#cat-text) (19) — I want to grab strings, paths, or URLs shown on screen without touching the mouse
- [**Plugin Management & Authoring**](#cat-meta) (7) — I want to manage plugins themselves, or build my own
- [**Other & Utilities**](#cat-other) (53) — Handy things that don't fit any of the categories above

<a id="cat-new"></a>

## 🆕 Recently added

> Plugins that joined this list in the last 7 days.

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**🆕 shepherdr**](https://github.com/eliasstravik/shepherdr)<br><sub>eliasstravik</sub> | Run many coding agents across machines from a phone, tablet or desktop. A herdr plugin. | `typescript` | 912 | 2026-10-28 |
| [**🆕 herdr-claude-usage**](https://github.com/aodanchenko/herdr-claude-usage)<br><sub>aodanchenko</sub> | Global Claude Code plan usage in Herdr: tab-bar summary + popup dashboard. statusLine-powered, multi-account aware. | `claude` `claude-code` `cli` `terminal` `shell` | 3 | 2026-09-01 |
| [**🆕 jumar**](https://github.com/joshbarrington/jumar)<br><sub>joshbarrington</sub> | A fast terminal UI for managing git worktrees | `claude-code-plugin` `cli` `git` `git-worktree` `rust` | 2 | 2026-10-27 |
| [**🆕 herdr-mailbox**](https://github.com/navishachiku/herdr-mailbox)<br><sub>navishachiku</sub> | A mailbox per receiving agent: merged messages and decision questions answered in a side pane | `javascript` | 2 | 2026-10-28 |
| [**🆕 fangyang-le**](https://github.com/RZfive/fangyang-le)<br><sub>RZfive</sub> | herdr skill: fan one task out to N parallel coding agents — Claude Code, OpenCode, Codex, Gemini & 20+. Same-kind spawn, workspace-locked, keep-fold-for-review… | `agent-orchestration` `agent-skill` `ai-workflow` `claude-code` `codex-cli` | 2 | 2026-10-28 |
| [**🆕 herdr-muse**](https://github.com/akshat12/herdr-muse)<br><sub>akshat12</sub> | Herdr integration for Muse Code: idle/working/blocked pane state via lifecycle hooks (no Herdr fork needed) | `ai-agents` `cli` `coding-agents` `muse-code` `terminal` | 1 | 2026-09-12 |
| [**🆕 herdr-wrapped-tabs**](https://github.com/AlexeyKrotkov/herdr-wrapped-tabs)<br><sub>AlexeyKrotkov</sub> | Always-visible wrapped tabs for Herdr | `python` | 1 | 2026-09-24 |
| [**🆕 herdr-unread**](https://github.com/arthurnw/herdr-unread)<br><sub>arthurnw</sub> | Mark Herdr agent sessions unread until revisited or resumed | `python` | 1 | 2026-09-14 |
| [**🆕 asgoto**](https://github.com/asumaran/asgoto)<br><sub>asumaran</sub> | Tree-style switcher across herdr repos, worktrees and panes | `go` | 1 | 2026-10-08 |
| [**🆕 herdr-async-message-relay**](https://github.com/avery20024/herdr-async-message-relay)<br><sub>avery20024</sub> | Durable async messaging for Herdr agents with stable role routing and batched delivery. | `go` | 1 | 2026-10-27 |
| [**🆕 herdr-auto-pull-main**](https://github.com/bring-shrubbery/herdr-auto-pull-main)<br><sub>bring-shrubbery</sub> | _(no description)_ | `shell` | 1 | 2026-10-12 |
| [**🆕 ws.numbered.herdr**](https://github.com/dhananjaylatkar/ws.numbered.herdr)<br><sub>dhananjaylatkar</sub> | Automatically Number The Workspaces in Herdr | `python` | 1 | 2026-10-09 |
| [**🆕 herdr-orch**](https://github.com/ellingtonsp/herdr-orch)<br><sub>ellingtonsp</sub> | Orchestrate coding agents in herdr: mailbox, blocking ask/reply, tasks with dependencies, tracked dispatch, decision gates, verified worker release. CLI: horch. | `ai-agents` `claude-code` `cli` `codex` `go` | 1 | 2026-10-14 |
| [**🆕 herdr-tab-smart-rename-rs**](https://github.com/EmmetZ/herdr-tab-smart-rename-rs)<br><sub>EmmetZ</sub> | _(no description)_ | `rust` | 1 | 2026-08-24 |
| [**🆕 agent-keep-awake**](https://github.com/happyeric77/agent-keep-awake)<br><sub>happyeric77</sub> | Prevent macOS sleep while Herdr agents are working | `javascript` | 1 | 2026-10-26 |
| [**🆕 herdr-emoji-time**](https://github.com/hotnugs/herdr-emoji-time)<br><sub>hotnugs</sub> | Emoji for your Herdr spaces, agents and tabs. Inject some fun into your terminal | `emoji` `terminal` `tui` `python` | 1 | 2026-09-12 |
| [**🆕 herdr-plugin-minimax-code**](https://github.com/jaaacki/herdr-plugin-minimax-code)<br><sub>jaaacki</sub> | Herdr plugin for MiniMax Code | `shell` | 1 | 2026-10-06 |
| [**🆕 hertrees**](https://github.com/janooh37-hue/hertrees)<br><sub>janooh37-hue</sub> | Every worktree, every agent, one popup. A Herdr plugin for git worktrees, PR state and AI agent sessions. | `git-worktree` `tui` `rust` | 1 | 2026-10-28 |
| [**🆕 herdr-open-editor**](https://github.com/jimididit/herdr-open-editor)<br><sub>jimididit</sub> | Fuzzy-pick a file with fzf and open it in your configured editor. | `herd` `text-editor` `tui` `shell` | 1 | 2026-09-03 |
| [**🆕 herdr-tab-title-sync**](https://github.com/lucasleon2107/herdr-tab-title-sync)<br><sub>lucasleon2107</sub> | herdr plugin: rename tabs to the AI agent's conversation title | `ai-agents` `claude-code` `terminal` `tmux` `shell` | 1 | 2026-08-04 |
| [**🆕 subtitle-sanitizer**](https://github.com/luismascotto/subtitle-sanitizer)<br><sub>luismascotto</sub> | Go CLI tool (and WASM too!) to load ASS/SRT subtitles, apply rules to identify and remove text for hearing impaired and other little details. Inspired on Subti… | `go` | 1 | 2026-10-28 |
| [**🆕 herdr-agents-preview**](https://github.com/maedana/herdr-agents-preview)<br><sub>maedana</sub> | Multi-agent terminal preview dashboard for Herdr: all running agents shown at once, with the selected agent taking most of the width. | `rust` | 1 | 2026-08-14 |
| [**🆕 herdr-hint**](https://github.com/maedana/herdr-hint)<br><sub>maedana</sub> | Vimium-style hint labels for Herdr — press a key to see labels on tabs and agents, then press a label to jump. | `rust` | 1 | 2026-08-11 |
| [**🆕 scopefuel**](https://github.com/mgh3326/scopefuel)<br><sub>mgh3326</sub> | Scope-aware headroom gauge for AI coding agent plans — what is actually blocked (account/model/group) and when it refills | `ai-agents` `antigravity` `claude-code` `cli` `codex` | 1 | 2026-10-28 |
| [**🆕 herdr-vimnav**](https://github.com/MykolaSuprun/herdr-vimnav)<br><sub>MykolaSuprun</sub> | Master-detail switcher for herdr — live pane previews, MRU priority sort, sidebar jump codes | `go` | 1 | 2026-10-26 |
| [**🆕 herdr-plugins**](https://github.com/narumiruna/herdr-plugins)<br><sub>narumiruna</sub> | _(no description)_ | `rust` | 1 | 2026-08-08 |
| [**🆕 herdr-standup**](https://github.com/natori-hrj/herdr-standup)<br><sub>natori-hrj</sub> | Agent standup for herdr — a per-agent digest of commits and uncommitted work across your agents' repos. | `ai-agents` `git` `standup` `rust` | 1 | 2026-07-23 |
| [**🆕 herdview**](https://github.com/Orchard-Robotics/herdview)<br><sub>Orchard-Robotics</sub> | View your herd from the web | `html` | 1 | 2026-09-24 |
| [**🆕 herdr-claude-tab-rename**](https://github.com/oronbz/herdr-claude-tab-rename)<br><sub>oronbz</sub> | Herdr plugin: keep each tab named after its Claude Code session title (/rename or auto title) | `shell` | 1 | 2026-10-19 |
| [**🆕 herdr-agent-panel**](https://github.com/patrikbraborec/herdr-agent-panel)<br><sub>patrikbraborec</sub> | herdr plugin: per-agent side panel with context usage, connectors, skills (update/remove via npx skills), sandbox info, and diffs of files the agent changed | `claude-code` `python` | 1 | 2026-10-28 |
| [**🆕 herdr-yank**](https://github.com/pgilad/herdr-yank)<br><sub>pgilad</sub> | Inline keyboard hints for copying visible tokens or opening URLs and files from Herdr panes. | `rust` | 1 | 2026-10-25 |
| [**🆕 herdr-discord**](https://github.com/ralphilius/herdr-discord)<br><sub>ralphilius</sub> | Herdr plugin: Discord as a UI layer — channels are workspaces, threads spawn agents | `discord` `javascript` | 1 | 2026-09-26 |
| [**🆕 herdr-copy-hints**](https://github.com/rotemb-wond/herdr-copy-hints)<br><sub>rotemb-wond</sub> | tmux-fingers-style keyboard copy hints for Herdr: paths, Git SHAs, URLs, and more | `clipboard` `developer-tools` `keyboard-navigation` `productivity` `terminal` | 1 | 2026-07-23 |
| [**🆕 herdr-jira-worktree**](https://github.com/spiritsack/herdr-jira-worktree)<br><sub>spiritsack</sub> | herdr plugin: prompt for a Jira ticket, open/reuse a matching git worktree, and prefill it into a fresh Claude Code session | `shell` | 1 | 2026-08-24 |
| [**🆕 herdr-claude-memories**](https://github.com/StGerman/herdr-claude-memories)<br><sub>StGerman</sub> | Surface and curate Claude Code auto-memory from inside herdr | `claude-code` `terminal` `rust` | 1 | 2026-09-11 |
| [**🆕 herdr-space-tab-metadata**](https://github.com/szrenwei/herdr-space-tab-metadata)<br><sub>szrenwei</sub> | Show each Herdr Space's active tab in the sidebar | `terminal-ui` `python` | 1 | 2026-08-04 |
| [**🆕 recess**](https://github.com/tatsuro-ueda/recess)<br><sub>tatsuro-ueda</sub> | A herdr plugin. AI works, you take recess. Your video plays by itself while the agents work, and pauses to bring you back to the terminal when herdr calls. | `ai-agents` `applescript` `launchd` `macos` `netflix` | 1 | 2026-10-27 |
| [**🆕 herdr-copy-pane-id**](https://github.com/wine-fall/herdr-copy-pane-id)<br><sub>wine-fall</sub> | Herdr plugin: copy the focused pane's id to the clipboard, or show every pane's id on its border | `cli` `terminal` `python` | 1 | 2026-10-27 |
| [**🆕 herdr-fzf-url**](https://github.com/x0d7x/herdr-fzf-url)<br><sub>x0d7x</sub> | Scan herdr terminal panes for URLs and interactively pick one with fzf | `fzf` `go` `url` | 1 | 2026-06-26 |
| [**🆕 herdr-pane-restart**](https://github.com/zap0xfce2/herdr-pane-restart)<br><sub>zap0xfce2</sub> | Run a configured command in named panes on server startup | `python` | 1 | 2026-10-21 |
| [**🆕 herdr-roles**](https://github.com/zeromountain/herdr-roles)<br><sub>zeromountain</sub> | herdr plugin: assign roles to panes, spawn a team from the main pane, and hand work between roles | `python` | 1 | 2026-10-26 |
| [**🆕 herdr-pacer**](https://github.com/amali01/herdr-pacer)<br><sub>amali01</sub> | Herdr plugin: context-window bars under each agent in the sidebar, plus a 5h/weekly usage popup for Claude, Codex and OpenCode | `claude-code` `codex` `opencode` `rust` | 2 | 2026-10-28 |
| [**🆕 herdr-plugin-last**](https://github.com/m4salah/herdr-plugin-last)<br><sub>m4salah</sub> | tmux-style last-tab and last-workspace navigation for Herdr | `rust` | 2 | 2026-07-30 |
| [**🆕 herdr-dictate**](https://github.com/abhishekrana/herdr-dictate)<br><sub>abhishekrana</sub> | Local speech-to-text dictation into the focused Herdr pane | `dictation` `speech-to-text` `voice` `whisper` `rust` | 1 | 2026-10-17 |
| [**🆕 herdr-plugin-jira-pr**](https://github.com/abtris/herdr-plugin-jira-pr)<br><sub>abtris</sub> | Herdr plugin: show the Jira issue behind the current branch's PR, and warn when they disagree | `github-pr` `jira` `shell` | 1 | 2026-08-04 |
| [**🆕 herdr-edit-windows**](https://github.com/aclima01/herdr-edit-windows)<br><sub>aclima01</sub> | A simple text editor that runs in a herdr pane beside your coding agent — file tree, syntax-highlighted editor, and an uncommitted-diff tab. Windows-only. | `rust` | 1 | 2026-07-25 |
| [**🆕 herdr-jump**](https://github.com/agustinvalencia/herdr-jump)<br><sub>agustinvalencia</sub> | Separate overlay pickers for herdr spaces and agents — jump to any workspace or agent, with live status colours | `go` | 1 | 2026-07-24 |
| [**🆕 herdr-tts**](https://github.com/Aktrov/herdr-tts)<br><sub>Aktrov</sub> | Herdr plugin that speaks the selected terminal text aloud in a natural neural voice (Piper) — right-click or a shortcut, with a stop key. | `tts` `python` | 1 | 2026-09-07 |
| [**🆕 herdr-context**](https://github.com/Anthodev/herdr-context)<br><sub>Anthodev</sub> | Project context dock for herdr — file tree with git status and LLM conversation history, always at your agent's side | `git` `jj` `ratatui` `rust` `sidebar` | 1 | 2026-09-30 |
| [**🆕 hird**](https://github.com/aoprisan/hird)<br><sub>aoprisan</sub> | Cross-harness agent work queue and shared assertion memory, backed by one local SQLite database | `ai-agents` `claude-code` `cli` `mcp` `rust` | 1 | 2026-09-29 |
| [**🆕 herdr-stay-awake**](https://github.com/assawalhy/herdr-stay-awake)<br><sub>assawalhy</sub> | Keeps the machine from sleeping while any herdr agent pane is working (Linux, macOS, Windows, and WSL) | `agent-orchestration` `agents` `harness` `linux` `macos` | 1 | 2026-10-07 |
| [**🆕 herdr-prayer-times**](https://github.com/bayoudhi/herdr-prayer-times)<br><sub>bayoudhi</sub> | Next Islamic prayer and countdown in the Herdr sidebar, with a timetable popup and notifications | `rust` | 1 | 2026-08-13 |
| [**🆕 herdr-git-tab-name**](https://github.com/blurname/herdr-git-tab-name)<br><sub>blurname</sub> | Herdr plugin that renames tabs to the focused pane's Git branch. | `shell` | 1 | 2026-07-06 |
| [**🆕 herdr-keep-root**](https://github.com/bonkey/herdr-keep-root)<br><sub>bonkey</sub> | Herdr plugin: keeps a repository's main-checkout workspace open while any of its worktree workspaces is open, so the Spaces panel never flattens a worktree gro… | `shell` | 1 | 2026-09-08 |
| [**🆕 Vincent**](https://github.com/chasereyn/Vincent)<br><sub>chasereyn</sub> | A mouse-first terminal client for reviewing code that AI agents wrote, and fixing it in place | `go` | 1 | 2026-09-03 |
| [**🆕 herdr-jetbrains**](https://github.com/chenyao0910/herdr-jetbrains)<br><sub>chenyao0910</sub> | Open the active Herdr workspace or worktree in Rider, WebStorm, IntelliJ IDEA, or GoLand. | `developer-tools` `git-worktree` `goland` `intellij-idea` `jetbrains` | 1 | 2026-08-30 |
| [**🆕 herdr-continue**](https://github.com/codergeek121/herdr-continue)<br><sub>codergeek121</sub> | Tell your agents to start working automatically | `shell` | 1 | 2026-09-30 |
| [**🆕 herdr-notes**](https://github.com/cyperx84/herdr-notes)<br><sub>cyperx84</sub> | Focused per-workspace Markdown scratch notes for Herdr, built in Go | `bubbletea` `golang` `markdown` `notes` `go` | 1 | 2026-08-16 |
| [**🆕 herdr-tab-jump**](https://github.com/cyperx84/herdr-tab-jump)<br><sub>cyperx84</sub> | Focus herdr tab N by position, from any keybinding — split your number row between tabs and workspaces | `shell` | 1 | 2026-09-01 |
| [**🆕 herdr-last-tab**](https://github.com/dantehemerson/herdr-last-tab)<br><sub>dantehemerson</sub> | Plugin for swapping to the last tab you had focused | `rust` | 1 | 2026-08-12 |
| [**🆕 herdr-review-panel**](https://github.com/Deetss/herdr-review-panel)<br><sub>Deetss</sub> | Herdr plugin: a Review Queue panel for files to look at and commands to run yourself, flagged by Claude Code | `claude-code` `ratatui` `rust` `tui` | 1 | 2026-10-22 |
| [**🆕 herdr-auto-tab-name**](https://github.com/dev-shimada/herdr-auto-tab-name)<br><sub>dev-shimada</sub> | herdr plugin: automatically name tabs after their current directory | `javascript` | 1 | 2026-10-17 |
| [**🆕 herdr-ids**](https://github.com/devicki/herdr-ids)<br><sub>devicki</sub> | Herdr plugin: show pane, tab and workspace ids in the sidebar, and pick a space, tab or pane to type its id into your agent | `shell` | 1 | 2026-10-16 |
| [**🆕 herdr-respawn**](https://github.com/devicki/herdr-respawn)<br><sub>devicki</sub> | Herdr plugin: relaunch lazygit, editors and other allowlisted TUIs in their panes after a server restart or reboot | `shell` | 1 | 2026-10-21 |
| [**🆕 herdr-cast**](https://github.com/DevooKim/herdr-cast)<br><sub>DevooKim</sub> | Spotlight/Raycast-style command palette plugin for Herdr | `command-palette` `go` | 1 | 2026-10-12 |
| [**🆕 herdr-scm**](https://github.com/dkbo/herdr-scm)<br><sub>dkbo</sub> | herdr plugin: a read-only, multi-repo source-control overview panel for the current herdr workspace | `git` `rust` `terminal` `tui` | 1 | 2026-09-10 |
| [**🆕 herdr-fleece**](https://github.com/dmazlum/herdr-fleece)<br><sub>dmazlum</sub> | Frame your agent's last answer in Herdr, then copy, save, or send it. | `typescript` | 1 | 2026-10-15 |
| [**🆕 herdr-context-monitor**](https://github.com/EMRahman/herdr-context-monitor)<br><sub>EMRahman</sub> | A minimal context meter for Herdr: one Python file, no dependencies. Shows each agent's context-window use in the sidebar, for Claude Code, Codex and Antigravi… | `ai-agents` `context-window` `python` | 1 | 2026-10-14 |
| [**🆕 herdr-allow**](https://github.com/Feasy01/herdr-allow)<br><sub>Feasy01</sub> | herdr plugin: copy gitignored files (.env, secrets, local configs) into every new worktree via a .herdr-allow allowlist | `shell` | 1 | 2026-07-02 |
| [**🆕 herdr-sesh**](https://github.com/fedeya/herdr-sesh)<br><sub>fedeya</sub> | sesh-style fzf picker for herdr: jump between workspaces and agents, or open sesh configs, zoxide and fd directories, with live previews and a last-workspace t… | `fzf` `sesh` `zoxide` `shell` | 1 | 2026-10-01 |
| [**🆕 file-editor-viewer**](https://github.com/Freddy-system/file-editor-viewer)<br><sub>Freddy-system</sub> | View and edit files in a herdr pane: Markdown with Mermaid, Graphviz and LaTeX, source code, images. Built-in editor. Written in Rust. | `editor` `file-viewer` `graphviz` `latex` `markdown` | 1 | 2026-10-14 |
| [**🆕 herdr-arcade**](https://github.com/giorgiostokje/herdr-arcade)<br><sub>giorgiostokje</sub> | Seventeen terminal arcade games in a Herdr popup pane that pause themselves when an agent needs attention | `python` | 1 | 2026-10-12 |
| [**🆕 herdr-machine-memory**](https://github.com/gosuwtf/herdr-machine-memory)<br><sub>gosuwtf</sub> | Herdr plugin: tab-bar memory usage for this machine and every connected Herdr machine | `python` | 1 | 2026-10-25 |
| [**🆕 heraldr**](https://github.com/gwenwindflower/heraldr)<br><sub>gwenwindflower</sub> | 🛡️ Reactive label chrome for Herdr tabs, workspaces, and agents | `rust` | 1 | 2026-10-01 |
| [**🆕 herdr-plan-approve**](https://github.com/jerryfane/herdr-plan-approve)<br><sub>jerryfane</sub> | Auto-approve Claude Code plan-mode dialogs in herdr — agents plan, then execute, without a keypress. | `claude-code` `shell` | 1 | 2026-08-25 |
| [**🆕 herdr-plugin-layerfs**](https://github.com/jiangkoumo/herdr-plugin-layerfs)<br><sub>jiangkoumo</sub> | Copy-on-write LayerFS branches as Herdr workspaces, grouped under the repo like worktrees and restored after restart. | `ai-agents` `copy-on-write` `git-worktree` `layerfs` `javascript` | 1 | 2026-10-26 |
| [**🆕 herdr-vista**](https://github.com/kamil-pociot/herdr-vista)<br><sub>kamil-pociot</sub> | Herdr plugin: one key opens vista, a terminal file viewer and editor, on the git repo you're in. Another key reviews what an agent changed on its branch. | `editor` `file-viewer` `rust` | 1 | 2026-10-24 |
| [**🆕 herdr-turn-coordinator**](https://github.com/KarthusLorin/herdr-turn-coordinator)<br><sub>KarthusLorin</sub> | Preserve interactive Herdr agent TUIs without model-driven status polling | `ai-agents` `python` | 1 | 2026-09-18 |
| [**🆕 herdr-agent-smart-rename**](https://github.com/malone-c/herdr-agent-smart-rename)<br><sub>malone-c</sub> | Names each herdr agent session from what it is actually doing | `python` | 1 | 2026-08-14 |
| [**🆕 herdr-revdiff**](https://github.com/mikhail-angelov/herdr-revdiff)<br><sub>mikhail-angelov</sub> | herdr plugin for https://github.com/umputun/revdiff tui | `revdiff` `tui` `shell` | 1 | 2026-09-16 |
| [**🆕 herdr-scratchdock**](https://github.com/mvaios/herdr-scratchdock)<br><sub>mvaios</sub> | Dock a coding agent's scratchpad folder beside it in herdr — live tree, text and image previews, opens itself when the agent starts working. | `claude-code` `tui` `python` | 1 | 2026-09-28 |
| [**🆕 agentflock**](https://github.com/neospark-sol/agentflock)<br><sub>neospark-sol</sub> | AI-coordinated builder and reviewer groups with durable milestone control | `ai-agents` `pair-programming` `typescript` | 1 | 2026-08-21 |
| [**🆕 paneyard**](https://github.com/nicholasjstock/paneyard)<br><sub>nicholasjstock</sub> | Queue coding tasks and run them in parallel as interactive agent sessions you can watch, steer, and resume. | `ruby` | 1 | 2026-10-26 |
| [**🆕 herdr-agent-board**](https://github.com/NoctisHsu/herdr-agent-board)<br><sub>NoctisHsu</sub> | Live task board for coding agents running in Herdr panes | `python` | 1 | 2026-10-14 |
| [**🆕 herdr-caffeinate**](https://github.com/nwarwick/herdr-caffeinate)<br><sub>nwarwick</sub> | Prevent macOS system sleep while Herdr agents are working | `caffeinate` `coding-agents` `macos` `shell` | 1 | 2026-07-29 |
| [**🆕 herdr-touchbar**](https://github.com/omerturhan/herdr-touchbar)<br><sub>omerturhan</sub> | Shows working and blocked herdr agents on the MacBook Touch Bar; tap one to jump straight to its tab. | `ai-agents` `macos` `touchbar` `swift` | 1 | 2026-09-14 |
| [**🆕 herdr-pr-worktree**](https://github.com/poislagarde/herdr-pr-worktree)<br><sub>poislagarde</sub> | Open GitHub pull requests as worktree spaces in Herdr, reusing existing checkouts. | `git-worktree` `python` | 1 | 2026-10-14 |
| [**🆕 herdr-automations**](https://github.com/ram4-dev/herdr-automations)<br><sub>ram4-dev</sub> | Declarative cron, interval, and event automations for Herdr | `automation` `bun` `typescript` | 1 | 2026-08-13 |
| [**🆕 herdr-pane-reopen**](https://github.com/rchougule/herdr-pane-reopen)<br><sub>rchougule</sub> | herdr plugin: undo close — reopen the last closed pane, tab or workspace in place and resume its agent | `rust` | 1 | 2026-09-17 |
| [**🆕 herdr-readpending**](https://github.com/rcosteira79/herdr-readpending)<br><sub>rcosteira79</sub> | Mark agents you haven't finished reading. Numbered badge ($read) + a reorderable list pane. Auto-clears when you focus the agent. | `python` | 1 | 2026-09-15 |
| [**🆕 herdr-pomodoro**](https://github.com/sazardev/herdr-pomodoro)<br><sub>sazardev</sub> | Minimal, elegant, theme-adaptive Pomodoro timer plugin for Herdr | `rust` | 1 | 2026-09-08 |
| [**🆕 herdr-agent-prs**](https://github.com/sebassdc/herdr-agent-prs)<br><sub>sebassdc</sub> | A cross-repo PR viewer for coding agents in Herdr. See every pull request an agent opened or pushed to, in any repo, with live CI, review and merge state. | `ratatui` `rust` | 1 | 2026-09-26 |
| [**🆕 herdr-scratch**](https://github.com/shadowfax92/herdr-scratch)<br><sub>shadowfax92</sub> | Persistent per-pane Herdr scratch popups backed by private tmux sessions. | `neovim` `productivity` `rust` `terminal` `tmux` | 1 | 2026-10-22 |
| [**🆕 goat-herdr**](https://github.com/shindakun/goat-herdr)<br><sub>shindakun</sub> | 🐐 Herdr plugin: alerts to Telegram, Slack, ntfy, Pushover/bullet or any webhook when an agent needs you | `ntfy` `rust` `slack` `telegram` `webhook` | 1 | 2026-09-24 |
| [**🆕 mimo-code-herdr**](https://github.com/ShinoharaHaruna/mimo-code-herdr)<br><sub>ShinoharaHaruna</sub> | MiMo Code <-> herdr custom-agent bridge: lifecycle state in the sidebar, crash-proof exit cleanup, one-command spawn | `ai-agents` `cli` `coding-agent` `mimo` `mimocode` | 1 | 2026-10-04 |
| [**🆕 herdr-git-graph**](https://github.com/sjlee06/herdr-git-graph)<br><sub>sjlee06</sub> | Interactive Git branch and commit graph for Herdr. Rust + Ratatui, smooth curves, search, and diffs. | `git` `git-graph` `ratatui` `rust` `terminal` | 1 | 2026-10-27 |
| [**🆕 herdr-pinned-workspaces**](https://github.com/skydiver/herdr-pinned-workspaces)<br><sub>skydiver</sub> | A Herdr plugin that keeps declared workspaces alive. | `terminal` `tui` `workspaces` `python` | 1 | 2026-09-21 |
| [**🆕 herdr-agent-metrics**](https://github.com/szrenwei/herdr-agent-metrics)<br><sub>szrenwei</sub> | Lightweight Herdr context and session usage metrics for Claude Code, Codex, and TraeX. | `claude-code` `openai-codex` `traex` `python` | 1 | 2026-08-04 |
| [**🆕 herdr-pr-modal**](https://github.com/Tarektouati/herdr-pr-modal)<br><sub>Tarektouati</sub> | Open any pull request in its own worktree, straight from a Herdr | `rust` | 1 | 2026-09-24 |
| [**🆕 herdeck**](https://github.com/thefahien/herdeck)<br><sub>thefahien</sub> | Turn commands, processes, health checks, JSON APIs and Prometheus queries into live tabs in a herdr pane | `curses` `monitoring` `prometheus` `python` `terminal-dashboard` | 1 | 2026-10-23 |
| [**🆕 herdr-claude-tab-title**](https://github.com/tmn73/herdr-claude-tab-title)<br><sub>tmn73</sub> | Mirrors each Claude Code session title, and its agent state, onto its Herdr tab | `claude-code` `tabs` `terminal` `typescript` | 1 | 2026-09-07 |
| [**🆕 herdr-customize**](https://github.com/wapenshaw/herdr-customize)<br><sub>wapenshaw</sub> | Customize Herdr's settings and key bindings in one popup, with optional Themes and Plugins pages. Linux, macOS and Windows. | `rust` | 1 | 2026-10-26 |
| [**🆕 herdr-balance-panes**](https://github.com/willfish/herdr-balance-panes)<br><sub>willfish</sub> | Evenly size panes in the current Herdr tab (tmux select-layout -E) | `rust` `terminal` `tmux` | 1 | 2026-08-05 |
| [**🆕 herdr-derby**](https://github.com/xzedx/herdr-derby)<br><sub>xzedx</sub> | Send one prompt to every coding agent in the current Herdr tab and watch them race: a popup to type in, live timers and finishing ranks on the pane borders. | `coding-agents` `rust` | 1 | 2026-10-23 |
| [**🆕 herdr-pr**](https://github.com/yelsed/herdr-pr)<br><sub>yelsed</sub> | A Todo of the pull requests waiting on you, in a herdr pane. Reads everything through the gh CLI. | `rust` | 1 | 2026-08-29 |
| [**🆕 herdr-space-groups**](https://github.com/yojahny55/herdr-space-groups)<br><sub>yojahny55</sub> | Herdr plugin: group Spaces into named, colored groups — picker popup (mouse + keyboard), sidebar group headers, automatic ordering | `javascript` | 1 | 2026-08-29 |
| [**🆕 herdr-focus**](https://github.com/Zeus-Deus/herdr-focus)<br><sub>Zeus-Deus</sub> | herdr plugin: an attention layer for the agent sidebar - clear titles, Needs you / Working / Done, unread and settle triage, and a watch eye for background PR… | `python` | 1 | 2026-10-25 |
| [**🆕 visor**](https://github.com/oronbz/visor)<br><sub>oronbz</sub> | A terminal dashboard your coding agent sets up: PRs, Jira, calendar and anything else, with Plugins in any language. | `ai-agents` `bubbletea` `claude-code` `cli` `dashboard` | 12 | 2026-10-28 |
| [**🆕 herduck**](https://github.com/wenhanweime/herduck)<br><sub>wenhanweime</sub> | Agent window management, project visibility, and a global conversation library. Built on Herdr for people and Agents. | `agent-memory` `ai-agents` `claude-code` `codex` `coding-agents` | 9 | 2026-10-28 |
| [**🆕 quicktui-herdr**](https://github.com/quicktui/quicktui-herdr)<br><sub>quicktui</sub> | Use Herdr from your iPhone or Android phone with QuickTUI: native mobile app, one-step install, QR pairing, and an optional end-to-end encrypted relay. | `shell` | 8 | 2026-10-26 |
| [**🆕 claude-deck**](https://github.com/bigsan/claude-deck)<br><sub>bigsan</sub> | Watch Claude Code sessions: scratchpad files, tasks and every tool call, standalone or as a herdr plugin | `claude-code` `ratatui` `tui` `rust` | 4 | 2026-10-28 |
| [**🆕 herdr-kata**](https://github.com/salmonumbrella/herdr-kata)<br><sub>salmonumbrella</sub> | Runs Kata cron jobs and workflows as Herdr agents | `kata` `go` | 2 | 2026-10-25 |
| [**🆕 herdr-todos-windows**](https://github.com/aclima01/herdr-todos-windows)<br><sub>aclima01</sub> | Live panel mirroring a herdr agent's task list (TaskCreate/TaskUpdate) so you can follow its plan | `powershell` | 1 | 2026-07-22 |
| [**🆕 yeet**](https://github.com/adriankarlen/yeet)<br><sub>adriankarlen</sub> | a minimal sesh style picker inside herdr | `sesh` `session-management` `yeet` `go` | 1 | 2026-09-25 |
| [**🆕 herdr-agent-tab-titles**](https://github.com/ajaykumarMohite/herdr-agent-tab-titles)<br><sub>ajaykumarMohite</sub> | Renames each Herdr tab to the task its coding agent is working on | `claude-code` `developer-tools` `terminal` `python` | 1 | 2026-09-17 |
| [**🆕 herdr-scrollback-capture**](https://github.com/alexjsp/herdr-scrollback-capture)<br><sub>alexjsp</sub> | Herdr plugin that saves the focused pane's scrollback to your Desktop as HTML or text | `shell` | 1 | 2026-06-30 |
| [**🆕 herdr-restart-agents**](https://github.com/aliaksandr-haurylau-godel/herdr-restart-agents)<br><sub>aliaksandr-haurylau-godel</sub> | Herdr plugin: restart coding agents in their panes and resume the same session | `python` | 1 | 2026-10-05 |
| [**🆕 herdr-workspace-prs**](https://github.com/andrewbrannan/herdr-workspace-prs)<br><sub>andrewbrannan</sub> | Herdr plugin for tracking workspace GitHub pull requests | `typescript` | 1 | 2026-09-04 |
| [**🆕 unblock**](https://github.com/aneym/unblock)<br><sub>aneym</sub> | One queue for everything your agents need from you. Blockers need an action, grills need a judgement; secrets never enter the model's context. | `agents` `human-in-the-loop` `mcp` `javascript` | 1 | 2026-10-28 |
| [**🆕 herdr-quotabar**](https://github.com/ArnaudRinquin/herdr-quotabar)<br><sub>ArnaudRinquin</sub> | Claude plan quotas (5h / 7d / per-model) as one compact line in the Herdr tab bar. Provider-pluggable. | `claude-code` `python` | 1 | 2026-09-08 |
| [**🆕 shep**](https://github.com/ArtMoreno/shep)<br><sub>ArtMoreno</sub> | Your Herdr terminals on your phone. Desktop setup, private pairing, themes, and QuotaDeck. | `pwa` `terminal` `javascript` | 1 | 2026-09-28 |
| [**🆕 herdr-glance**](https://github.com/arvmaan/herdr-glance)<br><sub>arvmaan</sub> | desktop widget to view the status of your agents | `rust` | 1 | 2026-09-08 |
| [**🆕 herdr-ssh-config-dash**](https://github.com/bearylabs/herdr-ssh-config-dash)<br><sub>bearylabs</sub> | A Herdr plugin for managing machines from literal hosts in ~/.ssh/config. | `typescript` | 1 | 2026-10-02 |
| [**🆕 herdr-corral**](https://github.com/bfreed/herdr-corral)<br><sub>bfreed</sub> | Herd your Git worktrees in Herdr: env files, dependencies, agent/shell/server tabs, and merge-safe cleanup. A workmux replacement for Herdr. | `git-worktree` `workmux` `python` | 1 | 2026-10-01 |
| [**🆕 herdr-stoplight**](https://github.com/BowlOfSoup/herdr-stoplight)<br><sub>BowlOfSoup</sub> | Drive a physical Arduino traffic-light module from the live status of Herdr | `go` | 1 | 2026-07-11 |
| [**🆕 archify-herdr-plugin**](https://github.com/bozoinc/archify-herdr-plugin)<br><sub>bozoinc</sub> | Herdr plugin derived from archify DESIGN.md (verified-source). M6 adapter directive-derived. | `html` | 1 | 2026-10-19 |
| [**🆕 herdr-agents-sidebar**](https://github.com/C0R0NELL/herdr-agents-sidebar)<br><sub>C0R0NELL</sub> | Customize Herdr’s native agent sidebar with Grouped and Priority layouts, flexible views, and per-mode colors. | `python` | 1 | 2026-10-12 |
| [**🆕 herdr-cheatsheet**](https://github.com/ChristianDeckert/herdr-cheatsheet)<br><sub>ChristianDeckert</sub> | Clickable herdr side panel: just recipes, herdr and terminal keybindings | `cheatsheet` `just` `zsh` `shell` | 1 | 2026-10-27 |
| [**🆕 herdr-spotify**](https://github.com/DeepRuparel/herdr-spotify)<br><sub>DeepRuparel</sub> | Spotify for Herdr — Go, zero-setup local controls + gated search/queue/save via PKCE | `spotify` `go` | 1 | 2026-08-28 |
| [**🆕 herdr-handoff**](https://github.com/devops-fj/herdr-handoff)<br><sub>devops-fj</sub> | Preview and securely hand off local working context between Herdr coding agents. | `ai-agents` `coding-agents` `go` | 1 | 2026-08-21 |
| [**🆕 herdr-pane-mover**](https://github.com/dimitri4d/herdr-pane-mover)<br><sub>dimitri4d</sub> | Move running Herdr panes between tabs and workspaces with a keyboard and mouse friendly destination picker. | `go` | 1 | 2026-09-13 |
| [**🆕 herdr-plugin-omp-state**](https://github.com/dk3775/herdr-plugin-omp-state)<br><sub>dk3775</sub> | Report omp agent state to Herdr from its terminal title, for panes the official integration does not cover | `coding-agents` `omp` `python` | 1 | 2026-09-24 |
| [**🆕 herdr-agents**](https://github.com/dleen/herdr-agents)<br><sub>dleen</sub> | An fzf agent picker for herdr: every agent pane, worst-first, with a session preview and one-key launching. | `coding-agents` `fzf` `python` `terminal` | 1 | 2026-08-20 |
| [**🆕 herdr-huddle**](https://github.com/DnzzL/herdr-huddle)<br><sub>DnzzL</sub> | Live Share for your coding agent: open a Herdr pane to teammates — they watch it live, steer it, and a GitHub pull request keeps the record. | `ai-agents` `claude-code` `coding-agents` `collaboration` `go` | 1 | 2026-10-08 |
| [**🆕 atd-herdr-command-palette**](https://github.com/doanhthong/atd-herdr-command-palette)<br><sub>doanhthong</sub> | Every Herdr action one keystroke away. Jump between coding agents, spin up agent tabs, and run project commands from a single palette. | `javascript` | 1 | 2026-10-08 |
| [**🆕 herdr-cache-hit**](https://github.com/e-kotov/herdr-cache-hit)<br><sub>e-kotov</sub> | Prompt-cache HUD tokens, real-time expiration alerts, and dynamic agent sorting for Herdr | `agentic-ai` `antigravity` `cache` `claude-code` `cli` | 1 | 2026-10-27 |
| [**🆕 herdr-drop**](https://github.com/ecylmz/herdr-drop)<br><sub>ecylmz</sub> | Drag a file onto a Herdr pane and it lands in that pane's directory, through the ssh session you already have | `file-transfer` `ssh` `terminal` `python` | 1 | 2026-09-18 |
| [**🆕 herdr-swipe-linux**](https://github.com/enisbu/herdr-swipe-linux)<br><sub>enisbu</sub> | Trackpad gestures for Herdr on Linux: swipe between panes, tabs and spaces, tap to jump to the waiting agent | `evdev` `gestures` `gnome` `hyprland` `linux` | 1 | 2026-09-02 |
| [**🆕 agent-watch**](https://github.com/gabrielmarcano/agent-watch)<br><sub>gabrielmarcano</sub> | Approve, answer and prompt your terminal coding agents (Claude Code, OpenCode, Antigravity…) from a Wear OS watch. Built on herdr, with a Go host bridge and a… | `ai-agents` `android` `claude-code` `coding-agents` `golang` | 1 | 2026-10-27 |
| [**🆕 herdr-plugin-pane-id-namer**](https://github.com/gcgo/herdr-plugin-pane-id-namer)<br><sub>gcgo</sub> | Automatically generate an agent name and display it in the terminal. | `shell` | 1 | 2026-09-05 |
| [**🆕 LunaCrab**](https://github.com/GranamyrBR/LunaCrab)<br><sub>GranamyrBR</sub> | Reserved for a separate project | `agents` `developer-tools` `multi-agent` `observability` `rust` | 1 | 2026-08-10 |
| [**🆕 herdr-random-sounds**](https://github.com/gridness/herdr-random-sounds)<br><sub>gridness</sub> | play random notification sounds per agent status in herdr on macOS | `herdr-integration` `macos` `notification` `notifications` `python` | 1 | 2026-08-23 |
| [**🆕 herdr-mistral-vibe**](https://github.com/guiand888/herdr-mistral-vibe)<br><sub>guiand888</sub> | Herdr plugin that starts Mistral Vibe sessions in Herdr panes | `shell` | 1 | 2026-10-12 |
| [**🆕 herdr-plugin-done-timer**](https://github.com/hanjm93/herdr-plugin-done-timer)<br><sub>hanjm93</sub> | A prompt-cache countdown for every AI agent on herdr's agents panel, read from each agent's transcript. | `ai-agents` `claude-code` `shell` | 1 | 2026-09-15 |
| [**🆕 herdr-web**](https://github.com/harshagowda/herdr-web)<br><sub>harshagowda</sub> | A real browser tab for herdr on macOS, drivable over CDP | `cmux` `herder-webui` `javascript` | 1 | 2026-10-19 |
| [**🆕 the-cat-concerto**](https://github.com/Herdanis/the-cat-concerto)<br><sub>Herdanis</sub> | Orchestrator prompt + worker contract for coding agents, driven by herdr | `claude-code` `codex` `coding-agent` `gemini-cli` `opencode` | 1 | 2026-10-26 |
| [**🆕 herdr-glab**](https://github.com/hlouis/herdr-glab)<br><sub>hlouis</sub> | Herdr plugin for GitLab merge requests: a grouped MR panel, worktree checkout, tuicr review, sidebar status, and a tab bar count. All access through the glab C… | `cli` `gitlab` `golang` `go` | 1 | 2026-09-19 |
| [**🆕 herdr-new-workspace**](https://github.com/Hon-Lu/herdr-new-workspace)<br><sub>Hon-Lu</sub> | Herdr plugin for opening a new workspace in any folder: type a path with fuzzy completion, or search your projects by name. | `terminal` `tmux-alternative` `javascript` | 1 | 2026-10-07 |
| [**🆕 herdr-palette**](https://github.com/iancharters/herdr-palette)<br><sub>iancharters</sub> | Fuzzy command palette for Herdr — core commands plus auto-discovered plugin actions, run where you can see them. Fast, keyboard-first, terminal-native. | `go` | 1 | 2026-09-25 |
| [**🆕 nexus**](https://github.com/IniZio/nexus)<br><sub>IniZio</sub> | Herdr plugin for running worktree in Cloud-Hypervisor sandboxes, with mem/cpu/disk hotplug and auto port-forwarding | `cloud-hypervisor` `go` | 1 | 2026-10-04 |
| [**🆕 herdr-tunnel**](https://github.com/ivorpad/herdr-tunnel)<br><sub>ivorpad</sub> | Herdr plugin: put a local port on the public internet, copy the URL, take it down again | `tui` `python` | 1 | 2026-08-27 |
| [**🆕 herdr-turbo-palette**](https://github.com/jackfrancisdalton/herdr-turbo-palette)<br><sub>jackfrancisdalton</sub> | Fuzzy-find any Herdr space, tab, agent or pane and jump straight to it. | `python` | 1 | 2026-08-22 |
| [**🆕 herdr-keys**](https://github.com/JacquesvanWyk/herdr-keys)<br><sub>JacquesvanWyk</sub> | Fuzzy-searchable keybinding cheatsheet for herdr (packs, discovery, personal overrides) | `shell` | 1 | 2026-07-12 |
| [**🆕 herdr-tiling**](https://github.com/jaeheonji/herdr-tiling)<br><sub>jaeheonji</sub> | Hyprland-style pane movement and tmux-style layouts for Herdr | `rust` | 1 | 2026-10-28 |
| [**🆕 tether-browser**](https://github.com/jeffhuen/tether-browser)<br><sub>jeffhuen</sub> | Remote-to-local browser bridge for AI coding agents. Your agent runs on the server; Chrome stays on your workstation, with your passkeys, password manager, and… | `go` | 1 | 2026-10-06 |
| [**🆕 herdr-ntfy-notify**](https://github.com/jjuraszek/herdr-ntfy-notify)<br><sub>jjuraszek</sub> | Herdr plugin: ntfy push notification to your phone when an agent goes blocked or done | `ntfy` `javascript` | 1 | 2026-09-13 |
| [**🆕 herdr-spaces-pr-status**](https://github.com/jmarbutt/herdr-spaces-pr-status)<br><sub>jmarbutt</sub> | Show GitHub pull request status on herdr spaces, with a Conductor-style PR board | `github-pull-request` `javascript` | 1 | 2026-09-09 |
| [**🆕 herdr-glab-status**](https://github.com/jpwallace22/herdr-glab-status)<br><sub>jpwallace22</sub> | A [Herdr](https://herdr.dev) plugin that shows each workspace's GitLab merge request status in the spaces sidebar, as a $mr token on the workspace row: | `typescript` | 1 | 2026-09-09 |
| [**🆕 herdr-slack-notify**](https://github.com/juninaba/herdr-slack-notify)<br><sub>juninaba</sub> | Send Slack notifications when Herdr agents finish or get blocked. | `javascript` | 1 | 2026-07-07 |
| [**🆕 herdr-plugin-switcher**](https://github.com/KadenThomp36/herdr-plugin-switcher)<br><sub>KadenThomp36</sub> | Hold Ctrl, tap Tab to cycle herdr panes MRU-style. Arc/Zen-style pane switcher for herdr on macOS. | `swift` | 1 | 2026-08-21 |
| [**🆕 herdr-claude-agents**](https://github.com/kamil-pociot/herdr-claude-agents)<br><sub>kamil-pociot</sub> | Herdr plugin: Claude Code background sessions as Herdr agents — one tab each in its project's space, live state and notifications. | `claude-code` `rust` | 1 | 2026-10-24 |
| [**🆕 herdr-jira-workspace**](https://github.com/khanal-samir/herdr-jira-workspace)<br><sub>khanal-samir</sub> | Native Jira Kanban, calendar worklogs, comments and attachments inside Herdr | `jira` `kanban` `ratatui` `rust` | 1 | 2026-10-10 |
| [**🆕 herdr-nvim-aware**](https://github.com/KoalaVim/herdr-nvim-aware)<br><sub>KoalaVim</sub> | Nvim-aware keybindings for herdr: navigation, splits, close, zoom | `rust` | 1 | 2026-08-20 |
| [**🆕 shop-plugin**](https://github.com/kyrosle/shop-plugin)<br><sub>kyrosle</sub> | A visible multi-agent workstation for Pi + Herdr, with configurable Lead/Worker models, file-based task handoffs, and explicit review. Local alpha. | `coding-agent` `developer-tools` `human-in-the-loop` `multi-agent` `pi-coding-agent` | 1 | 2026-09-27 |
| [**🆕 herdr-wtm**](https://github.com/LucasPcq/herdr-wtm)<br><sub>LucasPcq</sub> | herdr plugin for wtm (early preview): run your worktree commands from a herdr popup and keep workspaces in sync. One branch, one worktree, one isolated dev sta… | `developer-tools` `git-worktree` `go` `worktree` `wtm` | 1 | 2026-10-04 |
| [**🆕 herdr-services**](https://github.com/lucidstack/herdr-services)<br><sub>lucidstack</sub> | Plugin to track services running inside herdr workspaces | `rust` | 1 | 2026-09-16 |
| [**🆕 herdr-pane-labels**](https://github.com/macd2/herdr-pane-labels)<br><sub>macd2</sub> | Shows each pane's current directory, agent session title, and whether it's local or inside ssh, right in the herdr pane border. | `shell` | 1 | 2026-10-11 |
| [**🆕 herdr-standup**](https://github.com/mcc0x/herdr-standup)<br><sub>mcc0x</sub> | A digest of what your agents actually did. One command, one readable summary of every Herdr workspace over a time window — commits, change volume, branch, and… | `git` `rust` `standup` `terminal` | 1 | 2026-10-16 |
| [**🆕 herdr-sidekick**](https://github.com/minhtran3124/herdr-sidekick)<br><sub>minhtran3124</sub> | herdr plugin: side panels for coding agents — worktrees, changed files with diffs, and Claude Code subagents | `rust` | 1 | 2026-10-28 |
| [**🆕 mo-herdr**](https://github.com/momentohq/mo-herdr)<br><sub>momentohq</sub> | Run mo inside herdr panes: session restore after a herdr restart, a launch action, and SIGKILL cleanup | `python` | 1 | 2026-09-02 |
| [**🆕 ZimMux**](https://github.com/Mr-Destroyer/ZimMux)<br><sub>Mr-Destroyer</sub> | ZimMux: a one-file tmux theme in herdr Ink style. Lavender focus borders, quiet status bar, prefix-free Alt bindings, one-command install with backups. No plug… | `agent` `agent-framework` `agent-workflows` `agentic-ai` `agentic-workflow` | 1 | 2026-09-15 |
| [**🆕 herdr-web**](https://github.com/mttzzz/herdr-web)<br><sub>mttzzz</sub> | herdr in your browser: a 1:1 mirror of the herdr TUI for your phone, tablet or another computer (herdr plugin) | `bun` `mobile` `terminal` `websocket` `xterm` | 1 | 2026-10-07 |
| [**🆕 herdr-session-sync**](https://github.com/nengqi/herdr-session-sync)<br><sub>nengqi</sub> | Auto-sync Claude Code, Codex & Agent session names across Herdr pane labels, PTY window titles, and mobile companion apps (Heeler) | `agent` `claude-code` `codex` `heeler` `terminal-multiplexer` | 1 | 2026-10-26 |
| [**🆕 github-issue-herdr-plugin**](https://github.com/nyanyaon/github-issue-herdr-plugin)<br><sub>nyanyaon</sub> | Claude Code plugin for herding GitHub issues | `rust` | 1 | 2026-07-27 |
| [**🆕 herdr-spawn**](https://github.com/nytafar/herdr-spawn)<br><sub>nytafar</sub> | One MCP tool that hands a prompt from a chat to a real Claude Code session on one of your hosts, with Remote Control on. | `python` | 1 | 2026-08-21 |
| [**🆕 herdr-bar**](https://github.com/openalon-org/herdr-bar)<br><sub>openalon-org</sub> | macOS menu bar for Herdr. Live agent counts. One click to the pane that needs you. | `herdr-notify` `menu-bar` `menu-bar-app` `notification` `notify` | 1 | 2026-09-18 |
| [**🆕 herdr-plugins**](https://github.com/paniolo-ai/herdr-plugins)<br><sub>paniolo-ai</sub> | Paniolo plugins for Herdr: live status footers for coding agents and direct Obsidian links. | `claude-code` `codex` `coding-agents` `cursor` `devin` | 1 | 2026-10-21 |
| [**🆕 mission-control-capcom**](https://github.com/philals/mission-control-capcom)<br><sub>philals</sub> | Mission control for story-driven work: local kanban boards, Claude Code skills and a live terminal board for tasks, draft PRs, CI and manual runs | `claude-code` `kanban` `rust` `tui` | 1 | 2026-10-27 |
| [**🆕 herdr-tasks**](https://github.com/pinkpixel-dev/herdr-tasks)<br><sub>pinkpixel-dev</sub> | A Herdr plugin that puts your agent's task list in a split pane beside it, checked off as the agent works. | `ai` `ai-agents` `antigravity` `claude-code` `cli` | 1 | 2026-09-19 |
| [**🆕 herdr-api-client**](https://github.com/playsthisgame/herdr-api-client)<br><sub>playsthisgame</sub> | HTTP/REST API client in a herdr split pane or tab — browse, run and test requests without leaving the terminal | `http-client` `rest-client` `tui` `shell` | 1 | 2026-08-08 |
| [**🆕 herdr-cosyra**](https://github.com/portablcorp/herdr-cosyra)<br><sub>portablcorp</sub> | Open your Cosyra cloud workspace in Herdr: one tab per Cosyra terminal, attached over SSH. | `shell` | 1 | 2026-10-09 |
| [**🆕 herdr-github-metadata**](https://github.com/ralphilius/herdr-github-metadata)<br><sub>ralphilius</sub> | Herdr plugin: GitHub metadata for the sidebar — the PR each agent is working on | `github` `python` | 1 | 2026-09-29 |
| [**🆕 herdr-devin-board**](https://github.com/rigelstpierre/herdr-devin-board)<br><sub>rigelstpierre</sub> | herdr plugin: your Devin Cloud sessions with live PR, CI, and review status | `devin` `go` | 1 | 2026-10-02 |
| [**🆕 herdr-tab-flow**](https://github.com/RodrigoEspinosa/herdr-tab-flow)<br><sub>RodrigoEspinosa</sub> | Next/previous tab navigation for herdr that flows across spaces — past the last tab, continue into the next space. | `shell` | 1 | 2026-10-01 |
| [**🆕 herdr-edge-nav**](https://github.com/sebcbi1/herdr-edge-nav)<br><sub>sebcbi1</sub> | Herdr plugin for directional pane navigation/resizing that crosses tabs and workspaces at pane edges, with seamless Neovim split awareness. | `lua` | 1 | 2026-08-12 |
| [**🆕 herdr-talon**](https://github.com/shadowfax92/herdr-talon)<br><sub>shadowfax92</sub> | Spatial keyboard hints for visible Herdr terminal targets. | `keyboard-navigation` `productivity` `rust` `terminal` `tmux-fingers` | 1 | 2026-10-13 |
| [**🆕 herdr-llm-lint**](https://github.com/shindakun/herdr-llm-lint)<br><sub>shindakun</sub> | Lints CLAUDE.md, AGENTS.md, and agent instruction files for stale paths, commands, facts, and drift | `agents-md` `ai-agents` `claude-code` `claude-md` `cli` | 1 | 2026-09-21 |
| [**🆕 herdr-nav-plus**](https://github.com/shoaibkhanz/herdr-nav-plus)<br><sub>shoaibkhanz</sub> | Ctrl+h/j/k/l navigation that flows past herdr panes into workspaces — vim-aware, wraps at both ends | `javascript` | 1 | 2026-07-18 |
| [**🆕 agent-letterbox-herdr**](https://github.com/SimonMallas/agent-letterbox-herdr)<br><sub>SimonMallas</sub> | Agent-to-agent mail with Queryable Envelope Memory (QEM) for AI coding teams in Herdr: durable letters, a doorbell, and one read-only query over the team's sha… | `agent-communication` `agent-coordination` `agent-letterbox` `agent-memory` `agent-orchestration` | 1 | 2026-10-26 |
| [**🆕 herdr-atuin-plugin**](https://github.com/smanickam01/herdr-atuin-plugin)<br><sub>smanickam01</sub> | Atuin shell history search in a herdr popup — press prefix+a, Enter to run or Tab to edit. Binds itself on install. | `atuin` `macos` `shell-history` `terminal` `zsh` | 1 | 2026-08-17 |
| [**🆕 herdr-worktrees**](https://github.com/SpaceK33z/herdr-worktrees)<br><sub>SpaceK33z</sub> | Switch, create, and remove Git worktrees from a Herdr popup | `rust` | 1 | 2026-09-17 |
| [**🆕 herdr-awake**](https://github.com/susomejias/herdr-awake)<br><sub>susomejias</sub> | Herdr plugin: keep the machine awake while Herdr agents are busy | `shell` | 1 | 2026-08-26 |
| [**🆕 herdr-orc**](https://github.com/tamdogood/herdr-orc)<br><sub>tamdogood</sub> | A minimal, profile-driven custom orchestrator for Herdr | `ai-agents` `multi-agent` `orchestrator` `javascript` | 1 | 2026-08-11 |
| [**🆕 herdr-model-lanes**](https://github.com/terry-li-hm/herdr-model-lanes)<br><sub>terry-li-hm</sub> | Herdr plugin: Codex, Claude Max and Grok quota in the workspace row, plus quota-aware model-class lanes (ag) for new agents | `claude` `codex` `grok` `model-routing` `quota` | 1 | 2026-10-22 |
| [**🆕 jc-herdr-plugins**](https://github.com/thejiajun/jc-herdr-plugins)<br><sub>thejiajun</sub> | Herdr plugins: Autoname (auto-name workspaces from agent conversations) and Agent Switcher (search and jump between agents) | `python` | 1 | 2026-10-14 |
| [**🆕 tinysend-herdr**](https://github.com/tiny-send/tinysend-herdr)<br><sub>tiny-send</sub> | herdr plugin: email yourself when an agent blocks/finishes, reply to unblock it. Powered by tinysend. | `ai-agents` `tinysend` `javascript` | 1 | 2026-06-26 |
| [**🆕 taskherd**](https://github.com/ukwhatn/taskherd)<br><sub>ukwhatn</sub> | Task board linked to herdr agent sessions, PRs, and Jira tickets | `claude-code` `kanban` `task-management` `tui` `go` | 1 | 2026-09-01 |
| [**🆕 herdr-github-pr**](https://github.com/woshahua/herdr-github-pr)<br><sub>woshahua</sub> | Herdr plugin that syncs GitHub PR status, checks, reviews, and comments | `github` `javascript` | 1 | 2026-08-21 |
| [**🆕 herdr-session-titles**](https://github.com/wxomi/herdr-session-titles)<br><sub>wxomi</sub> | Rich session titles & task context for Devin, Cursor, Agy, Kiro, and Claude in Herdr | `ai-agents` `terminal` `python` | 1 | 2026-10-05 |
| [**🆕 herdr-mark**](https://github.com/y4le/herdr-mark)<br><sub>y4le</sub> | tmux-style marked pane for herdr: mark a pane, then join it beside or swap it with another | `shell` | 1 | 2026-09-26 |
| [**🆕 herdr-translate**](https://github.com/zackshen/herdr-translate)<br><sub>zackshen</sub> | Herdr plugin: translate mouse-selected terminal text in a centered popover | `rust` | 1 | 2026-08-25 |
| [**🆕 fence**](https://github.com/zenodea/fence)<br><sub>zenodea</sub> | Contained herdr sessions (bubblewrap + nftabels) | `ai-agents` `bubblewrap` `claude-code` `nftables` `sandbox` | 1 | 2026-10-05 |
| [**🆕 herdr-draft**](https://github.com/ZviBaratz/herdr-draft)<br><sub>ZviBaratz</sub> | herdr plugin: a new-session creation dialog — Linear issue, worktree, placement, agent kind, clauth account and initial prompt in one submit | `bubbletea` `claude-code` `go` `linear` `tui` | 1 | 2026-10-14 |
| [**🆕 corgi**](https://github.com/zyrre/corgi)<br><sub>zyrre</sub> | A compact dashboard for Herdr coding agents, with supervisor coordination and an Omarchy bar widget. | `claude-code` `codex` `tui` `rust` | 1 | 2026-10-28 |
| [**🆕 herdr-job-board**](https://github.com/larrychannon/herdr-job-board)<br><sub>larrychannon</sub> | A To do / Doing / Waiting-on-you board for agent jobs, in a Herdr split pane. | `javascript` | 1 | 2026-10-28 |
| [**🆕 herdr-fleet-plugin**](https://github.com/yarrasys/herdr-fleet-plugin)<br><sub>yarrasys</sub> | herdr plugin: start, restart and swap a team of named coding agents from a per-repository fleet file (.herdr/fleet.toml) | `coding-agents` `multi-agent` `python` | 1 | 2026-10-26 |
| [**🆕 instinct-herdr-tunnel**](https://github.com/romiluz13/instinct-herdr-tunnel)<br><sub>romiluz13</sub> | Let an AI assistant such as Instinct watch and steer your Herdr coding agents: a loopback portal with a 26-action allowlist, a bearer token and an audit log, p… | `ai-agents` `cloudflare-tunnel` `coding-agents` `nodejs` `javascript` | 2 | 2026-10-25 |
| [**🆕 herdr-ingest**](https://github.com/H3xept/herdr-ingest)<br><sub>H3xept</sub> | One herdr space per work item, from Sentry, Linear, GitHub or any JSON pipeline | `github` `linear` `sentry` `terminal` `shell` | 1 | 2026-09-26 |
| [**🆕 herdr-stats**](https://github.com/jeffarese/herdr-stats)<br><sub>jeffarese</sub> | Live CPU, memory, disk, temperature, GPU, power and network stats in herdr's tab bar: braille graphs, gauges and reactive icons | `linux` `macos` `rust` `system-monitor` `terminal` | 1 | 2026-10-23 |
| [**🆕 stampede**](https://github.com/vib-z/stampede)<br><sub>vib-z</sub> | Text tasks to your Grok Bot. It reaches your Mac over Tailscale, where Claude Code does the job, adding other agents (Codex, Cursor and more) as needed. Nothin… | `agent-orchestration` `ai-agents` `claude-code` `cli` `codex` | 5 | 2026-10-28 |
| [**🆕 account-capacity-dock**](https://github.com/Mako-L/account-capacity-dock)<br><sub>Mako-L</sub> | Quota rings for every Claude, Codex and Cursor account: a desktop dock, a terminal app and a Herdr widget. | `claude` `cliproxyapi` `codex` `cursor` `python` | 4 | 2026-10-28 |
| [**🆕 devnull-tui**](https://github.com/arhen/devnull-tui)<br><sub>arhen</sub> | Unofficial terminal UI for /dev/null (dev-null.sh) — the feed, threads and inbox in any terminal, or as a Herdr pane | `cli` `dev-null` `devnull` `terminal` `tui` | 2 | 2026-10-23 |
| [**🆕 diffui**](https://github.com/dgsienko/diffui)<br><sub>dgsienko</sub> | Locally hosted web tool and terminal ui for reviewing live diffs and improving your agentic coding and review flow. | `agentic-coding` `ai-agents` `ai-tools` `claude-code` `cli` | 2 | 2026-10-23 |
| [**🆕 herdr-sbx**](https://github.com/lanwen/herdr-sbx)<br><sub>lanwen</sub> | Herdr Plugin to enable Docker Sandboxes as SSH connected machines. Full agent visibility, plugin sync | `docker` `sandboxes` `go` | 2 | 2026-10-26 |
| [**🆕 ovis**](https://github.com/devswha/ovis)<br><sub>devswha</sub> | Ovis (formerly herdr web UI): free, open-source browser and phone client for herdr. Chat and live terminal for Claude Code, Codex and every agent pane, remote… | `agentic-coding` `ai-agents` `bun` `claude-code` `codex` | 1605 | 2026-10-28 |
| [**🆕 herdr-island**](https://github.com/speardragon/herdr-island)<br><sub>speardragon</sub> | Your herdr agents live in the MacBook notch: approve, answer and watch them from a Dynamic Island-style panel | `ai-agents` `claude-code` `macos` `notch` `swiftui` | 5 | 2026-10-28 |
| [**🆕 herdr-gh-runs**](https://github.com/kkjdaniel/herdr-gh-runs)<br><sub>kkjdaniel</sub> | GitHub Actions runs in a herdr pane: follows your repo, live status, step logs and notifications | `gh` `github-actions` `terminal` `tui` `python` | 1 | 2026-10-22 |
| [**🆕 reficus**](https://github.com/81zi/reficus)<br><sub>81zi</sub> | Grow the focused pane and shrink the others on every focus change | `python` | 3 | 2026-10-21 |
| [**🆕 herdr-claude-autoupdate**](https://github.com/0xMMA/herdr-claude-autoupdate)<br><sub>0xMMA</sub> | herdr plugin: restarts idle Claude Code panes onto the newly installed version, in place, same session and flags, drafts kept. | `claude-code` `typescript` | 1 | 2026-10-11 |
| [**🆕 medley**](https://github.com/WebscapeOrg/medley)<br><sub>WebscapeOrg</sub> | Custom sounds for every herdr workspace and status | `audio` `notifications` `python` | 1 | 2026-10-23 |

[⬆ Back to purposes](#purposes)

<a id="cat-notify"></a>

## Notifications & Alerts

> I want to know when an agent finishes or gets stuck waiting for input, even when I'm away from my desk

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**Heeler**](https://github.com/ZingerLittleBee/Heeler)<br><sub>ZingerLittleBee</sub> | Native iOS agent console for herdr — watch and drive the coding agents on your machines over SSH, with a real libghostty terminal, QR pairing, and push notific… | `ai-agents` `apns` `coding-agents` `ios` `libghostty` | 678 | 🔄 2026-10-28 |
| [**herdr-ohmyzsh**](https://github.com/robbyrussell/herdr-ohmyzsh)<br><sub>robbyrussell</sub> | Oh My Zsh plugin for Herdr: slow commands in the sidebar, done notifications, shell helpers, and one key to reload Oh My Zsh in every idle pane | `oh-my-zsh` `zsh` `shell` | 85 | 2026-09-09 |
| [**herdr-focus-notify**](https://github.com/yankewei/herdr-focus-notify)<br><sub>yankewei</sub> | Clickable macOS notifications for Herdr agents. Sends a native toast when an agent becomes blocked or done; clicking it brings the terminal forward and focuses… | `alerter` `macos` `notifications` `productivity` `rust` | 32 | 🔄 2026-10-28 |
| [**herdr-terminal-notifier**](https://github.com/dot/herdr-terminal-notifier)<br><sub>dot</sub> | Customizable macOS notifications for herdr agent state changes via terminal-notifier | `macos` `terminal-notifier` `shell` | 11 | 2026-09-07 |
| [**herdr-ntfy**](https://github.com/horn553/herdr-ntfy)<br><sub>horn553</sub> | Minimal dependencies: jq, curl, and sh — send ntfy notifications when Herdr agents finish or get blocked. | `shell` | 9 | 2026-09-16 |
| [**herdr-pings**](https://github.com/joelhooks/herdr-pings)<br><sub>joelhooks</sub> | Turn-level wake events for AI agents in herdr panes — pi extension, wait CLI, crash bridge, and Discworld callsigns for your workers | `ai-agents` `pi` `typescript` | 9 | 2026-08-09 |
| [**herdr-ntfy-notify**](https://github.com/zom-2018/herdr-ntfy-notify)<br><sub>zom-2018</sub> | Real-time ntfy push notifications for Herdr terminal agents | `agent` `ntfy` `push-notifications` `tui` `javascript` | 8 | 2026-06-23 |
| [**herdr-hail**](https://github.com/natori-hrj/herdr-hail)<br><sub>natori-hrj</sub> | Two-way Slack & Discord bridge for herdr — get pinged when an agent blocks, reply/tap to unblock. No tunnel. | `discord` `slack` `typescript` | 7 | 2026-07-19 |
| [**herdr-nudge**](https://github.com/justinchiasson/herdr-nudge)<br><sub>justinchiasson</sub> | Clickable macOS notifications for Herdr when an agent is blocked or done, or a long shell command finishes. Click one to jump to that exact pane. Nothing else… | `claude-code` `macos` `notifications` `notify` `zsh` | 6 | 2026-09-29 |
| [**herdr-telegram-plugin**](https://github.com/mvallebr/herdr-telegram-plugin)<br><sub>mvallebr</sub> | Telegram bot companion for herdr — remote control any agent via Telegram forum topics, zero LLM in the path. | `typescript` | 6 | 2026-08-31 |
| [**herdr-announcer**](https://github.com/nhclink16/herdr-announcer)<br><sub>nhclink16</sub> | Herdr plugin: speaks a one-sentence LLM summary when an agent finishes or needs input — local TTS, ElevenLabs, or any custom command | `tts` `rust` | 5 | 2026-09-09 |
| [**herdr-notify-windows**](https://github.com/aclima01/herdr-notify-windows)<br><sub>aclima01</sub> | Windows 11 toast notifications for herdr agents (turn finished / needs input) | `powershell` | 4 | 2026-07-23 |
| [**herdr-cache-alert**](https://github.com/AltanS/herdr-cache-alert)<br><sub>AltanS</sub> | Herdr plugin: prompt-cache countdown on every agent pane, with every cache rule sourced and dated | `ai-agents` `ai-coding` `ai-tools` `claude-code` `multiplexing` | 4 | 2026-09-17 |
| [**herdr-telegram-bridge**](https://github.com/cokekitten/herdr-telegram-bridge)<br><sub>cokekitten</sub> | Get a Telegram push when a herdr agent finishes or blocks — reply to it to send text or files straight back into that agent. No server, no tunnel, no app. | `ai-agents` `chatops` `claude-code` `developer-tools` `notifications` | 4 | 2026-08-06 |
| [**session-sounds**](https://github.com/ChrisPachulski/session-sounds)<br><sub>ChrisPachulski</sub> | Distinct per-agent completion and attention sounds for Herdr on macOS and Linux. | `coding-agents` `notifications` `rust` | 3 | 2026-07-19 |
| [**agent-webhook-notify**](https://github.com/happyeric77/agent-webhook-notify)<br><sub>happyeric77</sub> | Send webhook notifications when Herdr agents finish or get blocked | `javascript` | 3 | 2026-08-12 |
| [**herdr-telegram-notify**](https://github.com/naturalmoods/herdr-telegram-notify)<br><sub>naturalmoods</sub> | Messages you on Telegram when an agent finishes or needs input, with its last message, changes, duration and cost. Answer from the chat with text, menu buttons… | `claude-code` `notifications` `telegram` `javascript` | 3 | 2026-10-13 |
| [**herdr-warp**](https://github.com/ProjectAJ14/herdr-warp)<br><sub>ProjectAJ14</sub> | A simple plugin which lets Herdr send notification via Warp. | `python` | 3 | 🔄 2026-10-15 |
| [**herdr-discord-presence**](https://github.com/revanp/herdr-discord-presence)<br><sub>revanp</sub> | Herdr plugin: show your Herdr session and agent status as Discord Rich Presence | `typescript` | 3 | 2026-08-14 |
| [**herdr-wsl-notify**](https://github.com/tkmct/herdr-wsl-notify)<br><sub>tkmct</sub> | A Herdr plugin that shows a Windows desktop toast when an agent (Claude Code, etc.) running under WSL2 becomes done (finished) or blocked (waiting for approval… | `javascript` | 3 | 2026-08-27 |
| [**herdr-webhook-notify**](https://github.com/zgxme/herdr-webhook-notify)<br><sub>zgxme</sub> | Herdr plugin that forwards agent notifications to Slack, Discord, Teams, Google Chat, Feishu, Lark, DingTalk, WeCom, Telegram, ntfy or any HTTP webhook | `dingtalk` `discord` `feishu` `lark` `notifications` | 3 | 🔄 2026-10-27 |
| [**herdr-agent-notify**](https://github.com/A1exthegreat/herdr-agent-notify)<br><sub>A1exthegreat</sub> | Herdr plugin: desktop notifications when agents finish working, need confirmation, or go idle | `javascript` | 2 | 2026-08-15 |
| [**buzzr**](https://github.com/candypoets/buzzr)<br><sub>candypoets</sub> | Mirror live Herdr spaces and agents into Buzz channels with Nostr identities and mention routing. | `agents` `buzz` `nostr` `rust` | 2 | 2026-08-14 |
| [**herdr-telegram-slack-bridge**](https://github.com/lsisoft/herdr-telegram-slack-bridge)<br><sub>lsisoft</sub> | Bidirectional Telegram and Slack bot bridge for Herdr agent sessions, routing blocked-agent alerts and chat replies back to Herdr or tmux panes | `ai-agents` `slack-bot` `telegram-bot` `tmux` `python` | 2 | 2026-07-28 |
| [**herdr-guard**](https://github.com/StructuPath/herdr-guard)<br><sub>StructuPath</sub> | Cross-agent command policy for Herdr: audit, alert, and interrupt dangerous shell commands | `ai-agents` `command-policy` `security` `terminal` `javascript` | 2 | 2026-09-14 |
| [**🆕 herdr-prayer-times**](https://github.com/bayoudhi/herdr-prayer-times)<br><sub>bayoudhi</sub> | Next Islamic prayer and countdown in the Herdr sidebar, with a timetable popup and notifications | `rust` | 1 | 2026-08-13 |
| [**herdr-oncall**](https://github.com/fulanto/herdr-oncall)<br><sub>fulanto</sub> | Answer your coding agent's permission prompts from a floating macOS panel or Telegram — a Herdr plugin for Claude Code and Codex. | `ai-agents` `claude-code` `cli` `codex` `coding-agent` | 1 | 🔄 2026-10-27 |
| [**🆕 herdr-random-sounds**](https://github.com/gridness/herdr-random-sounds)<br><sub>gridness</sub> | play random notification sounds per agent status in herdr on macOS | `herdr-integration` `macos` `notification` `notifications` `python` | 1 | 2026-08-23 |
| [**🆕 herdr-ntfy-notify**](https://github.com/jjuraszek/herdr-ntfy-notify)<br><sub>jjuraszek</sub> | Herdr plugin: ntfy push notification to your phone when an agent goes blocked or done | `ntfy` `javascript` | 1 | 2026-09-13 |
| [**🆕 herdr-slack-notify**](https://github.com/juninaba/herdr-slack-notify)<br><sub>juninaba</sub> | Send Slack notifications when Herdr agents finish or get blocked. | `javascript` | 1 | 2026-07-07 |
| [**🆕 herdr-claude-agents**](https://github.com/kamil-pociot/herdr-claude-agents)<br><sub>kamil-pociot</sub> | Herdr plugin: Claude Code background sessions as Herdr agents — one tab each in its project's space, live state and notifications. | `claude-code` `rust` | 1 | 🔄 2026-10-24 |
| [**🆕 herdr-gh-runs**](https://github.com/kkjdaniel/herdr-gh-runs)<br><sub>kkjdaniel</sub> | GitHub Actions runs in a herdr pane: follows your repo, live status, step logs and notifications | `gh` `github-actions` `terminal` `tui` `python` | 1 | 🔄 2026-10-22 |
| [**🆕 herdr-bar**](https://github.com/openalon-org/herdr-bar)<br><sub>openalon-org</sub> | macOS menu bar for Herdr. Live agent counts. One click to the pane that needs you. | `herdr-notify` `menu-bar` `menu-bar-app` `notification` `notify` | 1 | 2026-09-18 |
| [**🆕 goat-herdr**](https://github.com/shindakun/goat-herdr)<br><sub>shindakun</sub> | 🐐 Herdr plugin: alerts to Telegram, Slack, ntfy, Pushover/bullet or any webhook when an agent needs you | `ntfy` `rust` `slack` `telegram` `webhook` | 1 | 2026-09-24 |
| [**🆕 medley**](https://github.com/WebscapeOrg/medley)<br><sub>WebscapeOrg</sub> | Custom sounds for every herdr workspace and status | `audio` `notifications` `python` | 1 | 🔄 2026-10-23 |

[⬆ Back to purposes](#purposes)

<a id="cat-remote"></a>

## Mobile & Remote Control

> I want to monitor agents from my phone or while away, and just send back approvals

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**🆕 ovis**](https://github.com/devswha/ovis)<br><sub>devswha</sub> | Ovis (formerly herdr web UI): free, open-source browser and phone client for herdr. Chat and live terminal for Claude Code, Codex and every agent pane, remote… | `agentic-coding` `ai-agents` `bun` `claude-code` `codex` | 1605 | 🔄 2026-10-28 |
| [**collie**](https://github.com/AltanS/collie)<br><sub>AltanS</sub> | Herdr mobile client for iPhone and Android. A self-hosted PWA to drive Claude Code, Pi, Codex and OpenCode in Herdr, tmux or zellij from your phone. Push alert… | `agent-orchestration` `ai` `ai-agents` `ai-coding` `ai-tools` | 1495 | 🔄 2026-10-28 |
| [**🆕 shepherdr**](https://github.com/eliasstravik/shepherdr)<br><sub>eliasstravik</sub> | Run many coding agents across machines from a phone, tablet or desktop. A herdr plugin. | `typescript` | 912 | 🔄 2026-10-28 |
| [**herdr-remote**](https://github.com/dcolinmorgan/herdr-remote)<br><sub>dcolinmorgan</sub> | Monitor and drive your herdr agents from menu bar, phone, or Telegram. Zero config locally. Free tunnel for remote. No Tailscale needed. | `macos` `mobile` `python` | 435 | 🔄 2026-10-23 |
| [**herdr-mobile-relay**](https://github.com/0cv/herdr-mobile-relay)<br><sub>0cv</sub> | Approve and monitor Herdr agents remotely from your phone, a mobile web app for Android/iOS smartphones with push notifications, QR setup, and multi-computer r… | `android` `approvals` `cloudflare` `ios` `mobile` | 324 | 🔄 2026-10-28 |
| [**pairfob**](https://github.com/arronKler/pairfob)<br><sub>arronKler</sub> | Your Herdr agents on your phone in one QR scan. Browser-first, optional Android beta, no Tailscale or ports, end-to-end encrypted. | `android` `apk` `claude-code` `codex` `herdr-mobile` | 181 | 🔄 2026-10-28 |
| [**herdr-telegram-agents**](https://github.com/permgps/herdr-telegram-agents)<br><sub>permgps</sub> | Drive your coding agents from Telegram like from the terminal. A topic per agent, live status in the topic icon, two-way chat with inline buttons for choices. | `claude-code` `coding-agents` `go` `telegram` `telegram-bot` | 84 | 🔄 2026-10-24 |
| [**termote**](https://github.com/lamngockhuong/termote)<br><sub>lamngockhuong</sub> | Self-hosted PWA to control Claude Code, Codex, GitHub Copilot or any terminal from your phone or desktop. Single Go binary streaming tmux/psmux/Herdr sessions… | `ai-coding-agent` `claude-code` `cli` `codex` `github-copilot` | 67 | 🔄 2026-10-28 |
| [**herdrchat**](https://github.com/cobanov/herdrchat)<br><sub>cobanov</sub> | Control your herdr coding agents from your phone. On the App Store for iPhone and iPad. | `app-store` `herdr-client` `herdr-integration` `herdr-mobile` `ios` | 39 | 🔄 2026-10-27 |
| [**herdr-watch**](https://github.com/Unayung/herdr-watch)<br><sub>Unayung</sub> | Agent status from herdr on an Apple Watch | `javascript` | 31 | 2026-08-14 |
| [**herdr-connect**](https://github.com/Tomyail/herdr-connect)<br><sub>Tomyail</sub> | Monitor and control your Herdr AI coding agents from your iPhone with this mobile companion app — read output, send follow-ups, and get notified when jobs fini… | `agent` `mobile-app` `react-native` `typescript` | 20 | 🔄 2026-10-28 |
| [**herdr-call**](https://github.com/eliasstravik/herdr-call)<br><sub>eliasstravik</sub> | Voice control for Herdr | `elevenlabs` `tailscale` `voice` `typescript` | 16 | 2026-08-07 |
| [**vscode-devcontainers-herdr**](https://github.com/scott-the-programmer/vscode-devcontainers-herdr)<br><sub>scott-the-programmer</sub> | Herdr relay for agents running inside a dev container | `container` `devcontainer` `rust` | 15 | 🔄 2026-10-25 |
| [**herdr-web**](https://github.com/barnuri/herdr-web)<br><sub>barnuri</sub> | Mobile-first web UI plugin for herdr — drive your coding agents from a phone, with notifications | `pwa` `typescript` | 13 | 🔄 2026-10-22 |
| [**herdr-office**](https://github.com/michaellandi/herdr-office)<br><sub>michaellandi</sub> | A Herdr plugin that draws your agents as people in an open-plan office. They raise a hand when they need approval. | `javascript` | 12 | 2026-10-05 |
| [**herdr-plugin-mobile-relay**](https://github.com/benkraus/herdr-plugin-mobile-relay)<br><sub>benkraus</sub> | _(no description)_ | `typescript` | 11 | 2026-08-12 |
| [**wherdr**](https://github.com/afloury/wherdr)<br><sub>afloury</sub> | Use Herdr from anywhere — your iPhone, Android phone or any browser. Watch your coding agents, answer them and run your herdr-projects, privately and securely. | `ai-agents` `claude-code` `codex` `mobile` `pwa` | 10 | 🔄 2026-10-28 |
| [**herdr-push**](https://github.com/dcolinmorgan/herdr-push)<br><sub>dcolinmorgan</sub> | herdr plugin: zero-dep event push to herdr-remote for mobile monitoring and one-tap approval | `shell` | 10 | 2026-07-09 |
| [**herdr-go**](https://github.com/herdr-go/herdr-go)<br><sub>herdr-go</sub> | Control your herdr coding agents from anywhere — private, P2P, EasyTier-secured. | `dart` | 8 | 2026-09-08 |
| [**paddock**](https://github.com/lntvan166/paddock)<br><sub>lntvan166</sub> | A mobile-first dashboard for herdr — reads its unix socket. Run on your phone without any configuration. | `agent-orchestration` `coding-agents` `herdr-mobile` `paddock` `pwa` | 8 | 🔄 2026-10-28 |
| [**🆕 quicktui-herdr**](https://github.com/quicktui/quicktui-herdr)<br><sub>quicktui</sub> | Use Herdr from your iPhone or Android phone with QuickTUI: native mobile app, one-step install, QR pairing, and an optional end-to-end encrypted relay. | `shell` | 8 | 🔄 2026-10-26 |
| [**muqun-gateway**](https://github.com/osuki-dev/muqun-gateway)<br><sub>osuki-dev</sub> | The program that lets Muqun reach a terminal on your own computer. It runs on your machine, talks to tmux or to Herdr, and answers your phone directly — there… | `rust` | 7 | 🔄 2026-10-27 |
| [**herdr-remote-panes**](https://github.com/Poor-Plebs/herdr-remote-panes)<br><sub>Poor-Plebs</sub> | Work on other machines from one Herdr: pick a machine from a menu, get a terminal on it. Optional experimental two-way mirroring. | `golang` `ssh` `terminal` `go` | 7 | 2026-09-11 |
| [**herdr-mobile**](https://github.com/bsorescu/herdr-mobile)<br><sub>bsorescu</sub> | Phone-friendly TUI for controlling Herdr coding agents over SSH | `mobile` `ssh` `textual` `tui` `python` | 6 | 2026-08-25 |
| [**herdr-web**](https://github.com/eyalev/herdr-web)<br><sub>eyalev</sub> | Mobile-first web UI for the herdr agent multiplexer — drive your coding agents from a phone | `claude-code` `mobile` `pwa` `terminal` `javascript` | 6 | 2026-07-29 |
| [**merino**](https://github.com/LoneExile/merino)<br><sub>LoneExile</sub> | Merino 🐑 — remote tunnel dashboard for Herdr agents | `go` `macos` `menubar` `react` `wails` | 6 | 2026-09-21 |
| [**arcdr**](https://github.com/arcnessai/arcdr)<br><sub>arcnessai</sub> | herdr mobile & web client that shows what your Claude Code mods report — answer your agents from your phone, over your own Tailscale | `ai-agents` `bun` `claude-code` `claude-code-mods` `coding-agents` | 5 | 🔄 2026-10-27 |
| [**herdr-phone**](https://github.com/matheus3301/herdr-phone)<br><sub>matheus3301</sub> | Mobile remote console for Herdr over Cloudflare Tunnel and Access | `cloudflare-tunnel` `coding-agents` `developer-tools` `golang` `mobile` | 5 | 🔄 2026-10-16 |
| [**herdr-tether**](https://github.com/mcc0x/herdr-tether)<br><sub>mcc0x</sub> | Keep local and remote terminal workloads running after their Herdr view closes. | `remote-development` `rust` `ssh` `terminal` `tmux` | 5 | 🔄 2026-10-16 |
| [**herdr-portfwd**](https://github.com/miko-misa/herdr-portfwd)<br><sub>miko-misa</sub> | Automatic SSH port forwarding for coding agents on remote machines: Ctrl+click the localhost URL your agent printed and the page opens on your machine, same po… | `ai-agents` `claude-code` `cli` `coding-agents` `developer-tools` | 5 | 2026-10-11 |
| [**herdweb**](https://github.com/zlxlabs/herdweb)<br><sub>zlxlabs</sub> | Monitor and drive your coding agents from your phone.Voice Input, Paste Image, webhook notification, multi devices server support.. | `typescript` | 5 | 🔄 2026-10-20 |
| [**herdr-aws-ssm**](https://github.com/maayanyosef/herdr-aws-ssm)<br><sub>maayanyosef</sub> | Pick an EC2 instance and connect over AWS SSM in a herdr --remote session - no bastion or public IP. | `aws-ssm` `terminal` `shell` | 4 | 2026-07-01 |
| [**herdr-farm**](https://github.com/mejiasd3v/herdr-farm)<br><sub>mejiasd3v</sub> | Herdr plugin: 3D farm that visualizes your Herdr workspaces and agents as livestock (three.js webapp) | `threejs` `javascript` | 4 | 2026-07-28 |
| [**herdr-mobile-app**](https://github.com/teasec4/herdr-mobile-app)<br><sub>teasec4</sub> | Native companion app + lightweight Go relay: stream live agent terminal output to your phone, check statuses, and send prompts — over LAN, Tailscale, or Funnel | `ai` `devtools` `flutter` `herdr-integration` `herdr-mobile` | 4 | 2026-09-05 |
| [**herdr-whistle**](https://github.com/amurru/herdr-whistle)<br><sub>amurru</sub> | Herdr plugin for remote agent management | `golang` `telegrambot` `go` | 3 | 2026-08-06 |
| [**herdr-topbar**](https://github.com/bigbug16/herdr-topbar)<br><sub>bigbug16</sub> | macOS menu bar icon for herdr — jump back to your session, open a project, and see which agent is waiting for input. | `macos` `menubar` `swift` | 3 | 2026-08-24 |
| [**herdr-remote**](https://github.com/dibin666/herdr-remote)<br><sub>dibin666</sub> | Remote browser access to your Herdr terminal workspaces | `claude-code` `codex` `pi` `vibe-coding` `typescript` | 3 | 🔄 2026-10-24 |
| [**community**](https://github.com/fab-agent/community)<br><sub>fab-agent</sub> | Put your teammates next to your agents: members, departments, tasks and direct messages inside Herdr. | `ai-agents` `chatinterface` `cloudflare-workers` `community` `terminal-chat` | 3 | 🔄 2026-10-15 |
| [**herdr-telegram-gate**](https://github.com/hkdom/herdr-telegram-gate)<br><sub>hkdom</sub> | Telegram approval inbox + risk-tiered auto-approval for your herdr AI agent fleet — blocked agents surface as Telegram cards with Approve/Deny buttons (zero-de… | `approval-gate` `telegram` `javascript` | 3 | 2026-08-06 |
| [**lerdr-rust-kotlin**](https://github.com/IGUNUBLUE/lerdr-rust-kotlin)<br><sub>IGUNUBLUE</sub> | Rust relay + Kotlin/Jetpack Compose Android app for Herdr: end-to-end encrypted agent sessions over Tailscale. AI-generated reimplementation (built with Cognit… | `ai-generated` `android` `e2ee` `jetpack-compose` `kotlin` | 3 | 🔄 2026-10-21 |
| [**herdr-remotedownloder**](https://github.com/kosuketut/herdr-remotedownloder)<br><sub>kosuketut</sub> | Download files from a remote Herdr pane to the connected Mac. | `developer-tools` `file-transfer` `macos` `rust` `ssh` | 3 | 🔄 2026-10-23 |
| [**herdr-mobile-pro**](https://github.com/spad-0x/herdr-mobile-pro)<br><sub>spad-0x</sub> | A high-performance, mobile-first PWA dashboard with a Cyber-Dark design for orchestrating Herdr and autonomous AI agents directly from your smartphone. Feature… | `javascript` | 3 | 2026-09-12 |
| [**herdr-devup**](https://github.com/alon-z/herdr-devup)<br><sub>alon-z</sub> | Herdr plugin: per-project dev layouts from .herdr/dev.toml with tunnel-URL env sync | `typescript` | 2 | 2026-06-22 |
| [**setnet**](https://github.com/chano-gpt/setnet)<br><sub>chano-gpt</sub> | Herd multi-harness coding agents from your phone — a Herdr plugin | `typescript` | 2 | 2026-08-29 |
| [**shahi**](https://github.com/iYassr/shahi)<br><sub>iYassr</sub> | Use Claude Code, Codex, Cursor CLI, OpenCode and Antigravity from your phone. A herdr plugin with iPhone and web apps: read agent conversations, answer permiss… | `ai-agents` `antigravity` `claude-code` `codex` `coding-agents` | 2 | 🔄 2026-10-28 |
| [**herdr-reach**](https://github.com/Luisalt20/herdr-reach)<br><sub>Luisalt20</sub> | Read-only network doctor for Herdr remote machines: measures what your network actually allows and recommends a transport with evidence. No writes, no third-pa… | `cli` `cloudflare-tunnel` `connectivity` `egress` `go` | 2 | 2026-09-21 |
| [**🆕 instinct-herdr-tunnel**](https://github.com/romiluz13/instinct-herdr-tunnel)<br><sub>romiluz13</sub> | Let an AI assistant such as Instinct watch and steer your Herdr coding agents: a loopback portal with a 26-action allowlist, a bearer token and an audit log, p… | `ai-agents` `cloudflare-tunnel` `coding-agents` `nodejs` `javascript` | 2 | 🔄 2026-10-25 |
| [**herdr-web-tui**](https://github.com/tigorlazuardi/herdr-web-tui)<br><sub>tigorlazuardi</sub> | Daemon-first browser/PWA frontend for Herdr with an optional plugin launcher | `go` | 2 | 2026-10-01 |
| [**herdr-hub**](https://github.com/alex-devdone/herdr-hub)<br><sub>alex-devdone</sub> | Describe a herdr session of remote-attach panes as a portable manifest, and rebuild it on any machine | `python` | 1 | 2026-08-23 |
| [**🆕 shep**](https://github.com/ArtMoreno/shep)<br><sub>ArtMoreno</sub> | Your Herdr terminals on your phone. Desktop setup, private pairing, themes, and QuotaDeck. | `pwa` `terminal` `javascript` | 1 | 2026-09-28 |
| [**🆕 herdr-async-message-relay**](https://github.com/avery20024/herdr-async-message-relay)<br><sub>avery20024</sub> | Durable async messaging for Herdr agents with stable role routing and batched delivery. | `go` | 1 | 🔄 2026-10-27 |
| [**sightr**](https://github.com/bartholomewtj/sightr)<br><sub>bartholomewtj</sub> | Sightr — phone web UI for a Herdr agent herd, over Tailscale | `typescript` | 1 | 🔄 2026-10-22 |
| [**herdr-amp-orbs**](https://github.com/BlockedPath/herdr-amp-orbs)<br><sub>BlockedPath</sub> | Herdr plugin: run Amp orbs (remote Amp agents) in Herdr panes | `amp` `shell` | 1 | 🔄 2026-10-27 |
| [**🆕 agent-watch**](https://github.com/gabrielmarcano/agent-watch)<br><sub>gabrielmarcano</sub> | Approve, answer and prompt your terminal coding agents (Claude Code, OpenCode, Antigravity…) from a Wear OS watch. Built on herdr, with a Go host bridge and a… | `ai-agents` `android` `claude-code` `coding-agents` `golang` | 1 | 🔄 2026-10-27 |
| [**🆕 herdr-tunnel**](https://github.com/ivorpad/herdr-tunnel)<br><sub>ivorpad</sub> | Herdr plugin: put a local port on the public internet, copy the URL, take it down again | `tui` `python` | 1 | 2026-08-27 |
| [**🆕 tether-browser**](https://github.com/jeffhuen/tether-browser)<br><sub>jeffhuen</sub> | Remote-to-local browser bridge for AI coding agents. Your agent runs on the server; Chrome stays on your workstation, with your passkeys, password manager, and… | `go` | 1 | 2026-10-06 |
| [**🆕 herdr-web**](https://github.com/mttzzz/herdr-web)<br><sub>mttzzz</sub> | herdr in your browser: a 1:1 mirror of the herdr TUI for your phone, tablet or another computer (herdr plugin) | `bun` `mobile` `terminal` `websocket` `xterm` | 1 | 2026-10-07 |
| [**🆕 herdview**](https://github.com/Orchard-Robotics/herdview)<br><sub>Orchard-Robotics</sub> | View your herd from the web | `html` | 1 | 2026-09-24 |
| [**herdr-vps-local**](https://github.com/yavuzhansarmaz/herdr-vps-local)<br><sub>yavuzhansarmaz</sub> | Local experience on remote machines: mirror VPS/Pi repos to your laptop via Mutagen | `rust` | 1 | 2026-09-28 |

<details><summary>Also relevant to this purpose</summary>

- [powerfooI/roamgate](https://github.com/powerfooI/roamgate) — A Herdr client for any screen. Control terminals, monitor coding agents, and review files and diffs from desk…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-agents"></a>

## Agent Orchestration

> I want to launch, split up, and manage multiple AI agents together

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**oh-my-opencode-slim**](https://github.com/alvinunreal/oh-my-opencode-slim)<br><sub>alvinunreal</sub> | Lean, fine tuned Opencode multi agent suite · Mix any models · Auto delegate tasks | `agentic-ai` `oh-my-opencode` `opencode` `orchestration` `typescript` | 9839 | 🔄 2026-10-26 |
| [**agentbox**](https://github.com/madarco/agentbox)<br><sub>madarco</sub> | Run multiple agents in parallel sandboxed VMs, with a single command, on your PC or in the cloud | `claude` `claude-code` `cli` `cmux` `codex` | 559 | 2026-10-07 |
| [**pi-workflows**](https://github.com/osolmaz/pi-workflows)<br><sub>osolmaz</sub> | Workflow engine, JSON control-flow tool, and live terminal viewer for the pi coding agent | `typescript` | 350 | 2026-10-08 |
| [**pi-extensible-workflows**](https://github.com/vekexasia/pi-extensible-workflows)<br><sub>vekexasia</sub> | Deterministic multi-agent workflow orchestration and codemode scripts for Pi | `codemode` `pi` `workflow` `workflows` `typescript` | 250 | 🔄 2026-10-28 |
| [**herdr-board**](https://github.com/nelsonPires5/herdr-board)<br><sub>nelsonPires5</sub> | Kanban board for herdr — cards are prompts dispatched to AI agents in visible panes | `board` `kanban` `kanban-board` `tui` `rust` | 185 | 🔄 2026-10-18 |
| [**herdr-dagr**](https://github.com/aemrebarut/herdr-dagr)<br><sub>aemrebarut</sub> | Your agent swarm as a live DAG: an orchestration graph with attempts, review gates, and evidence, in a herdr split pane. | `agents` `dag` `multi-agent` `orchestration` `rust` | 134 | 2026-08-23 |
| [**agent-router**](https://github.com/nidhi-singh02/agent-router)<br><sub>nidhi-singh02</sub> | CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr | `agents` `ai` `claude-code` `cli` `codex` | 119 | 2026-09-27 |
| [**herdr-file-annotator**](https://github.com/JonasBaeumer/herdr-file-annotator)<br><sub>JonasBaeumer</sub> | A plugin for herdr to maximize agentic development without losing touch with the actual codebase | `rust` | 64 | 2026-10-07 |
| [**proqi**](https://github.com/oborchers/proqi)<br><sub>oborchers</sub> | A terminal-native prompt composer for power users running multiple coding agents. | `ai-agents` `claude-code` `cli` `coding-agents` `developer-tools` | 43 | 🔄 2026-10-25 |
| [**agentbox-herdr-plugin**](https://github.com/madarco/agentbox-herdr-plugin)<br><sub>madarco</sub> | Run multiple agents in parallel sandboxed VMs, with a single command, on your PC or in the cloud | `claude-code` `codex-cli` `opencode` `sandbox` `shell` | 34 | 2026-06-24 |
| [**herdr-voice**](https://github.com/brogrammerMW/herdr-voice)<br><sub>brogrammerMW</sub> | Talk to your coding agents in your Herdr panes, and hear them answer with real-time voice using Grok, OpenAI, or Gemini. | `macos` `voice` `swift` | 31 | 2026-09-26 |
| [**entwurf**](https://github.com/junghan0611/entwurf)<br><sub>junghan0611</sub> | Open visible sibling AI sessions in Herdr or tmux, reopen pi sessions in tmux under the same garden id, and exchange messages across pi, pi-durable, Claude Cod… | `acp` `agent-collaboration` `agent-communication` `agent-to-agent` `ai-agents` | 31 | 🔄 2026-10-27 |
| [**herdr-browser**](https://github.com/StructuPath/herdr-browser)<br><sub>StructuPath</sub> | Drivable agent-browser pane for Herdr with live streaming, real interaction, adaptive rendering, console/page errors, recording, and localhost routing | `terminal` `javascript` | 31 | 2026-10-10 |
| [**herdr-world**](https://github.com/IvoryHeart/herdr-world)<br><sub>IvoryHeart</sub> | Herdr World — visualize agent work in Office, Tree, Graph, and Spaces; control Herdr agents across local and SSH hosts. | `agent-runtime` `agent-visualization` `coding-agents` `multi-agent` `observability` | 30 | 🔄 2026-10-28 |
| [**termaxa**](https://github.com/termaxa/termaxa)<br><sub>termaxa</sub> | The agent's prompt shows you the command; Termaxa shows you the consequence. Previews, backups, policy, an audit record. Claude Code, Codex, Cursor, Copilot. A… | `agent-safety` `ai-agents` `claude-code` `cli` `developer-tools` | 27 | 🔄 2026-10-27 |
| [**herdmates**](https://github.com/caioniehues/herdmates)<br><sub>caioniehues</sub> | Claude Code agent teams, native in herdr — teammux shim, mission-control board, focus pane | `agent-teams` `claude-code` `rust` `tui` | 26 | 2026-08-21 |
| [**pi-herd**](https://github.com/ribbons-digital/pi-herd)<br><sub>ribbons-digital</sub> | Visible Pi session orchestration with Herdr panes and git worktrees | `typescript` | 23 | 2026-07-06 |
| [**herdr-agent-handoff**](https://github.com/sanirudh17/herdr-agent-handoff)<br><sub>sanirudh17</sub> | Herdr plugin that hands an in-progress agent session to a fresh session of another installed coding agent, carrying the complete session inside the prompt - no… | `agent-handoff` `claude-code` `codex` `coding-agents` `developer-tools` | 22 | 2026-09-30 |
| [**PromptPilot**](https://github.com/ivanarama/PromptPilot)<br><sub>ivanarama</sub> | Background task queue for Claude Code and other AI CLIs — web UI + Telegram bot | `ai-agents` `claude-code` `telegram-bot` `python` | 20 | 🔄 2026-10-28 |
| [**herdr-vercel-sandbox-plugin**](https://github.com/vercel-labs/herdr-vercel-sandbox-plugin)<br><sub>vercel-labs</sub> | Run terminal-based coding agents in isolated Vercel Sandboxes from Herdr. | `javascript` | 15 | 2026-08-09 |
| [**herdr-social-glass**](https://github.com/ythx-101/herdr-social-glass)<br><sub>ythx-101</sub> | Screenshot-friendly Social Glass theme and workflow plugin for Herdr on macOS. | `macos` `multi-agent` `terminal-theme` `shell` | 14 | 2026-08-21 |
| [**herdr-catchup**](https://github.com/wilbeibi/herdr-catchup)<br><sub>wilbeibi</sub> | Cross-agent coding-session handoff for herdr: from a live pane, summarize, fork, or hand a Claude Code, Codex, Cursor, Cline, or OpenCode session to another ag… | `ai-agents` `claude-code` `codex` `coding-agents` `context-handoff` | 12 | 2026-09-28 |
| [**deevs-pi-kit**](https://github.com/DeevsDeevs/deevs-pi-kit)<br><sub>DeevsDeevs</sub> | Perfect pi kit to be 10x Deevs' engineer | `agents` `pi` `pi-agent` `pi-extension` `pi-package` | 11 | 2026-10-08 |
| [**herdr-devcontainer**](https://github.com/gambtho/herdr-devcontainer)<br><sub>gambtho</sub> | Herdr plugin for opening shells and coding agents inside a repo's Dev Container via the official Dev Containers CLI. | `coding-agents` `containers` `devcontainers` `developer-tools` `development-environment` | 11 | 2026-08-13 |
| [**herdr-recap**](https://github.com/mrolafsson/herdr-recap)<br><sub>mrolafsson</sub> | Come back to a bunch of agents and know in seconds which ones need you. A herdr popup that tells you, per agent, where it got to (a recap written while you wer… | `bubbletea` `claude-code` `codex` `coding-agents` `go` | 11 | 🔄 2026-10-21 |
| [**agys**](https://github.com/quaywin/agys)<br><sub>quaywin</sub> | Effortless multi-profile isolation & real-time quota tracking for Antigravity CLI in Herdr via zero-pollution sandboxing. | `ai-agents` `antigravity` `cli` `context-window` `developer-tools` | 11 | 2026-09-26 |
| [**vibetty**](https://github.com/second-state/vibetty)<br><sub>second-state</sub> | Share a live AI agent terminal to smart hardware (vibekeys, vibewatch, etc.) over MQTT; can also be used as a Herdr plugin. | `claude-code` `codex` `vibecoding` `rust` | 11 | 🔄 2026-10-15 |
| [**shepherdr**](https://github.com/afogel/shepherdr)<br><sub>afogel</sub> | Shepherd delegated coding agents into visible, auditable herdr panes you can watch, resume, and take over — a herdr plugin. | `ai-agents` `claude-code` `codex` `cursor` `rust` | 10 | 2026-07-24 |
| [**namedrop**](https://github.com/ericbust/namedrop)<br><sub>ericbust</sub> | @mentions for Codex, Claude Code, and your terminal. A Herdr plugin that lets agents in different panes work together. | `agent-collaboration` `ai-agents` `claude-code` `cli` `codex` | 10 | 🔄 2026-10-28 |
| [**herdr-swarm**](https://github.com/StructuPath/herdr-swarm)<br><sub>StructuPath</sub> | Parallel coding agents on one repo, safely: worktree-per-agent fan-out, live change visibility, and review-first harvest for Herdr | `terminal` `javascript` | 10 | 🔄 2026-10-15 |
| [**herdr-agent-messenger**](https://github.com/aashishd/herdr-agent-messenger)<br><sub>aashishd</sub> | Send focused, self-contained messages between AI agents running in live Herdr panes, so one agent can coordinate work with another without sharing its full con… | `python` | 9 | 2026-10-09 |
| [**herdr-plugin-odysseus**](https://github.com/jpolec/herdr-plugin-odysseus)<br><sub>jpolec</sub> | Governed multi-agent workflows for Herdr: tasks → agents in Herdr panes → checks, retries, review, policy, approvals, audit, draft PR | `ai-agents` `rust` | 9 | 2026-09-25 |
| [**herdr-helpr**](https://github.com/sohanemon/herdr-helpr)<br><sub>sohanemon</sub> | Prompt-driven workspace and pane management for herdr. | `ai-agents` `bun` `cli` `developer-tools` `ink` | 9 | 🔄 2026-10-26 |
| [**🆕 herduck**](https://github.com/wenhanweime/herduck)<br><sub>wenhanweime</sub> | Agent window management, project visibility, and a global conversation library. Built on Herdr for people and Agents. | `agent-memory` `ai-agents` `claude-code` `codex` `coding-agents` | 9 | 🔄 2026-10-28 |
| [**awp**](https://github.com/agentwireprotocol/awp)<br><sub>agentwireprotocol</sub> | Peer-to-peer messaging for AI coding agents: delegate tasks, share files, track state across Claude Code, Codex, Cursor, OpenCode, Pi and more. | `agent-orchestration` `agents` `protcol` `go` | 8 | 2026-09-29 |
| [**herdr-sbx-plugin**](https://github.com/dirien/herdr-sbx-plugin)<br><sub>dirien</sub> | Herdr plugin that runs coding agents inside Docker Sandboxes (sbx), one microVM per agent | `coding-agents` `docker-sandboxes` `javascript` | 8 | 2026-09-13 |
| [**spoolway**](https://github.com/marvingygas/spoolway)<br><sub>marvingygas</sub> | Minimalistic agent state machine for software development: a retro TUI dispatcher that drives agent sessions through defined pipelines | `agent` `cli` `descriptive` `llm` `pipeline` | 8 | 🔄 2026-10-28 |
| [**herdr-space-scoped-agents**](https://github.com/ShankyJS/herdr-space-scoped-agents)<br><sub>ShankyJS</sub> | herdr plugin that scopes the agent panel to the space you're focused on | `coding-agents` `terminal` `go` | 8 | 2026-07-23 |
| [**pet-town**](https://github.com/abhishek944/pet-town)<br><sub>abhishek944</sub> | A transparent desktop village for live Herdr agents | `javascript` | 7 | 🔄 2026-10-23 |
| [**herdr-orchestrate**](https://github.com/darjss/herdr-orchestrate)<br><sub>darjss</sub> | Pi-native orchestration for visible Herdr worker sessions — a run board, durable prompts/reports/state, isolated git worktrees, and explicit model routing. | `pi-package` `typescript` | 7 | 2026-07-13 |
| [**AgentRadio**](https://github.com/detailles/AgentRadio)<br><sub>detailles</sub> | Local message bus for AI coding agents running in Herdr panes — join, DM, presence, offline delivery | `agent-orchestration` `multi-agent` `radio` `python` | 7 | 2026-09-27 |
| [**agent-panel**](https://github.com/flowy11/agent-panel)<br><sub>flowy11</sub> | herdr plugin: a side panel for your Claude Code or Codex session, its subagents, messages, refs and to-dos | `claude-code` `codex` `javascript` | 7 | 2026-09-29 |
| [**pier**](https://github.com/July24/pier)<br><sub>July24</sub> | Pi is the coding-agent carrier; Herdr is a terminal workspace manager. pier adds the two capabilities pi deliberately leaves out — a todo list loop and interac… | `pi-coding-agent` `typescript` | 7 | 🔄 2026-10-28 |
| [**chatter**](https://github.com/marcvermeeren/chatter)<br><sub>marcvermeeren</sub> | Chatter is an experiment in cross-harness agent collaboration: a shared group chat and context layer for agents working on the same Git repository in Herdr. | `agent-collaboration` `agentic-ai` `agentic-workflow` `ai-agents` `group-chat` | 7 | 2026-08-18 |
| [**herdr-triage**](https://github.com/natori-hrj/herdr-triage)<br><sub>natori-hrj</sub> | Attention triage for herdr — ranks your agents by who needs you most; a long-blocked agent rises to the top. | `ai-agents` `triage` `rust` | 7 | 2026-07-23 |
| [**herdr-fleet**](https://github.com/Northern-Lighthouse/herdr-fleet)<br><sub>Northern-Lighthouse</sub> | Manage a fleet of herdr machines over Tailscale: dashboard plugin, auto-discovery, capacity-aware agent dispatch, diskless workspaces | `ai-agents` `tailscale` `python` | 7 | 2026-08-14 |
| [**herdr-scuttlebutt**](https://github.com/andybarilla/herdr-scuttlebutt)<br><sub>andybarilla</sub> | A herdr plugin that gives the agents in a herdr session a shared chat room | `rust` | 6 | 2026-09-22 |
| [**herdr-pane-topic-sync**](https://github.com/danbuhler/herdr-pane-topic-sync)<br><sub>danbuhler</sub> | herdr plugin: auto-name panes & tabs after each agent's live topic (Claude Code, Codex, …) instead of 1, 2, 3. | `ai-agents` `claude-code` `terminal` `tmux-alternative` `javascript` | 6 | 2026-09-02 |
| [**herdr-orchestrator**](https://github.com/kylezk777/herdr-orchestrator)<br><sub>kylezk777</sub> | Herdr-orch is a file-based agent orchestration tool that runs on top of Herdr. | `agent-orchestration` `orchestrator` `rust` | 6 | 2026-07-26 |
| [**herdr-birdseye**](https://github.com/calebcauthon/herdr-birdseye)<br><sub>calebcauthon</sub> | Birds Eye View of your agents in herdr | `rust` | 5 | 2026-07-24 |
| [**herdr-loop**](https://github.com/cyperx84/herdr-loop)<br><sub>cyperx84</sub> | Declarative, event-driven loop and graph orchestration for herdr — run Claude Code, Codex, opencode and pi together until the work converges | `ai-agents` `golang` `orchestration` `go` | 5 | 2026-09-10 |
| [**herdr-openclaw**](https://github.com/gejiliang/herdr-openclaw)<br><sub>gejiliang</sub> | herdr plugin: manage OpenClaw TUI panes as first-class herdr agents | `openclaw` `terminal` `javascript` | 5 | 2026-08-13 |
| [**herdr-espresso**](https://github.com/Hanyang-Li/herdr-espresso)<br><sub>Hanyang-Li</sub> | Keeps your MacBook awake even when the lid closed when agent is running | `rust` | 5 | 2026-10-10 |
| [**herdr-gamepad**](https://github.com/htlin222/herdr-gamepad)<br><sub>htlin222</sub> | Drive Herdr with a game controller. Patrol your AI agents, split panes and switch workspaces from the couch — any gamepad, mapped by you in 60 seconds. | `ai-agents` `gamepad` `macos` `swift` `terminal-multiplexer` | 5 | 2026-09-09 |
| [**herdr-walkietalkie**](https://github.com/jeffory/herdr-walkietalkie)<br><sub>jeffory</sub> | Herdr plugin: token-efficient cross-agent delegation (wt) — orchestrator agents spawn Claude/OpenCode/Antigravity workers in tabs or worktrees | `shell` | 5 | 🔄 2026-10-14 |
| [**herdr-nono-plugin**](https://github.com/schemaitat/herdr-nono-plugin)<br><sub>schemaitat</sub> | Herdr plugin that runs coding agents (OpenCode) in nono sandboxes: sandboxed server and client, localhost locked down, verified via /proc | `rust` | 5 | 2026-10-10 |
| [**🆕 stampede**](https://github.com/vib-z/stampede)<br><sub>vib-z</sub> | Text tasks to your Grok Bot. It reaches your Mac over Tailscale, where Claude Code does the job, adding other agents (Codex, Cursor and more) as needed. Nothin… | `agent-orchestration` `ai-agents` `claude-code` `cli` `codex` | 5 | 🔄 2026-10-28 |
| [**herdr-worker-orchestrator**](https://github.com/anhnd3005-infinity/herdr-worker-orchestrator)<br><sub>anhnd3005-infinity</sub> | Dispatch tasks to CLI agent workers (agy, codex, ...) via Herdr-managed panes with stateful task tracking, worktree isolation & diff-based review. Dual plugin… | `html` | 4 | 2026-08-25 |
| [**herdr-blaxel-sandbox-plugin**](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin)<br><sub>blaxel-ai</sub> | Run coding agents in persistent Blaxel sandboxes from Herdr. | `blaxel` `claude-code` `codex` `coding-agents` `opencode` | 4 | 🔄 2026-10-28 |
| [**herdr-blueprint**](https://github.com/chappse6/herdr-blueprint)<br><sub>chappse6</sub> | Your coding agent explains its work as diagrams, right next to the chat. A herdr plugin for Claude Code and Codex. | `ai-agents` `claude-code` `codex` `markdown` `mermaid` | 4 | 2026-10-12 |
| [**herdr-desktop-pet**](https://github.com/hanbong5938/herdr-desktop-pet)<br><sub>hanbong5938</sub> | Native macOS desktop companion for Herdr with Rubelia, session activity, and agent messaging | `desktop-pet` `macos` `rust` | 4 | 🔄 2026-10-19 |
| [**herdr-pets**](https://github.com/hmu332233/herdr-pets)<br><sub>hmu332233</sub> | macOS desktop pets for Herdr agents that come find you when an agent is blocked. | `desktop-pet` `swift` | 4 | 🔄 2026-10-25 |
| [**herdr-a2a**](https://github.com/IsaiasZc/herdr-a2a)<br><sub>IsaiasZc</sub> | Reliable agent-to-agent delegation layer for Herdr via A2A | `typescript` | 4 | 2026-08-27 |
| [**herdr-huddle**](https://github.com/ivolkoff/herdr-huddle)<br><sub>ivolkoff</sub> | herdr plugin: agents ask rich questions as a page over their pane and get JSON back | `javascript` | 4 | 2026-10-07 |
| [**herdr-newtab-plus**](https://github.com/jeffarese/herdr-newtab-plus)<br><sub>jeffarese</sub> | A Herdr new tab that asks which folder and which agent: completes real paths, remembers where you work, and starts an agent for you. | `rust` | 4 | 🔄 2026-10-24 |
| [**herdr-prompt-library**](https://github.com/jwkicklighter/herdr-prompt-library)<br><sub>jwkicklighter</sub> | A Herdr plugin for browsing, managing, and inserting reusable local or global Markdown prompts into the focused pane. | `go` `golang` `prompting` `snippets` `tui` | 4 | 🔄 2026-10-16 |
| [**herdr-sheepdog**](https://github.com/kccarlos/herdr-sheepdog)<br><sub>kccarlos</sub> | Manage your Herdr agents by voice — hands-free, from anywhere. A voice-first agent harness for Claude Code, Codex and other coding agents, with an iPhone app. | `agent-harness` `agent-orchestration` `ai-agents` `claude-code` `codex` | 4 | 🔄 2026-10-28 |
| [**herdr-math**](https://github.com/liambern/herdr-math)<br><sub>liambern</sub> | Render LaTeX display equations inside Herdr terminal panes, with a harness-independent agent skill. | `ai-agents` `latex` `mathjax` `terminal` `javascript` | 4 | 2026-09-14 |
| [**herdr-agent-profiles**](https://github.com/mikeyobrien/herdr-agent-profiles)<br><sub>mikeyobrien</sub> | Data-driven CLI harness and model profiles for Herdr | `ai-agents` `terminal` `python` | 4 | 2026-08-10 |
| [**arda**](https://github.com/Nirvaan05/arda)<br><sub>Nirvaan05</sub> | Herdr plugin that lets specialized coding agents find each other and work as one team across sessions and machines. | `agent-communication` `agent-handoff` `agent-orchestration` `agent-to-agent` `ai-agents` | 4 | 2026-10-09 |
| [**horchestra**](https://github.com/SimoneDaniotti/horchestra)<br><sub>SimoneDaniotti</sub> | Orchestrator-led agent teams for Herdr, with a live agent map in every tab | `ai-agents` `claude-code` `codex` `terminal` `tui` | 4 | 🔄 2026-10-13 |
| [**herdr-conductor**](https://github.com/StructuPath/herdr-conductor)<br><sub>StructuPath</sub> | Orchestrate a feature-delivery team as visible Herdr agent panes — the Conductor plugin | `orchestration` `javascript` | 4 | 2026-10-02 |
| [**herdr-auto-yes-sir**](https://github.com/xlinx/herdr-auto-yes-sir)<br><sub>xlinx</sub> | herdr-auto-yes-sir for non blocked running when agent ask for approve; like codex. | `javascript` | 4 | 2026-08-20 |
| [**herdr-council**](https://github.com/zekierman/herdr-council)<br><sub>zekierman</sub> | herdr plugin: ask every coding agent the same question, then let a judge weigh the answers blind | `ai-agents` `llm-council` `go` | 4 | 🔄 2026-10-18 |
| [**herdr-theos-settler**](https://github.com/calebcauthon/herdr-theos-settler)<br><sub>calebcauthon</sub> | Settle Herdr agent tabs and workspaces below active work to get finished work out of the way. Theo's idea. | `rust` | 3 | 2026-07-23 |
| [**herdr-chat**](https://github.com/eliasstravik/herdr-chat)<br><sub>eliasstravik</sub> | A live structured chat view for agents running inside Herdr. | `typescript` | 3 | 2026-08-24 |
| [**herdr-snip**](https://github.com/eStudio37/herdr-snip)<br><sub>eStudio37</sub> | Box what one agent printed and hand it to another. A Herdr plugin: freeze a pane, box part of it with two clicks, send it to any agent. | `ai-agents` `claude-code` `codex` `coding-agents` `terminal` | 3 | 🔄 2026-10-23 |
| [**herdr-cursor**](https://github.com/gabriel-laet/herdr-cursor)<br><sub>gabriel-laet</sub> | Cursor cloud agents as first-class herdr panes | `typescript` | 3 | 2026-09-08 |
| [**herdr-agent-restart**](https://github.com/hmu332233/herdr-agent-restart)<br><sub>hmu332233</sub> | Restart agents in Herdr with one shortcut when their display breaks, and continue the same conversation. | `agent-restart` `javascript` | 3 | 2026-09-08 |
| [**brgr**](https://github.com/justn-hyeok/brgr)<br><sub>justn-hyeok</sub> | Run Claude Code, Codex, OpenCode, Cursor and more as parallel coding-agent workers in Herdr panes, orchestrated by your Codex or Claude Code session. | `agent-orchestration` `ai-agents` `ai-coding` `claude-code` `codex` | 3 | 🔄 2026-10-28 |
| [**kubeflock**](https://github.com/LoriKarikari/kubeflock)<br><sub>LoriKarikari</sub> | [Experimental] Create and connect Kubernetes sandboxes in Herdr | `agent-sandbox` `gvisor` `kubernetes` `sandbox` `go` | 3 | 2026-09-11 |
| [**herdr-link**](https://github.com/LZHcode1986/herdr-link)<br><sub>LZHcode1986</sub> | Faster, token-efficient, and zero-reasoning cross-agent interoperability for Herdr sessions. Replaces heavyweight skills with a unified contract for peer disco… | `typescript` | 3 | 🔄 2026-10-19 |
| [**herdr-snooze**](https://github.com/mrolafsson/herdr-snooze)<br><sub>mrolafsson</sub> | Keep a long list of agents down to the ones you're working with. A herdr plugin that hides an agent, or a whole space, from the Agents panel until a time you p… | `bubbletea` `claude-code` `coding-agents` `go` `multi-agent` | 3 | 🔄 2026-10-20 |
| [**herdr-pinpoint**](https://github.com/navishachiku/herdr-pinpoint)<br><sub>navishachiku</sub> | Pick a Herdr space, tab, or pane and type its id into the agent you were talking to | `javascript` | 3 | 🔄 2026-10-28 |
| [**muster**](https://github.com/ofelcan164/muster)<br><sub>ofelcan164</sub> | One screen for every agent across every repo. A herdr plugin. | `go` | 3 | 2026-09-28 |
| [**herdr-space-topic**](https://github.com/panuhorsmalahti/herdr-space-topic)<br><sub>panuhorsmalahti</sub> | herdr plugin: name each Space after the work happening inside it — the live topic of its primary agent pane. | `ai-agents` `terminal-multiplexer` `javascript` | 3 | 🔄 2026-10-21 |
| [**herdr-crew**](https://github.com/rarce/herdr-crew)<br><sub>rarce</sub> | herdr plugin: bring up a team of Claude Code sessions, one tab per role, plus a live status board, from a versioned .herdr/crew.toml | `ai-agents` `claude-code` `git-worktree` `multi-agent` `rust` | 3 | 🔄 2026-10-24 |
| [**herdr-approve-all**](https://github.com/RenKoya1/herdr-approve-all)<br><sub>RenKoya1</sub> | herdr plugin: approve every blocked agent at once (one keystroke, all pending permission prompts) | `shell` | 3 | 2026-08-16 |
| [**herdr-agents-history**](https://github.com/speardragon/herdr-agents-history)<br><sub>speardragon</sub> | See what your AI coding agents are actually doing — a live, keyboard-driven herdr TUI streaming every tool call across all your agents (Claude Code & Codex). | `ai-agents` `claude-code` `codex` `tui` `typescript` | 3 | 2026-07-19 |
| [**herdr-bot**](https://github.com/speardragon/herdr-bot)<br><sub>speardragon</sub> | Turn your herdr agents into bots that talk to each other — give Claude Code, Codex or Grok a name and a chat, and put a few in a room. macOS app + herdr plugin. | `agent-orchestration` `ai-agents` `chat` `claude-code` `codex` | 3 | 🔄 2026-10-21 |
| [**herdr-agent-office**](https://github.com/suisya-systems/herdr-agent-office)<br><sub>suisya-systems</sub> | Your agent fleet as a pixel-art office - a herdr plugin. See who's working, who's stuck, and jump to them. | `python` | 3 | 2026-07-25 |
| [**herdr-upstash-box**](https://github.com/upstash/herdr-upstash-box)<br><sub>upstash</sub> | Herdr plugin: run a coding agent in an Upstash Box from the worktree you are looking at | `claude-code` `coding-agents` `sandbox` `upstash` `typescript` | 3 | 2026-09-10 |
| [**herdr-wakeup**](https://github.com/usrivastava92/herdr-wakeup)<br><sub>usrivastava92</sub> | Herdr plugin that keeps macOS or Linux awake while Herdr-managed agents are working | `power-management` `sleep-prevention` `wakeup` `rust` | 3 | 2026-07-17 |
| [**herdr-cadence**](https://github.com/zhenyufu/herdr-cadence)<br><sub>zhenyufu</sub> | Light agent orchestrator with one Lead and a fleet of agents | `rust` | 3 | 2026-10-13 |
| [**herdr-radar-plus**](https://github.com/4242labs/herdr-radar-plus)<br><sub>4242labs</sub> | Herdr plugin: agents sorted by what needs you, in named groups that span machines. Built on herdr-radar. | `agent-monitoring` `ai-agents` `coding-agents` `developer-tools` `multi-machine` | 2 | 🔄 2026-10-25 |
| [**herdr-threads**](https://github.com/alepar/herdr-threads)<br><sub>alepar</sub> | durable group threads (aka message inbox) for your agents, cross-harness and cross-machine | `rust` | 2 | 🔄 2026-10-28 |
| [**herdr-agent-tree**](https://github.com/dboeter/herdr-agent-tree)<br><sub>dboeter</sub> | herdr plugin: workspaces and their agents as a live tree, docked on the left or right of every tab | `agentic-workflow` `claude-code` `claudecode` `codex-cli` `coding-agents` | 2 | 🔄 2026-10-25 |
| [**herdr-glow**](https://github.com/DevooKim/herdr-glow)<br><sub>DevooKim</sub> | Ambient edge glow on macOS when a Herdr agent is blocked | `swift` | 2 | 🔄 2026-10-15 |
| [**herdr-docket**](https://github.com/DnzzL/herdr-docket)<br><sub>DnzzL</sub> | Give a task to a named coding agent: it opens a PR, a second agent verifies it, a merge gate in code merges it — or hands it to you. A Herdr plugin. | `agent-fleet` `ai-agents` `ai-code-review` `autonomous-agents` `backlog-md` | 2 | 🔄 2026-10-28 |
| [**browsr**](https://github.com/g00rek/browsr)<br><sub>g00rek</sub> | Keep a dedicated Chromium tab group aligned with each Herdr workspace | `chromium` `coding-agents` `developer-tools` `hyprland` `linux` | 2 | 🔄 2026-10-19 |
| [**herdr-prompt-bucket**](https://github.com/GNURub/herdr-prompt-bucket)<br><sub>GNURub</sub> | A durable, ordered prompt bucket for coding agents running in Herdr | `claude-code` `codex` `coding-agents` `opencode` `typescript` | 2 | 2026-08-19 |
| [**herdr-annotations**](https://github.com/IgorWarzocha/herdr-annotations)<br><sub>IgorWarzocha</sub> | Collect annotations on terminal selections and stage them into Herdr agents | `ai-agents` `annotations` `terminal` `javascript` | 2 | 2026-07-18 |
| [**herdr-watcher**](https://github.com/joshka0/herdr-watcher)<br><sub>joshka0</sub> | Durable continuations and detached worker callbacks for Herdr agents | `rust` | 2 | 🔄 2026-10-19 |
| [**herdr-plugin**](https://github.com/juscribe/herdr-plugin)<br><sub>juscribe</sub> | File and transition Juscribe tickets from a Herdr pane, and see which ticket each agent is on. | `juscribe` `shell` | 2 | 🔄 2026-10-22 |
| [**herdr-shame-report**](https://github.com/JYasha11/herdr-shame-report)<br><sub>JYasha11</sub> | Keeps a permanent ledger of how long you've left your AI agents waiting. The sheep remember. | `javascript` | 2 | 2026-07-10 |
| [**herdr-panorama**](https://github.com/LeaveMyYard/herdr-panorama)<br><sub>LeaveMyYard</sub> | Swarm view for herdr: every Claude Code orchestrator, thread and subagent on one live screen. | `claude-code` `claude-code-plugin` `rust` | 2 | 🔄 2026-10-22 |
| [**herdr-agents-status**](https://github.com/maedana/herdr-agents-status)<br><sub>maedana</sub> | Always-on-top transparent overlay showing Herdr agent status — a spiritual successor to claudeye, built for Herdr instead of tmux. | `rust` | 2 | 2026-08-15 |
| [**herdr-redact**](https://github.com/mcc0x/herdr-redact)<br><sub>mcc0x</sub> | Warns you when an agent pane has printed a credential — before you screenshot it, stream it, or paste it into a chat window. | `rust` `secret-detection` `security` `terminal` | 2 | 🔄 2026-10-16 |
| [**herdr-flow**](https://github.com/mohaphez/herdr-flow)<br><sub>mohaphez</sub> | Persistent multi-agent task coordination for Herdr with guarded review and worktree cleanup | `python` | 2 | 2026-10-04 |
| [**🆕 herdr-mailbox**](https://github.com/navishachiku/herdr-mailbox)<br><sub>navishachiku</sub> | A mailbox per receiving agent: merged messages and decision questions answered in a side pane | `javascript` | 2 | 🔄 2026-10-28 |
| [**herdr-plugins**](https://github.com/peteretelej/herdr-plugins)<br><sub>peteretelej</sub> | Open-source herdr plugins that tame my AI Agent herd (work best with OpenCode) 🐏🔌 | `agentic-engineering` `rust` `terminal` | 2 | 🔄 2026-10-25 |
| [**herdr-cam**](https://github.com/rchougule/herdr-cam)<br><sub>rchougule</sub> | Show your agent what's on your desk: press a key, point your webcam, and the photo lands in your coding agent's prompt. A herdr plugin for macOS. | `avfoundation` `claude-code` `codex` `coding-agents` `developer-tools` | 2 | 2026-10-09 |
| [**🆕 fangyang-le**](https://github.com/RZfive/fangyang-le)<br><sub>RZfive</sub> | herdr skill: fan one task out to N parallel coding agents — Claude Code, OpenCode, Codex, Gemini & 20+. Same-kind spawn, workspace-locked, keep-fold-for-review… | `agent-orchestration` `agent-skill` `ai-workflow` `claude-code` `codex-cli` | 2 | 🔄 2026-10-28 |
| [**herdr-browser**](https://github.com/salamituns/herdr-browser)<br><sub>salamituns</sub> | Watch your coding agents browse: a Herdr pane showing the Chrome that Claude Code, Codex, Cursor, Droid and Antigravity drive through chrome-devtools-mcp or Pl… | `ai-agents` `antigravity` `browser` `chrome-devtools` `chrome-devtools-mcp` | 2 | 🔄 2026-10-15 |
| [**herdr-code-board**](https://github.com/sazardev/herdr-code-board)<br><sub>sazardev</sub> | Kanban queue for agentic prompts inside Herdr: cards dispatch real agents into panes, worktrees and workspaces, with rules that chain one card to the next. | `ai-agents` `kanban` `rust` `tui` | 2 | 2026-08-30 |
| [**herdr-achievements**](https://github.com/SerHappy/herdr-achievements)<br><sub>SerHappy</sub> | Achievements and tiny celebrations for your Herdr AI agent herd | `achievements` `ai-agents` `developer-tools` `gamification` `go` | 2 | 2026-07-30 |
| [**herdr-traex**](https://github.com/szrenwei/herdr-traex)<br><sub>szrenwei</sub> | Herdr Marketplace integration for TraeX agent lifecycle and metadata | `traex` `python` | 2 | 2026-08-04 |
| [**herdr-forkr**](https://github.com/t4t5/herdr-forkr)<br><sub>t4t5</sub> | fork an agent conversation in a new herdr pane | `shell` | 2 | 2026-09-10 |
| [**herdr-rovo-dev**](https://github.com/usrivastava92/herdr-rovo-dev)<br><sub>usrivastava92</sub> | Herdr plugin that detects Rovo Dev CLI sessions and reports them as live agents in Herdr | `ai-agent` `rovo` `rovo-dev` `shell` | 2 | 2026-10-05 |
| [**opencode-herdr**](https://github.com/VicenteOlmos/opencode-herdr)<br><sub>VicenteOlmos</sub> | OpenCode plugin: route agents through Herdr as herdr/<adapter>/<model> | `ai-agent` `claude-code` `coding-agent` `cursor` `multi-agent` | 2 | 🔄 2026-10-21 |
| [**shelley-herdr**](https://github.com/webframp/shelley-herdr)<br><sub>webframp</sub> | Run exe.dev Shelley conversations as native herdr agents | `go` | 2 | 2026-10-10 |
| [**herdr-agent-timer**](https://github.com/Yemeni/herdr-agent-timer)<br><sub>Yemeni</sub> | A Herdr plugin that alternates each agent's status label with its elapsed time | `shell` | 2 | 2026-08-14 |
| [**cbds**](https://github.com/zqkra/cbds)<br><sub>zqkra</sub> | Reliable multi-agent orchestration for the Herdr herd. Durable tasks, authoritative worker reports, and a wait that cannot hang. | `agents` `cli` `multi-agent` `orchestration` `javascript` | 2 | 2026-08-31 |
| [**herdr-pouch**](https://github.com/AltanS/herdr-pouch)<br><sub>AltanS</sub> | Herdr plugin: stash prompts for an agent ahead of time and insert them when it's ready | `ai-agents` `ai-coding` `ai-tools` `multiplexing` `typescript` | 1 | 2026-09-02 |
| [**🆕 unblock**](https://github.com/aneym/unblock)<br><sub>aneym</sub> | One queue for everything your agents need from you. Blockers need an action, grills need a judgement; secrets never enter the model's context. | `agents` `human-in-the-loop` `mcp` `javascript` | 1 | 🔄 2026-10-28 |
| [**herdr-pi-reloader**](https://github.com/anrunt/herdr-pi-reloader)<br><sub>anrunt</sub> | Reload or restart idle Pi agent sessions from a Herdr overlay TUI. | `rust` | 1 | 2026-07-18 |
| [**🆕 hird**](https://github.com/aoprisan/hird)<br><sub>aoprisan</sub> | Cross-harness agent work queue and shared assertion memory, backed by one local SQLite database | `ai-agents` `claude-code` `cli` `mcp` `rust` | 1 | 2026-09-29 |
| [**herdr-pointr**](https://github.com/aristeoibarra/herdr-pointr)<br><sub>aristeoibarra</sub> | Point at a DOM element on a localhost page and it lands in the coding agent that owns that project, with its React component, selector and an optional screensh… | `coding-agent` `devtools` `react` `typescript` | 1 | 2026-09-25 |
| [**herdr-quick-prompt**](https://github.com/astwys/herdr-quick-prompt)<br><sub>astwys</sub> | A Herdr plugin to send predefined prompts to an agent pane | `shell` | 1 | 2026-08-24 |
| [**herdr-overview**](https://github.com/baeroe/herdr-overview)<br><sub>baeroe</sub> | Mission Control for herdr: a live tiled overview of all spaces, every agent or your favorite panes. | `ai-agents` `mission-control` `nodejs` `terminal` `tui` | 1 | 🔄 2026-10-15 |
| [**herdr-agent-queue**](https://github.com/connerohnesorge/herdr-agent-queue)<br><sub>connerohnesorge</sub> | herdr plugin: queue prompts for Claude Code and other agents, submit each as a new turn when the current turn ends (Codex-style queue) | `claude-code` `python` | 1 | 2026-09-29 |
| [**🆕 herdr-handoff**](https://github.com/devops-fj/herdr-handoff)<br><sub>devops-fj</sub> | Preview and securely hand off local working context between Herdr coding agents. | `ai-agents` `coding-agents` `go` | 1 | 2026-08-21 |
| [**🆕 herdr-orch**](https://github.com/ellingtonsp/herdr-orch)<br><sub>ellingtonsp</sub> | Orchestrate coding agents in herdr: mailbox, blocking ask/reply, tasks with dependencies, tracked dispatch, decision gates, verified worker release. CLI: horch. | `ai-agents` `claude-code` `cli` `codex` `go` | 1 | 🔄 2026-10-14 |
| [**herdr-agent-team**](https://github.com/gdli6177/herdr-agent-team)<br><sub>gdli6177</sub> | A Herdr plugin for Markdown-defined agent teams | `javascript` | 1 | 2026-08-16 |
| [**🆕 LunaCrab**](https://github.com/GranamyrBR/LunaCrab)<br><sub>GranamyrBR</sub> | Reserved for a separate project | `agents` `developer-tools` `multi-agent` `observability` `rust` | 1 | 2026-08-10 |
| [**🆕 heraldr**](https://github.com/gwenwindflower/heraldr)<br><sub>gwenwindflower</sub> | 🛡️ Reactive label chrome for Herdr tabs, workspaces, and agents | `rust` | 1 | 2026-10-01 |
| [**🆕 herdr-plugin-done-timer**](https://github.com/hanjm93/herdr-plugin-done-timer)<br><sub>hanjm93</sub> | A prompt-cache countdown for every AI agent on herdr's agents panel, read from each agent's transcript. | `ai-agents` `claude-code` `shell` | 1 | 2026-09-15 |
| [**🆕 agent-keep-awake**](https://github.com/happyeric77/agent-keep-awake)<br><sub>happyeric77</sub> | Prevent macOS sleep while Herdr agents are working | `javascript` | 1 | 🔄 2026-10-26 |
| [**🆕 the-cat-concerto**](https://github.com/Herdanis/the-cat-concerto)<br><sub>Herdanis</sub> | Orchestrator prompt + worker contract for coding agents, driven by herdr | `claude-code` `codex` `coding-agent` `gemini-cli` `opencode` | 1 | 🔄 2026-10-26 |
| [**herdr-diagrams**](https://github.com/jellespijker/herdr-diagrams)<br><sub>jellespijker</sub> | Mermaid, PlantUML, Structurizr, D2 and Graphviz diagrams from your coding agents, rendered as images in a Herdr pane | `claude-code` `diagrams` `kitty-graphics` `mermaid` `plantuml` | 1 | 2026-10-03 |
| [**paneMorph**](https://github.com/Jenish-Shobhit/paneMorph)<br><sub>Jenish-Shobhit</sub> | herdr plugin that moves live panes between tabs and spaces: send any pane anywhere, fetch any pane here, undo any move. | `ai-agents` `developer-tools` `pane-management` `ratatui` `rust` | 1 | 🔄 2026-10-18 |
| [**🆕 herdr-plan-approve**](https://github.com/jerryfane/herdr-plan-approve)<br><sub>jerryfane</sub> | Auto-approve Claude Code plan-mode dialogs in herdr — agents plan, then execute, without a keypress. | `claude-code` `shell` | 1 | 2026-08-25 |
| [**corral**](https://github.com/jirathip-dev/corral)<br><sub>jirathip-dev</sub> | Read-only fleet monitor for herdr coding agents | `agent-orchestration` `ai-agents` `coding-agents` `devtools` `fleet-management` | 1 | 🔄 2026-10-27 |
| [**🆕 herdr-turn-coordinator**](https://github.com/KarthusLorin/herdr-turn-coordinator)<br><sub>KarthusLorin</sub> | Preserve interactive Herdr agent TUIs without model-driven status polling | `ai-agents` `python` | 1 | 2026-09-18 |
| [**🆕 shop-plugin**](https://github.com/kyrosle/shop-plugin)<br><sub>kyrosle</sub> | A visible multi-agent workstation for Pi + Herdr, with configurable Lead/Worker models, file-based task handoffs, and explicit review. Local alpha. | `coding-agent` `developer-tools` `human-in-the-loop` `multi-agent` `pi-coding-agent` | 1 | 2026-09-27 |
| [**herdr-panel**](https://github.com/lukeda/herdr-panel)<br><sub>lukeda</sub> | Your herdr agents and their status in your desktop panel (KDE Plasma 6, more desktops coming) | `ai-agents` `kde` `kde-plasma` `plasma` `plasmoid` | 1 | 🔄 2026-10-16 |
| [**sheprd**](https://github.com/m-mohamed/sheprd)<br><sub>m-mohamed</sub> | Keep Pi, Codex, Claude Code, and OpenCode in one visible, isolated Herdr Flok. | `agent-tools` `claude-code` `cli` `codex` `coding-agents` | 1 | 2026-08-25 |
| [**herdr-matrix**](https://github.com/madebygrant/herdr-matrix)<br><sub>madebygrant</sub> | Herdr Matrix. Your agents become Smith, Brown and Jones, with Matrix status text and digital rain when idle. | `ai-agents` `matrix` `terminal` `python` | 1 | 2026-10-13 |
| [**🆕 herdr-agents-preview**](https://github.com/maedana/herdr-agents-preview)<br><sub>maedana</sub> | Multi-agent terminal preview dashboard for Herdr: all running agents shown at once, with the selected agent taking most of the width. | `rust` | 1 | 2026-08-14 |
| [**🆕 herdr-standup**](https://github.com/natori-hrj/herdr-standup)<br><sub>natori-hrj</sub> | Agent standup for herdr — a per-agent digest of commits and uncommitted work across your agents' repos. | `ai-agents` `git` `standup` `rust` | 1 | 2026-07-23 |
| [**herdr-tournament**](https://github.com/neospeed83/herdr-tournament)<br><sub>neospeed83</sub> | Adversarial multi-agent code reviews for Herdr | `rust` | 1 | 2026-08-29 |
| [**🆕 paneyard**](https://github.com/nicholasjstock/paneyard)<br><sub>nicholasjstock</sub> | Queue coding tasks and run them in parallel as interactive agent sessions you can watch, steer, and resume. | `ruby` | 1 | 🔄 2026-10-26 |
| [**🆕 herdr-caffeinate**](https://github.com/nwarwick/herdr-caffeinate)<br><sub>nwarwick</sub> | Prevent macOS system sleep while Herdr agents are working | `caffeinate` `coding-agents` `macos` `shell` | 1 | 2026-07-29 |
| [**🆕 herdr-spawn**](https://github.com/nytafar/herdr-spawn)<br><sub>nytafar</sub> | One MCP tool that hands a prompt from a chat to a real Claude Code session on one of your hosts, with Remote Control on. | `python` | 1 | 2026-08-21 |
| [**🆕 herdr-plugins**](https://github.com/paniolo-ai/herdr-plugins)<br><sub>paniolo-ai</sub> | Paniolo plugins for Herdr: live status footers for coding agents and direct Obsidian links. | `claude-code` `codex` `coding-agents` `cursor` `devin` | 1 | 🔄 2026-10-21 |
| [**🆕 herdr-agent-panel**](https://github.com/patrikbraborec/herdr-agent-panel)<br><sub>patrikbraborec</sub> | herdr plugin: per-agent side panel with context usage, connectors, skills (update/remove via npx skills), sandbox info, and diffs of files the agent changed | `claude-code` `python` | 1 | 🔄 2026-10-28 |
| [**🆕 herdr-tasks**](https://github.com/pinkpixel-dev/herdr-tasks)<br><sub>pinkpixel-dev</sub> | A Herdr plugin that puts your agent's task list in a split pane beside it, checked off as the agent works. | `ai` `ai-agents` `antigravity` `claude-code` `cli` | 1 | 2026-09-19 |
| [**🆕 herdr-discord**](https://github.com/ralphilius/herdr-discord)<br><sub>ralphilius</sub> | Herdr plugin: Discord as a UI layer — channels are workspaces, threads spawn agents | `discord` `javascript` | 1 | 2026-09-26 |
| [**herdr-imebox**](https://github.com/Sawakee/herdr-imebox)<br><sub>Sawakee</sub> | IME-friendly pop-up text box for typing Japanese/CJK into AI agent panes in herdr | `cjk` `ime` `input-method` `japanese` `ratatui` | 1 | 2026-07-17 |
| [**🆕 herdr-llm-lint**](https://github.com/shindakun/herdr-llm-lint)<br><sub>shindakun</sub> | Lints CLAUDE.md, AGENTS.md, and agent instruction files for stale paths, commands, facts, and drift | `agents-md` `ai-agents` `claude-code` `claude-md` `cli` | 1 | 2026-09-21 |
| [**herdr-testrun**](https://github.com/shindakun/herdr-testrun)<br><sub>shindakun</sub> | Herdr plugin. Runs a project's tests in a pane, lists the failures, sends them to the agent on one key. | `go` `nodejs` `rust` | 1 | 2026-09-20 |
| [**🆕 mimo-code-herdr**](https://github.com/ShinoharaHaruna/mimo-code-herdr)<br><sub>ShinoharaHaruna</sub> | MiMo Code <-> herdr custom-agent bridge: lifecycle state in the sidebar, crash-proof exit cleanup, one-command spawn | `ai-agents` `cli` `coding-agent` `mimo` `mimocode` | 1 | 2026-10-04 |
| [**🆕 agent-letterbox-herdr**](https://github.com/SimonMallas/agent-letterbox-herdr)<br><sub>SimonMallas</sub> | Agent-to-agent mail with Queryable Envelope Memory (QEM) for AI coding teams in Herdr: durable letters, a doorbell, and one read-only query over the team's sha… | `agent-communication` `agent-coordination` `agent-letterbox` `agent-memory` `agent-orchestration` | 1 | 🔄 2026-10-26 |
| [**🆕 herdr-awake**](https://github.com/susomejias/herdr-awake)<br><sub>susomejias</sub> | Herdr plugin: keep the machine awake while Herdr agents are busy | `shell` | 1 | 2026-08-26 |
| [**🆕 herdr-orc**](https://github.com/tamdogood/herdr-orc)<br><sub>tamdogood</sub> | A minimal, profile-driven custom orchestrator for Herdr | `ai-agents` `multi-agent` `orchestrator` `javascript` | 1 | 2026-08-11 |
| [**🆕 recess**](https://github.com/tatsuro-ueda/recess)<br><sub>tatsuro-ueda</sub> | A herdr plugin. AI works, you take recess. Your video plays by itself while the agents work, and pauses to bring you back to the terminal when herdr calls. | `ai-agents` `applescript` `launchd` `macos` `netflix` | 1 | 🔄 2026-10-27 |
| [**herdr-group-chat**](https://github.com/terry-li-hm/herdr-group-chat)<br><sub>terry-li-hm</sub> | A shared local Herdr room for Pi, Claude Code, Codex, and Grok Build. | `ai-agents` `claude-code` `codex` `grok` `multi-agent` | 1 | 🔄 2026-10-22 |
| [**🆕 tinysend-herdr**](https://github.com/tiny-send/tinysend-herdr)<br><sub>tiny-send</sub> | herdr plugin: email yourself when an agent blocks/finishes, reply to unblock it. Powered by tinysend. | `ai-agents` `tinysend` `javascript` | 1 | 2026-06-26 |
| [**herdr-plugin-agent-spawn**](https://github.com/varvand/herdr-plugin-agent-spawn)<br><sub>varvand</sub> | Open several Herdr agent panes from one prompt | `python` | 1 | 2026-10-08 |
| [**herdr-polyglot**](https://github.com/wazum/herdr-polyglot)<br><sub>wazum</sub> | Write coding-agent prompts in your own language — DeepL or Google Cloud Translate translates them to English and delivers them into Claude Code, Codex or any h… | `ai-agents` `bubbletea` `bubbletea-tui` `claude-code` `codex` | 1 | 2026-09-01 |
| [**🆕 herdr-session-titles**](https://github.com/wxomi/herdr-session-titles)<br><sub>wxomi</sub> | Rich session titles & task context for Devin, Cursor, Agy, Kiro, and Claude in Herdr | `ai-agents` `terminal` `python` | 1 | 2026-10-05 |
| [**🆕 herdr-derby**](https://github.com/xzedx/herdr-derby)<br><sub>xzedx</sub> | Send one prompt to every coding agent in the current Herdr tab and watch them race: a popup to type in, live timers and finishing ranks on the pane borders. | `coding-agents` `rust` | 1 | 🔄 2026-10-23 |
| [**🆕 herdr-fleet-plugin**](https://github.com/yarrasys/herdr-fleet-plugin)<br><sub>yarrasys</sub> | herdr plugin: start, restart and swap a team of named coding agents from a per-repository fleet file (.herdr/fleet.toml) | `coding-agents` `multi-agent` `python` | 1 | 🔄 2026-10-26 |
| [**agent-mail**](https://github.com/youssef-tharwat/agent-mail)<br><sub>youssef-tharwat</sub> | Durable mail and work records for coding agents. Local, compact, runtime-independent. | `agent-skill` `rust` | 1 | 2026-10-09 |
| [**🆕 fence**](https://github.com/zenodea/fence)<br><sub>zenodea</sub> | Contained herdr sessions (bubblewrap + nftabels) | `ai-agents` `bubblewrap` `claude-code` `nftables` `sandbox` | 1 | 2026-10-05 |
| [**🆕 herdr-roles**](https://github.com/zeromountain/herdr-roles)<br><sub>zeromountain</sub> | herdr plugin: assign roles to panes, spawn a team from the main pane, and hand work between roles | `python` | 1 | 🔄 2026-10-26 |

<details><summary>Also relevant to this purpose</summary>

- [ZingerLittleBee/Heeler](https://github.com/ZingerLittleBee/Heeler) — Native iOS agent console for herdr — watch and drive the coding agents on your machines over SSH, with a real…
- [a2u/herdr-jira](https://github.com/a2u/herdr-jira) — Jira TUI plugin for herdr — browse issues with configurable JQL filters, search, change statuses, and delegat…
- [e2b-dev/herdr-e2b-sandbox](https://github.com/e2b-dev/herdr-e2b-sandbox) — herdr plugin that mirrors a git worktree into an E2B sandbox — one box or a branch-per-agent fleet, with a TU…
- [walcew/herdr-assist](https://github.com/walcew/herdr-assist) — Physical desk panel for Herdr, the terminal multiplexer for AI coding agents — shows session state in color a…
- [miko-misa/herdr-portfwd](https://github.com/miko-misa/herdr-portfwd) — Automatic SSH port forwarding for coding agents on remote machines: Ctrl+click the localhost URL your agent p…
- [spad-0x/herdr-mobile-pro](https://github.com/spad-0x/herdr-mobile-pro) — A high-performance, mobile-first PWA dashboard with a Cyber-Dark design for orchestrating Herdr and autonomou…
- [hasuwini77/worktree-fleet](https://github.com/hasuwini77/worktree-fleet) — Parallel Claude Code / Codex builds on Herdr: /herd splits a task into worktree buckets, plus a live fleet po…
- [romiluz13/instinct-herdr-tunnel](https://github.com/romiluz13/instinct-herdr-tunnel) — Let an AI assistant such as Instinct watch and steer your Herdr coding agents: a loopback portal with a 26-ac…
- [DnzzL/herdr-huddle](https://github.com/DnzzL/herdr-huddle) — Live Share for your coding agent: open a Herdr pane to teammates — they watch it live, steer it, and a GitHub…
- [virtualboard/herdr-virtualboard](https://github.com/virtualboard/herdr-virtualboard) — Kanban board for VirtualBoard feature specs inside Herdr: columns are the lifecycle, cards are specs, and dis…
- [zyrre/corgi](https://github.com/zyrre/corgi) — A compact dashboard for Herdr coding agents, with supervisor coordination and an Omarchy bar widget.

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-worktree"></a>

## Git Worktrees & Branches

> I want to spin up a worktree for each piece of work, and have the cleanup handled automatically too

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-worktrunk**](https://github.com/devashish2203/herdr-worktrunk)<br><sub>devashish2203</sub> | Herdr Plugin to integrate worktrunk for git worktree management | `powershell` | 191 | 2026-10-06 |
| [**herdr-plugin-jj-workspace**](https://github.com/NathanFlurry/herdr-plugin-jj-workspace)<br><sub>NathanFlurry</sub> | Create and remove Jujutsu (jj) workspaces as Herdr workspaces | `jujutsu` `rust` | 48 | 2026-09-03 |
| [**herdr-plugin-renamer**](https://github.com/wyattjoh/herdr-plugin-renamer)<br><sub>wyattjoh</sub> | Renames an auto-generated herdr worktree branch and workspace from the agent's first prompt, via on-device Apple FoundationModels or Codex. | `rust` | 20 | 🔄 2026-10-26 |
| [**herdr-e2b-sandbox**](https://github.com/e2b-dev/herdr-e2b-sandbox)<br><sub>e2b-dev</sub> | herdr plugin that mirrors a git worktree into an E2B sandbox — one box or a branch-per-agent fleet, with a TUI dashboard | `cli` `cloud-dev` `e2b` `git-worktree` `integration` | 14 | 2026-09-29 |
| [**jj-waltz**](https://github.com/EzraCerpac/jj-waltz)<br><sub>EzraCerpac</sub> | A Jujutsu workspace switcher inspired by Worktrunk | `cli` `jj` `jujitsu` `utility` `workspace` | 10 | 🔄 2026-10-14 |
| [**bercail**](https://github.com/simoncrypta/bercail)<br><sub>simoncrypta</sub> | Herdr-based agentic development environment | `agentic-ide` `agentic-workflow` `herdr-integration` `omarchy` `pstack` | 8 | 🔄 2026-10-23 |
| [**herdr-plugin-git-worktree-hooks**](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks)<br><sub>freethinkel</sub> | Run shell commands when a git worktree is created/removed — one YAML config for all projects, living outside any repo. | `git-worktree` `javascript` | 7 | 2026-07-06 |
| [**herdr-symlink-worktree**](https://github.com/hmu332233/herdr-symlink-worktree)<br><sub>hmu332233</sub> | A herdr plugin that symlinks shared local files from your main repo into new worktrees. | `shell` | 7 | 2026-07-16 |
| [**herdr-worktree-setup**](https://github.com/lamngockhuong/herdr-worktree-setup)<br><sub>lamngockhuong</sub> | Herdr plugin that prepares every new worktree: auto-detected config files, shared-directory links, and opt-in setup commands | `dotenv` `git-worktree` `monorepo` `javascript` | 7 | 🔄 2026-10-28 |
| [**herdr-worktree-agents**](https://github.com/minhtran3124/herdr-worktree-agents)<br><sub>minhtran3124</sub> | herdr plugin: top-right panel of every git worktree with agent state, PR/CI and git status | `ai-agents` `claude-code` `git-worktree` `ratatui` `rust` | 7 | 2026-09-30 |
| [**herdr-worktree-from-pr**](https://github.com/tdi/herdr-worktree-from-pr)<br><sub>tdi</sub> | Create a git worktree from a GitHub PR and open it as a herdr workspace | `javascript` | 7 | 2026-09-11 |
| [**herdr-worktree-hooks**](https://github.com/timofey-TK/herdr-worktree-hooks)<br><sub>timofey-TK</sub> | herdr plugin: run custom setup/teardown commands when a git worktree is created, opened, or removed | `developer-tools` `git-worktree` `worktree` `python` | 6 | 2026-07-17 |
| [**herdr-worktree-seed**](https://github.com/jlimas/herdr-worktree-seed)<br><sub>jlimas</sub> | Herdr plugin that seeds new worktrees with copy-on-write node_modules and configurable local dotfiles | `developer-tools` `dotfiles` `git-worktree` `nodejs` `typescript` | 5 | 2026-07-28 |
| [**herdr-jj-status**](https://github.com/mroth/herdr-jj-status)<br><sub>mroth</sub> | herdr plugin: show the Jujutsu bookmark/status for jj workspaces in the spaces sidebar | `shell` | 5 | 2026-07-28 |
| [**herdr-worktreeinclude**](https://github.com/tanshio/herdr-worktreeinclude)<br><sub>tanshio</sub> | Herdr plugin: copy gitignored files matching .worktreeinclude into newly created worktrees | `worktree` `worktreeiclude` `shell` | 5 | 2026-07-11 |
| [**herdr-remote-worktrunk**](https://github.com/ditwrd/herdr-remote-worktrunk)<br><sub>ditwrd</sub> | Herdr remote worktrunk workspace | `shell` | 4 | 2026-07-10 |
| [**herdr-pi-tree**](https://github.com/edxeth/herdr-pi-tree)<br><sub>edxeth</sub> | A sidebar that shows your Pi agents as a tree — who spawned whom, which worktree is which branch, who's waiting on you. | `git-worktrees` `pi` `pi-coding-agent` `sidebar` `terminal` | 4 | 🔄 2026-10-28 |
| [**herdr-plugin-cow-worktree**](https://github.com/khatriafaz/herdr-plugin-cow-worktree)<br><sub>khatriafaz</sub> | Herdr plugin for strict copy-on-write Git worktrees that include ignored local files | `typescript` | 4 | 2026-09-20 |
| [**herdr-jj**](https://github.com/OliverGilan/herdr-jj)<br><sub>OliverGilan</sub> | Jujutsu workspace support for Herdr | `jujutsu` `rust` | 4 | 2026-10-12 |
| [**herdr-fresh-worktree**](https://github.com/persiyanov/herdr-fresh-worktree)<br><sub>persiyanov</sub> | Reset a newly created herdr worktree to the latest origin default branch. | `javascript` | 4 | 2026-06-25 |
| [**herdr-opendeck**](https://github.com/Resilient-Software/herdr-opendeck)<br><sub>Resilient-Software</sub> | Mirror Herdr workspaces onto a Stream Deck. Live tiles with repository, branch and agent status. | `elgato` `opendeck` `stream-deck` `typescript` | 4 | 🔄 2026-10-19 |
| [**herdr-quartermaster**](https://github.com/travisjeffery/herdr-quartermaster)<br><sub>travisjeffery</sub> | Herdr plugin: one coordinator, a worktree and agent per bead, beads as the only record | `go` | 4 | 🔄 2026-10-28 |
| [**herdr-worktreeinclude**](https://github.com/eightHundreds/herdr-worktreeinclude)<br><sub>eightHundreds</sub> | Herdr plugin: copy .worktreeinclude-selected gitignored files into new worktrees | `worktree` `rust` | 3 | 2026-07-28 |
| [**herdr-multirepo**](https://github.com/jattento/herdr-multirepo)<br><sub>jattento</sub> | One feature branch across many repositories, in one Herdr workspace | `git-worktree` `python` | 3 | 2026-08-03 |
| [**herdr-wish**](https://github.com/MovieHolic-Plex/herdr-wish)<br><sub>MovieHolic-Plex</sub> | Herdr plugin. Make a wish and omo commits a PR. omo-10 opens 10 worktrees. | `omo` `wish` `javascript` | 3 | 2026-10-09 |
| [**herdr-branch-cleanup**](https://github.com/osolmaz/herdr-branch-cleanup)<br><sub>osolmaz</sub> | Checkout the default branch when a pane's branch is merged or deleted on GitHub | `git` `github` `rust` | 3 | 2026-07-26 |
| [**herdr-worktree-lifecycle**](https://github.com/qdentity/herdr-worktree-lifecycle)<br><sub>qdentity</sub> | Herdr plugin: dispatch worktree lifecycle events to repo-owned setup/teardown wrappers | `rust` | 3 | 2026-06-29 |
| [**herdr-worktree-nav**](https://github.com/ShoMasegi/herdr-worktree-nav)<br><sub>ShoMasegi</sub> | _(no description)_ | `terminal` `rust` | 3 | 🔄 2026-10-19 |
| [**herdr-worktree-copy**](https://github.com/crexi/herdr-worktree-copy)<br><sub>crexi</sub> | Herdr plugin that copies and symlinks worktree-local files from a .worktree-copy manifest | `git-worktree` `shell` | 2 | 2026-07-28 |
| [**herdr-deck**](https://github.com/ctbaum/herdr-deck)<br><sub>ctbaum</sub> | The companion workspace launcher for herdr-agents.nvim: open or resume Claude, Codex, and Pi in a ready-made Neovim, agent, and shell deck. | `claude-code` `codex` `coding-agents` `git-worktree` `neovim` | 2 | 🔄 2026-10-24 |
| [**trunkr**](https://github.com/disintegrator/trunkr)<br><sub>disintegrator</sub> | Herdr 🤝 Worktrunk | `go` | 2 | 2026-08-12 |
| [**herdr-tagr**](https://github.com/dvoets/herdr-tagr)<br><sub>dvoets</sub> | Concise, icon-first tab titles for herdr: app icon + git branch + folder | `rust` `terminal` | 2 | 2026-10-09 |
| [**herdr-plugin-jj-workspace**](https://github.com/expnn/herdr-plugin-jj-workspace)<br><sub>expnn</sub> | A Herdr plugin to create and remove Jujutsu (jj) workspaces | `rust` | 2 | 2026-09-30 |
| [**herdr-gc**](https://github.com/H3xept/herdr-gc)<br><sub>H3xept</sub> | Run your own steps when a git worktree is created, opened, closed or removed in herdr: install, suggest cleanup, classify | `git-worktree` `terminal` `javascript` | 2 | 🔄 2026-10-18 |
| [**🆕 jumar**](https://github.com/joshbarrington/jumar)<br><sub>joshbarrington</sub> | A fast terminal UI for managing git worktrees | `claude-code-plugin` `cli` `git` `git-worktree` `rust` | 2 | 🔄 2026-10-27 |
| [**herdr-inbox**](https://github.com/lucasscariot/herdr-inbox)<br><sub>lucasscariot</sub> | Herdr plugin: start agent threads on any project, harness, machine, or worktree, and follow every agent in one live inbox | `blueprint` `coding-agents` `python` `tui` `rust` | 2 | 🔄 2026-10-17 |
| [**herdr-shear**](https://github.com/mcc0x/herdr-shear)<br><sub>mcc0x</sub> | Find the git worktrees that are safe to delete, and delete those. A worktree janitor for herdr. | `cleanup` `git-worktree` `rust` `terminal` | 2 | 🔄 2026-10-16 |
| [**herdr-worktreeinclude**](https://github.com/serhii-chernenko/herdr-worktreeinclude)<br><sub>serhii-chernenko</sub> | Allow custom path for new worktrees and respects `.worktreeinclude` file like Claude CLI does | `worktree` `shell` | 2 | 🔄 2026-10-14 |
| [**herdr-plugin-worktree-bootstrap**](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap)<br><sub>zerodice0</sub> | Safely copy ignored local files and run setup commands in new Herdr Git worktrees | `python` | 2 | 🔄 2026-10-17 |
| [**🆕 herdr-corral**](https://github.com/bfreed/herdr-corral)<br><sub>bfreed</sub> | Herd your Git worktrees in Herdr: env files, dependencies, agent/shell/server tabs, and merge-safe cleanup. A workmux replacement for Herdr. | `git-worktree` `workmux` `python` | 1 | 2026-10-01 |
| [**🆕 herdr-keep-root**](https://github.com/bonkey/herdr-keep-root)<br><sub>bonkey</sub> | Herdr plugin: keeps a repository's main-checkout workspace open while any of its worktree workspaces is open, so the Spaces panel never flattens a worktree gro… | `shell` | 1 | 2026-09-08 |
| [**herdr-worktree-upstream**](https://github.com/DaveBird99/herdr-worktree-upstream)<br><sub>DaveBird99</sub> | herdr plugin: link a new worktree to its existing origin branch | `shell` | 1 | 2026-10-07 |
| [**🆕 herdr-allow**](https://github.com/Feasy01/herdr-allow)<br><sub>Feasy01</sub> | herdr plugin: copy gitignored files (.env, secrets, local configs) into every new worktree via a .herdr-allow allowlist | `shell` | 1 | 2026-07-02 |
| [**🆕 herdr-glab**](https://github.com/hlouis/herdr-glab)<br><sub>hlouis</sub> | Herdr plugin for GitLab merge requests: a grouped MR panel, worktree checkout, tuicr review, sidebar status, and a tab bar count. All access through the glab C… | `cli` `gitlab` `golang` `go` | 1 | 2026-09-19 |
| [**🆕 nexus**](https://github.com/IniZio/nexus)<br><sub>IniZio</sub> | Herdr plugin for running worktree in Cloud-Hypervisor sandboxes, with mem/cpu/disk hotplug and auto port-forwarding | `cloud-hypervisor` `go` | 1 | 2026-10-04 |
| [**🆕 hertrees**](https://github.com/janooh37-hue/hertrees)<br><sub>janooh37-hue</sub> | Every worktree, every agent, one popup. A Herdr plugin for git worktrees, PR state and AI agent sessions. | `git-worktree` `tui` `rust` | 1 | 🔄 2026-10-28 |
| [**🆕 herdr-plugin-layerfs**](https://github.com/jiangkoumo/herdr-plugin-layerfs)<br><sub>jiangkoumo</sub> | Copy-on-write LayerFS branches as Herdr workspaces, grouped under the repo like worktrees and restored after restart. | `ai-agents` `copy-on-write` `git-worktree` `layerfs` `javascript` | 1 | 🔄 2026-10-26 |
| [**🆕 herdr-wtm**](https://github.com/LucasPcq/herdr-wtm)<br><sub>LucasPcq</sub> | herdr plugin for wtm (early preview): run your worktree commands from a herdr popup and keep workspaces in sync. One branch, one worktree, one isolated dev sta… | `developer-tools` `git-worktree` `go` `worktree` `wtm` | 1 | 2026-10-04 |
| [**🆕 herdr-standup**](https://github.com/mcc0x/herdr-standup)<br><sub>mcc0x</sub> | A digest of what your agents actually did. One command, one readable summary of every Herdr workspace over a time window — commits, change volume, branch, and… | `git` `rust` `standup` `terminal` | 1 | 🔄 2026-10-16 |
| [**🆕 herdr-pr-worktree**](https://github.com/poislagarde/herdr-pr-worktree)<br><sub>poislagarde</sub> | Open GitHub pull requests as worktree spaces in Herdr, reusing existing checkouts. | `git-worktree` `python` | 1 | 🔄 2026-10-14 |
| [**🆕 herdr-jira-worktree**](https://github.com/spiritsack/herdr-jira-worktree)<br><sub>spiritsack</sub> | herdr plugin: prompt for a Jira ticket, open/reuse a matching git worktree, and prefill it into a fresh Claude Code session | `shell` | 1 | 2026-08-24 |
| [**herdr-worktree-include**](https://github.com/tupton/herdr-worktree-include)<br><sub>tupton</sub> | Symlink or copy untracked files to git worktrees created by herdr. | `shell` | 1 | 2026-09-14 |

<details><summary>Also relevant to this purpose</summary>

- [tdi/herdr-worktree-from-linear](https://github.com/tdi/herdr-worktree-from-linear) — Create a git worktree from a Linear issue and open it as a herdr workspace
- [mrolafsson/herdr-github](https://github.com/mrolafsson/herdr-github) — GitHub pull requests in a herdr popup: merge readiness, checks and reviews, draft toggle, merge or auto-merge…
- [mrolafsson/herdr-linear](https://github.com/mrolafsson/herdr-linear) — Linear issues and projects in a herdr popup: status icons, rendered descriptions, status changes, one key to…
- [hanbong5938/herdr-jira-worktree](https://github.com/hanbong5938/herdr-jira-worktree) — Jira TUI plugin for herdr (fork of a2u/herdr-jira) — JQL filters, search, status transitions, delegate issues…
- [rarce/herdr-crew](https://github.com/rarce/herdr-crew) — herdr plugin: bring up a team of Claude Code sessions, one tab per role, plus a live status board, from a ver…
- [upstash/herdr-upstash-box](https://github.com/upstash/herdr-upstash-box) — Herdr plugin: run a coding agent in an Upstash Box from the worktree you are looking at
- [hasuwini77/worktree-fleet](https://github.com/hasuwini77/worktree-fleet) — Parallel Claude Code / Codex builds on Herdr: /herd splits a task into worktree buckets, plus a live fleet po…
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — Automatically bootstrap Herdr worktrees for JavaScript and TypeScript with lockfile-aware installs and safe e…
- [mohaphez/herdr-flow](https://github.com/mohaphez/herdr-flow) — Persistent multi-agent task coordination for Herdr with guarded review and worktree cleanup
- [tomasvarga/herdr-e2b](https://github.com/tomasvarga/herdr-e2b) — Mirror a git worktree into a fresh E2B cloud sandbox on demand — a snapshot upload (uncommitted changes and a…
- [poislagarde/herdr-worktree-cleanup](https://github.com/poislagarde/herdr-worktree-cleanup) — Automatically clean up safe GitHub PR worktrees when their Herdr space closes. Python, no dependencies, MIT.
- [Tarektouati/herdr-pr-modal](https://github.com/Tarektouati/herdr-pr-modal) — Open any pull request in its own worktree, straight from a Herdr
- [ZviBaratz/herdr-draft](https://github.com/ZviBaratz/herdr-draft) — herdr plugin: a new-session creation dialog — Linear issue, worktree, placement, agent kind, clauth account a…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-review"></a>

## Code Review & Diffs

> I want to read the diff an agent wrote and send comments back on it

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**crabbox**](https://github.com/openclaw/crabbox)<br><sub>openclaw</sub> | Crabbox: warm a box, sync the diff, run the suite. | `agent-skills` `remote-test-runner` `go` | 1507 | 🔄 2026-10-28 |
| [**herdr-reviewr**](https://github.com/persiyanov/herdr-reviewr)<br><sub>persiyanov</sub> | Review your agent's diff in a terminal pane and send comments back to Claude Code, Codex, OpenCode or Pi. A herdr plugin. | `agentic-coding` `ai-agents` `claude-code` `cli` `code-review` | 955 | 🔄 2026-10-28 |
| [**herdr-annotate**](https://github.com/plannotator/herdr-annotate)<br><sub>plannotator</sub> | Annotate terminal text, review documents and agent replies in Herdr, and send the feedback straight back to the agent. | `annotation` `multiplexer` `rust` | 710 | 🔄 2026-10-28 |
| [**roamgate**](https://github.com/powerfooI/roamgate)<br><sub>powerfooI</sub> | A Herdr client for any screen. Control terminals, monitor coding agents, and review files and diffs from desktop or mobile. | `ai-agents` `bun` `code-review` `developer-tools` `git-worktree` | 321 | 🔄 2026-10-27 |
| [**herdr-hunk-diff**](https://github.com/jhochenbaum/herdr-hunk-diff)<br><sub>jhochenbaum</sub> | Review agent-authored changes in hunk from herdr and send inline comments back to the responsible agent. | `code-review` `hunk` `typescript` | 148 | 🔄 2026-10-28 |
| [**herdr-plannotator**](https://github.com/plannotator/herdr-plannotator)<br><sub>plannotator</sub> | Open Plannotator reviews inside Herdr Browser panes. | `plannotator` `typescript` | 26 | 2026-07-29 |
| [**herdr-gitview**](https://github.com/ChmaraX/herdr-gitview)<br><sub>ChmaraX</sub> | Git status/diff panel for herdr - review changes, edit in nvim, stage/commit/discard, all from the terminal | `git` `git-diff` `git-tui` `neovim` `rust` | 21 | 🔄 2026-10-23 |
| [**herdr-pickr**](https://github.com/tomasvarga/herdr-pickr)<br><sub>tomasvarga</sub> | A PR review router for herdr — Ctrl+click a GitHub PR / GitLab MR link and pick a reviewer (tuicr · hunk · diff · browser · or your own tool), with an optional… | `cli` `code-review` `pull-request` `tui` `shell` | 20 | 2026-07-13 |
| [**herdr-plugin-hunk**](https://github.com/edmundmiller/herdr-plugin-hunk)<br><sub>edmundmiller</sub> | Herdr plugin for opening Hunk diffs in split panes or tabs | `python` | 15 | 2026-06-23 |
| [**herdr-extensions**](https://github.com/vonzelle-vzt/herdr-extensions)<br><sub>vonzelle-vzt</sub> | Tiny VS Code for herdr: a real editor with LSP diagnostics, autocomplete, rename and go-to-definition — plus source control, search, problems, tests, a debugge… | `agent-tools` `autocomplete` `claude-code` `cli` `code-review` | 7 | 🔄 2026-10-25 |
| [**herdr-plugin-hunk-autodiff**](https://github.com/scott306lr/herdr-plugin-hunk-autodiff)<br><sub>scott306lr</sub> | Herdr plugin: auto-open a hunk diff split when a coding agent finishes with uncommitted changes | `claude-code` `hunk` `python` | 5 | 2026-07-05 |
| [**herdr-progressive-reviewer**](https://github.com/flupke/herdr-progressive-reviewer)<br><sub>flupke</sub> | Turns based diff reviewer inspired by Tidewave | `rust` | 4 | 🔄 2026-10-28 |
| [**herdr-review**](https://github.com/alexeyco/herdr-review)<br><sub>alexeyco</sub> | Review agent-authored Git diffs in Herdr with revdiff, tuicr, or lumen | `ai-agents` `code-review` `coding-agents` `developer-tools` `git-diff` | 3 | 🔄 2026-10-23 |
| [**huicr**](https://github.com/claytonjschneider/huicr)<br><sub>claytonjschneider</sub> | Herdr User Interface for Code Review | `python` | 3 | 2026-10-01 |
| [**herdr-review.nvim**](https://github.com/inferst/herdr-review.nvim)<br><sub>inferst</sub> | Code review UI for Neovim with Git and herdr integration | `lua` | 3 | 2026-08-01 |
| [**herdr-review**](https://github.com/quantk/herdr-review)<br><sub>quantk</sub> | Review agent-authored changes in Hunk and send inline feedback back through Herdr | `code-review` `hunk` `javascript` | 3 | 2026-07-28 |
| [**easy-review**](https://github.com/VilfredSikker/easy-review)<br><sub>VilfredSikker</sub> | Git diff review for AI-assisted coding. Terminal TUI and Tauri desktop app. | `ai-code-review` `cli` `code-review` `desktop-app` `developer-tools` | 3 | 🔄 2026-10-28 |
| [**herdr-hunk**](https://github.com/yuucu/herdr-hunk)<br><sub>yuucu</sub> | herdr plugin: toggle Hunk diff reviews for your agent workspaces | `diff` `hunk` `go` | 3 | 2026-10-01 |
| [**magnum**](https://github.com/zhuravel/magnum)<br><sub>zhuravel</sub> | Your AI coding agents as a pull-request review team: Claude Code, Codex and others review each push in herdr panes, a judge proves every finding, one GitHub re… | `ai-agents` `ai-code-review` `bubbletea` `claude-code` `cli` | 3 | 🔄 2026-10-28 |
| [**herdr-stagr**](https://github.com/brianh20/herdr-stagr)<br><sub>brianh20</sub> | Source Control sidebar for herdr: stage, unstage, and discard with side-by-side diffs | `git` `tui` `rust` | 2 | 2026-08-06 |
| [**🆕 diffui**](https://github.com/dgsienko/diffui)<br><sub>dgsienko</sub> | Locally hosted web tool and terminal ui for reviewing live diffs and improving your agentic coding and review flow. | `agentic-coding` `ai-agents` `ai-tools` `claude-code` `cli` | 2 | 🔄 2026-10-23 |
| [**herdr-git-tree**](https://github.com/ExLuna-rs/herdr-git-tree)<br><sub>ExLuna-rs</sub> | Interactive git graph with real-time diffs and branch management — herdr plugin | `git` `rust` `tui` | 2 | 2026-10-01 |
| [**herdr-tasks**](https://github.com/husniadil/herdr-tasks)<br><sub>husniadil</sub> | Task backlog and notes board for coding agents on Herdr - claims with leases, evidence-backed review, and a human decision gate, in one Go binary. | `ai-agents` `mcp-server` `notes` `sqlite` `task-management` | 2 | 2026-08-30 |
| [**herdr-pr-tracker**](https://github.com/jakekroon/herdr-pr-tracker)<br><sub>jakekroon</sub> | Every open pull request you have authored, docked and colour-coded by what needs you. A Herdr plugin. | `bun` `code-review` `developer-tools` `github` `pull-requests` | 2 | 🔄 2026-10-28 |
| [**herdr-scribe**](https://github.com/Javamomma/herdr-scribe)<br><sub>Javamomma</sub> | herdr plugin: live no-recording meeting transcription — mic → RAM-only transcript + live analyst panes; on stop: meeting note, optional policy gate, reviewable… | `macos` `meeting-notes` `privacy` `speech-to-text` `terminal` | 2 | 2026-08-07 |
| [**herdr-router**](https://github.com/Qingswe/herdr-router)<br><sub>Qingswe</sub> | Route coding tasks to the right agent, model, and effort by difficulty and duration, with a visual web policy editor. | `python` | 2 | 2026-10-12 |
| [**herdr-comments**](https://github.com/shadowfax92/herdr-comments)<br><sub>shadowfax92</sub> | Annotate copied Herdr terminal output, collect per-pane comments, and review them in Neovim. | `ai-agents` `annotations` `neovim` `rust` `terminal` | 2 | 2026-10-13 |
| [**herdr-lazygit-viewer**](https://github.com/tareqmlx/herdr-lazygit-viewer)<br><sub>tareqmlx</sub> | Opens lazygit at the files, branches, commits, or stash panel, in whichever Herdr surface suits the moment. | `code-review` `lazygit` `rust` | 2 | 2026-08-14 |
| [**herdr-pr-ops**](https://github.com/tferreira/herdr-pr-ops)<br><sub>tferreira</sub> | PR//OPS - pull request mission control for Herdr: your PRs and review requests on one board, one-key agents in Herdr panes | `ai-agents` `claude-code` `code-review` `codex` `dashboard` | 2 | 🔄 2026-10-15 |
| [**roboherd**](https://github.com/andschneider/roboherd)<br><sub>andschneider</sub> | roborev review status and actions inside your herdr workspace | `rust` `tui` | 1 | 2026-09-20 |
| [**herdr-agent-diff**](https://github.com/baotran01/herdr-agent-diff)<br><sub>baotran01</sub> | Herdr plugin for inspecting agent filesystem and Git diffs | `rust` | 1 | 2026-08-03 |
| [**🆕 Vincent**](https://github.com/chasereyn/Vincent)<br><sub>chasereyn</sub> | A mouse-first terminal client for reviewing code that AI agents wrote, and fixing it in place | `go` | 1 | 2026-09-03 |
| [**🆕 herdr-review-panel**](https://github.com/Deetss/herdr-review-panel)<br><sub>Deetss</sub> | Herdr plugin: a Review Queue panel for files to look at and commands to run yourself, flagged by Claude Code | `claude-code` `ratatui` `rust` `tui` | 1 | 🔄 2026-10-22 |
| [**herdr-peer-review**](https://github.com/Elio2000/herdr-peer-review)<br><sub>Elio2000</sub> | Open a second coding agent in a herdr pane and have it review your diff — watchable, auto-approve, read-only. Ships a Claude Code skill for the autonomous revi… | `agent-skills` `ai-agents` `claude-code` `code-review` `codex` | 1 | 2026-07-16 |
| [**codeMap**](https://github.com/Jenish-Shobhit/codeMap)<br><sub>Jenish-Shobhit</sub> | herdr plugin that shows your code as a map and flowcharts, and reviews what your coding agents changed, in one popup over the agent's pane. | `ai-agents` `code-review` `code-visualization` `developer-tools` `git` | 1 | 🔄 2026-10-18 |
| [**herdr-git-graph**](https://github.com/jorge-huxley/herdr-git-graph)<br><sub>jorge-huxley</sub> | Read-only git graph TUI plugin for Herdr with colored ASCII lanes, branch filter, search, and on-demand diffs. | `rust` | 1 | 2026-07-17 |
| [**🆕 herdr-sidekick**](https://github.com/minhtran3124/herdr-sidekick)<br><sub>minhtran3124</sub> | herdr plugin: side panels for coding agents — worktrees, changed files with diffs, and Claude Code subagents | `rust` | 1 | 🔄 2026-10-28 |
| [**🆕 agentflock**](https://github.com/neospark-sol/agentflock)<br><sub>neospark-sol</sub> | AI-coordinated builder and reviewer groups with durable milestone control | `ai-agents` `pair-programming` `typescript` | 1 | 2026-08-21 |
| [**herdr-gitdeck**](https://github.com/pgen0x/herdr-gitdeck)<br><sub>pgen0x</sub> | herdr plugin: review, stage and commit diffs across every git repo in a folder, and send line comments to your coding agent | `git` `ratatui` `rust` `tui` | 1 | 🔄 2026-10-16 |
| [**🆕 herdr-devin-board**](https://github.com/rigelstpierre/herdr-devin-board)<br><sub>rigelstpierre</sub> | herdr plugin: your Devin Cloud sessions with live PR, CI, and review status | `devin` `go` | 1 | 2026-10-02 |
| [**codey**](https://github.com/rodeyseijkens/codey)<br><sub>rodeyseijkens</sub> | A review-first Git TUI (terminal UI) that provides a two-section staged/changes diff viewer with transient comments and real Git staging, built on OpenTUI. | `code-review` `opentui` `review-tool` `tui` `typescript` | 1 | 2026-10-01 |
| [**🆕 herdr-git-graph**](https://github.com/sjlee06/herdr-git-graph)<br><sub>sjlee06</sub> | Interactive Git branch and commit graph for Herdr. Rust + Ratatui, smooth curves, search, and diffs. | `git` `git-graph` `ratatui` `rust` `terminal` | 1 | 🔄 2026-10-27 |
| [**herdr-hunks**](https://github.com/winoooops/herdr-hunks)<br><sub>winoooops</sub> | A Git hunk viewer for Herdr. Review committed and uncommitted changes, compare branches, and explore diffs in your terminal. | `git` `rust` `tui` | 1 | 2026-10-08 |

<details><summary>Also relevant to this purpose</summary>

- [ericbust/namedrop](https://github.com/ericbust/namedrop) — @mentions for Codex, Claude Code, and your terminal. A Herdr plugin that lets agents in different panes work…
- [jpolec/herdr-plugin-odysseus](https://github.com/jpolec/herdr-plugin-odysseus) — Governed multi-agent workflows for Herdr: tasks → agents in Herdr panes → checks, retries, review, policy, ap…
- [JacquesvanWyk/herdr-hunk](https://github.com/JacquesvanWyk/herdr-hunk) — Interactive fzf picker for hunk diffs in herdr: commits, ranges, stashes, plus auto-open when an agent finish…
- [tomasvarga/herdr-sniffr](https://github.com/tomasvarga/herdr-sniffr) — An AI sniffs your PR for issues before you review — an agentic first-pass that drops draft comments into tuic…
- [mrolafsson/herdr-github](https://github.com/mrolafsson/herdr-github) — GitHub pull requests in a herdr popup: merge readiness, checks and reviews, draft toggle, merge or auto-merge…
- [anhnd3005-infinity/herdr-worker-orchestrator](https://github.com/anhnd3005-infinity/herdr-worker-orchestrator) — Dispatch tasks to CLI agent workers (agy, codex, ...) via Herdr-managed panes with stateful task tracking, wo…
- [itisbryan/herdr-gh-checks](https://github.com/itisbryan/herdr-gh-checks) — Herdr plugin: watch & review the current PR's CI in a pane; CI/merge status on sidebar rows. Go + Bubble Tea.
- [elKei24/herdr-co-review](https://github.com/elKei24/herdr-co-review) — Split-screen PR review in herdr: your agent finds issues, you triage each one next to its code in a TUI, the…
- [mikhail-angelov/herdr-review-loop](https://github.com/mikhail-angelov/herdr-review-loop) — Automated cross-review between agents in a herdr workspace — one writes, the other reviews, repeat.
- [DnzzL/herdr-docket](https://github.com/DnzzL/herdr-docket) — Give a task to a named coding agent: it opens a PR, a second agent verifies it, a merge gate in code merges i…
- [neospeed83/herdr-tournament](https://github.com/neospeed83/herdr-tournament) — Adversarial multi-agent code reviews for Herdr
- [patrikbraborec/herdr-agent-panel](https://github.com/patrikbraborec/herdr-agent-panel) — herdr plugin: per-agent side panel with context usage, connectors, skills (update/remove via npx skills), san…
- [sebassdc/herdr-agent-prs](https://github.com/sebassdc/herdr-agent-prs) — A cross-repo PR viewer for coding agents in Herdr. See every pull request an agent opened or pushed to, in an…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-forge"></a>

## GitHub & Issue Trackers

> I want to kick off work from an issue or PR, and track PR status

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**tsk**](https://github.com/smarzban/tsk)<br><sub>smarzban</sub> | tsk, a Linear alternative that stays in the terminal: a shared task board for you and your agents. TUI for you, CLI for them. | `cli` `productivity` `rust` `task-manager` `terminal` | 237 | 🔄 2026-10-27 |
| [**ghzinga**](https://github.com/osolmaz/ghzinga)<br><sub>osolmaz</sub> | Easy, clickable TUI to view a single GitHub issue or PR, in Rust | `rust` | 90 | 2026-09-06 |
| [**beady-eye**](https://github.com/CodeForBreakfast/beady-eye)<br><sub>CodeForBreakfast</sub> | Draws the work in your beads trackers as trees, with what each agent is doing beside the bead it works. It also watches beads for whatever waits on them, and s… | `agents` `beads` `claude-code` `claude-code-plugin` `github` | 24 | 🔄 2026-10-27 |
| [**herdr-plugin-gh-pr**](https://github.com/wyattjoh/herdr-plugin-gh-pr)<br><sub>wyattjoh</sub> | herdr plugin that shows the focused agent pane's branch GitHub PR status in the sidebar | `typescript` | 23 | 2026-07-16 |
| [**herdr-worktree-from-linear**](https://github.com/tdi/herdr-worktree-from-linear)<br><sub>tdi</sub> | Create a git worktree from a Linear issue and open it as a herdr workspace | `javascript` | 19 | 2026-09-11 |
| [**herdr-plugin-github-start**](https://github.com/ogulcancelik/herdr-plugin-github-start)<br><sub>ogulcancelik</sub> | Herdr plugin that starts Codex or Claude from a GitHub issue, PR, or discussion | `javascript` | 17 | 2026-08-31 |
| [**gitty**](https://github.com/VedangP57/gitty)<br><sub>VedangP57</sub> | A blazing-fast, GitHub-Desktop-style git TUI for the terminal (Rust + Ratatui) | `git` `ratatui` `rust` `terminal` `tui` | 16 | 🔄 2026-10-19 |
| [**herdr-jira**](https://github.com/a2u/herdr-jira)<br><sub>a2u</sub> | Jira TUI plugin for herdr — browse issues with configurable JQL filters, search, change statuses, and delegate issues to AI agents running in your terminal wit… | `ai-agents` `jira` `ratatui` `rust` `tui` | 15 | 2026-09-05 |
| [**herdr-pr-tracker**](https://github.com/Matovidlo/herdr-pr-tracker)<br><sub>Matovidlo</sub> | herdr plugin: track the GitHub PR each Claude Code session produces, with gh state + actions | `claude-code` `shell` | 12 | 🔄 2026-10-22 |
| [**herdr-linear**](https://github.com/JacquesvanWyk/herdr-linear)<br><sub>JacquesvanWyk</sub> | fzf-driven Linear panel in a herdr split pane or tab: search issues, drill into projects, create issues, change status | `shell` | 8 | 2026-07-12 |
| [**herdr-plugins**](https://github.com/JJLiebig/herdr-plugins)<br><sub>JJLiebig</sub> | Herdr plugin that starts Codex or Claude from a GitHub issue, PR, or discussion | `javascript` | 7 | 2026-10-04 |
| [**herdr-sniffr**](https://github.com/tomasvarga/herdr-sniffr)<br><sub>tomasvarga</sub> | An AI sniffs your PR for issues before you review — an agentic first-pass that drops draft comments into tuicr. Agent-agnostic (codex/claude/cursor/grok/…). | `ai` `cli` `code-review` `pull-request` `tuicr` | 6 | 2026-07-14 |
| [**mergr**](https://github.com/jsmenzies/mergr)<br><sub>jsmenzies</sub> | GitHub pull request status for Herdr Space sidebar rows. | `github-pull-requests` `rust` | 5 | 2026-07-30 |
| [**herdr-git-status**](https://github.com/krystof018/herdr-git-status)<br><sub>krystof018</sub> | Surfaces CI status inside herdr for both GitLab (pipelines + merge requests) and GitHub (Actions + pull requests), auto-detected from the repo's origin. | `bash` `ci-cd` `ci-status` `developer-tools` `github-actions` | 5 | 2026-09-20 |
| [**herdr-github**](https://github.com/mrolafsson/herdr-github)<br><sub>mrolafsson</sub> | GitHub pull requests in a herdr popup: merge readiness, checks and reviews, draft toggle, merge or auto-merge, one key to a worktree (forks too), and PR labels… | `bubbletea` `claude-code` `coding-agents` `git-worktree` `github` | 5 | 🔄 2026-10-20 |
| [**herdr-linear**](https://github.com/mrolafsson/herdr-linear)<br><sub>mrolafsson</sub> | Linear issues and projects in a herdr popup: status icons, rendered descriptions, status changes, one key to a worktree, and Start hands the issue to your codi… | `bubbletea` `claude-code` `coding-agents` `git-worktree` `go` | 5 | 🔄 2026-10-20 |
| [**herdr-linear**](https://github.com/talent-factory/herdr-linear)<br><sub>talent-factory</sub> | A Linear issues panel for Herdr, with implement-on-Enter. | `rust` | 5 | 2026-10-10 |
| [**herdr-pr-board**](https://github.com/cdowell09/herdr-pr-board)<br><sub>cdowell09</sub> | Configurable cross-repository GitHub pull request dashboard for Herdr | `github` `tui` `go` | 4 | 🔄 2026-10-21 |
| [**herdr-gh-checks**](https://github.com/itisbryan/herdr-gh-checks)<br><sub>itisbryan</sub> | Herdr plugin: watch & review the current PR's CI in a pane; CI/merge status on sidebar rows. Go + Bubble Tea. | `bubbletea` `ci` `github-actions` `tui` `go` | 4 | 2026-08-25 |
| [**herdr-linear-agent**](https://github.com/civitaspo/herdr-linear-agent)<br><sub>civitaspo</sub> | Herdr plugin that runs a coordinator and per-repository coding agents for Linear issues delegated to its app user. | `linear` `rust` | 3 | 🔄 2026-10-28 |
| [**herdr-co-review**](https://github.com/elKei24/herdr-co-review)<br><sub>elKei24</sub> | Split-screen PR review in herdr: your agent finds issues, you triage each one next to its code in a TUI, the agent posts what you approve. | `cli` `code-review` `pull-request` `rust` `tui` | 3 | 🔄 2026-10-28 |
| [**herdr-jira-worktree**](https://github.com/hanbong5938/herdr-jira-worktree)<br><sub>hanbong5938</sub> | Jira TUI plugin for herdr (fork of a2u/herdr-jira) — JQL filters, search, status transitions, delegate issues to AI agents, and check out issues into git workt… | `jira` `tui` `rust` | 3 | 2026-10-12 |
| [**herdr-beads**](https://github.com/hexsprite/herdr-beads)<br><sub>hexsprite</sub> | Ctrl-click a beads issue ID in Herdr to open its details in a split pane | `beads` `issue-tracker` `terminal` `shell` | 3 | 2026-09-26 |
| [**herdr-pane-issue**](https://github.com/ilazaridis/herdr-pane-issue)<br><sub>ilazaridis</sub> | Herdr plugin: shows the GitHub issue each agent pane is working on in the Agents sidebar, and opens it with one key. | `shell` | 3 | 2026-09-24 |
| [**herdr-plugin-gh-workflow**](https://github.com/kkckkc/herdr-plugin-gh-workflow)<br><sub>kkckkc</sub> | Herdr plugin for GitHub workflow | `javascript` | 3 | 2026-07-03 |
| [**herdr-board**](https://github.com/bredebjorhovd/herdr-board)<br><sub>bredebjorhovd</sub> | Where coding agents queue up and run their own work — GitHub issues in, autonomous agents in herdr panes, PR reviews delivered back to the agent that wrote the… | `rust` | 2 | 2026-08-14 |
| [**herdr-pr-watch**](https://github.com/maxguzenski/herdr-pr-watch)<br><sub>maxguzenski</sub> | Herdr plugin: GitHub PR status of each workspace and agent pane in the sidebar | `github-pull-requests` `python` | 2 | 2026-09-06 |
| [**herdr-issues**](https://github.com/zamarrowski/herdr-issues)<br><sub>zamarrowski</sub> | herdr plugin: browse the GitHub, Linear and Shortcut issues of the repo you're in and hand one to any coding agent (Claude Code, Codex, Gemini…) in its own git… | `coding-agents` `github-issues` `javascript` | 2 | 2026-09-30 |
| [**🆕 herdr-plugin-jira-pr**](https://github.com/abtris/herdr-plugin-jira-pr)<br><sub>abtris</sub> | Herdr plugin: show the Jira issue behind the current branch's PR, and warn when they disagree | `github-pr` `jira` `shell` | 1 | 2026-08-04 |
| [**🆕 herdr-workspace-prs**](https://github.com/andrewbrannan/herdr-workspace-prs)<br><sub>andrewbrannan</sub> | Herdr plugin for tracking workspace GitHub pull requests | `typescript` | 1 | 2026-09-04 |
| [**herdr-dashboard**](https://github.com/chouxcreams/herdr-dashboard)<br><sub>chouxcreams</sub> | PR status dashboard TUI for herdr workspaces — PR state / CI / reviews per pane at a glance | `dashboard` `github` `pull-requests` `ratatui` `rust` | 1 | 2026-07-28 |
| [**🆕 herdr-huddle**](https://github.com/DnzzL/herdr-huddle)<br><sub>DnzzL</sub> | Live Share for your coding agent: open a Herdr pane to teammates — they watch it live, steer it, and a GitHub pull request keeps the record. | `ai-agents` `claude-code` `coding-agents` `collaboration` `go` | 1 | 2026-10-08 |
| [**herdr-plugin-gh**](https://github.com/ecklf/herdr-plugin-gh)<br><sub>ecklf</sub> | GitHub PR and CI status in Herdr's Agents sidebar, with open/create PR and failing-check actions. | `github-cli` `terminal` `go` | 1 | 🔄 2026-10-27 |
| [**🆕 herdr-ingest**](https://github.com/H3xept/herdr-ingest)<br><sub>H3xept</sub> | One herdr space per work item, from Sentry, Linear, GitHub or any JSON pipeline | `github` `linear` `sentry` `terminal` `shell` | 1 | 2026-09-26 |
| [**🆕 herdr-spaces-pr-status**](https://github.com/jmarbutt/herdr-spaces-pr-status)<br><sub>jmarbutt</sub> | Show GitHub pull request status on herdr spaces, with a Conductor-style PR board | `github-pull-request` `javascript` | 1 | 2026-09-09 |
| [**🆕 herdr-glab-status**](https://github.com/jpwallace22/herdr-glab-status)<br><sub>jpwallace22</sub> | A [Herdr](https://herdr.dev) plugin that shows each workspace's GitLab merge request status in the spaces sidebar, as a $mr token on the workspace row: | `typescript` | 1 | 2026-09-09 |
| [**herdr-plugin-github-status**](https://github.com/jwanga/herdr-plugin-github-status)<br><sub>jwanga</sub> | herdr plugin: a real-time GitHub project status pane (milestones, issues, PRs, Actions) docked on the right at sidebar width | `github` `rust` `tui` | 1 | 2026-09-19 |
| [**🆕 herdr-jira-workspace**](https://github.com/khanal-samir/herdr-jira-workspace)<br><sub>khanal-samir</sub> | Native Jira Kanban, calendar worklogs, comments and attachments inside Herdr | `jira` `kanban` `ratatui` `rust` | 1 | 2026-10-10 |
| [**🆕 herdr-revdiff**](https://github.com/mikhail-angelov/herdr-revdiff)<br><sub>mikhail-angelov</sub> | herdr plugin for https://github.com/umputun/revdiff tui | `revdiff` `tui` `shell` | 1 | 2026-09-16 |
| [**🆕 github-issue-herdr-plugin**](https://github.com/nyanyaon/github-issue-herdr-plugin)<br><sub>nyanyaon</sub> | Claude Code plugin for herding GitHub issues | `rust` | 1 | 2026-07-27 |
| [**subscription-watcher**](https://github.com/PurrlyDigital/subscription-watcher)<br><sub>PurrlyDigital</sub> | Claude Code and Codex subscription allowance in the Herdr sidebar. Read-only mirror; open issues and merge requests on GitLab. | `python` | 1 | 2026-10-06 |
| [**🆕 herdr-github-metadata**](https://github.com/ralphilius/herdr-github-metadata)<br><sub>ralphilius</sub> | Herdr plugin: GitHub metadata for the sidebar — the PR each agent is working on | `github` `python` | 1 | 2026-09-29 |
| [**🆕 herdr-agent-prs**](https://github.com/sebassdc/herdr-agent-prs)<br><sub>sebassdc</sub> | A cross-repo PR viewer for coding agents in Herdr. See every pull request an agent opened or pushed to, in any repo, with live CI, review and merge state. | `ratatui` `rust` | 1 | 2026-09-26 |
| [**🆕 herdr-pr-modal**](https://github.com/Tarektouati/herdr-pr-modal)<br><sub>Tarektouati</sub> | Open any pull request in its own worktree, straight from a Herdr | `rust` | 1 | 2026-09-24 |
| [**herdr-ci-checks**](https://github.com/tdi/herdr-ci-checks)<br><sub>tdi</sub> | herdr plugin: live GitHub/GitLab CI checks for the current branch in a pane on the right | `javascript` | 1 | 2026-09-25 |
| [**agent-checks**](https://github.com/timmo001/agent-checks)<br><sub>timmo001</sub> | CI and lint status for Herdr workspaces, with an Omarchy panel | `gh-cli` `github-workflows` `typescript` | 1 | 🔄 2026-10-28 |
| [**🆕 herdr-github-pr**](https://github.com/woshahua/herdr-github-pr)<br><sub>woshahua</sub> | Herdr plugin that syncs GitHub PR status, checks, reviews, and comments | `github` `javascript` | 1 | 2026-08-21 |
| [**🆕 herdr-pr**](https://github.com/yelsed/herdr-pr)<br><sub>yelsed</sub> | A Todo of the pull requests waiting on you, in a herdr pane. Reads everything through the gh CLI. | `rust` | 1 | 2026-08-29 |
| [**🆕 herdr-draft**](https://github.com/ZviBaratz/herdr-draft)<br><sub>ZviBaratz</sub> | herdr plugin: a new-session creation dialog — Linear issue, worktree, placement, agent kind, clauth account and initial prompt in one submit | `bubbletea` `claude-code` `go` `linear` `tui` | 1 | 🔄 2026-10-14 |

<details><summary>Also relevant to this purpose</summary>

- [tomasvarga/herdr-pickr](https://github.com/tomasvarga/herdr-pickr) — A PR review router for herdr — Ctrl+click a GitHub PR / GitLab MR link and pick a reviewer (tuicr · hunk · di…
- [oronbz/visor](https://github.com/oronbz/visor) — A terminal dashboard your coding agent sets up: PRs, Jira, calendar and anything else, with Plugins in any la…
- [tdi/herdr-worktree-from-pr](https://github.com/tdi/herdr-worktree-from-pr) — Create a git worktree from a GitHub PR and open it as a herdr workspace
- [zhuravel/magnum](https://github.com/zhuravel/magnum) — Your AI coding agents as a pull-request review team: Claude Code, Codex and others review each push in herdr…
- [jakekroon/herdr-pr-tracker](https://github.com/jakekroon/herdr-pr-tracker) — Every open pull request you have authored, docked and colour-coded by what needs you. A Herdr plugin.
- [kiitosu/herdr-jira-board](https://github.com/kiitosu/herdr-jira-board) — Jira kanban board inside herdr with Claude Code session launcher
- [tferreira/herdr-pr-ops](https://github.com/tferreira/herdr-pr-ops) — PR//OPS - pull request mission control for Herdr: your PRs and review requests on one board, one-key agents i…
- [kkjdaniel/herdr-gh-runs](https://github.com/kkjdaniel/herdr-gh-runs) — GitHub Actions runs in a herdr pane: follows your repo, live status, step logs and notifications
- [poislagarde/herdr-pr-worktree](https://github.com/poislagarde/herdr-pr-worktree) — Open GitHub pull requests as worktree spaces in Herdr, reusing existing checkouts.
- [poislagarde/herdr-worktree-cleanup](https://github.com/poislagarde/herdr-worktree-cleanup) — Automatically clean up safe GitHub PR worktrees when their Herdr space closes. Python, no dependencies, MIT.
- [spiritsack/herdr-jira-worktree](https://github.com/spiritsack/herdr-jira-worktree) — herdr plugin: prompt for a Jira ticket, open/reuse a matching git worktree, and prefill it into a fresh Claud…
- [ukwhatn/taskherd](https://github.com/ukwhatn/taskherd) — Task board linked to herdr agent sessions, PRs, and Jira tickets

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-layout"></a>

## Workspaces & Layouts

> When I open a project, I want tabs, panes, and startup commands all set up in one shot

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-spreader**](https://github.com/yuk1ty/herdr-spreader)<br><sub>yuk1ty</sub> | Spin up your whole herdr workspace layout — tabs, panes, commands, and all — from a single YAML file. | `rust` | 142 | 2026-08-16 |
| [**dotfiles**](https://github.com/lararosekelley/dotfiles)<br><sub>lararosekelley</sub> | 👩‍💻 my dotfiles, plus a whole lot more | `bash` `bootstrap` `dotfiles` `homebrew` `macos` | 52 | 🔄 2026-10-28 |
| [**herdr-plugin-workspace-manager**](https://github.com/razajamil/herdr-plugin-workspace-manager)<br><sub>razajamil</sub> | Declarative tab/pane layouts with per-workspace defaults applied automatically when a worktree is created. | `rust` | 50 | 2026-08-23 |
| [**seshagy**](https://github.com/lmilojevicc/seshagy)<br><sub>lmilojevicc</sub> | Agent-aware session manager for tmux & herdr — discover projects, launch sessions, and track your AI agents work. | `bubbletea` `go` `session-management` `session-manager` `terminal` | 21 | 🔄 2026-10-22 |
| [**herdr-grid**](https://github.com/thuanlm215/herdr-grid)<br><sub>thuanlm215</sub> | Visual Herdr pane layout editor with drag-and-drop, new shells, reusable layouts, and sending panes across tabs and workspaces. | `layout-presets` `pane-layout` `productivity` `ratatui` `rust` | 14 | 2026-10-11 |
| [**herdr-sidebar-config**](https://github.com/testy-cool/herdr-sidebar-config)<br><sub>testy-cool</sub> | Workspace → tab → agent sidebar preset for Herdr, with compact single-tab groups, readable task labels, and provider icons. | `ai-agents` `claude-code` `codex` `configuration` `ghostty` | 13 | 🔄 2026-10-23 |
| [**herdr-warp**](https://github.com/HexSleeves/herdr-warp)<br><sub>HexSleeves</sub> | Open a Herdr workspace as native Warp panes | `shell` | 9 | 2026-07-25 |
| [**glyph**](https://github.com/fru-dev3/glyph)<br><sub>fru-dev3</sub> | One identity for every coding agent you run. Marks each Claude Code, Antigravity, Codex or Gemini session with your label, the project, the machine and the mom… | `ai-agents` `claude-code` `cli` `codex` `developer-tools` | 6 | 🔄 2026-10-28 |
| [**herdr-session-manager**](https://github.com/umutciloglu/herdr-session-manager)<br><sub>umutciloglu</sub> | agent session manager for herdr with cross harness messaging | `rust` | 5 | 🔄 2026-10-21 |
| [**herdr-workspace-organizer**](https://github.com/cesmunoz/herdr-workspace-organizer)<br><sub>cesmunoz</sub> | Herdr Workspace Organizer | `typescript` | 4 | 🔄 2026-10-16 |
| [**herdr-clone-layout**](https://github.com/danilolucasmd/herdr-clone-layout)<br><sub>danilolucasmd</sub> | Clone your workspace layout onto every new herdr worktree. No templates, no config, the layout you're in is the template. | `shell` | 4 | 2026-08-27 |
| [**herdr-fork-from-message**](https://github.com/dmangla3/herdr-fork-from-message)<br><sub>dmangla3</sub> | Fork Codex or Claude Code from an earlier message into a new Herdr tab, pane, or workspace | `claude-code` `codex` `developer-tools` `terminal-multiplexer` `python` | 4 | 2026-08-10 |
| [**herdr-pane-layouts**](https://github.com/iurysza/herdr-pane-layouts)<br><sub>iurysza</sub> | Seamless tmux-style pane resizing and layouts for Herdr | `pane-layout` `python` `terminal` | 4 | 🔄 2026-10-21 |
| [**herdr-muster**](https://github.com/marcoskichel/herdr-muster)<br><sub>marcoskichel</sub> | Agent-aware project switcher for herdr | `rust` | 4 | 2026-07-03 |
| [**dsh-plugin-herdr**](https://github.com/sunny0826/dsh-plugin-herdr)<br><sub>sunny0826</sub> | Herdr control-plane plugin for DeepSeek Harness (DSH): observe and drive Herdr — a terminal workspace manager for AI coding agents — from DSH sessions | `dsh-plugin` `typescript` | 4 | 2026-08-25 |
| [**herdr-layout-tools**](https://github.com/edouard-andrei/herdr-layout-tools)<br><sub>edouard-andrei</sub> | herdr plugin: in-place reshape (main-left + grid) and equalize — same tab id, same pane ids, processes preserved | `javascript` | 3 | 2026-08-06 |
| [**herdr-auto-layout**](https://github.com/ExLuna-rs/herdr-auto-layout)<br><sub>ExLuna-rs</sub> | Declarative layouts applied to every new workspace — cross-platform herdr plugin | `layout` `rust` `terminal` | 3 | 2026-09-30 |
| [**herdr-compose**](https://github.com/ropali/herdr-compose)<br><sub>ropali</sub> | herdr-compose is a declarative workspace layout manager for Herdr | `layout-manager` `python` | 3 | 🔄 2026-10-14 |
| [**herdr-setup-bootstrap**](https://github.com/shizlie/herdr-setup-bootstrap)<br><sub>shizlie</sub> | Herdr plugin to bootstrap new worktrees from worktree_init.toml | `shell` | 3 | 2026-06-17 |
| [**herdr-google-gmail**](https://github.com/Tomatio13/herdr-google-gmail)<br><sub>Tomatio13</sub> | herdr-google-gmail is a Gmail integration plugin for herdr, a terminal workspace tool. | `shell` | 3 | 2026-07-22 |
| [**herdr-layout**](https://github.com/3mmdrew/herdr-layout)<br><sub>3mmdrew</sub> | Minimalist workspace layouts for herdr. Lua file in -> workspace out. No deps, no daemon, no YAML. | `lua` `terminal` | 2 | 2026-08-04 |
| [**herdr-medieval**](https://github.com/gabrielbarretoo/herdr-medieval)<br><sub>gabrielbarretoo</sub> | A Herdr plugin that shows your workspaces and agents as a hexagonal medieval continent in 3D: each workspace is a fenced camp, each pane an adventurer that tra… | `3d` `hex-grid` `threejs` `javascript` | 2 | 2026-08-06 |
| [**herdr-better-workspace**](https://github.com/hamzahraihan/herdr-better-workspace)<br><sub>hamzahraihan</sub> | An interactive "Open Workspace" picker plugin for herdr, the terminal workspace manager for AI coding agents. | `go` | 2 | 2026-09-09 |
| [**herdr-mcp**](https://github.com/thomasfossum/herdr-mcp)<br><sub>thomasfossum</sub> | Model Context Protocol server for Herdr: full remote control of workspaces, tabs, panes, agents and worktrees. Dependency-free Python. | `agents` `mcp` `model-context-protocol` `terminal` `python` | 2 | 2026-10-12 |
| [**herdr-google-calendar**](https://github.com/Tomatio13/herdr-google-calendar)<br><sub>Tomatio13</sub> | herdr-gog-calendar is a Google Calendar integration plugin for herdr, a terminal workspace tool. | `shell` | 2 | 2026-07-22 |
| [**reasonix-herdr**](https://github.com/uuie/reasonix-herdr)<br><sub>uuie</sub> | Native Reasonix plugin with live lifecycle reporting and workspace control inside Herdr. | `reasonix` `python` | 2 | 2026-07-10 |
| [**herdr-workspace**](https://github.com/zackshen/herdr-workspace)<br><sub>zackshen</sub> | Herdr plugin: create a workspace and apply a layout profile from a centered popup | `rust` | 2 | 2026-08-24 |
| [**herdr-dwm-layout**](https://github.com/42lizard/herdr-dwm-layout)<br><sub>42lizard</sub> | DWM-style master/stack layouts for Herdr | `dwm` `fzf` `rust` `shell` `tiling` | 1 | 2026-08-28 |
| [**🆕 yeet**](https://github.com/adriankarlen/yeet)<br><sub>adriankarlen</sub> | a minimal sesh style picker inside herdr | `sesh` `session-management` `yeet` `go` | 1 | 2026-09-25 |
| [**herdr-better-worktrees**](https://github.com/bearylabs/herdr-better-worktrees)<br><sub>bearylabs</sub> | A fast Herdr popup for managing Git worktrees in a predictable embedded-bare layout: create, clone, open, inspect, fetch, and safely remove worktrees while kee… | `typescript` | 1 | 2026-09-18 |
| [**🆕 herdr-scm**](https://github.com/dkbo/herdr-scm)<br><sub>dkbo</sub> | herdr plugin: a read-only, multi-repo source-control overview panel for the current herdr workspace | `git` `rust` `terminal` `tui` | 1 | 2026-09-10 |
| [**🆕 herdr-cosyra**](https://github.com/portablcorp/herdr-cosyra)<br><sub>portablcorp</sub> | Open your Cosyra cloud workspace in Herdr: one tab per Cosyra terminal, attached over SSH. | `shell` | 1 | 2026-10-09 |
| [**herdr-spinup**](https://github.com/Royal-lobster/herdr-spinup)<br><sub>Royal-lobster</sub> | Start screen for every new herdr tab: pick a tool and it runs in that tab. Tools defined in JSON. | `javascript` | 1 | 2026-08-04 |

<details><summary>Also relevant to this purpose</summary>

- [andrewchng/herdr-sessionizer](https://github.com/andrewchng/herdr-sessionizer) — Fuzzy-open projects and worktrees, then bootstrap workspaces from declarative TOML layouts — tabs, pane split…
- [fullerzz/herdr-plugin-sesh](https://github.com/fullerzz/herdr-plugin-sesh) — Sesh-style workspace picker TUI for Herdr. Integrates with zoxide to create workspaces from commonly used dir…
- [ntindle/herdr-resurrect](https://github.com/ntindle/herdr-resurrect) — tmux-resurrect for herdr — snapshot workspaces, tabs, panes, cwd, running programs and agents, and restore th…
- [crierr/herdr-arrange](https://github.com/crierr/herdr-arrange) — Interactive popup UI for herdr pane move / swap / re-split / layout
- [enekos/herdr-quick-actions](https://github.com/enekos/herdr-quick-actions) — fzf picker for herdr's native tab/pane/workspace actions, ranked by usage — stop memorizing keybindings
- [salkhalil/herdr-sessionizer](https://github.com/salkhalil/herdr-sessionizer) — tmux-sessionizer for herdr: fzf over open workspaces and zoxide directories, create-or-focus with template ta…
- [aliou/herdr-cast](https://github.com/aliou/herdr-cast) — Personal Herdr plugin for native macOS agent notifications, fuzzy workspace navigation, zoxide-backed workspa…
- [chandrasekharan98/herdr-workspace-save](https://github.com/chandrasekharan98/herdr-workspace-save) — Save a Herdr workspace — layout, cwds, agent sessions, running commands — and reopen it later from an fzf pic…
- [cantona/herdr-revive](https://github.com/cantona/herdr-revive) — Restore Herdr commands, layouts and exact agent sessions with preview, named workspaces and explicit recovery.
- [42lizard/herdr-sessionizer](https://github.com/42lizard/herdr-sessionizer) — tmux-sessionizer style plugin for herdr

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-navigate"></a>

## Pane Navigation & Keys

> I want to move and resize between panes and workspaces using the same keys as my editor

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**vim-herdr-navigation**](https://github.com/paulbkim-dev/vim-herdr-navigation)<br><sub>paulbkim-dev</sub> | Seamless Ctrl+h/j/k/l navigation across herdr panes and Vim/Neovim splits — vim-tmux-navigator ported to herdr | `neovim` `vim` `shell` | 112 | 2026-10-10 |
| [**herdr-splits.nvim**](https://github.com/lmilojevicc/herdr-splits.nvim)<br><sub>lmilojevicc</sub> | Smart splits navigation and resizing for Herdr and Neovim | `lua` `neovim` `neovim-plugin` `neovim-plugins` `nvim` | 69 | 2026-08-17 |
| [**herdr-floax**](https://github.com/Tyru5/herdr-floax)<br><sub>Tyru5</sub> | Floating scratch shell for herdr — a tmux-floax style toggleable popup, one per workspace, with persistent sessions | `rust` `terminal` `tmux-floax` | 29 | 🔄 2026-10-23 |
| [**herdr-recent-navigator**](https://github.com/beyondlex/herdr-recent-navigator)<br><sub>beyondlex</sub> | MRU switching across recent workspaces, tabs, panes, and agents — like JetBrains's recent file — plus fuzzy search over any pane's content, fully keyboard-driv… | `agent` `mru` `navigator` `pane` `popup` | 24 | 🔄 2026-10-18 |
| [**herdr-nvim-nav**](https://github.com/aimdevlee/herdr-nvim-nav)<br><sub>aimdevlee</sub> | Seamless Ctrl+h/j/k/l across herdr panes and Neovim splits — socket-based, no per-keystroke process | `neovim` `neovim-plugin` `lua` | 23 | 2026-08-02 |
| [**herdr-command-center**](https://github.com/speardragon/herdr-command-center)<br><sub>speardragon</sub> | One keybinding for every command — a herdr popup that lists the commands you registered, runs them by arrow key or number, and closes itself before the command… | `command-palette` `nodejs` `terminal` `toml` `tui` | 19 | 🔄 2026-10-19 |
| [**herdr-last-workspace**](https://github.com/third774/herdr-last-workspace)<br><sub>third774</sub> | Plugin for swapping to the last workspace you had focused | `rust` | 19 | 2026-06-22 |
| [**herdr-pane-mover**](https://github.com/osamahbeig/herdr-pane-mover)<br><sub>osamahbeig</sub> | Clickable overlay menu for herdr: move, re-split, or swap panes across tabs and workspaces | `terminal` `tui` `javascript` | 15 | 2026-07-10 |
| [**herdr-cliamp**](https://github.com/coryshaw1/herdr-cliamp)<br><sub>coryshaw1</sub> | Floating cliamp for herdr that keeps playing when hidden: the player lives in a detached herdr session, so closing the float only detaches. | `audiobook` `cliamp` `music-player` `podcast` `terminal` | 14 | 2026-08-24 |
| [**herdr-logbook**](https://github.com/Resetnak/herdr-logbook)<br><sub>Resetnak</sub> | Your terminal's working memory — offline, Markdown-first notes, decisions, and an active-task now.md for Herdr | `adr` `bubbletea` `cli` `go` `markdown` | 13 | 🔄 2026-10-15 |
| [**herdr-profiles**](https://github.com/GiorgiTarsaidze/herdr-profiles)<br><sub>GiorgiTarsaidze</sub> | Chrome-style profiles for Herdr: isolated sets of spaces with a popup chooser | `rust` `terminal` | 12 | 2026-09-14 |
| [**herdr-paddock**](https://github.com/neyham/herdr-paddock)<br><sub>neyham</sub> | 🐑 A card-wall feed for your herdr agents — glance over the flock, zoom into one, reply, all over plain SSH | `bubbletea` `go` `ssh` `tui` | 12 | 🔄 2026-10-23 |
| [**musicforprogramming**](https://github.com/pivoshenko/musicforprogramming)<br><sub>pivoshenko</sub> | 🎧 TUI for musicforprogramming.net, written in Rust | `ambient` `audio` `daemon` `developer-tools` `focus` | 12 | 🔄 2026-10-21 |
| [**herdr-equalize-panes**](https://github.com/shibayu36/herdr-equalize-panes)<br><sub>shibayu36</sub> | herdr plugin that automatically equalizes pane sizes on split and close (tmux select-layout -E, but automatic) | `terminal` `perl` | 11 | 2026-08-22 |
| [**terminal-markdown-renderer**](https://github.com/slara/terminal-markdown-renderer)<br><sub>slara</sub> | tmdview: view Markdown rendered as HTML in a browser inside your terminal. A personal tool, written with AI. | `cli` `markdown` `rust` `terminal` | 10 | 🔄 2026-10-18 |
| [**herdr-trail**](https://github.com/catoncat/herdr-trail)<br><sub>catoncat</sub> | Herd-wide shared memos for herdr: agents jot follow-ups, humans manage one global list, every entry jumps back to its source conversation | `javascript` | 9 | 2026-08-26 |
| [**herdr-arrange**](https://github.com/crierr/herdr-arrange)<br><sub>crierr</sub> | Interactive popup UI for herdr pane move / swap / re-split / layout | `go` | 9 | 2026-09-05 |
| [**herdr-omnisearch**](https://github.com/dmnkf/herdr-omnisearch)<br><sub>dmnkf</sub> | Fast search and navigation for Herdr workspaces, panes, and archived agent sessions across all your connected machines | `python` | 9 | 🔄 2026-10-27 |
| [**herdr-git**](https://github.com/JeHwanYoo/herdr-git)<br><sub>JeHwanYoo</sub> | A Git client for Herdr, focused on the essentials. | `git` `rust` | 8 | 🔄 2026-10-21 |
| [**herdr-last**](https://github.com/lmilojevicc/herdr-last)<br><sub>lmilojevicc</sub> | Toggle back to the previously active workspace or tab in Herdr | `go` `linux` `macos` `productivity` `tabs` | 8 | 2026-08-07 |
| [**herdr-toggle-popup**](https://github.com/maro114510/herdr-toggle-popup)<br><sub>maro114510</sub> | One-keybinding overlay popup shell plugin for the Herdr terminal | `go` | 8 | 🔄 2026-10-25 |
| [**nvim-herdr-navigation**](https://github.com/bojackduy/nvim-herdr-navigation)<br><sub>bojackduy</sub> | vim-tmux-navigator style ctrl+h/j/k/l navigation between Neovim splits and Herdr panes | `keyboard-shortcuts` `lazyvim` `lua` `navigation` `neovim` | 7 | 2026-07-20 |
| [**herdr-swipe**](https://github.com/husniadil/herdr-swipe)<br><sub>husniadil</sub> | Trackpad gestures for Herdr: move between panes, tabs and spaces, and jump to the agent waiting on you | `cgeventtap` `gestures` `macos` `python` `terminal` | 7 | 2026-08-20 |
| [**herdr-scratch**](https://github.com/AkashJana18/herdr-scratch)<br><sub>AkashJana18</sub> | Persistent scratchpads for Herdr, paving the way for floating utility panes. | `cli` `rust` `scratchpad` | 6 | 2026-09-20 |
| [**herdr-which-key**](https://github.com/CowboyVang/herdr-which-key)<br><sub>CowboyVang</sub> | A which-key-style keymap overlay for herdr. Press one key, see every binding under your prefix grouped and labelled, press a second key to run it. Deliberately… | `keybindings` `terminal` `which-key` `python` | 6 | 2026-09-15 |
| [**nvim-herdr-navigator**](https://github.com/kaar/nvim-herdr-navigator)<br><sub>kaar</sub> | Seamless navigation between Neovim splits and herdr panes: one set of `ctrl+h/j/k/l` chords moves through vim and herdr panes. | `neovim` `neovim-plugin` `shell` | 6 | 2026-10-03 |
| [**herdr-attention**](https://github.com/milkyskies/herdr-attention)<br><sub>milkyskies</sub> | A herdr plugin: one keypress jumps focus to the next agent that needs attention (blocked, then done). | `javascript` | 6 | 2026-07-08 |
| [**herdr-voice**](https://github.com/aneym/herdr-voice)<br><sub>aneym</sub> | Voice control for herdr — speak to create spaces, split panes, and drive coding agents. OpenAI Realtime + floating HUD with live dictation and transcripts. | `openai-realtime-api` `voice` `javascript` | 5 | 2026-09-25 |
| [**herdr-annotations**](https://github.com/jagzmz/herdr-annotations)<br><sub>jagzmz</sub> | Annotate selected terminal text in Herdr with a fast local-first popup and reusable collections. | `annotations` `cli` `coding-agents` `developer-tools` `local-first` | 5 | 2026-07-16 |
| [**herdr-harpoon**](https://github.com/KonstantinKai/herdr-harpoon)<br><sub>KonstantinKai</sub> | Harpoon for herdr: mark panes and jump by index. Bash-only, zero build. | `bash` `harpoon` `tmux-harpoon` `shell` | 5 | 2026-07-29 |
| [**herdr-equalize-splits**](https://github.com/markhuot/herdr-equalize-splits)<br><sub>markhuot</sub> | herdr plugin: equalize every split in the current tab to an even share within each row/column (bind to Ctrl+b =) | `terminal` `tmux` `javascript` | 5 | 2026-07-08 |
| [**herdr-file-transfer**](https://github.com/mrolafsson/herdr-file-transfer)<br><sub>mrolafsson</sub> | Running herdr on a VPS or remote box (Hetzner, a cloud dev server) and uploading files is a pain? Drop them on a popup and they're copied over ssh into your ag… | `bubbletea` `claude-code` `coding-agents` `file-transfer` `go` | 5 | 🔄 2026-10-22 |
| [**herdr-easyjump**](https://github.com/xzedx/herdr-easyjump)<br><sub>xzedx</sub> | Press a key, type a letter, jump to any space, agent, pane, or tab. EasyMotion / Vimium / vim-choosewin style hint labels, drawn right in the Herdr sidebar. | `choosewin` `easymotion` `hints` `navigation` `rust` | 5 | 2026-09-14 |
| [**🆕 claude-deck**](https://github.com/bigsan/claude-deck)<br><sub>bigsan</sub> | Watch Claude Code sessions: scratchpad files, tasks and every tool call, standalone or as a herdr plugin | `claude-code` `ratatui` `tui` `rust` | 4 | 🔄 2026-10-28 |
| [**herdr-tmux-session-navigator**](https://github.com/caneppelevitor/herdr-tmux-session-navigator)<br><sub>caneppelevitor</sub> | tmux choose-tree for herdr. Written by someone who left tmux but never gave up prefix+s. | `bubbletea` `terminal` `tmux` `go` | 4 | 2026-09-18 |
| [**herdr-unread-marker**](https://github.com/JoanGil/herdr-unread-marker)<br><sub>JoanGil</sub> | Mark/unmark the focused agent unread with a keybinding, manual only | `shell` | 4 | 2026-07-17 |
| [**herdr-normal-mode**](https://github.com/maedana/herdr-normal-mode)<br><sub>maedana</sub> | Vim-style normal mode for the herdr sidebar: j/k rows, h/l tabs, 0-9 panes | `rust` `tui` | 4 | 2026-08-24 |
| [**herdr-next-agent**](https://github.com/martin-ro/herdr-next-agent)<br><sub>martin-ro</sub> | Herdr plugin: jump to the next agent needing attention, ranked by a configurable status priority | `python` | 4 | 2026-09-10 |
| [**herdr-smart-nav**](https://github.com/odiumuniverse/herdr-smart-nav)<br><sub>odiumuniverse</sub> | Smart Ctrl+h/j/k/l across nvim windows, herdr panes, tabs and workspaces | `navigation` `neovim` `neovim-plugin` `nvim` `nvim-lua` | 4 | 2026-09-14 |
| [**herdr-pretty-which**](https://github.com/ramarivera/herdr-pretty-which)<br><sub>ramarivera</sub> | A Rust/Ratatui which-key style keybinding overlay for Herdr. | `ratatui` `rust` `terminal` `tui` `which-key` | 4 | 🔄 2026-10-28 |
| [**herdr-account-switch**](https://github.com/rcosteira79/herdr-account-switch)<br><sub>rcosteira79</sub> | Hot-swap Claude Code / Codex logins without re-authenticating. Overlay picker, cycle-to-next keybinding, and a per-pane account badge ($acct). | `python` | 4 | 🔄 2026-10-28 |
| [**herdr-navigator**](https://github.com/willfish/herdr-navigator)<br><sub>willfish</sub> | Herdr-side navigation actions for Vim/Neovim-aware pane movement | `navigation` `neovim` `rust` | 4 | 2026-07-07 |
| [**🆕 reficus**](https://github.com/81zi/reficus)<br><sub>81zi</sub> | Grow the focused pane and shrink the others on every focus change | `python` | 3 | 🔄 2026-10-21 |
| [**herdr-pane-switcher**](https://github.com/AlexanderGrooff/herdr-pane-switcher)<br><sub>AlexanderGrooff</sub> | Shortcuts for switching attention to high-prio Herdr panes | `rust` | 3 | 2026-08-27 |
| [**herdr-convo-index**](https://github.com/dzwduan/herdr-convo-index)<br><sub>dzwduan</sub> | Turn index for Claude Code panes in herdr — jump to any past turn and read it in a popup | `python` | 3 | 2026-07-27 |
| [**herdr-aspire-hud**](https://github.com/H3xept/herdr-aspire-hud)<br><sub>H3xept</sub> | Live .NET Aspire AppHost health for every herdr space: sidebar badges and a popup HUD | `apphost` `aspire` `dotnet-aspire` `terminal` `tui` | 3 | 2026-09-26 |
| [**herdr-pane-shift**](https://github.com/Hon-Lu/herdr-pane-shift)<br><sub>Hon-Lu</sub> | Herdr plugin for rearranging panes from the keyboard: swap, break into a tab, rotate splits, and place beside any pane. | `terminal` `tmux-alternative` `javascript` | 3 | 2026-10-07 |
| [**herdr-popupx**](https://github.com/jeromychu23/herdr-popupx)<br><sub>jeromychu23</sub> | Persistent native floating scratch popups for Herdr. | `rust` `terminal` `tui` | 3 | 2026-07-21 |
| [**herdr-plan-meter**](https://github.com/JunSeo99/herdr-plan-meter)<br><sub>JunSeo99</sub> | Claude Code and Codex plan limits in the herdr tab bar, with a detail popup. One stdlib Python file, read-only credentials. | `claude-code` `codex` `rate-limit` `usage` `python` | 3 | 2026-10-13 |
| [**herdr-float**](https://github.com/meerzulee/herdr-float)<br><sub>meerzulee</sub> | Zellij like ALT+F floating pane | `shell` | 3 | 2026-07-20 |
| [**herdr-confirm-close-pane**](https://github.com/poweroutlet2/herdr-confirm-close-pane)<br><sub>poweroutlet2</sub> | A herdr plugin that asks for confirmation before closing a pane, like tmux's prefix+x confirm-before. | `shell` | 3 | 2026-07-06 |
| [**herdr-ask-inbox**](https://github.com/speardragon/herdr-ask-inbox)<br><sub>speardragon</sub> | Collect blocked Claude AskUserQuestion prompts from every herdr workspace into one popup, answer them in place, and never send an answer to the wrong agent. | `claude-code` `javascript` | 3 | 2026-07-25 |
| [**herdr-unread-jump**](https://github.com/to4iki/herdr-unread-jump)<br><sub>to4iki</sub> | Jump to the next Herdr agent pane that needs attention (blocked, then done). | `agents` `bash` `shell` | 3 | 2026-08-30 |
| [**herdr-mission-control**](https://github.com/vjeantet/herdr-mission-control)<br><sub>vjeantet</sub> | Mission Control for herdr: one key, every pane of the workspace as a live tile grid grouped by tab; pick one to switch to it | `expose` `mission-control` `terminal` `tui` `rust` | 3 | 2026-09-20 |
| [**🆕 herdr-pacer**](https://github.com/amali01/herdr-pacer)<br><sub>amali01</sub> | Herdr plugin: context-window bars under each agent in the sidebar, plus a 5h/weekly usage popup for Claude, Codex and OpenCode | `claude-code` `codex` `opencode` `rust` | 2 | 🔄 2026-10-28 |
| [**herdr-next-agent**](https://github.com/choplin/herdr-next-agent)<br><sub>choplin</sub> | Move between Herdr agents in configured semantic states. | `go` | 2 | 2026-08-24 |
| [**herdr-tmux-layout**](https://github.com/crierr/herdr-tmux-layout)<br><sub>crierr</sub> | tmux-style preset layouts for live Herdr panes: cycle, even-horizontal, even-vertical, main-horizontal, main-vertical, tiled, and balance | `go` | 2 | 2026-08-30 |
| [**herdr-equalize-vsplit**](https://github.com/devoc09/herdr-equalize-vsplit)<br><sub>devoc09</sub> | A Herdr plugin that splits the current pane to the right and equalizes column widths. | `go` | 2 | 2026-07-15 |
| [**herdr-crossroads**](https://github.com/eisenhauer-dev/herdr-crossroads)<br><sub>eisenhauer-dev</sub> | Navigate your Herdr. Find your sheep when you need them. | `rust` | 2 | 🔄 2026-10-28 |
| [**herdr-easymotion**](https://github.com/elliotekj/herdr-easymotion)<br><sub>elliotekj</sub> | 🦘 Jump directly between Herdr panes | `javascript` | 2 | 2026-07-20 |
| [**worktree-fleet**](https://github.com/hasuwini77/worktree-fleet)<br><sub>hasuwini77</sub> | Parallel Claude Code / Codex builds on Herdr: /herd splits a task into worktree buckets, plus a live fleet popup | `claude-code` `codex` `git-worktree` `shell` | 2 | 2026-09-29 |
| [**herdr-break-pane**](https://github.com/iuhoay/herdr-break-pane)<br><sub>iuhoay</sub> | A small Herdr plugin that moves the focused pane into a new tab. | `pane` `javascript` | 2 | 🔄 2026-10-22 |
| [**herdr-grid-slide**](https://github.com/jeiea/herdr-grid-slide)<br><sub>jeiea</sub> | A plugin born from the idea of focusing and moving panes with hjkl. | `navigation` `rust` | 2 | 🔄 2026-10-17 |
| [**herdr-prevtab**](https://github.com/joo-was-already-taken/herdr-prevtab)<br><sub>joo-was-already-taken</sub> | Herdr plugin for switching to the previously focused tab | `rust` | 2 | 2026-10-04 |
| [**herdr-inbox**](https://github.com/LeaveMyYard/herdr-inbox)<br><sub>LeaveMyYard</sub> | Non-blocking question inbox for Claude Code agents in herdr: agents ask once and keep working, you answer from one popup | `claude-code` `claude-code-plugin` `mcp` `python` | 2 | 🔄 2026-10-22 |
| [**🆕 herdr-plugin-last**](https://github.com/m4salah/herdr-plugin-last)<br><sub>m4salah</sub> | tmux-style last-tab and last-workspace navigation for Herdr | `rust` | 2 | 2026-07-30 |
| [**herdr-marks**](https://github.com/mcostasilva/herdr-marks)<br><sub>mcostasilva</sub> | Neovim-style letter marks for Herdr panes and workspaces, with colored sidebar labels and quick navigation | `rust` | 2 | 2026-10-06 |
| [**herdr-lazytask**](https://github.com/mdetweil/herdr-lazytask)<br><sub>mdetweil</sub> | Lazytask in a herdr split pane (open/focus/toggle) plus Taskwarrior quick actions | `lazytask` `taskwarrior` `terminal` `rust` | 2 | 2026-08-02 |
| [**herdr-quotr**](https://github.com/napalmpapalam/herdr-quotr)<br><sub>napalmpapalam</sub> | Quote your agent's own answer back at it, from a herdr popup. | `claude-code` `rust` `tui` | 2 | 2026-10-01 |
| [**grove-herdr**](https://github.com/nicksenap/grove-herdr)<br><sub>nicksenap</sub> | Herdr plugin: Grove workspace create popup and Herdr workspace bridge | `grove` `shell` | 2 | 🔄 2026-10-27 |
| [**herdr-topstrip**](https://github.com/orcchg/herdr-topstrip)<br><sub>orcchg</sub> | Opens every space or tab on existing space as two panes - a narrow top strip (normally used for directory navigation, shell commands and git) and a wide bottom… | `shell` | 2 | 2026-09-15 |
| [**herdr-plugin-agent-attention**](https://github.com/peterwiebe/herdr-plugin-agent-attention)<br><sub>peterwiebe</sub> | Herdr plugin to jump to the most recent blocked or finished agent | `python` | 2 | 2026-09-04 |
| [**herdr-equalize-panes**](https://github.com/ponko2/herdr-equalize-panes)<br><sub>ponko2</sub> | Automatically keeps panes in each tab evenly sized as panes are created, closed, moved, or exited. | `rust` | 2 | 🔄 2026-10-27 |
| [**herdr-pane-mover**](https://github.com/ronly2460/herdr-pane-mover)<br><sub>ronly2460</sub> | Move Herdr panes between workspaces with an interactive arrow-key picker | `terminal` `workspace` `shell` | 2 | 2026-08-23 |
| [**herdr-pane-orientation-switcher**](https://github.com/sf1tzp/herdr-pane-orientation-switcher)<br><sub>sf1tzp</sub> | Workflow Ergonomics for Split Panes in Herdr | `shell` | 2 | 2026-07-25 |
| [**edger**](https://github.com/suderman/edger)<br><sub>suderman</sub> | Seamlessly navigate splits in Herdr, tmux, Emacs, Neovim | `emacs` `emacs-package` `neovim` `neovim-plugin` `split-navigation` | 2 | 🔄 2026-10-17 |
| [**herdr-machine-manager**](https://github.com/vika2603/herdr-machine-manager)<br><sub>vika2603</sub> | Manage herdr's saved SSH machines from a popup TUI: add one from a ~/.ssh/config alias, disconnect without losing its configuration, edit its target. | `bubbletea` `go` `ssh` `ssh-config` `terminal` | 2 | 2026-10-01 |
| [**herdr-hintr**](https://github.com/wraithyy/herdr-hintr)<br><sub>wraithyy</sub> | herdr plugin: whichkey-style keybinding cheatsheet popup — press the key to run it | `shell` | 2 | 2026-08-11 |
| [**🆕 herdr-dictate**](https://github.com/abhishekrana/herdr-dictate)<br><sub>abhishekrana</sub> | Local speech-to-text dictation into the focused Herdr pane | `dictation` `speech-to-text` `voice` `whisper` `rust` | 1 | 🔄 2026-10-17 |
| [**herdr-display-panes**](https://github.com/abroller666/herdr-display-panes)<br><sub>abroller666</sub> | tmux display-panes for Herdr: label every pane in the current tab and jump with one key | `tmux` `python` | 1 | 2026-10-07 |
| [**herdr-plugin-ide-jump**](https://github.com/agentience/herdr-plugin-ide-jump)<br><sub>agentience</sub> | Get back to your IDE: raise the editor window for the focused pane's project, or pick one from a filterable popup. A Herdr plugin. | `python` | 1 | 2026-08-24 |
| [**herdr-hyprland**](https://github.com/aorumbayev/herdr-hyprland)<br><sub>aorumbayev</sub> | Hyprland inspired controls for herdr | `ai-agents` `developer-tools` `golang` `hyprland` `keybindings` | 1 | 2026-09-04 |
| [**asconfirmclose**](https://github.com/asumaran/asconfirmclose)<br><sub>asumaran</sub> | Herdr plugin: close the focused pane, asking first only when a process is running in it | `terminal` `go` | 1 | 2026-09-20 |
| [**herdr-scratchpad**](https://github.com/brunohq/herdr-scratchpad)<br><sub>brunohq</sub> | Minimal per-tab markdown scratchpad with checkbox todos for herdr | `python` `scratchpad` `tui` | 1 | 2026-09-12 |
| [**herdr-plugin-tiles**](https://github.com/carsonjones/herdr-plugin-tiles)<br><sub>carsonjones</sub> | simple pane manager for herdr | `python` | 1 | 2026-06-19 |
| [**lazyherd**](https://github.com/chriopter/lazyherd)<br><sub>chriopter</sub> | Cockpit over all your Git repos, with a jump into lazygit and Herdr workspaces | `git` `lazygit` `tui` `go` | 1 | 2026-10-05 |
| [**🆕 herdr-cheatsheet**](https://github.com/ChristianDeckert/herdr-cheatsheet)<br><sub>ChristianDeckert</sub> | Clickable herdr side panel: just recipes, herdr and terminal keybindings | `cheatsheet` `just` `zsh` `shell` | 1 | 🔄 2026-10-27 |
| [**🆕 herdr-notes**](https://github.com/cyperx84/herdr-notes)<br><sub>cyperx84</sub> | Focused per-workspace Markdown scratch notes for Herdr, built in Go | `bubbletea` `golang` `markdown` `notes` `go` | 1 | 2026-08-16 |
| [**🆕 herdr-tab-jump**](https://github.com/cyperx84/herdr-tab-jump)<br><sub>cyperx84</sub> | Focus herdr tab N by position, from any keybinding — split your number row between tabs and workspaces | `shell` | 1 | 2026-09-01 |
| [**🆕 herdr-last-tab**](https://github.com/dantehemerson/herdr-last-tab)<br><sub>dantehemerson</sub> | Plugin for swapping to the last tab you had focused | `rust` | 1 | 2026-08-12 |
| [**🆕 herdr-swipe-linux**](https://github.com/enisbu/herdr-swipe-linux)<br><sub>enisbu</sub> | Trackpad gestures for Herdr on Linux: swipe between panes, tabs and spaces, tap to jump to the waiting agent | `evdev` `gestures` `gnome` `hyprland` `linux` | 1 | 2026-09-02 |
| [**herdr-terminal-scripts**](https://github.com/Fadi729/herdr-terminal-scripts)<br><sub>Fadi729</sub> | Herdr plugin that runs named Scripts from a popup or numbered slots | `typescript` | 1 | 2026-09-21 |
| [**🆕 herdr-arcade**](https://github.com/giorgiostokje/herdr-arcade)<br><sub>giorgiostokje</sub> | Seventeen terminal arcade games in a Herdr popup pane that pause themselves when an agent needs attention | `python` | 1 | 2026-10-12 |
| [**bindr**](https://github.com/itsmistermoon/bindr)<br><sub>itsmistermoon</sub> | Herdr plugin for switching between named keybinding profiles and viewing/editing keybinds in a popup. | `rust` | 1 | 🔄 2026-10-20 |
| [**🆕 herdr-plugin-switcher**](https://github.com/KadenThomp36/herdr-plugin-switcher)<br><sub>KadenThomp36</sub> | Hold Ctrl, tap Tab to cycle herdr panes MRU-style. Arc/Zen-style pane switcher for herdr on macOS. | `swift` | 1 | 2026-08-21 |
| [**🆕 herdr-nvim-aware**](https://github.com/KoalaVim/herdr-nvim-aware)<br><sub>KoalaVim</sub> | Nvim-aware keybindings for herdr: navigation, splits, close, zoom | `rust` | 1 | 2026-08-20 |
| [**herdr-scratch**](https://github.com/macintacos/herdr-scratch)<br><sub>macintacos</sub> | A scratch shell for herdr, in a popup you toggle with one chord — backed by tmux, so it comes back exactly as you left it | `go` | 1 | 2026-08-28 |
| [**🆕 herdr-touchbar**](https://github.com/omerturhan/herdr-touchbar)<br><sub>omerturhan</sub> | Shows working and blocked herdr agents on the MacBook Touch Bar; tap one to jump straight to its tab. | `ai-agents` `macos` `touchbar` `swift` | 1 | 2026-09-14 |
| [**herdr-plugins**](https://github.com/oullin/herdr-plugins)<br><sub>oullin</sub> | A collection of focused, independently installable plugins for Herdr. | `typescript` | 1 | 🔄 2026-10-20 |
| [**🆕 herdr-tab-flow**](https://github.com/RodrigoEspinosa/herdr-tab-flow)<br><sub>RodrigoEspinosa</sub> | Next/previous tab navigation for herdr that flows across spaces — past the last tab, continue into the next space. | `shell` | 1 | 2026-10-01 |
| [**🆕 herdr-edge-nav**](https://github.com/sebcbi1/herdr-edge-nav)<br><sub>sebcbi1</sub> | Herdr plugin for directional pane navigation/resizing that crosses tabs and workspaces at pane edges, with seamless Neovim split awareness. | `lua` | 1 | 2026-08-12 |
| [**🆕 herdr-scratch**](https://github.com/shadowfax92/herdr-scratch)<br><sub>shadowfax92</sub> | Persistent per-pane Herdr scratch popups backed by private tmux sessions. | `neovim` `productivity` `rust` `terminal` `tmux` | 1 | 🔄 2026-10-22 |
| [**🆕 herdr-talon**](https://github.com/shadowfax92/herdr-talon)<br><sub>shadowfax92</sub> | Spatial keyboard hints for visible Herdr terminal targets. | `keyboard-navigation` `productivity` `rust` `terminal` `tmux-fingers` | 1 | 2026-10-13 |
| [**herdr-knapp**](https://github.com/shindakun/herdr-knapp)<br><sub>shindakun</sub> | Herdr plugin that reads Markdown notes by their links: backlinks, broken links, orphans, and link graphs | `backlinks` `cli` `markdown` `notes` `obsidian` | 1 | 2026-09-24 |
| [**🆕 herdr-nav-plus**](https://github.com/shoaibkhanz/herdr-nav-plus)<br><sub>shoaibkhanz</sub> | Ctrl+h/j/k/l navigation that flows past herdr panes into workspaces — vim-aware, wraps at both ends | `javascript` | 1 | 2026-07-18 |
| [**🆕 herdr-worktrees**](https://github.com/SpaceK33z/herdr-worktrees)<br><sub>SpaceK33z</sub> | Switch, create, and remove Git worktrees from a Herdr popup | `rust` | 1 | 2026-09-17 |
| [**🆕 jc-herdr-plugins**](https://github.com/thejiajun/jc-herdr-plugins)<br><sub>thejiajun</sub> | Herdr plugins: Autoname (auto-name workspaces from agent conversations) and Agent Switcher (search and jump between agents) | `python` | 1 | 🔄 2026-10-14 |
| [**🆕 herdr-customize**](https://github.com/wapenshaw/herdr-customize)<br><sub>wapenshaw</sub> | Customize Herdr's settings and key bindings in one popup, with optional Themes and Plugins pages. Linux, macOS and Windows. | `rust` | 1 | 🔄 2026-10-26 |
| [**🆕 herdr-balance-panes**](https://github.com/willfish/herdr-balance-panes)<br><sub>willfish</sub> | Evenly size panes in the current Herdr tab (tmux select-layout -E) | `rust` `terminal` `tmux` | 1 | 2026-08-05 |
| [**🆕 herdr-mark**](https://github.com/y4le/herdr-mark)<br><sub>y4le</sub> | tmux-style marked pane for herdr: mark a pane, then join it beside or swap it with another | `shell` | 1 | 2026-09-26 |

<details><summary>Also relevant to this purpose</summary>

- [thanhdat77/herdr-navigator](https://github.com/thanhdat77/herdr-navigator) — Jump to any Herdr workspace, agent, project, session, remote, directory, or action from one fuzzy navigator.
- [speardragon/herdr-plugin-manager](https://github.com/speardragon/herdr-plugin-manager) — Manage herdr plugins from a popup — install, update, enable/disable, uninstall, and browse the herdr-plugin m…
- [jorge07RD/herdr-ssh-manager](https://github.com/jorge07RD/herdr-ssh-manager) — Save SSH hosts and reconnect from a fuzzy popup inside Herdr — Enter hands the popup straight to ssh.
- [vika2603/herdr-plugin-manager](https://github.com/vika2603/herdr-plugin-manager) — Browse, install and update herdr plugins from a popup or the command line
- [purehate/herdr-plugin-picker](https://github.com/purehate/herdr-plugin-picker) — Floating popup picker for Herdr — jump to any space, agent, tab or pane, broadcast one command to every marke…
- [rheech22/herdr-comment-on-copy](https://github.com/rheech22/herdr-comment-on-copy) — Drag to select terminal text and open a comment popup automatically. Send feedback with context to AI agents…
- [victor-software-house/herdr-stash](https://github.com/victor-software-house/herdr-stash) — Stash a Herdr workspace: stop its agents, keep its shape and their conversations, and restore it later from a…
- [karanpatel1993/herdr-nav](https://github.com/karanpatel1993/herdr-nav) — File navigation, code search and jdb debugging inside herdr — fzf, ripgrep and a Java debugger wired into you…
- [bayoudhi/herdr-prayer-times](https://github.com/bayoudhi/herdr-prayer-times) — Next Islamic prayer and countdown in the Herdr sidebar, with a timetable popup and notifications
- [bearylabs/herdr-better-worktrees](https://github.com/bearylabs/herdr-better-worktrees) — A fast Herdr popup for managing Git worktrees in a predictable embedded-bare layout: create, clone, open, ins…
- [janooh37-hue/hertrees](https://github.com/janooh37-hue/hertrees) — Every worktree, every agent, one popup. A Herdr plugin for git worktrees, PR state and AI agent sessions.
- [MykolaSuprun/herdr-vimnav](https://github.com/MykolaSuprun/herdr-vimnav) — Master-detail switcher for herdr — live pane previews, MRU priority sort, sidebar jump codes
- [xzedx/herdr-derby](https://github.com/xzedx/herdr-derby) — Send one prompt to every coding agent in the current Herdr tab and watch them race: a popup to type in, live…
- [yojahny55/herdr-space-groups](https://github.com/yojahny55/herdr-space-groups) — Herdr plugin: group Spaces into named, colored groups — picker popup (mouse + keyboard), sidebar group header…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-files"></a>

## File Viewers & Editors

> I want to open a file tree inside a pane, or keep it in sync with my editor

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**terminal-code**](https://github.com/zenbu-labs/terminal-code)<br><sub>zenbu-labs</sub> | VS Code in the terminal | `cli` `terminal` `vscode` `typescript` | 2210 | 🔄 2026-10-19 |
| [**ttt**](https://github.com/eugenioenko/ttt)<br><sub>eugenioenko</sub> | TTT Editor (Terminal Text Tool): A real alternative to VS Code, Zed, and Sublime that runs in your terminal. A TUI that feels like GUI. Single binary, zero con… | `cli` `code-editor` `developer-tools` `diff` `editor` | 942 | 🔄 2026-10-28 |
| [**dotfiles**](https://github.com/babarot/dotfiles)<br><sub>babarot</sub> | A repository that gathered files starting with dot | `dotfiles` `neovim` `nix` | 782 | 🔄 2026-10-28 |
| [**herdr-file-viewer**](https://github.com/smarzban/herdr-file-viewer)<br><sub>smarzban</sub> | A git-aware, read-only file viewer for herdr. Mouse friendly, keyboard-driven TUI: tree + content pane with diffs, rendered markdown, and syntax highlighting. | `file-viewer` `git` `ratatui` `rust` `terminal` | 689 | 🔄 2026-10-26 |
| [**herdr-sidebar**](https://github.com/alexarthurs/herdr-sidebar)<br><sub>alexarthurs</sub> | VS Code-style sidebar for the herdr: file explorer + git source control in one pane — syntax-highlighted previews, VS Code-style diffs, GitLens-style drawers,… | `git` `ratatui` `rust` `sidebar` `terminal` | 516 | 🔄 2026-10-24 |
| [**token**](https://github.com/ThorstenRhau/token)<br><sub>ThorstenRhau</sub> | Neovim colorscheme with terminal-wide contrib themes | `bat-theme` `delta-theme` `emacs-theme` `fish-theme` `fzf-theme` | 311 | 🔄 2026-10-26 |
| [**herdr-nvim**](https://github.com/ChmaraX/herdr-nvim)<br><sub>ChmaraX</sub> | Neovim, fully integrated into your herdr workspace | `lua` `neovim` `nvim` `nvim-plugin` `rust` | 310 | 🔄 2026-10-22 |
| [**herdr-mirror**](https://github.com/nikok6/herdr-mirror)<br><sub>nikok6</sub> | Unify your local and remote sessions in one window: mirror remote herdr servers into your local sidebar and drive them over SSH | `rust` | 261 | 2026-09-06 |
| [**dotfiles**](https://github.com/edmundmiller/dotfiles)<br><sub>edmundmiller</sub> | For keeping all my Dotfiles update to date | `dotfiles` `emacs` `nix-dotfiles` `nixos` `nixos-configuration` | 80 | 🔄 2026-10-28 |
| [**herdr-lazygit**](https://github.com/Crokily/herdr-lazygit)<br><sub>Crokily</sub> | Run lazygit in a herdr sidebar pane with AI commit messages — one key to open, one to expand, one to commit | `git` `lazygit` `shell` | 43 | 2026-09-14 |
| [**herdr-agent-progress**](https://github.com/eliasstravik/herdr-agent-progress)<br><sub>eliasstravik</sub> | Agent-reported task progress and activity for the Herdr sidebar | `rust` | 34 | 2026-09-15 |
| [**herdr-yazi**](https://github.com/speardragon/herdr-yazi)<br><sub>speardragon</sub> | Open Yazi in a herdr pane | `shell` | 34 | 2026-08-19 |
| [**herdr-quicklook**](https://github.com/dwarvesf/herdr-quicklook)<br><sub>dwarvesf</sub> | Quick Look for herdr: pop the clipboard's path in an overlay, escalate to the file-viewer with one key | `terminal` `shell` | 16 | 2026-08-26 |
| [**herdr-context.nvim**](https://github.com/makyinmars/herdr-context.nvim)<br><sub>makyinmars</sub> | From Neovim, select code or stand on a line, choose a live Herdr agent, and stage structured context in that agent’s prompt—without submitting it. | `lua` | 15 | 2026-09-17 |
| [**herdr-git-status**](https://github.com/ezcorp-org/herdr-git-status)<br><sub>ezcorp-org</sub> | herdr plugin: per-space git working-tree status (staged/modified/untracked/conflicts) in the sidebar, next to the branch | `rust` | 11 | 2026-08-10 |
| [**bigtty**](https://github.com/v1k45/bigtty)<br><sub>v1k45</sub> | Native macOS client for herdr: Ghostty-rendered terminals, spaces sidebar, browser and file panes | `claude-code` `codex` `developer-tools` `ghostty` `macos` | 11 | 🔄 2026-10-21 |
| [**herdr-workbench**](https://github.com/azizuysal/herdr-workbench)<br><sub>azizuysal</sub> | A polished project sidebar for Herdr with Explorer, live file and content search, read-only Source Control, rich previews, file icons, and Git decorations. | `rust` | 9 | 🔄 2026-10-16 |
| [**herdr-fresh**](https://github.com/rvalledorjr/herdr-fresh)<br><sub>rvalledorjr</sub> | A herdr plugin that runs Fresh, the terminal IDE, as a file viewer and editor inside a herdr pane. | `developer-tools` `editor` `fresh` `ide` `terminal` | 7 | 2026-07-17 |
| [**herdr-marks-as-unread**](https://github.com/sachin-philip/herdr-marks-as-unread)<br><sub>sachin-philip</sub> | Mark agents as unread with a keyboard shortcut. A green sidebar marker reminds you to revisit them and clears when you return. | `python` | 6 | 🔄 2026-10-28 |
| [**advanced-herdr-file-viewer**](https://github.com/thuanlm215/advanced-herdr-file-viewer)<br><sub>thuanlm215</sub> | Git-aware, read-only herdr file viewer: tree, diffs, markdown, syntax, and inline image preview. | `file-viewer` `ripgrep` `rust` `tui` | 6 | 2026-09-29 |
| [**dotfiles**](https://github.com/tifandotme/dotfiles)<br><sub>tifandotme</sub> | ~/.* | `aerospace` `chezmoi` `dotfiles` `ghostty` `lazygit` | 6 | 🔄 2026-10-28 |
| [**herdr-markdown-viewer**](https://github.com/arvindparmar-me/herdr-markdown-viewer)<br><sub>arvindparmar-me</sub> | Herdr plugin: drag-select a markdown path and press prefix+m to preview it in a right-split pane. | `shell` | 5 | 2026-07-17 |
| [**herdr-file-viewer**](https://github.com/ismaelosuna7824/herdr-file-viewer)<br><sub>ismaelosuna7824</sub> | A keyboard-driven file explorer, code viewer and git client in a single Herdr pane — Go + Bubble Tea. | `bubbletea` `git` `golang` `tui` `go` | 5 | 2026-08-08 |
| [**herdr-claude-usage**](https://github.com/oszypczy/herdr-claude-usage)<br><sub>oszypczy</sub> | Claude Usage Mini: a simple, minimal Claude usage plugin for herdr. Context, 5h and 7d limit bars in the sidebar. No daemon, no credentials, no network. | `claude` `claude-code` `usage` `shell` | 5 | 2026-10-05 |
| [**herdr-disp-model**](https://github.com/pdalinis/herdr-disp-model)<br><sub>pdalinis</sub> | Display active Codex, Claude Code, Pi, and Hermes models in the Herdr agent sidebar. | `ai-agents` `claude-code` `codex` `developer-tools` `hermes-agent` | 5 | 2026-09-19 |
| [**herdr-open-in-editor**](https://github.com/timofey-TK/herdr-open-in-editor)<br><sub>timofey-TK</sub> | Open local and remote Herdr workspaces in VS Code or Zed | `vscode` `zed` `python` | 5 | 2026-07-30 |
| [**herdr-flutter**](https://github.com/ablause/herdr-flutter)<br><sub>ablause</sub> | A herdr sidebar to watch, hot reload and inspect a running Flutter app beside the coding agent. | `dart` | 4 | 2026-07-27 |
| [**herdr-wait**](https://github.com/cdc-lst/herdr-wait)<br><sub>cdc-lst</sub> | Configurable herdr plugin that tags an idle agent pane with what it's really doing — e.g. 'waiting: build-api' or 'waiting: codex' — matched from the pane's pr… | `typescript` | 4 | 2026-07-03 |
| [**herdr-lazygit**](https://github.com/JacquesvanWyk/herdr-lazygit)<br><sub>JacquesvanWyk</sub> | Open lazygit in a herdr split pane or tab with smart toggle (open / focus / close) | `lazygit` `shell` | 4 | 2026-07-12 |
| [**herdr-commander**](https://github.com/lurepos/herdr-commander)<br><sub>lurepos</sub> | Fast herdr menu to discover/launch (npm, cargo) commands or vscode tasks | `rust` | 4 | 2026-10-08 |
| [**herdr-plugin-mermaid-preview**](https://github.com/Volpestyle/herdr-plugin-mermaid-preview)<br><sub>Volpestyle</sub> | Live Mermaid previews for Claude Code and Codex output in Herdr | `claude-code` `mermaid` `openai-codex` `terminal` `javascript` | 4 | 2026-07-10 |
| [**openloc.nvim**](https://github.com/Zamua/openloc.nvim)<br><sub>Zamua</sub> | Open file references in the Neovim that already belongs to the workspace | `lua` | 4 | 2026-08-25 |
| [**herdr-open-in**](https://github.com/alexeyco/herdr-open-in)<br><sub>alexeyco</sub> | Open the current Herdr workspace in your preferred editor | `android-studio` `developer-tools` `helix` `jetbrains` `neovim` | 3 | 🔄 2026-10-22 |
| [**herdr-bandeja-to-dos**](https://github.com/gonzalonicolasr/herdr-bandeja-to-dos)<br><sub>gonzalonicolasr</sub> | Plugin de herdr: bandeja de agentes en el sidebar (quién te necesita, listos, trabajando) + to-dos que te dejan los agentes | `python` | 3 | 2026-10-02 |
| [**herdr-omp-subagents**](https://github.com/hanbong5938/herdr-omp-subagents)<br><sub>hanbong5938</sub> | Herdr sidebar metadata for live OMP subagent models, with a bundled OMP extension bridge | `typescript` | 3 | 2026-10-11 |
| [**herdr-visuals**](https://github.com/hx-w/herdr-visuals)<br><sub>hx-w</sub> | Session-scoped Mermaid, LaTeX and local image previews for Herdr with Kitty graphics proxy support | `javascript` | 3 | 2026-10-05 |
| [**herdr-yazi-windows**](https://github.com/Only-Moon/herdr-yazi-windows)<br><sub>Only-Moon</sub> | Windows port of herdr-yazi with native Windows pane spawning support via herdr v0.8+ | `file` `file-manager` `pidotdev` `python` `tui` | 3 | 2026-08-14 |
| [**herdr-x**](https://github.com/playsthisgame/herdr-x)<br><sub>playsthisgame</sub> | Browse x.com in a terminal split inside herdr, and draft posts in $EDITOR to send yourself. | `cli` `terminal` `terminal-browser` `twitter` `shell` | 3 | 2026-08-20 |
| [**scp-explorer**](https://github.com/TinocoAI/scp-explorer)<br><sub>TinocoAI</sub> | MobaXterm-style SCP file explorer herdr plugin (cross-platform macOS/Linux/Windows) | `curses` `file-manager` `scp` `python` | 3 | 2026-09-03 |
| [**herdr-wherewasi**](https://github.com/Trolzie/herdr-wherewasi)<br><sub>Trolzie</sub> | Herdr plugin: a live, rendered Markdown context sidebar beside your agents | `rust` | 3 | 2026-10-08 |
| [**herdr-yazi-links**](https://github.com/yakovlevs01/herdr-yazi-links)<br><sub>yakovlevs01</sub> | Open file hyperlinks in Yazi from Herdr; optional patch enables plain-text paths | `yazi` `python` | 3 | 🔄 2026-10-15 |
| [**agents-tree**](https://github.com/blavka/agents-tree)<br><sub>blavka</sub> | Live terminal tree of coding-agent sessions and nested subagents, with model, context use and status — Agy, Claude Code, Codex, and Grok Build. | `agy` `claude-code` `cli` `codex` `grok-build` | 2 | 🔄 2026-10-28 |
| [**herdr-covr**](https://github.com/evanbryant/herdr-covr)<br><sub>evanbryant</sub> | covr: a minimal, attention-first Spaces/Agents sidebar plugin for herdr | `python` | 2 | 2026-10-08 |
| [**herdr-footprint**](https://github.com/harpal-singh-qp/herdr-footprint)<br><sub>harpal-singh-qp</sub> | Per-space disk footprint and context usage in the Herdr sidebar. | `python` | 2 | 2026-09-16 |
| [**herdr-claude-usage-multi**](https://github.com/iamhouser/herdr-claude-usage-multi)<br><sub>iamhouser</sub> | Claude plan usage gauges in the Herdr sidebar - Session/Week %, color escalation, countdown to reset, multi-account via CLAUDE_CONFIG_DIR profiles | `claude-code` `python` | 2 | 2026-09-04 |
| [**herdr-file-viewer**](https://github.com/jomarmontuya/herdr-file-viewer)<br><sub>jomarmontuya</sub> | Right-side Herdr file tree plugin with file tabs, cwd following, git decorations, and clickable links | `go` | 2 | 2026-07-13 |
| [**herdr-agents-info**](https://github.com/rchougule/herdr-agents-info)<br><sub>rchougule</sub> | Tell your Claude Code panes apart in the herdr Agents sidebar — a distinguishing name, model, context %, and disk footprint per pane. | `claude-code` `rust` `sidebar` `terminal` `tui` | 2 | 2026-09-16 |
| [**herdr-launcher-pane**](https://github.com/y-hirakaw/herdr-launcher-pane)<br><sub>y-hirakaw</sub> | Docked click-to-launch pane for herdr — Finder/Explorer, VS Code, or any command you configure, per workspace | `launcher` `launcher-pane` `productivity` `python` | 2 | 2026-08-10 |
| [**herdr-cursor-open**](https://github.com/alex-devdone/herdr-cursor-open)<br><sub>alex-devdone</sub> | Open the focused herdr pane in Cursor or VS Code — including panes attached to a remote herdr, over Remote-SSH | `cursor` `vscode` `shell` | 1 | 2026-09-07 |
| [**🆕 herdr-context**](https://github.com/Anthodev/herdr-context)<br><sub>Anthodev</sub> | Project context dock for herdr — file tree with git status and LLM conversation history, always at your agent's side | `git` `jj` `ratatui` `rust` `sidebar` | 1 | 2026-09-30 |
| [**🆕 asgoto**](https://github.com/asumaran/asgoto)<br><sub>asumaran</sub> | Tree-style switcher across herdr repos, worktrees and panes | `go` | 1 | 2026-10-08 |
| [**herdr-sim**](https://github.com/baleen37/herdr-sim)<br><sub>baleen37</sub> | Herdr plugin: show the PRs each Claude Code / Codex pane touched as sidebar icons | `claude-code` `codex` `rust` | 1 | 🔄 2026-10-27 |
| [**🆕 herdr-agents-sidebar**](https://github.com/C0R0NELL/herdr-agents-sidebar)<br><sub>C0R0NELL</sub> | Customize Herdr’s native agent sidebar with Grouped and Priority layouts, flexible views, and per-mode colors. | `python` | 1 | 2026-10-12 |
| [**🆕 herdr-jetbrains**](https://github.com/chenyao0910/herdr-jetbrains)<br><sub>chenyao0910</sub> | Open the active Herdr workspace or worktree in Rider, WebStorm, IntelliJ IDEA, or GoLand. | `developer-tools` `git-worktree` `goland` `intellij-idea` `jetbrains` | 1 | 2026-08-30 |
| [**🆕 herdr-ids**](https://github.com/devicki/herdr-ids)<br><sub>devicki</sub> | Herdr plugin: show pane, tab and workspace ids in the sidebar, and pick a space, tab or pane to type its id into your agent | `shell` | 1 | 🔄 2026-10-16 |
| [**🆕 herdr-respawn**](https://github.com/devicki/herdr-respawn)<br><sub>devicki</sub> | Herdr plugin: relaunch lazygit, editors and other allowlisted TUIs in their panes after a server restart or reboot | `shell` | 1 | 🔄 2026-10-21 |
| [**herdr-zed-follow**](https://github.com/dlwr/herdr-zed-follow)<br><sub>dlwr</sub> | herdr plugin: Zed follows the focused herdr workspace | `zed` `shell` | 1 | 2026-09-24 |
| [**🆕 herdr-context-monitor**](https://github.com/EMRahman/herdr-context-monitor)<br><sub>EMRahman</sub> | A minimal context meter for Herdr: one Python file, no dependencies. Shows each agent's context-window use in the sidebar, for Claude Code, Codex and Antigravi… | `ai-agents` `context-window` `python` | 1 | 🔄 2026-10-14 |
| [**🆕 file-editor-viewer**](https://github.com/Freddy-system/file-editor-viewer)<br><sub>Freddy-system</sub> | View and edit files in a herdr pane: Markdown with Mermaid, Graphviz and LaTeX, source code, images. Built-in editor. Written in Rust. | `editor` `file-viewer` `graphviz` `latex` `markdown` | 1 | 🔄 2026-10-14 |
| [**🆕 herdr-vista**](https://github.com/kamil-pociot/herdr-vista)<br><sub>kamil-pociot</sub> | Herdr plugin: one key opens vista, a terminal file viewer and editor, on the git repo you're in. Another key reviews what an agent changed on its branch. | `editor` `file-viewer` `rust` | 1 | 🔄 2026-10-24 |
| [**🆕 herdr-scratchdock**](https://github.com/mvaios/herdr-scratchdock)<br><sub>mvaios</sub> | Dock a coding agent's scratchpad folder beside it in herdr — live tree, text and image previews, opens itself when the agent starts working. | `claude-code` `tui` `python` | 1 | 2026-09-28 |
| [**🆕 herdr-vimnav**](https://github.com/MykolaSuprun/herdr-vimnav)<br><sub>MykolaSuprun</sub> | Master-detail switcher for herdr — live pane previews, MRU priority sort, sidebar jump codes | `go` | 1 | 🔄 2026-10-26 |
| [**herdr-gitui**](https://github.com/Shi1xin/herdr-gitui)<br><sub>Shi1xin</sub> | herdr plugin: gitui in a sidebar pane — open/toggle, expand, light/dark themes | `gitui` `python` | 1 | 2026-07-28 |
| [**herdr-subagent-watch**](https://github.com/silencechung/herdr-subagent-watch)<br><sub>silencechung</sub> | herdr plugin: watch Claude Code sub agents live — popup viewer and sidebar tree | `javascript` | 1 | 🔄 2026-10-28 |
| [**🆕 herdr-focus**](https://github.com/Zeus-Deus/herdr-focus)<br><sub>Zeus-Deus</sub> | herdr plugin: an attention layer for the agent sidebar - clear titles, Needs you / Working / Done, unread and settle triage, and a watch eye for background PR… | `python` | 1 | 🔄 2026-10-25 |

<details><summary>Also relevant to this purpose</summary>

- [robbyrussell/herdr-ohmyzsh](https://github.com/robbyrussell/herdr-ohmyzsh) — Oh My Zsh plugin for Herdr: slow commands in the sidebar, done notifications, shell helpers, and one key to r…
- [ChmaraX/herdr-gitview](https://github.com/ChmaraX/herdr-gitview) — Git status/diff panel for herdr - review changes, edit in nvim, stage/commit/discard, all from the terminal
- [vonzelle-vzt/herdr-extensions](https://github.com/vonzelle-vzt/herdr-extensions) — Tiny VS Code for herdr: a real editor with LSP diagnostics, autocomplete, rename and go-to-definition — plus…
- [jsmenzies/mergr](https://github.com/jsmenzies/mergr) — GitHub pull request status for Herdr Space sidebar rows.
- [xzedx/herdr-easyjump](https://github.com/xzedx/herdr-easyjump) — Press a key, type a letter, jump to any space, agent, pane, or tab. EasyMotion / Vimium / vim-choosewin style…
- [edxeth/herdr-pi-tree](https://github.com/edxeth/herdr-pi-tree) — A sidebar that shows your Pi agents as a tree — who spawned whom, which worktree is which branch, who's waiti…
- [H3xept/herdr-aspire-hud](https://github.com/H3xept/herdr-aspire-hud) — Live .NET Aspire AppHost health for every herdr space: sidebar badges and a popup HUD
- [4242labs/herdr-radar-plus](https://github.com/4242labs/herdr-radar-plus) — Herdr plugin: agents sorted by what needs you, in named groups that span machines. Built on herdr-radar.
- [amali01/herdr-pacer](https://github.com/amali01/herdr-pacer) — Herdr plugin: context-window bars under each agent in the sidebar, plus a 5h/weekly usage popup for Claude, C…
- [brianh20/herdr-stagr](https://github.com/brianh20/herdr-stagr) — Source Control sidebar for herdr: stage, unstage, and discard with side-by-side diffs
- [ivanvykopal/herdr-slurm](https://github.com/ivanvykopal/herdr-slurm) — Live SLURM/HPC job monitor sidebar for herdr (Rust): squeue for your clusters over SSH, native sidebar token,…
- [maedana/herdr-whereami](https://github.com/maedana/herdr-whereami) — Herdr plugin that automatically renames tabs to show where you are, e.g. repo-name/branch when inside a git r…
- [mcostasilva/herdr-marks](https://github.com/mcostasilva/herdr-marks) — Neovim-style letter marks for Herdr panes and workspaces, with colored sidebar labels and quick navigation
- [bayoudhi/herdr-prayer-times](https://github.com/bayoudhi/herdr-prayer-times) — Next Islamic prayer and countdown in the Herdr sidebar, with a timetable popup and notifications
- [ecklf/herdr-plugin-gh](https://github.com/ecklf/herdr-plugin-gh) — GitHub PR and CI status in Herdr's Agents sidebar, with open/create PR and failing-check actions.
- [jwanga/herdr-plugin-github-status](https://github.com/jwanga/herdr-plugin-github-status) — herdr plugin: a real-time GitHub project status pane (milestones, issues, PRs, Actions) docked on the right a…
- [mastnacek/pi-herdr-sidebar](https://github.com/mastnacek/pi-herdr-sidebar) — Native Rust Herdr plugin sidebar for the Pi coding agent: status telemetry, live skills, gates — VSA slices i…
- [ralphilius/herdr-github-metadata](https://github.com/ralphilius/herdr-github-metadata) — Herdr plugin: GitHub metadata for the sidebar — the PR each agent is working on
- [ShinoharaHaruna/mimo-code-herdr](https://github.com/ShinoharaHaruna/mimo-code-herdr) — MiMo Code <-> herdr custom-agent bridge: lifecycle state in the sidebar, crash-proof exit cleanup, one-comman…
- [yojahny55/herdr-space-groups](https://github.com/yojahny55/herdr-space-groups) — Herdr plugin: group Spaces into named, colored groups — picker popup (mouse + keyboard), sidebar group header…
- [ZingerLittleBee/herdr-agent-pins](https://github.com/ZingerLittleBee/herdr-agent-pins) — Persistently pin Herdr agent sessions to the top of the Agents sidebar.

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-cost"></a>

## Tokens & Cost

> I want to see how much an agent is spending, and cut down on usage

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**memex**](https://github.com/nicosuave/memex)<br><sub>nicosuave</sub> | Search Claude Code, Codex, Pi, OpenCode, Github Copilot & Cursor transcripts. Resume sessions. Track tokens. | `bm25` `claude-code` `codex-cli` `copilot` `hermes-agent` | 292 | 🔄 2026-10-28 |
| [**herdr-agent-usage**](https://github.com/senna-lang/herdr-agent-usage)<br><sub>senna-lang</sub> | Context meters, quota tracking, and provider rate limits for agents running in Herdr. | `ai-agents` `claude-code` `codex` `golang` `rate-limiting` | 62 | 🔄 2026-10-25 |
| [**llmtrim-herdr**](https://github.com/fkiene/llmtrim-herdr)<br><sub>fkiene</sub> | 💸 Shrink your token bill in herdr: compresses every agent pane's requests (-31% input / -74% output, measured live) and shows the savings on a per-pane badge | `llm-proxy` `llmtrim` `powershell` | 58 | 2026-07-02 |
| [**quota**](https://github.com/pinkpixel-dev/quota)<br><sub>pinkpixel-dev</sub> | Desktop app, VSCode extension, CLI, and Herdr plugin for tracking AI usage across GitHub Copilot, Codex, Claude Code, Antigravity, Kiro, Grok, Cursor and OpenC… | `ai-tools` `antigravity` `claude` `codex` `cursor` | 33 | 🔄 2026-10-20 |
| [**herdr-token-dashboard**](https://github.com/Davidcreador/herdr-token-dashboard)<br><sub>Davidcreador</sub> | Live token spend dashboard and notifications for Herdr agent panes | `ai-agents` `bubbletea` `opencode` `pi-agent` `token-dashboard` | 28 | 2026-10-09 |
| [**herdr-grazr**](https://github.com/wazum/herdr-grazr)<br><sub>wazum</sub> | A simple and reliable auto account switcher for Claude Code: rotates to a fresh account before the 5-hour or weekly rate limit hits, so no pane ever stops at t… | `account-rotation` `account-switcher` `account-switching` `anthropic` `claude` | 5 | 🔄 2026-10-21 |
| [**🆕 account-capacity-dock**](https://github.com/Mako-L/account-capacity-dock)<br><sub>Mako-L</sub> | Quota rings for every Claude, Codex and Cursor account: a desktop dock, a terminal app and a Herdr widget. | `claude` `cliproxyapi` `codex` `cursor` `python` | 4 | 🔄 2026-10-28 |
| [**herdr-ctx-bar**](https://github.com/pdalinis/herdr-ctx-bar)<br><sub>pdalinis</sub> | Color-coded context-window usage bars for Codex, Claude Code, Pi, and Hermes Agent in Herdr's Agents sidebar. | `ai-agents` `claude-code` `codex` `context-window` `hermes-agent` | 4 | 2026-09-19 |
| [**herdr-claude-usage**](https://github.com/alejodelosrios/herdr-claude-usage)<br><sub>alejodelosrios</sub> | Stop opening a Claude session just to check your quota. Live Claude plan usage — Session % \| Week % — always visible in your Herdr sidebar, shared across ever… | `claude` `claude-code` `python` | 3 | 2026-07-21 |
| [**agentglass-herdr**](https://github.com/BjoernSchotte/agentglass-herdr)<br><sub>BjoernSchotte</sub> | agentglass inside herdr: popup, open-in-agentglass, agentglass:// links, cost and alert tokens | `agentglass` `coding-agents` `shell` | 3 | 2026-10-07 |
| [**herdr-opentab**](https://github.com/hamidi-dev/herdr-opentab)<br><sub>hamidi-dev</sub> | Live per-agent AI spend from OpenTab in the Herdr sidebar. | `ai-agents` `opentab` `terminal` `python` | 3 | 2026-10-07 |
| [**herdr-jarvis**](https://github.com/NexorPL/herdr-jarvis)<br><sub>NexorPL</sub> | Mission control for herdr: animated big-picture core, projects by path, threads, timeline and token usage. | `rust` | 3 | 🔄 2026-10-28 |
| [**herdr-gekiatsu-plugin**](https://github.com/yuuta1219/herdr-gekiatsu-plugin)<br><sub>yuuta1219</sub> | herdr plugin: Claude Code usage counter, but it's a pachislot machine. 1/99 jackpot, daily reset at 10:00 JST | `claude` `claude-code` `python` `tui` | 3 | 2026-08-17 |
| [**quota-deck**](https://github.com/ArtMoreno/quota-deck)<br><sub>ArtMoreno</sub> | quota-deck: credential-scoped AI quota and context for Herdr on Windows, macOS, and Linux | `rust` | 2 | 2026-10-03 |
| [**herdr-account-hub**](https://github.com/C0R0NELL/herdr-account-hub)<br><sub>C0R0NELL</sub> | Manage Codex, Claude accounts in Herdr, track usage, and use resets. Switch Codex accounts without losing chat history or titles. Claude Code support is beta. | `herd-management` `python` | 2 | 🔄 2026-10-23 |
| [**herdr-api-credit-bar**](https://github.com/CristianPeralta/herdr-api-credit-bar)<br><sub>CristianPeralta</sub> | Herdr plugin: remaining credit for pay-as-you-go API providers, starting with Alibaba Cloud Model Studio | `shell` | 2 | 2026-09-05 |
| [**herdr-slurm**](https://github.com/ivanvykopal/herdr-slurm)<br><sub>ivanvykopal</sub> | Live SLURM/HPC job monitor sidebar for herdr (Rust): squeue for your clusters over SSH, native sidebar token, width-adaptive table | `hpc` `slurm` `rust` | 2 | 2026-10-03 |
| [**herdr-quota**](https://github.com/kvkenyon/herdr-quota)<br><sub>kvkenyon</sub> | See Claude, Codex, Cursor, and Kimi subscription quota at a glance in Herdr. | `ai-tools` `claude-code` `cursor` `developer-tools` `kimi` | 2 | 2026-09-05 |
| [**herdr-whereami**](https://github.com/maedana/herdr-whereami)<br><sub>maedana</sub> | Herdr plugin that automatically renames tabs to show where you are, e.g. repo-name/branch when inside a git repository. | `rust` | 2 | 2026-09-14 |
| [**herdr-burnlog**](https://github.com/naturalmoods/herdr-burnlog)<br><sub>naturalmoods</sub> | Local project-based token and recorded-cost history for Herdr agents | `python` | 2 | 2026-09-28 |
| [**herdr-opencodex**](https://github.com/nordz0r/herdr-opencodex)<br><sub>nordz0r</sub> | OpenCodex Herdr plugins: spend stats and remaining 5h/7d quota | `opencodex` `quota` `rust` | 2 | 🔄 2026-10-15 |
| [**🆕 herdr-cache-hit**](https://github.com/e-kotov/herdr-cache-hit)<br><sub>e-kotov</sub> | Prompt-cache HUD tokens, real-time expiration alerts, and dynamic agent sorting for Herdr | `agentic-ai` `antigravity` `cache` `claude-code` `cli` | 1 | 🔄 2026-10-27 |
| [**🆕 scopefuel**](https://github.com/mgh3326/scopefuel)<br><sub>mgh3326</sub> | Scope-aware headroom gauge for AI coding agent plans — what is actually blocked (account/model/group) and when it refills | `ai-agents` `antigravity` `claude-code` `cli` `codex` | 1 | 🔄 2026-10-28 |
| [**🆕 herdr-model-lanes**](https://github.com/terry-li-hm/herdr-model-lanes)<br><sub>terry-li-hm</sub> | Herdr plugin: Codex, Claude Max and Grok quota in the workspace row, plus quota-aware model-class lanes (ag) for new agents | `claude` `codex` `grok` `model-routing` `quota` | 1 | 🔄 2026-10-22 |

<details><summary>Also relevant to this purpose</summary>

- [ThorstenRhau/token](https://github.com/ThorstenRhau/token) — Neovim colorscheme with terminal-wide contrib themes
- [jeffarese/herdr-agent-grid](https://github.com/jeffarese/herdr-agent-grid) — A fast native Rust command center for Herdr: agents, subagents, status, messages and API cost.
- [VHemanth45/herdr_agents_tracker](https://github.com/VHemanth45/herdr_agents_tracker) — Herdr plugin that shows your AI subscription usage: account limits in the tab bar, a context meter per agent,…
- [romiluz13/instinct-herdr-tunnel](https://github.com/romiluz13/instinct-herdr-tunnel) — Let an AI assistant such as Instinct watch and steer your Herdr coding agents: a loopback portal with a 26-ac…
- [pgilad/herdr-yank](https://github.com/pgilad/herdr-yank) — Inline keyboard hints for copying visible tokens or opening URLs and files from Herdr panes.

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-monitor"></a>

## Monitoring & Dashboards

> I want an at-a-glance overview of agent and machine status

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**zoetrope**](https://github.com/furkankly/zoetrope)<br><sub>furkankly</sub> | Watch a Claude Code or Codex session as a live flow graph, in your terminal or your browser. | `agent-visualization` `claude-code` `codex` `coding-agents` `flow` | 1116 | 🔄 2026-10-14 |
| [**clauth**](https://github.com/uwuclxdy/clauth)<br><sub>uwuclxdy</sub> | Claude Code multi-account manager, usage monitor (CLI, TUI & cross-account delegation via MCP) | `account-manager` `account-switcher` `anthropic` `claude` `claude-code` | 273 | 🔄 2026-10-28 |
| [**herdr-radar**](https://github.com/hhdebb/herdr-radar)<br><sub>hhdebb</sub> | Who's working, who's waiting on you — grouped by project, each agent in its vendor's logo and colour. Worktrees nest under their repo, rows order by activity,… | `claudecode` `codex-cli` `coding-agents-plugins` `developer-tools-ai-agent` `terminal-multiplexers` | 197 | 🔄 2026-10-26 |
| [**captains-deck**](https://github.com/deimantasnork/captains-deck)<br><sub>deimantasnork</sub> | Captain's Deck - a read-only Firstmate flow kanban plugin for Herdr | `firstmate` `python` | 70 | 🔄 2026-10-22 |
| [**herdr-beads**](https://github.com/miiraheart/herdr-beads)<br><sub>miiraheart</sub> | A beads (bd) task board for herdr: List, Table, Kanban over your bd issues, docked as a sidebar or floating. | `bd` `beads` `kanban` `rust` `tui` | 40 | 2026-10-08 |
| [**herdr-pc-ram-and-cpu-usage-overlay**](https://github.com/ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay)<br><sub>ezcorp-org</sub> | herdr plugin: live CPU/RAM usage per space (workspace), as a share of the whole machine | `rust` | 29 | 2026-09-13 |
| [**herdr-f1**](https://github.com/hmu332233/herdr-f1)<br><sub>hmu332233</sub> | An F1-style dashboard for your Herdr agents. | `agent-dashboard` `typescript` | 18 | 2026-10-09 |
| [**herdr-agent-grid**](https://github.com/jeffarese/herdr-agent-grid)<br><sub>jeffarese</sub> | A fast native Rust command center for Herdr: agents, subagents, status, messages and API cost. | `agent-dashboard` `ai-agents` `claude-code` `codex` `ratatui` | 17 | 🔄 2026-10-16 |
| [**herdr-shell-progress**](https://github.com/bayoudhi/herdr-shell-progress)<br><sub>bayoudhi</sub> | Herdr plugin: live sidebar progress for slow shell commands, not just coding agents | `rust` | 16 | 2026-09-23 |
| [**herdr-telemetry**](https://github.com/DIodide/herdr-telemetry)<br><sub>DIodide</sub> | Herdr plugin that streams workspace & agent telemetry to an endpoint you control — Go, single binary, privacy-first defaults | `golang` `telemetry` `go` | 12 | 2026-07-10 |
| [**🆕 visor**](https://github.com/oronbz/visor)<br><sub>oronbz</sub> | A terminal dashboard your coding agent sets up: PRs, Jira, calendar and anything else, with Plugins in any language. | `ai-agents` `bubbletea` `claude-code` `cli` `dashboard` | 12 | 🔄 2026-10-28 |
| [**shepherd**](https://github.com/ryonakae/shepherd)<br><sub>ryonakae</sub> | Worker observability daemon and runtime bridges for Herdr-managed coding agents. | `pi-coding-agent` `pi-extension` `typescript` | 12 | 2026-08-28 |
| [**herdr-lcars**](https://github.com/jlcases/herdr-lcars)<br><sub>jlcases</sub> | Command up to 2,000 Herdr AI agents from one LCARS bridge, track Claude/Codex quota per account, and hand off verified context without losing work. | `agent-observability` `ai-agents` `claude-code` `lcars` `openai-codex` | 10 | 2026-10-10 |
| [**herdr-sysmon**](https://github.com/getpipher/herdr-sysmon)<br><sub>getpipher</sub> | System metrics in the Herdr sidebar — CPU, memory, battery, network, disk, clock. A faithful port of a tmux-cpu/tmux-battery/tmux-online-status status bar into… | `battery` `catppuccin` `cpu` `getpipher` `macos` | 8 | 2026-07-26 |
| [**herdr-tally**](https://github.com/jasonrr/herdr-tally)<br><sub>jasonrr</sub> | Project-scoped todos & scratchpads for you and your agents.<br>📝 プロジェクト単位の TODO 管理 | `rust` `todo` | 8 | 🔄 2026-10-14 |
| [**herdr-ports**](https://github.com/Numbered-com/herdr-ports)<br><sub>Numbered-com</sub> | Surface active dev servers in herdr: a generic $ports badge on every Space running at least one TCP listener | `kill` `pids` `ports` `processes` `space` | 7 | 2026-09-29 |
| [**herdr-workboard**](https://github.com/Phoobobo/herdr-workboard)<br><sub>Phoobobo</sub> | Kanban workboard TUI for herdr: boards are workspaces, task states are tabs, task sessions are panes | `kanban` `tui` `typescript` | 7 | 2026-08-10 |
| [**herdr-devserver-status**](https://github.com/Razz21/herdr-devserver-status)<br><sub>Razz21</sub> | Herdr plugin that detects dev servers in panes via pluggable specs and reports lifecycle status. | `astro` `cli` `deamon` `dev-server` `extensible` | 7 | 🔄 2026-10-24 |
| [**herdr-lazydocker**](https://github.com/sudoeren/herdr-lazydocker)<br><sub>sudoeren</sub> | Run lazydocker in a herdr split pane or its own tab. | `docker` `lazydocker` `shell` | 7 | 2026-08-27 |
| [**herdr-monitoring**](https://github.com/enes/herdr-monitoring)<br><sub>enes</sub> | Herdr resource monitor plugin with agent summary and focused pane views | `rust` | 6 | 2026-09-28 |
| [**shepherd**](https://github.com/jwarykowski/shepherd)<br><sub>jwarykowski</sub> | your todos herded | `cli` `developer-tools` `go-lang` `productivity` `task-management` | 6 | 🔄 2026-10-26 |
| [**herdr-kanban**](https://github.com/KokiKono/herdr-kanban)<br><sub>KokiKono</sub> | Terminal Kanban board that links tasks to herdr tabs, persisted in SQLite | `rust` | 6 | 2026-07-10 |
| [**sbx-herdr**](https://github.com/dvdksn/sbx-herdr)<br><sub>dvdksn</sub> | Herdr integration for Docker Sandboxes | `go` | 5 | 🔄 2026-10-23 |
| [**herdr-jcode**](https://github.com/leonardoacosta/herdr-jcode)<br><sub>leonardoacosta</sub> | Standalone Herdr plugin that reports Jcode working/idle lifecycle state plus session identity. Independent implementation; no fork dependency. | `jcode` `rust` | 5 | 2026-09-16 |
| [**herdr_agents_tracker**](https://github.com/VHemanth45/herdr_agents_tracker)<br><sub>VHemanth45</sub> | Herdr plugin that shows your AI subscription usage: account limits in the tab bar, a context meter per agent, low-limit alerts and a token dashboard for Claude… | `chatgpt` `claude` `claude-code` `codex` `herdr-integration` | 5 | 2026-09-24 |
| [**herdr-agent-watcher**](https://github.com/winoooops/herdr-agent-watcher)<br><sub>winoooops</sub> | Coding-agent observability for Herdr: live sidebar cards, lifecycle notifications, and a zero-config Claude Code metrics bridge. | `claude-code` `rust` | 5 | 2026-09-21 |
| [**herdr-mise**](https://github.com/funsaized/herdr-mise)<br><sub>funsaized</sub> | Run the pass, not the prompts 🧑‍🍳 A visualizer for your agents. A herdr plugin. Intentionally small footprint | `agent` `agent-monitoring` `ai-agents` `cli-tool` `developer-tools` | 4 | 🔄 2026-10-26 |
| [**herdr-portal**](https://github.com/loofare/herdr-portal)<br><sub>loofare</sub> | Mission-control dashboard for herdr — aggregates every workspace/tab/pane agent into a live TUI kanban (keyboard + mouse) plus a web big-screen: structured pro… | `agent-dashboard` `agent-monitor` `ai-agents` `claude-code` `codex` | 4 | 🔄 2026-10-19 |
| [**herdr-status-ui-bar**](https://github.com/speardragon/herdr-status-ui-bar)<br><sub>speardragon</sub> | AI agent plan-usage gauges (Claude Code / Codex / Grok) in the herdr tab bar | `claude-code` `codex` `grok` `python` `tab-bar` | 4 | 2026-10-05 |
| [**🆕 herdr-claude-usage**](https://github.com/aodanchenko/herdr-claude-usage)<br><sub>aodanchenko</sub> | Global Claude Code plan usage in Herdr: tab-bar summary + popup dashboard. statusLine-powered, multi-account aware. | `claude` `claude-code` `cli` `terminal` `shell` | 3 | 2026-09-01 |
| [**herdr-codex-bridge**](https://github.com/ardasevinc/herdr-codex-bridge)<br><sub>ardasevinc</sub> | Native Herdr pane identity for Codex sessions using a centralized app-server | `ai-agents` `codex` `terminal` `go` | 3 | 🔄 2026-10-22 |
| [**herdr-macos-plugins**](https://github.com/klinter007/herdr-macos-plugins)<br><sub>klinter007</sub> | Files and Links, Stay Awake, and System Monitor plugins for standard Herdr on macOS | `python` | 3 | 2026-10-12 |
| [**herdr-tasks**](https://github.com/MatheusBBarni/herdr-tasks)<br><sub>MatheusBBarni</sub> | Kanban task runner for Herdr: OpenTUI board plus htasks CLI | `typescript` | 3 | 2026-09-11 |
| [**herdr-vitals**](https://github.com/mrolafsson/herdr-vitals)<br><sub>mrolafsson</sub> | How your machines are doing, at a glance, before they slow your agents down. A herdr plugin: CPU, load, memory, disks (and when they'll be full) and network fo… | `anthropic` `bubbletea` `claude-code` `codex` `coding-agents` | 3 | 🔄 2026-10-20 |
| [**herdr-slurm**](https://github.com/quan-meng/herdr-slurm)<br><sub>quan-meng</sub> | Create Herdr workspaces and monitored agent tabs for Slurm allocations | `hpc` `slurm` `terminal-multiplexer` `python` | 3 | 2026-08-13 |
| [**herdr-mem-cpu-load**](https://github.com/thewtex/herdr-mem-cpu-load)<br><sub>thewtex</sub> | CPU, memory, and load average monitor for herdr. | `rust` | 3 | 2026-09-07 |
| [**herdr-agent-state**](https://github.com/Tyru5/herdr-agent-state)<br><sub>Tyru5</sub> | Realtime agent status pane for herdr; what each agent in the workspace is working on (in a more human-readable format) | `claude-code` `rust` `terminal` | 3 | 2026-09-22 |
| [**adlc-herdr**](https://github.com/voodootikigod/adlc-herdr)<br><sub>voodootikigod</sub> | ADLC herdr plugin — per-pane phase/ticket/gate status, backlog board, gate actions, and adlc-fleet run observability. Auto-synced mirror of voodootikigod/adlc/… | `javascript` | 3 | 🔄 2026-10-25 |
| [**herdr-cache-timer**](https://github.com/ArteenHD/herdr-cache-timer)<br><sub>ArteenHD</sub> | Shows when each agent's prompt cache expires, right in the Herdr sidebar. | `claude-code` `prompt-caching` `terminal` `javascript` | 2 | 2026-08-08 |
| [**herdr-agent-dashboard**](https://github.com/carsonjones/herdr-agent-dashboard)<br><sub>carsonjones</sub> | prefix +a show herdr agents | `typescript` | 2 | 2026-07-16 |
| [**tsk**](https://github.com/chrisg32/tsk)<br><sub>chrisg32</sub> | tsk — a TaskPaper/PlainTasks-style plain-text task TUI, written in Rust. Runs standalone or as a herdr plugin. | `rust` `taskpaper` `todo` `tui` | 2 | 2026-09-03 |
| [**herdr-telemetry-bridge**](https://github.com/CodyBontecou/herdr-telemetry-bridge)<br><sub>CodyBontecou</sub> | Herdr plugin that streams local workspace, repo, coding-agent, model, and trace telemetry to external clients. | `coding-agents` `telemetry` `time-md` `javascript` | 2 | 2026-06-26 |
| [**herdr-agentsview**](https://github.com/cpcloud/herdr-agentsview)<br><sub>cpcloud</sub> | AgentsView activity, compressed into one very busy terminal. | `rust` | 2 | 🔄 2026-10-17 |
| [**herdr-spinner**](https://github.com/hasuwini77/herdr-spinner)<br><sub>hasuwini77</sub> | Animated braille spinner for Herdr panes in the working state, via display-only pane metadata | `ai-agents` `claude-code` `herdr-theme` `spinner` `terminal` | 2 | 2026-09-25 |
| [**herdr-statusline**](https://github.com/iiii1224/herdr-statusline)<br><sub>iiii1224</sub> | Customizable status line for herdr sessions. | `cli` `statusbar` `statusline` `tmux` `python` | 2 | 2026-08-15 |
| [**herdr-goose-bridge**](https://github.com/inoribea/herdr-goose-bridge)<br><sub>inoribea</sub> | Herdr plugin that reports goose agent lifecycle state (idle / working / blocked) into your panes. goose is a line-mode CLI, so Herdr cannot detect it on its ow… | `agent-state` `ai-agents` `developer-tools` `goose` `goose-cli` | 2 | 2026-09-11 |
| [**herdr-jira-board**](https://github.com/kiitosu/herdr-jira-board)<br><sub>kiitosu</sub> | Jira kanban board inside herdr with Claude Code session launcher | `python` | 2 | 🔄 2026-10-28 |
| [**🆕 herdr-sbx**](https://github.com/lanwen/herdr-sbx)<br><sub>lanwen</sub> | Herdr Plugin to enable Docker Sandboxes as SSH connected machines. Full agent visibility, plugin sync | `docker` `sandboxes` `go` | 2 | 🔄 2026-10-26 |
| [**kanban_tui**](https://github.com/m0hdrar/kanban_tui)<br><sub>m0hdrar</sub> | Keyboard-first kanban board for the terminal | `typescript` | 2 | 🔄 2026-10-18 |
| [**herdr-cache-ttl**](https://github.com/nytafar/herdr-cache-ttl)<br><sub>nytafar</sub> | Herdr plugin: live prompt-cache TTL countdown per agent pane | `rust` | 2 | 2026-10-02 |
| [**herdr-ports**](https://github.com/randomradio/herdr-ports)<br><sub>randomradio</sub> | Herdr plugin: forward a remote workspace port to http://herdr.{workspace}.localhost:{port} | `rust` | 2 | 2026-09-20 |
| [**herdr-tilt**](https://github.com/the-inconvenience-store/herdr-tilt)<br><sub>the-inconvenience-store</sub> | A keyboard-driven Tilt dashboard for Herdr | `k8s` `kubernetes` `tilt` `rust` | 2 | 🔄 2026-10-23 |
| [**herdr-memex-analytics**](https://github.com/vishnutskumar/herdr-memex-analytics)<br><sub>vishnutskumar</sub> | Herdr plugin: session efficiency analytics and realtime agent guidance, powered by memex history | `rust` | 2 | 2026-09-01 |
| [**herdr-docker**](https://github.com/abcxff/herdr-docker)<br><sub>abcxff</sub> | Keep track of docker builds like you do with agents for herdr. | `docker` `javascript` | 1 | 2026-08-12 |
| [**🆕 herdr-muse**](https://github.com/akshat12/herdr-muse)<br><sub>akshat12</sub> | Herdr integration for Muse Code: idle/working/blocked pane state via lifecycle hooks (no Herdr fork needed) | `ai-agents` `cli` `coding-agents` `muse-code` `terminal` | 1 | 2026-09-12 |
| [**🆕 herdr-glance**](https://github.com/arvmaan/herdr-glance)<br><sub>arvmaan</sub> | desktop widget to view the status of your agents | `rust` | 1 | 2026-09-08 |
| [**herdr-tokscale-dashboard**](https://github.com/astkaasa/herdr-tokscale-dashboard)<br><sub>astkaasa</sub> | Open Tokscale as a local Herdr dashboard pane. | `dashboard` `tokscale` `shell` | 1 | 2026-06-26 |
| [**herdr-nodejs-center**](https://github.com/AZenking/herdr-nodejs-center)<br><sub>AZenking</sub> | A Herdr popup for monitoring and focusing local Node.js, Bun, and Deno services | `developer-tools` `nodejs` `javascript` | 1 | 🔄 2026-10-18 |
| [**herdr-plugin-codex-subs**](https://github.com/benkraus/herdr-plugin-codex-subs)<br><sub>benkraus</sub> | Herdr dashboard for CLIProxyAPI Codex subscription quotas and reset credits | `go` | 1 | 2026-07-30 |
| [**🆕 herdr-machine-memory**](https://github.com/gosuwtf/herdr-machine-memory)<br><sub>gosuwtf</sub> | Herdr plugin: tab-bar memory usage for this machine and every connected Herdr machine | `python` | 1 | 🔄 2026-10-25 |
| [**herdr-overview**](https://github.com/iamgp/herdr-overview)<br><sub>iamgp</sub> | Mission Control / Exposé for Herdr — a live tiled overview of every space | `terminal` `tui` `javascript` | 1 | 2026-08-28 |
| [**herdr-ports**](https://github.com/ivorpad/herdr-ports)<br><sub>ivorpad</sub> | Herdr plugin: a popup that lists listening ports, names the project behind each one, and kills or opens it | `tui` `python` | 1 | 2026-08-27 |
| [**🆕 herdr-stats**](https://github.com/jeffarese/herdr-stats)<br><sub>jeffarese</sub> | Live CPU, memory, disk, temperature, GPU, power and network stats in herdr's tab bar: braille graphs, gauges and reactive icons | `linux` `macos` `rust` `system-monitor` `terminal` | 1 | 🔄 2026-10-23 |
| [**herdr-metrics**](https://github.com/jordanhawkes/herdr-metrics)<br><sub>jordanhawkes</sub> | Context, session-token and account-limit metrics for Claude Code, Codex and TraeX in the Herdr sidebar. Maintained continuation of szrenwei/herdr-agent-metrics. | `claude-code` `openai-codex` `traex` `tui` `python` | 1 | 2026-08-22 |
| [**🆕 herdr-job-board**](https://github.com/larrychannon/herdr-job-board)<br><sub>larrychannon</sub> | A To do / Doing / Waiting-on-you board for agent jobs, in a Herdr split pane. | `javascript` | 1 | 🔄 2026-10-28 |
| [**pi-herdr-sidebar**](https://github.com/mastnacek/pi-herdr-sidebar)<br><sub>mastnacek</sub> | Native Rust Herdr plugin sidebar for the Pi coding agent: status telemetry, live skills, gates — VSA slices in Rust/Ratatui | `pi` `ratatui` `rust` | 1 | 🔄 2026-10-14 |
| [**herdr-compose**](https://github.com/mattyan1053/herdr-compose)<br><sub>mattyan1053</sub> | Herdr Plugin for docker compose | `terminal` `tui` `shell` | 1 | 2026-07-24 |
| [**🆕 herdr-agent-board**](https://github.com/NoctisHsu/herdr-agent-board)<br><sub>NoctisHsu</sub> | Live task board for coding agents running in Herdr panes | `python` | 1 | 🔄 2026-10-14 |
| [**🆕 mission-control-capcom**](https://github.com/philals/mission-control-capcom)<br><sub>philals</sub> | Mission control for story-driven work: local kanban boards, Claude Code skills and a live terminal board for tasks, draft PRs, CI and manual runs | `claude-code` `kanban` `rust` `tui` | 1 | 🔄 2026-10-27 |
| [**🆕 herdr-readpending**](https://github.com/rcosteira79/herdr-readpending)<br><sub>rcosteira79</sub> | Mark agents you haven't finished reading. Numbered badge ($read) + a reorderable list pane. Auto-clears when you focus the agent. | `python` | 1 | 2026-09-15 |
| [**🆕 herdr-agent-metrics**](https://github.com/szrenwei/herdr-agent-metrics)<br><sub>szrenwei</sub> | Lightweight Herdr context and session usage metrics for Claude Code, Codex, and TraeX. | `claude-code` `openai-codex` `traex` `python` | 1 | 2026-08-04 |
| [**🆕 herdr-space-tab-metadata**](https://github.com/szrenwei/herdr-space-tab-metadata)<br><sub>szrenwei</sub> | Show each Herdr Space's active tab in the sidebar | `terminal-ui` `python` | 1 | 2026-08-04 |
| [**🆕 herdeck**](https://github.com/thefahien/herdeck)<br><sub>thefahien</sub> | Turn commands, processes, health checks, JSON APIs and Prometheus queries into live tabs in a herdr pane | `curses` `monitoring` `prometheus` `python` `terminal-dashboard` | 1 | 🔄 2026-10-23 |
| [**🆕 taskherd**](https://github.com/ukwhatn/taskherd)<br><sub>ukwhatn</sub> | Task board linked to herdr agent sessions, PRs, and Jira tickets | `claude-code` `kanban` `task-management` `tui` `go` | 1 | 2026-09-01 |
| [**herdr-virtualboard**](https://github.com/virtualboard/herdr-virtualboard)<br><sub>virtualboard</sub> | Kanban board for VirtualBoard feature specs inside Herdr: columns are the lifecycle, cards are specs, and dispatching a card starts a role agent in a pane. | `go` | 1 | 🔄 2026-10-16 |
| [**🆕 corgi**](https://github.com/zyrre/corgi)<br><sub>zyrre</sub> | A compact dashboard for Herdr coding agents, with supervisor coordination and an Omarchy bar widget. | `claude-code` `codex` `tui` `rust` | 1 | 🔄 2026-10-28 |

<details><summary>Also relevant to this purpose</summary>

- [nelsonPires5/herdr-board](https://github.com/nelsonPires5/herdr-board) — Kanban board for herdr — cards are prompts dispatched to AI agents in visible panes
- [e2b-dev/herdr-e2b-sandbox](https://github.com/e2b-dev/herdr-e2b-sandbox) — herdr plugin that mirrors a git worktree into an E2B sandbox — one box or a branch-per-agent fleet, with a TU…
- [quaywin/agys](https://github.com/quaywin/agys) — Effortless multi-profile isolation & real-time quota tracking for Antigravity CLI in Herdr via zero-pollution…
- [Northern-Lighthouse/herdr-fleet](https://github.com/Northern-Lighthouse/herdr-fleet) — Manage a fleet of herdr machines over Tailscale: dashboard plugin, auto-discovery, capacity-aware agent dispa…
- [cdowell09/herdr-pr-board](https://github.com/cdowell09/herdr-pr-board) — Configurable cross-repository GitHub pull request dashboard for Herdr
- [bengemine/herdr-hibernate](https://github.com/bengemine/herdr-hibernate) — Hibernate idle coding-agent panes in Herdr (Claude Code, Codex, Grok) — free the RAM, press Enter to resume t…
- [spad-0x/herdr-mobile-pro](https://github.com/spad-0x/herdr-mobile-pro) — A high-performance, mobile-first PWA dashboard with a Cyber-Dark design for orchestrating Herdr and autonomou…
- [4242labs/herdr-radar-plus](https://github.com/4242labs/herdr-radar-plus) — Herdr plugin: agents sorted by what needs you, in named groups that span machines. Built on herdr-radar.
- [eugeneb50/herdr-mcp](https://github.com/eugeneb50/herdr-mcp) — herdr plugin and MCP server: drive herdr panes and agents from AI clients, with recipes, triggers, schedules,…
- [ivanvykopal/herdr-slurm](https://github.com/ivanvykopal/herdr-slurm) — Live SLURM/HPC job monitor sidebar for herdr (Rust): squeue for your clusters over SSH, native sidebar token,…
- [Javamomma/herdr-scribe](https://github.com/Javamomma/herdr-scribe) — herdr plugin: live no-recording meeting transcription — mic → RAM-only transcript + live analyst panes; on st…
- [sazardev/herdr-code-board](https://github.com/sazardev/herdr-code-board) — Kanban queue for agentic prompts inside Herdr: cards dispatch real agents into panes, worktrees and workspace…
- [tferreira/herdr-pr-ops](https://github.com/tferreira/herdr-pr-ops) — PR//OPS - pull request mission control for Herdr: your PRs and review requests on one board, one-key agents i…
- [chouxcreams/herdr-dashboard](https://github.com/chouxcreams/herdr-dashboard) — PR status dashboard TUI for herdr workspaces — PR state / CI / reviews per pane at a glance
- [EMRahman/herdr-context-monitor](https://github.com/EMRahman/herdr-context-monitor) — A minimal context meter for Herdr: one Python file, no dependencies. Shows each agent's context-window use in…
- [gabrielmarcano/agent-watch](https://github.com/gabrielmarcano/agent-watch) — Approve, answer and prompt your terminal coding agents (Claude Code, OpenCode, Antigravity…) from a Wear OS w…
- [GranamyrBR/LunaCrab](https://github.com/GranamyrBR/LunaCrab) — Reserved for a separate project
- [IniZio/nexus](https://github.com/IniZio/nexus) — Herdr plugin for running worktree in Cloud-Hypervisor sandboxes, with mem/cpu/disk hotplug and auto port-forw…
- [maedana/herdr-agents-preview](https://github.com/maedana/herdr-agents-preview) — Multi-agent terminal preview dashboard for Herdr: all running agents shown at once, with the selected agent t…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-finder"></a>

## Fuzzy Finders & Palettes

> I want to invoke commands or projects even when I only half-remember their names

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-navigator**](https://github.com/thanhdat77/herdr-navigator)<br><sub>thanhdat77</sub> | Jump to any Herdr workspace, agent, project, session, remote, directory, or action from one fuzzy navigator. | `fuzzy-finder` `rust` `terminal` `workspace-manager` | 188 | 2026-09-24 |
| [**herdr-bar**](https://github.com/jeffarese/herdr-bar)<br><sub>jeffarese</sub> | Cmd+K and auto tab title for herdr: fuzzy-jump to any tab, agent, repo or branch. | `command-bar` `fuzzy-finder` `python` `terminal` `tui` | 166 | 🔄 2026-10-28 |
| [**termscope**](https://github.com/iurysza/termscope)<br><sub>iurysza</sub> | Open files and links already visible on your terminal screen in a split. | `python` `television` `terminal` `tmux` | 68 | 🔄 2026-10-25 |
| [**herdr-sessionizer**](https://github.com/andrewchng/herdr-sessionizer)<br><sub>andrewchng</sub> | Fuzzy-open projects and worktrees, then bootstrap workspaces from declarative TOML layouts — tabs, pane splits, commands, and per-repo overrides. | `bun` `fuzzy-finder` `fzf` `git-worktree` `sessionizer` | 52 | 🔄 2026-10-26 |
| [**herdr-plugin-sesh**](https://github.com/fullerzz/herdr-plugin-sesh)<br><sub>fullerzz</sub> | Sesh-style workspace picker TUI for Herdr. Integrates with zoxide to create workspaces from commonly used directories. | `bubbletea` `sesh` `tui` `zoxide` `go` | 51 | 🔄 2026-10-28 |
| [**herdr-command-palette**](https://github.com/JanTvrdik/herdr-command-palette)<br><sub>JanTvrdik</sub> | fzf command palette for herdr — fuzzy-pick and run any plugin action | `shell` | 47 | 2026-06-29 |
| [**herdr-drovr**](https://github.com/AVGVSTVS96/herdr-drovr)<br><sub>AVGVSTVS96</sub> | easily move herdr panes and tabs | `fzf` `terminal` `javascript` | 26 | 2026-10-10 |
| [**herdr-palette**](https://github.com/vjeantet/herdr-palette)<br><sub>vjeantet</sub> | Command palette for herdr, à la Sublime Text / VS Code — built-in operations, plugin actions and your own commands behind one key | `command-palette` `fuzzy-search` `terminal` `tui` `rust` | 19 | 2026-10-05 |
| [**herdr-omni**](https://github.com/mmjang/herdr-omni)<br><sub>mmjang</sub> | One search for Herdr workspaces, actions, and live or saved Codex & Claude sessions. Fuzzy-find by name, search conversation content, and resume where you left… | `claude-code` `codex` `opencode` `rust` | 13 | 2026-10-08 |
| [**herdr-zoxide**](https://github.com/den-tanui/herdr-zoxide)<br><sub>den-tanui</sub> | Herdr plugin to create workspaces, tabs and panes from zoxide directories. | `zoxide` `shell` | 12 | 2026-07-25 |
| [**herdr-palette**](https://github.com/ramarivera/herdr-palette)<br><sub>ramarivera</sub> | A Rust/Ratatui fuzzy command palette for Herdr workspaces. | `command-palette` `ratatui` `rust` `terminal` `tui` | 11 | 2026-09-11 |
| [**herdr-blink**](https://github.com/dartyuhov/herdr-blink)<br><sub>dartyuhov</sub> | Blazing-fast fuzzy agent switcher for herdr: attention first, then most recently used. | `rust` `tui` | 9 | 2026-10-11 |
| [**herdr-quick-actions**](https://github.com/enekos/herdr-quick-actions)<br><sub>enekos</sub> | fzf picker for herdr's native tab/pane/workspace actions, ranked by usage — stop memorizing keybindings | `shell` | 9 | 2026-08-05 |
| [**levi**](https://github.com/rsdlt/levi)<br><sub>rsdlt</sub> | The fastest blade for your git history. Fuzzy search for you, plain text for your agents. | `claude-code` `cli` `coding-agents` `diff` `fzf` | 8 | 🔄 2026-10-22 |
| [**herdr-openr**](https://github.com/wraithyy/herdr-openr)<br><sub>wraithyy</sub> | herdr plugin: fuzzy-open files/URLs your terminal or AI agent just mentioned — Claude panes read the session transcript | `shell` | 8 | 2026-08-14 |
| [**herdr-switchboard**](https://github.com/crafts69guy/herdr-switchboard)<br><sub>crafts69guy</sub> | A herdr plugin: fuzzy-switch across running agents, open workspaces, and ghq repositories in one Rust TUI — and open a repo in a new workspace, tab, split, or… | `developer-tools` `ghq` `ratatui` `rust` `terminal` | 7 | 🔄 2026-10-18 |
| [**herdr-transcripts**](https://github.com/hxreborn/herdr-transcripts)<br><sub>hxreborn</sub> | Search your coding-agent sessions, past and live, by any word you remember, then jump to them or resume them | `claude-code` `codex` `coding-agents` `droid` `fzf` | 7 | 2026-10-08 |
| [**herdr-hunk**](https://github.com/JacquesvanWyk/herdr-hunk)<br><sub>JacquesvanWyk</sub> | Interactive fzf picker for hunk diffs in herdr: commits, ranges, stashes, plus auto-open when an agent finishes | `fzf` `hunk` `shell` | 6 | 2026-07-12 |
| [**bracco**](https://github.com/rawnly/bracco)<br><sub>rawnly</sub> | Fast, Git-aware fuzzy file picker for the terminal. | `cli` `fuzzy` `fuzzy-finder` `ratatui` `rust` | 6 | 🔄 2026-10-28 |
| [**herdr-sessionizer**](https://github.com/salkhalil/herdr-sessionizer)<br><sub>salkhalil</sub> | tmux-sessionizer for herdr: fzf over open workspaces and zoxide directories, create-or-focus with template tabs | `shell` | 6 | 2026-07-27 |
| [**herdr-kiosk**](https://github.com/thomasschafer/herdr-kiosk)<br><sub>thomasschafer</sub> | Fuzzy-find Git repos and branches, and open them as worktrees in Herdr | `rust` | 6 | 🔄 2026-10-26 |
| [**herdr-launcher**](https://github.com/arjenblokzijl/herdr-launcher)<br><sub>arjenblokzijl</sub> | Fuzzy-pick a declarative TOML workflow, fill a form, and launch a coding agent in a new herdr space. | `launcher` `ratatui` `rust` `tui` | 5 | 2026-07-10 |
| [**herdr-palette**](https://github.com/cesarferreira/herdr-palette)<br><sub>cesarferreira</sub> | Popup command palette for Herdr. | `typescript` | 5 | 2026-09-08 |
| [**herdr-pickr**](https://github.com/javoscript/herdr-pickr)<br><sub>javoscript</sub> | YAP! Yet Another Picker for the Herdr multiplexer | `fzf` `lua` | 5 | 2026-09-23 |
| [**herdr-ssh-manager**](https://github.com/jorge07RD/herdr-ssh-manager)<br><sub>jorge07RD</sub> | Save SSH hosts and reconnect from a fuzzy popup inside Herdr — Enter hands the popup straight to ssh. | `rust` `ssh` `terminal` `tui` | 5 | 2026-08-24 |
| [**herdr-pane-navigator**](https://github.com/mr04vv/herdr-pane-navigator)<br><sub>mr04vv</sub> | Navigate Herdr's workspaces, tabs, and panes as one fuzzy tree — led by what each pane is actually doing. | `coding-agents` `fzf` `terminal` `tui` `shell` | 5 | 2026-09-07 |
| [**herdr-keymap**](https://github.com/The-Dave-Stack/herdr-keymap)<br><sub>The-Dave-Stack</sub> | A herdr plugin: shows every keybinding in an overlay palette and runs the ones with a CLI equivalent | `typescript` | 5 | 2026-08-12 |
| [**herdr-configurable-picker**](https://github.com/yoshiori/herdr-configurable-picker)<br><sub>yoshiori</sub> | Tree-based goto picker for herdr with fully configurable keybindings | `rust` | 5 | 2026-07-05 |
| [**herdr-cast**](https://github.com/aliou/herdr-cast)<br><sub>aliou</sub> | Personal Herdr plugin for native macOS agent notifications, fuzzy workspace navigation, zoxide-backed workspace creation, and layout commands. | `developer-tools` `macos` `notifications` `ratatui` `rust` | 4 | 🔄 2026-10-24 |
| [**herdr-workspace-save**](https://github.com/chandrasekharan98/herdr-workspace-save)<br><sub>chandrasekharan98</sub> | Save a Herdr workspace — layout, cwds, agent sessions, running commands — and reopen it later from an fzf picker. | `claude-code` `terminal` `tmux` `python` | 4 | 2026-10-13 |
| [**herdr-grep-nvim**](https://github.com/cinco/herdr-grep-nvim)<br><sub>cinco</sub> | herdr plugin: live-grep with fzf + ripgrep and open the match in nvim, in a split beside your work | `shell` | 3 | 2026-07-17 |
| [**herdr-simple-switcher**](https://github.com/haphamdev/herdr-simple-switcher)<br><sub>haphamdev</sub> | Fuzzy searching for workspaces, tabs and AI agents | `shell` | 3 | 🔄 2026-10-15 |
| [**herdr-command-palette**](https://github.com/hota911/herdr-command-palette)<br><sub>hota911</sub> | fzf command palette for herdr's built-in operations — workspaces, tabs, panes, agents | `command-palette` `fzf` `shell` | 3 | 2026-08-16 |
| [**herdr-spotify**](https://github.com/iikjl/herdr-spotify)<br><sub>iikjl</sub> | Spotify now-playing overlay plugin for herdr — album art, playback controls, and optional search/queue/like via the Spotify Web API | `spotify` `terminal` `go` | 3 | 2026-07-07 |
| [**herdr-workspacer**](https://github.com/mcuste/herdr-workspacer)<br><sub>mcuste</sub> | Find projects with zoxide, then switch or create Herdr workspaces | `rust` `tui` `zoxide` | 3 | 2026-10-01 |
| [**herdr-plugin-picker**](https://github.com/purehate/herdr-plugin-picker)<br><sub>purehate</sub> | Floating popup picker for Herdr — jump to any space, agent, tab or pane, broadcast one command to every marked pane, and SSH from ~/.ssh/config with live reach… | `broadcast` `fuzzy-finder` `golang` `picker` `ssh` | 3 | 2026-09-18 |
| [**herdr-flash-picker**](https://github.com/TinyWhite1997/herdr-flash-picker)<br><sub>TinyWhite1997</sub> | Fast pane picker for Herdr with aligned one- or two-letter jump labels | `rust` `tui` | 3 | 2026-09-07 |
| [**herdr-fzf-terminal-browser**](https://github.com/to4iki/herdr-fzf-terminal-browser)<br><sub>to4iki</sub> | A herdr plugin: press a key, pick a URL printed in the current pane with fzf, and it opens in terminal-browser | `fzf` `rust` `terminal-browser` | 3 | 2026-10-06 |
| [**herdr-agent-recency**](https://github.com/ugurtarlig/herdr-agent-recency)<br><sub>ugurtarlig</sub> | Theme-aware Herdr picker sorted by meaningful Codex and Claude activity | `claude-code` `codex` `fzf` `python` | 3 | 2026-07-17 |
| [**herdr-command-palette**](https://github.com/alon-z/herdr-command-palette)<br><sub>alon-z</sub> | Herdr plugin: fuzzy workspace/directory command palette. | `javascript` | 2 | 2026-09-22 |
| [**herdr-palette**](https://github.com/Binb1/herdr-palette)<br><sub>Binb1</sub> | Command palette for Herdr. Jump to workspaces and agents, run plugin actions, run Herdr commands. | `go` | 2 | 🔄 2026-10-26 |
| [**herdr-sesh-bro**](https://github.com/cyperx84/herdr-sesh-bro)<br><sub>cyperx84</sub> | sesh-style fuzzy session picker for Herdr — workspaces, agents, and zoxide dirs in one fzf popup with live previews | `go` | 2 | 2026-09-19 |
| [**herdr-workspaces-manager**](https://github.com/dardT/herdr-workspaces-manager)<br><sub>dardT</sub> | Discover projects and create distinctly named Herdr workspaces with a fast terminal picker | `rust` | 2 | 🔄 2026-10-19 |
| [**herdr-workspace-launcher**](https://github.com/ImArtisann/herdr-workspace-launcher)<br><sub>ImArtisann</sub> | A macOS Herdr plugin for quickly creating focused workspaces with a searchable, keyboard-driven directory picker. | `typescript` | 2 | 2026-07-16 |
| [**herdr-recent-workspaces**](https://github.com/ismaelosuna7824/herdr-recent-workspaces)<br><sub>ismaelosuna7824</sub> | Open Recent for Herdr — a fuzzy-filterable list of the folders you've opened as workspaces. Pick one to open or re-focus that workspace; browse the filesystem… | `go` | 2 | 2026-07-10 |
| [**herdr-nav**](https://github.com/karanpatel1993/herdr-nav)<br><sub>karanpatel1993</sub> | File navigation, code search and jdb debugging inside herdr — fzf, ripgrep and a Java debugger wired into your terminal workspace | `shell` | 2 | 2026-09-17 |
| [**herdr-ghq-open-agent**](https://github.com/kenchan/herdr-ghq-open-agent)<br><sub>kenchan</sub> | Herdr plugin: incrementally search ghq-managed repositories with fzf and open one in a workspace/tab, starting claude | `fzf` `ghq` `shell` | 2 | 2026-08-03 |
| [**herdr-keybind-search**](https://github.com/malone-c/herdr-keybind-search)<br><sub>malone-c</sub> | Searchable keybind overlay for herdr (fzf). Press a key, fuzzy-search your keybinds. | `shell` | 2 | 2026-07-15 |
| [**herdr-palette**](https://github.com/vika2603/herdr-palette)<br><sub>vika2603</sub> | A command palette for herdr: one popup that searches herdr's commands, every installed plugin's actions, your own commands and everything open in the session,… | `bubbletea` `command-palette` `fzf` `go` `terminal` | 2 | 2026-10-11 |
| [**herdr-bitwarden**](https://github.com/WillowMist/herdr-bitwarden)<br><sub>WillowMist</sub> | Fuzzy-search your Bitwarden vault and paste/copy credentials — a herdr port of tmux-bitwarden | `bitwarden` `fzf` `terminal` `tmux` `shell` | 2 | 2026-08-11 |
| [**herdr-waypoint**](https://github.com/wraithyy/herdr-waypoint)<br><sub>wraithyy</sub> | Save folders with a name, pick one from a fuzzy list, open it as a new herdr workspace. | `shell` | 2 | 2026-08-12 |
| [**herdr-open-local-paths**](https://github.com/yigitkg/herdr-open-local-paths)<br><sub>yigitkg</sub> | Herdr plugin that detects local paths and opens or reveals them through a simple picker on Windows, Linux, and WSL. | `developer-tools` `python` `terminal` `wsl` | 2 | 2026-07-28 |
| [**herdr-sessionizer**](https://github.com/42lizard/herdr-sessionizer)<br><sub>42lizard</sub> | tmux-sessionizer style plugin for herdr | `fzf` `shell` | 1 | 2026-08-28 |
| [**herdr-url-picker**](https://github.com/abrose/herdr-url-picker)<br><sub>abrose</sub> | herdr plugin: pick a URL printed in the current pane with fzf and open it in the default browser | `shell` | 1 | 2026-07-22 |
| [**🆕 herdr-jump**](https://github.com/agustinvalencia/herdr-jump)<br><sub>agustinvalencia</sub> | Separate overlay pickers for herdr spaces and agents — jump to any workspace or agent, with live status colours | `go` | 1 | 2026-07-24 |
| [**herdr-url-picker**](https://github.com/chouxcreams/herdr-url-picker)<br><sub>chouxcreams</sub> | Herdr plugin: pick a URL from the focused pane and open it in your browser | `shell` | 1 | 2026-07-22 |
| [**🆕 herdr-spotify**](https://github.com/DeepRuparel/herdr-spotify)<br><sub>DeepRuparel</sub> | Spotify for Herdr — Go, zero-setup local controls + gated search/queue/save via PKCE | `spotify` `go` | 1 | 2026-08-28 |
| [**🆕 herdr-cast**](https://github.com/DevooKim/herdr-cast)<br><sub>DevooKim</sub> | Spotlight/Raycast-style command palette plugin for Herdr | `command-palette` `go` | 1 | 2026-10-12 |
| [**🆕 herdr-pane-mover**](https://github.com/dimitri4d/herdr-pane-mover)<br><sub>dimitri4d</sub> | Move running Herdr panes between tabs and workspaces with a keyboard and mouse friendly destination picker. | `go` | 1 | 2026-09-13 |
| [**🆕 herdr-agents**](https://github.com/dleen/herdr-agents)<br><sub>dleen</sub> | An fzf agent picker for herdr: every agent pane, worst-first, with a session preview and one-key launching. | `coding-agents` `fzf` `python` `terminal` | 1 | 2026-08-20 |
| [**🆕 atd-herdr-command-palette**](https://github.com/doanhthong/atd-herdr-command-palette)<br><sub>doanhthong</sub> | Every Herdr action one keystroke away. Jump between coding agents, spin up agent tabs, and run project commands from a single palette. | `javascript` | 1 | 2026-10-08 |
| [**herdr-hosts**](https://github.com/ecylmz/herdr-hosts)<br><sub>ecylmz</sub> | Hierarchical SSH host picker for Herdr, with folders and notes straight from ~/.ssh/config | `ratatui` `rust` `ssh` `terminal` `tui` | 1 | 2026-09-18 |
| [**🆕 herdr-sesh**](https://github.com/fedeya/herdr-sesh)<br><sub>fedeya</sub> | sesh-style fzf picker for herdr: jump between workspaces and agents, or open sesh configs, zoxide and fd directories, with live previews and a last-workspace t… | `fzf` `sesh` `zoxide` `shell` | 1 | 2026-10-01 |
| [**🆕 herdr-new-workspace**](https://github.com/Hon-Lu/herdr-new-workspace)<br><sub>Hon-Lu</sub> | Herdr plugin for opening a new workspace in any folder: type a path with fuzzy completion, or search your projects by name. | `terminal` `tmux-alternative` `javascript` | 1 | 2026-10-07 |
| [**🆕 herdr-palette**](https://github.com/iancharters/herdr-palette)<br><sub>iancharters</sub> | Fuzzy command palette for Herdr — core commands plus auto-discovered plugin actions, run where you can see them. Fast, keyboard-first, terminal-native. | `go` | 1 | 2026-09-25 |
| [**🆕 herdr-turbo-palette**](https://github.com/jackfrancisdalton/herdr-turbo-palette)<br><sub>jackfrancisdalton</sub> | Fuzzy-find any Herdr space, tab, agent or pane and jump straight to it. | `python` | 1 | 2026-08-22 |
| [**🆕 herdr-keys**](https://github.com/JacquesvanWyk/herdr-keys)<br><sub>JacquesvanWyk</sub> | Fuzzy-searchable keybinding cheatsheet for herdr (packs, discovery, personal overrides) | `shell` | 1 | 2026-07-12 |
| [**🆕 herdr-open-editor**](https://github.com/jimididit/herdr-open-editor)<br><sub>jimididit</sub> | Fuzzy-pick a file with fzf and open it in your configured editor. | `herd` `text-editor` `tui` `shell` | 1 | 2026-09-03 |
| [**herdr-fzf-url**](https://github.com/kaar/herdr-fzf-url)<br><sub>kaar</sub> | Fuzzy-find and open URLs from your herdr pane scrollback — a port of tmux-fzf-url | `shell` | 1 | 2026-07-29 |
| [**🆕 herdr-hint**](https://github.com/maedana/herdr-hint)<br><sub>maedana</sub> | Vimium-style hint labels for Herdr — press a key to see labels on tabs and agents, then press a label to jump. | `rust` | 1 | 2026-08-11 |
| [**herdr-shortcut**](https://github.com/matheus3301/herdr-shortcut)<br><sub>matheus3301</sub> | Shortcut task picker and coding-agent launcher for Herdr | `bubbletea` `claude-code` `codex` `coding-agents` `developer-tools` | 1 | 2026-07-24 |
| [**🆕 herdr-atuin-plugin**](https://github.com/smanickam01/herdr-atuin-plugin)<br><sub>smanickam01</sub> | Atuin shell history search in a herdr popup — press prefix+a, Enter to run or Tab to edit. Binds itself on install. | `atuin` `macos` `shell-history` `terminal` `zsh` | 1 | 2026-08-17 |
| [**herdr-pane-picker**](https://github.com/ugurtarlig/herdr-pane-picker)<br><sub>ugurtarlig</sub> | Pick a Herdr pane by typing its on-pane character hint | `terminal` `wezterm` `python` | 1 | 2026-07-17 |
| [**🆕 herdr-fzf-url**](https://github.com/x0d7x/herdr-fzf-url)<br><sub>x0d7x</sub> | Scan herdr terminal panes for URLs and interactively pick one with fzf | `fzf` `go` `url` | 1 | 2026-06-26 |
| [**herdr-telescope**](https://github.com/zackshen/herdr-telescope)<br><sub>zackshen</sub> | fzf command telescope for herdr: native actions, plugin actions, file finder (@), and live ripgrep search (/) | `fzf` `rust` | 1 | 2026-08-20 |

<details><summary>Also relevant to this purpose</summary>

- [ThorstenRhau/token](https://github.com/ThorstenRhau/token) — Neovim colorscheme with terminal-wide contrib themes
- [beyondlex/herdr-recent-navigator](https://github.com/beyondlex/herdr-recent-navigator) — MRU switching across recent workspaces, tabs, panes, and agents — like JetBrains's recent file — plus fuzzy s…
- [JacquesvanWyk/herdr-linear](https://github.com/JacquesvanWyk/herdr-linear) — fzf-driven Linear panel in a herdr split pane or tab: search issues, drill into projects, create issues, chan…
- [hamzahraihan/herdr-better-workspace](https://github.com/hamzahraihan/herdr-better-workspace) — An interactive "Open Workspace" picker plugin for herdr, the terminal workspace manager for AI coding agents.
- [42lizard/herdr-dwm-layout](https://github.com/42lizard/herdr-dwm-layout) — DWM-style master/stack layouts for Herdr
- [adriankarlen/yeet](https://github.com/adriankarlen/yeet) — a minimal sesh style picker inside herdr

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-automation"></a>

## Automation, Hooks & Schedules

> I want a fixed set of steps to run automatically on worktree creation or at a chosen time

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-browser**](https://github.com/ogulcancelik/herdr-browser)<br><sub>ogulcancelik</sub> | Render a real Chromium view inside a Herdr pane and drive it over CDP. | `browser` `browser-automation` `cdp` `chromium` `kitty-graphics` | 360 | 2026-08-22 |
| [**herdr-auto-title**](https://github.com/kryptamine/herdr-auto-title)<br><sub>kryptamine</sub> | Automatically name Herdr tabs and panes from your current work, Git branch, terminal activity, and Claude Code sessions. | `claude-code` `coding-agents` `developer-tools` `terminal` `terminal-multiplexer` | 277 | 🔄 2026-10-28 |
| [**herdr-automatic-rename**](https://github.com/qu8n/herdr-automatic-rename)<br><sub>qu8n</sub> | Automatically name herdr tabs after the foreground process (like tmux) or agent session context | `shell` | 226 | 🔄 2026-10-22 |
| [**herdr-auto-title**](https://github.com/sh1ma/herdr-auto-title)<br><sub>sh1ma</sub> | Automatically generate titles for herdr tabs from Claude Code and Codex conversations. | `claude-code` `codex` `python` | 55 | 2026-09-11 |
| [**herdr-workflows**](https://github.com/aorumbayev/herdr-workflows)<br><sub>aorumbayev</sub> | Declarative automation for repetitive steps in herdr | `agentic-ai` `agentic-workflow` `agents` `ai` `claude` | 37 | 🔄 2026-10-28 |
| [**zed-herdr**](https://github.com/ImArtisann/zed-herdr)<br><sub>ImArtisann</sub> | Automatically keeps your active HerdR workspace in sync with your existing Zed session. | `typescript` | 35 | 2026-10-06 |
| [**herdr-worktree-setup**](https://github.com/tdi/herdr-worktree-setup)<br><sub>tdi</sub> | herdr plugin: run per-project setup steps when a worktree is created (copy .env from main, mise trust, direnv allow, install deps) | `javascript` | 30 | 2026-09-11 |
| [**herdr-auto-pilot**](https://github.com/0xGosu/herdr-auto-pilot)<br><sub>0xGosu</sub> | A Herdr plugin that will automatically prompt the running AI Coding CLI on-behalf of you via Herdr API. The plugin has training mode which learn from your acti… | `go` | 28 | 🔄 2026-10-28 |
| [**herdr-automations**](https://github.com/DnzzL/herdr-automations)<br><sub>DnzzL</sub> | Scheduled tasks for your coding agents, in the terminal. A prompt, a cron line, and a fresh git worktree per run — on Herdr. One YAML file, no store, prebuilt… | `ai-agents` `automation` `claude-code` `coding-agents` `cron` | 20 | 🔄 2026-10-20 |
| [**bermuda**](https://github.com/bon5co/bermuda)<br><sub>bon5co</sub> | Orchestration under Claude Code on herdr: flows an agent cannot skip, jobs on a clock, threads with claims, and a forum agents search later | `agent-orchestration` `agents` `ai-agents` `automation` `claude-code` | 14 | 🔄 2026-10-21 |
| [**herdr-routines**](https://github.com/mrcndz/herdr-routines)<br><sub>mrcndz</sub> | Herdr plugin that runs scheduled routines: cron or interval schedules that open a tab in a workspace and run a command or launch an agent. | `python` | 12 | 2026-07-18 |
| [**herdr-updater**](https://github.com/diegopzz/herdr-updater)<br><sub>diegopzz</sub> | Keep Herdr and its plugins current across a whole fleet, safely | `rust` `updater` | 10 | 2026-09-17 |
| [**herdr-agent-config-manager**](https://github.com/Phoobobo/herdr-agent-config-manager)<br><sub>Phoobobo</sub> | Hybrid CLI + Herdr plugin for detecting and centrally managing agent skills, MCP, plugins, and hooks | `python` | 10 | 2026-09-06 |
| [**herdr-tab-title**](https://github.com/aarsh21/herdr-tab-title)<br><sub>aarsh21</sub> | Automatic tmux-like tab titles for Herdr | `rust` `terminal` `tmux` | 8 | 2026-07-08 |
| [**herdr-shepherd**](https://github.com/mikedclarke/herdr-shepherd)<br><sub>mikedclarke</sub> | Scheduled agent sessions for herdr: heartbeats, cron routines, and scripts, launched as visible herdr workspaces. | `coding-agents` `cron` `go` `scheduler` `tui` | 7 | 2026-10-09 |
| [**herdr-fwd**](https://github.com/go-min/herdr-fwd)<br><sub>go-min</sub> | Automatic loopback port forwarding for remote Herdr sessions. | `port-forwarding` `ssh` `terminal` `rust` | 6 | 2026-10-07 |
| [**herdr-sched**](https://github.com/husniadil/herdr-sched)<br><sub>husniadil</sub> | Schedules and triggers for coding agents on Herdr - cron jobs and webhook/file-watcher triggers firing actions into the sibling plugins, each act signed by its… | `ai-agents` `cron` `mcp-server` `scheduler` `webhooks` | 5 | 2026-08-30 |
| [**herdr-pane-balancer**](https://github.com/jeph/herdr-pane-balancer)<br><sub>jeph</sub> | Automatically balance, equalize, and tile Herdr terminal panes on create, close, and exit. | `python` | 5 | 2026-08-02 |
| [**🆕 herdr-island**](https://github.com/speardragon/herdr-island)<br><sub>speardragon</sub> | Your herdr agents live in the MacBook notch: approve, answer and watch them from a Dynamic Island-style panel | `ai-agents` `claude-code` `macos` `notch` `swiftui` | 5 | 🔄 2026-10-28 |
| [**herdr-tab-autorun**](https://github.com/hanbong5938/herdr-tab-autorun)<br><sub>hanbong5938</sub> | Herdr plugin that runs a shell command or starts a coding agent in every new tab, driven by TOML rules | `ai-agents` `automation` `nodejs` `terminal` `javascript` | 4 | 2026-10-11 |
| [**herdr-review-loop**](https://github.com/mikhail-angelov/herdr-review-loop)<br><sub>mikhail-angelov</sub> | Automated cross-review between agents in a herdr workspace — one writes, the other reviews, repeat. | `terminal` `go` | 3 | 2026-10-12 |
| [**herdr-plugin**](https://github.com/ppggff/herdr-plugin)<br><sub>ppggff</sub> | Automatically remember and restore the right macOS input method (ime) for each Herdr pane. | `ime` `input-method` `macos` `python` | 3 | 2026-07-27 |
| [**herdr-autocontinue**](https://github.com/rcosteira79/herdr-autocontinue)<br><sub>rcosteira79</sub> | Watches agents for usage-limit walls, badges the countdown to the reset ($wall), and re-prompts the agents you armed once the window reopens. | `python` | 3 | 2026-09-23 |
| [**herdr-comment-on-copy**](https://github.com/rheech22/herdr-comment-on-copy)<br><sub>rheech22</sub> | Drag to select terminal text and open a comment popup automatically. Send feedback with context to AI agents in Herdr. | `typescript` | 3 | 2026-10-05 |
| [**herdr-labels**](https://github.com/Angel-O/herdr-labels)<br><sub>Angel-O</sub> | Herdr plugin that automatically names and numbers tabs while preserving manual labels | `rust` | 2 | 🔄 2026-10-25 |
| [**herdr-auto-update**](https://github.com/dio16/herdr-auto-update)<br><sub>dio16</sub> | herdr plugin: check installed plugins for newer upstream commits and reinstall them at startup | `rust` | 2 | 2026-08-16 |
| [**herdr-mcp**](https://github.com/eugeneb50/herdr-mcp)<br><sub>eugeneb50</sub> | herdr plugin and MCP server: drive herdr panes and agents from AI clients, with recipes, triggers, schedules, a dashboard and a web playground | `mcp` `rust` | 2 | 🔄 2026-10-28 |
| [**herdr-routines**](https://github.com/guidodinello/herdr-routines)<br><sub>guidodinello</sub> | _(no description)_ | `python` | 2 | 🔄 2026-10-28 |
| [**herdr-js-worktree-bootstrap**](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap)<br><sub>LeonardoTrapani</sub> | Automatically bootstrap Herdr worktrees for JavaScript and TypeScript with lockfile-aware installs and safe env restoration | `automation` `bun` `developer-tools` `git-worktree` `javascript` | 2 | 2026-07-15 |
| [**herdr-callsigns**](https://github.com/reobin/herdr-callsigns)<br><sub>reobin</sub> | auto-name every herdr pane with a short memorable callsign, so you and your agent can use pane names instead of IDs. | `shell` | 2 | 🔄 2026-10-26 |
| [**🆕 herdr-kata**](https://github.com/salmonumbrella/herdr-kata)<br><sub>salmonumbrella</sub> | Runs Kata cron jobs and workflows as Herdr agents | `kata` `go` | 2 | 🔄 2026-10-25 |
| [**herdr-hermes-manager**](https://github.com/skaftanis/herdr-hermes-manager)<br><sub>skaftanis</sub> | Hermes Agent workspaces, cron controls, recent conversations and continuous Bot chats for Herdr | `hermes-agent` `macos` `terminal` `tui` `python` | 2 | 🔄 2026-10-15 |
| [**herdr-starkeep**](https://github.com/yuya-take/herdr-starkeep)<br><sub>yuya-take</sub> | Watch your herdr agents work as knights on an orbital training ship — subagents come in as apprentices. | `rust` | 2 | 2026-10-06 |
| [**🆕 herdr-claude-autoupdate**](https://github.com/0xMMA/herdr-claude-autoupdate)<br><sub>0xMMA</sub> | herdr plugin: restarts idle Claude Code panes onto the newly installed version, in place, same session and flags, drafts kept. | `claude-code` `typescript` | 1 | 2026-10-11 |
| [**🆕 herdr-stay-awake**](https://github.com/assawalhy/herdr-stay-awake)<br><sub>assawalhy</sub> | Keeps the machine from sleeping while any herdr agent pane is working (Linux, macOS, Windows, and WSL) | `agent-orchestration` `agents` `harness` `linux` `macos` | 1 | 2026-10-07 |
| [**🆕 herdr-auto-pull-main**](https://github.com/bring-shrubbery/herdr-auto-pull-main)<br><sub>bring-shrubbery</sub> | _(no description)_ | `shell` | 1 | 2026-10-12 |
| [**herdr-triggers**](https://github.com/cantona/herdr-triggers)<br><sub>cantona</sub> | Resident regex triggers over pane output: automated logins and other regex-driven terminal triggers. | `rust` `terminal` `terminal-based` `terminal-multiplexer` `trigger` | 1 | 2026-09-18 |
| [**🆕 herdr-continue**](https://github.com/codergeek121/herdr-continue)<br><sub>codergeek121</sub> | Tell your agents to start working automatically | `shell` | 1 | 2026-09-30 |
| [**🆕 herdr-auto-tab-name**](https://github.com/dev-shimada/herdr-auto-tab-name)<br><sub>dev-shimada</sub> | herdr plugin: automatically name tabs after their current directory | `javascript` | 1 | 🔄 2026-10-17 |
| [**🆕 ws.numbered.herdr**](https://github.com/dhananjaylatkar/ws.numbered.herdr)<br><sub>dhananjaylatkar</sub> | Automatically Number The Workspaces in Herdr | `python` | 1 | 2026-10-09 |
| [**say-hook**](https://github.com/HikaruEgashira/say-hook)<br><sub>HikaruEgashira</sub> | A macOS CLI that reads Claude Code hook events aloud using ElevenLabs text-to-speech. | `typescript` | 1 | 🔄 2026-10-19 |
| [**herdr-worktree-cleanup**](https://github.com/poislagarde/herdr-worktree-cleanup)<br><sub>poislagarde</sub> | Automatically clean up safe GitHub PR worktrees when their Herdr space closes. Python, no dependencies, MIT. | `git-worktree` `python` | 1 | 2026-09-11 |
| [**🆕 herdr-automations**](https://github.com/ram4-dev/herdr-automations)<br><sub>ram4-dev</sub> | Declarative cron, interval, and event automations for Herdr | `automation` `bun` `typescript` | 1 | 2026-08-13 |
| [**herdr-nixos-vm**](https://github.com/Slimydog21/herdr-nixos-vm)<br><sub>Slimydog21</sub> | The NixOS VM pane for herdr — boot, stop, watch, and ssh into your Hashimoto-style dev VM. Requires the nixos-vm kit. | `shell` | 1 | 2026-08-18 |
| [**🆕 herdr-claude-memories**](https://github.com/StGerman/herdr-claude-memories)<br><sub>StGerman</sub> | Surface and curate Claude Code auto-memory from inside herdr | `claude-code` `terminal` `rust` | 1 | 2026-09-11 |
| [**herdr-jump-number**](https://github.com/voice0726/herdr-jump-number)<br><sub>voice0726</sub> | Herdr plugin that displays jump-key numbers on workspaces and tabs without breaking Herdr's automatic workspace labels | `typescript` | 1 | 2026-09-19 |
| [**🆕 herdr-space-groups**](https://github.com/yojahny55/herdr-space-groups)<br><sub>yojahny55</sub> | Herdr plugin: group Spaces into named, colored groups — picker popup (mouse + keyboard), sidebar group headers, automatic ordering | `javascript` | 1 | 2026-08-29 |
| [**🆕 herdr-pane-restart**](https://github.com/zap0xfce2/herdr-pane-restart)<br><sub>zap0xfce2</sub> | Run a configured command in named panes on server startup | `python` | 1 | 🔄 2026-10-21 |

<details><summary>Also relevant to this purpose</summary>

- [freethinkel/herdr-plugin-git-worktree-hooks](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks) — Run shell commands when a git worktree is created/removed — one YAML config for all projects, living outside…
- [timofey-TK/herdr-worktree-hooks](https://github.com/timofey-TK/herdr-worktree-hooks) — herdr plugin: run custom setup/teardown commands when a git worktree is created, opened, or removed
- [miko-misa/herdr-portfwd](https://github.com/miko-misa/herdr-portfwd) — Automatic SSH port forwarding for coding agents on remote machines: Ctrl+click the localhost URL your agent p…
- [itisbryan/herdr-gh-checks](https://github.com/itisbryan/herdr-gh-checks) — Herdr plugin: watch & review the current PR's CI in a pane; CI/merge status on sidebar rows. Go + Bubble Tea.
- [zhuravel/magnum](https://github.com/zhuravel/magnum) — Your AI coding agents as a pull-request review team: Claude Code, Codex and others review each push in herdr…

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-session"></a>

## Session State & Restore

> I want to close my work and later resume from exactly the same state

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-resurrect**](https://github.com/ntindle/herdr-resurrect)<br><sub>ntindle</sub> | tmux-resurrect for herdr — snapshot workspaces, tabs, panes, cwd, running programs and agents, and restore them after a crash or reboot. | `crash-recovery` `session-manager` `terminal-multiplexer` `tmux-resurrect` `javascript` | 41 | 2026-10-05 |
| [**session-digger**](https://github.com/taxueseek/session-digger)<br><sub>taxueseek</sub> | 跨环境会话历史挖掘与知识管理。分析记录。支持 Claude/Grok/Kimi Code/Codex/WorkBuddy/Trae CN 等主流环境 | `claude-code` `conversation-analysis` `jsonl` `knowledge-management` `log-analysis` | 33 | 2026-09-23 |
| [**herdr-notes**](https://github.com/alexarthurs/herdr-notes)<br><sub>alexarthurs</sub> | Persistent markdown notes pane for herdr - one note per workspace, rendered preview + edit mode, autosaves and survives restarts | `markdown` `notes` `ratatui` `rust` `terminal` | 23 | 🔄 2026-10-17 |
| [**herdr-session-parker**](https://github.com/iviaxpow3r/herdr-session-parker)<br><sub>iviaxpow3r</sub> | Herdr plugin to park panes/tabs and resume supported agent sessions later | `agent-tools` `python` | 13 | 2026-07-03 |
| [**herdr-agent-inbox**](https://github.com/douglascorrea/herdr-agent-inbox)<br><sub>douglascorrea</sub> | An inbox for your coding agents in herdr — session titles, settle/mark-unread triage, runtimes, workspace rollups, and resumable chat history | `ai-agents` `terminal` `python` | 11 | 2026-07-28 |
| [**herdr-assist**](https://github.com/walcew/herdr-assist)<br><sub>walcew</sub> | Physical desk panel for Herdr, the terminal multiplexer for AI coding agents — shows session state in color and rings a bell when an agent stops to ask for a d… | `ai-agents` `claude-code` `coding-agents` `embedded` `esp-idf` | 10 | 🔄 2026-10-23 |
| [**herdr-oh-my-agent**](https://github.com/GavinTomlins/herdr-oh-my-agent)<br><sub>GavinTomlins</sub> | Mirror every oh-my-openagent subagent delegation into its own Herdr pane or tab — live, with full session state and scrollback | `typescript` | 7 | 2026-07-31 |
| [**sheep**](https://github.com/gokay-ai/sheep)<br><sub>gokay-ai</sub> | Undo for AI coding agents. Every agent turn becomes a restorable checkpoint. | `ai-agents` `git` `llm` `rust` `tui` | 6 | 2026-08-28 |
| [**herdr-undo-close**](https://github.com/pedroloch/herdr-undo-close)<br><sub>pedroloch</sub> | Reopen a closed tab in herdr, like Cmd+Shift+T in a browser - restores the label, the split tree with its ratios, each pane's cwd, and the tab's position. | `python` | 4 | 2026-07-30 |
| [**herdr-hibernate**](https://github.com/bengemine/herdr-hibernate)<br><sub>bengemine</sub> | Hibernate idle coding-agent panes in Herdr (Claude Code, Codex, Grok) — free the RAM, press Enter to resume the exact session. | `claude-code` `python` | 3 | 🔄 2026-10-16 |
| [**herdr-stash**](https://github.com/victor-software-house/herdr-stash)<br><sub>victor-software-house</sub> | Stash a Herdr workspace: stop its agents, keep its shape and their conversations, and restore it later from a clickable two-column popup. | `rust` `terminal` `tui` | 3 | 2026-07-29 |
| [**herdr-pane-id-labeler**](https://github.com/4Born/herdr-pane-id-labeler)<br><sub>4Born</sub> | Herdr plugin that keeps pane labels synchronized with public pane IDs such as w1:p2. | `developer-tools` `terminal` `javascript` | 2 | 2026-07-26 |
| [**herdr-agent-auto-naming**](https://github.com/azyu/herdr-agent-auto-naming)<br><sub>azyu</sub> | Herdr plugin that gives every detected agent a readable two-word name, persisted as the pane label so it survives restarts. | `coding-agents` `developer-tools` `terminal` `python` | 2 | 🔄 2026-10-16 |
| [**herdr-revive**](https://github.com/cantona/herdr-revive)<br><sub>cantona</sub> | Restore Herdr commands, layouts and exact agent sessions with preview, named workspaces and explicit recovery. | `rust` `session-handoff` `session-history` `session-management` `session-manager` | 2 | 🔄 2026-10-15 |
| [**herdr-synchronize-panes**](https://github.com/furuhashin/herdr-synchronize-panes)<br><sub>furuhashin</sub> | Herdr plugin: broadcast one command to every pane in the current tab (tmux synchronize-panes style) | `javascript` | 2 | 2026-07-14 |
| [**herdr_sync**](https://github.com/kamaaina/herdr_sync)<br><sub>kamaaina</sub> | synchronize panes in herdr | `zig` | 2 | 2026-07-01 |
| [**herdr-e2b**](https://github.com/tomasvarga/herdr-e2b)<br><sub>tomasvarga</sub> | Mirror a git worktree into a fresh E2B cloud sandbox on demand — a snapshot upload (uncommitted changes and all), no push or clone. A herdr plugin. | `cli` `cloud-dev` `e2b` `git-worktree` `sandbox` | 2 | 2026-07-18 |
| [**herdr-thread-to-tab**](https://github.com/toyamarinyon/herdr-thread-to-tab)<br><sub>toyamarinyon</sub> | Keep single-pane Herdr tab labels in sync with Claude Code and Codex thread titles. | `rust` | 2 | 2026-08-06 |
| [**🆕 herdr-todos-windows**](https://github.com/aclima01/herdr-todos-windows)<br><sub>aclima01</sub> | Live panel mirroring a herdr agent's task list (TaskCreate/TaskUpdate) so you can follow its plan | `powershell` | 1 | 2026-07-22 |
| [**🆕 herdr-restart-agents**](https://github.com/aliaksandr-haurylau-godel/herdr-restart-agents)<br><sub>aliaksandr-haurylau-godel</sub> | Herdr plugin: restart coding agents in their panes and resume the same session | `python` | 1 | 2026-10-05 |
| [**🆕 herdr-unread**](https://github.com/arthurnw/herdr-unread)<br><sub>arthurnw</sub> | Mark Herdr agent sessions unread until revisited or resumed | `python` | 1 | 2026-09-14 |
| [**herdr-agent-hibernate**](https://github.com/dalogax/herdr-agent-hibernate)<br><sub>dalogax</sub> | Hibernate idle AI agent panes in Herdr: frees their memory, resumes the same session when you come back. Supports OpenCode, Claude Code and Codex. | `ai-agents` `claude-code` `codex` `opencode` `terminal` | 1 | 2026-10-01 |
| [**🆕 mo-herdr**](https://github.com/momentohq/mo-herdr)<br><sub>momentohq</sub> | Run mo inside herdr panes: session restore after a herdr restart, a launch action, and SIGKILL cleanup | `python` | 1 | 2026-09-02 |
| [**🆕 herdr-pane-reopen**](https://github.com/rchougule/herdr-pane-reopen)<br><sub>rchougule</sub> | herdr plugin: undo close — reopen the last closed pane, tab or workspace in place and resume its agent | `rust` | 1 | 2026-09-17 |
| [**attic**](https://github.com/TheThoughtagen/attic)<br><sub>TheThoughtagen</sub> | Auto-closes idle AI coding sessions, but archives each one first so you can restore it. | `claude-code` `developer-tools` `python` `session-management` `tui` | 1 | 2026-08-14 |
| [**herdr-agent-pins**](https://github.com/ZingerLittleBee/herdr-agent-pins)<br><sub>ZingerLittleBee</sub> | Persistently pin Herdr agent sessions to the top of the Agents sidebar. | `terminal` `javascript` | 1 | 2026-08-24 |

<details><summary>Also relevant to this purpose</summary>

- [nicosuave/memex](https://github.com/nicosuave/memex) — Search Claude Code, Codex, Pi, OpenCode, Github Copilot & Cursor transcripts. Resume sessions. Track tokens.
- [mmjang/herdr-omni](https://github.com/mmjang/herdr-omni) — One search for Herdr workspaces, actions, and live or saved Codex & Claude sessions. Fuzzy-find by name, sear…
- [afogel/shepherdr](https://github.com/afogel/shepherdr) — Shepherd delegated coding agents into visible, auditable herdr panes you can watch, resume, and take over — a…
- [hxreborn/herdr-transcripts](https://github.com/hxreborn/herdr-transcripts) — Search your coding-agent sessions, past and live, by any word you remember, then jump to them or resume them
- [AkashJana18/herdr-scratch](https://github.com/AkashJana18/herdr-scratch) — Persistent scratchpads for Herdr, paving the way for floating utility panes.
- [KokiKono/herdr-kanban](https://github.com/KokiKono/herdr-kanban) — Terminal Kanban board that links tasks to herdr tabs, persisted in SQLite
- [blaxel-ai/herdr-blaxel-sandbox-plugin](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin) — Run coding agents in persistent Blaxel sandboxes from Herdr.
- [ppggff/herdr-plugin](https://github.com/ppggff/herdr-plugin) — Automatically remember and restore the right macOS input method (ime) for each Herdr pane.
- [voodootikigod/adlc-herdr](https://github.com/voodootikigod/adlc-herdr) — ADLC herdr plugin — per-pane phase/ticket/gate status, backlog board, gate actions, and adlc-fleet run observ…
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — Automatically bootstrap Herdr worktrees for JavaScript and TypeScript with lockfile-aware installs and safe e…
- [mohaphez/herdr-flow](https://github.com/mohaphez/herdr-flow) — Persistent multi-agent task coordination for Herdr with guarded review and worktree cleanup
- [jiangkoumo/herdr-plugin-layerfs](https://github.com/jiangkoumo/herdr-plugin-layerfs) — Copy-on-write LayerFS branches as Herdr workspaces, grouped under the repo like worktrees and restored after…
- [nicholasjstock/paneyard](https://github.com/nicholasjstock/paneyard) — Queue coding tasks and run them in parallel as interactive agent sessions you can watch, steer, and resume.
- [shadowfax92/herdr-scratch](https://github.com/shadowfax92/herdr-scratch) — Persistent per-pane Herdr scratch popups backed by private tmux sessions.

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-naming"></a>

## Titles, Naming & Looks

> I want tab names and terminal titles to be automatically clear, or want to change how things look

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-tab-smart-rename**](https://github.com/iurysza/herdr-tab-smart-rename)<br><sub>iurysza</sub> | Generates context-aware workspace and tab names for Herdr. | `ai` `bun` `terminal` `typescript` | 77 | 🔄 2026-10-26 |
| [**herdr-flock**](https://github.com/ragamo/herdr-flock)<br><sub>ragamo</sub> | A herdr plugin that visualizes your AI coding agents as pixel-art sheep living on a top-down farm. | `cli` `ratatui` `rust` `tui` | 44 | 2026-08-31 |
| [**herdr-window-title-sync**](https://github.com/rjyo/herdr-window-title-sync)<br><sub>rjyo</sub> | Syncs terminal titles from workspaces, tabs, and agent sessions (use w/ Moshi) | `moshi` `terminal-title` `javascript` | 38 | 2026-06-26 |
| [**herdr-pet**](https://github.com/nikok6/herdr-pet)<br><sub>nikok6</sub> | Tiny desk pet on your herdr panes: types, waits, and celebrates with your agent. Works with any Codex pet. | `rust` | 18 | 2026-08-26 |
| [**herdr-theme-picker**](https://github.com/qintmb/herdr-theme-picker)<br><sub>qintmb</sub> | Theme picker for herdr UI based terminalcolors scheme and your customization. | `go` | 17 | 🔄 2026-10-18 |
| [**herdr-icon-agent-ui**](https://github.com/qintmb/herdr-icon-agent-ui)<br><sub>qintmb</sub> | Renders Agent icon, vertically-aligned monochrome icons in the Herdr sidebar. rendered via a custom font with non-uniform glyph scaling that matches terminal c… | `python` | 16 | 🔄 2026-10-14 |
| [**herdr-canvas**](https://github.com/aorumbayev/herdr-canvas)<br><sub>aorumbayev</sub> | Mouse-driven ASCII diagram canvas for herdr agents - draw in the TUI, share structured JSON, and let AI edit it. | `agentic-ai` `agents` `ai-agents` `ascii-art` `bubbletea` | 8 | 2026-08-31 |
| [**herdr-claude-session-title**](https://github.com/bcihanc/herdr-claude-session-title)<br><sub>bcihanc</sub> | Herdr plugin: mirrors the Claude Code session title (/rename or auto summary) into the herdr pane metadata title | `shell` | 8 | 2026-07-11 |
| [**herdr-pixel-office**](https://github.com/devangchhajed/herdr-pixel-office)<br><sub>devangchhajed</sub> | Watch your AI coding agents work as pixel-art characters in a tiny top-down office — a herdr plugin | `typescript` | 7 | 2026-09-21 |
| [**herdr-pet**](https://github.com/allmight-ai/herdr-pet)<br><sub>allmight-ai</sub> | Companion V-Pet for Herdr — mirrors your coding agent | `companion` `rust` `v-pet` | 6 | 2026-08-20 |
| [**herdr-ghostty-tab-title**](https://github.com/wjarka/herdr-ghostty-tab-title)<br><sub>wjarka</sub> | herdr plugin: color-coded agent status counts (blocked / done / working / idle) in the Ghostty tab title | `ai-agents` `ghostty` `terminal` `python` | 6 | 2026-08-04 |
| [**herdr-town**](https://github.com/Efeguclu1/herdr-town)<br><sub>Efeguclu1</sub> | Watch your Herdr coding agents as an 8-bit town. Read and answer them without leaving it. | `ai-agents` `pixel-art` `terminal` `tui` `javascript` | 5 | 2026-10-03 |
| [**herdr-auto-namer**](https://github.com/kakigakki/herdr-auto-namer)<br><sub>kakigakki</sub> | ChatGPT-style auto-naming for herdr: agents get their Claude session title, workspaces get their working directory | `claude-code` `python` | 5 | 🔄 2026-10-21 |
| [**herdr-agent-titler**](https://github.com/killerz3/herdr-agent-titler)<br><sub>killerz3</sub> | Auto-titles Herdr tabs using local agy, claude, codex, or opencode harnesses without external API keys | `antigravity` `claude-code` `python` | 5 | 2026-09-03 |
| [**herdr-colors**](https://github.com/ariel-ps/herdr-colors)<br><sub>ariel-ps</sub> | Give each Herdr pane a distinct color. | `rust` | 4 | 2026-10-10 |
| [**tamagoxtix**](https://github.com/fabandrade88/tamagoxtix)<br><sub>fabandrade88</sub> | TamaGoxtix: a tiny pixel monster for Claude Code and herdr — animated spinner, usage charts, palettes and a powerline status line. | `claude-code` `claude-code-plugin` `omarchy` `pixel-art` `javascript` | 4 | 🔄 2026-10-20 |
| [**herdr-in-your-face**](https://github.com/JYasha11/herdr-in-your-face)<br><sub>JYasha11</sub> | A giant ASCII face screams at you when you leave an AI agent blocked. Escalates the longer you ignore it. | `javascript` | 4 | 2026-07-10 |
| [**herdr-tab-rename**](https://github.com/lmilojevicc/herdr-tab-rename)<br><sub>lmilojevicc</sub> | Auto-rename each Herdr tab to its focused pane's working-directory name. Manually renamed tabs are left alone. | `go` | 4 | 2026-07-31 |
| [**herdr-questmancer**](https://github.com/opsydyn/herdr-questmancer)<br><sub>opsydyn</sub> | A cozy 16-bit adventurers' guild for your Herdr coding agents. Working agents delve, blocked agents call for counsel, finished work returns with spoils. | `coding-agents` `pixel-art` `ratatui` `tui` `rust` | 4 | 2026-09-09 |
| [**herdr-nerd-font-tab-name**](https://github.com/rohankewal/herdr-nerd-font-tab-name)<br><sub>rohankewal</sub> | Nerd Font icons for your herdr tabs — a port of joshmedeski/tmux-nerd-font-window-name | `nerd-fonts` `python` `terminal` `tui` | 4 | 2026-07-31 |
| [**herdr-powershell-title-sync**](https://github.com/aclima01/herdr-powershell-title-sync)<br><sub>aclima01</sub> | Windows/PowerShell port of window-title-sync: sync the terminal title to the focused herdr session | `powershell` | 3 | 2026-07-20 |
| [**herdr-workspace-renamer**](https://github.com/ryanlewis/herdr-workspace-renamer)<br><sub>ryanlewis</sub> | herdr plugin: syncs agent session names onto workspace labels | `rust` | 3 | 🔄 2026-10-15 |
| [**zenbones-herdr**](https://github.com/AkashJana18/zenbones-herdr)<br><sub>AkashJana18</sub> | Minimal paper theme for Herdr. Port of zenbones zenwritten for the Herdr TUI. | `herdr-themes` `themes` `zen-themes` `zenbones` `shell` | 2 | 2026-10-01 |
| [**herdr-pane-autorename**](https://github.com/b12o/herdr-pane-autorename)<br><sub>b12o</sub> | Herdr plugin that autorenames panes with the name of the current running process. | `shell` | 2 | 2026-09-07 |
| [**herdr-titles**](https://github.com/davidolrik/herdr-titles)<br><sub>davidolrik</sub> | Herdr Titles that keep up. – herdr-titles names your tabs and windows after what's actually running; including your AI agents' live session titles — and compos… | `ai-assisted` `go` | 2 | 2026-09-06 |
| [**herdr-english-coach**](https://github.com/GranamyrBR/herdr-english-coach)<br><sub>GranamyrBR</sub> | herdr plugin: color-coded English corrections board — your coding agent logs grammar + dev-jargon fixes to a live side pane while you work | `english` `language-learning` `shell` | 2 | 2026-07-06 |
| [**herdr-ai-tab-name**](https://github.com/ndom91/herdr-ai-tab-name)<br><sub>ndom91</sub> | Auto-rename your Herdr Tabs with local LLMs | `local-llm` `python` | 2 | 2026-09-19 |
| [**herdr-nerd-font-tab-name-windows**](https://github.com/Only-Moon/herdr-nerd-font-tab-name-windows)<br><sub>Only-Moon</sub> | Windows port of herdr-nerd-font-tab-name: Nerd Font icons for herdr tabs with cross-platform support (Windows, macOS, Linux) and folder-based icon resolution | `herdr-windows` `icons` `nerd-fonts` `python` `title` | 2 | 2026-08-10 |
| [**herdr-theme-synthwave-84**](https://github.com/s3rgiosan/herdr-theme-synthwave-84)<br><sub>s3rgiosan</sub> | Synthwave '84 theme for Herdr | `python` | 2 | 2026-09-30 |
| [**🆕 herdr-agent-tab-titles**](https://github.com/ajaykumarMohite/herdr-agent-tab-titles)<br><sub>ajaykumarMohite</sub> | Renames each Herdr tab to the task its coding agent is working on | `claude-code` `developer-tools` `terminal` `python` | 1 | 2026-09-17 |
| [**🆕 herdr-git-tab-name**](https://github.com/blurname/herdr-git-tab-name)<br><sub>blurname</sub> | Herdr plugin that renames tabs to the focused pane's Git branch. | `shell` | 1 | 2026-07-06 |
| [**🆕 herdr-plugin-omp-state**](https://github.com/dk3775/herdr-plugin-omp-state)<br><sub>dk3775</sub> | Report omp agent state to Herdr from its terminal title, for panes the official integration does not cover | `coding-agents` `omp` `python` | 1 | 2026-09-24 |
| [**🆕 herdr-tab-smart-rename-rs**](https://github.com/EmmetZ/herdr-tab-smart-rename-rs)<br><sub>EmmetZ</sub> | _(no description)_ | `rust` | 1 | 2026-08-24 |
| [**🆕 herdr-plugin-pane-id-namer**](https://github.com/gcgo/herdr-plugin-pane-id-namer)<br><sub>gcgo</sub> | Automatically generate an agent name and display it in the terminal. | `shell` | 1 | 2026-09-05 |
| [**🆕 herdr-emoji-time**](https://github.com/hotnugs/herdr-emoji-time)<br><sub>hotnugs</sub> | Emoji for your Herdr spaces, agents and tabs. Inject some fun into your terminal | `emoji` `terminal` `tui` `python` | 1 | 2026-09-12 |
| [**🆕 herdr-tab-title-sync**](https://github.com/lucasleon2107/herdr-tab-title-sync)<br><sub>lucasleon2107</sub> | herdr plugin: rename tabs to the AI agent's conversation title | `ai-agents` `claude-code` `terminal` `tmux` `shell` | 1 | 2026-08-04 |
| [**🆕 herdr-pane-labels**](https://github.com/macd2/herdr-pane-labels)<br><sub>macd2</sub> | Shows each pane's current directory, agent session title, and whether it's local or inside ssh, right in the herdr pane border. | `shell` | 1 | 2026-10-11 |
| [**🆕 herdr-agent-smart-rename**](https://github.com/malone-c/herdr-agent-smart-rename)<br><sub>malone-c</sub> | Names each herdr agent session from what it is actually doing | `python` | 1 | 2026-08-14 |
| [**🆕 ZimMux**](https://github.com/Mr-Destroyer/ZimMux)<br><sub>Mr-Destroyer</sub> | ZimMux: a one-file tmux theme in herdr Ink style. Lavender focus borders, quiet status bar, prefix-free Alt bindings, one-command install with backups. No plug… | `agent` `agent-framework` `agent-workflows` `agentic-ai` `agentic-workflow` | 1 | 2026-09-15 |
| [**🆕 herdr-session-sync**](https://github.com/nengqi/herdr-session-sync)<br><sub>nengqi</sub> | Auto-sync Claude Code, Codex & Agent session names across Herdr pane labels, PTY window titles, and mobile companion apps (Heeler) | `agent` `claude-code` `codex` `heeler` `terminal-multiplexer` | 1 | 🔄 2026-10-26 |
| [**🆕 herdr-claude-tab-rename**](https://github.com/oronbz/herdr-claude-tab-rename)<br><sub>oronbz</sub> | Herdr plugin: keep each tab named after its Claude Code session title (/rename or auto title) | `shell` | 1 | 🔄 2026-10-19 |
| [**herdr-claude-title**](https://github.com/ProjectAJ14/herdr-claude-title)<br><sub>ProjectAJ14</sub> | Herdr plugin that names your terminal tabs, panes and workspaces after the work in them — Claude Code sessions get titles written by Claude itself via claude -… | `ai` `ai-agents` `anthropic` `claude` `claude-code` | 1 | 2026-10-05 |
| [**🆕 herdr-pomodoro**](https://github.com/sazardev/herdr-pomodoro)<br><sub>sazardev</sub> | Minimal, elegant, theme-adaptive Pomodoro timer plugin for Herdr | `rust` | 1 | 2026-09-08 |
| [**🆕 herdr-claude-tab-title**](https://github.com/tmn73/herdr-claude-tab-title)<br><sub>tmn73</sub> | Mirrors each Claude Code session title, and its agent state, onto its Herdr tab | `claude-code` `tabs` `terminal` `typescript` | 1 | 2026-09-07 |

<details><summary>Also relevant to this purpose</summary>

- [kryptamine/herdr-auto-title](https://github.com/kryptamine/herdr-auto-title) — Automatically name Herdr tabs and panes from your current work, Git branch, terminal activity, and Claude Cod…
- [qu8n/herdr-automatic-rename](https://github.com/qu8n/herdr-automatic-rename) — Automatically name herdr tabs after the foreground process (like tmux) or agent session context
- [sh1ma/herdr-auto-title](https://github.com/sh1ma/herdr-auto-title) — Automatically generate titles for herdr tabs from Claude Code and Codex conversations.
- [wyattjoh/herdr-plugin-renamer](https://github.com/wyattjoh/herdr-plugin-renamer) — Renames an auto-generated herdr worktree branch and workspace from the agent's first prompt, via on-device Ap…
- [ythx-101/herdr-social-glass](https://github.com/ythx-101/herdr-social-glass) — Screenshot-friendly Social Glass theme and workflow plugin for Herdr on macOS.
- [aarsh21/herdr-tab-title](https://github.com/aarsh21/herdr-tab-title) — Automatic tmux-like tab titles for Herdr
- [funsaized/herdr-mise](https://github.com/funsaized/herdr-mise) — Run the pass, not the prompts 🧑‍🍳 A visualizer for your agents. A herdr plugin. Intentionally small footprint
- [suisya-systems/herdr-agent-office](https://github.com/suisya-systems/herdr-agent-office) — Your agent fleet as a pixel-art office - a herdr plugin. See who's working, who's stuck, and jump to them.
- [azyu/herdr-agent-auto-naming](https://github.com/azyu/herdr-agent-auto-naming) — Herdr plugin that gives every detected agent a readable two-word name, persisted as the pane label so it surv…
- [maedana/herdr-whereami](https://github.com/maedana/herdr-whereami) — Herdr plugin that automatically renames tabs to show where you are, e.g. repo-name/branch when inside a git r…
- [dev-shimada/herdr-auto-tab-name](https://github.com/dev-shimada/herdr-auto-tab-name) — herdr plugin: automatically name tabs after their current directory

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-text"></a>

## Text & URL Grabbing

> I want to grab strings, paths, or URLs shown on screen without touching the mouse

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-pluck**](https://github.com/rmarganti/herdr-pluck)<br><sub>rmarganti</sub> | quickly copy pattern-matched strings from Herdr panes | `rust` | 25 | 🔄 2026-10-17 |
| [**herdr-tiny-fingers**](https://github.com/hotchpotch/herdr-tiny-fingers)<br><sub>hotchpotch</sub> | tmux-fingers style visible-screen copy hints for Herdr | `tools` `rust` | 15 | 🔄 2026-10-22 |
| [**herdr-fingers**](https://github.com/nathan-poncet/herdr-fingers)<br><sub>nathan-poncet</sub> | 👉 tmux-fingers for Herdr — type a short hint to copy, paste or open any path, URL, hash or number on screen. Rust, Clean Architecture. | `clean-architecture` `clipboard` `rust` `terminal` `tmux-fingers` | 13 | 🔄 2026-10-15 |
| [**herdr-scratchpad**](https://github.com/vjeantet/herdr-scratchpad)<br><sub>vjeantet</sub> | One buffer per tab to prepare your prompt, one key to drop it to your agent's input box. | `clipboard` `ratatui` `rust` `scratchpad` `terminal` | 6 | 2026-08-31 |
| [**herdr-flash**](https://github.com/youguanxinqing/herdr-flash)<br><sub>youguanxinqing</sub> | flash.nvim-style search, select, and yank for Herdr panes | `rust` `terminal` | 6 | 2026-09-16 |
| [**herdr-paste-image**](https://github.com/ddfonseca/herdr-paste-image)<br><sub>ddfonseca</sub> | Paste clipboard images into herdr panes as file paths — tmux-paste-image, ported to herdr | `shell` | 5 | 2026-07-30 |
| [**herdr-ferry**](https://github.com/wavrin/herdr-ferry)<br><sub>wavrin</sub> | Move files and clipboard between the Herdr box and your laptop over SSH — no cloud bucket | `rust` | 4 | 2026-08-29 |
| [**herdr-agent-copy-paste-fork**](https://github.com/calebcauthon/herdr-agent-copy-paste-fork)<br><sub>calebcauthon</sub> | fork by simply copying and pasting, or hotkey the fork into a new pane | `claude-code` `codex` `shell` | 3 | 2026-07-24 |
| [**herdr-copy-search**](https://github.com/qq88976321/herdr-copy-search)<br><sub>qq88976321</sub> | regex and copycat pattern search with extrakto token extraction for herdr scrollback, landing in a tmux-style copy mode (OSC 52) | `copy-mode` `rust` `terminal` `tmux` | 3 | 2026-08-04 |
| [**scoopr**](https://github.com/TawfiqAbubaker/scoopr)<br><sub>TawfiqAbubaker</sub> | Herdr plugin for copying anything to the terminal without using the mouse, inspired by extrakto for tmux. | `rust` | 3 | 2026-09-06 |
| [**herdr-link-browser**](https://github.com/bonkey/herdr-link-browser)<br><sub>bonkey</sub> | Herdr plugin: Ctrl-click an http(s) URL to open it in terminal-browser as a split beside the pane | `terminal-browser` `shell` | 2 | 2026-09-07 |
| [**herdr-s3-clipboard**](https://github.com/jagzmz/herdr-s3-clipboard)<br><sub>jagzmz</sub> | Publish clipboard images as reusable public or presigned URLs from Herdr using S3-compatible storage. | `aws-s3` `clipboard` `cloudflare-r2` `developer-tools` `image-publishing` | 2 | 2026-07-16 |
| [**🆕 herdr-scrollback-capture**](https://github.com/alexjsp/herdr-scrollback-capture)<br><sub>alexjsp</sub> | Herdr plugin that saves the focused pane's scrollback to your Desktop as HTML or text | `shell` | 1 | 2026-06-30 |
| [**🆕 herdr-fleece**](https://github.com/dmazlum/herdr-fleece)<br><sub>dmazlum</sub> | Frame your agent's last answer in Herdr, then copy, save, or send it. | `typescript` | 1 | 🔄 2026-10-15 |
| [**herdr-paste-image**](https://github.com/grooni/herdr-paste-image)<br><sub>grooni</sub> | Paste images from clipboard into herdr panes (Codex, Gemini CLI) — F8 + clipboard cleanup tools (F9/F10) | `shell` | 1 | 2026-09-21 |
| [**🆕 herdr-yank**](https://github.com/pgilad/herdr-yank)<br><sub>pgilad</sub> | Inline keyboard hints for copying visible tokens or opening URLs and files from Herdr panes. | `rust` | 1 | 🔄 2026-10-25 |
| [**🆕 herdr-copy-hints**](https://github.com/rotemb-wond/herdr-copy-hints)<br><sub>rotemb-wond</sub> | tmux-fingers-style keyboard copy hints for Herdr: paths, Git SHAs, URLs, and more | `clipboard` `developer-tools` `keyboard-navigation` `productivity` `terminal` | 1 | 2026-07-23 |
| [**🆕 herdr-copy-pane-id**](https://github.com/wine-fall/herdr-copy-pane-id)<br><sub>wine-fall</sub> | Herdr plugin: copy the focused pane's id to the clipboard, or show every pane's id on its border | `cli` `terminal` `python` | 1 | 🔄 2026-10-27 |
| [**🆕 herdr-translate**](https://github.com/zackshen/herdr-translate)<br><sub>zackshen</sub> | Herdr plugin: translate mouse-selected terminal text in a centered popover | `rust` | 1 | 2026-08-25 |

<details><summary>Also relevant to this purpose</summary>

- [nicosuave/memex](https://github.com/nicosuave/memex) — Search Claude Code, Codex, Pi, OpenCode, Github Copilot & Cursor transcripts. Resume sessions. Track tokens.
- [iurysza/termscope](https://github.com/iurysza/termscope) — Open files and links already visible on your terminal screen in a split.
- [pinkpixel-dev/quota](https://github.com/pinkpixel-dev/quota) — Desktop app, VSCode extension, CLI, and Herdr plugin for tracking AI usage across GitHub Copilot, Codex, Clau…
- [termaxa/termaxa](https://github.com/termaxa/termaxa) — The agent's prompt shows you the command; Termaxa shows you the consequence. Previews, backups, policy, an au…
- [jlimas/herdr-worktree-seed](https://github.com/jlimas/herdr-worktree-seed) — Herdr plugin that seeds new worktrees with copy-on-write node_modules and configurable local dotfiles
- [mrolafsson/herdr-file-transfer](https://github.com/mrolafsson/herdr-file-transfer) — Running herdr on a VPS or remote box (Hetzner, a cloud dev server) and uploading files is a pain? Drop them o…
- [tanshio/herdr-worktreeinclude](https://github.com/tanshio/herdr-worktreeinclude) — Herdr plugin: copy gitignored files matching .worktreeinclude into newly created worktrees
- [khatriafaz/herdr-plugin-cow-worktree](https://github.com/khatriafaz/herdr-plugin-cow-worktree) — Herdr plugin for strict copy-on-write Git worktrees that include ignored local files
- [eightHundreds/herdr-worktreeinclude](https://github.com/eightHundreds/herdr-worktreeinclude) — Herdr plugin: copy .worktreeinclude-selected gitignored files into new worktrees
- [rheech22/herdr-comment-on-copy](https://github.com/rheech22/herdr-comment-on-copy) — Drag to select terminal text and open a comment popup automatically. Send feedback with context to AI agents…
- [crexi/herdr-worktree-copy](https://github.com/crexi/herdr-worktree-copy) — Herdr plugin that copies and symlinks worktree-local files from a .worktree-copy manifest
- [shadowfax92/herdr-comments](https://github.com/shadowfax92/herdr-comments) — Annotate copied Herdr terminal output, collect per-pane comments, and review them in Neovim.
- [zerodice0/herdr-plugin-worktree-bootstrap](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap) — Safely copy ignored local files and run setup commands in new Herdr Git worktrees
- [Feasy01/herdr-allow](https://github.com/Feasy01/herdr-allow) — herdr plugin: copy gitignored files (.env, secrets, local configs) into every new worktree via a .herdr-allow…
- [jiangkoumo/herdr-plugin-layerfs](https://github.com/jiangkoumo/herdr-plugin-layerfs) — Copy-on-write LayerFS branches as Herdr workspaces, grouped under the repo like worktrees and restored after…
- [tupton/herdr-worktree-include](https://github.com/tupton/herdr-worktree-include) — Symlink or copy untracked files to git worktrees created by herdr.

</details>

[⬆ Back to purposes](#purposes)

<a id="cat-meta"></a>

## Plugin Management & Authoring

> I want to manage plugins themselves, or build my own

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**herdr-plus**](https://github.com/cloudmanic/herdr-plus)<br><sub>cloudmanic</sub> | An extension for herdr, built as a first-class herdr plugin — a collection of tools that make it better: Projects and Quick Actions. | `go` | 367 | 2026-09-04 |
| [**herdr-plugin-manager**](https://github.com/speardragon/herdr-plugin-manager)<br><sub>speardragon</sub> | Manage herdr plugins from a popup — install, update, enable/disable, uninstall, and browse the herdr-plugin marketplace. Recommended key: prefix+p | `plugin-manager` `tui` `shell` | 81 | 🔄 2026-10-19 |
| [**herdr-lazy**](https://github.com/natori-hrj/herdr-lazy)<br><sub>natori-hrj</sub> | Declarative, reproducible plugin manager and curated distro for Herdr — one list, a lockfile, and a safe manage pane. | `cli` `lockfile` `plugin-manager` `rust` `terminal` | 27 | 🔄 2026-10-14 |
| [**house-of-herdr**](https://github.com/alasano/house-of-herdr)<br><sub>alasano</sub> | A collection of plugins for Herdr, including Codex Micro: agent status lights and controls on the Work Louder Codex Micro | `codex-micro` `work-louder` `typescript` | 8 | 2026-08-13 |
| [**herdr-plugin-manager**](https://github.com/vika2603/herdr-plugin-manager)<br><sub>vika2603</sub> | Browse, install and update herdr plugins from a popup or the command line | `go` `tui` | 5 | 🔄 2026-10-19 |
| [**herdr-plugin-rust**](https://github.com/Newt6611/herdr-plugin-rust)<br><sub>Newt6611</sub> | A Rust application framework for building Herdr plugins. | `rust` | 3 | 2026-07-09 |
| [**herdr-plugins-labs**](https://github.com/hmu332233/herdr-plugins-labs)<br><sub>hmu332233</sub> | Experimental plugins for Herdr — incubated here, graduated to their own repos | `labs` `javascript` | 2 | 2026-09-23 |

[⬆ Back to purposes](#purposes)

<a id="cat-other"></a>

## Other & Utilities

> Handy things that don't fit any of the categories above

| Plugin | What it does | Tags | ★ | Last updated |
| --- | --- | --- | --: | --- |
| [**terminal-browser**](https://github.com/zenbu-labs/terminal-browser)<br><sub>zenbu-labs</sub> | A real browser inside your terminal | `browser` `claude-code` `claude-code-plugin` `claude-skills` `cli` | 4318 | 🔄 2026-10-28 |
| [**herdr-lantern**](https://github.com/aigorahub/herdr-lantern)<br><sub>aigorahub</sub> | Lantern, by Elves. A Herdr plugin: the herd is in the field; Lantern illuminates who needs you and what they are working toward. | `python` | 70 | 🔄 2026-10-27 |
| [**herdr-openspec**](https://github.com/FlorisKr/herdr-openspec)<br><sub>FlorisKr</sub> | Openspec plugin for herdr | `python` | 23 | 2026-10-07 |
| [**herdr-gui**](https://github.com/undivisible/herdr-gui)<br><sub>undivisible</sub> | a gui surface for herdr + more. built with crepuscular gpui. | `crepuscularity` `gpui` `rust` | 22 | 2026-07-27 |
| [**herdr-commandcode-plugin**](https://github.com/TheMetalStorm/herdr-commandcode-plugin)<br><sub>TheMetalStorm</sub> | Integrates Commandcode into Herdr | `cli` `commandcode` `herdr-integration` `shell` | 13 | 2026-07-30 |
| [**herdr-plugins-directory**](https://github.com/MIDO-ruby7/herdr-plugins-directory)<br><sub>MIDO-ruby7</sub> | A link collection for finding herdr plugins by what you want to get done. | `python` | 12 | 🔄 2026-10-28 |
| [**herdr-plugin-cmux**](https://github.com/lachieh/herdr-plugin-cmux)<br><sub>lachieh</sub> | Mirrors every herdr-managed agent into a cmux sidebar as its own live row, with a status pill and a click-to-jump task line. | `javascript` | 11 | 2026-07-01 |
| [**neon-herdr**](https://github.com/neon-solutions/neon-herdr)<br><sub>neon-solutions</sub> | The official Neon Herdr Plugin | `typescript` | 11 | 2026-08-06 |
| [**herdr-freebuff-plugin**](https://github.com/TheMetalStorm/herdr-freebuff-plugin)<br><sub>TheMetalStorm</sub> | Freebuff lifecycle integration plugin for Herdr — reports idle/working/blocked state via file polling and PTY content scraping | `cli` `freebuff` `herdr-integration` `shell` | 8 | 2026-07-22 |
| [**wave-tui**](https://github.com/takemo101/wave-tui)<br><sub>takemo101</sub> | Quiet terminal radio for work sessions | `rust` | 5 | 2026-07-20 |
| [**mu-herdr**](https://github.com/AndresMpa/mu-herdr)<br><sub>AndresMpa</sub> | A herdr configuration made to work with MμVim | `herdr-integration` `muvim` `shell` | 4 | 2026-09-28 |
| [**shipframe**](https://github.com/juanitourquiza/shipframe)<br><sub>juanitourquiza</sub> | AI coding workflows for teams that plan, prove, and ship. | `ai` `ai-coding` `ai-tools` `claude` `claude-code` | 4 | 🔄 2026-10-24 |
| [**broadmand**](https://github.com/francjpd/broadmand)<br><sub>francjpd</sub> | Broadcast commands with ease | `shell` | 3 | 2026-10-10 |
| [**herdr-plugins**](https://github.com/JacobAtchley/herdr-plugins)<br><sub>JacobAtchley</sub> | My custom herdr plugins | `command-line-tool` `utility` `rust` | 3 | 2026-10-07 |
| [**herdr-memory**](https://github.com/jatingargiitk/herdr-memory)<br><sub>jatingargiitk</sub> | A Herdr plugin that builds a living brain from your coding sessions — progressively learning what works, what failed, and what you decided. | `shell` | 3 | 2026-08-11 |
| [**hrd**](https://github.com/joshuadavidthomas/hrd)<br><sub>joshuadavidthomas</sub> | Manage your herd of sandboxes and the Herdr sessions running on them | `go` | 3 | 🔄 2026-10-23 |
| [**herdr-sprites-plugin**](https://github.com/superfly/herdr-sprites-plugin)<br><sub>superfly</sub> | Official Herdr plugin for Fly.io Sprites | `sandboxes` `sprites` `javascript` | 3 | 🔄 2026-10-28 |
| [**herdr-codespaces**](https://github.com/alexjyong/herdr-codespaces)<br><sub>alexjyong</sub> | Plugin to add codespace support to heder | `shell` | 2 | 2026-09-28 |
| [**🆕 devnull-tui**](https://github.com/arhen/devnull-tui)<br><sub>arhen</sub> | Unofficial terminal UI for /dev/null (dev-null.sh) — the feed, threads and inbox in any terminal, or as a Herdr pane | `cli` `dev-null` `devnull` `terminal` `tui` | 2 | 🔄 2026-10-23 |
| [**herdr-rails**](https://github.com/codergeek121/herdr-rails)<br><sub>codergeek121</sub> | Herdr + Rails | `ai` `rails` `shell` | 2 | 2026-09-22 |
| [**herdr-undo-close**](https://github.com/federbenjamin/herdr-undo-close)<br><sub>federbenjamin</sub> | Reopen the pane you just closed in Herdr: same split, same scrollback, Claude Code conversation included | `claude-code` `scrollback` `shell` `terminal` `undo` | 2 | 🔄 2026-10-27 |
| [**herdrctx**](https://github.com/j0urneyk/herdrctx)<br><sub>j0urneyk</sub> | Terminal UI for managing local Herdr sessions | `go` | 2 | 🔄 2026-10-20 |
| [**herdr-standup**](https://github.com/neospeed83/herdr-standup)<br><sub>neospeed83</sub> | Evidence-backed daily standups from Git activity and Herdr context. | `developer-tools` `standup` `rust` | 2 | 2026-08-31 |
| [**herdr-handsfree**](https://github.com/RanolP/herdr-handsfree)<br><sub>RanolP</sub> | Hands-free herdr plugin: voice dictation (whisper.cpp) + webcam gaze mouse for macOS | `rust` | 2 | 2026-07-30 |
| [**pixtui**](https://github.com/RizRiyz/pixtui)<br><sub>RizRiyz</sub> | Pixel Art Editor on Terminal | `bohay-module` `editor` `luvus-module` `pixel-art` `termina` | 2 | 2026-08-07 |
| [**herdr-shadow-pane**](https://github.com/shaozk/herdr-shadow-pane)<br><sub>shaozk</sub> | A Herdr plugin—Shadow Clone Panel: Control multiple panels simultaneously. | `rust` `vibe-coding` | 2 | 2026-09-14 |
| [**herdr-suite-site**](https://github.com/StructuPath/herdr-suite-site)<br><sub>StructuPath</sub> | Landing page for the StructuPath Herdr Suite — herdr.structupath.ai | `herdr-integration` `javascript` | 2 | 2026-10-05 |
| [**herdr-stt**](https://github.com/xtwist/herdr-stt)<br><sub>xtwist</sub> | Speech-to-text for Herdr | `rust` | 2 | 2026-09-18 |
| [**herdr-zen**](https://github.com/y4m3/herdr-zen)<br><sub>y4m3</sub> | Zen mode for Herdr with an adjustable centered pane width | `rust` `terminal` `zen-mode` | 2 | 2026-08-19 |
| [**🆕 herdr-edit-windows**](https://github.com/aclima01/herdr-edit-windows)<br><sub>aclima01</sub> | A simple text editor that runs in a herdr pane beside your coding agent — file tree, syntax-highlighted editor, and an uncommitted-diff tab. Windows-only. | `rust` | 1 | 2026-07-25 |
| [**🆕 herdr-tts**](https://github.com/Aktrov/herdr-tts)<br><sub>Aktrov</sub> | Herdr plugin that speaks the selected terminal text aloud in a natural neural voice (Piper) — right-click or a shortcut, with a stop key. | `tts` `python` | 1 | 2026-09-07 |
| [**🆕 herdr-wrapped-tabs**](https://github.com/AlexeyKrotkov/herdr-wrapped-tabs)<br><sub>AlexeyKrotkov</sub> | Always-visible wrapped tabs for Herdr | `python` | 1 | 2026-09-24 |
| [**🆕 herdr-quotabar**](https://github.com/ArnaudRinquin/herdr-quotabar)<br><sub>ArnaudRinquin</sub> | Claude plan quotas (5h / 7d / per-model) as one compact line in the Herdr tab bar. Provider-pluggable. | `claude-code` `python` | 1 | 2026-09-08 |
| [**🆕 herdr-ssh-config-dash**](https://github.com/bearylabs/herdr-ssh-config-dash)<br><sub>bearylabs</sub> | A Herdr plugin for managing machines from literal hosts in ~/.ssh/config. | `typescript` | 1 | 2026-10-02 |
| [**🆕 herdr-stoplight**](https://github.com/BowlOfSoup/herdr-stoplight)<br><sub>BowlOfSoup</sub> | Drive a physical Arduino traffic-light module from the live status of Herdr | `go` | 1 | 2026-07-11 |
| [**🆕 archify-herdr-plugin**](https://github.com/bozoinc/archify-herdr-plugin)<br><sub>bozoinc</sub> | Herdr plugin derived from archify DESIGN.md (verified-source). M6 adapter directive-derived. | `html` | 1 | 🔄 2026-10-19 |
| [**harbr**](https://github.com/dev-town/harbr)<br><sub>dev-town</sub> | Harbour TUI | `typescript` | 1 | 2026-10-10 |
| [**herdr-desk**](https://github.com/duyet/herdr-desk)<br><sub>duyet</sub> | Herdr plugin for unattended repo maintenance | `typescript` | 1 | 🔄 2026-10-27 |
| [**🆕 herdr-drop**](https://github.com/ecylmz/herdr-drop)<br><sub>ecylmz</sub> | Drag a file onto a Herdr pane and it lands in that pane's directory, through the ssh session you already have | `file-transfer` `ssh` `terminal` `python` | 1 | 2026-09-18 |
| [**herdr-rainfrog**](https://github.com/fraction12/herdr-rainfrog)<br><sub>fraction12</sub> | Open Rainfrog in a managed HerdR pane. | `shell` | 1 | 2026-08-15 |
| [**🆕 herdr-mistral-vibe**](https://github.com/guiand888/herdr-mistral-vibe)<br><sub>guiand888</sub> | Herdr plugin that starts Mistral Vibe sessions in Herdr panes | `shell` | 1 | 2026-10-12 |
| [**🆕 herdr-web**](https://github.com/harshagowda/herdr-web)<br><sub>harshagowda</sub> | A real browser tab for herdr on macOS, drivable over CDP | `cmux` `herder-webui` `javascript` | 1 | 🔄 2026-10-19 |
| [**🆕 herdr-plugin-minimax-code**](https://github.com/jaaacki/herdr-plugin-minimax-code)<br><sub>jaaacki</sub> | Herdr plugin for MiniMax Code | `shell` | 1 | 2026-10-06 |
| [**🆕 herdr-tiling**](https://github.com/jaeheonji/herdr-tiling)<br><sub>jaeheonji</sub> | Hyprland-style pane movement and tmux-style layouts for Herdr | `rust` | 1 | 🔄 2026-10-28 |
| [**🆕 herdr-services**](https://github.com/lucidstack/herdr-services)<br><sub>lucidstack</sub> | Plugin to track services running inside herdr workspaces | `rust` | 1 | 2026-09-16 |
| [**🆕 subtitle-sanitizer**](https://github.com/luismascotto/subtitle-sanitizer)<br><sub>luismascotto</sub> | Go CLI tool (and WASM too!) to load ASS/SRT subtitles, apply rules to identify and remove text for hearing impaired and other little details. Inspired on Subti… | `go` | 1 | 🔄 2026-10-28 |
| [**🆕 herdr-plugins**](https://github.com/narumiruna/herdr-plugins)<br><sub>narumiruna</sub> | _(no description)_ | `rust` | 1 | 2026-08-08 |
| [**🆕 herdr-api-client**](https://github.com/playsthisgame/herdr-api-client)<br><sub>playsthisgame</sub> | HTTP/REST API client in a herdr split pane or tab — browse, run and test requests without leaving the terminal | `http-client` `rest-client` `tui` `shell` | 1 | 2026-08-08 |
| [**herdr-browser**](https://github.com/redsquiggle/herdr-browser)<br><sub>redsquiggle</sub> | Keep Chromium tab groups aligned with Herdr workspaces | `chromium` `ratatui` `rust` | 1 | 2026-07-28 |
| [**🆕 herdr-pinned-workspaces**](https://github.com/skydiver/herdr-pinned-workspaces)<br><sub>skydiver</sub> | A Herdr plugin that keeps declared workspaces alive. | `terminal` `tui` `workspaces` `python` | 1 | 2026-09-21 |
| [**herdr-pdf**](https://github.com/tim80411/herdr-pdf)<br><sub>tim80411</sub> | PDF viewer plugin for herdr: renders pages into a split pane through the pane.graphics stream API | `go` `pdf` `terminal` | 1 | 2026-09-17 |
| [**herdr-plugin-k8s-context**](https://github.com/tkuchiki/herdr-plugin-k8s-context)<br><sub>tkuchiki</sub> | Open Herdr tabs with isolated Kubernetes contexts and namespaces. | `go` | 1 | 2026-08-15 |
| [**multitrunk-herdr-plugin**](https://github.com/yoyoyeti/multitrunk-herdr-plugin)<br><sub>yoyoyeti</sub> | Herdr plugin for multitrunk task workspaces | `git` `multitrunk` `rust` | 1 | 2026-08-31 |

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
