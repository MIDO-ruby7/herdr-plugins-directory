# herdr plugins by purpose

[🇯🇵 日本語](README.md) · [🇺🇸 English](README.en.md) · 🇨🇳 中文

**一个按照「你想做什么」来查找 [herdr](https://herdr.dev/) 插件的链接合集。**

- 收录 **818** 个插件 / 最后更新 **2026-10-26 13:01 UTC**（每 6 小时自动刷新）
- 数据来源：打了 GitHub 话题标签 [`herdr-plugin`](https://github.com/topics/herdr-plugin) 的仓库——与官方市场 [herdr.dev/plugins](https://herdr.dev/plugins/) 的数据来源相同
- 分类是根据仓库描述和话题标签自动推断的。如果分类不准确，可以通过 PR 修改 [`data/overrides.json`](data/overrides.json)
- 安装：`herdr plugin install owner/repo` —— [官方文档](https://herdr.dev/docs/plugins/)

> [!WARNING]
> 这是自动采集的索引，不是经过审核的目录。插件是直接在你的电脑上运行的代码，安装前请检查其 manifest 和会执行的命令。

<a id="purposes"></a>

## 按目的浏览

- [**🆕 最近新增**](#cat-new) (52) — 最近 7 天内加入本列表的插件。
- [**通知与提醒**](#cat-notify) (28) — 即使离开座位，也想知道 Agent 何时完成或卡在等待输入
- [**手机与远程操控**](#cat-remote) (51) — 想在外出或用手机时监控 Agent，只需回传批准即可
- [**Agent 编排与并行执行**](#cat-agents) (145) — 想统一启动、分工并管理多个 AI Agent
- [**git 工作树与分支管理**](#cat-worktree) (42) — 想为每项工作单独开一个工作树，收尾清理也自动完成
- [**代码审查与差异对比**](#cat-review) (38) — 想阅读 Agent 写的差异并对其发表评论
- [**GitHub / issue 跟踪工具集成**](#cat-forge) (36) — 想以 issue 或 PR 为起点开始工作，并追踪 PR 状态
- [**工作区与布局搭建**](#cat-layout) (32) — 打开项目时，希望标签页、窗格和启动命令一次性就位
- [**窗格导航与快捷键**](#cat-navigate) (92) — 想用和编辑器一样的快捷键在窗格、工作区之间移动和调整大小
- [**文件浏览与编辑器联动**](#cat-files) (57) — 想在窗格中打开文件树，或与编辑器的状态保持一致
- [**Token 与费用管理**](#cat-cost) (23) — 想看看 Agent 花费了多少，并想削减用量
- [**监控与仪表盘**](#cat-monitor) (66) — 想一目览尽 Agent 和机器的状态
- [**搜索与模糊查找器**](#cat-finder) (60) — 只记得大概名字也想调出命令或项目
- [**自动化、钩子与定时任务**](#cat-automation) (39) — 想在创建工作树或指定时机自动运行固定的操作步骤
- [**会话保存与恢复**](#cat-session) (22) — 关闭工作后，希望之后能从同一状态继续
- [**标题、命名与外观**](#cat-naming) (30) — 想让标签页名称和终端标题自动变得清晰易懂，或想改变外观
- [**文本与 URL 提取**](#cat-text) (13) — 想不用鼠标就抓取屏幕上显示的字符串、路径或 URL
- [**插件管理与开发**](#cat-meta) (7) — 想管理插件本身，或者自己动手做一个
- [**其他与实用工具**](#cat-other) (37) — 不属于以上任何分类，但很实用的东西

<a id="cat-new"></a>

## 🆕 最近新增

> 最近 7 天内加入本列表的插件。

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**🆕 herduck**](https://github.com/wenhanweime/herduck)<br><sub>wenhanweime</sub> | Agent window management, project visibility, and a global conversation library. Built on Herdr for people and Agents. | `ai-agents` `claude-code` `codex` `coding-agents` `rust` | 8 | 2026-10-26 |
| [**🆕 herdr-kata**](https://github.com/salmonumbrella/herdr-kata)<br><sub>salmonumbrella</sub> | Runs Kata cron jobs and workflows as Herdr agents | `kata` `go` | 2 | 2026-10-25 |
| [**🆕 claude-deck**](https://github.com/bigsan/claude-deck)<br><sub>bigsan</sub> | Watch Claude Code sessions: scratchpad files, tasks and every tool call, standalone or as a herdr plugin | `claude-code` `ratatui` `tui` `rust` | 1 | 2026-10-24 |
| [**🆕 github-issue-herdr-plugin**](https://github.com/nyanyaon/github-issue-herdr-plugin)<br><sub>nyanyaon</sub> | 用于「牧养」GitHub issue 的 Claude Code 插件 | `rust` | 1 | 2026-07-27 |
| [**🆕 herdr-new-workspace**](https://github.com/bethanyj28/herdr-new-workspace)<br><sub>bethanyj28</sub> | Pop up new workspace modal for herdr | `shell` | 0 | 2026-10-23 |
| [**🆕 herdr-jcode-integration**](https://github.com/capt-marbles/herdr-jcode-integration)<br><sub>capt-marbles</sub> | 用于 Jcode 生命周期状态和会话报告的 Herdr 插件 | `jcode` `shell` | 0 | 2026-08-09 |
| [**🆕 herdr-session-fork**](https://github.com/DanielGnzlzVll/herdr-session-fork)<br><sub>DanielGnzlzVll</sub> | Herdr plugin: fork the focused agent session into a sibling pane with one keystroke | `shell` | 0 | 2026-09-22 |
| [**🆕 herdr-away-signal**](https://github.com/devicki/herdr-away-signal)<br><sub>devicki</sub> | Herdr plugin: an away signal for bots (Grok Bot, dots, any webhook). Toggle away mode with a key; while away, finished or waiting agents are POSTed to your bot… | `agent-orchestration` `ai-agents` `away-mode` `claude-code` `grok-bot` | 0 | 2026-10-20 |
| [**🆕 herdr-worktree-rm**](https://github.com/dorshinar/herdr-worktree-rm)<br><sub>dorshinar</sub> | Herdr plugin: delete a worktree checkout in the background with a confirm popup and sidebar spinner, without freezing the UI | `shell` | 0 | 2026-10-22 |
| [**🆕 herdr-run-targets**](https://github.com/fantoine/herdr-run-targets)<br><sub>fantoine</sub> | Launch, stop and restart a repository's dev services from a dashboard pane in Herdr | `python` | 0 | 2026-10-09 |
| [**🆕 herdr-plugin-session-pruner**](https://github.com/Gareth-Rouse/herdr-plugin-session-pruner)<br><sub>Gareth-Rouse</sub> | herdr 插件：记录工作区的最后使用时间，在 Spaces 侧边栏中显示已过去多久，并将闲置工作区排除在会话恢复之外 | `terminal-multiplexer` `shell` | 0 | 2026-10-05 |
| [**🆕 herdr-todos**](https://github.com/limonequantistico/herdr-todos)<br><sub>limonequantistico</sub> | Simple todo lists from a TODOS.md file, in a herdr side panel: drag to reorder, click to tick. | `rust` | 0 | 2026-10-20 |
| [**🆕 herdr-powertoys**](https://github.com/m16khb-org/herdr-powertoys)<br><sub>m16khb-org</sub> | Herdr plugin: equalize split panes, snap a split to half, or cycle 1/2, 2/3, 1/3 | `layout` `panes` `perl` `tiling` | 0 | 2026-10-09 |
| [**🆕 herdr-plugin-recent-spaces**](https://github.com/mike-bronner/herdr-plugin-recent-spaces)<br><sub>mike-bronner</sub> | Herdr 插件：让空间侧边栏始终按最近使用顺序排列。 | `rust` | 0 | 2026-09-24 |
| [**🆕 herdr-agent-tokens**](https://github.com/mikitahimpel/herdr-agent-tokens)<br><sub>mikitahimpel</sub> | Herdr plugin: show Claude Code and Codex token usage in the agent sidebar | `rust` | 0 | 2026-10-12 |
| [**🆕 herdr-whichkey**](https://github.com/Qu4tro/herdr-whichkey)<br><sub>Qu4tro</sub> | herdr 的 blezz/which-key 风格操作菜单——按下触发键后，每个操作只需一次按键，无需输入，无需回车 | `rust` | 0 | 2026-07-22 |
| [**🆕 herdr-close-other-panes**](https://github.com/reobin/herdr-close-other-panes)<br><sub>reobin</sub> | herdr 版的 vim ctrl-w o——关闭除聚焦窗格外的所有窗格 | `shell` | 0 | 2026-09-18 |
| [**🆕 herdr-context**](https://github.com/Somliga/herdr-context)<br><sub>Somliga</sub> | Your Claude Code conversations as one tree, and the context editable: a Herdr plugin. | `claude-code` `go` | 0 | 2026-09-30 |
| [**🆕 view-and-edit-herdr-plugin**](https://github.com/suzuki-junya108/view-and-edit-herdr-plugin)<br><sub>suzuki-junya108</sub> | herdr plugin: preview, edit, and browse files (text, Markdown, HTML, images, video, audio, PDF, Office, CSV/JSON, SQLite) in a popup. macOS, Japanese UI. | `file-viewer` `macos` `python` | 0 | 2026-09-28 |
| [**🆕 herdr-agent-notes**](https://github.com/timjonez/herdr-agent-notes)<br><sub>timjonez</sub> | herdr 插件：为 Agent 贴上便签，让你能看出某个 Agent 为何处于空闲状态 | `python` | 0 | 2026-08-20 |
| [**🆕 herdr-worktree**](https://github.com/tjg184/herdr-worktree)<br><sub>tjg184</sub> | 同时兼容 worktrunk 和原生工作树的 Herdr 工作树插件 | `rust` | 0 | 2026-10-13 |
| [**🆕 herdr-git-status**](https://github.com/ubuntudroid/herdr-git-status)<br><sub>ubuntudroid</sub> | herdr plugin: live CI and code-review status for GitHub and GitLab in the sidebar, plus on-demand CI-detail and My PRs panes | `shell` | 0 | 2026-10-23 |
| [**🆕 HerdRabbit**](https://github.com/ultivis-iot/HerdRabbit)<br><sub>ultivis-iot</sub> | Open your Herdr sessions from a phone or another PC (PWA over Tailscale). | `javascript` | 0 | 2026-10-26 |
| [**🆕 dotfiles**](https://github.com/Unique-Divine/dotfiles)<br><sub>Unique-Divine</sub> | 来自 Unique Divine 的 dotfiles 以及其他 ~ 目录下的配置 | `dotfiles` `lua` `neovim` `neovim-dotfiles` `nvim` | 0 | 2026-10-25 |
| [**🆕 herdr-radio**](https://github.com/vrwolf1004/herdr-radio)<br><sub>vrwolf1004</sub> | Play Radio Browser stations audio-only in herdr, with the current station and playback state shown in the sidebar dock | `python` | 0 | 2026-10-23 |
| [**🆕 pi-agent-usage**](https://github.com/w784415/pi-agent-usage)<br><sub>w784415</sub> | 显示 OpenAI Codex 配额和重置时间的 Pi 扩展，支持 Herdr 插件 | `openai-codex` `pi-extension` `pi-package` `quota` `typescript` | 0 | 2026-08-26 |
| [**🆕 herdr-job-board**](https://github.com/larrychannon/herdr-job-board)<br><sub>larrychannon</sub> | A To do / Doing / Waiting-on-you board for agent jobs, in a Herdr split pane. | `javascript` | 1 | 2026-10-23 |
| [**🆕 herdr-fleet-plugin**](https://github.com/yarrasys/herdr-fleet-plugin)<br><sub>yarrasys</sub> | herdr plugin: start, restart and swap a team of named coding agents from a per-repository fleet file (.herdr/fleet.toml) | `coding-agents` `multi-agent` `python` | 1 | 2026-10-26 |
| [**🆕 instinct-herdr-tunnel**](https://github.com/romiluz13/instinct-herdr-tunnel)<br><sub>romiluz13</sub> | Let an AI assistant such as Instinct watch and steer your Herdr coding agents: a loopback portal with a 26-action allowlist, a bearer token and an audit log, p… | `ai-agents` `cloudflare-tunnel` `coding-agents` `nodejs` `javascript` | 2 | 2026-10-25 |
| [**🆕 herdr-ingest**](https://github.com/H3xept/herdr-ingest)<br><sub>H3xept</sub> | 为来自 Sentry、Linear、GitHub 或任意 JSON 数据管道的每个工作项，创建一个独立的 herdr 空间。 | `github` `linear` `sentry` `terminal` `shell` | 1 | 2026-09-26 |
| [**🆕 herdr-stats**](https://github.com/jeffarese/herdr-stats)<br><sub>jeffarese</sub> | Live CPU, memory, disk, temperature, GPU, power and network stats in herdr's tab bar: braille graphs, gauges and reactive icons | `linux` `macos` `rust` `system-monitor` `terminal` | 1 | 2026-10-23 |
| [**🆕 account-capacity-dock**](https://github.com/Mako-L/account-capacity-dock)<br><sub>Mako-L</sub> | Quota rings for every Claude, Codex and Cursor account: a desktop dock, a terminal app and a Herdr widget. | `claude` `cliproxyapi` `codex` `cursor` `python` | 4 | 2026-10-22 |
| [**🆕 stampede**](https://github.com/vib-z/stampede)<br><sub>vib-z</sub> | Text tasks to your Grok Bot. It reaches your Mac over Tailscale, where Claude Code does the job, adding other agents (Codex, Cursor and more) as needed. Nothin… | `agent-orchestration` `ai-agents` `claude-code` `cli` `codex` | 3 | 2026-10-25 |
| [**🆕 devnull-tui**](https://github.com/arhen/devnull-tui)<br><sub>arhen</sub> | Unofficial terminal UI for /dev/null (dev-null.sh) — the feed, threads and inbox in any terminal, or as a Herdr pane | `cli` `dev-null` `devnull` `terminal` `tui` | 2 | 2026-10-23 |
| [**🆕 diffui**](https://github.com/dgsienko/diffui)<br><sub>dgsienko</sub> | Locally hosted web tool and terminal ui for reviewing live diffs and improving your agentic coding and review flow. | `agentic-coding` `ai-agents` `ai-tools` `claude-code` `cli` | 2 | 2026-10-23 |
| [**🆕 herdr-sbx**](https://github.com/lanwen/herdr-sbx)<br><sub>lanwen</sub> | Herdr Plugin to enable Docker Sandboxes as SSH connected machines. Full agent visibility, plugin sync | `docker` `sandboxes` `go` | 2 | 2026-10-26 |
| [**🆕 ovis**](https://github.com/devswha/ovis)<br><sub>devswha</sub> | Ovis (formerly herdr web UI): free, open-source browser and phone client for herdr. Chat and live terminal for Claude Code, Codex and every agent pane, remote… | `agentic-coding` `ai-agents` `bun` `claude-code` `codex` | 1502 | 2026-10-26 |
| [**🆕 herdr-island**](https://github.com/speardragon/herdr-island)<br><sub>speardragon</sub> | Your herdr agents live in the MacBook notch: approve, answer and watch them from a Dynamic Island-style panel | `ai-agents` `claude-code` `macos` `notch` `swiftui` | 4 | 2026-10-26 |
| [**🆕 herdr-gh-runs**](https://github.com/kkjdaniel/herdr-gh-runs)<br><sub>kkjdaniel</sub> | GitHub Actions runs in a herdr pane: follows your repo, live status, step logs and notifications | `gh` `github-actions` `terminal` `tui` `python` | 1 | 2026-10-22 |
| [**🆕 reficus**](https://github.com/81zi/reficus)<br><sub>81zi</sub> | Grow the focused pane and shrink the others on every focus change | `python` | 4 | 2026-10-21 |
| [**🆕 herdr-claude-autoupdate**](https://github.com/0xMMA/herdr-claude-autoupdate)<br><sub>0xMMA</sub> | herdr plugin: restarts idle Claude Code panes onto the newly installed version, in place, same session and flags, drafts kept. | `claude-code` `typescript` | 1 | 2026-10-11 |
| [**🆕 medley**](https://github.com/WebscapeOrg/medley)<br><sub>WebscapeOrg</sub> | Custom sounds for every herdr workspace and status | `audio` `notifications` `python` | 1 | 2026-10-23 |
| [**🆕 levi**](https://github.com/rsdlt/levi)<br><sub>rsdlt</sub> | The fastest blade for your git history. Fuzzy search for you, plain text for your agents. | `claude-code` `cli` `coding-agents` `diff` `fzf` | 8 | 2026-10-22 |
| [**🆕 herdr-vitals**](https://github.com/mrolafsson/herdr-vitals)<br><sub>mrolafsson</sub> | How your machines are doing, at a glance, before they slow your agents down. A herdr plugin: CPU, load, memory, disks (and when they'll be full) and network fo… | `anthropic` `bubbletea` `claude-code` `codex` `coding-agents` | 2 | 2026-10-20 |
| [**🆕 beady-eye**](https://github.com/CodeForBreakfast/beady-eye)<br><sub>CodeForBreakfast</sub> | Draws the work in your beads trackers as trees, with what each agent is doing beside the bead it works. It also watches beads for whatever waits on them, and s… | `agents` `beads` `claude-code` `claude-code-plugin` `github` | 24 | 2026-10-26 |
| [**🆕 herdr-macos-plugins**](https://github.com/klinter007/herdr-macos-plugins)<br><sub>klinter007</sub> | Files and Links, Stay Awake, and System Monitor plugins for standard Herdr on macOS | `python` | 3 | 2026-10-12 |
| [**🆕 herdr-file-transfer**](https://github.com/mrolafsson/herdr-file-transfer)<br><sub>mrolafsson</sub> | Running herdr on a VPS or remote box (Hetzner, a cloud dev server) and uploading files is a pain? Drop them on a popup and they're copied over ssh into your ag… | `bubbletea` `claude-code` `coding-agents` `file-transfer` `go` | 3 | 2026-10-22 |
| [**🆕 herdr-threads**](https://github.com/alepar/herdr-threads)<br><sub>alepar</sub> | durable group threads for your agents, cross-harness and cross-machine | `rust` | 2 | 2026-10-24 |
| [**🆕 herdr-workspaces-manager**](https://github.com/dardT/herdr-workspaces-manager)<br><sub>dardT</sub> | Discover projects and create distinctly named Herdr workspaces with a fast terminal picker | `rust` | 2 | 2026-10-19 |
| [**🆕 browsr**](https://github.com/g00rek/browsr)<br><sub>g00rek</sub> | Keep a dedicated Chromium tab group aligned with each Herdr workspace | `chromium` `coding-agents` `developer-tools` `hyprland` `linux` | 2 | 2026-10-19 |
| [**🆕 shelley-herdr**](https://github.com/webframp/shelley-herdr)<br><sub>webframp</sub> | Run exe.dev Shelley conversations as native herdr agents | `go` | 2 | 2026-10-10 |
| [**🆕 herdr-sim**](https://github.com/baleen37/herdr-sim)<br><sub>baleen37</sub> | Herdr plugin: show the PRs each Claude Code / Codex pane touched as sidebar icons | `claude-code` `codex` `rust` | 1 | 2026-10-23 |

[⬆ 返回目的列表](#purposes)

<a id="cat-notify"></a>

## 通知与提醒

> 即使离开座位，也想知道 Agent 何时完成或卡在等待输入

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**Heeler**](https://github.com/ZingerLittleBee/Heeler)<br><sub>ZingerLittleBee</sub> | 面向 herdr 的原生 iOS Agent 控制台——通过 SSH 查看并操控你机器上的编码 Agent，配备真正的 libghostty 终端、二维码配对，以及 Agent 需要你时的推送通知。 | `ai-agents` `apns` `coding-agents` `ios` `libghostty` | 661 | 🔄 2026-10-26 |
| [**herdr-ohmyzsh**](https://github.com/robbyrussell/herdr-ohmyzsh)<br><sub>robbyrussell</sub> | 面向 Herdr 的 Oh My Zsh 插件：在侧边栏显示耗时较长的命令、完成通知、shell 辅助工具，并可一键在所有闲置窗格中重新加载 Oh My Zsh。 | `oh-my-zsh` `zsh` `shell` | 86 | 2026-09-09 |
| [**herdr-focus-notify**](https://github.com/yankewei/herdr-focus-notify)<br><sub>yankewei</sub> | 面向 Herdr Agent 的可点击 macOS 通知。当 Agent 被阻塞或完成时发送原生提示通知；点击后将终端置于前台并聚焦到对应的 Herdr 窗格 | `alerter` `macos` `notifications` `productivity` `rust` | 31 | 🔄 2026-10-16 |
| [**herdr-terminal-notifier**](https://github.com/dot/herdr-terminal-notifier)<br><sub>dot</sub> | 通过 terminal-notifier 为 herdr Agent 状态变化发送可自定义的 macOS 通知 | `macos` `terminal-notifier` `shell` | 11 | 2026-09-07 |
| [**herdr-ntfy**](https://github.com/horn553/herdr-ntfy)<br><sub>horn553</sub> | 依赖极简（jq、curl、sh）——当 Herdr Agent 完成或被阻塞时发送 ntfy 通知 | `shell` | 9 | 2026-09-16 |
| [**herdr-pings**](https://github.com/joelhooks/herdr-pings)<br><sub>joelhooks</sub> | 面向 herdr 窗格中 AI Agent 的按轮次唤醒事件——pi 扩展、wait CLI、崩溃桥接，以及为你的 worker 起的 Discworld 风格代号 | `ai-agents` `pi` `typescript` | 9 | 2026-08-09 |
| [**herdr-ntfy-notify**](https://github.com/zom-2018/herdr-ntfy-notify)<br><sub>zom-2018</sub> | 面向 Herdr 终端 Agent 的实时 ntfy 推送通知 | `agent` `ntfy` `push-notifications` `tui` `javascript` | 8 | 2026-06-23 |
| [**herdr-hail**](https://github.com/natori-hrj/herdr-hail)<br><sub>natori-hrj</sub> | herdr 的 Slack 和 Discord 双向桥接——Agent 被阻塞时会收到提醒，回复或点击即可解除阻塞。无需内网穿透 | `discord` `slack` `typescript` | 7 | 2026-07-19 |
| [**herdr-telegram-plugin**](https://github.com/mvallebr/herdr-telegram-plugin)<br><sub>mvallebr</sub> | herdr 的 Telegram 机器人伴侣——通过 Telegram 论坛话题远程控制任意 Agent，整个流程中不涉及 LLM | `typescript` | 6 | 2026-08-31 |
| [**herdr-nudge**](https://github.com/justinchiasson/herdr-nudge)<br><sub>justinchiasson</sub> | Clickable macOS notifications for Herdr when an agent is blocked or done, or a long shell command finishes. Click one to jump to that exact pane. Nothing else… | `claude-code` `macos` `notifications` `notify` `zsh` | 5 | 2026-09-29 |
| [**herdr-announcer**](https://github.com/nhclink16/herdr-announcer)<br><sub>nhclink16</sub> | Herdr 插件：Agent 完成或需要输入时，用语音播报一句 LLM 生成的摘要——支持本地 TTS、ElevenLabs 或任意自定义命令 | `tts` `rust` | 5 | 2026-09-09 |
| [**herdr-notify-windows**](https://github.com/aclima01/herdr-notify-windows)<br><sub>aclima01</sub> | 面向 herdr Agent 的 Windows 11 提示通知（轮次完成/需要输入） | `powershell` | 4 | 2026-07-23 |
| [**herdr-cache-alert**](https://github.com/AltanS/herdr-cache-alert)<br><sub>AltanS</sub> | herdr 插件：在每个 Agent 窗格显示 prompt 缓存倒计时，并附带每条缓存规则的来源和日期 | `ai-agents` `ai-coding` `ai-tools` `claude-code` `multiplexing` | 4 | 2026-09-17 |
| [**herdr-telegram-bridge**](https://github.com/cokekitten/herdr-telegram-bridge)<br><sub>cokekitten</sub> | 当 herdr Agent 完成或被阻塞时收到 Telegram 推送——直接回复即可将文本或文件发回该 Agent。无需服务器、无需内网穿透、无需 App | `ai-agents` `chatops` `claude-code` `developer-tools` `notifications` | 4 | 2026-08-06 |
| [**session-sounds**](https://github.com/ChrisPachulski/session-sounds)<br><sub>ChrisPachulski</sub> | 面向 macOS 和 Linux 的 Herdr，为每个 Agent 提供不同的完成提示音和关注提示音 | `coding-agents` `notifications` `rust` | 3 | 2026-07-19 |
| [**agent-webhook-notify**](https://github.com/happyeric77/agent-webhook-notify)<br><sub>happyeric77</sub> | 当 Herdr Agent 完成或被阻塞时，发送 Webhook 通知 | `javascript` | 3 | 2026-08-12 |
| [**herdr-telegram-notify**](https://github.com/naturalmoods/herdr-telegram-notify)<br><sub>naturalmoods</sub> | Messages you on Telegram when an agent finishes or needs input, with its last message, changes, duration and cost. Answer from the chat with text, menu buttons… | `claude-code` `notifications` `telegram` `javascript` | 3 | 🔄 2026-10-13 |
| [**herdr-warp**](https://github.com/ProjectAJ14/herdr-warp)<br><sub>ProjectAJ14</sub> | 一个简单的插件，让 Herdr 可以通过 Warp 发送通知。 | `python` | 3 | 🔄 2026-10-15 |
| [**herdr-discord-presence**](https://github.com/revanp/herdr-discord-presence)<br><sub>revanp</sub> | herdr 插件：将 Herdr 会话和 Agent 状态显示为 Discord Rich Presence | `typescript` | 3 | 2026-08-14 |
| [**herdr-wsl-notify**](https://github.com/tkmct/herdr-wsl-notify)<br><sub>tkmct</sub> | 当运行在 WSL2 上的 Agent（如 Claude Code）完成或被阻塞（等待批准/输入）时，显示 Windows 桌面提示通知的 Herdr 插件 | `javascript` | 3 | 2026-08-27 |
| [**herdr-webhook-notify**](https://github.com/zgxme/herdr-webhook-notify)<br><sub>zgxme</sub> | 一个 Herdr 插件，将 Agent 通知转发到 Slack、Discord、Teams、Google Chat、飞书、Lark、钉钉、企业微信、Telegram、ntfy 或任意 HTTP webhook。 | `dingtalk` `discord` `feishu` `lark` `notifications` | 3 | 2026-09-21 |
| [**herdr-agent-notify**](https://github.com/A1exthegreat/herdr-agent-notify)<br><sub>A1exthegreat</sub> | herdr 插件：当 Agent 完成工作、需要确认或进入空闲状态时发送桌面通知 | `javascript` | 2 | 2026-08-15 |
| [**buzzr**](https://github.com/candypoets/buzzr)<br><sub>candypoets</sub> | 将运行中的 Herdr space 和 Agent 镜像到 Buzz 频道，并支持 Nostr 身份和提及路由 | `agents` `buzz` `nostr` `rust` | 2 | 2026-08-14 |
| [**herdr-telegram-slack-bridge**](https://github.com/lsisoft/herdr-telegram-slack-bridge)<br><sub>lsisoft</sub> | 面向 Herdr Agent 会话的 Telegram 与 Slack 机器人双向桥接——将被阻塞 Agent 的提醒和聊天回复路由回 Herdr 或 tmux 窗格 | `ai-agents` `slack-bot` `telegram-bot` `tmux` `python` | 2 | 2026-07-28 |
| [**herdr-guard**](https://github.com/StructuPath/herdr-guard)<br><sub>StructuPath</sub> | Herdr 的跨 Agent 命令策略：审计、警告并中断危险的 shell 命令 | `ai-agents` `command-policy` `security` `terminal` `javascript` | 2 | 2026-09-14 |
| [**herdr-oncall**](https://github.com/fulanto/herdr-oncall)<br><sub>fulanto</sub> | 通过浮动的 macOS 面板或 Telegram 回应编码 Agent 的权限确认提示——面向 Claude Code 和 Codex 的 Herdr 插件。 | `ai-agents` `claude-code` `cli` `codex` `coding-agent` | 1 | 🔄 2026-10-21 |
| [**🆕 herdr-gh-runs**](https://github.com/kkjdaniel/herdr-gh-runs)<br><sub>kkjdaniel</sub> | GitHub Actions runs in a herdr pane: follows your repo, live status, step logs and notifications | `gh` `github-actions` `terminal` `tui` `python` | 1 | 🔄 2026-10-22 |
| [**🆕 medley**](https://github.com/WebscapeOrg/medley)<br><sub>WebscapeOrg</sub> | Custom sounds for every herdr workspace and status | `audio` `notifications` `python` | 1 | 🔄 2026-10-23 |

[⬆ 返回目的列表](#purposes)

<a id="cat-remote"></a>

## 手机与远程操控

> 想在外出或用手机时监控 Agent，只需回传批准即可

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**🆕 ovis**](https://github.com/devswha/ovis)<br><sub>devswha</sub> | Ovis (formerly herdr web UI): free, open-source browser and phone client for herdr. Chat and live terminal for Claude Code, Codex and every agent pane, remote… | `agentic-coding` `ai-agents` `bun` `claude-code` `codex` | 1502 | 🔄 2026-10-26 |
| [**collie**](https://github.com/AltanS/collie)<br><sub>AltanS</sub> | Herdr mobile client for iPhone and Android. A self-hosted PWA to drive Claude Code, Pi, Codex and OpenCode in Herdr, tmux or zellij from your phone. Push alert… | `agent-orchestration` `ai` `ai-agents` `ai-coding` `ai-tools` | 1471 | 🔄 2026-10-25 |
| [**herdr-remote**](https://github.com/dcolinmorgan/herdr-remote)<br><sub>dcolinmorgan</sub> | 从菜单栏、手机或 Telegram 监控并操控你的 herdr Agent。本地零配置，远程连接提供免费内网穿透，无需 Tailscale | `macos` `mobile` `python` | 431 | 🔄 2026-10-23 |
| [**herdr-mobile-relay**](https://github.com/0cv/herdr-mobile-relay)<br><sub>0cv</sub> | 通过手机远程审批和监控 Herdr Agent——面向 Android/iOS 的移动 Web 应用，支持推送通知、二维码配置和多电脑中继 | `android` `approvals` `cloudflare` `ios` `mobile` | 318 | 🔄 2026-10-26 |
| [**pairfob**](https://github.com/arronKler/pairfob)<br><sub>arronKler</sub> | Your Herdr agents on your phone in one QR scan. Browser-first, optional Android beta, no Tailscale or ports, end-to-end encrypted. | `android` `apk` `claude-code` `codex` `herdr-mobile` | 178 | 🔄 2026-10-26 |
| [**herdr-telegram-agents**](https://github.com/permgps/herdr-telegram-agents)<br><sub>permgps</sub> | 像在终端里一样，从 Telegram 操控你的编码 Agent。每个 Agent 对应一个话题，话题图标实时显示状态，并通过带内联按钮的双向聊天进行选择。 | `claude-code` `coding-agents` `go` `telegram` `telegram-bot` | 83 | 🔄 2026-10-24 |
| [**termote**](https://github.com/lamngockhuong/termote)<br><sub>lamngockhuong</sub> | Self-hosted PWA to control Claude Code, Codex, GitHub Copilot or any terminal from your phone or desktop. Single Go binary streaming tmux/psmux/Herdr sessions… | `ai-coding-agent` `claude-code` `cli` `codex` `github-copilot` | 67 | 🔄 2026-10-26 |
| [**herdrchat**](https://github.com/cobanov/herdrchat)<br><sub>cobanov</sub> | 从手机操控你的 herdr 编码 Agent。已在 App Store 上架，支持 iPhone 和 iPad。 | `app-store` `herdr-client` `herdr-integration` `herdr-mobile` `ios` | 32 | 🔄 2026-10-26 |
| [**herdr-watch**](https://github.com/Unayung/herdr-watch)<br><sub>Unayung</sub> | 在 Apple Watch 上查看 herdr 的 Agent 状态 | `javascript` | 31 | 2026-08-14 |
| [**herdr-connect**](https://github.com/Tomyail/herdr-connect)<br><sub>Tomyail</sub> | 通过这款 iPhone 移动伴侣应用监控并操控你的 Herdr AI 编码 Agent——查看输出、发送后续指令，并在任务完成时收到通知。通过局域网或 Tailscale 私密运行，无需云端，也无需账号。 | `agent` `mobile-app` `react-native` `typescript` | 20 | 🔄 2026-10-24 |
| [**herdr-call**](https://github.com/eliasstravik/herdr-call)<br><sub>eliasstravik</sub> | 面向 Herdr 的语音控制 | `elevenlabs` `tailscale` `voice` `typescript` | 16 | 2026-08-07 |
| [**vscode-devcontainers-herdr**](https://github.com/scott-the-programmer/vscode-devcontainers-herdr)<br><sub>scott-the-programmer</sub> | 面向运行在 dev container 内的 Agent 的 Herdr 中继 | `container` `devcontainer` `rust` | 15 | 🔄 2026-10-25 |
| [**herdr-web**](https://github.com/barnuri/herdr-web)<br><sub>barnuri</sub> | 面向 herdr 的移动优先 Web UI 插件——从手机驱动你的编程 Agent，并带有通知功能 | `pwa` `typescript` | 13 | 🔄 2026-10-22 |
| [**herdr-office**](https://github.com/michaellandi/herdr-office)<br><sub>michaellandi</sub> | 一个 Herdr 插件，将你的 Agent 绘制成开放式办公室里的人物。当需要审批时，他们会举手示意。 | `javascript` | 12 | 2026-10-05 |
| [**herdr-plugin-mobile-relay**](https://github.com/benkraus/herdr-plugin-mobile-relay)<br><sub>benkraus</sub> | _(暂无描述)_ | `typescript` | 11 | 2026-08-12 |
| [**herdr-push**](https://github.com/dcolinmorgan/herdr-push)<br><sub>dcolinmorgan</sub> | herdr 插件：零依赖地将事件推送到 herdr-remote，用于手机端监控和一键批准 | `shell` | 10 | 2026-07-09 |
| [**wherdr**](https://github.com/afloury/wherdr)<br><sub>afloury</sub> | Use Herdr from anywhere — your iPhone, Android phone or any browser. Watch your coding agents, answer them and run your herdr-projects, privately and securely. | `ai-agents` `claude-code` `codex` `mobile` `pwa` | 9 | 🔄 2026-10-26 |
| [**herdr-go**](https://github.com/herdr-go/herdr-go)<br><sub>herdr-go</sub> | 从任何地方控制你的 herdr 编程 Agent——私密、点对点，并通过 EasyTier 加密保护 | `dart` | 8 | 2026-09-08 |
| [**paddock**](https://github.com/lntvan166/paddock)<br><sub>lntvan166</sub> | 面向 herdr 的移动优先仪表盘——读取其 unix socket。无需任何配置即可在手机上运行 | `agent-orchestration` `coding-agents` `herdr-mobile` `paddock` `pwa` | 8 | 🔄 2026-10-26 |
| [**muqun-gateway**](https://github.com/osuki-dev/muqun-gateway)<br><sub>osuki-dev</sub> | 让 Muqun 能够访问你自己电脑上终端的程序。它运行在你的机器上，与 tmux 或 Herdr 通信，并直接响应你的手机——中间没有账号，也没有我们的服务器 | `rust` | 7 | 🔄 2026-10-26 |
| [**herdr-remote-panes**](https://github.com/Poor-Plebs/herdr-remote-panes)<br><sub>Poor-Plebs</sub> | 从一个 Herdr 操作其他机器——从菜单中选择一台机器，即可获得该机器上的终端。还可选启用实验性的双向镜像 | `golang` `ssh` `terminal` `go` | 7 | 2026-09-11 |
| [**herdr-mobile**](https://github.com/bsorescu/herdr-mobile)<br><sub>bsorescu</sub> | 通过 SSH 控制 Herdr 编程 Agent 的手机友好型 TUI | `mobile` `ssh` `textual` `tui` `python` | 6 | 2026-08-25 |
| [**herdr-web**](https://github.com/eyalev/herdr-web)<br><sub>eyalev</sub> | 面向 herdr Agent 多路复用器的移动优先 Web UI——从手机操控你的编程 Agent | `claude-code` `mobile` `pwa` `terminal` `javascript` | 6 | 2026-07-29 |
| [**merino**](https://github.com/LoneExile/merino)<br><sub>LoneExile</sub> | Merino 🐑——面向 Herdr Agent 的远程隧道仪表盘 | `go` `macos` `menubar` `react` `wails` | 6 | 2026-09-21 |
| [**arcdr**](https://github.com/arcnessai/arcdr)<br><sub>arcnessai</sub> | herdr mobile & web client that shows what your Claude Code mods report — answer your agents from your phone, over your own Tailscale | `ai-agents` `bun` `claude-code` `claude-code-mods` `coding-agents` | 5 | 🔄 2026-10-19 |
| [**herdr-phone**](https://github.com/matheus3301/herdr-phone)<br><sub>matheus3301</sub> | 通过 Cloudflare Tunnel 和 Access 实现的 Herdr 移动端远程控制台 | `cloudflare-tunnel` `coding-agents` `developer-tools` `golang` `mobile` | 5 | 🔄 2026-10-16 |
| [**herdr-tether**](https://github.com/mcc0x/herdr-tether)<br><sub>mcc0x</sub> | Keep local and remote terminal workloads running after their Herdr view closes. | `remote-development` `rust` `ssh` `terminal` `tmux` | 5 | 🔄 2026-10-16 |
| [**herdr-portfwd**](https://github.com/miko-misa/herdr-portfwd)<br><sub>miko-misa</sub> | 面向远程机器上编程 Agent 的自动 SSH 端口转发——Ctrl+点击 Agent 打印的 localhost URL，即可在你本机以相同端口打开该页面。一个 Herdr 插件 | `ai-agents` `claude-code` `cli` `coding-agents` `developer-tools` | 5 | 🔄 2026-10-11 |
| [**herdweb**](https://github.com/zlxlabs/herdweb)<br><sub>zlxlabs</sub> | 在手机上监控并操控你的编码 Agent。支持语音输入、粘贴图片、Webhook 通知，以及多设备/多服务器。 | `typescript` | 5 | 🔄 2026-10-20 |
| [**herdr-aws-ssm**](https://github.com/maayanyosef/herdr-aws-ssm)<br><sub>maayanyosef</sub> | 在 herdr --remote 会话中选择一个 EC2 实例并通过 AWS SSM 连接——无需跳板机或公网 IP | `aws-ssm` `terminal` `shell` | 4 | 2026-07-01 |
| [**herdr-farm**](https://github.com/mejiasd3v/herdr-farm)<br><sub>mejiasd3v</sub> | Herdr 插件：将你的 Herdr 工作区和 Agent 可视化为牲畜的 3D 农场（three.js 网页应用） | `threejs` `javascript` | 4 | 2026-07-28 |
| [**herdr-mobile-app**](https://github.com/teasec4/herdr-mobile-app)<br><sub>teasec4</sub> | 原生伴侣应用 + 轻量级 Go 中继：将 Agent 终端输出实时推送到手机，可查看状态并发送提示词——支持通过局域网、Tailscale 或 Funnel 连接。 | `ai` `devtools` `flutter` `herdr-integration` `herdr-mobile` | 4 | 2026-09-05 |
| [**herdr-whistle**](https://github.com/amurru/herdr-whistle)<br><sub>amurru</sub> | 用于远程管理 Agent 的 Herdr 插件 | `golang` `telegrambot` `go` | 3 | 2026-08-06 |
| [**herdr-remote**](https://github.com/dibin666/herdr-remote)<br><sub>dibin666</sub> | 通过浏览器远程访问你的 Herdr 终端工作区。 | `claude-code` `codex` `pi` `vibe-coding` `typescript` | 3 | 🔄 2026-10-24 |
| [**herdr-telegram-gate**](https://github.com/hkdom/herdr-telegram-gate)<br><sub>hkdom</sub> | 面向 herdr AI Agent 群体的 Telegram 审批收件箱 + 按风险分级的自动批准——被阻塞的 Agent 会以带批准/拒绝按钮的 Telegram 卡片形式呈现（零依赖的 Node.js） | `approval-gate` `telegram` `javascript` | 3 | 2026-08-06 |
| [**lerdr-rust-kotlin**](https://github.com/IGUNUBLUE/lerdr-rust-kotlin)<br><sub>IGUNUBLUE</sub> | 面向 Herdr 的 Rust 中继服务 + Kotlin/Jetpack Compose Android 应用：通过 Tailscale 实现端到端加密的 Agent 会话。这是受 0cv/herdr-mobile-relay 启发、由 AI 生成的重新实现（使用 Cognition 的 SWE-2 构建）。测试版。 | `ai-generated` `android` `e2ee` `jetpack-compose` `kotlin` | 3 | 🔄 2026-10-21 |
| [**herdr-remotedownloder**](https://github.com/kosuketut/herdr-remotedownloder)<br><sub>kosuketut</sub> | 将文件从远程 Herdr 窗格下载到已连接的 Mac | `developer-tools` `file-transfer` `macos` `rust` `ssh` | 3 | 🔄 2026-10-23 |
| [**herdr-mobile-pro**](https://github.com/spad-0x/herdr-mobile-pro)<br><sub>spad-0x</sub> | 一款高性能、移动优先的 PWA 仪表盘，采用 Cyber-Dark 设计风格，可直接从智能手机编排 Herdr 与自主 AI Agent。具备安全 HTTPS、语音听写输入、图片上传，以及将终端输出实时语义解析为聊天式界面的能力。 | `javascript` | 3 | 2026-09-12 |
| [**herdr-devup**](https://github.com/alon-z/herdr-devup)<br><sub>alon-z</sub> | Herdr 插件：根据 .herdr/dev.toml 生成每个项目的开发布局，并同步隧道 URL 到环境变量 | `typescript` | 2 | 2026-06-22 |
| [**herdr-topbar**](https://github.com/bigbug16/herdr-topbar)<br><sub>bigbug16</sub> | 面向 herdr 的 macOS 菜单栏图标——可跳回会话、打开项目，并查看哪个 Agent 正在等待输入 | `macos` `menubar` `swift` | 2 | 2026-08-24 |
| [**setnet**](https://github.com/chano-gpt/setnet)<br><sub>chano-gpt</sub> | 从手机管理多种 harness 的编程 Agent——一个 Herdr 插件 | `typescript` | 2 | 2026-08-29 |
| [**community**](https://github.com/fab-agent/community)<br><sub>fab-agent</sub> | Put your teammates next to your agents: members, departments, tasks and direct messages inside Herdr. | `ai-agents` `chatinterface` `cloudflare-workers` `community` `terminal-chat` | 2 | 🔄 2026-10-15 |
| [**shahi**](https://github.com/iYassr/shahi)<br><sub>iYassr</sub> | Use Claude Code, Codex, Cursor CLI, OpenCode and Antigravity from your phone. A herdr plugin with iPhone and web apps: read agent conversations, answer permiss… | `ai-agents` `antigravity` `claude-code` `codex` `coding-agents` | 2 | 🔄 2026-10-23 |
| [**herdr-reach**](https://github.com/Luisalt20/herdr-reach)<br><sub>Luisalt20</sub> | 面向 Herdr 远程主机的只读网络诊断工具：实测你的网络实际允许的连接方式，并基于证据推荐合适的传输方案。不进行写入操作，也不使用第三方二进制文件。 | `cli` `cloudflare-tunnel` `connectivity` `egress` `go` | 2 | 2026-09-21 |
| [**🆕 instinct-herdr-tunnel**](https://github.com/romiluz13/instinct-herdr-tunnel)<br><sub>romiluz13</sub> | Let an AI assistant such as Instinct watch and steer your Herdr coding agents: a loopback portal with a 26-action allowlist, a bearer token and an audit log, p… | `ai-agents` `cloudflare-tunnel` `coding-agents` `nodejs` `javascript` | 2 | 🔄 2026-10-25 |
| [**herdr-web-tui**](https://github.com/tigorlazuardi/herdr-web-tui)<br><sub>tigorlazuardi</sub> | 以守护进程为核心的 Herdr 浏览器/PWA 前端，附带可选的插件启动器 | `go` | 2 | 2026-10-01 |
| [**herdr-hub**](https://github.com/alex-devdone/herdr-hub)<br><sub>alex-devdone</sub> | 将由远程连接窗格组成的 herdr 会话描述为可移植的清单文件，并可在任意机器上重建 | `python` | 1 | 2026-08-23 |
| [**sightr**](https://github.com/bartholomewtj/sightr)<br><sub>bartholomewtj</sub> | Sightr——通过 Tailscale，为 Herdr 的 Agent 群提供手机网页 UI。 | `typescript` | 1 | 🔄 2026-10-22 |
| [**herdr-amp-orbs**](https://github.com/BlockedPath/herdr-amp-orbs)<br><sub>BlockedPath</sub> | Herdr plugin: run Amp orbs (remote Amp agents) in Herdr panes | `amp` `shell` | 1 | 🔄 2026-10-26 |
| [**herdr-vps-local**](https://github.com/yavuzhansarmaz/herdr-vps-local)<br><sub>yavuzhansarmaz</sub> | 在远程主机上获得如本地般的操作体验：通过 Mutagen 将 VPS/Pi 上的仓库镜像到你的笔记本电脑。 | `rust` | 1 | 2026-09-28 |
| [**🆕 HerdRabbit**](https://github.com/ultivis-iot/HerdRabbit)<br><sub>ultivis-iot</sub> | Open your Herdr sessions from a phone or another PC (PWA over Tailscale). | `javascript` | 0 | 🔄 2026-10-26 |

<details><summary>与此目的也相关</summary>

- [powerfooI/roamgate](https://github.com/powerfooI/roamgate) — 适用于任意屏幕的 Herdr 客户端。可在桌面或移动设备上控制终端、监控编码 Agent，并查看文件与差异。

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-agents"></a>

## Agent 编排与并行执行

> 想统一启动、分工并管理多个 AI Agent

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**oh-my-opencode-slim**](https://github.com/alvinunreal/oh-my-opencode-slim)<br><sub>alvinunreal</sub> | 精简且经过调优的 Opencode 多 Agent 套件 · 可混用任意模型 · 自动委派任务 | `agentic-ai` `oh-my-opencode` `opencode` `orchestration` `typescript` | 9807 | 🔄 2026-10-25 |
| [**herdr-projects**](https://github.com/eliasstravik/herdr-projects)<br><sub>eliasstravik</sub> | Mission control for Herdr: run dozens of coding agents from one board. Each works on its own branch, a second agent reviews it, and you see what needs you. | `rust` | 892 | 🔄 2026-10-23 |
| [**agentbox**](https://github.com/madarco/agentbox)<br><sub>madarco</sub> | 一条命令即可在沙盒虚拟机中并行运行多个 Agent（本地或云端） | `claude` `claude-code` `cli` `cmux` `codex` | 558 | 2026-10-07 |
| [**pi-workflows**](https://github.com/osolmaz/pi-workflows)<br><sub>osolmaz</sub> | 面向 pi 编程 Agent 的工作流引擎、JSON 控制流工具与实时终端查看器 | `typescript` | 349 | 2026-10-08 |
| [**pi-extensible-workflows**](https://github.com/vekexasia/pi-extensible-workflows)<br><sub>vekexasia</sub> | Deterministic multi-agent workflow orchestration and codemode scripts for Pi | `codemode` `pi` `workflow` `workflows` `typescript` | 248 | 🔄 2026-10-25 |
| [**herdr-board**](https://github.com/nelsonPires5/herdr-board)<br><sub>nelsonPires5</sub> | herdr 的看板工具——卡片就是提示词，会被派发给可见窗格中的 AI Agent | `board` `kanban` `kanban-board` `tui` `rust` | 183 | 🔄 2026-10-18 |
| [**herdr-dagr**](https://github.com/aemrebarut/herdr-dagr)<br><sub>aemrebarut</sub> | 将 Agent 集群实时呈现为 DAG——在 herdr 分屏窗格中展示包含尝试记录、评审关卡和证据的编排图 | `agents` `dag` `multi-agent` `orchestration` `rust` | 125 | 2026-08-23 |
| [**agent-router**](https://github.com/nidhi-singh02/agent-router)<br><sub>nidhi-singh02</sub> | 一款 CLI 工具，会为任务选择 Cursor、Claude Code、Codex 或 OpenCode 及对应的模型/工作强度，并启动它。基于 Jev 和 Herdr 构建。 | `agents` `ai` `claude-code` `cli` `codex` | 118 | 2026-09-27 |
| [**herdr-file-annotator**](https://github.com/JonasBaeumer/herdr-file-annotator)<br><sub>JonasBaeumer</sub> | 在不脱离实际代码库的前提下，最大化 Agent 化开发效率的 herdr 插件 | `rust` | 63 | 2026-10-07 |
| [**proqi**](https://github.com/oborchers/proqi)<br><sub>oborchers</sub> | 一款面向同时运行多个编码 Agent 的高级用户的终端原生 prompt 编写工具。 | `ai-agents` `claude-code` `cli` `coding-agents` `developer-tools` | 43 | 🔄 2026-10-25 |
| [**agentbox-herdr-plugin**](https://github.com/madarco/agentbox-herdr-plugin)<br><sub>madarco</sub> | 一条命令即可在沙盒虚拟机中并行运行多个 Agent（本地或云端） | `claude-code` `codex-cli` `opencode` `sandbox` `shell` | 34 | 2026-06-24 |
| [**entwurf**](https://github.com/junghan0611/entwurf)<br><sub>junghan0611</sub> | Open visible sibling AI sessions in Herdr or tmux, reopen pi sessions in tmux under the same garden id, and exchange messages across pi, pi-durable, Claude Cod… | `acp` `agent-collaboration` `agent-communication` `agent-to-agent` `ai-agents` | 31 | 🔄 2026-10-26 |
| [**herdr-browser**](https://github.com/StructuPath/herdr-browser)<br><sub>StructuPath</sub> | Herdr 的可操控 Agent 浏览器窗格——支持实时流传输、真实交互、自适应渲染、控制台/页面错误显示、录制和 localhost 路由 | `terminal` `javascript` | 31 | 2026-10-10 |
| [**herdr-voice**](https://github.com/brogrammerMW/herdr-voice)<br><sub>brogrammerMW</sub> | 与 Herdr 窗格中的编码 Agent 对话，并通过 Grok、OpenAI 或 Gemini 以实时语音听到它们的回答。 | `macos` `voice` `swift` | 29 | 2026-09-26 |
| [**termaxa**](https://github.com/termaxa/termaxa)<br><sub>termaxa</sub> | Agent 的 prompt 会告诉你即将执行的命令，而 Termaxa 会告诉你其后果。提供预览、备份、策略与审计记录。支持 Claude Code、Codex、Cursor、Copilot。它是一块「挡风玻璃」，而非沙盒。 | `agent-safety` `ai-agents` `claude-code` `cli` `developer-tools` | 27 | 🔄 2026-10-23 |
| [**herdmates**](https://github.com/caioniehues/herdmates)<br><sub>caioniehues</sub> | herdr 原生的 Claude Code Agent 团队——teammux 兼容层、任务控制面板、聚焦窗格 | `agent-teams` `claude-code` `rust` `tui` | 26 | 2026-08-21 |
| [**herdr-world**](https://github.com/IvoryHeart/herdr-world)<br><sub>IvoryHeart</sub> | Herdr World — visualize agent work in Office, Tree, Graph, and Spaces; control Herdr agents across local and SSH hosts. | `agent-runtime` `agent-visualization` `coding-agents` `multi-agent` `observability` | 26 | 🔄 2026-10-26 |
| [**pi-herd**](https://github.com/ribbons-digital/pi-herd)<br><sub>ribbons-digital</sub> | 结合 Herdr 窗格和 git 工作树，对 Pi 会话进行可视化编排 | `typescript` | 23 | 2026-07-06 |
| [**herdr-agent-handoff**](https://github.com/sanirudh17/herdr-agent-handoff)<br><sub>sanirudh17</sub> | 将进行中的 Agent 会话交接给另一个已安装编程 Agent 的新会话的 Herdr 插件——完整会话直接放入提示词中传递，无需摘要、无需截断记录、无需再写后续提示 | `agent-handoff` `claude-code` `codex` `coding-agents` `developer-tools` | 22 | 2026-09-30 |
| [**PromptPilot**](https://github.com/ivanarama/PromptPilot)<br><sub>ivanarama</sub> | 面向 Claude Code 及其他 AI CLI 的后台任务队列——配有网页 UI 和 Telegram 机器人 | `ai-agents` `claude-code` `telegram-bot` `python` | 20 | 🔄 2026-10-21 |
| [**herdr-vercel-sandbox-plugin**](https://github.com/vercel-labs/herdr-vercel-sandbox-plugin)<br><sub>vercel-labs</sub> | 从 Herdr 在隔离的 Vercel Sandbox 中运行基于终端的编程 Agent | `javascript` | 15 | 2026-08-09 |
| [**herdr-social-glass**](https://github.com/ythx-101/herdr-social-glass)<br><sub>ythx-101</sub> | 面向 macOS 版 Herdr 的、适合截图分享的 Social Glass 主题与工作流插件 | `macos` `multi-agent` `terminal-theme` `shell` | 14 | 2026-08-21 |
| [**herdr-catchup**](https://github.com/wilbeibi/herdr-catchup)<br><sub>wilbeibi</sub> | herdr 的跨 Agent 编程会话交接：从正在运行的窗格中，对 Claude Code、Codex、Cursor、Cline 或 OpenCode 会话进行摘要、分叉，或转交给另一个 Agent | `ai-agents` `claude-code` `codex` `coding-agents` `context-handoff` | 12 | 2026-09-28 |
| [**deevs-pi-kit**](https://github.com/DeevsDeevs/deevs-pi-kit)<br><sub>DeevsDeevs</sub> | 完美的 pi 工具包，让 Deevs 的工程师效率提升 10 倍。 | `agents` `pi` `pi-agent` `pi-extension` `pi-package` | 11 | 2026-10-08 |
| [**agys**](https://github.com/quaywin/agys)<br><sub>quaywin</sub> | 通过零污染沙盒，为 Herdr 中的 Antigravity CLI 提供轻松的多配置文件隔离和实时配额追踪 | `ai-agents` `antigravity` `cli` `context-window` `developer-tools` | 11 | 2026-09-26 |
| [**vibetty**](https://github.com/second-state/vibetty)<br><sub>second-state</sub> | 通过 MQTT 将 AI Agent 终端实时共享给智能硬件（vibekeys、vibewatch 等），也可作为 Herdr 插件使用 | `claude-code` `codex` `vibecoding` `rust` | 11 | 🔄 2026-10-15 |
| [**herdr-swarm**](https://github.com/StructuPath/herdr-swarm)<br><sub>StructuPath</sub> | 在同一仓库上安全并行运行多个编程 Agent：为每个 Agent 分配独立工作树，实时可见变更，Herdr 上以审查优先的方式收获成果 | `terminal` `javascript` | 11 | 🔄 2026-10-15 |
| [**shepherdr**](https://github.com/afogel/shepherdr)<br><sub>afogel</sub> | 将委派出去的编程 Agent 收拢到可见、可审查的 herdr 窗格中，供你观察、恢复和接管的 herdr 插件 | `ai-agents` `claude-code` `codex` `cursor` `rust` | 10 | 2026-07-24 |
| [**herdr-devcontainer**](https://github.com/gambtho/herdr-devcontainer)<br><sub>gambtho</sub> | 通过官方 Dev Containers CLI，在仓库的 Dev Container 内打开 shell 和编程 Agent 的 Herdr 插件 | `coding-agents` `containers` `devcontainers` `developer-tools` `development-environment` | 10 | 2026-08-13 |
| [**herdr-recap**](https://github.com/mrolafsson/herdr-recap)<br><sub>mrolafsson</sub> | Come back to a bunch of agents and know in seconds which ones need you. A herdr popup that tells you, per agent, where it got to (a recap written while you wer… | `bubbletea` `claude-code` `codex` `coding-agents` `go` | 10 | 🔄 2026-10-21 |
| [**herdr-agent-messenger**](https://github.com/aashishd/herdr-agent-messenger)<br><sub>aashishd</sub> | 让运行中的 Herdr 窗格间的 AI Agent 互相发送简明、自成一体的消息——一个 Agent 可以在不共享完整上下文的情况下与另一个协调工作 | `python` | 9 | 2026-10-09 |
| [**herdr-plugin-odysseus**](https://github.com/jpolec/herdr-plugin-odysseus)<br><sub>jpolec</sub> | 面向 Herdr 的受治理多 Agent 工作流：任务 → Herdr 窗格中的 Agent → 检查、重试、评审、策略、审批、审计、草拟 PR。 | `ai-agents` `rust` | 9 | 2026-09-25 |
| [**spoolway**](https://github.com/marvingygas/spoolway)<br><sub>marvingygas</sub> | Minimalistic agent state machine for software development: a retro TUI dispatcher that drives agent sessions through defined pipelines | `agent` `cli` `descriptive` `llm` `pipeline` | 9 | 🔄 2026-10-26 |
| [**herdr-helpr**](https://github.com/sohanemon/herdr-helpr)<br><sub>sohanemon</sub> | 面向 herdr 的、由提示词驱动的工作区和窗格管理 | `ai-agents` `bun` `cli` `developer-tools` `ink` | 9 | 🔄 2026-10-22 |
| [**awp**](https://github.com/agentwireprotocol/awp)<br><sub>agentwireprotocol</sub> | Peer-to-peer messaging for AI coding agents: delegate tasks, share files, track state across Claude Code, Codex, Cursor, OpenCode, Pi and more. | `agent-orchestration` `agents` `protcol` `go` | 8 | 2026-09-29 |
| [**herdr-sbx-plugin**](https://github.com/dirien/herdr-sbx-plugin)<br><sub>dirien</sub> | 在 Docker Sandboxes（sbx）中运行编码 Agent 的 Herdr 插件，每个 Agent 对应一个 microVM。 | `coding-agents` `docker-sandboxes` `javascript` | 8 | 2026-09-13 |
| [**namedrop**](https://github.com/ericbust/namedrop)<br><sub>ericbust</sub> | @mentions for Codex, Claude Code, and your terminal. A Herdr plugin that lets agents in different panes work together. | `agent-collaboration` `ai-agents` `claude-code` `cli` `codex` | 8 | 🔄 2026-10-26 |
| [**herdr-space-scoped-agents**](https://github.com/ShankyJS/herdr-space-scoped-agents)<br><sub>ShankyJS</sub> | 将 Agent 面板范围限定为当前聚焦空间的 herdr 插件 | `coding-agents` `terminal` `go` | 8 | 2026-07-23 |
| [**🆕 herduck**](https://github.com/wenhanweime/herduck)<br><sub>wenhanweime</sub> | Agent window management, project visibility, and a global conversation library. Built on Herdr for people and Agents. | `ai-agents` `claude-code` `codex` `coding-agents` `rust` | 8 | 🔄 2026-10-26 |
| [**pet-town**](https://github.com/abhishek944/pet-town)<br><sub>abhishek944</sub> | 一个透明的桌面小镇，住着你正在运行的 Herdr Agent。 | `javascript` | 7 | 🔄 2026-10-23 |
| [**herdr-orchestrate**](https://github.com/darjss/herdr-orchestrate)<br><sub>darjss</sub> | 为可见的 Herdr worker 会话提供 Pi 原生编排——运行看板、持久化的提示词/报告/状态、独立的 git 工作树，以及明确的模型路由 | `pi-package` `typescript` | 7 | 2026-07-13 |
| [**AgentRadio**](https://github.com/detailles/AgentRadio)<br><sub>detailles</sub> | 面向运行在 Herdr 窗格中的 AI 编码 Agent 的本地消息总线——支持加入、私信、在线状态与离线消息投递。 | `agent-orchestration` `multi-agent` `radio` `python` | 7 | 2026-09-27 |
| [**agent-panel**](https://github.com/flowy11/agent-panel)<br><sub>flowy11</sub> | herdr plugin: a side panel for your Claude Code or Codex session, its subagents, messages, refs and to-dos | `claude-code` `codex` `javascript` | 7 | 2026-09-29 |
| [**pier**](https://github.com/July24/pier)<br><sub>July24</sub> | Pi 是编程 Agent 的载体，Herdr 是终端工作区管理器。pier 补上了 pi 刻意省略的两项能力——todo 列表循环和可交互的子 Agent——并将 herdr 的窗格/标签页层作为它们的视觉与交互基础 | `pi-coding-agent` `typescript` | 7 | 🔄 2026-10-23 |
| [**chatter**](https://github.com/marcvermeeren/chatter)<br><sub>marcvermeeren</sub> | Chatter 是一次跨 harness 的 Agent 协作实验——为在 Herdr 中处理同一 Git 仓库的多个 Agent 提供共享群聊和上下文层 | `agent-collaboration` `agentic-ai` `agentic-workflow` `ai-agents` `group-chat` | 7 | 2026-08-18 |
| [**herdr-triage**](https://github.com/natori-hrj/herdr-triage)<br><sub>natori-hrj</sub> | herdr 的关注度分级——按谁最需要你来排序 Agent；长时间被阻塞的 Agent 会排到最前面 | `ai-agents` `triage` `rust` | 7 | 2026-07-23 |
| [**herdr-fleet**](https://github.com/Northern-Lighthouse/herdr-fleet)<br><sub>Northern-Lighthouse</sub> | 通过 Tailscale 管理一批 herdr 机器——仪表盘插件、自动发现、感知容量的 Agent 派发、无盘工作区 | `ai-agents` `tailscale` `python` | 7 | 2026-08-14 |
| [**herdr-scuttlebutt**](https://github.com/andybarilla/herdr-scuttlebutt)<br><sub>andybarilla</sub> | 为 herdr 会话中的 Agent 提供共享聊天室的 herdr 插件 | `rust` | 6 | 2026-09-22 |
| [**herdr-pane-topic-sync**](https://github.com/danbuhler/herdr-pane-topic-sync)<br><sub>danbuhler</sub> | herdr 插件：将窗格和标签页自动命名为每个 Agent（Claude Code、Codex 等）实时的主题，而不是「1」「2」「3」 | `ai-agents` `claude-code` `terminal` `tmux-alternative` `javascript` | 6 | 2026-09-02 |
| [**herdr-orchestrator**](https://github.com/kylezk777/herdr-orchestrator)<br><sub>kylezk777</sub> | Herdr-orch 是运行在 Herdr 之上的基于文件的 Agent 编排工具 | `agent-orchestration` `orchestrator` `rust` | 6 | 2026-07-26 |
| [**herdr-birdseye**](https://github.com/calebcauthon/herdr-birdseye)<br><sub>calebcauthon</sub> | 以鸟瞰视角查看 herdr 中的 Agent | `rust` | 5 | 2026-07-24 |
| [**herdr-loop**](https://github.com/cyperx84/herdr-loop)<br><sub>cyperx84</sub> | 面向 herdr 的声明式、事件驱动的循环与图编排——同时运行 Claude Code、Codex、opencode 和 pi，直到工作收敛 | `ai-agents` `golang` `orchestration` `go` | 5 | 2026-09-10 |
| [**herdr-openclaw**](https://github.com/gejiliang/herdr-openclaw)<br><sub>gejiliang</sub> | herdr 插件：将 OpenClaw 的 TUI 窗格作为一等公民的 herdr Agent 来管理 | `openclaw` `terminal` `javascript` | 5 | 2026-08-13 |
| [**herdr-espresso**](https://github.com/Hanyang-Li/herdr-espresso)<br><sub>Hanyang-Li</sub> | 在 Agent 运行时，即使合上盖子也保持 MacBook 唤醒状态 | `rust` | 5 | 2026-10-10 |
| [**herdr-gamepad**](https://github.com/htlin222/herdr-gamepad)<br><sub>htlin222</sub> | 用游戏手柄操控 Herdr。窝在沙发上巡视你的 AI Agent、拆分窗格、切换工作区——任意手柄，60 秒内自定义按键映射 | `ai-agents` `gamepad` `macos` `swift` `terminal-multiplexer` | 5 | 2026-09-09 |
| [**herdr-walkietalkie**](https://github.com/jeffory/herdr-walkietalkie)<br><sub>jeffory</sub> | herdr 插件：token 高效的跨 Agent 委派（wt）——编排 Agent 在标签页或工作树中派生出 Claude/OpenCode/Antigravity 的 worker | `shell` | 5 | 🔄 2026-10-14 |
| [**herdr-nono-plugin**](https://github.com/schemaitat/herdr-nono-plugin)<br><sub>schemaitat</sub> | Herdr plugin that runs coding agents (OpenCode) in nono sandboxes: sandboxed server and client, localhost locked down, verified via /proc | `rust` | 5 | 2026-10-10 |
| [**herdr-worker-orchestrator**](https://github.com/anhnd3005-infinity/herdr-worker-orchestrator)<br><sub>anhnd3005-infinity</sub> | 通过 Herdr 管理的窗格，将任务派发给 CLI Agent worker（agy、codex 等）——支持有状态的任务追踪、工作树隔离和基于差异的评审。同时适用于 Claude Code 和 Herdr 的双用插件 | `html` | 4 | 2026-08-25 |
| [**herdr-blueprint**](https://github.com/chappse6/herdr-blueprint)<br><sub>chappse6</sub> | Your coding agent explains its work as diagrams, right next to the chat. A herdr plugin for Claude Code and Codex. | `ai-agents` `claude-code` `codex` `markdown` `mermaid` | 4 | 🔄 2026-10-12 |
| [**herdr-desktop-pet**](https://github.com/hanbong5938/herdr-desktop-pet)<br><sub>hanbong5938</sub> | Native macOS desktop companion for Herdr with Rubelia, session activity, and agent messaging | `desktop-pet` `macos` `rust` | 4 | 🔄 2026-10-19 |
| [**herdr-pets**](https://github.com/hmu332233/herdr-pets)<br><sub>hmu332233</sub> | macOS desktop pets for Herdr agents that come find you when an agent is blocked. | `desktop-pet` `swift` | 4 | 🔄 2026-10-25 |
| [**herdr-a2a**](https://github.com/IsaiasZc/herdr-a2a)<br><sub>IsaiasZc</sub> | 通过 A2A 为 Herdr 提供的可靠 Agent 间委派层 | `typescript` | 4 | 2026-08-27 |
| [**herdr-huddle**](https://github.com/ivolkoff/herdr-huddle)<br><sub>ivolkoff</sub> | herdr plugin: agents ask rich questions as a page over their pane and get JSON back | `javascript` | 4 | 2026-10-07 |
| [**herdr-newtab-plus**](https://github.com/jeffarese/herdr-newtab-plus)<br><sub>jeffarese</sub> | 会询问文件夹和 Agent 的 Herdr 新标签页：自动补全真实路径，记住你常用的工作目录，并为你启动 Agent | `rust` | 4 | 🔄 2026-10-24 |
| [**herdr-prompt-library**](https://github.com/jwkicklighter/herdr-prompt-library)<br><sub>jwkicklighter</sub> | 用于浏览、管理并将可复用的本地或全局 Markdown 提示词插入到聚焦窗格中的 Herdr 插件 | `go` `golang` `prompting` `snippets` `tui` | 4 | 🔄 2026-10-16 |
| [**herdr-math**](https://github.com/liambern/herdr-math)<br><sub>liambern</sub> | 在 Herdr 终端窗格中渲染 LaTeX 显示公式，并提供与 harness 无关的 Agent 技能。 | `ai-agents` `latex` `mathjax` `terminal` `javascript` | 4 | 2026-09-14 |
| [**herdr-agent-profiles**](https://github.com/mikeyobrien/herdr-agent-profiles)<br><sub>mikeyobrien</sub> | 面向 Herdr 的数据驱动型 CLI harness 与模型配置文件 | `ai-agents` `terminal` `python` | 4 | 2026-08-10 |
| [**arda**](https://github.com/Nirvaan05/arda)<br><sub>Nirvaan05</sub> | Herdr plugin that lets specialized coding agents find each other and work as one team across sessions and machines. | `agent-communication` `agent-handoff` `agent-orchestration` `agent-to-agent` `ai-agents` | 4 | 2026-10-09 |
| [**herdr-conductor**](https://github.com/StructuPath/herdr-conductor)<br><sub>StructuPath</sub> | 将功能交付团队编排为可见的 Herdr Agent 窗格——Conductor 插件 | `orchestration` `javascript` | 4 | 2026-10-02 |
| [**herdr-auto-yes-sir**](https://github.com/xlinx/herdr-auto-yes-sir)<br><sub>xlinx</sub> | herdr-auto-yes-sir——当 Agent 请求批准时，让运行不被阻塞地继续下去，类似 codex 的行为 | `javascript` | 4 | 2026-08-20 |
| [**herdr-council**](https://github.com/zekierman/herdr-council)<br><sub>zekierman</sub> | herdr plugin: ask every coding agent the same question, then let a judge weigh the answers blind | `ai-agents` `llm-council` `go` | 4 | 🔄 2026-10-18 |
| [**herdr-cadence**](https://github.com/zhenyufu/herdr-cadence)<br><sub>zhenyufu</sub> | 由一个 Lead 和一组 Agent 组成的轻量级 Agent 编排器 | `rust` | 4 | 🔄 2026-10-13 |
| [**herdr-blaxel-sandbox-plugin**](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin)<br><sub>blaxel-ai</sub> | 从 Herdr 在持久化的 Blaxel Sandbox 中运行编程 Agent | `blaxel` `claude-code` `codex` `coding-agents` `opencode` | 3 | 🔄 2026-10-21 |
| [**herdr-theos-settler**](https://github.com/calebcauthon/herdr-theos-settler)<br><sub>calebcauthon</sub> | 将已完成的 Herdr Agent 标签页和工作区沉到活跃工作下方，让它们不再挡路。Theo 的点子 | `rust` | 3 | 2026-07-23 |
| [**herdr-chat**](https://github.com/eliasstravik/herdr-chat)<br><sub>eliasstravik</sub> | 为运行在 Herdr 中的 Agent 提供结构化的实时聊天视图 | `typescript` | 3 | 2026-08-24 |
| [**herdr-snip**](https://github.com/eStudio37/herdr-snip)<br><sub>eStudio37</sub> | Box what one agent printed and hand it to another. A Herdr plugin: freeze a pane, box part of it with two clicks, send it to any agent. | `ai-agents` `claude-code` `codex` `coding-agents` `terminal` | 3 | 🔄 2026-10-23 |
| [**herdr-cursor**](https://github.com/gabriel-laet/herdr-cursor)<br><sub>gabriel-laet</sub> | 将 Cursor 的云端 Agent 作为一等公民的 herdr 窗格来使用 | `typescript` | 3 | 2026-09-08 |
| [**herdr-agent-restart**](https://github.com/hmu332233/herdr-agent-restart)<br><sub>hmu332233</sub> | 当显示出现异常时，通过一个快捷键重启 Herdr 中的 Agent，并继续同一段对话。 | `agent-restart` `javascript` | 3 | 2026-09-08 |
| [**brgr**](https://github.com/justn-hyeok/brgr)<br><sub>justn-hyeok</sub> | Run Claude Code, Codex, OpenCode, Cursor and more as parallel coding-agent workers in Herdr panes, orchestrated by your Codex or Claude Code session. | `agent-orchestration` `ai-agents` `ai-coding` `claude-code` `codex` | 3 | 🔄 2026-10-26 |
| [**herdr-sheepdog**](https://github.com/kccarlos/herdr-sheepdog)<br><sub>kccarlos</sub> | Manage your Herdr agents by voice — hands-free, from anywhere. A voice-first agent harness for Claude Code, Codex and other coding agents, with an iPhone app. | `agent-harness` `agent-orchestration` `ai-agents` `claude-code` `codex` | 3 | 🔄 2026-10-26 |
| [**kubeflock**](https://github.com/LoriKarikari/kubeflock)<br><sub>LoriKarikari</sub> | [Experimental] Create and connect Kubernetes sandboxes in Herdr | `agent-sandbox` `gvisor` `kubernetes` `sandbox` `go` | 3 | 2026-09-11 |
| [**herdr-link**](https://github.com/LZHcode1986/herdr-link)<br><sub>LZHcode1986</sub> | 为 Herdr 会话提供更快、更省 token、无需推理的跨 Agent 互操作性。用一份统一的契约取代笨重的 skill，涵盖对等发现、消息传递和窗格生命周期 | `typescript` | 3 | 🔄 2026-10-19 |
| [**herdr-pinpoint**](https://github.com/navishachiku/herdr-pinpoint)<br><sub>navishachiku</sub> | 选择一个 Herdr 空间、标签页或窗格，将其 ID 输入到你正在对话的 Agent 中。 | `javascript` | 3 | 2026-09-22 |
| [**muster**](https://github.com/ofelcan164/muster)<br><sub>ofelcan164</sub> | 在一个屏幕上查看所有仓库中的所有 Agent。一个 herdr 插件。 | `go` | 3 | 2026-09-28 |
| [**herdr-space-topic**](https://github.com/panuhorsmalahti/herdr-space-topic)<br><sub>panuhorsmalahti</sub> | herdr 插件：以 Space 内正在进行的工作——即主 Agent 窗格的实时主题——为每个 Space 命名。 | `ai-agents` `terminal-multiplexer` `javascript` | 3 | 🔄 2026-10-21 |
| [**herdr-crew**](https://github.com/rarce/herdr-crew)<br><sub>rarce</sub> | herdr plugin: bring up a team of Claude Code sessions, one tab per role, plus a live status board, from a versioned .herdr/crew.toml | `ai-agents` `claude-code` `git-worktree` `multi-agent` `rust` | 3 | 🔄 2026-10-24 |
| [**herdr-approve-all**](https://github.com/RenKoya1/herdr-approve-all)<br><sub>RenKoya1</sub> | herdr 插件：一键批准所有被阻塞的 Agent（一次按键处理所有待处理的权限提示） | `shell` | 3 | 2026-08-16 |
| [**horchestra**](https://github.com/SimoneDaniotti/horchestra)<br><sub>SimoneDaniotti</sub> | Orchestrator-led agent teams for Herdr, with a live agent map in every tab | `ai-agents` `claude-code` `codex` `terminal` `tui` | 3 | 🔄 2026-10-13 |
| [**herdr-agents-history**](https://github.com/speardragon/herdr-agents-history)<br><sub>speardragon</sub> | 查看你的 AI 编程 Agent 实际在做什么——一个实时、键盘驱动的 herdr TUI，串流展示你所有 Agent（Claude Code 和 Codex）的每一次工具调用 | `ai-agents` `claude-code` `codex` `tui` `typescript` | 3 | 2026-07-19 |
| [**herdr-bot**](https://github.com/speardragon/herdr-bot)<br><sub>speardragon</sub> | Turn your herdr agents into bots that talk to each other — give Claude Code, Codex or Grok a name and a chat, and put a few in a room. macOS app + herdr plugin. | `agent-orchestration` `ai-agents` `chat` `claude-code` `codex` | 3 | 🔄 2026-10-21 |
| [**herdr-agent-office**](https://github.com/suisya-systems/herdr-agent-office)<br><sub>suisya-systems</sub> | 将你的 Agent 团队呈现为像素风办公室的 herdr 插件。查看谁在工作、谁卡住了，并可直接跳转过去 | `python` | 3 | 2026-07-25 |
| [**herdr-upstash-box**](https://github.com/upstash/herdr-upstash-box)<br><sub>upstash</sub> | Herdr 插件：从你正在查看的 worktree 中，在 Upstash Box 里运行编码 Agent。 | `claude-code` `coding-agents` `sandbox` `upstash` `typescript` | 3 | 2026-09-10 |
| [**herdr-wakeup**](https://github.com/usrivastava92/herdr-wakeup)<br><sub>usrivastava92</sub> | 在 Herdr 管理的 Agent 工作期间，让 macOS 或 Linux 保持唤醒状态的 Herdr 插件 | `power-management` `sleep-prevention` `wakeup` `rust` | 3 | 2026-07-17 |
| [**🆕 stampede**](https://github.com/vib-z/stampede)<br><sub>vib-z</sub> | Text tasks to your Grok Bot. It reaches your Mac over Tailscale, where Claude Code does the job, adding other agents (Codex, Cursor and more) as needed. Nothin… | `agent-orchestration` `ai-agents` `claude-code` `cli` `codex` | 3 | 🔄 2026-10-25 |
| [**herdr-radar-plus**](https://github.com/4242labs/herdr-radar-plus)<br><sub>4242labs</sub> | Herdr 插件：按需要你处理的紧急程度对 Agent 排序，并以跨机器的具名分组呈现。基于 herdr-radar 构建。 | `agent-monitoring` `ai-agents` `coding-agents` `developer-tools` `multi-machine` | 2 | 🔄 2026-10-25 |
| [**🆕 herdr-threads**](https://github.com/alepar/herdr-threads)<br><sub>alepar</sub> | durable group threads for your agents, cross-harness and cross-machine | `rust` | 2 | 🔄 2026-10-24 |
| [**herdr-agent-tree**](https://github.com/dboeter/herdr-agent-tree)<br><sub>dboeter</sub> | herdr plugin: workspaces and their agents as a live tree, docked on the left or right of every tab | `agentic-workflow` `claude-code` `claudecode` `codex-cli` `coding-agents` | 2 | 🔄 2026-10-25 |
| [**herdr-glow**](https://github.com/DevooKim/herdr-glow)<br><sub>DevooKim</sub> | Ambient edge glow on macOS when a Herdr agent is blocked | `swift` | 2 | 🔄 2026-10-15 |
| [**herdr-docket**](https://github.com/DnzzL/herdr-docket)<br><sub>DnzzL</sub> | Give a task to a named coding agent: it opens a PR, a second agent verifies it, a merge gate in code merges it — or hands it to you. A Herdr plugin. | `agent-fleet` `ai-agents` `ai-code-review` `autonomous-agents` `backlog-md` | 2 | 🔄 2026-10-22 |
| [**🆕 browsr**](https://github.com/g00rek/browsr)<br><sub>g00rek</sub> | Keep a dedicated Chromium tab group aligned with each Herdr workspace | `chromium` `coding-agents` `developer-tools` `hyprland` `linux` | 2 | 🔄 2026-10-19 |
| [**herdr-prompt-bucket**](https://github.com/GNURub/herdr-prompt-bucket)<br><sub>GNURub</sub> | 面向运行在 Herdr 中的编程 Agent 的持久化、有序的提示词队列 | `claude-code` `codex` `coding-agents` `opencode` `typescript` | 2 | 2026-08-19 |
| [**herdr-annotations**](https://github.com/IgorWarzocha/herdr-annotations)<br><sub>IgorWarzocha</sub> | 收集对终端选中内容的注释，并暂存到 Herdr Agent 中 | `ai-agents` `annotations` `terminal` `javascript` | 2 | 2026-07-18 |
| [**herdr-watcher**](https://github.com/joshka0/herdr-watcher)<br><sub>joshka0</sub> | 为 Herdr Agent 提供持久化的执行续接和分离式 worker 回调 | `rust` | 2 | 🔄 2026-10-19 |
| [**herdr-plugin**](https://github.com/juscribe/herdr-plugin)<br><sub>juscribe</sub> | 在 Herdr 窗格中创建并流转 Juscribe 工单，并查看每个 Agent 正在处理哪张工单。 | `juscribe` `shell` | 2 | 🔄 2026-10-22 |
| [**herdr-shame-report**](https://github.com/JYasha11/herdr-shame-report)<br><sub>JYasha11</sub> | 永久记录你让 AI Agent 等了多久的账本。羊会记住的 | `javascript` | 2 | 2026-07-10 |
| [**herdr-panorama**](https://github.com/LeaveMyYard/herdr-panorama)<br><sub>LeaveMyYard</sub> | Swarm view for herdr: every Claude Code orchestrator, thread and subagent on one live screen. | `claude-code` `claude-code-plugin` `rust` | 2 | 🔄 2026-10-22 |
| [**herdr-agents-status**](https://github.com/maedana/herdr-agents-status)<br><sub>maedana</sub> | 显示 Herdr Agent 状态的常驻置顶透明浮层——claudeye 的精神续作，专为 Herdr（而非 tmux）打造 | `rust` | 2 | 2026-08-15 |
| [**herdr-redact**](https://github.com/mcc0x/herdr-redact)<br><sub>mcc0x</sub> | Warns you when an agent pane has printed a credential — before you screenshot it, stream it, or paste it into a chat window. | `rust` `secret-detection` `security` `terminal` | 2 | 🔄 2026-10-16 |
| [**herdr-flow**](https://github.com/mohaphez/herdr-flow)<br><sub>mohaphez</sub> | Persistent multi-agent task coordination for Herdr with guarded review and worktree cleanup | `python` | 2 | 2026-10-04 |
| [**herdr-snooze**](https://github.com/mrolafsson/herdr-snooze)<br><sub>mrolafsson</sub> | Keep a long list of agents down to the ones you're working with. A herdr plugin that hides an agent, or a whole space, from the Agents panel until a time you p… | `bubbletea` `claude-code` `coding-agents` `go` `multi-agent` | 2 | 🔄 2026-10-20 |
| [**herdr-plugins**](https://github.com/peteretelej/herdr-plugins)<br><sub>peteretelej</sub> | Open-source herdr plugins that tame my AI Agent herd (work best with OpenCode) 🐏🔌 | `agentic-engineering` `rust` `terminal` | 2 | 🔄 2026-10-25 |
| [**herdr-cam**](https://github.com/rchougule/herdr-cam)<br><sub>rchougule</sub> | Show your agent what's on your desk: press a key, point your webcam, and the photo lands in your coding agent's prompt. A herdr plugin for macOS. | `avfoundation` `claude-code` `codex` `coding-agents` `developer-tools` | 2 | 2026-10-09 |
| [**herdr-browser**](https://github.com/salamituns/herdr-browser)<br><sub>salamituns</sub> | Watch your coding agents browse: a Herdr pane showing the Chrome that Claude Code, Codex, Cursor, Droid and Antigravity drive through chrome-devtools-mcp or Pl… | `ai-agents` `antigravity` `browser` `chrome-devtools` `chrome-devtools-mcp` | 2 | 🔄 2026-10-15 |
| [**herdr-code-board**](https://github.com/sazardev/herdr-code-board)<br><sub>sazardev</sub> | Herdr 内面向 Agent 提示词的看板队列——卡片会将真实 Agent 派发到窗格、工作树和工作区，并可通过规则将一张卡片链到下一张 | `ai-agents` `kanban` `rust` `tui` | 2 | 2026-08-30 |
| [**herdr-achievements**](https://github.com/SerHappy/herdr-achievements)<br><sub>SerHappy</sub> | 为你的 Herdr AI Agent 群体添加成就和小小的庆祝 | `achievements` `ai-agents` `developer-tools` `gamification` `go` | 2 | 2026-07-30 |
| [**herdr-traex**](https://github.com/szrenwei/herdr-traex)<br><sub>szrenwei</sub> | 将 TraeX Agent 的生命周期与元数据接入 Herdr Marketplace | `traex` `python` | 2 | 2026-08-04 |
| [**herdr-forkr**](https://github.com/t4t5/herdr-forkr)<br><sub>t4t5</sub> | 在新的 herdr 窗格中派生（fork）一段 Agent 对话。 | `shell` | 2 | 2026-09-10 |
| [**herdr-rovo-dev**](https://github.com/usrivastava92/herdr-rovo-dev)<br><sub>usrivastava92</sub> | 检测 Rovo Dev CLI 会话并将其作为运行中的 Agent 报告给 Herdr 的插件 | `ai-agent` `rovo` `rovo-dev` `shell` | 2 | 2026-10-05 |
| [**opencode-herdr**](https://github.com/VicenteOlmos/opencode-herdr)<br><sub>VicenteOlmos</sub> | OpenCode plugin: route agents through Herdr as herdr/<adapter>/<model> | `ai-agent` `claude-code` `coding-agent` `cursor` `multi-agent` | 2 | 🔄 2026-10-21 |
| [**🆕 shelley-herdr**](https://github.com/webframp/shelley-herdr)<br><sub>webframp</sub> | Run exe.dev Shelley conversations as native herdr agents | `go` | 2 | 2026-10-10 |
| [**herdr-agent-timer**](https://github.com/Yemeni/herdr-agent-timer)<br><sub>Yemeni</sub> | 让每个 Agent 的状态标签与其耗时交替显示的 Herdr 插件 | `shell` | 2 | 2026-08-14 |
| [**cbds**](https://github.com/zqkra/cbds)<br><sub>zqkra</sub> | 面向 Herdr 群体的可靠多 Agent 编排。提供持久化任务、权威的 worker 报告，以及不会卡死的等待机制 | `agents` `cli` `multi-agent` `orchestration` `javascript` | 2 | 2026-08-31 |
| [**herdr-pouch**](https://github.com/AltanS/herdr-pouch)<br><sub>AltanS</sub> | herdr 插件：预先为 Agent 存储提示词，待其就绪时再插入 | `ai-agents` `ai-coding` `ai-tools` `multiplexing` `typescript` | 1 | 2026-09-02 |
| [**herdr-pi-reloader**](https://github.com/anrunt/herdr-pi-reloader)<br><sub>anrunt</sub> | 从 Herdr 浮层 TUI 中重新加载或重启闲置的 Pi Agent 会话 | `rust` | 1 | 2026-07-18 |
| [**herdr-pointr**](https://github.com/aristeoibarra/herdr-pointr)<br><sub>aristeoibarra</sub> | 指向 localhost 页面上的某个 DOM 元素，即可将其对应的 React 组件、选择器及可选截图发送给负责该项目的编码 Agent。一个 herdr 插件。 | `coding-agent` `devtools` `react` `typescript` | 1 | 2026-09-25 |
| [**herdr-quick-prompt**](https://github.com/astwys/herdr-quick-prompt)<br><sub>astwys</sub> | 向 Agent 窗格发送预定义提示词的 Herdr 插件 | `shell` | 1 | 2026-08-24 |
| [**herdr-overview**](https://github.com/baeroe/herdr-overview)<br><sub>baeroe</sub> | Mission Control for herdr: a live tiled overview of all spaces, every agent or your favorite panes. | `ai-agents` `mission-control` `nodejs` `terminal` `tui` | 1 | 🔄 2026-10-15 |
| [**herdr-agent-queue**](https://github.com/connerohnesorge/herdr-agent-queue)<br><sub>connerohnesorge</sub> | herdr plugin: queue prompts for Claude Code and other agents, submit each as a new turn when the current turn ends (Codex-style queue) | `claude-code` `python` | 1 | 2026-09-29 |
| [**herdr-agent-team**](https://github.com/gdli6177/herdr-agent-team)<br><sub>gdli6177</sub> | 用 Markdown 定义 Agent 团队的 Herdr 插件 | `javascript` | 1 | 2026-08-16 |
| [**herdr-diagrams**](https://github.com/jellespijker/herdr-diagrams)<br><sub>jellespijker</sub> | Mermaid, PlantUML, Structurizr, D2 and Graphviz diagrams from your coding agents, rendered as images in a Herdr pane | `claude-code` `diagrams` `kitty-graphics` `mermaid` `plantuml` | 1 | 2026-10-03 |
| [**paneMorph**](https://github.com/Jenish-Shobhit/paneMorph)<br><sub>Jenish-Shobhit</sub> | 一个 herdr 插件，可在标签页和空间之间移动正在运行的窗格：可将任意窗格发送到任意位置，也可从任意位置取回，且移动操作可撤销。 | `ai-agents` `developer-tools` `pane-management` `ratatui` `rust` | 1 | 🔄 2026-10-18 |
| [**corral**](https://github.com/jirathip-dev/corral)<br><sub>jirathip-dev</sub> | 面向 herdr 编码 Agent 群的只读监控工具。 | `agent-orchestration` `ai-agents` `coding-agents` `devtools` `fleet-management` | 1 | 🔄 2026-10-20 |
| [**herdr-panel**](https://github.com/lukeda/herdr-panel)<br><sub>lukeda</sub> | Your herdr agents and their status in your desktop panel (KDE Plasma 6, more desktops coming) | `ai-agents` `kde` `kde-plasma` `plasma` `plasmoid` | 1 | 🔄 2026-10-16 |
| [**sheprd**](https://github.com/m-mohamed/sheprd)<br><sub>m-mohamed</sub> | 将 Pi、Codex、Claude Code 和 OpenCode 统一收纳到一个可见且隔离的 Herdr「Flok」中 | `agent-tools` `claude-code` `cli` `codex` `coding-agents` | 1 | 2026-08-25 |
| [**herdr-matrix**](https://github.com/madebygrant/herdr-matrix)<br><sub>madebygrant</sub> | Herdr Matrix. Your agents become Smith, Brown and Jones, with Matrix status text and digital rain when idle. | `ai-agents` `matrix` `terminal` `python` | 1 | 🔄 2026-10-13 |
| [**herdr-tournament**](https://github.com/neospeed83/herdr-tournament)<br><sub>neospeed83</sub> | 面向 Herdr 的对抗式多 Agent 代码评审 | `rust` | 1 | 2026-08-29 |
| [**herdr-imebox**](https://github.com/Sawakee/herdr-imebox)<br><sub>Sawakee</sub> | 便于向 herdr 中 AI Agent 窗格输入日文/CJK 文字的 IME 友好弹出文本框 | `cjk` `ime` `input-method` `japanese` `ratatui` | 1 | 2026-07-17 |
| [**herdr-testrun**](https://github.com/shindakun/herdr-testrun)<br><sub>shindakun</sub> | 一个 Herdr 插件。在窗格中运行项目测试，列出失败项，一键发送给 Agent。 | `go` `nodejs` `rust` | 1 | 2026-09-20 |
| [**herdr-group-chat**](https://github.com/terry-li-hm/herdr-group-chat)<br><sub>terry-li-hm</sub> | 面向 Pi、Claude Code、Codex 和 Grok Build 的共享本地 Herdr 聊天室 | `ai-agents` `claude-code` `codex` `grok` `multi-agent` | 1 | 🔄 2026-10-22 |
| [**herdr-plugin-agent-spawn**](https://github.com/varvand/herdr-plugin-agent-spawn)<br><sub>varvand</sub> | Open several Herdr agent panes from one prompt | `python` | 1 | 2026-10-08 |
| [**herdr-polyglot**](https://github.com/wazum/herdr-polyglot)<br><sub>wazum</sub> | 用你自己的语言编写编程 Agent 提示词——DeepL 或 Google Cloud Translate 会将其翻译为英文，并投递到 Claude Code、Codex 或任意 herdr Agent 窗格中 | `ai-agents` `bubbletea` `bubbletea-tui` `claude-code` `codex` | 1 | 2026-09-01 |
| [**🆕 herdr-fleet-plugin**](https://github.com/yarrasys/herdr-fleet-plugin)<br><sub>yarrasys</sub> | herdr plugin: start, restart and swap a team of named coding agents from a per-repository fleet file (.herdr/fleet.toml) | `coding-agents` `multi-agent` `python` | 1 | 🔄 2026-10-26 |
| [**agent-mail**](https://github.com/youssef-tharwat/agent-mail)<br><sub>youssef-tharwat</sub> | Durable mail and work records for coding agents. Local, compact, runtime-independent. | `agent-skill` `rust` | 1 | 2026-10-09 |
| [**🆕 herdr-away-signal**](https://github.com/devicki/herdr-away-signal)<br><sub>devicki</sub> | Herdr plugin: an away signal for bots (Grok Bot, dots, any webhook). Toggle away mode with a key; while away, finished or waiting agents are POSTed to your bot… | `agent-orchestration` `ai-agents` `away-mode` `claude-code` `grok-bot` | 0 | 🔄 2026-10-20 |
| [**🆕 herdr-agent-notes**](https://github.com/timjonez/herdr-agent-notes)<br><sub>timjonez</sub> | herdr 插件：为 Agent 贴上便签，让你能看出某个 Agent 为何处于空闲状态 | `python` | 0 | 2026-08-20 |

<details><summary>与此目的也相关</summary>

- [ZingerLittleBee/Heeler](https://github.com/ZingerLittleBee/Heeler) — 面向 herdr 的原生 iOS Agent 控制台——通过 SSH 查看并操控你机器上的编码 Agent，配备真正的 libghostty 终端、二维码配对，以及 Agent 需要你时的推送通知。
- [a2u/herdr-jira](https://github.com/a2u/herdr-jira) — herdr 的 Jira TUI 插件——通过可配置的 JQL 过滤器浏览、搜索 issue，修改状态，并一键将 issue 交给终端中运行的 AI Agent 处理
- [e2b-dev/herdr-e2b-sandbox](https://github.com/e2b-dev/herdr-e2b-sandbox) — 将 git 工作树镜像到 E2B Sandbox 的 herdr 插件——支持单个沙盒或每个 Agent 一条分支的沙盒集群，并配有 TUI 仪表盘
- [walcew/herdr-assist](https://github.com/walcew/herdr-assist) — 面向 AI 编程 Agent 终端复用器 Herdr 的实体桌面面板——用颜色显示会话状态，当 Agent 停下来请求决策时会响铃提醒。基于 ESP32-S3 + LVGL，提供预编译固件
- [miko-misa/herdr-portfwd](https://github.com/miko-misa/herdr-portfwd) — 面向远程机器上编程 Agent 的自动 SSH 端口转发——Ctrl+点击 Agent 打印的 localhost URL，即可在你本机以相同端口打开该页面。一个 Herdr 插件
- [spad-0x/herdr-mobile-pro](https://github.com/spad-0x/herdr-mobile-pro) — 一款高性能、移动优先的 PWA 仪表盘，采用 Cyber-Dark 设计风格，可直接从智能手机编排 Herdr 与自主 AI Agent。具备安全 HTTPS、语音听写输入、图片上传，以及将终端输出实时语义解析为聊天式…
- [hasuwini77/worktree-fleet](https://github.com/hasuwini77/worktree-fleet) — Parallel Claude Code / Codex builds on Herdr: /herd splits a task into worktree buckets, plus a live fleet po…
- [romiluz13/instinct-herdr-tunnel](https://github.com/romiluz13/instinct-herdr-tunnel) — Let an AI assistant such as Instinct watch and steer your Herdr coding agents: a loopback portal with a 26-ac…
- [virtualboard/herdr-virtualboard](https://github.com/virtualboard/herdr-virtualboard) — 在 Herdr 中管理 VirtualBoard 功能规格的看板：列代表生命周期阶段，卡片代表规格，派发卡片会在窗格中启动对应角色的 Agent。

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-worktree"></a>

## git 工作树与分支管理

> 想为每项工作单独开一个工作树，收尾清理也自动完成

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-worktrunk**](https://github.com/devashish2203/herdr-worktrunk)<br><sub>devashish2203</sub> | 集成 worktrunk 以管理 git 工作树的 Herdr 插件 | `powershell` | 191 | 2026-10-06 |
| [**herdr-plugin-jj-workspace**](https://github.com/NathanFlurry/herdr-plugin-jj-workspace)<br><sub>NathanFlurry</sub> | 将 Jujutsu (jj) 工作区作为 Herdr 工作区进行创建和删除 | `jujutsu` `rust` | 48 | 2026-09-03 |
| [**herdr-plugin-renamer**](https://github.com/wyattjoh/herdr-plugin-renamer)<br><sub>wyattjoh</sub> | 根据 Agent 的第一条提示词，重命名自动生成的 herdr 工作树分支和工作区（通过设备端 Apple FoundationModels 或 Codex） | `rust` | 19 | 🔄 2026-10-26 |
| [**herdr-e2b-sandbox**](https://github.com/e2b-dev/herdr-e2b-sandbox)<br><sub>e2b-dev</sub> | 将 git 工作树镜像到 E2B Sandbox 的 herdr 插件——支持单个沙盒或每个 Agent 一条分支的沙盒集群，并配有 TUI 仪表盘 | `cli` `cloud-dev` `e2b` `git-worktree` `integration` | 14 | 2026-09-29 |
| [**jj-waltz**](https://github.com/EzraCerpac/jj-waltz)<br><sub>EzraCerpac</sub> | 受 Worktrunk 启发的 Jujutsu 工作区切换工具 | `cli` `jj` `jujitsu` `utility` `workspace` | 10 | 🔄 2026-10-14 |
| [**herdr-plugin-git-worktree-hooks**](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks)<br><sub>freethinkel</sub> | 在创建/移除 git 工作树时运行 shell 命令——一份 YAML 配置适用于所有项目，放在任何仓库之外 | `git-worktree` `javascript` | 7 | 2026-07-06 |
| [**herdr-worktree-setup**](https://github.com/lamngockhuong/herdr-worktree-setup)<br><sub>lamngockhuong</sub> | 为每个新 worktree 做好准备的 Herdr 插件：自动检测配置文件、创建共享目录链接，并可选择性运行初始化命令。 | `dotenv` `git-worktree` `monorepo` `javascript` | 7 | 🔄 2026-10-22 |
| [**herdr-worktree-agents**](https://github.com/minhtran3124/herdr-worktree-agents)<br><sub>minhtran3124</sub> | herdr plugin: top-right panel of every git worktree with agent state, PR/CI and git status | `ai-agents` `claude-code` `git-worktree` `ratatui` `rust` | 7 | 2026-09-30 |
| [**bercail**](https://github.com/simoncrypta/bercail)<br><sub>simoncrypta</sub> | 基于 Herdr 的 Agent 化开发环境。 | `agentic-ide` `agentic-workflow` `herdr-integration` `omarchy` `pstack` | 7 | 🔄 2026-10-23 |
| [**herdr-worktree-from-pr**](https://github.com/tdi/herdr-worktree-from-pr)<br><sub>tdi</sub> | 从 GitHub PR 创建 git 工作树，并作为 herdr 工作区打开 | `javascript` | 7 | 2026-09-11 |
| [**herdr-symlink-worktree**](https://github.com/hmu332233/herdr-symlink-worktree)<br><sub>hmu332233</sub> | 将主仓库中的共享本地文件符号链接到新工作树中的 herdr 插件 | `shell` | 6 | 2026-07-16 |
| [**herdr-worktree-hooks**](https://github.com/timofey-TK/herdr-worktree-hooks)<br><sub>timofey-TK</sub> | herdr 插件：在创建、打开或删除 git 工作树时运行自定义的初始化/清理命令 | `developer-tools` `git-worktree` `worktree` `python` | 6 | 2026-07-17 |
| [**herdr-worktree-seed**](https://github.com/jlimas/herdr-worktree-seed)<br><sub>jlimas</sub> | 为新工作树植入 copy-on-write 的 node_modules 和可配置本地 dotfiles 的 Herdr 插件 | `developer-tools` `dotfiles` `git-worktree` `nodejs` `typescript` | 5 | 2026-07-28 |
| [**herdr-jj-status**](https://github.com/mroth/herdr-jj-status)<br><sub>mroth</sub> | herdr 插件：在空间侧边栏中显示 jj 工作区的 Jujutsu 书签/状态 | `shell` | 5 | 2026-07-28 |
| [**herdr-worktreeinclude**](https://github.com/tanshio/herdr-worktreeinclude)<br><sub>tanshio</sub> | Herdr 插件：将匹配 .worktreeinclude 的被 gitignore 文件复制到新创建的工作树中 | `worktree` `worktreeiclude` `shell` | 5 | 2026-07-11 |
| [**herdr-remote-worktrunk**](https://github.com/ditwrd/herdr-remote-worktrunk)<br><sub>ditwrd</sub> | Herdr 的远程 worktrunk 工作区 | `shell` | 4 | 2026-07-10 |
| [**herdr-pi-tree**](https://github.com/edxeth/herdr-pi-tree)<br><sub>edxeth</sub> | 以树状结构展示你的 Pi Agent 的侧边栏——谁生成了谁、哪个 worktree 对应哪个分支、谁在等待你。 | `git-worktrees` `pi` `pi-coding-agent` `sidebar` `terminal` | 4 | 🔄 2026-10-20 |
| [**herdr-plugin-cow-worktree**](https://github.com/khatriafaz/herdr-plugin-cow-worktree)<br><sub>khatriafaz</sub> | 一个 Herdr 插件，用于创建严格的写时复制（copy-on-write）Git worktree，并包含被 .gitignore 忽略的本地文件。 | `typescript` | 4 | 2026-09-20 |
| [**herdr-jj**](https://github.com/OliverGilan/herdr-jj)<br><sub>OliverGilan</sub> | 为 Herdr 添加 Jujutsu 工作区支持 | `jujutsu` `rust` | 4 | 🔄 2026-10-12 |
| [**herdr-fresh-worktree**](https://github.com/persiyanov/herdr-fresh-worktree)<br><sub>persiyanov</sub> | 将新创建的 herdr 工作树重置为 origin 默认分支的最新状态 | `javascript` | 4 | 2026-06-25 |
| [**herdr-opendeck**](https://github.com/Resilient-Software/herdr-opendeck)<br><sub>Resilient-Software</sub> | 将 Herdr 工作区镜像到 Stream Deck 上。以实时磁贴显示仓库、分支和 Agent 状态。 | `elgato` `opendeck` `stream-deck` `typescript` | 4 | 🔄 2026-10-19 |
| [**herdr-quartermaster**](https://github.com/travisjeffery/herdr-quartermaster)<br><sub>travisjeffery</sub> | Herdr plugin: one coordinator, a worktree and agent per bead, beads as the only record | `go` | 4 | 🔄 2026-10-21 |
| [**herdr-worktreeinclude**](https://github.com/eightHundreds/herdr-worktreeinclude)<br><sub>eightHundreds</sub> | Herdr 插件：将 .worktreeinclude 指定的被 gitignore 文件复制到新工作树中 | `worktree` `rust` | 3 | 2026-07-28 |
| [**herdr-multirepo**](https://github.com/jattento/herdr-multirepo)<br><sub>jattento</sub> | 在一个 Herdr 工作区中管理跨多个仓库的同一条功能分支 | `git-worktree` `python` | 3 | 2026-08-03 |
| [**herdr-wish**](https://github.com/MovieHolic-Plex/herdr-wish)<br><sub>MovieHolic-Plex</sub> | Herdr 插件。许下一个愿望，omo 就会提交一个 PR。执行 omo-10 会打开 10 个 worktree。 | `omo` `wish` `javascript` | 3 | 2026-10-09 |
| [**herdr-branch-cleanup**](https://github.com/osolmaz/herdr-branch-cleanup)<br><sub>osolmaz</sub> | 当窗格所在分支在 GitHub 上被合并或删除后，自动切换到默认分支 | `git` `github` `rust` | 3 | 2026-07-26 |
| [**herdr-worktree-lifecycle**](https://github.com/qdentity/herdr-worktree-lifecycle)<br><sub>qdentity</sub> | Herdr 插件：将工作树生命周期事件分发给仓库自带的初始化/清理脚本 | `rust` | 3 | 2026-06-29 |
| [**herdr-worktree-nav**](https://github.com/ShoMasegi/herdr-worktree-nav)<br><sub>ShoMasegi</sub> | _(暂无描述)_ | `terminal` `rust` | 3 | 🔄 2026-10-19 |
| [**herdr-worktree-copy**](https://github.com/crexi/herdr-worktree-copy)<br><sub>crexi</sub> | 根据 .worktree-copy 清单复制并符号链接工作树本地文件的 Herdr 插件 | `git-worktree` `shell` | 2 | 2026-07-28 |
| [**herdr-deck**](https://github.com/ctbaum/herdr-deck)<br><sub>ctbaum</sub> | herdr-agents.nvim 的配套工作区启动器：在预置好的 Neovim、Agent 与 Shell 面板中，随时打开或恢复 Claude、Codex 和 Pi。 | `claude-code` `codex` `coding-agents` `git-worktree` `neovim` | 2 | 🔄 2026-10-24 |
| [**trunkr**](https://github.com/disintegrator/trunkr)<br><sub>disintegrator</sub> | Herdr 🤝 Worktrunk——连接 Herdr 与 Worktrunk 的插件 | `go` | 2 | 2026-08-12 |
| [**herdr-tagr**](https://github.com/dvoets/herdr-tagr)<br><sub>dvoets</sub> | 为 herdr 打造的简洁、以图标为先的标签页标题：应用图标 + git 分支 + 文件夹。 | `rust` `terminal` | 2 | 2026-10-09 |
| [**herdr-plugin-jj-workspace**](https://github.com/expnn/herdr-plugin-jj-workspace)<br><sub>expnn</sub> | 一个用于创建和删除 Jujutsu（jj）工作区的 Herdr 插件。 | `rust` | 2 | 2026-09-30 |
| [**herdr-gc**](https://github.com/H3xept/herdr-gc)<br><sub>H3xept</sub> | 当 herdr 中的 Git worktree 被创建、打开、关闭或删除时，运行你自定义的步骤：安装、建议清理、分类等。 | `git-worktree` `terminal` `javascript` | 2 | 🔄 2026-10-18 |
| [**herdr-inbox**](https://github.com/lucasscariot/herdr-inbox)<br><sub>lucasscariot</sub> | Herdr plugin: start agent threads on any project, harness, machine, or worktree, and follow every agent in one live inbox | `blueprint` `coding-agents` `python` `tui` `rust` | 2 | 🔄 2026-10-17 |
| [**herdr-shear**](https://github.com/mcc0x/herdr-shear)<br><sub>mcc0x</sub> | Find the git worktrees that are safe to delete, and delete those. A worktree janitor for herdr. | `cleanup` `git-worktree` `rust` `terminal` | 2 | 🔄 2026-10-16 |
| [**herdr-worktreeinclude**](https://github.com/serhii-chernenko/herdr-worktreeinclude)<br><sub>serhii-chernenko</sub> | 允许为新工作树指定自定义路径，并像 Claude CLI 一样遵循 `.worktreeinclude` 文件 | `worktree` `shell` | 2 | 🔄 2026-10-14 |
| [**herdr-plugin-worktree-bootstrap**](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap)<br><sub>zerodice0</sub> | 在新的 Herdr Git 工作树中安全地复制被忽略的本地文件并运行初始化命令 | `python` | 2 | 🔄 2026-10-17 |
| [**herdr-worktree-upstream**](https://github.com/DaveBird99/herdr-worktree-upstream)<br><sub>DaveBird99</sub> | herdr plugin: link a new worktree to its existing origin branch | `shell` | 1 | 2026-10-07 |
| [**herdr-worktree-include**](https://github.com/tupton/herdr-worktree-include)<br><sub>tupton</sub> | 将未跟踪的文件以符号链接或复制的方式引入 herdr 创建的 git worktree。 | `shell` | 1 | 2026-09-14 |
| [**🆕 herdr-worktree-rm**](https://github.com/dorshinar/herdr-worktree-rm)<br><sub>dorshinar</sub> | Herdr plugin: delete a worktree checkout in the background with a confirm popup and sidebar spinner, without freezing the UI | `shell` | 0 | 🔄 2026-10-22 |
| [**🆕 herdr-worktree**](https://github.com/tjg184/herdr-worktree)<br><sub>tjg184</sub> | 同时兼容 worktrunk 和原生工作树的 Herdr 工作树插件 | `rust` | 0 | 🔄 2026-10-13 |

<details><summary>与此目的也相关</summary>

- [tdi/herdr-worktree-from-linear](https://github.com/tdi/herdr-worktree-from-linear) — 从 Linear issue 创建 git 工作树，并作为 herdr 工作区打开
- [mrolafsson/herdr-linear](https://github.com/mrolafsson/herdr-linear) — 在 herdr 弹窗中管理 Linear 的工单和项目：显示状态图标、渲染后的描述、可变更状态，一键创建 worktree，点击 Start 即可将工单交给你的编码 Agent。支持 OAuth 登录。
- [hanbong5938/herdr-jira-worktree](https://github.com/hanbong5938/herdr-jira-worktree) — 面向 herdr 的 Jira TUI 插件（fork 自 a2u/herdr-jira）——支持 JQL 过滤、搜索、状态流转，可将工单委派给 AI Agent，或将其检出为 git worktree。
- [mrolafsson/herdr-github](https://github.com/mrolafsson/herdr-github) — GitHub pull requests in a herdr popup: merge readiness, checks and reviews, draft toggle, merge or auto-merge…
- [rarce/herdr-crew](https://github.com/rarce/herdr-crew) — herdr plugin: bring up a team of Claude Code sessions, one tab per role, plus a live status board, from a ver…
- [upstash/herdr-upstash-box](https://github.com/upstash/herdr-upstash-box) — Herdr 插件：从你正在查看的 worktree 中，在 Upstash Box 里运行编码 Agent。
- [hasuwini77/worktree-fleet](https://github.com/hasuwini77/worktree-fleet) — Parallel Claude Code / Codex builds on Herdr: /herd splits a task into worktree buckets, plus a live fleet po…
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — 为 JavaScript 和 TypeScript 自动初始化 Herdr 工作树，支持基于锁文件的安装和安全的环境变量还原
- [mohaphez/herdr-flow](https://github.com/mohaphez/herdr-flow) — Persistent multi-agent task coordination for Herdr with guarded review and worktree cleanup
- [tomasvarga/herdr-e2b](https://github.com/tomasvarga/herdr-e2b) — 按需将 git 工作树镜像到全新的 E2B 云沙盒——直接上传快照（包括未提交的更改），无需 push 或 clone。一个 herdr 插件
- [poislagarde/herdr-worktree-cleanup](https://github.com/poislagarde/herdr-worktree-cleanup) — 当对应的 Herdr 空间关闭时，自动清理可安全删除的 GitHub PR worktree。Python 编写，无依赖，MIT 许可。

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-review"></a>

## 代码审查与差异对比

> 想阅读 Agent 写的差异并对其发表评论

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**crabbox**](https://github.com/openclaw/crabbox)<br><sub>openclaw</sub> | Crabbox：预热沙盒、同步差异、运行测试套件 | `agent-skills` `remote-test-runner` `go` | 1502 | 🔄 2026-10-26 |
| [**herdr-reviewr**](https://github.com/persiyanov/herdr-reviewr)<br><sub>persiyanov</sub> | Review your agent's diff in a terminal pane and send comments back to Claude Code, Codex, OpenCode or Pi. A herdr plugin. | `agentic-coding` `ai-agents` `claude-code` `cli` `code-review` | 946 | 🔄 2026-10-24 |
| [**herdr-annotate**](https://github.com/plannotator/herdr-annotate)<br><sub>plannotator</sub> | 在 Herdr 中为终端文本、文档和 Agent 回复添加注释并进行评审，并将反馈直接发回给 Agent | `annotation` `multiplexer` `rust` | 700 | 🔄 2026-10-23 |
| [**roamgate**](https://github.com/powerfooI/roamgate)<br><sub>powerfooI</sub> | 适用于任意屏幕的 Herdr 客户端。可在桌面或移动设备上控制终端、监控编码 Agent，并查看文件与差异。 | `ai-agents` `bun` `code-review` `developer-tools` `git-worktree` | 320 | 🔄 2026-10-26 |
| [**herdr-hunk-diff**](https://github.com/jhochenbaum/herdr-hunk-diff)<br><sub>jhochenbaum</sub> | 从 herdr 在 Hunk 中审查 Agent 编写的更改，并将行内评论回传给对应的 Agent | `code-review` `hunk` `typescript` | 147 | 🔄 2026-10-21 |
| [**herdr-plannotator**](https://github.com/plannotator/herdr-plannotator)<br><sub>plannotator</sub> | 在 Herdr 的 Browser 窗格内打开 Plannotator 评审的插件 | `plannotator` `typescript` | 26 | 2026-07-29 |
| [**herdr-gitview**](https://github.com/ChmaraX/herdr-gitview)<br><sub>ChmaraX</sub> | herdr 的 Git 状态/差异面板——审查更改、在 nvim 中编辑、暂存/提交/丢弃，全部在终端内完成 | `git` `git-diff` `git-tui` `neovim` `rust` | 21 | 🔄 2026-10-23 |
| [**herdr-pickr**](https://github.com/tomasvarga/herdr-pickr)<br><sub>tomasvarga</sub> | herdr 的 PR 审查路由器——按住 Ctrl 点击 GitHub PR / GitLab MR 链接，选择审查工具（tuicr · hunk · diff · 浏览器 · 或自定义工具），可选启用 AI 初审 | `cli` `code-review` `pull-request` `tui` `shell` | 20 | 2026-07-13 |
| [**herdr-plugin-hunk**](https://github.com/edmundmiller/herdr-plugin-hunk)<br><sub>edmundmiller</sub> | 在分屏窗格或标签页中打开 Hunk 差异对比的 Herdr 插件 | `python` | 15 | 2026-06-23 |
| [**herdr-extensions**](https://github.com/vonzelle-vzt/herdr-extensions)<br><sub>vonzelle-vzt</sub> | 面向 herdr 的迷你 VS Code——具备 LSP 诊断、自动补全、重命名和跳转到定义的完整编辑器，外加源代码管理、搜索、问题面板、测试、调试器、应用实时预览、运行时错误捕获、图片粘贴和 Agent 差异审查。共 12 个面板，一条命令即可幂等且可逆地安装 | `agent-tools` `autocomplete` `claude-code` `cli` `code-review` | 7 | 🔄 2026-10-25 |
| [**herdr-plugin-hunk-autodiff**](https://github.com/scott306lr/herdr-plugin-hunk-autodiff)<br><sub>scott306lr</sub> | Herdr 插件：当编程 Agent 完成任务但留有未提交更改时，自动打开 hunk 差异分屏 | `claude-code` `hunk` `python` | 5 | 2026-07-05 |
| [**herdr-review**](https://github.com/alexeyco/herdr-review)<br><sub>alexeyco</sub> | Review agent-authored Git diffs in Herdr with revdiff, tuicr, or lumen | `ai-agents` `code-review` `coding-agents` `developer-tools` `git-diff` | 3 | 🔄 2026-10-23 |
| [**huicr**](https://github.com/claytonjschneider/huicr)<br><sub>claytonjschneider</sub> | 面向代码评审的 Herdr 用户界面。 | `python` | 3 | 2026-10-01 |
| [**herdr-progressive-reviewer**](https://github.com/flupke/herdr-progressive-reviewer)<br><sub>flupke</sub> | 受 Tidewave 启发的回合制差异审查工具 | `rust` | 3 | 🔄 2026-10-24 |
| [**herdr-review.nvim**](https://github.com/inferst/herdr-review.nvim)<br><sub>inferst</sub> | 集成 Git 和 herdr 的 Neovim 代码审查 UI | `lua` | 3 | 2026-08-01 |
| [**herdr-review**](https://github.com/quantk/herdr-review)<br><sub>quantk</sub> | 在 Hunk 中审查 Agent 编写的更改，并通过 Herdr 回传行内反馈 | `code-review` `hunk` `javascript` | 3 | 2026-07-28 |
| [**easy-review**](https://github.com/VilfredSikker/easy-review)<br><sub>VilfredSikker</sub> | 面向 AI 辅助编程的 Git 差异审查，提供终端 TUI 和 Tauri 桌面应用两种形式 | `ai-code-review` `cli` `code-review` `desktop-app` `developer-tools` | 3 | 🔄 2026-10-26 |
| [**herdr-hunk**](https://github.com/yuucu/herdr-hunk)<br><sub>yuucu</sub> | herdr 插件：为你的 Agent 工作区切换 Hunk 差异审查 | `diff` `hunk` `go` | 3 | 2026-10-01 |
| [**magnum**](https://github.com/zhuravel/magnum)<br><sub>zhuravel</sub> | Your AI coding agents as a pull-request review team: Claude Code, Codex and others review each push in herdr panes, a judge proves every finding, one GitHub re… | `ai-agents` `ai-code-review` `bubbletea` `claude-code` `cli` | 3 | 🔄 2026-10-25 |
| [**herdr-stagr**](https://github.com/brianh20/herdr-stagr)<br><sub>brianh20</sub> | 面向 herdr 的源代码管理侧边栏——通过并排差异对比进行暂存、取消暂存和放弃更改 | `git` `tui` `rust` | 2 | 2026-08-06 |
| [**🆕 diffui**](https://github.com/dgsienko/diffui)<br><sub>dgsienko</sub> | Locally hosted web tool and terminal ui for reviewing live diffs and improving your agentic coding and review flow. | `agentic-coding` `ai-agents` `ai-tools` `claude-code` `cli` | 2 | 🔄 2026-10-23 |
| [**herdr-git-tree**](https://github.com/ExLuna-rs/herdr-git-tree)<br><sub>ExLuna-rs</sub> | Interactive git graph with real-time diffs and branch management — herdr plugin | `git` `rust` `tui` | 2 | 2026-10-01 |
| [**herdr-tasks**](https://github.com/husniadil/herdr-tasks)<br><sub>husniadil</sub> | 面向 Herdr 编程 Agent 的任务待办和笔记看板——带租约的 claim、有证据支撑的评审，以及人工决策关卡，全部由一个 Go 二进制程序实现 | `ai-agents` `mcp-server` `notes` `sqlite` `task-management` | 2 | 2026-08-30 |
| [**herdr-pr-tracker**](https://github.com/jakekroon/herdr-pr-tracker)<br><sub>jakekroon</sub> | 将你所创建的所有未关闭拉取请求以停靠面板形式展示，并按你需要处理的紧迫程度进行颜色标注。一个 Herdr 插件 | `bun` `code-review` `developer-tools` `github` `pull-requests` | 2 | 2026-10-10 |
| [**herdr-scribe**](https://github.com/Javamomma/herdr-scribe)<br><sub>Javamomma</sub> | herdr 插件：不录音的实时会议转录——将麦克风输入转为仅存于内存的文字记录和实时分析窗格；停止时生成会议纪要、可选策略关卡以及可审查的自动草稿。支持 Linux/WSL2 和 macOS | `macos` `meeting-notes` `privacy` `speech-to-text` `terminal` | 2 | 2026-08-07 |
| [**herdr-router**](https://github.com/Qingswe/herdr-router)<br><sub>Qingswe</sub> | Route coding tasks to the right agent, model, and effort by difficulty and duration, with a visual web policy editor. | `python` | 2 | 🔄 2026-10-12 |
| [**herdr-comments**](https://github.com/shadowfax92/herdr-comments)<br><sub>shadowfax92</sub> | 为复制的 Herdr 终端输出添加注释，按窗格收集评论，并可在 Neovim 中审查 | `ai-agents` `annotations` `neovim` `rust` `terminal` | 2 | 🔄 2026-10-13 |
| [**herdr-lazygit-viewer**](https://github.com/tareqmlx/herdr-lazygit-viewer)<br><sub>tareqmlx</sub> | 在最适合当下场景的 Herdr 展示位置，以打开 files、branches、commits 或 stash 面板的状态启动 lazygit | `code-review` `lazygit` `rust` | 2 | 2026-08-14 |
| [**herdr-pr-ops**](https://github.com/tferreira/herdr-pr-ops)<br><sub>tferreira</sub> | PR//OPS - pull request mission control for Herdr: your PRs and review requests on one board, one-key agents in Herdr panes | `ai-agents` `claude-code` `code-review` `codex` `dashboard` | 2 | 🔄 2026-10-15 |
| [**roboherd**](https://github.com/andschneider/roboherd)<br><sub>andschneider</sub> | 在 herdr 工作区中处理 roborev 的评审状态和操作 | `rust` `tui` | 1 | 2026-09-20 |
| [**herdr-agent-diff**](https://github.com/baotran01/herdr-agent-diff)<br><sub>baotran01</sub> | 用于查看 Agent 文件系统和 Git 差异的 Herdr 插件 | `rust` | 1 | 2026-08-03 |
| [**herdr-peer-review**](https://github.com/Elio2000/herdr-peer-review)<br><sub>Elio2000</sub> | 在 herdr 窗格中打开第二个编程 Agent 来审查你的差异——可观察、自动批准、只读。附带用于「审查↔修改↔决策」自主循环的 Claude Code skill | `agent-skills` `ai-agents` `claude-code` `code-review` `codex` | 1 | 2026-07-16 |
| [**codeMap**](https://github.com/Jenish-Shobhit/codeMap)<br><sub>Jenish-Shobhit</sub> | 一个 herdr 插件，以地图和流程图的形式展示你的代码，并在 Agent 窗格上方的一个弹窗中评审编码 Agent 所做的更改。 | `ai-agents` `code-review` `code-visualization` `developer-tools` `git` | 1 | 🔄 2026-10-18 |
| [**herdr-git-graph**](https://github.com/jorge-huxley/herdr-git-graph)<br><sub>jorge-huxley</sub> | Herdr 的只读 git 图谱 TUI 插件，支持彩色 ASCII 分支线、分支过滤、搜索和按需查看差异 | `rust` | 1 | 2026-07-17 |
| [**herdr-gitdeck**](https://github.com/pgen0x/herdr-gitdeck)<br><sub>pgen0x</sub> | herdr plugin: review, stage and commit diffs across every git repo in a folder, and send line comments to your coding agent | `git` `ratatui` `rust` `tui` | 1 | 🔄 2026-10-16 |
| [**codey**](https://github.com/rodeyseijkens/codey)<br><sub>rodeyseijkens</sub> | 一个以代码审查为核心的 Git TUI（终端界面），提供分为「已暂存/变更」两个区域的差异查看器，支持临时评论与真实的 Git 暂存操作，基于 OpenTUI 构建。 | `code-review` `opentui` `review-tool` `tui` `typescript` | 1 | 2026-10-01 |
| [**herdr-hunks**](https://github.com/winoooops/herdr-hunks)<br><sub>winoooops</sub> | 面向 Herdr 的 Git hunk 查看器。可在终端中评审已提交和未提交的更改、比较分支并查看差异。 | `git` `rust` `tui` | 1 | 2026-10-08 |
| [**🆕 herdr-git-status**](https://github.com/ubuntudroid/herdr-git-status)<br><sub>ubuntudroid</sub> | herdr plugin: live CI and code-review status for GitHub and GitLab in the sidebar, plus on-demand CI-detail and My PRs panes | `shell` | 0 | 🔄 2026-10-23 |

<details><summary>与此目的也相关</summary>

- [eliasstravik/herdr-projects](https://github.com/eliasstravik/herdr-projects) — Mission control for Herdr: run dozens of coding agents from one board. Each works on its own branch, a second…
- [jpolec/herdr-plugin-odysseus](https://github.com/jpolec/herdr-plugin-odysseus) — 面向 Herdr 的受治理多 Agent 工作流：任务 → Herdr 窗格中的 Agent → 检查、重试、评审、策略、审批、审计、草拟 PR。
- [ericbust/namedrop](https://github.com/ericbust/namedrop) — @mentions for Codex, Claude Code, and your terminal. A Herdr plugin that lets agents in different panes work…
- [JacquesvanWyk/herdr-hunk](https://github.com/JacquesvanWyk/herdr-hunk) — herdr 中用于 Hunk 差异对比的交互式 fzf 选择器：支持提交、范围、stash，并可在 Agent 完成时自动打开
- [tomasvarga/herdr-sniffr](https://github.com/tomasvarga/herdr-sniffr) — 在你审查之前，AI 先嗅探你的 PR 有没有问题——一个 Agent 化的初审，将草稿评论投放到 tuicr。不限定 Agent（codex/claude/cursor/grok/…）
- [anhnd3005-infinity/herdr-worker-orchestrator](https://github.com/anhnd3005-infinity/herdr-worker-orchestrator) — 通过 Herdr 管理的窗格，将任务派发给 CLI Agent worker（agy、codex 等）——支持有状态的任务追踪、工作树隔离和基于差异的评审。同时适用于 Claude Code 和 Herdr 的双用插件
- [itisbryan/herdr-gh-checks](https://github.com/itisbryan/herdr-gh-checks) — herdr 插件：在窗格中监视并查看当前 PR 的 CI，并在侧边栏行中显示 CI/合并状态。使用 Go + Bubble Tea 编写
- [elKei24/herdr-co-review](https://github.com/elKei24/herdr-co-review) — 在 herdr 中进行分屏 PR 评审——你的 Agent 找出问题，你在 TUI 中于代码旁逐一裁定，最后由 Agent 发布你批准的内容
- [mikhail-angelov/herdr-review-loop](https://github.com/mikhail-angelov/herdr-review-loop) — 在 herdr 工作区中让 Agent 之间自动进行交叉评审——一个负责编写，另一个负责评审，如此反复
- [mrolafsson/herdr-github](https://github.com/mrolafsson/herdr-github) — GitHub pull requests in a herdr popup: merge readiness, checks and reviews, draft toggle, merge or auto-merge…
- [DnzzL/herdr-docket](https://github.com/DnzzL/herdr-docket) — Give a task to a named coding agent: it opens a PR, a second agent verifies it, a merge gate in code merges i…
- [neospeed83/herdr-tournament](https://github.com/neospeed83/herdr-tournament) — 面向 Herdr 的对抗式多 Agent 代码评审

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-forge"></a>

## GitHub / issue 跟踪工具集成

> 想以 issue 或 PR 为起点开始工作，并追踪 PR 状态

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**tsk**](https://github.com/smarzban/tsk)<br><sub>smarzban</sub> | tsk 是一款完全运行在终端中的 Linear 替代品：为你和你的 Agent 提供共享任务看板——你使用 TUI，Agent 使用 CLI。 | `cli` `productivity` `rust` `task-manager` `terminal` | 231 | 🔄 2026-10-22 |
| [**ghzinga**](https://github.com/osolmaz/ghzinga)<br><sub>osolmaz</sub> | 用于查看单个 GitHub issue 或 PR 的简易可点击 TUI，用 Rust 编写 | `rust` | 90 | 2026-09-06 |
| [**🆕 beady-eye**](https://github.com/CodeForBreakfast/beady-eye)<br><sub>CodeForBreakfast</sub> | Draws the work in your beads trackers as trees, with what each agent is doing beside the bead it works. It also watches beads for whatever waits on them, and s… | `agents` `beads` `claude-code` `claude-code-plugin` `github` | 24 | 🔄 2026-10-26 |
| [**herdr-plugin-gh-pr**](https://github.com/wyattjoh/herdr-plugin-gh-pr)<br><sub>wyattjoh</sub> | 在侧边栏显示当前聚焦 Agent 窗格所在分支的 GitHub PR 状态的 herdr 插件 | `typescript` | 23 | 2026-07-16 |
| [**herdr-worktree-from-linear**](https://github.com/tdi/herdr-worktree-from-linear)<br><sub>tdi</sub> | 从 Linear issue 创建 git 工作树，并作为 herdr 工作区打开 | `javascript` | 19 | 2026-09-11 |
| [**herdr-plugin-github-start**](https://github.com/ogulcancelik/herdr-plugin-github-start)<br><sub>ogulcancelik</sub> | 从 GitHub issue、PR 或讨论中启动 Codex 或 Claude 的 Herdr 插件 | `javascript` | 17 | 2026-08-31 |
| [**gitty**](https://github.com/VedangP57/gitty)<br><sub>VedangP57</sub> | A blazing-fast, GitHub-Desktop-style git TUI for the terminal (Rust + Ratatui) | `git` `ratatui` `rust` `terminal` `tui` | 16 | 🔄 2026-10-19 |
| [**herdr-jira**](https://github.com/a2u/herdr-jira)<br><sub>a2u</sub> | herdr 的 Jira TUI 插件——通过可配置的 JQL 过滤器浏览、搜索 issue，修改状态，并一键将 issue 交给终端中运行的 AI Agent 处理 | `ai-agents` `jira` `ratatui` `rust` `tui` | 14 | 2026-09-05 |
| [**herdr-pr-tracker**](https://github.com/Matovidlo/herdr-pr-tracker)<br><sub>Matovidlo</sub> | herdr 插件：追踪每个 Claude Code 会话产生的 GitHub PR，附带 gh 状态和操作 | `claude-code` `shell` | 12 | 🔄 2026-10-22 |
| [**herdr-linear**](https://github.com/JacquesvanWyk/herdr-linear)<br><sub>JacquesvanWyk</sub> | 在 herdr 分屏窗格或标签页中运行的 fzf 驱动 Linear 面板：搜索 issue、深入项目、创建 issue、修改状态 | `shell` | 8 | 2026-07-12 |
| [**herdr-plugins**](https://github.com/JJLiebig/herdr-plugins)<br><sub>JJLiebig</sub> | 一个 Herdr 插件，可从 GitHub 的 issue、PR 或讨论直接启动 Codex 或 Claude。 | `javascript` | 7 | 2026-10-04 |
| [**herdr-sniffr**](https://github.com/tomasvarga/herdr-sniffr)<br><sub>tomasvarga</sub> | 在你审查之前，AI 先嗅探你的 PR 有没有问题——一个 Agent 化的初审，将草稿评论投放到 tuicr。不限定 Agent（codex/claude/cursor/grok/…） | `ai` `cli` `code-review` `pull-request` `tuicr` | 6 | 2026-07-14 |
| [**mergr**](https://github.com/jsmenzies/mergr)<br><sub>jsmenzies</sub> | 在 Herdr Space 侧边栏行中显示 GitHub 拉取请求状态 | `github-pull-requests` `rust` | 5 | 2026-07-30 |
| [**herdr-git-status**](https://github.com/krystof018/herdr-git-status)<br><sub>krystof018</sub> | 在 herdr 内呈现 CI 状态——同时支持 GitLab（流水线+合并请求）和 GitHub（Actions+拉取请求），根据仓库的 origin 自动识别 | `bash` `ci-cd` `ci-status` `developer-tools` `github-actions` | 5 | 2026-09-20 |
| [**herdr-linear**](https://github.com/talent-factory/herdr-linear)<br><sub>talent-factory</sub> | 面向 Herdr 的 Linear issue 面板，按 Enter 即可开始实现 | `rust` | 5 | 2026-10-10 |
| [**herdr-pr-board**](https://github.com/cdowell09/herdr-pr-board)<br><sub>cdowell09</sub> | 面向 Herdr 的可配置跨仓库 GitHub 拉取请求仪表盘 | `github` `tui` `go` | 4 | 🔄 2026-10-21 |
| [**herdr-gh-checks**](https://github.com/itisbryan/herdr-gh-checks)<br><sub>itisbryan</sub> | herdr 插件：在窗格中监视并查看当前 PR 的 CI，并在侧边栏行中显示 CI/合并状态。使用 Go + Bubble Tea 编写 | `bubbletea` `ci` `github-actions` `tui` `go` | 4 | 2026-08-25 |
| [**herdr-linear**](https://github.com/mrolafsson/herdr-linear)<br><sub>mrolafsson</sub> | 在 herdr 弹窗中管理 Linear 的工单和项目：显示状态图标、渲染后的描述、可变更状态，一键创建 worktree，点击 Start 即可将工单交给你的编码 Agent。支持 OAuth 登录。 | `bubbletea` `claude-code` `coding-agents` `git-worktree` `go` | 4 | 🔄 2026-10-20 |
| [**herdr-linear-agent**](https://github.com/civitaspo/herdr-linear-agent)<br><sub>civitaspo</sub> | Herdr plugin that runs a coordinator and per-repository coding agents for Linear issues delegated to its app user. | `linear` `rust` | 3 | 🔄 2026-10-26 |
| [**herdr-co-review**](https://github.com/elKei24/herdr-co-review)<br><sub>elKei24</sub> | 在 herdr 中进行分屏 PR 评审——你的 Agent 找出问题，你在 TUI 中于代码旁逐一裁定，最后由 Agent 发布你批准的内容 | `cli` `code-review` `pull-request` `rust` `tui` | 3 | 🔄 2026-10-14 |
| [**herdr-jira-worktree**](https://github.com/hanbong5938/herdr-jira-worktree)<br><sub>hanbong5938</sub> | 面向 herdr 的 Jira TUI 插件（fork 自 a2u/herdr-jira）——支持 JQL 过滤、搜索、状态流转，可将工单委派给 AI Agent，或将其检出为 git worktree。 | `jira` `tui` `rust` | 3 | 🔄 2026-10-12 |
| [**herdr-beads**](https://github.com/hexsprite/herdr-beads)<br><sub>hexsprite</sub> | 在 Herdr 中 Ctrl+点击 beads 的 issue ID，即可在分屏窗格中打开其详情 | `beads` `issue-tracker` `terminal` `shell` | 3 | 2026-09-26 |
| [**herdr-pane-issue**](https://github.com/ilazaridis/herdr-pane-issue)<br><sub>ilazaridis</sub> | Herdr 插件：在 Agents 侧边栏中显示每个 Agent 窗格正在处理的 GitHub issue，一键即可打开。 | `shell` | 3 | 2026-09-24 |
| [**herdr-plugin-gh-workflow**](https://github.com/kkckkc/herdr-plugin-gh-workflow)<br><sub>kkckkc</sub> | 用于 GitHub workflow 的 Herdr 插件 | `javascript` | 3 | 2026-07-03 |
| [**herdr-github**](https://github.com/mrolafsson/herdr-github)<br><sub>mrolafsson</sub> | GitHub pull requests in a herdr popup: merge readiness, checks and reviews, draft toggle, merge or auto-merge, one key to a worktree (forks too), and PR labels… | `bubbletea` `claude-code` `coding-agents` `git-worktree` `github` | 3 | 🔄 2026-10-20 |
| [**herdr-board**](https://github.com/bredebjorhovd/herdr-board)<br><sub>bredebjorhovd</sub> | 编程 Agent 排队并自主完成工作的地方——输入 GitHub issue，自主 Agent 在 herdr 窗格中运行，PR 评审会返回给编写它的那个 Agent | `rust` | 2 | 2026-08-14 |
| [**herdr-pr-watch**](https://github.com/maxguzenski/herdr-pr-watch)<br><sub>maxguzenski</sub> | Herdr 插件：在侧边栏显示每个工作区和 Agent 窗格对应的 GitHub PR 状态。 | `github-pull-requests` `python` | 2 | 2026-09-06 |
| [**herdr-issues**](https://github.com/zamarrowski/herdr-issues)<br><sub>zamarrowski</sub> | herdr 插件：浏览当前所在仓库的 GitHub、Linear 和 Shortcut 工单，并将其交给任意编码 Agent（Claude Code、Codex、Gemini 等），在其专属 git worktree 中处理。 | `coding-agents` `github-issues` `javascript` | 2 | 2026-09-30 |
| [**herdr-dashboard**](https://github.com/chouxcreams/herdr-dashboard)<br><sub>chouxcreams</sub> | herdr 工作区的 PR 状态仪表盘 TUI——一目了然地查看每个窗格对应的 PR 状态/CI/审查情况 | `dashboard` `github` `pull-requests` `ratatui` `rust` | 1 | 2026-07-28 |
| [**herdr-plugin-gh**](https://github.com/ecklf/herdr-plugin-gh)<br><sub>ecklf</sub> | GitHub PR and CI status in Herdr's Agents sidebar, with open/create PR and failing-check actions. | `github-cli` `terminal` `go` | 1 | 🔄 2026-10-15 |
| [**🆕 herdr-ingest**](https://github.com/H3xept/herdr-ingest)<br><sub>H3xept</sub> | 为来自 Sentry、Linear、GitHub 或任意 JSON 数据管道的每个工作项，创建一个独立的 herdr 空间。 | `github` `linear` `sentry` `terminal` `shell` | 1 | 2026-09-26 |
| [**herdr-plugin-github-status**](https://github.com/jwanga/herdr-plugin-github-status)<br><sub>jwanga</sub> | herdr 插件：以侧边栏宽度停靠在右侧，实时展示 GitHub 项目状态（里程碑、issue、PR、Actions）。 | `github` `rust` `tui` | 1 | 2026-09-19 |
| [**🆕 github-issue-herdr-plugin**](https://github.com/nyanyaon/github-issue-herdr-plugin)<br><sub>nyanyaon</sub> | 用于「牧养」GitHub issue 的 Claude Code 插件 | `rust` | 1 | 2026-07-27 |
| [**subscription-watcher**](https://github.com/PurrlyDigital/subscription-watcher)<br><sub>PurrlyDigital</sub> | Claude Code and Codex subscription allowance in the Herdr sidebar. Read-only mirror; open issues and merge requests on GitLab. | `python` | 1 | 2026-10-06 |
| [**herdr-ci-checks**](https://github.com/tdi/herdr-ci-checks)<br><sub>tdi</sub> | herdr 插件：在右侧窗格中实时显示当前分支的 GitHub/GitLab CI 检查状态。 | `javascript` | 1 | 2026-09-25 |
| [**agent-checks**](https://github.com/timmo001/agent-checks)<br><sub>timmo001</sub> | CI and lint status for Herdr workspaces, with an Omarchy panel | `gh-cli` `github-workflows` `typescript` | 1 | 🔄 2026-10-26 |

<details><summary>与此目的也相关</summary>

- [tomasvarga/herdr-pickr](https://github.com/tomasvarga/herdr-pickr) — herdr 的 PR 审查路由器——按住 Ctrl 点击 GitHub PR / GitLab MR 链接，选择审查工具（tuicr · hunk · diff · 浏览器 · 或自定义工具），可选启用 AI 初审
- [tdi/herdr-worktree-from-pr](https://github.com/tdi/herdr-worktree-from-pr) — 从 GitHub PR 创建 git 工作树，并作为 herdr 工作区打开
- [zhuravel/magnum](https://github.com/zhuravel/magnum) — Your AI coding agents as a pull-request review team: Claude Code, Codex and others review each push in herdr…
- [jakekroon/herdr-pr-tracker](https://github.com/jakekroon/herdr-pr-tracker) — 将你所创建的所有未关闭拉取请求以停靠面板形式展示，并按你需要处理的紧迫程度进行颜色标注。一个 Herdr 插件
- [kiitosu/herdr-jira-board](https://github.com/kiitosu/herdr-jira-board) — 在 herdr 中运行的 Jira 看板，附带 Claude Code 会话启动器
- [tferreira/herdr-pr-ops](https://github.com/tferreira/herdr-pr-ops) — PR//OPS - pull request mission control for Herdr: your PRs and review requests on one board, one-key agents i…
- [kkjdaniel/herdr-gh-runs](https://github.com/kkjdaniel/herdr-gh-runs) — GitHub Actions runs in a herdr pane: follows your repo, live status, step logs and notifications
- [poislagarde/herdr-worktree-cleanup](https://github.com/poislagarde/herdr-worktree-cleanup) — 当对应的 Herdr 空间关闭时，自动清理可安全删除的 GitHub PR worktree。Python 编写，无依赖，MIT 许可。

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-layout"></a>

## 工作区与布局搭建

> 打开项目时，希望标签页、窗格和启动命令一次性就位

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-spreader**](https://github.com/yuk1ty/herdr-spreader)<br><sub>yuk1ty</sub> | 从一个 YAML 文件启动整套 herdr 工作区布局——标签页、窗格、命令，一次搞定 | `rust` | 140 | 2026-08-16 |
| [**dotfiles**](https://github.com/lararosekelley/dotfiles)<br><sub>lararosekelley</sub> | 👩‍💻 my dotfiles, plus a whole lot more | `bash` `bootstrap` `dotfiles` `homebrew` `macos` | 52 | 🔄 2026-10-21 |
| [**herdr-plugin-workspace-manager**](https://github.com/razajamil/herdr-plugin-workspace-manager)<br><sub>razajamil</sub> | 声明式的标签页/窗格布局，创建工作树时自动应用每个工作区的默认设置 | `rust` | 50 | 2026-08-23 |
| [**seshagy**](https://github.com/lmilojevicc/seshagy)<br><sub>lmilojevicc</sub> | 面向 tmux 和 herdr 的 Agent 感知会话管理器——发现项目、启动会话、追踪 AI Agent 的工作 | `bubbletea` `go` `session-management` `session-manager` `terminal` | 21 | 🔄 2026-10-22 |
| [**herdr-sidebar-config**](https://github.com/testy-cool/herdr-sidebar-config)<br><sub>testy-cool</sub> | 面向 Herdr 的工作区 → 标签页 → Agent 侧边栏预设，将单标签分组显示得更紧凑，配有易读的任务标签和服务商图标。 | `ai-agents` `claude-code` `codex` `configuration` `ghostty` | 13 | 🔄 2026-10-23 |
| [**herdr-grid**](https://github.com/thuanlm215/herdr-grid)<br><sub>thuanlm215</sub> | Herdr 的可视化窗格布局编辑器，支持拖放操作、新建 shell、可复用布局，以及跨标签页和工作区发送窗格。 | `layout-presets` `pane-layout` `productivity` `ratatui` `rust` | 13 | 2026-10-11 |
| [**herdr-warp**](https://github.com/HexSleeves/herdr-warp)<br><sub>HexSleeves</sub> | 将 Herdr 工作区作为原生 Warp 窗格打开 | `shell` | 9 | 2026-07-25 |
| [**glyph**](https://github.com/fru-dev3/glyph)<br><sub>fru-dev3</sub> | 为你运行的每一个编码 Agent 赋予一个身份标识。为 Claude Code、Antigravity、Codex 或 Gemini 的每个会话打上你的标签、项目、机器和时间戳。 | `ai-agents` `claude-code` `cli` `codex` `developer-tools` | 6 | 🔄 2026-10-26 |
| [**herdr-session-manager**](https://github.com/umutciloglu/herdr-session-manager)<br><sub>umutciloglu</sub> | 面向 herdr 的 Agent 会话管理器，支持跨 harness 消息传递。 | `rust` | 5 | 🔄 2026-10-21 |
| [**herdr-workspace-organizer**](https://github.com/cesmunoz/herdr-workspace-organizer)<br><sub>cesmunoz</sub> | Herdr Workspace Organizer | `typescript` | 4 | 🔄 2026-10-16 |
| [**herdr-clone-layout**](https://github.com/danilolucasmd/herdr-clone-layout)<br><sub>danilolucasmd</sub> | Clone your workspace layout onto every new herdr worktree. No templates, no config, the layout you're in is the template. | `shell` | 4 | 2026-08-27 |
| [**herdr-fork-from-message**](https://github.com/dmangla3/herdr-fork-from-message)<br><sub>dmangla3</sub> | 从更早的一条消息处分叉出 Codex 或 Claude Code，并在新的 Herdr 标签页、窗格或工作区中打开 | `claude-code` `codex` `developer-tools` `terminal-multiplexer` `python` | 4 | 2026-08-10 |
| [**herdr-pane-layouts**](https://github.com/iurysza/herdr-pane-layouts)<br><sub>iurysza</sub> | 面向 Herdr 的无缝 tmux 风格窗格调整大小和布局 | `pane-layout` `python` `terminal` | 4 | 🔄 2026-10-21 |
| [**herdr-muster**](https://github.com/marcoskichel/herdr-muster)<br><sub>marcoskichel</sub> | 面向 herdr 的、感知 Agent 状态的项目切换器 | `rust` | 4 | 2026-07-03 |
| [**dsh-plugin-herdr**](https://github.com/sunny0826/dsh-plugin-herdr)<br><sub>sunny0826</sub> | 面向 DeepSeek Harness（DSH）的 Herdr 控制平面插件——从 DSH 会话中观察并驱动 Herdr（面向 AI 编程 Agent 的终端工作区管理器） | `dsh-plugin` `typescript` | 4 | 2026-08-25 |
| [**herdr-layout-tools**](https://github.com/edouard-andrei/herdr-layout-tools)<br><sub>edouard-andrei</sub> | herdr 插件：原地重塑布局（主窗格居左+网格）并均分——标签页 ID 和窗格 ID 保持不变，进程也得以保留 | `javascript` | 3 | 2026-08-06 |
| [**herdr-auto-layout**](https://github.com/ExLuna-rs/herdr-auto-layout)<br><sub>ExLuna-rs</sub> | Declarative layouts applied to every new workspace — cross-platform herdr plugin | `layout` `rust` `terminal` | 3 | 2026-09-30 |
| [**herdr-compose**](https://github.com/ropali/herdr-compose)<br><sub>ropali</sub> | herdr-compose 是面向 Herdr 的声明式工作区布局管理器 | `layout-manager` `python` | 3 | 🔄 2026-10-14 |
| [**herdr-setup-bootstrap**](https://github.com/shizlie/herdr-setup-bootstrap)<br><sub>shizlie</sub> | 根据 worktree_init.toml 初始化新工作树的 Herdr 插件 | `shell` | 3 | 2026-06-17 |
| [**herdr-google-gmail**](https://github.com/Tomatio13/herdr-google-gmail)<br><sub>Tomatio13</sub> | herdr-google-gmail 是面向终端工作区工具 herdr 的 Gmail 集成插件 | `shell` | 3 | 2026-07-22 |
| [**herdr-layout**](https://github.com/3mmdrew/herdr-layout)<br><sub>3mmdrew</sub> | 面向 herdr 的极简工作区布局——输入一个 Lua 文件即可得到工作区。无依赖、无守护进程、无 YAML | `lua` `terminal` | 2 | 2026-08-04 |
| [**herdr-medieval**](https://github.com/gabrielbarretoo/herdr-medieval)<br><sub>gabrielbarretoo</sub> | 将工作区和 Agent 以六边形中世纪大陆的形式进行 3D 展示的 Herdr 插件——每个工作区是一座围栏营地，每个窗格是一名冒险者，会根据 Agent 状态训练、在营火旁休息或在塔楼站岗。内嵌 three.js，无需联网、无依赖 | `3d` `hex-grid` `threejs` `javascript` | 2 | 2026-08-06 |
| [**herdr-better-workspace**](https://github.com/hamzahraihan/herdr-better-workspace)<br><sub>hamzahraihan</sub> | 面向 herdr（AI 编码 Agent 的终端工作区管理器）的交互式「打开工作区」选择器插件。 | `go` | 2 | 2026-09-09 |
| [**herdr-mcp**](https://github.com/thomasfossum/herdr-mcp)<br><sub>thomasfossum</sub> | Model Context Protocol server for Herdr: full remote control of workspaces, tabs, panes, agents and worktrees. Dependency-free Python. | `agents` `mcp` `model-context-protocol` `terminal` `python` | 2 | 🔄 2026-10-12 |
| [**herdr-google-calendar**](https://github.com/Tomatio13/herdr-google-calendar)<br><sub>Tomatio13</sub> | herdr-gog-calendar 是面向终端工作区工具 herdr 的 Google 日历集成插件 | `shell` | 2 | 2026-07-22 |
| [**reasonix-herdr**](https://github.com/uuie/reasonix-herdr)<br><sub>uuie</sub> | 在 Herdr 内提供实时生命周期报告和工作区控制的原生 Reasonix 插件 | `reasonix` `python` | 2 | 2026-07-10 |
| [**herdr-workspace**](https://github.com/zackshen/herdr-workspace)<br><sub>zackshen</sub> | herdr 插件：从居中弹窗创建工作区并应用布局配置 | `rust` | 2 | 2026-08-24 |
| [**herdr-dwm-layout**](https://github.com/42lizard/herdr-dwm-layout)<br><sub>42lizard</sub> | 面向 Herdr 的 DWM 风格 master/stack 布局 | `dwm` `fzf` `rust` `shell` `tiling` | 1 | 2026-08-28 |
| [**herdr-better-worktrees**](https://github.com/bearylabs/herdr-better-worktrees)<br><sub>bearylabs</sub> | 一个快速的 Herdr 弹窗，用于以可预测的 embedded-bare 布局管理 Git worktree：支持创建、克隆、打开、查看、拉取以及安全移除 worktree。 | `typescript` | 1 | 2026-09-18 |
| [**herdr-spinup**](https://github.com/Royal-lobster/herdr-spinup)<br><sub>Royal-lobster</sub> | 每个新建 herdr 标签页的启动界面——选择一个工具，即会在该标签页中运行。工具通过 JSON 定义 | `javascript` | 1 | 2026-08-04 |
| [**🆕 herdr-new-workspace**](https://github.com/bethanyj28/herdr-new-workspace)<br><sub>bethanyj28</sub> | Pop up new workspace modal for herdr | `shell` | 0 | 🔄 2026-10-23 |
| [**🆕 herdr-powertoys**](https://github.com/m16khb-org/herdr-powertoys)<br><sub>m16khb-org</sub> | Herdr plugin: equalize split panes, snap a split to half, or cycle 1/2, 2/3, 1/3 | `layout` `panes` `perl` `tiling` | 0 | 2026-10-09 |

<details><summary>与此目的也相关</summary>

- [andrewchng/herdr-sessionizer](https://github.com/andrewchng/herdr-sessionizer) — 通过模糊搜索打开项目和工作树，再从声明式 TOML 布局（标签页、窗格分割、命令、按仓库覆盖配置）启动工作区
- [fullerzz/herdr-plugin-sesh](https://github.com/fullerzz/herdr-plugin-sesh) — 面向 Herdr 的 Sesh 风格工作区选择器 TUI，集成 zoxide，可从常用目录创建工作区
- [ntindle/herdr-resurrect](https://github.com/ntindle/herdr-resurrect) — herdr 的 tmux-resurrect——快照工作区、标签页、窗格、当前目录、运行中的程序和 Agent，并在崩溃或重启后恢复
- [enekos/herdr-quick-actions](https://github.com/enekos/herdr-quick-actions) — 以 fzf 选择器调用 herdr 原生的标签页/窗格/工作区操作，按使用频率排序——不必再死记快捷键
- [crierr/herdr-arrange](https://github.com/crierr/herdr-arrange) — 用于 herdr 窗格移动/交换/重新分屏/布局调整的交互式弹窗 UI
- [salkhalil/herdr-sessionizer](https://github.com/salkhalil/herdr-sessionizer) — herdr 的 tmux-sessionizer：用 fzf 搜索已打开的工作区和 zoxide 目录，创建或聚焦并附带模板标签页
- [aliou/herdr-cast](https://github.com/aliou/herdr-cast) — 个人 Herdr 插件——提供原生 macOS Agent 通知、模糊工作区导航、基于 zoxide 的工作区创建以及布局命令
- [chandrasekharan98/herdr-workspace-save](https://github.com/chandrasekharan98/herdr-workspace-save) — 保存 Herdr 工作区（布局、工作目录、Agent 会话、正在运行的命令），之后可从 fzf 选择器中重新打开
- [cantona/herdr-revive](https://github.com/cantona/herdr-revive) — 恢复 Herdr 的命令、布局以及完全一致的 Agent 会话，支持预览、具名工作区和明确的恢复操作。
- [42lizard/herdr-sessionizer](https://github.com/42lizard/herdr-sessionizer) — tmux-sessionizer 风格的 herdr 插件

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-navigate"></a>

## 窗格导航与快捷键

> 想用和编辑器一样的快捷键在窗格、工作区之间移动和调整大小

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**vim-herdr-navigation**](https://github.com/paulbkim-dev/vim-herdr-navigation)<br><sub>paulbkim-dev</sub> | 用 Ctrl+h/j/k/l 在 herdr 窗格与 Vim/Neovim 分屏之间无缝导航——vim-tmux-navigator 的 herdr 移植版 | `neovim` `vim` `shell` | 112 | 2026-10-10 |
| [**herdr-splits.nvim**](https://github.com/lmilojevicc/herdr-splits.nvim)<br><sub>lmilojevicc</sub> | 面向 Herdr 和 Neovim 的智能分屏导航与调整大小 | `lua` `neovim` `neovim-plugin` `neovim-plugins` `nvim` | 69 | 2026-08-17 |
| [**herdr-floax**](https://github.com/Tyru5/herdr-floax)<br><sub>Tyru5</sub> | herdr 的浮动临时终端——类似 tmux-floax 风格的可切换弹窗，每个工作区一个，会话持久保存 | `rust` `terminal` `tmux-floax` | 28 | 🔄 2026-10-23 |
| [**herdr-nvim-nav**](https://github.com/aimdevlee/herdr-nvim-nav)<br><sub>aimdevlee</sub> | 在 herdr 窗格与 Neovim 分屏之间无缝使用 Ctrl+h/j/k/l——基于 socket，无需每次按键都启动进程 | `neovim` `neovim-plugin` `lua` | 23 | 2026-08-02 |
| [**herdr-recent-navigator**](https://github.com/beyondlex/herdr-recent-navigator)<br><sub>beyondlex</sub> | 在最近使用的工作区、标签页、窗格和 Agent 之间进行 MRU（最近使用）切换——类似 JetBrains 的「最近文件」。此外还支持对任意窗格内容进行模糊搜索，完全由键盘驱动。 | `agent` `mru` `navigator` `pane` `popup` | 22 | 🔄 2026-10-18 |
| [**herdr-last-workspace**](https://github.com/third774/herdr-last-workspace)<br><sub>third774</sub> | 用于切换回上一个聚焦的工作区的插件 | `rust` | 19 | 2026-06-22 |
| [**herdr-command-center**](https://github.com/speardragon/herdr-command-center)<br><sub>speardragon</sub> | 一个快捷键统管所有命令——一个列出你注册命令的 herdr 弹窗，用方向键或数字执行，并在命令触发前自动关闭 | `command-palette` `nodejs` `terminal` `toml` `tui` | 18 | 🔄 2026-10-19 |
| [**herdr-pane-mover**](https://github.com/osamahbeig/herdr-pane-mover)<br><sub>osamahbeig</sub> | herdr 的可点击浮层菜单：跨标签页和工作区移动、重新分割或交换窗格 | `terminal` `tui` `javascript` | 15 | 2026-07-10 |
| [**herdr-cliamp**](https://github.com/coryshaw1/herdr-cliamp)<br><sub>coryshaw1</sub> | 面向 herdr 的浮动 cliamp，隐藏后仍会继续播放——播放器运行在一个分离的 herdr 会话中，因此关闭浮层只是分离而已 | `audiobook` `cliamp` `music-player` `podcast` `terminal` | 14 | 2026-08-24 |
| [**herdr-logbook**](https://github.com/Resetnak/herdr-logbook)<br><sub>Resetnak</sub> | 终端的工作记忆——离线、以 Markdown 为主的笔记、决策记录，以及 Herdr 的当前任务 now.md | `adr` `bubbletea` `cli` `go` `markdown` | 13 | 🔄 2026-10-15 |
| [**herdr-profiles**](https://github.com/GiorgiTarsaidze/herdr-profiles)<br><sub>GiorgiTarsaidze</sub> | 面向 Herdr 的 Chrome 风格配置文件：通过弹窗选择器切换相互隔离的空间集合。 | `rust` `terminal` | 12 | 2026-09-14 |
| [**herdr-paddock**](https://github.com/neyham/herdr-paddock)<br><sub>neyham</sub> | 🐑 面向 herdr Agent 的卡片墙动态流——一览整个羊群，放大查看单个 Agent 并回复，全部通过普通 SSH 完成 | `bubbletea` `go` `ssh` `tui` | 12 | 🔄 2026-10-23 |
| [**musicforprogramming**](https://github.com/pivoshenko/musicforprogramming)<br><sub>pivoshenko</sub> | 🎧 面向 musicforprogramming.net 的 TUI，使用 Rust 编写。 | `ambient` `audio` `daemon` `developer-tools` `focus` | 12 | 🔄 2026-10-21 |
| [**herdr-equalize-panes**](https://github.com/shibayu36/herdr-equalize-panes)<br><sub>shibayu36</sub> | 在分屏和关闭时自动均分窗格大小的 herdr 插件（相当于自动执行 tmux 的 select-layout -E） | `terminal` `perl` | 11 | 2026-08-22 |
| [**herdr-trail**](https://github.com/catoncat/herdr-trail)<br><sub>catoncat</sub> | herdr 全局共享的备忘录——Agent 记下待跟进事项，人类通过一份全局列表统一管理，每条记录都可跳回其来源对话 | `javascript` | 9 | 2026-08-26 |
| [**terminal-markdown-renderer**](https://github.com/slara/terminal-markdown-renderer)<br><sub>slara</sub> | tmdview: view Markdown rendered as HTML in a browser inside your terminal. A personal tool, written with AI. | `cli` `markdown` `rust` `terminal` | 9 | 🔄 2026-10-18 |
| [**herdr-arrange**](https://github.com/crierr/herdr-arrange)<br><sub>crierr</sub> | 用于 herdr 窗格移动/交换/重新分屏/布局调整的交互式弹窗 UI | `go` | 8 | 2026-09-05 |
| [**herdr-omnisearch**](https://github.com/dmnkf/herdr-omnisearch)<br><sub>dmnkf</sub> | 跨所有已连接的机器，对 Herdr 的工作区、窗格及归档的 Agent 会话进行快速搜索与导航。 | `python` | 8 | 🔄 2026-10-21 |
| [**herdr-last**](https://github.com/lmilojevicc/herdr-last)<br><sub>lmilojevicc</sub> | 切换回 Herdr 中上一个活动的工作区或标签页 | `go` `linux` `macos` `productivity` `tabs` | 8 | 2026-08-07 |
| [**herdr-toggle-popup**](https://github.com/maro114510/herdr-toggle-popup)<br><sub>maro114510</sub> | 一个快捷键即可切换浮层弹窗终端的 Herdr 插件 | `go` | 8 | 🔄 2026-10-25 |
| [**nvim-herdr-navigation**](https://github.com/bojackduy/nvim-herdr-navigation)<br><sub>bojackduy</sub> | vim-tmux-navigator 风格的 ctrl+h/j/k/l，在 Neovim 分屏和 Herdr 窗格之间导航 | `keyboard-shortcuts` `lazyvim` `lua` `navigation` `neovim` | 7 | 2026-07-20 |
| [**herdr-git**](https://github.com/JeHwanYoo/herdr-git)<br><sub>JeHwanYoo</sub> | 一款专注于核心功能的 Herdr Git 客户端。 | `git` `rust` | 7 | 🔄 2026-10-21 |
| [**herdr-scratch**](https://github.com/AkashJana18/herdr-scratch)<br><sub>AkashJana18</sub> | 面向 Herdr 的持久化速记板，为浮动实用窗格铺路 | `cli` `rust` `scratchpad` | 6 | 2026-09-20 |
| [**herdr-which-key**](https://github.com/CowboyVang/herdr-which-key)<br><sub>CowboyVang</sub> | 面向 herdr 的 which-key 风格键位映射浮层——按一个键即可看到 prefix 下所有按键绑定的分组和标签，再按第二个键即可执行。需主动呼出，而非长按显示。零依赖 | `keybindings` `terminal` `which-key` `python` | 6 | 2026-09-15 |
| [**herdr-swipe**](https://github.com/husniadil/herdr-swipe)<br><sub>husniadil</sub> | 面向 Herdr 的触控板手势——可在窗格、标签页和空间之间移动，并跳转到正在等待你的 Agent | `cgeventtap` `gestures` `macos` `python` `terminal` | 6 | 2026-08-20 |
| [**nvim-herdr-navigator**](https://github.com/kaar/nvim-herdr-navigator)<br><sub>kaar</sub> | 在 Neovim 分屏与 herdr 窗格之间无缝导航——一套 `ctrl+h/j/k/l` 按键即可同时穿梭于 vim 和 herdr 窗格 | `neovim` `neovim-plugin` `shell` | 6 | 2026-10-03 |
| [**herdr-voice**](https://github.com/aneym/herdr-voice)<br><sub>aneym</sub> | herdr 的语音控制——通过语音创建空间、拆分窗格并驱动编程 Agent。基于 OpenAI Realtime，带实时听写文本的浮动 HUD | `openai-realtime-api` `voice` `javascript` | 5 | 2026-09-25 |
| [**herdr-annotations**](https://github.com/jagzmz/herdr-annotations)<br><sub>jagzmz</sub> | 通过快速的本地优先弹窗和可复用的收藏集，为 Herdr 中选中的终端文本添加注释 | `annotations` `cli` `coding-agents` `developer-tools` `local-first` | 5 | 2026-07-16 |
| [**herdr-attention**](https://github.com/milkyskies/herdr-attention)<br><sub>milkyskies</sub> | herdr 插件：按一个键即可跳转到下一个需要关注的 Agent（先是被阻塞的，然后是已完成的） | `javascript` | 5 | 2026-07-08 |
| [**herdr-easyjump**](https://github.com/xzedx/herdr-easyjump)<br><sub>xzedx</sub> | 按下一个键、输入一个字母，即可跳转到任意空间、Agent、窗格或标签页。采用 EasyMotion / Vimium / vim-choosewin 风格的提示标签，直接绘制在 Herdr 侧边栏中。 | `choosewin` `easymotion` `hints` `navigation` `rust` | 5 | 2026-09-14 |
| [**🆕 reficus**](https://github.com/81zi/reficus)<br><sub>81zi</sub> | Grow the focused pane and shrink the others on every focus change | `python` | 4 | 🔄 2026-10-21 |
| [**herdr-tmux-session-navigator**](https://github.com/caneppelevitor/herdr-tmux-session-navigator)<br><sub>caneppelevitor</sub> | 面向 herdr 的 tmux choose-tree。作者已经告别了 tmux，却始终舍不得 prefix+s 这个习惯。 | `bubbletea` `terminal` `tmux` `go` | 4 | 2026-09-18 |
| [**herdr-unread-marker**](https://github.com/JoanGil/herdr-unread-marker)<br><sub>JoanGil</sub> | 通过快捷键手动将聚焦中的 Agent 标记为已读/未读（仅支持手动） | `shell` | 4 | 2026-07-17 |
| [**herdr-harpoon**](https://github.com/KonstantinKai/herdr-harpoon)<br><sub>KonstantinKai</sub> | herdr 的 Harpoon：给窗格打标记，按编号跳转。纯 Bash 实现，无需构建 | `bash` `harpoon` `tmux-harpoon` `shell` | 4 | 2026-07-29 |
| [**herdr-normal-mode**](https://github.com/maedana/herdr-normal-mode)<br><sub>maedana</sub> | 面向 herdr 侧边栏的 Vim 风格普通模式——j/k 移动行，h/l 切换标签页，0-9 选择窗格 | `rust` `tui` | 4 | 2026-08-24 |
| [**herdr-equalize-splits**](https://github.com/markhuot/herdr-equalize-splits)<br><sub>markhuot</sub> | herdr 插件：将当前标签页中所有分屏按行/列均分尺寸（绑定到 Ctrl+b =） | `terminal` `tmux` `javascript` | 4 | 2026-07-08 |
| [**herdr-smart-nav**](https://github.com/odiumuniverse/herdr-smart-nav)<br><sub>odiumuniverse</sub> | 跨 nvim 窗口、herdr 窗格、标签页与工作区的智能 Ctrl+h/j/k/l 导航。 | `navigation` `neovim` `neovim-plugin` `nvim` `nvim-lua` | 4 | 2026-09-14 |
| [**herdr-pretty-which**](https://github.com/ramarivera/herdr-pretty-which)<br><sub>ramarivera</sub> | 面向 Herdr 的 Rust/Ratatui which-key 风格快捷键浮层 | `ratatui` `rust` `terminal` `tui` `which-key` | 4 | 🔄 2026-10-22 |
| [**herdr-account-switch**](https://github.com/rcosteira79/herdr-account-switch)<br><sub>rcosteira79</sub> | 无需重新认证即可热切换 Claude Code / Codex 登录。提供浮层选择器、切换到下一个的快捷键，以及按窗格显示的账号徽章（$acct） | `python` | 4 | 2026-09-23 |
| [**herdr-navigator**](https://github.com/willfish/herdr-navigator)<br><sub>willfish</sub> | 面向 Vim/Neovim 感知窗格移动的 Herdr 端导航操作 | `navigation` `neovim` `rust` | 4 | 2026-07-07 |
| [**herdr-pane-switcher**](https://github.com/AlexanderGrooff/herdr-pane-switcher)<br><sub>AlexanderGrooff</sub> | 通过快捷键将注意力切换到高优先级的 Herdr 窗格。 | `rust` | 3 | 2026-08-27 |
| [**herdr-convo-index**](https://github.com/dzwduan/herdr-convo-index)<br><sub>dzwduan</sub> | herdr 中 Claude Code 窗格的轮次索引——跳转到任意历史轮次并在弹窗中查看 | `python` | 3 | 2026-07-27 |
| [**herdr-aspire-hud**](https://github.com/H3xept/herdr-aspire-hud)<br><sub>H3xept</sub> | 为每个 herdr 空间实时显示 .NET Aspire AppHost 的健康状态：侧边栏徽章与弹窗 HUD。 | `apphost` `aspire` `dotnet-aspire` `terminal` `tui` | 3 | 2026-09-26 |
| [**herdr-pane-shift**](https://github.com/Hon-Lu/herdr-pane-shift)<br><sub>Hon-Lu</sub> | Herdr plugin for rearranging panes from the keyboard: swap, break into a tab, rotate splits, and place beside any pane. | `terminal` `tmux-alternative` `javascript` | 3 | 2026-10-07 |
| [**herdr-popupx**](https://github.com/jeromychu23/herdr-popupx)<br><sub>jeromychu23</sub> | 面向 Herdr 的持久化原生浮动速记弹窗 | `rust` `terminal` `tui` | 3 | 2026-07-21 |
| [**herdr-next-agent**](https://github.com/martin-ro/herdr-next-agent)<br><sub>martin-ro</sub> | Herdr 插件：按可配置的状态优先级，跳转到下一个需要关注的 Agent | `python` | 3 | 2026-09-10 |
| [**herdr-float**](https://github.com/meerzulee/herdr-float)<br><sub>meerzulee</sub> | 类似 Zellij 的 ALT+F 浮动窗格 | `shell` | 3 | 2026-07-20 |
| [**🆕 herdr-file-transfer**](https://github.com/mrolafsson/herdr-file-transfer)<br><sub>mrolafsson</sub> | Running herdr on a VPS or remote box (Hetzner, a cloud dev server) and uploading files is a pain? Drop them on a popup and they're copied over ssh into your ag… | `bubbletea` `claude-code` `coding-agents` `file-transfer` `go` | 3 | 🔄 2026-10-22 |
| [**herdr-confirm-close-pane**](https://github.com/poweroutlet2/herdr-confirm-close-pane)<br><sub>poweroutlet2</sub> | 在关闭窗格前询问确认的 herdr 插件，类似 tmux 的 prefix+x confirm-before | `shell` | 3 | 2026-07-06 |
| [**herdr-ask-inbox**](https://github.com/speardragon/herdr-ask-inbox)<br><sub>speardragon</sub> | 将所有 herdr 工作区中被阻塞的 Claude AskUserQuestion 提示汇总到一个弹窗中，就地回答，绝不会把答案发错 Agent | `claude-code` `javascript` | 3 | 2026-07-25 |
| [**herdr-unread-jump**](https://github.com/to4iki/herdr-unread-jump)<br><sub>to4iki</sub> | 跳转到下一个需要关注的 Herdr Agent 窗格（先是被阻塞的，然后是已完成的） | `agents` `bash` `shell` | 3 | 2026-08-30 |
| [**herdr-mission-control**](https://github.com/vjeantet/herdr-mission-control)<br><sub>vjeantet</sub> | herdr 的 Mission Control：按一个键，将工作区所有窗格按标签页分组，以实时平铺网格展示，选中即可切换过去。 | `expose` `mission-control` `terminal` `tui` `rust` | 3 | 2026-09-20 |
| [**herdr-next-agent**](https://github.com/choplin/herdr-next-agent)<br><sub>choplin</sub> | 在处于所配置语义状态的 Herdr Agent 之间移动 | `go` | 2 | 2026-08-24 |
| [**herdr-tmux-layout**](https://github.com/crierr/herdr-tmux-layout)<br><sub>crierr</sub> | 面向运行中的 Herdr 窗格的 tmux 风格预设布局——支持 cycle、even-horizontal、even-vertical、main-horizontal、main-vertical、tiled 和 balance | `go` | 2 | 2026-08-30 |
| [**herdr-equalize-vsplit**](https://github.com/devoc09/herdr-equalize-vsplit)<br><sub>devoc09</sub> | 将当前窗格向右分屏并均分列宽的 Herdr 插件 | `go` | 2 | 2026-07-15 |
| [**herdr-crossroads**](https://github.com/eisenhauer-dev/herdr-crossroads)<br><sub>eisenhauer-dev</sub> | Navigate your Herdr. Find your sheep when you need them. | `rust` | 2 | 🔄 2026-10-21 |
| [**herdr-easymotion**](https://github.com/elliotekj/herdr-easymotion)<br><sub>elliotekj</sub> | 🦘 在 Herdr 窗格之间直接跳转 | `javascript` | 2 | 2026-07-20 |
| [**worktree-fleet**](https://github.com/hasuwini77/worktree-fleet)<br><sub>hasuwini77</sub> | Parallel Claude Code / Codex builds on Herdr: /herd splits a task into worktree buckets, plus a live fleet popup | `claude-code` `codex` `git-worktree` `shell` | 2 | 2026-09-29 |
| [**herdr-break-pane**](https://github.com/iuhoay/herdr-break-pane)<br><sub>iuhoay</sub> | 将聚焦窗格移动到新标签页的小型 Herdr 插件 | `pane` `javascript` | 2 | 🔄 2026-10-22 |
| [**herdr-grid-slide**](https://github.com/jeiea/herdr-grid-slide)<br><sub>jeiea</sub> | A plugin born from the idea of focusing and moving panes with hjkl. | `navigation` `rust` | 2 | 🔄 2026-10-17 |
| [**herdr-prevtab**](https://github.com/joo-was-already-taken/herdr-prevtab)<br><sub>joo-was-already-taken</sub> | 切换到上一个聚焦标签页的 Herdr 插件 | `rust` | 2 | 2026-10-04 |
| [**herdr-plan-meter**](https://github.com/JunSeo99/herdr-plan-meter)<br><sub>JunSeo99</sub> | 在 herdr 标签栏中显示 Claude Code 和 Codex 的套餐限额，并可通过弹窗查看详情。仅使用 Python 标准库的单文件实现，凭据只读访问。 | `claude-code` `codex` `rate-limit` `usage` `python` | 2 | 🔄 2026-10-13 |
| [**herdr-inbox**](https://github.com/LeaveMyYard/herdr-inbox)<br><sub>LeaveMyYard</sub> | Non-blocking question inbox for Claude Code agents in herdr: agents ask once and keep working, you answer from one popup | `claude-code` `claude-code-plugin` `mcp` `python` | 2 | 🔄 2026-10-22 |
| [**herdr-marks**](https://github.com/mcostasilva/herdr-marks)<br><sub>mcostasilva</sub> | Neovim-style letter marks for Herdr panes and workspaces, with colored sidebar labels and quick navigation | `rust` | 2 | 2026-10-06 |
| [**herdr-lazytask**](https://github.com/mdetweil/herdr-lazytask)<br><sub>mdetweil</sub> | 在 herdr 分屏窗格中使用 Lazytask（打开/聚焦/切换），并提供 Taskwarrior 快捷操作 | `lazytask` `taskwarrior` `terminal` `rust` | 2 | 2026-08-02 |
| [**herdr-quotr**](https://github.com/napalmpapalam/herdr-quotr)<br><sub>napalmpapalam</sub> | 通过 herdr 弹窗，把 Agent 自己的回答引用后再丢回给它 | `claude-code` `rust` `tui` | 2 | 2026-10-01 |
| [**grove-herdr**](https://github.com/nicksenap/grove-herdr)<br><sub>nicksenap</sub> | Herdr 插件：Grove 工作区创建弹窗，以及与 Herdr 工作区的桥接。 | `grove` `shell` | 2 | 🔄 2026-10-17 |
| [**herdr-topstrip**](https://github.com/orcchg/herdr-topstrip)<br><sub>orcchg</sub> | 将每个空间或已有空间上的标签页，以两个窗格的形式打开——上方是一条较窄的区域（通常用于目录导航、shell 命令和 git 操作），下方是较宽的区域（通常用于 Agent 会话）。 | `shell` | 2 | 2026-09-15 |
| [**herdr-plugin-agent-attention**](https://github.com/peterwiebe/herdr-plugin-agent-attention)<br><sub>peterwiebe</sub> | 跳转到最近被阻塞或已完成的 Agent 的 Herdr 插件。 | `python` | 2 | 2026-09-04 |
| [**herdr-equalize-panes**](https://github.com/ponko2/herdr-equalize-panes)<br><sub>ponko2</sub> | 在窗格被创建、关闭、移动或退出时，自动保持每个标签页内的窗格大小均匀 | `rust` | 2 | 🔄 2026-10-25 |
| [**herdr-pane-mover**](https://github.com/ronly2460/herdr-pane-mover)<br><sub>ronly2460</sub> | 通过交互式方向键选择器，在工作区之间移动 Herdr 窗格 | `terminal` `workspace` `shell` | 2 | 2026-08-23 |
| [**herdr-pane-orientation-switcher**](https://github.com/sf1tzp/herdr-pane-orientation-switcher)<br><sub>sf1tzp</sub> | 面向 Herdr 分屏窗格的工作流人体工学优化 | `shell` | 2 | 2026-07-25 |
| [**edger**](https://github.com/suderman/edger)<br><sub>suderman</sub> | 在 Herdr、tmux、Emacs、Neovim 的分屏之间无缝切换。 | `emacs` `emacs-package` `neovim` `neovim-plugin` `split-navigation` | 2 | 🔄 2026-10-17 |
| [**herdr-machine-manager**](https://github.com/vika2603/herdr-machine-manager)<br><sub>vika2603</sub> | 通过弹出式 TUI 管理 herdr 保存的 SSH 主机：可从 ~/.ssh/config 的别名添加、断开连接而不丢失配置、编辑目标地址。 | `bubbletea` `go` `ssh` `ssh-config` `terminal` | 2 | 2026-10-01 |
| [**herdr-hintr**](https://github.com/wraithyy/herdr-hintr)<br><sub>wraithyy</sub> | herdr 插件：which-key 风格的快捷键速查表弹窗——按下按键即可直接执行 | `shell` | 2 | 2026-08-11 |
| [**herdr-display-panes**](https://github.com/abroller666/herdr-display-panes)<br><sub>abroller666</sub> | tmux display-panes for Herdr: label every pane in the current tab and jump with one key | `tmux` `python` | 1 | 2026-10-07 |
| [**herdr-plugin-ide-jump**](https://github.com/agentience/herdr-plugin-ide-jump)<br><sub>agentience</sub> | 快速回到你的 IDE——将聚焦窗格所属项目的编辑器窗口置顶，或从可筛选的弹窗中选择一个。一个 Herdr 插件 | `python` | 1 | 2026-08-24 |
| [**herdr-hyprland**](https://github.com/aorumbayev/herdr-hyprland)<br><sub>aorumbayev</sub> | 受 Hyprland 启发，为 herdr 带来的操作方式。 | `ai-agents` `developer-tools` `golang` `hyprland` `keybindings` | 1 | 2026-09-04 |
| [**asconfirmclose**](https://github.com/asumaran/asconfirmclose)<br><sub>asumaran</sub> | Herdr 插件：关闭当前聚焦的窗格，仅当其中有进程正在运行时才会先行确认。 | `terminal` `go` | 1 | 2026-09-20 |
| [**🆕 claude-deck**](https://github.com/bigsan/claude-deck)<br><sub>bigsan</sub> | Watch Claude Code sessions: scratchpad files, tasks and every tool call, standalone or as a herdr plugin | `claude-code` `ratatui` `tui` `rust` | 1 | 🔄 2026-10-24 |
| [**herdr-scratchpad**](https://github.com/brunohq/herdr-scratchpad)<br><sub>brunohq</sub> | 为 herdr 打造的极简按标签页划分的 Markdown 便签本，支持带复选框的待办事项。 | `python` `scratchpad` `tui` | 1 | 2026-09-12 |
| [**herdr-plugin-tiles**](https://github.com/carsonjones/herdr-plugin-tiles)<br><sub>carsonjones</sub> | 面向 herdr 的简易窗格管理器 | `python` | 1 | 2026-06-19 |
| [**lazyherd**](https://github.com/chriopter/lazyherd)<br><sub>chriopter</sub> | 一个统揽你所有 Git 仓库的驾驶舱，可快速跳转到 lazygit 和 Herdr 工作区。 | `git` `lazygit` `tui` `go` | 1 | 2026-10-05 |
| [**herdr-terminal-scripts**](https://github.com/Fadi729/herdr-terminal-scripts)<br><sub>Fadi729</sub> | 一个 Herdr 插件，可通过弹窗或编号槽位运行具名脚本。 | `typescript` | 1 | 2026-09-21 |
| [**bindr**](https://github.com/itsmistermoon/bindr)<br><sub>itsmistermoon</sub> | 用于在具名快捷键配置之间切换，并可在弹窗中查看/编辑快捷键的 Herdr 插件。 | `rust` | 1 | 🔄 2026-10-20 |
| [**herdr-scratch**](https://github.com/macintacos/herdr-scratch)<br><sub>macintacos</sub> | 面向 herdr 的速记 shell——通过一个组合键开关的弹窗。底层基于 tmux，因此再次打开时会与离开时一模一样 | `go` | 1 | 2026-08-28 |
| [**herdr-plugins**](https://github.com/oullin/herdr-plugins)<br><sub>oullin</sub> | 面向 Herdr 的一组专注、可独立安装的插件合集 | `typescript` | 1 | 🔄 2026-10-20 |
| [**herdr-knapp**](https://github.com/shindakun/herdr-knapp)<br><sub>shindakun</sub> | 一个通过链接关系解析 Markdown 笔记的 Herdr 插件：支持反向链接、失效链接、孤立笔记以及链接关系图。 | `backlinks` `cli` `markdown` `notes` `obsidian` | 1 | 2026-09-24 |
| [**🆕 herdr-session-fork**](https://github.com/DanielGnzlzVll/herdr-session-fork)<br><sub>DanielGnzlzVll</sub> | Herdr plugin: fork the focused agent session into a sibling pane with one keystroke | `shell` | 0 | 2026-09-22 |
| [**🆕 herdr-plugin-recent-spaces**](https://github.com/mike-bronner/herdr-plugin-recent-spaces)<br><sub>mike-bronner</sub> | Herdr 插件：让空间侧边栏始终按最近使用顺序排列。 | `rust` | 0 | 2026-09-24 |
| [**🆕 herdr-whichkey**](https://github.com/Qu4tro/herdr-whichkey)<br><sub>Qu4tro</sub> | herdr 的 blezz/which-key 风格操作菜单——按下触发键后，每个操作只需一次按键，无需输入，无需回车 | `rust` | 0 | 2026-07-22 |
| [**🆕 herdr-close-other-panes**](https://github.com/reobin/herdr-close-other-panes)<br><sub>reobin</sub> | herdr 版的 vim ctrl-w o——关闭除聚焦窗格外的所有窗格 | `shell` | 0 | 2026-09-18 |

<details><summary>与此目的也相关</summary>

- [thanhdat77/herdr-navigator](https://github.com/thanhdat77/herdr-navigator) — 通过一个模糊导航器跳转到任意 Herdr 工作区、Agent、项目、会话、远程连接、目录或操作
- [speardragon/herdr-plugin-manager](https://github.com/speardragon/herdr-plugin-manager) — 在弹窗中管理 herdr 插件——安装、更新、启用/禁用、卸载，并浏览 herdr-plugin 市场。推荐快捷键：prefix+p
- [jorge07RD/herdr-ssh-manager](https://github.com/jorge07RD/herdr-ssh-manager) — 保存 SSH 主机，并从 Herdr 内的模糊弹窗中重新连接——按 Enter 即可直接将弹窗内容交给 ssh
- [vika2603/herdr-plugin-manager](https://github.com/vika2603/herdr-plugin-manager) — 通过弹窗或命令行浏览、安装和更新 herdr 插件。
- [purehate/herdr-plugin-picker](https://github.com/purehate/herdr-plugin-picker) — Herdr 的浮动弹窗选择器——可跳转到任意空间、Agent、标签页或窗格，向所有标记窗格广播同一条命令，并从 ~/.ssh/config 发起带实时可达性检测的 SSH 连接。完全由键盘驱动。
- [rheech22/herdr-comment-on-copy](https://github.com/rheech22/herdr-comment-on-copy) — Drag to select terminal text and open a comment popup automatically. Send feedback with context to AI agents…
- [victor-software-house/herdr-stash](https://github.com/victor-software-house/herdr-stash) — 储藏 Herdr 工作区——停止其中的 Agent，同时保留其结构和对话内容，之后可从可点击的双栏弹窗中恢复
- [karanpatel1993/herdr-nav](https://github.com/karanpatel1993/herdr-nav) — 在 herdr 中进行文件导航、代码搜索和 jdb 调试——将 fzf、ripgrep 与 Java 调试器接入你的终端工作区。
- [bearylabs/herdr-better-worktrees](https://github.com/bearylabs/herdr-better-worktrees) — 一个快速的 Herdr 弹窗，用于以可预测的 embedded-bare 布局管理 Git worktree：支持创建、克隆、打开、查看、拉取以及安全移除 worktree。
- [suzuki-junya108/view-and-edit-herdr-plugin](https://github.com/suzuki-junya108/view-and-edit-herdr-plugin) — herdr plugin: preview, edit, and browse files (text, Markdown, HTML, images, video, audio, PDF, Office, CSV/J…

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-files"></a>

## 文件浏览与编辑器联动

> 想在窗格中打开文件树，或与编辑器的状态保持一致

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**terminal-code**](https://github.com/zenbu-labs/terminal-code)<br><sub>zenbu-labs</sub> | 在终端中运行的 VS Code | `cli` `terminal` `vscode` `typescript` | 2201 | 🔄 2026-10-19 |
| [**ttt**](https://github.com/eugenioenko/ttt)<br><sub>eugenioenko</sub> | TTT Editor（Terminal Text Tool）——一款可在终端中运行、真正能替代 VS Code、Zed 和 Sublime 的编辑器。这是一个操作体验如 GUI 般的 TUI，单一二进制文件，零配置。 | `cli` `code-editor` `developer-tools` `diff` `editor` | 869 | 🔄 2026-10-26 |
| [**dotfiles**](https://github.com/babarot/dotfiles)<br><sub>babarot</sub> | A repository that gathered files starting with dot | `dotfiles` `neovim` `nix` | 782 | 🔄 2026-10-26 |
| [**herdr-file-viewer**](https://github.com/smarzban/herdr-file-viewer)<br><sub>smarzban</sub> | 面向 herdr 的只读文件查看器，支持感知 Git 状态。键盘驱动的 TUI（同时支持鼠标）：树形结构 + 内容窗格，支持差异对比、Markdown 渲染和语法高亮 | `file-viewer` `git` `ratatui` `rust` `terminal` | 681 | 🔄 2026-10-26 |
| [**herdr-sidebar**](https://github.com/alexarthurs/herdr-sidebar)<br><sub>alexarthurs</sub> | 面向 herdr 的 VS Code 风格侧边栏：将文件浏览器和 Git 源代码管理整合到一个窗格——带语法高亮的预览、VS Code 风格的差异对比、GitLens 风格的抽屉面板、AI 生成提交信息 | `git` `ratatui` `rust` `sidebar` `terminal` | 509 | 🔄 2026-10-24 |
| [**token**](https://github.com/ThorstenRhau/token)<br><sub>ThorstenRhau</sub> | Neovim 配色方案，并附带面向整个终端环境的社区贡献主题。 | `bat-theme` `delta-theme` `emacs-theme` `fish-theme` `fzf-theme` | 310 | 🔄 2026-10-26 |
| [**herdr-nvim**](https://github.com/ChmaraX/herdr-nvim)<br><sub>ChmaraX</sub> | 将 Neovim 完全集成到你的 herdr 工作区 | `lua` `neovim` `nvim` `nvim-plugin` `rust` | 306 | 🔄 2026-10-22 |
| [**herdr-mirror**](https://github.com/nikok6/herdr-mirror)<br><sub>nikok6</sub> | 在同一窗口统一本地和远程会话：将远程 herdr 服务器镜像到本地侧边栏，并通过 SSH 操控 | `rust` | 260 | 2026-09-06 |
| [**dotfiles**](https://github.com/edmundmiller/dotfiles)<br><sub>edmundmiller</sub> | 用于让我的 dotfiles 始终保持最新 | `dotfiles` `emacs` `nix-dotfiles` `nixos` `nixos-configuration` | 80 | 🔄 2026-10-26 |
| [**herdr-lazygit**](https://github.com/Crokily/herdr-lazygit)<br><sub>Crokily</sub> | 在 herdr 侧边栏窗格中运行 lazygit，支持 AI 生成提交信息——打开、展开、提交都只需一个按键 | `git` `lazygit` `shell` | 42 | 2026-09-14 |
| [**herdr-agent-progress**](https://github.com/eliasstravik/herdr-agent-progress)<br><sub>eliasstravik</sub> | 在 Herdr 侧边栏中显示由 Agent 上报的任务进度与活动状态。 | `rust` | 34 | 2026-09-15 |
| [**herdr-yazi**](https://github.com/speardragon/herdr-yazi)<br><sub>speardragon</sub> | 在 herdr 窗格中打开 Yazi | `shell` | 34 | 2026-08-19 |
| [**herdr-quicklook**](https://github.com/dwarvesf/herdr-quicklook)<br><sub>dwarvesf</sub> | herdr 的 Quick Look：将剪贴板中的路径以浮层形式弹出预览，一键切换到文件查看器 | `terminal` `shell` | 16 | 2026-08-26 |
| [**herdr-context.nvim**](https://github.com/makyinmars/herdr-context.nvim)<br><sub>makyinmars</sub> | 在 Neovim 中选中代码或停在某一行，选择一个正在运行的 Herdr Agent，将结构化的上下文暂存到该 Agent 的提示词中（不直接提交） | `lua` | 15 | 2026-09-17 |
| [**herdr-git-status**](https://github.com/ezcorp-org/herdr-git-status)<br><sub>ezcorp-org</sub> | herdr 插件：在侧边栏分支名旁显示每个空间的 git 工作区状态（已暂存/已修改/未跟踪/冲突） | `rust` | 11 | 2026-08-10 |
| [**bigtty**](https://github.com/v1k45/bigtty)<br><sub>v1k45</sub> | Native macOS client for herdr: Ghostty-rendered terminals, spaces sidebar, browser and file panes | `claude-code` `codex` `developer-tools` `ghostty` `macos` | 11 | 🔄 2026-10-21 |
| [**herdr-workbench**](https://github.com/azizuysal/herdr-workbench)<br><sub>azizuysal</sub> | 精致的 Herdr 项目侧边栏，具备文件浏览器、实时文件/内容搜索、只读源代码管理、丰富的预览、文件图标和 Git 状态装饰 | `rust` | 9 | 🔄 2026-10-16 |
| [**herdr-fresh**](https://github.com/rvalledorjr/herdr-fresh)<br><sub>rvalledorjr</sub> | 在 herdr 窗格内将终端 IDE「Fresh」作为文件查看器和编辑器运行的 herdr 插件 | `developer-tools` `editor` `fresh` `ide` `terminal` | 6 | 2026-07-17 |
| [**advanced-herdr-file-viewer**](https://github.com/thuanlm215/advanced-herdr-file-viewer)<br><sub>thuanlm215</sub> | 具备 Git 感知能力的只读 herdr 文件查看器：支持树形结构、差异对比、Markdown、语法高亮及内联图片预览。 | `file-viewer` `ripgrep` `rust` `tui` | 6 | 2026-09-29 |
| [**dotfiles**](https://github.com/tifandotme/dotfiles)<br><sub>tifandotme</sub> | ~/.*（家目录下的配置文件） | `aerospace` `chezmoi` `dotfiles` `ghostty` `lazygit` | 6 | 🔄 2026-10-26 |
| [**herdr-markdown-viewer**](https://github.com/arvindparmar-me/herdr-markdown-viewer)<br><sub>arvindparmar-me</sub> | Herdr 插件：拖选一个 Markdown 路径并按下 prefix+m，即可在右侧分屏窗格中预览 | `shell` | 5 | 2026-07-17 |
| [**herdr-file-viewer**](https://github.com/ismaelosuna7824/herdr-file-viewer)<br><sub>ismaelosuna7824</sub> | 集文件浏览器、代码查看器和 Git 客户端于一体的键盘驱动 Herdr 窗格应用——用 Go + Bubble Tea 编写 | `bubbletea` `git` `golang` `tui` `go` | 5 | 2026-08-08 |
| [**herdr-claude-usage**](https://github.com/oszypczy/herdr-claude-usage)<br><sub>oszypczy</sub> | Claude Usage Mini: a simple, minimal Claude usage plugin for herdr. Context, 5h and 7d limit bars in the sidebar. No daemon, no credentials, no network. | `claude` `claude-code` `usage` `shell` | 5 | 2026-10-05 |
| [**herdr-disp-model**](https://github.com/pdalinis/herdr-disp-model)<br><sub>pdalinis</sub> | 在 Herdr 的 Agent 侧边栏中显示当前正在运行的 Codex、Claude Code、Pi 和 Hermes 模型。 | `ai-agents` `claude-code` `codex` `developer-tools` `hermes-agent` | 5 | 2026-09-19 |
| [**herdr-marks-as-unread**](https://github.com/sachin-philip/herdr-marks-as-unread)<br><sub>sachin-philip</sub> | Mark agents as unread with a keyboard shortcut. A green sidebar marker reminds you to revisit them and clears when you return. | `javascript` | 5 | 🔄 2026-10-15 |
| [**herdr-open-in-editor**](https://github.com/timofey-TK/herdr-open-in-editor)<br><sub>timofey-TK</sub> | 在 VS Code 或 Zed 中打开本地或远程的 Herdr 工作区 | `vscode` `zed` `python` | 5 | 2026-07-30 |
| [**herdr-flutter**](https://github.com/ablause/herdr-flutter)<br><sub>ablause</sub> | 在编程 Agent 旁边监视、热重载并检查运行中 Flutter 应用的 herdr 侧边栏 | `dart` | 4 | 2026-07-27 |
| [**herdr-wait**](https://github.com/cdc-lst/herdr-wait)<br><sub>cdc-lst</sub> | 根据窗格的进程树判断闲置 Agent 窗格实际在做什么（例如 'waiting: build-api' 或 'waiting: codex'）并打上标签的可配置 herdr 插件 | `typescript` | 4 | 2026-07-03 |
| [**herdr-lazygit**](https://github.com/JacquesvanWyk/herdr-lazygit)<br><sub>JacquesvanWyk</sub> | 在 herdr 分屏窗格或标签页中打开 lazygit，支持智能切换（打开/聚焦/关闭） | `lazygit` `shell` | 4 | 2026-07-12 |
| [**herdr-commander**](https://github.com/lurepos/herdr-commander)<br><sub>lurepos</sub> | 一个快速的 herdr 菜单，用于发现并启动 npm、cargo 命令或 vscode 任务。 | `rust` | 4 | 2026-10-08 |
| [**herdr-plugin-mermaid-preview**](https://github.com/Volpestyle/herdr-plugin-mermaid-preview)<br><sub>Volpestyle</sub> | 在 Herdr 中为 Claude Code 和 Codex 的输出内容提供 Mermaid 图的实时预览 | `claude-code` `mermaid` `openai-codex` `terminal` `javascript` | 4 | 2026-07-10 |
| [**openloc.nvim**](https://github.com/Zamua/openloc.nvim)<br><sub>Zamua</sub> | 在已属于该工作区的 Neovim 中打开文件引用 | `lua` | 4 | 2026-08-25 |
| [**herdr-open-in**](https://github.com/alexeyco/herdr-open-in)<br><sub>alexeyco</sub> | Open the current Herdr workspace in your preferred editor | `android-studio` `developer-tools` `helix` `jetbrains` `neovim` | 3 | 🔄 2026-10-22 |
| [**herdr-bandeja-to-dos**](https://github.com/gonzalonicolasr/herdr-bandeja-to-dos)<br><sub>gonzalonicolasr</sub> | Plugin de herdr: bandeja de agentes en el sidebar (quién te necesita, listos, trabajando) + to-dos que te dejan los agentes | `python` | 3 | 2026-10-02 |
| [**herdr-omp-subagents**](https://github.com/hanbong5938/herdr-omp-subagents)<br><sub>hanbong5938</sub> | 在 Herdr 侧边栏中显示实时 OMP 子 Agent 的模型元数据，并内置 OMP 扩展桥接。 | `typescript` | 3 | 🔄 2026-10-11 |
| [**herdr-visuals**](https://github.com/hx-w/herdr-visuals)<br><sub>hx-w</sub> | 为 Herdr 提供按会话划分的 Mermaid、LaTeX 及本地图片预览，并支持 Kitty 图形代理。 | `javascript` | 3 | 2026-10-05 |
| [**herdr-yazi-windows**](https://github.com/Only-Moon/herdr-yazi-windows)<br><sub>Only-Moon</sub> | herdr-yazi 的 Windows 移植版，借助 herdr v0.8+ 支持原生 Windows 窗格生成 | `file` `file-manager` `pidotdev` `python` `tui` | 3 | 2026-08-14 |
| [**herdr-x**](https://github.com/playsthisgame/herdr-x)<br><sub>playsthisgame</sub> | 在 herdr 内的终端分屏中浏览 x.com，并在 $EDITOR 中起草推文发送给自己 | `cli` `terminal` `terminal-browser` `twitter` `shell` | 3 | 2026-08-20 |
| [**scp-explorer**](https://github.com/TinocoAI/scp-explorer)<br><sub>TinocoAI</sub> | MobaXterm 风格的 SCP 文件浏览器 herdr 插件（跨平台支持 macOS/Linux/Windows） | `curses` `file-manager` `scp` `python` | 3 | 2026-09-03 |
| [**herdr-wherewasi**](https://github.com/Trolzie/herdr-wherewasi)<br><sub>Trolzie</sub> | Herdr plugin: a live, rendered Markdown context sidebar beside your agents | `rust` | 3 | 2026-10-08 |
| [**herdr-yazi-links**](https://github.com/yakovlevs01/herdr-yazi-links)<br><sub>yakovlevs01</sub> | 从 Herdr 中打开 Yazi 里的文件超链接；可选补丁支持纯文本路径。 | `yazi` `python` | 3 | 🔄 2026-10-15 |
| [**agents-tree**](https://github.com/blavka/agents-tree)<br><sub>blavka</sub> | Live terminal tree of coding-agent sessions and nested subagents, with model, context use and status — Agy, Claude Code, Codex, and Grok Build. | `agy` `claude-code` `cli` `codex` `grok-build` | 2 | 🔄 2026-10-14 |
| [**herdr-covr**](https://github.com/evanbryant/herdr-covr)<br><sub>evanbryant</sub> | covr: a minimal, attention-first Spaces/Agents sidebar plugin for herdr | `python` | 2 | 2026-10-08 |
| [**herdr-footprint**](https://github.com/harpal-singh-qp/herdr-footprint)<br><sub>harpal-singh-qp</sub> | 在 Herdr 侧边栏中按空间显示磁盘占用与上下文用量。 | `python` | 2 | 2026-09-16 |
| [**herdr-claude-usage-multi**](https://github.com/iamhouser/herdr-claude-usage-multi)<br><sub>iamhouser</sub> | Herdr 侧边栏中的 Claude 套餐使用量表——会话/周 %、颜色随用量升级、重置倒计时，并通过 CLAUDE_CONFIG_DIR 配置支持多账号 | `claude-code` `python` | 2 | 2026-09-04 |
| [**herdr-file-viewer**](https://github.com/jomarmontuya/herdr-file-viewer)<br><sub>jomarmontuya</sub> | 右侧显示的 Herdr 文件树插件，支持文件标签页、跟随当前目录、Git 状态装饰和可点击链接 | `go` | 2 | 2026-07-13 |
| [**herdr-agents-info**](https://github.com/rchougule/herdr-agents-info)<br><sub>rchougule</sub> | Tell your Claude Code panes apart in the herdr Agents sidebar — a distinguishing name, model, context %, and disk footprint per pane. | `claude-code` `rust` `sidebar` `terminal` `tui` | 2 | 2026-09-16 |
| [**herdr-launcher-pane**](https://github.com/y-hirakaw/herdr-launcher-pane)<br><sub>y-hirakaw</sub> | herdr 的固定式点击启动窗格——按工作区启动 Finder/资源管理器、VS Code，或你配置的任意命令 | `launcher` `launcher-pane` `productivity` `python` | 2 | 2026-08-10 |
| [**herdr-cursor-open**](https://github.com/alex-devdone/herdr-cursor-open)<br><sub>alex-devdone</sub> | 在 Cursor 或 VS Code 中打开聚焦的 herdr 窗格——包括通过 Remote-SSH 连接到远程 herdr 的窗格 | `cursor` `vscode` `shell` | 1 | 2026-09-07 |
| [**🆕 herdr-sim**](https://github.com/baleen37/herdr-sim)<br><sub>baleen37</sub> | Herdr plugin: show the PRs each Claude Code / Codex pane touched as sidebar icons | `claude-code` `codex` `rust` | 1 | 🔄 2026-10-23 |
| [**herdr-zed-follow**](https://github.com/dlwr/herdr-zed-follow)<br><sub>dlwr</sub> | herdr 插件：让 Zed 跟随当前聚焦的 herdr 工作区。 | `zed` `shell` | 1 | 2026-09-24 |
| [**herdr-gitui**](https://github.com/Shi1xin/herdr-gitui)<br><sub>Shi1xin</sub> | 在侧边栏窗格中运行 gitui 的 herdr 插件——支持开关切换、展开以及浅色/深色主题 | `gitui` `python` | 1 | 2026-07-28 |
| [**herdr-subagent-watch**](https://github.com/silencechung/herdr-subagent-watch)<br><sub>silencechung</sub> | herdr plugin: watch Claude Code sub agents live — popup viewer and sidebar tree | `javascript` | 1 | 🔄 2026-10-23 |
| [**🆕 herdr-context**](https://github.com/Somliga/herdr-context)<br><sub>Somliga</sub> | Your Claude Code conversations as one tree, and the context editable: a Herdr plugin. | `claude-code` `go` | 0 | 2026-09-30 |
| [**🆕 view-and-edit-herdr-plugin**](https://github.com/suzuki-junya108/view-and-edit-herdr-plugin)<br><sub>suzuki-junya108</sub> | herdr plugin: preview, edit, and browse files (text, Markdown, HTML, images, video, audio, PDF, Office, CSV/JSON, SQLite) in a popup. macOS, Japanese UI. | `file-viewer` `macos` `python` | 0 | 2026-09-28 |
| [**🆕 dotfiles**](https://github.com/Unique-Divine/dotfiles)<br><sub>Unique-Divine</sub> | 来自 Unique Divine 的 dotfiles 以及其他 ~ 目录下的配置 | `dotfiles` `lua` `neovim` `neovim-dotfiles` `nvim` | 0 | 🔄 2026-10-25 |
| [**🆕 herdr-radio**](https://github.com/vrwolf1004/herdr-radio)<br><sub>vrwolf1004</sub> | Play Radio Browser stations audio-only in herdr, with the current station and playback state shown in the sidebar dock | `python` | 0 | 🔄 2026-10-23 |

<details><summary>与此目的也相关</summary>

- [robbyrussell/herdr-ohmyzsh](https://github.com/robbyrussell/herdr-ohmyzsh) — 面向 Herdr 的 Oh My Zsh 插件：在侧边栏显示耗时较长的命令、完成通知、shell 辅助工具，并可一键在所有闲置窗格中重新加载 Oh My Zsh。
- [ChmaraX/herdr-gitview](https://github.com/ChmaraX/herdr-gitview) — herdr 的 Git 状态/差异面板——审查更改、在 nvim 中编辑、暂存/提交/丢弃，全部在终端内完成
- [vonzelle-vzt/herdr-extensions](https://github.com/vonzelle-vzt/herdr-extensions) — 面向 herdr 的迷你 VS Code——具备 LSP 诊断、自动补全、重命名和跳转到定义的完整编辑器，外加源代码管理、搜索、问题面板、测试、调试器、应用实时预览、运行时错误捕获、图片粘贴和 Agent 差异审查。共…
- [jsmenzies/mergr](https://github.com/jsmenzies/mergr) — 在 Herdr Space 侧边栏行中显示 GitHub 拉取请求状态
- [xzedx/herdr-easyjump](https://github.com/xzedx/herdr-easyjump) — 按下一个键、输入一个字母，即可跳转到任意空间、Agent、窗格或标签页。采用 EasyMotion / Vimium / vim-choosewin 风格的提示标签，直接绘制在 Herdr 侧边栏中。
- [edxeth/herdr-pi-tree](https://github.com/edxeth/herdr-pi-tree) — 以树状结构展示你的 Pi Agent 的侧边栏——谁生成了谁、哪个 worktree 对应哪个分支、谁在等待你。
- [H3xept/herdr-aspire-hud](https://github.com/H3xept/herdr-aspire-hud) — 为每个 herdr 空间实时显示 .NET Aspire AppHost 的健康状态：侧边栏徽章与弹窗 HUD。
- [4242labs/herdr-radar-plus](https://github.com/4242labs/herdr-radar-plus) — Herdr 插件：按需要你处理的紧急程度对 Agent 排序，并以跨机器的具名分组呈现。基于 herdr-radar 构建。
- [brianh20/herdr-stagr](https://github.com/brianh20/herdr-stagr) — 面向 herdr 的源代码管理侧边栏——通过并排差异对比进行暂存、取消暂存和放弃更改
- [ivanvykopal/herdr-slurm](https://github.com/ivanvykopal/herdr-slurm) — Live SLURM/HPC job monitor sidebar for herdr (Rust): squeue for your clusters over SSH, native sidebar token,…
- [maedana/herdr-whereami](https://github.com/maedana/herdr-whereami) — 自动重命名标签页以显示你当前所在位置的 Herdr 插件——在 git 仓库内会显示为「仓库名/分支名」
- [mcostasilva/herdr-marks](https://github.com/mcostasilva/herdr-marks) — Neovim-style letter marks for Herdr panes and workspaces, with colored sidebar labels and quick navigation
- [ecklf/herdr-plugin-gh](https://github.com/ecklf/herdr-plugin-gh) — GitHub PR and CI status in Herdr's Agents sidebar, with open/create PR and failing-check actions.
- [jwanga/herdr-plugin-github-status](https://github.com/jwanga/herdr-plugin-github-status) — herdr 插件：以侧边栏宽度停靠在右侧，实时展示 GitHub 项目状态（里程碑、issue、PR、Actions）。
- [mastnacek/pi-herdr-sidebar](https://github.com/mastnacek/pi-herdr-sidebar) — Native Rust Herdr plugin sidebar for the Pi coding agent: status telemetry, live skills, gates — VSA slices i…
- [ZingerLittleBee/herdr-agent-pins](https://github.com/ZingerLittleBee/herdr-agent-pins) — 将 Herdr Agent 会话持久固定在 Agents 侧边栏顶部
- [Gareth-Rouse/herdr-plugin-session-pruner](https://github.com/Gareth-Rouse/herdr-plugin-session-pruner) — herdr 插件：记录工作区的最后使用时间，在 Spaces 侧边栏中显示已过去多久，并将闲置工作区排除在会话恢复之外

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-cost"></a>

## Token 与费用管理

> 想看看 Agent 花费了多少，并想削减用量

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**memex**](https://github.com/nicosuave/memex)<br><sub>nicosuave</sub> | 搜索 Claude Code、Codex、Pi、OpenCode、GitHub Copilot 和 Cursor 的会话记录。恢复会话。追踪 token 使用 | `bm25` `claude-code` `codex-cli` `copilot` `hermes-agent` | 285 | 🔄 2026-10-24 |
| [**herdr-agent-usage**](https://github.com/senna-lang/herdr-agent-usage)<br><sub>senna-lang</sub> | Context meters, quota tracking, and provider rate limits for agents running in Herdr. | `ai-agents` `claude-code` `codex` `golang` `rate-limiting` | 61 | 🔄 2026-10-25 |
| [**llmtrim-herdr**](https://github.com/fkiene/llmtrim-herdr)<br><sub>fkiene</sub> | 降低 herdr 的 token 费用：压缩每个 Agent 窗格的请求（实测输入 -31% / 输出 -74%），并在每个窗格的徽章上显示节省的费用 | `llm-proxy` `llmtrim` `powershell` | 58 | 2026-07-02 |
| [**quota**](https://github.com/pinkpixel-dev/quota)<br><sub>pinkpixel-dev</sub> | Desktop app, VSCode extension, CLI, and Herdr plugin for tracking AI usage across GitHub Copilot, Codex, Claude Code, Antigravity, Kiro, Grok, Cursor and OpenC… | `ai-tools` `antigravity` `claude` `codex` `cursor` | 31 | 🔄 2026-10-20 |
| [**herdr-token-dashboard**](https://github.com/Davidcreador/herdr-token-dashboard)<br><sub>Davidcreador</sub> | 面向 Herdr Agent 窗格的实时 token 消耗仪表盘和通知 | `ai-agents` `bubbletea` `opencode` `pi-agent` `token-dashboard` | 27 | 2026-10-09 |
| [**herdr-grazr**](https://github.com/wazum/herdr-grazr)<br><sub>wazum</sub> | 一个简单可靠的 Claude Code 账号自动切换工具：在触及 5 小时或每周速率限制之前，自动轮换到新账号，让窗格永远不会因用量配额而停摆。是一个 Herdr 插件。 | `account-rotation` `account-switcher` `account-switching` `anthropic` `claude` | 5 | 🔄 2026-10-21 |
| [**🆕 account-capacity-dock**](https://github.com/Mako-L/account-capacity-dock)<br><sub>Mako-L</sub> | Quota rings for every Claude, Codex and Cursor account: a desktop dock, a terminal app and a Herdr widget. | `claude` `cliproxyapi` `codex` `cursor` `python` | 4 | 🔄 2026-10-22 |
| [**herdr-ctx-bar**](https://github.com/pdalinis/herdr-ctx-bar)<br><sub>pdalinis</sub> | 在 Herdr 的 Agents 侧边栏中，为 Codex、Claude Code、Pi 和 Hermes Agent 显示带颜色编码的上下文窗口使用率进度条。 | `ai-agents` `claude-code` `codex` `context-window` `hermes-agent` | 4 | 2026-09-19 |
| [**herdr-claude-usage**](https://github.com/alejodelosrios/herdr-claude-usage)<br><sub>alejodelosrios</sub> | 不必再为了查配额而打开一个 Claude 会话。Claude 套餐使用情况（会话 % \| 周 %）始终显示在 Herdr 侧边栏中，同一账号下所有工作区共享。通过 Claude Code 自身的凭据获取与 /status 完全一致的精确数字：无需估算，无需额外登录，也不消耗套餐 token | `claude` `claude-code` `python` | 3 | 2026-07-21 |
| [**agentglass-herdr**](https://github.com/BjoernSchotte/agentglass-herdr)<br><sub>BjoernSchotte</sub> | agentglass inside herdr: popup, open-in-agentglass, agentglass:// links, cost and alert tokens | `agentglass` `coding-agents` `shell` | 3 | 2026-10-07 |
| [**herdr-opentab**](https://github.com/hamidi-dev/herdr-opentab)<br><sub>hamidi-dev</sub> | 在 Herdr 侧边栏中实时显示 OpenTab 提供的每个 Agent 的 AI 花费 | `ai-agents` `opentab` `terminal` `python` | 3 | 2026-10-07 |
| [**herdr-jarvis**](https://github.com/NexorPL/herdr-jarvis)<br><sub>NexorPL</sub> | Mission control for herdr: animated big-picture core, projects by path, threads, timeline and token usage. | `rust` | 3 | 🔄 2026-10-25 |
| [**herdr-gekiatsu-plugin**](https://github.com/yuuta1219/herdr-gekiatsu-plugin)<br><sub>yuuta1219</sub> | herdr 插件：把 Claude Code 的用量计数器做成了老虎机——1/99 中大奖概率，每天 10:00 JST 重置 | `claude` `claude-code` `python` `tui` | 3 | 2026-08-17 |
| [**quota-deck**](https://github.com/ArtMoreno/quota-deck)<br><sub>ArtMoreno</sub> | quota-deck：在 Windows、macOS 和 Linux 上的 Herdr 中，显示按凭据划分范围的 AI 配额与上下文。 | `rust` | 2 | 2026-10-03 |
| [**herdr-account-hub**](https://github.com/C0R0NELL/herdr-account-hub)<br><sub>C0R0NELL</sub> | Manage Codex, Claude accounts in Herdr, track usage, and use resets. Switch Codex accounts without losing chat history or titles. Claude Code support is beta. | `herd-management` `python` | 2 | 🔄 2026-10-23 |
| [**herdr-api-credit-bar**](https://github.com/CristianPeralta/herdr-api-credit-bar)<br><sub>CristianPeralta</sub> | herdr 插件：显示按量计费 API 服务商的剩余额度，首先支持阿里云 Model Studio | `shell` | 2 | 2026-09-05 |
| [**herdr-slurm**](https://github.com/ivanvykopal/herdr-slurm)<br><sub>ivanvykopal</sub> | Live SLURM/HPC job monitor sidebar for herdr (Rust): squeue for your clusters over SSH, native sidebar token, width-adaptive table | `hpc` `slurm` `rust` | 2 | 2026-10-03 |
| [**herdr-quota**](https://github.com/kvkenyon/herdr-quota)<br><sub>kvkenyon</sub> | 在 Herdr 中一目了然地查看 Claude、Codex、Cursor 和 Kimi 的订阅配额 | `ai-tools` `claude-code` `cursor` `developer-tools` `kimi` | 2 | 2026-09-05 |
| [**herdr-whereami**](https://github.com/maedana/herdr-whereami)<br><sub>maedana</sub> | 自动重命名标签页以显示你当前所在位置的 Herdr 插件——在 git 仓库内会显示为「仓库名/分支名」 | `rust` | 2 | 2026-09-14 |
| [**herdr-burnlog**](https://github.com/naturalmoods/herdr-burnlog)<br><sub>naturalmoods</sub> | 面向 Herdr Agent 的本地按项目记录的 token 用量与费用历史。 | `python` | 2 | 2026-09-28 |
| [**herdr-opencodex**](https://github.com/nordz0r/herdr-opencodex)<br><sub>nordz0r</sub> | OpenCodex 的 Herdr 插件：显示花费统计以及 5 小时/7 天的剩余配额。 | `opencodex` `quota` `rust` | 2 | 🔄 2026-10-15 |
| [**🆕 herdr-agent-tokens**](https://github.com/mikitahimpel/herdr-agent-tokens)<br><sub>mikitahimpel</sub> | Herdr plugin: show Claude Code and Codex token usage in the agent sidebar | `rust` | 0 | 🔄 2026-10-12 |
| [**🆕 pi-agent-usage**](https://github.com/w784415/pi-agent-usage)<br><sub>w784415</sub> | 显示 OpenAI Codex 配额和重置时间的 Pi 扩展，支持 Herdr 插件 | `openai-codex` `pi-extension` `pi-package` `quota` `typescript` | 0 | 2026-08-26 |

<details><summary>与此目的也相关</summary>

- [ThorstenRhau/token](https://github.com/ThorstenRhau/token) — Neovim 配色方案，并附带面向整个终端环境的社区贡献主题。
- [jeffarese/herdr-agent-grid](https://github.com/jeffarese/herdr-agent-grid) — A fast native Rust command center for Herdr: agents, subagents, status, messages and API cost.
- [VHemanth45/herdr_agents_tracker](https://github.com/VHemanth45/herdr_agents_tracker) — 显示 AI 订阅用量的 Herdr 插件：在标签栏展示账户额度、每个 Agent 的上下文使用计量、额度不足提醒，以及面向 Claude Code、Codex、OpenCode Go 和 Grok 的 token 仪表…
- [romiluz13/instinct-herdr-tunnel](https://github.com/romiluz13/instinct-herdr-tunnel) — Let an AI assistant such as Instinct watch and steer your Herdr coding agents: a loopback portal with a 26-ac…

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-monitor"></a>

## 监控与仪表盘

> 想一目览尽 Agent 和机器的状态

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**zoetrope**](https://github.com/furkankly/zoetrope)<br><sub>furkankly</sub> | 在终端或浏览器中，将 Claude Code 或 Codex 会话实时可视化为流程图。 | `agent-visualization` `claude-code` `codex` `coding-agents` `flow` | 1104 | 🔄 2026-10-14 |
| [**clauth**](https://github.com/uwuclxdy/clauth)<br><sub>uwuclxdy</sub> | Claude Code multi-account manager, usage monitor (CLI, TUI & cross-account delegation via MCP) | `account-manager` `account-switcher` `anthropic` `claude` `claude-code` | 261 | 🔄 2026-10-26 |
| [**herdr-radar**](https://github.com/hhdebb/herdr-radar)<br><sub>hhdebb</sub> | 谁在工作、谁在等你——一目了然。按项目分组，每个 Agent 以其厂商的图标和颜色显示。worktree 嵌套在所属仓库下，各行按活跃度排序，空闲会话会淡出显示。支持浅色和深色主题。 | `claudecode` `codex-cli` `coding-agents-plugins` `developer-tools-ai-agent` `terminal-multiplexers` | 193 | 🔄 2026-10-20 |
| [**captains-deck**](https://github.com/deimantasnork/captains-deck)<br><sub>deimantasnork</sub> | Captain's Deck——面向 Herdr 的只读 Firstmate 流程看板插件。 | `firstmate` `python` | 69 | 🔄 2026-10-22 |
| [**herdr-beads**](https://github.com/miiraheart/herdr-beads)<br><sub>miiraheart</sub> | herdr 的 beads（bd）任务面板：以列表、表格或看板形式展示你的 bd issue，可作为侧边栏或浮动窗口 | `bd` `beads` `kanban` `rust` `tui` | 39 | 2026-10-08 |
| [**herdr-pc-ram-and-cpu-usage-overlay**](https://github.com/ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay)<br><sub>ezcorp-org</sub> | herdr 插件：按空间（工作区）实时显示 CPU/内存占用率，以占整机资源的比例呈现 | `rust` | 27 | 2026-09-13 |
| [**herdr-f1**](https://github.com/hmu332233/herdr-f1)<br><sub>hmu332233</sub> | 为 Herdr Agent 打造的 F1 风格仪表盘 | `agent-dashboard` `typescript` | 18 | 2026-10-09 |
| [**herdr-shell-progress**](https://github.com/bayoudhi/herdr-shell-progress)<br><sub>bayoudhi</sub> | herdr 插件：不仅是编程 Agent，耗时较长的 shell 命令的进度也会实时显示在侧边栏 | `rust` | 16 | 2026-09-23 |
| [**herdr-agent-grid**](https://github.com/jeffarese/herdr-agent-grid)<br><sub>jeffarese</sub> | A fast native Rust command center for Herdr: agents, subagents, status, messages and API cost. | `agent-dashboard` `ai-agents` `claude-code` `codex` `ratatui` | 16 | 🔄 2026-10-16 |
| [**herdr-telemetry**](https://github.com/DIodide/herdr-telemetry)<br><sub>DIodide</sub> | 将工作区和 Agent 遥测数据流式传输到你自己掌控的端点的 Herdr 插件——Go 编写的单一二进制文件，默认注重隐私 | `golang` `telemetry` `go` | 12 | 2026-07-10 |
| [**shepherd**](https://github.com/ryonakae/shepherd)<br><sub>ryonakae</sub> | 面向 Herdr 管理的编程 Agent 的 worker 可观测性守护进程和运行时桥接 | `pi-coding-agent` `pi-extension` `typescript` | 12 | 2026-08-28 |
| [**herdr-lcars**](https://github.com/jlcases/herdr-lcars)<br><sub>jlcases</sub> | 从一个 LCARS 舰桥指挥最多 2000 个 Herdr AI Agent，按账户追踪 Claude/Codex 配额，并在不丢失工作内容的前提下移交经过验证的上下文。 | `agent-observability` `ai-agents` `claude-code` `lcars` `openai-codex` | 10 | 2026-10-10 |
| [**herdr-sysmon**](https://github.com/getpipher/herdr-sysmon)<br><sub>getpipher</sub> | 在 Herdr 侧边栏显示系统指标——CPU、内存、电池、网络、磁盘、时钟。忠实地将 tmux-cpu/tmux-battery/tmux-online-status 状态栏移植为 Herdr 工作区 token。以 macOS 为主 | `battery` `catppuccin` `cpu` `getpipher` `macos` | 8 | 2026-07-26 |
| [**herdr-tally**](https://github.com/jasonrr/herdr-tally)<br><sub>jasonrr</sub> | 为你和你的 Agent 提供按项目划分的待办事项和速记板<br>📝 プロジェクト単位の TODO 管理 | `rust` `todo` | 8 | 🔄 2026-10-14 |
| [**herdr-ports**](https://github.com/Numbered-com/herdr-ports)<br><sub>Numbered-com</sub> | 在 herdr 中呈现正在运行的开发服务器：为每个至少运行一个 TCP 监听器的空间显示通用的 $ports 徽章 | `kill` `pids` `ports` `processes` `space` | 7 | 2026-09-29 |
| [**herdr-workboard**](https://github.com/Phoobobo/herdr-workboard)<br><sub>Phoobobo</sub> | herdr 的看板式工作板 TUI：看板对应工作区，任务状态对应标签页，任务会话对应窗格 | `kanban` `tui` `typescript` | 7 | 2026-08-10 |
| [**herdr-devserver-status**](https://github.com/Razz21/herdr-devserver-status)<br><sub>Razz21</sub> | 通过可插拔规范检测窗格中开发服务器，并报告其生命周期状态的 Herdr 插件 | `astro` `cli` `deamon` `dev-server` `extensible` | 7 | 🔄 2026-10-24 |
| [**herdr-lazydocker**](https://github.com/sudoeren/herdr-lazydocker)<br><sub>sudoeren</sub> | 在 herdr 的分屏窗格或独立标签页中运行 lazydocker | `docker` `lazydocker` `shell` | 7 | 2026-08-27 |
| [**herdr-monitoring**](https://github.com/enes/herdr-monitoring)<br><sub>enes</sub> | Herdr resource monitor plugin with agent summary and focused pane views | `rust` | 6 | 2026-09-28 |
| [**herdr-kanban**](https://github.com/KokiKono/herdr-kanban)<br><sub>KokiKono</sub> | 将任务与 herdr 标签页关联的终端看板，数据持久化在 SQLite 中 | `rust` | 6 | 2026-07-10 |
| [**sbx-herdr**](https://github.com/dvdksn/sbx-herdr)<br><sub>dvdksn</sub> | Herdr integration for Docker Sandboxes | `go` | 5 | 🔄 2026-10-23 |
| [**shepherd**](https://github.com/jwarykowski/shepherd)<br><sub>jwarykowski</sub> | 把你的待办事项统一「牧」起来 | `cli` `developer-tools` `go-lang` `productivity` `task-management` | 5 | 🔄 2026-10-26 |
| [**herdr_agents_tracker**](https://github.com/VHemanth45/herdr_agents_tracker)<br><sub>VHemanth45</sub> | 显示 AI 订阅用量的 Herdr 插件：在标签栏展示账户额度、每个 Agent 的上下文使用计量、额度不足提醒，以及面向 Claude Code、Codex、OpenCode Go 和 Grok 的 token 仪表盘。 | `chatgpt` `claude` `claude-code` `codex` `herdr-integration` | 5 | 2026-09-24 |
| [**herdr-agent-watcher**](https://github.com/winoooops/herdr-agent-watcher)<br><sub>winoooops</sub> | 面向 Herdr 的编程 Agent 可观测性——实时侧边栏卡片、生命周期通知，以及零配置的 Claude Code 指标桥接 | `claude-code` `rust` | 5 | 2026-09-21 |
| [**herdr-mise**](https://github.com/funsaized/herdr-mise)<br><sub>funsaized</sub> | Run the pass, not the prompts 🧑‍🍳 A visualizer for your agents. A herdr plugin. Intentionally small footprint | `agent` `agent-monitoring` `ai-agents` `cli-tool` `developer-tools` | 4 | 🔄 2026-10-26 |
| [**herdr-jcode**](https://github.com/leonardoacosta/herdr-jcode)<br><sub>leonardoacosta</sub> | 一个独立的 Herdr 插件，报告 Jcode 的 working/idle 生命周期状态及会话身份信息。为独立实现，不依赖 fork。 | `jcode` `rust` | 4 | 2026-09-16 |
| [**herdr-portal**](https://github.com/loofare/herdr-portal)<br><sub>loofare</sub> | 面向 herdr 的任务控制仪表盘——将所有工作区/标签页/窗格中的 Agent 汇总到一个实时 TUI 看板（支持键盘和鼠标）以及网页大屏中：结构化进度展示、Ctrl+B A 打开、点击跳转、可从浏览器直接回复 Agent | `agent-dashboard` `agent-monitor` `ai-agents` `claude-code` `codex` | 4 | 🔄 2026-10-19 |
| [**herdr-status-ui-bar**](https://github.com/speardragon/herdr-status-ui-bar)<br><sub>speardragon</sub> | 在 herdr 标签栏中显示 AI Agent 的方案用量仪表（Claude Code / Codex / Grok） | `claude-code` `codex` `grok` `python` `tab-bar` | 4 | 2026-10-05 |
| [**herdr-claude-usage**](https://github.com/anyaachan/herdr-claude-usage)<br><sub>anyaachan</sub> | 在 Herdr 中查看 Claude Code 套餐的全局用量：标签栏摘要 + 弹出式仪表盘，基于 statusLine 实现，支持多账号。 | `claude` `claude-code` `cli` `terminal` `shell` | 3 | 2026-09-01 |
| [**herdr-codex-bridge**](https://github.com/ardasevinc/herdr-codex-bridge)<br><sub>ardasevinc</sub> | 通过一个集中式的 app-server，为 Codex 会话赋予原生的 Herdr 窗格身份标识。 | `ai-agents` `codex` `terminal` `go` | 3 | 🔄 2026-10-22 |
| [**🆕 herdr-macos-plugins**](https://github.com/klinter007/herdr-macos-plugins)<br><sub>klinter007</sub> | Files and Links, Stay Awake, and System Monitor plugins for standard Herdr on macOS | `python` | 3 | 🔄 2026-10-12 |
| [**herdr-tasks**](https://github.com/MatheusBBarni/herdr-tasks)<br><sub>MatheusBBarni</sub> | 面向 Herdr 的看板任务运行器：包含 OpenTUI 看板与 htasks CLI。 | `typescript` | 3 | 2026-09-11 |
| [**herdr-slurm**](https://github.com/quan-meng/herdr-slurm)<br><sub>quan-meng</sub> | 为 Slurm 分配任务创建 Herdr 工作区和受监控的 Agent 标签页 | `hpc` `slurm` `terminal-multiplexer` `python` | 3 | 2026-08-13 |
| [**herdr-mem-cpu-load**](https://github.com/thewtex/herdr-mem-cpu-load)<br><sub>thewtex</sub> | 面向 herdr 的 CPU、内存与负载均值监控工具。 | `rust` | 3 | 2026-09-07 |
| [**herdr-agent-state**](https://github.com/Tyru5/herdr-agent-state)<br><sub>Tyru5</sub> | herdr 的实时 Agent 状态窗格——以更易读的形式显示工作区中每个 Agent 正在做什么 | `claude-code` `rust` `terminal` | 3 | 2026-09-22 |
| [**adlc-herdr**](https://github.com/voodootikigod/adlc-herdr)<br><sub>voodootikigod</sub> | ADLC 的 herdr 插件——按窗格显示阶段/工单/关卡状态，附带待办看板、关卡操作和 adlc-fleet 运行可观测性。是 voodootikigod/adlc/plugins/adlc-herdr 的自动同步镜像 | `javascript` | 3 | 🔄 2026-10-25 |
| [**herdr-cache-timer**](https://github.com/ArteenHD/herdr-cache-timer)<br><sub>ArteenHD</sub> | 在 Herdr 侧边栏中直接显示每个 Agent 的 prompt 缓存何时过期 | `claude-code` `prompt-caching` `terminal` `javascript` | 2 | 2026-08-08 |
| [**herdr-agent-dashboard**](https://github.com/carsonjones/herdr-agent-dashboard)<br><sub>carsonjones</sub> | prefix+a 显示 herdr Agent 列表 | `typescript` | 2 | 2026-07-16 |
| [**tsk**](https://github.com/chrisg32/tsk)<br><sub>chrisg32</sub> | tsk——一个 TaskPaper/PlainTasks 风格的纯文本任务管理 TUI，使用 Rust 编写。既可独立运行，也可作为 herdr 插件使用。 | `rust` `taskpaper` `todo` `tui` | 2 | 2026-09-03 |
| [**herdr-telemetry-bridge**](https://github.com/CodyBontecou/herdr-telemetry-bridge)<br><sub>CodyBontecou</sub> | 将本地工作区、仓库、编程 Agent、模型和追踪遥测数据流式传输到外部客户端的 Herdr 插件 | `coding-agents` `telemetry` `time-md` `javascript` | 2 | 2026-06-26 |
| [**herdr-agentsview**](https://github.com/cpcloud/herdr-agentsview)<br><sub>cpcloud</sub> | 将 AgentsView 的活动压缩显示在一个异常繁忙的终端里 | `rust` | 2 | 🔄 2026-10-17 |
| [**herdr-spinner**](https://github.com/hasuwini77/herdr-spinner)<br><sub>hasuwini77</sub> | 通过仅用于显示的窗格元数据，为处于工作状态的 Herdr 窗格显示动态盲文旋转指示器 | `ai-agents` `claude-code` `herdr-theme` `spinner` `terminal` | 2 | 2026-09-25 |
| [**herdr-statusline**](https://github.com/iiii1224/herdr-statusline)<br><sub>iiii1224</sub> | 面向 herdr 会话的可自定义状态栏 | `cli` `statusbar` `statusline` `tmux` `python` | 2 | 2026-08-15 |
| [**herdr-goose-bridge**](https://github.com/inoribea/herdr-goose-bridge)<br><sub>inoribea</sub> | Herdr plugin that reports goose agent lifecycle state (idle / working / blocked) into your panes. goose is a line-mode CLI, so Herdr cannot detect it on its ow… | `agent-state` `ai-agents` `developer-tools` `goose` `goose-cli` | 2 | 2026-09-11 |
| [**herdr-jira-board**](https://github.com/kiitosu/herdr-jira-board)<br><sub>kiitosu</sub> | 在 herdr 中运行的 Jira 看板，附带 Claude Code 会话启动器 | `python` | 2 | 🔄 2026-10-22 |
| [**🆕 herdr-sbx**](https://github.com/lanwen/herdr-sbx)<br><sub>lanwen</sub> | Herdr Plugin to enable Docker Sandboxes as SSH connected machines. Full agent visibility, plugin sync | `docker` `sandboxes` `go` | 2 | 🔄 2026-10-26 |
| [**kanban_tui**](https://github.com/m0hdrar/kanban_tui)<br><sub>m0hdrar</sub> | 一款以键盘操作为核心的终端看板工具。 | `typescript` | 2 | 🔄 2026-10-18 |
| [**🆕 herdr-vitals**](https://github.com/mrolafsson/herdr-vitals)<br><sub>mrolafsson</sub> | How your machines are doing, at a glance, before they slow your agents down. A herdr plugin: CPU, load, memory, disks (and when they'll be full) and network fo… | `anthropic` `bubbletea` `claude-code` `codex` `coding-agents` | 2 | 🔄 2026-10-20 |
| [**herdr-cache-ttl**](https://github.com/nytafar/herdr-cache-ttl)<br><sub>nytafar</sub> | herdr 插件：按 Agent 窗格实时倒计时显示 prompt 缓存的 TTL | `rust` | 2 | 2026-10-02 |
| [**herdr-ports**](https://github.com/randomradio/herdr-ports)<br><sub>randomradio</sub> | Herdr 插件：将远程工作区的端口转发到 http://herdr.{workspace}.localhost:{port}。 | `rust` | 2 | 2026-09-20 |
| [**herdr-tilt**](https://github.com/the-inconvenience-store/herdr-tilt)<br><sub>the-inconvenience-store</sub> | 面向 Herdr 的键盘驱动 Tilt 仪表盘 | `k8s` `kubernetes` `tilt` `rust` | 2 | 🔄 2026-10-23 |
| [**herdr-memex-analytics**](https://github.com/vishnutskumar/herdr-memex-analytics)<br><sub>vishnutskumar</sub> | herdr 插件：基于 memex 历史记录，提供会话效率分析和实时 Agent 指导 | `rust` | 2 | 2026-09-01 |
| [**herdr-docker**](https://github.com/abcxff/herdr-docker)<br><sub>abcxff</sub> | 像追踪 herdr 中的 Agent 一样，追踪 docker 构建 | `docker` `javascript` | 1 | 2026-08-12 |
| [**herdr-tokscale-dashboard**](https://github.com/astkaasa/herdr-tokscale-dashboard)<br><sub>astkaasa</sub> | 将 Tokscale 作为本地 Herdr 仪表盘窗格打开 | `dashboard` `tokscale` `shell` | 1 | 2026-06-26 |
| [**herdr-nodejs-center**](https://github.com/AZenking/herdr-nodejs-center)<br><sub>AZenking</sub> | 用于监控并聚焦本地 Node.js、Bun 和 Deno 服务的 Herdr 弹窗 | `developer-tools` `nodejs` `javascript` | 1 | 🔄 2026-10-18 |
| [**herdr-plugin-codex-subs**](https://github.com/benkraus/herdr-plugin-codex-subs)<br><sub>benkraus</sub> | 显示 CLIProxyAPI 中 Codex 订阅额度和重置积分的 Herdr 仪表盘 | `go` | 1 | 2026-07-30 |
| [**herdr-overview**](https://github.com/iamgp/herdr-overview)<br><sub>iamgp</sub> | 面向 Herdr 的 Mission Control / Exposé——以平铺方式实时展示所有 space | `terminal` `tui` `javascript` | 1 | 2026-08-28 |
| [**herdr-ports**](https://github.com/ivorpad/herdr-ports)<br><sub>ivorpad</sub> | herdr 插件：一个弹窗，列出正在监听的端口，标出每个端口背后的项目名称，并可将其终止或打开 | `tui` `python` | 1 | 2026-08-27 |
| [**🆕 herdr-stats**](https://github.com/jeffarese/herdr-stats)<br><sub>jeffarese</sub> | Live CPU, memory, disk, temperature, GPU, power and network stats in herdr's tab bar: braille graphs, gauges and reactive icons | `linux` `macos` `rust` `system-monitor` `terminal` | 1 | 🔄 2026-10-23 |
| [**herdr-metrics**](https://github.com/jordanhawkes/herdr-metrics)<br><sub>jordanhawkes</sub> | 在 Herdr 侧边栏中显示 Claude Code、Codex 和 TraeX 的上下文、会话 token 和账号限额指标。是 szrenwei/herdr-agent-metrics 的维护延续 | `claude-code` `openai-codex` `traex` `tui` `python` | 1 | 2026-08-22 |
| [**🆕 herdr-job-board**](https://github.com/larrychannon/herdr-job-board)<br><sub>larrychannon</sub> | A To do / Doing / Waiting-on-you board for agent jobs, in a Herdr split pane. | `javascript` | 1 | 🔄 2026-10-23 |
| [**pi-herdr-sidebar**](https://github.com/mastnacek/pi-herdr-sidebar)<br><sub>mastnacek</sub> | Native Rust Herdr plugin sidebar for the Pi coding agent: status telemetry, live skills, gates — VSA slices in Rust/Ratatui | `pi` `ratatui` `rust` | 1 | 🔄 2026-10-14 |
| [**herdr-compose**](https://github.com/mattyan1053/herdr-compose)<br><sub>mattyan1053</sub> | 用于 docker compose 的 Herdr 插件 | `terminal` `tui` `shell` | 1 | 2026-07-24 |
| [**herdr-virtualboard**](https://github.com/virtualboard/herdr-virtualboard)<br><sub>virtualboard</sub> | 在 Herdr 中管理 VirtualBoard 功能规格的看板：列代表生命周期阶段，卡片代表规格，派发卡片会在窗格中启动对应角色的 Agent。 | `go` | 1 | 🔄 2026-10-16 |
| [**🆕 herdr-jcode-integration**](https://github.com/capt-marbles/herdr-jcode-integration)<br><sub>capt-marbles</sub> | 用于 Jcode 生命周期状态和会话报告的 Herdr 插件 | `jcode` `shell` | 0 | 2026-08-09 |
| [**🆕 herdr-run-targets**](https://github.com/fantoine/herdr-run-targets)<br><sub>fantoine</sub> | Launch, stop and restart a repository's dev services from a dashboard pane in Herdr | `python` | 0 | 2026-10-09 |

<details><summary>与此目的也相关</summary>

- [nelsonPires5/herdr-board](https://github.com/nelsonPires5/herdr-board) — herdr 的看板工具——卡片就是提示词，会被派发给可见窗格中的 AI Agent
- [e2b-dev/herdr-e2b-sandbox](https://github.com/e2b-dev/herdr-e2b-sandbox) — 将 git 工作树镜像到 E2B Sandbox 的 herdr 插件——支持单个沙盒或每个 Agent 一条分支的沙盒集群，并配有 TUI 仪表盘
- [quaywin/agys](https://github.com/quaywin/agys) — 通过零污染沙盒，为 Herdr 中的 Antigravity CLI 提供轻松的多配置文件隔离和实时配额追踪
- [Northern-Lighthouse/herdr-fleet](https://github.com/Northern-Lighthouse/herdr-fleet) — 通过 Tailscale 管理一批 herdr 机器——仪表盘插件、自动发现、感知容量的 Agent 派发、无盘工作区
- [cdowell09/herdr-pr-board](https://github.com/cdowell09/herdr-pr-board) — 面向 Herdr 的可配置跨仓库 GitHub 拉取请求仪表盘
- [bengemine/herdr-hibernate](https://github.com/bengemine/herdr-hibernate) — 让 Herdr 中空闲的编程 Agent 窗格（Claude Code、Codex、Grok）休眠——释放内存，按 Enter 即可恢复原会话
- [spad-0x/herdr-mobile-pro](https://github.com/spad-0x/herdr-mobile-pro) — 一款高性能、移动优先的 PWA 仪表盘，采用 Cyber-Dark 设计风格，可直接从智能手机编排 Herdr 与自主 AI Agent。具备安全 HTTPS、语音听写输入、图片上传，以及将终端输出实时语义解析为聊天式…
- [4242labs/herdr-radar-plus](https://github.com/4242labs/herdr-radar-plus) — Herdr 插件：按需要你处理的紧急程度对 Agent 排序，并以跨机器的具名分组呈现。基于 herdr-radar 构建。
- [eugeneb50/herdr-mcp](https://github.com/eugeneb50/herdr-mcp) — herdr plugin and MCP server: drive herdr panes and agents from AI clients, with recipes, triggers, schedules,…
- [ivanvykopal/herdr-slurm](https://github.com/ivanvykopal/herdr-slurm) — Live SLURM/HPC job monitor sidebar for herdr (Rust): squeue for your clusters over SSH, native sidebar token,…
- [Javamomma/herdr-scribe](https://github.com/Javamomma/herdr-scribe) — herdr 插件：不录音的实时会议转录——将麦克风输入转为仅存于内存的文字记录和实时分析窗格；停止时生成会议纪要、可选策略关卡以及可审查的自动草稿。支持 Linux/WSL2 和 macOS
- [sazardev/herdr-code-board](https://github.com/sazardev/herdr-code-board) — Herdr 内面向 Agent 提示词的看板队列——卡片会将真实 Agent 派发到窗格、工作树和工作区，并可通过规则将一张卡片链到下一张
- [tferreira/herdr-pr-ops](https://github.com/tferreira/herdr-pr-ops) — PR//OPS - pull request mission control for Herdr: your PRs and review requests on one board, one-key agents i…
- [chouxcreams/herdr-dashboard](https://github.com/chouxcreams/herdr-dashboard) — herdr 工作区的 PR 状态仪表盘 TUI——一目了然地查看每个窗格对应的 PR 状态/CI/审查情况

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-finder"></a>

## 搜索与模糊查找器

> 只记得大概名字也想调出命令或项目

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-navigator**](https://github.com/thanhdat77/herdr-navigator)<br><sub>thanhdat77</sub> | 通过一个模糊导航器跳转到任意 Herdr 工作区、Agent、项目、会话、远程连接、目录或操作 | `fuzzy-finder` `rust` `terminal` `workspace-manager` | 188 | 2026-09-24 |
| [**herdr-bar**](https://github.com/jeffarese/herdr-bar)<br><sub>jeffarese</sub> | 面向 herdr 的 Cmd+K 与自动标签标题：可模糊跳转到任意标签页、Agent、仓库或分支。 | `command-bar` `fuzzy-finder` `python` `terminal` `tui` | 148 | 🔄 2026-10-26 |
| [**termscope**](https://github.com/iurysza/termscope)<br><sub>iurysza</sub> | 在分屏中打开终端屏幕上已经可见的文件和链接 | `python` `television` `terminal` `tmux` | 68 | 🔄 2026-10-25 |
| [**herdr-sessionizer**](https://github.com/andrewchng/herdr-sessionizer)<br><sub>andrewchng</sub> | 通过模糊搜索打开项目和工作树，再从声明式 TOML 布局（标签页、窗格分割、命令、按仓库覆盖配置）启动工作区 | `bun` `fuzzy-finder` `fzf` `git-worktree` `sessionizer` | 52 | 🔄 2026-10-26 |
| [**herdr-plugin-sesh**](https://github.com/fullerzz/herdr-plugin-sesh)<br><sub>fullerzz</sub> | 面向 Herdr 的 Sesh 风格工作区选择器 TUI，集成 zoxide，可从常用目录创建工作区 | `bubbletea` `sesh` `tui` `zoxide` `go` | 51 | 🔄 2026-10-25 |
| [**herdr-command-palette**](https://github.com/JanTvrdik/herdr-command-palette)<br><sub>JanTvrdik</sub> | herdr 的 fzf 命令面板——模糊选择并运行任意插件操作 | `shell` | 45 | 2026-06-29 |
| [**herdr-drovr**](https://github.com/AVGVSTVS96/herdr-drovr)<br><sub>AVGVSTVS96</sub> | 轻松移动 herdr 窗格和标签页 | `fzf` `terminal` `javascript` | 26 | 2026-10-10 |
| [**herdr-palette**](https://github.com/vjeantet/herdr-palette)<br><sub>vjeantet</sub> | Sublime Text / VS Code 风格的 herdr 命令面板——内置操作、插件动作和你自己的命令，全部藏在一个按键之后 | `command-palette` `fuzzy-search` `terminal` `tui` `rust` | 19 | 2026-10-05 |
| [**herdr-omni**](https://github.com/mmjang/herdr-omni)<br><sub>mmjang</sub> | 一个搜索框，覆盖 Herdr 的工作区、操作以及正在运行或已保存的 Codex 与 Claude 会话。可按名称模糊查找、搜索对话内容，并从中断处继续。 | `claude-code` `codex` `opencode` `rust` | 13 | 2026-10-08 |
| [**herdr-zoxide**](https://github.com/den-tanui/herdr-zoxide)<br><sub>den-tanui</sub> | 从 zoxide 记录的目录创建工作区、标签页和窗格的 Herdr 插件 | `zoxide` `shell` | 12 | 2026-07-25 |
| [**herdr-palette**](https://github.com/ramarivera/herdr-palette)<br><sub>ramarivera</sub> | 面向 Herdr 工作区的 Rust/Ratatui 模糊命令面板 | `command-palette` `ratatui` `rust` `terminal` `tui` | 11 | 2026-09-11 |
| [**herdr-blink**](https://github.com/dartyuhov/herdr-blink)<br><sub>dartyuhov</sub> | Blazing-fast fuzzy agent switcher for herdr: attention first, then most recently used. | `rust` `tui` | 9 | 🔄 2026-10-11 |
| [**herdr-quick-actions**](https://github.com/enekos/herdr-quick-actions)<br><sub>enekos</sub> | 以 fzf 选择器调用 herdr 原生的标签页/窗格/工作区操作，按使用频率排序——不必再死记快捷键 | `shell` | 9 | 2026-08-05 |
| [**🆕 levi**](https://github.com/rsdlt/levi)<br><sub>rsdlt</sub> | The fastest blade for your git history. Fuzzy search for you, plain text for your agents. | `claude-code` `cli` `coding-agents` `diff` `fzf` | 8 | 🔄 2026-10-22 |
| [**herdr-openr**](https://github.com/wraithyy/herdr-openr)<br><sub>wraithyy</sub> | herdr 插件：模糊查找并打开终端或 AI Agent 刚提到的文件/URL——在 Claude 窗格中会读取会话记录 | `shell` | 8 | 2026-08-14 |
| [**herdr-switchboard**](https://github.com/crafts69guy/herdr-switchboard)<br><sub>crafts69guy</sub> | herdr 插件：在一个 Rust 编写的 TUI 中模糊切换运行中的 Agent、已打开的工作区和 ghq 管理的仓库——并可将仓库在新工作区、标签页、分屏或当前窗格中打开 | `developer-tools` `ghq` `ratatui` `rust` `terminal` | 7 | 🔄 2026-10-18 |
| [**herdr-transcripts**](https://github.com/hxreborn/herdr-transcripts)<br><sub>hxreborn</sub> | 用你记得的任意关键词，搜索过去或正在进行的编码 Agent 会话，然后跳转过去或直接恢复。 | `claude-code` `codex` `coding-agents` `droid` `fzf` | 7 | 2026-10-08 |
| [**herdr-hunk**](https://github.com/JacquesvanWyk/herdr-hunk)<br><sub>JacquesvanWyk</sub> | herdr 中用于 Hunk 差异对比的交互式 fzf 选择器：支持提交、范围、stash，并可在 Agent 完成时自动打开 | `fzf` `hunk` `shell` | 6 | 2026-07-12 |
| [**bracco**](https://github.com/rawnly/bracco)<br><sub>rawnly</sub> | Fast, Git-aware fuzzy file picker for the terminal. | `cli` `fuzzy` `fuzzy-finder` `ratatui` `rust` | 6 | 2026-09-30 |
| [**herdr-sessionizer**](https://github.com/salkhalil/herdr-sessionizer)<br><sub>salkhalil</sub> | herdr 的 tmux-sessionizer：用 fzf 搜索已打开的工作区和 zoxide 目录，创建或聚焦并附带模板标签页 | `shell` | 6 | 2026-07-27 |
| [**herdr-kiosk**](https://github.com/thomasschafer/herdr-kiosk)<br><sub>thomasschafer</sub> | 模糊查找 Git 仓库和分支，并在 Herdr 中作为工作树打开 | `rust` | 6 | 🔄 2026-10-22 |
| [**herdr-launcher**](https://github.com/arjenblokzijl/herdr-launcher)<br><sub>arjenblokzijl</sub> | 模糊选择一个声明式 TOML 工作流，填写表单，在新的 herdr 空间中启动编程 Agent | `launcher` `ratatui` `rust` `tui` | 5 | 2026-07-10 |
| [**herdr-palette**](https://github.com/cesarferreira/herdr-palette)<br><sub>cesarferreira</sub> | 面向 Herdr 的弹窗式命令面板 | `typescript` | 5 | 2026-09-08 |
| [**herdr-pickr**](https://github.com/javoscript/herdr-pickr)<br><sub>javoscript</sub> | YAP！又一个面向 Herdr 多路复用器的选择器。 | `fzf` `lua` | 5 | 2026-09-23 |
| [**herdr-ssh-manager**](https://github.com/jorge07RD/herdr-ssh-manager)<br><sub>jorge07RD</sub> | 保存 SSH 主机，并从 Herdr 内的模糊弹窗中重新连接——按 Enter 即可直接将弹窗内容交给 ssh | `rust` `ssh` `terminal` `tui` | 5 | 2026-08-24 |
| [**herdr-pane-navigator**](https://github.com/mr04vv/herdr-pane-navigator)<br><sub>mr04vv</sub> | 将 Herdr 的工作区、标签页和窗格作为一棵模糊树进行导航——以每个窗格实际在做什么为线索 | `coding-agents` `fzf` `terminal` `tui` `shell` | 5 | 2026-09-07 |
| [**herdr-keymap**](https://github.com/The-Dave-Stack/herdr-keymap)<br><sub>The-Dave-Stack</sub> | herdr 插件：在浮层面板中展示所有快捷键，并可直接运行有对应 CLI 命令的那些 | `typescript` | 5 | 2026-08-12 |
| [**herdr-configurable-picker**](https://github.com/yoshiori/herdr-configurable-picker)<br><sub>yoshiori</sub> | 面向 herdr 的树形跳转选择器，快捷键完全可配置 | `rust` | 5 | 2026-07-05 |
| [**herdr-cast**](https://github.com/aliou/herdr-cast)<br><sub>aliou</sub> | 个人 Herdr 插件——提供原生 macOS Agent 通知、模糊工作区导航、基于 zoxide 的工作区创建以及布局命令 | `developer-tools` `macos` `notifications` `ratatui` `rust` | 4 | 🔄 2026-10-24 |
| [**herdr-workspace-save**](https://github.com/chandrasekharan98/herdr-workspace-save)<br><sub>chandrasekharan98</sub> | 保存 Herdr 工作区（布局、工作目录、Agent 会话、正在运行的命令），之后可从 fzf 选择器中重新打开 | `claude-code` `terminal` `tmux` `python` | 4 | 🔄 2026-10-13 |
| [**herdr-grep-nvim**](https://github.com/cinco/herdr-grep-nvim)<br><sub>cinco</sub> | herdr 插件：用 fzf + ripgrep 进行实时搜索，并在你工作区旁边的分屏中用 nvim 打开匹配结果 | `shell` | 3 | 2026-07-17 |
| [**herdr-simple-switcher**](https://github.com/haphamdev/herdr-simple-switcher)<br><sub>haphamdev</sub> | 对工作区、标签页和 AI Agent 进行模糊搜索 | `shell` | 3 | 🔄 2026-10-15 |
| [**herdr-command-palette**](https://github.com/hota911/herdr-command-palette)<br><sub>hota911</sub> | 面向 herdr 内置操作（工作区、标签页、窗格、Agent）的 fzf 命令面板 | `command-palette` `fzf` `shell` | 3 | 2026-08-16 |
| [**herdr-spotify**](https://github.com/iikjl/herdr-spotify)<br><sub>iikjl</sub> | herdr 的 Spotify 正在播放浮层插件——专辑封面、播放控制，并可通过 Spotify Web API 搜索/加入队列/点赞 | `spotify` `terminal` `go` | 3 | 2026-07-07 |
| [**herdr-workspacer**](https://github.com/mcuste/herdr-workspacer)<br><sub>mcuste</sub> | 使用 zoxide 查找项目，然后切换或创建 Herdr 工作区 | `rust` `tui` `zoxide` | 3 | 2026-10-01 |
| [**herdr-plugin-picker**](https://github.com/purehate/herdr-plugin-picker)<br><sub>purehate</sub> | Herdr 的浮动弹窗选择器——可跳转到任意空间、Agent、标签页或窗格，向所有标记窗格广播同一条命令，并从 ~/.ssh/config 发起带实时可达性检测的 SSH 连接。完全由键盘驱动。 | `broadcast` `fuzzy-finder` `golang` `picker` `ssh` | 3 | 2026-09-18 |
| [**herdr-fzf-terminal-browser**](https://github.com/to4iki/herdr-fzf-terminal-browser)<br><sub>to4iki</sub> | 一个 herdr 插件：按下一个键，即可用 fzf 从当前窗格中选取一个 URL，并在 terminal-browser 中打开。 | `fzf` `rust` `terminal-browser` | 3 | 2026-10-06 |
| [**herdr-agent-recency**](https://github.com/ugurtarlig/herdr-agent-recency)<br><sub>ugurtarlig</sub> | 支持主题的 Herdr 选择器，按 Codex 和 Claude 有意义的活动情况排序 | `claude-code` `codex` `fzf` `python` | 3 | 2026-07-17 |
| [**herdr-command-palette**](https://github.com/alon-z/herdr-command-palette)<br><sub>alon-z</sub> | Herdr 插件：模糊搜索工作区/目录的命令面板 | `javascript` | 2 | 2026-09-22 |
| [**herdr-palette**](https://github.com/Binb1/herdr-palette)<br><sub>Binb1</sub> | Herdr 的命令面板。可跳转到工作区和 Agent，运行插件动作，也可执行 Herdr 命令。 | `go` | 2 | 🔄 2026-10-26 |
| [**herdr-sesh-bro**](https://github.com/cyperx84/herdr-sesh-bro)<br><sub>cyperx84</sub> | 面向 Herdr 的 sesh 风格模糊会话选择器——将工作区、Agent 和 zoxide 目录整合到一个带实时预览的 fzf 弹窗中 | `go` | 2 | 2026-09-19 |
| [**🆕 herdr-workspaces-manager**](https://github.com/dardT/herdr-workspaces-manager)<br><sub>dardT</sub> | Discover projects and create distinctly named Herdr workspaces with a fast terminal picker | `rust` | 2 | 🔄 2026-10-19 |
| [**herdr-workspace-launcher**](https://github.com/ImArtisann/herdr-workspace-launcher)<br><sub>ImArtisann</sub> | 面向 macOS 的 Herdr 插件，通过可搜索的键盘驱动目录选择器快速创建聚焦工作区 | `typescript` | 2 | 2026-07-16 |
| [**herdr-recent-workspaces**](https://github.com/ismaelosuna7824/herdr-recent-workspaces)<br><sub>ismaelosuna7824</sub> | Herdr 的「打开最近使用的文件夹」——可模糊筛选你曾作为工作区打开过的文件夹列表。选择一个即可打开或重新聚焦该工作区，也可浏览文件系统打开新的 | `go` | 2 | 2026-07-10 |
| [**herdr-nav**](https://github.com/karanpatel1993/herdr-nav)<br><sub>karanpatel1993</sub> | 在 herdr 中进行文件导航、代码搜索和 jdb 调试——将 fzf、ripgrep 与 Java 调试器接入你的终端工作区。 | `shell` | 2 | 2026-09-17 |
| [**herdr-ghq-open-agent**](https://github.com/kenchan/herdr-ghq-open-agent)<br><sub>kenchan</sub> | herdr 插件：用 fzf 对 ghq 管理的仓库进行增量搜索，在工作区/标签页中打开所选仓库并启动 claude | `fzf` `ghq` `shell` | 2 | 2026-08-03 |
| [**herdr-keybind-search**](https://github.com/malone-c/herdr-keybind-search)<br><sub>malone-c</sub> | herdr 的可搜索快捷键浮层（基于 fzf）。按下一个键即可模糊搜索你的快捷键 | `shell` | 2 | 2026-07-15 |
| [**herdr-flash-picker**](https://github.com/TinyWhite1997/herdr-flash-picker)<br><sub>TinyWhite1997</sub> | 为 Herdr 提供的快速窗格选择器，采用对齐的一到两字母跳转标签。 | `rust` `tui` | 2 | 2026-09-07 |
| [**herdr-palette**](https://github.com/vika2603/herdr-palette)<br><sub>vika2603</sub> | 为 herdr 打造的命令面板：一个弹窗即可搜索 herdr 的命令、所有已安装插件的操作、你自定义的命令，以及会话中打开的一切内容，并执行你选中的项目。 | `bubbletea` `command-palette` `fzf` `go` `terminal` | 2 | 2026-10-11 |
| [**herdr-bitwarden**](https://github.com/WillowMist/herdr-bitwarden)<br><sub>WillowMist</sub> | 模糊搜索你的 Bitwarden 密码库并粘贴/复制凭据——tmux-bitwarden 的 herdr 移植版 | `bitwarden` `fzf` `terminal` `tmux` `shell` | 2 | 2026-08-11 |
| [**herdr-waypoint**](https://github.com/wraithyy/herdr-waypoint)<br><sub>wraithyy</sub> | 为文件夹命名并保存，从模糊列表中选一个，作为新的 herdr 工作区打开 | `shell` | 2 | 2026-08-12 |
| [**herdr-open-local-paths**](https://github.com/yigitkg/herdr-open-local-paths)<br><sub>yigitkg</sub> | 检测本地路径，并通过简易选择器在 Windows、Linux 和 WSL 上打开或显示的 Herdr 插件 | `developer-tools` `python` `terminal` `wsl` | 2 | 2026-07-28 |
| [**herdr-sessionizer**](https://github.com/42lizard/herdr-sessionizer)<br><sub>42lizard</sub> | tmux-sessionizer 风格的 herdr 插件 | `fzf` `shell` | 1 | 2026-08-28 |
| [**herdr-url-picker**](https://github.com/abrose/herdr-url-picker)<br><sub>abrose</sub> | herdr 插件：用 fzf 选取当前窗格中显示的 URL，并用默认浏览器打开 | `shell` | 1 | 2026-07-22 |
| [**herdr-url-picker**](https://github.com/chouxcreams/herdr-url-picker)<br><sub>chouxcreams</sub> | Herdr 插件：从聚焦窗格中选取一个 URL 并在浏览器中打开 | `shell` | 1 | 2026-07-22 |
| [**herdr-hosts**](https://github.com/ecylmz/herdr-hosts)<br><sub>ecylmz</sub> | 面向 Herdr 的分层 SSH 主机选择器，文件夹和备注直接来自 ~/.ssh/config。 | `ratatui` `rust` `ssh` `terminal` `tui` | 1 | 2026-09-18 |
| [**herdr-fzf-url**](https://github.com/kaar/herdr-fzf-url)<br><sub>kaar</sub> | 从 herdr 窗格的滚动记录中模糊查找并打开 URL——tmux-fzf-url 的 herdr 移植版 | `shell` | 1 | 2026-07-29 |
| [**herdr-shortcut**](https://github.com/matheus3301/herdr-shortcut)<br><sub>matheus3301</sub> | 面向 Herdr 的快捷任务选择器兼编程 Agent 启动器 | `bubbletea` `claude-code` `codex` `coding-agents` `developer-tools` | 1 | 2026-07-24 |
| [**herdr-pane-picker**](https://github.com/ugurtarlig/herdr-pane-picker)<br><sub>ugurtarlig</sub> | 输入窗格上显示的字符提示来选择 Herdr 窗格 | `terminal` `wezterm` `python` | 1 | 2026-07-17 |
| [**herdr-telescope**](https://github.com/zackshen/herdr-telescope)<br><sub>zackshen</sub> | 面向 herdr 的 fzf 命令 telescope——支持原生操作、插件操作、文件查找（@）和实时 ripgrep 搜索（/） | `fzf` `rust` | 1 | 2026-08-20 |

<details><summary>与此目的也相关</summary>

- [ThorstenRhau/token](https://github.com/ThorstenRhau/token) — Neovim 配色方案，并附带面向整个终端环境的社区贡献主题。
- [beyondlex/herdr-recent-navigator](https://github.com/beyondlex/herdr-recent-navigator) — 在最近使用的工作区、标签页、窗格和 Agent 之间进行 MRU（最近使用）切换——类似 JetBrains 的「最近文件」。此外还支持对任意窗格内容进行模糊搜索，完全由键盘驱动。
- [JacquesvanWyk/herdr-linear](https://github.com/JacquesvanWyk/herdr-linear) — 在 herdr 分屏窗格或标签页中运行的 fzf 驱动 Linear 面板：搜索 issue、深入项目、创建 issue、修改状态
- [hamzahraihan/herdr-better-workspace](https://github.com/hamzahraihan/herdr-better-workspace) — 面向 herdr（AI 编码 Agent 的终端工作区管理器）的交互式「打开工作区」选择器插件。
- [42lizard/herdr-dwm-layout](https://github.com/42lizard/herdr-dwm-layout) — 面向 Herdr 的 DWM 风格 master/stack 布局

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-automation"></a>

## 自动化、钩子与定时任务

> 想在创建工作树或指定时机自动运行固定的操作步骤

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-browser**](https://github.com/ogulcancelik/herdr-browser)<br><sub>ogulcancelik</sub> | 在 Herdr 窗格内渲染真实的 Chromium 视图，并通过 CDP 进行操控 | `browser` `browser-automation` `cdp` `chromium` `kitty-graphics` | 360 | 2026-08-22 |
| [**herdr-auto-title**](https://github.com/kryptamine/herdr-auto-title)<br><sub>kryptamine</sub> | 根据当前工作内容、Git 分支、终端活动和 Claude Code 会话，自动为 Herdr 的标签页和窗格命名。 | `claude-code` `coding-agents` `developer-tools` `terminal` `terminal-multiplexer` | 271 | 🔄 2026-10-26 |
| [**herdr-automatic-rename**](https://github.com/qu8n/herdr-automatic-rename)<br><sub>qu8n</sub> | Automatically name herdr tabs after the foreground process (like tmux) or agent session context | `shell` | 221 | 🔄 2026-10-22 |
| [**herdr-auto-title**](https://github.com/sh1ma/herdr-auto-title)<br><sub>sh1ma</sub> | 根据 Claude Code 和 Codex 的对话内容，自动生成 herdr 标签页标题 | `claude-code` `codex` `python` | 55 | 2026-09-11 |
| [**herdr-workflows**](https://github.com/aorumbayev/herdr-workflows)<br><sub>aorumbayev</sub> | 为 herdr 中的重复步骤提供声明式自动化 | `agentic-ai` `agentic-workflow` `agents` `ai` `claude` | 37 | 🔄 2026-10-22 |
| [**zed-herdr**](https://github.com/ImArtisann/zed-herdr)<br><sub>ImArtisann</sub> | 自动将当前活动的 HerdR 工作区与已有的 Zed 会话保持同步 | `typescript` | 35 | 2026-10-06 |
| [**herdr-worktree-setup**](https://github.com/tdi/herdr-worktree-setup)<br><sub>tdi</sub> | herdr 插件：创建工作树时执行按项目定制的初始化步骤（从 main 复制 .env、mise trust、direnv allow、安装依赖等） | `javascript` | 30 | 2026-09-11 |
| [**herdr-auto-pilot**](https://github.com/0xGosu/herdr-auto-pilot)<br><sub>0xGosu</sub> | 通过 Herdr API 代替你自动向运行中的 AI 编程 CLI 发送提示词的 Herdr 插件。插件具有从你的操作中学习的训练模式，并内置防止危险/恶意操作的防护机制。经过充分训练后，可让它以「完全自主提示（FSP）」模式运行 | `go` | 28 | 🔄 2026-10-16 |
| [**herdr-automations**](https://github.com/DnzzL/herdr-automations)<br><sub>DnzzL</sub> | 在终端中运行、面向编程 Agent 的定时任务，基于 Herdr。每次运行都会准备一条提示词、一行 cron 和一个全新的 git 工作树。仅需一个 YAML 文件，无需存储、提供预编译二进制、可按自动化单独指定模型、支持睡眠后补跑，并附带实时看板 | `ai-agents` `automation` `claude-code` `coding-agents` `cron` | 20 | 🔄 2026-10-20 |
| [**bermuda**](https://github.com/bon5co/bermuda)<br><sub>bon5co</sub> | 在 herdr 上由 Claude Code 驱动的编排——Agent 无法跳过的流程、定时任务、带 claim 的线程，以及供 Agent 日后检索的论坛 | `agent-orchestration` `agents` `ai-agents` `automation` `claude-code` | 14 | 🔄 2026-10-21 |
| [**herdr-routines**](https://github.com/mrcndz/herdr-routines)<br><sub>mrcndz</sub> | 运行定时任务的 Herdr 插件：按 cron 或固定间隔在工作区中打开标签页，运行命令或启动 Agent | `python` | 12 | 2026-07-18 |
| [**herdr-updater**](https://github.com/diegopzz/herdr-updater)<br><sub>diegopzz</sub> | 在整个机群范围内安全地让 Herdr 本体及其插件保持最新 | `rust` `updater` | 10 | 2026-09-17 |
| [**herdr-agent-config-manager**](https://github.com/Phoobobo/herdr-agent-config-manager)<br><sub>Phoobobo</sub> | 混合 CLI + Herdr 插件，用于检测并集中管理 Agent 的 skill、MCP、插件和 hook | `python` | 10 | 2026-09-06 |
| [**herdr-tab-title**](https://github.com/aarsh21/herdr-tab-title)<br><sub>aarsh21</sub> | 为 Herdr 提供类似 tmux 的自动标签页标题 | `rust` `terminal` `tmux` | 8 | 2026-07-08 |
| [**herdr-shepherd**](https://github.com/mikedclarke/herdr-shepherd)<br><sub>mikedclarke</sub> | 面向 herdr 的定时 Agent 会话——将心跳检测、cron 例程和脚本作为可见的 herdr 工作区启动 | `coding-agents` `cron` `go` `scheduler` `tui` | 7 | 2026-10-09 |
| [**herdr-fwd**](https://github.com/go-min/herdr-fwd)<br><sub>go-min</sub> | 为远程 Herdr 会话自动设置回环端口转发 | `port-forwarding` `ssh` `terminal` `rust` | 6 | 2026-10-07 |
| [**herdr-sched**](https://github.com/husniadil/herdr-sched)<br><sub>husniadil</sub> | 面向 Herdr 编程 Agent 的调度与触发器——cron 任务和 webhook/文件监视触发器会向相邻插件触发动作，每个动作都由其执行主体签名。全部由一个 Go 二进制程序实现 | `ai-agents` `cron` `mcp-server` `scheduler` `webhooks` | 5 | 2026-08-30 |
| [**herdr-pane-balancer**](https://github.com/jeph/herdr-pane-balancer)<br><sub>jeph</sub> | 在窗格创建、关闭和退出时，自动均衡、均分并平铺 Herdr 终端窗格 | `python` | 5 | 2026-08-02 |
| [**herdr-tab-autorun**](https://github.com/hanbong5938/herdr-tab-autorun)<br><sub>hanbong5938</sub> | 根据 TOML 规则，在每个新标签页中自动运行 shell 命令或启动编码 Agent 的 Herdr 插件。 | `ai-agents` `automation` `nodejs` `terminal` `javascript` | 4 | 🔄 2026-10-11 |
| [**🆕 herdr-island**](https://github.com/speardragon/herdr-island)<br><sub>speardragon</sub> | Your herdr agents live in the MacBook notch: approve, answer and watch them from a Dynamic Island-style panel | `ai-agents` `claude-code` `macos` `notch` `swiftui` | 4 | 🔄 2026-10-26 |
| [**herdr-review-loop**](https://github.com/mikhail-angelov/herdr-review-loop)<br><sub>mikhail-angelov</sub> | 在 herdr 工作区中让 Agent 之间自动进行交叉评审——一个负责编写，另一个负责评审，如此反复 | `terminal` `go` | 3 | 🔄 2026-10-12 |
| [**herdr-plugin**](https://github.com/ppggff/herdr-plugin)<br><sub>ppggff</sub> | 自动记住并恢复每个 Herdr 窗格对应的正确 macOS 输入法（IME） | `ime` `input-method` `macos` `python` | 3 | 2026-07-27 |
| [**herdr-autocontinue**](https://github.com/rcosteira79/herdr-autocontinue)<br><sub>rcosteira79</sub> | 监控 Agent 是否触及用量上限，以徽章形式显示重置倒计时（$wall），并在时间窗口重新开放后，向你预先设置的 Agent 重新发送提示词 | `python` | 3 | 2026-09-23 |
| [**herdr-comment-on-copy**](https://github.com/rheech22/herdr-comment-on-copy)<br><sub>rheech22</sub> | Drag to select terminal text and open a comment popup automatically. Send feedback with context to AI agents in Herdr. | `typescript` | 3 | 2026-10-05 |
| [**herdr-labels**](https://github.com/Angel-O/herdr-labels)<br><sub>Angel-O</sub> | 在保留手动标签的同时，自动为标签页命名和编号的 Herdr 插件 | `rust` | 2 | 🔄 2026-10-25 |
| [**herdr-auto-update**](https://github.com/dio16/herdr-auto-update)<br><sub>dio16</sub> | herdr 插件：启动时检查已安装插件是否有更新的上游提交，如有则自动重新安装 | `rust` | 2 | 2026-08-16 |
| [**herdr-mcp**](https://github.com/eugeneb50/herdr-mcp)<br><sub>eugeneb50</sub> | herdr plugin and MCP server: drive herdr panes and agents from AI clients, with recipes, triggers, schedules, a dashboard and a web playground | `mcp` `rust` | 2 | 🔄 2026-10-26 |
| [**herdr-routines**](https://github.com/guidodinello/herdr-routines)<br><sub>guidodinello</sub> | _(暂无描述)_ | `python` | 2 | 🔄 2026-10-26 |
| [**herdr-js-worktree-bootstrap**](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap)<br><sub>LeonardoTrapani</sub> | 为 JavaScript 和 TypeScript 自动初始化 Herdr 工作树，支持基于锁文件的安装和安全的环境变量还原 | `automation` `bun` `developer-tools` `git-worktree` `javascript` | 2 | 2026-07-15 |
| [**herdr-callsigns**](https://github.com/reobin/herdr-callsigns)<br><sub>reobin</sub> | auto-name every herdr pane with a short memorable callsign, so you and your agent can use pane names instead of IDs. | `shell` | 2 | 🔄 2026-10-15 |
| [**🆕 herdr-kata**](https://github.com/salmonumbrella/herdr-kata)<br><sub>salmonumbrella</sub> | Runs Kata cron jobs and workflows as Herdr agents | `kata` `go` | 2 | 🔄 2026-10-25 |
| [**herdr-hermes-manager**](https://github.com/skaftanis/herdr-hermes-manager)<br><sub>skaftanis</sub> | Hermes Agent workspaces, cron controls, recent conversations and continuous Bot chats for Herdr | `hermes-agent` `macos` `terminal` `tui` `python` | 2 | 🔄 2026-10-15 |
| [**herdr-starkeep**](https://github.com/yuya-take/herdr-starkeep)<br><sub>yuya-take</sub> | Watch your herdr agents work as knights on an orbital training ship — subagents come in as apprentices. | `rust` | 2 | 2026-10-06 |
| [**🆕 herdr-claude-autoupdate**](https://github.com/0xMMA/herdr-claude-autoupdate)<br><sub>0xMMA</sub> | herdr plugin: restarts idle Claude Code panes onto the newly installed version, in place, same session and flags, drafts kept. | `claude-code` `typescript` | 1 | 2026-10-11 |
| [**herdr-triggers**](https://github.com/cantona/herdr-triggers)<br><sub>cantona</sub> | 常驻监听窗格输出并按正则表达式触发动作：自动登录等由正则驱动的终端触发器。 | `rust` `terminal` `terminal-based` `terminal-multiplexer` `trigger` | 1 | 2026-09-18 |
| [**say-hook**](https://github.com/HikaruEgashira/say-hook)<br><sub>HikaruEgashira</sub> | 使用 ElevenLabs 文字转语音朗读 Claude Code hook 事件的 macOS CLI | `typescript` | 1 | 🔄 2026-10-19 |
| [**herdr-worktree-cleanup**](https://github.com/poislagarde/herdr-worktree-cleanup)<br><sub>poislagarde</sub> | 当对应的 Herdr 空间关闭时，自动清理可安全删除的 GitHub PR worktree。Python 编写，无依赖，MIT 许可。 | `git-worktree` `python` | 1 | 2026-09-11 |
| [**herdr-nixos-vm**](https://github.com/Slimydog21/herdr-nixos-vm)<br><sub>Slimydog21</sub> | 面向 herdr 的 NixOS 虚拟机窗格——启动、停止、监视 Hashimoto 风格的开发虚拟机，并可 ssh 连接。需要 nixos-vm kit | `shell` | 1 | 2026-08-18 |
| [**herdr-jump-number**](https://github.com/voice0726/herdr-jump-number)<br><sub>voice0726</sub> | 在不破坏 Herdr 自动工作区标签的前提下，在工作区和标签页上显示跳转键编号的 Herdr 插件。 | `typescript` | 1 | 2026-09-19 |

<details><summary>与此目的也相关</summary>

- [freethinkel/herdr-plugin-git-worktree-hooks](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks) — 在创建/移除 git 工作树时运行 shell 命令——一份 YAML 配置适用于所有项目，放在任何仓库之外
- [timofey-TK/herdr-worktree-hooks](https://github.com/timofey-TK/herdr-worktree-hooks) — herdr 插件：在创建、打开或删除 git 工作树时运行自定义的初始化/清理命令
- [miko-misa/herdr-portfwd](https://github.com/miko-misa/herdr-portfwd) — 面向远程机器上编程 Agent 的自动 SSH 端口转发——Ctrl+点击 Agent 打印的 localhost URL，即可在你本机以相同端口打开该页面。一个 Herdr 插件
- [itisbryan/herdr-gh-checks](https://github.com/itisbryan/herdr-gh-checks) — herdr 插件：在窗格中监视并查看当前 PR 的 CI，并在侧边栏行中显示 CI/合并状态。使用 Go + Bubble Tea 编写
- [zhuravel/magnum](https://github.com/zhuravel/magnum) — Your AI coding agents as a pull-request review team: Claude Code, Codex and others review each push in herdr…

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-session"></a>

## 会话保存与恢复

> 关闭工作后，希望之后能从同一状态继续

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-resurrect**](https://github.com/ntindle/herdr-resurrect)<br><sub>ntindle</sub> | herdr 的 tmux-resurrect——快照工作区、标签页、窗格、当前目录、运行中的程序和 Agent，并在崩溃或重启后恢复 | `crash-recovery` `session-manager` `terminal-multiplexer` `tmux-resurrect` `javascript` | 40 | 2026-10-05 |
| [**session-digger**](https://github.com/taxueseek/session-digger)<br><sub>taxueseek</sub> | 跨环境会话历史挖掘与知识管理。分析记录。支持 Claude/Grok/Kimi Code/Codex/WorkBuddy/Trae CN 等主流环境 | `claude-code` `conversation-analysis` `jsonl` `knowledge-management` `log-analysis` | 32 | 2026-09-23 |
| [**herdr-notes**](https://github.com/alexarthurs/herdr-notes)<br><sub>alexarthurs</sub> | 面向 herdr 的持久化 Markdown 笔记窗格——每个工作区一份笔记，支持预览渲染+编辑模式，自动保存且重启后仍保留 | `markdown` `notes` `ratatui` `rust` `terminal` | 23 | 🔄 2026-10-17 |
| [**herdr-session-parker**](https://github.com/iviaxpow3r/herdr-session-parker)<br><sub>iviaxpow3r</sub> | 用于暂存窗格/标签页，并在之后恢复受支持的 Agent 会话的 Herdr 插件 | `agent-tools` `python` | 13 | 2026-07-03 |
| [**herdr-agent-inbox**](https://github.com/douglascorrea/herdr-agent-inbox)<br><sub>douglascorrea</sub> | herdr 编程 Agent 的收件箱——会话标题、已读/未读标记、运行时长、工作区汇总、可续接的聊天记录 | `ai-agents` `terminal` `python` | 11 | 2026-07-28 |
| [**herdr-assist**](https://github.com/walcew/herdr-assist)<br><sub>walcew</sub> | 面向 AI 编程 Agent 终端复用器 Herdr 的实体桌面面板——用颜色显示会话状态，当 Agent 停下来请求决策时会响铃提醒。基于 ESP32-S3 + LVGL，提供预编译固件 | `ai-agents` `claude-code` `coding-agents` `embedded` `esp-idf` | 10 | 🔄 2026-10-23 |
| [**herdr-oh-my-agent**](https://github.com/GavinTomlins/herdr-oh-my-agent)<br><sub>GavinTomlins</sub> | 将 oh-my-openagent 的每个子 Agent 委派实时镜像到独立的 Herdr 窗格或标签页——保留完整会话状态和滚动记录 | `typescript` | 7 | 2026-07-31 |
| [**sheep**](https://github.com/gokay-ai/sheep)<br><sub>gokay-ai</sub> | 面向 AI 编程 Agent 的撤销功能。Agent 的每一轮操作都会成为一个可恢复的检查点 | `ai-agents` `git` `llm` `rust` `tui` | 6 | 2026-08-28 |
| [**herdr-undo-close**](https://github.com/pedroloch/herdr-undo-close)<br><sub>pedroloch</sub> | 如浏览器的 Cmd+Shift+T 一样，在 herdr 中重新打开已关闭的标签页——恢复标签名、含比例的分屏结构、每个窗格的工作目录以及标签页位置 | `python` | 4 | 2026-07-30 |
| [**herdr-hibernate**](https://github.com/bengemine/herdr-hibernate)<br><sub>bengemine</sub> | 让 Herdr 中空闲的编程 Agent 窗格（Claude Code、Codex、Grok）休眠——释放内存，按 Enter 即可恢复原会话 | `claude-code` `python` | 3 | 🔄 2026-10-16 |
| [**herdr-stash**](https://github.com/victor-software-house/herdr-stash)<br><sub>victor-software-house</sub> | 储藏 Herdr 工作区——停止其中的 Agent，同时保留其结构和对话内容，之后可从可点击的双栏弹窗中恢复 | `rust` `terminal` `tui` | 3 | 2026-07-29 |
| [**herdr-pane-id-labeler**](https://github.com/4Born/herdr-pane-id-labeler)<br><sub>4Born</sub> | 让窗格标签与如 w1:p2 之类的公开窗格 ID 保持同步的 Herdr 插件 | `developer-tools` `terminal` `javascript` | 2 | 2026-07-26 |
| [**herdr-agent-auto-naming**](https://github.com/azyu/herdr-agent-auto-naming)<br><sub>azyu</sub> | 一个 Herdr 插件，为检测到的每个 Agent 分配一个易读的双词名称，并作为窗格标签持久保存，重启后依然保留。 | `coding-agents` `developer-tools` `terminal` `python` | 2 | 🔄 2026-10-16 |
| [**herdr-revive**](https://github.com/cantona/herdr-revive)<br><sub>cantona</sub> | 恢复 Herdr 的命令、布局以及完全一致的 Agent 会话，支持预览、具名工作区和明确的恢复操作。 | `rust` `session-handoff` `session-history` `session-management` `session-manager` | 2 | 🔄 2026-10-15 |
| [**herdr-synchronize-panes**](https://github.com/furuhashin/herdr-synchronize-panes)<br><sub>furuhashin</sub> | Herdr 插件：将一条命令广播到当前标签页内的所有窗格（类似 tmux 的 synchronize-panes） | `javascript` | 2 | 2026-07-14 |
| [**herdr_sync**](https://github.com/kamaaina/herdr_sync)<br><sub>kamaaina</sub> | 同步 herdr 中的窗格 | `zig` | 2 | 2026-07-01 |
| [**herdr-e2b**](https://github.com/tomasvarga/herdr-e2b)<br><sub>tomasvarga</sub> | 按需将 git 工作树镜像到全新的 E2B 云沙盒——直接上传快照（包括未提交的更改），无需 push 或 clone。一个 herdr 插件 | `cli` `cloud-dev` `e2b` `git-worktree` `sandbox` | 2 | 2026-07-18 |
| [**herdr-thread-to-tab**](https://github.com/toyamarinyon/herdr-thread-to-tab)<br><sub>toyamarinyon</sub> | 让单窗格 Herdr 标签页标签与 Claude Code 和 Codex 的线程标题保持同步 | `rust` | 2 | 2026-08-06 |
| [**herdr-agent-hibernate**](https://github.com/dalogax/herdr-agent-hibernate)<br><sub>dalogax</sub> | 让 Herdr 中空闲的 AI Agent 窗格进入休眠：释放其占用的内存，待你返回时恢复同一会话。支持 OpenCode、Claude Code 和 Codex。 | `ai-agents` `claude-code` `codex` `opencode` `terminal` | 1 | 2026-10-01 |
| [**attic**](https://github.com/TheThoughtagen/attic)<br><sub>TheThoughtagen</sub> | 自动关闭空闲的 AI 编程会话，但会先归档每一个，方便之后恢复 | `claude-code` `developer-tools` `python` `session-management` `tui` | 1 | 2026-08-14 |
| [**herdr-agent-pins**](https://github.com/ZingerLittleBee/herdr-agent-pins)<br><sub>ZingerLittleBee</sub> | 将 Herdr Agent 会话持久固定在 Agents 侧边栏顶部 | `terminal` `javascript` | 1 | 2026-08-24 |
| [**🆕 herdr-plugin-session-pruner**](https://github.com/Gareth-Rouse/herdr-plugin-session-pruner)<br><sub>Gareth-Rouse</sub> | herdr 插件：记录工作区的最后使用时间，在 Spaces 侧边栏中显示已过去多久，并将闲置工作区排除在会话恢复之外 | `terminal-multiplexer` `shell` | 0 | 2026-10-05 |

<details><summary>与此目的也相关</summary>

- [nicosuave/memex](https://github.com/nicosuave/memex) — 搜索 Claude Code、Codex、Pi、OpenCode、GitHub Copilot 和 Cursor 的会话记录。恢复会话。追踪 token 使用
- [mmjang/herdr-omni](https://github.com/mmjang/herdr-omni) — 一个搜索框，覆盖 Herdr 的工作区、操作以及正在运行或已保存的 Codex 与 Claude 会话。可按名称模糊查找、搜索对话内容，并从中断处继续。
- [afogel/shepherdr](https://github.com/afogel/shepherdr) — 将委派出去的编程 Agent 收拢到可见、可审查的 herdr 窗格中，供你观察、恢复和接管的 herdr 插件
- [hxreborn/herdr-transcripts](https://github.com/hxreborn/herdr-transcripts) — 用你记得的任意关键词，搜索过去或正在进行的编码 Agent 会话，然后跳转过去或直接恢复。
- [AkashJana18/herdr-scratch](https://github.com/AkashJana18/herdr-scratch) — 面向 Herdr 的持久化速记板，为浮动实用窗格铺路
- [KokiKono/herdr-kanban](https://github.com/KokiKono/herdr-kanban) — 将任务与 herdr 标签页关联的终端看板，数据持久化在 SQLite 中
- [blaxel-ai/herdr-blaxel-sandbox-plugin](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin) — 从 Herdr 在持久化的 Blaxel Sandbox 中运行编程 Agent
- [ppggff/herdr-plugin](https://github.com/ppggff/herdr-plugin) — 自动记住并恢复每个 Herdr 窗格对应的正确 macOS 输入法（IME）
- [voodootikigod/adlc-herdr](https://github.com/voodootikigod/adlc-herdr) — ADLC 的 herdr 插件——按窗格显示阶段/工单/关卡状态，附带待办看板、关卡操作和 adlc-fleet 运行可观测性。是 voodootikigod/adlc/plugins/adlc-herdr 的自动同步…
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — 为 JavaScript 和 TypeScript 自动初始化 Herdr 工作树，支持基于锁文件的安装和安全的环境变量还原
- [mohaphez/herdr-flow](https://github.com/mohaphez/herdr-flow) — Persistent multi-agent task coordination for Herdr with guarded review and worktree cleanup

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-naming"></a>

## 标题、命名与外观

> 想让标签页名称和终端标题自动变得清晰易懂，或想改变外观

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-tab-smart-rename**](https://github.com/iurysza/herdr-tab-smart-rename)<br><sub>iurysza</sub> | 为 Herdr 生成基于上下文的工作区和标签页名称 | `ai` `bun` `terminal` `typescript` | 77 | 🔄 2026-10-26 |
| [**herdr-flock**](https://github.com/ragamo/herdr-flock)<br><sub>ragamo</sub> | 将你的 AI 编程 Agent 可视化为生活在俯视视角农场里的像素风羊群的 herdr 插件 | `cli` `ratatui` `rust` `tui` | 44 | 2026-08-31 |
| [**herdr-window-title-sync**](https://github.com/rjyo/herdr-window-title-sync)<br><sub>rjyo</sub> | 将工作区、标签页和 Agent 会话同步到终端标题（可配合 Moshi 使用） | `moshi` `terminal-title` `javascript` | 38 | 2026-06-26 |
| [**herdr-pet**](https://github.com/nikok6/herdr-pet)<br><sub>nikok6</sub> | 生活在 herdr 窗格中的小小桌面宠物——陪你的 Agent 一起打字、等待和庆祝。兼容任意 Codex pet | `rust` | 18 | 2026-08-26 |
| [**herdr-theme-picker**](https://github.com/qintmb/herdr-theme-picker)<br><sub>qintmb</sub> | 基于终端配色方案和自定义设置的 herdr UI 主题选择器 | `go` | 17 | 🔄 2026-10-18 |
| [**herdr-icon-agent-ui**](https://github.com/qintmb/herdr-icon-agent-ui)<br><sub>qintmb</sub> | 在 Herdr 侧边栏中渲染纵向对齐的单色 Agent 图标。通过自定义字体渲染，字形按终端 cap-height 进行非均匀缩放，与 Agent 名称、标签页和工作区标签紧密贴合，而不是显示为小方块 | `python` | 16 | 🔄 2026-10-14 |
| [**herdr-canvas**](https://github.com/aorumbayev/herdr-canvas)<br><sub>aorumbayev</sub> | 面向 herdr Agent 的鼠标驱动 ASCII 图表画布——在 TUI 中绘制，分享结构化 JSON，还可以让 AI 编辑它 | `agentic-ai` `agents` `ai-agents` `ascii-art` `bubbletea` | 8 | 2026-08-31 |
| [**herdr-claude-session-title**](https://github.com/bcihanc/herdr-claude-session-title)<br><sub>bcihanc</sub> | Herdr 插件：将 Claude Code 的会话标题（/rename 或自动摘要）同步到 herdr 窗格的元数据标题中 | `shell` | 8 | 2026-07-11 |
| [**herdr-pixel-office**](https://github.com/devangchhajed/herdr-pixel-office)<br><sub>devangchhajed</sub> | 在一个俯视角的像素小办公室里，看着你的 AI 编码 Agent 化身像素小人认真工作——一个 herdr 插件。 | `typescript` | 7 | 2026-09-21 |
| [**herdr-pet**](https://github.com/allmight-ai/herdr-pet)<br><sub>allmight-ai</sub> | Herdr 的伴侣电子宠物——映射你的编程 Agent 的状态 | `companion` `rust` `v-pet` | 6 | 2026-08-20 |
| [**herdr-ghostty-tab-title**](https://github.com/wjarka/herdr-ghostty-tab-title)<br><sub>wjarka</sub> | herdr 插件：在 Ghostty 标签标题中按颜色显示 Agent 各状态（阻塞/完成/工作中/空闲）的数量 | `ai-agents` `ghostty` `terminal` `python` | 6 | 2026-08-04 |
| [**herdr-town**](https://github.com/Efeguclu1/herdr-town)<br><sub>Efeguclu1</sub> | 把你的 Herdr 编程 Agent 当作一座 8 位像素小镇来观赏。无需离开，就能阅读并回复它们 | `ai-agents` `pixel-art` `terminal` `tui` `javascript` | 5 | 2026-10-03 |
| [**herdr-auto-namer**](https://github.com/kakigakki/herdr-auto-namer)<br><sub>kakigakki</sub> | herdr 的 ChatGPT 风格自动命名：Agent 使用其 Claude 会话标题，工作区使用其工作目录名 | `claude-code` `python` | 5 | 🔄 2026-10-21 |
| [**herdr-agent-titler**](https://github.com/killerz3/herdr-agent-titler)<br><sub>killerz3</sub> | 无需外部 API key，使用本地的 agy、claude、codex 或 opencode 运行环境，自动为 Herdr 标签页设置标题。 | `antigravity` `claude-code` `python` | 5 | 2026-09-03 |
| [**herdr-colors**](https://github.com/ariel-ps/herdr-colors)<br><sub>ariel-ps</sub> | Give each Herdr pane a distinct color. | `rust` | 4 | 2026-10-10 |
| [**tamagoxtix**](https://github.com/fabandrade88/tamagoxtix)<br><sub>fabandrade88</sub> | TamaGoxtix: a tiny pixel monster for Claude Code and herdr — animated spinner, usage charts, palettes and a powerline status line. | `claude-code` `claude-code-plugin` `omarchy` `pixel-art` `javascript` | 4 | 🔄 2026-10-20 |
| [**herdr-in-your-face**](https://github.com/JYasha11/herdr-in-your-face)<br><sub>JYasha11</sub> | 如果你放着被阻塞的 AI Agent 不管，一个巨大的 ASCII 脸会对你怒吼。你无视得越久，警告就升级得越厉害 | `javascript` | 4 | 2026-07-10 |
| [**herdr-tab-rename**](https://github.com/lmilojevicc/herdr-tab-rename)<br><sub>lmilojevicc</sub> | 将每个 Herdr 标签页自动重命名为其聚焦窗格的工作目录名。手动重命名过的标签页不受影响 | `go` | 4 | 2026-07-31 |
| [**herdr-questmancer**](https://github.com/opsydyn/herdr-questmancer)<br><sub>opsydyn</sub> | 为你的 Herdr 编程 Agent 打造的温馨 16 位冒险者公会。工作中的 Agent 在探索地下城，被阻塞的 Agent 在寻求指点，完成的工作则带着战利品归来 | `coding-agents` `pixel-art` `ratatui` `tui` `rust` | 4 | 2026-09-09 |
| [**herdr-nerd-font-tab-name**](https://github.com/rohankewal/herdr-nerd-font-tab-name)<br><sub>rohankewal</sub> | 为 herdr 标签页添加 Nerd Font 图标——joshmedeski/tmux-nerd-font-window-name 的 herdr 移植版 | `nerd-fonts` `python` `terminal` `tui` | 4 | 2026-07-31 |
| [**herdr-powershell-title-sync**](https://github.com/aclima01/herdr-powershell-title-sync)<br><sub>aclima01</sub> | window-title-sync 的 Windows/PowerShell 移植版：将终端标题同步为当前聚焦的 herdr 会话 | `powershell` | 3 | 2026-07-20 |
| [**herdr-workspace-renamer**](https://github.com/ryanlewis/herdr-workspace-renamer)<br><sub>ryanlewis</sub> | herdr 插件：将 Agent 会话名称同步到工作区标签 | `rust` | 3 | 🔄 2026-10-15 |
| [**zenbones-herdr**](https://github.com/AkashJana18/zenbones-herdr)<br><sub>AkashJana18</sub> | Minimal paper theme for Herdr. Port of zenbones zenwritten for the Herdr TUI. | `herdr-themes` `themes` `zen-themes` `zenbones` `shell` | 2 | 2026-10-01 |
| [**herdr-pane-autorename**](https://github.com/b12o/herdr-pane-autorename)<br><sub>b12o</sub> | 根据当前运行的进程名称，自动重命名窗格的 Herdr 插件。 | `shell` | 2 | 2026-09-07 |
| [**herdr-titles**](https://github.com/davidolrik/herdr-titles)<br><sub>davidolrik</sub> | 始终跟得上变化的 Herdr 标题。herdr-titles 会根据实际运行的内容（包括 AI Agent 的实时会话标题）为标签页和窗口命名，并通过一个小型 HCL 模板，从工作区、标签页、Agent 待处理数量和 shell 环境组合出窗口标题。即时生效，CPU 占用近乎为零。零配置即可开始使用，且可无限调整 | `ai-assisted` `go` | 2 | 2026-09-06 |
| [**herdr-english-coach**](https://github.com/GranamyrBR/herdr-english-coach)<br><sub>GranamyrBR</sub> | herdr 插件：彩色标注的英语纠错面板——在你工作时，编程 Agent 将语法和开发行话的修正实时记录到侧边窗格 | `english` `language-learning` `shell` | 2 | 2026-07-06 |
| [**herdr-ai-tab-name**](https://github.com/ndom91/herdr-ai-tab-name)<br><sub>ndom91</sub> | 使用本地 LLM 自动为 Herdr 标签页命名 | `local-llm` `python` | 2 | 2026-09-19 |
| [**herdr-nerd-font-tab-name-windows**](https://github.com/Only-Moon/herdr-nerd-font-tab-name-windows)<br><sub>Only-Moon</sub> | herdr-nerd-font-tab-name 的 Windows 移植版：为 herdr 标签页显示 Nerd Font 图标，跨平台支持 Windows、macOS、Linux，并支持按文件夹解析图标 | `herdr-windows` `icons` `nerd-fonts` `python` `title` | 2 | 2026-08-10 |
| [**herdr-theme-synthwave-84**](https://github.com/s3rgiosan/herdr-theme-synthwave-84)<br><sub>s3rgiosan</sub> | Synthwave '84 theme for Herdr | `python` | 2 | 2026-09-30 |
| [**herdr-claude-title**](https://github.com/ProjectAJ14/herdr-claude-title)<br><sub>ProjectAJ14</sub> | 一个 Herdr 插件，根据窗口内正在进行的工作为终端标签页、窗格和工作区命名——Claude Code 会话的标题由 Claude 通过 claude -p 自己撰写。使用 Go 编写，支持 macOS/Linux/Windows。 | `ai` `ai-agents` `anthropic` `claude` `claude-code` | 1 | 2026-10-05 |

<details><summary>与此目的也相关</summary>

- [kryptamine/herdr-auto-title](https://github.com/kryptamine/herdr-auto-title) — 根据当前工作内容、Git 分支、终端活动和 Claude Code 会话，自动为 Herdr 的标签页和窗格命名。
- [qu8n/herdr-automatic-rename](https://github.com/qu8n/herdr-automatic-rename) — Automatically name herdr tabs after the foreground process (like tmux) or agent session context
- [sh1ma/herdr-auto-title](https://github.com/sh1ma/herdr-auto-title) — 根据 Claude Code 和 Codex 的对话内容，自动生成 herdr 标签页标题
- [wyattjoh/herdr-plugin-renamer](https://github.com/wyattjoh/herdr-plugin-renamer) — 根据 Agent 的第一条提示词，重命名自动生成的 herdr 工作树分支和工作区（通过设备端 Apple FoundationModels 或 Codex）
- [ythx-101/herdr-social-glass](https://github.com/ythx-101/herdr-social-glass) — 面向 macOS 版 Herdr 的、适合截图分享的 Social Glass 主题与工作流插件
- [aarsh21/herdr-tab-title](https://github.com/aarsh21/herdr-tab-title) — 为 Herdr 提供类似 tmux 的自动标签页标题
- [funsaized/herdr-mise](https://github.com/funsaized/herdr-mise) — Run the pass, not the prompts 🧑‍🍳 A visualizer for your agents. A herdr plugin. Intentionally small footprint
- [suisya-systems/herdr-agent-office](https://github.com/suisya-systems/herdr-agent-office) — 将你的 Agent 团队呈现为像素风办公室的 herdr 插件。查看谁在工作、谁卡住了，并可直接跳转过去
- [azyu/herdr-agent-auto-naming](https://github.com/azyu/herdr-agent-auto-naming) — 一个 Herdr 插件，为检测到的每个 Agent 分配一个易读的双词名称，并作为窗格标签持久保存，重启后依然保留。
- [maedana/herdr-whereami](https://github.com/maedana/herdr-whereami) — 自动重命名标签页以显示你当前所在位置的 Herdr 插件——在 git 仓库内会显示为「仓库名/分支名」

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-text"></a>

## 文本与 URL 提取

> 想不用鼠标就抓取屏幕上显示的字符串、路径或 URL

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-pluck**](https://github.com/rmarganti/herdr-pluck)<br><sub>rmarganti</sub> | 从 Herdr 窗格中快速复制匹配特定模式的字符串 | `rust` | 25 | 🔄 2026-10-17 |
| [**herdr-tiny-fingers**](https://github.com/hotchpotch/herdr-tiny-fingers)<br><sub>hotchpotch</sub> | 面向 Herdr 的 tmux-fingers 风格可见屏幕复制提示 | `tools` `rust` | 15 | 🔄 2026-10-22 |
| [**herdr-fingers**](https://github.com/nathan-poncet/herdr-fingers)<br><sub>nathan-poncet</sub> | 👉 面向 Herdr 的 tmux-fingers——输入简短提示即可复制、粘贴或打开屏幕上的任意路径、URL、哈希值或数字。使用 Rust 编写，遵循整洁架构。 | `clean-architecture` `clipboard` `rust` `terminal` `tmux-fingers` | 12 | 🔄 2026-10-15 |
| [**herdr-scratchpad**](https://github.com/vjeantet/herdr-scratchpad)<br><sub>vjeantet</sub> | 每个标签页一个缓冲区用于准备提示词，一键即可投递到 Agent 的输入框 | `clipboard` `ratatui` `rust` `scratchpad` `terminal` | 6 | 2026-08-31 |
| [**herdr-flash**](https://github.com/youguanxinqing/herdr-flash)<br><sub>youguanxinqing</sub> | 面向 Herdr 窗格的 flash.nvim 风格搜索、选择与复制 | `rust` `terminal` | 6 | 2026-09-16 |
| [**herdr-paste-image**](https://github.com/ddfonseca/herdr-paste-image)<br><sub>ddfonseca</sub> | 将剪贴板中的图片以文件路径形式粘贴到 herdr 窗格——tmux-paste-image 的 herdr 移植版 | `shell` | 5 | 2026-07-30 |
| [**herdr-ferry**](https://github.com/wavrin/herdr-ferry)<br><sub>wavrin</sub> | 通过 SSH 在 Herdr 所在机器和你的笔记本电脑之间传输文件和剪贴板内容——无需云存储桶 | `rust` | 4 | 2026-08-29 |
| [**herdr-agent-copy-paste-fork**](https://github.com/calebcauthon/herdr-agent-copy-paste-fork)<br><sub>calebcauthon</sub> | 只需复制粘贴即可分叉，或用快捷键将分叉分到新窗格 | `claude-code` `codex` `shell` | 3 | 2026-07-24 |
| [**herdr-copy-search**](https://github.com/qq88976321/herdr-copy-search)<br><sub>qq88976321</sub> | 面向 herdr 回滚缓冲区的正则表达式和 copycat 模式搜索，配合 extrakto 令牌提取，落地到 tmux 风格的复制模式（OSC 52） | `copy-mode` `rust` `terminal` `tmux` | 3 | 2026-08-04 |
| [**scoopr**](https://github.com/TawfiqAbubaker/scoopr)<br><sub>TawfiqAbubaker</sub> | 无需使用鼠标即可将任意内容复制到终端的 Herdr 插件，灵感来自 tmux 的 extrakto。 | `rust` | 3 | 2026-09-06 |
| [**herdr-link-browser**](https://github.com/bonkey/herdr-link-browser)<br><sub>bonkey</sub> | Herdr 插件：按住 Ctrl 点击 http(s) 链接，即可在窗格旁以分屏方式用 terminal-browser 打开。 | `terminal-browser` `shell` | 2 | 2026-09-07 |
| [**herdr-s3-clipboard**](https://github.com/jagzmz/herdr-s3-clipboard)<br><sub>jagzmz</sub> | 使用 S3 兼容存储，将 Herdr 中剪贴板的图片发布为可复用的公开链接或预签名链接 | `aws-s3` `clipboard` `cloudflare-r2` `developer-tools` `image-publishing` | 2 | 2026-07-16 |
| [**herdr-paste-image**](https://github.com/grooni/herdr-paste-image)<br><sub>grooni</sub> | 将剪贴板中的图片粘贴到 herdr 窗格（Codex、Gemini CLI）中——按 F8 粘贴，并配有 F9/F10 剪贴板清理工具。 | `shell` | 1 | 2026-09-21 |

<details><summary>与此目的也相关</summary>

- [nicosuave/memex](https://github.com/nicosuave/memex) — 搜索 Claude Code、Codex、Pi、OpenCode、GitHub Copilot 和 Cursor 的会话记录。恢复会话。追踪 token 使用
- [iurysza/termscope](https://github.com/iurysza/termscope) — 在分屏中打开终端屏幕上已经可见的文件和链接
- [pinkpixel-dev/quota](https://github.com/pinkpixel-dev/quota) — Desktop app, VSCode extension, CLI, and Herdr plugin for tracking AI usage across GitHub Copilot, Codex, Clau…
- [termaxa/termaxa](https://github.com/termaxa/termaxa) — Agent 的 prompt 会告诉你即将执行的命令，而 Termaxa 会告诉你其后果。提供预览、备份、策略与审计记录。支持 Claude Code、Codex、Cursor、Copilot。它是一块「挡风玻璃」，而…
- [jlimas/herdr-worktree-seed](https://github.com/jlimas/herdr-worktree-seed) — 为新工作树植入 copy-on-write 的 node_modules 和可配置本地 dotfiles 的 Herdr 插件
- [tanshio/herdr-worktreeinclude](https://github.com/tanshio/herdr-worktreeinclude) — Herdr 插件：将匹配 .worktreeinclude 的被 gitignore 文件复制到新创建的工作树中
- [khatriafaz/herdr-plugin-cow-worktree](https://github.com/khatriafaz/herdr-plugin-cow-worktree) — 一个 Herdr 插件，用于创建严格的写时复制（copy-on-write）Git worktree，并包含被 .gitignore 忽略的本地文件。
- [eightHundreds/herdr-worktreeinclude](https://github.com/eightHundreds/herdr-worktreeinclude) — Herdr 插件：将 .worktreeinclude 指定的被 gitignore 文件复制到新工作树中
- [mrolafsson/herdr-file-transfer](https://github.com/mrolafsson/herdr-file-transfer) — Running herdr on a VPS or remote box (Hetzner, a cloud dev server) and uploading files is a pain? Drop them o…
- [rheech22/herdr-comment-on-copy](https://github.com/rheech22/herdr-comment-on-copy) — Drag to select terminal text and open a comment popup automatically. Send feedback with context to AI agents…
- [crexi/herdr-worktree-copy](https://github.com/crexi/herdr-worktree-copy) — 根据 .worktree-copy 清单复制并符号链接工作树本地文件的 Herdr 插件
- [shadowfax92/herdr-comments](https://github.com/shadowfax92/herdr-comments) — 为复制的 Herdr 终端输出添加注释，按窗格收集评论，并可在 Neovim 中审查
- [zerodice0/herdr-plugin-worktree-bootstrap](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap) — 在新的 Herdr Git 工作树中安全地复制被忽略的本地文件并运行初始化命令
- [tupton/herdr-worktree-include](https://github.com/tupton/herdr-worktree-include) — 将未跟踪的文件以符号链接或复制的方式引入 herdr 创建的 git worktree。

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-meta"></a>

## 插件管理与开发

> 想管理插件本身，或者自己动手做一个

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-plus**](https://github.com/cloudmanic/herdr-plus)<br><sub>cloudmanic</sub> | herdr 的扩展，作为原生插件构建——一组让 herdr 更好用的工具集：项目管理和快捷操作 | `go` | 366 | 2026-09-04 |
| [**herdr-plugin-manager**](https://github.com/speardragon/herdr-plugin-manager)<br><sub>speardragon</sub> | 在弹窗中管理 herdr 插件——安装、更新、启用/禁用、卸载，并浏览 herdr-plugin 市场。推荐快捷键：prefix+p | `plugin-manager` `tui` `shell` | 79 | 🔄 2026-10-19 |
| [**herdr-lazy**](https://github.com/natori-hrj/herdr-lazy)<br><sub>natori-hrj</sub> | 面向 Herdr 的声明式、可复现插件管理器与精选套件——一份清单、一个锁定文件，以及一个安全的管理窗格。 | `cli` `lockfile` `plugin-manager` `rust` `terminal` | 27 | 🔄 2026-10-14 |
| [**house-of-herdr**](https://github.com/alasano/house-of-herdr)<br><sub>alasano</sub> | Herdr 插件合集——包含 Codex Micro：在 Work Louder Codex Micro 上显示 Agent 状态灯并提供操作控制 | `codex-micro` `work-louder` `typescript` | 8 | 2026-08-13 |
| [**herdr-plugin-manager**](https://github.com/vika2603/herdr-plugin-manager)<br><sub>vika2603</sub> | 通过弹窗或命令行浏览、安装和更新 herdr 插件。 | `go` `tui` | 5 | 🔄 2026-10-19 |
| [**herdr-plugin-rust**](https://github.com/Newt6611/herdr-plugin-rust)<br><sub>Newt6611</sub> | 用于构建 Herdr 插件的 Rust 应用框架 | `rust` | 3 | 2026-07-09 |
| [**herdr-plugins-labs**](https://github.com/hmu332233/herdr-plugins-labs)<br><sub>hmu332233</sub> | Herdr 的实验性插件——在这里孵化，成熟后独立成自己的仓库 | `labs` `javascript` | 2 | 2026-09-23 |

[⬆ 返回目的列表](#purposes)

<a id="cat-other"></a>

## 其他与实用工具

> 不属于以上任何分类，但很实用的东西

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**terminal-browser**](https://github.com/zenbu-labs/terminal-browser)<br><sub>zenbu-labs</sub> | A real browser inside your terminal | `browser` `claude-code` `claude-code-plugin` `claude-skills` `cli` | 4259 | 🔄 2026-10-26 |
| [**herdr-lantern**](https://github.com/aigorahub/herdr-lantern)<br><sub>aigorahub</sub> | Lantern，来自 Elves。一个 Herdr 插件：羊群正在田野中——Lantern 会照亮谁需要你、以及他们正朝着什么目标努力 | `python` | 70 | 🔄 2026-10-22 |
| [**herdr-gui**](https://github.com/undivisible/herdr-gui)<br><sub>undivisible</sub> | 为 herdr 打造的 GUI 界面及更多功能，基于 crepuscular gpui 构建。 | `crepuscularity` `gpui` `rust` | 22 | 2026-07-27 |
| [**herdr-openspec**](https://github.com/FlorisKr/herdr-openspec)<br><sub>FlorisKr</sub> | Openspec plugin for herdr | `python` | 19 | 2026-10-07 |
| [**herdr-commandcode-plugin**](https://github.com/TheMetalStorm/herdr-commandcode-plugin)<br><sub>TheMetalStorm</sub> | 将 Commandcode 集成到 Herdr 中 | `cli` `commandcode` `herdr-integration` `shell` | 13 | 2026-07-30 |
| [**herdr-plugins-directory**](https://github.com/MIDO-ruby7/herdr-plugins-directory)<br><sub>MIDO-ruby7</sub> | 按你想完成的事情来查找 herdr 插件的链接集合 | `python` | 12 | 🔄 2026-10-26 |
| [**herdr-plugin-cmux**](https://github.com/lachieh/herdr-plugin-cmux)<br><sub>lachieh</sub> | 将每个由 herdr 管理的 Agent 镜像到 cmux 侧边栏中各自独立的一行——带状态徽标和可点击跳转的任务行 | `javascript` | 11 | 2026-07-01 |
| [**neon-herdr**](https://github.com/neon-solutions/neon-herdr)<br><sub>neon-solutions</sub> | Neon 官方的 Herdr 插件 | `typescript` | 11 | 2026-08-06 |
| [**herdr-freebuff-plugin**](https://github.com/TheMetalStorm/herdr-freebuff-plugin)<br><sub>TheMetalStorm</sub> | Herdr 的 Freebuff 生命周期集成插件——通过文件轮询和 PTY 内容抓取来报告闲置/工作中/被阻塞状态 | `cli` `freebuff` `herdr-integration` `shell` | 8 | 2026-07-22 |
| [**wave-tui**](https://github.com/takemo101/wave-tui)<br><sub>takemo101</sub> | 适合工作时段的安静终端电台 | `rust` | 5 | 2026-07-20 |
| [**mu-herdr**](https://github.com/AndresMpa/mu-herdr)<br><sub>AndresMpa</sub> | 专为搭配 MμVim 使用而设计的 herdr 配置。 | `herdr-integration` `muvim` `shell` | 4 | 2026-09-28 |
| [**shipframe**](https://github.com/juanitourquiza/shipframe)<br><sub>juanitourquiza</sub> | 面向「规划、验证、发布」团队的 AI 编码工作流。 | `ai` `ai-coding` `ai-tools` `claude` `claude-code` | 4 | 🔄 2026-10-24 |
| [**broadmand**](https://github.com/francjpd/broadmand)<br><sub>francjpd</sub> | Broadcast commands with ease | `shell` | 3 | 2026-10-10 |
| [**herdr-plugins**](https://github.com/JacobAtchley/herdr-plugins)<br><sub>JacobAtchley</sub> | My custom herdr plugins | `command-line-tool` `utility` `rust` | 3 | 2026-10-07 |
| [**herdr-memory**](https://github.com/jatingargiitk/herdr-memory)<br><sub>jatingargiitk</sub> | 从你的编程会话中构建「活的大脑」的 Herdr 插件——逐步学习哪些做法有效、哪些失败了，以及你做出的决定 | `shell` | 3 | 2026-08-11 |
| [**hrd**](https://github.com/joshuadavidthomas/hrd)<br><sub>joshuadavidthomas</sub> | 管理你的沙盒集群及运行在其上的 Herdr 会话 | `go` | 3 | 🔄 2026-10-23 |
| [**herdr-sprites-plugin**](https://github.com/superfly/herdr-sprites-plugin)<br><sub>superfly</sub> | Fly.io Sprites 的官方 Herdr 插件。 | `sandboxes` `sprites` `javascript` | 3 | 2026-09-09 |
| [**herdr-codespaces**](https://github.com/alexjyong/herdr-codespaces)<br><sub>alexjyong</sub> | Plugin to add codespace support to heder | `shell` | 2 | 2026-09-28 |
| [**🆕 devnull-tui**](https://github.com/arhen/devnull-tui)<br><sub>arhen</sub> | Unofficial terminal UI for /dev/null (dev-null.sh) — the feed, threads and inbox in any terminal, or as a Herdr pane | `cli` `dev-null` `devnull` `terminal` `tui` | 2 | 🔄 2026-10-23 |
| [**herdr-rails**](https://github.com/codergeek121/herdr-rails)<br><sub>codergeek121</sub> | Herdr 与 Rails 的集成。 | `ai` `rails` `shell` | 2 | 2026-09-22 |
| [**herdr-undo-close**](https://github.com/federbenjamin/herdr-undo-close)<br><sub>federbenjamin</sub> | Reopen the pane you just closed in Herdr: same split, same scrollback, Claude Code conversation included | `claude-code` `scrollback` `shell` `terminal` `undo` | 2 | 2026-10-09 |
| [**herdrctx**](https://github.com/j0urneyk/herdrctx)<br><sub>j0urneyk</sub> | 用于管理本地 Herdr 会话的终端 UI。 | `go` | 2 | 🔄 2026-10-20 |
| [**herdr-standup**](https://github.com/neospeed83/herdr-standup)<br><sub>neospeed83</sub> | 根据 Git 活动和 Herdr 上下文，生成有据可查的每日站会摘要 | `developer-tools` `standup` `rust` | 2 | 2026-08-31 |
| [**herdr-handsfree**](https://github.com/RanolP/herdr-handsfree)<br><sub>RanolP</sub> | 免提操作的 herdr 插件——提供基于 whisper.cpp 的语音听写和面向 macOS 的摄像头视线鼠标 | `rust` | 2 | 2026-07-30 |
| [**pixtui**](https://github.com/RizRiyz/pixtui)<br><sub>RizRiyz</sub> | 在终端中运行的像素画编辑器 | `bohay-module` `editor` `luvus-module` `pixel-art` `termina` | 2 | 2026-08-07 |
| [**herdr-shadow-pane**](https://github.com/shaozk/herdr-shadow-pane)<br><sub>shaozk</sub> | Herdr 插件「Shadow Clone Panel」——可同时操控多个面板。 | `rust` `vibe-coding` | 2 | 2026-09-14 |
| [**herdr-suite-site**](https://github.com/StructuPath/herdr-suite-site)<br><sub>StructuPath</sub> | StructuPath Herdr Suite 的官网首页——herdr.structupath.ai | `herdr-integration` `javascript` | 2 | 2026-10-05 |
| [**herdr-stt**](https://github.com/xtwist/herdr-stt)<br><sub>xtwist</sub> | 面向 Herdr 的语音转文字功能。 | `rust` | 2 | 2026-09-18 |
| [**herdr-zen**](https://github.com/y4m3/herdr-zen)<br><sub>y4m3</sub> | 为 Herdr 提供带可调居中窗格宽度的禅模式 | `rust` `terminal` `zen-mode` | 2 | 2026-08-19 |
| [**harbr**](https://github.com/dev-town/harbr)<br><sub>dev-town</sub> | Harbour TUI | `typescript` | 1 | 2026-10-10 |
| [**herdr-desk**](https://github.com/duyet/herdr-desk)<br><sub>duyet</sub> | 用于无人值守仓库维护的 Herdr 插件。 | `typescript` | 1 | 🔄 2026-10-25 |
| [**herdr-rainfrog**](https://github.com/fraction12/herdr-rainfrog)<br><sub>fraction12</sub> | 在受管理的 HerdR 窗格中打开 Rainfrog | `shell` | 1 | 2026-08-15 |
| [**herdr-browser**](https://github.com/redsquiggle/herdr-browser)<br><sub>redsquiggle</sub> | 让 Chromium 标签组与 Herdr 工作区保持一致 | `chromium` `ratatui` `rust` | 1 | 2026-07-28 |
| [**herdr-pdf**](https://github.com/tim80411/herdr-pdf)<br><sub>tim80411</sub> | 面向 herdr 的 PDF 查看器插件：通过 pane.graphics 流式 API 将页面渲染到分屏窗格中。 | `go` `pdf` `terminal` | 1 | 2026-09-17 |
| [**herdr-plugin-k8s-context**](https://github.com/tkuchiki/herdr-plugin-k8s-context)<br><sub>tkuchiki</sub> | 以隔离的 Kubernetes context 和 namespace 打开 Herdr 标签页 | `go` | 1 | 2026-08-15 |
| [**multitrunk-herdr-plugin**](https://github.com/yoyoyeti/multitrunk-herdr-plugin)<br><sub>yoyoyeti</sub> | 面向 multitrunk 任务工作区的 Herdr 插件 | `git` `multitrunk` `rust` | 1 | 2026-08-31 |
| [**🆕 herdr-todos**](https://github.com/limonequantistico/herdr-todos)<br><sub>limonequantistico</sub> | Simple todo lists from a TODOS.md file, in a herdr side panel: drag to reorder, click to tick. | `rust` | 0 | 🔄 2026-10-20 |

[⬆ 返回目的列表](#purposes)

## 使用方法

```sh
# 直接使用表格中某一行的 owner/repo
herdr plugin install ogulcancelik/herdr-plugin-github-start
herdr plugin list
```

位于子目录中的插件使用 `owner/repo/subdir` 的形式。详情参见 [Plugins](https://herdr.dev/docs/plugins/) 和 [Marketplace](https://herdr.dev/docs/marketplace/)。

## 想要修正时

如果分类不对、想加标签、或想加一句备注，请在 [`data/overrides.json`](data/overrides.json) 中添加条目并提交 PR。

```json
{
  "owner/repo": {
    "category": "notify",
    "add_tags": ["macos"],
    "note": "安装时需要配置 ntfy 的 topic"
  }
}
```

分类键： `notify`, `remote`, `agents`, `worktree`, `review`, `forge`, `layout`, `navigate`, `files`, `cost`, `monitor`, `finder`, `automation`, `session`, `naming`, `text`, `meta`, `other`

对于 GitHub 上没有描述的仓库，可以用 `description` 键覆盖（用英文；ja/zh 页面的译文请添加到 `data/translations.json`）。

收录是全自动的——只要仓库打上 GitHub 话题标签 `herdr-plugin` 就会自动出现在此列表中（无需在这里申请）。

---

*README.zh.md 和 `data/plugins.json` 由 [`scripts/build.py`](scripts/build.py) 自动生成，请勿直接编辑。*
