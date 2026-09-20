# herdr plugins by purpose

[🇯🇵 日本語](README.md) · [🇺🇸 English](README.en.md) · 🇨🇳 中文

**一个按照「你想做什么」来查找 [herdr](https://herdr.dev/) 插件的链接合集。**

- 收录 **995** 个插件 / 最后更新 **2026-09-20 16:05 UTC**（每 6 小时自动刷新）
- 数据来源：打了 GitHub 话题标签 [`herdr-plugin`](https://github.com/topics/herdr-plugin) 的仓库——与官方市场 [herdr.dev/plugins](https://herdr.dev/plugins/) 的数据来源相同
- 分类是根据仓库描述和话题标签自动推断的。如果分类不准确，可以通过 PR 修改 [`data/overrides.json`](data/overrides.json)
- 安装：`herdr plugin install owner/repo` —— [官方文档](https://herdr.dev/docs/plugins/)

> [!WARNING]
> 这是自动采集的索引，不是经过审核的目录。插件是直接在你的电脑上运行的代码，安装前请检查其 manifest 和会执行的命令。

<a id="purposes"></a>

## 按目的浏览

- [**🆕 最近新增**](#cat-new) (215) — 最近 7 天内加入本列表的插件。
- [**通知与提醒**](#cat-notify) (40) — 即使离开座位，也想知道 Agent 何时完成或卡在等待输入
- [**手机与远程操控**](#cat-remote) (51) — 想在外出或用手机时监控 Agent，只需回传批准即可
- [**Agent 编排与并行执行**](#cat-agents) (139) — 想统一启动、分工并管理多个 AI Agent
- [**git 工作树与分支管理**](#cat-worktree) (52) — 想为每项工作单独开一个工作树，收尾清理也自动完成
- [**代码审查与差异对比**](#cat-review) (42) — 想阅读 Agent 写的差异并对其发表评论
- [**GitHub / issue 跟踪工具集成**](#cat-forge) (42) — 想以 issue 或 PR 为起点开始工作，并追踪 PR 状态
- [**工作区与布局搭建**](#cat-layout) (40) — 打开项目时，希望标签页、窗格和启动命令一次性就位
- [**窗格导航与快捷键**](#cat-navigate) (120) — 想用和编辑器一样的快捷键在窗格、工作区之间移动和调整大小
- [**文件浏览与编辑器联动**](#cat-files) (60) — 想在窗格中打开文件树，或与编辑器的状态保持一致
- [**Token 与费用管理**](#cat-cost) (26) — 想看看 Agent 花费了多少，并想削减用量
- [**监控与仪表盘**](#cat-monitor) (74) — 想一目览尽 Agent 和机器的状态
- [**搜索与模糊查找器**](#cat-finder) (88) — 只记得大概名字也想调出命令或项目
- [**自动化、钩子与定时任务**](#cat-automation) (47) — 想在创建工作树或指定时机自动运行固定的操作步骤
- [**会话保存与恢复**](#cat-session) (32) — 关闭工作后，希望之后能从同一状态继续
- [**标题、命名与外观**](#cat-naming) (50) — 想让标签页名称和终端标题自动变得清晰易懂，或想改变外观
- [**文本与 URL 提取**](#cat-text) (20) — 想不用鼠标就抓取屏幕上显示的字符串、路径或 URL
- [**插件管理与开发**](#cat-meta) (9) — 想管理插件本身，或者自己动手做一个
- [**其他与实用工具**](#cat-other) (63) — 不属于以上任何分类，但很实用的东西

<a id="cat-new"></a>

## 🆕 最近新增

> 最近 7 天内加入本列表的插件。

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**🆕 herdr-lcars**](https://github.com/jlcases/herdr-lcars)<br><sub>jlcases</sub> | Command up to 2,000 Herdr AI agents from one LCARS bridge, track Claude/Codex quota per account, and hand off verified context without losing work. | `agent-observability` `ai-agents` `claude-code` `lcars` `openai-codex` | 10 | 2026-09-20 |
| [**🆕 AgentRadio**](https://github.com/detailles/AgentRadio)<br><sub>detailles</sub> | Local message bus for AI coding agents running in Herdr panes — join, DM, presence, offline delivery | `agent-orchestration` `multi-agent` `radio` `python` | 3 | 2026-09-20 |
| [**🆕 herdr-commander**](https://github.com/lurepos/herdr-commander)<br><sub>lurepos</sub> | Fast palette to discover/launch npm, cargo, .vscode tasks and commands from herdr | `rust` | 2 | 2026-09-20 |
| [**🆕 herdr-tasks**](https://github.com/Eslsamu/herdr-tasks)<br><sub>Eslsamu</sub> | 为 Herdr 提供由 Agent 拥有的本地任务队列，并配有实时的只读浏览器视图。 | `ai-agents` `codex` `local-first` `python` `sqlite` | 1 | 2026-09-09 |
| [**🆕 herdr-plugin-cow-worktree**](https://github.com/khatriafaz/herdr-plugin-cow-worktree)<br><sub>khatriafaz</sub> | Herdr plugin for strict copy-on-write Git worktrees that include ignored local files | `typescript` | 1 | 2026-09-20 |
| [**🆕 herdr-disp-model**](https://github.com/pdalinis/herdr-disp-model)<br><sub>pdalinis</sub> | Display active Codex, Claude Code, Pi, and Hermes models in the Herdr agent sidebar. | `ai-agents` `claude-code` `codex` `developer-tools` `hermes-agent` | 1 | 2026-09-19 |
| [**🆕 herdr-rss**](https://github.com/shindakun/herdr-rss)<br><sub>shindakun</sub> | An RSS reader plugin for herdr, cuz why not | `rss` `rss-reader` `rust` | 1 | 2026-09-20 |
| [**🆕 herdr-testrun**](https://github.com/shindakun/herdr-testrun)<br><sub>shindakun</sub> | Herdr plugin. Runs a project's tests in a pane, lists the failures, sends them to the agent on one key. | `go` `nodejs` `rust` | 1 | 2026-09-20 |
| [**🆕 herdr-webhook-notify**](https://github.com/zgxme/herdr-webhook-notify)<br><sub>zgxme</sub> | Herdr plugin that forwards agent notifications to Slack, Discord, Teams, Google Chat, Feishu, Lark, DingTalk, WeCom, Telegram, ntfy or any HTTP webhook | `dingtalk` `discord` `feishu` `lark` `notifications` | 1 | 2026-09-20 |
| [**🆕 herdr-dictate**](https://github.com/abhishekrana/herdr-dictate)<br><sub>abhishekrana</sub> | 在本地将语音转文字，并输入到当前聚焦的 Herdr 窗格中。 | `dictation` `speech-to-text` `voice` `whisper` `rust` | 0 | 2026-09-12 |
| [**🆕 herdr-hermes-bridge**](https://github.com/AdriaBA/herdr-hermes-bridge)<br><sub>AdriaBA</sub> | 将 Hermes Agent 的生命周期状态报告到 Herdr 窗格中——提供子 Agent、审批与工具活动的确切信息，而非基于屏幕抓取的猜测。 | `python` | 0 | 2026-09-11 |
| [**🆕 herdr**](https://github.com/AgentTeamsRun/herdr)<br><sub>AgentTeamsRun</sub> | 将 herdr 工作树的生命周期事件上报给 AgentTeams 注册中心 | — | 0 | 2026-08-19 |
| [**🆕 herdr-preview**](https://github.com/AlexanderMakarov/herdr-preview)<br><sub>AlexanderMakarov</sub> | Herdr 插件：按下热键高亮屏幕上可见的文件/文件夹路径，并在 file-viewer 中打开。可在 Agent 界面和终端中使用。 | `rust` | 0 | 2026-08-29 |
| [**🆕 open-project**](https://github.com/benbrackenbury/open-project)<br><sub>benbrackenbury</sub> | Herdr 插件：模糊搜索选择一个项目，并将其作为工作区打开。 | `shell` | 0 | 2026-09-08 |
| [**🆕 herdr-cwd**](https://github.com/bonanyan/herdr-cwd)<br><sub>bonanyan</sub> | Mirror the focused herdr pane's working directory to the host terminal with OSC 7, so terminal file panels, titles, and new splits follow herdr. | `osc7` `terminal` `javascript` | 0 | 2026-09-20 |
| [**🆕 herdr-bookmark**](https://github.com/bonkey/herdr-bookmark)<br><sub>bonkey</sub> | Herdr 插件：每个工作区可设置三个独立书签（− = ≡），集中显示为一个侧边栏 token，可通过按键切换。 | `python` | 0 | 2026-09-15 |
| [**🆕 herdr-codex-cost**](https://github.com/Coolsik/herdr-codex-cost)<br><sub>Coolsik</sub> | 在 Herdr 侧边栏中显示 Codex 会话的估算费用 | `codex` `shell` | 0 | 2026-09-08 |
| [**🆕 herdr-pr-glance**](https://github.com/cupsadarius/herdr-pr-glance)<br><sub>cupsadarius</sub> | Herdr 插件：一目了然地查看当前分支的拉取请求、CI 检查、审查情况与提交栈。 | `bubbletea` `github` `go` `pull-requests` | 0 | 2026-09-08 |
| [**🆕 herdr-review-panel**](https://github.com/Deetss/herdr-review-panel)<br><sub>Deetss</sub> | Herdr 插件：一个「审查队列」面板，展示由 Claude Code 标记出的、需要你查看的文件和需要亲自运行的命令。 | `claude-code` `ratatui` `rust` `tui` | 0 | 2026-09-16 |
| [**🆕 herdr-web-ui**](https://github.com/devswha/herdr-web-ui)<br><sub>devswha</sub> | herdr in the browser: your live herdr workspaces, tabs and panes in a web UI / PWA, bridged over herdr's socket API | `bun` `pwa` `react` `terminal` `xterm` | 0 | 2026-09-19 |
| [**🆕 herdr-slack**](https://github.com/egemenyildiz/herdr-slack)<br><sub>egemenyildiz</sub> | 从 Slack 驱动你本地的 herdr Agent——在手机上浏览、发送提示词并启动 Agent，无需内网穿透 | `slack` `typescript` | 0 | 2026-09-17 |
| [**🆕 herdr-tuicr**](https://github.com/ekropotin/herdr-tuicr)<br><sub>ekropotin</sub> | tuicr code review in a Herdr pane, with automatic handoff to the agent that opened it. | `shell` | 0 | 2026-09-14 |
| [**🆕 herdr-title**](https://github.com/filoozom/herdr-title)<br><sub>filoozom</sub> | 在终端标签页标题中显示所选工作树和 Agent 活动状态的 Herdr 插件 | `rust` | 0 | 2026-07-24 |
| [**🆕 herdr-workspace-copy**](https://github.com/GODVvVZzz/herdr-workspace-copy)<br><sub>GODVvVZzz</sub> | Herdr plugin: copy a workspace folder to a sibling path and open it as a new workspace (no git worktree required). | `rust` `workspace` | 0 | 2026-09-20 |
| [**🆕 herdr-git-tab**](https://github.com/hamzahraihan/herdr-git-tab)<br><sub>hamzahraihan</sub> | Herdr 标签页插件：在一个视图中以六个窗格展示 GitHub TUI。 | `typescript` | 0 | 2026-09-09 |
| [**🆕 herdr-jira-peek**](https://github.com/hilmimuktitama/herdr-jira-peek)<br><sub>hilmimuktitama</sub> | 在当前 Herdr 窗格中，以只读方式预览 Jira Cloud 内容。 | `jira` `terminal` `shell` | 0 | 2026-09-19 |
| [**🆕 herdr-implement-review**](https://github.com/Idan-Levin/herdr-implement-review)<br><sub>Idan-Levin</sub> | 用于 Codex 实现、安全扫描和「母 Agent」评审的 Herdr 工作流 | `claude-code` `codex` `security-review` `shell` | 0 | 2026-08-10 |
| [**🆕 herdr-plan-code-review**](https://github.com/inxx/herdr-plan-code-review)<br><sub>inxx</sub> | herdr 插件：Opus 做计划，Sonnet 写代码，Claude+Codex 做审查——一个操作打开四个 Agent 窗格 | `claude-code` `codex` `terminal` `shell` | 0 | 2026-07-06 |
| [**🆕 herdr-harvest**](https://github.com/j1nn0/herdr-harvest)<br><sub>j1nn0</sub> | 收集你的 Agent 群体产出的结果——一个 Herdr 插件，将 Agent 完成时的输出捕获到持久化的结果收件箱中。 | `typescript` | 0 | 2026-09-18 |
| [**🆕 herdr-plugin-vault**](https://github.com/Joxtacy/herdr-plugin-vault)<br><sub>Joxtacy</sub> | 在 herdr 弹窗中浏览过去的 Claude Code 会话，并在新标签页中恢复所选的那个 | `shell` | 0 | 2026-08-11 |
| [**🆕 herdr-agent-index**](https://github.com/kadaliao/herdr-agent-index)<br><sub>kadaliao</sub> | Show each Herdr agent's panel number in the sidebar, so focus_agent = prefix+alt+1..9 has visible targets. | `sidebar` `terminal` `python` | 0 | 2026-09-20 |
| [**🆕 herdr-busywatch**](https://github.com/KamalF/herdr-busywatch)<br><sub>KamalF</sub> | A herdr plugin: is anything still running, and does it need me? | `python` | 0 | 2026-09-18 |
| [**🆕 herdr-ccs**](https://github.com/KennethWKZ/herdr-ccs)<br><sub>KennethWKZ</sub> | 让 `ccs claude` 在 Herdr 中表现得如同原生 Claude Code——支持窗格检测，以及通过 ccs 实现的、感知启动方式的会话恢复 | `shell` | 0 | 2026-08-29 |
| [**🆕 herdr-hub-worktrees**](https://github.com/klukacin/herdr-hub-worktrees)<br><sub>klukacin</sub> | herdr 插件：将 hub 工作树镜像到每个嵌套子仓库的克隆中 | `git-worktree` `monorepo` `terminal-multiplexer` `shell` | 0 | 2026-08-12 |
| [**🆕 herdr-plugin-workspace-groups**](https://github.com/kwanwooi25/herdr-plugin-workspace-groups)<br><sub>kwanwooi25</sub> | Keyboard-first workspace grouping and colored sidebar badges for Herdr | `python` `terminal` `workspace-manager` | 0 | 2026-09-20 |
| [**🆕 herdr-laravel-tinker**](https://github.com/lancodev/herdr-laravel-tinker)<br><sub>lancodev</sub> | herdr 的分屏式 Laravel tinker REPL——编辑器旁边实时显示运行结果，可作为窗格或弹窗使用 | `laravel` `tinker` `php` `repl` | 0 | 2026-07-16 |
| [**🆕 herdr-reach**](https://github.com/Luisalt20/herdr-reach)<br><sub>Luisalt20</sub> | Read-only network doctor for Herdr remote machines: measures what your network actually allows and recommends a transport with evidence. No writes, no third-pa… | `cli` `cloudflare-tunnel` `connectivity` `egress` `go` | 0 | 2026-09-20 |
| [**🆕 herdr-markmap**](https://github.com/maaalo/herdr-markmap)<br><sub>maaalo</sub> | Herdr plugin: live Markmap mind map of AI agent's conversation, merged after every turn without touching the agent's context | `python` | 0 | 2026-09-20 |
| [**🆕 herdr-prompts**](https://github.com/oppenheimor/herdr-prompts)<br><sub>oppenheimor</sub> | 在 Herdr 中跨编程 Agent 保存、搜索、填充和复用提示词模板。灵感来自我的朋友 bingguanqi | `typescript` | 0 | 2026-08-19 |
| [**🆕 herdr-guard**](https://github.com/pauljohnchamberlain/herdr-guard)<br><sub>pauljohnchamberlain</sub> | 让 Codex、Claude 等编码 Agent 能够安全地对 Herdr 进行外部控制。 | `coding-agents` `typescript` | 0 | 2026-09-04 |
| [**🆕 herdr-quicknotes**](https://github.com/QuantumEdu/herdr-quicknotes)<br><sub>QuantumEdu</sub> | _(暂无描述)_ | `notes` `rust` `terminal` `tui` | 0 | 2026-09-19 |
| [**🆕 herdr-codex-session-title**](https://github.com/sergeybataev/herdr-codex-session-title)<br><sub>sergeybataev</sub> | 将 Codex 聊天标题同步为 Agent 名称的 Herdr 插件 | `codex` `python` | 0 | 2026-08-01 |
| [**🆕 herdr-ask**](https://github.com/TaylorFinklea/herdr-ask)<br><sub>TaylorFinklea</sub> | 面向 Herdr 及任意终端的轻量命令生成与终端聊天 | `cli` `rust` `terminal` `tui` | 0 | 2026-07-21 |
| [**🆕 herdr-quota-theme**](https://github.com/ummoftgo/herdr-quota-theme)<br><sub>ummoftgo</sub> | 无需修改上游插件，即可让 Herdr Agent Quota 的侧边栏颜色随主题自适应。 | `python` `themes` | 0 | 2026-09-09 |
| [**🆕 herdr-hop**](https://github.com/utahta/herdr-hop)<br><sub>utahta</sub> | herdr 插件：通过一个弹窗即可跳转到仓库、worktree 或工作区。 | `git-worktree` `go` `terminal` `tui` | 0 | 2026-09-16 |
| [**🆕 herdr-event-log**](https://github.com/waynewu411/herdr-event-log)<br><sub>waynewu411</sub> | herdr 插件：将 pane.agent_status_changed（以及未来的其他事件类型）记录到一份持久化、可从游标恢复的全局日志中，任何父 Agent 都可以 tail 它 | `shell` | 0 | 2026-08-24 |
| [**🆕 herdr-translate**](https://github.com/wenPKtalk/herdr-translate)<br><sub>wenPKtalk</sub> | herdr 插件：用 translate-shell 翻译窗格中选中的文本，并以浮动弹窗显示（支持 macOS 和 Linux） | `translate` `shell` | 0 | 2026-08-19 |
| [**🆕 herdr-balance-panes**](https://github.com/willfish/herdr-balance-panes)<br><sub>willfish</sub> | 将当前 Herdr 标签页中的窗格调整为均匀大小（相当于 tmux 的 select-layout -E） | `rust` `terminal` `tmux` | 0 | 2026-08-05 |
| [**🆕 herdr-plugin-move**](https://github.com/wyattjoh/herdr-plugin-move)<br><sub>wyattjoh</sub> | Move the focused Herdr pane to another workspace and tab | `bun` `terminal` `tui` `typescript` | 0 | 2026-09-15 |
| [**🆕 herdr-agent-topic**](https://github.com/wynemo/herdr-agent-topic)<br><sub>wynemo</sub> | herdr 插件：在每张 Agent 卡片中显示你最近发送的用户提示词 | `go` | 0 | 2026-08-20 |
| [**🆕 herdr-desktop-bridge**](https://github.com/yonatangross/herdr-desktop-bridge)<br><sub>yonatangross</sub> | 一个 stdio MCP 服务器，让 Claude Desktop 能够读取 herdr 的「楼层」并留言。它只是信箱和门铃，绝非指挥席。 | `claude-desktop` `mcp` `python` | 0 | 2026-09-11 |
| [**🆕 herdr-plugin-win-terminal**](https://github.com/yuloop/herdr-plugin-win-terminal)<br><sub>yuloop</sub> | Herdr 插件：一键安装 Windows Terminal 配置。 | `powershell` | 0 | 2026-09-04 |
| [**🆕 kubeflock**](https://github.com/LoriKarikari/kubeflock)<br><sub>LoriKarikari</sub> | 在 Herdr 中创建并连接 Kubernetes 沙箱。 | `agent-sandbox` `gvisor` `kubernetes` `sandbox` `go` | 3 | 2026-09-11 |
| [**🆕 pet-town**](https://github.com/abhishek944/pet-town)<br><sub>abhishek944</sub> | A transparent desktop village for live Herdr agents | `rust` | 2 | 2026-09-20 |
| [**🆕 herdr-target-picker**](https://github.com/navishachiku/herdr-target-picker)<br><sub>navishachiku</sub> | Pick a Herdr space, tab, or pane and type its id into the agent you were talking to | `typescript` | 2 | 2026-09-19 |
| [**🆕 herdr-ctx-bar**](https://github.com/pdalinis/herdr-ctx-bar)<br><sub>pdalinis</sub> | Color-coded context-window usage bars for Codex, Claude Code, Pi, and Hermes Agent in Herdr's Agents sidebar. | `ai-agents` `claude-code` `codex` `context-window` `hermes-agent` | 2 | 2026-09-19 |
| [**🆕 asgoto**](https://github.com/asumaran/asgoto)<br><sub>asumaran</sub> | Tree-style switcher across herdr repos, worktrees and panes | `go` | 1 | 2026-09-20 |
| [**🆕 shop-plugin**](https://github.com/kyrosle/shop-plugin)<br><sub>kyrosle</sub> | A visible multi-agent workstation for Pi + Herdr, with configurable Lead/Worker models, file-based task handoffs, and explicit review. Local alpha. | `coding-agent` `developer-tools` `human-in-the-loop` `multi-agent` `pi-coding-agent` | 1 | 2026-09-20 |
| [**🆕 herdr-tasks**](https://github.com/pinkpixel-dev/herdr-tasks)<br><sub>pinkpixel-dev</sub> | A Herdr plugin that puts your agent's task list in a split pane beside it, checked off as the agent works. | `ai` `ai-agents` `antigravity` `claude-code` `cli` | 1 | 2026-09-19 |
| [**🆕 goat-herdr**](https://github.com/shindakun/goat-herdr)<br><sub>shindakun</sub> | 🐐 Herdr plugin: alerts to Telegram, Slack, ntfy, Pushover/bullet or any webhook when an agent needs you | `ntfy` `rust` `slack` `telegram` `webhook` | 1 | 2026-09-20 |
| [**🆕 herdr-issues**](https://github.com/zamarrowski/herdr-issues)<br><sub>zamarrowski</sub> | herdr plugin: browse the GitHub issues of the repo you're in and hand one to any coding agent (Claude Code, Codex, Gemini…) in its own git worktree. | `coding-agents` `github-issues` `javascript` | 1 | 2026-09-19 |
| [**🆕 herdr-ai-notify**](https://github.com/8liang/herdr-ai-notify)<br><sub>8liang</sub> | _(暂无描述)_ | `notifications` `shell` | 0 | 2026-09-09 |
| [**🆕 herdr-ipc**](https://github.com/adihex/herdr-ipc)<br><sub>adihex</sub> | Herdr plugin + Agent Plugin: workspace-scoped Unix-socket IPC for pane workers | `ipc` `python` | 0 | 2026-09-20 |
| [**🆕 herdr-plugin-echo**](https://github.com/andischerer/herdr-plugin-echo)<br><sub>andischerer</sub> | 将一个窗格中的按键广播到多个已标记窗格的 Herdr 插件 | `typescript` | 0 | 2026-08-23 |
| [**🆕 asconfirmclose**](https://github.com/asumaran/asconfirmclose)<br><sub>asumaran</sub> | Herdr plugin: close the focused pane, asking first only when a process is running in it | `terminal` `go` | 0 | 2026-09-20 |
| [**🆕 asgotopr**](https://github.com/asumaran/asgotopr)<br><sub>asumaran</sub> | Herdr plugin: jump to your open GitHub PRs across local repos and worktrees | `go` | 0 | 2026-09-20 |
| [**🆕 herdr-project-filter**](https://github.com/bshearrer/herdr-project-filter)<br><sub>bshearrer</sub> | 将 herdr 的 Agents 侧边栏一次限定显示为单个 git 仓库。 | `javascript` | 0 | 2026-09-05 |
| [**🆕 herdr-links**](https://github.com/dima-m711/herdr-links)<br><sub>dima-m711</sub> | 为 Herdr 和 Pi 提供的、绑定会话的导航链接。 | `typescript` | 0 | 2026-09-13 |
| [**🆕 ai-share-usage-herdr**](https://github.com/DongHyunnn/ai-share-usage-herdr)<br><sub>DongHyunnn</sub> | AI Share Usage 的 herdr 插件：在 herdr 终端中追踪共享的 Codex 配额。 | `javascript` | 0 | 2026-09-12 |
| [**🆕 herdr-plugin-dotfiles-dev-layout**](https://github.com/edmundmiller/herdr-plugin-dotfiles-dev-layout)<br><sub>edmundmiller</sub> | 用于打开我的 dotfiles 开发工作区布局的 Herdr 插件 | `python` | 0 | 2026-06-23 |
| [**🆕 herdr-terminal-scripts**](https://github.com/Fadi729/herdr-terminal-scripts)<br><sub>Fadi729</sub> | Herdr plugin that runs named Scripts from a popup or numbered slots | `typescript` | 0 | 2026-09-19 |
| [**🆕 herdr-drover**](https://github.com/followbl/herdr-drover)<br><sub>followbl</sub> | Herdr 的「牧羊犬」标签页切换器：按住 Super+T 循环浏览标签页，松开即切换到当前标签页。 | `linux` `python` | 0 | 2026-09-03 |
| [**🆕 herdr-plugin-pane-id-namer**](https://github.com/gcgo/herdr-plugin-pane-id-namer)<br><sub>gcgo</sub> | 自动生成 Agent 名称并显示在终端中。 | `shell` | 0 | 2026-09-05 |
| [**🆕 herdr-reap**](https://github.com/ivorpad/herdr-reap)<br><sub>ivorpad</sub> | herdr 插件：显示所有 Agent 的生命周期状态，一键关闭已完成的那些 | `tui` `python` | 0 | 2026-08-27 |
| [**🆕 herdr-ntfy-notify**](https://github.com/jjuraszek/herdr-ntfy-notify)<br><sub>jjuraszek</sub> | Herdr 插件：当 Agent 被阻塞或完成时，通过 ntfy 向手机发送推送通知。 | `ntfy` `javascript` | 0 | 2026-09-13 |
| [**🆕 herdr-nnn**](https://github.com/linuxing3/herdr-nnn)<br><sub>linuxing3</sub> | 在 herdr 中打开 nnn | `shell` | 0 | 2026-08-04 |
| [**🆕 herdr-spaces**](https://github.com/lukecameron/herdr-spaces)<br><sub>lukecameron</sub> | Agent counts and model-generated names for Herdr spaces | `go` | 0 | 2026-09-18 |
| [**🆕 herdr-tab-title**](https://github.com/Newt6611/herdr-tab-title)<br><sub>Newt6611</sub> | Herdr Tab Title 会将 Herdr 标签页自动重命名为整洁的、按工作区独立编号的名称，如「1. Codex」「2. Terminal」，格式可自定义 | `rust` | 0 | 2026-07-09 |
| [**🆕 agentic-box**](https://github.com/nicoRomeroCuruchet/agentic-box)<br><sub>nicoRomeroCuruchet</sub> | 一个由 Claude Code 驱动本地模型 Agent 的隔离沙盒 | `agent-orchestration` `agentic` `agentic-workflow` `docker` `ornith-1-0-35b` | 0 | 2026-08-17 |
| [**🆕 herdr-action-launcher**](https://github.com/nnexai/herdr-action-launcher)<br><sub>nnexai</sub> | _(暂无描述)_ | `javascript` | 0 | 2026-08-05 |
| [**🆕 mux-prompter**](https://github.com/phine-apps/mux-prompter)<br><sub>phine-apps</sub> | 模糊选取上下文相关的提示词，并注入到 Herdr 或 tmux 窗格中 | `fzf` `prompt-engineering` `terminal-multiplexer` `tmux` `tmux-plugin` | 0 | 2026-09-13 |
| [**🆕 herdr-bot**](https://github.com/Phoobobo/herdr-bot)<br><sub>Phoobobo</sub> | _(暂无描述)_ | `tui` `typescript` | 0 | 2026-09-02 |
| [**🆕 herdr-sidekick**](https://github.com/qapquiz/herdr-sidekick)<br><sub>qapquiz</sub> | 面向 Herdr 的可开关的「副驾」AI Agent 窗格——可将选中的代码粘贴到 Agent 的输入框中而不直接提交。可与 qapquiz/herdr-sidekick.nvim 搭配使用 | `neovim` `terminal` `shell` | 0 | 2026-08-15 |
| [**🆕 herdr-openmd**](https://github.com/RufusLin/herdr-openmd)<br><sub>RufusLin</sub> | 在 openmd 中打开选中的 Markdown——从 herdr 启动的丰富 Qt 预览 | `shell` | 0 | 2026-07-29 |
| [**🆕 herdr-worktree-include**](https://github.com/scoussens-nthplusio/herdr-worktree-include)<br><sub>scoussens-nthplusio</sub> | 使用仓库的 .worktreeinclude（与 Claude Code 使用的同一份文件、同一套规则），将 .env 等被 gitignore 忽略的文件复制到新的 Herdr 工作树中 | `dotenv` `git-worktree` `shell` | 0 | 2026-08-27 |
| [**🆕 herdr-tab-new**](https://github.com/softwarecrafts/herdr-tab-new)<br><sub>softwarecrafts</sub> | 在此项目的 herdr 工作区中恢复或启动一个 Agent 会话——既是 herdr 插件，也是可在 herdr 之外的终端使用的 CLI。 | `typescript` | 0 | 2026-08-31 |
| [**🆕 herdr-worktrees**](https://github.com/SpaceK33z/herdr-worktrees)<br><sub>SpaceK33z</sub> | Switch, create, and remove Git worktrees from a Herdr popup | `rust` | 0 | 2026-09-17 |
| [**🆕 herdr-claude-context-meter**](https://github.com/tmastalirsch/herdr-claude-context-meter)<br><sub>tmastalirsch</sub> | herdr 插件：以进度条形式显示 Claude Code 的上下文用量——同时支持状态栏和 herdr 窗格 | `claude-code` `context-window` `statusline` `shell` | 0 | 2026-08-27 |
| [**🆕 herdr-focus**](https://github.com/trapple/herdr-focus)<br><sub>trapple</sub> | 聚焦下一个被阻塞/已完成的 Agent 窗格，并将终端应用置于前台。附带全局快捷键 | `shell` | 0 | 2026-07-19 |
| [**🆕 herdr-code-review**](https://github.com/txmed82/herdr-code-review)<br><sub>txmed82</sub> | 面向 Herdr 的结构化 AI 代码审查插件 | `code-review` `javascript` | 0 | 2026-08-19 |
| [**🆕 herdr-plugins**](https://github.com/tyler-jewell/herdr-plugins)<br><sub>tyler-jewell</sub> | 纯 Rust 编写的 Herdr 插件 monorepo（优先使用标准库）。安装方式：herdr plugin install tyler-jewell/herdr-plugins/<subdir> | `rust` `go` | 0 | 2026-08-10 |
| [**🆕 herdr-projects**](https://github.com/eliasstravik/herdr-projects)<br><sub>eliasstravik</sub> | A coordinator conversation, parallel worker threads, shared memory and an overview of what needs you. A Herdr plugin. | `rust` | 262 | 2026-09-18 |
| [**🆕 entwurf**](https://github.com/junghan0611/entwurf)<br><sub>junghan0611</sub> | Herdr and tmux sibling AI sessions: pi, Claude Code, Codex, Copilot, OMP and Antigravity can message and spawn each other while keeping their own auth, tools a… | `acp` `agent-client-protocol` `ai-agent` `claude-code` `codex` | 28 | 2026-09-20 |
| [**🆕 herdr-omni**](https://github.com/mmjang/herdr-omni)<br><sub>mmjang</sub> | One search for Herdr workspaces, actions, and live or saved Codex & Claude sessions. Fuzzy-find by name, search conversation content, and resume where you left… | `claude-code` `codex` `opencode` `typescript` | 9 | 2026-09-20 |
| [**🆕 herdr-transcripts**](https://github.com/hxreborn/herdr-transcripts)<br><sub>hxreborn</sub> | Search your coding-agent sessions, past and live, by any word you remember, then jump to them or resume them | `claude-code` `codex` `coding-agents` `droid` `fzf` | 6 | 2026-09-20 |
| [**🆕 herdr-tmux-session-navigator**](https://github.com/caneppelevitor/herdr-tmux-session-navigator)<br><sub>caneppelevitor</sub> | tmux choose-tree for herdr. Written by someone who left tmux but never gave up prefix+s. | `bubbletea` `terminal` `tmux` `go` | 3 | 2026-09-18 |
| [**🆕 herdr-stt**](https://github.com/xtwist/herdr-stt)<br><sub>xtwist</sub> | Speech-to-text for Herdr | `rust` | 2 | 2026-09-18 |
| [**🆕 herdr-agent-icons**](https://github.com/adihex/herdr-agent-icons)<br><sub>adihex</sub> | Herdr plugin: real per-agent logo icons in the sidebar via a generated PUA font | `python` | 1 | 2026-09-18 |
| [**🆕 herdr-revive**](https://github.com/cantona/herdr-revive)<br><sub>cantona</sub> | Restore Herdr commands, layouts and exact agent sessions with preview, named workspaces and explicit recovery. | `rust` `session-management` `terminal` `terminal-based` `terminal-multiplexer` | 1 | 2026-09-19 |
| [**🆕 herdr-hosts**](https://github.com/ecylmz/herdr-hosts)<br><sub>ecylmz</sub> | Hierarchical SSH host picker for Herdr, with folders and notes straight from ~/.ssh/config | `ratatui` `rust` `ssh` `terminal` `tui` | 1 | 2026-09-18 |
| [**🆕 herdr-chat**](https://github.com/eliasstravik/herdr-chat)<br><sub>eliasstravik</sub> | 为运行在 Herdr 中的 Agent 提供结构化的实时聊天视图 | `typescript` | 1 | 2026-08-24 |
| [**🆕 herdr-visuals**](https://github.com/hx-w/herdr-visuals)<br><sub>hx-w</sub> | 为 Herdr 提供按会话划分的 Mermaid、LaTeX 及本地图片预览，并支持 Kitty 图形代理。 | `javascript` | 1 | 2026-09-19 |
| [**🆕 nexus**](https://github.com/IniZio/nexus)<br><sub>IniZio</sub> | Herdr plugin for running worktree in Cloud-Hypervisor sandboxes, with mem/cpu/disk hotplug and auto port-forwarding | `cloud-hypervisor` `go` | 1 | 2026-09-20 |
| [**🆕 herdr-tiling**](https://github.com/jaeheonji/herdr-tiling)<br><sub>jaeheonji</sub> | Hyprland-style pane movement and tmux-style layouts for Herdr | `rust` | 1 | 2026-09-18 |
| [**🆕 herdr-equalize-panes**](https://github.com/ponko2/herdr-equalize-panes)<br><sub>ponko2</sub> | 在窗格被创建、关闭、移动或退出时，自动保持每个标签页内的窗格大小均匀 | `rust` | 1 | 2026-09-18 |
| [**🆕 herdr-pane-resurrect**](https://github.com/unstable-code/herdr-pane-resurrect)<br><sub>unstable-code</sub> | Save the commands running in your herdr panes and bring them back after a restart. | `shell` | 1 | 2026-09-19 |
| [**🆕 herdr-plugins**](https://github.com/VladPatr96/herdr-plugins)<br><sub>VladPatr96</sub> | Plugins for Herdr, the terminal workspace manager for AI coding agents | `javascript` | 1 | 2026-09-20 |
| [**🆕 herdr-numbered-workspaces**](https://github.com/abrose/herdr-numbered-workspaces)<br><sub>abrose</sub> | 在 herdr 侧边栏中为每个空间前面加上编号，与带索引的 switch_workspace 快捷键对应 | `shell` | 0 | 2026-07-21 |
| [**🆕 herdr-better-worktrees**](https://github.com/bearylabs/herdr-better-worktrees)<br><sub>bearylabs</sub> | A fast Herdr popup for managing Git worktrees in a predictable embedded-bare layout: create, clone, open, inspect, fetch, and safely remove worktrees while kee… | `typescript` | 0 | 2026-09-18 |
| [**🆕 herdr-tabline**](https://github.com/btj93/herdr-tabline)<br><sub>btj93</sub> | 使用安全的模板和感知项目的配置文件来渲染 Herdr 的标签页标题。 | `golang` `tabline` `terminal` `tui` `go` | 0 | 2026-09-04 |
| [**🆕 herdr-pi-slack-notify**](https://github.com/DylanG5/herdr-pi-slack-notify)<br><sub>DylanG5</sub> | Herdr plugin that sends Slack notifications when unseen Pi agent runs finish. | `pi` `slack-notifications` `javascript` | 0 | 2026-09-18 |
| [**🆕 shahi**](https://github.com/iYassr/shahi)<br><sub>iYassr</sub> | 在手机或浏览器上查看 Agent 对话、回应权限确认提示，并管理 herdr 会话。 | `ai-agents` `claude-code` `codex` `expo` `react-native` | 0 | 2026-09-20 |
| [**🆕 herdr-menu**](https://github.com/leonardoacosta/herdr-menu)<br><sub>leonardoacosta</sub> | Pane, tab, and workspace management actions for Herdr | `menu` `pane` `tab` `workspace` `shell` | 0 | 2026-09-16 |
| [**🆕 herdr-idle-panes**](https://github.com/leonho/herdr-idle-panes)<br><sub>leonho</sub> | herdr 插件：以清单弹窗形式查看并关闭停留在闲置 shell 的窗格 | `python` | 0 | 2026-08-22 |
| [**🆕 herdr-pane-id-metadata**](https://github.com/limars874/herdr-pane-id-metadata)<br><sub>limars874</sub> | 用于规范化窗格 ID 和精简标签页/窗格侧边栏元数据的最小化 Herdr 插件 | `coding-agents` `terminal` `javascript` | 0 | 2026-08-17 |
| [**🆕 herdr-linear-launcher**](https://github.com/logocode/herdr-linear-launcher)<br><sub>logocode</sub> | 从 Linear 工单出发，在后台 Herdr worktree 中启动 Codex 或 Claude。 | `javascript` | 0 | 2026-09-17 |
| [**🆕 herdr-battery**](https://github.com/morphysh/herdr-battery)<br><sub>morphysh</sub> | Laptop battery status for the herdr tab bar (⚡charging 🔋on-battery 🔌held), plus a health/power details popup. Linux sysfs, zero dependencies. | `battery` `linux` `status-bar` `shell` | 0 | 2026-09-16 |
| [**🆕 nvim-ascii-on-focus**](https://github.com/NathanymousFu/nvim-ascii-on-focus)<br><sub>NathanymousFu</sub> | Switch to a Latin input source when a Herdr pane running Neovim gains focus | `input-method` `macos` `neovim` `shell` | 0 | 2026-09-18 |
| [**🆕 herdr-claude-profile**](https://github.com/quinnjr/herdr-claude-profile)<br><sub>quinnjr</sub> | herdr 插件：通过浮层面板切换和管理 claude-profile 的配置 | `typescript` | 0 | 2026-09-11 |
| [**🆕 ocean-herdr**](https://github.com/Risingtides-dev/ocean-herdr)<br><sub>Risingtides-dev</sub> | 面向 Herdr 的 Ocean Agent 集成 | `coding-agent` `ocean` `rust` | 0 | 2026-07-17 |
| [**🆕 tmurdr**](https://github.com/sergiopx/tmurdr)<br><sub>sergiopx</sub> | 在 Herdr 中延续你的 tmux 肌肉记忆：将 ctrl+space 前缀键与完整的 tmux 键位映射应用到你的 config.toml 中。 | `keybindings` `terminal` `tmux` `shell` | 0 | 2026-09-14 |
| [**🆕 herdr-worktree-from-gitlab**](https://github.com/snics/herdr-worktree-from-gitlab)<br><sub>snics</sub> | herdr 插件：从 GitLab issue（通过 glab）创建 git 工作树和工作区 | `gitlab` `rust` `worktree` | 0 | 2026-07-09 |
| [**🆕 herdr-pane-restart**](https://github.com/zap0xfce2/herdr-pane-restart)<br><sub>zap0xfce2</sub> | 在服务器启动时，于命名窗格中运行已配置的命令 | `python` | 0 | 2026-09-15 |
| [**🆕 tsk**](https://github.com/smarzban/tsk)<br><sub>smarzban</sub> | tsk, a Linear alternative that stays in the terminal: a shared task board for you and your agents. TUI for you, CLI for them. | `cli` `productivity` `rust` `task-manager` `terminal` | 69 | 2026-09-20 |
| [**🆕 agent-router**](https://github.com/nidhi-singh02/agent-router)<br><sub>nidhi-singh02</sub> | CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr | `agents` `ai` `claude-code` `cli` `codex` | 54 | 2026-09-19 |
| [**🆕 herdr-ports**](https://github.com/randomradio/herdr-ports)<br><sub>randomradio</sub> | Herdr plugin: forward a remote workspace port to http://herdr.{workspace}.localhost:{port} | `rust` | 2 | 2026-09-20 |
| [**🆕 herdr-agent-tab-titles**](https://github.com/ajaykumarMohite/herdr-agent-tab-titles)<br><sub>ajaykumarMohite</sub> | Renames each Herdr tab to the task its coding agent is working on | `claude-code` `developer-tools` `terminal` `python` | 1 | 2026-09-17 |
| [**🆕 herdr-keep-root**](https://github.com/bonkey/herdr-keep-root)<br><sub>bonkey</sub> | Herdr 插件：只要某个仓库的任意 worktree 工作区处于打开状态，就保持该仓库主检出工作区一直打开，从而避免 Spaces 面板中的 worktree 分组被拍平。 | `shell` | 1 | 2026-09-08 |
| [**🆕 herdr-plugin-jj-workspace**](https://github.com/expnn/herdr-plugin-jj-workspace)<br><sub>expnn</sub> | A Herdr plugin to create and remove Jujutsu (jj) workspaces | `rust` | 1 | 2026-09-14 |
| [**🆕 herdr-cron**](https://github.com/huketo/herdr-cron)<br><sub>huketo</sub> | 为编码 Agent 安排自动化任务：在 Herdr 窗格中定时执行 shell 命令，或向编码 Agent 发送提示词。 | `agent-skills` `automation` `bubbletea` `cli` `coding-agent` | 1 | 2026-09-18 |
| [**🆕 herdr-nav**](https://github.com/karanpatel1993/herdr-nav)<br><sub>karanpatel1993</sub> | File navigation, code search and jdb debugging inside herdr — fzf, ripgrep and a Java debugger wired into your terminal workspace | `shell` | 1 | 2026-09-17 |
| [**🆕 herdr-pane-reopen**](https://github.com/rchougule/herdr-pane-reopen)<br><sub>rchougule</sub> | herdr plugin: undo close — reopen the last closed pane, tab or workspace in place and resume its agent | `rust` | 1 | 2026-09-17 |
| [**🆕 herdr-pdf**](https://github.com/tim80411/herdr-pdf)<br><sub>tim80411</sub> | PDF viewer plugin for herdr: renders pages into a split pane through the pane.graphics stream API | `go` `pdf` `terminal` | 1 | 2026-09-17 |
| [**🆕 herdr-ssh-sessions**](https://github.com/ananianatid/herdr-ssh-sessions)<br><sub>ananianatid</sub> | Herdr plugin that shows ssh and mosh sessions as agent rows in the Agent sidebar. | `mosh` `ssh` `javascript` | 0 | 2026-09-17 |
| [**🆕 herdr-ctx**](https://github.com/aorumbayev/herdr-ctx)<br><sub>aorumbayev</sub> | 面向 herdr 侧边栏窗格的 Claude 上下文窗口指示器 | `typescript` | 0 | 2026-07-21 |
| [**🆕 herdr-priority-view**](https://github.com/asermax/herdr-priority-view)<br><sub>asermax</sub> | 面向 herdr 的自定义优先级视图，按三级优先级排序，并优先显示最旧的项目。 | `typescript` | 0 | 2026-09-12 |
| [**🆕 hrdr-azure-plugin**](https://github.com/gbaeke/hrdr-azure-plugin)<br><sub>gbaeke</sub> | herdr 插件：浏览 Azure 资源组和资源，点击资源即可在 Azure 门户中打开 | `azure` `javascript` | 0 | 2026-08-23 |
| [**🆕 herdr-pane-id-border**](https://github.com/Haichiu/herdr-pane-id-border)<br><sub>Haichiu</sub> | 一个极简的 Herdr 插件，在窗格边框上显示规范的窗格 ID。 | `shell` | 0 | 2026-09-02 |
| [**🆕 herdr-space-index**](https://github.com/kadaliao/herdr-space-index)<br><sub>kadaliao</sub> | Show each Herdr workspace's switch number in the sidebar, so prefix+shift+1..9 has visible targets. | `sidebar` `terminal` `python` | 0 | 2026-09-17 |
| [**🆕 herdr-new-task**](https://github.com/leonho/herdr-new-task)<br><sub>leonho</sub> | herdr 插件：一键选择项目目录并在新标签页中启动 claude，标签页采用名词优先的命名方式 | `python` | 0 | 2026-07-16 |
| [**🆕 herdr-repo-picker**](https://github.com/mayaton/herdr-repo-picker)<br><sub>mayaton</sub> | A herdr plugin that opens an overlay pane to fuzzy-pick a ghq repository and jump to its workspace. | `fuzzy-finder` `ghq` `ratatui` `rust` `tui` | 0 | 2026-09-17 |
| [**🆕 herdr-git-pull**](https://github.com/nimrc/herdr-git-pull)<br><sub>nimrc</sub> | _(暂无描述)_ | `python` | 0 | 2026-08-13 |
| [**🆕 hither**](https://github.com/T0mSIlver/hither)<br><sub>T0mSIlver</sub> | 在远程主机上的 herdr 窗格里按下组合键，Zed 就会在你的 Mac 上打开对应目录。 | `shell` | 0 | 2026-09-18 |
| [**🆕 herdr-pr-workflow**](https://github.com/tamdogood/herdr-pr-workflow)<br><sub>tamdogood</sub> | 促使聚焦中的 Agent 安全地创建或合并当前分支拉取请求的 Herdr 操作 | `javascript` | 0 | 2026-08-10 |
| [**🆕 herdr-ghostty-theme-sync**](https://github.com/themuuln/herdr-ghostty-theme-sync)<br><sub>themuuln</sub> | 让 herdr 的主题和侧边栏配色跟随当前使用的 Ghostty 主题——即使 herdr 重启，侧边栏的配色 token 也会保留。herdr.dev 出品的插件 | `python` | 0 | 2026-08-12 |
| [**🆕 herdr-space-groups**](https://github.com/yojahny55/herdr-space-groups)<br><sub>yojahny55</sub> | herdr 插件：将 Space 分组为带名称、带颜色的组——支持选择器弹窗（鼠标+键盘）、侧边栏分组标题和自动排序 | `javascript` | 0 | 2026-08-29 |
| [**🆕 herdr-kakoune-popup**](https://github.com/Yukaii/herdr-kakoune-popup)<br><sub>Yukaii</sub> | 在 Herdr 原生弹窗中运行 Kakoune 的终端命令 | `kakoune` `shell` | 0 | 2026-08-20 |
| [**🆕 herdr-plugin-pane-move**](https://github.com/yuloop/herdr-plugin-pane-move)<br><sub>yuloop</sub> | Herdr 插件：通过快捷键移动窗格。 | `shell` | 0 | 2026-09-04 |
| [**🆕 claude-usage**](https://github.com/yuuta1219/claude-usage)<br><sub>yuuta1219</sub> | herdr 插件：将 Claude Code 使用率（会话%/周%）固定显示在侧边栏底部 | `claude` `claude-code` `python` `tui` | 0 | 2026-08-01 |
| [**🆕 herdr-image-gallery**](https://github.com/zbyhoo/herdr-image-gallery)<br><sub>zbyhoo</sub> | Browse AI-generated images, screenshots, and whole image folders in a Herdr terminal pane | `python` | 0 | 2026-09-20 |
| [**🆕 herdr-wake_on_lan**](https://github.com/zbyhoo/herdr-wake_on_lan)<br><sub>zbyhoo</sub> | Wake sleeping Herdr SSH machines with Wake-on-LAN — terminal app and Herdr plugin | `cli` `terminal` `tui` `typescript` `wake-on-lan` | 0 | 2026-09-17 |
| [**🆕 herdr-agent-progress**](https://github.com/eliasstravik/herdr-agent-progress)<br><sub>eliasstravik</sub> | Agent-reported task progress and activity for the Herdr sidebar | `rust` | 24 | 2026-09-15 |
| [**🆕 glyph**](https://github.com/fru-dev3/glyph)<br><sub>fru-dev3</sub> | One identity for every coding agent you run. Marks each Claude Code, Antigravity, Codex or Gemini session with your label, the project, the machine and the mom… | `ai-agents` `claude-code` `cli` `codex` `developer-tools` | 4 | 2026-09-19 |
| [**🆕 herdr-pi-tree**](https://github.com/edxeth/herdr-pi-tree)<br><sub>edxeth</sub> | 以树状结构展示你的 Pi Agent 的侧边栏——谁生成了谁、哪个 worktree 对应哪个分支、谁在等待你。 | `git-worktrees` `pi` `pi-coding-agent` `sidebar` `terminal` | 3 | 2026-09-18 |
| [**🆕 herdr-pixel-office**](https://github.com/devangchhajed/herdr-pixel-office)<br><sub>devangchhajed</sub> | Watch your AI coding agents work as pixel-art characters in a tiny top-down office — a herdr plugin | `typescript` | 2 | 2026-09-18 |
| [**🆕 herdr-sbx-plugin**](https://github.com/dirien/herdr-sbx-plugin)<br><sub>dirien</sub> | 在 Docker Sandboxes（sbx）中运行编码 Agent 的 Herdr 插件，每个 Agent 对应一个 microVM。 | `coding-agents` `docker-sandboxes` `javascript` | 2 | 2026-09-13 |
| [**🆕 shipframe**](https://github.com/juanitourquiza/shipframe)<br><sub>juanitourquiza</sub> | AI coding workflows for teams that plan, prove, and ship. | `ai` `ai-coding` `ai-tools` `claude` `claude-code` | 2 | 2026-09-16 |
| [**🆕 herdr-workspace**](https://github.com/zackshen/herdr-workspace)<br><sub>zackshen</sub> | herdr 插件：从居中弹窗创建工作区并应用布局配置 | `rust` | 2 | 2026-08-24 |
| [**🆕 herdr-tts**](https://github.com/Aktrov/herdr-tts)<br><sub>Aktrov</sub> | 一个 Herdr 插件，可用自然的神经网络语音（Piper）朗读选中的终端文本——右键点击或使用快捷键触发，并配有停止键。 | `tts` `python` | 1 | 2026-09-07 |
| [**🆕 herdr-stagr**](https://github.com/brianh20/herdr-stagr)<br><sub>brianh20</sub> | 面向 herdr 的源代码管理侧边栏——通过并排差异对比进行暂存、取消暂存和放弃更改 | `git` `tui` `rust` | 1 | 2026-08-06 |
| [**🆕 herdr-notes**](https://github.com/cyperx84/herdr-notes)<br><sub>cyperx84</sub> | 面向 Herdr 的、按工作区独立的 Markdown 速记笔记，用 Go 编写 | `bubbletea` `golang` `markdown` `notes` `go` | 1 | 2026-08-16 |
| [**🆕 herdr-auto-tab-name**](https://github.com/dev-shimada/herdr-auto-tab-name)<br><sub>dev-shimada</sub> | herdr 插件：根据当前目录自动命名标签页 | `javascript` | 1 | 2026-09-19 |
| [**🆕 herdr-scm**](https://github.com/dkbo/herdr-scm)<br><sub>dkbo</sub> | herdr 插件：为当前 herdr 工作区提供只读的多仓库源代码管理概览面板。 | `git` `rust` `terminal` `tui` | 1 | 2026-09-10 |
| [**🆕 herdr-services**](https://github.com/lucidstack/herdr-services)<br><sub>lucidstack</sub> | Plugin to track services running inside herdr workspaces | `rust` | 1 | 2026-09-16 |
| [**🆕 herdr-automations**](https://github.com/ram4-dev/herdr-automations)<br><sub>ram4-dev</sub> | 面向 Herdr 的声明式 cron、间隔和事件自动化 | `automation` `bun` `typescript` | 1 | 2026-08-13 |
| [**🆕 pixtui**](https://github.com/RizRiyz/pixtui)<br><sub>RizRiyz</sub> | 在终端中运行的像素画编辑器 | `bohay-module` `editor` `luvus-module` `pixel-art` `termina` | 1 | 2026-08-07 |
| [**🆕 herdr-scratch**](https://github.com/shadowfax92/herdr-scratch)<br><sub>shadowfax92</sub> | 由私有 tmux 会话支撑的、按窗格持久化的 Herdr 便签弹窗 | `neovim` `productivity` `rust` `terminal` `tmux` | 1 | 2026-08-04 |
| [**🆕 herdr-clock**](https://github.com/Tyru5/herdr-clock)<br><sub>Tyru5</sub> | 面向 herdr 的 tmux 时钟模式——一个以大号方块字符显示本地时间的弹窗时钟，按任意键即可关闭。 | `rust` `terminal` `tmux` | 1 | 2026-09-15 |
| [**🆕 herdr-plugins**](https://github.com/JJLiebig/herdr-plugins)<br><sub>JJLiebig</sub> | Herdr plugin that starts Codex or Claude from a GitHub issue, PR, or discussion | `javascript` | 0 | 2026-09-20 |
| [**🆕 herdr-worktree-bootstrap**](https://github.com/piesuke/herdr-worktree-bootstrap)<br><sub>piesuke</sub> | Bootstrap a new worktree: copy gitignored files, install deps, run hooks | `cli` `worktree` `worktree-workflow` `rust` | 0 | 2026-09-16 |
| [**🆕 herdr-quickpad**](https://github.com/rhinoc/herdr-quickpad)<br><sub>rhinoc</sub> | Notes and shell commands in a Herdr popup. | `checklist` `developer-tools` `markdown` `notes` `productivity` | 0 | 2026-09-18 |
| [**🆕 herdr-quick-prompt**](https://github.com/Taanviir/herdr-quick-prompt)<br><sub>Taanviir</sub> | Herdr plugin — press a key, pick a coding agent, type a prompt, and it launches in a new tab or split. | `coding-agents` `terminal` `tui` `javascript` | 0 | 2026-09-17 |
| [**🆕 herdr-virtualboard**](https://github.com/virtualboard/herdr-virtualboard)<br><sub>virtualboard</sub> | Kanban board for VirtualBoard feature specs inside Herdr: columns are the lifecycle, cards are specs, and dispatching a card starts a role agent in a pane. | `go` | 0 | 2026-09-16 |
| [**🆕 herdr-tab-notes**](https://github.com/yang3kc/herdr-tab-notes)<br><sub>yang3kc</sub> | 为每个 Herdr 标签页提供一个纯 Markdown 便签本，可切换显示在右侧的窄分屏中。无需构建步骤，也无需后台守护进程。 | `shell` | 0 | 2026-09-15 |
| [**🆕 deevs-pi-kit**](https://github.com/DeevsDeevs/deevs-pi-kit)<br><sub>DeevsDeevs</sub> | 完美的 pi 工具包，让 Deevs 的工程师效率提升 10 倍。 | `agents` `pi` `pi-agent` `pi-extension` `pi-package` | 9 | 2026-09-20 |
| [**🆕 herdr-agent-auto-naming**](https://github.com/azyu/herdr-agent-auto-naming)<br><sub>azyu</sub> | 一个 Herdr 插件，为检测到的每个 Agent 分配一个易读的双词名称，并作为窗格标签持久保存，重启后依然保留。 | `coding-agents` `developer-tools` `terminal` `python` | 1 | 2026-09-20 |
| [**🆕 herdr-scratchpad**](https://github.com/brunohq/herdr-scratchpad)<br><sub>brunohq</sub> | 为 herdr 打造的极简按标签页划分的 Markdown 便签本，支持带复选框的待办事项。 | `python` `scratchpad` `tui` | 1 | 2026-09-12 |
| [**🆕 herdr-mobile**](https://github.com/carsol/herdr-mobile)<br><sub>carsol</sub> | 面向 Herdr 的移动优先 Web UI：在手机上查看你的 Agent、连接窗格，并与 Claude Code、Codex 聊天。 | `claude-code` `codex` `mobile` `pwa` `python` | 1 | 2026-09-15 |
| [**🆕 herdr-agent-chat**](https://github.com/GODVvVZzz/herdr-agent-chat)<br><sub>GODVvVZzz</sub> | 在 Herdr 上的终端 Agent 之间实现类似聊天的任务委托——非阻塞式派发，并保证结果回报。 | `ai-agents` `claude-code` `python` | 1 | 2026-09-16 |
| [**🆕 herdr-plugin-done-timer**](https://github.com/hanjm93/herdr-plugin-done-timer)<br><sub>hanjm93</sub> | 在 herdr 的 Agent 面板中，为每个 AI Agent 显示从其对话记录中读取的 prompt 缓存倒计时。 | `ai-agents` `claude-code` `shell` | 1 | 2026-09-15 |
| [**🆕 herdr-plan-meter**](https://github.com/JunSeo99/herdr-plan-meter)<br><sub>JunSeo99</sub> | 在 herdr 标签栏中显示 Claude Code 和 Codex 的套餐限额，并可通过弹窗查看详情。仅使用 Python 标准库的单文件实现，凭据只读访问。 | `claude-code` `codex` `rate-limit` `usage` `python` | 1 | 2026-09-16 |
| [**🆕 herdr-attention-queue**](https://github.com/justmytwospence/herdr-attention-queue)<br><sub>justmytwospence</sub> | herdr 插件：在你处理之前持续保持「完成」状态，并提供按需关注优先级排序的 Agents 面板。 | `python` | 1 | 2026-09-14 |
| [**🆕 ZimMux**](https://github.com/Mr-Destroyer/ZimMux)<br><sub>Mr-Destroyer</sub> | ZimMux：一款单文件的 tmux 主题，采用 herdr 的 Ink 风格。薰衣草色聚焦边框、低调的状态栏、无需前缀键的 Alt 快捷键绑定，一条命令即可安装并自动备份。无需任何插件。 | `agent` `agent-framework` `agent-workflows` `agentic-ai` `agentic-workflow` | 1 | 2026-09-15 |
| [**🆕 herdr-topstrip**](https://github.com/orcchg/herdr-topstrip)<br><sub>orcchg</sub> | 将每个空间或已有空间上的标签页，以两个窗格的形式打开——上方是一条较窄的区域（通常用于目录导航、shell 命令和 git 操作），下方是较宽的区域（通常用于 Agent 会话）。 | `shell` | 1 | 2026-09-15 |
| [**🆕 herdr-autoname**](https://github.com/thejiajun/herdr-autoname)<br><sub>thejiajun</sub> | 根据最近的 Agent 会话，自动为 Herdr 的工作区、标签页和窗格命名。 | `python` | 1 | 2026-09-18 |
| [**🆕 herdr-simple-prompts**](https://github.com/AlexSamarsky/herdr-simple-prompts)<br><sub>AlexSamarsky</sub> | 只显示你自己的提示词和 Codex 或 Claude 的最终回答，并配有可用的输入框 | `rust` | 0 | 2026-08-31 |
| [**🆕 herdr-rails**](https://github.com/codergeek121/herdr-rails)<br><sub>codergeek121</sub> | Herdr 与 Rails 的集成。 | `ai` `rails` `shell` | 0 | 2026-09-17 |
| [**🆕 herdr-pane-mover**](https://github.com/dimitri4d/herdr-pane-mover)<br><sub>dimitri4d</sub> | 通过对键盘和鼠标都友好的目标选择器，在标签页和工作区之间移动正在运行的 Herdr 窗格。 | `go` | 0 | 2026-09-13 |
| [**🆕 herdr-sort-spaces-plugin**](https://github.com/dorzey/herdr-sort-spaces-plugin)<br><sub>dorzey</sub> | 按标签的字典序保持工作区排列顺序。 | `shell` | 0 | 2026-09-16 |
| [**🆕 herdr-cache-hit**](https://github.com/e-kotov/herdr-cache-hit)<br><sub>e-kotov</sub> | 为 Herdr 提供 prompt 缓存 HUD token 显示、实时过期提醒，以及动态的 Agent 排序。 | `agentic-ai` `antigravity` `cache` `claude-code` `cli` | 0 | 2026-09-11 |
| [**🆕 herdr-approval-gate**](https://github.com/Javamomma/herdr-approval-gate)<br><sub>Javamomma</sub> | herdr 中针对 Agent 操作的人工签核关卡——在专用窗格中运行任务，对其记录进行核验，直到有人输入 「APPROVE <姓名缩写>」 才会解除阻塞 | `shell` | 0 | 2026-07-15 |
| [**🆕 herdr-suffix-agent-filter**](https://github.com/kazimshah39/herdr-suffix-agent-filter)<br><sub>kazimshah39</sub> | 在精确的 Space 后缀分组视图与默认视图之间切换 Herdr 的 Agents 侧边栏 | `coding-agents` `developer-tools` `terminal` `javascript` | 0 | 2026-08-27 |
| [**🆕 drover-notify**](https://github.com/keinstn/drover-notify)<br><sub>keinstn</sub> | 在 Agent 被阻塞时发送 Drover 推送通知的 Herdr 插件 | `javascript` | 0 | 2026-09-15 |
| [**🆕 herdr-plugin-auto-rename**](https://github.com/khatriafaz/herdr-plugin-auto-rename)<br><sub>khatriafaz</sub> | 根据 Pi 会话的第一条提示词，自动重命名新的 Herdr 工作区和 Git 分支 | `typescript` | 0 | 2026-09-20 |
| [**🆕 strays**](https://github.com/m1sk9/strays)<br><sub>m1sk9</sub> | 用于集中管理 Claude Code 的 TUI | `claude-code` `llm` `tui` `rust` | 0 | 2026-09-20 |
| [**🆕 herdr-atuin-plugin**](https://github.com/smanickam01/herdr-atuin-plugin)<br><sub>smanickam01</sub> | 在 herdr 弹窗中搜索 Atuin 的 shell 历史记录——按 prefix+a，Enter 执行、Tab 编辑。安装后自动绑定快捷键 | `atuin` `macos` `shell-history` `terminal` `zsh` | 0 | 2026-08-17 |
| [**🆕 meadow**](https://github.com/Tetat-Chulchue/meadow)<br><sub>Tetat-Chulchue</sub> | 面向 herdr 终端多路复用器的鼠标驱动文件浏览器窗格 | `python` | 0 | 2026-07-21 |
| [**🆕 herdr-git-dirty**](https://github.com/viko16/herdr-git-dirty)<br><sub>viko16</sub> | 一个轻量级 Herdr 插件，显示每个 Space 中未提交的 Git 文件数量。 | `git` `python` | 0 | 2026-09-09 |
| [**🆕 herdr-worktree-setup**](https://github.com/lamngockhuong/herdr-worktree-setup)<br><sub>lamngockhuong</sub> | 为每个新 worktree 做好准备的 Herdr 插件：自动检测配置文件、创建共享目录链接，并可选择性运行初始化命令。 | `dotenv` `git-worktree` `monorepo` `javascript` | 3 | 2026-09-20 |
| [**🆕 muster**](https://github.com/ofelcan164/muster)<br><sub>ofelcan164</sub> | 在一个屏幕上查看所有仓库中的所有 Agent。一个 herdr 插件。 | `go` | 2 | 2026-09-16 |
| [**🆕 herdr-plugin-picker**](https://github.com/purehate/herdr-plugin-picker)<br><sub>purehate</sub> | Herdr 的浮动弹窗选择器——可跳转到任意空间、Agent、标签页或窗格，向所有标记窗格广播同一条命令，并从 ~/.ssh/config 发起带实时可达性检测的 SSH 连接。完全由键盘驱动。 | `broadcast` `fuzzy-finder` `golang` `picker` `ssh` | 2 | 2026-09-18 |
| [**🆕 herdr-docket**](https://github.com/DnzzL/herdr-docket)<br><sub>DnzzL</sub> | 由你的 Herdr Agent 处理的共享任务队列——类似 Backlog.md 或 Basecamp：将任务分配给指定名称的 Agent，守护进程会逐一执行。 | `go` | 1 | 2026-09-16 |
| [**🆕 herdr-revdiff**](https://github.com/mikhail-angelov/herdr-revdiff)<br><sub>mikhail-angelov</sub> | 面向 revdiff（https://github.com/umputun/revdiff）TUI 的 herdr 插件。 | `revdiff` `tui` `shell` | 1 | 2026-09-16 |
| [**🆕 herdr-lastfocus**](https://github.com/pedrobarco/herdr-lastfocus)<br><sub>pedrobarco</sub> | herdr 的 tmux 风格「上一个活跃」窗格/标签页/工作区切换——通过聚焦事件历史守护进程实现 | `terminal-multiplexer` `tmux` `go` | 1 | 2026-07-25 |
| [**🆕 herdr-reliable-messaging**](https://github.com/feelautom/herdr-reliable-messaging)<br><sub>feelautom</sub> | 在 Windows 上，为具名的 Herdr 窗格之间提供持久且确定性的消息传递。 | `developer-tools` `nodejs` `windows` `javascript` | 0 | 2026-09-14 |
| [**🆕 herdr-rbw**](https://github.com/ibanks42/herdr-rbw)<br><sub>ibanks42</sub> | 在 herdr 中模糊搜索你的 Bitwarden 密码库，并粘贴/复制凭据——rbw 版本。 | `shell` | 0 | 2026-09-14 |
| [**🆕 herdr-math**](https://github.com/liambern/herdr-math)<br><sub>liambern</sub> | 在 Herdr 终端窗格中渲染 LaTeX 显示公式，并提供与 harness 无关的 Agent 技能。 | `ai-agents` `latex` `mathjax` `terminal` `javascript` | 0 | 2026-09-14 |
| [**🆕 herdr-pane-memo**](https://github.com/NakasamaJ/herdr-pane-memo)<br><sub>NakasamaJ</sub> | 为 Herdr 提供的按窗格划分的便签备忘录，通过你自行添加的快捷键以模态弹窗打开。非官方社区工具。 | `shell` | 0 | 2026-09-13 |
| [**🆕 lazy-herd**](https://github.com/pve-homelab/lazy-herd)<br><sub>pve-homelab</sub> | _(暂无描述)_ | `rust` | 0 | 2026-09-14 |
| [**🆕 roamgate**](https://github.com/powerfooI/roamgate)<br><sub>powerfooI</sub> | A Herdr client for any screen. Control terminals, monitor coding agents, and review files and diffs from desktop or mobile. | `ai-agents` `bun` `code-review` `developer-tools` `git-worktree` | 222 | 2026-09-20 |
| [**🆕 herdr-profiles**](https://github.com/GiorgiTarsaidze/herdr-profiles)<br><sub>GiorgiTarsaidze</sub> | 面向 Herdr 的 Chrome 风格配置文件：通过弹窗选择器切换相互隔离的空间集合。 | `rust` `terminal` | 9 | 2026-09-14 |
| [**🆕 herdr-launch-default-agent**](https://github.com/blauerberg/herdr-launch-default-agent)<br><sub>blauerberg</sub> | 受 Omarchy 启发的 Herdr 默认 Agent 工作流：在专属标签页中聚焦或启动你偏好的 AI Agent。 | `agents` `herdr-integration` `shell` | 1 | 2026-09-11 |
| [**🆕 herdr-prompt-deck**](https://github.com/matdac12/herdr-prompt-deck)<br><sub>matdac12</sub> | Herdr 的底部提示词栏：可将文件路径、代码片段和草稿文本插入到当前聚焦的 Agent 中。 | `rust` | 1 | 2026-09-12 |
| [**🆕 codey**](https://github.com/rodeyseijkens/codey)<br><sub>rodeyseijkens</sub> | 一个以代码审查为核心的 Git TUI（终端界面），提供分为「已暂存/变更」两个区域的差异查看器，支持临时评论与真实的 Git 暂存操作，基于 OpenTUI 构建。 | `code-review` `opentui` `review-tool` `tui` `typescript` | 1 | 2026-09-19 |
| [**🆕 herdr-zcode**](https://github.com/Nofuture123/herdr-zcode)<br><sub>Nofuture123</sub> | Herdr 中的 ZCode：提供 TUI 窗格与委托桥接（任意 CLI Agent -> 原生 ZCode 执行器）。 | `zcode` `python` | 0 | 2026-09-19 |

[⬆ 返回目的列表](#purposes)

<a id="cat-notify"></a>

## 通知与提醒

> 即使离开座位，也想知道 Agent 何时完成或卡在等待输入

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**Heeler**](https://github.com/ZingerLittleBee/Heeler)<br><sub>ZingerLittleBee</sub> | 面向 herdr 的原生 iOS Agent 控制台——通过 SSH 查看并操控你机器上的编码 Agent，配备真正的 libghostty 终端、二维码配对，以及 Agent 需要你时的推送通知。 | `ai-agents` `apns` `coding-agents` `ios` `libghostty` | 370 | 🔄 2026-09-19 |
| [**herdr-ohmyzsh**](https://github.com/robbyrussell/herdr-ohmyzsh)<br><sub>robbyrussell</sub> | 面向 Herdr 的 Oh My Zsh 插件：在侧边栏显示耗时较长的命令、完成通知、shell 辅助工具，并可一键在所有闲置窗格中重新加载 Oh My Zsh。 | `oh-my-zsh` `zsh` `shell` | 73 | 🔄 2026-09-09 |
| [**herdr-focus-notify**](https://github.com/yankewei/herdr-focus-notify)<br><sub>yankewei</sub> | 面向 Herdr Agent 的可点击 macOS 通知。当 Agent 被阻塞或完成时发送原生提示通知；点击后将终端置于前台并聚焦到对应的 Herdr 窗格 | `alerter` `macos` `notifications` `productivity` `rust` | 24 | 🔄 2026-09-20 |
| [**herdr-terminal-notifier**](https://github.com/dot/herdr-terminal-notifier)<br><sub>dot</sub> | 通过 terminal-notifier 为 herdr Agent 状态变化发送可自定义的 macOS 通知 | `macos` `terminal-notifier` `shell` | 9 | 🔄 2026-09-07 |
| [**herdr-pings**](https://github.com/joelhooks/herdr-pings)<br><sub>joelhooks</sub> | 面向 herdr 窗格中 AI Agent 的按轮次唤醒事件——pi 扩展、wait CLI、崩溃桥接，以及为你的 worker 起的 Discworld 风格代号 | `ai-agents` `pi` `typescript` | 9 | 2026-08-09 |
| [**herdr-ntfy**](https://github.com/horn553/herdr-ntfy)<br><sub>horn553</sub> | 依赖极简（jq、curl、sh）——当 Herdr Agent 完成或被阻塞时发送 ntfy 通知 | `shell` | 8 | 🔄 2026-09-16 |
| [**herdr-hail**](https://github.com/natori-hrj/herdr-hail)<br><sub>natori-hrj</sub> | herdr 的 Slack 和 Discord 双向桥接——Agent 被阻塞时会收到提醒，回复或点击即可解除阻塞。无需内网穿透 | `discord` `slack` `typescript` | 7 | 2026-07-19 |
| [**herdr-ntfy-notify**](https://github.com/zom-2018/herdr-ntfy-notify)<br><sub>zom-2018</sub> | 面向 Herdr 终端 Agent 的实时 ntfy 推送通知 | `agent` `ntfy` `push-notifications` `tui` `javascript` | 7 | 2026-06-23 |
| [**herdr-telegram-bridge**](https://github.com/cokekitten/herdr-telegram-bridge)<br><sub>cokekitten</sub> | 当 herdr Agent 完成或被阻塞时收到 Telegram 推送——直接回复即可将文本或文件发回该 Agent。无需服务器、无需内网穿透、无需 App | `ai-agents` `chatops` `claude-code` `developer-tools` `notifications` | 5 | 2026-08-06 |
| [**herdr-telegram-plugin**](https://github.com/mvallebr/herdr-telegram-plugin)<br><sub>mvallebr</sub> | herdr 的 Telegram 机器人伴侣——通过 Telegram 论坛话题远程控制任意 Agent，整个流程中不涉及 LLM | `typescript` | 5 | 2026-08-31 |
| [**herdr-notify-windows**](https://github.com/aclima01/herdr-notify-windows)<br><sub>aclima01</sub> | 面向 herdr Agent 的 Windows 11 提示通知（轮次完成/需要输入） | `powershell` | 4 | 2026-07-23 |
| [**herdr-cache-alert**](https://github.com/AltanS/herdr-cache-alert)<br><sub>AltanS</sub> | herdr 插件：在每个 Agent 窗格显示 prompt 缓存倒计时，并附带每条缓存规则的来源和日期 | `ai-agents` `ai-coding` `ai-tools` `claude-code` `multiplexing` | 3 | 🔄 2026-09-17 |
| [**session-sounds**](https://github.com/ChrisPachulski/session-sounds)<br><sub>ChrisPachulski</sub> | 面向 macOS 和 Linux 的 Herdr，为每个 Agent 提供不同的完成提示音和关注提示音 | `coding-agents` `notifications` `rust` | 3 | 2026-07-19 |
| [**herdr-announcer**](https://github.com/nhclink16/herdr-announcer)<br><sub>nhclink16</sub> | Herdr 插件：Agent 完成或需要输入时，用语音播报一句 LLM 生成的摘要——支持本地 TTS、ElevenLabs 或任意自定义命令 | `tts` `rust` | 3 | 🔄 2026-09-09 |
| [**herdr-discord-presence**](https://github.com/revanp/herdr-discord-presence)<br><sub>revanp</sub> | herdr 插件：将 Herdr 会话和 Agent 状态显示为 Discord Rich Presence | `typescript` | 3 | 2026-08-14 |
| [**herdr-agent-notify**](https://github.com/A1exthegreat/herdr-agent-notify)<br><sub>A1exthegreat</sub> | herdr 插件：当 Agent 完成工作、需要确认或进入空闲状态时发送桌面通知 | `javascript` | 2 | 2026-08-15 |
| [**buzzr**](https://github.com/candypoets/buzzr)<br><sub>candypoets</sub> | 将运行中的 Herdr space 和 Agent 镜像到 Buzz 频道，并支持 Nostr 身份和提及路由 | `agents` `buzz` `nostr` `rust` | 2 | 2026-08-14 |
| [**agent-webhook-notify**](https://github.com/happyeric77/agent-webhook-notify)<br><sub>happyeric77</sub> | 当 Herdr Agent 完成或被阻塞时，发送 Webhook 通知 | `javascript` | 2 | 2026-08-12 |
| [**herdr-bar**](https://github.com/openalon-org/herdr-bar)<br><sub>openalon-org</sub> | Herdr 的 macOS 菜单栏应用：实时显示 Agent 数量，一键跳转到需要你处理的窗格。 | `herdr-notify` `menu-bar` `menu-bar-app` `notification` `notify` | 2 | 🔄 2026-09-18 |
| [**herdr-guard**](https://github.com/StructuPath/herdr-guard)<br><sub>StructuPath</sub> | Herdr 的跨 Agent 命令策略：审计、警告并中断危险的 shell 命令 | `ai-agents` `command-policy` `security` `terminal` `javascript` | 2 | 🔄 2026-09-14 |
| [**herdr-wsl-notify**](https://github.com/tkmct/herdr-wsl-notify)<br><sub>tkmct</sub> | 当运行在 WSL2 上的 Agent（如 Claude Code）完成或被阻塞（等待批准/输入）时，显示 Windows 桌面提示通知的 Herdr 插件 | `javascript` | 2 | 2026-08-27 |
| [**herdr-notifications**](https://github.com/barnuri/herdr-notifications)<br><sub>barnuri</sub> | herdr 插件：当 Agent 进入空闲、被阻塞或完成任务时，通过 Telegram 发送通知。 | `telegram` `javascript` | 1 | 🔄 2026-09-08 |
| [**herdr-prayer-times**](https://github.com/bayoudhi/herdr-prayer-times)<br><sub>bayoudhi</sub> | 在 Herdr 侧边栏中显示下一次礼拜时间和倒计时，并附带时间表弹窗和通知 | `rust` | 1 | 2026-08-13 |
| [**herdr-random-sounds**](https://github.com/gridness/herdr-random-sounds)<br><sub>gridness</sub> | 在 macOS 版 herdr 中，根据 Agent 状态播放随机通知音 | `herdr-integration` `macos` `notification` `notifications` `python` | 1 | 2026-08-23 |
| [**herdr-telegram-slack-bridge**](https://github.com/lsisoft/herdr-telegram-slack-bridge)<br><sub>lsisoft</sub> | 面向 Herdr Agent 会话的 Telegram 与 Slack 机器人双向桥接——将被阻塞 Agent 的提醒和聊天回复路由回 Herdr 或 tmux 窗格 | `ai-agents` `slack-bot` `telegram-bot` `tmux` `python` | 1 | 2026-07-28 |
| [**herdr-telegram-notify**](https://github.com/naturalmoods/herdr-telegram-notify)<br><sub>naturalmoods</sub> | Herdr 插件：当 Agent 完成或被阻塞时通过 Telegram 通知——包含会话标题、项目、耗时、token 用量及其最后一条消息。你在聊天中的回复也会发回给该 Agent。 | `claude-code` `notifications` `telegram` `javascript` | 1 | 🔄 2026-09-11 |
| [**herdr-notify-wsl**](https://github.com/saeedrahimi/herdr-notify-wsl)<br><sub>saeedrahimi</sub> | 为运行在 WSL 内的 herdr Agent 提供 Windows 11 提示通知——基于 aclima01/herdr-notify-windows | `powershell` | 1 | 2026-07-23 |
| [**🆕 goat-herdr**](https://github.com/shindakun/goat-herdr)<br><sub>shindakun</sub> | 🐐 Herdr plugin: alerts to Telegram, Slack, ntfy, Pushover/bullet or any webhook when an agent needs you | `ntfy` `rust` `slack` `telegram` `webhook` | 1 | 🔄 2026-09-20 |
| [**🆕 herdr-webhook-notify**](https://github.com/zgxme/herdr-webhook-notify)<br><sub>zgxme</sub> | Herdr plugin that forwards agent notifications to Slack, Discord, Teams, Google Chat, Feishu, Lark, DingTalk, WeCom, Telegram, ntfy or any HTTP webhook | `dingtalk` `discord` `feishu` `lark` `notifications` | 1 | 🔄 2026-09-20 |
| [**🆕 herdr-ai-notify**](https://github.com/8liang/herdr-ai-notify)<br><sub>8liang</sub> | _(暂无描述)_ | `notifications` `shell` | 0 | 🔄 2026-09-09 |
| [**🆕 herdr-pi-slack-notify**](https://github.com/DylanG5/herdr-pi-slack-notify)<br><sub>DylanG5</sub> | Herdr plugin that sends Slack notifications when unseen Pi agent runs finish. | `pi` `slack-notifications` `javascript` | 0 | 🔄 2026-09-18 |
| [**herdr-telegram-notify**](https://github.com/elkraps/herdr-telegram-notify)<br><sub>elkraps</sub> | 针对 Herdr Agent 状态变化的可自定义 Telegram 通知——支持状态过滤、模板、多聊天投递、去重、Codex 批准按钮、完成摘要和内置诊断 | `ai-agents` `automation` `developer-tools` `javascript` `nodejs` | 0 | 2026-08-27 |
| [**herdr-oncall**](https://github.com/fulanto/herdr-oncall)<br><sub>fulanto</sub> | 通过浮动的 macOS 面板或 Telegram 回应编码 Agent 的权限确认提示——面向 Claude Code 和 Codex 的 Herdr 插件。 | `ai-agents` `claude-code` `cli` `codex` `coding-agent` | 0 | 🔄 2026-09-17 |
| [**herdr-hitl**](https://github.com/huketo/herdr-hitl)<br><sub>huketo</sub> | 让 Herdr 的编码 Agent 在等待人工决策时暂停，并通过 Telegram 或 Discord 推送到你的手机。 | `agent-skill` `ai-agents` `cli` `discord-bot` `go` | 0 | 🔄 2026-09-09 |
| [**🆕 herdr-ntfy-notify**](https://github.com/jjuraszek/herdr-ntfy-notify)<br><sub>jjuraszek</sub> | Herdr 插件：当 Agent 被阻塞或完成时，通过 ntfy 向手机发送推送通知。 | `ntfy` `javascript` | 0 | 🔄 2026-09-13 |
| [**🆕 drover-notify**](https://github.com/keinstn/drover-notify)<br><sub>keinstn</sub> | 在 Agent 被阻塞时发送 Drover 推送通知的 Herdr 插件 | `javascript` | 0 | 🔄 2026-09-15 |
| [**herdr-apple-music-plugin**](https://github.com/perlporter/herdr-apple-music-plugin)<br><sub>perlporter</sub> | 当 Apple Music（macOS）正在播放的曲目变化时，在 herdr 中显示提示通知 | `shell` | 0 | 2026-07-28 |
| [**herdr-notify-center**](https://github.com/ram4-dev/herdr-notify-center)<br><sub>ram4-dev</sub> | 为 Herdr 提供服务器范围的 Agent 通知，配有持久化的弹窗收件箱 | `notifications` `typescript` | 0 | 2026-08-14 |
| [**herdr-kaku-bell**](https://github.com/Rockheung/herdr-kaku-bell)<br><sub>Rockheung</sub> | 当 Agent 在等待人工操作时，在 kaku 标签页上点亮一个提示点——herdr 插件。 | `kaku` `terminal` `python` | 0 | 🔄 2026-09-06 |
| [**🆕 herdr-wake_on_lan**](https://github.com/zbyhoo/herdr-wake_on_lan)<br><sub>zbyhoo</sub> | Wake sleeping Herdr SSH machines with Wake-on-LAN — terminal app and Herdr plugin | `cli` `terminal` `tui` `typescript` `wake-on-lan` | 0 | 🔄 2026-09-17 |

[⬆ 返回目的列表](#purposes)

<a id="cat-remote"></a>

## 手机与远程操控

> 想在外出或用手机时监控 Agent，只需回传批准即可

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**collie**](https://github.com/AltanS/collie)<br><sub>AltanS</sub> | 随时随地管理 herdr 的 PWA 应用。支持 Tailnet 访问、推送通知、快捷操作等 | `agent-orchestration` `ai` `ai-agents` `ai-coding` `ai-tools` | 1043 | 🔄 2026-09-20 |
| [**herdr-remote**](https://github.com/dcolinmorgan/herdr-remote)<br><sub>dcolinmorgan</sub> | 从菜单栏、手机或 Telegram 监控并操控你的 herdr Agent。本地零配置，远程连接提供免费内网穿透，无需 Tailscale | `macos` `mobile` `python` | 377 | 🔄 2026-09-19 |
| [**herdr-mobile-relay**](https://github.com/0cv/herdr-mobile-relay)<br><sub>0cv</sub> | 通过手机远程审批和监控 Herdr Agent——面向 Android/iOS 的移动 Web 应用，支持推送通知、二维码配置和多电脑中继 | `android` `approvals` `cloudflare` `ios` `mobile` | 238 | 🔄 2026-09-20 |
| [**herdr-telegram-agents**](https://github.com/permgps/herdr-telegram-agents)<br><sub>permgps</sub> | 像在终端里一样，从 Telegram 操控你的编码 Agent。每个 Agent 对应一个话题，话题图标实时显示状态，并通过带内联按钮的双向聊天进行选择。 | `claude-code` `coding-agents` `go` `telegram` `telegram-bot` | 53 | 🔄 2026-09-07 |
| [**pairfob**](https://github.com/arronKler/pairfob)<br><sub>arronKler</sub> | Herdr 的手机端界面。Codex、Claude、Grok 依然在你的电脑上运行；手机端打开的是同一批实时会话。只需配对一次——由电脑主动外拨连接，无需开放入站端口，也不需要 Tailscale。 | `herdr-mobile` `typescript` | 40 | 🔄 2026-09-20 |
| [**herdr-watch**](https://github.com/Unayung/herdr-watch)<br><sub>Unayung</sub> | 在 Apple Watch 上查看 herdr 的 Agent 状态 | `javascript` | 28 | 2026-08-14 |
| [**herdr-connect**](https://github.com/Tomyail/herdr-connect)<br><sub>Tomyail</sub> | 通过这款 iPhone 移动伴侣应用监控并操控你的 Herdr AI 编码 Agent——查看输出、发送后续指令，并在任务完成时收到通知。通过局域网或 Tailscale 私密运行，无需云端，也无需账号。 | `agent` `mobile-app` `react-native` `typescript` | 16 | 🔄 2026-09-19 |
| [**herdr-web**](https://github.com/barnuri/herdr-web)<br><sub>barnuri</sub> | 面向 herdr 的移动优先 Web UI 插件——从手机驱动你的编程 Agent，并带有通知功能 | `pwa` `typescript` | 12 | 🔄 2026-09-10 |
| [**herdr-plugin-mobile-relay**](https://github.com/benkraus/herdr-plugin-mobile-relay)<br><sub>benkraus</sub> | _(暂无描述)_ | `typescript` | 11 | 2026-08-12 |
| [**vscode-devcontainers-herdr**](https://github.com/scott-the-programmer/vscode-devcontainers-herdr)<br><sub>scott-the-programmer</sub> | 面向运行在 dev container 内的 Agent 的 Herdr 中继 | `container` `devcontainer` `rust` | 11 | 🔄 2026-09-17 |
| [**herdr-push**](https://github.com/dcolinmorgan/herdr-push)<br><sub>dcolinmorgan</sub> | herdr 插件：零依赖地将事件推送到 herdr-remote，用于手机端监控和一键批准 | `shell` | 10 | 2026-07-09 |
| [**herdr-call**](https://github.com/eliasstravik/herdr-call)<br><sub>eliasstravik</sub> | 面向 Herdr 的语音控制 | `elevenlabs` `tailscale` `voice` `typescript` | 8 | 2026-08-07 |
| [**herdr-office**](https://github.com/michaellandi/herdr-office)<br><sub>michaellandi</sub> | 一个 Herdr 插件，将你的 Agent 绘制成开放式办公室里的人物。当需要审批时，他们会举手示意。 | `javascript` | 8 | 🔄 2026-09-19 |
| [**paddock**](https://github.com/lntvan166/paddock)<br><sub>lntvan166</sub> | 面向 herdr 的移动优先仪表盘——读取其 unix socket。无需任何配置即可在手机上运行 | `agent-orchestration` `coding-agents` `herdr-mobile` `paddock` `pwa` | 7 | 2026-09-03 |
| [**herdr-remote-panes**](https://github.com/Poor-Plebs/herdr-remote-panes)<br><sub>Poor-Plebs</sub> | 从一个 Herdr 操作其他机器——从菜单中选择一台机器，即可获得该机器上的终端。还可选启用实验性的双向镜像 | `golang` `ssh` `terminal` `go` | 7 | 🔄 2026-09-11 |
| [**herdr-mobile**](https://github.com/bsorescu/herdr-mobile)<br><sub>bsorescu</sub> | 通过 SSH 控制 Herdr 编程 Agent 的手机友好型 TUI | `mobile` `ssh` `textual` `tui` `python` | 6 | 2026-08-25 |
| [**merino**](https://github.com/LoneExile/merino)<br><sub>LoneExile</sub> | Merino 🐑——面向 Herdr Agent 的远程隧道仪表盘 | `go` `macos` `menubar` `react` `wails` | 6 | 2026-08-23 |
| [**muqun-gateway**](https://github.com/osuki-dev/muqun-gateway)<br><sub>osuki-dev</sub> | 让 Muqun 能够访问你自己电脑上终端的程序。它运行在你的机器上，与 tmux 或 Herdr 通信，并直接响应你的手机——中间没有账号，也没有我们的服务器 | `rust` | 6 | 🔄 2026-09-20 |
| [**herdr-web**](https://github.com/eyalev/herdr-web)<br><sub>eyalev</sub> | 面向 herdr Agent 多路复用器的移动优先 Web UI——从手机操控你的编程 Agent | `claude-code` `mobile` `pwa` `terminal` `javascript` | 5 | 2026-07-29 |
| [**herdr-tether**](https://github.com/moneycaringcoder/herdr-tether)<br><sub>moneycaringcoder</sub> | 即使关闭 Herdr 视图，也能让本地和远程的终端任务继续运行 | `remote-development` `rust` `ssh` `terminal` `tmux` | 5 | 2026-09-01 |
| [**herdweb**](https://github.com/zlxlabs/herdweb)<br><sub>zlxlabs</sub> | 在手机上监控并操控你的编码 Agent。支持语音输入、粘贴图片、Webhook 通知，以及多设备/多服务器。 | `typescript` | 5 | 🔄 2026-09-19 |
| [**herdr-go**](https://github.com/herdr-go/herdr-go)<br><sub>herdr-go</sub> | 从任何地方控制你的 herdr 编程 Agent——私密、点对点，并通过 EasyTier 加密保护 | `dart` | 4 | 🔄 2026-09-08 |
| [**herdr-aws-ssm**](https://github.com/maayanyosef/herdr-aws-ssm)<br><sub>maayanyosef</sub> | 在 herdr --remote 会话中选择一个 EC2 实例并通过 AWS SSM 连接——无需跳板机或公网 IP | `aws-ssm` `terminal` `shell` | 4 | 2026-07-01 |
| [**herdr-portfwd**](https://github.com/miko-misa/herdr-portfwd)<br><sub>miko-misa</sub> | 面向远程机器上编程 Agent 的自动 SSH 端口转发——Ctrl+点击 Agent 打印的 localhost URL，即可在你本机以相同端口打开该页面。一个 Herdr 插件 | `ai-agents` `claude-code` `cli` `coding-agents` `developer-tools` | 4 | 🔄 2026-09-13 |
| [**herdr-whistle**](https://github.com/amurru/herdr-whistle)<br><sub>amurru</sub> | 用于远程管理 Agent 的 Herdr 插件 | `golang` `telegrambot` `go` | 3 | 2026-08-06 |
| [**herdrchat**](https://github.com/cobanov/herdrchat)<br><sub>cobanov</sub> | 在手机（iOS 和 Android）上操控你的 herdr 编码 Agent。 | `herdr-client` `herdr-integration` `herdr-mobile` `typescript` | 3 | 🔄 2026-09-17 |
| [**herdr-telegram-gate**](https://github.com/hkdom/herdr-telegram-gate)<br><sub>hkdom</sub> | 面向 herdr AI Agent 群体的 Telegram 审批收件箱 + 按风险分级的自动批准——被阻塞的 Agent 会以带批准/拒绝按钮的 Telegram 卡片形式呈现（零依赖的 Node.js） | `approval-gate` `telegram` `javascript` | 3 | 2026-08-06 |
| [**herdr-phone**](https://github.com/matheus3301/herdr-phone)<br><sub>matheus3301</sub> | 通过 Cloudflare Tunnel 和 Access 实现的 Herdr 移动端远程控制台 | `cloudflare-tunnel` `coding-agents` `developer-tools` `golang` `mobile` | 3 | 2026-09-04 |
| [**herdr-farm**](https://github.com/mejiasd3v/herdr-farm)<br><sub>mejiasd3v</sub> | Herdr 插件：将你的 Herdr 工作区和 Agent 可视化为牲畜的 3D 农场（three.js 网页应用） | `threejs` `javascript` | 3 | 2026-07-28 |
| [**herdr-devup**](https://github.com/alon-z/herdr-devup)<br><sub>alon-z</sub> | Herdr 插件：根据 .herdr/dev.toml 生成每个项目的开发布局，并同步隧道 URL 到环境变量 | `typescript` | 2 | 2026-06-22 |
| [**herdr-topbar**](https://github.com/bigbug16/herdr-topbar)<br><sub>bigbug16</sub> | 面向 herdr 的 macOS 菜单栏图标——可跳回会话、打开项目，并查看哪个 Agent 正在等待输入 | `macos` `menubar` `swift` | 2 | 2026-08-24 |
| [**herdr-remote**](https://github.com/dibin666/herdr-remote)<br><sub>dibin666</sub> | 通过浏览器远程访问你的 Herdr 终端工作区。 | `typescript` | 2 | 🔄 2026-09-17 |
| [**herdr-remotedownloder**](https://github.com/kosuketut/herdr-remotedownloder)<br><sub>kosuketut</sub> | 将文件从远程 Herdr 窗格下载到已连接的 Mac | `rust` | 2 | 🔄 2026-09-10 |
| [**herdr-mobile-pro**](https://github.com/spad-0x/herdr-mobile-pro)<br><sub>spad-0x</sub> | 一款高性能、移动优先的 PWA 仪表盘，采用 Cyber-Dark 设计风格，可直接从智能手机编排 Herdr 与自主 AI Agent。具备安全 HTTPS、语音听写输入、图片上传，以及将终端输出实时语义解析为聊天式界面的能力。 | `javascript` | 2 | 🔄 2026-09-12 |
| [**herdr-mobile-app**](https://github.com/teasec4/herdr-mobile-app)<br><sub>teasec4</sub> | 原生伴侣应用 + 轻量级 Go 中继：将 Agent 终端输出实时推送到手机，可查看状态并发送提示词——支持通过局域网、Tailscale 或 Funnel 连接。 | `ai` `devtools` `flutter` `herdr-integration` `herdr-mobile` | 2 | 2026-09-05 |
| [**herdr-web-tui**](https://github.com/tigorlazuardi/herdr-web-tui)<br><sub>tigorlazuardi</sub> | 以守护进程为核心的 Herdr 浏览器/PWA 前端，附带可选的插件启动器 | `go` | 2 | 2026-08-29 |
| [**herdr-hub**](https://github.com/alex-devdone/herdr-hub)<br><sub>alex-devdone</sub> | 将由远程连接窗格组成的 herdr 会话描述为可移植的清单文件，并可在任意机器上重建 | `python` | 1 | 2026-08-23 |
| [**shep**](https://github.com/ArtMoreno/shep)<br><sub>ArtMoreno</sub> | 在手机上使用你的 Herdr 终端。支持桌面端设置、私密配对、主题以及 QuotaDeck。 | `pwa` `terminal` `javascript` | 1 | 🔄 2026-09-09 |
| [**🆕 herdr-mobile**](https://github.com/carsol/herdr-mobile)<br><sub>carsol</sub> | 面向 Herdr 的移动优先 Web UI：在手机上查看你的 Agent、连接窗格，并与 Claude Code、Codex 聊天。 | `claude-code` `codex` `mobile` `pwa` `python` | 1 | 🔄 2026-09-15 |
| [**setnet**](https://github.com/chano-gpt/setnet)<br><sub>chano-gpt</sub> | 从手机管理多种 harness 的编程 Agent——一个 Herdr 插件 | `typescript` | 1 | 2026-08-29 |
| [**herdr-tunnel**](https://github.com/ivorpad/herdr-tunnel)<br><sub>ivorpad</sub> | herdr 插件：将本地端口暴露到公网，复制其 URL，并可随时撤下 | `tui` `python` | 1 | 2026-08-27 |
| [**herdview**](https://github.com/Orchard-Robotics/herdview)<br><sub>Orchard-Robotics</sub> | 从网页查看你的「herd」 | `html` | 1 | 🔄 2026-09-09 |
| [**🆕 herdr-web-ui**](https://github.com/devswha/herdr-web-ui)<br><sub>devswha</sub> | herdr in the browser: your live herdr workspaces, tabs and panes in a web UI / PWA, bridged over herdr's socket API | `bun` `pwa` `react` `terminal` `xterm` | 0 | 🔄 2026-09-19 |
| [**🆕 herdr-slack**](https://github.com/egemenyildiz/herdr-slack)<br><sub>egemenyildiz</sub> | 从 Slack 驱动你本地的 herdr Agent——在手机上浏览、发送提示词并启动 Agent，无需内网穿透 | `slack` `typescript` | 0 | 🔄 2026-09-17 |
| [**🆕 shahi**](https://github.com/iYassr/shahi)<br><sub>iYassr</sub> | 在手机或浏览器上查看 Agent 对话、回应权限确认提示，并管理 herdr 会话。 | `ai-agents` `claude-code` `codex` `expo` `react-native` | 0 | 🔄 2026-09-20 |
| [**🆕 herdr-approval-gate**](https://github.com/Javamomma/herdr-approval-gate)<br><sub>Javamomma</sub> | herdr 中针对 Agent 操作的人工签核关卡——在专用窗格中运行任务，对其记录进行核验，直到有人输入 「APPROVE <姓名缩写>」 才会解除阻塞 | `shell` | 0 | 2026-07-15 |
| [**🆕 herdr-reach**](https://github.com/Luisalt20/herdr-reach)<br><sub>Luisalt20</sub> | Read-only network doctor for Herdr remote machines: measures what your network actually allows and recommends a transport with evidence. No writes, no third-pa… | `cli` `cloudflare-tunnel` `connectivity` `egress` `go` | 0 | 🔄 2026-09-20 |
| [**herdr-agents-bridge**](https://github.com/maedana/herdr-agents-bridge)<br><sub>maedana</sub> | 通过本地移动端友好 Web UI，从手机监控并操作编程 Agent——扫描二维码即可连接 | `rust` | 0 | 2026-07-22 |
| [**herdr-osx-menubar**](https://github.com/marcelpanse/herdr-osx-menubar)<br><sub>marcelpanse</sub> | herdr 的 macOS 菜单栏图标——可快速返回会话、打开项目，并查看哪个 Agent 正在等待输入。 | `swift` | 0 | 🔄 2026-09-08 |
| [**🆕 hither**](https://github.com/T0mSIlver/hither)<br><sub>T0mSIlver</sub> | 在远程主机上的 herdr 窗格里按下组合键，Zed 就会在你的 Mac 上打开对应目录。 | `shell` | 0 | 🔄 2026-09-18 |
| [**herdr-codex-confirm**](https://github.com/utahta/herdr-codex-confirm)<br><sub>utahta</sub> | 一个 Herdr 插件，可批准或拒绝选定的 Codex shell 命令，拒绝时还可选择附上反馈。 | `go` | 0 | 🔄 2026-09-12 |

<details><summary>与此目的也相关</summary>

- [powerfooI/roamgate](https://github.com/powerfooI/roamgate) — A Herdr client for any screen. Control terminals, monitor coding agents, and review files and diffs from desk…
- [huketo/herdr-hitl](https://github.com/huketo/herdr-hitl) — 让 Herdr 的编码 Agent 在等待人工决策时暂停，并通过 Telegram 或 Discord 推送到你的手机。

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-agents"></a>

## Agent 编排与并行执行

> 想统一启动、分工并管理多个 AI Agent

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**agentbox**](https://github.com/madarco/agentbox)<br><sub>madarco</sub> | 一条命令即可在沙盒虚拟机中并行运行多个 Agent（本地或云端） | `claude` `claude-code` `cli` `cmux` `codex` | 465 | 🔄 2026-09-20 |
| [**pi-workflows**](https://github.com/osolmaz/pi-workflows)<br><sub>osolmaz</sub> | 面向 pi 编程 Agent 的工作流引擎、JSON 控制流工具与实时终端查看器 | `typescript` | 298 | 🔄 2026-09-18 |
| [**🆕 herdr-projects**](https://github.com/eliasstravik/herdr-projects)<br><sub>eliasstravik</sub> | A coordinator conversation, parallel worker threads, shared memory and an overview of what needs you. A Herdr plugin. | `rust` | 262 | 🔄 2026-09-18 |
| [**pi-extensible-workflows**](https://github.com/vekexasia/pi-extensible-workflows)<br><sub>vekexasia</sub> | 面向 Pi 的确定性多 Agent 工作流编排 | `pi` `workflow` `workflows` `typescript` | 224 | 🔄 2026-09-18 |
| [**herdr-board**](https://github.com/nelsonPires5/herdr-board)<br><sub>nelsonPires5</sub> | herdr 的看板工具——卡片就是提示词，会被派发给可见窗格中的 AI Agent | `board` `kanban` `kanban-board` `tui` `rust` | 143 | 🔄 2026-09-13 |
| [**herdr-dagr**](https://github.com/aemrebarut/herdr-dagr)<br><sub>aemrebarut</sub> | 将 Agent 集群实时呈现为 DAG——在 herdr 分屏窗格中展示包含尝试记录、评审关卡和证据的编排图 | `agents` `dag` `multi-agent` `orchestration` `rust` | 84 | 2026-08-23 |
| [**herdr-file-annotator**](https://github.com/JonasBaeumer/herdr-file-annotator)<br><sub>JonasBaeumer</sub> | 在不脱离实际代码库的前提下，最大化 Agent 化开发效率的 herdr 插件 | `rust` | 61 | 🔄 2026-09-20 |
| [**🆕 agent-router**](https://github.com/nidhi-singh02/agent-router)<br><sub>nidhi-singh02</sub> | CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr | `agents` `ai` `claude-code` `cli` `codex` | 54 | 🔄 2026-09-19 |
| [**agentbox-herdr-plugin**](https://github.com/madarco/agentbox-herdr-plugin)<br><sub>madarco</sub> | 一条命令即可在沙盒虚拟机中并行运行多个 Agent（本地或云端） | `claude-code` `codex-cli` `opencode` `sandbox` `shell` | 32 | 2026-06-24 |
| [**🆕 entwurf**](https://github.com/junghan0611/entwurf)<br><sub>junghan0611</sub> | Herdr and tmux sibling AI sessions: pi, Claude Code, Codex, Copilot, OMP and Antigravity can message and spawn each other while keeping their own auth, tools a… | `acp` `agent-client-protocol` `ai-agent` `claude-code` `codex` | 28 | 🔄 2026-09-20 |
| [**herdmates**](https://github.com/caioniehues/herdmates)<br><sub>caioniehues</sub> | herdr 原生的 Claude Code Agent 团队——teammux 兼容层、任务控制面板、聚焦窗格 | `agent-teams` `claude-code` `rust` `tui` | 24 | 2026-08-21 |
| [**pi-herd**](https://github.com/ribbons-digital/pi-herd)<br><sub>ribbons-digital</sub> | 结合 Herdr 窗格和 git 工作树，对 Pi 会话进行可视化编排 | `typescript` | 21 | 2026-07-06 |
| [**herdr-agent-handoff**](https://github.com/sanirudh17/herdr-agent-handoff)<br><sub>sanirudh17</sub> | 将进行中的 Agent 会话交接给另一个已安装编程 Agent 的新会话的 Herdr 插件——完整会话直接放入提示词中传递，无需摘要、无需截断记录、无需再写后续提示 | `agent-handoff` `claude-code` `codex` `coding-agents` `developer-tools` | 17 | 🔄 2026-09-14 |
| [**herdr-browser**](https://github.com/StructuPath/herdr-browser)<br><sub>StructuPath</sub> | Herdr 的可操控 Agent 浏览器窗格——支持实时流传输、真实交互、自适应渲染、控制台/页面错误显示、录制和 localhost 路由 | `terminal` `javascript` | 17 | 🔄 2026-09-16 |
| [**PromptPilot**](https://github.com/ivanarama/PromptPilot)<br><sub>ivanarama</sub> | 面向 Claude Code 及其他 AI CLI 的后台任务队列——配有网页 UI 和 Telegram 机器人 | `ai-agents` `claude-code` `telegram-bot` `python` | 16 | 🔄 2026-09-17 |
| [**herdr-world**](https://github.com/IvoryHeart/herdr-world)<br><sub>IvoryHeart</sub> | Herdr World——面向 Herdr 的多界面网页体验 | `multi-agent` `observability` `pixel-art` `react` `rust` | 15 | 🔄 2026-09-19 |
| [**herdr-vercel-sandbox-plugin**](https://github.com/vercel-labs/herdr-vercel-sandbox-plugin)<br><sub>vercel-labs</sub> | 从 Herdr 在隔离的 Vercel Sandbox 中运行基于终端的编程 Agent | `javascript` | 13 | 2026-08-09 |
| [**herdr-social-glass**](https://github.com/ythx-101/herdr-social-glass)<br><sub>ythx-101</sub> | 面向 macOS 版 Herdr 的、适合截图分享的 Social Glass 主题与工作流插件 | `macos` `multi-agent` `terminal-theme` `shell` | 12 | 2026-08-21 |
| [**vibetty**](https://github.com/second-state/vibetty)<br><sub>second-state</sub> | 通过 MQTT 将 AI Agent 终端实时共享给智能硬件（vibekeys、vibewatch 等），也可作为 Herdr 插件使用 | `claude-code` `codex` `vibecoding` `rust` | 11 | 2026-08-17 |
| [**agys**](https://github.com/quaywin/agys)<br><sub>quaywin</sub> | 通过零污染沙盒，为 Herdr 中的 Antigravity CLI 提供轻松的多配置文件隔离和实时配额追踪 | `ai-agents` `antigravity` `cli` `context-window` `developer-tools` | 10 | 🔄 2026-09-19 |
| [**herdr-catchup**](https://github.com/wilbeibi/herdr-catchup)<br><sub>wilbeibi</sub> | herdr 的跨 Agent 编程会话交接：从正在运行的窗格中，对 Claude Code、Codex、Cursor、Cline 或 OpenCode 会话进行摘要、分叉，或转交给另一个 Agent | `ai-agents` `claude-code` `codex` `coding-agents` `context-handoff` | 10 | 🔄 2026-09-20 |
| [**🆕 deevs-pi-kit**](https://github.com/DeevsDeevs/deevs-pi-kit)<br><sub>DeevsDeevs</sub> | 完美的 pi 工具包，让 Deevs 的工程师效率提升 10 倍。 | `agents` `pi` `pi-agent` `pi-extension` `pi-package` | 9 | 🔄 2026-09-20 |
| [**herdr-helpr**](https://github.com/sohanemon/herdr-helpr)<br><sub>sohanemon</sub> | 面向 herdr 的、由提示词驱动的工作区和窗格管理 | `ai-agents` `bun` `cli` `developer-tools` `ink` | 8 | 2026-07-16 |
| [**herdr-swarm**](https://github.com/StructuPath/herdr-swarm)<br><sub>StructuPath</sub> | 在同一仓库上安全并行运行多个编程 Agent：为每个 Agent 分配独立工作树，实时可见变更，Herdr 上以审查优先的方式收获成果 | `terminal` `javascript` | 8 | 🔄 2026-09-14 |
| [**herdr-agent-messenger**](https://github.com/aashishd/herdr-agent-messenger)<br><sub>aashishd</sub> | 让运行中的 Herdr 窗格间的 AI Agent 互相发送简明、自成一体的消息——一个 Agent 可以在不共享完整上下文的情况下与另一个协调工作 | `python` | 7 | 2026-08-02 |
| [**shepherdr**](https://github.com/afogel/shepherdr)<br><sub>afogel</sub> | 将委派出去的编程 Agent 收拢到可见、可审查的 herdr 窗格中，供你观察、恢复和接管的 herdr 插件 | `ai-agents` `claude-code` `codex` `cursor` `rust` | 6 | 2026-07-24 |
| [**herdr-scuttlebutt**](https://github.com/andybarilla/herdr-scuttlebutt)<br><sub>andybarilla</sub> | 为 herdr 会话中的 Agent 提供共享聊天室的 herdr 插件 | `rust` | 6 | 2026-08-31 |
| [**herdr-orchestrate**](https://github.com/darjss/herdr-orchestrate)<br><sub>darjss</sub> | 为可见的 Herdr worker 会话提供 Pi 原生编排——运行看板、持久化的提示词/报告/状态、独立的 git 工作树，以及明确的模型路由 | `pi-package` `typescript` | 6 | 2026-07-13 |
| [**pier**](https://github.com/July24/pier)<br><sub>July24</sub> | Pi 是编程 Agent 的载体，Herdr 是终端工作区管理器。pier 补上了 pi 刻意省略的两项能力——todo 列表循环和可交互的子 Agent——并将 herdr 的窗格/标签页层作为它们的视觉与交互基础 | `pi-coding-agent` `typescript` | 6 | 🔄 2026-09-20 |
| [**herdr-triage**](https://github.com/natori-hrj/herdr-triage)<br><sub>natori-hrj</sub> | herdr 的关注度分级——按谁最需要你来排序 Agent；长时间被阻塞的 Agent 会排到最前面 | `ai-agents` `triage` `rust` | 6 | 2026-07-23 |
| [**herdr-space-scoped-agents**](https://github.com/ShankyJS/herdr-space-scoped-agents)<br><sub>ShankyJS</sub> | 将 Agent 面板范围限定为当前聚焦空间的 herdr 插件 | `coding-agents` `terminal` `go` | 6 | 2026-07-23 |
| [**herdr-devcontainer**](https://github.com/gambtho/herdr-devcontainer)<br><sub>gambtho</sub> | 通过官方 Dev Containers CLI，在仓库的 Dev Container 内打开 shell 和编程 Agent 的 Herdr 插件 | `coding-agents` `containers` `devcontainers` `developer-tools` `development-environment` | 5 | 2026-08-13 |
| [**herdr-gamepad**](https://github.com/htlin222/herdr-gamepad)<br><sub>htlin222</sub> | 用游戏手柄操控 Herdr。窝在沙发上巡视你的 AI Agent、拆分窗格、切换工作区——任意手柄，60 秒内自定义按键映射 | `ai-agents` `gamepad` `macos` `swift` `terminal-multiplexer` | 5 | 🔄 2026-09-09 |
| [**chatter**](https://github.com/marcvermeeren/chatter)<br><sub>marcvermeeren</sub> | Chatter 是一次跨 harness 的 Agent 协作实验——为在 Herdr 中处理同一 Git 仓库的多个 Agent 提供共享群聊和上下文层 | `agent-collaboration` `agentic-ai` `agentic-workflow` `ai-agents` `group-chat` | 5 | 2026-08-18 |
| [**herdr-fleet**](https://github.com/Northern-Lighthouse/herdr-fleet)<br><sub>Northern-Lighthouse</sub> | 通过 Tailscale 管理一批 herdr 机器——仪表盘插件、自动发现、感知容量的 Agent 派发、无盘工作区 | `ai-agents` `tailscale` `python` | 5 | 2026-08-14 |
| [**herdr-insight**](https://github.com/0x5c0f/herdr-insight)<br><sub>0x5c0f</sub> | Agent 状态时间线面板 | `rust` | 4 | 2026-06-23 |
| [**herdr-worker-orchestrator**](https://github.com/anhnd3005-infinity/herdr-worker-orchestrator)<br><sub>anhnd3005-infinity</sub> | 通过 Herdr 管理的窗格，将任务派发给 CLI Agent worker（agy、codex 等）——支持有状态的任务追踪、工作树隔离和基于差异的评审。同时适用于 Claude Code 和 Herdr 的双用插件 | `html` | 4 | 2026-08-25 |
| [**herdr-pane-topic-sync**](https://github.com/danbuhler/herdr-pane-topic-sync)<br><sub>danbuhler</sub> | herdr 插件：将窗格和标签页自动命名为每个 Agent（Claude Code、Codex 等）实时的主题，而不是「1」「2」「3」 | `ai-agents` `claude-code` `terminal` `tmux-alternative` `javascript` | 4 | 2026-09-02 |
| [**herdr-openclaw**](https://github.com/gejiliang/herdr-openclaw)<br><sub>gejiliang</sub> | herdr 插件：将 OpenClaw 的 TUI 窗格作为一等公民的 herdr Agent 来管理 | `openclaw` `terminal` `javascript` | 4 | 2026-08-13 |
| [**herdr-espresso**](https://github.com/Hanyang-Li/herdr-espresso)<br><sub>Hanyang-Li</sub> | 在 Agent 运行时，即使合上盖子也保持 MacBook 唤醒状态 | `rust` | 4 | 2026-07-25 |
| [**herdr-a2a**](https://github.com/IsaiasZc/herdr-a2a)<br><sub>IsaiasZc</sub> | 通过 A2A 为 Herdr 提供的可靠 Agent 间委派层 | `typescript` | 4 | 2026-08-27 |
| [**herdr-walkietalkie**](https://github.com/jeffory/herdr-walkietalkie)<br><sub>jeffory</sub> | herdr 插件：token 高效的跨 Agent 委派（wt）——编排 Agent 在标签页或工作树中派生出 Claude/OpenCode/Antigravity 的 worker | `shell` | 4 | 2026-08-12 |
| [**herdr-prompt-library**](https://github.com/jwkicklighter/herdr-prompt-library)<br><sub>jwkicklighter</sub> | 用于浏览、管理并将可复用的本地或全局 Markdown 提示词插入到聚焦窗格中的 Herdr 插件 | `go` `golang` `prompting` `snippets` `tui` | 4 | 2026-09-01 |
| [**herdr-blaxel-sandbox-plugin**](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin)<br><sub>blaxel-ai</sub> | 从 Herdr 在持久化的 Blaxel Sandbox 中运行编程 Agent | `blaxel` `claude-code` `codex` `coding-agents` `opencode` | 3 | 🔄 2026-09-16 |
| [**herdr-theos-settler**](https://github.com/calebcauthon/herdr-theos-settler)<br><sub>calebcauthon</sub> | 将已完成的 Herdr Agent 标签页和工作区沉到活跃工作下方，让它们不再挡路。Theo 的点子 | `rust` | 3 | 2026-07-23 |
| [**herdr-loop**](https://github.com/cyperx84/herdr-loop)<br><sub>cyperx84</sub> | 面向 herdr 的声明式、事件驱动的循环与图编排——同时运行 Claude Code、Codex、opencode 和 pi，直到工作收敛 | `ai-agents` `golang` `orchestration` `go` | 3 | 🔄 2026-09-10 |
| [**🆕 AgentRadio**](https://github.com/detailles/AgentRadio)<br><sub>detailles</sub> | Local message bus for AI coding agents running in Herdr panes — join, DM, presence, offline delivery | `agent-orchestration` `multi-agent` `radio` `python` | 3 | 🔄 2026-09-20 |
| [**herdr-agent-restart**](https://github.com/hmu332233/herdr-agent-restart)<br><sub>hmu332233</sub> | 当显示出现异常时，通过一个快捷键重启 Herdr 中的 Agent，并继续同一段对话。 | `agent-restart` `javascript` | 3 | 🔄 2026-09-08 |
| [**herdr-orchestrator**](https://github.com/kylezk777/herdr-orchestrator)<br><sub>kylezk777</sub> | Herdr-orch 是运行在 Herdr 之上的基于文件的 Agent 编排工具 | `agent-orchestration` `orchestrator` `rust` | 3 | 2026-07-26 |
| [**🆕 kubeflock**](https://github.com/LoriKarikari/kubeflock)<br><sub>LoriKarikari</sub> | 在 Herdr 中创建并连接 Kubernetes 沙箱。 | `agent-sandbox` `gvisor` `kubernetes` `sandbox` `go` | 3 | 🔄 2026-09-11 |
| [**herdr-agent-profiles**](https://github.com/mikeyobrien/herdr-agent-profiles)<br><sub>mikeyobrien</sub> | 面向 Herdr 的数据驱动型 CLI harness 与模型配置文件 | `ai-agents` `terminal` `python` | 3 | 2026-08-10 |
| [**herdr-agents-history**](https://github.com/speardragon/herdr-agents-history)<br><sub>speardragon</sub> | 查看你的 AI 编程 Agent 实际在做什么——一个实时、键盘驱动的 herdr TUI，串流展示你所有 Agent（Claude Code 和 Codex）的每一次工具调用 | `ai-agents` `claude-code` `codex` `tui` `typescript` | 3 | 2026-07-19 |
| [**herdr-agent-office**](https://github.com/suisya-systems/herdr-agent-office)<br><sub>suisya-systems</sub> | 将你的 Agent 团队呈现为像素风办公室的 herdr 插件。查看谁在工作、谁卡住了，并可直接跳转过去 | `python` | 3 | 2026-07-25 |
| [**herdr-upstash-box**](https://github.com/upstash/herdr-upstash-box)<br><sub>upstash</sub> | Herdr 插件：从你正在查看的 worktree 中，在 Upstash Box 里运行编码 Agent。 | `claude-code` `coding-agents` `sandbox` `upstash` `typescript` | 3 | 🔄 2026-09-10 |
| [**🆕 pet-town**](https://github.com/abhishek944/pet-town)<br><sub>abhishek944</sub> | A transparent desktop village for live Herdr agents | `rust` | 2 | 🔄 2026-09-20 |
| [**herdr-birdseye**](https://github.com/calebcauthon/herdr-birdseye)<br><sub>calebcauthon</sub> | 以鸟瞰视角查看 herdr 中的 Agent | `rust` | 2 | 2026-07-24 |
| [**🆕 herdr-sbx-plugin**](https://github.com/dirien/herdr-sbx-plugin)<br><sub>dirien</sub> | 在 Docker Sandboxes（sbx）中运行编码 Agent 的 Herdr 插件，每个 Agent 对应一个 microVM。 | `coding-agents` `docker-sandboxes` `javascript` | 2 | 🔄 2026-09-13 |
| [**herdr-cursor**](https://github.com/gabriel-laet/herdr-cursor)<br><sub>gabriel-laet</sub> | 将 Cursor 的云端 Agent 作为一等公民的 herdr 窗格来使用 | `typescript` | 2 | 🔄 2026-09-08 |
| [**herdr-newtab-plus**](https://github.com/jeffarese/herdr-newtab-plus)<br><sub>jeffarese</sub> | 会询问文件夹和 Agent 的 Herdr 新标签页：自动补全真实路径，记住你常用的工作目录，并为你启动 Agent | `python` | 2 | 2026-07-26 |
| [**herdr-shame-report**](https://github.com/JYasha11/herdr-shame-report)<br><sub>JYasha11</sub> | 永久记录你让 AI Agent 等了多久的账本。羊会记住的 | `javascript` | 2 | 2026-07-10 |
| [**herdr-link**](https://github.com/LZHcode1986/herdr-link)<br><sub>LZHcode1986</sub> | 为 Herdr 会话提供更快、更省 token、无需推理的跨 Agent 互操作性。用一份统一的契约取代笨重的 skill，涵盖对等发现、消息传递和窗格生命周期 | `typescript` | 2 | 🔄 2026-09-11 |
| [**herdr-agents-status**](https://github.com/maedana/herdr-agents-status)<br><sub>maedana</sub> | 显示 Herdr Agent 状态的常驻置顶透明浮层——claudeye 的精神续作，专为 Herdr（而非 tmux）打造 | `rust` | 2 | 2026-08-15 |
| [**herdr-redact**](https://github.com/moneycaringcoder/herdr-redact)<br><sub>moneycaringcoder</sub> | 当 Agent 窗格打印出凭据时向你发出警告——在你截图、直播或粘贴到聊天窗口之前提醒你 | `rust` `secret-detection` `security` `terminal` | 2 | 2026-09-01 |
| [**🆕 muster**](https://github.com/ofelcan164/muster)<br><sub>ofelcan164</sub> | 在一个屏幕上查看所有仓库中的所有 Agent。一个 herdr 插件。 | `go` | 2 | 🔄 2026-09-16 |
| [**herdr-approve-all**](https://github.com/RenKoya1/herdr-approve-all)<br><sub>RenKoya1</sub> | herdr 插件：一键批准所有被阻塞的 Agent（一次按键处理所有待处理的权限提示） | `shell` | 2 | 2026-08-16 |
| [**herdr-code-board**](https://github.com/sazardev/herdr-code-board)<br><sub>sazardev</sub> | Herdr 内面向 Agent 提示词的看板队列——卡片会将真实 Agent 派发到窗格、工作树和工作区，并可通过规则将一张卡片链到下一张 | `ai-agents` `kanban` `rust` `tui` | 2 | 2026-08-30 |
| [**herdr-achievements**](https://github.com/SerHappy/herdr-achievements)<br><sub>SerHappy</sub> | 为你的 Herdr AI Agent 群体添加成就和小小的庆祝 | `achievements` `ai-agents` `developer-tools` `gamification` `go` | 2 | 2026-07-30 |
| [**herdr-conductor**](https://github.com/StructuPath/herdr-conductor)<br><sub>StructuPath</sub> | 将功能交付团队编排为可见的 Herdr Agent 窗格——Conductor 插件 | `orchestration` `javascript` | 2 | 🔄 2026-09-14 |
| [**herdr-wakeup**](https://github.com/usrivastava92/herdr-wakeup)<br><sub>usrivastava92</sub> | 在 Herdr 管理的 Agent 工作期间，让 macOS 或 Linux 保持唤醒状态的 Herdr 插件 | `power-management` `sleep-prevention` `wakeup` `rust` | 2 | 2026-07-17 |
| [**herdr-auto-yes-sir**](https://github.com/xlinx/herdr-auto-yes-sir)<br><sub>xlinx</sub> | herdr-auto-yes-sir——当 Agent 请求批准时，让运行不被阻塞地继续下去，类似 codex 的行为 | `javascript` | 2 | 2026-08-20 |
| [**herdr-agent-timer**](https://github.com/Yemeni/herdr-agent-timer)<br><sub>Yemeni</sub> | 让每个 Agent 的状态标签与其耗时交替显示的 Herdr 插件 | `shell` | 2 | 2026-08-14 |
| [**herdr-cadence**](https://github.com/zhenyufu/herdr-cadence)<br><sub>zhenyufu</sub> | 由一个 Lead 和一组 Agent 组成的轻量级 Agent 编排器 | `rust` | 2 | 🔄 2026-09-07 |
| [**herdr-pouch**](https://github.com/AltanS/herdr-pouch)<br><sub>AltanS</sub> | herdr 插件：预先为 Agent 存储提示词，待其就绪时再插入 | `ai-agents` `ai-coding` `ai-tools` `multiplexing` `typescript` | 1 | 2026-09-02 |
| [**herdr-pi-reloader**](https://github.com/anrunt/herdr-pi-reloader)<br><sub>anrunt</sub> | 从 Herdr 浮层 TUI 中重新加载或重启闲置的 Pi Agent 会话 | `rust` | 1 | 2026-07-18 |
| [**herdr-convo**](https://github.com/arvemy/herdr-convo)<br><sub>arvemy</sub> | 以标准化的对话轮次读取其他编码 Agent 的对话——在 Claude Code、Codex、OpenCode 和 Pi 之间保持统一格式。 | `ai-agents` `claude-code` `cli` `codex` `coding-agents` | 1 | 🔄 2026-09-11 |
| [**herdr-quick-prompt**](https://github.com/astwys/herdr-quick-prompt)<br><sub>astwys</sub> | 向 Agent 窗格发送预定义提示词的 Herdr 插件 | `shell` | 1 | 2026-08-24 |
| [**herdr-handoff**](https://github.com/devops-fj/herdr-handoff)<br><sub>devops-fj</sub> | 在 Herdr 编程 Agent 之间预览并安全地移交本地工作上下文 | `ai-agents` `coding-agents` `go` | 1 | 2026-08-21 |
| [**🆕 herdr-docket**](https://github.com/DnzzL/herdr-docket)<br><sub>DnzzL</sub> | 由你的 Herdr Agent 处理的共享任务队列——类似 Backlog.md 或 Basecamp：将任务分配给指定名称的 Agent，守护进程会逐一执行。 | `go` | 1 | 🔄 2026-09-16 |
| [**🆕 herdr-chat**](https://github.com/eliasstravik/herdr-chat)<br><sub>eliasstravik</sub> | 为运行在 Herdr 中的 Agent 提供结构化的实时聊天视图 | `typescript` | 1 | 2026-08-24 |
| [**🆕 herdr-tasks**](https://github.com/Eslsamu/herdr-tasks)<br><sub>Eslsamu</sub> | 为 Herdr 提供由 Agent 拥有的本地任务队列，并配有实时的只读浏览器视图。 | `ai-agents` `codex` `local-first` `python` `sqlite` | 1 | 🔄 2026-09-09 |
| [**herdr-state-icons**](https://github.com/flowreaction/herdr-state-icons)<br><sub>flowreaction</sub> | 为 HerdR 的空间与 Agent 提供可着色的动态生命周期图标。 | `python` | 1 | 🔄 2026-09-10 |
| [**herdr-agent-team**](https://github.com/gdli6177/herdr-agent-team)<br><sub>gdli6177</sub> | 用 Markdown 定义 Agent 团队的 Herdr 插件 | `javascript` | 1 | 2026-08-16 |
| [**herdr-prompt-bucket**](https://github.com/GNURub/herdr-prompt-bucket)<br><sub>GNURub</sub> | 面向运行在 Herdr 中的编程 Agent 的持久化、有序的提示词队列 | `claude-code` `codex` `coding-agents` `opencode` `typescript` | 1 | 2026-08-19 |
| [**🆕 herdr-agent-chat**](https://github.com/GODVvVZzz/herdr-agent-chat)<br><sub>GODVvVZzz</sub> | 在 Herdr 上的终端 Agent 之间实现类似聊天的任务委托——非阻塞式派发，并保证结果回报。 | `ai-agents` `claude-code` `python` | 1 | 🔄 2026-09-16 |
| [**LunaCrab**](https://github.com/GranamyrBR/LunaCrab)<br><sub>GranamyrBR</sub> | 为另一个项目保留 | `agents` `developer-tools` `multi-agent` `observability` `rust` | 1 | 2026-08-10 |
| [**🆕 herdr-plugin-done-timer**](https://github.com/hanjm93/herdr-plugin-done-timer)<br><sub>hanjm93</sub> | 在 herdr 的 Agent 面板中，为每个 AI Agent 显示从其对话记录中读取的 prompt 缓存倒计时。 | `ai-agents` `claude-code` `shell` | 1 | 🔄 2026-09-15 |
| [**agent-keep-awake**](https://github.com/happyeric77/agent-keep-awake)<br><sub>happyeric77</sub> | 在 Herdr Agent 工作期间阻止 macOS 休眠 | `javascript` | 1 | 2026-08-12 |
| [**herdr-dispatch**](https://github.com/husniadil/herdr-dispatch)<br><sub>husniadil</sub> | 面向 herdr-tasks 看板的调度器——为每个已就绪的任务启动一个 worker Agent 窗格，传递目标、追踪 worker，并在评审处暂停。全部由一个 Go 二进制程序实现 | `agent-orchestration` `ai-agents` `dispatcher` `mcp-server` `go` | 1 | 2026-08-31 |
| [**herdr-annotations**](https://github.com/IgorWarzocha/herdr-annotations)<br><sub>IgorWarzocha</sub> | 收集对终端选中内容的注释，并暂存到 Herdr Agent 中 | `ai-agents` `annotations` `terminal` `javascript` | 1 | 2026-07-18 |
| [**herdr-agent-prompt**](https://github.com/jeffbking/herdr-agent-prompt)<br><sub>jeffbking</sub> | Herdr 插件：按下 prefix+p 打开浮层，查看当前聚焦编码 Agent（Claude Code、Codex、Antigravity、Pi）的原始 prompt。 | `claude-code` `codex` `python` | 1 | 🔄 2026-09-08 |
| [**herdr-plan-approve**](https://github.com/jerryfane/herdr-plan-approve)<br><sub>jerryfane</sub> | 在 herdr 中自动批准 Claude Code 的计划模式对话框——Agent 制定计划后无需按键即可直接执行 | `claude-code` `shell` | 1 | 2026-08-25 |
| [**corral**](https://github.com/jirathip-dev/corral)<br><sub>jirathip-dev</sub> | 面向 herdr 编码 Agent 群的只读监控工具。 | `agent-orchestration` `ai-agents` `coding-agents` `devtools` `fleet-management` | 1 | 🔄 2026-09-19 |
| [**herdr-watcher**](https://github.com/joshka0/herdr-watcher)<br><sub>joshka0</sub> | 为 Herdr Agent 提供持久化的执行续接和分离式 worker 回调 | `rust` | 1 | 2026-08-02 |
| [**🆕 herdr-attention-queue**](https://github.com/justmytwospence/herdr-attention-queue)<br><sub>justmytwospence</sub> | herdr 插件：在你处理之前持续保持「完成」状态，并提供按需关注优先级排序的 Agents 面板。 | `python` | 1 | 🔄 2026-09-14 |
| [**herdr-turn-coordinator**](https://github.com/KarthusLorin/herdr-turn-coordinator)<br><sub>KarthusLorin</sub> | 在不依赖模型驱动的状态轮询的情况下，维持交互式 Herdr Agent TUI | `ai-agents` `python` | 1 | 🔄 2026-09-18 |
| [**herdr-island**](https://github.com/kay-ws/herdr-island)<br><sub>kay-ws</sub> | 找出正在等待你处理的 Agent——显示每个 herdr Agent 停下的原因，并将 Agents 面板筛选到只剩这些 | `shell` | 1 | 2026-08-04 |
| [**🆕 shop-plugin**](https://github.com/kyrosle/shop-plugin)<br><sub>kyrosle</sub> | A visible multi-agent workstation for Pi + Herdr, with configurable Lead/Worker models, file-based task handoffs, and explicit review. Local alpha. | `coding-agent` `developer-tools` `human-in-the-loop` `multi-agent` `pi-coding-agent` | 1 | 🔄 2026-09-20 |
| [**sheprd**](https://github.com/m-mohamed/sheprd)<br><sub>m-mohamed</sub> | 将 Pi、Codex、Claude Code 和 OpenCode 统一收纳到一个可见且隔离的 Herdr「Flok」中 | `agent-tools` `claude-code` `cli` `codex` `coding-agents` | 1 | 2026-08-25 |
| [**herdr-agents-preview**](https://github.com/maedana/herdr-agents-preview)<br><sub>maedana</sub> | Herdr 的多 Agent 终端预览仪表盘：同时显示所有运行中的 Agent，所选 Agent 占据大部分宽度 | `rust` | 1 | 2026-08-14 |
| [**herdr-standup**](https://github.com/natori-hrj/herdr-standup)<br><sub>natori-hrj</sub> | herdr 的 Agent 站会摘要——按 Agent 汇总其所在仓库中的提交和未提交的工作 | `ai-agents` `git` `standup` `rust` | 1 | 2026-07-23 |
| [**herdr-replay**](https://github.com/neospeed83/herdr-replay)<br><sub>neospeed83</sub> | 将多 Agent 的 Herdr 编程会话录制并回放为可交互的时间线 | `ai-agents` `developer-tools` `terminal-recording` `rust` | 1 | 2026-08-29 |
| [**herdr-tournament**](https://github.com/neospeed83/herdr-tournament)<br><sub>neospeed83</sub> | 面向 Herdr 的对抗式多 Agent 代码评审 | `rust` | 1 | 2026-08-29 |
| [**herdr-caffeinate**](https://github.com/nwarwick/herdr-caffeinate)<br><sub>nwarwick</sub> | 在 Herdr Agent 工作期间阻止 macOS 系统休眠 | `caffeinate` `coding-agents` `macos` `shell` | 1 | 2026-07-29 |
| [**herdr-spawn**](https://github.com/nytafar/herdr-spawn)<br><sub>nytafar</sub> | 一个 MCP 工具，将聊天中的提示词交给你某台主机上开启了 Remote Control 的真实 Claude Code 会话 | `python` | 1 | 2026-08-21 |
| [**🆕 herdr-tasks**](https://github.com/pinkpixel-dev/herdr-tasks)<br><sub>pinkpixel-dev</sub> | A Herdr plugin that puts your agent's task list in a split pane beside it, checked off as the agent works. | `ai` `ai-agents` `antigravity` `claude-code` `cli` | 1 | 🔄 2026-09-19 |
| [**herdr-imebox**](https://github.com/Sawakee/herdr-imebox)<br><sub>Sawakee</sub> | 便于向 herdr 中 AI Agent 窗格输入日文/CJK 文字的 IME 友好弹出文本框 | `cjk` `ime` `input-method` `japanese` `ratatui` | 1 | 2026-07-17 |
| [**🆕 herdr-testrun**](https://github.com/shindakun/herdr-testrun)<br><sub>shindakun</sub> | Herdr plugin. Runs a project's tests in a pane, lists the failures, sends them to the agent on one key. | `go` `nodejs` `rust` | 1 | 🔄 2026-09-20 |
| [**herdr-awake**](https://github.com/susomejias/herdr-awake)<br><sub>susomejias</sub> | herdr 插件：在 Herdr Agent 忙碌期间保持机器唤醒 | `shell` | 1 | 2026-08-26 |
| [**herdr-traex**](https://github.com/szrenwei/herdr-traex)<br><sub>szrenwei</sub> | 将 TraeX Agent 的生命周期与元数据接入 Herdr Marketplace | `traex` `python` | 1 | 2026-08-04 |
| [**herdr-forkr**](https://github.com/t4t5/herdr-forkr)<br><sub>t4t5</sub> | 在新的 herdr 窗格中派生（fork）一段 Agent 对话。 | `shell` | 1 | 🔄 2026-09-10 |
| [**herdr-orc**](https://github.com/tamdogood/herdr-orc)<br><sub>tamdogood</sub> | 面向 Herdr 的极简、基于配置文件驱动的自定义编排器 | `ai-agents` `multi-agent` `orchestrator` `javascript` | 1 | 2026-08-11 |
| [**tinysend-herdr**](https://github.com/tiny-send/tinysend-herdr)<br><sub>tiny-send</sub> | herdr 插件：当 Agent 阻塞/完成时给自己发邮件，回复即可解除阻塞。由 tinysend 提供支持 | `ai-agents` `tinysend` `javascript` | 1 | 2026-06-26 |
| [**herdr-rovo-dev**](https://github.com/usrivastava92/herdr-rovo-dev)<br><sub>usrivastava92</sub> | 检测 Rovo Dev CLI 会话并将其作为运行中的 Agent 报告给 Herdr 的插件 | `ai-agent` `rovo` `rovo-dev` `shell` | 1 | 2026-07-19 |
| [**herdr-polyglot**](https://github.com/wazum/herdr-polyglot)<br><sub>wazum</sub> | 用你自己的语言编写编程 Agent 提示词——DeepL 或 Google Cloud Translate 会将其翻译为英文，并投递到 Claude Code、Codex 或任意 herdr Agent 窗格中 | `ai-agents` `bubbletea` `bubbletea-tui` `claude-code` `codex` | 1 | 2026-09-01 |
| [**herdr-session-titles**](https://github.com/wxomi/herdr-session-titles)<br><sub>wxomi</sub> | 为 Herdr 中的 Devin、Cursor、Agy、Kiro 和 Claude 提供丰富的会话标题与任务上下文。 | `ai-agents` `terminal` `python` | 1 | 🔄 2026-09-17 |
| [**cbds**](https://github.com/zqkra/cbds)<br><sub>zqkra</sub> | 面向 Herdr 群体的可靠多 Agent 编排。提供持久化任务、权威的 worker 报告，以及不会卡死的等待机制 | `agents` `cli` `multi-agent` `orchestration` `javascript` | 1 | 2026-08-31 |
| [**🆕 herdr-simple-prompts**](https://github.com/AlexSamarsky/herdr-simple-prompts)<br><sub>AlexSamarsky</sub> | 只显示你自己的提示词和 Codex 或 Claude 的最终回答，并配有可用的输入框 | `rust` | 0 | 2026-08-31 |
| [**herdr-dynamic-workflow**](https://github.com/andthezhang/herdr-dynamic-workflow)<br><sub>andthezhang</sub> | 用于在 Herdr 中编排编程 Agent CLI 的 JavaScript 工作流 | `agent-fleet` `agent-orchestration` `agent-swarm` `agentic-ai` `agents` | 0 | 2026-08-30 |
| [**herdr-warp**](https://github.com/cdpath/herdr-warp)<br><sub>cdpath</sub> | 在 Herdr 窗格中驱动交互式 Warp Agent CLI（warp）的 Herdr 插件：支持 open/send/status/wait/read/approve/deny/new/stop/exit，并通过屏幕抓取判断 idle/working/blocked 状态 | `shell` | 0 | 2026-08-13 |
| [**clawsouls-herdr-plugin**](https://github.com/clawsouls/clawsouls-herdr-plugin)<br><sub>clawsouls</sub> | _(暂无描述)_ | `ai-agents` `persona` `shell` | 0 | 2026-08-11 |
| [**herdr-supervisor**](https://github.com/Ejlonn/herdr-supervisor)<br><sub>Ejlonn</sub> | 为运行在 Herdr 中的编码 Agent 提供持久化的人机协同编排与远程控制。 | `python` | 0 | 🔄 2026-09-12 |
| [**herdr-nudge**](https://github.com/EricBois/herdr-nudge)<br><sub>EricBois</sub> | 为 herdr Agent 设置「继续提醒」——在指定时间，或它变为闲置/被阻塞时触发 | `shell` | 0 | 2026-07-17 |
| [**herdr-mail**](https://github.com/husniadil/herdr-mail)<br><sub>husniadil</sub> | Herdr 上编程 Agent 之间的异步邮件——以存储为准的邮箱、作为提示的单行窗格标记，以及带追踪义务的 ask/reply，全部由一个 Go 二进制程序实现 | `ai-agents` `mail` `mcp-server` `sqlite` `go` | 0 | 2026-08-30 |
| [**🆕 herdr-harvest**](https://github.com/j1nn0/herdr-harvest)<br><sub>j1nn0</sub> | 收集你的 Agent 群体产出的结果——一个 Herdr 插件，将 Agent 完成时的输出捕获到持久化的结果收件箱中。 | `typescript` | 0 | 🔄 2026-09-18 |
| [**🆕 herdr-suffix-agent-filter**](https://github.com/kazimshah39/herdr-suffix-agent-filter)<br><sub>kazimshah39</sub> | 在精确的 Space 后缀分组视图与默认视图之间切换 Herdr 的 Agents 侧边栏 | `coding-agents` `developer-tools` `terminal` `javascript` | 0 | 2026-08-27 |
| [**🆕 herdr-math**](https://github.com/liambern/herdr-math)<br><sub>liambern</sub> | 在 Herdr 终端窗格中渲染 LaTeX 显示公式，并提供与 harness 无关的 Agent 技能。 | `ai-agents` `latex` `mathjax` `terminal` `javascript` | 0 | 🔄 2026-09-14 |
| [**🆕 herdr-spaces**](https://github.com/lukecameron/herdr-spaces)<br><sub>lukecameron</sub> | Agent counts and model-generated names for Herdr spaces | `go` | 0 | 🔄 2026-09-18 |
| [**herdr-green**](https://github.com/natori-hrj/herdr-green)<br><sub>natori-hrj</sub> | herdr 的按 Agent 显示测试状态——当某个 Agent 完成时运行该项目的测试，并显示通过/失败 | `ai-agents` `ci` `tests` `rust` | 0 | 2026-07-23 |
| [**🆕 agentic-box**](https://github.com/nicoRomeroCuruchet/agentic-box)<br><sub>nicoRomeroCuruchet</sub> | 一个由 Claude Code 驱动本地模型 Agent 的隔离沙盒 | `agent-orchestration` `agentic` `agentic-workflow` `docker` `ornith-1-0-35b` | 0 | 2026-08-17 |
| [**herdr-plugin-aos**](https://github.com/noctaIO/herdr-plugin-aos)<br><sub>noctaIO</sub> | 从任意工作区在 herdr 窗格中启动支持 Agentic OS 的 Claude Code Agent。无侵入式 herdr 插件 | `shell` | 0 | 2026-07-11 |
| [**🆕 herdr-zcode**](https://github.com/Nofuture123/herdr-zcode)<br><sub>Nofuture123</sub> | Herdr 中的 ZCode：提供 TUI 窗格与委托桥接（任意 CLI Agent -> 原生 ZCode 执行器）。 | `zcode` `python` | 0 | 🔄 2026-09-19 |
| [**🆕 herdr-prompts**](https://github.com/oppenheimor/herdr-prompts)<br><sub>oppenheimor</sub> | 在 Herdr 中跨编程 Agent 保存、搜索、填充和复用提示词模板。灵感来自我的朋友 bingguanqi | `typescript` | 0 | 2026-08-19 |
| [**🆕 herdr-guard**](https://github.com/pauljohnchamberlain/herdr-guard)<br><sub>pauljohnchamberlain</sub> | 让 Codex、Claude 等编码 Agent 能够安全地对 Herdr 进行外部控制。 | `coding-agents` `typescript` | 0 | 2026-09-04 |
| [**🆕 herdr-sidekick**](https://github.com/qapquiz/herdr-sidekick)<br><sub>qapquiz</sub> | 面向 Herdr 的可开关的「副驾」AI Agent 窗格——可将选中的代码粘贴到 Agent 的输入框中而不直接提交。可与 qapquiz/herdr-sidekick.nvim 搭配使用 | `neovim` `terminal` `shell` | 0 | 2026-08-15 |
| [**🆕 ocean-herdr**](https://github.com/Risingtides-dev/ocean-herdr)<br><sub>Risingtides-dev</sub> | 面向 Herdr 的 Ocean Agent 集成 | `coding-agent` `ocean` `rust` | 0 | 2026-07-17 |
| [**🆕 herdr-quick-prompt**](https://github.com/Taanviir/herdr-quick-prompt)<br><sub>Taanviir</sub> | Herdr plugin — press a key, pick a coding agent, type a prompt, and it launches in a new tab or split. | `coding-agents` `terminal` `tui` `javascript` | 0 | 🔄 2026-09-17 |
| [**🆕 herdr-ask**](https://github.com/TaylorFinklea/herdr-ask)<br><sub>TaylorFinklea</sub> | 面向 Herdr 及任意终端的轻量命令生成与终端聊天 | `cli` `rust` `terminal` `tui` | 0 | 2026-07-21 |
| [**herdr-group-chat**](https://github.com/terry-li-hm/herdr-group-chat)<br><sub>terry-li-hm</sub> | 面向 Pi、Claude Code、Codex 和 Grok Build 的共享本地 Herdr 聊天室 | `ai-agents` `claude-code` `codex` `grok` `multi-agent` | 0 | 🔄 2026-09-08 |
| [**🆕 herdr-agent-topic**](https://github.com/wynemo/herdr-agent-topic)<br><sub>wynemo</sub> | herdr 插件：在每张 Agent 卡片中显示你最近发送的用户提示词 | `go` | 0 | 2026-08-20 |

<details><summary>与此目的也相关</summary>

- [AltanS/collie](https://github.com/AltanS/collie) — 随时随地管理 herdr 的 PWA 应用。支持 Tailnet 访问、推送通知、快捷操作等
- [ZingerLittleBee/Heeler](https://github.com/ZingerLittleBee/Heeler) — 面向 herdr 的原生 iOS Agent 控制台——通过 SSH 查看并操控你机器上的编码 Agent，配备真正的 libghostty 终端、二维码配对，以及 Agent 需要你时的推送通知。
- [a2u/herdr-jira](https://github.com/a2u/herdr-jira) — herdr 的 Jira TUI 插件——通过可配置的 JQL 过滤器浏览、搜索 issue，修改状态，并一键将 issue 交给终端中运行的 AI Agent 处理
- [e2b-dev/herdr-e2b-sandbox](https://github.com/e2b-dev/herdr-e2b-sandbox) — 将 git 工作树镜像到 E2B Sandbox 的 herdr 插件——支持单个沙盒或每个 Agent 一条分支的沙盒集群，并配有 TUI 仪表盘
- [walcew/herdr-assist](https://github.com/walcew/herdr-assist) — 面向 AI 编程 Agent 终端复用器 Herdr 的实体桌面面板——用颜色显示会话状态，当 Agent 停下来请求决策时会响铃提醒。基于 ESP32-S3 + LVGL，提供预编译固件
- [miko-misa/herdr-portfwd](https://github.com/miko-misa/herdr-portfwd) — 面向远程机器上编程 Agent 的自动 SSH 端口转发——Ctrl+点击 Agent 打印的 localhost URL，即可在你本机以相同端口打开该页面。一个 Herdr 插件
- [spad-0x/herdr-mobile-pro](https://github.com/spad-0x/herdr-mobile-pro) — 一款高性能、移动优先的 PWA 仪表盘，采用 Cyber-Dark 设计风格，可直接从智能手机编排 Herdr 与自主 AI Agent。具备安全 HTTPS、语音听写输入、图片上传，以及将终端输出实时语义解析为聊天式…
- [virtualboard/herdr-virtualboard](https://github.com/virtualboard/herdr-virtualboard) — Kanban board for VirtualBoard feature specs inside Herdr: columns are the lifecycle, cards are specs, and dis…

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-worktree"></a>

## git 工作树与分支管理

> 想为每项工作单独开一个工作树，收尾清理也自动完成

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-worktrunk**](https://github.com/devashish2203/herdr-worktrunk)<br><sub>devashish2203</sub> | 集成 worktrunk 以管理 git 工作树的 Herdr 插件 | `shell` | 156 | 🔄 2026-09-08 |
| [**herdr-plugin-jj-workspace**](https://github.com/NathanFlurry/herdr-plugin-jj-workspace)<br><sub>NathanFlurry</sub> | 将 Jujutsu (jj) 工作区作为 Herdr 工作区进行创建和删除 | `jujutsu` `rust` | 48 | 2026-09-03 |
| [**herdr-plugin-renamer**](https://github.com/wyattjoh/herdr-plugin-renamer)<br><sub>wyattjoh</sub> | 根据 Agent 的第一条提示词，重命名自动生成的 herdr 工作树分支和工作区（通过设备端 Apple FoundationModels 或 Codex） | `rust` | 14 | 2026-08-17 |
| [**herdr-e2b-sandbox**](https://github.com/e2b-dev/herdr-e2b-sandbox)<br><sub>e2b-dev</sub> | 将 git 工作树镜像到 E2B Sandbox 的 herdr 插件——支持单个沙盒或每个 Agent 一条分支的沙盒集群，并配有 TUI 仪表盘 | `cli` `cloud-dev` `e2b` `git-worktree` `sandbox` | 12 | 🔄 2026-09-10 |
| [**jj-waltz**](https://github.com/EzraCerpac/jj-waltz)<br><sub>EzraCerpac</sub> | 受 Worktrunk 启发的 Jujutsu 工作区切换工具 | `cli` `jj` `jujitsu` `utility` `workspace` | 9 | 🔄 2026-09-20 |
| [**bercail**](https://github.com/simoncrypta/bercail)<br><sub>simoncrypta</sub> | 基于 Herdr 的 Agent 化开发环境。 | `agentic-coding` `agentic-development` `agentic-development-environment` `agentic-ide` `agentic-workflow` | 7 | 🔄 2026-09-10 |
| [**herdr-plugin-git-worktree-hooks**](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks)<br><sub>freethinkel</sub> | 在创建/移除 git 工作树时运行 shell 命令——一份 YAML 配置适用于所有项目，放在任何仓库之外 | `git-worktree` `javascript` | 6 | 2026-07-06 |
| [**herdr-symlink-worktree**](https://github.com/hmu332233/herdr-symlink-worktree)<br><sub>hmu332233</sub> | 将主仓库中的共享本地文件符号链接到新工作树中的 herdr 插件 | `shell` | 6 | 2026-07-16 |
| [**herdr-worktree-from-pr**](https://github.com/tdi/herdr-worktree-from-pr)<br><sub>tdi</sub> | 从 GitHub PR 创建 git 工作树，并作为 herdr 工作区打开 | `javascript` | 6 | 🔄 2026-09-11 |
| [**herdr-worktree-seed**](https://github.com/jlimas/herdr-worktree-seed)<br><sub>jlimas</sub> | 为新工作树植入 copy-on-write 的 node_modules 和可配置本地 dotfiles 的 Herdr 插件 | `developer-tools` `dotfiles` `git-worktree` `nodejs` `typescript` | 5 | 2026-07-28 |
| [**herdr-jj-status**](https://github.com/mroth/herdr-jj-status)<br><sub>mroth</sub> | herdr 插件：在空间侧边栏中显示 jj 工作区的 Jujutsu 书签/状态 | `shell` | 5 | 2026-07-28 |
| [**herdr-worktree-hooks**](https://github.com/timofey-TK/herdr-worktree-hooks)<br><sub>timofey-TK</sub> | herdr 插件：在创建、打开或删除 git 工作树时运行自定义的初始化/清理命令 | `developer-tools` `git-worktree` `worktree` `python` | 5 | 2026-07-17 |
| [**herdr-jj**](https://github.com/OliverGilan/herdr-jj)<br><sub>OliverGilan</sub> | 为 Herdr 添加 Jujutsu 工作区支持 | `jujutsu` `rust` | 4 | 2026-08-12 |
| [**herdr-fresh-worktree**](https://github.com/persiyanov/herdr-fresh-worktree)<br><sub>persiyanov</sub> | 将新创建的 herdr 工作树重置为 origin 默认分支的最新状态 | `javascript` | 4 | 2026-06-25 |
| [**herdr-worktreeinclude**](https://github.com/tanshio/herdr-worktreeinclude)<br><sub>tanshio</sub> | Herdr 插件：将匹配 .worktreeinclude 的被 gitignore 文件复制到新创建的工作树中 | `worktree` `worktreeiclude` `shell` | 4 | 2026-07-11 |
| [**herdr-remote-worktrunk**](https://github.com/ditwrd/herdr-remote-worktrunk)<br><sub>ditwrd</sub> | Herdr 的远程 worktrunk 工作区 | `shell` | 3 | 2026-07-10 |
| [**🆕 herdr-pi-tree**](https://github.com/edxeth/herdr-pi-tree)<br><sub>edxeth</sub> | 以树状结构展示你的 Pi Agent 的侧边栏——谁生成了谁、哪个 worktree 对应哪个分支、谁在等待你。 | `git-worktrees` `pi` `pi-coding-agent` `sidebar` `terminal` | 3 | 🔄 2026-09-18 |
| [**🆕 herdr-worktree-setup**](https://github.com/lamngockhuong/herdr-worktree-setup)<br><sub>lamngockhuong</sub> | 为每个新 worktree 做好准备的 Herdr 插件：自动检测配置文件、创建共享目录链接，并可选择性运行初始化命令。 | `dotenv` `git-worktree` `monorepo` `javascript` | 3 | 🔄 2026-09-20 |
| [**herdr-wish**](https://github.com/MovieHolic-Plex/herdr-wish)<br><sub>MovieHolic-Plex</sub> | Herdr 插件。许下一个愿望，omo 就会提交一个 PR。执行 omo-10 会打开 10 个 worktree。 | `omo` `wish` `javascript` | 3 | 2026-09-04 |
| [**herdr-branch-cleanup**](https://github.com/osolmaz/herdr-branch-cleanup)<br><sub>osolmaz</sub> | 当窗格所在分支在 GitHub 上被合并或删除后，自动切换到默认分支 | `git` `github` `rust` | 3 | 2026-07-26 |
| [**herdr-worktree-lifecycle**](https://github.com/qdentity/herdr-worktree-lifecycle)<br><sub>qdentity</sub> | Herdr 插件：将工作树生命周期事件分发给仓库自带的初始化/清理脚本 | `rust` | 3 | 2026-06-29 |
| [**herdr-worktree-nav**](https://github.com/ShoMasegi/herdr-worktree-nav)<br><sub>ShoMasegi</sub> | _(暂无描述)_ | `terminal` `rust` | 3 | 🔄 2026-09-20 |
| [**herdr-deck**](https://github.com/ctbaum/herdr-deck)<br><sub>ctbaum</sub> | herdr-agents.nvim 的搭配工作区启动器：在预先搭好的 Neovim、Agent、shell 和 lazygit 组合面板中打开或恢复 Claude 和 Codex | `claude-code` `codex` `coding-agents` `git-worktree` `neovim` | 2 | 🔄 2026-09-13 |
| [**trunkr**](https://github.com/disintegrator/trunkr)<br><sub>disintegrator</sub> | Herdr 🤝 Worktrunk——连接 Herdr 与 Worktrunk 的插件 | `go` | 2 | 2026-08-12 |
| [**herdr-tagr**](https://github.com/dvoets/herdr-tagr)<br><sub>dvoets</sub> | 为 herdr 打造的简洁、以图标为先的标签页标题：应用图标 + git 分支 + 文件夹。 | `rust` `terminal` | 2 | 🔄 2026-09-14 |
| [**herdr-worktreeinclude**](https://github.com/eightHundreds/herdr-worktreeinclude)<br><sub>eightHundreds</sub> | Herdr 插件：将 .worktreeinclude 指定的被 gitignore 文件复制到新工作树中 | `worktree` `rust` | 2 | 2026-07-28 |
| [**herdr-multirepo**](https://github.com/jattento/herdr-multirepo)<br><sub>jattento</sub> | 在一个 Herdr 工作区中管理跨多个仓库的同一条功能分支 | `git-worktree` `python` | 2 | 2026-08-03 |
| [**herdr-shear**](https://github.com/moneycaringcoder/herdr-shear)<br><sub>moneycaringcoder</sub> | 找出可以安全删除的 git 工作树并将其删除——一个面向 herdr 的工作树清洁工 | `cleanup` `git-worktree` `rust` `terminal` | 2 | 2026-09-01 |
| [**herdr-worktreeinclude**](https://github.com/serhii-chernenko/herdr-worktreeinclude)<br><sub>serhii-chernenko</sub> | 允许为新工作树指定自定义路径，并像 Claude CLI 一样遵循 `.worktreeinclude` 文件 | `worktree` `shell` | 2 | 2026-07-23 |
| [**herdr-corral**](https://github.com/bfreed/herdr-corral)<br><sub>bfreed</sub> | 在 Herdr 中集中管理 Git 工作树：env 文件、依赖、Agent/shell/服务器标签页，以及合并安全的清理。作为 Herdr 版的 workmux 替代品 | `git-worktree` `workmux` `python` | 1 | 2026-08-14 |
| [**🆕 herdr-keep-root**](https://github.com/bonkey/herdr-keep-root)<br><sub>bonkey</sub> | Herdr 插件：只要某个仓库的任意 worktree 工作区处于打开状态，就保持该仓库主检出工作区一直打开，从而避免 Spaces 面板中的 worktree 分组被拍平。 | `shell` | 1 | 🔄 2026-09-08 |
| [**herdr-worktree-copy**](https://github.com/crexi/herdr-worktree-copy)<br><sub>crexi</sub> | 根据 .worktree-copy 清单复制并符号链接工作树本地文件的 Herdr 插件 | `git-worktree` `shell` | 1 | 2026-07-28 |
| [**herdr-composer**](https://github.com/danieljvdm/herdr-composer)<br><sub>danieljvdm</sub> | 编排任务、附加上下文，并在隔离的 Herdr 工作区中启动编码 Agent。 | `coding-agents` `git-worktree` `rust` | 1 | 🔄 2026-09-15 |
| [**🆕 herdr-plugin-jj-workspace**](https://github.com/expnn/herdr-plugin-jj-workspace)<br><sub>expnn</sub> | A Herdr plugin to create and remove Jujutsu (jj) workspaces | `rust` | 1 | 🔄 2026-09-14 |
| [**herdr-allow**](https://github.com/Feasy01/herdr-allow)<br><sub>Feasy01</sub> | herdr 插件：通过 .herdr-allow 允许列表，将被 gitignore 的文件（.env、密钥、本地配置）复制到每个新工作树中 | `shell` | 1 | 2026-07-02 |
| [**🆕 nexus**](https://github.com/IniZio/nexus)<br><sub>IniZio</sub> | Herdr plugin for running worktree in Cloud-Hypervisor sandboxes, with mem/cpu/disk hotplug and auto port-forwarding | `cloud-hypervisor` `go` | 1 | 🔄 2026-09-20 |
| [**herdr-plugin-gwm**](https://github.com/kbrdn1/herdr-plugin-gwm)<br><sub>kbrdn1</sub> | 驱动 gwm 来管理 git 工作树的 herdr 插件——gwm 保持权威数据源，herdr 只是采纳它 | `bash` `cli` `git-worktree` `gwm` `worktree` | 1 | 2026-07-27 |
| [**🆕 herdr-plugin-cow-worktree**](https://github.com/khatriafaz/herdr-plugin-cow-worktree)<br><sub>khatriafaz</sub> | Herdr plugin for strict copy-on-write Git worktrees that include ignored local files | `typescript` | 1 | 🔄 2026-09-20 |
| [**herdr-collide**](https://github.com/moneycaringcoder/herdr-collide)<br><sub>moneycaringcoder</sub> | 当在同一仓库不同 git 工作树中工作的 Agent 即将发生冲突时发出警告——并判断它们的修改只是重叠还是会真正产生冲突 | `conflict-detection` `git-worktree` `rust` `terminal` | 1 | 2026-09-01 |
| [**herdr-standup**](https://github.com/moneycaringcoder/herdr-standup)<br><sub>moneycaringcoder</sub> | 总结你的 Agent 实际做了什么。一条命令即可获得指定时间段内所有 Herdr 工作区的可读摘要——提交、改动量、分支，以及工作是否落地 | `git` `rust` `standup` `terminal` | 1 | 2026-09-01 |
| [**herdr-pr-worktree**](https://github.com/poislagarde/herdr-pr-worktree)<br><sub>poislagarde</sub> | 将 GitHub 拉取请求作为 worktree 空间在 Herdr 中打开，并复用已有的检出。 | `git-worktree` `python` | 1 | 🔄 2026-09-18 |
| [**herdr-jira-worktree**](https://github.com/spiritsack/herdr-jira-worktree)<br><sub>spiritsack</sub> | herdr 插件：提示输入 Jira 工单，打开或复用对应的 git 工作树，并预填到全新的 Claude Code 会话中 | `shell` | 1 | 2026-08-24 |
| [**herdr-worktree-include**](https://github.com/tupton/herdr-worktree-include)<br><sub>tupton</sub> | 将未跟踪的文件以符号链接或复制的方式引入 herdr 创建的 git worktree。 | `shell` | 1 | 🔄 2026-09-14 |
| [**herdr-plugin-worktree-bootstrap**](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap)<br><sub>zerodice0</sub> | 在新的 Herdr Git 工作树中安全地复制被忽略的本地文件并运行初始化命令 | `python` | 1 | 2026-08-03 |
| [**herdr-plugin-pr-board**](https://github.com/0xthc/herdr-plugin-pr-board)<br><sub>0xthc</sub> | 在 herdr 中处理当前仓库的 GitHub PR——在窗格中浏览，将选中的 PR 检出为工作树工作区，并安全地回收已合并的 PR | `shell` | 0 | 2026-08-20 |
| [**🆕 herdr**](https://github.com/AgentTeamsRun/herdr)<br><sub>AgentTeamsRun</sub> | 将 herdr 工作树的生命周期事件上报给 AgentTeams 注册中心 | — | 0 | 2026-08-19 |
| [**🆕 herdr-title**](https://github.com/filoozom/herdr-title)<br><sub>filoozom</sub> | 在终端标签页标题中显示所选工作树和 Agent 活动状态的 Herdr 插件 | `rust` | 0 | 2026-07-24 |
| [**🆕 herdr-workspace-copy**](https://github.com/GODVvVZzz/herdr-workspace-copy)<br><sub>GODVvVZzz</sub> | Herdr plugin: copy a workspace folder to a sibling path and open it as a new workspace (no git worktree required). | `rust` `workspace` | 0 | 🔄 2026-09-20 |
| [**🆕 herdr-hub-worktrees**](https://github.com/klukacin/herdr-hub-worktrees)<br><sub>klukacin</sub> | herdr 插件：将 hub 工作树镜像到每个嵌套子仓库的克隆中 | `git-worktree` `monorepo` `terminal-multiplexer` `shell` | 0 | 2026-08-12 |
| [**🆕 herdr-worktree-bootstrap**](https://github.com/piesuke/herdr-worktree-bootstrap)<br><sub>piesuke</sub> | Bootstrap a new worktree: copy gitignored files, install deps, run hooks | `cli` `worktree` `worktree-workflow` `rust` | 0 | 🔄 2026-09-16 |
| [**🆕 herdr-worktree-include**](https://github.com/scoussens-nthplusio/herdr-worktree-include)<br><sub>scoussens-nthplusio</sub> | 使用仓库的 .worktreeinclude（与 Claude Code 使用的同一份文件、同一套规则），将 .env 等被 gitignore 忽略的文件复制到新的 Herdr 工作树中 | `dotenv` `git-worktree` `shell` | 0 | 2026-08-27 |
| [**herdr-worktree-guard**](https://github.com/takeaship/herdr-worktree-guard)<br><sub>takeaship</sub> | 专注安全性、用于追踪并清理 Agent 工作树的 Herdr 插件 | `coding-agents` `git-worktree` | 0 | 2026-08-30 |

<details><summary>与此目的也相关</summary>

- [tdi/herdr-worktree-from-linear](https://github.com/tdi/herdr-worktree-from-linear) — 从 Linear issue 创建 git 工作树，并作为 herdr 工作区打开
- [upstash/herdr-upstash-box](https://github.com/upstash/herdr-upstash-box) — Herdr 插件：从你正在查看的 worktree 中，在 Upstash Box 里运行编码 Agent。
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — 为 JavaScript 和 TypeScript 自动初始化 Herdr 工作树，支持基于锁文件的安装和安全的环境变量还原
- [tomasvarga/herdr-e2b](https://github.com/tomasvarga/herdr-e2b) — 按需将 git 工作树镜像到全新的 E2B 云沙盒——直接上传快照（包括未提交的更改），无需 push 或 clone。一个 herdr 插件
- [poislagarde/herdr-worktree-cleanup](https://github.com/poislagarde/herdr-worktree-cleanup) — 当对应的 Herdr 空间关闭时，自动清理可安全删除的 GitHub PR worktree。Python 编写，无依赖，MIT 许可。
- [zamarrowski/herdr-issues](https://github.com/zamarrowski/herdr-issues) — herdr plugin: browse the GitHub issues of the repo you're in and hand one to any coding agent (Claude Code, C…
- [logocode/herdr-linear-launcher](https://github.com/logocode/herdr-linear-launcher) — 从 Linear 工单出发，在后台 Herdr worktree 中启动 Codex 或 Claude。
- [snics/herdr-worktree-from-gitlab](https://github.com/snics/herdr-worktree-from-gitlab) — herdr 插件：从 GitLab issue（通过 glab）创建 git 工作树和工作区
- [untalfranfernandez/herdr-worktreeinclude](https://github.com/untalfranfernandez/herdr-worktreeinclude) — 为每个新建 git 工作树自动填充所需的、被 gitignore 忽略的本地文件（.env、settings.local.json、fixtures 等）的 Herdr 插件。只需在 .worktreeinclude…

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-review"></a>

## 代码审查与差异对比

> 想阅读 Agent 写的差异并对其发表评论

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**crabbox**](https://github.com/openclaw/crabbox)<br><sub>openclaw</sub> | Crabbox：预热沙盒、同步差异、运行测试套件 | `agent-skills` `remote-test-runner` `go` | 1408 | 🔄 2026-09-20 |
| [**herdr-reviewr**](https://github.com/persiyanov/herdr-reviewr)<br><sub>persiyanov</sub> | herdr 的代码审查 + 文件查看器侧边栏。可在差异上添加评论并发回给 Agent，还能查看差异、文件与 PR 状态。 | `code-review` `rust` `tui` | 732 | 🔄 2026-09-19 |
| [**herdr-annotate**](https://github.com/plannotator/herdr-annotate)<br><sub>plannotator</sub> | 在 Herdr 中为终端文本、文档和 Agent 回复添加注释并进行评审，并将反馈直接发回给 Agent | `annotation` `multiplexer` `rust` | 521 | 🔄 2026-09-10 |
| [**🆕 roamgate**](https://github.com/powerfooI/roamgate)<br><sub>powerfooI</sub> | A Herdr client for any screen. Control terminals, monitor coding agents, and review files and diffs from desktop or mobile. | `ai-agents` `bun` `code-review` `developer-tools` `git-worktree` | 222 | 🔄 2026-09-20 |
| [**herdr-hunk-diff**](https://github.com/jhochenbaum/herdr-hunk-diff)<br><sub>jhochenbaum</sub> | 从 herdr 在 Hunk 中审查 Agent 编写的更改，并将行内评论回传给对应的 Agent | `code-review` `hunk` `typescript` | 132 | 🔄 2026-09-16 |
| [**herdr-plannotator**](https://github.com/plannotator/herdr-plannotator)<br><sub>plannotator</sub> | 在 Herdr 的 Browser 窗格内打开 Plannotator 评审的插件 | `plannotator` `typescript` | 26 | 2026-07-29 |
| [**herdr-pickr**](https://github.com/tomasvarga/herdr-pickr)<br><sub>tomasvarga</sub> | herdr 的 PR 审查路由器——按住 Ctrl 点击 GitHub PR / GitLab MR 链接，选择审查工具（tuicr · hunk · diff · 浏览器 · 或自定义工具），可选启用 AI 初审 | `cli` `code-review` `pull-request` `tui` `shell` | 20 | 2026-07-13 |
| [**herdr-plugin-hunk**](https://github.com/edmundmiller/herdr-plugin-hunk)<br><sub>edmundmiller</sub> | 在分屏窗格或标签页中打开 Hunk 差异对比的 Herdr 插件 | `python` | 15 | 2026-06-23 |
| [**herdr-gitview**](https://github.com/ChmaraX/herdr-gitview)<br><sub>ChmaraX</sub> | herdr 的 Git 状态/差异面板——审查更改、在 nvim 中编辑、暂存/提交/丢弃，全部在终端内完成 | `git` `git-diff` `git-tui` `neovim` `rust` | 11 | 🔄 2026-09-06 |
| [**herdr-extensions**](https://github.com/vonzelle-vzt/herdr-extensions)<br><sub>vonzelle-vzt</sub> | 面向 herdr 的迷你 VS Code——具备 LSP 诊断、自动补全、重命名和跳转到定义的完整编辑器，外加源代码管理、搜索、问题面板、测试、调试器、应用实时预览、运行时错误捕获、图片粘贴和 Agent 差异审查。共 12 个面板，一条命令即可幂等且可逆地安装 | `agent-tools` `autocomplete` `claude-code` `cli` `code-review` | 6 | 2026-08-03 |
| [**herdr-plugin-hunk-autodiff**](https://github.com/scott306lr/herdr-plugin-hunk-autodiff)<br><sub>scott306lr</sub> | Herdr 插件：当编程 Agent 完成任务但留有未提交更改时，自动打开 hunk 差异分屏 | `claude-code` `hunk` `python` | 5 | 2026-07-05 |
| [**herdr-progressive-reviewer**](https://github.com/flupke/herdr-progressive-reviewer)<br><sub>flupke</sub> | 受 Tidewave 启发的回合制差异审查工具 | `rust` | 3 | 🔄 2026-09-16 |
| [**herdr-tasks**](https://github.com/husniadil/herdr-tasks)<br><sub>husniadil</sub> | 面向 Herdr 编程 Agent 的任务待办和笔记看板——带租约的 claim、有证据支撑的评审，以及人工决策关卡，全部由一个 Go 二进制程序实现 | `ai-agents` `mcp-server` `notes` `sqlite` `task-management` | 3 | 2026-08-30 |
| [**herdr-review.nvim**](https://github.com/inferst/herdr-review.nvim)<br><sub>inferst</sub> | 集成 Git 和 herdr 的 Neovim 代码审查 UI | `lua` | 3 | 2026-08-01 |
| [**herdr-review**](https://github.com/quantk/herdr-review)<br><sub>quantk</sub> | 在 Hunk 中审查 Agent 编写的更改，并通过 Herdr 回传行内反馈 | `code-review` `hunk` `javascript` | 3 | 2026-07-28 |
| [**easy-review**](https://github.com/VilfredSikker/easy-review)<br><sub>VilfredSikker</sub> | 面向 AI 辅助编程的 Git 差异审查，提供终端 TUI 和 Tauri 桌面应用两种形式 | `ai-code-review` `cli` `code-review` `desktop-app` `developer-tools` | 3 | 🔄 2026-09-19 |
| [**herdr-pr-tracker**](https://github.com/jakekroon/herdr-pr-tracker)<br><sub>jakekroon</sub> | 将你所创建的所有未关闭拉取请求以停靠面板形式展示，并按你需要处理的紧迫程度进行颜色标注。一个 Herdr 插件 | `bun` `code-review` `developer-tools` `github` `pull-requests` | 2 | 🔄 2026-09-16 |
| [**herdr-scribe**](https://github.com/Javamomma/herdr-scribe)<br><sub>Javamomma</sub> | herdr 插件：不录音的实时会议转录——将麦克风输入转为仅存于内存的文字记录和实时分析窗格；停止时生成会议纪要、可选策略关卡以及可审查的自动草稿。支持 Linux/WSL2 和 macOS | `macos` `meeting-notes` `privacy` `speech-to-text` `terminal` | 2 | 2026-08-07 |
| [**herdr-comments**](https://github.com/shadowfax92/herdr-comments)<br><sub>shadowfax92</sub> | 为复制的 Herdr 终端输出添加注释，按窗格收集评论，并可在 Neovim 中审查 | `ai-agents` `annotations` `neovim` `rust` `terminal` | 2 | 2026-08-19 |
| [**herdr-hunk**](https://github.com/yuucu/herdr-hunk)<br><sub>yuucu</sub> | herdr 插件：为你的 Agent 工作区切换 Hunk 差异审查 | `diff` `hunk` `go` | 2 | 2026-07-20 |
| [**herdr-strays**](https://github.com/aleslanger/herdr-strays)<br><sub>aleslanger</sub> | 用于整理散落 git 工作树的终端 UI——浏览项目、实时查看变更文件、阅读差异，并可在不离开面板的情况下向 Claude 发送提示词 | `rust` | 1 | 2026-08-12 |
| [**roboherd**](https://github.com/andschneider/roboherd)<br><sub>andschneider</sub> | 在 herdr 工作区中处理 roborev 的评审状态和操作 | `rust` `tui` | 1 | 🔄 2026-09-07 |
| [**herdr-agent-diff**](https://github.com/baotran01/herdr-agent-diff)<br><sub>baotran01</sub> | 用于查看 Agent 文件系统和 Git 差异的 Herdr 插件 | `rust` | 1 | 2026-08-03 |
| [**🆕 herdr-stagr**](https://github.com/brianh20/herdr-stagr)<br><sub>brianh20</sub> | 面向 herdr 的源代码管理侧边栏——通过并排差异对比进行暂存、取消暂存和放弃更改 | `git` `tui` `rust` | 1 | 2026-08-06 |
| [**Vincent**](https://github.com/chasereyn/Vincent)<br><sub>chasereyn</sub> | 一款以鼠标操作为主的终端客户端，用于审查 AI Agent 编写的代码，并可就地修改。 | `go` | 1 | 2026-09-03 |
| [**herdr-peer-review**](https://github.com/Elio2000/herdr-peer-review)<br><sub>Elio2000</sub> | 在 herdr 窗格中打开第二个编程 Agent 来审查你的差异——可观察、自动批准、只读。附带用于「审查↔修改↔决策」自主循环的 Claude Code skill | `agent-skills` `ai-agents` `claude-code` `code-review` `codex` | 1 | 2026-07-16 |
| [**herdr-git-graph**](https://github.com/jorge-huxley/herdr-git-graph)<br><sub>jorge-huxley</sub> | Herdr 的只读 git 图谱 TUI 插件，支持彩色 ASCII 分支线、分支过滤、搜索和按需查看差异 | `rust` | 1 | 2026-07-17 |
| [**agentflock**](https://github.com/neospark-sol/agentflock)<br><sub>neospark-sol</sub> | 由 AI 协调的构建者与评审者小组，配有持久化的里程碑管理 | `ai-agents` `pair-programming` `typescript` | 1 | 2026-08-21 |
| [**🆕 codey**](https://github.com/rodeyseijkens/codey)<br><sub>rodeyseijkens</sub> | 一个以代码审查为核心的 Git TUI（终端界面），提供分为「已暂存/变更」两个区域的差异查看器，支持临时评论与真实的 Git 暂存操作，基于 OpenTUI 构建。 | `code-review` `opentui` `review-tool` `tui` `typescript` | 1 | 🔄 2026-09-19 |
| [**herdr-git-graph**](https://github.com/sjlee06/herdr-git-graph)<br><sub>sjlee06</sub> | 为 Herdr 打造的交互式 Git 分支与提交图，基于 Rust + Ratatui 构建，具备平滑曲线、搜索与差异查看功能。 | `git` `git-graph` `ratatui` `rust` `terminal` | 1 | 🔄 2026-09-14 |
| [**herdr-hunk-viewer**](https://github.com/tareqmlx/herdr-hunk-viewer)<br><sub>tareqmlx</sub> | _(暂无描述)_ | `code-review` `hunk` `rust` | 1 | 2026-08-21 |
| [**herdr-lazygit-viewer**](https://github.com/tareqmlx/herdr-lazygit-viewer)<br><sub>tareqmlx</sub> | 在最适合当下场景的 Herdr 展示位置，以打开 files、branches、commits 或 stash 面板的状态启动 lazygit | `code-review` `lazygit` `rust` | 1 | 2026-08-14 |
| [**herdr-hunk**](https://github.com/cevr/herdr-hunk)<br><sub>cevr</sub> | 将 Hunk 的评审记录发送到对应的 Herdr Agent 窗格 | `effect-ts` `hunk` `typescript` | 0 | 2026-07-28 |
| [**🆕 herdr-review-panel**](https://github.com/Deetss/herdr-review-panel)<br><sub>Deetss</sub> | Herdr 插件：一个「审查队列」面板，展示由 Claude Code 标记出的、需要你查看的文件和需要亲自运行的命令。 | `claude-code` `ratatui` `rust` `tui` | 0 | 🔄 2026-09-16 |
| [**🆕 herdr-tuicr**](https://github.com/ekropotin/herdr-tuicr)<br><sub>ekropotin</sub> | tuicr code review in a Herdr pane, with automatic handoff to the agent that opened it. | `shell` | 0 | 🔄 2026-09-14 |
| [**herdr-hunk**](https://github.com/goofansu/herdr-hunk)<br><sub>goofansu</sub> | 提供快速的 Herdr 评审操作，打开一个临时的 Hunk 浮层。退出 Hunk 会关闭浮层并恢复你的工作区 | `python` | 0 | 🔄 2026-09-17 |
| [**🆕 herdr-implement-review**](https://github.com/Idan-Levin/herdr-implement-review)<br><sub>Idan-Levin</sub> | 用于 Codex 实现、安全扫描和「母 Agent」评审的 Herdr 工作流 | `claude-code` `codex` `security-review` `shell` | 0 | 2026-08-10 |
| [**🆕 herdr-plan-code-review**](https://github.com/inxx/herdr-plan-code-review)<br><sub>inxx</sub> | herdr 插件：Opus 做计划，Sonnet 写代码，Claude+Codex 做审查——一个操作打开四个 Agent 窗格 | `claude-code` `codex` `terminal` `shell` | 0 | 2026-07-06 |
| [**🆕 herdr-idle-panes**](https://github.com/leonho/herdr-idle-panes)<br><sub>leonho</sub> | herdr 插件：以清单弹窗形式查看并关闭停留在闲置 shell 的窗格 | `python` | 0 | 2026-08-22 |
| [**herdr-diff-review.nvim**](https://github.com/rytkmt/herdr-diff-review.nvim)<br><sub>rytkmt</sub> | 在应用之前，于 Neovim diff 模式中审查 AI Agent 的文件更改——用一条命令即可批准或拒绝来自 Claude Code 和 Kiro CLI 的编辑 | `kiro-cli` `neovim` `neovim-plugin` `neovim-plugins` `nvim` | 0 | 2026-08-18 |
| [**🆕 herdr-code-review**](https://github.com/txmed82/herdr-code-review)<br><sub>txmed82</sub> | 面向 Herdr 的结构化 AI 代码审查插件 | `code-review` `javascript` | 0 | 2026-08-19 |
| [**herdr-review-pack**](https://github.com/YmlyZA/herdr-review-pack)<br><sub>YmlyZA</sub> | 实验性 Herdr 插件：为人工审查整理任务简介、Git 差异，以及绑定快照的检查结果。 | `code-review` `developer-tools` `python` | 0 | 🔄 2026-09-09 |

<details><summary>与此目的也相关</summary>

- [JacquesvanWyk/herdr-hunk](https://github.com/JacquesvanWyk/herdr-hunk) — herdr 中用于 Hunk 差异对比的交互式 fzf 选择器：支持提交、范围、stash，并可在 Agent 完成时自动打开
- [anhnd3005-infinity/herdr-worker-orchestrator](https://github.com/anhnd3005-infinity/herdr-worker-orchestrator) — 通过 Herdr 管理的窗格，将任务派发给 CLI Agent worker（agy、codex 等）——支持有状态的任务追踪、工作树隔离和基于差异的评审。同时适用于 Claude Code 和 Herdr 的双用插件
- [tomasvarga/herdr-sniffr](https://github.com/tomasvarga/herdr-sniffr) — 在你审查之前，AI 先嗅探你的 PR 有没有问题——一个 Agent 化的初审，将草稿评论投放到 tuicr。不限定 Agent（codex/claude/cursor/grok/…）
- [elKei24/herdr-co-review](https://github.com/elKei24/herdr-co-review) — 在 herdr 中进行分屏 PR 评审——你的 Agent 找出问题，你在 TUI 中于代码旁逐一裁定，最后由 Agent 发布你批准的内容
- [itisbryan/herdr-gh-checks](https://github.com/itisbryan/herdr-gh-checks) — herdr 插件：在窗格中监视并查看当前 PR 的 CI，并在侧边栏行中显示 CI/合并状态。使用 Go + Bubble Tea 编写
- [mikhail-angelov/herdr-review-loop](https://github.com/mikhail-angelov/herdr-review-loop) — 在 herdr 工作区中让 Agent 之间自动进行交叉评审——一个负责编写，另一个负责评审，如此反复
- [moneycaringcoder/herdr-collide](https://github.com/moneycaringcoder/herdr-collide) — 当在同一仓库不同 git 工作树中工作的 Agent 即将发生冲突时发出警告——并判断它们的修改只是重叠还是会真正产生冲突
- [neospeed83/herdr-tournament](https://github.com/neospeed83/herdr-tournament) — 面向 Herdr 的对抗式多 Agent 代码评审

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-forge"></a>

## GitHub / issue 跟踪工具集成

> 想以 issue 或 PR 为起点开始工作，并追踪 PR 状态

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**ghzinga**](https://github.com/osolmaz/ghzinga)<br><sub>osolmaz</sub> | 用于查看单个 GitHub issue 或 PR 的简易可点击 TUI，用 Rust 编写 | `rust` | 87 | 🔄 2026-09-06 |
| [**🆕 tsk**](https://github.com/smarzban/tsk)<br><sub>smarzban</sub> | tsk, a Linear alternative that stays in the terminal: a shared task board for you and your agents. TUI for you, CLI for them. | `cli` `productivity` `rust` `task-manager` `terminal` | 69 | 🔄 2026-09-20 |
| [**herdr-plugin-gh-pr**](https://github.com/wyattjoh/herdr-plugin-gh-pr)<br><sub>wyattjoh</sub> | 在侧边栏显示当前聚焦 Agent 窗格所在分支的 GitHub PR 状态的 herdr 插件 | `typescript` | 22 | 2026-07-16 |
| [**herdr-plugin-github-start**](https://github.com/ogulcancelik/herdr-plugin-github-start)<br><sub>ogulcancelik</sub> | 从 GitHub issue、PR 或讨论中启动 Codex 或 Claude 的 Herdr 插件 | `javascript` | 17 | 2026-08-31 |
| [**herdr-worktree-from-linear**](https://github.com/tdi/herdr-worktree-from-linear)<br><sub>tdi</sub> | 从 Linear issue 创建 git 工作树，并作为 herdr 工作区打开 | `javascript` | 16 | 🔄 2026-09-11 |
| [**herdr-jira**](https://github.com/a2u/herdr-jira)<br><sub>a2u</sub> | herdr 的 Jira TUI 插件——通过可配置的 JQL 过滤器浏览、搜索 issue，修改状态，并一键将 issue 交给终端中运行的 AI Agent 处理 | `ai-agents` `jira` `ratatui` `rust` `tui` | 12 | 🔄 2026-09-05 |
| [**herdr-pr-tracker**](https://github.com/Matovidlo/herdr-pr-tracker)<br><sub>Matovidlo</sub> | herdr 插件：追踪每个 Claude Code 会话产生的 GitHub PR，附带 gh 状态和操作 | `claude-code` `shell` | 12 | 2026-08-12 |
| [**herdr-linear**](https://github.com/JacquesvanWyk/herdr-linear)<br><sub>JacquesvanWyk</sub> | 在 herdr 分屏窗格或标签页中运行的 fzf 驱动 Linear 面板：搜索 issue、深入项目、创建 issue、修改状态 | `shell` | 8 | 2026-07-12 |
| [**herdr-git-status**](https://github.com/krystof018/herdr-git-status)<br><sub>krystof018</sub> | 在 herdr 内呈现 CI 状态——同时支持 GitLab（流水线+合并请求）和 GitHub（Actions+拉取请求），根据仓库的 origin 自动识别 | `bash` `ci-cd` `ci-status` `developer-tools` `github-actions` | 6 | 🔄 2026-09-20 |
| [**herdr-pr-board**](https://github.com/cdowell09/herdr-pr-board)<br><sub>cdowell09</sub> | 面向 Herdr 的可配置跨仓库 GitHub 拉取请求仪表盘 | `github` `tui` `go` | 4 | 🔄 2026-09-10 |
| [**mergr**](https://github.com/jsmenzies/mergr)<br><sub>jsmenzies</sub> | 在 Herdr Space 侧边栏行中显示 GitHub 拉取请求状态 | `github-pull-requests` `rust` | 4 | 2026-07-30 |
| [**herdr-linear**](https://github.com/talent-factory/herdr-linear)<br><sub>talent-factory</sub> | 面向 Herdr 的 Linear issue 面板，按 Enter 即可开始实现 | `rust` | 4 | 🔄 2026-09-16 |
| [**herdr-sniffr**](https://github.com/tomasvarga/herdr-sniffr)<br><sub>tomasvarga</sub> | 在你审查之前，AI 先嗅探你的 PR 有没有问题——一个 Agent 化的初审，将草稿评论投放到 tuicr。不限定 Agent（codex/claude/cursor/grok/…） | `ai` `cli` `code-review` `pull-request` `tuicr` | 4 | 2026-07-14 |
| [**herdr-co-review**](https://github.com/elKei24/herdr-co-review)<br><sub>elKei24</sub> | 在 herdr 中进行分屏 PR 评审——你的 Agent 找出问题，你在 TUI 中于代码旁逐一裁定，最后由 Agent 发布你批准的内容 | `cli` `code-review` `pull-request` `rust` `tui` | 3 | 🔄 2026-09-16 |
| [**herdr-gh-checks**](https://github.com/itisbryan/herdr-gh-checks)<br><sub>itisbryan</sub> | herdr 插件：在窗格中监视并查看当前 PR 的 CI，并在侧边栏行中显示 CI/合并状态。使用 Go + Bubble Tea 编写 | `bubbletea` `ci` `github-actions` `tui` `go` | 3 | 2026-08-25 |
| [**herdr-plugin-gh-workflow**](https://github.com/kkckkc/herdr-plugin-gh-workflow)<br><sub>kkckkc</sub> | 用于 GitHub workflow 的 Herdr 插件 | `javascript` | 3 | 2026-07-03 |
| [**herdr-beads**](https://github.com/hexsprite/herdr-beads)<br><sub>hexsprite</sub> | 在 Herdr 中 Ctrl+点击 beads 的 issue ID，即可在分屏窗格中打开其详情 | `beads` `issue-tracker` `terminal` `shell` | 2 | 2026-08-07 |
| [**herdr-pr-watch**](https://github.com/maxguzenski/herdr-pr-watch)<br><sub>maxguzenski</sub> | Herdr 插件：在侧边栏显示每个工作区和 Agent 窗格对应的 GitHub PR 状态。 | `github-pull-requests` `python` | 2 | 🔄 2026-09-06 |
| [**herdr-plugin-jira-pr**](https://github.com/abtris/herdr-plugin-jira-pr)<br><sub>abtris</sub> | herdr 插件：显示当前分支 PR 背后关联的 Jira issue，并在两者不一致时发出警告 | `github-pr` `jira` `shell` | 1 | 2026-08-04 |
| [**herdr-workspace-prs**](https://github.com/andrewbrannan/herdr-workspace-prs)<br><sub>andrewbrannan</sub> | 用于追踪工作区 GitHub 拉取请求的 Herdr 插件。 | `typescript` | 1 | 2026-09-04 |
| [**herdr-board**](https://github.com/bredebjorhovd/herdr-board)<br><sub>bredebjorhovd</sub> | 编程 Agent 排队并自主完成工作的地方——输入 GitHub issue，自主 Agent 在 herdr 窗格中运行，PR 评审会返回给编写它的那个 Agent | `rust` | 1 | 2026-08-14 |
| [**herdr-dashboard**](https://github.com/chouxcreams/herdr-dashboard)<br><sub>chouxcreams</sub> | herdr 工作区的 PR 状态仪表盘 TUI——一目了然地查看每个窗格对应的 PR 状态/CI/审查情况 | `dashboard` `github` `pull-requests` `ratatui` `rust` | 1 | 2026-07-28 |
| [**herdr-plugin-dotfiles-github-link-preview**](https://github.com/edmundmiller/herdr-plugin-dotfiles-github-link-preview)<br><sub>edmundmiller</sub> | 在侧边窗格中预览 GitHub issue 和拉取请求的 Herdr 插件 | `python` | 1 | 2026-06-23 |
| [**herdr-spaces-pr-status**](https://github.com/jmarbutt/herdr-spaces-pr-status)<br><sub>jmarbutt</sub> | 在 herdr 空间中显示 GitHub 拉取请求状态，附带 Conductor 风格的 PR 看板 | `github-pull-request` `javascript` | 1 | 🔄 2026-09-09 |
| [**herdr-glab-status**](https://github.com/jpwallace22/herdr-glab-status)<br><sub>jpwallace22</sub> | 一个 [Herdr](https://herdr.dev) 插件，会在空间侧边栏的工作区行中以 $mr token 的形式显示每个工作区对应的 GitLab 合并请求状态。 | `typescript` | 1 | 🔄 2026-09-09 |
| [**🆕 herdr-revdiff**](https://github.com/mikhail-angelov/herdr-revdiff)<br><sub>mikhail-angelov</sub> | 面向 revdiff（https://github.com/umputun/revdiff）TUI 的 herdr 插件。 | `revdiff` `tui` `shell` | 1 | 🔄 2026-09-16 |
| [**worktender**](https://github.com/steig/worktender)<br><sub>steig</sub> | 一条命令，从 GitHub issue 直达在专属工作树中处理它的编程 Agent | `ai-agents` `claude-code` `coding-agents` `git-worktree` `golang` | 1 | 🔄 2026-09-16 |
| [**herdr-github-pr**](https://github.com/woshahua/herdr-github-pr)<br><sub>woshahua</sub> | 同步 GitHub PR 状态、检查、评审和评论的 Herdr 插件 | `github` `javascript` | 1 | 2026-08-21 |
| [**herdr-pr**](https://github.com/yelsed/herdr-pr)<br><sub>yelsed</sub> | 在 herdr 窗格中以待办事项形式显示等待你处理的拉取请求，全部通过 gh CLI 读取 | `rust` | 1 | 2026-08-29 |
| [**🆕 herdr-issues**](https://github.com/zamarrowski/herdr-issues)<br><sub>zamarrowski</sub> | herdr plugin: browse the GitHub issues of the repo you're in and hand one to any coding agent (Claude Code, Codex, Gemini…) in its own git worktree. | `coding-agents` `github-issues` `javascript` | 1 | 🔄 2026-09-19 |
| [**herdr-pr-status**](https://github.com/anthonykimm/herdr-pr-status)<br><sub>anthonykimm</sub> | 在侧边栏的每个工作区行中，以彩色图标显示 GitHub PR 编号、审查状态与 CI 状态。 | `python` | 0 | 🔄 2026-09-10 |
| [**🆕 herdr-pr-glance**](https://github.com/cupsadarius/herdr-pr-glance)<br><sub>cupsadarius</sub> | Herdr 插件：一目了然地查看当前分支的拉取请求、CI 检查、审查情况与提交栈。 | `bubbletea` `github` `go` `pull-requests` | 0 | 🔄 2026-09-08 |
| [**🆕 herdr-git-tab**](https://github.com/hamzahraihan/herdr-git-tab)<br><sub>hamzahraihan</sub> | Herdr 标签页插件：在一个视图中以六个窗格展示 GitHub TUI。 | `typescript` | 0 | 🔄 2026-09-09 |
| [**🆕 herdr-jira-peek**](https://github.com/hilmimuktitama/herdr-jira-peek)<br><sub>hilmimuktitama</sub> | 在当前 Herdr 窗格中，以只读方式预览 Jira Cloud 内容。 | `jira` `terminal` `shell` | 0 | 🔄 2026-09-19 |
| [**🆕 herdr-plugins**](https://github.com/JJLiebig/herdr-plugins)<br><sub>JJLiebig</sub> | Herdr plugin that starts Codex or Claude from a GitHub issue, PR, or discussion | `javascript` | 0 | 🔄 2026-09-20 |
| [**herdr-pr-preview**](https://github.com/juninaba/herdr-pr-preview)<br><sub>juninaba</sub> | 在分屏窗格中预览当前分支的 GitHub 拉取请求的 Herdr 插件 | `shell` | 0 | 2026-07-08 |
| [**herdr-plugin-github-status**](https://github.com/jwanga/herdr-plugin-github-status)<br><sub>jwanga</sub> | herdr 插件：以侧边栏宽度停靠在右侧，实时展示 GitHub 项目状态（里程碑、issue、PR、Actions）。 | `github` `rust` `tui` | 0 | 🔄 2026-09-19 |
| [**🆕 herdr-linear-launcher**](https://github.com/logocode/herdr-linear-launcher)<br><sub>logocode</sub> | 从 Linear 工单出发，在后台 Herdr worktree 中启动 Codex 或 Claude。 | `javascript` | 0 | 🔄 2026-09-17 |
| [**github-issue-herdr-plugin**](https://github.com/nyanyaon/github-issue-herdr-plugin)<br><sub>nyanyaon</sub> | 用于「牧养」GitHub issue 的 Claude Code 插件 | `rust` | 0 | 2026-07-27 |
| [**herdr-gh-issue-label**](https://github.com/polidog/herdr-gh-issue-label)<br><sub>polidog</sub> | 在 Herdr 的 space 中显示与分支对应的 GitHub issue 编号和标题的插件 | `github-issues` `shell` | 0 | 2026-08-28 |
| [**🆕 herdr-worktree-from-gitlab**](https://github.com/snics/herdr-worktree-from-gitlab)<br><sub>snics</sub> | herdr 插件：从 GitLab issue（通过 glab）创建 git 工作树和工作区 | `gitlab` `rust` `worktree` | 0 | 2026-07-09 |
| [**🆕 herdr-pr-workflow**](https://github.com/tamdogood/herdr-pr-workflow)<br><sub>tamdogood</sub> | 促使聚焦中的 Agent 安全地创建或合并当前分支拉取请求的 Herdr 操作 | `javascript` | 0 | 2026-08-10 |

<details><summary>与此目的也相关</summary>

- [tomasvarga/herdr-pickr](https://github.com/tomasvarga/herdr-pickr) — herdr 的 PR 审查路由器——按住 Ctrl 点击 GitHub PR / GitLab MR 链接，选择审查工具（tuicr · hunk · diff · 浏览器 · 或自定义工具），可选启用 AI 初审
- [tdi/herdr-worktree-from-pr](https://github.com/tdi/herdr-worktree-from-pr) — 从 GitHub PR 创建 git 工作树，并作为 herdr 工作区打开
- [jakekroon/herdr-pr-tracker](https://github.com/jakekroon/herdr-pr-tracker) — 将你所创建的所有未关闭拉取请求以停靠面板形式展示，并按你需要处理的紧迫程度进行颜色标注。一个 Herdr 插件
- [kiitosu/herdr-jira-board](https://github.com/kiitosu/herdr-jira-board) — 在 herdr 中运行的 Jira 看板，附带 Claude Code 会话启动器
- [poislagarde/herdr-pr-worktree](https://github.com/poislagarde/herdr-pr-worktree) — 将 GitHub 拉取请求作为 worktree 空间在 Herdr 中打开，并复用已有的检出。
- [poislagarde/herdr-worktree-cleanup](https://github.com/poislagarde/herdr-worktree-cleanup) — 当对应的 Herdr 空间关闭时，自动清理可安全删除的 GitHub PR worktree。Python 编写，无依赖，MIT 许可。
- [spiritsack/herdr-jira-worktree](https://github.com/spiritsack/herdr-jira-worktree) — herdr 插件：提示输入 Jira 工单，打开或复用对应的 git 工作树，并预填到全新的 Claude Code 会话中
- [ukwhatn/taskherd](https://github.com/ukwhatn/taskherd) — 与 herdr Agent 会话、PR 和 Jira 工单相关联的任务看板
- [0xthc/herdr-plugin-pr-board](https://github.com/0xthc/herdr-plugin-pr-board) — 在 herdr 中处理当前仓库的 GitHub PR——在窗格中浏览，将选中的 PR 检出为工作树工作区，并安全地回收已合并的 PR

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-layout"></a>

## 工作区与布局搭建

> 打开项目时，希望标签页、窗格和启动命令一次性就位

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-spreader**](https://github.com/yuk1ty/herdr-spreader)<br><sub>yuk1ty</sub> | 从一个 YAML 文件启动整套 herdr 工作区布局——标签页、窗格、命令，一次搞定 | `rust` | 122 | 2026-08-16 |
| [**dotfiles**](https://github.com/lararosekelley/dotfiles)<br><sub>lararosekelley</sub> | 面向 Bash shell 使用而准备的个人 dotfiles | `bash` `bootstrap` `dotfiles` `homebrew` `macos` | 51 | 🔄 2026-09-19 |
| [**herdr-plugin-workspace-manager**](https://github.com/razajamil/herdr-plugin-workspace-manager)<br><sub>razajamil</sub> | 声明式的标签页/窗格布局，创建工作树时自动应用每个工作区的默认设置 | `rust` | 41 | 2026-08-23 |
| [**seshagy**](https://github.com/lmilojevicc/seshagy)<br><sub>lmilojevicc</sub> | 面向 tmux 和 herdr 的 Agent 感知会话管理器——发现项目、启动会话、追踪 AI Agent 的工作 | `bubbletea` `go` `session-management` `session-manager` `terminal` | 20 | 🔄 2026-09-10 |
| [**herdr-grid**](https://github.com/thuanlm215/herdr-grid)<br><sub>thuanlm215</sub> | Herdr 的可视化窗格布局编辑器，支持拖放操作、新建 shell、可复用布局，以及跨标签页和工作区发送窗格。 | `layout-presets` `pane-layout` `productivity` `ratatui` `rust` | 10 | 🔄 2026-09-12 |
| [**herdr-sidebar-config**](https://github.com/testy-cool/herdr-sidebar-config)<br><sub>testy-cool</sub> | 面向 Herdr 的工作区 → 标签页 → Agent 侧边栏预设，将单标签分组显示得更紧凑，配有易读的任务标签和服务商图标。 | `ai-agents` `claude-code` `codex` `configuration` `ghostty` | 9 | 🔄 2026-09-16 |
| [**herdr-warp**](https://github.com/HexSleeves/herdr-warp)<br><sub>HexSleeves</sub> | 将 Herdr 工作区作为原生 Warp 窗格打开 | `shell` | 5 | 2026-07-25 |
| [**🆕 glyph**](https://github.com/fru-dev3/glyph)<br><sub>fru-dev3</sub> | One identity for every coding agent you run. Marks each Claude Code, Antigravity, Codex or Gemini session with your label, the project, the machine and the mom… | `ai-agents` `claude-code` `cli` `codex` `developer-tools` | 4 | 🔄 2026-09-19 |
| [**herdr-pane-layouts**](https://github.com/iurysza/herdr-pane-layouts)<br><sub>iurysza</sub> | 面向 Herdr 的无缝 tmux 风格窗格调整大小和布局 | `pane-layout` `python` `terminal` | 4 | 🔄 2026-09-14 |
| [**herdr-muster**](https://github.com/marcoskichel/herdr-muster)<br><sub>marcoskichel</sub> | 面向 herdr 的、感知 Agent 状态的项目切换器 | `rust` | 4 | 2026-07-03 |
| [**herdr-layout-tools**](https://github.com/edouard-andrei/herdr-layout-tools)<br><sub>edouard-andrei</sub> | herdr 插件：原地重塑布局（主窗格居左+网格）并均分——标签页 ID 和窗格 ID 保持不变，进程也得以保留 | `javascript` | 3 | 2026-08-06 |
| [**herdr-compose**](https://github.com/ropali/herdr-compose)<br><sub>ropali</sub> | herdr-compose 是面向 Herdr 的声明式工作区布局管理器 | `layout-manager` `python` | 3 | 2026-07-25 |
| [**herdr-setup-bootstrap**](https://github.com/shizlie/herdr-setup-bootstrap)<br><sub>shizlie</sub> | 根据 worktree_init.toml 初始化新工作树的 Herdr 插件 | `shell` | 3 | 2026-06-17 |
| [**herdr-google-gmail**](https://github.com/Tomatio13/herdr-google-gmail)<br><sub>Tomatio13</sub> | herdr-google-gmail 是面向终端工作区工具 herdr 的 Gmail 集成插件 | `shell` | 3 | 2026-07-22 |
| [**herdr-session-manager**](https://github.com/umutciloglu/herdr-session-manager)<br><sub>umutciloglu</sub> | 面向 herdr 的 Agent 会话管理器，支持跨 harness 消息传递。 | `rust` | 3 | 🔄 2026-09-18 |
| [**herdr-clone-layout**](https://github.com/danilolucasmd/herdr-clone-layout)<br><sub>danilolucasmd</sub> | 将你当前的工作区布局克隆到每个新的 herdr 工作树。无需模板、无需配置——你当前所在的布局本身就是模板 | `shell` | 2 | 2026-08-27 |
| [**herdr-fork-from-message**](https://github.com/dmangla3/herdr-fork-from-message)<br><sub>dmangla3</sub> | 从更早的一条消息处分叉出 Codex 或 Claude Code，并在新的 Herdr 标签页、窗格或工作区中打开 | `claude-code` `codex` `developer-tools` `terminal-multiplexer` `python` | 2 | 2026-08-10 |
| [**herdr-better-workspace**](https://github.com/hamzahraihan/herdr-better-workspace)<br><sub>hamzahraihan</sub> | 面向 herdr（AI 编码 Agent 的终端工作区管理器）的交互式「打开工作区」选择器插件。 | `go` | 2 | 🔄 2026-09-09 |
| [**dsh-plugin-herdr**](https://github.com/sunny0826/dsh-plugin-herdr)<br><sub>sunny0826</sub> | 面向 DeepSeek Harness（DSH）的 Herdr 控制平面插件——从 DSH 会话中观察并驱动 Herdr（面向 AI 编程 Agent 的终端工作区管理器） | `dsh-plugin` `typescript` | 2 | 2026-08-25 |
| [**herdr-google-calendar**](https://github.com/Tomatio13/herdr-google-calendar)<br><sub>Tomatio13</sub> | herdr-gog-calendar 是面向终端工作区工具 herdr 的 Google 日历集成插件 | `shell` | 2 | 2026-07-22 |
| [**reasonix-herdr**](https://github.com/uuie/reasonix-herdr)<br><sub>uuie</sub> | 在 Herdr 内提供实时生命周期报告和工作区控制的原生 Reasonix 插件 | `reasonix` `python` | 2 | 2026-07-10 |
| [**🆕 herdr-workspace**](https://github.com/zackshen/herdr-workspace)<br><sub>zackshen</sub> | herdr 插件：从居中弹窗创建工作区并应用布局配置 | `rust` | 2 | 2026-08-24 |
| [**herdr-layout**](https://github.com/3mmdrew/herdr-layout)<br><sub>3mmdrew</sub> | 面向 herdr 的极简工作区布局——输入一个 Lua 文件即可得到工作区。无依赖、无守护进程、无 YAML | `lua` `terminal` | 1 | 2026-08-04 |
| [**herdr-dwm-layout**](https://github.com/42lizard/herdr-dwm-layout)<br><sub>42lizard</sub> | 面向 Herdr 的 DWM 风格 master/stack 布局 | `dwm` `fzf` `rust` `shell` `tiling` | 1 | 2026-08-28 |
| [**🆕 herdr-scm**](https://github.com/dkbo/herdr-scm)<br><sub>dkbo</sub> | herdr 插件：为当前 herdr 工作区提供只读的多仓库源代码管理概览面板。 | `git` `rust` `terminal` `tui` | 1 | 🔄 2026-09-10 |
| [**herdr-medieval**](https://github.com/gabrielbarretoo/herdr-medieval)<br><sub>gabrielbarretoo</sub> | 将工作区和 Agent 以六边形中世纪大陆的形式进行 3D 展示的 Herdr 插件——每个工作区是一座围栏营地，每个窗格是一名冒险者，会根据 Agent 状态训练、在营火旁休息或在塔楼站岗。内嵌 three.js，无需联网、无依赖 | `3d` `hex-grid` `threejs` `javascript` | 1 | 2026-08-06 |
| [**herdr-opendde-harness**](https://github.com/mrzzmrzz/herdr-opendde-harness)<br><sub>mrzzmrzz</sub> | 面向 ddeharness 的 Herdr 侧边栏集成：在默认布局中提供原生状态、动态 Agent 名称与摘要，并支持远程客户端。 | `python` | 1 | 🔄 2026-09-10 |
| [**🆕 herdr-lastfocus**](https://github.com/pedrobarco/herdr-lastfocus)<br><sub>pedrobarco</sub> | herdr 的 tmux 风格「上一个活跃」窗格/标签页/工作区切换——通过聚焦事件历史守护进程实现 | `terminal-multiplexer` `tmux` `go` | 1 | 2026-07-25 |
| [**herdr-spinup**](https://github.com/Royal-lobster/herdr-spinup)<br><sub>Royal-lobster</sub> | 每个新建 herdr 标签页的启动界面——选择一个工具，即会在该标签页中运行。工具通过 JSON 定义 | `javascript` | 1 | 2026-08-04 |
| [**🆕 herdr-plugins**](https://github.com/VladPatr96/herdr-plugins)<br><sub>VladPatr96</sub> | Plugins for Herdr, the terminal workspace manager for AI coding agents | `javascript` | 1 | 🔄 2026-09-20 |
| [**herdr-sesh**](https://github.com/xheisenbugx/herdr-sesh)<br><sub>xheisenbugx</sub> | 受 sesh 启发的智能 herdr 工作区管理器 | `go` | 1 | 🔄 2026-09-09 |
| [**🆕 herdr-ipc**](https://github.com/adihex/herdr-ipc)<br><sub>adihex</sub> | Herdr plugin + Agent Plugin: workspace-scoped Unix-socket IPC for pane workers | `ipc` `python` | 0 | 🔄 2026-09-20 |
| [**🆕 herdr-better-worktrees**](https://github.com/bearylabs/herdr-better-worktrees)<br><sub>bearylabs</sub> | A fast Herdr popup for managing Git worktrees in a predictable embedded-bare layout: create, clone, open, inspect, fetch, and safely remove worktrees while kee… | `typescript` | 0 | 🔄 2026-09-18 |
| [**herdr-yoke**](https://github.com/dgnsrekt/herdr-yoke)<br><sub>dgnsrekt</sub> | get yoked——一键将两个标签页并排显示，herdr 版的 Chrome 分屏视图 | `split-view` `terminal` `shell` | 0 | 2026-08-09 |
| [**🆕 herdr-plugin-dotfiles-dev-layout**](https://github.com/edmundmiller/herdr-plugin-dotfiles-dev-layout)<br><sub>edmundmiller</sub> | 用于打开我的 dotfiles 开发工作区布局的 Herdr 插件 | `python` | 0 | 2026-06-23 |
| [**🆕 herdr-plugin-workspace-groups**](https://github.com/kwanwooi25/herdr-plugin-workspace-groups)<br><sub>kwanwooi25</sub> | Keyboard-first workspace grouping and colored sidebar badges for Herdr | `python` `terminal` `workspace-manager` | 0 | 🔄 2026-09-20 |
| [**🆕 herdr-menu**](https://github.com/leonardoacosta/herdr-menu)<br><sub>leonardoacosta</sub> | Pane, tab, and workspace management actions for Herdr | `menu` `pane` `tab` `workspace` `shell` | 0 | 🔄 2026-09-16 |
| [**🆕 herdr-pane-id-metadata**](https://github.com/limars874/herdr-pane-id-metadata)<br><sub>limars874</sub> | 用于规范化窗格 ID 和精简标签页/窗格侧边栏元数据的最小化 Herdr 插件 | `coding-agents` `terminal` `javascript` | 0 | 2026-08-17 |
| [**herdr-active-agent-jump**](https://github.com/shoaibkhanz/herdr-active-agent-jump)<br><sub>shoaibkhanz</sub> | herdr 插件：按布局顺序前后循环聚焦正在进行中（工作中/被阻塞）的 Agent——作为 attention-jump 的 vim 风格补充 | `javascript` | 0 | 2026-07-12 |
| [**🆕 herdr-plugin-move**](https://github.com/wyattjoh/herdr-plugin-move)<br><sub>wyattjoh</sub> | Move the focused Herdr pane to another workspace and tab | `bun` `terminal` `tui` `typescript` | 0 | 🔄 2026-09-15 |

<details><summary>与此目的也相关</summary>

- [andrewchng/herdr-sessionizer](https://github.com/andrewchng/herdr-sessionizer) — 通过模糊搜索打开项目和工作树，再从声明式 TOML 布局（标签页、窗格分割、命令、按仓库覆盖配置）启动工作区
- [fullerzz/herdr-plugin-sesh](https://github.com/fullerzz/herdr-plugin-sesh) — 面向 Herdr 的 Sesh 风格工作区选择器 TUI，集成 zoxide，可从常用目录创建工作区
- [ntindle/herdr-resurrect](https://github.com/ntindle/herdr-resurrect) — herdr 的 tmux-resurrect——快照工作区、标签页、窗格、当前目录、运行中的程序和 Agent，并在崩溃或重启后恢复
- [enekos/herdr-quick-actions](https://github.com/enekos/herdr-quick-actions) — 以 fzf 选择器调用 herdr 原生的标签页/窗格/工作区操作，按使用频率排序——不必再死记快捷键
- [salkhalil/herdr-sessionizer](https://github.com/salkhalil/herdr-sessionizer) — herdr 的 tmux-sessionizer：用 fzf 搜索已打开的工作区和 zoxide 目录，创建或聚焦并附带模板标签页
- [crierr/herdr-arrange](https://github.com/crierr/herdr-arrange) — 用于 herdr 窗格移动/交换/重新分屏/布局调整的交互式弹窗 UI
- [aliou/herdr-cast](https://github.com/aliou/herdr-cast) — 个人 Herdr 插件——提供原生 macOS Agent 通知、模糊工作区导航、基于 zoxide 的工作区创建以及布局命令
- [chandrasekharan98/herdr-workspace-save](https://github.com/chandrasekharan98/herdr-workspace-save) — 保存 Herdr 工作区（布局、工作目录、Agent 会话、正在运行的命令），之后可从 fzf 选择器中重新打开
- [42lizard/herdr-sessionizer](https://github.com/42lizard/herdr-sessionizer) — tmux-sessionizer 风格的 herdr 插件

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-navigate"></a>

## 窗格导航与快捷键

> 想用和编辑器一样的快捷键在窗格、工作区之间移动和调整大小

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**vim-herdr-navigation**](https://github.com/paulbkim-dev/vim-herdr-navigation)<br><sub>paulbkim-dev</sub> | 用 Ctrl+h/j/k/l 在 herdr 窗格与 Vim/Neovim 分屏之间无缝导航——vim-tmux-navigator 的 herdr 移植版 | `neovim` `vim` `shell` | 108 | 2026-08-23 |
| [**herdr-splits.nvim**](https://github.com/lmilojevicc/herdr-splits.nvim)<br><sub>lmilojevicc</sub> | 面向 Herdr 和 Neovim 的智能分屏导航与调整大小 | `lua` `neovim` `neovim-plugin` `neovim-plugins` `nvim` | 63 | 2026-08-17 |
| [**herdr-floax**](https://github.com/Tyru5/herdr-floax)<br><sub>Tyru5</sub> | herdr 的浮动临时终端——类似 tmux-floax 风格的可切换弹窗，每个工作区一个，会话持久保存 | `rust` `terminal` `tmux-floax` | 26 | 2026-07-26 |
| [**herdr-nvim-nav**](https://github.com/aimdevlee/herdr-nvim-nav)<br><sub>aimdevlee</sub> | 在 herdr 窗格与 Neovim 分屏之间无缝使用 Ctrl+h/j/k/l——基于 socket，无需每次按键都启动进程 | `neovim` `neovim-plugin` `lua` | 18 | 2026-08-02 |
| [**herdr-last-workspace**](https://github.com/third774/herdr-last-workspace)<br><sub>third774</sub> | 用于切换回上一个聚焦的工作区的插件 | `rust` | 18 | 2026-06-22 |
| [**herdr-recent-navigator**](https://github.com/beyondlex/herdr-recent-navigator)<br><sub>beyondlex</sub> | 在最近使用的工作区、标签页、窗格和 Agent 之间进行 MRU（最近使用）切换——类似 JetBrains 的「最近文件」。此外还支持对任意窗格内容进行模糊搜索，完全由键盘驱动。 | `agent` `mru` `navigator` `pane` `popup` | 16 | 🔄 2026-09-12 |
| [**herdr-cliamp**](https://github.com/coryshaw1/herdr-cliamp)<br><sub>coryshaw1</sub> | 面向 herdr 的浮动 cliamp，隐藏后仍会继续播放——播放器运行在一个分离的 herdr 会话中，因此关闭浮层只是分离而已 | `audiobook` `cliamp` `music-player` `podcast` `terminal` | 12 | 2026-08-24 |
| [**herdr-logbook**](https://github.com/Resetnak/herdr-logbook)<br><sub>Resetnak</sub> | 终端的工作记忆——离线、以 Markdown 为主的笔记、决策记录，以及 Herdr 的当前任务 now.md | `adr` `bubbletea` `cli` `go` `markdown` | 12 | 2026-09-03 |
| [**herdr-command-center**](https://github.com/speardragon/herdr-command-center)<br><sub>speardragon</sub> | 一个快捷键统管所有命令——一个列出你注册命令的 herdr 弹窗，用方向键或数字执行，并在命令触发前自动关闭 | `command-palette` `nodejs` `terminal` `toml` `tui` | 12 | 2026-08-19 |
| [**herdr-pane-mover**](https://github.com/osamahbeig/herdr-pane-mover)<br><sub>osamahbeig</sub> | herdr 的可点击浮层菜单：跨标签页和工作区移动、重新分割或交换窗格 | `terminal` `tui` `javascript` | 11 | 2026-07-10 |
| [**herdr-equalize-panes**](https://github.com/shibayu36/herdr-equalize-panes)<br><sub>shibayu36</sub> | 在分屏和关闭时自动均分窗格大小的 herdr 插件（相当于自动执行 tmux 的 select-layout -E） | `terminal` `perl` | 11 | 2026-08-22 |
| [**🆕 herdr-profiles**](https://github.com/GiorgiTarsaidze/herdr-profiles)<br><sub>GiorgiTarsaidze</sub> | 面向 Herdr 的 Chrome 风格配置文件：通过弹窗选择器切换相互隔离的空间集合。 | `rust` `terminal` | 9 | 🔄 2026-09-14 |
| [**herdr-paddock**](https://github.com/neyham/herdr-paddock)<br><sub>neyham</sub> | 🐑 面向 herdr Agent 的卡片墙动态流——一览整个羊群，放大查看单个 Agent 并回复，全部通过普通 SSH 完成 | `bubbletea` `go` `ssh` `tui` | 9 | 2026-08-25 |
| [**herdr-trail**](https://github.com/catoncat/herdr-trail)<br><sub>catoncat</sub> | herdr 全局共享的备忘录——Agent 记下待跟进事项，人类通过一份全局列表统一管理，每条记录都可跳回其来源对话 | `javascript` | 8 | 2026-08-26 |
| [**herdr-toggle-popup**](https://github.com/maro114510/herdr-toggle-popup)<br><sub>maro114510</sub> | 一个快捷键即可切换浮层弹窗终端的 Herdr 插件 | `go` | 8 | 🔄 2026-09-18 |
| [**nvim-herdr-navigation**](https://github.com/bojackduy/nvim-herdr-navigation)<br><sub>bojackduy</sub> | vim-tmux-navigator 风格的 ctrl+h/j/k/l，在 Neovim 分屏和 Herdr 窗格之间导航 | `keyboard-shortcuts` `lazyvim` `lua` `navigation` `neovim` | 6 | 2026-07-20 |
| [**herdr-omnisearch**](https://github.com/dmnkf/herdr-omnisearch)<br><sub>dmnkf</sub> | 为 Herdr 工作区、窗格和已归档 Agent 会话提供快速本地搜索与导航 | `python` | 6 | 2026-08-31 |
| [**herdr-swipe**](https://github.com/husniadil/herdr-swipe)<br><sub>husniadil</sub> | 面向 Herdr 的触控板手势——可在窗格、标签页和空间之间移动，并跳转到正在等待你的 Agent | `cgeventtap` `gestures` `macos` `python` `terminal` | 6 | 2026-08-20 |
| [**herdr-last**](https://github.com/lmilojevicc/herdr-last)<br><sub>lmilojevicc</sub> | 切换回 Herdr 中上一个活动的工作区或标签页 | `go` `linux` `macos` `productivity` `tabs` | 6 | 2026-08-07 |
| [**herdr-scratch**](https://github.com/AkashJana18/herdr-scratch)<br><sub>AkashJana18</sub> | 面向 Herdr 的持久化速记板，为浮动实用窗格铺路 | `cli` `rust` `scratchpad` | 5 | 🔄 2026-09-20 |
| [**herdr-arrange**](https://github.com/crierr/herdr-arrange)<br><sub>crierr</sub> | 用于 herdr 窗格移动/交换/重新分屏/布局调整的交互式弹窗 UI | `go` | 5 | 2026-09-05 |
| [**nvim-herdr-navigator**](https://github.com/kaar/nvim-herdr-navigator)<br><sub>kaar</sub> | 在 Neovim 分屏与 herdr 窗格之间无缝导航——一套 `ctrl+h/j/k/l` 按键即可同时穿梭于 vim 和 herdr 窗格 | `neovim` `neovim-plugin` `lua` | 5 | 2026-07-29 |
| [**herdr-attention**](https://github.com/milkyskies/herdr-attention)<br><sub>milkyskies</sub> | herdr 插件：按一个键即可跳转到下一个需要关注的 Agent（先是被阻塞的，然后是已完成的） | `javascript` | 5 | 2026-07-08 |
| [**herdr-annotations**](https://github.com/jagzmz/herdr-annotations)<br><sub>jagzmz</sub> | 通过快速的本地优先弹窗和可复用的收藏集，为 Herdr 中选中的终端文本添加注释 | `annotations` `cli` `coding-agents` `developer-tools` `local-first` | 4 | 2026-07-16 |
| [**herdr-unread-marker**](https://github.com/JoanGil/herdr-unread-marker)<br><sub>JoanGil</sub> | 通过快捷键手动将聚焦中的 Agent 标记为已读/未读（仅支持手动） | `shell` | 4 | 2026-07-17 |
| [**herdr-harpoon**](https://github.com/KonstantinKai/herdr-harpoon)<br><sub>KonstantinKai</sub> | herdr 的 Harpoon：给窗格打标记，按编号跳转。纯 Bash 实现，无需构建 | `bash` `harpoon` `tmux-harpoon` `shell` | 4 | 2026-07-29 |
| [**herdr-equalize-splits**](https://github.com/markhuot/herdr-equalize-splits)<br><sub>markhuot</sub> | herdr 插件：将当前标签页中所有分屏按行/列均分尺寸（绑定到 Ctrl+b =） | `terminal` `tmux` `javascript` | 4 | 2026-07-08 |
| [**herdr-smart-nav**](https://github.com/odiumuniverse/herdr-smart-nav)<br><sub>odiumuniverse</sub> | 跨 nvim 窗口、herdr 窗格、标签页与工作区的智能 Ctrl+h/j/k/l 导航。 | `navigation` `neovim` `neovim-plugin` `nvim` `nvim-lua` | 4 | 🔄 2026-09-14 |
| [**herdr-pretty-which**](https://github.com/ramarivera/herdr-pretty-which)<br><sub>ramarivera</sub> | 面向 Herdr 的 Rust/Ratatui which-key 风格快捷键浮层 | `ratatui` `rust` `terminal` `tui` `which-key` | 4 | 🔄 2026-09-18 |
| [**herdr-navigator**](https://github.com/willfish/herdr-navigator)<br><sub>willfish</sub> | 面向 Vim/Neovim 感知窗格移动的 Herdr 端导航操作 | `navigation` `neovim` `rust` | 4 | 2026-07-07 |
| [**herdr-easyjump**](https://github.com/xzedx/herdr-easyjump)<br><sub>xzedx</sub> | 按下一个键、输入一个字母，即可跳转到任意空间、Agent、窗格或标签页。采用 EasyMotion / Vimium / vim-choosewin 风格的提示标签，直接绘制在 Herdr 侧边栏中。 | `choosewin` `easymotion` `hints` `navigation` `rust` | 4 | 🔄 2026-09-14 |
| [**herdr-pane-switcher**](https://github.com/AlexanderGrooff/herdr-pane-switcher)<br><sub>AlexanderGrooff</sub> | 通过快捷键将注意力切换到高优先级的 Herdr 窗格。 | `rust` | 3 | 2026-08-27 |
| [**🆕 herdr-tmux-session-navigator**](https://github.com/caneppelevitor/herdr-tmux-session-navigator)<br><sub>caneppelevitor</sub> | tmux choose-tree for herdr. Written by someone who left tmux but never gave up prefix+s. | `bubbletea` `terminal` `tmux` `go` | 3 | 🔄 2026-09-18 |
| [**herdr-tmux-layout**](https://github.com/crierr/herdr-tmux-layout)<br><sub>crierr</sub> | 面向运行中的 Herdr 窗格的 tmux 风格预设布局——支持 cycle、even-horizontal、even-vertical、main-horizontal、main-vertical、tiled 和 balance | `go` | 3 | 2026-08-30 |
| [**herdr-convo-index**](https://github.com/dzwduan/herdr-convo-index)<br><sub>dzwduan</sub> | herdr 中 Claude Code 窗格的轮次索引——跳转到任意历史轮次并在弹窗中查看 | `python` | 3 | 2026-07-27 |
| [**herdr-popupx**](https://github.com/jeromychu23/herdr-popupx)<br><sub>jeromychu23</sub> | 面向 Herdr 的持久化原生浮动速记弹窗 | `rust` `terminal` `tui` | 3 | 2026-07-21 |
| [**herdr-float**](https://github.com/meerzulee/herdr-float)<br><sub>meerzulee</sub> | 类似 Zellij 的 ALT+F 浮动窗格 | `shell` | 3 | 2026-07-20 |
| [**herdr-confirm-close-pane**](https://github.com/poweroutlet2/herdr-confirm-close-pane)<br><sub>poweroutlet2</sub> | 在关闭窗格前询问确认的 herdr 插件，类似 tmux 的 prefix+x confirm-before | `shell` | 3 | 2026-07-06 |
| [**herdr-mission-control**](https://github.com/vjeantet/herdr-mission-control)<br><sub>vjeantet</sub> | herdr 的 Mission Control：按一个键，将工作区所有窗格按标签页分组，以实时平铺网格展示，选中即可切换过去。 | `expose` `mission-control` `terminal` `tui` `rust` | 3 | 2026-09-01 |
| [**herdr-voice**](https://github.com/aneym/herdr-voice)<br><sub>aneym</sub> | herdr 的语音控制——通过语音创建空间、拆分窗格并驱动编程 Agent。基于 OpenAI Realtime，带实时听写文本的浮动 HUD | `openai-realtime-api` `voice` `javascript` | 2 | 🔄 2026-09-17 |
| [**herdr-next-agent**](https://github.com/choplin/herdr-next-agent)<br><sub>choplin</sub> | 在处于所配置语义状态的 Herdr Agent 之间移动 | `go` | 2 | 2026-08-24 |
| [**herdr-which-key**](https://github.com/CowboyVang/herdr-which-key)<br><sub>CowboyVang</sub> | 面向 herdr 的 which-key 风格键位映射浮层——按一个键即可看到 prefix 下所有按键绑定的分组和标签，再按第二个键即可执行。需主动呼出，而非长按显示。零依赖 | `keybindings` `terminal` `which-key` `python` | 2 | 🔄 2026-09-15 |
| [**herdr-equalize-vsplit**](https://github.com/devoc09/herdr-equalize-vsplit)<br><sub>devoc09</sub> | 将当前窗格向右分屏并均分列宽的 Herdr 插件 | `go` | 2 | 2026-07-15 |
| [**herdr-easymotion**](https://github.com/elliotekj/herdr-easymotion)<br><sub>elliotekj</sub> | 🦘 在 Herdr 窗格之间直接跳转 | `javascript` | 2 | 2026-07-20 |
| [**herdr-break-pane**](https://github.com/iuhoay/herdr-break-pane)<br><sub>iuhoay</sub> | 将聚焦窗格移动到新标签页的小型 Herdr 插件 | `pane` `javascript` | 2 | 2026-08-27 |
| [**herdr-prevtab**](https://github.com/joo-was-already-taken/herdr-prevtab)<br><sub>joo-was-already-taken</sub> | 切换到上一个聚焦标签页的 Herdr 插件 | `rust` | 2 | 🔄 2026-09-08 |
| [**herdr-normal-mode**](https://github.com/maedana/herdr-normal-mode)<br><sub>maedana</sub> | 面向 herdr 侧边栏的 Vim 风格普通模式——j/k 移动行，h/l 切换标签页，0-9 选择窗格 | `rust` `tui` | 2 | 2026-08-24 |
| [**herdr-next-agent**](https://github.com/martin-ro/herdr-next-agent)<br><sub>martin-ro</sub> | Herdr 插件：按可配置的状态优先级，跳转到下一个需要关注的 Agent | `python` | 2 | 🔄 2026-09-10 |
| [**herdr-lazytask**](https://github.com/mdetweil/herdr-lazytask)<br><sub>mdetweil</sub> | 在 herdr 分屏窗格中使用 Lazytask（打开/聚焦/切换），并提供 Taskwarrior 快捷操作 | `lazytask` `taskwarrior` `terminal` `rust` | 2 | 2026-08-02 |
| [**herdr-quotr**](https://github.com/napalmpapalam/herdr-quotr)<br><sub>napalmpapalam</sub> | 通过 herdr 弹窗，把 Agent 自己的回答引用后再丢回给它 | `claude-code` `rust` `tui` | 2 | 2026-09-01 |
| [**herdr-plugin-agent-attention**](https://github.com/peterwiebe/herdr-plugin-agent-attention)<br><sub>peterwiebe</sub> | 跳转到最近被阻塞或已完成的 Agent 的 Herdr 插件。 | `python` | 2 | 2026-09-04 |
| [**herdr-account-switch**](https://github.com/rcosteira79/herdr-account-switch)<br><sub>rcosteira79</sub> | 无需重新认证即可热切换 Claude Code / Codex 登录。提供浮层选择器、切换到下一个的快捷键，以及按窗格显示的账号徽章（$acct） | `python` | 2 | 🔄 2026-09-07 |
| [**herdr-pane-mover**](https://github.com/ronly2460/herdr-pane-mover)<br><sub>ronly2460</sub> | 通过交互式方向键选择器，在工作区之间移动 Herdr 窗格 | `terminal` `workspace` `shell` | 2 | 2026-08-23 |
| [**herdr-pane-orientation-switcher**](https://github.com/sf1tzp/herdr-pane-orientation-switcher)<br><sub>sf1tzp</sub> | 面向 Herdr 分屏窗格的工作流人体工学优化 | `shell` | 2 | 2026-07-25 |
| [**herdr-ask-inbox**](https://github.com/speardragon/herdr-ask-inbox)<br><sub>speardragon</sub> | 将所有 herdr 工作区中被阻塞的 Claude AskUserQuestion 提示汇总到一个弹窗中，就地回答，绝不会把答案发错 Agent | `claude-code` `javascript` | 2 | 2026-07-25 |
| [**herdr-unread-jump**](https://github.com/to4iki/herdr-unread-jump)<br><sub>to4iki</sub> | 跳转到下一个需要关注的 Herdr Agent 窗格（先是被阻塞的，然后是已完成的） | `agents` `bash` `shell` | 2 | 2026-08-30 |
| [**herdr-machine-manager**](https://github.com/vika2603/herdr-machine-manager)<br><sub>vika2603</sub> | 通过弹出式 TUI 管理 herdr 保存的 SSH 主机：可从 ~/.ssh/config 的别名添加、断开连接而不丢失配置、编辑目标地址。 | `bubbletea` `go` `ssh` `ssh-config` `terminal` | 2 | 🔄 2026-09-15 |
| [**herdr-plugin-ide-jump**](https://github.com/agentience/herdr-plugin-ide-jump)<br><sub>agentience</sub> | 快速回到你的 IDE——将聚焦窗格所属项目的编辑器窗口置顶，或从可筛选的弹窗中选择一个。一个 Herdr 插件 | `python` | 1 | 2026-08-24 |
| [**herdr-hyprland**](https://github.com/aorumbayev/herdr-hyprland)<br><sub>aorumbayev</sub> | 受 Hyprland 启发，为 herdr 带来的操作方式。 | `ai-agents` `developer-tools` `golang` `hyprland` `keybindings` | 1 | 2026-09-04 |
| [**🆕 herdr-launch-default-agent**](https://github.com/blauerberg/herdr-launch-default-agent)<br><sub>blauerberg</sub> | 受 Omarchy 启发的 Herdr 默认 Agent 工作流：在专属标签页中聚焦或启动你偏好的 AI Agent。 | `agents` `herdr-integration` `shell` | 1 | 🔄 2026-09-11 |
| [**🆕 herdr-scratchpad**](https://github.com/brunohq/herdr-scratchpad)<br><sub>brunohq</sub> | 为 herdr 打造的极简按标签页划分的 Markdown 便签本，支持带复选框的待办事项。 | `python` `scratchpad` `tui` | 1 | 🔄 2026-09-12 |
| [**herdr-plugin-tiles**](https://github.com/carsonjones/herdr-plugin-tiles)<br><sub>carsonjones</sub> | 面向 herdr 的简易窗格管理器 | `python` | 1 | 2026-06-19 |
| [**🆕 herdr-notes**](https://github.com/cyperx84/herdr-notes)<br><sub>cyperx84</sub> | 面向 Herdr 的、按工作区独立的 Markdown 速记笔记，用 Go 编写 | `bubbletea` `golang` `markdown` `notes` `go` | 1 | 2026-08-16 |
| [**herdr-tab-jump**](https://github.com/cyperx84/herdr-tab-jump)<br><sub>cyperx84</sub> | 通过任意快捷键，按位置聚焦到 herdr 的第 N 个标签页——可以把数字键分配给标签页和工作区。 | `shell` | 1 | 2026-09-01 |
| [**herdr-last-tab**](https://github.com/dantehemerson/herdr-last-tab)<br><sub>dantehemerson</sub> | 用于切换回上一个聚焦的标签页的插件 | `rust` | 1 | 2026-08-12 |
| [**herdr-swipe-linux**](https://github.com/enisbu/herdr-swipe-linux)<br><sub>enisbu</sub> | 面向 Linux 上 Herdr 的触控板手势：滑动可在窗格、标签页和空间之间切换，轻点即可跳转到等待中的 Agent。 | `evdev` `gestures` `gnome` `hyprland` `linux` | 1 | 2026-09-02 |
| [**herdr-nav-history**](https://github.com/jugyo/herdr-nav-history)<br><sub>jugyo</sub> | 面向 herdr 的浏览器风格前进/后退导航（针对窗格、标签页、工作区的聚焦历史） | `javascript` | 1 | 2026-07-12 |
| [**🆕 herdr-plan-meter**](https://github.com/JunSeo99/herdr-plan-meter)<br><sub>JunSeo99</sub> | 在 herdr 标签栏中显示 Claude Code 和 Codex 的套餐限额，并可通过弹窗查看详情。仅使用 Python 标准库的单文件实现，凭据只读访问。 | `claude-code` `codex` `rate-limit` `usage` `python` | 1 | 🔄 2026-09-16 |
| [**herdr-plugin-switcher**](https://github.com/KadenThomp36/herdr-plugin-switcher)<br><sub>KadenThomp36</sub> | 按住 Ctrl，点按 Tab 即可按最近使用顺序循环切换 herdr 窗格。面向 macOS 版 herdr 的 Arc/Zen 风格窗格切换器 | `swift` | 1 | 2026-08-21 |
| [**herdr-nvim-aware**](https://github.com/KoalaVim/herdr-nvim-aware)<br><sub>KoalaVim</sub> | 面向 herdr 的 Nvim 感知快捷键——支持导航、分屏、关闭、缩放 | `rust` | 1 | 2026-08-20 |
| [**herdr-plugin-last**](https://github.com/m4salah/herdr-plugin-last)<br><sub>m4salah</sub> | 为 Herdr 提供 tmux 风格的上一个标签页/上一个工作区跳转 | `rust` | 1 | 2026-07-30 |
| [**herdr-scratch**](https://github.com/macintacos/herdr-scratch)<br><sub>macintacos</sub> | 面向 herdr 的速记 shell——通过一个组合键开关的弹窗。底层基于 tmux，因此再次打开时会与离开时一模一样 | `go` | 1 | 2026-08-28 |
| [**🆕 herdr-prompt-deck**](https://github.com/matdac12/herdr-prompt-deck)<br><sub>matdac12</sub> | Herdr 的底部提示词栏：可将文件路径、代码片段和草稿文本插入到当前聚焦的 Agent 中。 | `rust` | 1 | 🔄 2026-09-12 |
| [**grove-herdr**](https://github.com/nicksenap/grove-herdr)<br><sub>nicksenap</sub> | Herdr 插件：Grove 工作区创建弹窗，以及与 Herdr 工作区的桥接。 | `grove` `shell` | 1 | 🔄 2026-09-09 |
| [**herdr-touchbar**](https://github.com/omerturhan/herdr-touchbar)<br><sub>omerturhan</sub> | 在 MacBook Touch Bar 上显示工作中和被阻塞的 herdr Agent——点按即可直接跳转到对应标签页 | `ai-agents` `macos` `touchbar` `swift` | 1 | 🔄 2026-09-14 |
| [**🆕 herdr-topstrip**](https://github.com/orcchg/herdr-topstrip)<br><sub>orcchg</sub> | 将每个空间或已有空间上的标签页，以两个窗格的形式打开——上方是一条较窄的区域（通常用于目录导航、shell 命令和 git 操作），下方是较宽的区域（通常用于 Agent 会话）。 | `shell` | 1 | 🔄 2026-09-15 |
| [**🆕 herdr-equalize-panes**](https://github.com/ponko2/herdr-equalize-panes)<br><sub>ponko2</sub> | 在窗格被创建、关闭、移动或退出时，自动保持每个标签页内的窗格大小均匀 | `rust` | 1 | 🔄 2026-09-18 |
| [**herdr-deck-navigation**](https://github.com/raghu-nandan-bs/herdr-deck-navigation)<br><sub>raghu-nandan-bs</sub> | 将 herdr 内置的扁平化工作区/标签页/窗格导航器，替换为无需滚动即可快速到达任意窗格的「Deck」视图 | `rust` `terminal` `tui` | 1 | 2026-08-24 |
| [**herdr-smartnav**](https://github.com/retroaalto/herdr-smartnav)<br><sub>retroaalto</sub> | 为 Herdr 提供方向感知窗格导航的插件 | `go` | 1 | 2026-08-01 |
| [**herdr-edge-nav**](https://github.com/sebcbi1/herdr-edge-nav)<br><sub>sebcbi1</sub> | 在窗格边缘可跨标签页、跨工作区进行方向性移动/调整大小的 Herdr 插件，并能无缝识别 Neovim 分屏 | `lua` | 1 | 2026-08-12 |
| [**herdr-ferry**](https://github.com/shadowfax92/herdr-ferry)<br><sub>shadowfax92</sub> | 可批量移动运行中的 Herdr 窗格和标签页，或合并工作区的 Rust 原生弹窗 | `productivity` `rust` `terminal` `tui` | 1 | 2026-08-19 |
| [**🆕 herdr-scratch**](https://github.com/shadowfax92/herdr-scratch)<br><sub>shadowfax92</sub> | 由私有 tmux 会话支撑的、按窗格持久化的 Herdr 便签弹窗 | `neovim` `productivity` `rust` `terminal` `tmux` | 1 | 2026-08-04 |
| [**herdr-talon**](https://github.com/shadowfax92/herdr-talon)<br><sub>shadowfax92</sub> | 为可见的 Herdr 终端目标显示空间化的键盘提示 | `keyboard-navigation` `productivity` `rust` `terminal` `tmux-fingers` | 1 | 2026-08-20 |
| [**herdr-nav-plus**](https://github.com/shoaibkhanz/herdr-nav-plus)<br><sub>shoaibkhanz</sub> | Ctrl+h/j/k/l 导航可以跨越 herdr 窗格直达工作区——感知 vim 行为，两端可循环 | `javascript` | 1 | 2026-07-18 |
| [**🆕 herdr-clock**](https://github.com/Tyru5/herdr-clock)<br><sub>Tyru5</sub> | 面向 herdr 的 tmux 时钟模式——一个以大号方块字符显示本地时间的弹窗时钟，按任意键即可关闭。 | `rust` `terminal` `tmux` | 1 | 🔄 2026-09-15 |
| [**herdr-hintr**](https://github.com/wraithyy/herdr-hintr)<br><sub>wraithyy</sub> | herdr 插件：which-key 风格的快捷键速查表弹窗——按下按键即可直接执行 | `shell` | 1 | 2026-08-11 |
| [**🆕 herdr-dictate**](https://github.com/abhishekrana/herdr-dictate)<br><sub>abhishekrana</sub> | 在本地将语音转文字，并输入到当前聚焦的 Herdr 窗格中。 | `dictation` `speech-to-text` `voice` `whisper` `rust` | 0 | 🔄 2026-09-12 |
| [**🆕 herdr-plugin-echo**](https://github.com/andischerer/herdr-plugin-echo)<br><sub>andischerer</sub> | 将一个窗格中的按键广播到多个已标记窗格的 Herdr 插件 | `typescript` | 0 | 2026-08-23 |
| [**🆕 asconfirmclose**](https://github.com/asumaran/asconfirmclose)<br><sub>asumaran</sub> | Herdr plugin: close the focused pane, asking first only when a process is running in it | `terminal` `go` | 0 | 🔄 2026-09-20 |
| [**🆕 asgotopr**](https://github.com/asumaran/asgotopr)<br><sub>asumaran</sub> | Herdr plugin: jump to your open GitHub PRs across local repos and worktrees | `go` | 0 | 🔄 2026-09-20 |
| [**🆕 herdr-cwd**](https://github.com/bonanyan/herdr-cwd)<br><sub>bonanyan</sub> | Mirror the focused herdr pane's working directory to the host terminal with OSC 7, so terminal file panels, titles, and new splits follow herdr. | `osc7` `terminal` `javascript` | 0 | 🔄 2026-09-20 |
| [**herdr-split-pane**](https://github.com/choplin/herdr-split-pane)<br><sub>choplin</sub> | 在 Herdr 分屏窗格中直接打开调用方指定的命令 | — | 0 | 2026-08-24 |
| [**herdr-nav**](https://github.com/codingfragments/herdr-nav)<br><sub>codingfragments</sub> | herdr 工作区与窗格导航——herdr-navigation 的现代版，改进了预览支持并新增工作区模板处理 | `html` | 0 | 2026-08-27 |
| [**herdr-agent-numbers**](https://github.com/DillonWall/herdr-agent-numbers)<br><sub>DillonWall</sub> | 为 herdr 的 Agent 面板编号，与 focus_agent（前缀+1..9）保持一致。 | `terminal-multiplexer` `shell` | 0 | 🔄 2026-09-14 |
| [**🆕 herdr-links**](https://github.com/dima-m711/herdr-links)<br><sub>dima-m711</sub> | 为 Herdr 和 Pi 提供的、绑定会话的导航链接。 | `typescript` | 0 | 🔄 2026-09-13 |
| [**🆕 herdr-terminal-scripts**](https://github.com/Fadi729/herdr-terminal-scripts)<br><sub>Fadi729</sub> | Herdr plugin that runs named Scripts from a popup or numbered slots | `typescript` | 0 | 🔄 2026-09-19 |
| [**🆕 herdr-drover**](https://github.com/followbl/herdr-drover)<br><sub>followbl</sub> | Herdr 的「牧羊犬」标签页切换器：按住 Super+T 循环浏览标签页，松开即切换到当前标签页。 | `linux` `python` | 0 | 2026-09-03 |
| [**herdr-desktop-switcher**](https://github.com/gustavocaiano/herdr-desktop-switcher)<br><sub>gustavocaiano</sub> | 面向 Herdr 的实验性 macOS 桌面切换器 | `rust` | 0 | 2026-08-26 |
| [**herdr-harpoon**](https://github.com/hadeson/herdr-harpoon)<br><sub>hadeson</sub> | herdr 的 Harpoon 风格窗格标记：将窗格固定到 1-9 号槽位，跨标签页和工作区直接跳转 | `harpoon` `pane-navigation` `terminal` `tmux` `python` | 0 | 2026-07-25 |
| [**bindr**](https://github.com/itsmistermoon/bindr)<br><sub>itsmistermoon</sub> | 用于在具名快捷键配置之间切换，并可在弹窗中查看/编辑快捷键的 Herdr 插件。 | `rust` | 0 | 2026-09-04 |
| [**herdr-agent-nav**](https://github.com/julianbonomini/herdr-agent-nav)<br><sub>julianbonomini</sub> | 为 herdr 提供的简单 Agent 导航功能。 | `javascript` | 0 | 🔄 2026-09-13 |
| [**herdr-last-tab**](https://github.com/k-narusawa/herdr-last-tab)<br><sub>k-narusawa</sub> | _(暂无描述)_ | `shell` | 0 | 2026-08-22 |
| [**herdr-hasr**](https://github.com/KazBrekker1/herdr-hasr)<br><sub>KazBrekker1</sub> | Hasr（حصر——意为「枚举、完整清点」）——herdr 的 goto 风格弹窗切换器：切换、重命名、删除并创建 Agent、标签页和空间，并实时追踪完成状态 | `tui` `go` | 0 | 2026-07-23 |
| [**herdr-focus-attention**](https://github.com/kuwa72/herdr-focus-attention)<br><sub>kuwa72</sub> | Herdr 插件：依次切换浏览需要关注的 Agent。 | `python` | 0 | 🔄 2026-09-08 |
| [**🆕 herdr-markmap**](https://github.com/maaalo/herdr-markmap)<br><sub>maaalo</sub> | Herdr plugin: live Markmap mind map of AI agent's conversation, merged after every turn without touching the agent's context | `python` | 0 | 🔄 2026-09-20 |
| [**herdr-pane-balancer**](https://github.com/malone-c/herdr-pane-balancer)<br><sub>malone-c</sub> | 在窗格打开和关闭时，让 herdr 窗格始终保持均匀大小。分屏会将聚焦窗格减半，本插件会重新平衡整个标签页 | `python` | 0 | 2026-08-07 |
| [**🆕 herdr-battery**](https://github.com/morphysh/herdr-battery)<br><sub>morphysh</sub> | Laptop battery status for the herdr tab bar (⚡charging 🔋on-battery 🔌held), plus a health/power details popup. Linux sysfs, zero dependencies. | `battery` `linux` `status-bar` `shell` | 0 | 🔄 2026-09-16 |
| [**🆕 herdr-pane-memo**](https://github.com/NakasamaJ/herdr-pane-memo)<br><sub>NakasamaJ</sub> | 为 Herdr 提供的按窗格划分的便签备忘录，通过你自行添加的快捷键以模态弹窗打开。非官方社区工具。 | `shell` | 0 | 🔄 2026-09-13 |
| [**🆕 nvim-ascii-on-focus**](https://github.com/NathanymousFu/nvim-ascii-on-focus)<br><sub>NathanymousFu</sub> | Switch to a Latin input source when a Herdr pane running Neovim gains focus | `input-method` `macos` `neovim` `shell` | 0 | 🔄 2026-09-18 |
| [**herdr-plugins**](https://github.com/oullin/herdr-plugins)<br><sub>oullin</sub> | 面向 Herdr 的一组专注、可独立安装的插件合集 | `typescript` | 0 | 2026-08-09 |
| [**🆕 herdr-quickpad**](https://github.com/rhinoc/herdr-quickpad)<br><sub>rhinoc</sub> | Notes and shell commands in a Herdr popup. | `checklist` `developer-tools` `markdown` `notes` `productivity` | 0 | 🔄 2026-09-18 |
| [**🆕 tmurdr**](https://github.com/sergiopx/tmurdr)<br><sub>sergiopx</sub> | 在 Herdr 中延续你的 tmux 肌肉记忆：将 ctrl+space 前缀键与完整的 tmux 键位映射应用到你的 config.toml 中。 | `keybindings` `terminal` `tmux` `shell` | 0 | 🔄 2026-09-14 |
| [**herdr-pane-equalizer**](https://github.com/shanefully-done/herdr-pane-equalizer)<br><sub>shanefully-done</sub> | 将 herdr 窗格调整为均匀大小，支持自动或手动执行 | `javascript` | 0 | 2026-08-20 |
| [**🆕 herdr-worktrees**](https://github.com/SpaceK33z/herdr-worktrees)<br><sub>SpaceK33z</sub> | Switch, create, and remove Git worktrees from a Herdr popup | `rust` | 0 | 🔄 2026-09-17 |
| [**herdr-jump**](https://github.com/tp6gw94/herdr-jump)<br><sub>tp6gw94</sub> | 面向 Herdr 工作区、标签页、窗格和 Agent 的键盘导航 | `javascript` | 0 | 2026-08-16 |
| [**🆕 herdr-focus**](https://github.com/trapple/herdr-focus)<br><sub>trapple</sub> | 聚焦下一个被阻塞/已完成的 Agent 窗格，并将终端应用置于前台。附带全局快捷键 | `shell` | 0 | 2026-07-19 |
| [**🆕 herdr-balance-panes**](https://github.com/willfish/herdr-balance-panes)<br><sub>willfish</sub> | 将当前 Herdr 标签页中的窗格调整为均匀大小（相当于 tmux 的 select-layout -E） | `rust` `terminal` `tmux` | 0 | 2026-08-05 |
| [**🆕 herdr-tab-notes**](https://github.com/yang3kc/herdr-tab-notes)<br><sub>yang3kc</sub> | 为每个 Herdr 标签页提供一个纯 Markdown 便签本，可切换显示在右侧的窄分屏中。无需构建步骤，也无需后台守护进程。 | `shell` | 0 | 🔄 2026-09-15 |
| [**🆕 herdr-kakoune-popup**](https://github.com/Yukaii/herdr-kakoune-popup)<br><sub>Yukaii</sub> | 在 Herdr 原生弹窗中运行 Kakoune 的终端命令 | `kakoune` `shell` | 0 | 2026-08-20 |
| [**🆕 herdr-plugin-pane-move**](https://github.com/yuloop/herdr-plugin-pane-move)<br><sub>yuloop</sub> | Herdr 插件：通过快捷键移动窗格。 | `shell` | 0 | 2026-09-04 |

<details><summary>与此目的也相关</summary>

- [thanhdat77/herdr-navigator](https://github.com/thanhdat77/herdr-navigator) — 通过一个模糊导航器跳转到任意 Herdr 工作区、Agent、项目、会话、远程连接、目录或操作
- [speardragon/herdr-plugin-manager](https://github.com/speardragon/herdr-plugin-manager) — 在弹窗中管理 herdr 插件——安装、更新、启用/禁用、卸载，并浏览 herdr-plugin 市场。推荐快捷键：prefix+p
- [jorge07RD/herdr-ssh-manager](https://github.com/jorge07RD/herdr-ssh-manager) — 保存 SSH 主机，并从 Herdr 内的模糊弹窗中重新连接——按 Enter 即可直接将弹窗内容交给 ssh
- [purehate/herdr-plugin-picker](https://github.com/purehate/herdr-plugin-picker) — Herdr 的浮动弹窗选择器——可跳转到任意空间、Agent、标签页或窗格，向所有标记窗格广播同一条命令，并从 ~/.ssh/config 发起带实时可达性检测的 SSH 连接。完全由键盘驱动。
- [victor-software-house/herdr-stash](https://github.com/victor-software-house/herdr-stash) — 储藏 Herdr 工作区——停止其中的 Agent，同时保留其结构和对话内容，之后可从可点击的双栏弹窗中恢复
- [bayoudhi/herdr-prayer-times](https://github.com/bayoudhi/herdr-prayer-times) — 在 Herdr 侧边栏中显示下一次礼拜时间和倒计时，并附带时间表弹窗和通知
- [black-atom-industries/helm.herdr](https://github.com/black-atom-industries/helm.herdr) — 通过一个模糊导航器跳转到任意 Herdr 工作区、Agent、项目、会话、远程连接、目录或操作
- [karanpatel1993/herdr-nav](https://github.com/karanpatel1993/herdr-nav) — File navigation, code search and jdb debugging inside herdr — fzf, ripgrep and a Java debugger wired into you…
- [bearylabs/herdr-better-worktrees](https://github.com/bearylabs/herdr-better-worktrees) — A fast Herdr popup for managing Git worktrees in a predictable embedded-bare layout: create, clone, open, ins…
- [Joxtacy/herdr-plugin-vault](https://github.com/Joxtacy/herdr-plugin-vault) — 在 herdr 弹窗中浏览过去的 Claude Code 会话，并在新标签页中恢复所选的那个
- [leonho/herdr-idle-panes](https://github.com/leonho/herdr-idle-panes) — herdr 插件：以清单弹窗形式查看并关闭停留在闲置 shell 的窗格
- [ram4-dev/herdr-notify-center](https://github.com/ram4-dev/herdr-notify-center) — 为 Herdr 提供服务器范围的 Agent 通知，配有持久化的弹窗收件箱
- [shoaibkhanz/herdr-active-agent-jump](https://github.com/shoaibkhanz/herdr-active-agent-jump) — herdr 插件：按布局顺序前后循环聚焦正在进行中（工作中/被阻塞）的 Agent——作为 attention-jump 的 vim 风格补充
- [yojahny55/herdr-space-groups](https://github.com/yojahny55/herdr-space-groups) — herdr 插件：将 Space 分组为带名称、带颜色的组——支持选择器弹窗（鼠标+键盘）、侧边栏分组标题和自动排序

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-files"></a>

## 文件浏览与编辑器联动

> 想在窗格中打开文件树，或与编辑器的状态保持一致

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**terminal-code**](https://github.com/zenbu-labs/terminal-code)<br><sub>zenbu-labs</sub> | 在终端中运行的 VS Code | `cli` `terminal` `vscode` `typescript` | 2037 | 🔄 2026-09-11 |
| [**herdr-file-viewer**](https://github.com/smarzban/herdr-file-viewer)<br><sub>smarzban</sub> | 面向 herdr 的只读文件查看器，支持感知 Git 状态。键盘驱动的 TUI（同时支持鼠标）：树形结构 + 内容窗格，支持差异对比、Markdown 渲染和语法高亮 | `file-viewer` `git` `ratatui` `rust` `terminal` | 585 | 🔄 2026-09-16 |
| [**herdr-sidebar**](https://github.com/alexarthurs/herdr-sidebar)<br><sub>alexarthurs</sub> | 面向 herdr 的 VS Code 风格侧边栏：将文件浏览器和 Git 源代码管理整合到一个窗格——带语法高亮的预览、VS Code 风格的差异对比、GitLens 风格的抽屉面板、AI 生成提交信息 | `git` `ratatui` `rust` `sidebar` `terminal` | 366 | 🔄 2026-09-19 |
| [**token**](https://github.com/ThorstenRhau/token)<br><sub>ThorstenRhau</sub> | Neovim 配色方案，并附带面向整个终端环境的社区贡献主题。 | `bat-theme` `delta-theme` `emacs-theme` `fish-theme` `fzf-theme` | 309 | 🔄 2026-09-13 |
| [**ttt**](https://github.com/eugenioenko/ttt)<br><sub>eugenioenko</sub> | TTT Editor（Terminal Text Tool）——一款可在终端中运行、真正能替代 VS Code、Zed 和 Sublime 的编辑器。这是一个操作体验如 GUI 般的 TUI，单一二进制文件，零配置。 | `cli` `code-editor` `developer-tools` `diff` `editor` | 304 | 🔄 2026-09-20 |
| [**herdr-mirror**](https://github.com/nikok6/herdr-mirror)<br><sub>nikok6</sub> | 在同一窗口统一本地和远程会话：将远程 herdr 服务器镜像到本地侧边栏，并通过 SSH 操控 | `rust` | 238 | 🔄 2026-09-06 |
| [**herdr-nvim**](https://github.com/ChmaraX/herdr-nvim)<br><sub>ChmaraX</sub> | 将 Neovim 完全集成到你的 herdr 工作区 | `lua` `neovim` `nvim` `nvim-plugin` `rust` | 196 | 🔄 2026-09-13 |
| [**dotfiles**](https://github.com/edmundmiller/dotfiles)<br><sub>edmundmiller</sub> | 用于让我的 dotfiles 始终保持最新 | `dotfiles` `emacs` `nix-dotfiles` `nixos` `nixos-configuration` | 80 | 🔄 2026-09-20 |
| [**herdr-lazygit**](https://github.com/Crokily/herdr-lazygit)<br><sub>Crokily</sub> | 在 herdr 侧边栏窗格中运行 lazygit，支持 AI 生成提交信息——打开、展开、提交都只需一个按键 | `git` `lazygit` `shell` | 34 | 🔄 2026-09-14 |
| [**herdr-yazi**](https://github.com/speardragon/herdr-yazi)<br><sub>speardragon</sub> | 在 herdr 窗格中打开 Yazi | `shell` | 28 | 2026-08-19 |
| [**🆕 herdr-agent-progress**](https://github.com/eliasstravik/herdr-agent-progress)<br><sub>eliasstravik</sub> | Agent-reported task progress and activity for the Herdr sidebar | `rust` | 24 | 🔄 2026-09-15 |
| [**herdr-quicklook**](https://github.com/dwarvesf/herdr-quicklook)<br><sub>dwarvesf</sub> | herdr 的 Quick Look：将剪贴板中的路径以浮层形式弹出预览，一键切换到文件查看器 | `terminal` `shell` | 12 | 2026-08-26 |
| [**herdr-context.nvim**](https://github.com/makyinmars/herdr-context.nvim)<br><sub>makyinmars</sub> | 在 Neovim 中选中代码或停在某一行，选择一个正在运行的 Herdr Agent，将结构化的上下文暂存到该 Agent 的提示词中（不直接提交） | `lua` | 11 | 🔄 2026-09-17 |
| [**herdr-git-status**](https://github.com/ezcorp-org/herdr-git-status)<br><sub>ezcorp-org</sub> | herdr 插件：在侧边栏分支名旁显示每个空间的 git 工作区状态（已暂存/已修改/未跟踪/冲突） | `rust` | 9 | 2026-08-10 |
| [**herdr-workbench**](https://github.com/azizuysal/herdr-workbench)<br><sub>azizuysal</sub> | 精致的 Herdr 项目侧边栏，具备文件浏览器、实时文件/内容搜索、只读源代码管理、丰富的预览、文件图标和 Git 状态装饰 | `rust` | 7 | 🔄 2026-09-19 |
| [**herdr-fresh**](https://github.com/rvalledorjr/herdr-fresh)<br><sub>rvalledorjr</sub> | 在 herdr 窗格内将终端 IDE「Fresh」作为文件查看器和编辑器运行的 herdr 插件 | `developer-tools` `editor` `fresh` `ide` `terminal` | 6 | 2026-07-17 |
| [**herdr-markdown-viewer**](https://github.com/arvindparmar-me/herdr-markdown-viewer)<br><sub>arvindparmar-me</sub> | Herdr 插件：拖选一个 Markdown 路径并按下 prefix+m，即可在右侧分屏窗格中预览 | `shell` | 5 | 2026-07-17 |
| [**herdr-flist**](https://github.com/devskale/herdr-flist)<br><sub>devskale</sub> | herdr 的文件列表插件 | `python` | 5 | 2026-07-10 |
| [**advanced-herdr-file-viewer**](https://github.com/thuanlm215/advanced-herdr-file-viewer)<br><sub>thuanlm215</sub> | Git-aware, read-only herdr file viewer: tree, diffs, markdown, syntax, and inline image preview. | `file-viewer` `ripgrep` `rust` `tui` | 4 | 🔄 2026-09-19 |
| [**dotfiles**](https://github.com/tifandotme/dotfiles)<br><sub>tifandotme</sub> | ~/.*（家目录下的配置文件） | `aerospace` `chezmoi` `cmux` `dotfiles` `ghostty` | 4 | 🔄 2026-09-20 |
| [**herdr-plugin-mermaid-preview**](https://github.com/Volpestyle/herdr-plugin-mermaid-preview)<br><sub>Volpestyle</sub> | 在 Herdr 中为 Claude Code 和 Codex 的输出内容提供 Mermaid 图的实时预览 | `claude-code` `mermaid` `openai-codex` `terminal` `javascript` | 4 | 2026-07-10 |
| [**openloc.nvim**](https://github.com/Zamua/openloc.nvim)<br><sub>Zamua</sub> | 在已属于该工作区的 Neovim 中打开文件引用 | `lua` | 4 | 2026-08-25 |
| [**herdr-wait**](https://github.com/cdc-lst/herdr-wait)<br><sub>cdc-lst</sub> | 根据窗格的进程树判断闲置 Agent 窗格实际在做什么（例如 'waiting: build-api' 或 'waiting: codex'）并打上标签的可配置 herdr 插件 | `typescript` | 3 | 2026-07-03 |
| [**herdr-file-viewer**](https://github.com/ismaelosuna7824/herdr-file-viewer)<br><sub>ismaelosuna7824</sub> | 集文件浏览器、代码查看器和 Git 客户端于一体的键盘驱动 Herdr 窗格应用——用 Go + Bubble Tea 编写 | `bubbletea` `git` `golang` `tui` `go` | 3 | 2026-08-08 |
| [**herdr-lazygit**](https://github.com/JacquesvanWyk/herdr-lazygit)<br><sub>JacquesvanWyk</sub> | 在 herdr 分屏窗格或标签页中打开 lazygit，支持智能切换（打开/聚焦/关闭） | `lazygit` `shell` | 3 | 2026-07-12 |
| [**herdr-yazi-windows**](https://github.com/Only-Moon/herdr-yazi-windows)<br><sub>Only-Moon</sub> | herdr-yazi 的 Windows 移植版，借助 herdr v0.8+ 支持原生 Windows 窗格生成 | `file` `file-manager` `pidotdev` `python` `tui` | 3 | 2026-08-14 |
| [**herdr-x**](https://github.com/playsthisgame/herdr-x)<br><sub>playsthisgame</sub> | 在 herdr 内的终端分屏中浏览 x.com，并在 $EDITOR 中起草推文发送给自己 | `cli` `terminal` `terminal-browser` `twitter` `shell` | 3 | 2026-08-20 |
| [**herdr-open-in-editor**](https://github.com/timofey-TK/herdr-open-in-editor)<br><sub>timofey-TK</sub> | 在 VS Code 或 Zed 中打开本地或远程的 Herdr 工作区 | `vscode` `zed` `python` | 3 | 2026-07-30 |
| [**herdr-flutter**](https://github.com/ablause/herdr-flutter)<br><sub>ablause</sub> | 在编程 Agent 旁边监视、热重载并检查运行中 Flutter 应用的 herdr 侧边栏 | `dart` | 2 | 2026-07-27 |
| [**herdr-footprint**](https://github.com/harpal-singh-qp/herdr-footprint)<br><sub>harpal-singh-qp</sub> | 在 Herdr 侧边栏中按空间显示磁盘占用与上下文用量。 | `python` | 2 | 🔄 2026-09-16 |
| [**herdr-claude-usage-multi**](https://github.com/iamhouser/herdr-claude-usage-multi)<br><sub>iamhouser</sub> | Herdr 侧边栏中的 Claude 套餐使用量表——会话/周 %、颜色随用量升级、重置倒计时，并通过 CLAUDE_CONFIG_DIR 配置支持多账号 | `claude-code` `python` | 2 | 2026-09-04 |
| [**scp-explorer**](https://github.com/TinocoAI/scp-explorer)<br><sub>TinocoAI</sub> | MobaXterm 风格的 SCP 文件浏览器 herdr 插件（跨平台支持 macOS/Linux/Windows） | `curses` `file-manager` `scp` `python` | 2 | 2026-09-03 |
| [**herdr-launcher-pane**](https://github.com/y-hirakaw/herdr-launcher-pane)<br><sub>y-hirakaw</sub> | herdr 的固定式点击启动窗格——按工作区启动 Finder/资源管理器、VS Code，或你配置的任意命令 | `launcher` `launcher-pane` `productivity` `python` | 2 | 2026-08-10 |
| [**herdr-yazi-links**](https://github.com/yakovlevs01/herdr-yazi-links)<br><sub>yakovlevs01</sub> | 从 Herdr 中打开 Yazi 里的文件超链接；可选补丁支持纯文本路径。 | `yazi` `python` | 2 | 🔄 2026-09-15 |
| [**🆕 herdr-agent-icons**](https://github.com/adihex/herdr-agent-icons)<br><sub>adihex</sub> | Herdr plugin: real per-agent logo icons in the sidebar via a generated PUA font | `python` | 1 | 🔄 2026-09-18 |
| [**herdr-cursor-open**](https://github.com/alex-devdone/herdr-cursor-open)<br><sub>alex-devdone</sub> | 在 Cursor 或 VS Code 中打开聚焦的 herdr 窗格——包括通过 Remote-SSH 连接到远程 herdr 的窗格 | `cursor` `vscode` `shell` | 1 | 🔄 2026-09-07 |
| [**herdr-context**](https://github.com/Anthodev/herdr-context)<br><sub>Anthodev</sub> | 面向 herdr 的项目上下文面板——带 git 状态的文件树和 LLM 对话历史，始终陪伴在你的 Agent 身旁 | `git` `jj` `ratatui` `rust` `sidebar` | 1 | 🔄 2026-09-11 |
| [**🆕 asgoto**](https://github.com/asumaran/asgoto)<br><sub>asumaran</sub> | Tree-style switcher across herdr repos, worktrees and panes | `go` | 1 | 🔄 2026-09-20 |
| [**herdr-jetbrains**](https://github.com/chenyao0910/herdr-jetbrains)<br><sub>chenyao0910</sub> | 在 Rider、WebStorm、IntelliJ IDEA 或 GoLand 中打开当前活动的 Herdr 工作区或工作树 | `developer-tools` `git-worktree` `goland` `intellij-idea` `jetbrains` | 1 | 2026-08-30 |
| [**herdr-usage-line**](https://github.com/hanbong5938/herdr-usage-line)<br><sub>hanbong5938</sub> | 在 Herdr 侧边栏用一行显示订阅速率限制窗口及重置倒计时。 | `cli` `usage` `go` | 1 | 🔄 2026-09-10 |
| [**🆕 herdr-visuals**](https://github.com/hx-w/herdr-visuals)<br><sub>hx-w</sub> | 为 Herdr 提供按会话划分的 Mermaid、LaTeX 及本地图片预览，并支持 Kitty 图形代理。 | `javascript` | 1 | 🔄 2026-09-19 |
| [**herdr-file-viewer**](https://github.com/jomarmontuya/herdr-file-viewer)<br><sub>jomarmontuya</sub> | 右侧显示的 Herdr 文件树插件，支持文件标签页、跟随当前目录、Git 状态装饰和可点击链接 | `go` | 1 | 2026-07-13 |
| [**herdr-scratchdock**](https://github.com/mvaios/herdr-scratchdock)<br><sub>mvaios</sub> | 在 herdr 中将编码 Agent 的临时文件夹停靠在其旁边——实时目录树、文本与图片预览，并在 Agent 开始工作时自动打开。 | `claude-code` `tui` `python` | 1 | 🔄 2026-09-13 |
| [**🆕 herdr-disp-model**](https://github.com/pdalinis/herdr-disp-model)<br><sub>pdalinis</sub> | Display active Codex, Claude Code, Pi, and Hermes models in the Herdr agent sidebar. | `ai-agents` `claude-code` `codex` `developer-tools` `hermes-agent` | 1 | 🔄 2026-09-19 |
| [**herdr-yazi-explorer**](https://github.com/pjs-0457/herdr-yazi-explorer)<br><sub>pjs-0457</sub> | 在触发它的工作区内的 herdr 标签页/分屏中打开 Yazi（标记为 🗂 yazi），退出后会自动重启 | `yazi` `shell` | 1 | 2026-08-13 |
| [**herdr-branch-labels**](https://github.com/poislagarde/herdr-branch-labels)<br><sub>poislagarde</sub> | 可通过正则表达式配置 Herdr 侧边栏分支标签的格式。 | `git` `regex` `rust` | 1 | 🔄 2026-09-10 |
| [**🆕 herdr-numbered-workspaces**](https://github.com/abrose/herdr-numbered-workspaces)<br><sub>abrose</sub> | 在 herdr 侧边栏中为每个空间前面加上编号，与带索引的 switch_workspace 快捷键对应 | `shell` | 0 | 2026-07-21 |
| [**🆕 herdr-preview**](https://github.com/AlexanderMakarov/herdr-preview)<br><sub>AlexanderMakarov</sub> | Herdr 插件：按下热键高亮屏幕上可见的文件/文件夹路径，并在 file-viewer 中打开。可在 Agent 界面和终端中使用。 | `rust` | 0 | 2026-08-29 |
| [**🆕 herdr-ssh-sessions**](https://github.com/ananianatid/herdr-ssh-sessions)<br><sub>ananianatid</sub> | Herdr plugin that shows ssh and mosh sessions as agent rows in the Agent sidebar. | `mosh` `ssh` `javascript` | 0 | 🔄 2026-09-17 |
| [**🆕 herdr-ctx**](https://github.com/aorumbayev/herdr-ctx)<br><sub>aorumbayev</sub> | 面向 herdr 侧边栏窗格的 Claude 上下文窗口指示器 | `typescript` | 0 | 2026-07-21 |
| [**herdr-sidebar-plugin**](https://github.com/caoool/herdr-sidebar-plugin)<br><sub>caoool</sub> | _(暂无描述)_ | `typescript` | 0 | 2026-09-02 |
| [**🆕 herdr-codex-cost**](https://github.com/Coolsik/herdr-codex-cost)<br><sub>Coolsik</sub> | 在 Herdr 侧边栏中显示 Codex 会话的估算费用 | `codex` `shell` | 0 | 🔄 2026-09-08 |
| [**🆕 herdr-agent-index**](https://github.com/kadaliao/herdr-agent-index)<br><sub>kadaliao</sub> | Show each Herdr agent's panel number in the sidebar, so focus_agent = prefix+alt+1..9 has visible targets. | `sidebar` `terminal` `python` | 0 | 🔄 2026-09-20 |
| [**🆕 herdr-space-index**](https://github.com/kadaliao/herdr-space-index)<br><sub>kadaliao</sub> | Show each Herdr workspace's switch number in the sidebar, so prefix+shift+1..9 has visible targets. | `sidebar` `terminal` `python` | 0 | 🔄 2026-09-17 |
| [**🆕 herdr-nnn**](https://github.com/linuxing3/herdr-nnn)<br><sub>linuxing3</sub> | 在 herdr 中打开 nnn | `shell` | 0 | 2026-08-04 |
| [**🆕 herdr-openmd**](https://github.com/RufusLin/herdr-openmd)<br><sub>RufusLin</sub> | 在 openmd 中打开选中的 Markdown——从 herdr 启动的丰富 Qt 预览 | `shell` | 0 | 2026-07-29 |
| [**herdr-gitui**](https://github.com/Shi1xin/herdr-gitui)<br><sub>Shi1xin</sub> | 在侧边栏窗格中运行 gitui 的 herdr 插件——支持开关切换、展开以及浅色/深色主题 | `gitui` `python` | 0 | 2026-07-28 |
| [**🆕 meadow**](https://github.com/Tetat-Chulchue/meadow)<br><sub>Tetat-Chulchue</sub> | 面向 herdr 终端多路复用器的鼠标驱动文件浏览器窗格 | `python` | 0 | 2026-07-21 |
| [**🆕 herdr-quota-theme**](https://github.com/ummoftgo/herdr-quota-theme)<br><sub>ummoftgo</sub> | 无需修改上游插件，即可让 Herdr Agent Quota 的侧边栏颜色随主题自适应。 | `python` `themes` | 0 | 🔄 2026-09-09 |
| [**🆕 herdr-git-dirty**](https://github.com/viko16/herdr-git-dirty)<br><sub>viko16</sub> | 一个轻量级 Herdr 插件，显示每个 Space 中未提交的 Git 文件数量。 | `git` `python` | 0 | 🔄 2026-09-09 |

<details><summary>与此目的也相关</summary>

- [robbyrussell/herdr-ohmyzsh](https://github.com/robbyrussell/herdr-ohmyzsh) — 面向 Herdr 的 Oh My Zsh 插件：在侧边栏显示耗时较长的命令、完成通知、shell 辅助工具，并可一键在所有闲置窗格中重新加载 Oh My Zsh。
- [ChmaraX/herdr-gitview](https://github.com/ChmaraX/herdr-gitview) — herdr 的 Git 状态/差异面板——审查更改、在 nvim 中编辑、暂存/提交/丢弃，全部在终端内完成
- [vonzelle-vzt/herdr-extensions](https://github.com/vonzelle-vzt/herdr-extensions) — 面向 herdr 的迷你 VS Code——具备 LSP 诊断、自动补全、重命名和跳转到定义的完整编辑器，外加源代码管理、搜索、问题面板、测试、调试器、应用实时预览、运行时错误捕获、图片粘贴和 Agent 差异审查。共…
- [jsmenzies/mergr](https://github.com/jsmenzies/mergr) — 在 Herdr Space 侧边栏行中显示 GitHub 拉取请求状态
- [xzedx/herdr-easyjump](https://github.com/xzedx/herdr-easyjump) — 按下一个键、输入一个字母，即可跳转到任意空间、Agent、窗格或标签页。采用 EasyMotion / Vimium / vim-choosewin 风格的提示标签，直接绘制在 Herdr 侧边栏中。
- [edxeth/herdr-pi-tree](https://github.com/edxeth/herdr-pi-tree) — 以树状结构展示你的 Pi Agent 的侧边栏——谁生成了谁、哪个 worktree 对应哪个分支、谁在等待你。
- [ctbaum/herdr-deck](https://github.com/ctbaum/herdr-deck) — herdr-agents.nvim 的搭配工作区启动器：在预先搭好的 Neovim、Agent、shell 和 lazygit 组合面板中打开或恢复 Claude 和 Codex
- [maedana/herdr-whereami](https://github.com/maedana/herdr-whereami) — 自动重命名标签页以显示你当前所在位置的 Herdr 插件——在 git 仓库内会显示为「仓库名/分支名」
- [bayoudhi/herdr-prayer-times](https://github.com/bayoudhi/herdr-prayer-times) — 在 Herdr 侧边栏中显示下一次礼拜时间和倒计时，并附带时间表弹窗和通知
- [brianh20/herdr-stagr](https://github.com/brianh20/herdr-stagr) — 面向 herdr 的源代码管理侧边栏——通过并排差异对比进行暂存、取消暂存和放弃更改
- [mrzzmrzz/herdr-opendde-harness](https://github.com/mrzzmrzz/herdr-opendde-harness) — 面向 ddeharness 的 Herdr 侧边栏集成：在默认布局中提供原生状态、动态 Agent 名称与摘要，并支持远程客户端。
- [ZingerLittleBee/herdr-agent-pins](https://github.com/ZingerLittleBee/herdr-agent-pins) — 将 Herdr Agent 会话持久固定在 Agents 侧边栏顶部
- [azyu/herdr-agent-cli](https://github.com/azyu/herdr-agent-cli) — 显示每个窗格中运行的是哪个 CLI 的 Herdr 插件，以侧边栏 token 形式呈现，并可按运行时分别着色。
- [bonkey/herdr-bookmark](https://github.com/bonkey/herdr-bookmark) — Herdr 插件：每个工作区可设置三个独立书签（− = ≡），集中显示为一个侧边栏 token，可通过按键切换。
- [jovylle/herdr-session-title-name](https://github.com/jovylle/herdr-session-title-name) — herdr 插件：将 terminal_title_stripped 持久化到标签页（顶部只保留 session_title，标签页关闭后依然保留该标题）
- [jwanga/herdr-plugin-github-status](https://github.com/jwanga/herdr-plugin-github-status) — herdr 插件：以侧边栏宽度停靠在右侧，实时展示 GitHub 项目状态（里程碑、issue、PR、Actions）。
- [kwanwooi25/herdr-plugin-workspace-groups](https://github.com/kwanwooi25/herdr-plugin-workspace-groups) — Keyboard-first workspace grouping and colored sidebar badges for Herdr
- [limars874/herdr-pane-id-metadata](https://github.com/limars874/herdr-pane-id-metadata) — 用于规范化窗格 ID 和精简标签页/窗格侧边栏元数据的最小化 Herdr 插件
- [NathanymousFu/nvim-ascii-on-focus](https://github.com/NathanymousFu/nvim-ascii-on-focus) — Switch to a Latin input source when a Herdr pane running Neovim gains focus
- [yojahny55/herdr-space-groups](https://github.com/yojahny55/herdr-space-groups) — herdr 插件：将 Space 分组为带名称、带颜色的组——支持选择器弹窗（鼠标+键盘）、侧边栏分组标题和自动排序

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-cost"></a>

## Token 与费用管理

> 想看看 Agent 花费了多少，并想削减用量

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**memex**](https://github.com/nicosuave/memex)<br><sub>nicosuave</sub> | 搜索 Claude Code、Codex、Pi、OpenCode、GitHub Copilot 和 Cursor 的会话记录。恢复会话。追踪 token 使用 | `bm25` `claude-code` `codex-cli` `copilot` `hermes-agent` | 222 | 🔄 2026-09-18 |
| [**llmtrim-herdr**](https://github.com/fkiene/llmtrim-herdr)<br><sub>fkiene</sub> | 降低 herdr 的 token 费用：压缩每个 Agent 窗格的请求（实测输入 -31% / 输出 -74%），并在每个窗格的徽章上显示节省的费用 | `llm-proxy` `llmtrim` `powershell` | 51 | 2026-07-02 |
| [**herdr-agent-usage**](https://github.com/senna-lang/herdr-agent-usage)<br><sub>senna-lang</sub> | 为 Herdr 中运行的 Agent 显示上下文使用量表和服务商速率限制 | `ai-agents` `claude-code` `codex` `golang` `rate-limiting` | 43 | 🔄 2026-09-19 |
| [**herdr-token-dashboard**](https://github.com/Davidcreador/herdr-token-dashboard)<br><sub>Davidcreador</sub> | 面向 Herdr Agent 窗格的实时 token 消耗仪表盘和通知 | `ai-agents` `bubbletea` `opencode` `pi-agent` `token-dashboard` | 21 | 🔄 2026-09-14 |
| [**quota**](https://github.com/pinkpixel-dev/quota)<br><sub>pinkpixel-dev</sub> | 一款桌面应用、VSCode 扩展兼 Herdr 插件，用于跟踪 GitHub Copilot、Codex、Claude Code、Antigravity、Kiro、Grok 和 Cursor 的 AI 使用情况。 | `ai-tools` `antigravity` `claude` `codex` `cursor` | 8 | 🔄 2026-09-11 |
| [**herdr-opentab**](https://github.com/hamidi-dev/herdr-opentab)<br><sub>hamidi-dev</sub> | 在 Herdr 侧边栏中实时显示 OpenTab 提供的每个 Agent 的 AI 花费 | `ai-agents` `opentab` `terminal` `python` | 4 | 🔄 2026-09-11 |
| [**herdr-claude-usage**](https://github.com/alejodelosrios/herdr-claude-usage)<br><sub>alejodelosrios</sub> | 不必再为了查配额而打开一个 Claude 会话。Claude 套餐使用情况（会话 % \| 周 %）始终显示在 Herdr 侧边栏中，同一账号下所有工作区共享。通过 Claude Code 自身的凭据获取与 /status 完全一致的精确数字：无需估算，无需额外登录，也不消耗套餐 token | `claude` `claude-code` `python` | 3 | 2026-07-21 |
| [**herdr-grazr**](https://github.com/wazum/herdr-grazr)<br><sub>wazum</sub> | 一个简单可靠的 Claude Code 账号自动切换工具：在触及 5 小时或每周速率限制之前，自动轮换到新账号，让窗格永远不会因用量配额而停摆。是一个 Herdr 插件。 | `account-rotation` `account-switcher` `account-switching` `anthropic` `claude` | 3 | 🔄 2026-09-13 |
| [**herdr-gekiatsu-plugin**](https://github.com/yuuta1219/herdr-gekiatsu-plugin)<br><sub>yuuta1219</sub> | herdr 插件：把 Claude Code 的用量计数器做成了老虎机——1/99 中大奖概率，每天 10:00 JST 重置 | `claude` `claude-code` `python` `tui` | 3 | 2026-08-17 |
| [**herdr-api-credit-bar**](https://github.com/CristianPeralta/herdr-api-credit-bar)<br><sub>CristianPeralta</sub> | herdr 插件：显示按量计费 API 服务商的剩余额度，首先支持阿里云 Model Studio | `shell` | 2 | 2026-09-05 |
| [**herdr-quota**](https://github.com/kvkenyon/herdr-quota)<br><sub>kvkenyon</sub> | 在 Herdr 中一目了然地查看 Claude、Codex、Cursor 和 Kimi 的订阅配额 | `ai-tools` `claude-code` `cursor` `developer-tools` `kimi` | 2 | 2026-09-05 |
| [**herdr-whereami**](https://github.com/maedana/herdr-whereami)<br><sub>maedana</sub> | 自动重命名标签页以显示你当前所在位置的 Herdr 插件——在 git 仓库内会显示为「仓库名/分支名」 | `rust` | 2 | 🔄 2026-09-14 |
| [**🆕 herdr-ctx-bar**](https://github.com/pdalinis/herdr-ctx-bar)<br><sub>pdalinis</sub> | Color-coded context-window usage bars for Codex, Claude Code, Pi, and Hermes Agent in Herdr's Agents sidebar. | `ai-agents` `claude-code` `codex` `context-window` `hermes-agent` | 2 | 🔄 2026-09-19 |
| [**quota-deck**](https://github.com/ArtMoreno/quota-deck)<br><sub>ArtMoreno</sub> | quota-deck：在 Windows、macOS 和 Linux 上的 Herdr 中，显示按凭据划分范围的 AI 配额与上下文。 | `rust` | 1 | 🔄 2026-09-08 |
| [**scopefuel**](https://github.com/mgh3326/scopefuel)<br><sub>mgh3326</sub> | 面向 AI 编程 Agent 套餐的范围感知余量表——显示实际被限制的是什么（账号/模型/分组）以及何时恢复 | `ai-agents` `antigravity` `claude-code` `cli` `codex` | 1 | 🔄 2026-09-19 |
| [**herdr-model-lanes**](https://github.com/terry-li-hm/herdr-model-lanes)<br><sub>terry-li-hm</sub> | herdr 插件：在工作区行中显示 Codex、Claude Max 和 Grok 的配额，并为新 Agent 提供感知配额的模型档位车道（ag） | `claude` `codex` `grok` `model-routing` `quota` | 1 | 2026-08-30 |
| [**herdr-agent-cli**](https://github.com/azyu/herdr-agent-cli)<br><sub>azyu</sub> | 显示每个窗格中运行的是哪个 CLI 的 Herdr 插件，以侧边栏 token 形式呈现，并可按运行时分别着色。 | `coding-agents` `developer-tools` `terminal` `python` | 0 | 🔄 2026-09-11 |
| [**🆕 herdr-bookmark**](https://github.com/bonkey/herdr-bookmark)<br><sub>bonkey</sub> | Herdr 插件：每个工作区可设置三个独立书签（− = ≡），集中显示为一个侧边栏 token，可通过按键切换。 | `python` | 0 | 🔄 2026-09-15 |
| [**🆕 ai-share-usage-herdr**](https://github.com/DongHyunnn/ai-share-usage-herdr)<br><sub>DongHyunnn</sub> | AI Share Usage 的 herdr 插件：在 herdr 终端中追踪共享的 Codex 配额。 | `javascript` | 0 | 🔄 2026-09-12 |
| [**🆕 herdr-cache-hit**](https://github.com/e-kotov/herdr-cache-hit)<br><sub>e-kotov</sub> | 为 Herdr 提供 prompt 缓存 HUD token 显示、实时过期提醒，以及动态的 Agent 排序。 | `agentic-ai` `antigravity` `cache` `claude-code` `cli` | 0 | 🔄 2026-09-11 |
| [**herdr-usage**](https://github.com/Efeguclu1/herdr-usage)<br><sub>Efeguclu1</sub> | 在 Herdr Agent 标签页上以紧凑标记显示 Claude、Codex、Cursor、OpenCode 和 Pi 的账号用量 | `claude-code` `cursor` `openai` `opencode` `python` | 0 | 2026-08-22 |
| [**herdr-tokenlens**](https://github.com/KeithMoc/herdr-tokenlens)<br><sub>KeithMoc</sub> | 以 herdr 窗格形式，实时显示 AI 编码 Agent 的持续成本，以及压缩上下文的收支平衡点。 | `ai-agents` `claude-code` `llm-cost` `tui` `python` | 0 | 2026-09-04 |
| [**herdr-plugin-agent-quota**](https://github.com/kwanwooi25/herdr-plugin-agent-quota)<br><sub>kwanwooi25</sub> | 面向 Herdr 的 Agent 配额——为 Claude Code、Codex 和 Grok 提供 token 与费用仪表盘、侧边栏配额仪表和标签栏摘要 | `javascript` | 0 | 2026-08-30 |
| [**provider-usage**](https://github.com/ryus1234/provider-usage)<br><sub>ryus1234</sub> | Herdr 的服务商用量与配额显示条。 | `ai-usage` `quota-monitor` `rust` | 0 | 2026-08-31 |
| [**herdr-usage-bar**](https://github.com/silverwolfdoc/herdr-usage-bar)<br><sub>silverwolfdoc</sub> | 为 Herdr 中的 AI Agent 显示使用限额和上下文用量，紧凑的底部用量条形式呈现 | `go` | 0 | 🔄 2026-09-17 |
| [**🆕 claude-usage**](https://github.com/yuuta1219/claude-usage)<br><sub>yuuta1219</sub> | herdr 插件：将 Claude Code 使用率（会话%/周%）固定显示在侧边栏底部 | `claude` `claude-code` `python` `tui` | 0 | 2026-08-01 |

<details><summary>与此目的也相关</summary>

- [ThorstenRhau/token](https://github.com/ThorstenRhau/token) — Neovim 配色方案，并附带面向整个终端环境的社区贡献主题。
- [levi-qiao/herdr-agent-quota](https://github.com/levi-qiao/herdr-agent-quota) — 面向 Herdr 的、按凭据划分范围的 AI 配额、上下文与缓存——支持 Claude、Codex、Grok、Agy、OpenCode、Pi、omp、Devin、Muse 和 Cursor
- [Coolsik/herdr-codex-cost](https://github.com/Coolsik/herdr-codex-cost) — 在 Herdr 侧边栏中显示 Codex 会话的估算费用

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-monitor"></a>

## 监控与仪表盘

> 想一目览尽 Agent 和机器的状态

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**zoetrope**](https://github.com/furkankly/zoetrope)<br><sub>furkankly</sub> | 在终端或浏览器中，将 Claude Code 或 Codex 会话实时可视化为流程图。 | `agent-visualization` `claude-code` `codex` `coding-agents` `flow` | 912 | 🔄 2026-09-15 |
| [**clauth**](https://github.com/uwuclxdy/clauth)<br><sub>uwuclxdy</sub> | Claude Code 多账号管理器与用量监控（支持 CLI、TUI 和 MCP 跨账号委派） | `account-manager` `account-switcher` `anthropic` `claude` `claude-code` | 187 | 🔄 2026-09-20 |
| [**herdr-agent-quota**](https://github.com/levi-qiao/herdr-agent-quota)<br><sub>levi-qiao</sub> | 面向 Herdr 的、按凭据划分范围的 AI 配额、上下文与缓存——支持 Claude、Codex、Grok、Agy、OpenCode、Pi、omp、Devin、Muse 和 Cursor | `agent-usage` `ai-agents` `antigravity` `claude-code` `codex` | 128 | 🔄 2026-09-20 |
| [**herdr-radar**](https://github.com/hhdebb/herdr-radar)<br><sub>hhdebb</sub> | Who's working, who's waiting on you — grouped by project, each agent in its vendor's logo and colour. Worktrees nest under their repo, rows order by activity,… | `claudecode` `codex-cli` `coding-agents-plugins` `developer-tools-ai-agent` `terminal-multiplexers` | 58 | 🔄 2026-09-20 |
| [**herdr-beads**](https://github.com/miiraheart/herdr-beads)<br><sub>miiraheart</sub> | herdr 的 beads（bd）任务面板：以列表、表格或看板形式展示你的 bd issue，可作为侧边栏或浮动窗口 | `bd` `beads` `kanban` `rust` `tui` | 27 | 2026-08-25 |
| [**herdr-pc-ram-and-cpu-usage-overlay**](https://github.com/ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay)<br><sub>ezcorp-org</sub> | herdr 插件：按空间（工作区）实时显示 CPU/内存占用率，以占整机资源的比例呈现 | `rust` | 19 | 🔄 2026-09-13 |
| [**herdr-f1**](https://github.com/hmu332233/herdr-f1)<br><sub>hmu332233</sub> | 为 Herdr Agent 打造的 F1 风格仪表盘 | `agent-dashboard` `typescript` | 15 | 🔄 2026-09-10 |
| [**herdr-shell-progress**](https://github.com/bayoudhi/herdr-shell-progress)<br><sub>bayoudhi</sub> | herdr 插件：不仅是编程 Agent，耗时较长的 shell 命令的进度也会实时显示在侧边栏 | `rust` | 13 | 2026-09-04 |
| [**herdr-telemetry**](https://github.com/DIodide/herdr-telemetry)<br><sub>DIodide</sub> | 将工作区和 Agent 遥测数据流式传输到你自己掌控的端点的 Herdr 插件——Go 编写的单一二进制文件，默认注重隐私 | `golang` `telemetry` `go` | 12 | 2026-07-10 |
| [**herdres**](https://github.com/luminexord/herdres)<br><sub>luminexord</sub> | 基于 Tendwire 构建的 Telegram 界面，用于监控和向 Herdr 编程 Agent 发送消息 | `coding-agents` `telegram` `python` | 11 | 2026-08-09 |
| [**shepherd**](https://github.com/ryonakae/shepherd)<br><sub>ryonakae</sub> | 面向 Herdr 管理的编程 Agent 的 worker 可观测性守护进程和运行时桥接 | `pi-coding-agent` `pi-extension` `typescript` | 11 | 2026-08-28 |
| [**🆕 herdr-lcars**](https://github.com/jlcases/herdr-lcars)<br><sub>jlcases</sub> | Command up to 2,000 Herdr AI agents from one LCARS bridge, track Claude/Codex quota per account, and hand off verified context without losing work. | `agent-observability` `ai-agents` `claude-code` `lcars` `openai-codex` | 10 | 🔄 2026-09-20 |
| [**herdr-sysmon**](https://github.com/getpipher/herdr-sysmon)<br><sub>getpipher</sub> | 在 Herdr 侧边栏显示系统指标——CPU、内存、电池、网络、磁盘、时钟。忠实地将 tmux-cpu/tmux-battery/tmux-online-status 状态栏移植为 Herdr 工作区 token。以 macOS 为主 | `battery` `catppuccin` `cpu` `getpipher` `macos` | 7 | 2026-07-26 |
| [**herdr-tally**](https://github.com/jasonrr/herdr-tally)<br><sub>jasonrr</sub> | 为你和你的 Agent 提供按项目划分的待办事项和速记板<br>📝 プロジェクト単位の TODO 管理 | `rust` `todo` | 7 | 🔄 2026-09-20 |
| [**herdr-workboard**](https://github.com/Phoobobo/herdr-workboard)<br><sub>Phoobobo</sub> | herdr 的看板式工作板 TUI：看板对应工作区，任务状态对应标签页，任务会话对应窗格 | `kanban` `tui` `typescript` | 7 | 2026-08-10 |
| [**herdr-devserver-status**](https://github.com/Razz21/herdr-devserver-status)<br><sub>Razz21</sub> | 通过可插拔规范检测窗格中开发服务器，并报告其生命周期状态的 Herdr 插件 | `astro` `cli` `deamon` `dev-server` `extensible` | 7 | 2026-08-25 |
| [**herdr-lazydocker**](https://github.com/sudoeren/herdr-lazydocker)<br><sub>sudoeren</sub> | 在 herdr 的分屏窗格或独立标签页中运行 lazydocker | `docker` `lazydocker` `shell` | 6 | 2026-08-27 |
| [**herdr-kanban**](https://github.com/KokiKono/herdr-kanban)<br><sub>KokiKono</sub> | 将任务与 herdr 标签页关联的终端看板，数据持久化在 SQLite 中 | `rust` | 5 | 2026-07-10 |
| [**herdr-portal**](https://github.com/loofare/herdr-portal)<br><sub>loofare</sub> | 面向 herdr 的任务控制仪表盘——将所有工作区/标签页/窗格中的 Agent 汇总到一个实时 TUI 看板（支持键盘和鼠标）以及网页大屏中：结构化进度展示、Ctrl+B A 打开、点击跳转、可从浏览器直接回复 Agent | `agent-dashboard` `agent-monitor` `ai-agents` `claude-code` `codex` | 5 | 2026-08-20 |
| [**herdr-agent-watcher**](https://github.com/winoooops/herdr-agent-watcher)<br><sub>winoooops</sub> | 面向 Herdr 的编程 Agent 可观测性——实时侧边栏卡片、生命周期通知，以及零配置的 Claude Code 指标桥接 | `claude-code` `rust` | 5 | 🔄 2026-09-09 |
| [**herdr-codex-bridge**](https://github.com/ardasevinc/herdr-codex-bridge)<br><sub>ardasevinc</sub> | 通过一个集中式的 app-server，为 Codex 会话赋予原生的 Herdr 窗格身份标识。 | `ai-agents` `codex` `terminal` `go` | 3 | 🔄 2026-09-13 |
| [**herdr-mise**](https://github.com/funsaized/herdr-mise)<br><sub>funsaized</sub> | 追求「通过」而非「提示词数量」🧑‍🍳 一款在 herdr 中可视化你的 Agent 的工具，刻意保持极小的资源占用。 | `agent` `agent-monitoring` `ai-agents` `cli-tool` `developer-tools` | 3 | 🔄 2026-09-20 |
| [**shepherd**](https://github.com/jwarykowski/shepherd)<br><sub>jwarykowski</sub> | 把你的待办事项统一「牧」起来 | `cli` `developer-tools` `go-lang` `productivity` `task-management` | 3 | 2026-08-21 |
| [**herdr-jcode**](https://github.com/leonardoacosta/herdr-jcode)<br><sub>leonardoacosta</sub> | 一个独立的 Herdr 插件，报告 Jcode 的 working/idle 生命周期状态及会话身份信息。为独立实现，不依赖 fork。 | `jcode` `rust` | 3 | 🔄 2026-09-16 |
| [**herdr-ports**](https://github.com/Numbered-com/herdr-ports)<br><sub>Numbered-com</sub> | 在 herdr 中呈现正在运行的开发服务器：为每个至少运行一个 TCP 监听器的空间显示通用的 $ports 徽章 | `kill` `pids` `ports` `processes` `space` | 3 | 🔄 2026-09-19 |
| [**herdr-status-ui-bar**](https://github.com/speardragon/herdr-status-ui-bar)<br><sub>speardragon</sub> | 在 herdr 标签栏中显示 AI Agent 的方案用量仪表（Claude Code / Codex / Grok） | `claude-code` `codex` `grok` `python` `tab-bar` | 3 | 🔄 2026-09-20 |
| [**herdr-agent-state**](https://github.com/Tyru5/herdr-agent-state)<br><sub>Tyru5</sub> | herdr 的实时 Agent 状态窗格——以更易读的形式显示工作区中每个 Agent 正在做什么 | `claude-code` `rust` `terminal` | 3 | 🔄 2026-09-20 |
| [**adlc-herdr**](https://github.com/voodootikigod/adlc-herdr)<br><sub>voodootikigod</sub> | ADLC 的 herdr 插件——按窗格显示阶段/工单/关卡状态，附带待办看板、关卡操作和 adlc-fleet 运行可观测性。是 voodootikigod/adlc/plugins/adlc-herdr 的自动同步镜像 | `javascript` | 3 | 🔄 2026-09-08 |
| [**herdr-claude-usage**](https://github.com/anyaachan/herdr-claude-usage)<br><sub>anyaachan</sub> | 在 Herdr 中查看 Claude Code 套餐的全局用量：标签栏摘要 + 弹出式仪表盘，基于 statusLine 实现，支持多账号。 | `claude` `claude-code` `cli` `terminal` `shell` | 2 | 2026-09-01 |
| [**herdr-agent-dashboard**](https://github.com/carsonjones/herdr-agent-dashboard)<br><sub>carsonjones</sub> | prefix+a 显示 herdr Agent 列表 | `typescript` | 2 | 2026-07-16 |
| [**herdr-telemetry-bridge**](https://github.com/CodyBontecou/herdr-telemetry-bridge)<br><sub>CodyBontecou</sub> | 将本地工作区、仓库、编程 Agent、模型和追踪遥测数据流式传输到外部客户端的 Herdr 插件 | `coding-agents` `telemetry` `time-md` `javascript` | 2 | 2026-06-26 |
| [**herdr-agentsview**](https://github.com/cpcloud/herdr-agentsview)<br><sub>cpcloud</sub> | 将 AgentsView 的活动压缩显示在一个异常繁忙的终端里 | `rust` | 2 | 2026-08-24 |
| [**herdr-spinner**](https://github.com/hasuwini77/herdr-spinner)<br><sub>hasuwini77</sub> | 通过仅用于显示的窗格元数据，为处于工作状态的 Herdr 窗格显示动态盲文旋转指示器 | `spinner` `terminal` `tui` `javascript` | 2 | 2026-08-27 |
| [**herdr-statusline**](https://github.com/iiii1224/herdr-statusline)<br><sub>iiii1224</sub> | 面向 herdr 会话的可自定义状态栏 | `cli` `statusbar` `statusline` `tmux` `python` | 2 | 2026-08-15 |
| [**herdr-jira-board**](https://github.com/kiitosu/herdr-jira-board)<br><sub>kiitosu</sub> | 在 herdr 中运行的 Jira 看板，附带 Claude Code 会话启动器 | `python` | 2 | 🔄 2026-09-08 |
| [**herdr-cache-ttl**](https://github.com/nytafar/herdr-cache-ttl)<br><sub>nytafar</sub> | herdr 插件：按 Agent 窗格实时倒计时显示 prompt 缓存的 TTL | `rust` | 2 | 2026-08-05 |
| [**herdr-slurm**](https://github.com/quan-meng/herdr-slurm)<br><sub>quan-meng</sub> | 为 Slurm 分配任务创建 Herdr 工作区和受监控的 Agent 标签页 | `hpc` `slurm` `terminal-multiplexer` `python` | 2 | 2026-08-13 |
| [**🆕 herdr-ports**](https://github.com/randomradio/herdr-ports)<br><sub>randomradio</sub> | Herdr plugin: forward a remote workspace port to http://herdr.{workspace}.localhost:{port} | `rust` | 2 | 🔄 2026-09-20 |
| [**herdr-tilt**](https://github.com/the-inconvenience-store/herdr-tilt)<br><sub>the-inconvenience-store</sub> | 面向 Herdr 的键盘驱动 Tilt 仪表盘 | `k8s` `kubernetes` `tilt` `rust` | 2 | 2026-08-24 |
| [**herdr-mem-cpu-load**](https://github.com/thewtex/herdr-mem-cpu-load)<br><sub>thewtex</sub> | 面向 herdr 的 CPU、内存与负载均值监控工具。 | `rust` | 2 | 🔄 2026-09-07 |
| [**herdr-memex-analytics**](https://github.com/vishnutskumar/herdr-memex-analytics)<br><sub>vishnutskumar</sub> | herdr 插件：基于 memex 历史记录，提供会话效率分析和实时 Agent 指导 | `rust` | 2 | 2026-09-01 |
| [**herdr-docker**](https://github.com/abcxff/herdr-docker)<br><sub>abcxff</sub> | 像追踪 herdr 中的 Agent 一样，追踪 docker 构建 | `docker` `javascript` | 1 | 2026-08-12 |
| [**herdr-muse**](https://github.com/akshat12/herdr-muse)<br><sub>akshat12</sub> | 面向 Muse Code 的 Herdr 集成：通过生命周期 hook 获取窗格的 idle/working/blocked 状态（无需 fork Herdr）。 | `ai-agents` `cli` `coding-agents` `muse-code` `terminal` | 1 | 🔄 2026-09-12 |
| [**herdr-cache-timer**](https://github.com/ArteenHD/herdr-cache-timer)<br><sub>ArteenHD</sub> | 在 Herdr 侧边栏中直接显示每个 Agent 的 prompt 缓存何时过期 | `claude-code` `prompt-caching` `terminal` `javascript` | 1 | 2026-08-08 |
| [**herdr-glance**](https://github.com/arvmaan/herdr-glance)<br><sub>arvmaan</sub> | 用于查看 Agent 状态的桌面小组件 | `rust` | 1 | 🔄 2026-09-08 |
| [**herdr-tokscale-dashboard**](https://github.com/astkaasa/herdr-tokscale-dashboard)<br><sub>astkaasa</sub> | 将 Tokscale 作为本地 Herdr 仪表盘窗格打开 | `dashboard` `tokscale` `shell` | 1 | 2026-06-26 |
| [**herdr-nodejs-center**](https://github.com/AZenking/herdr-nodejs-center)<br><sub>AZenking</sub> | 用于监控并聚焦本地 Node.js、Bun 和 Deno 服务的 Herdr 弹窗 | `developer-tools` `nodejs` `javascript` | 1 | 2026-08-20 |
| [**herdr-plugin-codex-subs**](https://github.com/benkraus/herdr-plugin-codex-subs)<br><sub>benkraus</sub> | 显示 CLIProxyAPI 中 Codex 订阅额度和重置积分的 Herdr 仪表盘 | `go` | 1 | 2026-07-30 |
| [**tsk**](https://github.com/chrisg32/tsk)<br><sub>chrisg32</sub> | tsk——一个 TaskPaper/PlainTasks 风格的纯文本任务管理 TUI，使用 Rust 编写。既可独立运行，也可作为 herdr 插件使用。 | `rust` `taskpaper` `todo` `tui` | 1 | 2026-09-03 |
| [**herdr-model-badge**](https://github.com/dkbo/herdr-model-badge)<br><sub>dkbo</sub> | herdr 插件：在 Agent 侧边栏中显示每个 Agent 使用的模型及推理强度。 | `ai-agents` `terminal` `tui` `python` | 1 | 🔄 2026-09-08 |
| [**herdr-overview**](https://github.com/iamgp/herdr-overview)<br><sub>iamgp</sub> | 面向 Herdr 的 Mission Control / Exposé——以平铺方式实时展示所有 space | `terminal` `tui` `javascript` | 1 | 2026-08-28 |
| [**herdr-ports**](https://github.com/ivorpad/herdr-ports)<br><sub>ivorpad</sub> | herdr 插件：一个弹窗，列出正在监听的端口，标出每个端口背后的项目名称，并可将其终止或打开 | `tui` `python` | 1 | 2026-08-27 |
| [**herdr-metrics**](https://github.com/jordanhawkes/herdr-metrics)<br><sub>jordanhawkes</sub> | 在 Herdr 侧边栏中显示 Claude Code、Codex 和 TraeX 的上下文、会话 token 和账号限额指标。是 szrenwei/herdr-agent-metrics 的维护延续 | `claude-code` `openai-codex` `traex` `tui` `python` | 1 | 2026-08-22 |
| [**herdr-tasks**](https://github.com/MatheusBBarni/herdr-tasks)<br><sub>MatheusBBarni</sub> | 面向 Herdr 的看板任务运行器：包含 OpenTUI 看板与 htasks CLI。 | `typescript` | 1 | 🔄 2026-09-11 |
| [**herdr-compose**](https://github.com/mattyan1053/herdr-compose)<br><sub>mattyan1053</sub> | 用于 docker compose 的 Herdr 插件 | `terminal` `tui` `shell` | 1 | 2026-07-24 |
| [**herdr-pulse**](https://github.com/moneycaringcoder/herdr-pulse)<br><sub>moneycaringcoder</sub> | 面向 herdr 的按工作区划分的 Agent 活动历史，以侧边栏迷你走势图形式呈现 | `monitoring` `rust` `sparkline` `terminal` | 1 | 2026-09-01 |
| [**omarchy-crook**](https://github.com/parker-brown-family/omarchy-crook)<br><sub>parker-brown-family</sub> | Crook——在 Omarchy 状态栏上显示哪个编码 Agent 正在等你。一旦有事情等待你处理，图标就会立刻变为紧急状态，托盘中会显示是哪一个。 | `agents` `bar-widget` `claude-code` `hyprland` `omarchy` | 1 | 🔄 2026-09-07 |
| [**herdr-readpending**](https://github.com/rcosteira79/herdr-readpending)<br><sub>rcosteira79</sub> | 标记你还没看完的 Agent。提供带编号的徽章（$read）+ 可重新排序的列表窗格。聚焦该 Agent 时会自动清除标记 | `python` | 1 | 🔄 2026-09-15 |
| [**herdr-agent-metrics**](https://github.com/szrenwei/herdr-agent-metrics)<br><sub>szrenwei</sub> | 面向 Claude Code、Codex 和 TraeX 的轻量级 Herdr 上下文与会话用量指标 | `claude-code` `openai-codex` `traex` `python` | 1 | 2026-08-04 |
| [**herdr-space-tab-metadata**](https://github.com/szrenwei/herdr-space-tab-metadata)<br><sub>szrenwei</sub> | 在侧边栏显示每个 Herdr Space 当前活动的标签页 | `terminal-ui` `python` | 1 | 2026-08-04 |
| [**taskherd**](https://github.com/ukwhatn/taskherd)<br><sub>ukwhatn</sub> | 与 herdr Agent 会话、PR 和 Jira 工单相关联的任务看板 | `claude-code` `kanban` `task-management` `tui` `go` | 1 | 2026-09-01 |
| [**🆕 herdr-hermes-bridge**](https://github.com/AdriaBA/herdr-hermes-bridge)<br><sub>AdriaBA</sub> | 将 Hermes Agent 的生命周期状态报告到 Herdr 窗格中——提供子 Agent、审批与工具活动的确切信息，而非基于屏幕抓取的猜测。 | `python` | 0 | 🔄 2026-09-11 |
| [**herdr-ios-build-status-plugin**](https://github.com/atomsbaza/herdr-ios-build-status-plugin)<br><sub>atomsbaza</sub> | 按需查看的 Herdr iOS 构建+测试状态窗格，附带失败时的截图 | `shell` | 0 | 2026-08-06 |
| [**🆕 herdr-project-filter**](https://github.com/bshearrer/herdr-project-filter)<br><sub>bshearrer</sub> | 将 herdr 的 Agents 侧边栏一次限定显示为单个 git 仓库。 | `javascript` | 0 | 2026-09-05 |
| [**herdr-dev-servers**](https://github.com/carellano/herdr-dev-servers)<br><sub>carellano</sub> | 发现并安全管理运行在 Herdr 窗格中的开发服务器 | `developer-tools` `go` `terminal` | 0 | 2026-08-12 |
| [**herdr-process-guard**](https://github.com/Efeguclu1/herdr-process-guard)<br><sub>Efeguclu1</sub> | 解释并安全停止由编程 Agent 遗留运行的开发服务器 | `claude-code` `codex` `coding-agents` `cursor` `macos` | 0 | 2026-08-24 |
| [**herdr-kanban**](https://github.com/hassox/herdr-kanban)<br><sub>hassox</sub> | 将工作区窗格呈现为看板 | `go` | 0 | 2026-08-21 |
| [**🆕 herdr-reap**](https://github.com/ivorpad/herdr-reap)<br><sub>ivorpad</sub> | herdr 插件：显示所有 Agent 的生命周期状态，一键关闭已完成的那些 | `tui` `python` | 0 | 2026-08-27 |
| [**herdr-pomodoro**](https://github.com/michmos/herdr-pomodoro)<br><sub>michmos</sub> | 在 herdr 状态栏中使用的番茄钟。 | `focus` `pomodoro` `pomodoro-timer` `python` | 0 | 2026-09-04 |
| [**herdr-last-used**](https://github.com/MorganCollins/herdr-last-used)<br><sub>MorganCollins</sub> | 显示每个 herdr Agent 最后一次活跃的时间，按新旧程度着色，并可按活跃度筛选 Agent 侧边栏 | `terminal` `shell` | 0 | 🔄 2026-09-08 |
| [**herdr-idle-shell-badge**](https://github.com/rcosteira79/herdr-idle-shell-badge)<br><sub>rcosteira79</sub> | 为仍有后台 shell 在运行的空闲 Agent 显示徽章 | `python` | 0 | 2026-08-26 |
| [**colloquy**](https://github.com/SoMaCoSF/colloquy)<br><sub>SoMaCoSF</sub> | 面向 Agent 集群的自寻址、临时缓存的因果 DAG 审计日志与遥测 | `colloquy` `gyst` `javascript` | 0 | 2026-07-29 |
| [**🆕 herdr-claude-context-meter**](https://github.com/tmastalirsch/herdr-claude-context-meter)<br><sub>tmastalirsch</sub> | herdr 插件：以进度条形式显示 Claude Code 的上下文用量——同时支持状态栏和 herdr 窗格 | `claude-code` `context-window` `statusline` `shell` | 0 | 2026-08-27 |
| [**🆕 herdr-virtualboard**](https://github.com/virtualboard/herdr-virtualboard)<br><sub>virtualboard</sub> | Kanban board for VirtualBoard feature specs inside Herdr: columns are the lifecycle, cards are specs, and dispatching a card starts a role agent in a pane. | `go` | 0 | 🔄 2026-09-16 |

<details><summary>与此目的也相关</summary>

- [nelsonPires5/herdr-board](https://github.com/nelsonPires5/herdr-board) — herdr 的看板工具——卡片就是提示词，会被派发给可见窗格中的 AI Agent
- [IvoryHeart/herdr-world](https://github.com/IvoryHeart/herdr-world) — Herdr World——面向 Herdr 的多界面网页体验
- [e2b-dev/herdr-e2b-sandbox](https://github.com/e2b-dev/herdr-e2b-sandbox) — 将 git 工作树镜像到 E2B Sandbox 的 herdr 插件——支持单个沙盒或每个 Agent 一条分支的沙盒集群，并配有 TUI 仪表盘
- [quaywin/agys](https://github.com/quaywin/agys) — 通过零污染沙盒，为 Herdr 中的 Antigravity CLI 提供轻松的多配置文件隔离和实时配额追踪
- [Northern-Lighthouse/herdr-fleet](https://github.com/Northern-Lighthouse/herdr-fleet) — 通过 Tailscale 管理一批 herdr 机器——仪表盘插件、自动发现、感知容量的 Agent 派发、无盘工作区
- [cdowell09/herdr-pr-board](https://github.com/cdowell09/herdr-pr-board) — 面向 Herdr 的可配置跨仓库 GitHub 拉取请求仪表盘
- [bengemine/herdr-hibernate](https://github.com/bengemine/herdr-hibernate) — 让 Herdr 中空闲的编程 Agent 窗格（Claude Code、Codex、Grok）休眠——释放内存，按 Enter 即可恢复原会话
- [Javamomma/herdr-scribe](https://github.com/Javamomma/herdr-scribe) — herdr 插件：不录音的实时会议转录——将麦克风输入转为仅存于内存的文字记录和实时分析窗格；停止时生成会议纪要、可选策略关卡以及可审查的自动草稿。支持 Linux/WSL2 和 macOS
- [sazardev/herdr-code-board](https://github.com/sazardev/herdr-code-board) — Herdr 内面向 Agent 提示词的看板队列——卡片会将真实 Agent 派发到窗格、工作树和工作区，并可通过规则将一张卡片链到下一张
- [spad-0x/herdr-mobile-pro](https://github.com/spad-0x/herdr-mobile-pro) — 一款高性能、移动优先的 PWA 仪表盘，采用 Cyber-Dark 设计风格，可直接从智能手机编排 Herdr 与自主 AI Agent。具备安全 HTTPS、语音听写输入、图片上传，以及将终端输出实时语义解析为聊天式…
- [chouxcreams/herdr-dashboard](https://github.com/chouxcreams/herdr-dashboard) — herdr 工作区的 PR 状态仪表盘 TUI——一目了然地查看每个窗格对应的 PR 状态/CI/审查情况
- [GranamyrBR/LunaCrab](https://github.com/GranamyrBR/LunaCrab) — 为另一个项目保留
- [IniZio/nexus](https://github.com/IniZio/nexus) — Herdr plugin for running worktree in Cloud-Hypervisor sandboxes, with mem/cpu/disk hotplug and auto port-forw…
- [maedana/herdr-agents-preview](https://github.com/maedana/herdr-agents-preview) — Herdr 的多 Agent 终端预览仪表盘：同时显示所有运行中的 Agent，所选 Agent 占据大部分宽度
- [ryus1234/provider-usage](https://github.com/ryus1234/provider-usage) — Herdr 的服务商用量与配额显示条。

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-finder"></a>

## 搜索与模糊查找器

> 只记得大概名字也想调出命令或项目

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-navigator**](https://github.com/thanhdat77/herdr-navigator)<br><sub>thanhdat77</sub> | 通过一个模糊导航器跳转到任意 Herdr 工作区、Agent、项目、会话、远程连接、目录或操作 | `fuzzy-finder` `rust` `terminal` `workspace-manager` | 157 | 2026-08-25 |
| [**termscope**](https://github.com/iurysza/termscope)<br><sub>iurysza</sub> | 在分屏中打开终端屏幕上已经可见的文件和链接 | `python` `television` `terminal` `tmux` | 54 | 🔄 2026-09-16 |
| [**herdr-sessionizer**](https://github.com/andrewchng/herdr-sessionizer)<br><sub>andrewchng</sub> | 通过模糊搜索打开项目和工作树，再从声明式 TOML 布局（标签页、窗格分割、命令、按仓库覆盖配置）启动工作区 | `bun` `fuzzy-finder` `fzf` `git-worktree` `sessionizer` | 47 | 🔄 2026-09-14 |
| [**herdr-plugin-sesh**](https://github.com/fullerzz/herdr-plugin-sesh)<br><sub>fullerzz</sub> | 面向 Herdr 的 Sesh 风格工作区选择器 TUI，集成 zoxide，可从常用目录创建工作区 | `bubbletea` `sesh` `tui` `zoxide` `go` | 43 | 🔄 2026-09-20 |
| [**herdr-bar**](https://github.com/jeffarese/herdr-bar)<br><sub>jeffarese</sub> | Cmd+K and auto tab title for herdr: fuzzy-jump to any tab, agent, repo or branch. | `command-bar` `fuzzy-finder` `python` `terminal` `tui` | 40 | 🔄 2026-09-20 |
| [**herdr-command-palette**](https://github.com/JanTvrdik/herdr-command-palette)<br><sub>JanTvrdik</sub> | herdr 的 fzf 命令面板——模糊选择并运行任意插件操作 | `shell` | 38 | 2026-06-29 |
| [**herdr-drovr**](https://github.com/AVGVSTVS96/herdr-drovr)<br><sub>AVGVSTVS96</sub> | 轻松移动 herdr 窗格和标签页 | `fzf` `terminal` `javascript` | 18 | 2026-08-08 |
| [**herdr-zoxide**](https://github.com/den-tanui/herdr-zoxide)<br><sub>den-tanui</sub> | 从 zoxide 记录的目录创建工作区、标签页和窗格的 Herdr 插件 | `zoxide` `shell` | 11 | 2026-07-25 |
| [**herdr-palette**](https://github.com/vjeantet/herdr-palette)<br><sub>vjeantet</sub> | Sublime Text / VS Code 风格的 herdr 命令面板——内置操作、插件动作和你自己的命令，全部藏在一个按键之后 | `command-palette` `fuzzy-search` `terminal` `tui` `rust` | 11 | 🔄 2026-09-10 |
| [**🆕 herdr-omni**](https://github.com/mmjang/herdr-omni)<br><sub>mmjang</sub> | One search for Herdr workspaces, actions, and live or saved Codex & Claude sessions. Fuzzy-find by name, search conversation content, and resume where you left… | `claude-code` `codex` `opencode` `typescript` | 9 | 🔄 2026-09-20 |
| [**herdr-palette**](https://github.com/ramarivera/herdr-palette)<br><sub>ramarivera</sub> | 面向 Herdr 工作区的 Rust/Ratatui 模糊命令面板 | `command-palette` `ratatui` `rust` `terminal` `tui` | 9 | 🔄 2026-09-11 |
| [**herdr-quick-actions**](https://github.com/enekos/herdr-quick-actions)<br><sub>enekos</sub> | 以 fzf 选择器调用 herdr 原生的标签页/窗格/工作区操作，按使用频率排序——不必再死记快捷键 | `shell` | 8 | 2026-08-05 |
| [**🆕 herdr-transcripts**](https://github.com/hxreborn/herdr-transcripts)<br><sub>hxreborn</sub> | Search your coding-agent sessions, past and live, by any word you remember, then jump to them or resume them | `claude-code` `codex` `coding-agents` `droid` `fzf` | 6 | 🔄 2026-09-20 |
| [**herdr-hunk**](https://github.com/JacquesvanWyk/herdr-hunk)<br><sub>JacquesvanWyk</sub> | herdr 中用于 Hunk 差异对比的交互式 fzf 选择器：支持提交、范围、stash，并可在 Agent 完成时自动打开 | `fzf` `hunk` `shell` | 6 | 2026-07-12 |
| [**herdr-sessionizer**](https://github.com/salkhalil/herdr-sessionizer)<br><sub>salkhalil</sub> | herdr 的 tmux-sessionizer：用 fzf 搜索已打开的工作区和 zoxide 目录，创建或聚焦并附带模板标签页 | `shell` | 6 | 2026-07-27 |
| [**herdr-palette**](https://github.com/cesarferreira/herdr-palette)<br><sub>cesarferreira</sub> | 面向 Herdr 的弹窗式命令面板 | `typescript` | 5 | 🔄 2026-09-08 |
| [**herdr-switchboard**](https://github.com/crafts69guy/herdr-switchboard)<br><sub>crafts69guy</sub> | herdr 插件：在一个 Rust 编写的 TUI 中模糊切换运行中的 Agent、已打开的工作区和 ghq 管理的仓库——并可将仓库在新工作区、标签页、分屏或当前窗格中打开 | `developer-tools` `ghq` `ratatui` `rust` `terminal` | 5 | 🔄 2026-09-18 |
| [**herdr-ssh-manager**](https://github.com/jorge07RD/herdr-ssh-manager)<br><sub>jorge07RD</sub> | 保存 SSH 主机，并从 Herdr 内的模糊弹窗中重新连接——按 Enter 即可直接将弹窗内容交给 ssh | `rust` `ssh` `terminal` `tui` | 5 | 2026-08-24 |
| [**herdr-kiosk**](https://github.com/thomasschafer/herdr-kiosk)<br><sub>thomasschafer</sub> | 模糊查找 Git 仓库和分支，并在 Herdr 中作为工作树打开 | `rust` | 5 | 🔄 2026-09-17 |
| [**herdr-cast**](https://github.com/aliou/herdr-cast)<br><sub>aliou</sub> | 个人 Herdr 插件——提供原生 macOS Agent 通知、模糊工作区导航、基于 zoxide 的工作区创建以及布局命令 | `developer-tools` `macos` `notifications` `ratatui` `rust` | 4 | 🔄 2026-09-20 |
| [**herdr-pickr**](https://github.com/javoscript/herdr-pickr)<br><sub>javoscript</sub> | YAP！又一个面向 Herdr 多路复用器的选择器。 | `fzf` `lua` | 4 | 🔄 2026-09-14 |
| [**herdr-pane-navigator**](https://github.com/mr04vv/herdr-pane-navigator)<br><sub>mr04vv</sub> | 将 Herdr 的工作区、标签页和窗格作为一棵模糊树进行导航——以每个窗格实际在做什么为线索 | `coding-agents` `fzf` `terminal` `tui` `shell` | 4 | 🔄 2026-09-07 |
| [**herdr-keymap**](https://github.com/The-Dave-Stack/herdr-keymap)<br><sub>The-Dave-Stack</sub> | herdr 插件：在浮层面板中展示所有快捷键，并可直接运行有对应 CLI 命令的那些 | `typescript` | 4 | 2026-08-12 |
| [**herdr-configurable-picker**](https://github.com/yoshiori/herdr-configurable-picker)<br><sub>yoshiori</sub> | 面向 herdr 的树形跳转选择器，快捷键完全可配置 | `rust` | 4 | 2026-07-05 |
| [**herdr-grep-nvim**](https://github.com/cinco/herdr-grep-nvim)<br><sub>cinco</sub> | herdr 插件：用 fzf + ripgrep 进行实时搜索，并在你工作区旁边的分屏中用 nvim 打开匹配结果 | `shell` | 3 | 2026-07-17 |
| [**herdr-spotify**](https://github.com/iikjl/herdr-spotify)<br><sub>iikjl</sub> | herdr 的 Spotify 正在播放浮层插件——专辑封面、播放控制，并可通过 Spotify Web API 搜索/加入队列/点赞 | `spotify` `terminal` `go` | 3 | 2026-07-07 |
| [**herdr-workspacer**](https://github.com/mcuste/herdr-workspacer)<br><sub>mcuste</sub> | 使用 zoxide 查找项目，然后切换或创建 Herdr 工作区 | `rust` `tui` `zoxide` | 3 | 🔄 2026-09-16 |
| [**herdr-fzf-terminal-browser**](https://github.com/to4iki/herdr-fzf-terminal-browser)<br><sub>to4iki</sub> | 一个 herdr 插件：按下一个键，即可用 fzf 从当前窗格中选取一个 URL，并在 terminal-browser 中打开。 | `fzf` `rust` `terminal-browser` | 3 | 🔄 2026-09-12 |
| [**herdr-agent-recency**](https://github.com/ugurtarlig/herdr-agent-recency)<br><sub>ugurtarlig</sub> | 支持主题的 Herdr 选择器，按 Codex 和 Claude 有意义的活动情况排序 | `claude-code` `codex` `fzf` `python` | 3 | 2026-07-17 |
| [**herdr-openr**](https://github.com/wraithyy/herdr-openr)<br><sub>wraithyy</sub> | herdr 插件：模糊查找并打开终端或 AI Agent 刚提到的文件/URL——在 Claude 窗格中会读取会话记录 | `shell` | 3 | 2026-08-14 |
| [**herdr-command-palette**](https://github.com/alon-z/herdr-command-palette)<br><sub>alon-z</sub> | Herdr 插件：模糊搜索工作区/目录的命令面板 | `javascript` | 2 | 2026-06-22 |
| [**herdr-launcher**](https://github.com/arjenblokzijl/herdr-launcher)<br><sub>arjenblokzijl</sub> | 模糊选择一个声明式 TOML 工作流，填写表单，在新的 herdr 空间中启动编程 Agent | `launcher` `ratatui` `rust` `tui` | 2 | 2026-07-10 |
| [**herdr-palette**](https://github.com/Binb1/herdr-palette)<br><sub>Binb1</sub> | Herdr 的命令面板。可跳转到工作区和 Agent，运行插件动作，也可执行 Herdr 命令。 | `go` | 2 | 2026-09-03 |
| [**herdr-workspace-save**](https://github.com/chandrasekharan98/herdr-workspace-save)<br><sub>chandrasekharan98</sub> | 保存 Herdr 工作区（布局、工作目录、Agent 会话、正在运行的命令），之后可从 fzf 选择器中重新打开 | `claude-code` `terminal` `tmux` `python` | 2 | 2026-08-19 |
| [**herdr-sesh-bro**](https://github.com/cyperx84/herdr-sesh-bro)<br><sub>cyperx84</sub> | 面向 Herdr 的 sesh 风格模糊会话选择器——将工作区、Agent 和 zoxide 目录整合到一个带实时预览的 fzf 弹窗中 | `go` | 2 | 🔄 2026-09-19 |
| [**herdr-simple-switcher**](https://github.com/haphamdev/herdr-simple-switcher)<br><sub>haphamdev</sub> | 对工作区、标签页和 AI Agent 进行模糊搜索 | `shell` | 2 | 2026-08-01 |
| [**herdr-command-palette**](https://github.com/hota911/herdr-command-palette)<br><sub>hota911</sub> | 面向 herdr 内置操作（工作区、标签页、窗格、Agent）的 fzf 命令面板 | `command-palette` `fzf` `shell` | 2 | 2026-08-16 |
| [**herdr-workspace-launcher**](https://github.com/ImArtisann/herdr-workspace-launcher)<br><sub>ImArtisann</sub> | 面向 macOS 的 Herdr 插件，通过可搜索的键盘驱动目录选择器快速创建聚焦工作区 | `typescript` | 2 | 2026-07-16 |
| [**herdr-recent-workspaces**](https://github.com/ismaelosuna7824/herdr-recent-workspaces)<br><sub>ismaelosuna7824</sub> | Herdr 的「打开最近使用的文件夹」——可模糊筛选你曾作为工作区打开过的文件夹列表。选择一个即可打开或重新聚焦该工作区，也可浏览文件系统打开新的 | `go` | 2 | 2026-07-10 |
| [**herdr-ghq-open-agent**](https://github.com/kenchan/herdr-ghq-open-agent)<br><sub>kenchan</sub> | herdr 插件：用 fzf 对 ghq 管理的仓库进行增量搜索，在工作区/标签页中打开所选仓库并启动 claude | `fzf` `ghq` `shell` | 2 | 2026-08-03 |
| [**🆕 herdr-commander**](https://github.com/lurepos/herdr-commander)<br><sub>lurepos</sub> | Fast palette to discover/launch npm, cargo, .vscode tasks and commands from herdr | `rust` | 2 | 🔄 2026-09-20 |
| [**herdr-keybind-search**](https://github.com/malone-c/herdr-keybind-search)<br><sub>malone-c</sub> | herdr 的可搜索快捷键浮层（基于 fzf）。按下一个键即可模糊搜索你的快捷键 | `shell` | 2 | 2026-07-15 |
| [**🆕 herdr-target-picker**](https://github.com/navishachiku/herdr-target-picker)<br><sub>navishachiku</sub> | Pick a Herdr space, tab, or pane and type its id into the agent you were talking to | `typescript` | 2 | 🔄 2026-09-19 |
| [**🆕 herdr-plugin-picker**](https://github.com/purehate/herdr-plugin-picker)<br><sub>purehate</sub> | Herdr 的浮动弹窗选择器——可跳转到任意空间、Agent、标签页或窗格，向所有标记窗格广播同一条命令，并从 ~/.ssh/config 发起带实时可达性检测的 SSH 连接。完全由键盘驱动。 | `broadcast` `fuzzy-finder` `golang` `picker` `ssh` | 2 | 🔄 2026-09-18 |
| [**herdr-flash-picker**](https://github.com/TinyWhite1997/herdr-flash-picker)<br><sub>TinyWhite1997</sub> | 为 Herdr 提供的快速窗格选择器，采用对齐的一到两字母跳转标签。 | `rust` `tui` | 2 | 🔄 2026-09-07 |
| [**herdr-waypoint**](https://github.com/wraithyy/herdr-waypoint)<br><sub>wraithyy</sub> | 为文件夹命名并保存，从模糊列表中选一个，作为新的 herdr 工作区打开 | `shell` | 2 | 2026-08-12 |
| [**herdr-sessionizer**](https://github.com/42lizard/herdr-sessionizer)<br><sub>42lizard</sub> | tmux-sessionizer 风格的 herdr 插件 | `fzf` `shell` | 1 | 2026-08-28 |
| [**herdr-url-picker**](https://github.com/abrose/herdr-url-picker)<br><sub>abrose</sub> | herdr 插件：用 fzf 选取当前窗格中显示的 URL，并用默认浏览器打开 | `shell` | 1 | 2026-07-22 |
| [**herdr-jump**](https://github.com/agustinvalencia/herdr-jump)<br><sub>agustinvalencia</sub> | 为 herdr 空间和 Agent 分别提供的浮层选择器——跳转到任意工作区或 Agent，并以颜色实时显示状态 | `go` | 1 | 2026-07-24 |
| [**herdr-command-palette**](https://github.com/barnuri/herdr-command-palette)<br><sub>barnuri</sub> | 面向 herdr 的 F1 风格命令面板——可模糊搜索并运行所有已安装插件的全部操作，零依赖 | `command-palette` `terminal` `javascript` | 1 | 2026-09-01 |
| [**helm.herdr**](https://github.com/black-atom-industries/helm.herdr)<br><sub>black-atom-industries</sub> | 通过一个模糊导航器跳转到任意 Herdr 工作区、Agent、项目、会话、远程连接、目录或操作 | `rust` | 1 | 2026-09-03 |
| [**herdr-url-picker**](https://github.com/chouxcreams/herdr-url-picker)<br><sub>chouxcreams</sub> | Herdr 插件：从聚焦窗格中选取一个 URL 并在浏览器中打开 | `shell` | 1 | 2026-07-22 |
| [**herdr-spotify**](https://github.com/DeepRuparel/herdr-spotify)<br><sub>DeepRuparel</sub> | 面向 Herdr 的 Spotify 集成——Go 编写，提供零配置的本地控制，并通过 PKCE 授权支持搜索/加入队列/保存 | `spotify` `go` | 1 | 2026-08-28 |
| [**herdr-agents**](https://github.com/dleen/herdr-agents)<br><sub>dleen</sub> | 面向 herdr 的 fzf Agent 选择器——列出所有 Agent 窗格并按最需处理优先排序，支持会话预览和一键启动 | `coding-agents` `fzf` `python` `terminal` | 1 | 2026-08-20 |
| [**🆕 herdr-hosts**](https://github.com/ecylmz/herdr-hosts)<br><sub>ecylmz</sub> | Hierarchical SSH host picker for Herdr, with folders and notes straight from ~/.ssh/config | `ratatui` `rust` `ssh` `terminal` `tui` | 1 | 🔄 2026-09-18 |
| [**herdr-plugin-command-palette**](https://github.com/haisi/herdr-plugin-command-palette)<br><sub>haisi</sub> | 基于 fzf、支持模糊搜索的 herdr 命令面板 | `fzf` `python` | 1 | 2026-08-17 |
| [**herdr-turbo-palette**](https://github.com/jackfrancisdalton/herdr-turbo-palette)<br><sub>jackfrancisdalton</sub> | 模糊查找任意 Herdr space、标签页、Agent 或窗格，并直接跳转过去 | `python` | 1 | 2026-08-22 |
| [**herdr-keys**](https://github.com/JacquesvanWyk/herdr-keys)<br><sub>JacquesvanWyk</sub> | 面向 herdr 的可模糊搜索快捷键速查表（支持功能包、发现和个人自定义覆盖） | `shell` | 1 | 2026-07-12 |
| [**herdr-open-editor**](https://github.com/jimididit/herdr-open-editor)<br><sub>jimididit</sub> | 用 fzf 模糊搜索并选择文件，然后在你配置的编辑器中打开。 | `herd` `text-editor` `tui` `shell` | 1 | 2026-09-03 |
| [**herdr-fzf-url**](https://github.com/kaar/herdr-fzf-url)<br><sub>kaar</sub> | 从 herdr 窗格的滚动记录中模糊查找并打开 URL——tmux-fzf-url 的 herdr 移植版 | `shell` | 1 | 2026-07-29 |
| [**🆕 herdr-nav**](https://github.com/karanpatel1993/herdr-nav)<br><sub>karanpatel1993</sub> | File navigation, code search and jdb debugging inside herdr — fzf, ripgrep and a Java debugger wired into your terminal workspace | `shell` | 1 | 🔄 2026-09-17 |
| [**herdr-hint**](https://github.com/maedana/herdr-hint)<br><sub>maedana</sub> | Herdr 的 Vimium 风格提示标签——按键后在标签页和 Agent 上显示标签，再按标签即可跳转 | `rust` | 1 | 2026-08-11 |
| [**herdr-shortcut**](https://github.com/matheus3301/herdr-shortcut)<br><sub>matheus3301</sub> | 面向 Herdr 的快捷任务选择器兼编程 Agent 启动器 | `bubbletea` `claude-code` `codex` `coding-agents` `developer-tools` | 1 | 2026-07-24 |
| [**herdr-pickers**](https://github.com/sagmans/herdr-pickers)<br><sub>sagmans</sub> | 为 Agent、worktree、工作区和项目提供多种自定义的弹出式选择器。 | `typescript` | 1 | 🔄 2026-09-10 |
| [**herdr-jump**](https://github.com/solidsnakedev/herdr-jump)<br><sub>solidsnakedev</sub> | 为 herdr 提供工作区、窗格与标签页的模糊搜索选择器，外加一个切换到上一个工作区的开关。 | `shell` | 1 | 2026-09-01 |
| [**herdr-pane-picker**](https://github.com/ugurtarlig/herdr-pane-picker)<br><sub>ugurtarlig</sub> | 输入窗格上显示的字符提示来选择 Herdr 窗格 | `terminal` `wezterm` `python` | 1 | 2026-07-17 |
| [**herdr-palette**](https://github.com/vika2603/herdr-palette)<br><sub>vika2603</sub> | 为 herdr 打造的命令面板：一个弹窗即可搜索 herdr 的命令、所有已安装插件的操作、你自定义的命令，以及会话中打开的一切内容，并执行你选中的项目。 | `bubbletea` `command-palette` `fzf` `go` `terminal` | 1 | 🔄 2026-09-13 |
| [**herdr-bitwarden**](https://github.com/WillowMist/herdr-bitwarden)<br><sub>WillowMist</sub> | 模糊搜索你的 Bitwarden 密码库并粘贴/复制凭据——tmux-bitwarden 的 herdr 移植版 | `bitwarden` `fzf` `terminal` `tmux` `shell` | 1 | 2026-08-11 |
| [**herdr-fzf-url**](https://github.com/x0d7x/herdr-fzf-url)<br><sub>x0d7x</sub> | 扫描 herdr 终端窗格中的 URL，并用 fzf 交互式选取一个 | `fzf` `go` `url` | 1 | 2026-06-26 |
| [**herdr-open-local-paths**](https://github.com/yigitkg/herdr-open-local-paths)<br><sub>yigitkg</sub> | 检测本地路径，并通过简易选择器在 Windows、Linux 和 WSL 上打开或显示的 Herdr 插件 | `developer-tools` `python` `terminal` `wsl` | 1 | 2026-07-28 |
| [**herdr-agents-picker**](https://github.com/yxhta/herdr-agents-picker)<br><sub>yxhta</sub> | Herdr 插件：类似工作区选择器的 Agent 窗格模糊选择器，带实时窗格预览（Rust + ratatui 编写） | `rust` | 1 | 🔄 2026-09-08 |
| [**herdr-telescope**](https://github.com/zackshen/herdr-telescope)<br><sub>zackshen</sub> | 面向 herdr 的 fzf 命令 telescope——支持原生操作、插件操作、文件查找（@）和实时 ripgrep 搜索（/） | `fzf` `rust` | 1 | 2026-08-20 |
| [**herdr-iris**](https://github.com/a-curious-coder/herdr-iris)<br><sub>a-curious-coder</sub> | Iris——herdr 插件：针对窗格中检测到的 Agent，提供 AI Agent 技能的模糊搜索速查表 | `shell` | 0 | 2026-08-07 |
| [**herdr-project-manager**](https://github.com/barnuri/herdr-project-manager)<br><sub>barnuri</sub> | 面向 herdr 的项目管理插件——支持 glob/手动项目发现、模糊选择器，并可作为标签页或工作区打开 | `javascript` | 0 | 2026-08-25 |
| [**🆕 open-project**](https://github.com/benbrackenbury/open-project)<br><sub>benbrackenbury</sub> | Herdr 插件：模糊搜索选择一个项目，并将其作为工作区打开。 | `shell` | 0 | 🔄 2026-09-08 |
| [**herdr-locksmith**](https://github.com/bkarpinos/herdr-locksmith)<br><sub>bkarpinos</sub> | 面向 herdr 的快捷键命令面板 | `go` | 0 | 2026-09-01 |
| [**herdr-opencode-sessions**](https://github.com/damianpoole/herdr-opencode-sessions)<br><sub>damianpoole</sub> | 可按标题、项目、路径、日期或会话记录内容对过去的 OpenCode 会话进行模糊搜索的 Herdr 插件——带会话预览，并提供在当前或新工作区中恢复/分叉会话的快捷方式 | `typescript` | 0 | 2026-08-14 |
| [**🆕 herdr-pane-mover**](https://github.com/dimitri4d/herdr-pane-mover)<br><sub>dimitri4d</sub> | 通过对键盘和鼠标都友好的目标选择器，在标签页和工作区之间移动正在运行的 Herdr 窗格。 | `go` | 0 | 🔄 2026-09-13 |
| [**🆕 herdr-rbw**](https://github.com/ibanks42/herdr-rbw)<br><sub>ibanks42</sub> | 在 herdr 中模糊搜索你的 Bitwarden 密码库，并粘贴/复制凭据——rbw 版本。 | `shell` | 0 | 🔄 2026-09-14 |
| [**herdr-control-panel**](https://github.com/iskwyuki/herdr-control-panel)<br><sub>iskwyuki</sub> | 一个快捷键、一个面板操控 herdr——从历史记录或任意路径打开工作区，还可添加自定义操作。纯 bash + fzf 实现，无需构建 | `bash` `fzf` `terminal` `shell` | 0 | 2026-08-11 |
| [**🆕 herdr-repo-picker**](https://github.com/mayaton/herdr-repo-picker)<br><sub>mayaton</sub> | A herdr plugin that opens an overlay pane to fuzzy-pick a ghq repository and jump to its workspace. | `fuzzy-finder` `ghq` `ratatui` `rust` `tui` | 0 | 🔄 2026-09-17 |
| [**🆕 mux-prompter**](https://github.com/phine-apps/mux-prompter)<br><sub>phine-apps</sub> | 模糊选取上下文相关的提示词，并注入到 Herdr 或 tmux 窗格中 | `fzf` `prompt-engineering` `terminal-multiplexer` `tmux` `tmux-plugin` | 0 | 🔄 2026-09-13 |
| [**herdr-repo-picker**](https://github.com/princejoogie/herdr-repo-picker)<br><sub>princejoogie</sub> | 通过 OpenTUI 选择器，将 Git 仓库作为 Herdr 工作区打开 | `git` `opentui` `typescript` | 0 | 2026-08-17 |
| [**🆕 herdr-claude-profile**](https://github.com/quinnjr/herdr-claude-profile)<br><sub>quinnjr</sub> | herdr 插件：通过浮层面板切换和管理 claude-profile 的配置 | `typescript` | 0 | 🔄 2026-09-11 |
| [**herdr-file-picker**](https://github.com/shivammehta25/herdr-file-picker)<br><sub>shivammehta25</sub> | 将 tmux-file-picker 移植到 herdr 的「vibe coding」作品 | `shell` | 0 | 2026-07-29 |
| [**🆕 herdr-atuin-plugin**](https://github.com/smanickam01/herdr-atuin-plugin)<br><sub>smanickam01</sub> | 在 herdr 弹窗中搜索 Atuin 的 shell 历史记录——按 prefix+a，Enter 执行、Tab 编辑。安装后自动绑定快捷键 | `atuin` `macos` `shell-history` `terminal` `zsh` | 0 | 2026-08-17 |
| [**🆕 herdr-hop**](https://github.com/utahta/herdr-hop)<br><sub>utahta</sub> | herdr 插件：通过一个弹窗即可跳转到仓库、worktree 或工作区。 | `git-worktree` `go` `terminal` `tui` | 0 | 🔄 2026-09-16 |
| [**herdr-fzf-url**](https://github.com/willian/herdr-fzf-url)<br><sub>willian</sub> | 用 `fzf` 从聚焦窗格中选取 URL，然后打开或复制 | `fzf` `shell` | 0 | 2026-07-28 |

<details><summary>与此目的也相关</summary>

- [ThorstenRhau/token](https://github.com/ThorstenRhau/token) — Neovim 配色方案，并附带面向整个终端环境的社区贡献主题。
- [beyondlex/herdr-recent-navigator](https://github.com/beyondlex/herdr-recent-navigator) — 在最近使用的工作区、标签页、窗格和 Agent 之间进行 MRU（最近使用）切换——类似 JetBrains 的「最近文件」。此外还支持对任意窗格内容进行模糊搜索，完全由键盘驱动。
- [JacquesvanWyk/herdr-linear](https://github.com/JacquesvanWyk/herdr-linear) — 在 herdr 分屏窗格或标签页中运行的 fzf 驱动 Linear 面板：搜索 issue、深入项目、创建 issue、修改状态
- [hamzahraihan/herdr-better-workspace](https://github.com/hamzahraihan/herdr-better-workspace) — 面向 herdr（AI 编码 Agent 的终端工作区管理器）的交互式「打开工作区」选择器插件。
- [42lizard/herdr-dwm-layout](https://github.com/42lizard/herdr-dwm-layout) — 面向 Herdr 的 DWM 风格 master/stack 布局
- [adamwangxx/herdr-codex-resume](https://github.com/adamwangxx/herdr-codex-resume) — 在保留 Herdr 实时上下文的新分屏中打开原生的 Codex resume 选择器

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-automation"></a>

## 自动化、钩子与定时任务

> 想在创建工作树或指定时机自动运行固定的操作步骤

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-browser**](https://github.com/ogulcancelik/herdr-browser)<br><sub>ogulcancelik</sub> | 在 Herdr 窗格内渲染真实的 Chromium 视图，并通过 CDP 进行操控 | `browser` `browser-automation` `cdp` `chromium` `kitty-graphics` | 352 | 2026-08-22 |
| [**herdr-auto-title**](https://github.com/kryptamine/herdr-auto-title)<br><sub>kryptamine</sub> | 自动跟随每个标签页中工作内容变化的标签标题。借助 Herdr 让标签页保持整洁，一眼就知道自己在做什么。 | `go` | 180 | 🔄 2026-09-20 |
| [**herdr-automatic-rename**](https://github.com/qu8n/herdr-automatic-rename)<br><sub>qu8n</sub> | 智能的 herdr 标签页名称，帮助你更快地在 Agent 与 shell 之间切换。 | `shell` | 147 | 🔄 2026-09-14 |
| [**herdr-auto-title**](https://github.com/sh1ma/herdr-auto-title)<br><sub>sh1ma</sub> | 根据 Claude Code 和 Codex 的对话内容，自动生成 herdr 标签页标题 | `claude-code` `codex` `python` | 51 | 🔄 2026-09-11 |
| [**zed-herdr**](https://github.com/ImArtisann/zed-herdr)<br><sub>ImArtisann</sub> | 自动将当前活动的 HerdR 工作区与已有的 Zed 会话保持同步 | `typescript` | 27 | 2026-08-17 |
| [**herdr-worktree-setup**](https://github.com/tdi/herdr-worktree-setup)<br><sub>tdi</sub> | herdr 插件：创建工作树时执行按项目定制的初始化步骤（从 main 复制 .env、mise trust、direnv allow、安装依赖等） | `javascript` | 26 | 🔄 2026-09-11 |
| [**herdr-auto-pilot**](https://github.com/0xGosu/herdr-auto-pilot)<br><sub>0xGosu</sub> | 通过 Herdr API 代替你自动向运行中的 AI 编程 CLI 发送提示词的 Herdr 插件。插件具有从你的操作中学习的训练模式，并内置防止危险/恶意操作的防护机制。经过充分训练后，可让它以「完全自主提示（FSP）」模式运行 | `go` | 24 | 🔄 2026-09-20 |
| [**herdr-workflows**](https://github.com/aorumbayev/herdr-workflows)<br><sub>aorumbayev</sub> | 为 herdr 中的重复步骤提供声明式自动化 | `agentic-ai` `agentic-workflow` `agents` `ai` `claude` | 22 | 🔄 2026-09-08 |
| [**herdr-routines**](https://github.com/mrcndz/herdr-routines)<br><sub>mrcndz</sub> | 运行定时任务的 Herdr 插件：按 cron 或固定间隔在工作区中打开标签页，运行命令或启动 Agent | `python` | 11 | 2026-07-18 |
| [**herdr-updater**](https://github.com/diegopzz/herdr-updater)<br><sub>diegopzz</sub> | 在整个机群范围内安全地让 Herdr 本体及其插件保持最新 | `rust` `updater` | 9 | 🔄 2026-09-17 |
| [**herdr-automations**](https://github.com/DnzzL/herdr-automations)<br><sub>DnzzL</sub> | 在终端中运行、面向编程 Agent 的定时任务，基于 Herdr。每次运行都会准备一条提示词、一行 cron 和一个全新的 git 工作树。仅需一个 YAML 文件，无需存储、提供预编译二进制、可按自动化单独指定模型、支持睡眠后补跑，并附带实时看板 | `ai-agents` `automation` `claude-code` `coding-agents` `cron` | 9 | 🔄 2026-09-14 |
| [**herdr-tab-title**](https://github.com/aarsh21/herdr-tab-title)<br><sub>aarsh21</sub> | 为 Herdr 提供类似 tmux 的自动标签页标题 | `rust` `terminal` `tmux` | 8 | 2026-07-08 |
| [**bermuda**](https://github.com/bon5co/bermuda)<br><sub>bon5co</sub> | 在 herdr 上由 Claude Code 驱动的编排——Agent 无法跳过的流程、定时任务、带 claim 的线程，以及供 Agent 日后检索的论坛 | `agent-orchestration` `agents` `ai-agents` `automation` `claude-code` | 8 | 🔄 2026-09-08 |
| [**herdr-agent-config-manager**](https://github.com/Phoobobo/herdr-agent-config-manager)<br><sub>Phoobobo</sub> | 混合 CLI + Herdr 插件，用于检测并集中管理 Agent 的 skill、MCP、插件和 hook | `python` | 8 | 🔄 2026-09-06 |
| [**herdr-shepherd**](https://github.com/mikedclarke/herdr-shepherd)<br><sub>mikedclarke</sub> | 面向 herdr 的定时 Agent 会话——将心跳检测、cron 例程和脚本作为可见的 herdr 工作区启动 | `coding-agents` `cron` `go` `scheduler` `tui` | 6 | 🔄 2026-09-13 |
| [**herdr-pane-balancer**](https://github.com/jeph/herdr-pane-balancer)<br><sub>jeph</sub> | 在窗格创建、关闭和退出时，自动均衡、均分并平铺 Herdr 终端窗格 | `python` | 5 | 2026-08-02 |
| [**herdr-sched**](https://github.com/husniadil/herdr-sched)<br><sub>husniadil</sub> | 面向 Herdr 编程 Agent 的调度与触发器——cron 任务和 webhook/文件监视触发器会向相邻插件触发动作，每个动作都由其执行主体签名。全部由一个 Go 二进制程序实现 | `ai-agents` `cron` `mcp-server` `scheduler` `webhooks` | 4 | 2026-08-30 |
| [**herdr-fwd**](https://github.com/go-min/herdr-fwd)<br><sub>go-min</sub> | 为远程 Herdr 会话自动设置回环端口转发 | `port-forwarding` `ssh` `terminal` `rust` | 3 | 🔄 2026-09-09 |
| [**herdr-review-loop**](https://github.com/mikhail-angelov/herdr-review-loop)<br><sub>mikhail-angelov</sub> | 在 herdr 工作区中让 Agent 之间自动进行交叉评审——一个负责编写，另一个负责评审，如此反复 | `terminal` `go` | 3 | 🔄 2026-09-19 |
| [**herdr-autocontinue**](https://github.com/rcosteira79/herdr-autocontinue)<br><sub>rcosteira79</sub> | 监控 Agent 是否触及用量上限，以徽章形式显示重置倒计时（$wall），并在时间窗口重新开放后，向你预先设置的 Agent 重新发送提示词 | `python` | 3 | 🔄 2026-09-15 |
| [**herdr-labels**](https://github.com/Angel-O/herdr-labels)<br><sub>Angel-O</sub> | 在保留手动标签的同时，自动为标签页命名和编号的 Herdr 插件 | `rust` | 2 | 🔄 2026-09-20 |
| [**hermes-herdr-auto-reconcile**](https://github.com/chris-yyau/hermes-herdr-auto-reconcile)<br><sub>chris-yyau</sub> | 面向监视 Herdr 窗格的 Hermes 监督者的网关存活检测插件 | `automation` `hermes-agent` `multi-agent` `python` | 2 | 🔄 2026-09-16 |
| [**herdr-auto-update**](https://github.com/dio16/herdr-auto-update)<br><sub>dio16</sub> | herdr 插件：启动时检查已安装插件是否有更新的上游提交，如有则自动重新安装 | `rust` | 2 | 2026-08-16 |
| [**herdr-js-worktree-bootstrap**](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap)<br><sub>LeonardoTrapani</sub> | 为 JavaScript 和 TypeScript 自动初始化 Herdr 工作树，支持基于锁文件的安装和安全的环境变量还原 | `automation` `bun` `developer-tools` `git-worktree` `javascript` | 2 | 2026-07-15 |
| [**herdr-plugin**](https://github.com/ppggff/herdr-plugin)<br><sub>ppggff</sub> | 自动记住并恢复每个 Herdr 窗格对应的正确 macOS 输入法（IME） | `ime` `input-method` `macos` `python` | 2 | 2026-07-27 |
| [**herdr-triggers**](https://github.com/cantona/herdr-triggers)<br><sub>cantona</sub> | 常驻监听窗格输出并按正则表达式触发动作：自动登录等由正则驱动的终端触发器。 | `rust` `terminal` `terminal-based` `terminal-multiplexer` `trigger` | 1 | 🔄 2026-09-18 |
| [**🆕 herdr-auto-tab-name**](https://github.com/dev-shimada/herdr-auto-tab-name)<br><sub>dev-shimada</sub> | herdr 插件：根据当前目录自动命名标签页 | `javascript` | 1 | 🔄 2026-09-19 |
| [**herdr-routines**](https://github.com/guidodinello/herdr-routines)<br><sub>guidodinello</sub> | _(暂无描述)_ | `python` | 1 | 🔄 2026-09-19 |
| [**herdr-tab-autorun**](https://github.com/hanbong5938/herdr-tab-autorun)<br><sub>hanbong5938</sub> | 根据 TOML 规则，在每个新标签页中自动运行 shell 命令或启动编码 Agent 的 Herdr 插件。 | `ai-agents` `automation` `nodejs` `terminal` `javascript` | 1 | 🔄 2026-09-10 |
| [**say-hook**](https://github.com/HikaruEgashira/say-hook)<br><sub>HikaruEgashira</sub> | 使用 ElevenLabs 文字转语音朗读 Claude Code hook 事件的 macOS CLI | `typescript` | 1 | 🔄 2026-09-12 |
| [**🆕 herdr-cron**](https://github.com/huketo/herdr-cron)<br><sub>huketo</sub> | 为编码 Agent 安排自动化任务：在 Herdr 窗格中定时执行 shell 命令，或向编码 Agent 发送提示词。 | `agent-skills` `automation` `bubbletea` `cli` `coding-agent` | 1 | 🔄 2026-09-18 |
| [**herdr-worktree-cleanup**](https://github.com/poislagarde/herdr-worktree-cleanup)<br><sub>poislagarde</sub> | 当对应的 Herdr 空间关闭时，自动清理可安全删除的 GitHub PR worktree。Python 编写，无依赖，MIT 许可。 | `git-worktree` `python` | 1 | 🔄 2026-09-11 |
| [**🆕 herdr-automations**](https://github.com/ram4-dev/herdr-automations)<br><sub>ram4-dev</sub> | 面向 Herdr 的声明式 cron、间隔和事件自动化 | `automation` `bun` `typescript` | 1 | 2026-08-13 |
| [**herdr-callsigns**](https://github.com/reobin/herdr-callsigns)<br><sub>reobin</sub> | 为每个 herdr 窗格自动分配简短易记的呼号，让你和 Agent 都能用窗格名而非 ID 来指代它们。 | `shell` | 1 | 🔄 2026-09-14 |
| [**herdr-nixos-vm**](https://github.com/Slimydog21/herdr-nixos-vm)<br><sub>Slimydog21</sub> | 面向 herdr 的 NixOS 虚拟机窗格——启动、停止、监视 Hashimoto 风格的开发虚拟机，并可 ssh 连接。需要 nixos-vm kit | `shell` | 1 | 2026-08-18 |
| [**🆕 herdr-autoname**](https://github.com/thejiajun/herdr-autoname)<br><sub>thejiajun</sub> | 根据最近的 Agent 会话，自动为 Herdr 的工作区、标签页和窗格命名。 | `python` | 1 | 🔄 2026-09-18 |
| [**herdr-jump-number**](https://github.com/voice0726/herdr-jump-number)<br><sub>voice0726</sub> | 在不破坏 Herdr 自动工作区标签的前提下，在工作区和标签页上显示跳转键编号的 Herdr 插件。 | `typescript` | 1 | 🔄 2026-09-19 |
| [**herdr-agent-title-sync**](https://github.com/winoooops/herdr-agent-title-sync)<br><sub>winoooops</sub> | 为 Claude Code、Codex、Kimi Code、OpenCode 等编程 Agent 提供的 Herdr 窗格标题自动同步 | `developer-tools` `typescript` | 1 | 2026-08-20 |
| [**herdr-looper**](https://github.com/gurronen/herdr-looper)<br><sub>gurronen</sub> | 在全新的 Herdr 工作区和工作树中启动可重复运行的本机 Pi 任务 | `automation` `rust` `terminal` | 0 | 2026-08-26 |
| [**🆕 herdr-plugin-auto-rename**](https://github.com/khatriafaz/herdr-plugin-auto-rename)<br><sub>khatriafaz</sub> | 根据 Pi 会话的第一条提示词，自动重命名新的 Herdr 工作区和 Git 分支 | `typescript` | 0 | 🔄 2026-09-20 |
| [**herdr-unrecoverable**](https://github.com/neilwashere/herdr-unrecoverable)<br><sub>neilwashere</sub> | 从终端服务商错误中恢复 Pi 编程 Agent 会话的 Herdr 看门狗 | `pi-coding-agent` `javascript` | 0 | 2026-08-14 |
| [**herdr-kitchen-brigade**](https://github.com/Operator-create/herdr-kitchen-brigade)<br><sub>Operator-create</sub> | 在 Herdr 编码 Agent 完成任务时运行你的仓库检查。提供本地报告、简明的失败反馈，且零 Python 依赖。 | `ai-agents` `automation` `developer-tools` `python` `testing` | 0 | 🔄 2026-09-10 |
| [**herdr-worktreeinclude**](https://github.com/untalfranfernandez/herdr-worktreeinclude)<br><sub>untalfranfernandez</sub> | 为每个新建 git 工作树自动填充所需的、被 gitignore 忽略的本地文件（.env、settings.local.json、fixtures 等）的 Herdr 插件。只需在 .worktreeinclude 文件中用 gitignore 语法声明一次，Herdr 创建的每个工作树都会自动获得这些文件。实现了… | `claude-code` `dotenv` `git-worktree` `worktree` | 0 | 2026-07-29 |
| [**🆕 herdr-space-groups**](https://github.com/yojahny55/herdr-space-groups)<br><sub>yojahny55</sub> | herdr 插件：将 Space 分组为带名称、带颜色的组——支持选择器弹窗（鼠标+键盘）、侧边栏分组标题和自动排序 | `javascript` | 0 | 2026-08-29 |
| [**🆕 herdr-plugin-win-terminal**](https://github.com/yuloop/herdr-plugin-win-terminal)<br><sub>yuloop</sub> | Herdr 插件：一键安装 Windows Terminal 配置。 | `powershell` | 0 | 2026-09-04 |
| [**numberer-manager**](https://github.com/yuritada/numberer-manager)<br><sub>yuritada</sub> | 轻量级 Herdr 插件，自动在工作区和标签页标签前加上其在列表中的当前位置（例如「1: space」「1: tab」） | `python` | 0 | 2026-07-25 |
| [**🆕 herdr-pane-restart**](https://github.com/zap0xfce2/herdr-pane-restart)<br><sub>zap0xfce2</sub> | 在服务器启动时，于命名窗格中运行已配置的命令 | `python` | 0 | 🔄 2026-09-15 |

<details><summary>与此目的也相关</summary>

- [freethinkel/herdr-plugin-git-worktree-hooks](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks) — 在创建/移除 git 工作树时运行 shell 命令——一份 YAML 配置适用于所有项目，放在任何仓库之外
- [timofey-TK/herdr-worktree-hooks](https://github.com/timofey-TK/herdr-worktree-hooks) — herdr 插件：在创建、打开或删除 git 工作树时运行自定义的初始化/清理命令
- [miko-misa/herdr-portfwd](https://github.com/miko-misa/herdr-portfwd) — 面向远程机器上编程 Agent 的自动 SSH 端口转发——Ctrl+点击 Agent 打印的 localhost URL，即可在你本机以相同端口打开该页面。一个 Herdr 插件
- [itisbryan/herdr-gh-checks](https://github.com/itisbryan/herdr-gh-checks) — herdr 插件：在窗格中监视并查看当前 PR 的 CI，并在侧边栏行中显示 CI/合并状态。使用 Go + Bubble Tea 编写
- [ekropotin/herdr-tuicr](https://github.com/ekropotin/herdr-tuicr) — tuicr code review in a Herdr pane, with automatic handoff to the agent that opened it.
- [elkraps/herdr-telegram-notify](https://github.com/elkraps/herdr-telegram-notify) — 针对 Herdr Agent 状态变化的可自定义 Telegram 通知——支持状态过滤、模板、多聊天投递、去重、Codex 批准按钮、完成摘要和内置诊断
- [Newt6611/herdr-tab-title](https://github.com/Newt6611/herdr-tab-title) — Herdr Tab Title 会将 Herdr 标签页自动重命名为整洁的、按工作区独立编号的名称，如「1. Codex」「2. Terminal」，格式可自定义
- [piesuke/herdr-worktree-bootstrap](https://github.com/piesuke/herdr-worktree-bootstrap) — Bootstrap a new worktree: copy gitignored files, install deps, run hooks

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-session"></a>

## 会话保存与恢复

> 关闭工作后，希望之后能从同一状态继续

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-resurrect**](https://github.com/ntindle/herdr-resurrect)<br><sub>ntindle</sub> | herdr 的 tmux-resurrect——快照工作区、标签页、窗格、当前目录、运行中的程序和 Agent，并在崩溃或重启后恢复 | `crash-recovery` `session-manager` `terminal-multiplexer` `tmux-resurrect` `javascript` | 31 | 2026-08-24 |
| [**session-digger**](https://github.com/taxueseek/session-digger)<br><sub>taxueseek</sub> | 跨环境会话历史挖掘与知识管理。分析记录。支持 Claude/Grok/Kimi Code/Codex/WorkBuddy/Trae CN 等主流环境 | `claude-code` `conversation-analysis` `jsonl` `knowledge-management` `log-analysis` | 18 | 🔄 2026-09-20 |
| [**herdr-notes**](https://github.com/alexarthurs/herdr-notes)<br><sub>alexarthurs</sub> | 面向 herdr 的持久化 Markdown 笔记窗格——每个工作区一份笔记，支持预览渲染+编辑模式，自动保存且重启后仍保留 | `markdown` `notes` `ratatui` `rust` `terminal` | 15 | 2026-07-25 |
| [**herdr-claude-auto-retry**](https://github.com/mo-arvan/herdr-claude-auto-retry)<br><sub>mo-arvan</sub> | 等待 Anthropic 速率限制解除后自动恢复 Claude Code，herdr 原生实现：无需 tmux，无需 shell 包装 | `javascript` | 15 | 2026-09-03 |
| [**herdr-session-parker**](https://github.com/iviaxpow3r/herdr-session-parker)<br><sub>iviaxpow3r</sub> | 用于暂存窗格/标签页，并在之后恢复受支持的 Agent 会话的 Herdr 插件 | `agent-tools` `python` | 11 | 2026-07-03 |
| [**herdr-agent-inbox**](https://github.com/douglascorrea/herdr-agent-inbox)<br><sub>douglascorrea</sub> | herdr 编程 Agent 的收件箱——会话标题、已读/未读标记、运行时长、工作区汇总、可续接的聊天记录 | `ai-agents` `terminal` `python` | 9 | 2026-07-28 |
| [**herdr-assist**](https://github.com/walcew/herdr-assist)<br><sub>walcew</sub> | 面向 AI 编程 Agent 终端复用器 Herdr 的实体桌面面板——用颜色显示会话状态，当 Agent 停下来请求决策时会响铃提醒。基于 ESP32-S3 + LVGL，提供预编译固件 | `ai-agents` `claude-code` `coding-agents` `embedded` `esp-idf` | 8 | 2026-08-27 |
| [**sheep**](https://github.com/gokay-ai/sheep)<br><sub>gokay-ai</sub> | 面向 AI 编程 Agent 的撤销功能。Agent 的每一轮操作都会成为一个可恢复的检查点 | `ai-agents` `git` `llm` `rust` `tui` | 6 | 2026-08-28 |
| [**herdr-oh-my-agent**](https://github.com/GavinTomlins/herdr-oh-my-agent)<br><sub>GavinTomlins</sub> | 将 oh-my-openagent 的每个子 Agent 委派实时镜像到独立的 Herdr 窗格或标签页——保留完整会话状态和滚动记录 | `typescript` | 5 | 2026-07-31 |
| [**herdr-hibernate**](https://github.com/bengemine/herdr-hibernate)<br><sub>bengemine</sub> | 让 Herdr 中空闲的编程 Agent 窗格（Claude Code、Codex、Grok）休眠——释放内存，按 Enter 即可恢复原会话 | `claude-code` `python` | 3 | 🔄 2026-09-10 |
| [**herdr-pane-id-labeler**](https://github.com/4Born/herdr-pane-id-labeler)<br><sub>4Born</sub> | 让窗格标签与如 w1:p2 之类的公开窗格 ID 保持同步的 Herdr 插件 | `developer-tools` `terminal` `javascript` | 2 | 2026-07-26 |
| [**herdr-synchronize-panes**](https://github.com/furuhashin/herdr-synchronize-panes)<br><sub>furuhashin</sub> | Herdr 插件：将一条命令广播到当前标签页内的所有窗格（类似 tmux 的 synchronize-panes） | `javascript` | 2 | 2026-07-14 |
| [**herdr_sync**](https://github.com/kamaaina/herdr_sync)<br><sub>kamaaina</sub> | 同步 herdr 中的窗格 | `zig` | 2 | 2026-07-01 |
| [**herdr-e2b**](https://github.com/tomasvarga/herdr-e2b)<br><sub>tomasvarga</sub> | 按需将 git 工作树镜像到全新的 E2B 云沙盒——直接上传快照（包括未提交的更改），无需 push 或 clone。一个 herdr 插件 | `cli` `cloud-dev` `e2b` `git-worktree` `sandbox` | 2 | 2026-07-18 |
| [**herdr-thread-to-tab**](https://github.com/toyamarinyon/herdr-thread-to-tab)<br><sub>toyamarinyon</sub> | 让单窗格 Herdr 标签页标签与 Claude Code 和 Codex 的线程标题保持同步 | `rust` | 2 | 2026-08-06 |
| [**herdr-stash**](https://github.com/victor-software-house/herdr-stash)<br><sub>victor-software-house</sub> | 储藏 Herdr 工作区——停止其中的 Agent，同时保留其结构和对话内容，之后可从可点击的双栏弹窗中恢复 | `rust` `terminal` `tui` | 2 | 2026-07-29 |
| [**herdr-todos-windows**](https://github.com/aclima01/herdr-todos-windows)<br><sub>aclima01</sub> | 实时镜像 herdr Agent 任务列表（TaskCreate/TaskUpdate）的面板，方便你跟踪它的计划 | `powershell` | 1 | 2026-07-22 |
| [**🆕 herdr-agent-auto-naming**](https://github.com/azyu/herdr-agent-auto-naming)<br><sub>azyu</sub> | 一个 Herdr 插件，为检测到的每个 Agent 分配一个易读的双词名称，并作为窗格标签持久保存，重启后依然保留。 | `coding-agents` `developer-tools` `terminal` `python` | 1 | 🔄 2026-09-20 |
| [**🆕 herdr-revive**](https://github.com/cantona/herdr-revive)<br><sub>cantona</sub> | Restore Herdr commands, layouts and exact agent sessions with preview, named workspaces and explicit recovery. | `rust` `session-management` `terminal` `terminal-based` `terminal-multiplexer` | 1 | 🔄 2026-09-19 |
| [**mo-herdr**](https://github.com/momentohq/mo-herdr)<br><sub>momentohq</sub> | 在 herdr 窗格中运行 mo——支持 herdr 重启后的会话恢复、启动操作，以及 SIGKILL 清理 | `python` | 1 | 2026-09-02 |
| [**herdr-undo-close**](https://github.com/pedroloch/herdr-undo-close)<br><sub>pedroloch</sub> | 如浏览器的 Cmd+Shift+T 一样，在 herdr 中重新打开已关闭的标签页——恢复标签名、含比例的分屏结构、每个窗格的工作目录以及标签页位置 | `python` | 1 | 2026-07-30 |
| [**🆕 herdr-pane-reopen**](https://github.com/rchougule/herdr-pane-reopen)<br><sub>rchougule</sub> | herdr plugin: undo close — reopen the last closed pane, tab or workspace in place and resume its agent | `rust` | 1 | 🔄 2026-09-17 |
| [**attic**](https://github.com/TheThoughtagen/attic)<br><sub>TheThoughtagen</sub> | 自动关闭空闲的 AI 编程会话，但会先归档每一个，方便之后恢复 | `claude-code` `developer-tools` `python` `session-management` `tui` | 1 | 2026-08-14 |
| [**herdr-agent-pins**](https://github.com/ZingerLittleBee/herdr-agent-pins)<br><sub>ZingerLittleBee</sub> | 将 Herdr Agent 会话持久固定在 Agents 侧边栏顶部 | `terminal` `javascript` | 1 | 2026-08-24 |
| [**herdr-codex-resume**](https://github.com/adamwangxx/herdr-codex-resume)<br><sub>adamwangxx</sub> | 在保留 Herdr 实时上下文的新分屏中打开原生的 Codex resume 选择器 | `codex-cli` `terminal` `shell` | 0 | 2026-08-21 |
| [**herdr-session-title-name**](https://github.com/jovylle/herdr-session-title-name)<br><sub>jovylle</sub> | herdr 插件：将 terminal_title_stripped 持久化到标签页（顶部只保留 session_title，标签页关闭后依然保留该标题） | `sidebar` `terminal` `html` | 0 | 2026-08-28 |
| [**🆕 herdr-plugin-vault**](https://github.com/Joxtacy/herdr-plugin-vault)<br><sub>Joxtacy</sub> | 在 herdr 弹窗中浏览过去的 Claude Code 会话，并在新标签页中恢复所选的那个 | `shell` | 0 | 2026-08-11 |
| [**🆕 herdr-ccs**](https://github.com/KennethWKZ/herdr-ccs)<br><sub>KennethWKZ</sub> | 让 `ccs claude` 在 Herdr 中表现得如同原生 Claude Code——支持窗格检测，以及通过 ccs 实现的、感知启动方式的会话恢复 | `shell` | 0 | 2026-08-29 |
| [**resume-globally**](https://github.com/muscaiu/resume-globally)<br><sub>muscaiu</sub> | Herdr 插件：跨 Claude Code、Cursor 和 OpenCode 浏览并恢复最近的会话。 | `shell` | 0 | 🔄 2026-09-13 |
| [**herdr-layout**](https://github.com/noviadi/herdr-layout)<br><sub>noviadi</sub> | 保存并重放 Herdr 窗格布局——面向 Herdr 终端复用器的配套插件（tmux-resurrect 风格） | `cli` `terminal` `tmux-resurrect` `shell` | 0 | 2026-08-13 |
| [**🆕 herdr-tab-new**](https://github.com/softwarecrafts/herdr-tab-new)<br><sub>softwarecrafts</sub> | 在此项目的 herdr 工作区中恢复或启动一个 Agent 会话——既是 herdr 插件，也是可在 herdr 之外的终端使用的 CLI。 | `typescript` | 0 | 2026-08-31 |
| [**🆕 herdr-event-log**](https://github.com/waynewu411/herdr-event-log)<br><sub>waynewu411</sub> | herdr 插件：将 pane.agent_status_changed（以及未来的其他事件类型）记录到一份持久化、可从游标恢复的全局日志中，任何父 Agent 都可以 tail 它 | `shell` | 0 | 2026-08-24 |

<details><summary>与此目的也相关</summary>

- [nicosuave/memex](https://github.com/nicosuave/memex) — 搜索 Claude Code、Codex、Pi、OpenCode、GitHub Copilot 和 Cursor 的会话记录。恢复会话。追踪 token 使用
- [mmjang/herdr-omni](https://github.com/mmjang/herdr-omni) — One search for Herdr workspaces, actions, and live or saved Codex & Claude sessions. Fuzzy-find by name, sear…
- [afogel/shepherdr](https://github.com/afogel/shepherdr) — 将委派出去的编程 Agent 收拢到可见、可审查的 herdr 窗格中，供你观察、恢复和接管的 herdr 插件
- [hxreborn/herdr-transcripts](https://github.com/hxreborn/herdr-transcripts) — Search your coding-agent sessions, past and live, by any word you remember, then jump to them or resume them
- [AkashJana18/herdr-scratch](https://github.com/AkashJana18/herdr-scratch) — 面向 Herdr 的持久化速记板，为浮动实用窗格铺路
- [KokiKono/herdr-kanban](https://github.com/KokiKono/herdr-kanban) — 将任务与 herdr 标签页关联的终端看板，数据持久化在 SQLite 中
- [blaxel-ai/herdr-blaxel-sandbox-plugin](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin) — 从 Herdr 在持久化的 Blaxel Sandbox 中运行编程 Agent
- [voodootikigod/adlc-herdr](https://github.com/voodootikigod/adlc-herdr) — ADLC 的 herdr 插件——按窗格显示阶段/工单/关卡状态，附带待办看板、关卡操作和 adlc-fleet 运行可观测性。是 voodootikigod/adlc/plugins/adlc-herdr 的自动同步…
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
| [**herdr-tab-smart-rename**](https://github.com/iurysza/herdr-tab-smart-rename)<br><sub>iurysza</sub> | 为 Herdr 生成基于上下文的工作区和标签页名称 | `ai` `bun` `terminal` `typescript` | 77 | 🔄 2026-09-19 |
| [**herdr-flock**](https://github.com/ragamo/herdr-flock)<br><sub>ragamo</sub> | 将你的 AI 编程 Agent 可视化为生活在俯视视角农场里的像素风羊群的 herdr 插件 | `cli` `ratatui` `rust` `tui` | 38 | 2026-08-31 |
| [**herdr-window-title-sync**](https://github.com/rjyo/herdr-window-title-sync)<br><sub>rjyo</sub> | 将工作区、标签页和 Agent 会话同步到终端标题（可配合 Moshi 使用） | `moshi` `terminal-title` `javascript` | 36 | 2026-06-26 |
| [**herdr-pet**](https://github.com/nikok6/herdr-pet)<br><sub>nikok6</sub> | 生活在 herdr 窗格中的小小桌面宠物——陪你的 Agent 一起打字、等待和庆祝。兼容任意 Codex pet | `rust` | 11 | 2026-08-26 |
| [**herdr-icon-agent-ui**](https://github.com/qintmb/herdr-icon-agent-ui)<br><sub>qintmb</sub> | 在 Herdr 侧边栏中渲染纵向对齐的单色 Agent 图标。通过自定义字体渲染，字形按终端 cap-height 进行非均匀缩放，与 Agent 名称、标签页和工作区标签紧密贴合，而不是显示为小方块 | `python` | 10 | 🔄 2026-09-18 |
| [**herdr-theme-picker**](https://github.com/qintmb/herdr-theme-picker)<br><sub>qintmb</sub> | 基于终端配色方案和自定义设置的 herdr UI 主题选择器 | `shell` | 10 | 2026-08-31 |
| [**herdr-claude-session-title**](https://github.com/bcihanc/herdr-claude-session-title)<br><sub>bcihanc</sub> | Herdr 插件：将 Claude Code 的会话标题（/rename 或自动摘要）同步到 herdr 窗格的元数据标题中 | `shell` | 8 | 2026-07-11 |
| [**herdr-canvas**](https://github.com/aorumbayev/herdr-canvas)<br><sub>aorumbayev</sub> | 面向 herdr Agent 的鼠标驱动 ASCII 图表画布——在 TUI 中绘制，分享结构化 JSON，还可以让 AI 编辑它 | `agentic-ai` `agents` `ai-agents` `ascii-art` `bubbletea` | 7 | 2026-08-31 |
| [**herdr-pet**](https://github.com/allmight-ai/herdr-pet)<br><sub>allmight-ai</sub> | Herdr 的伴侣电子宠物——映射你的编程 Agent 的状态 | `companion` `rust` `v-pet` | 6 | 2026-08-20 |
| [**herdr-ghostty-tab-title**](https://github.com/wjarka/herdr-ghostty-tab-title)<br><sub>wjarka</sub> | herdr 插件：在 Ghostty 标签标题中按颜色显示 Agent 各状态（阻塞/完成/工作中/空闲）的数量 | `ai-agents` `ghostty` `terminal` `python` | 6 | 2026-08-04 |
| [**herdr-town**](https://github.com/Efeguclu1/herdr-town)<br><sub>Efeguclu1</sub> | 把你的 Herdr 编程 Agent 当作一座 8 位像素小镇来观赏。无需离开，就能阅读并回复它们 | `ai-agents` `pixel-art` `terminal` `tui` `javascript` | 5 | 2026-08-08 |
| [**herdr-agent-titler**](https://github.com/killerz3/herdr-agent-titler)<br><sub>killerz3</sub> | 无需外部 API key，使用本地的 agy、claude、codex 或 opencode 运行环境，自动为 Herdr 标签页设置标题。 | `antigravity` `claude-code` `python` | 5 | 2026-09-03 |
| [**herdr-in-your-face**](https://github.com/JYasha11/herdr-in-your-face)<br><sub>JYasha11</sub> | 如果你放着被阻塞的 AI Agent 不管，一个巨大的 ASCII 脸会对你怒吼。你无视得越久，警告就升级得越厉害 | `javascript` | 4 | 2026-07-10 |
| [**herdr-auto-namer**](https://github.com/kakigakki/herdr-auto-namer)<br><sub>kakigakki</sub> | herdr 的 ChatGPT 风格自动命名：Agent 使用其 Claude 会话标题，工作区使用其工作目录名 | `claude-code` `python` | 4 | 2026-08-27 |
| [**herdr-tab-rename**](https://github.com/lmilojevicc/herdr-tab-rename)<br><sub>lmilojevicc</sub> | 将每个 Herdr 标签页自动重命名为其聚焦窗格的工作目录名。手动重命名过的标签页不受影响 | `go` | 4 | 2026-07-31 |
| [**herdr-questmancer**](https://github.com/opsydyn/herdr-questmancer)<br><sub>opsydyn</sub> | 为你的 Herdr 编程 Agent 打造的温馨 16 位冒险者公会。工作中的 Agent 在探索地下城，被阻塞的 Agent 在寻求指点，完成的工作则带着战利品归来 | `coding-agents` `pixel-art` `ratatui` `tui` `rust` | 4 | 🔄 2026-09-09 |
| [**herdr-nerd-font-tab-name**](https://github.com/rohankewal/herdr-nerd-font-tab-name)<br><sub>rohankewal</sub> | 为 herdr 标签页添加 Nerd Font 图标——joshmedeski/tmux-nerd-font-window-name 的 herdr 移植版 | `nerd-fonts` `python` `terminal` `tui` | 4 | 2026-07-31 |
| [**herdr-powershell-title-sync**](https://github.com/aclima01/herdr-powershell-title-sync)<br><sub>aclima01</sub> | window-title-sync 的 Windows/PowerShell 移植版：将终端标题同步为当前聚焦的 herdr 会话 | `powershell` | 2 | 2026-07-20 |
| [**herdr-pane-autorename**](https://github.com/b12o/herdr-pane-autorename)<br><sub>b12o</sub> | 根据当前运行的进程名称，自动重命名窗格的 Herdr 插件。 | `shell` | 2 | 🔄 2026-09-07 |
| [**herdr-titles**](https://github.com/davidolrik/herdr-titles)<br><sub>davidolrik</sub> | 始终跟得上变化的 Herdr 标题。herdr-titles 会根据实际运行的内容（包括 AI Agent 的实时会话标题）为标签页和窗口命名，并通过一个小型 HCL 模板，从工作区、标签页、Agent 待处理数量和 shell 环境组合出窗口标题。即时生效，CPU 占用近乎为零。零配置即可开始使用，且可无限调整 | `ai-assisted` `go` | 2 | 🔄 2026-09-06 |
| [**🆕 herdr-pixel-office**](https://github.com/devangchhajed/herdr-pixel-office)<br><sub>devangchhajed</sub> | Watch your AI coding agents work as pixel-art characters in a tiny top-down office — a herdr plugin | `typescript` | 2 | 🔄 2026-09-18 |
| [**herdr-english-coach**](https://github.com/GranamyrBR/herdr-english-coach)<br><sub>GranamyrBR</sub> | herdr 插件：彩色标注的英语纠错面板——在你工作时，编程 Agent 将语法和开发行话的修正实时记录到侧边窗格 | `english` `language-learning` `shell` | 2 | 2026-07-06 |
| [**herdr-ai-tab-name**](https://github.com/ndom91/herdr-ai-tab-name)<br><sub>ndom91</sub> | 使用本地 LLM 自动为 Herdr 标签页命名 | `local-llm` `python` | 2 | 🔄 2026-09-19 |
| [**🆕 herdr-agent-tab-titles**](https://github.com/ajaykumarMohite/herdr-agent-tab-titles)<br><sub>ajaykumarMohite</sub> | Renames each Herdr tab to the task its coding agent is working on | `claude-code` `developer-tools` `terminal` `python` | 1 | 🔄 2026-09-17 |
| [**herdr-git-tab-name**](https://github.com/blurname/herdr-git-tab-name)<br><sub>blurname</sub> | 将标签页重命名为聚焦窗格所在 Git 分支名的 Herdr 插件 | `shell` | 1 | 2026-07-06 |
| [**herdr-hermes-session-title**](https://github.com/btorresgil/herdr-hermes-session-title)<br><sub>btorresgil</sub> | 在 Herdr 侧边栏中显示 Hermes Agent 的会话标题 | `python` | 1 | 2026-08-07 |
| [**herdr-tab-smart-rename-rs**](https://github.com/EmmetZ/herdr-tab-smart-rename-rs)<br><sub>EmmetZ</sub> | _(暂无描述)_ | `rust` | 1 | 2026-08-24 |
| [**pane-identity**](https://github.com/Ghost-LZW/pane-identity)<br><sub>Ghost-LZW</sub> | 无需修改你的 Agent，即可在 Herdr 中显示窗格 ID、主机名和标签。 | `python` `terminal` | 1 | 2026-09-05 |
| [**herdr-emoji-time**](https://github.com/hotnugs/herdr-emoji-time)<br><sub>hotnugs</sub> | 为你的 Herdr 空间、Agent 和标签页添加表情符号，给终端增添一点乐趣。 | `emoji` `terminal` `tui` `python` | 1 | 🔄 2026-09-12 |
| [**herdr-chromatic-spaces**](https://github.com/jackfrancisdalton/herdr-chromatic-spaces)<br><sub>jackfrancisdalton</sub> | 为每个 Herdr Space 赋予专属颜色和表情符号——彩色侧边栏圆点、Agent 分组，以及切换 Space 时可选的界面着色 | `python` | 1 | 2026-08-22 |
| [**herdr-tab-title-sync**](https://github.com/lucasleon2107/herdr-tab-title-sync)<br><sub>lucasleon2107</sub> | 将标签页名称同步为 AI Agent 对话标题的 herdr 插件 | `ai-agents` `claude-code` `terminal` `tmux` `shell` | 1 | 2026-08-04 |
| [**herdr-agent-smart-rename**](https://github.com/malone-c/herdr-agent-smart-rename)<br><sub>malone-c</sub> | 根据每个 herdr Agent 会话实际在做的事情为其命名 | `python` | 1 | 2026-08-14 |
| [**🆕 ZimMux**](https://github.com/Mr-Destroyer/ZimMux)<br><sub>Mr-Destroyer</sub> | ZimMux：一款单文件的 tmux 主题，采用 herdr 的 Ink 风格。薰衣草色聚焦边框、低调的状态栏、无需前缀键的 Alt 快捷键绑定，一条命令即可安装并自动备份。无需任何插件。 | `agent` `agent-framework` `agent-workflows` `agentic-ai` `agentic-workflow` | 1 | 🔄 2026-09-15 |
| [**herdr-session-sync**](https://github.com/nengqi/herdr-session-sync)<br><sub>nengqi</sub> | 将 Claude Code、Codex 和 Agent 的会话名称，自动同步到 Herdr 窗格标签、PTY 窗口标题和移动配套应用（Heeler）之间 | `agent` `claude-code` `codex` `heeler` `terminal-multiplexer` | 1 | 🔄 2026-09-15 |
| [**herdr-nerd-font-tab-name-windows**](https://github.com/Only-Moon/herdr-nerd-font-tab-name-windows)<br><sub>Only-Moon</sub> | herdr-nerd-font-tab-name 的 Windows 移植版：为 herdr 标签页显示 Nerd Font 图标，跨平台支持 Windows、macOS、Linux，并支持按文件夹解析图标 | `herdr-windows` `icons` `nerd-fonts` `python` `title` | 1 | 2026-08-10 |
| [**herdr-tab-renamer**](https://github.com/ryanlewis/herdr-tab-renamer)<br><sub>ryanlewis</sub> | herdr 插件：根据标签页的实际内容（Agent 会话标题和 shell 目录）为其打标签 | `javascript` | 1 | 2026-08-08 |
| [**herdr-workspace-renamer**](https://github.com/ryanlewis/herdr-workspace-renamer)<br><sub>ryanlewis</sub> | herdr 插件：将 Agent 会话名称同步到工作区标签 | `javascript` | 1 | 2026-08-08 |
| [**herdr-pomodoro**](https://github.com/sazardev/herdr-pomodoro)<br><sub>sazardev</sub> | 简约优雅、可随主题自适应的 Herdr 番茄钟插件。 | `rust` | 1 | 🔄 2026-09-08 |
| [**herdr-claude-tab-title**](https://github.com/tmn73/herdr-claude-tab-title)<br><sub>tmn73</sub> | 将每个 Claude Code 会话标题及其 Agent 状态同步到对应的 Herdr 标签页 | `claude-code` `tabs` `terminal` `typescript` | 1 | 🔄 2026-09-07 |
| [**herdr-stack-icon**](https://github.com/bonkey/herdr-stack-icon)<br><sub>bonkey</sub> | Herdr 插件：根据仓库文件自动检测技术栈，在每个工作区旁显示对应的技术图标（🍏 🤖 🦀 🐹 🟩 🐍）。 | `python` | 0 | 🔄 2026-09-10 |
| [**🆕 herdr-tabline**](https://github.com/btj93/herdr-tabline)<br><sub>btj93</sub> | 使用安全的模板和感知项目的配置文件来渲染 Herdr 的标签页标题。 | `golang` `tabline` `terminal` `tui` `go` | 0 | 2026-09-04 |
| [**herdr-habitat**](https://github.com/chantlong/herdr-habitat)<br><sub>chantlong</sub> | herdr habitat 是一个随 Agent 工作而成长的「活的」终端生态系统。培育需要时间，所以请不要过度堆砌 Agent。讽刺的是，当 Agent 在损害生态的高耗能数据中心里燃烧 token 时，herdr habitat 却在培育虚拟植物、吸引虚拟野生动物 | `chill` `cozy` `javascript` | 0 | 2026-08-16 |
| [**herdr-tab-title-from-terminal**](https://github.com/christiangroth/herdr-tab-title-from-terminal)<br><sub>christiangroth</sub> | 为每个 Herdr 标签页命名为其内部 Agent 的终端标题。在 Claude Code 中执行一次 /rename，会同时为会话和标签页命名。手动命名过的标签页则不受影响 | `python` | 0 | 2026-08-25 |
| [**herdr-llm-summary-header**](https://github.com/dnf0/herdr-llm-summary-header)<br><sub>dnf0</sub> | herdr 插件：Agent 完成后，将 LLM 生成的一行摘要写入窗格标题 | `javascript` | 0 | 2026-08-03 |
| [**🆕 herdr-plugin-pane-id-namer**](https://github.com/gcgo/herdr-plugin-pane-id-namer)<br><sub>gcgo</sub> | 自动生成 Agent 名称并显示在终端中。 | `shell` | 0 | 2026-09-05 |
| [**🆕 herdr-pane-id-border**](https://github.com/Haichiu/herdr-pane-id-border)<br><sub>Haichiu</sub> | 一个极简的 Herdr 插件，在窗格边框上显示规范的窗格 ID。 | `shell` | 0 | 2026-09-02 |
| [**herdr-tab-numbers**](https://github.com/kokatsu/herdr-tab-numbers)<br><sub>kokatsu</sub> | 在每个标签页名称前加上其 switch_tab 位置编号 | `shell` | 0 | 2026-08-26 |
| [**🆕 herdr-tab-title**](https://github.com/Newt6611/herdr-tab-title)<br><sub>Newt6611</sub> | Herdr Tab Title 会将 Herdr 标签页自动重命名为整洁的、按工作区独立编号的名称，如「1. Codex」「2. Terminal」，格式可自定义 | `rust` | 0 | 2026-07-09 |
| [**🆕 herdr-codex-session-title**](https://github.com/sergeybataev/herdr-codex-session-title)<br><sub>sergeybataev</sub> | 将 Codex 聊天标题同步为 Agent 名称的 Herdr 插件 | `codex` `python` | 0 | 2026-08-01 |
| [**🆕 herdr-ghostty-theme-sync**](https://github.com/themuuln/herdr-ghostty-theme-sync)<br><sub>themuuln</sub> | 让 herdr 的主题和侧边栏配色跟随当前使用的 Ghostty 主题——即使 herdr 重启，侧边栏的配色 token 也会保留。herdr.dev 出品的插件 | `python` | 0 | 2026-08-12 |

<details><summary>与此目的也相关</summary>

- [kryptamine/herdr-auto-title](https://github.com/kryptamine/herdr-auto-title) — 自动跟随每个标签页中工作内容变化的标签标题。借助 Herdr 让标签页保持整洁，一眼就知道自己在做什么。
- [qu8n/herdr-automatic-rename](https://github.com/qu8n/herdr-automatic-rename) — 智能的 herdr 标签页名称，帮助你更快地在 Agent 与 shell 之间切换。
- [sh1ma/herdr-auto-title](https://github.com/sh1ma/herdr-auto-title) — 根据 Claude Code 和 Codex 的对话内容，自动生成 herdr 标签页标题
- [IvoryHeart/herdr-world](https://github.com/IvoryHeart/herdr-world) — Herdr World——面向 Herdr 的多界面网页体验
- [wyattjoh/herdr-plugin-renamer](https://github.com/wyattjoh/herdr-plugin-renamer) — 根据 Agent 的第一条提示词，重命名自动生成的 herdr 工作树分支和工作区（通过设备端 Apple FoundationModels 或 Codex）
- [ythx-101/herdr-social-glass](https://github.com/ythx-101/herdr-social-glass) — 面向 macOS 版 Herdr 的、适合截图分享的 Social Glass 主题与工作流插件
- [aarsh21/herdr-tab-title](https://github.com/aarsh21/herdr-tab-title) — 为 Herdr 提供类似 tmux 的自动标签页标题
- [funsaized/herdr-mise](https://github.com/funsaized/herdr-mise) — 追求「通过」而非「提示词数量」🧑‍🍳 一款在 herdr 中可视化你的 Agent 的工具，刻意保持极小的资源占用。
- [suisya-systems/herdr-agent-office](https://github.com/suisya-systems/herdr-agent-office) — 将你的 Agent 团队呈现为像素风办公室的 herdr 插件。查看谁在工作、谁卡住了，并可直接跳转过去
- [maedana/herdr-whereami](https://github.com/maedana/herdr-whereami) — 自动重命名标签页以显示你当前所在位置的 Herdr 插件——在 git 仓库内会显示为「仓库名/分支名」
- [azyu/herdr-agent-auto-naming](https://github.com/azyu/herdr-agent-auto-naming) — 一个 Herdr 插件，为检测到的每个 Agent 分配一个易读的双词名称，并作为窗格标签持久保存，重启后依然保留。
- [dev-shimada/herdr-auto-tab-name](https://github.com/dev-shimada/herdr-auto-tab-name) — herdr 插件：根据当前目录自动命名标签页
- [winoooops/herdr-agent-title-sync](https://github.com/winoooops/herdr-agent-title-sync) — 为 Claude Code、Codex、Kimi Code、OpenCode 等编程 Agent 提供的 Herdr 窗格标题自动同步
- [filoozom/herdr-title](https://github.com/filoozom/herdr-title) — 在终端标签页标题中显示所选工作树和 Agent 活动状态的 Herdr 插件
- [jovylle/herdr-session-title-name](https://github.com/jovylle/herdr-session-title-name) — herdr 插件：将 terminal_title_stripped 持久化到标签页（顶部只保留 session_title，标签页关闭后依然保留该标题）
- [KazBrekker1/herdr-hasr](https://github.com/KazBrekker1/herdr-hasr) — Hasr（حصر——意为「枚举、完整清点」）——herdr 的 goto 风格弹窗切换器：切换、重命名、删除并创建 Agent、标签页和空间，并实时追踪完成状态
- [khatriafaz/herdr-plugin-auto-rename](https://github.com/khatriafaz/herdr-plugin-auto-rename) — 根据 Pi 会话的第一条提示词，自动重命名新的 Herdr 工作区和 Git 分支
- [ummoftgo/herdr-quota-theme](https://github.com/ummoftgo/herdr-quota-theme) — 无需修改上游插件，即可让 Herdr Agent Quota 的侧边栏颜色随主题自适应。

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-text"></a>

## 文本与 URL 提取

> 想不用鼠标就抓取屏幕上显示的字符串、路径或 URL

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-pluck**](https://github.com/rmarganti/herdr-pluck)<br><sub>rmarganti</sub> | 从 Herdr 窗格中快速复制匹配特定模式的字符串 | `rust` | 24 | 2026-08-07 |
| [**herdr-tiny-fingers**](https://github.com/hotchpotch/herdr-tiny-fingers)<br><sub>hotchpotch</sub> | 面向 Herdr 的 tmux-fingers 风格可见屏幕复制提示 | `tools` `rust` | 14 | 🔄 2026-09-15 |
| [**herdr-scratchpad**](https://github.com/vjeantet/herdr-scratchpad)<br><sub>vjeantet</sub> | 每个标签页一个缓冲区用于准备提示词，一键即可投递到 Agent 的输入框 | `clipboard` `ratatui` `rust` `scratchpad` `terminal` | 5 | 2026-08-31 |
| [**herdr-flash**](https://github.com/youguanxinqing/herdr-flash)<br><sub>youguanxinqing</sub> | 面向 Herdr 窗格的 flash.nvim 风格搜索、选择与复制 | `rust` `terminal` | 5 | 🔄 2026-09-16 |
| [**herdr-fingers**](https://github.com/hitaishi2222/herdr-fingers)<br><sub>hitaishi2222</sub> | Fingers to clipboard：从当前窗格中拾取信息的智能浮层 | `python` | 4 | 2026-07-16 |
| [**herdr-agent-copy-paste-fork**](https://github.com/calebcauthon/herdr-agent-copy-paste-fork)<br><sub>calebcauthon</sub> | 只需复制粘贴即可分叉，或用快捷键将分叉分到新窗格 | `claude-code` `codex` `shell` | 3 | 2026-07-24 |
| [**herdr-paste-image**](https://github.com/ddfonseca/herdr-paste-image)<br><sub>ddfonseca</sub> | 将剪贴板中的图片以文件路径形式粘贴到 herdr 窗格——tmux-paste-image 的 herdr 移植版 | `shell` | 3 | 2026-07-30 |
| [**herdr-copy-search**](https://github.com/qq88976321/herdr-copy-search)<br><sub>qq88976321</sub> | 面向 herdr 回滚缓冲区的正则表达式和 copycat 模式搜索，配合 extrakto 令牌提取，落地到 tmux 风格的复制模式（OSC 52） | `copy-mode` `rust` `terminal` `tmux` | 3 | 2026-08-04 |
| [**herdr-s3-clipboard**](https://github.com/jagzmz/herdr-s3-clipboard)<br><sub>jagzmz</sub> | 使用 S3 兼容存储，将 Herdr 中剪贴板的图片发布为可复用的公开链接或预签名链接 | `aws-s3` `clipboard` `cloudflare-r2` `developer-tools` `image-publishing` | 2 | 2026-07-16 |
| [**scoopr**](https://github.com/TawfiqAbubaker/scoopr)<br><sub>TawfiqAbubaker</sub> | 无需使用鼠标即可将任意内容复制到终端的 Herdr 插件，灵感来自 tmux 的 extrakto。 | `rust` | 2 | 🔄 2026-09-06 |
| [**herdr-ferry**](https://github.com/wavrin/herdr-ferry)<br><sub>wavrin</sub> | 通过 SSH 在 Herdr 所在机器和你的笔记本电脑之间传输文件和剪贴板内容——无需云存储桶 | `rust` | 2 | 2026-08-29 |
| [**herdr-scrollback-capture**](https://github.com/alexjsp/herdr-scrollback-capture)<br><sub>alexjsp</sub> | 将聚焦窗格的回滚缓冲区以 HTML 或文本形式保存到桌面的 Herdr 插件 | `shell` | 1 | 2026-06-30 |
| [**herdr-link-browser**](https://github.com/bonkey/herdr-link-browser)<br><sub>bonkey</sub> | Herdr 插件：按住 Ctrl 点击 http(s) 链接，即可在窗格旁以分屏方式用 terminal-browser 打开。 | `terminal-browser` `shell` | 1 | 🔄 2026-09-07 |
| [**herdr-fleece**](https://github.com/dmazlum/herdr-fleece)<br><sub>dmazlum</sub> | 在 Herdr 中截取 Agent 的最后一条回答，随后可复制、保存或发送。 | `typescript` | 1 | 🔄 2026-09-11 |
| [**herdr-leap**](https://github.com/RooseveltAdvisors/herdr-leap)<br><sub>RooseveltAdvisors</sub> | 面向 Herdr 终端多路复用器的 EasyMotion/leap 风格字符跳转+选中复制 | `easymotion` `rust` `terminal` `tui` | 1 | 2026-07-24 |
| [**herdr-copy-hints**](https://github.com/rotemb-wond/herdr-copy-hints)<br><sub>rotemb-wond</sub> | 面向 Herdr 的 tmux-fingers 风格键盘复制提示：路径、Git SHA、URL 等 | `clipboard` `developer-tools` `keyboard-navigation` `productivity` `terminal` | 1 | 2026-07-23 |
| [**herdr-copy-pane-id**](https://github.com/wine-fall/herdr-copy-pane-id)<br><sub>wine-fall</sub> | herdr 插件：将聚焦窗格的 ID 复制到剪贴板，或在每个窗格的边框上显示其 ID | `cli` `terminal` `python` | 1 | 2026-08-24 |
| [**herdr-translate**](https://github.com/zackshen/herdr-translate)<br><sub>zackshen</sub> | herdr 插件：在居中弹出层中翻译鼠标选中的终端文本 | `rust` | 1 | 2026-08-25 |
| [**herdr-agent-links**](https://github.com/OmarDadabhoy/herdr-agent-links)<br><sub>OmarDadabhoy</sub> | 在 Herdr 中打开隐藏在 Codex 和 Claude 输出的 Markdown 标签背后的链接。 | `claude-code` `codex` `productivity` `terminal` `python` | 0 | 2026-09-02 |
| [**🆕 herdr-translate**](https://github.com/wenPKtalk/herdr-translate)<br><sub>wenPKtalk</sub> | herdr 插件：用 translate-shell 翻译窗格中选中的文本，并以浮动弹窗显示（支持 macOS 和 Linux） | `translate` `shell` | 0 | 2026-08-19 |

<details><summary>与此目的也相关</summary>

- [nicosuave/memex](https://github.com/nicosuave/memex) — 搜索 Claude Code、Codex、Pi、OpenCode、GitHub Copilot 和 Cursor 的会话记录。恢复会话。追踪 token 使用
- [iurysza/termscope](https://github.com/iurysza/termscope) — 在分屏中打开终端屏幕上已经可见的文件和链接
- [junghan0611/entwurf](https://github.com/junghan0611/entwurf) — Herdr and tmux sibling AI sessions: pi, Claude Code, Codex, Copilot, OMP and Antigravity can message and spaw…
- [pinkpixel-dev/quota](https://github.com/pinkpixel-dev/quota) — 一款桌面应用、VSCode 扩展兼 Herdr 插件，用于跟踪 GitHub Copilot、Codex、Claude Code、Antigravity、Kiro、Grok 和 Cursor 的 AI 使用情况。
- [jlimas/herdr-worktree-seed](https://github.com/jlimas/herdr-worktree-seed) — 为新工作树植入 copy-on-write 的 node_modules 和可配置本地 dotfiles 的 Herdr 插件
- [tanshio/herdr-worktreeinclude](https://github.com/tanshio/herdr-worktreeinclude) — Herdr 插件：将匹配 .worktreeinclude 的被 gitignore 文件复制到新创建的工作树中
- [eightHundreds/herdr-worktreeinclude](https://github.com/eightHundreds/herdr-worktreeinclude) — Herdr 插件：将 .worktreeinclude 指定的被 gitignore 文件复制到新工作树中
- [shadowfax92/herdr-comments](https://github.com/shadowfax92/herdr-comments) — 为复制的 Herdr 终端输出添加注释，按窗格收集评论，并可在 Neovim 中审查
- [crexi/herdr-worktree-copy](https://github.com/crexi/herdr-worktree-copy) — 根据 .worktree-copy 清单复制并符号链接工作树本地文件的 Herdr 插件
- [Feasy01/herdr-allow](https://github.com/Feasy01/herdr-allow) — herdr 插件：通过 .herdr-allow 允许列表，将被 gitignore 的文件（.env、密钥、本地配置）复制到每个新工作树中
- [khatriafaz/herdr-plugin-cow-worktree](https://github.com/khatriafaz/herdr-plugin-cow-worktree) — Herdr plugin for strict copy-on-write Git worktrees that include ignored local files
- [tupton/herdr-worktree-include](https://github.com/tupton/herdr-worktree-include) — 将未跟踪的文件以符号链接或复制的方式引入 herdr 创建的 git worktree。
- [zerodice0/herdr-plugin-worktree-bootstrap](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap) — 在新的 Herdr Git 工作树中安全地复制被忽略的本地文件并运行初始化命令
- [GODVvVZzz/herdr-workspace-copy](https://github.com/GODVvVZzz/herdr-workspace-copy) — Herdr plugin: copy a workspace folder to a sibling path and open it as a new workspace (no git worktree requi…
- [piesuke/herdr-worktree-bootstrap](https://github.com/piesuke/herdr-worktree-bootstrap) — Bootstrap a new worktree: copy gitignored files, install deps, run hooks
- [scoussens-nthplusio/herdr-worktree-include](https://github.com/scoussens-nthplusio/herdr-worktree-include) — 使用仓库的 .worktreeinclude（与 Claude Code 使用的同一份文件、同一套规则），将 .env 等被 gitignore 忽略的文件复制到新的 Herdr 工作树中
- [willian/herdr-fzf-url](https://github.com/willian/herdr-fzf-url) — 用 `fzf` 从聚焦窗格中选取 URL，然后打开或复制

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-meta"></a>

## 插件管理与开发

> 想管理插件本身，或者自己动手做一个

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-plus**](https://github.com/cloudmanic/herdr-plus)<br><sub>cloudmanic</sub> | herdr 的扩展，作为原生插件构建——一组让 herdr 更好用的工具集：项目管理和快捷操作 | `go` | 326 | 2026-09-04 |
| [**herdr-plugin-manager**](https://github.com/speardragon/herdr-plugin-manager)<br><sub>speardragon</sub> | 在弹窗中管理 herdr 插件——安装、更新、启用/禁用、卸载，并浏览 herdr-plugin 市场。推荐快捷键：prefix+p | `plugin-manager` `tui` `shell` | 39 | 🔄 2026-09-18 |
| [**herdr-lazy**](https://github.com/natori-hrj/herdr-lazy)<br><sub>natori-hrj</sub> | Declarative, reproducible plugin manager and curated distro for Herdr — one list, a lockfile, and a safe manage pane. | `cli` `lockfile` `plugin-manager` `rust` `terminal` | 25 | 🔄 2026-09-16 |
| [**house-of-herdr**](https://github.com/alasano/house-of-herdr)<br><sub>alasano</sub> | Herdr 插件合集——包含 Codex Micro：在 Work Louder Codex Micro 上显示 Agent 状态灯并提供操作控制 | `codex-micro` `work-louder` `typescript` | 7 | 2026-08-13 |
| [**herdr-plugins-labs**](https://github.com/hmu332233/herdr-plugins-labs)<br><sub>hmu332233</sub> | Herdr 的实验性插件——在这里孵化，成熟后独立成自己的仓库 | `labs` `javascript` | 2 | 🔄 2026-09-08 |
| [**herdr-plugin-rust**](https://github.com/Newt6611/herdr-plugin-rust)<br><sub>Newt6611</sub> | 用于构建 Herdr 插件的 Rust 应用框架 | `rust` | 2 | 2026-07-09 |
| [**herdr-plugins**](https://github.com/alastairsounds/herdr-plugins)<br><sub>alastairsounds</sub> | 面向 herdr 的插件合集 | `rust` | 1 | 2026-08-28 |
| [**herdr-client**](https://github.com/vika2603/herdr-client)<br><sub>vika2603</sub> | 面向 Herdr socket API 的 Go 客户端兼插件工具包：涵盖全部 102 个方法、会话镜像与插件运行时，均从 herdr 打印的 schema 生成。对应 herdr 0.9.0，协议版本 22。 | `coding-agents` `go` `golang` `sdk` `terminal-multiplexer` | 1 | 🔄 2026-09-18 |
| [**🆕 herdr-plugins**](https://github.com/tyler-jewell/herdr-plugins)<br><sub>tyler-jewell</sub> | 纯 Rust 编写的 Herdr 插件 monorepo（优先使用标准库）。安装方式：herdr plugin install tyler-jewell/herdr-plugins/<subdir> | `rust` `go` | 0 | 2026-08-10 |

[⬆ 返回目的列表](#purposes)

<a id="cat-other"></a>

## 其他与实用工具

> 不属于以上任何分类，但很实用的东西

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**terminal-browser**](https://github.com/zenbu-labs/terminal-browser)<br><sub>zenbu-labs</sub> | 终端里的浏览器 | `browser` `claude-code` `claude-code-plugin` `claude-skills` `cli` | 3151 | 🔄 2026-09-19 |
| [**herdr-lantern**](https://github.com/aigorahub/herdr-lantern)<br><sub>aigorahub</sub> | Lantern，来自 Elves。一个 Herdr 插件：羊群正在田野中——Lantern 会照亮谁需要你、以及他们正朝着什么目标努力 | `shell` | 67 | 🔄 2026-09-06 |
| [**herdr-gui**](https://github.com/undivisible/herdr-gui)<br><sub>undivisible</sub> | 为 herdr 打造的 GUI 界面及更多功能，基于 crepuscular gpui 构建。 | `crepuscularity` `gpui` `rust` | 16 | 2026-07-27 |
| [**herdr-commandcode-plugin**](https://github.com/TheMetalStorm/herdr-commandcode-plugin)<br><sub>TheMetalStorm</sub> | 将 Commandcode 集成到 Herdr 中 | `cli` `commandcode` `herdr-integration` `shell` | 13 | 2026-07-30 |
| [**herdr-plugins-directory**](https://github.com/MIDO-ruby7/herdr-plugins-directory)<br><sub>MIDO-ruby7</sub> | 按你想完成的事情来查找 herdr 插件的链接集合 | `python` | 10 | 🔄 2026-09-20 |
| [**neon-herdr**](https://github.com/neon-solutions/neon-herdr)<br><sub>neon-solutions</sub> | Neon 官方的 Herdr 插件 | `typescript` | 10 | 2026-08-06 |
| [**herdr-plugin-cmux**](https://github.com/lachieh/herdr-plugin-cmux)<br><sub>lachieh</sub> | 将每个由 herdr 管理的 Agent 镜像到 cmux 侧边栏中各自独立的一行——带状态徽标和可点击跳转的任务行 | `javascript` | 9 | 2026-07-01 |
| [**herdr-freebuff-plugin**](https://github.com/TheMetalStorm/herdr-freebuff-plugin)<br><sub>TheMetalStorm</sub> | Herdr 的 Freebuff 生命周期集成插件——通过文件轮询和 PTY 内容抓取来报告闲置/工作中/被阻塞状态 | `cli` `freebuff` `herdr-integration` `shell` | 6 | 2026-07-22 |
| [**wave-tui**](https://github.com/takemo101/wave-tui)<br><sub>takemo101</sub> | 适合工作时段的安静终端电台 | `rust` | 5 | 2026-07-20 |
| [**herdr-memory**](https://github.com/jatingargiitk/herdr-memory)<br><sub>jatingargiitk</sub> | 从你的编程会话中构建「活的大脑」的 Herdr 插件——逐步学习哪些做法有效、哪些失败了，以及你做出的决定 | `shell` | 3 | 2026-08-11 |
| [**hrd**](https://github.com/joshuadavidthomas/hrd)<br><sub>joshuadavidthomas</sub> | 管理你的沙盒集群及运行在其上的 Herdr 会话 | `go` | 3 | 2026-09-04 |
| [**herdrctx**](https://github.com/j0urneyk/herdrctx)<br><sub>j0urneyk</sub> | 用于管理本地 Herdr 会话的终端 UI。 | `go` | 2 | 🔄 2026-09-10 |
| [**🆕 shipframe**](https://github.com/juanitourquiza/shipframe)<br><sub>juanitourquiza</sub> | AI coding workflows for teams that plan, prove, and ship. | `ai` `ai-coding` `ai-tools` `claude` `claude-code` | 2 | 🔄 2026-09-16 |
| [**herdr-standup**](https://github.com/neospeed83/herdr-standup)<br><sub>neospeed83</sub> | 根据 Git 活动和 Herdr 上下文，生成有据可查的每日站会摘要 | `developer-tools` `standup` `rust` | 2 | 2026-08-31 |
| [**herdr-handsfree**](https://github.com/RanolP/herdr-handsfree)<br><sub>RanolP</sub> | 免提操作的 herdr 插件——提供基于 whisper.cpp 的语音听写和面向 macOS 的摄像头视线鼠标 | `rust` | 2 | 2026-07-30 |
| [**herdr-shadow-pane**](https://github.com/shaozk/herdr-shadow-pane)<br><sub>shaozk</sub> | Herdr 插件「Shadow Clone Panel」——可同时操控多个面板。 | `rust` `vibe-coding` | 2 | 🔄 2026-09-14 |
| [**herdr-suite-site**](https://github.com/StructuPath/herdr-suite-site)<br><sub>StructuPath</sub> | StructuPath Herdr Suite 的官网首页——herdr.structupath.ai | `herdr-integration` `html` | 2 | 🔄 2026-09-16 |
| [**herdr-sprites-plugin**](https://github.com/superfly/herdr-sprites-plugin)<br><sub>superfly</sub> | Fly.io Sprites 的官方 Herdr 插件。 | `sandboxes` `sprites` `javascript` | 2 | 🔄 2026-09-09 |
| [**🆕 herdr-stt**](https://github.com/xtwist/herdr-stt)<br><sub>xtwist</sub> | Speech-to-text for Herdr | `rust` | 2 | 🔄 2026-09-18 |
| [**herdr-zen**](https://github.com/y4m3/herdr-zen)<br><sub>y4m3</sub> | 为 Herdr 提供带可调居中窗格宽度的禅模式 | `rust` `terminal` `zen-mode` | 2 | 2026-08-19 |
| [**herdr-edit-windows**](https://github.com/aclima01/herdr-edit-windows)<br><sub>aclima01</sub> | 在编程 Agent 旁边的 herdr 窗格中运行的简易文本编辑器——文件树、语法高亮编辑器、未提交差异标签页。仅支持 Windows | `rust` | 1 | 2026-07-25 |
| [**🆕 herdr-tts**](https://github.com/Aktrov/herdr-tts)<br><sub>Aktrov</sub> | 一个 Herdr 插件，可用自然的神经网络语音（Piper）朗读选中的终端文本——右键点击或使用快捷键触发，并配有停止键。 | `tts` `python` | 1 | 🔄 2026-09-07 |
| [**herdr-quotabar**](https://github.com/ArnaudRinquin/herdr-quotabar)<br><sub>ArnaudRinquin</sub> | 将 Claude 套餐配额（5 小时 / 7 天 / 按模型）以紧凑的一行显示在 Herdr 标签栏中，服务商可插拔替换。 | `claude-code` `python` | 1 | 🔄 2026-09-08 |
| [**herdr-stoplight**](https://github.com/BowlOfSoup/herdr-stoplight)<br><sub>BowlOfSoup</sub> | 根据 Herdr 的实时状态驱动一个物理 Arduino 红绿灯模块 | `go` | 1 | 2026-07-11 |
| [**harbr**](https://github.com/dev-town/harbr)<br><sub>dev-town</sub> | Harbour TUI | `typescript` | 1 | 2026-09-03 |
| [**herdr-rainfrog**](https://github.com/fraction12/herdr-rainfrog)<br><sub>fraction12</sub> | 在受管理的 HerdR 窗格中打开 Rainfrog | `shell` | 1 | 2026-08-15 |
| [**herdr-openlogi**](https://github.com/giacolees/herdr-openlogi)<br><sub>giacolees</sub> | 通过 OpenLogi 绑定浮层，将罗技鼠标接入 herdr | `ghostty` `logitech-mouse` `macos` `openlogi` `shell` | 1 | 2026-08-24 |
| [**🆕 herdr-tiling**](https://github.com/jaeheonji/herdr-tiling)<br><sub>jaeheonji</sub> | Hyprland-style pane movement and tmux-style layouts for Herdr | `rust` | 1 | 🔄 2026-09-18 |
| [**🆕 herdr-services**](https://github.com/lucidstack/herdr-services)<br><sub>lucidstack</sub> | Plugin to track services running inside herdr workspaces | `rust` | 1 | 🔄 2026-09-16 |
| [**herdr-plugins**](https://github.com/narumiruna/herdr-plugins)<br><sub>narumiruna</sub> | _(暂无描述)_ | `rust` | 1 | 2026-08-08 |
| [**herdr-docs**](https://github.com/natori-hrj/herdr-docs)<br><sub>natori-hrj</sub> | 为 Herdr 打造的安静、格式统一的文档阅读窗格。 | `docs` `rust` | 1 | 🔄 2026-09-10 |
| [**herdr-phin-util**](https://github.com/phin-tech/herdr-phin-util)<br><sub>phin-tech</sub> | 个人 Herdr 实用工具集 | `bubbletea` `tui` `go` | 1 | 2026-08-18 |
| [**herdr-api-client**](https://github.com/playsthisgame/herdr-api-client)<br><sub>playsthisgame</sub> | 在 herdr 分屏窗格或标签页中运行的 HTTP/REST API 客户端——无需离开终端即可浏览、运行和测试请求 | `http-client` `rest-client` `tui` `shell` | 1 | 2026-08-08 |
| [**herdr-browser**](https://github.com/redsquiggle/herdr-browser)<br><sub>redsquiggle</sub> | 让 Chromium 标签组与 Herdr 工作区保持一致 | `chromium` `ratatui` `rust` | 1 | 2026-07-28 |
| [**🆕 pixtui**](https://github.com/RizRiyz/pixtui)<br><sub>RizRiyz</sub> | 在终端中运行的像素画编辑器 | `bohay-module` `editor` `luvus-module` `pixel-art` `termina` | 1 | 2026-08-07 |
| [**herdr-orca**](https://github.com/rudironsoni/herdr-orca)<br><sub>rudironsoni</sub> | 将标准 Orca 标签页附加到 Herdr 管理的终端上的 Herdr 插件。 | `typescript` | 1 | 2026-09-03 |
| [**🆕 herdr-rss**](https://github.com/shindakun/herdr-rss)<br><sub>shindakun</sub> | An RSS reader plugin for herdr, cuz why not | `rss` `rss-reader` `rust` | 1 | 🔄 2026-09-20 |
| [**herdr-sidepulse**](https://github.com/third774/herdr-sidepulse)<br><sub>third774</sub> | _(暂无描述)_ | `javascript` | 1 | 2026-08-14 |
| [**🆕 herdr-pdf**](https://github.com/tim80411/herdr-pdf)<br><sub>tim80411</sub> | PDF viewer plugin for herdr: renders pages into a split pane through the pane.graphics stream API | `go` `pdf` `terminal` | 1 | 🔄 2026-09-17 |
| [**herdr-plugin-k8s-context**](https://github.com/tkuchiki/herdr-plugin-k8s-context)<br><sub>tkuchiki</sub> | 以隔离的 Kubernetes context 和 namespace 打开 Herdr 标签页 | `go` | 1 | 2026-08-15 |
| [**🆕 herdr-pane-resurrect**](https://github.com/unstable-code/herdr-pane-resurrect)<br><sub>unstable-code</sub> | Save the commands running in your herdr panes and bring them back after a restart. | `shell` | 1 | 🔄 2026-09-19 |
| [**multitrunk-herdr-plugin**](https://github.com/yoyoyeti/multitrunk-herdr-plugin)<br><sub>yoyoyeti</sub> | 面向 multitrunk 任务工作区的 Herdr 插件 | `git` `multitrunk` `rust` | 1 | 2026-08-31 |
| [**🆕 herdr-priority-view**](https://github.com/asermax/herdr-priority-view)<br><sub>asermax</sub> | 面向 herdr 的自定义优先级视图，按三级优先级排序，并优先显示最旧的项目。 | `typescript` | 0 | 🔄 2026-09-12 |
| [**🆕 herdr-rails**](https://github.com/codergeek121/herdr-rails)<br><sub>codergeek121</sub> | Herdr 与 Rails 的集成。 | `ai` `rails` `shell` | 0 | 🔄 2026-09-17 |
| [**🆕 herdr-sort-spaces-plugin**](https://github.com/dorzey/herdr-sort-spaces-plugin)<br><sub>dorzey</sub> | 按标签的字典序保持工作区排列顺序。 | `shell` | 0 | 🔄 2026-09-16 |
| [**🆕 herdr-reliable-messaging**](https://github.com/feelautom/herdr-reliable-messaging)<br><sub>feelautom</sub> | 在 Windows 上，为具名的 Herdr 窗格之间提供持久且确定性的消息传递。 | `developer-tools` `nodejs` `windows` `javascript` | 0 | 🔄 2026-09-14 |
| [**🆕 hrdr-azure-plugin**](https://github.com/gbaeke/hrdr-azure-plugin)<br><sub>gbaeke</sub> | herdr 插件：浏览 Azure 资源组和资源，点击资源即可在 Azure 门户中打开 | `azure` `javascript` | 0 | 2026-08-23 |
| [**🆕 herdr-busywatch**](https://github.com/KamalF/herdr-busywatch)<br><sub>KamalF</sub> | A herdr plugin: is anything still running, and does it need me? | `python` | 0 | 🔄 2026-09-18 |
| [**🆕 herdr-laravel-tinker**](https://github.com/lancodev/herdr-laravel-tinker)<br><sub>lancodev</sub> | herdr 的分屏式 Laravel tinker REPL——编辑器旁边实时显示运行结果，可作为窗格或弹窗使用 | `laravel` `tinker` `php` `repl` | 0 | 2026-07-16 |
| [**🆕 herdr-new-task**](https://github.com/leonho/herdr-new-task)<br><sub>leonho</sub> | herdr 插件：一键选择项目目录并在新标签页中启动 claude，标签页采用名词优先的命名方式 | `python` | 0 | 2026-07-16 |
| [**🆕 strays**](https://github.com/m1sk9/strays)<br><sub>m1sk9</sub> | 用于集中管理 Claude Code 的 TUI | `claude-code` `llm` `tui` `rust` | 0 | 🔄 2026-09-20 |
| [**🆕 herdr-git-pull**](https://github.com/nimrc/herdr-git-pull)<br><sub>nimrc</sub> | _(暂无描述)_ | `python` | 0 | 2026-08-13 |
| [**ayatsumugi**](https://github.com/nkwork9999/ayatsumugi)<br><sub>nkwork9999</sub> | 面向 Ayatori 和 Tsumugi 的本地优先 React DOM、Fiber 与状态图可视化 | `cmux` `ghostty` `orca` `react-devtools` `javascript` | 0 | 2026-09-05 |
| [**🆕 herdr-action-launcher**](https://github.com/nnexai/herdr-action-launcher)<br><sub>nnexai</sub> | _(暂无描述)_ | `javascript` | 0 | 2026-08-05 |
| [**🆕 herdr-bot**](https://github.com/Phoobobo/herdr-bot)<br><sub>Phoobobo</sub> | _(暂无描述)_ | `tui` `typescript` | 0 | 2026-09-02 |
| [**herdr-traex-integration**](https://github.com/Phoobobo/herdr-traex-integration)<br><sub>Phoobobo</sub> | 支持 traex 集成的 Herdr 插件 | `shell` | 0 | 🔄 2026-09-18 |
| [**🆕 lazy-herd**](https://github.com/pve-homelab/lazy-herd)<br><sub>pve-homelab</sub> | _(暂无描述)_ | `rust` | 0 | 🔄 2026-09-14 |
| [**🆕 herdr-quicknotes**](https://github.com/QuantumEdu/herdr-quicknotes)<br><sub>QuantumEdu</sub> | _(暂无描述)_ | `notes` `rust` `terminal` `tui` | 0 | 🔄 2026-09-19 |
| [**herdr-plugins**](https://github.com/RadeJR/herdr-plugins)<br><sub>RadeJR</sub> | _(暂无描述)_ | `shell` | 0 | 🔄 2026-09-11 |
| [**herdr-now-playing**](https://github.com/spywhere/herdr-now-playing)<br><sub>spywhere</sub> | 为 herdr 添加可通过快捷键控制的音乐播放器 | `shell` | 0 | 2026-08-22 |
| [**herdr-plugins**](https://github.com/tomaszhanc/herdr-plugins)<br><sub>tomaszhanc</sub> | 个人的 herdr 插件 monorepo，每个插件都在自己的文件夹中，附带 herdr-plugin.toml 清单和可执行文件 | — | 0 | 2026-07-16 |
| [**🆕 herdr-desktop-bridge**](https://github.com/yonatangross/herdr-desktop-bridge)<br><sub>yonatangross</sub> | 一个 stdio MCP 服务器，让 Claude Desktop 能够读取 herdr 的「楼层」并留言。它只是信箱和门铃，绝非指挥席。 | `claude-desktop` `mcp` `python` | 0 | 🔄 2026-09-11 |
| [**🆕 herdr-image-gallery**](https://github.com/zbyhoo/herdr-image-gallery)<br><sub>zbyhoo</sub> | Browse AI-generated images, screenshots, and whole image folders in a Herdr terminal pane | `python` | 0 | 🔄 2026-09-20 |

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
