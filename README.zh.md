# herdr plugins by purpose

[🇯🇵 日本語](README.md) · [🇺🇸 English](README.en.md) · 🇨🇳 中文

**一个按照「你想做什么」来查找 [herdr](https://herdr.dev/) 插件的链接合集。**

- 收录 **994** 个插件 / 最后更新 **2026-09-07 04:40 UTC**（每 6 小时自动刷新）
- 数据来源：打了 GitHub 话题标签 [`herdr-plugin`](https://github.com/topics/herdr-plugin) 的仓库——与官方市场 [herdr.dev/plugins](https://herdr.dev/plugins/) 的数据来源相同
- 分类是根据仓库描述和话题标签自动推断的。如果分类不准确，可以通过 PR 修改 [`data/overrides.json`](data/overrides.json)
- 安装：`herdr plugin install owner/repo` —— [官方文档](https://herdr.dev/docs/plugins/)

> [!WARNING]
> 这是自动采集的索引，不是经过审核的目录。插件是直接在你的电脑上运行的代码，安装前请检查其 manifest 和会执行的命令。

<a id="purposes"></a>

## 按目的浏览

- [**🆕 最近新增**](#cat-new) (116) — 最近 7 天内加入本列表的插件。
- [**通知与提醒**](#cat-notify) (40) — 即使离开座位，也想知道 Agent 何时完成或卡在等待输入
- [**手机与远程操控**](#cat-remote) (46) — 想在外出或用手机时监控 Agent，只需回传批准即可
- [**Agent 编排与并行执行**](#cat-agents) (135) — 想统一启动、分工并管理多个 AI Agent
- [**git 工作树与分支管理**](#cat-worktree) (50) — 想为每项工作单独开一个工作树，收尾清理也自动完成
- [**代码审查与差异对比**](#cat-review) (38) — 想阅读 Agent 写的差异并对其发表评论
- [**GitHub / issue 跟踪工具集成**](#cat-forge) (35) — 想以 issue 或 PR 为起点开始工作，并追踪 PR 状态
- [**工作区与布局搭建**](#cat-layout) (36) — 打开项目时，希望标签页、窗格和启动命令一次性就位
- [**窗格导航与快捷键**](#cat-navigate) (114) — 想用和编辑器一样的快捷键在窗格、工作区之间移动和调整大小
- [**文件浏览与编辑器联动**](#cat-files) (59) — 想在窗格中打开文件树，或与编辑器的状态保持一致
- [**Token 与费用管理**](#cat-cost) (29) — 想看看 Agent 花费了多少，并想削减用量
- [**监控与仪表盘**](#cat-monitor) (76) — 想一目览尽 Agent 和机器的状态
- [**搜索与模糊查找器**](#cat-finder) (91) — 只记得大概名字也想调出命令或项目
- [**自动化、钩子与定时任务**](#cat-automation) (52) — 想在创建工作树或指定时机自动运行固定的操作步骤
- [**会话保存与恢复**](#cat-session) (36) — 关闭工作后，希望之后能从同一状态继续
- [**标题、命名与外观**](#cat-naming) (60) — 想让标签页名称和终端标题自动变得清晰易懂，或想改变外观
- [**文本与 URL 提取**](#cat-text) (26) — 想不用鼠标就抓取屏幕上显示的字符串、路径或 URL
- [**插件管理与开发**](#cat-meta) (9) — 想管理插件本身，或者自己动手做一个
- [**其他与实用工具**](#cat-other) (62) — 不属于以上任何分类，但很实用的东西

<a id="cat-new"></a>

## 🆕 最近新增

> 最近 7 天内加入本列表的插件。

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**🆕 pairfob**](https://github.com/arronKler/pairfob)<br><sub>arronKler</sub> | The phone surface for Herdr. Codex, Claude, and Grok keep running on your computer; the phone opens those same live sessions. Pair once. The computer dials out… | `herdr-mobile` `typescript` | 21 | 2026-09-05 |
| [**🆕 herdr-pr-watch**](https://github.com/maxguzenski/herdr-pr-watch)<br><sub>maxguzenski</sub> | Herdr plugin: GitHub PR status of each workspace and agent pane in the sidebar | `github-pull-requests` `python` | 1 | 2026-09-06 |
| [**🆕 herdr-pane-autorename**](https://github.com/b12o/herdr-pane-autorename)<br><sub>b12o</sub> | Herdr plugin that autorenames panes with the name of the current running process. | `shell` | 0 | 2026-09-07 |
| [**🆕 herdr-namesync**](https://github.com/oddurs/herdr-namesync)<br><sub>oddurs</sub> | Keeps herdr workspace, tab and agent names in step with the work as it changes — and holds off when it shouldn't. Works with no model; can use one when you wan… | `claude-code` `cli` `developer-tools` `terminal` `javascript` | 0 | 2026-09-07 |
| [**🆕 herdr-plugin-shortcut-shepherd**](https://github.com/Roshvan/herdr-plugin-shortcut-shepherd)<br><sub>Roshvan</sub> | Shortcut insights and gentle coaching for Herdr. | `typescript` | 0 | 2026-09-07 |
| [**🆕 herdr-park-agents**](https://github.com/rrg/herdr-park-agents)<br><sub>rrg</sub> | Park a coding-agent pane in herdr: stop the process, close the pane, and resume the session later from a workspace panel. | `agent-tools` `python` | 0 | 2026-09-07 |
| [**🆕 herdr-mem-cpu-load**](https://github.com/thewtex/herdr-mem-cpu-load)<br><sub>thewtex</sub> | CPU, memory, and load average monitor for herdr. | `rust` | 0 | 2026-09-07 |
| [**🆕 herdr-flash-picker**](https://github.com/TinyWhite1997/herdr-flash-picker)<br><sub>TinyWhite1997</sub> | Fast pane picker for Herdr with aligned one- or two-letter jump labels | `rust` `tui` | 2 | 2026-09-06 |
| [**🆕 herdr-remote**](https://github.com/dibin666/herdr-remote)<br><sub>dibin666</sub> | Remote browser access to your Herdr terminal workspaces | `typescript` | 1 | 2026-09-06 |
| [**🆕 scoopr**](https://github.com/TawfiqAbubaker/scoopr)<br><sub>TawfiqAbubaker</sub> | Herdr plugin for copying anything to the terminal without using the mouse, inspired by extrakto for tmux. | `rust` | 1 | 2026-09-06 |
| [**🆕 herdr-gotify**](https://github.com/8liang/herdr-gotify)<br><sub>8liang</sub> | _(暂无描述)_ | `gotify` `notifications` `python` | 0 | 2026-09-07 |
| [**🆕 deepseek-counter-herdr**](https://github.com/alkevintan/deepseek-counter-herdr)<br><sub>alkevintan</sub> | DeepSeek API credit in the herdr statusline — top-up spent, balance left, and today's pace toward a level month. | `python` | 0 | 2026-09-06 |
| [**🆕 herdr-stay-awake**](https://github.com/assawalhy/herdr-stay-awake)<br><sub>assawalhy</sub> | Keeps the machine from sleeping while any herdr agent pane is working (Linux, macOS, Windows, and WSL) | `agent-orchestration` `agents` `harness` `linux` `macos` | 0 | 2026-09-06 |
| [**🆕 herdr-dup-tab**](https://github.com/bonkey/herdr-dup-tab)<br><sub>bonkey</sub> | Herdr plugin: duplicate the focused pane's running command into a new tab | `shell` | 0 | 2026-09-06 |
| [**🆕 herdr-wt-purpose**](https://github.com/bonkey/herdr-wt-purpose)<br><sub>bonkey</sub> | Herdr plugin: worktree from a purpose or ticket URL, branch named by Apple's on-device model, scaffolded in the background | `apple-intelligence` `git-worktree` `shell` | 0 | 2026-09-06 |
| [**🆕 herdr-flight-radar**](https://github.com/corygforsythe/herdr-flight-radar)<br><sub>corygforsythe</sub> | Herdr plugin: real-time ADS-B flight radar TUI backed by dump1090 | `python` | 0 | 2026-09-05 |
| [**🆕 herdr-awst**](https://github.com/kedwards/herdr-awst)<br><sub>kedwards</sub> | AWST integration with herdr | `shell` | 0 | 2026-09-06 |
| [**🆕 herdr-telegram-notify**](https://github.com/naturalmoods/herdr-telegram-notify)<br><sub>naturalmoods</sub> | Herdr plugin: Telegram notification when an agent finishes or gets blocked — with the session title, project, duration, token use and the agent's last message. | `claude-code` `notifications` `telegram` `javascript` | 0 | 2026-09-06 |
| [**🆕 omarchy-crook**](https://github.com/parker-brown-family/omarchy-crook)<br><sub>parker-brown-family</sub> | Crook — which coding agent needs you, on the Omarchy bar. One icon that goes urgent the moment something is waiting on you, and a tray that says who. | `agents` `bar-widget` `claude-code` `hyprland` `omarchy` | 1 | 2026-09-06 |
| [**🆕 herdr-web-dashboard**](https://github.com/spad-0x/herdr-web-dashboard)<br><sub>spad-0x</sub> | A high-performance, mobile-first PWA dashboard with a Cyber-Dark design for orchestrating Herdr and autonomous AI agents directly from your smartphone. Feature… | `html` | 1 | 2026-09-05 |
| [**🆕 quota-deck**](https://github.com/ArtMoreno/quota-deck)<br><sub>ArtMoreno</sub> | quota-deck: credential-scoped AI quota and context for Herdr on Windows, macOS, and Linux | `rust` | 0 | 2026-09-06 |
| [**🆕 herdr-autoreload**](https://github.com/Austinsuyoyo/herdr-autoreload)<br><sub>Austinsuyoyo</sub> | Reload herdr's config.toml the moment you save it, and toast the diagnostics when an edit is rejected | `rust` | 0 | 2026-09-05 |
| [**🆕 herdr-project-filter**](https://github.com/bshearrer/herdr-project-filter)<br><sub>bshearrer</sub> | Scope herdr's Agents sidebar to one git repository at a time. | `javascript` | 0 | 2026-09-05 |
| [**🆕 ai-share-usage-herdr**](https://github.com/DongHyunnn/ai-share-usage-herdr)<br><sub>DongHyunnn</sub> | herdr plugin for AI Share Usage: shared Codex quota tracking in the herdr terminal | `javascript` | 0 | 2026-09-06 |
| [**🆕 herdr-plugin-pane-id-namer**](https://github.com/gcgo/herdr-plugin-pane-id-namer)<br><sub>gcgo</sub> | Automatically generate an agent name and display it in the terminal. | `shell` | 0 | 2026-09-05 |
| [**🆕 pane-identity**](https://github.com/Ghost-LZW/pane-identity)<br><sub>Ghost-LZW</sub> | Display pane IDs, hostnames, and labels in Herdr without modifying your agents. | `python` `terminal` | 0 | 2026-09-05 |
| [**🆕 herdr-wrangler**](https://github.com/jone/herdr-wrangler)<br><sub>jone</sub> | tmux-style pane layouts and rotation for herdr | `python` | 0 | 2026-09-05 |
| [**🆕 herdr-glab-status**](https://github.com/jpwallace22/herdr-glab-status)<br><sub>jpwallace22</sub> | A [Herdr](https://herdr.dev) plugin that shows each workspace's GitLab merge request status in the spaces sidebar, as a $mr token on the workspace row: | `typescript` | 0 | 2026-09-05 |
| [**🆕 herdr-tokenlens**](https://github.com/KeithMoc/herdr-tokenlens)<br><sub>KeithMoc</sub> | Live carrying-cost and compact-breakeven meter for AI coding agents, as a herdr pane | `ai-agents` `claude-code` `llm-cost` `tui` `python` | 0 | 2026-09-04 |
| [**🆕 herdr-focus-attention**](https://github.com/kuwa72/herdr-focus-attention)<br><sub>kuwa72</sub> | Herdr plugin: cycle through agents needing attention | `python` | 0 | 2026-09-05 |
| [**🆕 herdr-sleep-inhibit**](https://github.com/moosingin3space/herdr-sleep-inhibit)<br><sub>moosingin3space</sub> | _(暂无描述)_ | `rust` | 0 | 2026-09-05 |
| [**🆕 herdr-kaku-bell**](https://github.com/Rockheung/herdr-kaku-bell)<br><sub>Rockheung</sub> | 에이전트가 손을 기다릴 때 kaku 탭에 점을 켠다 — herdr plugin | `kaku` `terminal` `python` | 0 | 2026-09-06 |
| [**🆕 herdr-restore-notice**](https://github.com/victor-software-house/herdr-restore-notice)<br><sub>victor-software-house</sub> | Compact Herdr restore notices with click-to-resume agent sessions | `typescript` | 0 | 2026-09-05 |
| [**🆕 herdr-hop**](https://github.com/youguanxinqing/herdr-hop)<br><sub>youguanxinqing</sub> | Jump to any visible Herdr pane by pressing a labeled key | `rust` | 0 | 2026-09-05 |
| [**🆕 herdr-harbor**](https://github.com/zlj-zz/herdr-harbor)<br><sub>zlj-zz</sub> | _(暂无描述)_ | `rust` | 0 | 2026-09-05 |
| [**🆕 ttt**](https://github.com/eugenioenko/ttt)<br><sub>eugenioenko</sub> | TTT Editor (Terminal Text Tool): A real alternative to VS Code, Zed, and Sublime that runs in your terminal. A TUI that feels like GUI. Single binary, zero con… | `cli` `code-editor` `developer-tools` `diff` `editor` | 238 | 2026-09-05 |
| [**🆕 herdr-wish**](https://github.com/MovieHolic-Plex/herdr-wish)<br><sub>MovieHolic-Plex</sub> | Herdr plugin. Make a wish and omo commits a PR. omo-10 opens 10 worktrees. | `omo` `wish` `javascript` | 2 | 2026-09-04 |
| [**🆕 herdr-emoji-time**](https://github.com/hotnugs/herdr-emoji-time)<br><sub>hotnugs</sub> | Emoji for your Herdr spaces, agents and tabs. Inject some fun into your terminal | `emoji` `terminal` `tui` `python` | 1 | 2026-09-04 |
| [**🆕 herdr-mobile**](https://github.com/martebytes/herdr-mobile)<br><sub>martebytes</sub> | Mobile-first web UI for Herdr: see your agents, attach to panes, chat with Claude Code and Codex from your phone | `claude-code` `codex` `pwa` `python` | 1 | 2026-09-04 |
| [**🆕 herdr-worktree-include**](https://github.com/tupton/herdr-worktree-include)<br><sub>tupton</sub> | Symlink or copy untracked files to git worktrees created by herdr. | `shell` | 1 | 2026-09-06 |
| [**🆕 herdr-muse**](https://github.com/akshat12/herdr-muse)<br><sub>akshat12</sub> | Herdr integration for Muse Code: idle/working/blocked pane state via lifecycle hooks (no Herdr fork needed) | `ai-agents` `cli` `coding-agents` `muse-code` `terminal` | 0 | 2026-09-04 |
| [**🆕 herdr-tabline**](https://github.com/btj93/herdr-tabline)<br><sub>btj93</sub> | Render Herdr tab labels with safe templates and project-aware profiles. | `golang` `tabline` `terminal` `tui` `go` | 0 | 2026-09-04 |
| [**🆕 herdr-tokens**](https://github.com/btj93/herdr-tokens)<br><sub>btj93</sub> | Publishes workspace metadata tokens derived from agent status, so sidebar colours can vary by state. | `golang` `terminal` `tui` `go` | 0 | 2026-09-04 |
| [**🆕 bindr**](https://github.com/itsmistermoon/bindr)<br><sub>itsmistermoon</sub> | Herdr plugin for switching between named keybinding profiles and viewing/editing keybinds in a popup. | `rust` | 0 | 2026-09-04 |
| [**🆕 shahi**](https://github.com/iYassr/shahi)<br><sub>iYassr</sub> | Read agent conversations, answer permission prompts, and manage herdr sessions from your phone or browser. | `ai-agents` `claude-code` `codex` `expo` `react-native` | 0 | 2026-09-05 |
| [**🆕 herdr-plugin-github-status**](https://github.com/jwanga/herdr-plugin-github-status)<br><sub>jwanga</sub> | herdr plugin: a real-time GitHub project status pane (milestones, issues, PRs, Actions) docked on the right at sidebar width | `github` `rust` `tui` | 0 | 2026-09-04 |
| [**🆕 herdr-pomodoro**](https://github.com/michmos/herdr-pomodoro)<br><sub>michmos</sub> | Pomodoro inside herdr's status bar | `focus` `pomodoro` `pomodoro-timer` `python` | 0 | 2026-09-04 |
| [**🆕 herdr-auto-warm-cache**](https://github.com/parker-brown-family/herdr-auto-warm-cache)<br><sub>parker-brown-family</sub> | A herdr plugin that keeps an idle agent's prompt cache warm before the one-hour TTL expires — 20x cheaper than letting it lapse. Asks before it types, and neve… | `claude-code` `prompt-caching` `shell` | 0 | 2026-09-04 |
| [**🆕 herdr-plugin-agent-attention**](https://github.com/peterwiebe/herdr-plugin-agent-attention)<br><sub>peterwiebe</sub> | Herdr plugin to jump to the most recent blocked or finished agent | `python` | 0 | 2026-09-04 |
| [**🆕 herdr-numbered-tabs**](https://github.com/RickyMarou/herdr-numbered-tabs)<br><sub>RickyMarou</sub> | Herdr plugin: prefix every tab label with its current displayed position/shortcut number | `python` | 0 | 2026-09-04 |
| [**🆕 herdr-launcher**](https://github.com/Tatendaz/herdr-launcher)<br><sub>Tatendaz</sub> | Unofficial macOS Dock launcher for the herdr TUI: click the ram, get herdr in your terminal | `applescript` `developer-tools` `dock` `launcher` `macos` | 0 | 2026-09-04 |
| [**🆕 herdr-grazr**](https://github.com/wazum/herdr-grazr)<br><sub>wazum</sub> | A simple and reliable auto account switcher for Claude Code: rotates to a fresh account before the 5-hour or weekly rate limit hits, so no pane ever stops at t… | `account-rotation` `account-switcher` `account-switching` `anthropic` `claude` | 0 | 2026-09-06 |
| [**🆕 herdr-plugin-pane-move**](https://github.com/yuloop/herdr-plugin-pane-move)<br><sub>yuloop</sub> | Herdr插件:快捷键搬窗格 | `shell` | 0 | 2026-09-04 |
| [**🆕 herdr-plugin-win-terminal**](https://github.com/yuloop/herdr-plugin-win-terminal)<br><sub>yuloop</sub> | Herdr插件:一键安装Windows Terminal配置 | `powershell` | 0 | 2026-09-04 |
| [**🆕 herdr-studio**](https://github.com/powerfooI/herdr-studio)<br><sub>powerfooI</sub> | Herdr 的 Web 客户端，专为移动端体验打磨——提供浏览器终端、工作区与 worktree 管理、文件与差异查看器，以及 AI Agent 会话查看功能。 | `ai-agents` `dogfooding` `git-worktree` `herdr-client` `mobile-friendly` | 38 | 2026-09-06 |
| [**🆕 herdr-telegram-agents**](https://github.com/permgps/herdr-telegram-agents)<br><sub>permgps</sub> | 像在终端里一样，从 Telegram 操控你的编码 Agent。每个 Agent 对应一个话题，话题图标实时显示状态，并通过带内联按钮的双向聊天进行选择。 | `claude-code` `coding-agents` `go` `telegram` `telegram-bot` | 11 | 2026-09-07 |
| [**🆕 herdr-agent-titler**](https://github.com/killerz3/herdr-agent-titler)<br><sub>killerz3</sub> | 无需外部 API key，使用本地的 agy、claude、codex 或 opencode 运行环境，自动为 Herdr 标签页设置标题。 | `antigravity` `claude-code` `python` | 3 | 2026-09-03 |
| [**🆕 herdr-palette**](https://github.com/Binb1/herdr-palette)<br><sub>Binb1</sub> | Herdr 的命令面板。可跳转到工作区和 Agent，运行插件动作，也可执行 Herdr 命令。 | `go` | 2 | 2026-09-03 |
| [**🆕 herdr-shadow-pane**](https://github.com/shaozk/herdr-shadow-pane)<br><sub>shaozk</sub> | Herdr 插件「Shadow Clone Panel」——可同时操控多个面板。 | `rust` `vibe-coding` | 2 | 2026-09-06 |
| [**🆕 herdr-workspace-prs**](https://github.com/andrewbrannan/herdr-workspace-prs)<br><sub>andrewbrannan</sub> | 用于追踪工作区 GitHub 拉取请求的 Herdr 插件。 | `typescript` | 1 | 2026-09-04 |
| [**🆕 Vincent**](https://github.com/chasereyn/Vincent)<br><sub>chasereyn</sub> | 一款以鼠标操作为主的终端客户端，用于审查 AI Agent 编写的代码，并可就地修改。 | `go` | 1 | 2026-09-03 |
| [**🆕 tsk**](https://github.com/chrisg32/tsk)<br><sub>chrisg32</sub> | tsk——一个 TaskPaper/PlainTasks 风格的纯文本任务管理 TUI，使用 Rust 编写。既可独立运行，也可作为 herdr 插件使用。 | `rust` `taskpaper` `todo` `tui` | 1 | 2026-09-03 |
| [**🆕 herdr-open-editor**](https://github.com/jimididit/herdr-open-editor)<br><sub>jimididit</sub> | 用 fzf 模糊搜索并选择文件，然后在你配置的编辑器中打开。 | `herd` `text-editor` `tui` `shell` | 1 | 2026-09-03 |
| [**🆕 herdr-achievements**](https://github.com/SerHappy/herdr-achievements)<br><sub>SerHappy</sub> | 为你的 Herdr AI Agent 群体添加成就和小小的庆祝 | `achievements` `ai-agents` `developer-tools` `gamification` `go` | 1 | 2026-07-30 |
| [**🆕 herdr-plugin-echo**](https://github.com/andischerer/herdr-plugin-echo)<br><sub>andischerer</sub> | 将一个窗格中的按键广播到多个已标记窗格的 Herdr 插件 | `typescript` | 0 | 2026-08-23 |
| [**🆕 herdr-plugin-dotfiles-dev-layout**](https://github.com/edmundmiller/herdr-plugin-dotfiles-dev-layout)<br><sub>edmundmiller</sub> | 用于打开我的 dotfiles 开发工作区布局的 Herdr 插件 | `python` | 0 | 2026-06-23 |
| [**🆕 herdr-kitty-theme-sync**](https://github.com/enisbu/herdr-kitty-theme-sync)<br><sub>enisbu</sub> | 把 Herdr 当前使用的主题同步到 kitty 的 ANSI 调色板，使窗格内容与 Herdr 的外观保持一致。 | `kitty` `linux` `terminal` `theme` `shell` | 0 | 2026-09-03 |
| [**🆕 herdr-drover**](https://github.com/followbl/herdr-drover)<br><sub>followbl</sub> | Herdr 的「牧羊犬」标签页切换器：按住 Super+T 循环浏览标签页，松开即切换到当前标签页。 | `linux` `python` | 0 | 2026-09-03 |
| [**🆕 subherd**](https://github.com/HalloSouf/subherd)<br><sub>HalloSouf</sub> | 一个 herdr 插件，按会话所在的工作区分组，展示每个 Claude Code 子 Agent 正在做什么。 | `claude-code` `tui` `go` | 0 | 2026-09-05 |
| [**🆕 herdr-nnn**](https://github.com/linuxing3/herdr-nnn)<br><sub>linuxing3</sub> | 在 herdr 中打开 nnn | `shell` | 0 | 2026-08-04 |
| [**🆕 herdr-tab-title**](https://github.com/Newt6611/herdr-tab-title)<br><sub>Newt6611</sub> | Herdr Tab Title 会将 Herdr 标签页自动重命名为整洁的、按工作区独立编号的名称，如「1. Codex」「2. Terminal」，格式可自定义 | `rust` | 0 | 2026-07-09 |
| [**🆕 agentic-box**](https://github.com/nicoRomeroCuruchet/agentic-box)<br><sub>nicoRomeroCuruchet</sub> | 一个由 Claude Code 驱动本地模型 Agent 的隔离沙盒 | `agent-orchestration` `agentic` `agentic-workflow` `docker` `ornith-1-0-35b` | 0 | 2026-08-17 |
| [**🆕 herdr-guard**](https://github.com/pauljohnchamberlain/herdr-guard)<br><sub>pauljohnchamberlain</sub> | 让 Codex、Claude 等编码 Agent 能够安全地对 Herdr 进行外部控制。 | `coding-agents` `typescript` | 0 | 2026-09-04 |
| [**🆕 herdr-display-workspace**](https://github.com/RickyMarou/herdr-display-workspace)<br><sub>RickyMarou</sub> | Herdr 插件：在标签栏右侧显示当前工作区名称。 | `shell` | 0 | 2026-09-03 |
| [**🆕 herdr-worktree-include**](https://github.com/scoussens-nthplusio/herdr-worktree-include)<br><sub>scoussens-nthplusio</sub> | 使用仓库的 .worktreeinclude（与 Claude Code 使用的同一份文件、同一套规则），将 .env 等被 gitignore 忽略的文件复制到新的 Herdr 工作树中 | `dotenv` `git-worktree` `shell` | 0 | 2026-08-27 |
| [**🆕 herdr-plugins**](https://github.com/shubham-cpp/herdr-plugins)<br><sub>shubham-cpp</sub> | 用于标签页/Agent 命名以及方向键窗格聚焦的 Herdr 插件合集。 | `rust` | 0 | 2026-09-03 |
| [**🆕 herdr-copy-conversation**](https://github.com/testy-cool/herdr-copy-conversation)<br><sub>testy-cool</sub> | 在 Herdr 中，可将完整的终端回滚内容或与 Agent 的对话直接复制到剪贴板。 | `ai-agents` `claude-code` `clipboard` `codex` `developer-tools` | 0 | 2026-09-03 |
| [**🆕 herdr-focus**](https://github.com/trapple/herdr-focus)<br><sub>trapple</sub> | 聚焦下一个被阻塞/已完成的 Agent 窗格，并将终端应用置于前台。附带全局快捷键 | `shell` | 0 | 2026-07-19 |
| [**🆕 herdrctx**](https://github.com/j0urneyk/herdrctx)<br><sub>j0urneyk</sub> | 用于管理本地 Herdr 会话的终端 UI。 | `go` | 2 | 2026-09-05 |
| [**🆕 herdr-triggers**](https://github.com/cantona/herdr-triggers)<br><sub>cantona</sub> | 常驻监听窗格输出并按正则表达式触发动作：自动登录等由正则驱动的终端触发器。 | `rust` `terminal` | 1 | 2026-09-02 |
| [**🆕 herdr-swipe-linux**](https://github.com/enisbu/herdr-swipe-linux)<br><sub>enisbu</sub> | 面向 Linux 上 Herdr 的触控板手势：滑动可在窗格、标签页和空间之间切换，轻点即可跳转到等待中的 Agent。 | `evdev` `gestures` `gnome` `hyprland` `linux` | 1 | 2026-09-02 |
| [**🆕 herdr-pickers**](https://github.com/sagmans/herdr-pickers)<br><sub>sagmans</sub> | 为 Agent、worktree、工作区和项目提供多种自定义的弹出式选择器。 | `typescript` | 1 | 2026-09-04 |
| [**🆕 herdr-claude-lifecycle**](https://github.com/daocoding/herdr-claude-lifecycle)<br><sub>daocoding</sub> | 面向 herdr + Omarchy、以 hook 为核心的 Claude Code 生命周期管理：通过 Claude 自身的 hook 获取 working/blocked/idle 状态，并在每次 Claude Code 更新后进行验证。 | `claude-code` `omarchy` `python` | 0 | 2026-09-04 |
| [**🆕 herdr-oncall**](https://github.com/fulanto/herdr-oncall)<br><sub>fulanto</sub> | Herdr 插件：当 Agent 被阻塞时向 Telegram 发送通知。 | `javascript` | 0 | 2026-09-04 |
| [**🆕 herdr-pane-id-border**](https://github.com/Haichiu/herdr-pane-id-border)<br><sub>Haichiu</sub> | 一个极简的 Herdr 插件，在窗格边框上显示规范的窗格 ID。 | `shell` | 0 | 2026-09-02 |
| [**🆕 herdr-webhook**](https://github.com/jefflau/herdr-webhook)<br><sub>jefflau</sub> | Herdr 插件：将 Agent 的完成/阻塞事件通过 POST 发送到 Webhook。 | `python` | 0 | 2026-09-06 |
| [**🆕 herdr-checkpoint**](https://github.com/lancodev/herdr-checkpoint)<br><sub>lancodev</sub> | herdr 版的 tmux-resurrect——精确保存会话检查点并可还原，还原时会关闭不在检查点中的内容。 | `tmux-resurrect` `tui` `shell` | 0 | 2026-09-02 |
| [**🆕 herdr-plugin-project-finder**](https://github.com/mike-bronner/herdr-plugin-project-finder)<br><sub>mike-bronner</sub> | Herdr 插件：模糊搜索 git 仓库，并将其作为工作区打开。 | `python` | 0 | 2026-09-05 |
| [**🆕 herdr-plugin-recent-spaces**](https://github.com/mike-bronner/herdr-plugin-recent-spaces)<br><sub>mike-bronner</sub> | Herdr 插件：让空间侧边栏始终按最近使用顺序排列。 | `python` | 0 | 2026-09-02 |
| [**🆕 herdr-agent-links**](https://github.com/OmarDadabhoy/herdr-agent-links)<br><sub>OmarDadabhoy</sub> | 在 Herdr 中打开隐藏在 Codex 和 Claude 输出的 Markdown 标签背后的链接。 | `claude-code` `codex` `productivity` `terminal` `python` | 0 | 2026-09-02 |
| [**🆕 herdr-orca**](https://github.com/rudironsoni/herdr-orca)<br><sub>rudironsoni</sub> | 将标准 Orca 标签页附加到 Herdr 管理的终端上的 Herdr 插件。 | `typescript` | 0 | 2026-09-03 |
| [**🆕 hither**](https://github.com/T0mSIlver/hither)<br><sub>T0mSIlver</sub> | 在远程主机上的 herdr 窗格里按下组合键，Zed 就会在你的 Mac 上打开对应目录。 | `shell` | 0 | 2026-09-02 |
| [**🆕 herdr-hop**](https://github.com/utahta/herdr-hop)<br><sub>utahta</sub> | herdr 插件：通过一个弹窗即可跳转到仓库、worktree 或工作区。 | `git-worktree` `go` `terminal` `tui` | 0 | 2026-09-02 |
| [**🆕 herdr-git-dirty**](https://github.com/viko16/herdr-git-dirty)<br><sub>viko16</sub> | 一个轻量级 Herdr 插件，显示每个 Space 中未提交的 Git 文件数量。 | `git` `shell` | 0 | 2026-09-02 |
| [**🆕 herdr-tab-jump**](https://github.com/cyperx84/herdr-tab-jump)<br><sub>cyperx84</sub> | 通过任意快捷键，按位置聚焦到 herdr 的第 N 个标签页——可以把数字键分配给标签页和工作区。 | `shell` | 1 | 2026-09-01 |
| [**🆕 herdr-claude-usage**](https://github.com/anyaachan/herdr-claude-usage)<br><sub>anyaachan</sub> | 在 Herdr 中查看 Claude Code 套餐的全局用量：标签栏摘要 + 弹出式仪表盘，基于 statusLine 实现，支持多账号。 | `claude` `claude-code` `cli` `terminal` `shell` | 0 | 2026-09-01 |
| [**🆕 herdr-tab-command**](https://github.com/asermax/herdr-tab-command)<br><sub>asermax</sub> | 根据你给新标签页起的名字，自动启动 Agent 或运行相应命令。 | `typescript` | 0 | 2026-08-31 |
| [**🆕 herdr-agent-numbers**](https://github.com/DillonWall/herdr-agent-numbers)<br><sub>DillonWall</sub> | 为 herdr 的 Agent 面板编号，与 focus_agent（前缀+1..9）保持一致。 | `terminal-multiplexer` `shell` | 0 | 2026-09-01 |
| [**🆕 herdr-hitl**](https://github.com/huketo/herdr-hitl)<br><sub>huketo</sub> | 让 Herdr 的编码 Agent 在等待人工决策时暂停，并通过 Telegram 或 Discord 推送到你的手机。 | `agent-skill` `ai-agents` `cli` `discord-bot` `go` | 0 | 2026-09-06 |
| [**🆕 herdr-jump**](https://github.com/lancodev/herdr-jump)<br><sub>lancodev</sub> | 为 herdr 的工作区与 Agent 提供双窗格模糊搜索切换器，支持 vim 按键操作。 | `fzf` `tui` `shell` | 0 | 2026-09-01 |
| [**🆕 lasso**](https://github.com/skellleks/lasso)<br><sub>skellleks</sub> | herdr 的审查窗格：按 Agent 展示带语法高亮的差异，并可将行内评论发回给该 Agent。 | `ai-agents` `claude-code` `code-review` `git-diff` `ratatui` | 0 | 2026-08-31 |
| [**🆕 herdr-jump**](https://github.com/solidsnakedev/herdr-jump)<br><sub>solidsnakedev</sub> | 为 herdr 提供工作区、窗格与标签页的模糊搜索选择器，外加一个切换到上一个工作区的开关。 | `shell` | 0 | 2026-09-01 |
| [**🆕 herdr-pane-tools**](https://github.com/solidsnakedev/herdr-pane-tools)<br><sub>solidsnakedev</sub> | 为 herdr 提供感知 Vim 的窗格导航、aerospace 风格的窗格移动，以及 tmux 风格的窗格轮换。 | `shell` | 0 | 2026-09-01 |
| [**🆕 herdweb**](https://github.com/zlxlabs/herdweb)<br><sub>zlxlabs</sub> | 在手机上监控并操控你的编码 Agent。支持语音输入、粘贴图片、Webhook 通知，以及多设备/多服务器。 | `typescript` | 5 | 2026-09-06 |
| [**🆕 herdr-codex-bridge**](https://github.com/ardasevinc/herdr-codex-bridge)<br><sub>ardasevinc</sub> | 通过一个集中式的 app-server，为 Codex 会话赋予原生的 Herdr 窗格身份标识。 | `ai-agents` `codex` `terminal` `go` | 3 | 2026-09-05 |
| [**🆕 herdr-mission-control**](https://github.com/vjeantet/herdr-mission-control)<br><sub>vjeantet</sub> | herdr 的 Mission Control：按一个键，将工作区所有窗格按标签页分组，以实时平铺网格展示，选中即可切换过去。 | `expose` `mission-control` `terminal` `tui` `rust` | 3 | 2026-09-01 |
| [**🆕 herdr-pets**](https://github.com/abhishek944/herdr-pets)<br><sub>abhishek944</sub> | 以一个透明的桌面村庄，展示正在运行的 Herdr Agent。 | `typescript` | 2 | 2026-08-31 |
| [**🆕 herdr-mobile-app**](https://github.com/teasec4/herdr-mobile-app)<br><sub>teasec4</sub> | Native companion app + lightweight Go relay: stream live agent terminal output to your phone, check statuses, and send prompts — over LAN, Tailscale, or Funnel | `ai` `devtools` `flutter` `herdr-integration` `herdr-mobile` | 2 | 2026-09-05 |
| [**🆕 herdr-composer**](https://github.com/danieljvdm/herdr-composer)<br><sub>danieljvdm</sub> | 编排任务、附加上下文，并在隔离的 Herdr 工作区中启动编码 Agent。 | `coding-agents` `git-worktree` `rust` | 1 | 2026-09-01 |
| [**🆕 herdr-hyprland**](https://github.com/aorumbayev/herdr-hyprland)<br><sub>aorumbayev</sub> | 受 Hyprland 启发，为 herdr 带来的操作方式。 | `ai-agents` `developer-tools` `golang` `hyprland` `keybindings` | 0 | 2026-09-04 |
| [**🆕 herdr-sheep**](https://github.com/huketo/herdr-sheep)<br><sub>huketo</sub> | 把 Herdr 的编码 Agent 变成一群会动的 ASCII 羊，供你观赏。 | `ascii-art` `rust` `tui` | 0 | 2026-09-04 |
| [**🆕 herdr-tab-titles**](https://github.com/kewah/herdr-tab-titles)<br><sub>kewah</sub> | 根据发给编码 Agent 的第一条提示词，为窗格和标签页命名的 Herdr 插件。 | `javascript` | 0 | 2026-09-06 |
| [**🆕 precc-herdr-plugin**](https://github.com/peria-ai/precc-herdr-plugin)<br><sub>peria-ai</sub> | herdr 的 PRECC 插件：跨 Agent 统计 token 节省情况的遥测，并支持一键完成 PRECC 设置。 | `claude-code` `precc` `shell` | 0 | 2026-09-02 |
| [**🆕 provider-usage**](https://github.com/ryus1234/provider-usage)<br><sub>ryus1234</sub> | Herdr 的服务商用量与配额显示条。 | `ai-usage` `quota-monitor` `rust` | 0 | 2026-08-31 |
| [**🆕 herdr-tab-new**](https://github.com/softwarecrafts/herdr-tab-new)<br><sub>softwarecrafts</sub> | 在此项目的 herdr 工作区中恢复或启动一个 Agent 会话——既是 herdr 插件，也是可在 herdr 之外的终端使用的 CLI。 | `typescript` | 0 | 2026-08-31 |
| [**🆕 herdr-grid**](https://github.com/WillHeather/herdr-grid)<br><sub>WillHeather</sub> | 将 herdr 工作区里的 Agent 窗格平铺成铺满屏幕的网格，也可以还原回去。 | `python` | 0 | 2026-08-31 |

[⬆ 返回目的列表](#purposes)

<a id="cat-notify"></a>

## 通知与提醒

> 即使离开座位，也想知道 Agent 何时完成或卡在等待输入

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-focus-notify**](https://github.com/yankewei/herdr-focus-notify)<br><sub>yankewei</sub> | 面向 Herdr Agent 的可点击 macOS 通知。当 Agent 被阻塞或完成时发送原生提示通知；点击后将终端置于前台并聚焦到对应的 Herdr 窗格 | `alerter` `macos` `notifications` `productivity` `rust` | 20 | 2026-08-18 |
| [**herdr-pings**](https://github.com/joelhooks/herdr-pings)<br><sub>joelhooks</sub> | 面向 herdr 窗格中 AI Agent 的按轮次唤醒事件——pi 扩展、wait CLI、崩溃桥接，以及为你的 worker 起的 Discworld 风格代号 | `ai-agents` `pi` `typescript` | 9 | 2026-08-09 |
| [**herdr-terminal-notifier**](https://github.com/dot/herdr-terminal-notifier)<br><sub>dot</sub> | 通过 terminal-notifier 为 herdr Agent 状态变化发送可自定义的 macOS 通知 | `macos` `terminal-notifier` `shell` | 8 | 2026-07-14 |
| [**herdr-ntfy**](https://github.com/horn553/herdr-ntfy)<br><sub>horn553</sub> | 依赖极简（jq、curl、sh）——当 Herdr Agent 完成或被阻塞时发送 ntfy 通知 | `shell` | 7 | 2026-08-01 |
| [**herdr-ntfy-notify**](https://github.com/zom-2018/herdr-ntfy-notify)<br><sub>zom-2018</sub> | 面向 Herdr 终端 Agent 的实时 ntfy 推送通知 | `agent` `ntfy` `push-notifications` `tui` `javascript` | 7 | 2026-06-23 |
| [**herdr-hail**](https://github.com/natori-hrj/herdr-hail)<br><sub>natori-hrj</sub> | herdr 的 Slack 和 Discord 双向桥接——Agent 被阻塞时会收到提醒，回复或点击即可解除阻塞。无需内网穿透 | `discord` `slack` `typescript` | 6 | 2026-07-19 |
| [**herdr-telegram-plugin**](https://github.com/mvallebr/herdr-telegram-plugin)<br><sub>mvallebr</sub> | herdr 的 Telegram 机器人伴侣——通过 Telegram 论坛话题远程控制任意 Agent，整个流程中不涉及 LLM | `typescript` | 5 | 🔄 2026-08-31 |
| [**herdr-notify-windows**](https://github.com/aclima01/herdr-notify-windows)<br><sub>aclima01</sub> | 面向 herdr Agent 的 Windows 11 提示通知（轮次完成/需要输入） | `powershell` | 4 | 2026-07-23 |
| [**herdr-telegram-bridge**](https://github.com/cokekitten/herdr-telegram-bridge)<br><sub>cokekitten</sub> | 当 herdr Agent 完成或被阻塞时收到 Telegram 推送——直接回复即可将文本或文件发回该 Agent。无需服务器、无需内网穿透、无需 App | `ai-agents` `chatops` `claude-code` `developer-tools` `notifications` | 4 | 2026-08-06 |
| [**herdr-cache-alert**](https://github.com/AltanS/herdr-cache-alert)<br><sub>AltanS</sub> | herdr 插件：在每个 Agent 窗格显示 prompt 缓存倒计时，并附带每条缓存规则的来源和日期 | `ai-agents` `ai-coding` `ai-tools` `claude-code` `multiplexing` | 3 | 🔄 2026-09-01 |
| [**herdr-announcer**](https://github.com/nhclink16/herdr-announcer)<br><sub>nhclink16</sub> | Herdr 插件：Agent 完成或需要输入时，用语音播报一句 LLM 生成的摘要——支持本地 TTS、ElevenLabs 或任意自定义命令 | `tts` `python` | 3 | 2026-08-20 |
| [**herdr-discord-presence**](https://github.com/revanp/herdr-discord-presence)<br><sub>revanp</sub> | herdr 插件：将 Herdr 会话和 Agent 状态显示为 Discord Rich Presence | `typescript` | 3 | 2026-08-14 |
| [**herdr-agent-notify**](https://github.com/A1exthegreat/herdr-agent-notify)<br><sub>A1exthegreat</sub> | herdr 插件：当 Agent 完成工作、需要确认或进入空闲状态时发送桌面通知 | `javascript` | 2 | 2026-08-15 |
| [**buzzr**](https://github.com/candypoets/buzzr)<br><sub>candypoets</sub> | 将运行中的 Herdr space 和 Agent 镜像到 Buzz 频道，并支持 Nostr 身份和提及路由 | `agents` `buzz` `nostr` `rust` | 2 | 2026-08-14 |
| [**agent-webhook-notify**](https://github.com/happyeric77/agent-webhook-notify)<br><sub>happyeric77</sub> | 当 Herdr Agent 完成或被阻塞时，发送 Webhook 通知 | `javascript` | 2 | 2026-08-12 |
| [**herdr-guard**](https://github.com/StructuPath/herdr-guard)<br><sub>StructuPath</sub> | Herdr 的跨 Agent 命令策略：审计、警告并中断危险的 shell 命令 | `ai-agents` `command-policy` `security` `terminal` `javascript` | 2 | 🔄 2026-08-23 |
| [**herdr-wsl-notify**](https://github.com/tkmct/herdr-wsl-notify)<br><sub>tkmct</sub> | 当运行在 WSL2 上的 Agent（如 Claude Code）完成或被阻塞（等待批准/输入）时，显示 Windows 桌面提示通知的 Herdr 插件 | `javascript` | 2 | 🔄 2026-08-27 |
| [**herdr-telegram-notifications**](https://github.com/barnuri/herdr-telegram-notifications)<br><sub>barnuri</sub> | herdr 插件：当 Agent 进入空闲、被阻塞或完成时发送 Telegram 通知 | `telegram` `javascript` | 1 | 🔄 2026-09-01 |
| [**herdr-prayer-times**](https://github.com/bayoudhi/herdr-prayer-times)<br><sub>bayoudhi</sub> | 在 Herdr 侧边栏中显示下一次礼拜时间和倒计时，并附带时间表弹窗和通知 | `rust` | 1 | 2026-08-13 |
| [**session-sounds**](https://github.com/ChrisPachulski/session-sounds)<br><sub>ChrisPachulski</sub> | 面向 macOS 和 Linux 的 Herdr，为每个 Agent 提供不同的完成提示音和关注提示音 | `coding-agents` `notifications` `rust` | 1 | 2026-07-19 |
| [**herdr-telegram-slack-bridge**](https://github.com/lsisoft/herdr-telegram-slack-bridge)<br><sub>lsisoft</sub> | 面向 Herdr Agent 会话的 Telegram 与 Slack 机器人双向桥接——将被阻塞 Agent 的提醒和聊天回复路由回 Herdr 或 tmux 窗格 | `ai-agents` `slack-bot` `telegram-bot` `tmux` `python` | 1 | 2026-07-28 |
| [**herdr-notify-wsl**](https://github.com/saeedrahimi/herdr-notify-wsl)<br><sub>saeedrahimi</sub> | 为运行在 WSL 内的 herdr Agent 提供 Windows 11 提示通知——基于 aclima01/herdr-notify-windows | `powershell` | 1 | 2026-07-23 |
| [**🆕 herdr-gotify**](https://github.com/8liang/herdr-gotify)<br><sub>8liang</sub> | _(暂无描述)_ | `gotify` `notifications` `python` | 0 | 🔄 2026-09-07 |
| [**🆕 herdr-autoreload**](https://github.com/Austinsuyoyo/herdr-autoreload)<br><sub>Austinsuyoyo</sub> | Reload herdr's config.toml the moment you save it, and toast the diagnostics when an edit is rejected | `rust` | 0 | 🔄 2026-09-05 |
| [**herdr-telegram-notify**](https://github.com/elkraps/herdr-telegram-notify)<br><sub>elkraps</sub> | 针对 Herdr Agent 状态变化的可自定义 Telegram 通知——支持状态过滤、模板、多聊天投递、去重、Codex 批准按钮、完成摘要和内置诊断 | `ai-agents` `automation` `developer-tools` `javascript` `nodejs` | 0 | 🔄 2026-08-27 |
| [**🆕 herdr-oncall**](https://github.com/fulanto/herdr-oncall)<br><sub>fulanto</sub> | Herdr 插件：当 Agent 被阻塞时向 Telegram 发送通知。 | `javascript` | 0 | 🔄 2026-09-04 |
| [**herdr-random-sounds**](https://github.com/gridness/herdr-random-sounds)<br><sub>gridness</sub> | 在 macOS 版 herdr 中，根据 Agent 状态播放随机通知音 | `herdr-integration` `macos` `notification` `notifications` `python` | 0 | 🔄 2026-08-23 |
| [**🆕 herdr-hitl**](https://github.com/huketo/herdr-hitl)<br><sub>huketo</sub> | 让 Herdr 的编码 Agent 在等待人工决策时暂停，并通过 Telegram 或 Discord 推送到你的手机。 | `agent-skill` `ai-agents` `cli` `discord-bot` `go` | 0 | 🔄 2026-09-06 |
| [**🆕 herdr-webhook**](https://github.com/jefflau/herdr-webhook)<br><sub>jefflau</sub> | Herdr 插件：将 Agent 的完成/阻塞事件通过 POST 发送到 Webhook。 | `python` | 0 | 🔄 2026-09-06 |
| [**herdr-slack-notify**](https://github.com/juninaba/herdr-slack-notify)<br><sub>juninaba</sub> | 当 Herdr Agent 完成或被阻塞时发送 Slack 通知 | `javascript` | 0 | 2026-07-07 |
| [**drover-notify**](https://github.com/keinstn/drover-notify)<br><sub>keinstn</sub> | 在 Agent 被阻塞时发送 Drover 推送通知的 Herdr 插件 | `javascript` | 0 | 2026-08-01 |
| [**herdr-rich-notifications**](https://github.com/liamwh/herdr-rich-notifications)<br><sub>liamwh</sub> | 针对 herdr Agent 状态变化的丰富原生桌面通知——无需 LLM 的上下文增强、点击即可聚焦（herdr Agent 聚焦 + Niri 窗口定位）。fork 自 quinnjr/herdr-notifications | `notifications` `rust` | 0 | 🔄 2026-08-28 |
| [**herdr-pane-agent-unread**](https://github.com/NachoPal/herdr-pane-agent-unread)<br><sub>NachoPal</sub> | 面向 herdr 的按窗格「未读」提醒 + 侧边栏徽章——找出你未在查看的窗格中已完成或需要输入的 Agent（因为 herdr 是按标签页而非按窗格追踪「已读」状态的） | `python` | 0 | 🔄 2026-09-01 |
| [**🆕 herdr-telegram-notify**](https://github.com/naturalmoods/herdr-telegram-notify)<br><sub>naturalmoods</sub> | Herdr plugin: Telegram notification when an agent finishes or gets blocked — with the session title, project, duration, token use and the agent's last message. | `claude-code` `notifications` `telegram` `javascript` | 0 | 🔄 2026-09-06 |
| [**herdr-plugin-telegram-notify**](https://github.com/OiAnthony/herdr-plugin-telegram-notify)<br><sub>OiAnthony</sub> | 当 Agent 完成或被阻塞时发送 Telegram 通知的独立 Herdr 插件 | `javascript` | 0 | 2026-07-16 |
| [**herdr-apple-music-plugin**](https://github.com/perlporter/herdr-apple-music-plugin)<br><sub>perlporter</sub> | 当 Apple Music（macOS）正在播放的曲目变化时，在 herdr 中显示提示通知 | `shell` | 0 | 2026-07-28 |
| [**herdr-plugin-call-me**](https://github.com/radres/herdr-plugin-call-me)<br><sub>radres</sub> | 当 herdr Agent 被阻塞时，会拨打你真实的手机——用语音应答，你的回答就会变成 Agent 一直在等待的按键输入 | `ai-agents` `claude-code` `codex` `developer-tools` `notifications` | 0 | 🔄 2026-08-25 |
| [**herdr-notify-center**](https://github.com/ram4-dev/herdr-notify-center)<br><sub>ram4-dev</sub> | 为 Herdr 提供服务器范围的 Agent 通知，配有持久化的弹窗收件箱 | `notifications` `typescript` | 0 | 2026-08-14 |
| [**🆕 herdr-kaku-bell**](https://github.com/Rockheung/herdr-kaku-bell)<br><sub>Rockheung</sub> | 에이전트가 손을 기다릴 때 kaku 탭에 점을 켠다 — herdr plugin | `kaku` `terminal` `python` | 0 | 🔄 2026-09-06 |
| [**herdr-cc-mac-notify**](https://github.com/y-hirakaw/herdr-cc-mac-notify)<br><sub>y-hirakaw</sub> | 面向 Claude Code 的 macOS 通知——显示 Agent 真实的最后一条消息，而不只是「完成」 | `claude-code` `macos` `notifications` `python` | 0 | 2026-07-17 |

<details><summary>与此目的也相关</summary>

- [donghaolicd/herdr-teams-notify](https://github.com/donghaolicd/herdr-teams-notify) — 为 Microsoft Teams 提供带节流控制的 Agent 生命周期通知的 Herdr 插件

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-remote"></a>

## 手机与远程操控

> 想在外出或用手机时监控 Agent，只需回传批准即可

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**collie**](https://github.com/AltanS/collie)<br><sub>AltanS</sub> | 随时随地管理 herdr 的 PWA 应用。支持 Tailnet 访问、推送通知、快捷操作等 | `agent-orchestration` `ai` `ai-agents` `ai-coding` `ai-tools` | 823 | 🔄 2026-09-06 |
| [**herdr-remote**](https://github.com/dcolinmorgan/herdr-remote)<br><sub>dcolinmorgan</sub> | 从菜单栏、手机或 Telegram 监控并操控你的 herdr Agent。本地零配置，远程连接提供免费内网穿透，无需 Tailscale | `macos` `mobile` `python` | 325 | 🔄 2026-09-04 |
| [**herdr-mobile-relay**](https://github.com/0cv/herdr-mobile-relay)<br><sub>0cv</sub> | 通过手机远程审批和监控 Herdr Agent——面向 Android/iOS 的移动 Web 应用，支持推送通知、二维码配置和多电脑中继 | `android` `approvals` `cloudflare` `ios` `mobile` | 176 | 🔄 2026-09-06 |
| [**herdr-watch**](https://github.com/Unayung/herdr-watch)<br><sub>Unayung</sub> | 在 Apple Watch 上查看 herdr 的 Agent 状态 | `javascript` | 27 | 2026-08-14 |
| [**🆕 pairfob**](https://github.com/arronKler/pairfob)<br><sub>arronKler</sub> | The phone surface for Herdr. Codex, Claude, and Grok keep running on your computer; the phone opens those same live sessions. Pair once. The computer dials out… | `herdr-mobile` `typescript` | 21 | 🔄 2026-09-05 |
| [**herdr-connect**](https://github.com/Tomyail/herdr-connect)<br><sub>Tomyail</sub> | 通过这款 iPhone 移动伴侣应用监控并操控你的 Herdr AI 编码 Agent——查看输出、发送后续指令，并在任务完成时收到通知。通过局域网或 Tailscale 私密运行，无需云端，也无需账号。 | `agent` `mobile-app` `react-native` `typescript` | 13 | 🔄 2026-09-06 |
| [**herdr-plugin-mobile-relay**](https://github.com/benkraus/herdr-plugin-mobile-relay)<br><sub>benkraus</sub> | _(暂无描述)_ | `typescript` | 11 | 2026-08-12 |
| [**🆕 herdr-telegram-agents**](https://github.com/permgps/herdr-telegram-agents)<br><sub>permgps</sub> | 像在终端里一样，从 Telegram 操控你的编码 Agent。每个 Agent 对应一个话题，话题图标实时显示状态，并通过带内联按钮的双向聊天进行选择。 | `claude-code` `coding-agents` `go` `telegram` `telegram-bot` | 11 | 🔄 2026-09-07 |
| [**herdr-push**](https://github.com/dcolinmorgan/herdr-push)<br><sub>dcolinmorgan</sub> | herdr 插件：零依赖地将事件推送到 herdr-remote，用于手机端监控和一键批准 | `shell` | 10 | 2026-07-09 |
| [**herdr-web**](https://github.com/barnuri/herdr-web)<br><sub>barnuri</sub> | 面向 herdr 的移动优先 Web UI 插件——从手机驱动你的编程 Agent，并带有通知功能 | `pwa` `typescript` | 7 | 🔄 2026-09-01 |
| [**paddock**](https://github.com/lntvan166/paddock)<br><sub>lntvan166</sub> | 面向 herdr 的移动优先仪表盘——读取其 unix socket。无需任何配置即可在手机上运行 | `agent-orchestration` `coding-agents` `herdr-mobile` `paddock` `pwa` | 7 | 🔄 2026-09-03 |
| [**herdr-remote-panes**](https://github.com/Poor-Plebs/herdr-remote-panes)<br><sub>Poor-Plebs</sub> | 从一个 Herdr 操作其他机器——从菜单中选择一台机器，即可获得该机器上的终端。还可选启用实验性的双向镜像 | `golang` `ssh` `terminal` `go` | 7 | 🔄 2026-09-07 |
| [**herdr-web**](https://github.com/eyalev/herdr-web)<br><sub>eyalev</sub> | 面向 herdr Agent 多路复用器的移动优先 Web UI——从手机操控你的编程 Agent | `claude-code` `mobile` `pwa` `terminal` `javascript` | 6 | 2026-07-29 |
| [**merino**](https://github.com/LoneExile/merino)<br><sub>LoneExile</sub> | Merino 🐑——面向 Herdr Agent 的远程隧道仪表盘 | `go` `macos` `menubar` `react` `wails` | 6 | 🔄 2026-08-23 |
| [**muqun-gateway**](https://github.com/osuki-dev/muqun-gateway)<br><sub>osuki-dev</sub> | 让 Muqun 能够访问你自己电脑上终端的程序。它运行在你的机器上，与 tmux 或 Herdr 通信，并直接响应你的手机——中间没有账号，也没有我们的服务器 | `rust` | 6 | 🔄 2026-09-06 |
| [**herdr-call**](https://github.com/eliasstravik/herdr-call)<br><sub>eliasstravik</sub> | 面向 Herdr 的语音控制 | `elevenlabs` `tailscale` `voice` `typescript` | 5 | 2026-08-07 |
| [**herdr-tether**](https://github.com/moneycaringcoder/herdr-tether)<br><sub>moneycaringcoder</sub> | 即使关闭 Herdr 视图，也能让本地和远程的终端任务继续运行 | `remote-development` `rust` `ssh` `terminal` `tmux` | 5 | 🔄 2026-09-01 |
| [**🆕 herdweb**](https://github.com/zlxlabs/herdweb)<br><sub>zlxlabs</sub> | 在手机上监控并操控你的编码 Agent。支持语音输入、粘贴图片、Webhook 通知，以及多设备/多服务器。 | `typescript` | 5 | 🔄 2026-09-06 |
| [**herdr-portfwd**](https://github.com/miko-misa/herdr-portfwd)<br><sub>miko-misa</sub> | 面向远程机器上编程 Agent 的自动 SSH 端口转发——Ctrl+点击 Agent 打印的 localhost URL，即可在你本机以相同端口打开该页面。一个 Herdr 插件 | `ai-agents` `claude-code` `cli` `coding-agents` `developer-tools` | 4 | 🔄 2026-09-06 |
| [**vscode-devcontainers-herdr**](https://github.com/scott-the-programmer/vscode-devcontainers-herdr)<br><sub>scott-the-programmer</sub> | 面向运行在 dev container 内的 Agent 的 Herdr 中继 | `container` `devcontainer` `rust` | 4 | 🔄 2026-09-03 |
| [**herdr-whistle**](https://github.com/amurru/herdr-whistle)<br><sub>amurru</sub> | 用于远程管理 Agent 的 Herdr 插件 | `golang` `telegrambot` `go` | 3 | 2026-08-06 |
| [**herdr-mobile**](https://github.com/bsorescu/herdr-mobile)<br><sub>bsorescu</sub> | 通过 SSH 控制 Herdr 编程 Agent 的手机友好型 TUI | `mobile` `ssh` `textual` `tui` `python` | 3 | 🔄 2026-08-25 |
| [**herdr-aws-ssm**](https://github.com/maayanyosef/herdr-aws-ssm)<br><sub>maayanyosef</sub> | 在 herdr --remote 会话中选择一个 EC2 实例并通过 AWS SSM 连接——无需跳板机或公网 IP | `aws-ssm` `terminal` `shell` | 3 | 2026-07-01 |
| [**herdr-phone**](https://github.com/matheus3301/herdr-phone)<br><sub>matheus3301</sub> | 通过 Cloudflare Tunnel 和 Access 实现的 Herdr 移动端远程控制台 | `cloudflare-tunnel` `coding-agents` `developer-tools` `golang` `mobile` | 3 | 🔄 2026-09-04 |
| [**herdr-farm**](https://github.com/mejiasd3v/herdr-farm)<br><sub>mejiasd3v</sub> | Herdr 插件：将你的 Herdr 工作区和 Agent 可视化为牲畜的 3D 农场（three.js 网页应用） | `threejs` `javascript` | 3 | 2026-07-28 |
| [**herdr-devup**](https://github.com/alon-z/herdr-devup)<br><sub>alon-z</sub> | Herdr 插件：根据 .herdr/dev.toml 生成每个项目的开发布局，并同步隧道 URL 到环境变量 | `typescript` | 2 | 2026-06-22 |
| [**herdr-topbar**](https://github.com/bigbug16/herdr-topbar)<br><sub>bigbug16</sub> | 面向 herdr 的 macOS 菜单栏图标——可跳回会话、打开项目，并查看哪个 Agent 正在等待输入 | `macos` `menubar` `swift` | 2 | 🔄 2026-08-24 |
| [**herdr-go**](https://github.com/herdr-go/herdr-go)<br><sub>herdr-go</sub> | 从任何地方控制你的 herdr 编程 Agent——私密、点对点，并通过 EasyTier 加密保护 | `dart` | 2 | 🔄 2026-09-02 |
| [**herdr-telegram-gate**](https://github.com/hkdom/herdr-telegram-gate)<br><sub>hkdom</sub> | 面向 herdr AI Agent 群体的 Telegram 审批收件箱 + 按风险分级的自动批准——被阻塞的 Agent 会以带批准/拒绝按钮的 Telegram 卡片形式呈现（零依赖的 Node.js） | `approval-gate` `telegram` `javascript` | 2 | 2026-08-06 |
| [**herdr-remotedownloder**](https://github.com/kosuketut/herdr-remotedownloder)<br><sub>kosuketut</sub> | 将文件从远程 Herdr 窗格下载到已连接的 Mac | `rust` | 2 | 🔄 2026-08-24 |
| [**🆕 herdr-mobile-app**](https://github.com/teasec4/herdr-mobile-app)<br><sub>teasec4</sub> | Native companion app + lightweight Go relay: stream live agent terminal output to your phone, check statuses, and send prompts — over LAN, Tailscale, or Funnel | `ai` `devtools` `flutter` `herdr-integration` `herdr-mobile` | 2 | 🔄 2026-09-05 |
| [**herdr-web-tui**](https://github.com/tigorlazuardi/herdr-web-tui)<br><sub>tigorlazuardi</sub> | 以守护进程为核心的 Herdr 浏览器/PWA 前端，附带可选的插件启动器 | `go` | 2 | 🔄 2026-08-29 |
| [**herdr-hub**](https://github.com/alex-devdone/herdr-hub)<br><sub>alex-devdone</sub> | 将由远程连接窗格组成的 herdr 会话描述为可移植的清单文件，并可在任意机器上重建 | `python` | 1 | 🔄 2026-08-23 |
| [**herdrchat**](https://github.com/cobanov/herdrchat)<br><sub>cobanov</sub> | 在手机（iOS 和 Android）上操控你的 herdr 编码 Agent。 | `herdr-client` `herdr-integration` `herdr-mobile` `typescript` | 1 | 🔄 2026-08-27 |
| [**🆕 herdr-remote**](https://github.com/dibin666/herdr-remote)<br><sub>dibin666</sub> | Remote browser access to your Herdr terminal workspaces | `typescript` | 1 | 🔄 2026-09-06 |
| [**herdr-tunnel**](https://github.com/ivorpad/herdr-tunnel)<br><sub>ivorpad</sub> | herdr 插件：将本地端口暴露到公网，复制其 URL，并可随时撤下 | `tui` `python` | 1 | 🔄 2026-08-27 |
| [**🆕 herdr-mobile**](https://github.com/martebytes/herdr-mobile)<br><sub>martebytes</sub> | Mobile-first web UI for Herdr: see your agents, attach to panes, chat with Claude Code and Codex from your phone | `claude-code` `codex` `pwa` `python` | 1 | 🔄 2026-09-04 |
| [**herdview**](https://github.com/Orchard-Robotics/herdview)<br><sub>Orchard-Robotics</sub> | 从网页查看你的「herd」 | `html` | 1 | 2026-07-17 |
| [**🆕 herdr-web-dashboard**](https://github.com/spad-0x/herdr-web-dashboard)<br><sub>spad-0x</sub> | A high-performance, mobile-first PWA dashboard with a Cyber-Dark design for orchestrating Herdr and autonomous AI agents directly from your smartphone. Feature… | `html` | 1 | 🔄 2026-09-05 |
| [**setnet**](https://github.com/chano-gpt/setnet)<br><sub>chano-gpt</sub> | 从手机管理多种 harness 的编程 Agent——一个 Herdr 插件 | `typescript` | 0 | 🔄 2026-08-29 |
| [**herdr-slack**](https://github.com/egemenyildiz/herdr-slack)<br><sub>egemenyildiz</sub> | 从 Slack 驱动你本地的 herdr Agent——在手机上浏览、发送提示词并启动 Agent，无需内网穿透 | `slack` `typescript` | 0 | 🔄 2026-09-03 |
| [**🆕 shahi**](https://github.com/iYassr/shahi)<br><sub>iYassr</sub> | Read agent conversations, answer permission prompts, and manage herdr sessions from your phone or browser. | `ai-agents` `claude-code` `codex` `expo` `react-native` | 0 | 🔄 2026-09-05 |
| [**herdr-approval-gate**](https://github.com/Javamomma/herdr-approval-gate)<br><sub>Javamomma</sub> | herdr 中针对 Agent 操作的人工签核关卡——在专用窗格中运行任务，对其记录进行核验，直到有人输入 「APPROVE <姓名缩写>」 才会解除阻塞 | `shell` | 0 | 2026-07-15 |
| [**herdr-wechat-plugin**](https://github.com/LuYanFCP/herdr-wechat-plugin)<br><sub>LuYanFCP</sub> | 用于微信远程控制的 Herdr 插件 | `rust` | 0 | 2026-07-17 |
| [**herdr-agents-bridge**](https://github.com/maedana/herdr-agents-bridge)<br><sub>maedana</sub> | 通过本地移动端友好 Web UI，从手机监控并操作编程 Agent——扫描二维码即可连接 | `rust` | 0 | 2026-07-22 |
| [**🆕 hither**](https://github.com/T0mSIlver/hither)<br><sub>T0mSIlver</sub> | 在远程主机上的 herdr 窗格里按下组合键，Zed 就会在你的 Mac 上打开对应目录。 | `shell` | 0 | 🔄 2026-09-02 |

<details><summary>与此目的也相关</summary>

- [powerfooI/herdr-studio](https://github.com/powerfooI/herdr-studio) — Herdr 的 Web 客户端，专为移动端体验打磨——提供浏览器终端、工作区与 worktree 管理、文件与差异查看器，以及 AI Agent 会话查看功能。
- [huketo/herdr-hitl](https://github.com/huketo/herdr-hitl) — 让 Herdr 的编码 Agent 在等待人工决策时暂停，并通过 Telegram 或 Discord 推送到你的手机。
- [radres/herdr-plugin-call-me](https://github.com/radres/herdr-plugin-call-me) — 当 herdr Agent 被阻塞时，会拨打你真实的手机——用语音应答，你的回答就会变成 Agent 一直在等待的按键输入

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-agents"></a>

## Agent 编排与并行执行

> 想统一启动、分工并管理多个 AI Agent

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**oh-my-opencode-slim**](https://github.com/alvinunreal/oh-my-opencode-slim)<br><sub>alvinunreal</sub> | 精简且经过调优的 Opencode 多 Agent 套件 · 可混用任意模型 · 自动委派任务 | `agentic-ai` `antigravity` `cerebras` `oh-my-opencode` `opencode` | 8671 | 🔄 2026-09-04 |
| [**agentbox**](https://github.com/madarco/agentbox)<br><sub>madarco</sub> | 一条命令即可在沙盒虚拟机中并行运行多个 Agent（本地或云端） | `claude` `claude-code` `cli` `cmux` `codex` | 387 | 🔄 2026-09-06 |
| [**pi-workflows**](https://github.com/osolmaz/pi-workflows)<br><sub>osolmaz</sub> | 面向 pi 编程 Agent 的工作流引擎、JSON 控制流工具与实时终端查看器 | `typescript` | 265 | 🔄 2026-09-07 |
| [**pi-extensible-workflows**](https://github.com/vekexasia/pi-extensible-workflows)<br><sub>vekexasia</sub> | 面向 Pi 的确定性多 Agent 工作流编排 | `pi` `workflow` `workflows` `typescript` | 205 | 🔄 2026-09-06 |
| [**herdr-board**](https://github.com/nelsonPires5/herdr-board)<br><sub>nelsonPires5</sub> | herdr 的看板工具——卡片就是提示词，会被派发给可见窗格中的 AI Agent | `board` `kanban` `kanban-board` `tui` `rust` | 96 | 🔄 2026-08-23 |
| [**herdr-dagr**](https://github.com/aemrebarut/herdr-dagr)<br><sub>aemrebarut</sub> | 将 Agent 集群实时呈现为 DAG——在 herdr 分屏窗格中展示包含尝试记录、评审关卡和证据的编排图 | `agents` `dag` `multi-agent` `orchestration` `rust` | 63 | 🔄 2026-08-23 |
| [**herdr-file-annotator**](https://github.com/JonasBaeumer/herdr-file-annotator)<br><sub>JonasBaeumer</sub> | 在不脱离实际代码库的前提下，最大化 Agent 化开发效率的 herdr 插件 | `rust` | 52 | 🔄 2026-09-04 |
| [**agentbox-herdr-plugin**](https://github.com/madarco/agentbox-herdr-plugin)<br><sub>madarco</sub> | 一条命令即可在沙盒虚拟机中并行运行多个 Agent（本地或云端） | `claude-code` `codex-cli` `opencode` `sandbox` `shell` | 30 | 2026-06-24 |
| [**herdmates**](https://github.com/caioniehues/herdmates)<br><sub>caioniehues</sub> | herdr 原生的 Claude Code Agent 团队——teammux 兼容层、任务控制面板、聚焦窗格 | `agent-teams` `claude-code` `rust` `tui` | 24 | 2026-08-21 |
| [**pi-herd**](https://github.com/ribbons-digital/pi-herd)<br><sub>ribbons-digital</sub> | 结合 Herdr 窗格和 git 工作树，对 Pi 会话进行可视化编排 | `typescript` | 18 | 2026-07-06 |
| [**herdr-agent-handoff**](https://github.com/sanirudh17/herdr-agent-handoff)<br><sub>sanirudh17</sub> | 将进行中的 Agent 会话交接给另一个已安装编程 Agent 的新会话的 Herdr 插件——完整会话直接放入提示词中传递，无需摘要、无需截断记录、无需再写后续提示 | `agent-handoff` `claude-code` `codex` `coding-agents` `developer-tools` | 16 | 🔄 2026-09-05 |
| [**PromptPilot**](https://github.com/ivanarama/PromptPilot)<br><sub>ivanarama</sub> | 面向 Claude Code 及其他 AI CLI 的后台任务队列——配有网页 UI 和 Telegram 机器人 | `ai-agents` `claude-code` `telegram-bot` `python` | 14 | 🔄 2026-09-04 |
| [**herdr-vercel-sandbox-plugin**](https://github.com/vercel-labs/herdr-vercel-sandbox-plugin)<br><sub>vercel-labs</sub> | 从 Herdr 在隔离的 Vercel Sandbox 中运行基于终端的编程 Agent | `javascript` | 13 | 2026-08-09 |
| [**herdr-social-glass**](https://github.com/ythx-101/herdr-social-glass)<br><sub>ythx-101</sub> | 面向 macOS 版 Herdr 的、适合截图分享的 Social Glass 主题与工作流插件 | `macos` `multi-agent` `terminal-theme` `shell` | 12 | 2026-08-21 |
| [**herdr-browser**](https://github.com/StructuPath/herdr-browser)<br><sub>StructuPath</sub> | Herdr 的可操控 Agent 浏览器窗格——支持实时流传输、真实交互、自适应渲染、控制台/页面错误显示、录制和 localhost 路由 | `terminal` `javascript` | 11 | 🔄 2026-08-23 |
| [**vibetty**](https://github.com/second-state/vibetty)<br><sub>second-state</sub> | 通过 MQTT 将 AI Agent 终端实时共享给智能硬件（vibekeys、vibewatch 等），也可作为 Herdr 插件使用 | `claude-code` `codex` `vibecoding` `rust` | 10 | 2026-08-17 |
| [**agys**](https://github.com/quaywin/agys)<br><sub>quaywin</sub> | 通过零污染沙盒，为 Herdr 中的 Antigravity CLI 提供轻松的多配置文件隔离和实时配额追踪 | `ai-agents` `antigravity` `cli` `context-window` `developer-tools` | 9 | 🔄 2026-09-07 |
| [**herdr-helpr**](https://github.com/sohanemon/herdr-helpr)<br><sub>sohanemon</sub> | 面向 herdr 的、由提示词驱动的工作区和窗格管理 | `ai-agents` `bun` `cli` `developer-tools` `ink` | 8 | 2026-07-16 |
| [**herdr-catchup**](https://github.com/wilbeibi/herdr-catchup)<br><sub>wilbeibi</sub> | herdr 的跨 Agent 编程会话交接：从正在运行的窗格中，对 Claude Code、Codex、Cursor、Cline 或 OpenCode 会话进行摘要、分叉，或转交给另一个 Agent | `ai-agents` `claude-code` `codex` `coding-agents` `context-handoff` | 8 | 🔄 2026-09-07 |
| [**herdr-world**](https://github.com/IvoryHeart/herdr-world)<br><sub>IvoryHeart</sub> | Herdr World——面向 Herdr 的多界面网页体验 | `multi-agent` `observability` `pixel-art` `react` `rust` | 7 | 🔄 2026-09-06 |
| [**herdr-agent-messenger**](https://github.com/aashishd/herdr-agent-messenger)<br><sub>aashishd</sub> | 让运行中的 Herdr 窗格间的 AI Agent 互相发送简明、自成一体的消息——一个 Agent 可以在不共享完整上下文的情况下与另一个协调工作 | `python` | 6 | 2026-08-02 |
| [**herdr-scuttlebutt**](https://github.com/andybarilla/herdr-scuttlebutt)<br><sub>andybarilla</sub> | 为 herdr 会话中的 Agent 提供共享聊天室的 herdr 插件 | `rust` | 6 | 🔄 2026-08-31 |
| [**pier**](https://github.com/July24/pier)<br><sub>July24</sub> | Pi 是编程 Agent 的载体，Herdr 是终端工作区管理器。pier 补上了 pi 刻意省略的两项能力——todo 列表循环和可交互的子 Agent——并将 herdr 的窗格/标签页层作为它们的视觉与交互基础 | `pi-coding-agent` `typescript` | 6 | 🔄 2026-09-04 |
| [**herdr-triage**](https://github.com/natori-hrj/herdr-triage)<br><sub>natori-hrj</sub> | herdr 的关注度分级——按谁最需要你来排序 Agent；长时间被阻塞的 Agent 会排到最前面 | `ai-agents` `triage` `rust` | 6 | 2026-07-23 |
| [**herdr-space-scoped-agents**](https://github.com/ShankyJS/herdr-space-scoped-agents)<br><sub>ShankyJS</sub> | 将 Agent 面板范围限定为当前聚焦空间的 herdr 插件 | `coding-agents` `terminal` `go` | 6 | 2026-07-23 |
| [**herdr-swarm**](https://github.com/StructuPath/herdr-swarm)<br><sub>StructuPath</sub> | 在同一仓库上安全并行运行多个编程 Agent：为每个 Agent 分配独立工作树，实时可见变更，Herdr 上以审查优先的方式收获成果 | `terminal` `javascript` | 6 | 🔄 2026-08-24 |
| [**herdr-orchestrate**](https://github.com/darjss/herdr-orchestrate)<br><sub>darjss</sub> | 为可见的 Herdr worker 会话提供 Pi 原生编排——运行看板、持久化的提示词/报告/状态、独立的 git 工作树，以及明确的模型路由 | `pi-package` `typescript` | 5 | 2026-07-13 |
| [**herdr-gamepad**](https://github.com/htlin222/herdr-gamepad)<br><sub>htlin222</sub> | 用游戏手柄操控 Herdr。窝在沙发上巡视你的 AI Agent、拆分窗格、切换工作区——任意手柄，60 秒内自定义按键映射 | `ai-agents` `gamepad` `macos` `swift` `terminal-multiplexer` | 5 | 2026-08-08 |
| [**herdr-fleet**](https://github.com/Northern-Lighthouse/herdr-fleet)<br><sub>Northern-Lighthouse</sub> | 通过 Tailscale 管理一批 herdr 机器——仪表盘插件、自动发现、感知容量的 Agent 派发、无盘工作区 | `ai-agents` `tailscale` `python` | 5 | 2026-08-14 |
| [**herdr-insight**](https://github.com/0x5c0f/herdr-insight)<br><sub>0x5c0f</sub> | Agent 状态时间线面板 | `rust` | 4 | 2026-06-23 |
| [**shepherdr**](https://github.com/afogel/shepherdr)<br><sub>afogel</sub> | 将委派出去的编程 Agent 收拢到可见、可审查的 herdr 窗格中，供你观察、恢复和接管的 herdr 插件 | `ai-agents` `claude-code` `codex` `cursor` `rust` | 4 | 2026-07-24 |
| [**herdr-devcontainer**](https://github.com/gambtho/herdr-devcontainer)<br><sub>gambtho</sub> | 通过官方 Dev Containers CLI，在仓库的 Dev Container 内打开 shell 和编程 Agent 的 Herdr 插件 | `coding-agents` `containers` `devcontainers` `developer-tools` `development-environment` | 4 | 2026-08-13 |
| [**herdr-espresso**](https://github.com/Hanyang-Li/herdr-espresso)<br><sub>Hanyang-Li</sub> | 在 Agent 运行时，即使合上盖子也保持 MacBook 唤醒状态 | `rust` | 4 | 2026-07-25 |
| [**herdr-worker-orchestrator**](https://github.com/anhnd3005-infinity/herdr-worker-orchestrator)<br><sub>anhnd3005-infinity</sub> | 通过 Herdr 管理的窗格，将任务派发给 CLI Agent worker（agy、codex 等）——支持有状态的任务追踪、工作树隔离和基于差异的评审。同时适用于 Claude Code 和 Herdr 的双用插件 | `html` | 3 | 🔄 2026-08-25 |
| [**herdr-theos-settler**](https://github.com/calebcauthon/herdr-theos-settler)<br><sub>calebcauthon</sub> | 将已完成的 Herdr Agent 标签页和工作区沉到活跃工作下方，让它们不再挡路。Theo 的点子 | `rust` | 3 | 2026-07-23 |
| [**herdr-a2a**](https://github.com/IsaiasZc/herdr-a2a)<br><sub>IsaiasZc</sub> | 通过 A2A 为 Herdr 提供的可靠 Agent 间委派层 | `typescript` | 3 | 🔄 2026-08-27 |
| [**herdr-walkietalkie**](https://github.com/jeffory/herdr-walkietalkie)<br><sub>jeffory</sub> | herdr 插件：token 高效的跨 Agent 委派（wt）——编排 Agent 在标签页或工作树中派生出 Claude/OpenCode/Antigravity 的 worker | `shell` | 3 | 2026-08-12 |
| [**herdr-prompt-library**](https://github.com/jwkicklighter/herdr-prompt-library)<br><sub>jwkicklighter</sub> | 用于浏览、管理并将可复用的本地或全局 Markdown 提示词插入到聚焦窗格中的 Herdr 插件 | `go` `golang` `prompting` `snippets` `tui` | 3 | 🔄 2026-09-01 |
| [**chatter**](https://github.com/marcvermeeren/chatter)<br><sub>marcvermeeren</sub> | Chatter 是一次跨 harness 的 Agent 协作实验——为在 Herdr 中处理同一 Git 仓库的多个 Agent 提供共享群聊和上下文层 | `agent-collaboration` `agentic-ai` `agentic-workflow` `ai-agents` `group-chat` | 3 | 2026-08-18 |
| [**herdr-agent-office**](https://github.com/suisya-systems/herdr-agent-office)<br><sub>suisya-systems</sub> | 将你的 Agent 团队呈现为像素风办公室的 herdr 插件。查看谁在工作、谁卡住了，并可直接跳转过去 | `python` | 3 | 2026-07-25 |
| [**herdr-blaxel-sandbox-plugin**](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin)<br><sub>blaxel-ai</sub> | 从 Herdr 在持久化的 Blaxel Sandbox 中运行编程 Agent | `blaxel` `claude-code` `codex` `coding-agents` `opencode` | 2 | 🔄 2026-09-03 |
| [**herdr-birdseye**](https://github.com/calebcauthon/herdr-birdseye)<br><sub>calebcauthon</sub> | 以鸟瞰视角查看 herdr 中的 Agent | `rust` | 2 | 2026-07-24 |
| [**herdr-loop**](https://github.com/cyperx84/herdr-loop)<br><sub>cyperx84</sub> | 面向 herdr 的声明式、事件驱动的循环与图编排——同时运行 Claude Code、Codex、opencode 和 pi，直到工作收敛 | `ai-agents` `golang` `orchestration` `go` | 2 | 2026-08-12 |
| [**herdr-pane-topic-sync**](https://github.com/danbuhler/herdr-pane-topic-sync)<br><sub>danbuhler</sub> | herdr 插件：将窗格和标签页自动命名为每个 Agent（Claude Code、Codex 等）实时的主题，而不是「1」「2」「3」 | `ai-agents` `claude-code` `terminal` `tmux-alternative` `javascript` | 2 | 🔄 2026-09-02 |
| [**herdr-openclaw**](https://github.com/gejiliang/herdr-openclaw)<br><sub>gejiliang</sub> | herdr 插件：将 OpenClaw 的 TUI 窗格作为一等公民的 herdr Agent 来管理 | `openclaw` `terminal` `javascript` | 2 | 2026-08-13 |
| [**herdr-amphetamine-macos**](https://github.com/gw31415/herdr-amphetamine-macos)<br><sub>gw31415</sub> | 在 Agent 工作期间持续为 Amphetamine 续时的 herdr 插件 | `python` | 2 | 2026-07-09 |
| [**herdr-newtab-plus**](https://github.com/jeffarese/herdr-newtab-plus)<br><sub>jeffarese</sub> | 会询问文件夹和 Agent 的 Herdr 新标签页：自动补全真实路径，记住你常用的工作目录，并为你启动 Agent | `python` | 2 | 2026-07-26 |
| [**herdr-shame-report**](https://github.com/JYasha11/herdr-shame-report)<br><sub>JYasha11</sub> | 永久记录你让 AI Agent 等了多久的账本。羊会记住的 | `javascript` | 2 | 2026-07-10 |
| [**herdr-orchestrator**](https://github.com/kylezk777/herdr-orchestrator)<br><sub>kylezk777</sub> | Herdr-orch 是运行在 Herdr 之上的基于文件的 Agent 编排工具 | `agent-orchestration` `orchestrator` `rust` | 2 | 2026-07-26 |
| [**herdr-agents-status**](https://github.com/maedana/herdr-agents-status)<br><sub>maedana</sub> | 显示 Herdr Agent 状态的常驻置顶透明浮层——claudeye 的精神续作，专为 Herdr（而非 tmux）打造 | `rust` | 2 | 2026-08-15 |
| [**herdr-agent-profiles**](https://github.com/mikeyobrien/herdr-agent-profiles)<br><sub>mikeyobrien</sub> | 面向 Herdr 的数据驱动型 CLI harness 与模型配置文件 | `ai-agents` `terminal` `python` | 2 | 2026-08-10 |
| [**herdr-redact**](https://github.com/moneycaringcoder/herdr-redact)<br><sub>moneycaringcoder</sub> | 当 Agent 窗格打印出凭据时向你发出警告——在你截图、直播或粘贴到聊天窗口之前提醒你 | `rust` `secret-detection` `security` `terminal` | 2 | 🔄 2026-09-01 |
| [**herdr-approve-all**](https://github.com/RenKoya1/herdr-approve-all)<br><sub>RenKoya1</sub> | herdr 插件：一键批准所有被阻塞的 Agent（一次按键处理所有待处理的权限提示） | `shell` | 2 | 2026-08-16 |
| [**herdr-code-board**](https://github.com/sazardev/herdr-code-board)<br><sub>sazardev</sub> | Herdr 内面向 Agent 提示词的看板队列——卡片会将真实 Agent 派发到窗格、工作树和工作区，并可通过规则将一张卡片链到下一张 | `ai-agents` `kanban` `rust` `tui` | 2 | 🔄 2026-08-30 |
| [**herdr-agents-history**](https://github.com/speardragon/herdr-agents-history)<br><sub>speardragon</sub> | 查看你的 AI 编程 Agent 实际在做什么——一个实时、键盘驱动的 herdr TUI，串流展示你所有 Agent（Claude Code 和 Codex）的每一次工具调用 | `ai-agents` `claude-code` `codex` `tui` `typescript` | 2 | 2026-07-19 |
| [**herdr-conductor**](https://github.com/StructuPath/herdr-conductor)<br><sub>StructuPath</sub> | 将功能交付团队编排为可见的 Herdr Agent 窗格——Conductor 插件 | `orchestration` `javascript` | 2 | 🔄 2026-08-23 |
| [**herdr-wakeup**](https://github.com/usrivastava92/herdr-wakeup)<br><sub>usrivastava92</sub> | 在 Herdr 管理的 Agent 工作期间，让 macOS 或 Linux 保持唤醒状态的 Herdr 插件 | `power-management` `sleep-prevention` `wakeup` `rust` | 2 | 2026-07-17 |
| [**herdr-agent-timer**](https://github.com/Yemeni/herdr-agent-timer)<br><sub>Yemeni</sub> | 让每个 Agent 的状态标签与其耗时交替显示的 Herdr 插件 | `shell` | 2 | 2026-08-14 |
| [**herdr-pouch**](https://github.com/AltanS/herdr-pouch)<br><sub>AltanS</sub> | herdr 插件：预先为 Agent 存储提示词，待其就绪时再插入 | `ai-agents` `ai-coding` `ai-tools` `multiplexing` `typescript` | 1 | 🔄 2026-09-02 |
| [**herdr-pi-reloader**](https://github.com/anrunt/herdr-pi-reloader)<br><sub>anrunt</sub> | 从 Herdr 浮层 TUI 中重新加载或重启闲置的 Pi Agent 会话 | `rust` | 1 | 2026-07-18 |
| [**herdr-handoff**](https://github.com/devops-fj/herdr-handoff)<br><sub>devops-fj</sub> | 在 Herdr 编程 Agent 之间预览并安全地移交本地工作上下文 | `ai-agents` `coding-agents` `go` | 1 | 2026-08-21 |
| [**herdr-cursor**](https://github.com/gabriel-laet/herdr-cursor)<br><sub>gabriel-laet</sub> | 将 Cursor 的云端 Agent 作为一等公民的 herdr 窗格来使用 | `typescript` | 1 | 2026-08-21 |
| [**herdr-agent-team**](https://github.com/gdli6177/herdr-agent-team)<br><sub>gdli6177</sub> | 用 Markdown 定义 Agent 团队的 Herdr 插件 | `javascript` | 1 | 2026-08-16 |
| [**herdr-prompt-bucket**](https://github.com/GNURub/herdr-prompt-bucket)<br><sub>GNURub</sub> | 面向运行在 Herdr 中的编程 Agent 的持久化、有序的提示词队列 | `claude-code` `codex` `coding-agents` `opencode` `typescript` | 1 | 2026-08-19 |
| [**LunaCrab**](https://github.com/GranamyrBR/LunaCrab)<br><sub>GranamyrBR</sub> | 为另一个项目保留 | `agents` `developer-tools` `multi-agent` `observability` `rust` | 1 | 2026-08-10 |
| [**agent-keep-awake**](https://github.com/happyeric77/agent-keep-awake)<br><sub>happyeric77</sub> | 在 Herdr Agent 工作期间阻止 macOS 休眠 | `javascript` | 1 | 2026-08-12 |
| [**herdr-dispatch**](https://github.com/husniadil/herdr-dispatch)<br><sub>husniadil</sub> | 面向 herdr-tasks 看板的调度器——为每个已就绪的任务启动一个 worker Agent 窗格，传递目标、追踪 worker，并在评审处暂停。全部由一个 Go 二进制程序实现 | `agent-orchestration` `ai-agents` `dispatcher` `mcp-server` `go` | 1 | 🔄 2026-08-31 |
| [**herdr-annotations**](https://github.com/IgorWarzocha/herdr-annotations)<br><sub>IgorWarzocha</sub> | 收集对终端选中内容的注释，并暂存到 Herdr Agent 中 | `ai-agents` `annotations` `terminal` `javascript` | 1 | 2026-07-18 |
| [**herdr-plan-approve**](https://github.com/jerryfane/herdr-plan-approve)<br><sub>jerryfane</sub> | 在 herdr 中自动批准 Claude Code 的计划模式对话框——Agent 制定计划后无需按键即可直接执行 | `claude-code` `shell` | 1 | 🔄 2026-08-25 |
| [**corral**](https://github.com/jirathip-dev/corral)<br><sub>jirathip-dev</sub> | Read-only fleet monitor for herdr coding agents | `agent-orchestration` `ai-agents` `coding-agents` `devtools` `fleet-management` | 1 | 🔄 2026-09-07 |
| [**herdr-watcher**](https://github.com/joshka0/herdr-watcher)<br><sub>joshka0</sub> | 为 Herdr Agent 提供持久化的执行续接和分离式 worker 回调 | `rust` | 1 | 2026-08-02 |
| [**herdr-turn-coordinator**](https://github.com/KarthusLorin/herdr-turn-coordinator)<br><sub>KarthusLorin</sub> | 在不依赖模型驱动的状态轮询的情况下，维持交互式 Herdr Agent TUI | `ai-agents` `python` | 1 | 🔄 2026-09-04 |
| [**herdr-island**](https://github.com/kay-ws/herdr-island)<br><sub>kay-ws</sub> | 找出正在等待你处理的 Agent——显示每个 herdr Agent 停下的原因，并将 Agents 面板筛选到只剩这些 | `shell` | 1 | 2026-08-04 |
| [**herdr-link**](https://github.com/LZHcode1986/herdr-link)<br><sub>LZHcode1986</sub> | 为 Herdr 会话提供更快、更省 token、无需推理的跨 Agent 互操作性。用一份统一的契约取代笨重的 skill，涵盖对等发现、消息传递和窗格生命周期 | `typescript` | 1 | 🔄 2026-09-06 |
| [**sheprd**](https://github.com/m-mohamed/sheprd)<br><sub>m-mohamed</sub> | 将 Pi、Codex、Claude Code 和 OpenCode 统一收纳到一个可见且隔离的 Herdr「Flok」中 | `agent-tools` `claude-code` `cli` `codex` `coding-agents` | 1 | 🔄 2026-08-25 |
| [**herdr-agents-preview**](https://github.com/maedana/herdr-agents-preview)<br><sub>maedana</sub> | Herdr 的多 Agent 终端预览仪表盘：同时显示所有运行中的 Agent，所选 Agent 占据大部分宽度 | `rust` | 1 | 2026-08-14 |
| [**herdr-standup**](https://github.com/natori-hrj/herdr-standup)<br><sub>natori-hrj</sub> | herdr 的 Agent 站会摘要——按 Agent 汇总其所在仓库中的提交和未提交的工作 | `ai-agents` `git` `standup` `rust` | 1 | 2026-07-23 |
| [**herdr-replay**](https://github.com/neospeed83/herdr-replay)<br><sub>neospeed83</sub> | 将多 Agent 的 Herdr 编程会话录制并回放为可交互的时间线 | `ai-agents` `developer-tools` `terminal-recording` `rust` | 1 | 🔄 2026-08-29 |
| [**herdr-tournament**](https://github.com/neospeed83/herdr-tournament)<br><sub>neospeed83</sub> | 面向 Herdr 的对抗式多 Agent 代码评审 | `rust` | 1 | 🔄 2026-08-29 |
| [**herdr-caffeinate**](https://github.com/nwarwick/herdr-caffeinate)<br><sub>nwarwick</sub> | 在 Herdr Agent 工作期间阻止 macOS 系统休眠 | `caffeinate` `coding-agents` `macos` `shell` | 1 | 2026-07-29 |
| [**herdr-spawn**](https://github.com/nytafar/herdr-spawn)<br><sub>nytafar</sub> | 一个 MCP 工具，将聊天中的提示词交给你某台主机上开启了 Remote Control 的真实 Claude Code 会话 | `python` | 1 | 2026-08-21 |
| [**herdr-imebox**](https://github.com/Sawakee/herdr-imebox)<br><sub>Sawakee</sub> | 便于向 herdr 中 AI Agent 窗格输入日文/CJK 文字的 IME 友好弹出文本框 | `cjk` `ime` `input-method` `japanese` `ratatui` | 1 | 2026-07-17 |
| [**🆕 herdr-achievements**](https://github.com/SerHappy/herdr-achievements)<br><sub>SerHappy</sub> | 为你的 Herdr AI Agent 群体添加成就和小小的庆祝 | `achievements` `ai-agents` `developer-tools` `gamification` `go` | 1 | 2026-07-30 |
| [**herdr-awake**](https://github.com/susomejias/herdr-awake)<br><sub>susomejias</sub> | herdr 插件：在 Herdr Agent 忙碌期间保持机器唤醒 | `shell` | 1 | 🔄 2026-08-26 |
| [**herdr-traex**](https://github.com/szrenwei/herdr-traex)<br><sub>szrenwei</sub> | 将 TraeX Agent 的生命周期与元数据接入 Herdr Marketplace | `traex` `python` | 1 | 2026-08-04 |
| [**herdr-orc**](https://github.com/tamdogood/herdr-orc)<br><sub>tamdogood</sub> | 面向 Herdr 的极简、基于配置文件驱动的自定义编排器 | `ai-agents` `multi-agent` `orchestrator` `javascript` | 1 | 2026-08-11 |
| [**tinysend-herdr**](https://github.com/tiny-send/tinysend-herdr)<br><sub>tiny-send</sub> | herdr 插件：当 Agent 阻塞/完成时给自己发邮件，回复即可解除阻塞。由 tinysend 提供支持 | `ai-agents` `tinysend` `javascript` | 1 | 2026-06-26 |
| [**herdr-rovo-dev**](https://github.com/usrivastava92/herdr-rovo-dev)<br><sub>usrivastava92</sub> | 检测 Rovo Dev CLI 会话并将其作为运行中的 Agent 报告给 Herdr 的插件 | `ai-agent` `rovo` `rovo-dev` `shell` | 1 | 2026-07-19 |
| [**herdr-polyglot**](https://github.com/wazum/herdr-polyglot)<br><sub>wazum</sub> | 用你自己的语言编写编程 Agent 提示词——DeepL 或 Google Cloud Translate 会将其翻译为英文，并投递到 Claude Code、Codex 或任意 herdr Agent 窗格中 | `ai-agents` `bubbletea` `bubbletea-tui` `claude-code` `codex` | 1 | 🔄 2026-09-01 |
| [**herdr-auto-yes-sir**](https://github.com/xlinx/herdr-auto-yes-sir)<br><sub>xlinx</sub> | herdr-auto-yes-sir——当 Agent 请求批准时，让运行不被阻塞地继续下去，类似 codex 的行为 | `javascript` | 1 | 2026-08-20 |
| [**herdr-cadence**](https://github.com/zhenyufu/herdr-cadence)<br><sub>zhenyufu</sub> | 由一个 Lead 和一组 Agent 组成的轻量级 Agent 编排器 | `rust` | 1 | 🔄 2026-09-04 |
| [**🆕 herdr-muse**](https://github.com/akshat12/herdr-muse)<br><sub>akshat12</sub> | Herdr integration for Muse Code: idle/working/blocked pane state via lifecycle hooks (no Herdr fork needed) | `ai-agents` `cli` `coding-agents` `muse-code` `terminal` | 0 | 🔄 2026-09-04 |
| [**herdr-simple-prompts**](https://github.com/AlexSamarsky/herdr-simple-prompts)<br><sub>AlexSamarsky</sub> | 只显示你自己的提示词和 Codex 或 Claude 的最终回答，并配有可用的输入框 | `rust` | 0 | 🔄 2026-08-31 |
| [**herdr-dynamic-workflow**](https://github.com/andthezhang/herdr-dynamic-workflow)<br><sub>andthezhang</sub> | 用于在 Herdr 中编排编程 Agent CLI 的 JavaScript 工作流 | `agent-fleet` `agent-orchestration` `agent-swarm` `agentic-ai` `agents` | 0 | 🔄 2026-08-30 |
| [**unblock**](https://github.com/aneym/unblock)<br><sub>aneym</sub> | 将 Agent 需要你处理的一切汇总到一个队列中。阻塞项需要你采取行动，grill 需要你做出判断——密钥永远不会进入模型的上下文 | `agents` `human-in-the-loop` `mcp` `javascript` | 0 | 🔄 2026-08-28 |
| [**hird**](https://github.com/aoprisan/hird)<br><sub>aoprisan</sub> | 跨 harness 的 Agent 工作队列与共享断言记忆，由一个本地 SQLite 数据库支撑 | `ai-agents` `claude-code` `cli` `mcp` `rust` | 0 | 🔄 2026-09-05 |
| [**🆕 herdr-stay-awake**](https://github.com/assawalhy/herdr-stay-awake)<br><sub>assawalhy</sub> | Keeps the machine from sleeping while any herdr agent pane is working (Linux, macOS, Windows, and WSL) | `agent-orchestration` `agents` `harness` `linux` `macos` | 0 | 🔄 2026-09-06 |
| [**herdr-quick-prompt**](https://github.com/astwys/herdr-quick-prompt)<br><sub>astwys</sub> | 向 Agent 窗格发送预定义提示词的 Herdr 插件 | `shell` | 0 | 🔄 2026-08-24 |
| [**otito-herdr-plugin**](https://github.com/BASHBOP/otito-herdr-plugin)<br><sub>BASHBOP</sub> | 在 Herdr Agent 工作区内运行 Otito 的上下文和确定性合并证据 | `ai-agents` `developer-tools` `merge-safety` `otito` `javascript` | 0 | 2026-08-21 |
| [**herdr-agent-manager**](https://github.com/bleedingfight/herdr-agent-manager)<br><sub>bleedingfight</sub> | 一个基于fzf的模糊搜索workspace、tab、pane、agent工具 | `python` | 0 | 🔄 2026-09-04 |
| [**herdr-warp**](https://github.com/cdpath/herdr-warp)<br><sub>cdpath</sub> | 在 Herdr 窗格中驱动交互式 Warp Agent CLI（warp）的 Herdr 插件：支持 open/send/status/wait/read/approve/deny/new/stop/exit，并通过屏幕抓取判断 idle/working/blocked 状态 | `shell` | 0 | 2026-08-13 |
| [**clawsouls-herdr-plugin**](https://github.com/clawsouls/clawsouls-herdr-plugin)<br><sub>clawsouls</sub> | _(暂无描述)_ | `ai-agents` `persona` `shell` | 0 | 2026-08-11 |
| [**herdr-tuple-plugin**](https://github.com/doggyfish/herdr-tuple-plugin)<br><sub>doggyfish</sub> | 在一个标签页中将两个编程 Agent 并排配对，并可在二者之间传递文本的 herdr 插件 | `javascript` | 0 | 2026-08-08 |
| [**herdr-chat**](https://github.com/eliasstravik/herdr-chat)<br><sub>eliasstravik</sub> | 为运行在 Herdr 中的 Agent 提供结构化的实时聊天视图 | `typescript` | 0 | 🔄 2026-08-24 |
| [**herdr-nudge**](https://github.com/EricBois/herdr-nudge)<br><sub>EricBois</sub> | 为 herdr Agent 设置「继续提醒」——在指定时间，或它变为闲置/被阻塞时触发 | `shell` | 0 | 2026-07-17 |
| [**🆕 pane-identity**](https://github.com/Ghost-LZW/pane-identity)<br><sub>Ghost-LZW</sub> | Display pane IDs, hostnames, and labels in Herdr without modifying your agents. | `python` `terminal` | 0 | 🔄 2026-09-05 |
| [**ezdras-herdr**](https://github.com/GranamyrBR/ezdras-herdr)<br><sub>GranamyrBR</sub> | 面向 Herdr 的实时多 Agent 可观测性与窗格控制 | `rust` | 0 | 2026-08-10 |
| [**herdr-mail**](https://github.com/husniadil/herdr-mail)<br><sub>husniadil</sub> | Herdr 上编程 Agent 之间的异步邮件——以存储为准的邮箱、作为提示的单行窗格标记，以及带追踪义务的 ask/reply，全部由一个 Go 二进制程序实现 | `ai-agents` `mail` `mcp-server` `sqlite` `go` | 0 | 🔄 2026-08-30 |
| [**herdr-ai-memory**](https://github.com/iagogfe/herdr-ai-memory)<br><sub>iagogfe</sub> | Herdr 插件：通过 ai-memory 管理的工作流启动编程 Agent——实现跨 Agent 的会话连续性 | `ai-agents` `ai-memory` `terminal` `javascript` | 0 | 2026-07-24 |
| [**herdr-pane-id**](https://github.com/imtim/herdr-pane-id)<br><sub>imtim</sub> | herdr 插件：为窗格标注 ID 和 Agent 名称，并加上标签页和工作区的 ID 标签——让你和你的 Agent 都能通过 ID 指定任意窗格或 Agent。与 herdr agent skill 配合使用效果最佳 | `ai-agents` `coding-agents` `developer-tools` `terminal-multiplexer` `tui` | 0 | 🔄 2026-08-24 |
| [**herdr-spawn**](https://github.com/JLighter/herdr-spawn)<br><sub>JLighter</sub> | herdr 插件：用提示词启动编程 Agent——每个 Agent 分配一个独立的 git 工作树 | `shell` | 0 | 2026-08-03 |
| [**herdr-suffix-agent-filter**](https://github.com/kazimshah39/herdr-suffix-agent-filter)<br><sub>kazimshah39</sub> | 在精确的 Space 后缀分组视图与默认视图之间切换 Herdr 的 Agents 侧边栏 | `coding-agents` `developer-tools` `terminal` `javascript` | 0 | 🔄 2026-08-27 |
| [**herdr-kit**](https://github.com/kevinWangSheng/herdr-kit)<br><sub>kevinWangSheng</sub> | 面向 Herdr 的声明式布局、事件监视器、插件和 socket 客户端——补齐 herdr CLI 未暴露的部分 | `coding-agents` `terminal-multiplexer` `python` | 0 | 2026-08-14 |
| [**led-agent-status**](https://github.com/lfsmoura/led-agent-status)<br><sub>lfsmoura</sub> | herdr 插件：在 BLE LED 灯带上显示 AI Agent 的状态——工作中为蓝色，阻塞时红色闪烁，完成时为绿色 | `ble` `led` `swift` | 0 | 2026-08-10 |
| [**herdr-claude-launcher**](https://github.com/lucasleon2107/herdr-claude-launcher)<br><sub>lucasleon2107</sub> | 打开已运行 Claude Code 的新标签页的 herdr 插件 | `ai-agents` `claude-code` `terminal` `tmux` `shell` | 0 | 2026-08-03 |
| [**herdr-alias-setter**](https://github.com/m2selfA/herdr-alias-setter)<br><sub>m2selfA</sub> | 设置窗格名称和 Agent 别名的 Herdr 插件（可快速输入或使用完整菜单） | `powershell` | 0 | 2026-08-21 |
| [**quickTUI**](https://github.com/marcjfj-vmlyr/quickTUI)<br><sub>marcjfj-vmlyr</sub> | 构建于 OpenTUI 之上、可拼装组合以快速搭建终端 UI 的基础组件集，以 Herdr 插件形式发布，为编程 Agent 提供 /quicktui 技能 | `bun` `opentui` `terminal` `tui` `typescript` | 0 | 2026-08-13 |
| [**herdr-agent-dash**](https://github.com/MartinBspheroid/herdr-agent-dash)<br><sub>MartinBspheroid</sub> | Herdr Agent Board：一目查看正在运行的编程 Agent 及其状态、工作目录和 Git 上下文的本地键盘优先 Herdr 插件 | `typescript` | 0 | 2026-07-21 |
| [**herdr-green**](https://github.com/natori-hrj/herdr-green)<br><sub>natori-hrj</sub> | herdr 的按 Agent 显示测试状态——当某个 Agent 完成时运行该项目的测试，并显示通过/失败 | `ai-agents` `ci` `tests` `rust` | 0 | 2026-07-23 |
| [**🆕 agentic-box**](https://github.com/nicoRomeroCuruchet/agentic-box)<br><sub>nicoRomeroCuruchet</sub> | 一个由 Claude Code 驱动本地模型 Agent 的隔离沙盒 | `agent-orchestration` `agentic` `agentic-workflow` `docker` `ornith-1-0-35b` | 0 | 2026-08-17 |
| [**herdr-plugin-aos**](https://github.com/noctaIO/herdr-plugin-aos)<br><sub>noctaIO</sub> | 从任意工作区在 herdr 窗格中启动支持 Agentic OS 的 Claude Code Agent。无侵入式 herdr 插件 | `shell` | 0 | 2026-07-11 |
| [**herdr-prompts**](https://github.com/oppenheimor/herdr-prompts)<br><sub>oppenheimor</sub> | 在 Herdr 中跨编程 Agent 保存、搜索、填充和复用提示词模板。灵感来自我的朋友 bingguanqi | `typescript` | 0 | 2026-08-19 |
| [**🆕 herdr-auto-warm-cache**](https://github.com/parker-brown-family/herdr-auto-warm-cache)<br><sub>parker-brown-family</sub> | A herdr plugin that keeps an idle agent's prompt cache warm before the one-hour TTL expires — 20x cheaper than letting it lapse. Asks before it types, and neve… | `claude-code` `prompt-caching` `shell` | 0 | 🔄 2026-09-04 |
| [**🆕 herdr-guard**](https://github.com/pauljohnchamberlain/herdr-guard)<br><sub>pauljohnchamberlain</sub> | 让 Codex、Claude 等编码 Agent 能够安全地对 Herdr 进行外部控制。 | `coding-agents` `typescript` | 0 | 🔄 2026-09-04 |
| [**herdr-sidekick**](https://github.com/qapquiz/herdr-sidekick)<br><sub>qapquiz</sub> | 面向 Herdr 的可开关的「副驾」AI Agent 窗格——可将选中的代码粘贴到 Agent 的输入框中而不直接提交。可与 qapquiz/herdr-sidekick.nvim 搭配使用 | `neovim` `terminal` `shell` | 0 | 2026-08-15 |
| [**ocean-herdr**](https://github.com/Risingtides-dev/ocean-herdr)<br><sub>Risingtides-dev</sub> | 面向 Herdr 的 Ocean Agent 集成 | `coding-agent` `ocean` `rust` | 0 | 2026-07-17 |
| [**herdr-want-to-sleep**](https://github.com/scheron/herdr-want-to-sleep)<br><sub>scheron</sub> | 当所有编程 Agent 都不再工作时，让 Mac 进入睡眠的 herdr 插件。睡前启用后，它会等待每个 Agent 都稳定下来，然后记录每个 Agent 所做的事情——包括最终被阻塞的那些 | `coding-agents` `macos` `shell` | 0 | 2026-07-28 |
| [**herdr-ask**](https://github.com/TaylorFinklea/herdr-ask)<br><sub>TaylorFinklea</sub> | 面向 Herdr 及任意终端的轻量命令生成与终端聊天 | `cli` `rust` `terminal` `tui` | 0 | 2026-07-21 |
| [**herdr-restart-always**](https://github.com/terafin/herdr-restart-always)<br><sub>terafin</sub> | 监督 herdr Agent 窗格，一旦 Agent 意外终止，就始终重启该窗格中运行的程序（claude、hermes、codex、pi、opencode 等） | `python` | 0 | 2026-08-15 |
| [**herdr-group-chat**](https://github.com/terry-li-hm/herdr-group-chat)<br><sub>terry-li-hm</sub> | 面向 Pi、Claude Code、Codex 和 Grok Build 的共享本地 Herdr 聊天室 | `ai-agents` `claude-code` `codex` `grok` `multi-agent` | 0 | 🔄 2026-09-07 |
| [**herdr-cline-plugin**](https://github.com/TheMetalStorm/herdr-cline-plugin)<br><sub>TheMetalStorm</sub> | 让从任意窗格启动的原生 Cline CLI 看起来像原生 Herdr Agent 的 Herdr 插件 | `cli` `cline` `herdr-integration` `shell` | 0 | 2026-07-31 |
| [**herdr-cmd-agent-plugin**](https://github.com/thesimonharms/herdr-cmd-agent-plugin)<br><sub>thesimonharms</sub> | 将 CommandCode（cmd）识别为 Agent 的 Herdr 插件——通过屏幕清单和 cmd mod 判断 idle/working/blocked 状态 | `cmd` `commandcode` `shell` | 0 | 🔄 2026-09-04 |
| [**herdr-agent-notes**](https://github.com/timjonez/herdr-agent-notes)<br><sub>timjonez</sub> | herdr 插件：为 Agent 贴上便签，让你能看出某个 Agent 为何处于空闲状态 | `python` | 0 | 2026-08-20 |
| [**herdr-agent-topic**](https://github.com/wynemo/herdr-agent-topic)<br><sub>wynemo</sub> | herdr 插件：在每张 Agent 卡片中显示你最近发送的用户提示词 | `go` | 0 | 2026-08-20 |
| [**cbds**](https://github.com/zqkra/cbds)<br><sub>zqkra</sub> | 面向 Herdr 群体的可靠多 Agent 编排。提供持久化任务、权威的 worker 报告，以及不会卡死的等待机制 | `agents` `cli` `multi-agent` `orchestration` `javascript` | 0 | 🔄 2026-08-31 |

<details><summary>与此目的也相关</summary>

- [AltanS/collie](https://github.com/AltanS/collie) — 随时随地管理 herdr 的 PWA 应用。支持 Tailnet 访问、推送通知、快捷操作等
- [a2u/herdr-jira](https://github.com/a2u/herdr-jira) — herdr 的 Jira TUI 插件——通过可配置的 JQL 过滤器浏览、搜索 issue，修改状态，并一键将 issue 交给终端中运行的 AI Agent 处理
- [walcew/herdr-assist](https://github.com/walcew/herdr-assist) — 面向 AI 编程 Agent 终端复用器 Herdr 的实体桌面面板——用颜色显示会话状态，当 Agent 停下来请求决策时会响铃提醒。基于 ESP32-S3 + LVGL，提供预编译固件
- [e2b-dev/herdr-e2b-sandbox](https://github.com/e2b-dev/herdr-e2b-sandbox) — 将 git 工作树镜像到 E2B Sandbox 的 herdr 插件——支持单个沙盒或每个 Agent 一条分支的沙盒集群，并配有 TUI 仪表盘
- [miko-misa/herdr-portfwd](https://github.com/miko-misa/herdr-portfwd) — 面向远程机器上编程 Agent 的自动 SSH 端口转发——Ctrl+点击 Agent 打印的 localhost URL，即可在你本机以相同端口打开该页面。一个 Herdr 插件
- [spad-0x/herdr-web-dashboard](https://github.com/spad-0x/herdr-web-dashboard) — A high-performance, mobile-first PWA dashboard with a Cyber-Dark design for orchestrating Herdr and autonomou…
- [JefeLabs/herdr-web-broker](https://github.com/JefeLabs/herdr-web-broker) — 面向 herdr 的自托管 REST/WS API——可从任何地方启动并操控编程 Agent。支持 token、多用户会话所有权、git 操作、事件流以及父子实例联邦。附带 TypeScript SDK 和 React…

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-worktree"></a>

## git 工作树与分支管理

> 想为每项工作单独开一个工作树，收尾清理也自动完成

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-worktrunk**](https://github.com/devashish2203/herdr-worktrunk)<br><sub>devashish2203</sub> | 集成 worktrunk 以管理 git 工作树的 Herdr 插件 | `shell` | 130 | 🔄 2026-08-27 |
| [**herdr-plugin-jj-workspace**](https://github.com/NathanFlurry/herdr-plugin-jj-workspace)<br><sub>NathanFlurry</sub> | 将 Jujutsu (jj) 工作区作为 Herdr 工作区进行创建和删除 | `jujutsu` `rust` | 47 | 🔄 2026-09-03 |
| [**🆕 herdr-studio**](https://github.com/powerfooI/herdr-studio)<br><sub>powerfooI</sub> | Herdr 的 Web 客户端，专为移动端体验打磨——提供浏览器终端、工作区与 worktree 管理、文件与差异查看器，以及 AI Agent 会话查看功能。 | `ai-agents` `dogfooding` `git-worktree` `herdr-client` `mobile-friendly` | 38 | 🔄 2026-09-06 |
| [**herdr-plugin-renamer**](https://github.com/wyattjoh/herdr-plugin-renamer)<br><sub>wyattjoh</sub> | 根据 Agent 的第一条提示词，重命名自动生成的 herdr 工作树分支和工作区（通过设备端 Apple FoundationModels 或 Codex） | `rust` | 12 | 2026-08-17 |
| [**jj-waltz**](https://github.com/EzraCerpac/jj-waltz)<br><sub>EzraCerpac</sub> | 受 Worktrunk 启发的 Jujutsu 工作区切换工具 | `cli` `jj` `jujitsu` `utility` `workspace` | 8 | 2026-08-21 |
| [**herdr-e2b-sandbox**](https://github.com/e2b-dev/herdr-e2b-sandbox)<br><sub>e2b-dev</sub> | 将 git 工作树镜像到 E2B Sandbox 的 herdr 插件——支持单个沙盒或每个 Agent 一条分支的沙盒集群，并配有 TUI 仪表盘 | `cli` `cloud-dev` `e2b` `git-worktree` `sandbox` | 6 | 🔄 2026-09-04 |
| [**herdr-plugin-git-worktree-hooks**](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks)<br><sub>freethinkel</sub> | 在创建/移除 git 工作树时运行 shell 命令——一份 YAML 配置适用于所有项目，放在任何仓库之外 | `git-worktree` `javascript` | 6 | 2026-07-06 |
| [**herdr-worktree-from-pr**](https://github.com/tdi/herdr-worktree-from-pr)<br><sub>tdi</sub> | 从 GitHub PR 创建 git 工作树，并作为 herdr 工作区打开 | `javascript` | 6 | 2026-07-20 |
| [**herdr-symlink-worktree**](https://github.com/hmu332233/herdr-symlink-worktree)<br><sub>hmu332233</sub> | 将主仓库中的共享本地文件符号链接到新工作树中的 herdr 插件 | `shell` | 5 | 2026-07-16 |
| [**herdr-worktree-seed**](https://github.com/jlimas/herdr-worktree-seed)<br><sub>jlimas</sub> | 为新工作树植入 copy-on-write 的 node_modules 和可配置本地 dotfiles 的 Herdr 插件 | `developer-tools` `dotfiles` `git-worktree` `nodejs` `typescript` | 5 | 2026-07-28 |
| [**herdr-fresh-worktree**](https://github.com/persiyanov/herdr-fresh-worktree)<br><sub>persiyanov</sub> | 将新创建的 herdr 工作树重置为 origin 默认分支的最新状态 | `javascript` | 4 | 2026-06-25 |
| [**herdr-worktreeinclude**](https://github.com/tanshio/herdr-worktreeinclude)<br><sub>tanshio</sub> | Herdr 插件：将匹配 .worktreeinclude 的被 gitignore 文件复制到新创建的工作树中 | `worktree` `worktreeiclude` `shell` | 4 | 2026-07-11 |
| [**herdr-worktree-hooks**](https://github.com/timofey-TK/herdr-worktree-hooks)<br><sub>timofey-TK</sub> | herdr 插件：在创建、打开或删除 git 工作树时运行自定义的初始化/清理命令 | `developer-tools` `git-worktree` `worktree` `python` | 4 | 2026-07-17 |
| [**herdr-remote-worktrunk**](https://github.com/ditwrd/herdr-remote-worktrunk)<br><sub>ditwrd</sub> | Herdr 的远程 worktrunk 工作区 | `shell` | 3 | 2026-07-10 |
| [**herdr-jj**](https://github.com/OliverGilan/herdr-jj)<br><sub>OliverGilan</sub> | 为 Herdr 添加 Jujutsu 工作区支持 | `jujutsu` `rust` | 3 | 2026-08-12 |
| [**herdr-branch-cleanup**](https://github.com/osolmaz/herdr-branch-cleanup)<br><sub>osolmaz</sub> | 当窗格所在分支在 GitHub 上被合并或删除后，自动切换到默认分支 | `git` `github` `rust` | 3 | 2026-07-26 |
| [**herdr-worktree-lifecycle**](https://github.com/qdentity/herdr-worktree-lifecycle)<br><sub>qdentity</sub> | Herdr 插件：将工作树生命周期事件分发给仓库自带的初始化/清理脚本 | `rust` | 3 | 2026-06-29 |
| [**herdr-multirepo**](https://github.com/jattento/herdr-multirepo)<br><sub>jattento</sub> | 在一个 Herdr 工作区中管理跨多个仓库的同一条功能分支 | `git-worktree` `python` | 2 | 2026-08-03 |
| [**herdr-shear**](https://github.com/moneycaringcoder/herdr-shear)<br><sub>moneycaringcoder</sub> | 找出可以安全删除的 git 工作树并将其删除——一个面向 herdr 的工作树清洁工 | `cleanup` `git-worktree` `rust` `terminal` | 2 | 🔄 2026-09-01 |
| [**herdr-jj-status**](https://github.com/mroth/herdr-jj-status)<br><sub>mroth</sub> | herdr 插件：在空间侧边栏中显示 jj 工作区的 Jujutsu 书签/状态 | `shell` | 2 | 2026-07-28 |
| [**herdr-worktreeinclude**](https://github.com/serhii-chernenko/herdr-worktreeinclude)<br><sub>serhii-chernenko</sub> | 允许为新工作树指定自定义路径，并像 Claude CLI 一样遵循 `.worktreeinclude` 文件 | `worktree` `shell` | 2 | 2026-07-23 |
| [**herdr-worktree-nav**](https://github.com/ShoMasegi/herdr-worktree-nav)<br><sub>ShoMasegi</sub> | _(暂无描述)_ | `terminal` `rust` | 2 | 🔄 2026-09-07 |
| [**herdr-corral**](https://github.com/bfreed/herdr-corral)<br><sub>bfreed</sub> | 在 Herdr 中集中管理 Git 工作树：env 文件、依赖、Agent/shell/服务器标签页，以及合并安全的清理。作为 Herdr 版的 workmux 替代品 | `git-worktree` `workmux` `python` | 1 | 2026-08-14 |
| [**herdr-worktree-copy**](https://github.com/crexi/herdr-worktree-copy)<br><sub>crexi</sub> | 根据 .worktree-copy 清单复制并符号链接工作树本地文件的 Herdr 插件 | `git-worktree` `shell` | 1 | 2026-07-28 |
| [**herdr-deck**](https://github.com/ctbaum/herdr-deck)<br><sub>ctbaum</sub> | herdr-agents.nvim 的搭配工作区启动器：在预先搭好的 Neovim、Agent、shell 和 lazygit 组合面板中打开或恢复 Claude 和 Codex | `claude-code` `codex` `coding-agents` `git-worktree` `neovim` | 1 | 🔄 2026-08-24 |
| [**🆕 herdr-composer**](https://github.com/danieljvdm/herdr-composer)<br><sub>danieljvdm</sub> | 编排任务、附加上下文，并在隔离的 Herdr 工作区中启动编码 Agent。 | `coding-agents` `git-worktree` `rust` | 1 | 🔄 2026-09-01 |
| [**trunkr**](https://github.com/disintegrator/trunkr)<br><sub>disintegrator</sub> | Herdr 🤝 Worktrunk——连接 Herdr 与 Worktrunk 的插件 | `go` | 1 | 2026-08-12 |
| [**herdr-allow**](https://github.com/Feasy01/herdr-allow)<br><sub>Feasy01</sub> | herdr 插件：通过 .herdr-allow 允许列表，将被 gitignore 的文件（.env、密钥、本地配置）复制到每个新工作树中 | `shell` | 1 | 2026-07-02 |
| [**herdr-plugin-gwm**](https://github.com/kbrdn1/herdr-plugin-gwm)<br><sub>kbrdn1</sub> | 驱动 gwm 来管理 git 工作树的 herdr 插件——gwm 保持权威数据源，herdr 只是采纳它 | `bash` `cli` `git-worktree` `gwm` `worktree` | 1 | 2026-07-27 |
| [**herdr-collide**](https://github.com/moneycaringcoder/herdr-collide)<br><sub>moneycaringcoder</sub> | 当在同一仓库不同 git 工作树中工作的 Agent 即将发生冲突时发出警告——并判断它们的修改只是重叠还是会真正产生冲突 | `conflict-detection` `git-worktree` `rust` `terminal` | 1 | 🔄 2026-09-01 |
| [**herdr-standup**](https://github.com/moneycaringcoder/herdr-standup)<br><sub>moneycaringcoder</sub> | 总结你的 Agent 实际做了什么。一条命令即可获得指定时间段内所有 Herdr 工作区的可读摘要——提交、改动量、分支，以及工作是否落地 | `git` `rust` `standup` `terminal` | 1 | 🔄 2026-09-01 |
| [**🆕 herdr-worktree-include**](https://github.com/tupton/herdr-worktree-include)<br><sub>tupton</sub> | Symlink or copy untracked files to git worktrees created by herdr. | `shell` | 1 | 🔄 2026-09-06 |
| [**herdr-plugin-worktree-bootstrap**](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap)<br><sub>zerodice0</sub> | 在新的 Herdr Git 工作树中安全地复制被忽略的本地文件并运行初始化命令 | `python` | 1 | 2026-08-03 |
| [**herdr-plugin-pr-board**](https://github.com/0xthc/herdr-plugin-pr-board)<br><sub>0xthc</sub> | 在 herdr 中处理当前仓库的 GitHub PR——在窗格中浏览，将选中的 PR 检出为工作树工作区，并安全地回收已合并的 PR | `shell` | 0 | 2026-08-20 |
| [**herdr-plugin-worktree-bootstrap**](https://github.com/0xthc/herdr-plugin-worktree-bootstrap)<br><sub>0xthc</sub> | 在新的 herdr 工作树打开的瞬间，为其植入 .env 文件和 node_modules | `shell` | 0 | 2026-08-22 |
| [**herdr**](https://github.com/AgentTeamsRun/herdr)<br><sub>AgentTeamsRun</sub> | 将 herdr 工作树的生命周期事件上报给 AgentTeams 注册中心 | — | 0 | 2026-08-19 |
| [**herdr-worktree-provisioner**](https://github.com/arjenblokzijl/herdr-worktree-provisioner)<br><sub>arjenblokzijl</sub> | 在新工作树自己的可见窗格中运行按仓库定制的初始化——可组合，无需守卫检查 | `bootstrap` `git-worktree` `worktree` `shell` | 0 | 2026-07-08 |
| [**🆕 herdr-wt-purpose**](https://github.com/bonkey/herdr-wt-purpose)<br><sub>bonkey</sub> | Herdr plugin: worktree from a purpose or ticket URL, branch named by Apple's on-device model, scaffolded in the background | `apple-intelligence` `git-worktree` `shell` | 0 | 🔄 2026-09-06 |
| [**herdr-plugin-env-sync**](https://github.com/DecampsRenan/herdr-plugin-env-sync)<br><sub>DecampsRenan</sub> | Herdr 插件：env-sync 会为新的 Git 工作树完成初始化（复制 .env、跟踪远程分支、运行初始化命令），并提供实时状态面板 | `developer-tools` `git-worktree` `shell` | 0 | 🔄 2026-08-28 |
| [**herdr-worktreeinclude**](https://github.com/eightHundreds/herdr-worktreeinclude)<br><sub>eightHundreds</sub> | Herdr 插件：将 .worktreeinclude 指定的被 gitignore 文件复制到新工作树中 | `worktree` `rust` | 0 | 2026-07-28 |
| [**herdr-title**](https://github.com/filoozom/herdr-title)<br><sub>filoozom</sub> | 在终端标签页标题中显示所选工作树和 Agent 活动状态的 Herdr 插件 | `rust` | 0 | 2026-07-24 |
| [**herdr-hub-worktrees**](https://github.com/klukacin/herdr-hub-worktrees)<br><sub>klukacin</sub> | herdr 插件：将 hub 工作树镜像到每个嵌套子仓库的克隆中 | `git-worktree` `monorepo` `terminal-multiplexer` `shell` | 0 | 2026-08-12 |
| [**gren-herdr**](https://github.com/langtind/gren-herdr)<br><sub>langtind</sub> | 通过 gren 创建、切换和删除 git 工作树的 herdr 插件——支持 gren 的创建后初始化 | `git-worktree` `gren` `shell` | 0 | 🔄 2026-09-02 |
| [**herdr-worktree-hooks-plugin**](https://github.com/m1sk9/herdr-worktree-hooks-plugin)<br><sub>m1sk9</sub> | 为 Herdr 的工作树添加可自定义钩子的插件 | `rust` | 0 | 🔄 2026-09-06 |
| [**🆕 herdr-worktree-include**](https://github.com/scoussens-nthplusio/herdr-worktree-include)<br><sub>scoussens-nthplusio</sub> | 使用仓库的 .worktreeinclude（与 Claude Code 使用的同一份文件、同一套规则），将 .env 等被 gitignore 忽略的文件复制到新的 Herdr 工作树中 | `dotenv` `git-worktree` `shell` | 0 | 🔄 2026-08-27 |
| [**herdr-jira-worktree**](https://github.com/spiritsack/herdr-jira-worktree)<br><sub>spiritsack</sub> | herdr 插件：提示输入 Jira 工单，打开或复用对应的 git 工作树，并预填到全新的 Claude Code 会话中 | `shell` | 0 | 🔄 2026-08-24 |
| [**herdr-worktree-guard**](https://github.com/takeaship/herdr-worktree-guard)<br><sub>takeaship</sub> | 专注安全性、用于追踪并清理 Agent 工作树的 Herdr 插件 | `coding-agents` `git-worktree` | 0 | 🔄 2026-08-30 |
| [**herdr-worktree**](https://github.com/tjg184/herdr-worktree)<br><sub>tjg184</sub> | 同时兼容 worktrunk 和原生工作树的 Herdr 工作树插件 | `rust` | 0 | 2026-08-13 |
| [**herdr-coder-sessions**](https://github.com/ubuntudroid/herdr-coder-sessions)<br><sub>ubuntudroid</sub> | 在 herdr 中浏览正在运行的 Coder Agent 会话，并将每个会话作为独立工作区打开——通过 agentty 连接到该会话，其更改会被镜像到本地工作树中以供评审 | `agentapi` `coder` `coding-agents` `python` | 0 | 🔄 2026-09-04 |
| [**herdr-git-stack**](https://github.com/ubuntudroid/herdr-git-stack)<br><sub>ubuntudroid</sub> | herdr 插件：在 spaces 侧边栏中显示每个 space 在其 git 分支栈中的位置，标记出父分支已移动的分支，并保持栈的连续性。仅使用本地提交图——无需联网、无需 forge API、无需额外的堆栈工具 | `bash` `developer-tools` `git` `stacked-branches` `shell` | 0 | 🔄 2026-09-03 |

<details><summary>与此目的也相关</summary>

- [tdi/herdr-worktree-from-linear](https://github.com/tdi/herdr-worktree-from-linear) — 从 Linear issue 创建 git 工作树，并作为 herdr 工作区打开
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — 为 JavaScript 和 TypeScript 自动初始化 Herdr 工作树，支持基于锁文件的安装和安全的环境变量还原
- [tomasvarga/herdr-e2b](https://github.com/tomasvarga/herdr-e2b) — 按需将 git 工作树镜像到全新的 E2B 云沙盒——直接上传快照（包括未提交的更改），无需 push 或 clone。一个 herdr 插件
- [JLighter/herdr-spawn](https://github.com/JLighter/herdr-spawn) — herdr 插件：用提示词启动编程 Agent——每个 Agent 分配一个独立的 git 工作树
- [jtnovellis/herdr-worktree-setup](https://github.com/jtnovellis/herdr-worktree-setup) — herdr 插件：让新建的 git 工作树立刻可用——复制 .env 和开发状态、克隆依赖缓存（APFS/reflink）、执行 mise trust、direnv allow、安装依赖，并提供实时 TUI
- [snics/herdr-worktree-from-gitlab](https://github.com/snics/herdr-worktree-from-gitlab) — herdr 插件：从 GitLab issue（通过 glab）创建 git 工作树和工作区
- [untalfranfernandez/herdr-worktreeinclude](https://github.com/untalfranfernandez/herdr-worktreeinclude) — 为每个新建 git 工作树自动填充所需的、被 gitignore 忽略的本地文件（.env、settings.local.json、fixtures 等）的 Herdr 插件。只需在 .worktreeinclude…

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-review"></a>

## 代码审查与差异对比

> 想阅读 Agent 写的差异并对其发表评论

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**crabbox**](https://github.com/openclaw/crabbox)<br><sub>openclaw</sub> | Crabbox：预热沙盒、同步差异、运行测试套件 | `agent-skills` `remote-test-runner` `go` | 1373 | 🔄 2026-09-07 |
| [**herdr-reviewr**](https://github.com/persiyanov/herdr-reviewr)<br><sub>persiyanov</sub> | A code review + file viewer sidebar for herdr. Comment on a diff and send back to agent. Inspect diffs, files, and a PR state. | `code-review` `rust` `tui` | 612 | 🔄 2026-09-05 |
| [**herdr-annotate**](https://github.com/plannotator/herdr-annotate)<br><sub>plannotator</sub> | 在 Herdr 中为终端文本、文档和 Agent 回复添加注释并进行评审，并将反馈直接发回给 Agent | `annotation` `multiplexer` `rust` | 381 | 🔄 2026-09-07 |
| [**herdr-hunk-diff**](https://github.com/jhochenbaum/herdr-hunk-diff)<br><sub>jhochenbaum</sub> | 从 herdr 在 Hunk 中审查 Agent 编写的更改，并将行内评论回传给对应的 Agent | `code-review` `hunk` `typescript` | 111 | 🔄 2026-09-02 |
| [**herdr-plannotator**](https://github.com/plannotator/herdr-plannotator)<br><sub>plannotator</sub> | 在 Herdr 的 Browser 窗格内打开 Plannotator 评审的插件 | `plannotator` `typescript` | 24 | 2026-07-29 |
| [**herdr-pickr**](https://github.com/tomasvarga/herdr-pickr)<br><sub>tomasvarga</sub> | herdr 的 PR 审查路由器——按住 Ctrl 点击 GitHub PR / GitLab MR 链接，选择审查工具（tuicr · hunk · diff · 浏览器 · 或自定义工具），可选启用 AI 初审 | `cli` `code-review` `pull-request` `tui` `shell` | 16 | 2026-07-13 |
| [**herdr-plugin-hunk**](https://github.com/edmundmiller/herdr-plugin-hunk)<br><sub>edmundmiller</sub> | 在分屏窗格或标签页中打开 Hunk 差异对比的 Herdr 插件 | `python` | 15 | 2026-06-23 |
| [**herdr-gitview**](https://github.com/ChmaraX/herdr-gitview)<br><sub>ChmaraX</sub> | herdr 的 Git 状态/差异面板——审查更改、在 nvim 中编辑、暂存/提交/丢弃，全部在终端内完成 | `git` `git-diff` `git-tui` `neovim` `rust` | 9 | 🔄 2026-09-06 |
| [**herdr-plugin-hunk-autodiff**](https://github.com/scott306lr/herdr-plugin-hunk-autodiff)<br><sub>scott306lr</sub> | Herdr 插件：当编程 Agent 完成任务但留有未提交更改时，自动打开 hunk 差异分屏 | `claude-code` `hunk` `python` | 5 | 2026-07-05 |
| [**herdr-extensions**](https://github.com/vonzelle-vzt/herdr-extensions)<br><sub>vonzelle-vzt</sub> | 面向 herdr 的迷你 VS Code——具备 LSP 诊断、自动补全、重命名和跳转到定义的完整编辑器，外加源代码管理、搜索、问题面板、测试、调试器、应用实时预览、运行时错误捕获、图片粘贴和 Agent 差异审查。共 12 个面板，一条命令即可幂等且可逆地安装 | `agent-tools` `autocomplete` `claude-code` `cli` `code-review` | 5 | 2026-08-03 |
| [**herdr-progressive-reviewer**](https://github.com/flupke/herdr-progressive-reviewer)<br><sub>flupke</sub> | 受 Tidewave 启发的回合制差异审查工具 | `rust` | 3 | 🔄 2026-09-04 |
| [**herdr-review.nvim**](https://github.com/inferst/herdr-review.nvim)<br><sub>inferst</sub> | 集成 Git 和 herdr 的 Neovim 代码审查 UI | `lua` | 3 | 2026-08-01 |
| [**herdr-review**](https://github.com/quantk/herdr-review)<br><sub>quantk</sub> | 在 Hunk 中审查 Agent 编写的更改，并通过 Herdr 回传行内反馈 | `code-review` `hunk` `javascript` | 3 | 2026-07-28 |
| [**easy-review**](https://github.com/VilfredSikker/easy-review)<br><sub>VilfredSikker</sub> | 面向 AI 辅助编程的 Git 差异审查，提供终端 TUI 和 Tauri 桌面应用两种形式 | `ai-code-review` `cli` `code-review` `desktop-app` `developer-tools` | 3 | 🔄 2026-09-06 |
| [**herdr-pr-tracker**](https://github.com/jakekroon/herdr-pr-tracker)<br><sub>jakekroon</sub> | 将你所创建的所有未关闭拉取请求以停靠面板形式展示，并按你需要处理的紧迫程度进行颜色标注。一个 Herdr 插件 | `bun` `code-review` `developer-tools` `github` `pull-requests` | 2 | 🔄 2026-09-05 |
| [**herdr-scribe**](https://github.com/Javamomma/herdr-scribe)<br><sub>Javamomma</sub> | herdr 插件：不录音的实时会议转录——将麦克风输入转为仅存于内存的文字记录和实时分析窗格；停止时生成会议纪要、可选策略关卡以及可审查的自动草稿。支持 Linux/WSL2 和 macOS | `macos` `meeting-notes` `privacy` `speech-to-text` `terminal` | 2 | 2026-08-07 |
| [**herdr-comments**](https://github.com/shadowfax92/herdr-comments)<br><sub>shadowfax92</sub> | 为复制的 Herdr 终端输出添加注释，按窗格收集评论，并可在 Neovim 中审查 | `ai-agents` `annotations` `neovim` `rust` `terminal` | 2 | 2026-08-19 |
| [**herdr-hunk**](https://github.com/yuucu/herdr-hunk)<br><sub>yuucu</sub> | herdr 插件：为你的 Agent 工作区切换 Hunk 差异审查 | `diff` `hunk` `go` | 2 | 2026-07-20 |
| [**herdr-strays**](https://github.com/aleslanger/herdr-strays)<br><sub>aleslanger</sub> | 用于整理散落 git 工作树的终端 UI——浏览项目、实时查看变更文件、阅读差异，并可在不离开面板的情况下向 Claude 发送提示词 | `rust` | 1 | 2026-08-12 |
| [**roboherd**](https://github.com/andschneider/roboherd)<br><sub>andschneider</sub> | 在 herdr 工作区中处理 roborev 的评审状态和操作 | `rust` `tui` | 1 | 🔄 2026-09-06 |
| [**herdr-agent-diff**](https://github.com/baotran01/herdr-agent-diff)<br><sub>baotran01</sub> | 用于查看 Agent 文件系统和 Git 差异的 Herdr 插件 | `rust` | 1 | 2026-08-03 |
| [**herdr-stagr**](https://github.com/brianh20/herdr-stagr)<br><sub>brianh20</sub> | 面向 herdr 的源代码管理侧边栏——通过并排差异对比进行暂存、取消暂存和放弃更改 | `git` `tui` `rust` | 1 | 2026-08-06 |
| [**🆕 Vincent**](https://github.com/chasereyn/Vincent)<br><sub>chasereyn</sub> | 一款以鼠标操作为主的终端客户端，用于审查 AI Agent 编写的代码，并可就地修改。 | `go` | 1 | 🔄 2026-09-03 |
| [**herdr-peer-review**](https://github.com/Elio2000/herdr-peer-review)<br><sub>Elio2000</sub> | 在 herdr 窗格中打开第二个编程 Agent 来审查你的差异——可观察、自动批准、只读。附带用于「审查↔修改↔决策」自主循环的 Claude Code skill | `agent-skills` `ai-agents` `claude-code` `code-review` `codex` | 1 | 2026-07-16 |
| [**herdr-tasks**](https://github.com/husniadil/herdr-tasks)<br><sub>husniadil</sub> | 面向 Herdr 编程 Agent 的任务待办和笔记看板——带租约的 claim、有证据支撑的评审，以及人工决策关卡，全部由一个 Go 二进制程序实现 | `ai-agents` `mcp-server` `notes` `sqlite` `task-management` | 1 | 🔄 2026-08-30 |
| [**herdr-git-graph**](https://github.com/jorge-huxley/herdr-git-graph)<br><sub>jorge-huxley</sub> | Herdr 的只读 git 图谱 TUI 插件，支持彩色 ASCII 分支线、分支过滤、搜索和按需查看差异 | `rust` | 1 | 2026-07-17 |
| [**agentflock**](https://github.com/neospark-sol/agentflock)<br><sub>neospark-sol</sub> | 由 AI 协调的构建者与评审者小组，配有持久化的里程碑管理 | `ai-agents` `pair-programming` `typescript` | 1 | 2026-08-21 |
| [**herdr-hunk-viewer**](https://github.com/tareqmlx/herdr-hunk-viewer)<br><sub>tareqmlx</sub> | _(暂无描述)_ | `code-review` `hunk` `rust` | 1 | 2026-08-21 |
| [**herdr-lazygit-viewer**](https://github.com/tareqmlx/herdr-lazygit-viewer)<br><sub>tareqmlx</sub> | 在最适合当下场景的 Herdr 展示位置，以打开 files、branches、commits 或 stash 面板的状态启动 lazygit | `code-review` `lazygit` `rust` | 1 | 2026-08-14 |
| [**herdr-hunk-gh-diff**](https://github.com/Allianaab2m/herdr-hunk-gh-diff)<br><sub>Allianaab2m</sub> | Herdr 插件：在当前窗格所在分支与其 GitHub 拉取请求的目标分支之间打开 Hunk 差异 | `python` | 0 | 2026-07-15 |
| [**herdr-hunk**](https://github.com/cevr/herdr-hunk)<br><sub>cevr</sub> | 将 Hunk 的评审记录发送到对应的 Herdr Agent 窗格 | `effect-ts` `hunk` `typescript` | 0 | 2026-07-28 |
| [**herdr-hunk**](https://github.com/goofansu/herdr-hunk)<br><sub>goofansu</sub> | 提供快速的 Herdr 评审操作，打开一个临时的 Hunk 浮层。退出 Hunk 会关闭浮层并恢复你的工作区 | `python` | 0 | 🔄 2026-08-25 |
| [**herdr-implement-review**](https://github.com/Idan-Levin/herdr-implement-review)<br><sub>Idan-Levin</sub> | 用于 Codex 实现、安全扫描和「母 Agent」评审的 Herdr 工作流 | `claude-code` `codex` `security-review` `shell` | 0 | 2026-08-10 |
| [**herdr-plan-code-review**](https://github.com/inxx/herdr-plan-code-review)<br><sub>inxx</sub> | herdr 插件：Opus 做计划，Sonnet 写代码，Claude+Codex 做审查——一个操作打开四个 Agent 窗格 | `claude-code` `codex` `terminal` `shell` | 0 | 2026-07-06 |
| [**herdr-idle-panes**](https://github.com/leonho/herdr-idle-panes)<br><sub>leonho</sub> | herdr 插件：以清单弹窗形式查看并关闭停留在闲置 shell 的窗格 | `python` | 0 | 2026-08-22 |
| [**herdr-diff-review.nvim**](https://github.com/rytkmt/herdr-diff-review.nvim)<br><sub>rytkmt</sub> | 在应用之前，于 Neovim diff 模式中审查 AI Agent 的文件更改——用一条命令即可批准或拒绝来自 Claude Code 和 Kiro CLI 的编辑 | `kiro-cli` `neovim` `neovim-plugin` `neovim-plugins` `nvim` | 0 | 2026-08-18 |
| [**🆕 lasso**](https://github.com/skellleks/lasso)<br><sub>skellleks</sub> | herdr 的审查窗格：按 Agent 展示带语法高亮的差异，并可将行内评论发回给该 Agent。 | `ai-agents` `claude-code` `code-review` `git-diff` `ratatui` | 0 | 🔄 2026-08-31 |
| [**herdr-code-review**](https://github.com/txmed82/herdr-code-review)<br><sub>txmed82</sub> | 面向 Herdr 的结构化 AI 代码审查插件 | `code-review` `javascript` | 0 | 2026-08-19 |

<details><summary>与此目的也相关</summary>

- [powerfooI/herdr-studio](https://github.com/powerfooI/herdr-studio) — Herdr 的 Web 客户端，专为移动端体验打磨——提供浏览器终端、工作区与 worktree 管理、文件与差异查看器，以及 AI Agent 会话查看功能。
- [JacquesvanWyk/herdr-hunk](https://github.com/JacquesvanWyk/herdr-hunk) — herdr 中用于 Hunk 差异对比的交互式 fzf 选择器：支持提交、范围、stash，并可在 Agent 完成时自动打开
- [anhnd3005-infinity/herdr-worker-orchestrator](https://github.com/anhnd3005-infinity/herdr-worker-orchestrator) — 通过 Herdr 管理的窗格，将任务派发给 CLI Agent worker（agy、codex 等）——支持有状态的任务追踪、工作树隔离和基于差异的评审。同时适用于 Claude Code 和 Herdr 的双用插件
- [elKei24/herdr-co-review](https://github.com/elKei24/herdr-co-review) — 在 herdr 中进行分屏 PR 评审——你的 Agent 找出问题，你在 TUI 中于代码旁逐一裁定，最后由 Agent 发布你批准的内容
- [itisbryan/herdr-gh-checks](https://github.com/itisbryan/herdr-gh-checks) — herdr 插件：在窗格中监视并查看当前 PR 的 CI，并在侧边栏行中显示 CI/合并状态。使用 Go + Bubble Tea 编写
- [mikhail-angelov/herdr-review-loop](https://github.com/mikhail-angelov/herdr-review-loop) — 在 herdr 工作区中让 Agent 之间自动进行交叉评审——一个负责编写，另一个负责评审，如此反复
- [tomasvarga/herdr-sniffr](https://github.com/tomasvarga/herdr-sniffr) — 在你审查之前，AI 先嗅探你的 PR 有没有问题——一个 Agent 化的初审，将草稿评论投放到 tuicr。不限定 Agent（codex/claude/cursor/grok/…）
- [moneycaringcoder/herdr-collide](https://github.com/moneycaringcoder/herdr-collide) — 当在同一仓库不同 git 工作树中工作的 Agent 即将发生冲突时发出警告——并判断它们的修改只是重叠还是会真正产生冲突
- [neospeed83/herdr-tournament](https://github.com/neospeed83/herdr-tournament) — 面向 Herdr 的对抗式多 Agent 代码评审
- [krzysztoff1/herdr-cull](https://github.com/krzysztoff1/herdr-cull) — 查看并关闭 herdr 中闲置的 Agent 窗格——fzf 多选，未经确认绝不关闭
- [ubuntudroid/herdr-coder-sessions](https://github.com/ubuntudroid/herdr-coder-sessions) — 在 herdr 中浏览正在运行的 Coder Agent 会话，并将每个会话作为独立工作区打开——通过 agentty 连接到该会话，其更改会被镜像到本地工作树中以供评审

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-forge"></a>

## GitHub / issue 跟踪工具集成

> 想以 issue 或 PR 为起点开始工作，并追踪 PR 状态

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**ghzinga**](https://github.com/osolmaz/ghzinga)<br><sub>osolmaz</sub> | 用于查看单个 GitHub issue 或 PR 的简易可点击 TUI，用 Rust 编写 | `rust` | 84 | 🔄 2026-09-06 |
| [**herdr-plugin-gh-pr**](https://github.com/wyattjoh/herdr-plugin-gh-pr)<br><sub>wyattjoh</sub> | 在侧边栏显示当前聚焦 Agent 窗格所在分支的 GitHub PR 状态的 herdr 插件 | `typescript` | 22 | 2026-07-16 |
| [**herdr-plugin-github-start**](https://github.com/ogulcancelik/herdr-plugin-github-start)<br><sub>ogulcancelik</sub> | 从 GitHub issue、PR 或讨论中启动 Codex 或 Claude 的 Herdr 插件 | `javascript` | 17 | 🔄 2026-08-31 |
| [**herdr-worktree-from-linear**](https://github.com/tdi/herdr-worktree-from-linear)<br><sub>tdi</sub> | 从 Linear issue 创建 git 工作树，并作为 herdr 工作区打开 | `javascript` | 14 | 🔄 2026-09-02 |
| [**herdr-jira**](https://github.com/a2u/herdr-jira)<br><sub>a2u</sub> | herdr 的 Jira TUI 插件——通过可配置的 JQL 过滤器浏览、搜索 issue，修改状态，并一键将 issue 交给终端中运行的 AI Agent 处理 | `ai-agents` `jira` `ratatui` `rust` `tui` | 12 | 🔄 2026-09-05 |
| [**herdr-pr-tracker**](https://github.com/Matovidlo/herdr-pr-tracker)<br><sub>Matovidlo</sub> | herdr 插件：追踪每个 Claude Code 会话产生的 GitHub PR，附带 gh 状态和操作 | `claude-code` `shell` | 12 | 2026-08-12 |
| [**herdr-linear**](https://github.com/JacquesvanWyk/herdr-linear)<br><sub>JacquesvanWyk</sub> | 在 herdr 分屏窗格或标签页中运行的 fzf 驱动 Linear 面板：搜索 issue、深入项目、创建 issue、修改状态 | `shell` | 8 | 2026-07-12 |
| [**herdr-git-status**](https://github.com/krystof018/herdr-git-status)<br><sub>krystof018</sub> | 在 herdr 内呈现 CI 状态——同时支持 GitLab（流水线+合并请求）和 GitHub（Actions+拉取请求），根据仓库的 origin 自动识别 | `bash` `ci-cd` `ci-status` `developer-tools` `github-actions` | 5 | 2026-07-01 |
| [**herdr-linear**](https://github.com/talent-factory/herdr-linear)<br><sub>talent-factory</sub> | 面向 Herdr 的 Linear issue 面板，按 Enter 即可开始实现 | `rust` | 4 | 2026-08-21 |
| [**herdr-pr-board**](https://github.com/cdowell09/herdr-pr-board)<br><sub>cdowell09</sub> | 面向 Herdr 的可配置跨仓库 GitHub 拉取请求仪表盘 | `github` `tui` `go` | 3 | 🔄 2026-09-02 |
| [**herdr-co-review**](https://github.com/elKei24/herdr-co-review)<br><sub>elKei24</sub> | 在 herdr 中进行分屏 PR 评审——你的 Agent 找出问题，你在 TUI 中于代码旁逐一裁定，最后由 Agent 发布你批准的内容 | `cli` `code-review` `pull-request` `rust` `tui` | 3 | 🔄 2026-09-02 |
| [**herdr-gh-checks**](https://github.com/itisbryan/herdr-gh-checks)<br><sub>itisbryan</sub> | herdr 插件：在窗格中监视并查看当前 PR 的 CI，并在侧边栏行中显示 CI/合并状态。使用 Go + Bubble Tea 编写 | `bubbletea` `ci` `github-actions` `tui` `go` | 3 | 🔄 2026-08-25 |
| [**mergr**](https://github.com/jsmenzies/mergr)<br><sub>jsmenzies</sub> | 在 Herdr Space 侧边栏行中显示 GitHub 拉取请求状态 | `github-pull-requests` `rust` | 3 | 2026-07-30 |
| [**herdr-plugin-gh-workflow**](https://github.com/kkckkc/herdr-plugin-gh-workflow)<br><sub>kkckkc</sub> | 用于 GitHub workflow 的 Herdr 插件 | `javascript` | 3 | 2026-07-03 |
| [**herdr-beads**](https://github.com/hexsprite/herdr-beads)<br><sub>hexsprite</sub> | 在 Herdr 中 Ctrl+点击 beads 的 issue ID，即可在分屏窗格中打开其详情 | `beads` `issue-tracker` `terminal` `shell` | 2 | 2026-08-07 |
| [**🆕 herdr-wish**](https://github.com/MovieHolic-Plex/herdr-wish)<br><sub>MovieHolic-Plex</sub> | Herdr plugin. Make a wish and omo commits a PR. omo-10 opens 10 worktrees. | `omo` `wish` `javascript` | 2 | 🔄 2026-09-04 |
| [**herdr-sniffr**](https://github.com/tomasvarga/herdr-sniffr)<br><sub>tomasvarga</sub> | 在你审查之前，AI 先嗅探你的 PR 有没有问题——一个 Agent 化的初审，将草稿评论投放到 tuicr。不限定 Agent（codex/claude/cursor/grok/…） | `ai` `cli` `code-review` `pull-request` `tuicr` | 2 | 2026-07-14 |
| [**🆕 herdr-workspace-prs**](https://github.com/andrewbrannan/herdr-workspace-prs)<br><sub>andrewbrannan</sub> | 用于追踪工作区 GitHub 拉取请求的 Herdr 插件。 | `typescript` | 1 | 🔄 2026-09-04 |
| [**herdr-board**](https://github.com/bredebjorhovd/herdr-board)<br><sub>bredebjorhovd</sub> | 编程 Agent 排队并自主完成工作的地方——输入 GitHub issue，自主 Agent 在 herdr 窗格中运行，PR 评审会返回给编写它的那个 Agent | `rust` | 1 | 2026-08-14 |
| [**herdr-dashboard**](https://github.com/chouxcreams/herdr-dashboard)<br><sub>chouxcreams</sub> | herdr 工作区的 PR 状态仪表盘 TUI——一目了然地查看每个窗格对应的 PR 状态/CI/审查情况 | `dashboard` `github` `pull-requests` `ratatui` `rust` | 1 | 2026-07-28 |
| [**herdr-plugin-dotfiles-github-link-preview**](https://github.com/edmundmiller/herdr-plugin-dotfiles-github-link-preview)<br><sub>edmundmiller</sub> | 在侧边窗格中预览 GitHub issue 和拉取请求的 Herdr 插件 | `python` | 1 | 2026-06-23 |
| [**🆕 herdr-pr-watch**](https://github.com/maxguzenski/herdr-pr-watch)<br><sub>maxguzenski</sub> | Herdr plugin: GitHub PR status of each workspace and agent pane in the sidebar | `github-pull-requests` `python` | 1 | 🔄 2026-09-06 |
| [**worktender**](https://github.com/steig/worktender)<br><sub>steig</sub> | 一条命令，从 GitHub issue 直达在专属工作树中处理它的编程 Agent | `ai-agents` `claude-code` `coding-agents` `git-worktree` `golang` | 1 | 🔄 2026-08-26 |
| [**herdr-github-pr**](https://github.com/woshahua/herdr-github-pr)<br><sub>woshahua</sub> | 同步 GitHub PR 状态、检查、评审和评论的 Herdr 插件 | `github` `javascript` | 1 | 2026-08-21 |
| [**herdr-pr**](https://github.com/yelsed/herdr-pr)<br><sub>yelsed</sub> | 在 herdr 窗格中以待办事项形式显示等待你处理的拉取请求，全部通过 gh CLI 读取 | `rust` | 1 | 🔄 2026-08-29 |
| [**herdr-plugin-jira-pr**](https://github.com/abtris/herdr-plugin-jira-pr)<br><sub>abtris</sub> | herdr 插件：显示当前分支 PR 背后关联的 Jira issue，并在两者不一致时发出警告 | `github-pr` `jira` `shell` | 0 | 2026-08-04 |
| [**git-shepherd**](https://github.com/H3xept/git-shepherd)<br><sub>H3xept</sub> | 在每个 Herdr Space 旁以图标显示拉取请求状态（草稿/打开/已合并/已关闭） | `developer-tools` `github-cli` `tui` `javascript` | 0 | 2026-08-21 |
| [**herdr-spaces-pr-status**](https://github.com/jmarbutt/herdr-spaces-pr-status)<br><sub>jmarbutt</sub> | 在 herdr 空间中显示 GitHub 拉取请求状态，附带 Conductor 风格的 PR 看板 | `github-pull-request` `javascript` | 0 | 2026-08-01 |
| [**herdr-pr-preview**](https://github.com/juninaba/herdr-pr-preview)<br><sub>juninaba</sub> | 在分屏窗格中预览当前分支的 GitHub 拉取请求的 Herdr 插件 | `shell` | 0 | 2026-07-08 |
| [**🆕 herdr-plugin-github-status**](https://github.com/jwanga/herdr-plugin-github-status)<br><sub>jwanga</sub> | herdr plugin: a real-time GitHub project status pane (milestones, issues, PRs, Actions) docked on the right at sidebar width | `github` `rust` `tui` | 0 | 🔄 2026-09-04 |
| [**github-issue-herdr-plugin**](https://github.com/nyanyaon/github-issue-herdr-plugin)<br><sub>nyanyaon</sub> | 用于「牧养」GitHub issue 的 Claude Code 插件 | `rust` | 0 | 2026-07-27 |
| [**herdr-gh-issue-label**](https://github.com/polidog/herdr-gh-issue-label)<br><sub>polidog</sub> | 在 Herdr 的 space 中显示与分支对应的 GitHub issue 编号和标题的插件 | `github-issues` `shell` | 0 | 🔄 2026-08-28 |
| [**herdr-pr-tab-renamer**](https://github.com/ralphilius/herdr-pr-tab-renamer)<br><sub>ralphilius</sub> | 根据检测到的拉取请求编号重命名标签页的 Herdr 插件 | `javascript` | 0 | 2026-08-03 |
| [**herdr-worktree-from-gitlab**](https://github.com/snics/herdr-worktree-from-gitlab)<br><sub>snics</sub> | herdr 插件：从 GitLab issue（通过 glab）创建 git 工作树和工作区 | `gitlab` `rust` `worktree` | 0 | 2026-07-09 |
| [**herdr-pr-workflow**](https://github.com/tamdogood/herdr-pr-workflow)<br><sub>tamdogood</sub> | 促使聚焦中的 Agent 安全地创建或合并当前分支拉取请求的 Herdr 操作 | `javascript` | 0 | 2026-08-10 |

<details><summary>与此目的也相关</summary>

- [tomasvarga/herdr-pickr](https://github.com/tomasvarga/herdr-pickr) — herdr 的 PR 审查路由器——按住 Ctrl 点击 GitHub PR / GitLab MR 链接，选择审查工具（tuicr · hunk · diff · 浏览器 · 或自定义工具），可选启用 AI 初审
- [tdi/herdr-worktree-from-pr](https://github.com/tdi/herdr-worktree-from-pr) — 从 GitHub PR 创建 git 工作树，并作为 herdr 工作区打开
- [jakekroon/herdr-pr-tracker](https://github.com/jakekroon/herdr-pr-tracker) — 将你所创建的所有未关闭拉取请求以停靠面板形式展示，并按你需要处理的紧迫程度进行颜色标注。一个 Herdr 插件
- [kiitosu/herdr-jira-board](https://github.com/kiitosu/herdr-jira-board) — 在 herdr 中运行的 Jira 看板，附带 Claude Code 会话启动器
- [ukwhatn/taskherd](https://github.com/ukwhatn/taskherd) — 与 herdr Agent 会话、PR 和 Jira 工单相关联的任务看板
- [0xthc/herdr-plugin-pr-board](https://github.com/0xthc/herdr-plugin-pr-board) — 在 herdr 中处理当前仓库的 GitHub PR——在窗格中浏览，将选中的 PR 检出为工作树工作区，并安全地回收已合并的 PR
- [spiritsack/herdr-jira-worktree](https://github.com/spiritsack/herdr-jira-worktree) — herdr 插件：提示输入 Jira 工单，打开或复用对应的 git 工作树，并预填到全新的 Claude Code 会话中

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-layout"></a>

## 工作区与布局搭建

> 打开项目时，希望标签页、窗格和启动命令一次性就位

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-spreader**](https://github.com/yuk1ty/herdr-spreader)<br><sub>yuk1ty</sub> | 从一个 YAML 文件启动整套 herdr 工作区布局——标签页、窗格、命令，一次搞定 | `rust` | 103 | 2026-08-16 |
| [**dotfiles**](https://github.com/lararosekelley/dotfiles)<br><sub>lararosekelley</sub> | 面向 Bash shell 使用而准备的个人 dotfiles | `bash` `bootstrap` `dotfiles` `homebrew` `macos` | 51 | 🔄 2026-09-06 |
| [**herdr-plugin-workspace-manager**](https://github.com/razajamil/herdr-plugin-workspace-manager)<br><sub>razajamil</sub> | 声明式的标签页/窗格布局，创建工作树时自动应用每个工作区的默认设置 | `rust` | 38 | 🔄 2026-08-23 |
| [**seshagy**](https://github.com/lmilojevicc/seshagy)<br><sub>lmilojevicc</sub> | 面向 tmux 和 herdr 的 Agent 感知会话管理器——发现项目、启动会话、追踪 AI Agent 的工作 | `bubbletea` `go` `session-management` `session-manager` `terminal` | 17 | 2026-08-20 |
| [**herdr-grid**](https://github.com/thuanlm215/herdr-grid)<br><sub>thuanlm215</sub> | 面向 Herdr 的可视化窗格布局编辑器，支持拖放、新建 shell、均衡分屏、固定预设和安全的工作区创建 | `layout-presets` `pane-layout` `productivity` `ratatui` `rust` | 6 | 🔄 2026-09-04 |
| [**herdr-warp**](https://github.com/HexSleeves/herdr-warp)<br><sub>HexSleeves</sub> | 将 Herdr 工作区作为原生 Warp 窗格打开 | `shell` | 4 | 2026-07-25 |
| [**herdr-muster**](https://github.com/marcoskichel/herdr-muster)<br><sub>marcoskichel</sub> | 面向 herdr 的、感知 Agent 状态的项目切换器 | `rust` | 4 | 2026-07-03 |
| [**herdr-layout-tools**](https://github.com/edouard-andrei/herdr-layout-tools)<br><sub>edouard-andrei</sub> | herdr 插件：原地重塑布局（主窗格居左+网格）并均分——标签页 ID 和窗格 ID 保持不变，进程也得以保留 | `javascript` | 3 | 2026-08-06 |
| [**herdr-pane-layouts**](https://github.com/iurysza/herdr-pane-layouts)<br><sub>iurysza</sub> | 面向 Herdr 的无缝 tmux 风格窗格调整大小和布局 | `pane-layout` `python` `terminal` | 3 | 2026-07-17 |
| [**herdr-setup-bootstrap**](https://github.com/shizlie/herdr-setup-bootstrap)<br><sub>shizlie</sub> | 根据 worktree_init.toml 初始化新工作树的 Herdr 插件 | `shell` | 3 | 2026-06-17 |
| [**dsh-plugin-herdr**](https://github.com/sunny0826/dsh-plugin-herdr)<br><sub>sunny0826</sub> | 面向 DeepSeek Harness（DSH）的 Herdr 控制平面插件——从 DSH 会话中观察并驱动 Herdr（面向 AI 编程 Agent 的终端工作区管理器） | `dsh-plugin` `typescript` | 3 | 🔄 2026-08-25 |
| [**herdr-google-gmail**](https://github.com/Tomatio13/herdr-google-gmail)<br><sub>Tomatio13</sub> | herdr-google-gmail 是面向终端工作区工具 herdr 的 Gmail 集成插件 | `shell` | 3 | 2026-07-22 |
| [**herdr-clone-layout**](https://github.com/danilolucasmd/herdr-clone-layout)<br><sub>danilolucasmd</sub> | 将你当前的工作区布局克隆到每个新的 herdr 工作树。无需模板、无需配置——你当前所在的布局本身就是模板 | `shell` | 2 | 🔄 2026-08-27 |
| [**herdr-fork-from-message**](https://github.com/dmangla3/herdr-fork-from-message)<br><sub>dmangla3</sub> | 从更早的一条消息处分叉出 Codex 或 Claude Code，并在新的 Herdr 标签页、窗格或工作区中打开 | `claude-code` `codex` `developer-tools` `terminal-multiplexer` `python` | 2 | 2026-08-10 |
| [**herdr-compose**](https://github.com/ropali/herdr-compose)<br><sub>ropali</sub> | herdr-compose 是面向 Herdr 的声明式工作区布局管理器 | `layout-manager` `python` | 2 | 2026-07-25 |
| [**herdr-google-calendar**](https://github.com/Tomatio13/herdr-google-calendar)<br><sub>Tomatio13</sub> | herdr-gog-calendar 是面向终端工作区工具 herdr 的 Google 日历集成插件 | `shell` | 2 | 2026-07-22 |
| [**herdr-layout**](https://github.com/3mmdrew/herdr-layout)<br><sub>3mmdrew</sub> | 面向 herdr 的极简工作区布局——输入一个 Lua 文件即可得到工作区。无依赖、无守护进程、无 YAML | `lua` `terminal` | 1 | 2026-08-04 |
| [**herdr-dwm-layout**](https://github.com/42lizard/herdr-dwm-layout)<br><sub>42lizard</sub> | 面向 Herdr 的 DWM 风格 master/stack 布局 | `dwm` `fzf` `rust` `shell` `tiling` | 1 | 🔄 2026-08-28 |
| [**herdr-medieval**](https://github.com/gabrielbarretoo/herdr-medieval)<br><sub>gabrielbarretoo</sub> | 将工作区和 Agent 以六边形中世纪大陆的形式进行 3D 展示的 Herdr 插件——每个工作区是一座围栏营地，每个窗格是一名冒险者，会根据 Agent 状态训练、在营火旁休息或在塔楼站岗。内嵌 three.js，无需联网、无依赖 | `3d` `hex-grid` `threejs` `javascript` | 1 | 2026-08-06 |
| [**herdr-spinup**](https://github.com/Royal-lobster/herdr-spinup)<br><sub>Royal-lobster</sub> | 每个新建 herdr 标签页的启动界面——选择一个工具，即会在该标签页中运行。工具通过 JSON 定义 | `javascript` | 1 | 2026-08-04 |
| [**reasonix-herdr**](https://github.com/uuie/reasonix-herdr)<br><sub>uuie</sub> | 在 Herdr 内提供实时生命周期报告和工作区控制的原生 Reasonix 插件 | `reasonix` `python` | 1 | 2026-07-10 |
| [**herdr-sesh**](https://github.com/xheisenbugx/herdr-sesh)<br><sub>xheisenbugx</sub> | 受 sesh 启发的智能 herdr 工作区管理器 | `go` | 1 | 2026-08-21 |
| [**herdr-workspace**](https://github.com/zackshen/herdr-workspace)<br><sub>zackshen</sub> | herdr 插件：从居中弹窗创建工作区并应用布局配置 | `rust` | 1 | 🔄 2026-08-24 |
| [**🆕 herdr-tab-command**](https://github.com/asermax/herdr-tab-command)<br><sub>asermax</sub> | 根据你给新标签页起的名字，自动启动 Agent 或运行相应命令。 | `typescript` | 0 | 🔄 2026-08-31 |
| [**🆕 herdr-tabline**](https://github.com/btj93/herdr-tabline)<br><sub>btj93</sub> | Render Herdr tab labels with safe templates and project-aware profiles. | `golang` `tabline` `terminal` `tui` `go` | 0 | 🔄 2026-09-04 |
| [**ccc-herdr-layout**](https://github.com/caoer/ccc-herdr-layout)<br><sub>caoer</sub> | 面向 herdr 的可视化布局选择器插件——一键操作，实时预览 | `go` | 0 | 2026-08-01 |
| [**herdr-yoke**](https://github.com/dgnsrekt/herdr-yoke)<br><sub>dgnsrekt</sub> | get yoked——一键将两个标签页并排显示，herdr 版的 Chrome 分屏视图 | `split-view` `terminal` `shell` | 0 | 2026-08-09 |
| [**🆕 herdr-plugin-dotfiles-dev-layout**](https://github.com/edmundmiller/herdr-plugin-dotfiles-dev-layout)<br><sub>edmundmiller</sub> | 用于打开我的 dotfiles 开发工作区布局的 Herdr 插件 | `python` | 0 | 2026-06-23 |
| [**herdr-notebook**](https://github.com/goofansu/herdr-notebook)<br><sub>goofansu</sub> | 每个工作区一个永久的 Markdown 笔记本，在活动窗格上方用你的编辑器打开 | `python` | 0 | 2026-08-20 |
| [**herdr-follow-cwd**](https://github.com/hasuwini77/herdr-follow-cwd)<br><sub>hasuwini77</sub> | herdr 插件：工作区标签会跟随其窗格实际所在的目录 | `javascript` | 0 | 2026-08-13 |
| [**herdr-pane-id-metadata**](https://github.com/limars874/herdr-pane-id-metadata)<br><sub>limars874</sub> | 用于规范化窗格 ID 和精简标签页/窗格侧边栏元数据的最小化 Herdr 插件 | `coding-agents` `terminal` `javascript` | 0 | 2026-08-17 |
| [**🆕 herdr-namesync**](https://github.com/oddurs/herdr-namesync)<br><sub>oddurs</sub> | Keeps herdr workspace, tab and agent names in step with the work as it changes — and holds off when it shouldn't. Works with no model; can use one when you wan… | `claude-code` `cli` `developer-tools` `terminal` `javascript` | 0 | 🔄 2026-09-07 |
| [**herdr-lastfocus**](https://github.com/pedrobarco/herdr-lastfocus)<br><sub>pedrobarco</sub> | herdr 的 tmux 风格「上一个活跃」窗格/标签页/工作区切换——通过聚焦事件历史守护进程实现 | `terminal-multiplexer` `tmux` `go` | 0 | 2026-07-25 |
| [**herdr-workspace-description**](https://github.com/rstacruz/herdr-workspace-description)<br><sub>rstacruz</sub> | _(暂无描述)_ | `typescript` | 0 | 2026-08-08 |
| [**herdr-active-agent-jump**](https://github.com/shoaibkhanz/herdr-active-agent-jump)<br><sub>shoaibkhanz</sub> | herdr 插件：按布局顺序前后循环聚焦正在进行中（工作中/被阻塞）的 Agent——作为 attention-jump 的 vim 风格补充 | `javascript` | 0 | 2026-07-12 |
| [**herdr-dev-layout**](https://github.com/simoncrypta/herdr-dev-layout)<br><sub>simoncrypta</sub> | 面向 Herdr 的常驻 Agent 窗格 | `herdr-integration` `shell` | 0 | 2026-08-20 |

<details><summary>与此目的也相关</summary>

- [andrewchng/herdr-sessionizer](https://github.com/andrewchng/herdr-sessionizer) — 通过模糊搜索打开项目和工作树，再从声明式 TOML 布局（标签页、窗格分割、命令、按仓库覆盖配置）启动工作区
- [fullerzz/herdr-plugin-sesh](https://github.com/fullerzz/herdr-plugin-sesh) — 面向 Herdr 的 Sesh 风格工作区选择器 TUI，集成 zoxide，可从常用目录创建工作区
- [ntindle/herdr-resurrect](https://github.com/ntindle/herdr-resurrect) — herdr 的 tmux-resurrect——快照工作区、标签页、窗格、当前目录、运行中的程序和 Agent，并在崩溃或重启后恢复
- [enekos/herdr-quick-actions](https://github.com/enekos/herdr-quick-actions) — 以 fzf 选择器调用 herdr 原生的标签页/窗格/工作区操作，按使用频率排序——不必再死记快捷键
- [salkhalil/herdr-sessionizer](https://github.com/salkhalil/herdr-sessionizer) — herdr 的 tmux-sessionizer：用 fzf 搜索已打开的工作区和 zoxide 目录，创建或聚焦并附带模板标签页
- [crierr/herdr-arrange](https://github.com/crierr/herdr-arrange) — 用于 herdr 窗格移动/交换/重新分屏/布局调整的交互式弹窗 UI
- [aliou/herdr-cast](https://github.com/aliou/herdr-cast) — 个人 Herdr 插件——提供原生 macOS Agent 通知、模糊工作区导航、基于 zoxide 的工作区创建以及布局命令
- [42lizard/herdr-sessionizer](https://github.com/42lizard/herdr-sessionizer) — tmux-sessionizer 风格的 herdr 插件
- [chandrasekharan98/herdr-workspace-save](https://github.com/chandrasekharan98/herdr-workspace-save) — 保存 Herdr 工作区（布局、工作目录、Agent 会话、正在运行的命令），之后可从 fzf 选择器中重新打开
- [asermax/herdr-suspend-workspace](https://github.com/asermax/herdr-suspend-workspace) — 挂起 herdr 工作区——将布局和 Agent 快照后关闭，之后可从弹出选择器中恢复
- [willfish/herdr-workspacex](https://github.com/willfish/herdr-workspacex) — Rust 原生的模糊 Herdr 工作区切换器，支持基于 zoxide 的工作区创建

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-navigate"></a>

## 窗格导航与快捷键

> 想用和编辑器一样的快捷键在窗格、工作区之间移动和调整大小

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**vim-herdr-navigation**](https://github.com/paulbkim-dev/vim-herdr-navigation)<br><sub>paulbkim-dev</sub> | 用 Ctrl+h/j/k/l 在 herdr 窗格与 Vim/Neovim 分屏之间无缝导航——vim-tmux-navigator 的 herdr 移植版 | `neovim` `vim` `shell` | 101 | 2026-08-23 |
| [**herdr-splits.nvim**](https://github.com/lmilojevicc/herdr-splits.nvim)<br><sub>lmilojevicc</sub> | 面向 Herdr 和 Neovim 的智能分屏导航与调整大小 | `lua` `neovim` `neovim-plugin` `neovim-plugins` `nvim` | 57 | 2026-08-17 |
| [**herdr-floax**](https://github.com/Tyru5/herdr-floax)<br><sub>Tyru5</sub> | herdr 的浮动临时终端——类似 tmux-floax 风格的可切换弹窗，每个工作区一个，会话持久保存 | `rust` `terminal` `tmux-floax` | 24 | 2026-07-26 |
| [**herdr-nvim-nav**](https://github.com/aimdevlee/herdr-nvim-nav)<br><sub>aimdevlee</sub> | 在 herdr 窗格与 Neovim 分屏之间无缝使用 Ctrl+h/j/k/l——基于 socket，无需每次按键都启动进程 | `neovim` `neovim-plugin` `lua` | 18 | 2026-08-02 |
| [**herdr-last-workspace**](https://github.com/third774/herdr-last-workspace)<br><sub>third774</sub> | 用于切换回上一个聚焦的工作区的插件 | `rust` | 17 | 2026-06-22 |
| [**herdr-logbook**](https://github.com/Resetnak/herdr-logbook)<br><sub>Resetnak</sub> | 终端的工作记忆——离线、以 Markdown 为主的笔记、决策记录，以及 Herdr 的当前任务 now.md | `adr` `bubbletea` `cli` `go` `markdown` | 12 | 🔄 2026-09-03 |
| [**herdr-recent-navigator**](https://github.com/beyondlex/herdr-recent-navigator)<br><sub>beyondlex</sub> | 面向 Herdr 的最近工作区/标签页/窗格切换器。弹出窗口列出最近聚焦过的工作区、标签页、窗格和 AI Agent，支持模糊搜索和键盘导航 | `agent` `mru` `navigator` `pane` `popup` | 11 | 2026-07-28 |
| [**herdr-pane-mover**](https://github.com/osamahbeig/herdr-pane-mover)<br><sub>osamahbeig</sub> | herdr 的可点击浮层菜单：跨标签页和工作区移动、重新分割或交换窗格 | `terminal` `tui` `javascript` | 11 | 2026-07-10 |
| [**herdr-paddock**](https://github.com/neyham/herdr-paddock)<br><sub>neyham</sub> | 🐑 面向 herdr Agent 的卡片墙动态流——一览整个羊群，放大查看单个 Agent 并回复，全部通过普通 SSH 完成 | `bubbletea` `go` `ssh` `tui` | 10 | 🔄 2026-08-25 |
| [**herdr-command-center**](https://github.com/speardragon/herdr-command-center)<br><sub>speardragon</sub> | 一个快捷键统管所有命令——一个列出你注册命令的 herdr 弹窗，用方向键或数字执行，并在命令触发前自动关闭 | `command-palette` `nodejs` `terminal` `toml` `tui` | 10 | 2026-08-19 |
| [**herdr-equalize-panes**](https://github.com/shibayu36/herdr-equalize-panes)<br><sub>shibayu36</sub> | 在分屏和关闭时自动均分窗格大小的 herdr 插件（相当于自动执行 tmux 的 select-layout -E） | `terminal` `perl` | 9 | 2026-08-22 |
| [**herdr-trail**](https://github.com/catoncat/herdr-trail)<br><sub>catoncat</sub> | herdr 全局共享的备忘录——Agent 记下待跟进事项，人类通过一份全局列表统一管理，每条记录都可跳回其来源对话 | `javascript` | 8 | 🔄 2026-08-26 |
| [**herdr-cliamp**](https://github.com/coryshaw1/herdr-cliamp)<br><sub>coryshaw1</sub> | 面向 herdr 的浮动 cliamp，隐藏后仍会继续播放——播放器运行在一个分离的 herdr 会话中，因此关闭浮层只是分离而已 | `audiobook` `cliamp` `music-player` `podcast` `terminal` | 7 | 🔄 2026-08-24 |
| [**herdr-toggle-popup**](https://github.com/maro114510/herdr-toggle-popup)<br><sub>maro114510</sub> | 一个快捷键即可切换浮层弹窗终端的 Herdr 插件 | `go` | 7 | 2026-08-12 |
| [**nvim-herdr-navigation**](https://github.com/bojackduy/nvim-herdr-navigation)<br><sub>bojackduy</sub> | vim-tmux-navigator 风格的 ctrl+h/j/k/l，在 Neovim 分屏和 Herdr 窗格之间导航 | `keyboard-shortcuts` `lazyvim` `lua` `navigation` `neovim` | 6 | 2026-07-20 |
| [**herdr-swipe**](https://github.com/husniadil/herdr-swipe)<br><sub>husniadil</sub> | 面向 Herdr 的触控板手势——可在窗格、标签页和空间之间移动，并跳转到正在等待你的 Agent | `cgeventtap` `gestures` `macos` `python` `terminal` | 6 | 2026-08-20 |
| [**herdr-omnisearch**](https://github.com/dmnkf/herdr-omnisearch)<br><sub>dmnkf</sub> | 为 Herdr 工作区、窗格和已归档 Agent 会话提供快速本地搜索与导航 | `python` | 5 | 🔄 2026-08-31 |
| [**nvim-herdr-navigator**](https://github.com/kaar/nvim-herdr-navigator)<br><sub>kaar</sub> | 在 Neovim 分屏与 herdr 窗格之间无缝导航——一套 `ctrl+h/j/k/l` 按键即可同时穿梭于 vim 和 herdr 窗格 | `neovim` `neovim-plugin` `lua` | 5 | 2026-07-29 |
| [**herdr-last**](https://github.com/lmilojevicc/herdr-last)<br><sub>lmilojevicc</sub> | 切换回 Herdr 中上一个活动的工作区或标签页 | `go` `linux` `macos` `productivity` `tabs` | 5 | 2026-08-07 |
| [**herdr-scratch**](https://github.com/AkashJana18/herdr-scratch)<br><sub>AkashJana18</sub> | 面向 Herdr 的持久化速记板，为浮动实用窗格铺路 | `cli` `rust` `scratchpad` | 4 | 🔄 2026-08-30 |
| [**herdr-arrange**](https://github.com/crierr/herdr-arrange)<br><sub>crierr</sub> | 用于 herdr 窗格移动/交换/重新分屏/布局调整的交互式弹窗 UI | `go` | 4 | 🔄 2026-09-05 |
| [**herdr-annotations**](https://github.com/jagzmz/herdr-annotations)<br><sub>jagzmz</sub> | 通过快速的本地优先弹窗和可复用的收藏集，为 Herdr 中选中的终端文本添加注释 | `annotations` `cli` `coding-agents` `developer-tools` `local-first` | 4 | 2026-07-16 |
| [**herdr-harpoon**](https://github.com/KonstantinKai/herdr-harpoon)<br><sub>KonstantinKai</sub> | herdr 的 Harpoon：给窗格打标记，按编号跳转。纯 Bash 实现，无需构建 | `bash` `harpoon` `tmux-harpoon` `shell` | 4 | 2026-07-29 |
| [**herdr-equalize-splits**](https://github.com/markhuot/herdr-equalize-splits)<br><sub>markhuot</sub> | herdr 插件：将当前标签页中所有分屏按行/列均分尺寸（绑定到 Ctrl+b =） | `terminal` `tmux` `javascript` | 4 | 2026-07-08 |
| [**herdr-attention**](https://github.com/milkyskies/herdr-attention)<br><sub>milkyskies</sub> | herdr 插件：按一个键即可跳转到下一个需要关注的 Agent（先是被阻塞的，然后是已完成的） | `javascript` | 4 | 2026-07-08 |
| [**herdr-navigator**](https://github.com/willfish/herdr-navigator)<br><sub>willfish</sub> | 面向 Vim/Neovim 感知窗格移动的 Herdr 端导航操作 | `navigation` `neovim` `rust` | 4 | 2026-07-07 |
| [**herdr-tmux-layout**](https://github.com/crierr/herdr-tmux-layout)<br><sub>crierr</sub> | 面向运行中的 Herdr 窗格的 tmux 风格预设布局——支持 cycle、even-horizontal、even-vertical、main-horizontal、main-vertical、tiled 和 balance | `go` | 3 | 🔄 2026-08-30 |
| [**herdr-convo-index**](https://github.com/dzwduan/herdr-convo-index)<br><sub>dzwduan</sub> | herdr 中 Claude Code 窗格的轮次索引——跳转到任意历史轮次并在弹窗中查看 | `python` | 3 | 2026-07-27 |
| [**herdr-popupx**](https://github.com/jeromychu23/herdr-popupx)<br><sub>jeromychu23</sub> | 面向 Herdr 的持久化原生浮动速记弹窗 | `rust` `terminal` `tui` | 3 | 2026-07-21 |
| [**herdr-unread-marker**](https://github.com/JoanGil/herdr-unread-marker)<br><sub>JoanGil</sub> | 通过快捷键手动将聚焦中的 Agent 标记为已读/未读（仅支持手动） | `shell` | 3 | 2026-07-17 |
| [**herdr-confirm-close-pane**](https://github.com/poweroutlet2/herdr-confirm-close-pane)<br><sub>poweroutlet2</sub> | 在关闭窗格前询问确认的 herdr 插件，类似 tmux 的 prefix+x confirm-before | `shell` | 3 | 2026-07-06 |
| [**herdr-pretty-which**](https://github.com/ramarivera/herdr-pretty-which)<br><sub>ramarivera</sub> | 面向 Herdr 的 Rust/Ratatui which-key 风格快捷键浮层 | `ratatui` `rust` `terminal` `tui` `which-key` | 3 | 2026-08-14 |
| [**🆕 herdr-mission-control**](https://github.com/vjeantet/herdr-mission-control)<br><sub>vjeantet</sub> | herdr 的 Mission Control：按一个键，将工作区所有窗格按标签页分组，以实时平铺网格展示，选中即可切换过去。 | `expose` `mission-control` `terminal` `tui` `rust` | 3 | 🔄 2026-09-01 |
| [**herdr-voice**](https://github.com/aneym/herdr-voice)<br><sub>aneym</sub> | herdr 的语音控制——通过语音创建空间、拆分窗格并驱动编程 Agent。基于 OpenAI Realtime，带实时听写文本的浮动 HUD | `openai-realtime-api` `voice` `javascript` | 2 | 2026-08-01 |
| [**herdr-next-agent**](https://github.com/choplin/herdr-next-agent)<br><sub>choplin</sub> | 在处于所配置语义状态的 Herdr Agent 之间移动 | `go` | 2 | 🔄 2026-08-24 |
| [**herdr-equalize-vsplit**](https://github.com/devoc09/herdr-equalize-vsplit)<br><sub>devoc09</sub> | 将当前窗格向右分屏并均分列宽的 Herdr 插件 | `go` | 2 | 2026-07-15 |
| [**herdr-easymotion**](https://github.com/elliotekj/herdr-easymotion)<br><sub>elliotekj</sub> | 🦘 在 Herdr 窗格之间直接跳转 | `javascript` | 2 | 2026-07-20 |
| [**herdr-break-pane**](https://github.com/iuhoay/herdr-break-pane)<br><sub>iuhoay</sub> | 将聚焦窗格移动到新标签页的小型 Herdr 插件 | `pane` `javascript` | 2 | 🔄 2026-08-27 |
| [**herdr-prevtab**](https://github.com/joo-was-already-taken/herdr-prevtab)<br><sub>joo-was-already-taken</sub> | 切换到上一个聚焦标签页的 Herdr 插件 | `rust` | 2 | 🔄 2026-09-05 |
| [**herdr-lazytask**](https://github.com/mdetweil/herdr-lazytask)<br><sub>mdetweil</sub> | 在 herdr 分屏窗格中使用 Lazytask（打开/聚焦/切换），并提供 Taskwarrior 快捷操作 | `lazytask` `taskwarrior` `terminal` `rust` | 2 | 2026-08-02 |
| [**herdr-float**](https://github.com/meerzulee/herdr-float)<br><sub>meerzulee</sub> | 类似 Zellij 的 ALT+F 浮动窗格 | `shell` | 2 | 2026-07-20 |
| [**herdr-quotr**](https://github.com/napalmpapalam/herdr-quotr)<br><sub>napalmpapalam</sub> | 通过 herdr 弹窗，把 Agent 自己的回答引用后再丢回给它 | `claude-code` `rust` `tui` | 2 | 🔄 2026-09-01 |
| [**herdr-pane-mover**](https://github.com/ronly2460/herdr-pane-mover)<br><sub>ronly2460</sub> | 通过交互式方向键选择器，在工作区之间移动 Herdr 窗格 | `terminal` `workspace` `shell` | 2 | 🔄 2026-08-23 |
| [**herdr-pane-orientation-switcher**](https://github.com/sf1tzp/herdr-pane-orientation-switcher)<br><sub>sf1tzp</sub> | 面向 Herdr 分屏窗格的工作流人体工学优化 | `shell` | 2 | 2026-07-25 |
| [**herdr-ask-inbox**](https://github.com/speardragon/herdr-ask-inbox)<br><sub>speardragon</sub> | 将所有 herdr 工作区中被阻塞的 Claude AskUserQuestion 提示汇总到一个弹窗中，就地回答，绝不会把答案发错 Agent | `claude-code` `javascript` | 2 | 2026-07-25 |
| [**herdr-unread-jump**](https://github.com/to4iki/herdr-unread-jump)<br><sub>to4iki</sub> | 跳转到下一个需要关注的 Herdr Agent 窗格（先是被阻塞的，然后是已完成的） | `agents` `bash` `shell` | 2 | 🔄 2026-08-30 |
| [**herdr-plugin-ide-jump**](https://github.com/agentience/herdr-plugin-ide-jump)<br><sub>agentience</sub> | 快速回到你的 IDE——将聚焦窗格所属项目的编辑器窗口置顶，或从可筛选的弹窗中选择一个。一个 Herdr 插件 | `python` | 1 | 🔄 2026-08-24 |
| [**herdr-plugin-tiles**](https://github.com/carsonjones/herdr-plugin-tiles)<br><sub>carsonjones</sub> | 面向 herdr 的简易窗格管理器 | `python` | 1 | 2026-06-19 |
| [**herdr-notes**](https://github.com/cyperx84/herdr-notes)<br><sub>cyperx84</sub> | 面向 Herdr 的、按工作区独立的 Markdown 速记笔记，用 Go 编写 | `bubbletea` `golang` `markdown` `notes` `go` | 1 | 2026-08-16 |
| [**🆕 herdr-tab-jump**](https://github.com/cyperx84/herdr-tab-jump)<br><sub>cyperx84</sub> | 通过任意快捷键，按位置聚焦到 herdr 的第 N 个标签页——可以把数字键分配给标签页和工作区。 | `shell` | 1 | 🔄 2026-09-01 |
| [**herdr-last-tab**](https://github.com/dantehemerson/herdr-last-tab)<br><sub>dantehemerson</sub> | 用于切换回上一个聚焦的标签页的插件 | `rust` | 1 | 2026-08-12 |
| [**🆕 herdr-swipe-linux**](https://github.com/enisbu/herdr-swipe-linux)<br><sub>enisbu</sub> | 面向 Linux 上 Herdr 的触控板手势：滑动可在窗格、标签页和空间之间切换，轻点即可跳转到等待中的 Agent。 | `evdev` `gestures` `gnome` `hyprland` `linux` | 1 | 🔄 2026-09-02 |
| [**herdr-nav-history**](https://github.com/jugyo/herdr-nav-history)<br><sub>jugyo</sub> | 面向 herdr 的浏览器风格前进/后退导航（针对窗格、标签页、工作区的聚焦历史） | `javascript` | 1 | 2026-07-12 |
| [**herdr-plugin-switcher**](https://github.com/KadenThomp36/herdr-plugin-switcher)<br><sub>KadenThomp36</sub> | 按住 Ctrl，点按 Tab 即可按最近使用顺序循环切换 herdr 窗格。面向 macOS 版 herdr 的 Arc/Zen 风格窗格切换器 | `swift` | 1 | 2026-08-21 |
| [**herdr-nvim-aware**](https://github.com/KoalaVim/herdr-nvim-aware)<br><sub>KoalaVim</sub> | 面向 herdr 的 Nvim 感知快捷键——支持导航、分屏、关闭、缩放 | `rust` | 1 | 2026-08-20 |
| [**herdr-plugin-last**](https://github.com/m4salah/herdr-plugin-last)<br><sub>m4salah</sub> | 为 Herdr 提供 tmux 风格的上一个标签页/上一个工作区跳转 | `rust` | 1 | 2026-07-30 |
| [**herdr-scratch**](https://github.com/macintacos/herdr-scratch)<br><sub>macintacos</sub> | 面向 herdr 的速记 shell——通过一个组合键开关的弹窗。底层基于 tmux，因此再次打开时会与离开时一模一样 | `go` | 1 | 🔄 2026-08-28 |
| [**herdr-normal-mode**](https://github.com/maedana/herdr-normal-mode)<br><sub>maedana</sub> | 面向 herdr 侧边栏的 Vim 风格普通模式——j/k 移动行，h/l 切换标签页，0-9 选择窗格 | `rust` `tui` | 1 | 🔄 2026-08-24 |
| [**herdr-next-agent**](https://github.com/martin-ro/herdr-next-agent)<br><sub>martin-ro</sub> | Herdr 插件：按可配置的状态优先级，跳转到下一个需要关注的 Agent | `python` | 1 | 2026-07-15 |
| [**herdr-touchbar**](https://github.com/omerturhan/herdr-touchbar)<br><sub>omerturhan</sub> | 在 MacBook Touch Bar 上显示工作中和被阻塞的 herdr Agent——点按即可直接跳转到对应标签页 | `ai-agents` `macos` `touchbar` `swift` | 1 | 2026-07-30 |
| [**herdr-deck-navigation**](https://github.com/raghu-nandan-bs/herdr-deck-navigation)<br><sub>raghu-nandan-bs</sub> | 将 herdr 内置的扁平化工作区/标签页/窗格导航器，替换为无需滚动即可快速到达任意窗格的「Deck」视图 | `rust` `terminal` `tui` | 1 | 🔄 2026-08-24 |
| [**herdr-account-switch**](https://github.com/rcosteira79/herdr-account-switch)<br><sub>rcosteira79</sub> | 无需重新认证即可热切换 Claude Code / Codex 登录。提供浮层选择器、切换到下一个的快捷键，以及按窗格显示的账号徽章（$acct） | `python` | 1 | 🔄 2026-09-05 |
| [**herdr-smartnav**](https://github.com/retroaalto/herdr-smartnav)<br><sub>retroaalto</sub> | 为 Herdr 提供方向感知窗格导航的插件 | `go` | 1 | 2026-08-01 |
| [**herdr-edge-nav**](https://github.com/sebcbi1/herdr-edge-nav)<br><sub>sebcbi1</sub> | 在窗格边缘可跨标签页、跨工作区进行方向性移动/调整大小的 Herdr 插件，并能无缝识别 Neovim 分屏 | `lua` | 1 | 2026-08-12 |
| [**herdr-ferry**](https://github.com/shadowfax92/herdr-ferry)<br><sub>shadowfax92</sub> | 可批量移动运行中的 Herdr 窗格和标签页，或合并工作区的 Rust 原生弹窗 | `productivity` `rust` `terminal` `tui` | 1 | 2026-08-19 |
| [**herdr-scratch**](https://github.com/shadowfax92/herdr-scratch)<br><sub>shadowfax92</sub> | 由私有 tmux 会话支撑的、按窗格持久化的 Herdr 便签弹窗 | `neovim` `productivity` `rust` `terminal` `tmux` | 1 | 2026-08-04 |
| [**herdr-talon**](https://github.com/shadowfax92/herdr-talon)<br><sub>shadowfax92</sub> | 为可见的 Herdr 终端目标显示空间化的键盘提示 | `keyboard-navigation` `productivity` `rust` `terminal` `tmux-fingers` | 1 | 2026-08-20 |
| [**herdr-nav-plus**](https://github.com/shoaibkhanz/herdr-nav-plus)<br><sub>shoaibkhanz</sub> | Ctrl+h/j/k/l 导航可以跨越 herdr 窗格直达工作区——感知 vim 行为，两端可循环 | `javascript` | 1 | 2026-07-18 |
| [**herdr-hintr**](https://github.com/wraithyy/herdr-hintr)<br><sub>wraithyy</sub> | herdr 插件：which-key 风格的快捷键速查表弹窗——按下按键即可直接执行 | `shell` | 1 | 2026-08-11 |
| [**herdr-notes**](https://github.com/0xfelixli/herdr-notes)<br><sub>0xfelixli</sub> | 在 Rust 编写的弹窗文本框中为选中的终端文本添加注释——herdr 插件 | `rust` `terminal` | 0 | 🔄 2026-08-27 |
| [**herdr-popup**](https://github.com/abelfubu/herdr-popup)<br><sub>abelfubu</sub> | 用于执行临时 shell 命令的通用 Herdr 弹窗窗格插件 | `shell` | 0 | 2026-08-21 |
| [**🆕 herdr-plugin-echo**](https://github.com/andischerer/herdr-plugin-echo)<br><sub>andischerer</sub> | 将一个窗格中的按键广播到多个已标记窗格的 Herdr 插件 | `typescript` | 0 | 🔄 2026-08-23 |
| [**🆕 herdr-hyprland**](https://github.com/aorumbayev/herdr-hyprland)<br><sub>aorumbayev</sub> | 受 Hyprland 启发，为 herdr 带来的操作方式。 | `ai-agents` `developer-tools` `golang` `hyprland` `keybindings` | 0 | 🔄 2026-09-04 |
| [**gotopr**](https://github.com/asumaran/gotopr)<br><sub>asumaran</sub> | 跨本地仓库和工作树跳转到你打开的 GitHub PR 的 Herdr 插件 | `go` | 0 | 2026-08-23 |
| [**herdr-confirm-close**](https://github.com/asumaran/herdr-confirm-close)<br><sub>asumaran</sub> | herdr 插件：关闭聚焦窗格时，仅当其中有进程正在运行时才会询问确认 | `terminal` `go` | 0 | 2026-08-23 |
| [**🆕 herdr-dup-tab**](https://github.com/bonkey/herdr-dup-tab)<br><sub>bonkey</sub> | Herdr plugin: duplicate the focused pane's running command into a new tab | `shell` | 0 | 🔄 2026-09-06 |
| [**herdr-auto-focus**](https://github.com/calorie/herdr-auto-focus)<br><sub>calorie</sub> | 当 macOS 输入闲置后，自动聚焦到需要关注的 Herdr Agent | `golang` `macos` `go` | 0 | 2026-07-27 |
| [**herdr-split-pane**](https://github.com/choplin/herdr-split-pane)<br><sub>choplin</sub> | 在 Herdr 分屏窗格中直接打开调用方指定的命令 | — | 0 | 🔄 2026-08-24 |
| [**herdr-nav**](https://github.com/codingfragments/herdr-nav)<br><sub>codingfragments</sub> | herdr 工作区与窗格导航——herdr-navigation 的现代版，改进了预览支持并新增工作区模板处理 | `html` | 0 | 🔄 2026-08-27 |
| [**herdr-which-key**](https://github.com/CowboyVang/herdr-which-key)<br><sub>CowboyVang</sub> | 面向 herdr 的 which-key 风格键位映射浮层——按一个键即可看到 prefix 下所有按键绑定的分组和标签，再按第二个键即可执行。需主动呼出，而非长按显示。零依赖 | `keybindings` `terminal` `which-key` `python` | 0 | 2026-08-02 |
| [**🆕 herdr-agent-numbers**](https://github.com/DillonWall/herdr-agent-numbers)<br><sub>DillonWall</sub> | 为 herdr 的 Agent 面板编号，与 focus_agent（前缀+1..9）保持一致。 | `terminal-multiplexer` `shell` | 0 | 🔄 2026-09-01 |
| [**🆕 herdr-drover**](https://github.com/followbl/herdr-drover)<br><sub>followbl</sub> | Herdr 的「牧羊犬」标签页切换器：按住 Super+T 循环浏览标签页，松开即切换到当前标签页。 | `linux` `python` | 0 | 🔄 2026-09-03 |
| [**herdr-plugin-agents-usage**](https://github.com/gecm0/herdr-plugin-agents-usage)<br><sub>gecm0</sub> | 在 Herdr 的模态弹窗中显示各服务商的使用情况（Claude、Codex、OpenCode Go、Neuralwatt） | `claude` `codex` `opencode` `terminal` `usage` | 0 | 2026-07-26 |
| [**herdr-desktop-switcher**](https://github.com/gustavocaiano/herdr-desktop-switcher)<br><sub>gustavocaiano</sub> | 面向 Herdr 的实验性 macOS 桌面切换器 | `rust` | 0 | 🔄 2026-08-26 |
| [**herdr-harpoon**](https://github.com/hadeson/herdr-harpoon)<br><sub>hadeson</sub> | herdr 的 Harpoon 风格窗格标记：将窗格固定到 1-9 号槽位，跨标签页和工作区直接跳转 | `harpoon` `pane-navigation` `terminal` `tmux` `python` | 0 | 2026-07-25 |
| [**herdr-counting-sheep**](https://github.com/inonprince/herdr-counting-sheep)<br><sub>inonprince</sub> | Herdr 的 Space 与 Agent 实时索引，并提供跳转到上一个标签页、Space 或 Agent 的快捷键 | `productivity` `terminal` `javascript` | 0 | 2026-08-03 |
| [**🆕 bindr**](https://github.com/itsmistermoon/bindr)<br><sub>itsmistermoon</sub> | Herdr plugin for switching between named keybinding profiles and viewing/editing keybinds in a popup. | `rust` | 0 | 🔄 2026-09-04 |
| [**herdr-matter-wall**](https://github.com/Javamomma/herdr-matter-wall)<br><sub>Javamomma</sub> | herdr 插件：将项目中最活跃的子目录以只读 AI 状态卡片墙的形式平铺展示 | `claude-code` `shell` | 0 | 2026-07-14 |
| [**herdr-nav**](https://github.com/jmarcelomb/herdr-nav)<br><sub>jmarcelomb</sub> | 面向 herdr 的窗格、标签页与工作区导航插件 | `rust` | 0 | 2026-07-30 |
| [**herdr-positional-tabs**](https://github.com/juezhong/herdr-positional-tabs)<br><sub>juezhong</sub> | 面向 Herdr 的稳定位置标签页标签与 Alt+数字导航 | `rust` `terminal` | 0 | 🔄 2026-08-30 |
| [**herdr-last-tab**](https://github.com/k-narusawa/herdr-last-tab)<br><sub>k-narusawa</sub> | _(暂无描述)_ | `shell` | 0 | 2026-08-22 |
| [**herdr-hasr**](https://github.com/KazBrekker1/herdr-hasr)<br><sub>KazBrekker1</sub> | Hasr（حصر——意为「枚举、完整清点」）——herdr 的 goto 风格弹窗切换器：切换、重命名、删除并创建 Agent、标签页和空间，并实时追踪完成状态 | `tui` `go` | 0 | 2026-07-23 |
| [**🆕 herdr-focus-attention**](https://github.com/kuwa72/herdr-focus-attention)<br><sub>kuwa72</sub> | Herdr plugin: cycle through agents needing attention | `python` | 0 | 🔄 2026-09-05 |
| [**herdr-cmd-marks**](https://github.com/leonho/herdr-cmd-marks)<br><sub>leonho</sub> | herdr 插件：按项目管理的命令收藏弹窗。即使 Agent 正忙，也能在独立 shell 中运行已收藏的命令（支持全局、项目和智能分组） | `shell` | 0 | 2026-07-18 |
| [**herdr-reshape**](https://github.com/macintacos/herdr-reshape)<br><sub>macintacos</sub> | 将聚焦窗格在其标签页内移动，并把整个标签页整理成均匀网格的 herdr 插件 | `go` | 0 | 🔄 2026-09-04 |
| [**herdr-pane-balancer**](https://github.com/malone-c/herdr-pane-balancer)<br><sub>malone-c</sub> | 在窗格打开和关闭时，让 herdr 窗格始终保持均匀大小。分屏会将聚焦窗格减半，本插件会重新平衡整个标签页 | `python` | 0 | 2026-08-07 |
| [**herdr-focus-or-tab**](https://github.com/mholtzscher/herdr-focus-or-tab)<br><sub>mholtzscher</sub> | 跨标签页边界循环切换 Herdr 窗格 | `terminal-multiplexer` `rust` | 0 | 2026-07-31 |
| [**🆕 herdr-plugin-recent-spaces**](https://github.com/mike-bronner/herdr-plugin-recent-spaces)<br><sub>mike-bronner</sub> | Herdr 插件：让空间侧边栏始终按最近使用顺序排列。 | `python` | 0 | 🔄 2026-09-02 |
| [**herdr-plugins**](https://github.com/oullin/herdr-plugins)<br><sub>oullin</sub> | 面向 Herdr 的一组专注、可独立安装的插件合集 | `typescript` | 0 | 2026-08-09 |
| [**🆕 herdr-plugin-agent-attention**](https://github.com/peterwiebe/herdr-plugin-agent-attention)<br><sub>peterwiebe</sub> | Herdr plugin to jump to the most recent blocked or finished agent | `python` | 0 | 🔄 2026-09-04 |
| [**herdr-equalize-panes**](https://github.com/ponko2/herdr-equalize-panes)<br><sub>ponko2</sub> | 在窗格被创建、关闭、移动或退出时，自动保持每个标签页内的窗格大小均匀 | `rust` | 0 | 🔄 2026-09-06 |
| [**herdr-focused-codex-fork**](https://github.com/potatoQi/herdr-focused-codex-fork)<br><sub>potatoQi</sub> | 将聚焦中的 Herdr 窗格里的 Codex 会话分叉到右侧窗格 | `shell` | 0 | 2026-08-09 |
| [**herdr-whichkey**](https://github.com/Qu4tro/herdr-whichkey)<br><sub>Qu4tro</sub> | herdr 的 blezz/which-key 风格操作菜单——按下触发键后，每个操作只需一次按键，无需输入，无需回车 | `rust` | 0 | 2026-07-22 |
| [**herdr-close-other-panes**](https://github.com/reobin/herdr-close-other-panes)<br><sub>reobin</sub> | herdr 版的 vim ctrl-w o——关闭除聚焦窗格外的所有窗格 | `shell` | 0 | 🔄 2026-08-25 |
| [**herdr-pane-equalizer**](https://github.com/shanefully-done/herdr-pane-equalizer)<br><sub>shanefully-done</sub> | 将 herdr 窗格调整为均匀大小，支持自动或手动执行 | `javascript` | 0 | 2026-08-20 |
| [**🆕 herdr-pane-tools**](https://github.com/solidsnakedev/herdr-pane-tools)<br><sub>solidsnakedev</sub> | 为 herdr 提供感知 Vim 的窗格导航、aerospace 风格的窗格移动，以及 tmux 风格的窗格轮换。 | `shell` | 0 | 🔄 2026-09-01 |
| [**herdr-confirm-close**](https://github.com/tajdien/herdr-confirm-close)<br><sub>tajdien</sub> | herdr 插件：关闭窗格或标签页前弹出确认提示 | `shell` | 0 | 2026-08-13 |
| [**herdr-jump**](https://github.com/tp6gw94/herdr-jump)<br><sub>tp6gw94</sub> | 面向 Herdr 工作区、标签页、窗格和 Agent 的键盘导航 | `javascript` | 0 | 2026-08-16 |
| [**🆕 herdr-focus**](https://github.com/trapple/herdr-focus)<br><sub>trapple</sub> | 聚焦下一个被阻塞/已完成的 Agent 窗格，并将终端应用置于前台。附带全局快捷键 | `shell` | 0 | 2026-07-19 |
| [**herdr-golden-ratio**](https://github.com/vigneshwerv/herdr-golden-ratio)<br><sub>vigneshwerv</sub> | 将聚焦的 Herdr 窗格调整为黄金比例（约 61.8%）大小 | `go` `terminal` | 0 | 🔄 2026-08-24 |
| [**herdr-balance-panes**](https://github.com/willfish/herdr-balance-panes)<br><sub>willfish</sub> | 将当前 Herdr 标签页中的窗格调整为均匀大小（相当于 tmux 的 select-layout -E） | `rust` `terminal` `tmux` | 0 | 2026-08-05 |
| [**🆕 herdr-grid**](https://github.com/WillHeather/herdr-grid)<br><sub>WillHeather</sub> | 将 herdr 工作区里的 Agent 窗格平铺成铺满屏幕的网格，也可以还原回去。 | `python` | 0 | 🔄 2026-08-31 |
| [**herdr-compass**](https://github.com/ycros/herdr-compass)<br><sub>ycros</sub> | 跨窗格、标签页和工作区的统一方向导航，面向 Herdr | `python` | 0 | 2026-08-07 |
| [**herdr-kakoune-popup**](https://github.com/Yukaii/herdr-kakoune-popup)<br><sub>Yukaii</sub> | 在 Herdr 原生弹窗中运行 Kakoune 的终端命令 | `kakoune` `shell` | 0 | 2026-08-20 |

<details><summary>与此目的也相关</summary>

- [thanhdat77/herdr-navigator](https://github.com/thanhdat77/herdr-navigator) — 通过一个模糊导航器跳转到任意 Herdr 工作区、Agent、项目、会话、远程连接、目录或操作
- [qu8n/herdr-automatic-rename](https://github.com/qu8n/herdr-automatic-rename) — Smart tab names and numbered labels for a smooth herdr navigation
- [speardragon/herdr-plugin-manager](https://github.com/speardragon/herdr-plugin-manager) — 在弹窗中管理 herdr 插件——安装、更新、启用/禁用、卸载，并浏览 herdr-plugin 市场。推荐快捷键：prefix+p
- [jorge07RD/herdr-ssh-manager](https://github.com/jorge07RD/herdr-ssh-manager) — 保存 SSH 主机，并从 Herdr 内的模糊弹窗中重新连接——按 Enter 即可直接将弹窗内容交给 ssh
- [bayoudhi/herdr-prayer-times](https://github.com/bayoudhi/herdr-prayer-times) — 在 Herdr 侧边栏中显示下一次礼拜时间和倒计时，并附带时间表弹窗和通知
- [black-atom-industries/helm.herdr](https://github.com/black-atom-industries/helm.herdr) — 通过一个模糊导航器跳转到任意 Herdr 工作区、Agent、项目、会话、远程连接、目录或操作
- [victor-software-house/herdr-stash](https://github.com/victor-software-house/herdr-stash) — 储藏 Herdr 工作区——停止其中的 Agent，同时保留其结构和对话内容，之后可从可点击的双栏弹窗中恢复
- [Joxtacy/herdr-plugin-vault](https://github.com/Joxtacy/herdr-plugin-vault) — 在 herdr 弹窗中浏览过去的 Claude Code 会话，并在新标签页中恢复所选的那个
- [leonho/herdr-idle-panes](https://github.com/leonho/herdr-idle-panes) — herdr 插件：以清单弹窗形式查看并关闭停留在闲置 shell 的窗格
- [ram4-dev/herdr-notify-center](https://github.com/ram4-dev/herdr-notify-center) — 为 Herdr 提供服务器范围的 Agent 通知，配有持久化的弹窗收件箱
- [shoaibkhanz/herdr-active-agent-jump](https://github.com/shoaibkhanz/herdr-active-agent-jump) — herdr 插件：按布局顺序前后循环聚焦正在进行中（工作中/被阻塞）的 Agent——作为 attention-jump 的 vim 风格补充
- [vgreg/herdr-padio](https://github.com/vgreg/herdr-padio) — 根据 herdr 当前聚焦窗格中运行的应用，自动切换 PadIO 控制器模式
- [yojahny55/herdr-space-groups](https://github.com/yojahny55/herdr-space-groups) — herdr 插件：将 Space 分组为带名称、带颜色的组——支持选择器弹窗（鼠标+键盘）、侧边栏分组标题和自动排序

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-files"></a>

## 文件浏览与编辑器联动

> 想在窗格中打开文件树，或与编辑器的状态保持一致

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**terminal-code**](https://github.com/zenbu-labs/terminal-code)<br><sub>zenbu-labs</sub> | 在终端中运行的 VS Code | `cli` `terminal` `vscode` `typescript` | 1899 | 🔄 2026-09-02 |
| [**herdr-file-viewer**](https://github.com/smarzban/herdr-file-viewer)<br><sub>smarzban</sub> | 面向 herdr 的只读文件查看器，支持感知 Git 状态。键盘驱动的 TUI（同时支持鼠标）：树形结构 + 内容窗格，支持差异对比、Markdown 渲染和语法高亮 | `file-viewer` `git` `ratatui` `rust` `terminal` | 533 | 🔄 2026-09-02 |
| [**herdr-sidebar**](https://github.com/alexarthurs/herdr-sidebar)<br><sub>alexarthurs</sub> | 面向 herdr 的 VS Code 风格侧边栏：将文件浏览器和 Git 源代码管理整合到一个窗格——带语法高亮的预览、VS Code 风格的差异对比、GitLens 风格的抽屉面板、AI 生成提交信息 | `git` `ratatui` `rust` `sidebar` `terminal` | 281 | 🔄 2026-09-05 |
| [**🆕 ttt**](https://github.com/eugenioenko/ttt)<br><sub>eugenioenko</sub> | TTT Editor (Terminal Text Tool): A real alternative to VS Code, Zed, and Sublime that runs in your terminal. A TUI that feels like GUI. Single binary, zero con… | `cli` `code-editor` `developer-tools` `diff` `editor` | 238 | 🔄 2026-09-05 |
| [**herdr-mirror**](https://github.com/nikok6/herdr-mirror)<br><sub>nikok6</sub> | 在同一窗口统一本地和远程会话：将远程 herdr 服务器镜像到本地侧边栏，并通过 SSH 操控 | `rust` | 221 | 🔄 2026-09-06 |
| [**herdr-nvim**](https://github.com/ChmaraX/herdr-nvim)<br><sub>ChmaraX</sub> | 将 Neovim 完全集成到你的 herdr 工作区 | `lua` `neovim` `nvim` `nvim-plugin` `rust` | 141 | 🔄 2026-09-03 |
| [**dotfiles**](https://github.com/edmundmiller/dotfiles)<br><sub>edmundmiller</sub> | 用于让我的 dotfiles 始终保持最新 | `dotfiles` `emacs` `nix-dotfiles` `nixos` `nixos-configuration` | 80 | 🔄 2026-09-07 |
| [**herdr-lazygit**](https://github.com/Crokily/herdr-lazygit)<br><sub>Crokily</sub> | 在 herdr 侧边栏窗格中运行 lazygit，支持 AI 生成提交信息——打开、展开、提交都只需一个按键 | `git` `lazygit` `shell` | 29 | 2026-07-17 |
| [**herdr-yazi**](https://github.com/speardragon/herdr-yazi)<br><sub>speardragon</sub> | 在 herdr 窗格中打开 Yazi | `shell` | 24 | 2026-08-19 |
| [**herdr-quicklook**](https://github.com/dwarvesf/herdr-quicklook)<br><sub>dwarvesf</sub> | herdr 的 Quick Look：将剪贴板中的路径以浮层形式弹出预览，一键切换到文件查看器 | `terminal` `shell` | 10 | 🔄 2026-08-26 |
| [**herdr-git-status**](https://github.com/ezcorp-org/herdr-git-status)<br><sub>ezcorp-org</sub> | herdr 插件：在侧边栏分支名旁显示每个空间的 git 工作区状态（已暂存/已修改/未跟踪/冲突） | `rust` | 9 | 2026-08-10 |
| [**herdr-context.nvim**](https://github.com/makyinmars/herdr-context.nvim)<br><sub>makyinmars</sub> | 在 Neovim 中选中代码或停在某一行，选择一个正在运行的 Herdr Agent，将结构化的上下文暂存到该 Agent 的提示词中（不直接提交） | `lua` | 9 | 🔄 2026-08-26 |
| [**herdr-workbench**](https://github.com/azizuysal/herdr-workbench)<br><sub>azizuysal</sub> | 精致的 Herdr 项目侧边栏，具备文件浏览器、实时文件/内容搜索、只读源代码管理、丰富的预览、文件图标和 Git 状态装饰 | `rust` | 6 | 2026-08-07 |
| [**herdr-flist**](https://github.com/devskale/herdr-flist)<br><sub>devskale</sub> | herdr 的文件列表插件 | `python` | 5 | 2026-07-10 |
| [**herdr-fresh**](https://github.com/rvalledorjr/herdr-fresh)<br><sub>rvalledorjr</sub> | 在 herdr 窗格内将终端 IDE「Fresh」作为文件查看器和编辑器运行的 herdr 插件 | `developer-tools` `editor` `fresh` `ide` `terminal` | 5 | 2026-07-17 |
| [**herdr-markdown-viewer**](https://github.com/arvindparmar-me/herdr-markdown-viewer)<br><sub>arvindparmar-me</sub> | Herdr 插件：拖选一个 Markdown 路径并按下 prefix+m，即可在右侧分屏窗格中预览 | `shell` | 4 | 2026-07-17 |
| [**herdr-plugin-mermaid-preview**](https://github.com/Volpestyle/herdr-plugin-mermaid-preview)<br><sub>Volpestyle</sub> | 在 Herdr 中为 Claude Code 和 Codex 的输出内容提供 Mermaid 图的实时预览 | `claude-code` `mermaid` `openai-codex` `terminal` `javascript` | 4 | 2026-07-10 |
| [**openloc.nvim**](https://github.com/Zamua/openloc.nvim)<br><sub>Zamua</sub> | 在已属于该工作区的 Neovim 中打开文件引用 | `lua` | 4 | 🔄 2026-08-25 |
| [**herdr-wait**](https://github.com/cdc-lst/herdr-wait)<br><sub>cdc-lst</sub> | 根据窗格的进程树判断闲置 Agent 窗格实际在做什么（例如 'waiting: build-api' 或 'waiting: codex'）并打上标签的可配置 herdr 插件 | `typescript` | 3 | 2026-07-03 |
| [**herdr-file-viewer**](https://github.com/ismaelosuna7824/herdr-file-viewer)<br><sub>ismaelosuna7824</sub> | 集文件浏览器、代码查看器和 Git 客户端于一体的键盘驱动 Herdr 窗格应用——用 Go + Bubble Tea 编写 | `bubbletea` `git` `golang` `tui` `go` | 3 | 2026-08-08 |
| [**herdr-lazygit**](https://github.com/JacquesvanWyk/herdr-lazygit)<br><sub>JacquesvanWyk</sub> | 在 herdr 分屏窗格或标签页中打开 lazygit，支持智能切换（打开/聚焦/关闭） | `lazygit` `shell` | 3 | 2026-07-12 |
| [**herdr-yazi-windows**](https://github.com/Only-Moon/herdr-yazi-windows)<br><sub>Only-Moon</sub> | herdr-yazi 的 Windows 移植版，借助 herdr v0.8+ 支持原生 Windows 窗格生成 | `file` `file-manager` `pidotdev` `python` `tui` | 3 | 2026-08-14 |
| [**herdr-x**](https://github.com/playsthisgame/herdr-x)<br><sub>playsthisgame</sub> | 在 herdr 内的终端分屏中浏览 x.com，并在 $EDITOR 中起草推文发送给自己 | `cli` `terminal` `terminal-browser` `twitter` `shell` | 3 | 2026-08-20 |
| [**advanced-herdr-file-viewer**](https://github.com/thuanlm215/advanced-herdr-file-viewer)<br><sub>thuanlm215</sub> | 面向 Herdr 的 Git 感知文件查看器——支持全文和文件名搜索（按工作区或文件夹）、可打开工作区和窗格的上下文操作、Unicode/Nerd 图标，以及独立滚动的树形结构 | `file-viewer` `ripgrep` `rust` `tui` | 3 | 🔄 2026-09-04 |
| [**dotfiles**](https://github.com/tifandotme/dotfiles)<br><sub>tifandotme</sub> | ~/.*（家目录下的配置文件） | `aerospace` `chezmoi` `cmux` `dotfiles` `ghostty` | 3 | 🔄 2026-09-05 |
| [**herdr-open-in-editor**](https://github.com/timofey-TK/herdr-open-in-editor)<br><sub>timofey-TK</sub> | 在 VS Code 或 Zed 中打开本地或远程的 Herdr 工作区 | `vscode` `zed` `python` | 3 | 2026-07-30 |
| [**herdr-claude-usage-multi**](https://github.com/iamhouser/herdr-claude-usage-multi)<br><sub>iamhouser</sub> | Herdr 侧边栏中的 Claude 套餐使用量表——会话/周 %、颜色随用量升级、重置倒计时，并通过 CLAUDE_CONFIG_DIR 配置支持多账号 | `claude-code` `python` | 2 | 🔄 2026-09-04 |
| [**scp-explorer**](https://github.com/TinocoAI/scp-explorer)<br><sub>TinocoAI</sub> | MobaXterm 风格的 SCP 文件浏览器 herdr 插件（跨平台支持 macOS/Linux/Windows） | `curses` `file-manager` `scp` `python` | 2 | 🔄 2026-09-03 |
| [**herdr-launcher-pane**](https://github.com/y-hirakaw/herdr-launcher-pane)<br><sub>y-hirakaw</sub> | herdr 的固定式点击启动窗格——按工作区启动 Finder/资源管理器、VS Code，或你配置的任意命令 | `launcher` `launcher-pane` `productivity` `python` | 2 | 2026-08-10 |
| [**herdr-flutter**](https://github.com/ablause/herdr-flutter)<br><sub>ablause</sub> | 在编程 Agent 旁边监视、热重载并检查运行中 Flutter 应用的 herdr 侧边栏 | `dart` | 1 | 2026-07-27 |
| [**herdr-cursor-open**](https://github.com/alex-devdone/herdr-cursor-open)<br><sub>alex-devdone</sub> | 在 Cursor 或 VS Code 中打开聚焦的 herdr 窗格——包括通过 Remote-SSH 连接到远程 herdr 的窗格 | `cursor` `vscode` `shell` | 1 | 🔄 2026-08-23 |
| [**herdr-goto**](https://github.com/asumaran/herdr-goto)<br><sub>asumaran</sub> | 跨 herdr 仓库、工作树和窗格的树形切换器 | `go` | 1 | 2026-08-23 |
| [**herdr-file-viewer**](https://github.com/jomarmontuya/herdr-file-viewer)<br><sub>jomarmontuya</sub> | 右侧显示的 Herdr 文件树插件，支持文件标签页、跟随当前目录、Git 状态装饰和可点击链接 | `go` | 1 | 2026-07-13 |
| [**herdr-yazi-explorer**](https://github.com/pjs-0457/herdr-yazi-explorer)<br><sub>pjs-0457</sub> | 在触发它的工作区内的 herdr 标签页/分屏中打开 Yazi（标记为 🗂 yazi），退出后会自动重启 | `yazi` `shell` | 1 | 2026-08-13 |
| [**herdr-terminal-file-manager**](https://github.com/robert-flo/herdr-terminal-file-manager)<br><sub>robert-flo</sub> | elio 文件管理器的轻量 herdr 封装。自动检测你当前的目录并原生启动 elio，将其流畅的预览、内联图片和批量操作直接带入你的 herdr 窗格 | `shell` | 1 | 2026-07-10 |
| [**herdr-numbered-workspaces**](https://github.com/abrose/herdr-numbered-workspaces)<br><sub>abrose</sub> | 在 herdr 侧边栏中为每个空间前面加上编号，与带索引的 switch_workspace 快捷键对应 | `shell` | 0 | 2026-07-21 |
| [**herdr-preview**](https://github.com/AlexanderMakarov/herdr-preview)<br><sub>AlexanderMakarov</sub> | Herdr 插件：按下热键高亮屏幕上可见的文件/文件夹路径，并在 file-viewer 中打开。可在 Agent 界面和终端中使用。 | `rust` | 0 | 🔄 2026-08-29 |
| [**herdr_plugin**](https://github.com/Andreslvc/herdr_plugin)<br><sub>Andreslvc</sub> | herdr 插件：在 VS Code 中打开窗格所在文件夹、复制路径，并将文件夹作为 space 打开 | `python` | 0 | 🔄 2026-08-24 |
| [**herdr-context**](https://github.com/Anthodev/herdr-context)<br><sub>Anthodev</sub> | 面向 herdr 的项目上下文面板——带 git 状态的文件树和 LLM 对话历史，始终陪伴在你的 Agent 身旁 | `git` `jj` `ratatui` `rust` `sidebar` | 0 | 🔄 2026-08-31 |
| [**herdr-ctx**](https://github.com/aorumbayev/herdr-ctx)<br><sub>aorumbayev</sub> | 面向 herdr 侧边栏窗格的 Claude 上下文窗口指示器 | `typescript` | 0 | 2026-07-21 |
| [**Renderd**](https://github.com/Brutheron/Renderd)<br><sub>Brutheron</sub> | 在 Herdr 中实时阅读已完成的 Claude Code 和 Codex 回复的 Markdown 阅读器 | `go` | 0 | 2026-08-15 |
| [**🆕 herdr-project-filter**](https://github.com/bshearrer/herdr-project-filter)<br><sub>bshearrer</sub> | Scope herdr's Agents sidebar to one git repository at a time. | `javascript` | 0 | 🔄 2026-09-05 |
| [**herdr-sidebar-plugin**](https://github.com/caoool/herdr-sidebar-plugin)<br><sub>caoool</sub> | _(暂无描述)_ | `typescript` | 0 | 🔄 2026-09-02 |
| [**herdr-jetbrains**](https://github.com/chenyao0910/herdr-jetbrains)<br><sub>chenyao0910</sub> | 在 Rider、WebStorm、IntelliJ IDEA 或 GoLand 中打开当前活动的 Herdr 工作区或工作树 | `developer-tools` `git-worktree` `goland` `intellij-idea` `jetbrains` | 0 | 🔄 2026-08-30 |
| [**herdr-codex-cost**](https://github.com/Coolsik/herdr-codex-cost)<br><sub>Coolsik</sub> | 在 Herdr 侧边栏中显示 Codex 会话的估算费用 | `codex` `shell` | 0 | 2026-07-31 |
| [**herdr-tab-badges**](https://github.com/CowboyVang/herdr-tab-badges)<br><sub>CowboyVang</sub> | 为持有多个标签页的 herdr 空间在侧边栏加上徽章 | `shell` | 0 | 2026-07-21 |
| [**herdr-tab-git**](https://github.com/hasuwini77/herdr-tab-git)<br><sub>hasuwini77</sub> | 在 Herdr Spaces 侧边栏中显示 Git 分支和状态，且跟随当前活动标签页而非第一个标签页 | `git` `terminal` `tui` `javascript` | 0 | 🔄 2026-08-28 |
| [**herdr-plugin-mado**](https://github.com/hidekingerz/herdr-plugin-mado)<br><sub>hidekingerz</sub> | 在编写该 Markdown 的 Agent 旁边，用 TUI 查看器 mado 打开 Agent 所写 Markdown 的 herdr 插件 | `mado` `markdown` `tui` `shell` | 0 | 🔄 2026-09-06 |
| [**herdr-nvim**](https://github.com/jtnovellis/herdr-nvim)<br><sub>jtnovellis</sub> | 在 Herdr 中运行的 Neovim：按标签页显示的全高侧边栏，以及与编码 Agent 之间真正的往返交流——就正在查看的代码提问、无需离开 Neovim 即可阅读回答，并逐步查看 Agent 所做的修改。 | `ai-agents` `claude-code` `developer-tools` `lua` `neovim` | 0 | 🔄 2026-09-06 |
| [**herdr-plugin-agent-repo**](https://github.com/khatriafaz/herdr-plugin-agent-repo)<br><sub>khatriafaz</sub> | 在 Agent 窗格标题和侧边栏中显示 Agent、仓库和分支名称的 Herdr 插件 | `javascript` | 0 | 2026-07-24 |
| [**🆕 herdr-nnn**](https://github.com/linuxing3/herdr-nnn)<br><sub>linuxing3</sub> | 在 herdr 中打开 nnn | `shell` | 0 | 2026-08-04 |
| [**herdr-cmux-file-viewer**](https://github.com/linvald/herdr-cmux-file-viewer)<br><sub>linvald</sub> | 将 cmux 的文件查看器同步到当前聚焦 herdr 空间的 herdr 插件 | `python` | 0 | 2026-07-23 |
| [**herdr-openmd**](https://github.com/RufusLin/herdr-openmd)<br><sub>RufusLin</sub> | 在 openmd 中打开选中的 Markdown——从 herdr 启动的丰富 Qt 预览 | `shell` | 0 | 2026-07-29 |
| [**herdr-git-detail**](https://github.com/sfroment/herdr-git-detail)<br><sub>sfroment</sub> | herdr 插件：以 $git_detail 侧边栏 token 的形式显示详细的 git 状态（已修改/已暂存/未跟踪/领先落后提交数/stash） | `developer-tools` `git` `shell` `starship` `terminal` | 0 | 2026-08-05 |
| [**herdr-gitui**](https://github.com/Shi1xin/herdr-gitui)<br><sub>Shi1xin</sub> | 在侧边栏窗格中运行 gitui 的 herdr 插件——支持开关切换、展开以及浅色/深色主题 | `gitui` `python` | 0 | 2026-07-28 |
| [**meadow**](https://github.com/Tetat-Chulchue/meadow)<br><sub>Tetat-Chulchue</sub> | 面向 herdr 终端多路复用器的鼠标驱动文件浏览器窗格 | `python` | 0 | 2026-07-21 |
| [**dotfiles**](https://github.com/Unique-Divine/dotfiles)<br><sub>Unique-Divine</sub> | 来自 Unique Divine 的 dotfiles 以及其他 ~ 目录下的配置 | `dotfiles` `lua` `neovim` `neovim-dotfiles` `nvim` | 0 | 🔄 2026-09-07 |
| [**🆕 herdr-git-dirty**](https://github.com/viko16/herdr-git-dirty)<br><sub>viko16</sub> | 一个轻量级 Herdr 插件，显示每个 Space 中未提交的 Git 文件数量。 | `git` `shell` | 0 | 🔄 2026-09-02 |
| [**herdr-cmux-cwd-sync**](https://github.com/WerrySs/herdr-cmux-cwd-sync)<br><sub>WerrySs</sub> | 为聚焦的 HerdR 窗格提供无侵入式的 cmux 文件浏览器同步 | `cmux` `macos` `python` | 0 | 2026-08-14 |

<details><summary>与此目的也相关</summary>

- [ChmaraX/herdr-gitview](https://github.com/ChmaraX/herdr-gitview) — herdr 的 Git 状态/差异面板——审查更改、在 nvim 中编辑、暂存/提交/丢弃，全部在终端内完成
- [vonzelle-vzt/herdr-extensions](https://github.com/vonzelle-vzt/herdr-extensions) — 面向 herdr 的迷你 VS Code——具备 LSP 诊断、自动补全、重命名和跳转到定义的完整编辑器，外加源代码管理、搜索、问题面板、测试、调试器、应用实时预览、运行时错误捕获、图片粘贴和 Agent 差异审查。共…
- [jsmenzies/mergr](https://github.com/jsmenzies/mergr) — 在 Herdr Space 侧边栏行中显示 GitHub 拉取请求状态
- [maedana/herdr-whereami](https://github.com/maedana/herdr-whereami) — 自动重命名标签页以显示你当前所在位置的 Herdr 插件——在 git 仓库内会显示为「仓库名/分支名」
- [bayoudhi/herdr-prayer-times](https://github.com/bayoudhi/herdr-prayer-times) — 在 Herdr 侧边栏中显示下一次礼拜时间和倒计时，并附带时间表弹窗和通知
- [brianh20/herdr-stagr](https://github.com/brianh20/herdr-stagr) — 面向 herdr 的源代码管理侧边栏——通过并排差异对比进行暂存、取消暂存和放弃更改
- [ctbaum/herdr-deck](https://github.com/ctbaum/herdr-deck) — herdr-agents.nvim 的搭配工作区启动器：在预先搭好的 Neovim、Agent、shell 和 lazygit 组合面板中打开或恢复 Claude 和 Codex
- [ZingerLittleBee/herdr-agent-pins](https://github.com/ZingerLittleBee/herdr-agent-pins) — 将 Herdr Agent 会话持久固定在 Agents 侧边栏顶部
- [btj93/herdr-tokens](https://github.com/btj93/herdr-tokens) — Publishes workspace metadata tokens derived from agent status, so sidebar colours can vary by state.
- [caner-akca/herdr-plugin-atomic-workflows](https://github.com/caner-akca/herdr-plugin-atomic-workflows) — herdr 插件：启动并监控隔离的 Atomic 工作流任务——包含活动看板、侧边栏 token、运行台账，以及可选的 Telegram 控制台
- [Gareth-Rouse/herdr-plugin-session-pruner](https://github.com/Gareth-Rouse/herdr-plugin-session-pruner) — herdr 插件：记录工作区的最后使用时间，在 Spaces 侧边栏中显示已过去多久，并将闲置工作区排除在会话恢复之外
- [jovylle/herdr-session-title-name](https://github.com/jovylle/herdr-session-title-name) — herdr 插件：将 terminal_title_stripped 持久化到标签页（顶部只保留 session_title，标签页关闭后依然保留该标题）
- [jpwallace22/herdr-glab-status](https://github.com/jpwallace22/herdr-glab-status) — A [Herdr](https://herdr.dev) plugin that shows each workspace's GitLab merge request status in the spaces sid…
- [jwanga/herdr-plugin-github-status](https://github.com/jwanga/herdr-plugin-github-status) — herdr plugin: a real-time GitHub project status pane (milestones, issues, PRs, Actions) docked on the right a…
- [limars874/herdr-pane-id-metadata](https://github.com/limars874/herdr-pane-id-metadata) — 用于规范化窗格 ID 和精简标签页/窗格侧边栏元数据的最小化 Herdr 插件
- [NachoPal/herdr-pane-agent-unread](https://github.com/NachoPal/herdr-pane-agent-unread) — 面向 herdr 的按窗格「未读」提醒 + 侧边栏徽章——找出你未在查看的窗格中已完成或需要输入的 Agent（因为 herdr 是按标签页而非按窗格追踪「已读」状态的）
- [ubuntudroid/herdr-git-stack](https://github.com/ubuntudroid/herdr-git-stack) — herdr 插件：在 spaces 侧边栏中显示每个 space 在其 git 分支栈中的位置，标记出父分支已移动的分支，并保持栈的连续性。仅使用本地提交图——无需联网、无需 forge API、无需额外的堆栈工具
- [yojahny55/herdr-space-groups](https://github.com/yojahny55/herdr-space-groups) — herdr 插件：将 Space 分组为带名称、带颜色的组——支持选择器弹窗（鼠标+键盘）、侧边栏分组标题和自动排序

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-cost"></a>

## Token 与费用管理

> 想看看 Agent 花费了多少，并想削减用量

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**memex**](https://github.com/nicosuave/memex)<br><sub>nicosuave</sub> | 搜索 Claude Code、Codex、Pi、OpenCode、GitHub Copilot 和 Cursor 的会话记录。恢复会话。追踪 token 使用 | `bm25` `claude-code` `codex-cli` `hybrid-search` `rag` | 189 | 🔄 2026-09-06 |
| [**llmtrim-herdr**](https://github.com/fkiene/llmtrim-herdr)<br><sub>fkiene</sub> | 降低 herdr 的 token 费用：压缩每个 Agent 窗格的请求（实测输入 -31% / 输出 -74%），并在每个窗格的徽章上显示节省的费用 | `llm-proxy` `llmtrim` `powershell` | 44 | 2026-07-02 |
| [**herdr-agent-usage**](https://github.com/senna-lang/herdr-agent-usage)<br><sub>senna-lang</sub> | 为 Herdr 中运行的 Agent 显示上下文使用量表和服务商速率限制 | `ai-agents` `claude-code` `codex` `golang` `rate-limiting` | 31 | 🔄 2026-09-06 |
| [**herdr-token-dashboard**](https://github.com/Davidcreador/herdr-token-dashboard)<br><sub>Davidcreador</sub> | 面向 Herdr Agent 窗格的实时 token 消耗仪表盘和通知 | `ai-agents` `bubbletea` `opencode` `pi-agent` `token-dashboard` | 18 | 2026-08-13 |
| [**herdr-claude-usage**](https://github.com/alejodelosrios/herdr-claude-usage)<br><sub>alejodelosrios</sub> | 不必再为了查配额而打开一个 Claude 会话。Claude 套餐使用情况（会话 % \| 周 %）始终显示在 Herdr 侧边栏中，同一账号下所有工作区共享。通过 Claude Code 自身的凭据获取与 /status 完全一致的精确数字：无需估算，无需额外登录，也不消耗套餐 token | `claude` `claude-code` `python` | 3 | 2026-07-21 |
| [**herdr-opentab**](https://github.com/hamidi-dev/herdr-opentab)<br><sub>hamidi-dev</sub> | 在 Herdr 侧边栏中实时显示 OpenTab 提供的每个 Agent 的 AI 花费 | `ai-agents` `opentab` `terminal` `python` | 3 | 2026-08-18 |
| [**herdr-gekiatsu-plugin**](https://github.com/yuuta1219/herdr-gekiatsu-plugin)<br><sub>yuuta1219</sub> | herdr 插件：把 Claude Code 的用量计数器做成了老虎机——1/99 中大奖概率，每天 10:00 JST 重置 | `claude` `claude-code` `python` `tui` | 3 | 2026-08-17 |
| [**herdr-api-credit-bar**](https://github.com/CristianPeralta/herdr-api-credit-bar)<br><sub>CristianPeralta</sub> | herdr 插件：显示按量计费 API 服务商的剩余额度，首先支持阿里云 Model Studio | `shell` | 2 | 🔄 2026-09-05 |
| [**herdr-quota**](https://github.com/kvkenyon/herdr-quota)<br><sub>kvkenyon</sub> | 在 Herdr 中一目了然地查看 Claude、Codex、Cursor 和 Kimi 的订阅配额 | `ai-tools` `claude-code` `cursor` `developer-tools` `kimi` | 2 | 🔄 2026-09-05 |
| [**herdr-whereami**](https://github.com/maedana/herdr-whereami)<br><sub>maedana</sub> | 自动重命名标签页以显示你当前所在位置的 Herdr 插件——在 git 仓库内会显示为「仓库名/分支名」 | `rust` | 2 | 2026-08-14 |
| [**scopefuel**](https://github.com/mgh3326/scopefuel)<br><sub>mgh3326</sub> | 面向 AI 编程 Agent 套餐的范围感知余量表——显示实际被限制的是什么（账号/模型/分组）以及何时恢复 | `ai-agents` `antigravity` `claude-code` `cli` `codex` | 1 | 🔄 2026-09-04 |
| [**herdr-model-lanes**](https://github.com/terry-li-hm/herdr-model-lanes)<br><sub>terry-li-hm</sub> | herdr 插件：在工作区行中显示 Codex、Claude Max 和 Grok 的配额，并为新 Agent 提供感知配额的模型档位车道（ag） | `claude` `codex` `grok` `model-routing` `quota` | 1 | 🔄 2026-08-30 |
| [**🆕 quota-deck**](https://github.com/ArtMoreno/quota-deck)<br><sub>ArtMoreno</sub> | quota-deck: credential-scoped AI quota and context for Herdr on Windows, macOS, and Linux | `rust` | 0 | 🔄 2026-09-06 |
| [**🆕 herdr-tokens**](https://github.com/btj93/herdr-tokens)<br><sub>btj93</sub> | Publishes workspace metadata tokens derived from agent status, so sidebar colours can vary by state. | `golang` `terminal` `tui` `go` | 0 | 🔄 2026-09-04 |
| [**🆕 ai-share-usage-herdr**](https://github.com/DongHyunnn/ai-share-usage-herdr)<br><sub>DongHyunnn</sub> | herdr plugin for AI Share Usage: shared Codex quota tracking in the herdr terminal | `javascript` | 0 | 🔄 2026-09-06 |
| [**herdr-usage**](https://github.com/Efeguclu1/herdr-usage)<br><sub>Efeguclu1</sub> | 在 Herdr Agent 标签页上以紧凑标记显示 Claude、Codex、Cursor、OpenCode 和 Pi 的账号用量 | `claude-code` `cursor` `openai` `opencode` `python` | 0 | 2026-08-22 |
| [**herdr-web-broker**](https://github.com/JefeLabs/herdr-web-broker)<br><sub>JefeLabs</sub> | 面向 herdr 的自托管 REST/WS API——可从任何地方启动并操控编程 Agent。支持 token、多用户会话所有权、git 操作、事件流以及父子实例联邦。附带 TypeScript SDK 和 React 包 | `typescript` | 0 | 🔄 2026-09-01 |
| [**🆕 herdr-glab-status**](https://github.com/jpwallace22/herdr-glab-status)<br><sub>jpwallace22</sub> | A [Herdr](https://herdr.dev) plugin that shows each workspace's GitLab merge request status in the spaces sidebar, as a $mr token on the workspace row: | `typescript` | 0 | 🔄 2026-09-05 |
| [**🆕 herdr-tokenlens**](https://github.com/KeithMoc/herdr-tokenlens)<br><sub>KeithMoc</sub> | Live carrying-cost and compact-breakeven meter for AI coding agents, as a herdr pane | `ai-agents` `claude-code` `llm-cost` `tui` `python` | 0 | 🔄 2026-09-04 |
| [**herdr-plugin-agent-quota**](https://github.com/kwanwooi25/herdr-plugin-agent-quota)<br><sub>kwanwooi25</sub> | 面向 Herdr 的 Agent 配额——为 Claude Code、Codex 和 Grok 提供 token 与费用仪表盘、侧边栏配额仪表和标签栏摘要 | `javascript` | 0 | 🔄 2026-08-30 |
| [**🆕 precc-herdr-plugin**](https://github.com/peria-ai/precc-herdr-plugin)<br><sub>peria-ai</sub> | herdr 的 PRECC 插件：跨 Agent 统计 token 节省情况的遥测，并支持一键完成 PRECC 设置。 | `claude-code` `precc` `shell` | 0 | 🔄 2026-09-02 |
| [**🆕 provider-usage**](https://github.com/ryus1234/provider-usage)<br><sub>ryus1234</sub> | Herdr 的服务商用量与配额显示条。 | `ai-usage` `quota-monitor` `rust` | 0 | 🔄 2026-08-31 |
| [**herdr-burn**](https://github.com/samuelbaldwin05/herdr-burn)<br><sub>samuelbaldwin05</sub> | 在 herdr 侧边栏中实时显示每个窗格的 Claude Code 费用/配额，并提供工作区总消耗量的浮层显示 | `python` | 0 | 2026-08-12 |
| [**herdr-model-capacity**](https://github.com/shrivatsas/herdr-model-capacity)<br><sub>shrivatsas</sub> | 显示账号级别 Claude、Codex/OpenAI 和 OpenRouter 容量的 Herdr 窗格 | `claude` `codex` `openrouter` `rust` | 0 | 🔄 2026-08-28 |
| [**herdr-usage-bar**](https://github.com/silverwolfdoc/herdr-usage-bar)<br><sub>silverwolfdoc</sub> | 为 Herdr 中的 AI Agent 显示使用限额和上下文用量，紧凑的底部用量条形式呈现 | `go` | 0 | 🔄 2026-08-27 |
| [**herdr-context-display**](https://github.com/TheBrunoPetkovic/herdr-context-display)<br><sub>TheBrunoPetkovic</sub> | 在 herdr 中每一行 Claude Code Agent 上以颜色标注上下文窗口用量 | `claude-code` `terminal` `typescript` | 0 | 🔄 2026-08-26 |
| [**pi-agent-usage**](https://github.com/w784415/pi-agent-usage)<br><sub>w784415</sub> | 显示 OpenAI Codex 配额和重置时间的 Pi 扩展，支持 Herdr 插件 | `openai-codex` `pi-extension` `pi-package` `quota` `typescript` | 0 | 🔄 2026-08-26 |
| [**🆕 herdr-grazr**](https://github.com/wazum/herdr-grazr)<br><sub>wazum</sub> | A simple and reliable auto account switcher for Claude Code: rotates to a fresh account before the 5-hour or weekly rate limit hits, so no pane ever stops at t… | `account-rotation` `account-switcher` `account-switching` `anthropic` `claude` | 0 | 🔄 2026-09-06 |
| [**claude-usage**](https://github.com/yuuta1219/claude-usage)<br><sub>yuuta1219</sub> | herdr 插件：将 Claude Code 使用率（会话%/周%）固定显示在侧边栏底部 | `claude` `claude-code` `python` `tui` | 0 | 2026-08-01 |

<details><summary>与此目的也相关</summary>

- [levi-qiao/herdr-agent-quota](https://github.com/levi-qiao/herdr-agent-quota) — Credential-scoped AI quota, context, and cache in Herdr for Claude, Codex, Grok, Agy, OpenCode, Pi, omp, and…
- [caner-akca/herdr-plugin-atomic-workflows](https://github.com/caner-akca/herdr-plugin-atomic-workflows) — herdr 插件：启动并监控隔离的 Atomic 工作流任务——包含活动看板、侧边栏 token、运行台账，以及可选的 Telegram 控制台
- [Coolsik/herdr-codex-cost](https://github.com/Coolsik/herdr-codex-cost) — 在 Herdr 侧边栏中显示 Codex 会话的估算费用

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-monitor"></a>

## 监控与仪表盘

> 想一目览尽 Agent 和机器的状态

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**clauth**](https://github.com/uwuclxdy/clauth)<br><sub>uwuclxdy</sub> | Claude Code 多账号管理器与用量监控（支持 CLI、TUI 和 MCP 跨账号委派） | `account-manager` `account-switcher` `anthropic` `claude` `claude-code` | 110 | 🔄 2026-09-06 |
| [**herdr-agent-quota**](https://github.com/levi-qiao/herdr-agent-quota)<br><sub>levi-qiao</sub> | Credential-scoped AI quota, context, and cache in Herdr for Claude, Codex, Grok, Agy, OpenCode, Pi, omp, and Devin. | `agent-usage` `agy` `ai-agents` `antigravity` `claude-code` | 67 | 🔄 2026-09-06 |
| [**herdr-beads**](https://github.com/miiraheart/herdr-beads)<br><sub>miiraheart</sub> | herdr 的 beads（bd）任务面板：以列表、表格或看板形式展示你的 bd issue，可作为侧边栏或浮动窗口 | `bd` `beads` `kanban` `rust` `tui` | 18 | 🔄 2026-08-25 |
| [**herdr-pc-ram-and-cpu-usage-overlay**](https://github.com/ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay)<br><sub>ezcorp-org</sub> | herdr 插件：按空间（工作区）实时显示 CPU/内存占用率，以占整机资源的比例呈现 | `rust` | 16 | 🔄 2026-08-27 |
| [**herdr-f1**](https://github.com/hmu332233/herdr-f1)<br><sub>hmu332233</sub> | 为 Herdr Agent 打造的 F1 风格仪表盘 | `agent-dashboard` `typescript` | 14 | 🔄 2026-09-07 |
| [**herdr-telemetry**](https://github.com/DIodide/herdr-telemetry)<br><sub>DIodide</sub> | 将工作区和 Agent 遥测数据流式传输到你自己掌控的端点的 Herdr 插件——Go 编写的单一二进制文件，默认注重隐私 | `golang` `telemetry` `go` | 12 | 2026-07-10 |
| [**herdres**](https://github.com/luminexord/herdres)<br><sub>luminexord</sub> | 基于 Tendwire 构建的 Telegram 界面，用于监控和向 Herdr 编程 Agent 发送消息 | `coding-agents` `telegram` `python` | 10 | 2026-08-09 |
| [**shepherd**](https://github.com/ryonakae/shepherd)<br><sub>ryonakae</sub> | 面向 Herdr 管理的编程 Agent 的 worker 可观测性守护进程和运行时桥接 | `pi-coding-agent` `pi-extension` `typescript` | 9 | 🔄 2026-08-28 |
| [**herdr-sysmon**](https://github.com/getpipher/herdr-sysmon)<br><sub>getpipher</sub> | 在 Herdr 侧边栏显示系统指标——CPU、内存、电池、网络、磁盘、时钟。忠实地将 tmux-cpu/tmux-battery/tmux-online-status 状态栏移植为 Herdr 工作区 token。以 macOS 为主 | `battery` `catppuccin` `cpu` `getpipher` `macos` | 7 | 2026-07-26 |
| [**herdr-workboard**](https://github.com/Phoobobo/herdr-workboard)<br><sub>Phoobobo</sub> | herdr 的看板式工作板 TUI：看板对应工作区，任务状态对应标签页，任务会话对应窗格 | `kanban` `tui` `typescript` | 7 | 2026-08-10 |
| [**herdr-devserver-status**](https://github.com/Razz21/herdr-devserver-status)<br><sub>Razz21</sub> | 通过可插拔规范检测窗格中开发服务器，并报告其生命周期状态的 Herdr 插件 | `astro` `cli` `deamon` `dev-server` `extensible` | 7 | 🔄 2026-08-25 |
| [**herdr-tally**](https://github.com/jasonrr/herdr-tally)<br><sub>jasonrr</sub> | 为你和你的 Agent 提供按项目划分的待办事项和速记板<br>📝 プロジェクト単位の TODO 管理 | `rust` `todo` | 6 | 🔄 2026-09-06 |
| [**herdr-lazydocker**](https://github.com/sudoeren/herdr-lazydocker)<br><sub>sudoeren</sub> | 在 herdr 的分屏窗格或独立标签页中运行 lazydocker | `docker` `lazydocker` `shell` | 6 | 🔄 2026-08-27 |
| [**herdr-shell-progress**](https://github.com/bayoudhi/herdr-shell-progress)<br><sub>bayoudhi</sub> | herdr 插件：不仅是编程 Agent，耗时较长的 shell 命令的进度也会实时显示在侧边栏 | `rust` | 5 | 🔄 2026-09-04 |
| [**herdr-kanban**](https://github.com/KokiKono/herdr-kanban)<br><sub>KokiKono</sub> | 将任务与 herdr 标签页关联的终端看板，数据持久化在 SQLite 中 | `rust` | 5 | 2026-07-10 |
| [**herdr-agent-watcher**](https://github.com/winoooops/herdr-agent-watcher)<br><sub>winoooops</sub> | 面向 Herdr 的编程 Agent 可观测性——实时侧边栏卡片、生命周期通知，以及零配置的 Claude Code 指标桥接 | `claude-code` `rust` | 5 | 🔄 2026-09-06 |
| [**🆕 herdr-codex-bridge**](https://github.com/ardasevinc/herdr-codex-bridge)<br><sub>ardasevinc</sub> | 通过一个集中式的 app-server，为 Codex 会话赋予原生的 Herdr 窗格身份标识。 | `ai-agents` `codex` `terminal` `go` | 3 | 🔄 2026-09-05 |
| [**herdr-mise**](https://github.com/funsaized/herdr-mise)<br><sub>funsaized</sub> | 运行的是「一轮」，而不是提示词 🧑‍🍳 面向 herdr 中 Agent 的可视化工具 | `agent` `agent-monitoring` `ai-agents` `cli-tool` `developer-tools` | 3 | 🔄 2026-09-06 |
| [**herdr-portal**](https://github.com/loofare/herdr-portal)<br><sub>loofare</sub> | 面向 herdr 的任务控制仪表盘——将所有工作区/标签页/窗格中的 Agent 汇总到一个实时 TUI 看板（支持键盘和鼠标）以及网页大屏中：结构化进度展示、Ctrl+B A 打开、点击跳转、可从浏览器直接回复 Agent | `agent-dashboard` `agent-monitor` `ai-agents` `claude-code` `codex` | 3 | 2026-08-20 |
| [**adlc-herdr**](https://github.com/voodootikigod/adlc-herdr)<br><sub>voodootikigod</sub> | ADLC 的 herdr 插件——按窗格显示阶段/工单/关卡状态，附带待办看板、关卡操作和 adlc-fleet 运行可观测性。是 voodootikigod/adlc/plugins/adlc-herdr 的自动同步镜像 | `javascript` | 3 | 🔄 2026-09-04 |
| [**herdr-agent-dashboard**](https://github.com/carsonjones/herdr-agent-dashboard)<br><sub>carsonjones</sub> | prefix+a 显示 herdr Agent 列表 | `typescript` | 2 | 2026-07-16 |
| [**herdr-telemetry-bridge**](https://github.com/CodyBontecou/herdr-telemetry-bridge)<br><sub>CodyBontecou</sub> | 将本地工作区、仓库、编程 Agent、模型和追踪遥测数据流式传输到外部客户端的 Herdr 插件 | `coding-agents` `telemetry` `time-md` `javascript` | 2 | 2026-06-26 |
| [**herdr-agentsview**](https://github.com/cpcloud/herdr-agentsview)<br><sub>cpcloud</sub> | 将 AgentsView 的活动压缩显示在一个异常繁忙的终端里 | `rust` | 2 | 🔄 2026-08-24 |
| [**herdr-statusline**](https://github.com/iiii1224/herdr-statusline)<br><sub>iiii1224</sub> | 面向 herdr 会话的可自定义状态栏 | `cli` `statusbar` `statusline` `tmux` `python` | 2 | 2026-08-15 |
| [**shepherd**](https://github.com/jwarykowski/shepherd)<br><sub>jwarykowski</sub> | 把你的待办事项统一「牧」起来 | `cli` `developer-tools` `go-lang` `productivity` `task-management` | 2 | 2026-08-21 |
| [**herdr-jira-board**](https://github.com/kiitosu/herdr-jira-board)<br><sub>kiitosu</sub> | 在 herdr 中运行的 Jira 看板，附带 Claude Code 会话启动器 | `python` | 2 | 🔄 2026-09-07 |
| [**herdr-ports**](https://github.com/Numbered-com/herdr-ports)<br><sub>Numbered-com</sub> | 在 herdr 中呈现正在运行的开发服务器：为每个至少运行一个 TCP 监听器的空间显示通用的 $ports 徽章 | `pids` `ports` `shell` | 2 | 2026-07-23 |
| [**herdr-cache-ttl**](https://github.com/nytafar/herdr-cache-ttl)<br><sub>nytafar</sub> | herdr 插件：按 Agent 窗格实时倒计时显示 prompt 缓存的 TTL | `rust` | 2 | 2026-08-05 |
| [**herdr-slurm**](https://github.com/quan-meng/herdr-slurm)<br><sub>quan-meng</sub> | 为 Slurm 分配任务创建 Herdr 工作区和受监控的 Agent 标签页 | `hpc` `slurm` `terminal-multiplexer` `python` | 2 | 2026-08-13 |
| [**herdr-tilt**](https://github.com/the-inconvenience-store/herdr-tilt)<br><sub>the-inconvenience-store</sub> | 面向 Herdr 的键盘驱动 Tilt 仪表盘 | `k8s` `kubernetes` `tilt` `rust` | 2 | 🔄 2026-08-24 |
| [**herdr-agent-state**](https://github.com/Tyru5/herdr-agent-state)<br><sub>Tyru5</sub> | herdr 的实时 Agent 状态窗格——以更易读的形式显示工作区中每个 Agent 正在做什么 | `claude-code` `rust` `terminal` | 2 | 2026-08-05 |
| [**herdr-memex-analytics**](https://github.com/vishnutskumar/herdr-memex-analytics)<br><sub>vishnutskumar</sub> | herdr 插件：基于 memex 历史记录，提供会话效率分析和实时 Agent 指导 | `rust` | 2 | 🔄 2026-09-01 |
| [**herdr-cache-timer**](https://github.com/ArteenHD/herdr-cache-timer)<br><sub>ArteenHD</sub> | 在 Herdr 侧边栏中直接显示每个 Agent 的 prompt 缓存何时过期 | `claude-code` `prompt-caching` `terminal` `javascript` | 1 | 2026-08-08 |
| [**herdr-glance**](https://github.com/arvmaan/herdr-glance)<br><sub>arvmaan</sub> | 用于查看 Agent 状态的桌面小组件 | `rust` | 1 | 🔄 2026-08-26 |
| [**herdr-tokscale-dashboard**](https://github.com/astkaasa/herdr-tokscale-dashboard)<br><sub>astkaasa</sub> | 将 Tokscale 作为本地 Herdr 仪表盘窗格打开 | `dashboard` `tokscale` `shell` | 1 | 2026-06-26 |
| [**herdr-plugin-codex-subs**](https://github.com/benkraus/herdr-plugin-codex-subs)<br><sub>benkraus</sub> | 显示 CLIProxyAPI 中 Codex 订阅额度和重置积分的 Herdr 仪表盘 | `go` | 1 | 2026-07-30 |
| [**🆕 tsk**](https://github.com/chrisg32/tsk)<br><sub>chrisg32</sub> | tsk——一个 TaskPaper/PlainTasks 风格的纯文本任务管理 TUI，使用 Rust 编写。既可独立运行，也可作为 herdr 插件使用。 | `rust` `taskpaper` `todo` `tui` | 1 | 🔄 2026-09-03 |
| [**herdr-spinner**](https://github.com/hasuwini77/herdr-spinner)<br><sub>hasuwini77</sub> | 通过仅用于显示的窗格元数据，为处于工作状态的 Herdr 窗格显示动态盲文旋转指示器 | `spinner` `terminal` `tui` `javascript` | 1 | 🔄 2026-08-27 |
| [**herdr-overview**](https://github.com/iamgp/herdr-overview)<br><sub>iamgp</sub> | 面向 Herdr 的 Mission Control / Exposé——以平铺方式实时展示所有 space | `terminal` `tui` `javascript` | 1 | 🔄 2026-08-28 |
| [**herdr-compose**](https://github.com/mattyan1053/herdr-compose)<br><sub>mattyan1053</sub> | 用于 docker compose 的 Herdr 插件 | `terminal` `tui` `shell` | 1 | 2026-07-24 |
| [**herdr-pulse**](https://github.com/moneycaringcoder/herdr-pulse)<br><sub>moneycaringcoder</sub> | 面向 herdr 的按工作区划分的 Agent 活动历史，以侧边栏迷你走势图形式呈现 | `monitoring` `rust` `sparkline` `terminal` | 1 | 🔄 2026-09-01 |
| [**herdr-readpending**](https://github.com/rcosteira79/herdr-readpending)<br><sub>rcosteira79</sub> | 标记你还没看完的 Agent。提供带编号的徽章（$read）+ 可重新排序的列表窗格。聚焦该 Agent 时会自动清除标记 | `python` | 1 | 🔄 2026-08-24 |
| [**herdr-status-ui-bar**](https://github.com/speardragon/herdr-status-ui-bar)<br><sub>speardragon</sub> | 在 herdr 标签栏中显示 AI Agent 的方案用量仪表（Claude Code / Codex / Grok） | `claude-code` `codex` `grok` `python` `tab-bar` | 1 | 🔄 2026-09-07 |
| [**herdr-agent-metrics**](https://github.com/szrenwei/herdr-agent-metrics)<br><sub>szrenwei</sub> | 面向 Claude Code、Codex 和 TraeX 的轻量级 Herdr 上下文与会话用量指标 | `claude-code` `openai-codex` `traex` `python` | 1 | 2026-08-04 |
| [**herdr-space-tab-metadata**](https://github.com/szrenwei/herdr-space-tab-metadata)<br><sub>szrenwei</sub> | 在侧边栏显示每个 Herdr Space 当前活动的标签页 | `terminal-ui` `python` | 1 | 2026-08-04 |
| [**taskherd**](https://github.com/ukwhatn/taskherd)<br><sub>ukwhatn</sub> | 与 herdr Agent 会话、PR 和 Jira 工单相关联的任务看板 | `claude-code` `kanban` `task-management` `tui` `go` | 1 | 🔄 2026-09-01 |
| [**herdr-activity-age**](https://github.com/1Morganmore/herdr-activity-age)<br><sub>1Morganmore</sub> | 显示每个 Agent 距上次状态变化已过去多久的 Windows 版 Herdr 插件 | `powershell` `windows` | 0 | 🔄 2026-08-30 |
| [**herdr-docker**](https://github.com/abcxff/herdr-docker)<br><sub>abcxff</sub> | 像追踪 herdr 中的 Agent 一样，追踪 docker 构建 | `docker` `javascript` | 0 | 2026-08-12 |
| [**🆕 deepseek-counter-herdr**](https://github.com/alkevintan/deepseek-counter-herdr)<br><sub>alkevintan</sub> | DeepSeek API credit in the herdr statusline — top-up spent, balance left, and today's pace toward a level month. | `python` | 0 | 🔄 2026-09-06 |
| [**🆕 herdr-claude-usage**](https://github.com/anyaachan/herdr-claude-usage)<br><sub>anyaachan</sub> | 在 Herdr 中查看 Claude Code 套餐的全局用量：标签栏摘要 + 弹出式仪表盘，基于 statusLine 实现，支持多账号。 | `claude` `claude-code` `cli` `terminal` `shell` | 0 | 🔄 2026-09-01 |
| [**herdr-ios-build-status-plugin**](https://github.com/atomsbaza/herdr-ios-build-status-plugin)<br><sub>atomsbaza</sub> | 按需查看的 Herdr iOS 构建+测试状态窗格，附带失败时的截图 | `shell` | 0 | 2026-08-06 |
| [**herdr-nodejs-center**](https://github.com/AZenking/herdr-nodejs-center)<br><sub>AZenking</sub> | 用于监控并聚焦本地 Node.js、Bun 和 Deno 服务的 Herdr 弹窗 | `developer-tools` `nodejs` `javascript` | 0 | 2026-08-20 |
| [**herdr-plugin-atomic-workflows**](https://github.com/caner-akca/herdr-plugin-atomic-workflows)<br><sub>caner-akca</sub> | herdr 插件：启动并监控隔离的 Atomic 工作流任务——包含活动看板、侧边栏 token、运行台账，以及可选的 Telegram 控制台 | `javascript` | 0 | 🔄 2026-09-01 |
| [**herdr-jcode-integration**](https://github.com/capt-marbles/herdr-jcode-integration)<br><sub>capt-marbles</sub> | 用于 Jcode 生命周期状态和会话报告的 Herdr 插件 | `jcode` `shell` | 0 | 2026-08-09 |
| [**herdr-dev-servers**](https://github.com/carellano/herdr-dev-servers)<br><sub>carellano</sub> | 发现并安全管理运行在 Herdr 窗格中的开发服务器 | `developer-tools` `go` `terminal` | 0 | 2026-08-12 |
| [**herdr-agent-metadata**](https://github.com/choplin/herdr-agent-metadata)<br><sub>choplin</sub> | 显示每个 Herdr Agent 的语义状态最后一次发生变化的时间 | `go` | 0 | 🔄 2026-08-26 |
| [**herdr-repository-identity**](https://github.com/choplin/herdr-repository-identity)<br><sub>choplin</sub> | 报告每个 Herdr 工作区所共享的 Git 仓库身份信息 | `go` | 0 | 🔄 2026-08-24 |
| [**🆕 herdr-claude-lifecycle**](https://github.com/daocoding/herdr-claude-lifecycle)<br><sub>daocoding</sub> | 面向 herdr + Omarchy、以 hook 为核心的 Claude Code 生命周期管理：通过 Claude 自身的 hook 获取 working/blocked/idle 状态，并在每次 Claude Code 更新后进行验证。 | `claude-code` `omarchy` `python` | 0 | 🔄 2026-09-04 |
| [**herdr-process-guard**](https://github.com/Efeguclu1/herdr-process-guard)<br><sub>Efeguclu1</sub> | 解释并安全停止由编程 Agent 遗留运行的开发服务器 | `claude-code` `codex` `coding-agents` `cursor` `macos` | 0 | 🔄 2026-08-24 |
| [**herdr-vitals**](https://github.com/ericcparsons/herdr-vitals)<br><sub>ericcparsons</sub> | 面向 macOS 的 herdr 插件——在侧边栏显示每个 Agent 的 CPU/RAM 占用和每个空间中运行的开发服务器端口，并可通过弹窗结束它们 | `bun` `developer-tools` `terminal` `typescript` | 0 | 2026-07-29 |
| [**🆕 subherd**](https://github.com/HalloSouf/subherd)<br><sub>HalloSouf</sub> | 一个 herdr 插件，按会话所在的工作区分组，展示每个 Claude Code 子 Agent 正在做什么。 | `claude-code` `tui` `go` | 0 | 🔄 2026-09-05 |
| [**herdr-kanban**](https://github.com/hassox/herdr-kanban)<br><sub>hassox</sub> | 将工作区窗格呈现为看板 | `go` | 0 | 2026-08-21 |
| [**herdr-ports**](https://github.com/ivorpad/herdr-ports)<br><sub>ivorpad</sub> | herdr 插件：一个弹窗，列出正在监听的端口，标出每个端口背后的项目名称，并可将其终止或打开 | `tui` `python` | 0 | 🔄 2026-08-27 |
| [**herdr-reap**](https://github.com/ivorpad/herdr-reap)<br><sub>ivorpad</sub> | herdr 插件：显示所有 Agent 的生命周期状态，一键关闭已完成的那些 | `tui` `python` | 0 | 🔄 2026-08-27 |
| [**herdr-metrics**](https://github.com/jordanhawkes/herdr-metrics)<br><sub>jordanhawkes</sub> | 在 Herdr 侧边栏中显示 Claude Code、Codex 和 TraeX 的上下文、会话 token 和账号限额指标。是 szrenwei/herdr-agent-metrics 的维护延续 | `claude-code` `openai-codex` `traex` `tui` `python` | 0 | 2026-08-22 |
| [**🆕 herdr-pomodoro**](https://github.com/michmos/herdr-pomodoro)<br><sub>michmos</sub> | Pomodoro inside herdr's status bar | `focus` `pomodoro` `pomodoro-timer` `python` | 0 | 🔄 2026-09-04 |
| [**herdr-last-used**](https://github.com/MorganCollins/herdr-last-used)<br><sub>MorganCollins</sub> | 显示每个 herdr Agent 最后一次活跃的时间，按新旧程度着色，并可按活跃度筛选 Agent 侧边栏 | `terminal` `shell` | 0 | 🔄 2026-08-24 |
| [**herdr-phin-board**](https://github.com/phin-tech/herdr-phin-board)<br><sub>phin-tech</sub> | Herdr 插件：覆盖你所有空间的状态板——待办、进行中、等待他人、已完成，还可以自定义任意状态。支持列表或看板视图 | `bubbletea` `tui` `go` | 0 | 2026-07-29 |
| [**herdr-idle-shell-badge**](https://github.com/rcosteira79/herdr-idle-shell-badge)<br><sub>rcosteira79</sub> | 为仍有后台 shell 在运行的空闲 Agent 显示徽章 | `python` | 0 | 🔄 2026-08-26 |
| [**colloquy**](https://github.com/SoMaCoSF/colloquy)<br><sub>SoMaCoSF</sub> | 面向 Agent 集群的自寻址、临时缓存的因果 DAG 审计日志与遥测 | `colloquy` `gyst` `javascript` | 0 | 2026-07-29 |
| [**🆕 herdr-launcher**](https://github.com/Tatendaz/herdr-launcher)<br><sub>Tatendaz</sub> | Unofficial macOS Dock launcher for the herdr TUI: click the ram, get herdr in your terminal | `applescript` `developer-tools` `dock` `launcher` `macos` | 0 | 🔄 2026-09-04 |
| [**🆕 herdr-mem-cpu-load**](https://github.com/thewtex/herdr-mem-cpu-load)<br><sub>thewtex</sub> | CPU, memory, and load average monitor for herdr. | `rust` | 0 | 🔄 2026-09-07 |
| [**herdr-claude-context-meter**](https://github.com/tmastalirsch/herdr-claude-context-meter)<br><sub>tmastalirsch</sub> | herdr 插件：以进度条形式显示 Claude Code 的上下文用量——同时支持状态栏和 herdr 窗格 | `claude-code` `context-window` `statusline` `shell` | 0 | 🔄 2026-08-27 |
| [**herdr-workspace-board**](https://github.com/tmastalirsch/herdr-workspace-board)<br><sub>tmastalirsch</sub> | herdr 插件：为每个有未完成工作的 git 仓库显示一行，并按被遗忘的可能性排序 | `git` `productivity` `workspace` `shell` | 0 | 🔄 2026-08-27 |
| [**conflux-herdr**](https://github.com/tumf/conflux-herdr)<br><sub>tumf</sub> | 用于运行 Conflux TUI 并报告其生命周期状态的 Herdr 插件窗格 | `shell` | 0 | 2026-07-26 |
| [**herdr-hud**](https://github.com/zetlen/herdr-hud)<br><sub>zetlen</sub> | herdr 插件：通过快捷键弹出面板，显示主机、网络、Agent 和会话信息——可配置，并可通过自定义脚本扩展 | `bash` `terminal` `shell` | 0 | 2026-08-03 |

<details><summary>与此目的也相关</summary>

- [nelsonPires5/herdr-board](https://github.com/nelsonPires5/herdr-board) — herdr 的看板工具——卡片就是提示词，会被派发给可见窗格中的 AI Agent
- [quaywin/agys](https://github.com/quaywin/agys) — 通过零污染沙盒，为 Herdr 中的 Antigravity CLI 提供轻松的多配置文件隔离和实时配额追踪
- [IvoryHeart/herdr-world](https://github.com/IvoryHeart/herdr-world) — Herdr World——面向 Herdr 的多界面网页体验
- [e2b-dev/herdr-e2b-sandbox](https://github.com/e2b-dev/herdr-e2b-sandbox) — 将 git 工作树镜像到 E2B Sandbox 的 herdr 插件——支持单个沙盒或每个 Agent 一条分支的沙盒集群，并配有 TUI 仪表盘
- [Northern-Lighthouse/herdr-fleet](https://github.com/Northern-Lighthouse/herdr-fleet) — 通过 Tailscale 管理一批 herdr 机器——仪表盘插件、自动发现、感知容量的 Agent 派发、无盘工作区
- [cdowell09/herdr-pr-board](https://github.com/cdowell09/herdr-pr-board) — 面向 Herdr 的可配置跨仓库 GitHub 拉取请求仪表盘
- [bengemine/herdr-hibernate](https://github.com/bengemine/herdr-hibernate) — 让 Herdr 中空闲的编程 Agent 窗格（Claude Code、Codex、Grok）休眠——释放内存，按 Enter 即可恢复原会话
- [Javamomma/herdr-scribe](https://github.com/Javamomma/herdr-scribe) — herdr 插件：不录音的实时会议转录——将麦克风输入转为仅存于内存的文字记录和实时分析窗格；停止时生成会议纪要、可选策略关卡以及可审查的自动草稿。支持 Linux/WSL2 和 macOS
- [sazardev/herdr-code-board](https://github.com/sazardev/herdr-code-board) — Herdr 内面向 Agent 提示词的看板队列——卡片会将真实 Agent 派发到窗格、工作树和工作区，并可通过规则将一张卡片链到下一张
- [chouxcreams/herdr-dashboard](https://github.com/chouxcreams/herdr-dashboard) — herdr 工作区的 PR 状态仪表盘 TUI——一目了然地查看每个窗格对应的 PR 状态/CI/审查情况
- [GranamyrBR/LunaCrab](https://github.com/GranamyrBR/LunaCrab) — 为另一个项目保留
- [maedana/herdr-agents-preview](https://github.com/maedana/herdr-agents-preview) — Herdr 的多 Agent 终端预览仪表盘：同时显示所有运行中的 Agent，所选 Agent 占据大部分宽度
- [spad-0x/herdr-web-dashboard](https://github.com/spad-0x/herdr-web-dashboard) — A high-performance, mobile-first PWA dashboard with a Cyber-Dark design for orchestrating Herdr and autonomou…
- [GranamyrBR/ezdras-herdr](https://github.com/GranamyrBR/ezdras-herdr) — 面向 Herdr 的实时多 Agent 可观测性与窗格控制
- [peria-ai/precc-herdr-plugin](https://github.com/peria-ai/precc-herdr-plugin) — herdr 的 PRECC 插件：跨 Agent 统计 token 节省情况的遥测，并支持一键完成 PRECC 设置。
- [ryus1234/provider-usage](https://github.com/ryus1234/provider-usage) — Herdr 的服务商用量与配额显示条。

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-finder"></a>

## 搜索与模糊查找器

> 只记得大概名字也想调出命令或项目

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-navigator**](https://github.com/thanhdat77/herdr-navigator)<br><sub>thanhdat77</sub> | 通过一个模糊导航器跳转到任意 Herdr 工作区、Agent、项目、会话、远程连接、目录或操作 | `fuzzy-finder` `rust` `terminal` `workspace-manager` | 131 | 🔄 2026-08-25 |
| [**termscope**](https://github.com/iurysza/termscope)<br><sub>iurysza</sub> | 在分屏中打开终端屏幕上已经可见的文件和链接 | `python` `television` `terminal` `tmux` | 51 | 2026-08-19 |
| [**herdr-sessionizer**](https://github.com/andrewchng/herdr-sessionizer)<br><sub>andrewchng</sub> | 通过模糊搜索打开项目和工作树，再从声明式 TOML 布局（标签页、窗格分割、命令、按仓库覆盖配置）启动工作区 | `bun` `fuzzy-finder` `fzf` `git-worktree` `sessionizer` | 46 | 🔄 2026-09-02 |
| [**herdr-plugin-sesh**](https://github.com/fullerzz/herdr-plugin-sesh)<br><sub>fullerzz</sub> | 面向 Herdr 的 Sesh 风格工作区选择器 TUI，集成 zoxide，可从常用目录创建工作区 | `bubbletea` `sesh` `tui` `zoxide` `go` | 38 | 🔄 2026-09-06 |
| [**herdr-command-palette**](https://github.com/JanTvrdik/herdr-command-palette)<br><sub>JanTvrdik</sub> | herdr 的 fzf 命令面板——模糊选择并运行任意插件操作 | `shell` | 36 | 2026-06-29 |
| [**herdr-bar**](https://github.com/jeffarese/herdr-bar)<br><sub>jeffarese</sub> | herdr 的 Cmd+K：模糊跳转到任意标签页、Agent、仓库或分支。仅使用 Python 标准库 | `command-bar` `fuzzy-finder` `python` `terminal` `tui` | 36 | 🔄 2026-08-31 |
| [**herdr-drovr**](https://github.com/AVGVSTVS96/herdr-drovr)<br><sub>AVGVSTVS96</sub> | 轻松移动 herdr 窗格和标签页 | `fzf` `terminal` `javascript` | 15 | 2026-08-08 |
| [**herdr-zoxide**](https://github.com/den-tanui/herdr-zoxide)<br><sub>den-tanui</sub> | 从 zoxide 记录的目录创建工作区、标签页和窗格的 Herdr 插件 | `zoxide` `shell` | 11 | 2026-07-25 |
| [**herdr-palette**](https://github.com/ramarivera/herdr-palette)<br><sub>ramarivera</sub> | 面向 Herdr 工作区的 Rust/Ratatui 模糊命令面板 | `command-palette` `ratatui` `rust` `terminal` `tui` | 8 | 2026-08-14 |
| [**herdr-palette**](https://github.com/vjeantet/herdr-palette)<br><sub>vjeantet</sub> | Sublime Text / VS Code 风格的 herdr 命令面板——内置操作、插件动作和你自己的命令，全部藏在一个按键之后 | `command-palette` `fuzzy-search` `terminal` `tui` `rust` | 8 | 🔄 2026-08-31 |
| [**herdr-quick-actions**](https://github.com/enekos/herdr-quick-actions)<br><sub>enekos</sub> | 以 fzf 选择器调用 herdr 原生的标签页/窗格/工作区操作，按使用频率排序——不必再死记快捷键 | `shell` | 7 | 2026-08-05 |
| [**herdr-switchboard**](https://github.com/crafts69guy/herdr-switchboard)<br><sub>crafts69guy</sub> | herdr 插件：在一个 Rust 编写的 TUI 中模糊切换运行中的 Agent、已打开的工作区和 ghq 管理的仓库——并可将仓库在新工作区、标签页、分屏或当前窗格中打开 | `developer-tools` `ghq` `ratatui` `rust` `terminal` | 5 | 🔄 2026-09-03 |
| [**herdr-sessionizer**](https://github.com/salkhalil/herdr-sessionizer)<br><sub>salkhalil</sub> | herdr 的 tmux-sessionizer：用 fzf 搜索已打开的工作区和 zoxide 目录，创建或聚焦并附带模板标签页 | `shell` | 5 | 2026-07-27 |
| [**herdr-hunk**](https://github.com/JacquesvanWyk/herdr-hunk)<br><sub>JacquesvanWyk</sub> | herdr 中用于 Hunk 差异对比的交互式 fzf 选择器：支持提交、范围、stash，并可在 Agent 完成时自动打开 | `fzf` `hunk` `shell` | 4 | 2026-07-12 |
| [**herdr-pane-navigator**](https://github.com/mr04vv/herdr-pane-navigator)<br><sub>mr04vv</sub> | 将 Herdr 的工作区、标签页和窗格作为一棵模糊树进行导航——以每个窗格实际在做什么为线索 | `coding-agents` `fzf` `terminal` `tui` `shell` | 4 | 🔄 2026-09-07 |
| [**herdr-keymap**](https://github.com/The-Dave-Stack/herdr-keymap)<br><sub>The-Dave-Stack</sub> | herdr 插件：在浮层面板中展示所有快捷键，并可直接运行有对应 CLI 命令的那些 | `typescript` | 4 | 2026-08-12 |
| [**herdr-kiosk**](https://github.com/thomasschafer/herdr-kiosk)<br><sub>thomasschafer</sub> | 模糊查找 Git 仓库和分支，并在 Herdr 中作为工作树打开 | `rust` | 4 | 🔄 2026-08-27 |
| [**herdr-cast**](https://github.com/aliou/herdr-cast)<br><sub>aliou</sub> | 个人 Herdr 插件——提供原生 macOS Agent 通知、模糊工作区导航、基于 zoxide 的工作区创建以及布局命令 | `developer-tools` `macos` `notifications` `ratatui` `rust` | 3 | 🔄 2026-08-31 |
| [**herdr-palette**](https://github.com/cesarferreira/herdr-palette)<br><sub>cesarferreira</sub> | 面向 Herdr 的弹窗式命令面板 | `typescript` | 3 | 2026-08-14 |
| [**herdr-grep-nvim**](https://github.com/cinco/herdr-grep-nvim)<br><sub>cinco</sub> | herdr 插件：用 fzf + ripgrep 进行实时搜索，并在你工作区旁边的分屏中用 nvim 打开匹配结果 | `shell` | 3 | 2026-07-17 |
| [**herdr-spotify**](https://github.com/iikjl/herdr-spotify)<br><sub>iikjl</sub> | herdr 的 Spotify 正在播放浮层插件——专辑封面、播放控制，并可通过 Spotify Web API 搜索/加入队列/点赞 | `spotify` `terminal` `go` | 3 | 2026-07-07 |
| [**herdr-ssh-manager**](https://github.com/jorge07RD/herdr-ssh-manager)<br><sub>jorge07RD</sub> | 保存 SSH 主机，并从 Herdr 内的模糊弹窗中重新连接——按 Enter 即可直接将弹窗内容交给 ssh | `rust` `ssh` `terminal` `tui` | 3 | 🔄 2026-08-24 |
| [**herdr-workspacer**](https://github.com/mcuste/herdr-workspacer)<br><sub>mcuste</sub> | 使用 zoxide 查找项目，然后切换或创建 Herdr 工作区 | `rust` `tui` `zoxide` | 3 | 🔄 2026-09-03 |
| [**herdr-agent-recency**](https://github.com/ugurtarlig/herdr-agent-recency)<br><sub>ugurtarlig</sub> | 支持主题的 Herdr 选择器，按 Codex 和 Claude 有意义的活动情况排序 | `claude-code` `codex` `fzf` `python` | 3 | 2026-07-17 |
| [**herdr-openr**](https://github.com/wraithyy/herdr-openr)<br><sub>wraithyy</sub> | herdr 插件：模糊查找并打开终端或 AI Agent 刚提到的文件/URL——在 Claude 窗格中会读取会话记录 | `shell` | 3 | 2026-08-14 |
| [**herdr-configurable-picker**](https://github.com/yoshiori/herdr-configurable-picker)<br><sub>yoshiori</sub> | 面向 herdr 的树形跳转选择器，快捷键完全可配置 | `rust` | 3 | 2026-07-05 |
| [**herdr-command-palette**](https://github.com/alon-z/herdr-command-palette)<br><sub>alon-z</sub> | Herdr 插件：模糊搜索工作区/目录的命令面板 | `javascript` | 2 | 2026-06-22 |
| [**herdr-launcher**](https://github.com/arjenblokzijl/herdr-launcher)<br><sub>arjenblokzijl</sub> | 模糊选择一个声明式 TOML 工作流，填写表单，在新的 herdr 空间中启动编程 Agent | `launcher` `ratatui` `rust` `tui` | 2 | 2026-07-10 |
| [**🆕 herdr-palette**](https://github.com/Binb1/herdr-palette)<br><sub>Binb1</sub> | Herdr 的命令面板。可跳转到工作区和 Agent，运行插件动作，也可执行 Herdr 命令。 | `go` | 2 | 🔄 2026-09-03 |
| [**herdr-sesh-bro**](https://github.com/cyperx84/herdr-sesh-bro)<br><sub>cyperx84</sub> | 面向 Herdr 的 sesh 风格模糊会话选择器——将工作区、Agent 和 zoxide 目录整合到一个带实时预览的 fzf 弹窗中 | `go` | 2 | 🔄 2026-09-07 |
| [**herdr-simple-switcher**](https://github.com/haphamdev/herdr-simple-switcher)<br><sub>haphamdev</sub> | 对工作区、标签页和 AI Agent 进行模糊搜索 | `shell` | 2 | 2026-08-01 |
| [**herdr-workspace-launcher**](https://github.com/ImArtisann/herdr-workspace-launcher)<br><sub>ImArtisann</sub> | 面向 macOS 的 Herdr 插件，通过可搜索的键盘驱动目录选择器快速创建聚焦工作区 | `typescript` | 2 | 2026-07-16 |
| [**herdr-recent-workspaces**](https://github.com/ismaelosuna7824/herdr-recent-workspaces)<br><sub>ismaelosuna7824</sub> | Herdr 的「打开最近使用的文件夹」——可模糊筛选你曾作为工作区打开过的文件夹列表。选择一个即可打开或重新聚焦该工作区，也可浏览文件系统打开新的 | `go` | 2 | 2026-07-10 |
| [**herdr-ghq-open-agent**](https://github.com/kenchan/herdr-ghq-open-agent)<br><sub>kenchan</sub> | herdr 插件：用 fzf 对 ghq 管理的仓库进行增量搜索，在工作区/标签页中打开所选仓库并启动 claude | `fzf` `ghq` `shell` | 2 | 2026-08-03 |
| [**herdr-keybind-search**](https://github.com/malone-c/herdr-keybind-search)<br><sub>malone-c</sub> | herdr 的可搜索快捷键浮层（基于 fzf）。按下一个键即可模糊搜索你的快捷键 | `shell` | 2 | 2026-07-15 |
| [**🆕 herdr-flash-picker**](https://github.com/TinyWhite1997/herdr-flash-picker)<br><sub>TinyWhite1997</sub> | Fast pane picker for Herdr with aligned one- or two-letter jump labels | `rust` `tui` | 2 | 🔄 2026-09-06 |
| [**herdr-waypoint**](https://github.com/wraithyy/herdr-waypoint)<br><sub>wraithyy</sub> | 为文件夹命名并保存，从模糊列表中选一个，作为新的 herdr 工作区打开 | `shell` | 2 | 2026-08-12 |
| [**herdr-sessionizer**](https://github.com/42lizard/herdr-sessionizer)<br><sub>42lizard</sub> | tmux-sessionizer 风格的 herdr 插件 | `fzf` `shell` | 1 | 🔄 2026-08-28 |
| [**herdr-url-picker**](https://github.com/abrose/herdr-url-picker)<br><sub>abrose</sub> | herdr 插件：用 fzf 选取当前窗格中显示的 URL，并用默认浏览器打开 | `shell` | 1 | 2026-07-22 |
| [**herdr-jump**](https://github.com/agustinvalencia/herdr-jump)<br><sub>agustinvalencia</sub> | 为 herdr 空间和 Agent 分别提供的浮层选择器——跳转到任意工作区或 Agent，并以颜色实时显示状态 | `go` | 1 | 2026-07-24 |
| [**herdr-command-palette**](https://github.com/barnuri/herdr-command-palette)<br><sub>barnuri</sub> | 面向 herdr 的 F1 风格命令面板——可模糊搜索并运行所有已安装插件的全部操作，零依赖 | `command-palette` `terminal` `javascript` | 1 | 🔄 2026-09-01 |
| [**helm.herdr**](https://github.com/black-atom-industries/helm.herdr)<br><sub>black-atom-industries</sub> | 通过一个模糊导航器跳转到任意 Herdr 工作区、Agent、项目、会话、远程连接、目录或操作 | `rust` | 1 | 🔄 2026-09-03 |
| [**herdr-workspace-save**](https://github.com/chandrasekharan98/herdr-workspace-save)<br><sub>chandrasekharan98</sub> | 保存 Herdr 工作区（布局、工作目录、Agent 会话、正在运行的命令），之后可从 fzf 选择器中重新打开 | `claude-code` `terminal` `tmux` `python` | 1 | 2026-08-19 |
| [**herdr-url-picker**](https://github.com/chouxcreams/herdr-url-picker)<br><sub>chouxcreams</sub> | Herdr 插件：从聚焦窗格中选取一个 URL 并在浏览器中打开 | `shell` | 1 | 2026-07-22 |
| [**herdr-spotify**](https://github.com/DeepRuparel/herdr-spotify)<br><sub>DeepRuparel</sub> | 面向 Herdr 的 Spotify 集成——Go 编写，提供零配置的本地控制，并通过 PKCE 授权支持搜索/加入队列/保存 | `spotify` `go` | 1 | 🔄 2026-08-28 |
| [**herdr-plugin-command-palette**](https://github.com/haisi/herdr-plugin-command-palette)<br><sub>haisi</sub> | 基于 fzf、支持模糊搜索的 herdr 命令面板 | `fzf` `python` | 1 | 2026-08-17 |
| [**herdr-command-palette**](https://github.com/hota911/herdr-command-palette)<br><sub>hota911</sub> | 面向 herdr 内置操作（工作区、标签页、窗格、Agent）的 fzf 命令面板 | `command-palette` `fzf` `shell` | 1 | 2026-08-16 |
| [**herdr-turbo-palette**](https://github.com/jackfrancisdalton/herdr-turbo-palette)<br><sub>jackfrancisdalton</sub> | 模糊查找任意 Herdr space、标签页、Agent 或窗格，并直接跳转过去 | `python` | 1 | 2026-08-22 |
| [**herdr-keys**](https://github.com/JacquesvanWyk/herdr-keys)<br><sub>JacquesvanWyk</sub> | 面向 herdr 的可模糊搜索快捷键速查表（支持功能包、发现和个人自定义覆盖） | `shell` | 1 | 2026-07-12 |
| [**🆕 herdr-open-editor**](https://github.com/jimididit/herdr-open-editor)<br><sub>jimididit</sub> | 用 fzf 模糊搜索并选择文件，然后在你配置的编辑器中打开。 | `herd` `text-editor` `tui` `shell` | 1 | 🔄 2026-09-03 |
| [**herdr-fzf-url**](https://github.com/kaar/herdr-fzf-url)<br><sub>kaar</sub> | 从 herdr 窗格的滚动记录中模糊查找并打开 URL——tmux-fzf-url 的 herdr 移植版 | `shell` | 1 | 2026-07-29 |
| [**herdr-hint**](https://github.com/maedana/herdr-hint)<br><sub>maedana</sub> | Herdr 的 Vimium 风格提示标签——按键后在标签页和 Agent 上显示标签，再按标签即可跳转 | `rust` | 1 | 2026-08-11 |
| [**herdr-shortcut**](https://github.com/matheus3301/herdr-shortcut)<br><sub>matheus3301</sub> | 面向 Herdr 的快捷任务选择器兼编程 Agent 启动器 | `bubbletea` `claude-code` `codex` `coding-agents` `developer-tools` | 1 | 2026-07-24 |
| [**🆕 herdr-pickers**](https://github.com/sagmans/herdr-pickers)<br><sub>sagmans</sub> | 为 Agent、worktree、工作区和项目提供多种自定义的弹出式选择器。 | `typescript` | 1 | 🔄 2026-09-04 |
| [**herdr-pane-picker**](https://github.com/ugurtarlig/herdr-pane-picker)<br><sub>ugurtarlig</sub> | 输入窗格上显示的字符提示来选择 Herdr 窗格 | `terminal` `wezterm` `python` | 1 | 2026-07-17 |
| [**herdr-bitwarden**](https://github.com/WillowMist/herdr-bitwarden)<br><sub>WillowMist</sub> | 模糊搜索你的 Bitwarden 密码库并粘贴/复制凭据——tmux-bitwarden 的 herdr 移植版 | `bitwarden` `fzf` `terminal` `tmux` `shell` | 1 | 2026-08-11 |
| [**herdr-fzf-url**](https://github.com/x0d7x/herdr-fzf-url)<br><sub>x0d7x</sub> | 扫描 herdr 终端窗格中的 URL，并用 fzf 交互式选取一个 | `fzf` `go` `url` | 1 | 2026-06-26 |
| [**herdr-open-local-paths**](https://github.com/yigitkg/herdr-open-local-paths)<br><sub>yigitkg</sub> | 检测本地路径，并通过简易选择器在 Windows、Linux 和 WSL 上打开或显示的 Herdr 插件 | `developer-tools` `python` `terminal` `wsl` | 1 | 2026-07-28 |
| [**herdr-agents-picker**](https://github.com/yxhta/herdr-agents-picker)<br><sub>yxhta</sub> | Herdr 插件：类似工作区选择器的 Agent 窗格模糊选择器，带实时窗格预览（Rust + ratatui 编写） | `rust` | 1 | 2026-07-31 |
| [**herdr-telescope**](https://github.com/zackshen/herdr-telescope)<br><sub>zackshen</sub> | 面向 herdr 的 fzf 命令 telescope——支持原生操作、插件操作、文件查找（@）和实时 ripgrep 搜索（/） | `fzf` `rust` | 1 | 2026-08-20 |
| [**herdr-iris**](https://github.com/a-curious-coder/herdr-iris)<br><sub>a-curious-coder</sub> | Iris——herdr 插件：针对窗格中检测到的 Agent，提供 AI Agent 技能的模糊搜索速查表 | `shell` | 0 | 2026-08-07 |
| [**herdr-project-manager**](https://github.com/barnuri/herdr-project-manager)<br><sub>barnuri</sub> | 面向 herdr 的项目管理插件——支持 glob/手动项目发现、模糊选择器，并可作为标签页或工作区打开 | `javascript` | 0 | 🔄 2026-08-25 |
| [**herdr-worktree-picker**](https://github.com/BjoernSchotte/herdr-worktree-picker)<br><sub>BjoernSchotte</sub> | 面向 Herdr 的模糊 Git 工作树选择器——只需输入分支名，而不必输入 worktree-rapid-river-6486 这样的名字。可作为分组工作区或分屏窗格打开 | `bash` `cli` `developer-tools` `fzf` `git-worktree` | 0 | 🔄 2026-08-24 |
| [**herdr-locksmith**](https://github.com/bkarpinos/herdr-locksmith)<br><sub>bkarpinos</sub> | 面向 herdr 的快捷键命令面板 | `go` | 0 | 🔄 2026-09-01 |
| [**herdr-picker**](https://github.com/bkarpinos/herdr-picker)<br><sub>bkarpinos</sub> | 用于在 herdr 中搜索和预览工作区、Agent 和标签页的快速弹窗选择器 | `go` | 0 | 2026-07-25 |
| [**herdr-opencode-sessions**](https://github.com/damianpoole/herdr-opencode-sessions)<br><sub>damianpoole</sub> | 可按标题、项目、路径、日期或会话记录内容对过去的 OpenCode 会话进行模糊搜索的 Herdr 插件——带会话预览，并提供在当前或新工作区中恢复/分叉会话的快捷方式 | `typescript` | 0 | 2026-08-14 |
| [**herdr-agents**](https://github.com/dleen/herdr-agents)<br><sub>dleen</sub> | 面向 herdr 的 fzf Agent 选择器——列出所有 Agent 窗格并按最需处理优先排序，支持会话预览和一键启动 | `coding-agents` `fzf` `python` `terminal` | 0 | 2026-08-20 |
| [**herdr-command-palette**](https://github.com/fabiogaliano/herdr-command-palette)<br><sub>fabiogaliano</sub> | 面向 Herdr 的模糊命令面板——搜索任意操作、查看其快捷键并执行 | `command-palette` `fzf` `terminal` `python` | 0 | 2026-08-10 |
| [**herdr-keybinds**](https://github.com/gwelican/herdr-keybinds)<br><sub>gwelican</sub> | 用于列出/搜索所有快捷键绑定（包括插件的快捷键）的 Herdr 插件。 | `python` | 0 | 🔄 2026-08-31 |
| [**herdr-control-panel**](https://github.com/iskwyuki/herdr-control-panel)<br><sub>iskwyuki</sub> | 一个快捷键、一个面板操控 herdr——从历史记录或任意路径打开工作区，还可添加自定义操作。纯 bash + fzf 实现，无需构建 | `bash` `fzf` `terminal` `shell` | 0 | 2026-08-11 |
| [**pj-herdr**](https://github.com/josephschmitt/pj-herdr)<br><sub>josephschmitt</sub> | 使用 PJ 选择器打开新工作区的 Herdr 插件 | `shell` | 0 | 2026-07-15 |
| [**herdr-finder-reveal**](https://github.com/klukacin/herdr-finder-reveal)<br><sub>klukacin</sub> | 点击 Herdr 窗格中的本地文件路径，即可在 macOS 的 Finder 中显示该文件 | `finder` `ghostty` `macos` `terminal-multiplexer` `shell` | 0 | 2026-08-10 |
| [**herdr-cull**](https://github.com/krzysztoff1/herdr-cull)<br><sub>krzysztoff1</sub> | 查看并关闭 herdr 中闲置的 Agent 窗格——fzf 多选，未经确认绝不关闭 | `ai-agents` `claude` `codex` `fzf` `terminal` | 0 | 2026-07-20 |
| [**🆕 herdr-jump**](https://github.com/lancodev/herdr-jump)<br><sub>lancodev</sub> | 为 herdr 的工作区与 Agent 提供双窗格模糊搜索切换器，支持 vim 按键操作。 | `fzf` `tui` `shell` | 0 | 🔄 2026-09-01 |
| [**herdr-vscode-tasks**](https://github.com/lurepos/herdr-vscode-tasks)<br><sub>lurepos</sub> | 处理项目中 .vscode 文件夹时很实用的 herdr 选择器 | `typescript` | 0 | 🔄 2026-09-02 |
| [**herdr-omarchy-theme-sync**](https://github.com/maxBRT/herdr-omarchy-theme-sync)<br><sub>maxBRT</sub> | 将 Herdr 的 UI 配色与当前使用的 Omarchy 主题同步 | `linux` `omarchy` `theme` `python` | 0 | 2026-08-15 |
| [**🆕 herdr-plugin-project-finder**](https://github.com/mike-bronner/herdr-plugin-project-finder)<br><sub>mike-bronner</sub> | Herdr 插件：模糊搜索 git 仓库，并将其作为工作区打开。 | `python` | 0 | 🔄 2026-09-05 |
| [**herdr-workspaces**](https://github.com/mikedclarke/herdr-workspaces)<br><sub>mikedclarke</sub> | 将目录作为 herdr 的工作区：注册常用工作目录，模糊选择其一，即可在那里获得一个具名工作区 | `go` `terminal` `tui` `workspaces` | 0 | 🔄 2026-09-02 |
| [**herdr-smart-workspace**](https://github.com/nicolasvasquez/herdr-smart-workspace)<br><sub>nicolasvasquez</sub> | 用于在会话内快速切换工作区，或通过浮层 fzf 选择器从 zoxide 创建新工作区的 Herdr 插件 | `python` | 0 | 2026-07-02 |
| [**herdr-launcher**](https://github.com/nicolegros/herdr-launcher)<br><sub>nicolegros</sub> | 提供模糊目录选择器以快速创建或切换工作区的 herdr 插件 | `go` | 0 | 2026-07-15 |
| [**mux-prompter**](https://github.com/phine-apps/mux-prompter)<br><sub>phine-apps</sub> | 模糊选取上下文相关的提示词，并注入到 Herdr 或 tmux 窗格中 | `fzf` `prompt-engineering` `terminal-multiplexer` `tmux` `tmux-plugin` | 0 | 🔄 2026-08-31 |
| [**herdr-repo-picker**](https://github.com/princejoogie/herdr-repo-picker)<br><sub>princejoogie</sub> | 通过 OpenTUI 选择器，将 Git 仓库作为 Herdr 工作区打开 | `git` `opentui` `typescript` | 0 | 2026-08-17 |
| [**herdr-claude-profile**](https://github.com/quinnjr/herdr-claude-profile)<br><sub>quinnjr</sub> | herdr 插件：通过浮层面板切换和管理 claude-profile 的配置 | `typescript` | 0 | 2026-07-20 |
| [**herdr-plugins**](https://github.com/shelken/herdr-plugins)<br><sub>shelken</sub> | Herdr 插件 monorepo（auto-pi：按区域打开 pi + 会话选择器） | `python` | 0 | 2026-07-17 |
| [**herdr-file-picker**](https://github.com/shivammehta25/herdr-file-picker)<br><sub>shivammehta25</sub> | 将 tmux-file-picker 移植到 herdr 的「vibe coding」作品 | `shell` | 0 | 2026-07-29 |
| [**herdr-atuin-plugin**](https://github.com/smanickam01/herdr-atuin-plugin)<br><sub>smanickam01</sub> | 在 herdr 弹窗中搜索 Atuin 的 shell 历史记录——按 prefix+a，Enter 执行、Tab 编辑。安装后自动绑定快捷键 | `atuin` `macos` `shell-history` `terminal` `zsh` | 0 | 2026-08-17 |
| [**🆕 herdr-jump**](https://github.com/solidsnakedev/herdr-jump)<br><sub>solidsnakedev</sub> | 为 herdr 提供工作区、窗格与标签页的模糊搜索选择器，外加一个切换到上一个工作区的开关。 | `shell` | 0 | 🔄 2026-09-01 |
| [**🆕 herdr-hop**](https://github.com/utahta/herdr-hop)<br><sub>utahta</sub> | herdr 插件：通过一个弹窗即可跳转到仓库、worktree 或工作区。 | `git-worktree` `go` `terminal` `tui` | 0 | 🔄 2026-09-02 |
| [**herdr-workspacex**](https://github.com/willfish/herdr-workspacex)<br><sub>willfish</sub> | Rust 原生的模糊 Herdr 工作区切换器，支持基于 zoxide 的工作区创建 | `rust` `workspace-manager` `zoxide` | 0 | 2026-07-07 |
| [**herdr-fzf-url**](https://github.com/willian/herdr-fzf-url)<br><sub>willian</sub> | 用 `fzf` 从聚焦窗格中选取 URL，然后打开或复制 | `fzf` `shell` | 0 | 2026-07-28 |
| [**🆕 herdr-hop**](https://github.com/youguanxinqing/herdr-hop)<br><sub>youguanxinqing</sub> | Jump to any visible Herdr pane by pressing a labeled key | `rust` | 0 | 🔄 2026-09-05 |

<details><summary>与此目的也相关</summary>

- [beyondlex/herdr-recent-navigator](https://github.com/beyondlex/herdr-recent-navigator) — 面向 Herdr 的最近工作区/标签页/窗格切换器。弹出窗口列出最近聚焦过的工作区、标签页、窗格和 AI Agent，支持模糊搜索和键盘导航
- [JacquesvanWyk/herdr-linear](https://github.com/JacquesvanWyk/herdr-linear) — 在 herdr 分屏窗格或标签页中运行的 fzf 驱动 Linear 面板：搜索 issue、深入项目、创建 issue、修改状态
- [42lizard/herdr-dwm-layout](https://github.com/42lizard/herdr-dwm-layout) — 面向 Herdr 的 DWM 风格 master/stack 布局
- [adamwangxx/herdr-codex-resume](https://github.com/adamwangxx/herdr-codex-resume) — 在保留 Herdr 实时上下文的新分屏中打开原生的 Codex resume 选择器
- [caoer/ccc-herdr-layout](https://github.com/caoer/ccc-herdr-layout) — 面向 herdr 的可视化布局选择器插件——一键操作，实时预览

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-automation"></a>

## 自动化、钩子与定时任务

> 想在创建工作树或指定时机自动运行固定的操作步骤

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-browser**](https://github.com/ogulcancelik/herdr-browser)<br><sub>ogulcancelik</sub> | 在 Herdr 窗格内渲染真实的 Chromium 视图，并通过 CDP 进行操控 | `browser` `browser-automation` `cdp` `chromium` `kitty-graphics` | 349 | 2026-08-22 |
| [**herdr-auto-title**](https://github.com/kryptamine/herdr-auto-title)<br><sub>kryptamine</sub> | 自动跟随每个标签页中工作内容变化的标签标题。借助 Herdr 让标签页保持整洁，一眼就知道自己在做什么。 | `go` | 75 | 🔄 2026-09-06 |
| [**herdr-automatic-rename**](https://github.com/qu8n/herdr-automatic-rename)<br><sub>qu8n</sub> | Smart tab names and numbered labels for a smooth herdr navigation | `shell` | 71 | 🔄 2026-09-04 |
| [**herdr-auto-title**](https://github.com/sh1ma/herdr-auto-title)<br><sub>sh1ma</sub> | 根据 Claude Code 和 Codex 的对话内容，自动生成 herdr 标签页标题 | `claude-code` `codex` `python` | 53 | 2026-08-13 |
| [**zed-herdr**](https://github.com/ImArtisann/zed-herdr)<br><sub>ImArtisann</sub> | 自动将当前活动的 HerdR 工作区与已有的 Zed 会话保持同步 | `typescript` | 27 | 2026-08-17 |
| [**herdr-worktree-setup**](https://github.com/tdi/herdr-worktree-setup)<br><sub>tdi</sub> | herdr 插件：创建工作树时执行按项目定制的初始化步骤（从 main 复制 .env、mise trust、direnv allow、安装依赖等） | `javascript` | 24 | 2026-07-20 |
| [**herdr-workflows**](https://github.com/aorumbayev/herdr-workflows)<br><sub>aorumbayev</sub> | 为 herdr 中的重复步骤提供声明式自动化 | `agentic-ai` `agentic-workflow` `agents` `ai` `claude` | 20 | 🔄 2026-09-05 |
| [**herdr-auto-pilot**](https://github.com/0xGosu/herdr-auto-pilot)<br><sub>0xGosu</sub> | 通过 Herdr API 代替你自动向运行中的 AI 编程 CLI 发送提示词的 Herdr 插件。插件具有从你的操作中学习的训练模式，并内置防止危险/恶意操作的防护机制。经过充分训练后，可让它以「完全自主提示（FSP）」模式运行 | `go` | 19 | 🔄 2026-09-07 |
| [**herdr-routines**](https://github.com/mrcndz/herdr-routines)<br><sub>mrcndz</sub> | 运行定时任务的 Herdr 插件：按 cron 或固定间隔在工作区中打开标签页，运行命令或启动 Agent | `python` | 11 | 2026-07-18 |
| [**herdr-tab-title**](https://github.com/aarsh21/herdr-tab-title)<br><sub>aarsh21</sub> | 为 Herdr 提供类似 tmux 的自动标签页标题 | `rust` `terminal` `tmux` | 8 | 2026-07-08 |
| [**herdr-updater**](https://github.com/diegopzz/herdr-updater)<br><sub>diegopzz</sub> | 在整个机群范围内安全地让 Herdr 本体及其插件保持最新 | `rust` `updater` | 8 | 🔄 2026-09-01 |
| [**herdr-agent-config-manager**](https://github.com/Phoobobo/herdr-agent-config-manager)<br><sub>Phoobobo</sub> | 混合 CLI + Herdr 插件，用于检测并集中管理 Agent 的 skill、MCP、插件和 hook | `python` | 8 | 🔄 2026-09-06 |
| [**bermuda**](https://github.com/bon5co/bermuda)<br><sub>bon5co</sub> | 在 herdr 上由 Claude Code 驱动的编排——Agent 无法跳过的流程、定时任务、带 claim 的线程，以及供 Agent 日后检索的论坛 | `agent-orchestration` `agents` `ai-agents` `automation` `claude-code` | 6 | 🔄 2026-09-06 |
| [**herdr-automations**](https://github.com/DnzzL/herdr-automations)<br><sub>DnzzL</sub> | 在终端中运行、面向编程 Agent 的定时任务，基于 Herdr。每次运行都会准备一条提示词、一行 cron 和一个全新的 git 工作树。仅需一个 YAML 文件，无需存储、提供预编译二进制、可按自动化单独指定模型、支持睡眠后补跑，并附带实时看板 | `ai-agents` `automation` `claude-code` `coding-agents` `cron` | 6 | 🔄 2026-09-01 |
| [**herdr-pane-balancer**](https://github.com/jeph/herdr-pane-balancer)<br><sub>jeph</sub> | 在窗格创建、关闭和退出时，自动均衡、均分并平铺 Herdr 终端窗格 | `python` | 5 | 2026-08-02 |
| [**herdr-fwd**](https://github.com/go-min/herdr-fwd)<br><sub>go-min</sub> | 为远程 Herdr 会话自动设置回环端口转发 | `port-forwarding` `ssh` `terminal` `rust` | 3 | 🔄 2026-09-01 |
| [**tendwire**](https://github.com/plotarmordev/tendwire)<br><sub>plotarmordev</sub> | Herdr 的本地 API：将编程 Agent 连接到应用、自动化流程和任意本地系统 | `agent-api` `local-first` `python` | 3 | 2026-08-10 |
| [**herdr-labels**](https://github.com/Angel-O/herdr-labels)<br><sub>Angel-O</sub> | 在保留手动标签的同时，自动为标签页命名和编号的 Herdr 插件 | `rust` | 2 | 2026-08-17 |
| [**herdr-js-worktree-bootstrap**](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap)<br><sub>LeonardoTrapani</sub> | 为 JavaScript 和 TypeScript 自动初始化 Herdr 工作树，支持基于锁文件的安装和安全的环境变量还原 | `automation` `bun` `developer-tools` `git-worktree` `javascript` | 2 | 2026-07-15 |
| [**herdr-shepherd**](https://github.com/mikedclarke/herdr-shepherd)<br><sub>mikedclarke</sub> | 面向 herdr 的定时 Agent 会话——将心跳检测、cron 例程和脚本作为可见的 herdr 工作区启动 | `coding-agents` `cron` `go` `scheduler` `tui` | 2 | 🔄 2026-09-05 |
| [**herdr-review-loop**](https://github.com/mikhail-angelov/herdr-review-loop)<br><sub>mikhail-angelov</sub> | 在 herdr 工作区中让 Agent 之间自动进行交叉评审——一个负责编写，另一个负责评审，如此反复 | `terminal` `go` | 2 | 2026-08-16 |
| [**herdr-plugin**](https://github.com/ppggff/herdr-plugin)<br><sub>ppggff</sub> | 自动记住并恢复每个 Herdr 窗格对应的正确 macOS 输入法（IME） | `ime` `input-method` `macos` `python` | 2 | 2026-07-27 |
| [**🆕 herdr-triggers**](https://github.com/cantona/herdr-triggers)<br><sub>cantona</sub> | 常驻监听窗格输出并按正则表达式触发动作：自动登录等由正则驱动的终端触发器。 | `rust` `terminal` | 1 | 🔄 2026-09-02 |
| [**hermes-herdr-auto-reconcile**](https://github.com/chris-yyau/hermes-herdr-auto-reconcile)<br><sub>chris-yyau</sub> | 面向监视 Herdr 窗格的 Hermes 监督者的网关存活检测插件 | `automation` `hermes-agent` `multi-agent` `python` | 1 | 🔄 2026-09-02 |
| [**herdr-auto-tab-name**](https://github.com/dev-shimada/herdr-auto-tab-name)<br><sub>dev-shimada</sub> | herdr 插件：根据当前目录自动命名标签页 | `javascript` | 1 | 🔄 2026-09-05 |
| [**herdr-auto-update**](https://github.com/dio16/herdr-auto-update)<br><sub>dio16</sub> | herdr 插件：启动时检查已安装插件是否有更新的上游提交，如有则自动重新安装 | `rust` | 1 | 2026-08-16 |
| [**herdr-routines**](https://github.com/guidodinello/herdr-routines)<br><sub>guidodinello</sub> | _(暂无描述)_ | `python` | 1 | 🔄 2026-09-06 |
| [**say-hook**](https://github.com/HikaruEgashira/say-hook)<br><sub>HikaruEgashira</sub> | 使用 ElevenLabs 文字转语音朗读 Claude Code hook 事件的 macOS CLI | `typescript` | 1 | 🔄 2026-09-01 |
| [**herdr-sched**](https://github.com/husniadil/herdr-sched)<br><sub>husniadil</sub> | 面向 Herdr 编程 Agent 的调度与触发器——cron 任务和 webhook/文件监视触发器会向相邻插件触发动作，每个动作都由其执行主体签名。全部由一个 Go 二进制程序实现 | `ai-agents` `cron` `mcp-server` `scheduler` `webhooks` | 1 | 🔄 2026-08-30 |
| [**herdr-automations**](https://github.com/ram4-dev/herdr-automations)<br><sub>ram4-dev</sub> | 面向 Herdr 的声明式 cron、间隔和事件自动化 | `automation` `bun` `typescript` | 1 | 2026-08-13 |
| [**herdr-autocontinue**](https://github.com/rcosteira79/herdr-autocontinue)<br><sub>rcosteira79</sub> | 监控 Agent 是否触及用量上限，以徽章形式显示重置倒计时（$wall），并在时间窗口重新开放后，向你预先设置的 Agent 重新发送提示词 | `python` | 1 | 🔄 2026-08-31 |
| [**herdr-nixos-vm**](https://github.com/Slimydog21/herdr-nixos-vm)<br><sub>Slimydog21</sub> | 面向 herdr 的 NixOS 虚拟机窗格——启动、停止、监视 Hashimoto 风格的开发虚拟机，并可 ssh 连接。需要 nixos-vm kit | `shell` | 1 | 2026-08-18 |
| [**herdr-agent-title-sync**](https://github.com/winoooops/herdr-agent-title-sync)<br><sub>winoooops</sub> | 为 Claude Code、Codex、Kimi Code、OpenCode 等编程 Agent 提供的 Herdr 窗格标题自动同步 | `developer-tools` `typescript` | 1 | 2026-08-20 |
| [**herdr-plugin-orbstack**](https://github.com/AsgardMuninn/herdr-plugin-orbstack)<br><sub>AsgardMuninn</sub> | 将 OrbStack 的 Linux 虚拟机作为 herdr 工作区打开（直接 shell 连接、SSH 回退、自动同步） | `python` | 0 | 2026-08-11 |
| [**🆕 herdr-pane-autorename**](https://github.com/b12o/herdr-pane-autorename)<br><sub>b12o</sub> | Herdr plugin that autorenames panes with the name of the current running process. | `shell` | 0 | 🔄 2026-09-07 |
| [**herdr-auto-update**](https://github.com/barnuri/herdr-auto-update)<br><sub>barnuri</sub> | 让 herdr 始终保持最新——自动进行 patch/minor/major 更新，并支持无缝交接 | `auto-update` `javascript` | 0 | 🔄 2026-08-25 |
| [**herdr-teams-notify**](https://github.com/donghaolicd/herdr-teams-notify)<br><sub>donghaolicd</sub> | 为 Microsoft Teams 提供带节流控制的 Agent 生命周期通知的 Herdr 插件 | `automation` `microsoft-teams` `notifications` `javascript` | 0 | 2026-08-15 |
| [**herdr-context-namer**](https://github.com/eabadim/herdr-context-namer)<br><sub>eabadim</sub> | 通过 OpenCode 根据窗格上下文自动为 Herdr 标签页和工作区命名 | `opencode` `python` | 0 | 2026-08-06 |
| [**herdr-claude-title-hook**](https://github.com/eduardoborges/herdr-claude-title-hook)<br><sub>eduardoborges</sub> | 将会话标题同步到 Herdr 标签页标题的 Claude Code 插件 | `shell` | 0 | 🔄 2026-08-26 |
| [**🆕 herdr-plugin-pane-id-namer**](https://github.com/gcgo/herdr-plugin-pane-id-namer)<br><sub>gcgo</sub> | Automatically generate an agent name and display it in the terminal. | `shell` | 0 | 🔄 2026-09-05 |
| [**herdr-pane-name**](https://github.com/go-min/herdr-pane-name)<br><sub>go-min</sub> | 为你终端会话中的窗格自动命名的 Herdr 插件 | `pane-naming` `terminal` `terminal-multiplexer` `rust` | 0 | 🔄 2026-09-06 |
| [**herdr-looper**](https://github.com/gurronen/herdr-looper)<br><sub>gurronen</sub> | 在全新的 Herdr 工作区和工作树中启动可重复运行的本机 Pi 任务 | `automation` `rust` `terminal` | 0 | 🔄 2026-08-26 |
| [**herdr-worktree-setup**](https://github.com/jtnovellis/herdr-worktree-setup)<br><sub>jtnovellis</sub> | herdr 插件：让新建的 git 工作树立刻可用——复制 .env 和开发状态、克隆依赖缓存（APFS/reflink）、执行 mise trust、direnv allow、安装依赖，并提供实时 TUI | `git-worktree` `rust` | 0 | 🔄 2026-08-29 |
| [**herdr-plugin-auto-rename**](https://github.com/khatriafaz/herdr-plugin-auto-rename)<br><sub>khatriafaz</sub> | 根据 Pi 会话的第一条提示词，自动重命名新的 Herdr 工作区和 Git 分支 | `typescript` | 0 | 2026-08-14 |
| [**herdr-unrecoverable**](https://github.com/neilwashere/herdr-unrecoverable)<br><sub>neilwashere</sub> | 从终端服务商错误中恢复 Pi 编程 Agent 会话的 Herdr 看门狗 | `pi-coding-agent` `javascript` | 0 | 2026-08-14 |
| [**herdr-claude-safe-compact**](https://github.com/tmastalirsch/herdr-claude-safe-compact)<br><sub>tmastalirsch</sub> | herdr 插件：压缩空闲的 Claude Code 窗格，但仅在交接内容已安全落盘之后才会执行 | `claude-code` `compaction` `shell` | 0 | 🔄 2026-08-31 |
| [**herdr-worktreeinclude**](https://github.com/untalfranfernandez/herdr-worktreeinclude)<br><sub>untalfranfernandez</sub> | 为每个新建 git 工作树自动填充所需的、被 gitignore 忽略的本地文件（.env、settings.local.json、fixtures 等）的 Herdr 插件。只需在 .worktreeinclude 文件中用 gitignore 语法声明一次，Herdr 创建的每个工作树都会自动获得这些文件。实现了… | `claude-code` `dotenv` `git-worktree` `worktree` | 0 | 2026-07-29 |
| [**herdr-padio**](https://github.com/vgreg/herdr-padio)<br><sub>vgreg</sub> | 根据 herdr 当前聚焦窗格中运行的应用，自动切换 PadIO 控制器模式 | `game-controller` `macos` `padio` `python` | 0 | 2026-08-02 |
| [**herdr-space-groups**](https://github.com/yojahny55/herdr-space-groups)<br><sub>yojahny55</sub> | herdr 插件：将 Space 分组为带名称、带颜色的组——支持选择器弹窗（鼠标+键盘）、侧边栏分组标题和自动排序 | `javascript` | 0 | 🔄 2026-08-29 |
| [**numberer-manager**](https://github.com/yuritada/numberer-manager)<br><sub>yuritada</sub> | 轻量级 Herdr 插件，自动在工作区和标签页标签前加上其在列表中的当前位置（例如「1: space」「1: tab」） | `python` | 0 | 2026-07-25 |
| [**herdr-pane-restart**](https://github.com/zap0xfce2/herdr-pane-restart)<br><sub>zap0xfce2</sub> | 在服务器启动时，于命名窗格中运行已配置的命令 | `python` | 0 | 2026-08-10 |
| [**herdr-booking-task-plugin**](https://github.com/zerodice0/herdr-booking-task-plugin)<br><sub>zerodice0</sub> | 在 macOS 和 Linux 上调度 Herdr Agent 提示词和本地 CLI 命令 | `golang` `scheduler` `go` | 0 | 2026-08-03 |

<details><summary>与此目的也相关</summary>

- [freethinkel/herdr-plugin-git-worktree-hooks](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks) — 在创建/移除 git 工作树时运行 shell 命令——一份 YAML 配置适用于所有项目，放在任何仓库之外
- [miko-misa/herdr-portfwd](https://github.com/miko-misa/herdr-portfwd) — 面向远程机器上编程 Agent 的自动 SSH 端口转发——Ctrl+点击 Agent 打印的 localhost URL，即可在你本机以相同端口打开该页面。一个 Herdr 插件
- [timofey-TK/herdr-worktree-hooks](https://github.com/timofey-TK/herdr-worktree-hooks) — herdr 插件：在创建、打开或删除 git 工作树时运行自定义的初始化/清理命令
- [itisbryan/herdr-gh-checks](https://github.com/itisbryan/herdr-gh-checks) — herdr 插件：在窗格中监视并查看当前 PR 的 CI，并在侧边栏行中显示 CI/合并状态。使用 Go + Bubble Tea 编写
- [akshat12/herdr-muse](https://github.com/akshat12/herdr-muse) — Herdr integration for Muse Code: idle/working/blocked pane state via lifecycle hooks (no Herdr fork needed)
- [elkraps/herdr-telegram-notify](https://github.com/elkraps/herdr-telegram-notify) — 针对 Herdr Agent 状态变化的可自定义 Telegram 通知——支持状态过滤、模板、多聊天投递、去重、Codex 批准按钮、完成摘要和内置诊断
- [m1sk9/herdr-worktree-hooks-plugin](https://github.com/m1sk9/herdr-worktree-hooks-plugin) — 为 Herdr 的工作树添加可自定义钩子的插件
- [Newt6611/herdr-tab-title](https://github.com/Newt6611/herdr-tab-title) — Herdr Tab Title 会将 Herdr 标签页自动重命名为整洁的、按工作区独立编号的名称，如「1. Codex」「2. Terminal」，格式可自定义

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-session"></a>

## 会话保存与恢复

> 关闭工作后，希望之后能从同一状态继续

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-resurrect**](https://github.com/ntindle/herdr-resurrect)<br><sub>ntindle</sub> | herdr 的 tmux-resurrect——快照工作区、标签页、窗格、当前目录、运行中的程序和 Agent，并在崩溃或重启后恢复 | `crash-recovery` `session-manager` `terminal-multiplexer` `tmux-resurrect` `javascript` | 28 | 🔄 2026-08-24 |
| [**session-digger**](https://github.com/taxueseek/session-digger)<br><sub>taxueseek</sub> | 跨环境会话历史挖掘与知识管理。分析记录。支持 Claude/Grok/Kimi Code/Codex/WorkBuddy/Trae CN 等主流环境 | `claude-code` `conversation-analysis` `jsonl` `knowledge-management` `log-analysis` | 17 | 2026-07-21 |
| [**herdr-notes**](https://github.com/alexarthurs/herdr-notes)<br><sub>alexarthurs</sub> | 面向 herdr 的持久化 Markdown 笔记窗格——每个工作区一份笔记，支持预览渲染+编辑模式，自动保存且重启后仍保留 | `markdown` `notes` `ratatui` `rust` `terminal` | 16 | 2026-07-25 |
| [**herdr-claude-auto-retry**](https://github.com/mo-arvan/herdr-claude-auto-retry)<br><sub>mo-arvan</sub> | 等待 Anthropic 速率限制解除后自动恢复 Claude Code，herdr 原生实现：无需 tmux，无需 shell 包装 | `javascript` | 14 | 🔄 2026-09-03 |
| [**herdr-session-parker**](https://github.com/iviaxpow3r/herdr-session-parker)<br><sub>iviaxpow3r</sub> | 用于暂存窗格/标签页，并在之后恢复受支持的 Agent 会话的 Herdr 插件 | `agent-tools` `python` | 11 | 2026-07-03 |
| [**herdr-agent-inbox**](https://github.com/douglascorrea/herdr-agent-inbox)<br><sub>douglascorrea</sub> | herdr 编程 Agent 的收件箱——会话标题、已读/未读标记、运行时长、工作区汇总、可续接的聊天记录 | `ai-agents` `terminal` `python` | 9 | 2026-07-28 |
| [**herdr-assist**](https://github.com/walcew/herdr-assist)<br><sub>walcew</sub> | 面向 AI 编程 Agent 终端复用器 Herdr 的实体桌面面板——用颜色显示会话状态，当 Agent 停下来请求决策时会响铃提醒。基于 ESP32-S3 + LVGL，提供预编译固件 | `ai-agents` `claude-code` `coding-agents` `embedded` `esp-idf` | 8 | 🔄 2026-08-27 |
| [**sheep**](https://github.com/gokay-ai/sheep)<br><sub>gokay-ai</sub> | 面向 AI 编程 Agent 的撤销功能。Agent 的每一轮操作都会成为一个可恢复的检查点 | `git` `rust` `tui` `undo` | 5 | 🔄 2026-08-28 |
| [**herdr-oh-my-agent**](https://github.com/GavinTomlins/herdr-oh-my-agent)<br><sub>GavinTomlins</sub> | 将 oh-my-openagent 的每个子 Agent 委派实时镜像到独立的 Herdr 窗格或标签页——保留完整会话状态和滚动记录 | `typescript` | 4 | 2026-07-31 |
| [**herdr-pane-id-labeler**](https://github.com/4Born/herdr-pane-id-labeler)<br><sub>4Born</sub> | 让窗格标签与如 w1:p2 之类的公开窗格 ID 保持同步的 Herdr 插件 | `developer-tools` `terminal` `javascript` | 2 | 2026-07-26 |
| [**herdr-hibernate**](https://github.com/bengemine/herdr-hibernate)<br><sub>bengemine</sub> | 让 Herdr 中空闲的编程 Agent 窗格（Claude Code、Codex、Grok）休眠——释放内存，按 Enter 即可恢复原会话 | `claude-code` `python` | 2 | 2026-08-03 |
| [**herdr-synchronize-panes**](https://github.com/furuhashin/herdr-synchronize-panes)<br><sub>furuhashin</sub> | Herdr 插件：将一条命令广播到当前标签页内的所有窗格（类似 tmux 的 synchronize-panes） | `javascript` | 2 | 2026-07-14 |
| [**herdr_sync**](https://github.com/kamaaina/herdr_sync)<br><sub>kamaaina</sub> | 同步 herdr 中的窗格 | `zig` | 2 | 2026-07-01 |
| [**herdr-e2b**](https://github.com/tomasvarga/herdr-e2b)<br><sub>tomasvarga</sub> | 按需将 git 工作树镜像到全新的 E2B 云沙盒——直接上传快照（包括未提交的更改），无需 push 或 clone。一个 herdr 插件 | `cli` `cloud-dev` `e2b` `git-worktree` `sandbox` | 2 | 2026-07-18 |
| [**herdr-thread-to-tab**](https://github.com/toyamarinyon/herdr-thread-to-tab)<br><sub>toyamarinyon</sub> | 让单窗格 Herdr 标签页标签与 Claude Code 和 Codex 的线程标题保持同步 | `rust` | 2 | 2026-08-06 |
| [**herdr-todos-windows**](https://github.com/aclima01/herdr-todos-windows)<br><sub>aclima01</sub> | 实时镜像 herdr Agent 任务列表（TaskCreate/TaskUpdate）的面板，方便你跟踪它的计划 | `powershell` | 1 | 2026-07-22 |
| [**mo-herdr**](https://github.com/momentohq/mo-herdr)<br><sub>momentohq</sub> | 在 herdr 窗格中运行 mo——支持 herdr 重启后的会话恢复、启动操作，以及 SIGKILL 清理 | `python` | 1 | 🔄 2026-09-02 |
| [**herdr-undo-close**](https://github.com/pedroloch/herdr-undo-close)<br><sub>pedroloch</sub> | 如浏览器的 Cmd+Shift+T 一样，在 herdr 中重新打开已关闭的标签页——恢复标签名、含比例的分屏结构、每个窗格的工作目录以及标签页位置 | `python` | 1 | 2026-07-30 |
| [**attic**](https://github.com/TheThoughtagen/attic)<br><sub>TheThoughtagen</sub> | 自动关闭空闲的 AI 编程会话，但会先归档每一个，方便之后恢复 | `claude-code` `developer-tools` `python` `session-management` `tui` | 1 | 2026-08-14 |
| [**herdr-stash**](https://github.com/victor-software-house/herdr-stash)<br><sub>victor-software-house</sub> | 储藏 Herdr 工作区——停止其中的 Agent，同时保留其结构和对话内容，之后可从可点击的双栏弹窗中恢复 | `rust` `terminal` `tui` | 1 | 2026-07-29 |
| [**herdr-agent-pins**](https://github.com/ZingerLittleBee/herdr-agent-pins)<br><sub>ZingerLittleBee</sub> | 将 Herdr Agent 会话持久固定在 Agents 侧边栏顶部 | `terminal` `javascript` | 1 | 🔄 2026-08-24 |
| [**herdr-codex-resume**](https://github.com/adamwangxx/herdr-codex-resume)<br><sub>adamwangxx</sub> | 在保留 Herdr 实时上下文的新分屏中打开原生的 Codex resume 选择器 | `codex-cli` `terminal` `shell` | 0 | 2026-08-21 |
| [**herdr-agent-resume**](https://github.com/Angel-O/herdr-agent-resume)<br><sub>Angel-O</sub> | 插入或复制恢复命令，以便顺畅恢复 AI Agent 会话的 Herdr 插件 | `rust` | 0 | 2026-08-15 |
| [**herdr-suspend-workspace**](https://github.com/asermax/herdr-suspend-workspace)<br><sub>asermax</sub> | 挂起 herdr 工作区——将布局和 Agent 快照后关闭，之后可从弹出选择器中恢复 | `typescript` | 0 | 2026-07-31 |
| [**herdr-plugin-session-pruner**](https://github.com/Gareth-Rouse/herdr-plugin-session-pruner)<br><sub>Gareth-Rouse</sub> | herdr 插件：记录工作区的最后使用时间，在 Spaces 侧边栏中显示已过去多久，并将闲置工作区排除在会话恢复之外 | `terminal-multiplexer` `shell` | 0 | 2026-08-07 |
| [**herdr-flakes**](https://github.com/iQua/herdr-flakes)<br><sub>iQua</sub> | Herdr 的 Flakes 插件——将你的 Flakes 运行镜像到本地 Herdr 会话并进行操控 | `javascript` | 0 | 2026-07-22 |
| [**herdr-session-title-name**](https://github.com/jovylle/herdr-session-title-name)<br><sub>jovylle</sub> | herdr 插件：将 terminal_title_stripped 持久化到标签页（顶部只保留 session_title，标签页关闭后依然保留该标题） | `sidebar` `terminal` `html` | 0 | 🔄 2026-08-28 |
| [**herdr-plugin-vault**](https://github.com/Joxtacy/herdr-plugin-vault)<br><sub>Joxtacy</sub> | 在 herdr 弹窗中浏览过去的 Claude Code 会话，并在新标签页中恢复所选的那个 | `shell` | 0 | 2026-08-11 |
| [**herdr-ccs**](https://github.com/KennethWKZ/herdr-ccs)<br><sub>KennethWKZ</sub> | 让 `ccs claude` 在 Herdr 中表现得如同原生 Claude Code——支持窗格检测，以及通过 ccs 实现的、感知启动方式的会话恢复 | `shell` | 0 | 🔄 2026-08-29 |
| [**🆕 herdr-checkpoint**](https://github.com/lancodev/herdr-checkpoint)<br><sub>lancodev</sub> | herdr 版的 tmux-resurrect——精确保存会话检查点并可还原，还原时会关闭不在检查点中的内容。 | `tmux-resurrect` `tui` `shell` | 0 | 🔄 2026-09-02 |
| [**herdr-layout**](https://github.com/noviadi/herdr-layout)<br><sub>noviadi</sub> | 保存并重放 Herdr 窗格布局——面向 Herdr 终端复用器的配套插件（tmux-resurrect 风格） | `cli` `terminal` `tmux-resurrect` `shell` | 0 | 2026-08-13 |
| [**🆕 herdr-park-agents**](https://github.com/rrg/herdr-park-agents)<br><sub>rrg</sub> | Park a coding-agent pane in herdr: stop the process, close the pane, and resume the session later from a workspace panel. | `agent-tools` `python` | 0 | 🔄 2026-09-07 |
| [**🆕 herdr-tab-new**](https://github.com/softwarecrafts/herdr-tab-new)<br><sub>softwarecrafts</sub> | 在此项目的 herdr 工作区中恢复或启动一个 Agent 会话——既是 herdr 插件，也是可在 herdr 之外的终端使用的 CLI。 | `typescript` | 0 | 🔄 2026-08-31 |
| [**🆕 herdr-restore-notice**](https://github.com/victor-software-house/herdr-restore-notice)<br><sub>victor-software-house</sub> | Compact Herdr restore notices with click-to-resume agent sessions | `typescript` | 0 | 🔄 2026-09-05 |
| [**herdr-event-log**](https://github.com/waynewu411/herdr-event-log)<br><sub>waynewu411</sub> | herdr 插件：将 pane.agent_status_changed（以及未来的其他事件类型）记录到一份持久化、可从游标恢复的全局日志中，任何父 Agent 都可以 tail 它 | `shell` | 0 | 🔄 2026-08-24 |
| [**live-sync-panes**](https://github.com/wg1k/live-sync-panes)<br><sub>wg1k</sub> | Herdr 插件：将命令广播，或将按键实时同步到标签页内的所有窗格 | `javascript` | 0 | 2026-08-11 |

<details><summary>与此目的也相关</summary>

- [nicosuave/memex](https://github.com/nicosuave/memex) — 搜索 Claude Code、Codex、Pi、OpenCode、GitHub Copilot 和 Cursor 的会话记录。恢复会话。追踪 token 使用
- [KokiKono/herdr-kanban](https://github.com/KokiKono/herdr-kanban) — 将任务与 herdr 标签页关联的终端看板，数据持久化在 SQLite 中
- [afogel/shepherdr](https://github.com/afogel/shepherdr) — 将委派出去的编程 Agent 收拢到可见、可审查的 herdr 窗格中，供你观察、恢复和接管的 herdr 插件
- [AkashJana18/herdr-scratch](https://github.com/AkashJana18/herdr-scratch) — 面向 Herdr 的持久化速记板，为浮动实用窗格铺路
- [voodootikigod/adlc-herdr](https://github.com/voodootikigod/adlc-herdr) — ADLC 的 herdr 插件——按窗格显示阶段/工单/关卡状态，附带待办看板、关卡操作和 adlc-fleet 运行可观测性。是 voodootikigod/adlc/plugins/adlc-herdr 的自动同步…
- [blaxel-ai/herdr-blaxel-sandbox-plugin](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin) — 从 Herdr 在持久化的 Blaxel Sandbox 中运行编程 Agent
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — 为 JavaScript 和 TypeScript 自动初始化 Herdr 工作树，支持基于锁文件的安装和安全的环境变量还原
- [ppggff/herdr-plugin](https://github.com/ppggff/herdr-plugin) — 自动记住并恢复每个 Herdr 窗格对应的正确 macOS 输入法（IME）
- [shadowfax92/herdr-scratch](https://github.com/shadowfax92/herdr-scratch) — 由私有 tmux 会话支撑的、按窗格持久化的 Herdr 便签弹窗
- [damianpoole/herdr-opencode-sessions](https://github.com/damianpoole/herdr-opencode-sessions) — 可按标题、项目、路径、日期或会话记录内容对过去的 OpenCode 会话进行模糊搜索的 Herdr 插件——带会话预览，并提供在当前或新工作区中恢复/分叉会话的快捷方式
- [goofansu/herdr-hunk](https://github.com/goofansu/herdr-hunk) — 提供快速的 Herdr 评审操作，打开一个临时的 Hunk 浮层。退出 Hunk 会关闭浮层并恢复你的工作区

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-naming"></a>

## 标题、命名与外观

> 想让标签页名称和终端标题自动变得清晰易懂，或想改变外观

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-tab-smart-rename**](https://github.com/iurysza/herdr-tab-smart-rename)<br><sub>iurysza</sub> | 为 Herdr 生成基于上下文的工作区和标签页名称 | `ai` `bun` `terminal` `typescript` | 69 | 🔄 2026-09-06 |
| [**herdr-window-title-sync**](https://github.com/rjyo/herdr-window-title-sync)<br><sub>rjyo</sub> | 将工作区、标签页和 Agent 会话同步到终端标题（可配合 Moshi 使用） | `moshi` `terminal-title` `javascript` | 35 | 2026-06-26 |
| [**herdr-flock**](https://github.com/ragamo/herdr-flock)<br><sub>ragamo</sub> | 将你的 AI 编程 Agent 可视化为生活在俯视视角农场里的像素风羊群的 herdr 插件 | `cli` `ratatui` `rust` `tui` | 31 | 🔄 2026-08-31 |
| [**herdr-claude-session-title**](https://github.com/bcihanc/herdr-claude-session-title)<br><sub>bcihanc</sub> | Herdr 插件：将 Claude Code 的会话标题（/rename 或自动摘要）同步到 herdr 窗格的元数据标题中 | `shell` | 8 | 2026-07-11 |
| [**herdr-canvas**](https://github.com/aorumbayev/herdr-canvas)<br><sub>aorumbayev</sub> | 面向 herdr Agent 的鼠标驱动 ASCII 图表画布——在 TUI 中绘制，分享结构化 JSON，还可以让 AI 编辑它 | `agentic-ai` `agents` `ai-agents` `ascii-art` `bubbletea` | 7 | 🔄 2026-08-31 |
| [**herdr-icon-agent-ui**](https://github.com/qintmb/herdr-icon-agent-ui)<br><sub>qintmb</sub> | 在 Herdr 侧边栏中渲染纵向对齐的单色 Agent 图标。通过自定义字体渲染，字形按终端 cap-height 进行非均匀缩放，与 Agent 名称、标签页和工作区标签紧密贴合，而不是显示为小方块 | `python` | 7 | 2026-08-20 |
| [**herdr-pet**](https://github.com/allmight-ai/herdr-pet)<br><sub>allmight-ai</sub> | Herdr 的伴侣电子宠物——映射你的编程 Agent 的状态 | `companion` `rust` `v-pet` | 6 | 2026-08-20 |
| [**herdr-theme-picker**](https://github.com/qintmb/herdr-theme-picker)<br><sub>qintmb</sub> | 基于终端配色方案和自定义设置的 herdr UI 主题选择器 | `shell` | 6 | 🔄 2026-08-31 |
| [**herdr-town**](https://github.com/Efeguclu1/herdr-town)<br><sub>Efeguclu1</sub> | 把你的 Herdr 编程 Agent 当作一座 8 位像素小镇来观赏。无需离开，就能阅读并回复它们 | `ai-agents` `pixel-art` `terminal` `tui` `javascript` | 5 | 2026-08-08 |
| [**herdr-ghostty-tab-title**](https://github.com/wjarka/herdr-ghostty-tab-title)<br><sub>wjarka</sub> | herdr 插件：在 Ghostty 标签标题中按颜色显示 Agent 各状态（阻塞/完成/工作中/空闲）的数量 | `ai-agents` `ghostty` `terminal` `python` | 5 | 2026-08-04 |
| [**herdr-in-your-face**](https://github.com/JYasha11/herdr-in-your-face)<br><sub>JYasha11</sub> | 如果你放着被阻塞的 AI Agent 不管，一个巨大的 ASCII 脸会对你怒吼。你无视得越久，警告就升级得越厉害 | `javascript` | 4 | 2026-07-10 |
| [**herdr-auto-namer**](https://github.com/kakigakki/herdr-auto-namer)<br><sub>kakigakki</sub> | herdr 的 ChatGPT 风格自动命名：Agent 使用其 Claude 会话标题，工作区使用其工作目录名 | `claude-code` `python` | 4 | 🔄 2026-08-27 |
| [**herdr-tab-rename**](https://github.com/lmilojevicc/herdr-tab-rename)<br><sub>lmilojevicc</sub> | 将每个 Herdr 标签页自动重命名为其聚焦窗格的工作目录名。手动重命名过的标签页不受影响 | `go` | 4 | 2026-07-31 |
| [**herdr-pet**](https://github.com/nikok6/herdr-pet)<br><sub>nikok6</sub> | 生活在 herdr 窗格中的小小桌面宠物——陪你的 Agent 一起打字、等待和庆祝。兼容任意 Codex pet | `rust` | 4 | 🔄 2026-08-26 |
| [**herdr-questmancer**](https://github.com/opsydyn/herdr-questmancer)<br><sub>opsydyn</sub> | 为你的 Herdr 编程 Agent 打造的温馨 16 位冒险者公会。工作中的 Agent 在探索地下城，被阻塞的 Agent 在寻求指点，完成的工作则带着战利品归来 | `coding-agents` `pixel-art` `ratatui` `tui` `rust` | 4 | 2026-08-11 |
| [**herdr-nerd-font-tab-name**](https://github.com/rohankewal/herdr-nerd-font-tab-name)<br><sub>rohankewal</sub> | 为 herdr 标签页添加 Nerd Font 图标——joshmedeski/tmux-nerd-font-window-name 的 herdr 移植版 | `nerd-fonts` `python` `terminal` `tui` | 4 | 2026-07-31 |
| [**🆕 herdr-agent-titler**](https://github.com/killerz3/herdr-agent-titler)<br><sub>killerz3</sub> | 无需外部 API key，使用本地的 agy、claude、codex 或 opencode 运行环境，自动为 Herdr 标签页设置标题。 | `antigravity` `claude-code` `python` | 3 | 🔄 2026-09-03 |
| [**🆕 herdr-pets**](https://github.com/abhishek944/herdr-pets)<br><sub>abhishek944</sub> | 以一个透明的桌面村庄，展示正在运行的 Herdr Agent。 | `typescript` | 2 | 🔄 2026-08-31 |
| [**herdr-titles**](https://github.com/davidolrik/herdr-titles)<br><sub>davidolrik</sub> | 始终跟得上变化的 Herdr 标题。herdr-titles 会根据实际运行的内容（包括 AI Agent 的实时会话标题）为标签页和窗口命名，并通过一个小型 HCL 模板，从工作区、标签页、Agent 待处理数量和 shell 环境组合出窗口标题。即时生效，CPU 占用近乎为零。零配置即可开始使用，且可无限调整 | `ai-assisted` `go` | 2 | 🔄 2026-09-06 |
| [**herdr-english-coach**](https://github.com/GranamyrBR/herdr-english-coach)<br><sub>GranamyrBR</sub> | herdr 插件：彩色标注的英语纠错面板——在你工作时，编程 Agent 将语法和开发行话的修正实时记录到侧边窗格 | `english` `language-learning` `shell` | 2 | 2026-07-06 |
| [**herdr-ai-tab-name**](https://github.com/ndom91/herdr-ai-tab-name)<br><sub>ndom91</sub> | 使用本地 LLM 自动为 Herdr 标签页命名 | `local-llm` `python` | 2 | 2026-08-05 |
| [**herdr-powershell-title-sync**](https://github.com/aclima01/herdr-powershell-title-sync)<br><sub>aclima01</sub> | window-title-sync 的 Windows/PowerShell 移植版：将终端标题同步为当前聚焦的 herdr 会话 | `powershell` | 1 | 2026-07-20 |
| [**herdr-git-tab-name**](https://github.com/blurname/herdr-git-tab-name)<br><sub>blurname</sub> | 将标签页重命名为聚焦窗格所在 Git 分支名的 Herdr 插件 | `shell` | 1 | 2026-07-06 |
| [**herdr-hermes-session-title**](https://github.com/btorresgil/herdr-hermes-session-title)<br><sub>btorresgil</sub> | 在 Herdr 侧边栏中显示 Hermes Agent 的会话标题 | `python` | 1 | 2026-08-07 |
| [**herdr-tab-smart-rename-rs**](https://github.com/EmmetZ/herdr-tab-smart-rename-rs)<br><sub>EmmetZ</sub> | _(暂无描述)_ | `rust` | 1 | 🔄 2026-08-24 |
| [**🆕 herdr-emoji-time**](https://github.com/hotnugs/herdr-emoji-time)<br><sub>hotnugs</sub> | Emoji for your Herdr spaces, agents and tabs. Inject some fun into your terminal | `emoji` `terminal` `tui` `python` | 1 | 🔄 2026-09-04 |
| [**herdr-tab-title-sync**](https://github.com/lucasleon2107/herdr-tab-title-sync)<br><sub>lucasleon2107</sub> | 将标签页名称同步为 AI Agent 对话标题的 herdr 插件 | `ai-agents` `claude-code` `terminal` `tmux` `shell` | 1 | 2026-08-04 |
| [**herdr-session-sync**](https://github.com/nengqi/herdr-session-sync)<br><sub>nengqi</sub> | 将 Claude Code、Codex 和 Agent 的会话名称，自动同步到 Herdr 窗格标签、PTY 窗口标题和移动配套应用（Heeler）之间 | `agent` `claude-code` `codex` `heeler` `terminal-multiplexer` | 1 | 🔄 2026-09-07 |
| [**herdr-nerd-font-tab-name-windows**](https://github.com/Only-Moon/herdr-nerd-font-tab-name-windows)<br><sub>Only-Moon</sub> | herdr-nerd-font-tab-name 的 Windows 移植版：为 herdr 标签页显示 Nerd Font 图标，跨平台支持 Windows、macOS、Linux，并支持按文件夹解析图标 | `herdr-windows` `icons` `nerd-fonts` `python` `title` | 1 | 2026-08-10 |
| [**🆕 omarchy-crook**](https://github.com/parker-brown-family/omarchy-crook)<br><sub>parker-brown-family</sub> | Crook — which coding agent needs you, on the Omarchy bar. One icon that goes urgent the moment something is waiting on you, and a tray that says who. | `agents` `bar-widget` `claude-code` `hyprland` `omarchy` | 1 | 🔄 2026-09-06 |
| [**herdr-tab-renamer**](https://github.com/ryanlewis/herdr-tab-renamer)<br><sub>ryanlewis</sub> | herdr 插件：根据标签页的实际内容（Agent 会话标题和 shell 目录）为其打标签 | `javascript` | 1 | 2026-08-08 |
| [**herdr-claude-tab-title**](https://github.com/tmn73/herdr-claude-tab-title)<br><sub>tmn73</sub> | 将每个 Claude Code 会话标题及其 Agent 状态同步到对应的 Herdr 标签页 | `claude-code` `tabs` `terminal` `typescript` | 1 | 🔄 2026-08-27 |
| [**workspace-basename**](https://github.com/42lizard/workspace-basename)<br><sub>42lizard</sub> | 根据创建工作区时所在目录的基名来设置工作区名称的 herdr 插件 | `shell` | 0 | 🔄 2026-08-27 |
| [**herdr-habitat**](https://github.com/chantlong/herdr-habitat)<br><sub>chantlong</sub> | herdr habitat 是一个随 Agent 工作而成长的「活的」终端生态系统。培育需要时间，所以请不要过度堆砌 Agent。讽刺的是，当 Agent 在损害生态的高耗能数据中心里燃烧 token 时，herdr habitat 却在培育虚拟植物、吸引虚拟野生动物 | `chill` `cozy` `javascript` | 0 | 2026-08-16 |
| [**herdr-tab-title-from-terminal**](https://github.com/christiangroth/herdr-tab-title-from-terminal)<br><sub>christiangroth</sub> | 为每个 Herdr 标签页命名为其内部 Agent 的终端标题。在 Claude Code 中执行一次 /rename，会同时为会话和标签页命名。手动命名过的标签页则不受影响 | `python` | 0 | 🔄 2026-08-25 |
| [**herdr-llm-summary-header**](https://github.com/dnf0/herdr-llm-summary-header)<br><sub>dnf0</sub> | herdr 插件：Agent 完成后，将 LLM 生成的一行摘要写入窗格标题 | `javascript` | 0 | 2026-08-03 |
| [**herdr-smart-rename**](https://github.com/edouard-andrei/herdr-smart-rename)<br><sub>edouard-andrei</sub> | herdr 插件：根据 Agent 会话记录，用 AI 为标签页和窗格命名——按一个键即可，支持任意 OpenAI 兼容模型 | `javascript` | 0 | 2026-08-20 |
| [**herdr-title-sync**](https://github.com/elKei24/herdr-title-sync)<br><sub>elKei24</sub> | herdr 插件：将每个 Agent 的终端标题同步到其标签页标签上 | `python` | 0 | 🔄 2026-09-01 |
| [**🆕 herdr-kitty-theme-sync**](https://github.com/enisbu/herdr-kitty-theme-sync)<br><sub>enisbu</sub> | 把 Herdr 当前使用的主题同步到 kitty 的 ANSI 调色板，使窗格内容与 Herdr 的外观保持一致。 | `kitty` `linux` `terminal` `theme` `shell` | 0 | 🔄 2026-09-03 |
| [**🆕 herdr-pane-id-border**](https://github.com/Haichiu/herdr-pane-id-border)<br><sub>Haichiu</sub> | 一个极简的 Herdr 插件，在窗格边框上显示规范的窗格 ID。 | `shell` | 0 | 🔄 2026-09-02 |
| [**🆕 herdr-sheep**](https://github.com/huketo/herdr-sheep)<br><sub>huketo</sub> | 把 Herdr 的编码 Agent 变成一群会动的 ASCII 羊，供你观赏。 | `ascii-art` `rust` `tui` | 0 | 🔄 2026-09-04 |
| [**herdr-tab-session-name-sync**](https://github.com/itayo-m/herdr-tab-session-name-sync)<br><sub>itayo-m</sub> | 将 Agent 会话名称同步到 herdr 的标签页和窗格标题 | `developer-tools` `github-copilot` `terminal` `javascript` | 0 | 2026-08-03 |
| [**herdr-chromatic-spaces**](https://github.com/jackfrancisdalton/herdr-chromatic-spaces)<br><sub>jackfrancisdalton</sub> | 为每个 Herdr Space 赋予专属颜色和表情符号——彩色侧边栏圆点、Agent 分组，以及切换 Space 时可选的界面着色 | `python` | 0 | 2026-08-22 |
| [**🆕 herdr-tab-titles**](https://github.com/kewah/herdr-tab-titles)<br><sub>kewah</sub> | 根据发给编码 Agent 的第一条提示词，为窗格和标签页命名的 Herdr 插件。 | `javascript` | 0 | 🔄 2026-09-06 |
| [**herdr-tab-numbers**](https://github.com/kokatsu/herdr-tab-numbers)<br><sub>kokatsu</sub> | 在每个标签页名称前加上其 switch_tab 位置编号 | `shell` | 0 | 🔄 2026-08-26 |
| [**herdr-window-title**](https://github.com/mackt/herdr-window-title)<br><sub>mackt</sub> | 面向 herdr 的可配置外层终端标题——模板驱动、感知会话，并实时显示 Agent 状态（阻塞/完成/工作中） | `rust` | 0 | 2026-08-03 |
| [**herdr-agent-smart-rename**](https://github.com/malone-c/herdr-agent-smart-rename)<br><sub>malone-c</sub> | 根据每个 herdr Agent 会话实际在做的事情为其命名 | `python` | 0 | 2026-08-14 |
| [**herdr-machine-title**](https://github.com/mikevalstar/herdr-machine-title)<br><sub>mikevalstar</sub> | herdr 插件：将外层终端标题固定为 herdr@<主机名> · <工作区> | `shell` | 0 | 2026-07-02 |
| [**🆕 herdr-tab-title**](https://github.com/Newt6611/herdr-tab-title)<br><sub>Newt6611</sub> | Herdr Tab Title 会将 Herdr 标签页自动重命名为整洁的、按工作区独立编号的名称，如「1. Codex」「2. Terminal」，格式可自定义 | `rust` | 0 | 2026-07-09 |
| [**🆕 herdr-display-workspace**](https://github.com/RickyMarou/herdr-display-workspace)<br><sub>RickyMarou</sub> | Herdr 插件：在标签栏右侧显示当前工作区名称。 | `shell` | 0 | 🔄 2026-09-03 |
| [**tab-blank-number**](https://github.com/riq0h/tab-blank-number)<br><sub>riq0h</sub> | 将 herdr 默认的数字标签页标签（1、2、3…）清空为空白的 herdr 插件 | `javascript` | 0 | 2026-07-19 |
| [**tab-process-name**](https://github.com/riq0h/tab-process-name)<br><sub>riq0h</sub> | 为每个标签页标注其前台运行进程名称的 herdr 插件——相当于把 tmux 的 automatic-rename 行为带到 herdr | `javascript` | 0 | 2026-07-19 |
| [**herdr-workspace-renamer**](https://github.com/ryanlewis/herdr-workspace-renamer)<br><sub>ryanlewis</sub> | herdr 插件：将 Agent 会话名称同步到工作区标签 | `javascript` | 0 | 2026-08-08 |
| [**herdr-codex-session-title**](https://github.com/sergeybataev/herdr-codex-session-title)<br><sub>sergeybataev</sub> | 将 Codex 聊天标题同步为 Agent 名称的 Herdr 插件 | `codex` `python` | 0 | 2026-08-01 |
| [**🆕 herdr-plugins**](https://github.com/shubham-cpp/herdr-plugins)<br><sub>shubham-cpp</sub> | 用于标签页/Agent 命名以及方向键窗格聚焦的 Herdr 插件合集。 | `rust` | 0 | 🔄 2026-09-03 |
| [**herdr-title-wrap**](https://github.com/T0mSIlver/herdr-title-wrap)<br><sub>T0mSIlver</sub> | herdr 插件：将 Claude Code 会话标题在侧边栏中换行显示为多行，并自动适应侧边栏宽度 | `python` | 0 | 2026-08-06 |
| [**herdr-agent-session-title**](https://github.com/the-inconvenience-store/herdr-agent-session-title)<br><sub>the-inconvenience-store</sub> | 将 Claude Code 或 Codex 的会话标题（/rename 或自动摘要）同步到 herdr 窗格元数据标题的 Herdr 插件 | `python` | 0 | 🔄 2026-09-05 |
| [**herdr-ghostty-theme-sync**](https://github.com/themuuln/herdr-ghostty-theme-sync)<br><sub>themuuln</sub> | 让 herdr 的主题和侧边栏配色跟随当前使用的 Ghostty 主题——即使 herdr 重启，侧边栏的配色 token 也会保留。herdr.dev 出品的插件 | `python` | 0 | 2026-08-12 |
| [**tabby**](https://github.com/yersonargotev/tabby)<br><sub>yersonargotev</sub> | 为聚焦标签页打上「关键命令」或「工作目录名」标签的 Herdr 插件 | `rust` | 0 | 2026-08-20 |
| [**herdr-auto-session-title**](https://github.com/zhangzujian/herdr-auto-session-title)<br><sub>zhangzujian</sub> | 生成简洁的 Herdr 窗格标题，并与原生 Codex 会话名称保持同步 | `javascript` | 0 | 2026-07-30 |

<details><summary>与此目的也相关</summary>

- [kryptamine/herdr-auto-title](https://github.com/kryptamine/herdr-auto-title) — 自动跟随每个标签页中工作内容变化的标签标题。借助 Herdr 让标签页保持整洁，一眼就知道自己在做什么。
- [qu8n/herdr-automatic-rename](https://github.com/qu8n/herdr-automatic-rename) — Smart tab names and numbered labels for a smooth herdr navigation
- [sh1ma/herdr-auto-title](https://github.com/sh1ma/herdr-auto-title) — 根据 Claude Code 和 Codex 的对话内容，自动生成 herdr 标签页标题
- [wyattjoh/herdr-plugin-renamer](https://github.com/wyattjoh/herdr-plugin-renamer) — 根据 Agent 的第一条提示词，重命名自动生成的 herdr 工作树分支和工作区（通过设备端 Apple FoundationModels 或 Codex）
- [ythx-101/herdr-social-glass](https://github.com/ythx-101/herdr-social-glass) — 面向 macOS 版 Herdr 的、适合截图分享的 Social Glass 主题与工作流插件
- [aarsh21/herdr-tab-title](https://github.com/aarsh21/herdr-tab-title) — 为 Herdr 提供类似 tmux 的自动标签页标题
- [IvoryHeart/herdr-world](https://github.com/IvoryHeart/herdr-world) — Herdr World——面向 Herdr 的多界面网页体验
- [funsaized/herdr-mise](https://github.com/funsaized/herdr-mise) — 运行的是「一轮」，而不是提示词 🧑‍🍳 面向 herdr 中 Agent 的可视化工具
- [suisya-systems/herdr-agent-office](https://github.com/suisya-systems/herdr-agent-office) — 将你的 Agent 团队呈现为像素风办公室的 herdr 插件。查看谁在工作、谁卡住了，并可直接跳转过去
- [maedana/herdr-whereami](https://github.com/maedana/herdr-whereami) — 自动重命名标签页以显示你当前所在位置的 Herdr 插件——在 git 仓库内会显示为「仓库名/分支名」
- [dev-shimada/herdr-auto-tab-name](https://github.com/dev-shimada/herdr-auto-tab-name) — herdr 插件：根据当前目录自动命名标签页
- [winoooops/herdr-agent-title-sync](https://github.com/winoooops/herdr-agent-title-sync) — 为 Claude Code、Codex、Kimi Code、OpenCode 等编程 Agent 提供的 Herdr 窗格标题自动同步
- [eduardoborges/herdr-claude-title-hook](https://github.com/eduardoborges/herdr-claude-title-hook) — 将会话标题同步到 Herdr 标签页标题的 Claude Code 插件
- [filoozom/herdr-title](https://github.com/filoozom/herdr-title) — 在终端标签页标题中显示所选工作树和 Agent 活动状态的 Herdr 插件
- [go-min/herdr-pane-name](https://github.com/go-min/herdr-pane-name) — 为你终端会话中的窗格自动命名的 Herdr 插件
- [jovylle/herdr-session-title-name](https://github.com/jovylle/herdr-session-title-name) — herdr 插件：将 terminal_title_stripped 持久化到标签页（顶部只保留 session_title，标签页关闭后依然保留该标题）
- [KazBrekker1/herdr-hasr](https://github.com/KazBrekker1/herdr-hasr) — Hasr（حصر——意为「枚举、完整清点」）——herdr 的 goto 风格弹窗切换器：切换、重命名、删除并创建 Agent、标签页和空间，并实时追踪完成状态
- [khatriafaz/herdr-plugin-auto-rename](https://github.com/khatriafaz/herdr-plugin-auto-rename) — 根据 Pi 会话的第一条提示词，自动重命名新的 Herdr 工作区和 Git 分支
- [maxBRT/herdr-omarchy-theme-sync](https://github.com/maxBRT/herdr-omarchy-theme-sync) — 将 Herdr 的 UI 配色与当前使用的 Omarchy 主题同步
- [ralphilius/herdr-pr-tab-renamer](https://github.com/ralphilius/herdr-pr-tab-renamer) — 根据检测到的拉取请求编号重命名标签页的 Herdr 插件

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-text"></a>

## 文本与 URL 提取

> 想不用鼠标就抓取屏幕上显示的字符串、路径或 URL

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-pluck**](https://github.com/rmarganti/herdr-pluck)<br><sub>rmarganti</sub> | 从 Herdr 窗格中快速复制匹配特定模式的字符串 | `rust` | 23 | 2026-08-07 |
| [**herdr-tiny-fingers**](https://github.com/hotchpotch/herdr-tiny-fingers)<br><sub>hotchpotch</sub> | 面向 Herdr 的 tmux-fingers 风格可见屏幕复制提示 | `tools` `rust` | 9 | 2026-08-04 |
| [**herdr-scratchpad**](https://github.com/vjeantet/herdr-scratchpad)<br><sub>vjeantet</sub> | 每个标签页一个缓冲区用于准备提示词，一键即可投递到 Agent 的输入框 | `clipboard` `ratatui` `rust` `scratchpad` `terminal` | 5 | 🔄 2026-08-31 |
| [**herdr-fingers**](https://github.com/hitaishi2222/herdr-fingers)<br><sub>hitaishi2222</sub> | Fingers to clipboard：从当前窗格中拾取信息的智能浮层 | `python` | 4 | 2026-07-16 |
| [**herdr-copy-search**](https://github.com/qq88976321/herdr-copy-search)<br><sub>qq88976321</sub> | 面向 herdr 回滚缓冲区的正则表达式和 copycat 模式搜索，配合 extrakto 令牌提取，落地到 tmux 风格的复制模式（OSC 52） | `copy-mode` `rust` `terminal` `tmux` | 3 | 2026-08-04 |
| [**herdr-flash**](https://github.com/youguanxinqing/herdr-flash)<br><sub>youguanxinqing</sub> | 面向 Herdr 窗格的 flash.nvim 风格搜索、选择与复制 | `rust` `terminal` | 3 | 🔄 2026-09-02 |
| [**herdr-agent-copy-paste-fork**](https://github.com/calebcauthon/herdr-agent-copy-paste-fork)<br><sub>calebcauthon</sub> | 只需复制粘贴即可分叉，或用快捷键将分叉分到新窗格 | `claude-code` `codex` `shell` | 2 | 2026-07-24 |
| [**herdr-paste-image**](https://github.com/ddfonseca/herdr-paste-image)<br><sub>ddfonseca</sub> | 将剪贴板中的图片以文件路径形式粘贴到 herdr 窗格——tmux-paste-image 的 herdr 移植版 | `shell` | 2 | 2026-07-30 |
| [**herdr-s3-clipboard**](https://github.com/jagzmz/herdr-s3-clipboard)<br><sub>jagzmz</sub> | 使用 S3 兼容存储，将 Herdr 中剪贴板的图片发布为可复用的公开链接或预签名链接 | `aws-s3` `clipboard` `cloudflare-r2` `developer-tools` `image-publishing` | 2 | 2026-07-16 |
| [**herdr-ferry**](https://github.com/wavrin/herdr-ferry)<br><sub>wavrin</sub> | 通过 SSH 在 Herdr 所在机器和你的笔记本电脑之间传输文件和剪贴板内容——无需云存储桶 | `rust` | 2 | 🔄 2026-08-29 |
| [**herdr-scrollback-capture**](https://github.com/alexjsp/herdr-scrollback-capture)<br><sub>alexjsp</sub> | 将聚焦窗格的回滚缓冲区以 HTML 或文本形式保存到桌面的 Herdr 插件 | `shell` | 1 | 2026-06-30 |
| [**herdr-leap**](https://github.com/RooseveltAdvisors/herdr-leap)<br><sub>RooseveltAdvisors</sub> | 面向 Herdr 终端多路复用器的 EasyMotion/leap 风格字符跳转+选中复制 | `easymotion` `rust` `terminal` `tui` | 1 | 2026-07-24 |
| [**herdr-copy-hints**](https://github.com/rotemb-wond/herdr-copy-hints)<br><sub>rotemb-wond</sub> | 面向 Herdr 的 tmux-fingers 风格键盘复制提示：路径、Git SHA、URL 等 | `clipboard` `developer-tools` `keyboard-navigation` `productivity` `terminal` | 1 | 2026-07-23 |
| [**🆕 scoopr**](https://github.com/TawfiqAbubaker/scoopr)<br><sub>TawfiqAbubaker</sub> | Herdr plugin for copying anything to the terminal without using the mouse, inspired by extrakto for tmux. | `rust` | 1 | 🔄 2026-09-06 |
| [**herdr-translate**](https://github.com/zackshen/herdr-translate)<br><sub>zackshen</sub> | herdr 插件：在居中弹出层中翻译鼠标选中的终端文本 | `rust` | 1 | 🔄 2026-08-25 |
| [**herdr-quickselect**](https://github.com/choplin/herdr-quickselect)<br><sub>choplin</sub> | 在 Herdr 中选中可见的终端文本，并执行可配置的操作 | `go` | 0 | 🔄 2026-08-24 |
| [**herdr-flash**](https://github.com/codingfragments/herdr-flash)<br><sub>codingfragments</sub> | 将 zellij-flash（Zellij 插件）移植为原生 Herdr 插件 | `rust` | 0 | 🔄 2026-08-26 |
| [**herdr-zextract**](https://github.com/codingfragments/herdr-zextract)<br><sub>codingfragments</sub> | 将 zextract（Zellij 插件）移植为原生 Herdr 插件 | `rust` | 0 | 2026-08-18 |
| [**herdr-vaultr**](https://github.com/connerohnesorge/herdr-vaultr)<br><sub>connerohnesorge</sub> | vaultr 的官方 herdr 插件——从运行 Agent 会话的窗格中，对已捕获的会话进行复制、查看、分叉和搜索 | `vaultr` `shell` | 0 | 2026-08-13 |
| [**herdr-context-locator**](https://github.com/Dimon94/herdr-context-locator)<br><sub>Dimon94</sub> | 复制一个可自我描述的定位符，指向 Herdr Agent 的规范原生会话上下文 | `python` | 0 | 🔄 2026-08-26 |
| [**🆕 herdr-agent-links**](https://github.com/OmarDadabhoy/herdr-agent-links)<br><sub>OmarDadabhoy</sub> | 在 Herdr 中打开隐藏在 Codex 和 Claude 输出的 Markdown 标签背后的链接。 | `claude-code` `codex` `productivity` `terminal` `python` | 0 | 🔄 2026-09-02 |
| [**herdr-thumbs**](https://github.com/sd2k/herdr-thumbs)<br><sub>sd2k</sub> | Herdr 版的 tmux-thumbs——通过提示选取屏幕上的任意内容，进行复制、粘贴或打开 | `tmux-thumbs` `shell` | 0 | 2026-08-21 |
| [**🆕 herdr-copy-conversation**](https://github.com/testy-cool/herdr-copy-conversation)<br><sub>testy-cool</sub> | 在 Herdr 中，可将完整的终端回滚内容或与 Agent 的对话直接复制到剪贴板。 | `ai-agents` `claude-code` `clipboard` `codex` `developer-tools` | 0 | 🔄 2026-09-03 |
| [**herdr-lens**](https://github.com/VoidAxon/herdr-lens)<br><sub>VoidAxon</sub> | 在 Herdr 窗格中选中文本，按一个键即可用你自己的语言阅读——支持翻译、词典查询、标识符查找和摘要，仅依赖标准库，零配置 | `ai` `cli` `terminal` `translation` `python` | 0 | 🔄 2026-08-25 |
| [**herdr-translate**](https://github.com/wenPKtalk/herdr-translate)<br><sub>wenPKtalk</sub> | herdr 插件：用 translate-shell 翻译窗格中选中的文本，并以浮动弹窗显示（支持 macOS 和 Linux） | `translate` `shell` | 0 | 2026-08-19 |
| [**herdr-copy-pane-id**](https://github.com/wine-fall/herdr-copy-pane-id)<br><sub>wine-fall</sub> | herdr 插件：将聚焦窗格的 ID 复制到剪贴板，或在每个窗格的边框上显示其 ID | `cli` `terminal` `python` | 0 | 🔄 2026-08-24 |

<details><summary>与此目的也相关</summary>

- [nicosuave/memex](https://github.com/nicosuave/memex) — 搜索 Claude Code、Codex、Pi、OpenCode、GitHub Copilot 和 Cursor 的会话记录。恢复会话。追踪 token 使用
- [iurysza/termscope](https://github.com/iurysza/termscope) — 在分屏中打开终端屏幕上已经可见的文件和链接
- [jlimas/herdr-worktree-seed](https://github.com/jlimas/herdr-worktree-seed) — 为新工作树植入 copy-on-write 的 node_modules 和可配置本地 dotfiles 的 Herdr 插件
- [tanshio/herdr-worktreeinclude](https://github.com/tanshio/herdr-worktreeinclude) — Herdr 插件：将匹配 .worktreeinclude 的被 gitignore 文件复制到新创建的工作树中
- [shadowfax92/herdr-comments](https://github.com/shadowfax92/herdr-comments) — 为复制的 Herdr 终端输出添加注释，按窗格收集评论，并可在 Neovim 中审查
- [crexi/herdr-worktree-copy](https://github.com/crexi/herdr-worktree-copy) — 根据 .worktree-copy 清单复制并符号链接工作树本地文件的 Herdr 插件
- [Feasy01/herdr-allow](https://github.com/Feasy01/herdr-allow) — herdr 插件：通过 .herdr-allow 允许列表，将被 gitignore 的文件（.env、密钥、本地配置）复制到每个新工作树中
- [tupton/herdr-worktree-include](https://github.com/tupton/herdr-worktree-include) — Symlink or copy untracked files to git worktrees created by herdr.
- [zerodice0/herdr-plugin-worktree-bootstrap](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap) — 在新的 Herdr Git 工作树中安全地复制被忽略的本地文件并运行初始化命令
- [Angel-O/herdr-agent-resume](https://github.com/Angel-O/herdr-agent-resume) — 插入或复制恢复命令，以便顺畅恢复 AI Agent 会话的 Herdr 插件
- [eightHundreds/herdr-worktreeinclude](https://github.com/eightHundreds/herdr-worktreeinclude) — Herdr 插件：将 .worktreeinclude 指定的被 gitignore 文件复制到新工作树中
- [itayo-m/herdr-tab-session-name-sync](https://github.com/itayo-m/herdr-tab-session-name-sync) — 将 Agent 会话名称同步到 herdr 的标签页和窗格标题
- [jtnovellis/herdr-worktree-setup](https://github.com/jtnovellis/herdr-worktree-setup) — herdr 插件：让新建的 git 工作树立刻可用——复制 .env 和开发状态、克隆依赖缓存（APFS/reflink）、执行 mise trust、direnv allow、安装依赖，并提供实时 TUI
- [scoussens-nthplusio/herdr-worktree-include](https://github.com/scoussens-nthplusio/herdr-worktree-include) — 使用仓库的 .worktreeinclude（与 Claude Code 使用的同一份文件、同一套规则），将 .env 等被 gitignore 忽略的文件复制到新的 Herdr 工作树中
- [willian/herdr-fzf-url](https://github.com/willian/herdr-fzf-url) — 用 `fzf` 从聚焦窗格中选取 URL，然后打开或复制

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-meta"></a>

## 插件管理与开发

> 想管理插件本身，或者自己动手做一个

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-plus**](https://github.com/cloudmanic/herdr-plus)<br><sub>cloudmanic</sub> | herdr 的扩展，作为原生插件构建——一组让 herdr 更好用的工具集：项目管理和快捷操作 | `go` | 289 | 🔄 2026-09-04 |
| [**herdr-plugin-manager**](https://github.com/speardragon/herdr-plugin-manager)<br><sub>speardragon</sub> | 在弹窗中管理 herdr 插件——安装、更新、启用/禁用、卸载，并浏览 herdr-plugin 市场。推荐快捷键：prefix+p | `plugin-manager` `tui` `shell` | 25 | 🔄 2026-09-04 |
| [**herdr-lazy**](https://github.com/natori-hrj/herdr-lazy)<br><sub>natori-hrj</sub> | herdr 的声明式插件管理器兼精选发行版——一份清单、真正的锁文件、一个管理窗格 | `cli` `lockfile` `plugin-manager` `rust` `terminal` | 23 | 🔄 2026-09-01 |
| [**house-of-herdr**](https://github.com/alasano/house-of-herdr)<br><sub>alasano</sub> | Herdr 插件合集——包含 Codex Micro：在 Work Louder Codex Micro 上显示 Agent 状态灯并提供操作控制 | `codex-micro` `work-louder` `typescript` | 5 | 2026-08-13 |
| [**herdr-plugin-rust**](https://github.com/Newt6611/herdr-plugin-rust)<br><sub>Newt6611</sub> | 用于构建 Herdr 插件的 Rust 应用框架 | `rust` | 2 | 2026-07-09 |
| [**herdr-plugins**](https://github.com/alastairsounds/herdr-plugins)<br><sub>alastairsounds</sub> | 面向 herdr 的插件合集 | `rust` | 1 | 🔄 2026-08-28 |
| [**herdr-plugins-labs**](https://github.com/hmu332233/herdr-plugins-labs)<br><sub>hmu332233</sub> | Herdr 的实验性插件——在这里孵化，成熟后独立成自己的仓库 | `labs` `javascript` | 1 | 🔄 2026-08-24 |
| [**herdr-plugin-manager**](https://github.com/a-curious-coder/herdr-plugin-manager)<br><sub>a-curious-coder</sub> | 在一个弹出窗格中管理和发现 herdr 插件——安装/卸载/更新、运行或绑定操作、浏览公共注册表 | `shell` | 0 | 2026-08-13 |
| [**herdr-plugins**](https://github.com/tyler-jewell/herdr-plugins)<br><sub>tyler-jewell</sub> | 纯 Rust 编写的 Herdr 插件 monorepo（优先使用标准库）。安装方式：herdr plugin install tyler-jewell/herdr-plugins/<subdir> | `rust` `go` | 0 | 2026-08-10 |

<details><summary>与此目的也相关</summary>

- [JefeLabs/herdr-web-broker](https://github.com/JefeLabs/herdr-web-broker) — 面向 herdr 的自托管 REST/WS API——可从任何地方启动并操控编程 Agent。支持 token、多用户会话所有权、git 操作、事件流以及父子实例联邦。附带 TypeScript SDK 和 React…

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-other"></a>

## 其他与实用工具

> 不属于以上任何分类，但很实用的东西

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**terminal-browser**](https://github.com/zenbu-labs/terminal-browser)<br><sub>zenbu-labs</sub> | 终端里的浏览器 | `browser` `claude-code` `claude-skills` `cli` `codex` | 2715 | 🔄 2026-09-07 |
| [**herdr-lantern**](https://github.com/aigorahub/herdr-lantern)<br><sub>aigorahub</sub> | Lantern，来自 Elves。一个 Herdr 插件：羊群正在田野中——Lantern 会照亮谁需要你、以及他们正朝着什么目标努力 | `shell` | 61 | 🔄 2026-09-06 |
| [**herdr-plugins-directory**](https://github.com/MIDO-ruby7/herdr-plugins-directory)<br><sub>MIDO-ruby7</sub> | 按你想完成的事情来查找 herdr 插件的链接集合 | `python` | 10 | 🔄 2026-09-06 |
| [**neon-herdr**](https://github.com/neon-solutions/neon-herdr)<br><sub>neon-solutions</sub> | Neon 官方的 Herdr 插件 | `typescript` | 10 | 2026-08-06 |
| [**herdr-plugin-cmux**](https://github.com/lachieh/herdr-plugin-cmux)<br><sub>lachieh</sub> | 将每个由 herdr 管理的 Agent 镜像到 cmux 侧边栏中各自独立的一行——带状态徽标和可点击跳转的任务行 | `javascript` | 7 | 2026-07-01 |
| [**herdr-commandcode-plugin**](https://github.com/TheMetalStorm/herdr-commandcode-plugin)<br><sub>TheMetalStorm</sub> | 将 Commandcode 集成到 Herdr 中 | `cli` `commandcode` `herdr-integration` `shell` | 7 | 2026-07-30 |
| [**wave-tui**](https://github.com/takemo101/wave-tui)<br><sub>takemo101</sub> | 适合工作时段的安静终端电台 | `rust` | 5 | 2026-07-20 |
| [**herdr-freebuff-plugin**](https://github.com/TheMetalStorm/herdr-freebuff-plugin)<br><sub>TheMetalStorm</sub> | Herdr 的 Freebuff 生命周期集成插件——通过文件轮询和 PTY 内容抓取来报告闲置/工作中/被阻塞状态 | `cli` `freebuff` `herdr-integration` `shell` | 4 | 2026-07-22 |
| [**herdr-memory**](https://github.com/jatingargiitk/herdr-memory)<br><sub>jatingargiitk</sub> | 从你的编程会话中构建「活的大脑」的 Herdr 插件——逐步学习哪些做法有效、哪些失败了，以及你做出的决定 | `shell` | 3 | 2026-08-11 |
| [**🆕 herdrctx**](https://github.com/j0urneyk/herdrctx)<br><sub>j0urneyk</sub> | 用于管理本地 Herdr 会话的终端 UI。 | `go` | 2 | 🔄 2026-09-05 |
| [**herdr-standup**](https://github.com/neospeed83/herdr-standup)<br><sub>neospeed83</sub> | 根据 Git 活动和 Herdr 上下文，生成有据可查的每日站会摘要 | `developer-tools` `standup` `rust` | 2 | 🔄 2026-08-31 |
| [**herdr-streamdeck**](https://github.com/Pimpmuckl/herdr-streamdeck)<br><sub>Pimpmuckl</sub> | 通过 Elgato Stream Deck+ 对 Herdr 进行实体操控 | `typescript` | 2 | 🔄 2026-09-02 |
| [**herdr-handsfree**](https://github.com/RanolP/herdr-handsfree)<br><sub>RanolP</sub> | 免提操作的 herdr 插件——提供基于 whisper.cpp 的语音听写和面向 macOS 的摄像头视线鼠标 | `rust` | 2 | 2026-07-30 |
| [**🆕 herdr-shadow-pane**](https://github.com/shaozk/herdr-shadow-pane)<br><sub>shaozk</sub> | Herdr 插件「Shadow Clone Panel」——可同时操控多个面板。 | `rust` `vibe-coding` | 2 | 🔄 2026-09-06 |
| [**herdr-suite-site**](https://github.com/StructuPath/herdr-suite-site)<br><sub>StructuPath</sub> | StructuPath Herdr Suite 的官网首页——herdr.structupath.ai | `herdr-integration` `html` | 2 | 2026-07-31 |
| [**herdr-edit-windows**](https://github.com/aclima01/herdr-edit-windows)<br><sub>aclima01</sub> | 在编程 Agent 旁边的 herdr 窗格中运行的简易文本编辑器——文件树、语法高亮编辑器、未提交差异标签页。仅支持 Windows | `rust` | 1 | 2026-07-25 |
| [**herdr-stoplight**](https://github.com/BowlOfSoup/herdr-stoplight)<br><sub>BowlOfSoup</sub> | 根据 Herdr 的实时状态驱动一个物理 Arduino 红绿灯模块 | `go` | 1 | 2026-07-11 |
| [**harbr**](https://github.com/dev-town/harbr)<br><sub>dev-town</sub> | Harbour TUI | `typescript` | 1 | 🔄 2026-09-03 |
| [**herdr-rainfrog**](https://github.com/fraction12/herdr-rainfrog)<br><sub>fraction12</sub> | 在受管理的 HerdR 窗格中打开 Rainfrog | `shell` | 1 | 2026-08-15 |
| [**herdr-openlogi**](https://github.com/giacolees/herdr-openlogi)<br><sub>giacolees</sub> | 通过 OpenLogi 绑定浮层，将罗技鼠标接入 herdr | `ghostty` `logitech-mouse` `macos` `openlogi` `shell` | 1 | 🔄 2026-08-24 |
| [**hrd**](https://github.com/joshuadavidthomas/hrd)<br><sub>joshuadavidthomas</sub> | 管理你的沙盒集群及运行在其上的 Herdr 会话 | `go` | 1 | 🔄 2026-09-04 |
| [**herdr-plugins**](https://github.com/narumiruna/herdr-plugins)<br><sub>narumiruna</sub> | _(暂无描述)_ | `rust` | 1 | 2026-08-08 |
| [**herdr-phin-util**](https://github.com/phin-tech/herdr-phin-util)<br><sub>phin-tech</sub> | 个人 Herdr 实用工具集 | `bubbletea` `tui` `go` | 1 | 2026-08-18 |
| [**herdr-api-client**](https://github.com/playsthisgame/herdr-api-client)<br><sub>playsthisgame</sub> | 在 herdr 分屏窗格或标签页中运行的 HTTP/REST API 客户端——无需离开终端即可浏览、运行和测试请求 | `http-client` `rest-client` `tui` `shell` | 1 | 2026-08-08 |
| [**pixtui**](https://github.com/RizRiyz/pixtui)<br><sub>RizRiyz</sub> | 在终端中运行的像素画编辑器 | `bohay-module` `editor` `luvus-module` `pixel-art` `termina` | 1 | 2026-08-07 |
| [**herdr-jetbrains**](https://github.com/Soemii/herdr-jetbrains)<br><sub>Soemii</sub> | _(暂无描述)_ | `go` | 1 | 2026-08-09 |
| [**herdr-sidepulse**](https://github.com/third774/herdr-sidepulse)<br><sub>third774</sub> | _(暂无描述)_ | `javascript` | 1 | 2026-08-14 |
| [**herdr-plugin-k8s-context**](https://github.com/tkuchiki/herdr-plugin-k8s-context)<br><sub>tkuchiki</sub> | 以隔离的 Kubernetes context 和 namespace 打开 Herdr 标签页 | `go` | 1 | 2026-08-15 |
| [**herdr-zen**](https://github.com/y4m3/herdr-zen)<br><sub>y4m3</sub> | 为 Herdr 提供带可调居中窗格宽度的禅模式 | `rust` `terminal` `zen-mode` | 1 | 2026-08-19 |
| [**multitrunk-herdr-plugin**](https://github.com/yoyoyeti/multitrunk-herdr-plugin)<br><sub>yoyoyeti</sub> | 面向 multitrunk 任务工作区的 Herdr 插件 | `git` `multitrunk` `rust` | 1 | 🔄 2026-08-31 |
| [**herdr-panes**](https://github.com/atm028/herdr-panes)<br><sub>atm028</sub> | _(暂无描述)_ | `python` | 0 | 2026-08-01 |
| [**🆕 herdr-flight-radar**](https://github.com/corygforsythe/herdr-flight-radar)<br><sub>corygforsythe</sub> | Herdr plugin: real-time ADS-B flight radar TUI backed by dump1090 | `python` | 0 | 🔄 2026-09-05 |
| [**hrdr-azure-plugin**](https://github.com/gbaeke/hrdr-azure-plugin)<br><sub>gbaeke</sub> | herdr 插件：浏览 Azure 资源组和资源，点击资源即可在 Azure 门户中打开 | `azure` `javascript` | 0 | 🔄 2026-08-23 |
| [**capslock-herdr-prefix**](https://github.com/GHJQ/capslock-herdr-prefix)<br><sub>GHJQ</sub> | 在 macOS 上将 Caps Lock 键设为 herdr 的 prefix 键 | `capslock` `macos` `shell` | 0 | 2026-08-11 |
| [**herdr-attach**](https://github.com/gilvanecesar/herdr-attach)<br><sub>gilvanecesar</sub> | 从 Herdr 弹窗中选择本地文件并发送给聚焦中的编程 Agent——无需离开终端即可附加文件上下文 | `javascript` | 0 | 2026-07-26 |
| [**herdr-llama**](https://github.com/hitaishi2222/herdr-llama)<br><sub>hitaishi2222</sub> | 在指尖操控你的 llama-server | `llama-cpp` `local-ai` `python` | 0 | 2026-07-16 |
| [**herdr-pane-update-timestamps**](https://github.com/johnlindquist/herdr-pane-update-timestamps)<br><sub>johnlindquist</sub> | 为窗格输出添加时间戳并支持滚动查看的 Herdr 插件 | `rust` | 0 | 2026-07-29 |
| [**🆕 herdr-wrangler**](https://github.com/jone/herdr-wrangler)<br><sub>jone</sub> | tmux-style pane layouts and rotation for herdr | `python` | 0 | 🔄 2026-09-05 |
| [**herdr-status**](https://github.com/jrswab/herdr-status)<br><sub>jrswab</sub> | 面向 Linux 版 Herdr 的常驻机器状态窗格 | `go` | 0 | 2026-07-30 |
| [**🆕 herdr-awst**](https://github.com/kedwards/herdr-awst)<br><sub>kedwards</sub> | AWST integration with herdr | `shell` | 0 | 🔄 2026-09-06 |
| [**herdr-laravel-tinker**](https://github.com/lancodev/herdr-laravel-tinker)<br><sub>lancodev</sub> | herdr 的分屏式 Laravel tinker REPL——编辑器旁边实时显示运行结果，可作为窗格或弹窗使用 | `laravel` `tinker` `php` `repl` | 0 | 2026-07-16 |
| [**herdr-new-task**](https://github.com/leonho/herdr-new-task)<br><sub>leonho</sub> | herdr 插件：一键选择项目目录并在新标签页中启动 claude，标签页采用名词优先的命名方式 | `python` | 0 | 2026-07-16 |
| [**herdr-plugin-loopreview**](https://github.com/loopkeep/herdr-plugin-loopreview)<br><sub>loopkeep</sub> | 用于 loopreview 的 Herdr 插件 | `rust` | 0 | 2026-07-23 |
| [**strays**](https://github.com/m1sk9/strays)<br><sub>m1sk9</sub> | 用于集中管理 Claude Code 的 TUI | `claude-code` `llm` `tui` `rust` | 0 | 🔄 2026-09-06 |
| [**herdr-source-control**](https://github.com/mariotmc/herdr-source-control)<br><sub>mariotmc</sub> | _(暂无描述)_ | `go` | 0 | 2026-08-15 |
| [**herdr-brainrot**](https://github.com/marius-se/herdr-brainrot)<br><sub>marius-se</sub> | 在 Agent 工作时，于 Herdr 窗格中玩 DOOM 的「brainrot」插件，支持可插拔的应用 | `doom` `go` | 0 | 2026-08-06 |
| [**🆕 herdr-sleep-inhibit**](https://github.com/moosingin3space/herdr-sleep-inhibit)<br><sub>moosingin3space</sub> | _(暂无描述)_ | `rust` | 0 | 🔄 2026-09-05 |
| [**herdr-git-pull**](https://github.com/nimrc/herdr-git-pull)<br><sub>nimrc</sub> | _(暂无描述)_ | `python` | 0 | 2026-08-13 |
| [**ayatsumugi**](https://github.com/nkwork9999/ayatsumugi)<br><sub>nkwork9999</sub> | 面向 Ayatori 和 Tsumugi 的本地优先 React DOM、Fiber 与状态图可视化 | `cmux` `ghostty` `orca` `react-devtools` `javascript` | 0 | 🔄 2026-09-05 |
| [**herdr-action-launcher**](https://github.com/nnexai/herdr-action-launcher)<br><sub>nnexai</sub> | _(暂无描述)_ | `javascript` | 0 | 2026-08-05 |
| [**herdr-bot**](https://github.com/Phoobobo/herdr-bot)<br><sub>Phoobobo</sub> | _(暂无描述)_ | `tui` `typescript` | 0 | 🔄 2026-09-02 |
| [**herdr-traex-integration**](https://github.com/Phoobobo/herdr-traex-integration)<br><sub>Phoobobo</sub> | 支持 traex 集成的 Herdr 插件 | `shell` | 0 | 2026-07-02 |
| [**herdr-browser**](https://github.com/redsquiggle/herdr-browser)<br><sub>redsquiggle</sub> | 让 Chromium 标签组与 Herdr 工作区保持一致 | `chromium` `ratatui` `rust` | 0 | 2026-07-28 |
| [**🆕 herdr-numbered-tabs**](https://github.com/RickyMarou/herdr-numbered-tabs)<br><sub>RickyMarou</sub> | Herdr plugin: prefix every tab label with its current displayed position/shortcut number | `python` | 0 | 🔄 2026-09-04 |
| [**🆕 herdr-plugin-shortcut-shepherd**](https://github.com/Roshvan/herdr-plugin-shortcut-shepherd)<br><sub>Roshvan</sub> | Shortcut insights and gentle coaching for Herdr. | `typescript` | 0 | 🔄 2026-09-07 |
| [**🆕 herdr-orca**](https://github.com/rudironsoni/herdr-orca)<br><sub>rudironsoni</sub> | 将标准 Orca 标签页附加到 Herdr 管理的终端上的 Herdr 插件。 | `typescript` | 0 | 🔄 2026-09-03 |
| [**herdr-cwd-control**](https://github.com/skinp/herdr-cwd-control)<br><sub>skinp</sub> | 更精细地控制新工作区、标签页和窗格初始工作目录的 herdr 插件 | `python` | 0 | 2026-08-10 |
| [**herdr-now-playing**](https://github.com/spywhere/herdr-now-playing)<br><sub>spywhere</sub> | 为 herdr 添加可通过快捷键控制的音乐播放器 | `shell` | 0 | 2026-08-22 |
| [**herdr-plugins**](https://github.com/tomaszhanc/herdr-plugins)<br><sub>tomaszhanc</sub> | 个人的 herdr 插件 monorepo，每个插件都在自己的文件夹中，附带 herdr-plugin.toml 清单和可执行文件 | — | 0 | 2026-07-16 |
| [**🆕 herdr-plugin-pane-move**](https://github.com/yuloop/herdr-plugin-pane-move)<br><sub>yuloop</sub> | Herdr插件:快捷键搬窗格 | `shell` | 0 | 🔄 2026-09-04 |
| [**🆕 herdr-plugin-win-terminal**](https://github.com/yuloop/herdr-plugin-win-terminal)<br><sub>yuloop</sub> | Herdr插件:一键安装Windows Terminal配置 | `powershell` | 0 | 🔄 2026-09-04 |
| [**🆕 herdr-harbor**](https://github.com/zlj-zz/herdr-harbor)<br><sub>zlj-zz</sub> | _(暂无描述)_ | `rust` | 0 | 🔄 2026-09-05 |

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
