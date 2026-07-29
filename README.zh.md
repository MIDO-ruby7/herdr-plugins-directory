# herdr plugins by purpose

[🇯🇵 日本語](README.md) · [🇺🇸 English](README.en.md) · 🇨🇳 中文

**一个按照「你想做什么」来查找 [herdr](https://herdr.dev/) 插件的链接合集。**

- 收录 **396** 个插件 / 最后更新 **2026-07-29 09:08 UTC**（每 6 小时自动刷新）
- 数据来源：打了 GitHub 话题标签 [`herdr-plugin`](https://github.com/topics/herdr-plugin) 的仓库——与官方市场 [herdr.dev/plugins](https://herdr.dev/plugins/) 的数据来源相同
- 分类是根据仓库描述和话题标签自动推断的。如果分类不准确，可以通过 PR 修改 [`data/overrides.json`](data/overrides.json)
- 安装：`herdr plugin install owner/repo` —— [官方文档](https://herdr.dev/docs/plugins/)

> [!WARNING]
> 这是自动采集的索引，不是经过审核的目录。插件是直接在你的电脑上运行的代码，安装前请检查其 manifest 和会执行的命令。

<a id="purposes"></a>

## 按目的浏览

- [**通知与提醒**](#cat-notify) (21) — 即使离开座位，也想知道 Agent 何时完成或卡在等待输入
- [**手机与远程操控**](#cat-remote) (16) — 想在外出或用手机时监控 Agent，只需回传批准即可
- [**Agent 编排与并行执行**](#cat-agents) (48) — 想统一启动、分工并管理多个 AI Agent
- [**git 工作树与分支管理**](#cat-worktree) (25) — 想为每项工作单独开一个工作树，收尾清理也自动完成
- [**代码审查与差异对比**](#cat-review) (18) — 想阅读 Agent 写的差异并对其发表评论
- [**GitHub / issue 跟踪工具集成**](#cat-forge) (17) — 想以 issue 或 PR 为起点开始工作，并追踪 PR 状态
- [**工作区与布局搭建**](#cat-layout) (19) — 打开项目时，希望标签页、窗格和启动命令一次性就位
- [**窗格导航与快捷键**](#cat-navigate) (44) — 想用和编辑器一样的快捷键在窗格、工作区之间移动和调整大小
- [**文件浏览与编辑器联动**](#cat-files) (34) — 想在窗格中打开文件树，或与编辑器的状态保持一致
- [**Token 与费用管理**](#cat-cost) (6) — 想看看 Agent 花费了多少，并想削减用量
- [**监控与仪表盘**](#cat-monitor) (20) — 想一目览尽 Agent 和机器的状态
- [**搜索与模糊查找器**](#cat-finder) (44) — 只记得大概名字也想调出命令或项目
- [**自动化、钩子与定时任务**](#cat-automation) (20) — 想在创建工作树或指定时机自动运行固定的操作步骤
- [**会话保存与恢复**](#cat-session) (14) — 关闭工作后，希望之后能从同一状态继续
- [**标题、命名与外观**](#cat-naming) (14) — 想让标签页名称和终端标题自动变得清晰易懂，或想改变外观
- [**文本与 URL 提取**](#cat-text) (9) — 想不用鼠标就抓取屏幕上显示的字符串、路径或 URL
- [**插件管理与开发**](#cat-meta) (6) — 想管理插件本身，或者自己动手做一个
- [**其他与实用工具**](#cat-other) (21) — 不属于以上任何分类，但很实用的东西

<a id="cat-notify"></a>

## 通知与提醒

> 即使离开座位，也想知道 Agent 何时完成或卡在等待输入

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-ntfysh**](https://github.com/cobanov/herdr-ntfysh)<br><sub>cobanov</sub> | herdr 插件：当 Agent 完成或需要输入时，通过 ntfy 发送推送通知 | `notifications` `ntfy` `go` | 17 | 2026-07-02 |
| [**herdr-focus-notify**](https://github.com/yankewei/herdr-focus-notify)<br><sub>yankewei</sub> | 面向 Herdr Agent 的可点击 macOS 通知。当 Agent 被阻塞或完成时发送原生提示通知；点击后将终端置于前台并聚焦到对应的 Herdr 窗格 | `alerter` `macos` `notifications` `productivity` `rust` | 8 | 🆕 2026-07-24 |
| [**herdr-ntfy-notify**](https://github.com/zom-2018/herdr-ntfy-notify)<br><sub>zom-2018</sub> | 面向 Herdr 终端 Agent 的实时 ntfy 推送通知 | `agent` `ntfy` `push-notifications` `tui` `javascript` | 6 | 2026-06-23 |
| [**herdr-terminal-notifier**](https://github.com/dot/herdr-terminal-notifier)<br><sub>dot</sub> | 通过 terminal-notifier 为 herdr Agent 状态变化发送可自定义的 macOS 通知 | `macos` `terminal-notifier` `shell` | 5 | 2026-07-14 |
| [**herdr-pings**](https://github.com/joelhooks/herdr-pings)<br><sub>joelhooks</sub> | 面向 herdr 窗格中 AI Agent 的按轮次唤醒事件——pi 扩展、wait CLI、崩溃桥接，以及为你的 worker 起的 Discworld 风格代号 | `ai-agents` `pi` `typescript` | 5 | 🆕 2026-07-24 |
| [**herdr-ntfy**](https://github.com/horn553/herdr-ntfy)<br><sub>horn553</sub> | 依赖极简（jq、curl、sh）——当 Herdr Agent 完成或被阻塞时发送 ntfy 通知 | `shell` | 4 | 2026-07-03 |
| [**herdr-notify-windows**](https://github.com/aclima01/herdr-notify-windows)<br><sub>aclima01</sub> | 面向 herdr Agent 的 Windows 11 提示通知（轮次完成/需要输入） | `powershell` | 3 | 🆕 2026-07-23 |
| [**herdr-telegram-plugin**](https://github.com/mvallebr/herdr-telegram-plugin)<br><sub>mvallebr</sub> | herdr 的 Telegram 机器人伴侣——通过 Telegram 论坛话题远程控制任意 Agent，整个流程中不涉及 LLM | `typescript` | 3 | 🆕 2026-07-27 |
| [**herdr-hail**](https://github.com/natori-hrj/herdr-hail)<br><sub>natori-hrj</sub> | herdr 的 Slack 和 Discord 双向桥接——Agent 被阻塞时会收到提醒，回复或点击即可解除阻塞。无需内网穿透 | `discord` `slack` `typescript` | 2 | 🆕 2026-07-19 |
| [**herdr-guard**](https://github.com/StructuPath/herdr-guard)<br><sub>StructuPath</sub> | Herdr 的跨 Agent 命令策略：审计、警告并中断危险的 shell 命令 | `ai-agents` `command-policy` `security` `terminal` `javascript` | 2 | 🆕 2026-07-28 |
| [**session-sounds**](https://github.com/ChrisPachulski/session-sounds)<br><sub>ChrisPachulski</sub> | 面向 macOS 和 Linux 的 Herdr，为每个 Agent 提供不同的完成提示音和关注提示音 | `coding-agents` `notifications` `rust` | 1 | 🆕 2026-07-19 |
| [**herdr-telegram-bridge**](https://github.com/cokekitten/herdr-telegram-bridge)<br><sub>cokekitten</sub> | 当 herdr Agent 完成或被阻塞时收到 Telegram 推送——直接回复即可将文本或文件发回该 Agent。无需服务器、无需内网穿透、无需 App | `ai-agents` `chatops` `claude-code` `developer-tools` `notifications` | 1 | 🆕 2026-07-26 |
| [**herdr-announcer**](https://github.com/nhclink16/herdr-announcer)<br><sub>nhclink16</sub> | Herdr 插件：Agent 完成或需要输入时，用语音播报一句 LLM 生成的摘要——支持本地 TTS、ElevenLabs 或任意自定义命令 | `tts` `python` | 1 | 🆕 2026-07-24 |
| [**herdr-prompt-reply**](https://github.com/cedrus-8864/herdr-prompt-reply)<br><sub>cedrus-8864</sub> | 直接从 macOS 通知回答 herdr Agent 的权限提示——真实可点击的回答按钮，单一 Swift 二进制文件，后台没有任何驻留进程 | `ai-agents` `claude-code` `macos` `macos-notifications` `notifications` | 0 | 🆕 2026-07-28 |
| [**herdr-slack-notify**](https://github.com/juninaba/herdr-slack-notify)<br><sub>juninaba</sub> | 当 Herdr Agent 完成或被阻塞时发送 Slack 通知 | `javascript` | 0 | 2026-07-07 |
| [**drover-notify**](https://github.com/keinstn/drover-notify)<br><sub>keinstn</sub> | Herdr plugin that sends Drover push notifications when an agent becomes blocked | `javascript` | 0 | 🆕 2026-07-28 |
| [**herdr-telegram-slack-bridge**](https://github.com/lsisoft/herdr-telegram-slack-bridge)<br><sub>lsisoft</sub> | 面向 Herdr Agent 会话的 Telegram 与 Slack 机器人双向桥接——将被阻塞 Agent 的提醒和聊天回复路由回 Herdr 或 tmux 窗格 | `ai-agents` `slack-bot` `telegram-bot` `tmux` `python` | 0 | 🆕 2026-07-28 |
| [**herdr-plugin-telegram-notify**](https://github.com/OiAnthony/herdr-plugin-telegram-notify)<br><sub>OiAnthony</sub> | 当 Agent 完成或被阻塞时发送 Telegram 通知的独立 Herdr 插件 | `javascript` | 0 | 🆕 2026-07-16 |
| [**herdr-apple-music-plugin**](https://github.com/perlporter/herdr-apple-music-plugin)<br><sub>perlporter</sub> | Shows a toast in herdr when the currently playing track changes in Apple Music (macOS) | `shell` | 0 | 🆕 2026-07-28 |
| [**herdr-notify-back**](https://github.com/vjbee/herdr-notify-back)<br><sub>vjbee</sub> | Clickable macOS notifications for Herdr that jump you back to the agent pane that needs you | `macos` `notifications` `terminal` `python` | 0 | 🆕 2026-07-28 |
| [**herdr-cc-mac-notify**](https://github.com/y-hirakaw/herdr-cc-mac-notify)<br><sub>y-hirakaw</sub> | 面向 Claude Code 的 macOS 通知——显示 Agent 真实的最后一条消息，而不只是「完成」 | `claude-code` `macos` `notifications` `python` | 0 | 🆕 2026-07-17 |

[⬆ 返回目的列表](#purposes)

<a id="cat-remote"></a>

## 手机与远程操控

> 想在外出或用手机时监控 Agent，只需回传批准即可

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-remote**](https://github.com/dcolinmorgan/herdr-remote)<br><sub>dcolinmorgan</sub> | 从菜单栏、手机或 Telegram 监控并操控你的 herdr Agent。本地零配置，远程连接提供免费内网穿透，无需 Tailscale | `macos` `mobile` `swift` | 155 | 🆕 2026-07-26 |
| [**collie**](https://github.com/AltanS/collie)<br><sub>AltanS</sub> | 随时随地管理 herdr 的 PWA 应用。支持 Tailnet 访问、推送通知、快捷操作等 | `typescript` | 150 | 🆕 2026-07-29 |
| [**herdr-mobile-relay**](https://github.com/0cv/herdr-mobile-relay)<br><sub>0cv</sub> | 通过手机远程审批和监控 Herdr Agent——面向 Android/iOS 的移动 Web 应用，支持推送通知、二维码配置和多电脑中继 | `android` `approvals` `cloudflare` `ios` `mobile` | 16 | 🆕 2026-07-28 |
| [**herdr-push**](https://github.com/dcolinmorgan/herdr-push)<br><sub>dcolinmorgan</sub> | herdr 插件：零依赖地将事件推送到 herdr-remote，用于手机端监控和一键批准 | `shell` | 6 | 2026-07-09 |
| [**herdr-tether**](https://github.com/moneycaringcoder/herdr-tether)<br><sub>moneycaringcoder</sub> | 即使关闭 Herdr 视图，也能让本地和远程的终端任务继续运行 | `remote-development` `rust` `ssh` `terminal` `tmux` | 5 | 🆕 2026-07-28 |
| [**herdr-aws-ssm**](https://github.com/maayanyosef/herdr-aws-ssm)<br><sub>maayanyosef</sub> | 在 herdr --remote 会话中选择一个 EC2 实例并通过 AWS SSM 连接——无需跳板机或公网 IP | `aws-ssm` `terminal` `shell` | 3 | 2026-07-01 |
| [**herdr-devup**](https://github.com/alon-z/herdr-devup)<br><sub>alon-z</sub> | Herdr 插件：根据 .herdr/dev.toml 生成每个项目的开发布局，并同步隧道 URL 到环境变量 | `typescript` | 2 | 2026-06-22 |
| [**herdr-web**](https://github.com/eyalev/herdr-web)<br><sub>eyalev</sub> | 面向 herdr Agent 多路复用器的移动优先 Web UI——从手机操控你的编程 Agent | `claude-code` `mobile` `pwa` `terminal` `javascript` | 2 | 🆕 2026-07-27 |
| [**herdr-whistle**](https://github.com/amurru/herdr-whistle)<br><sub>amurru</sub> | 用于远程管理 Agent 的 Herdr 插件 | `golang` `telegrambot` `go` | 1 | 2026-07-04 |
| [**merino**](https://github.com/LoneExile/merino)<br><sub>LoneExile</sub> | Merino 🐑 — remote tunnel dashboard for Herdr agents | `go` `macos` `menubar` `react` `wails` | 1 | 🆕 2026-07-29 |
| [**herdr-phone**](https://github.com/matheus3301/herdr-phone)<br><sub>matheus3301</sub> | 通过 Cloudflare Tunnel 和 Access 实现的 Herdr 移动端远程控制台 | `cloudflare-tunnel` `coding-agents` `developer-tools` `golang` `mobile` | 1 | 🆕 2026-07-28 |
| [**herdr-farm**](https://github.com/mejiasd3v/herdr-farm)<br><sub>mejiasd3v</sub> | Herdr plugin: 3D farm that visualizes your Herdr workspaces and agents as livestock (three.js webapp) | `threejs` `javascript` | 1 | 🆕 2026-07-28 |
| [**herdr-approval-gate**](https://github.com/Javamomma/herdr-approval-gate)<br><sub>Javamomma</sub> | herdr 中针对 Agent 操作的人工签核关卡——在专用窗格中运行任务，对其记录进行核验，直到有人输入 「APPROVE <姓名缩写>」 才会解除阻塞 | `shell` | 0 | 🆕 2026-07-15 |
| [**herdr-wechat-plugin**](https://github.com/LuYanFCP/herdr-wechat-plugin)<br><sub>LuYanFCP</sub> | 用于微信远程控制的 Herdr 插件 | `rust` | 0 | 🆕 2026-07-17 |
| [**herdview**](https://github.com/Orchard-Robotics/herdview)<br><sub>Orchard-Robotics</sub> | 从网页查看你的「herd」 | `html` | 0 | 🆕 2026-07-17 |
| [**herdr-web-tui**](https://github.com/tigorlazuardi/herdr-web-tui)<br><sub>tigorlazuardi</sub> | Daemon-first browser/PWA frontend for Herdr with an optional plugin launcher | `go` | 0 | 🆕 2026-07-29 |

[⬆ 返回目的列表](#purposes)

<a id="cat-agents"></a>

## Agent 编排与并行执行

> 想统一启动、分工并管理多个 AI Agent

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**agentbox**](https://github.com/madarco/agentbox)<br><sub>madarco</sub> | 一条命令即可在沙盒虚拟机中并行运行多个 Agent（本地或云端） | `claude` `claude-code` `cli` `cmux` `codex` | 326 | 🆕 2026-07-29 |
| [**agentbox-herdr-plugin**](https://github.com/madarco/agentbox-herdr-plugin)<br><sub>madarco</sub> | 一条命令即可在沙盒虚拟机中并行运行多个 Agent（本地或云端） | `claude-code` `codex-cli` `opencode` `sandbox` `shell` | 19 | 2026-06-24 |
| [**herdmates**](https://github.com/caioniehues/herdmates)<br><sub>caioniehues</sub> | herdr 原生的 Claude Code Agent 团队——teammux 兼容层、任务控制面板、聚焦窗格 | `agent-teams` `claude-code` `rust` `tui` | 11 | 🆕 2026-07-17 |
| [**pi-herd**](https://github.com/ribbons-digital/pi-herd)<br><sub>ribbons-digital</sub> | 结合 Herdr 窗格和 git 工作树，对 Pi 会话进行可视化编排 | `typescript` | 9 | 2026-07-06 |
| [**herdr-board**](https://github.com/nelsonPires5/herdr-board)<br><sub>nelsonPires5</sub> | herdr 的看板工具——卡片就是提示词，会被派发给可见窗格中的 AI Agent | `board` `kanban` `kanban-board` `tui` `rust` | 7 | 🆕 2026-07-27 |
| [**herdr-helpr**](https://github.com/sohanemon/herdr-helpr)<br><sub>sohanemon</sub> | 面向 herdr 的、由提示词驱动的工作区和窗格管理 | `ai-agents` `bun` `cli` `developer-tools` `ink` | 7 | 🆕 2026-07-16 |
| [**herdr-browser**](https://github.com/StructuPath/herdr-browser)<br><sub>StructuPath</sub> | Herdr 的可操控 Agent 浏览器窗格——支持实时流传输、真实交互、自适应渲染、控制台/页面错误显示、录制和 localhost 路由 | `terminal` `javascript` | 7 | 🆕 2026-07-28 |
| [**herdr-agent-handoff**](https://github.com/sanirudh17/herdr-agent-handoff)<br><sub>sanirudh17</sub> | 将进行中的 Agent 会话交接给另一个已安装编程 Agent 的新会话的 Herdr 插件——完整会话直接放入提示词中传递，无需摘要、无需截断记录、无需再写后续提示 | `agent-handoff` `claude-code` `codex` `coding-agents` `developer-tools` | 5 | 🆕 2026-07-29 |
| [**herdr-insight**](https://github.com/0x5c0f/herdr-insight)<br><sub>0x5c0f</sub> | Agent 状态时间线面板 | `rust` | 4 | 2026-06-23 |
| [**shepherdr**](https://github.com/afogel/shepherdr)<br><sub>afogel</sub> | 将委派出去的编程 Agent 收拢到可见、可审查的 herdr 窗格中，供你观察、恢复和接管的 herdr 插件 | `ai-agents` `claude-code` `codex` `cursor` `rust` | 3 | 🆕 2026-07-24 |
| [**herdr-theos-settler**](https://github.com/calebcauthon/herdr-theos-settler)<br><sub>calebcauthon</sub> | 将已完成的 Herdr Agent 标签页和工作区沉到活跃工作下方，让它们不再挡路。Theo 的点子 | `rust` | 3 | 🆕 2026-07-23 |
| [**herdr-triage**](https://github.com/natori-hrj/herdr-triage)<br><sub>natori-hrj</sub> | herdr 的关注度分级——按谁最需要你来排序 Agent；长时间被阻塞的 Agent 会排到最前面 | `ai-agents` `triage` `rust` | 3 | 🆕 2026-07-23 |
| [**herdr-space-scoped-agents**](https://github.com/ShankyJS/herdr-space-scoped-agents)<br><sub>ShankyJS</sub> | 将 Agent 面板范围限定为当前聚焦空间的 herdr 插件 | `coding-agents` `terminal` `go` | 3 | 🆕 2026-07-23 |
| [**herdr-catchup**](https://github.com/wilbeibi/herdr-catchup)<br><sub>wilbeibi</sub> | herdr 的跨 Agent 编程会话交接：从正在运行的窗格中，对 Claude Code、Codex、Cursor、Cline 或 OpenCode 会话进行摘要、分叉，或转交给另一个 Agent | `ai-agents` `claude-code` `codex` `coding-agents` `context-handoff` | 3 | 🆕 2026-07-27 |
| [**herdr-agent-messenger**](https://github.com/aashishd/herdr-agent-messenger)<br><sub>aashishd</sub> | 让运行中的 Herdr 窗格间的 AI Agent 互相发送简明、自成一体的消息——一个 Agent 可以在不共享完整上下文的情况下与另一个协调工作 | `python` | 2 | 2026-07-10 |
| [**herdr-orchestrate**](https://github.com/darjss/herdr-orchestrate)<br><sub>darjss</sub> | 为可见的 Herdr worker 会话提供 Pi 原生编排——运行看板、持久化的提示词/报告/状态、独立的 git 工作树，以及明确的模型路由 | `pi-package` `typescript` | 2 | 2026-07-13 |
| [**herdr-espresso**](https://github.com/Hanyang-Li/herdr-espresso)<br><sub>Hanyang-Li</sub> | 在 Agent 运行时，即使合上盖子也保持 MacBook 唤醒状态 | `rust` | 2 | 🆕 2026-07-25 |
| [**herdr-shame-report**](https://github.com/JYasha11/herdr-shame-report)<br><sub>JYasha11</sub> | 永久记录你让 AI Agent 等了多久的账本。羊会记住的 | `javascript` | 2 | 2026-07-10 |
| [**herdr-swarm**](https://github.com/StructuPath/herdr-swarm)<br><sub>StructuPath</sub> | 在同一仓库上安全并行运行多个编程 Agent：为每个 Agent 分配独立工作树，实时可见变更，Herdr 上以审查优先的方式收获成果 | `terminal` `javascript` | 2 | 🆕 2026-07-28 |
| [**herdr-wakeup**](https://github.com/usrivastava92/herdr-wakeup)<br><sub>usrivastava92</sub> | 在 Herdr 管理的 Agent 工作期间，让 macOS 或 Linux 保持唤醒状态的 Herdr 插件 | `power-management` `sleep-prevention` `wakeup` `rust` | 2 | 🆕 2026-07-17 |
| [**herdr-agent-timer**](https://github.com/Yemeni/herdr-agent-timer)<br><sub>Yemeni</sub> | 让每个 Agent 的状态标签与其耗时交替显示的 Herdr 插件 | `shell` | 2 | 🆕 2026-07-29 |
| [**herdr-pi-reloader**](https://github.com/anrunt/herdr-pi-reloader)<br><sub>anrunt</sub> | 从 Herdr 浮层 TUI 中重新加载或重启闲置的 Pi Agent 会话 | `rust` | 1 | 🆕 2026-07-18 |
| [**herdr-birdseye**](https://github.com/calebcauthon/herdr-birdseye)<br><sub>calebcauthon</sub> | 以鸟瞰视角查看 herdr 中的 Agent | `rust` | 1 | 🆕 2026-07-24 |
| [**herdr-pane-topic-sync**](https://github.com/danbuhler/herdr-pane-topic-sync)<br><sub>danbuhler</sub> | herdr 插件：将窗格和标签页自动命名为每个 Agent（Claude Code、Codex 等）实时的主题，而不是「1」「2」「3」 | `ai-agents` `claude-code` `terminal` `tmux-alternative` `javascript` | 1 | 🆕 2026-07-17 |
| [**herdr-amphetamine-macos**](https://github.com/gw31415/herdr-amphetamine-macos)<br><sub>gw31415</sub> | 在 Agent 工作期间持续为 Amphetamine 续时的 herdr 插件 | `python` | 1 | 2026-07-09 |
| [**herdr-newtab-plus**](https://github.com/jeffarese/herdr-newtab-plus)<br><sub>jeffarese</sub> | 会询问文件夹和 Agent 的 Herdr 新标签页：自动补全真实路径，记住你常用的工作目录，并为你启动 Agent | `python` | 1 | 🆕 2026-07-26 |
| [**herdr-agents-status**](https://github.com/maedana/herdr-agents-status)<br><sub>maedana</sub> | 显示 Herdr Agent 状态的常驻置顶透明浮层——claudeye 的精神续作，专为 Herdr（而非 tmux）打造 | `rust` | 1 | 🆕 2026-07-22 |
| [**herdr-imebox**](https://github.com/Sawakee/herdr-imebox)<br><sub>Sawakee</sub> | 便于向 herdr 中 AI Agent 窗格输入日文/CJK 文字的 IME 友好弹出文本框 | `cjk` `ime` `input-method` `japanese` `ratatui` | 1 | 🆕 2026-07-17 |
| [**herdr-agents-history**](https://github.com/speardragon/herdr-agents-history)<br><sub>speardragon</sub> | 查看你的 AI 编程 Agent 实际在做什么——一个实时、键盘驱动的 herdr TUI，串流展示你所有 Agent（Claude Code 和 Codex）的每一次工具调用 | `ai-agents` `claude-code` `codex` `tui` `typescript` | 1 | 🆕 2026-07-19 |
| [**herdr-conductor**](https://github.com/StructuPath/herdr-conductor)<br><sub>StructuPath</sub> | 将功能交付团队编排为可见的 Herdr Agent 窗格——Conductor 插件 | `orchestration` `javascript` | 1 | 🆕 2026-07-29 |
| [**herdr-agent-office**](https://github.com/suisya-systems/herdr-agent-office)<br><sub>suisya-systems</sub> | 将你的 Agent 团队呈现为像素风办公室的 herdr 插件。查看谁在工作、谁卡住了，并可直接跳转过去 | `python` | 1 | 🆕 2026-07-25 |
| [**tinysend-herdr**](https://github.com/tiny-send/tinysend-herdr)<br><sub>tiny-send</sub> | herdr 插件：当 Agent 阻塞/完成时给自己发邮件，回复即可解除阻塞。由 tinysend 提供支持 | `ai-agents` `tinysend` `javascript` | 1 | 2026-06-26 |
| [**herdr-rovo-dev**](https://github.com/usrivastava92/herdr-rovo-dev)<br><sub>usrivastava92</sub> | 检测 Rovo Dev CLI 会话并将其作为运行中的 Agent 报告给 Herdr 的插件 | `ai-agent` `rovo` `rovo-dev` `shell` | 1 | 🆕 2026-07-19 |
| [**herdr-nudge**](https://github.com/EricBois/herdr-nudge)<br><sub>EricBois</sub> | 为 herdr Agent 设置「继续提醒」——在指定时间，或它变为闲置/被阻塞时触发 | `shell` | 0 | 🆕 2026-07-17 |
| [**herdr-ai-memory**](https://github.com/iagogfe/herdr-ai-memory)<br><sub>iagogfe</sub> | Herdr 插件：通过 ai-memory 管理的工作流启动编程 Agent——实现跨 Agent 的会话连续性 | `ai-agents` `ai-memory` `terminal` `javascript` | 0 | 🆕 2026-07-24 |
| [**herdr-annotations**](https://github.com/IgorWarzocha/herdr-annotations)<br><sub>IgorWarzocha</sub> | 收集对终端选中内容的注释，并暂存到 Herdr Agent 中 | `ai-agents` `annotations` `terminal` `javascript` | 0 | 🆕 2026-07-18 |
| [**herdr-orchestrator**](https://github.com/kylezk777/herdr-orchestrator)<br><sub>kylezk777</sub> | Herdr-orch 是运行在 Herdr 之上的基于文件的 Agent 编排工具 | `agent-orchestration` `orchestrator` `rust` | 0 | 🆕 2026-07-26 |
| [**sheprd**](https://github.com/m-mohamed/sheprd)<br><sub>m-mohamed</sub> | 将 Pi、Codex、Claude Code 和 OpenCode 统一收纳到一个可见且隔离的 Herdr「Flok」中 | `agent-tools` `claude-code` `cli` `codex` `coding-agents` | 0 | 🆕 2026-07-26 |
| [**herdr-alias-setter**](https://github.com/m2selfA/herdr-alias-setter)<br><sub>m2selfA</sub> | Herdr plugin: set pane name + agent alias (quick type-in or full menu) | `powershell` | 0 | 🆕 2026-07-28 |
| [**herdr-agents-bridge**](https://github.com/maedana/herdr-agents-bridge)<br><sub>maedana</sub> | 通过本地移动端友好 Web UI，从手机监控并操作编程 Agent——扫描二维码即可连接 | `rust` | 0 | 🆕 2026-07-22 |
| [**herdr-agent-dash**](https://github.com/MartinBspheroid/herdr-agent-dash)<br><sub>MartinBspheroid</sub> | Herdr Agent Board：一目查看正在运行的编程 Agent 及其状态、工作目录和 Git 上下文的本地键盘优先 Herdr 插件 | `typescript` | 0 | 🆕 2026-07-21 |
| [**herdr-green**](https://github.com/natori-hrj/herdr-green)<br><sub>natori-hrj</sub> | herdr 的按 Agent 显示测试状态——当某个 Agent 完成时运行该项目的测试，并显示通过/失败 | `ai-agents` `ci` `tests` `rust` | 0 | 🆕 2026-07-23 |
| [**herdr-standup**](https://github.com/natori-hrj/herdr-standup)<br><sub>natori-hrj</sub> | herdr 的 Agent 站会摘要——按 Agent 汇总其所在仓库中的提交和未提交的工作 | `ai-agents` `git` `standup` `rust` | 0 | 🆕 2026-07-23 |
| [**herdr-plugin-aos**](https://github.com/noctaIO/herdr-plugin-aos)<br><sub>noctaIO</sub> | 从任意工作区在 herdr 窗格中启动支持 Agentic OS 的 Claude Code Agent。无侵入式 herdr 插件 | `shell` | 0 | 2026-07-11 |
| [**ocean-herdr**](https://github.com/Risingtides-dev/ocean-herdr)<br><sub>Risingtides-dev</sub> | 面向 Herdr 的 Ocean Agent 集成 | `coding-agent` `ocean` `rust` | 0 | 🆕 2026-07-17 |
| [**herdr-want-to-sleep**](https://github.com/scheron/herdr-want-to-sleep)<br><sub>scheron</sub> | A herdr plugin that puts your Mac to sleep once no coding agent is working any more. Arm it before bed and it waits for every agent to settle, then journals wh… | `coding-agents` `macos` `shell` | 0 | 🆕 2026-07-28 |
| [**herdr-achievements**](https://github.com/SerHappy/herdr-achievements)<br><sub>SerHappy</sub> | Achievements and tiny celebrations for your Herdr AI agent herd | `go` | 0 | 🆕 2026-07-28 |
| [**herdr-ask**](https://github.com/TaylorFinklea/herdr-ask)<br><sub>TaylorFinklea</sub> | 面向 Herdr 及任意终端的轻量命令生成与终端聊天 | `cli` `rust` `terminal` `tui` | 0 | 🆕 2026-07-21 |

<details><summary>与此目的也相关</summary>

- [a2u/herdr-jira](https://github.com/a2u/herdr-jira) — herdr 的 Jira TUI 插件——通过可配置的 JQL 过滤器浏览、搜索 issue，修改状态，并一键将 issue 交给终端中运行的 AI Agent 处理

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-worktree"></a>

## git 工作树与分支管理

> 想为每项工作单独开一个工作树，收尾清理也自动完成

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-worktrunk**](https://github.com/devashish2203/herdr-worktrunk)<br><sub>devashish2203</sub> | 集成 worktrunk 以管理 git 工作树的 Herdr 插件 | `shell` | 62 | 🆕 2026-07-24 |
| [**herdr-plugin-jj-workspace**](https://github.com/NathanFlurry/herdr-plugin-jj-workspace)<br><sub>NathanFlurry</sub> | 将 Jujutsu (jj) 工作区作为 Herdr 工作区进行创建和删除 | `jujutsu` `rust` | 36 | 2026-07-08 |
| [**herdr-worktree-from-pr**](https://github.com/tdi/herdr-worktree-from-pr)<br><sub>tdi</sub> | 从 GitHub PR 创建 git 工作树，并作为 herdr 工作区打开 | `javascript` | 6 | 🆕 2026-07-20 |
| [**herdr-plugin-renamer**](https://github.com/wyattjoh/herdr-plugin-renamer)<br><sub>wyattjoh</sub> | 根据 Agent 的第一条提示词，重命名自动生成的 herdr 工作树分支和工作区（通过设备端 Apple FoundationModels 或 Codex） | `rust` | 5 | 🆕 2026-07-27 |
| [**jj-waltz**](https://github.com/EzraCerpac/jj-waltz)<br><sub>EzraCerpac</sub> | 受 Worktrunk 启发的 Jujutsu 工作区切换工具 | `cli` `jj` `jujitsu` `utility` `workspace` | 4 | 🆕 2026-07-28 |
| [**herdr-fresh-worktree**](https://github.com/persiyanov/herdr-fresh-worktree)<br><sub>persiyanov</sub> | 将新创建的 herdr 工作树重置为 origin 默认分支的最新状态 | `javascript` | 4 | 2026-06-25 |
| [**herdr-worktreeinclude**](https://github.com/tanshio/herdr-worktreeinclude)<br><sub>tanshio</sub> | Herdr 插件：将匹配 .worktreeinclude 的被 gitignore 文件复制到新创建的工作树中 | `worktree` `worktreeiclude` `shell` | 4 | 2026-07-11 |
| [**herdr-plugin-git-worktree-hooks**](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks)<br><sub>freethinkel</sub> | 在创建/移除 git 工作树时运行 shell 命令——一份 YAML 配置适用于所有项目，放在任何仓库之外 | `git-worktree` `javascript` | 3 | 2026-07-06 |
| [**herdr-symlink-worktree**](https://github.com/hmu332233/herdr-symlink-worktree)<br><sub>hmu332233</sub> | 将主仓库中的共享本地文件符号链接到新工作树中的 herdr 插件 | `shell` | 3 | 🆕 2026-07-16 |
| [**herdr-worktree-seed**](https://github.com/jlimas/herdr-worktree-seed)<br><sub>jlimas</sub> | 为新工作树植入 copy-on-write 的 node_modules 和可配置本地 dotfiles 的 Herdr 插件 | `developer-tools` `dotfiles` `git-worktree` `nodejs` `typescript` | 3 | 🆕 2026-07-28 |
| [**herdr-branch-cleanup**](https://github.com/osolmaz/herdr-branch-cleanup)<br><sub>osolmaz</sub> | 当窗格所在分支在 GitHub 上被合并或删除后，自动切换到默认分支 | `git` `github` `rust` | 3 | 🆕 2026-07-26 |
| [**herdr-worktree-lifecycle**](https://github.com/qdentity/herdr-worktree-lifecycle)<br><sub>qdentity</sub> | Herdr 插件：将工作树生命周期事件分发给仓库自带的初始化/清理脚本 | `rust` | 3 | 2026-06-29 |
| [**herdr-worktree-hooks**](https://github.com/timofey-TK/herdr-worktree-hooks)<br><sub>timofey-TK</sub> | herdr 插件：在创建、打开或删除 git 工作树时运行自定义的初始化/清理命令 | `developer-tools` `git-worktree` `worktree` `python` | 3 | 🆕 2026-07-17 |
| [**herdr-remote-worktrunk**](https://github.com/ditwrd/herdr-remote-worktrunk)<br><sub>ditwrd</sub> | Herdr 的远程 worktrunk 工作区 | `shell` | 2 | 2026-07-10 |
| [**herdr-worktreeinclude**](https://github.com/serhii-chernenko/herdr-worktreeinclude)<br><sub>serhii-chernenko</sub> | 允许为新工作树指定自定义路径，并像 Claude CLI 一样遵循 `.worktreeinclude` 文件 | `worktree` `shell` | 2 | 🆕 2026-07-23 |
| [**herdr-allow**](https://github.com/Feasy01/herdr-allow)<br><sub>Feasy01</sub> | herdr 插件：通过 .herdr-allow 允许列表，将被 gitignore 的文件（.env、密钥、本地配置）复制到每个新工作树中 | `shell` | 1 | 2026-07-02 |
| [**herdr-plugin-gwm**](https://github.com/kbrdn1/herdr-plugin-gwm)<br><sub>kbrdn1</sub> | 驱动 gwm 来管理 git 工作树的 herdr 插件——gwm 保持权威数据源，herdr 只是采纳它 | `bash` `cli` `git-worktree` `gwm` `worktree` | 1 | 🆕 2026-07-27 |
| [**herdr-worktree-provisioner**](https://github.com/arjenblokzijl/herdr-worktree-provisioner)<br><sub>arjenblokzijl</sub> | 在新工作树自己的可见窗格中运行按仓库定制的初始化——可组合，无需守卫检查 | `bootstrap` `git-worktree` `worktree` `shell` | 0 | 2026-07-08 |
| [**herdr-worktree-copy**](https://github.com/crexi/herdr-worktree-copy)<br><sub>crexi</sub> | Herdr plugin that copies and symlinks worktree-local files from a .worktree-copy manifest | `git-worktree` `shell` | 0 | 🆕 2026-07-28 |
| [**herdr-deck**](https://github.com/ctbaum/herdr-deck)<br><sub>ctbaum</sub> | herdr-agents.nvim 的搭配工作区启动器：在预先搭好的 Neovim、Agent、shell 和 lazygit 组合面板中打开或恢复 Claude 和 Codex | `claude-code` `codex` `coding-agents` `git-worktree` `neovim` | 0 | 🆕 2026-07-24 |
| [**trunkr**](https://github.com/disintegrator/trunkr)<br><sub>disintegrator</sub> | Herdr 🤝 Worktrunk | `go` | 0 | 🆕 2026-07-28 |
| [**herdr-worktreeinclude**](https://github.com/eightHundreds/herdr-worktreeinclude)<br><sub>eightHundreds</sub> | Herdr 插件：将 .worktreeinclude 指定的被 gitignore 文件复制到新工作树中 | `worktree` `rust` | 0 | 🆕 2026-07-28 |
| [**herdr-title**](https://github.com/filoozom/herdr-title)<br><sub>filoozom</sub> | 在终端标签页标题中显示所选工作树和 Agent 活动状态的 Herdr 插件 | `rust` | 0 | 🆕 2026-07-24 |
| [**gren-herdr**](https://github.com/langtind/gren-herdr)<br><sub>langtind</sub> | 通过 gren 创建、切换和删除 git 工作树的 herdr 插件——支持 gren 的创建后初始化 | `git-worktree` `gren` `shell` | 0 | 🆕 2026-07-22 |
| [**herdr-jj-status**](https://github.com/mroth/herdr-jj-status)<br><sub>mroth</sub> | herdr 插件：在空间侧边栏中显示 jj 工作区的 Jujutsu 书签/状态 | `shell` | 0 | 🆕 2026-07-28 |

<details><summary>与此目的也相关</summary>

- [tdi/herdr-worktree-from-linear](https://github.com/tdi/herdr-worktree-from-linear) — 从 Linear issue 创建 git 工作树，并作为 herdr 工作区打开
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — 为 JavaScript 和 TypeScript 自动初始化 Herdr 工作树，支持基于锁文件的安装和安全的环境变量还原
- [simoncrypta/agentic-dev-setup](https://github.com/simoncrypta/agentic-dev-setup) — 面向 Agent 化编程工作流的、可共享的 Herdr + worktrunk 开发布局
- [tomasvarga/herdr-e2b](https://github.com/tomasvarga/herdr-e2b) — 按需将 git 工作树镜像到全新的 E2B 云沙盒——直接上传快照（包括未提交的更改），无需 push 或 clone。一个 herdr 插件
- [snics/herdr-worktree-from-gitlab](https://github.com/snics/herdr-worktree-from-gitlab) — herdr 插件：从 GitLab issue（通过 glab）创建 git 工作树和工作区

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-review"></a>

## 代码审查与差异对比

> 想阅读 Agent 写的差异并对其发表评论

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**crabbox**](https://github.com/openclaw/crabbox)<br><sub>openclaw</sub> | Crabbox：预热沙盒、同步差异、运行测试套件 | `agent-skills` `remote-test-runner` `go` | 1228 | 🆕 2026-07-28 |
| [**herdr-reviewr**](https://github.com/persiyanov/herdr-reviewr)<br><sub>persiyanov</sub> | herdr 的代码审查 + 文件查看器侧边栏——对 Agent 的差异发表评论并打回。同时提供 PR 及其检查、评论的只读视图 | `code-review` `rust` `tui` | 265 | 🆕 2026-07-28 |
| [**herdr-plugin-hunk**](https://github.com/edmundmiller/herdr-plugin-hunk)<br><sub>edmundmiller</sub> | 在分屏窗格或标签页中打开 Hunk 差异对比的 Herdr 插件 | `python` | 10 | 2026-06-23 |
| [**herdr-pickr**](https://github.com/tomasvarga/herdr-pickr)<br><sub>tomasvarga</sub> | herdr 的 PR 审查路由器——按住 Ctrl 点击 GitHub PR / GitLab MR 链接，选择审查工具（tuicr · hunk · diff · 浏览器 · 或自定义工具），可选启用 AI 初审 | `cli` `code-review` `pull-request` `tui` `shell` | 10 | 2026-07-13 |
| [**herdr-plannotator**](https://github.com/plannotator/herdr-plannotator)<br><sub>plannotator</sub> | Open Plannotator reviews inside Herdr Browser panes. | `plannotator` `typescript` | 4 | 🆕 2026-07-28 |
| [**herdr-plugin-hunk-autodiff**](https://github.com/scott306lr/herdr-plugin-hunk-autodiff)<br><sub>scott306lr</sub> | Herdr 插件：当编程 Agent 完成任务但留有未提交更改时，自动打开 hunk 差异分屏 | `claude-code` `hunk` `python` | 4 | 2026-07-05 |
| [**herdr-hunk**](https://github.com/yuucu/herdr-hunk)<br><sub>yuucu</sub> | herdr 插件：为你的 Agent 工作区切换 Hunk 差异审查 | `diff` `hunk` `go` | 2 | 🆕 2026-07-20 |
| [**herdr-peer-review**](https://github.com/Elio2000/herdr-peer-review)<br><sub>Elio2000</sub> | 在 herdr 窗格中打开第二个编程 Agent 来审查你的差异——可观察、自动批准、只读。附带用于「审查↔修改↔决策」自主循环的 Claude Code skill | `agent-skills` `ai-agents` `claude-code` `code-review` `codex` | 1 | 🆕 2026-07-16 |
| [**herdr-git-graph**](https://github.com/jorge-huxley/herdr-git-graph)<br><sub>jorge-huxley</sub> | Herdr 的只读 git 图谱 TUI 插件，支持彩色 ASCII 分支线、分支过滤、搜索和按需查看差异 | `rust` | 1 | 🆕 2026-07-17 |
| [**herdr-hunk-gh-diff**](https://github.com/Allianaab2m/herdr-hunk-gh-diff)<br><sub>Allianaab2m</sub> | Herdr 插件：在当前窗格所在分支与其 GitHub 拉取请求的目标分支之间打开 Hunk 差异 | `python` | 0 | 🆕 2026-07-15 |
| [**herdr-stagr**](https://github.com/brianh20/herdr-stagr)<br><sub>brianh20</sub> | Source Control sidebar for herdr: stage, unstage, and discard with side-by-side diffs | `git` `tui` `rust` | 0 | 🆕 2026-07-29 |
| [**herdr-hunk**](https://github.com/cevr/herdr-hunk)<br><sub>cevr</sub> | Send Hunk review notes to the correct Herdr agent pane | `effect-ts` `hunk` `typescript` | 0 | 🆕 2026-07-28 |
| [**herdr-gitview**](https://github.com/ChmaraX/herdr-gitview)<br><sub>ChmaraX</sub> | herdr 的 Git 状态/差异面板——审查更改、在 nvim 中编辑、暂存/提交/丢弃，全部在终端内完成 | `git` `git-diff` `git-tui` `neovim` `rust` | 0 | 🆕 2026-07-26 |
| [**herdr-plan-code-review**](https://github.com/inxx/herdr-plan-code-review)<br><sub>inxx</sub> | herdr 插件：Opus 做计划，Sonnet 写代码，Claude+Codex 做审查——一个操作打开四个 Agent 窗格 | `claude-code` `codex` `terminal` `shell` | 0 | 2026-07-06 |
| [**herdr-file-explore**](https://github.com/kylezk777/herdr-file-explore)<br><sub>kylezk777</sub> | 在 herdr 窗格中运行的只读代码浏览与审查 TUI | `diff` `file-viewer` `git` `rust` | 0 | 🆕 2026-07-27 |
| [**herdr-idle-panes**](https://github.com/leonho/herdr-idle-panes)<br><sub>leonho</sub> | herdr 插件：以清单弹窗形式查看并关闭停留在闲置 shell 的窗格 | `python` | 0 | 🆕 2026-07-18 |
| [**herdr-roborev**](https://github.com/phin-tech/herdr-roborev)<br><sub>phin-tech</sub> | 在 Herdr 窗格中打开 roborev 的审查 TUI | `shell` | 0 | 🆕 2026-07-21 |
| [**herdr-review**](https://github.com/quantk/herdr-review)<br><sub>quantk</sub> | Review agent-authored changes in Hunk and send inline feedback back through Herdr | `code-review` `hunk` `javascript` | 0 | 🆕 2026-07-28 |

<details><summary>与此目的也相关</summary>

- [JacquesvanWyk/herdr-hunk](https://github.com/JacquesvanWyk/herdr-hunk) — herdr 中用于 Hunk 差异对比的交互式 fzf 选择器：支持提交、范围、stash，并可在 Agent 完成时自动打开
- [tomasvarga/herdr-sniffr](https://github.com/tomasvarga/herdr-sniffr) — 在你审查之前，AI 先嗅探你的 PR 有没有问题——一个 Agent 化的初审，将草稿评论投放到 tuicr。不限定 Agent（codex/claude/cursor/grok/…）
- [krzysztoff1/herdr-cull](https://github.com/krzysztoff1/herdr-cull) — 查看并关闭 herdr 中闲置的 Agent 窗格——fzf 多选，未经确认绝不关闭

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-forge"></a>

## GitHub / issue 跟踪工具集成

> 想以 issue 或 PR 为起点开始工作，并追踪 PR 状态

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**ghzinga**](https://github.com/osolmaz/ghzinga)<br><sub>osolmaz</sub> | 用于查看单个 GitHub issue 或 PR 的简易可点击 TUI，用 Rust 编写 | `rust` | 64 | 🆕 2026-07-26 |
| [**herdr-plugin-github-start**](https://github.com/ogulcancelik/herdr-plugin-github-start)<br><sub>ogulcancelik</sub> | 从 GitHub issue、PR 或讨论中启动 Codex 或 Claude 的 Herdr 插件 | `javascript` | 15 | 2026-06-30 |
| [**herdr-plugin-gh-pr**](https://github.com/wyattjoh/herdr-plugin-gh-pr)<br><sub>wyattjoh</sub> | 在侧边栏显示当前聚焦 Agent 窗格所在分支的 GitHub PR 状态的 herdr 插件 | `typescript` | 13 | 🆕 2026-07-16 |
| [**herdr-worktree-from-linear**](https://github.com/tdi/herdr-worktree-from-linear)<br><sub>tdi</sub> | 从 Linear issue 创建 git 工作树，并作为 herdr 工作区打开 | `javascript` | 11 | 🆕 2026-07-22 |
| [**herdr-pr-tracker**](https://github.com/Matovidlo/herdr-pr-tracker)<br><sub>Matovidlo</sub> | herdr 插件：追踪每个 Claude Code 会话产生的 GitHub PR，附带 gh 状态和操作 | `claude-code` `shell` | 8 | 🆕 2026-07-21 |
| [**herdr-jira**](https://github.com/a2u/herdr-jira)<br><sub>a2u</sub> | herdr 的 Jira TUI 插件——通过可配置的 JQL 过滤器浏览、搜索 issue，修改状态，并一键将 issue 交给终端中运行的 AI Agent 处理 | `ai-agents` `jira` `ratatui` `rust` `tui` | 6 | 🆕 2026-07-18 |
| [**herdr-linear**](https://github.com/JacquesvanWyk/herdr-linear)<br><sub>JacquesvanWyk</sub> | 在 herdr 分屏窗格或标签页中运行的 fzf 驱动 Linear 面板：搜索 issue、深入项目、创建 issue、修改状态 | `shell` | 6 | 2026-07-12 |
| [**herdr-plugin-github-dash**](https://github.com/kukv/herdr-plugin-github-dash)<br><sub>kukv</sub> | 用于浏览和管理 GitHub 拉取请求与 issue 的 Herdr 插件 | `cli` `github` `go` | 4 | 🆕 2026-07-25 |
| [**herdr-plugin-gh-workflow**](https://github.com/kkckkc/herdr-plugin-gh-workflow)<br><sub>kkckkc</sub> | 用于 GitHub workflow 的 Herdr 插件 | `javascript` | 3 | 2026-07-03 |
| [**herdr-git-status**](https://github.com/krystof018/herdr-git-status)<br><sub>krystof018</sub> | 在 herdr 内呈现 CI 状态——同时支持 GitLab（流水线+合并请求）和 GitHub（Actions+拉取请求），根据仓库的 origin 自动识别 | `bash` `ci-cd` `ci-status` `developer-tools` `github-actions` | 3 | 2026-07-01 |
| [**mergr**](https://github.com/jsmenzies/mergr)<br><sub>jsmenzies</sub> | GitHub pull request status for Herdr Space sidebar rows. | `github-pull-requests` `javascript` | 2 | 🆕 2026-07-28 |
| [**herdr-dashboard**](https://github.com/chouxcreams/herdr-dashboard)<br><sub>chouxcreams</sub> | herdr 工作区的 PR 状态仪表盘 TUI——一目了然地查看每个窗格对应的 PR 状态/CI/审查情况 | `dashboard` `github` `pull-requests` `ratatui` `rust` | 1 | 🆕 2026-07-28 |
| [**herdr-plugin-dotfiles-github-link-preview**](https://github.com/edmundmiller/herdr-plugin-dotfiles-github-link-preview)<br><sub>edmundmiller</sub> | 在侧边窗格中预览 GitHub issue 和拉取请求的 Herdr 插件 | `python` | 1 | 2026-06-23 |
| [**herdr-sniffr**](https://github.com/tomasvarga/herdr-sniffr)<br><sub>tomasvarga</sub> | 在你审查之前，AI 先嗅探你的 PR 有没有问题——一个 Agent 化的初审，将草稿评论投放到 tuicr。不限定 Agent（codex/claude/cursor/grok/…） | `ai` `cli` `code-review` `pull-request` `tuicr` | 1 | 🆕 2026-07-14 |
| [**herdr-pr-preview**](https://github.com/juninaba/herdr-pr-preview)<br><sub>juninaba</sub> | 在分屏窗格中预览当前分支的 GitHub 拉取请求的 Herdr 插件 | `shell` | 0 | 2026-07-08 |
| [**github-issue-herdr-plugin**](https://github.com/nyanyaon/github-issue-herdr-plugin)<br><sub>nyanyaon</sub> | 用于「牧养」GitHub issue 的 Claude Code 插件 | `rust` | 0 | 🆕 2026-07-27 |
| [**herdr-worktree-from-gitlab**](https://github.com/snics/herdr-worktree-from-gitlab)<br><sub>snics</sub> | herdr 插件：从 GitLab issue（通过 glab）创建 git 工作树和工作区 | `gitlab` `rust` `worktree` | 0 | 2026-07-09 |

<details><summary>与此目的也相关</summary>

- [tomasvarga/herdr-pickr](https://github.com/tomasvarga/herdr-pickr) — herdr 的 PR 审查路由器——按住 Ctrl 点击 GitHub PR / GitLab MR 链接，选择审查工具（tuicr · hunk · diff · 浏览器 · 或自定义工具），可选启用 AI 初审
- [tdi/herdr-worktree-from-pr](https://github.com/tdi/herdr-worktree-from-pr) — 从 GitHub PR 创建 git 工作树，并作为 herdr 工作区打开

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-layout"></a>

## 工作区与布局搭建

> 打开项目时，希望标签页、窗格和启动命令一次性就位

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-spreader**](https://github.com/yuk1ty/herdr-spreader)<br><sub>yuk1ty</sub> | 从一个 YAML 文件启动整套 herdr 工作区布局——标签页、窗格、命令，一次搞定 | `rust` | 54 | 🆕 2026-07-16 |
| [**herdr-sessionizer**](https://github.com/andrewchng/herdr-sessionizer)<br><sub>andrewchng</sub> | 通过模糊搜索打开项目和工作树，再从声明式 TOML 布局（标签页、窗格分割、命令、按仓库覆盖配置）启动工作区 | `typescript` | 23 | 🆕 2026-07-26 |
| [**herdr-plugin-workspace-manager**](https://github.com/razajamil/herdr-plugin-workspace-manager)<br><sub>razajamil</sub> | 声明式的标签页/窗格布局，创建工作树时自动应用每个工作区的默认设置 | `rust` | 22 | 🆕 2026-07-25 |
| [**seshagy**](https://github.com/lmilojevicc/seshagy)<br><sub>lmilojevicc</sub> | 面向 tmux 和 herdr 的 Agent 感知会话管理器——发现项目、启动会话、追踪 AI Agent 的工作 | `bubbletea` `go` `session-management` `session-manager` `terminal` | 9 | 🆕 2026-07-23 |
| [**herdr-muster**](https://github.com/marcoskichel/herdr-muster)<br><sub>marcoskichel</sub> | 面向 herdr 的、感知 Agent 状态的项目切换器 | `rust` | 4 | 2026-07-03 |
| [**herdr-setup-bootstrap**](https://github.com/shizlie/herdr-setup-bootstrap)<br><sub>shizlie</sub> | 根据 worktree_init.toml 初始化新工作树的 Herdr 插件 | `shell` | 3 | 2026-06-17 |
| [**herdr-pane-layouts**](https://github.com/iurysza/herdr-pane-layouts)<br><sub>iurysza</sub> | 面向 Herdr 的无缝 tmux 风格窗格调整大小和布局 | `pane-layout` `python` `terminal` | 2 | 🆕 2026-07-17 |
| [**agentic-dev-setup**](https://github.com/simoncrypta/agentic-dev-setup)<br><sub>simoncrypta</sub> | 面向 Agent 化编程工作流的、可共享的 Herdr + worktrunk 开发布局 | `shell` | 2 | 🆕 2026-07-28 |
| [**herdr-layout-tools**](https://github.com/edouard-andrei/herdr-layout-tools)<br><sub>edouard-andrei</sub> | herdr 插件：原地重塑布局（主窗格居左+网格）并均分——标签页 ID 和窗格 ID 保持不变，进程也得以保留 | `javascript` | 1 | 2026-07-08 |
| [**herdr-google-calendar**](https://github.com/Tomatio13/herdr-google-calendar)<br><sub>Tomatio13</sub> | herdr-gog-calendar 是面向终端工作区工具 herdr 的 Google 日历集成插件 | `shell` | 1 | 🆕 2026-07-22 |
| [**herdr-google-gmail**](https://github.com/Tomatio13/herdr-google-gmail)<br><sub>Tomatio13</sub> | herdr-google-gmail 是面向终端工作区工具 herdr 的 Gmail 集成插件 | `shell` | 1 | 🆕 2026-07-22 |
| [**herdr-clone-layout**](https://github.com/danilolucasmd/herdr-clone-layout)<br><sub>danilolucasmd</sub> | 将你当前的工作区布局克隆到每个新的 herdr 工作树。无需模板、无需配置——你当前所在的布局本身就是模板 | `shell` | 0 | 🆕 2026-07-27 |
| [**herdr-plugin-dotfiles-dev-layout**](https://github.com/edmundmiller/herdr-plugin-dotfiles-dev-layout)<br><sub>edmundmiller</sub> | 用于打开我的 dotfiles 开发工作区布局的 Herdr 插件 | `python` | 0 | 2026-06-23 |
| [**herdr-warp**](https://github.com/HexSleeves/herdr-warp)<br><sub>HexSleeves</sub> | 将 Herdr 工作区作为原生 Warp 窗格打开 | `shell` | 0 | 🆕 2026-07-25 |
| [**herdr-gateway**](https://github.com/osuki-dev/herdr-gateway)<br><sub>osuki-dev</sub> | Herdr Gateway exposes a small HTTP API for reading Herdr workspaces, tabs, panes, agents, pane output, and sending pane input. It talks to the local Herdr sock… | `rust` | 0 | 🆕 2026-07-22 |
| [**herdr-lastfocus**](https://github.com/pedrobarco/herdr-lastfocus)<br><sub>pedrobarco</sub> | herdr 的 tmux 风格「上一个活跃」窗格/标签页/工作区切换——通过聚焦事件历史守护进程实现 | `terminal-multiplexer` `tmux` `go` | 0 | 🆕 2026-07-25 |
| [**herdr-compose**](https://github.com/ropali/herdr-compose)<br><sub>ropali</sub> | herdr-compose 是面向 Herdr 的声明式工作区布局管理器 | `layout-manager` `python` | 0 | 🆕 2026-07-25 |
| [**herdr-active-agent-jump**](https://github.com/shoaibkhanz/herdr-active-agent-jump)<br><sub>shoaibkhanz</sub> | herdr 插件：按布局顺序前后循环聚焦正在进行中（工作中/被阻塞）的 Agent——作为 attention-jump 的 vim 风格补充 | `javascript` | 0 | 2026-07-12 |
| [**reasonix-herdr**](https://github.com/uuie/reasonix-herdr)<br><sub>uuie</sub> | 在 Herdr 内提供实时生命周期报告和工作区控制的原生 Reasonix 插件 | `reasonix` `python` | 0 | 2026-07-10 |

<details><summary>与此目的也相关</summary>

- [fullerzz/herdr-plugin-sesh](https://github.com/fullerzz/herdr-plugin-sesh) — 面向 Herdr 的 Sesh 风格工作区选择器 TUI，集成 zoxide，可从常用目录创建工作区
- [ntindle/herdr-resurrect](https://github.com/ntindle/herdr-resurrect) — herdr 的 tmux-resurrect——快照工作区、标签页、窗格、当前目录、运行中的程序和 Agent，并在崩溃或重启后恢复
- [salkhalil/herdr-sessionizer](https://github.com/salkhalil/herdr-sessionizer) — herdr 的 tmux-sessionizer：用 fzf 搜索已打开的工作区和 zoxide 目录，创建或聚焦并附带模板标签页
- [aliou/herdr-cast](https://github.com/aliou/herdr-cast) — Personal Herdr plugin for native macOS agent notifications, fuzzy workspace navigation, zoxide-backed workspa…
- [willfish/herdr-workspacex](https://github.com/willfish/herdr-workspacex) — Rust 原生的模糊 Herdr 工作区切换器，支持基于 zoxide 的工作区创建

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-navigate"></a>

## 窗格导航与快捷键

> 想用和编辑器一样的快捷键在窗格、工作区之间移动和调整大小

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**vim-herdr-navigation**](https://github.com/paulbkim-dev/vim-herdr-navigation)<br><sub>paulbkim-dev</sub> | 用 Ctrl+h/j/k/l 在 herdr 窗格与 Vim/Neovim 分屏之间无缝导航——vim-tmux-navigator 的 herdr 移植版 | `neovim` `vim` `shell` | 58 | 2026-07-07 |
| [**herdr-splits.nvim**](https://github.com/lmilojevicc/herdr-splits.nvim)<br><sub>lmilojevicc</sub> | 面向 Herdr 和 Neovim 的智能分屏导航与调整大小 | `lua` `neovim` `neovim-plugin` `neovim-plugins` `nvim` | 33 | 🆕 2026-07-20 |
| [**herdr-floax**](https://github.com/Tyru5/herdr-floax)<br><sub>Tyru5</sub> | herdr 的浮动临时终端——类似 tmux-floax 风格的可切换弹窗，每个工作区一个，会话持久保存 | `rust` `terminal` `tmux-floax` | 16 | 🆕 2026-07-26 |
| [**herdr-last-workspace**](https://github.com/third774/herdr-last-workspace)<br><sub>third774</sub> | 用于切换回上一个聚焦的工作区的插件 | `rust` | 11 | 2026-06-22 |
| [**herdr-pane-mover**](https://github.com/osamahbeig/herdr-pane-mover)<br><sub>osamahbeig</sub> | herdr 的可点击浮层菜单：跨标签页和工作区移动、重新分割或交换窗格 | `terminal` `tui` `javascript` | 6 | 2026-07-10 |
| [**herdr-recent-navigator**](https://github.com/beyondlex/herdr-recent-navigator)<br><sub>beyondlex</sub> | 面向 Herdr 的最近工作区/标签页/窗格切换器。弹出窗口列出最近聚焦过的工作区、标签页、窗格和 AI Agent，支持模糊搜索和键盘导航 | `agent` `mru` `navigator` `pane` `popup` | 5 | 🆕 2026-07-28 |
| [**herdr-toggle-popup**](https://github.com/maro114510/herdr-toggle-popup)<br><sub>maro114510</sub> | 一个快捷键即可切换浮层弹窗终端的 Herdr 插件 | `go` | 5 | 🆕 2026-07-28 |
| [**herdr-scratch**](https://github.com/AkashJana18/herdr-scratch)<br><sub>AkashJana18</sub> | 面向 Herdr 的持久化速记板，为浮动实用窗格铺路 | `cli` `rust` `scratchpad` | 3 | 2026-07-06 |
| [**herdr-annotations**](https://github.com/jagzmz/herdr-annotations)<br><sub>jagzmz</sub> | 通过快速的本地优先弹窗和可复用的收藏集，为 Herdr 中选中的终端文本添加注释 | `annotations` `cli` `coding-agents` `developer-tools` `local-first` | 3 | 🆕 2026-07-16 |
| [**herdr-harpoon**](https://github.com/KonstantinKai/herdr-harpoon)<br><sub>KonstantinKai</sub> | herdr 的 Harpoon：给窗格打标记，按编号跳转。纯 Bash 实现，无需构建 | `bash` `harpoon` `tmux-harpoon` `shell` | 3 | 🆕 2026-07-29 |
| [**herdr-equalize-splits**](https://github.com/markhuot/herdr-equalize-splits)<br><sub>markhuot</sub> | herdr 插件：将当前标签页中所有分屏按行/列均分尺寸（绑定到 Ctrl+b =） | `terminal` `tmux` `javascript` | 3 | 2026-07-08 |
| [**herdr-command-center**](https://github.com/speardragon/herdr-command-center)<br><sub>speardragon</sub> | 一个快捷键统管所有命令——一个列出你注册命令的 herdr 弹窗，用方向键或数字执行，并在命令触发前自动关闭 | `command-palette` `nodejs` `terminal` `toml` `tui` | 3 | 🆕 2026-07-29 |
| [**herdr-equalize-vsplit**](https://github.com/devoc09/herdr-equalize-vsplit)<br><sub>devoc09</sub> | 将当前窗格向右分屏并均分列宽的 Herdr 插件 | `go` | 2 | 🆕 2026-07-15 |
| [**herdr-convo-index**](https://github.com/dzwduan/herdr-convo-index)<br><sub>dzwduan</sub> | herdr 中 Claude Code 窗格的轮次索引——跳转到任意历史轮次并在弹窗中查看 | `python` | 2 | 🆕 2026-07-27 |
| [**herdr-unread-marker**](https://github.com/JoanGil/herdr-unread-marker)<br><sub>JoanGil</sub> | 通过快捷键手动将聚焦中的 Agent 标记为已读/未读（仅支持手动） | `shell` | 2 | 🆕 2026-07-17 |
| [**herdr-attention**](https://github.com/milkyskies/herdr-attention)<br><sub>milkyskies</sub> | herdr 插件：按一个键即可跳转到下一个需要关注的 Agent（先是被阻塞的，然后是已完成的） | `javascript` | 2 | 2026-07-08 |
| [**herdr-logbook**](https://github.com/Resetnak/herdr-logbook)<br><sub>Resetnak</sub> | 终端的工作记忆——离线、以 Markdown 为主的笔记、决策记录，以及 Herdr 的当前任务 now.md | `adr` `bubbletea` `cli` `go` `markdown` | 2 | 🆕 2026-07-28 |
| [**herdr-navigator**](https://github.com/willfish/herdr-navigator)<br><sub>willfish</sub> | 面向 Vim/Neovim 感知窗格移动的 Herdr 端导航操作 | `navigation` `neovim` `rust` | 2 | 2026-07-07 |
| [**nvim-herdr-navigation**](https://github.com/bojackduy/nvim-herdr-navigation)<br><sub>bojackduy</sub> | vim-tmux-navigator 风格的 ctrl+h/j/k/l，在 Neovim 分屏和 Herdr 窗格之间导航 | `keyboard-shortcuts` `lazyvim` `lua` `navigation` `neovim` | 1 | 🆕 2026-07-20 |
| [**herdr-plugin-tiles**](https://github.com/carsonjones/herdr-plugin-tiles)<br><sub>carsonjones</sub> | 面向 herdr 的简易窗格管理器 | `python` | 1 | 2026-06-19 |
| [**herdr-last-tab**](https://github.com/dantehemerson/herdr-last-tab)<br><sub>dantehemerson</sub> | 用于切换回上一个聚焦的标签页的插件 | `rust` | 1 | 2026-07-07 |
| [**herdr-omnisearch**](https://github.com/dmnkf/herdr-omnisearch)<br><sub>dmnkf</sub> | 为 Herdr 工作区、窗格和已归档 Agent 会话提供快速本地搜索与导航 | `python` | 1 | 🆕 2026-07-24 |
| [**herdr-easymotion**](https://github.com/elliotekj/herdr-easymotion)<br><sub>elliotekj</sub> | 🦘 在 Herdr 窗格之间直接跳转 | `javascript` | 1 | 🆕 2026-07-20 |
| [**herdr-break-pane**](https://github.com/iuhoay/herdr-break-pane)<br><sub>iuhoay</sub> | 将聚焦窗格移动到新标签页的小型 Herdr 插件 | `pane` `javascript` | 1 | 🆕 2026-07-27 |
| [**herdr-popupx**](https://github.com/jeromychu23/herdr-popupx)<br><sub>jeromychu23</sub> | 面向 Herdr 的持久化原生浮动速记弹窗 | `rust` `terminal` `tui` | 1 | 🆕 2026-07-21 |
| [**herdr-nav-history**](https://github.com/jugyo/herdr-nav-history)<br><sub>jugyo</sub> | 面向 herdr 的浏览器风格前进/后退导航（针对窗格、标签页、工作区的聚焦历史） | `javascript` | 1 | 2026-07-12 |
| [**herdr-pretty-which**](https://github.com/ramarivera/herdr-pretty-which)<br><sub>ramarivera</sub> | 面向 Herdr 的 Rust/Ratatui which-key 风格快捷键浮层 | `ratatui` `rust` `terminal` `tui` `which-key` | 1 | 🆕 2026-07-24 |
| [**herdr-nav-plus**](https://github.com/shoaibkhanz/herdr-nav-plus)<br><sub>shoaibkhanz</sub> | Ctrl+h/j/k/l 导航可以跨越 herdr 窗格直达工作区——感知 vim 行为，两端可循环 | `javascript` | 1 | 🆕 2026-07-18 |
| [**herdr-ask-inbox**](https://github.com/speardragon/herdr-ask-inbox)<br><sub>speardragon</sub> | 将所有 herdr 工作区中被阻塞的 Claude AskUserQuestion 提示汇总到一个弹窗中，就地回答，绝不会把答案发错 Agent | `claude-code` `javascript` | 1 | 🆕 2026-07-25 |
| [**herdr-unread-jump**](https://github.com/to4iki/herdr-unread-jump)<br><sub>to4iki</sub> | 跳转到下一个需要关注的 Herdr Agent 窗格（先是被阻塞的，然后是已完成的） | `agents` `bash` `shell` | 1 | 🆕 2026-07-22 |
| [**herdr-auto-focus**](https://github.com/calorie/herdr-auto-focus)<br><sub>calorie</sub> | 当 macOS 输入闲置后，自动聚焦到需要关注的 Herdr Agent | `golang` `macos` `go` | 0 | 🆕 2026-07-27 |
| [**herdr-plugin-agents-usage**](https://github.com/gecm0/herdr-plugin-agents-usage)<br><sub>gecm0</sub> | 在 Herdr 的模态弹窗中显示各服务商的使用情况（Claude、Codex、OpenCode Go、Neuralwatt） | `claude` `codex` `opencode` `terminal` `usage` | 0 | 🆕 2026-07-26 |
| [**herdr-harpoon**](https://github.com/hadeson/herdr-harpoon)<br><sub>hadeson</sub> | herdr 的 Harpoon 风格窗格标记：将窗格固定到 1-9 号槽位，跨标签页和工作区直接跳转 | `harpoon` `pane-navigation` `terminal` `tmux` `python` | 0 | 🆕 2026-07-25 |
| [**herdr-matter-wall**](https://github.com/Javamomma/herdr-matter-wall)<br><sub>Javamomma</sub> | herdr 插件：将项目中最活跃的子目录以只读 AI 状态卡片墙的形式平铺展示 | `claude-code` `shell` | 0 | 🆕 2026-07-14 |
| [**herdr-hasr**](https://github.com/KazBrekker1/herdr-hasr)<br><sub>KazBrekker1</sub> | Hasr（حصر——意为「枚举、完整清点」）——herdr 的 goto 风格弹窗切换器：切换、重命名、删除并创建 Agent、标签页和空间，并实时追踪完成状态 | `tui` `go` | 0 | 🆕 2026-07-23 |
| [**herdr-cmd-marks**](https://github.com/leonho/herdr-cmd-marks)<br><sub>leonho</sub> | herdr 插件：按项目管理的命令收藏弹窗。即使 Agent 正忙，也能在独立 shell 中运行已收藏的命令（支持全局、项目和智能分组） | `shell` | 0 | 🆕 2026-07-18 |
| [**herdr-next-agent**](https://github.com/martin-ro/herdr-next-agent)<br><sub>martin-ro</sub> | Herdr 插件：按可配置的状态优先级，跳转到下一个需要关注的 Agent | `python` | 0 | 🆕 2026-07-15 |
| [**herdr-float**](https://github.com/meerzulee/herdr-float)<br><sub>meerzulee</sub> | 类似 Zellij 的 ALT+F 浮动窗格 | `shell` | 0 | 🆕 2026-07-20 |
| [**herdr-plugins**](https://github.com/oullin/herdr-plugins)<br><sub>oullin</sub> | 面向 Herdr 的一组专注、可独立安装的插件合集 | `typescript` | 0 | 🆕 2026-07-22 |
| [**herdr-confirm-close-pane**](https://github.com/poweroutlet2/herdr-confirm-close-pane)<br><sub>poweroutlet2</sub> | 在关闭窗格前询问确认的 herdr 插件，类似 tmux 的 prefix+x confirm-before | `shell` | 0 | 2026-07-06 |
| [**herdr-whichkey**](https://github.com/Qu4tro/herdr-whichkey)<br><sub>Qu4tro</sub> | herdr 的 blezz/which-key 风格操作菜单——按下触发键后，每个操作只需一次按键，无需输入，无需回车 | `rust` | 0 | 🆕 2026-07-22 |
| [**herdr-deck-navigation**](https://github.com/raghu-nandan-bs/herdr-deck-navigation)<br><sub>raghu-nandan-bs</sub> | 将 herdr 内置的扁平化工作区/标签页/窗格导航器，替换为无需滚动即可快速到达任意窗格的「Deck」视图 | `rust` `terminal` `tui` | 0 | 🆕 2026-07-21 |
| [**herdr-focus**](https://github.com/trapple/herdr-focus)<br><sub>trapple</sub> | 聚焦下一个被阻塞/已完成的 Agent 窗格，并将终端应用置于前台。附带全局快捷键 | `shell` | 0 | 🆕 2026-07-19 |
| [**herdr-compass**](https://github.com/ycros/herdr-compass)<br><sub>ycros</sub> | 跨窗格、标签页和工作区的统一方向导航，面向 Herdr | `python` | 0 | 2026-07-05 |

<details><summary>与此目的也相关</summary>

- [thanhdat77/herdr-navigator](https://github.com/thanhdat77/herdr-navigator) — 通过一个模糊导航器跳转到任意 Herdr 工作区、Agent、项目、会话、远程连接、目录或操作
- [qu8n/herdr-automatic-rename](https://github.com/qu8n/herdr-automatic-rename) — 以 tmux 风格自动重命名 herdr 标签页，并为工作区/标签页/Agent 分配 1-9 的跳转快捷键编号
- [speardragon/herdr-plugin-manager](https://github.com/speardragon/herdr-plugin-manager) — 在弹窗中管理 herdr 插件——安装、更新、启用/禁用、卸载，并浏览 herdr-plugin 市场。推荐快捷键：prefix+p
- [leonho/herdr-idle-panes](https://github.com/leonho/herdr-idle-panes) — herdr 插件：以清单弹窗形式查看并关闭停留在闲置 shell 的窗格
- [shoaibkhanz/herdr-active-agent-jump](https://github.com/shoaibkhanz/herdr-active-agent-jump) — herdr 插件：按布局顺序前后循环聚焦正在进行中（工作中/被阻塞）的 Agent——作为 attention-jump 的 vim 风格补充

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-files"></a>

## 文件浏览与编辑器联动

> 想在窗格中打开文件树，或与编辑器的状态保持一致

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-file-viewer**](https://github.com/smarzban/herdr-file-viewer)<br><sub>smarzban</sub> | 面向 herdr 的只读文件查看器，支持感知 Git 状态。键盘驱动的 TUI（同时支持鼠标）：树形结构 + 内容窗格，支持差异对比、Markdown 渲染和语法高亮 | `file-viewer` `git` `ratatui` `rust` `terminal` | 273 | 🆕 2026-07-20 |
| [**herdr-mirror**](https://github.com/nikok6/herdr-mirror)<br><sub>nikok6</sub> | 在同一窗口统一本地和远程会话：将远程 herdr 服务器镜像到本地侧边栏，并通过 SSH 操控 | `rust` | 80 | 🆕 2026-07-28 |
| [**dotfiles**](https://github.com/edmundmiller/dotfiles)<br><sub>edmundmiller</sub> | 用于让我的 dotfiles 始终保持最新 | `dotfiles` `emacs` `nix-dotfiles` `nixos` `nixos-configuration` | 77 | 🆕 2026-07-29 |
| [**herdr-sidebar**](https://github.com/alexarthurs/herdr-sidebar)<br><sub>alexarthurs</sub> | 面向 herdr 的 VS Code 风格侧边栏：将文件浏览器和 Git 源代码管理整合到一个窗格——带语法高亮的预览、VS Code 风格的差异对比、GitLens 风格的抽屉面板、AI 生成提交信息 | `git` `ratatui` `rust` `sidebar` `terminal` | 16 | 🆕 2026-07-25 |
| [**herdr-yazi**](https://github.com/speardragon/herdr-yazi)<br><sub>speardragon</sub> | 在 herdr 窗格中打开 Yazi | `shell` | 10 | 2026-07-09 |
| [**herdr-lazygit**](https://github.com/Crokily/herdr-lazygit)<br><sub>Crokily</sub> | 在 herdr 侧边栏窗格中运行 lazygit，支持 AI 生成提交信息——打开、展开、提交都只需一个按键 | `git` `lazygit` `shell` | 8 | 🆕 2026-07-17 |
| [**herdr-quicklook**](https://github.com/dwarvesf/herdr-quicklook)<br><sub>dwarvesf</sub> | herdr 的 Quick Look：将剪贴板中的路径以浮层形式弹出预览，一键切换到文件查看器 | `terminal` `shell` | 7 | 🆕 2026-07-27 |
| [**herdr-flist**](https://github.com/devskale/herdr-flist)<br><sub>devskale</sub> | herdr 的文件列表插件 | `python` | 5 | 2026-07-10 |
| [**herdr-git-status**](https://github.com/ezcorp-org/herdr-git-status)<br><sub>ezcorp-org</sub> | herdr 插件：在侧边栏分支名旁显示每个空间的 git 工作区状态（已暂存/已修改/未跟踪/冲突） | `rust` | 5 | 🆕 2026-07-21 |
| [**herdr-context.nvim**](https://github.com/makyinmars/herdr-context.nvim)<br><sub>makyinmars</sub> | 在 Neovim 中选中代码或停在某一行，选择一个正在运行的 Herdr Agent，将结构化的上下文暂存到该 Agent 的提示词中（不直接提交） | `lua` | 4 | 🆕 2026-07-26 |
| [**herdr-file-viewer**](https://github.com/ismaelosuna7824/herdr-file-viewer)<br><sub>ismaelosuna7824</sub> | 集文件浏览器、代码查看器和 Git 客户端于一体的键盘驱动 Herdr 窗格应用——用 Go + Bubble Tea 编写 | `bubbletea` `git` `golang` `tui` `go` | 3 | 🆕 2026-07-15 |
| [**herdr-lazygit**](https://github.com/JacquesvanWyk/herdr-lazygit)<br><sub>JacquesvanWyk</sub> | 在 herdr 分屏窗格或标签页中打开 lazygit，支持智能切换（打开/聚焦/关闭） | `lazygit` `shell` | 3 | 2026-07-12 |
| [**herdr-markdown-viewer**](https://github.com/arvindparmar-me/herdr-markdown-viewer)<br><sub>arvindparmar-me</sub> | Herdr 插件：拖选一个 Markdown 路径并按下 prefix+m，即可在右侧分屏窗格中预览 | `shell` | 2 | 🆕 2026-07-17 |
| [**herdr-file-viewer**](https://github.com/jomarmontuya/herdr-file-viewer)<br><sub>jomarmontuya</sub> | 右侧显示的 Herdr 文件树插件，支持文件标签页、跟随当前目录、Git 状态装饰和可点击链接 | `go` | 2 | 2026-07-13 |
| [**herdr-plugin-mermaid-preview**](https://github.com/Volpestyle/herdr-plugin-mermaid-preview)<br><sub>Volpestyle</sub> | 在 Herdr 中为 Claude Code 和 Codex 的输出内容提供 Mermaid 图的实时预览 | `claude-code` `mermaid` `openai-codex` `terminal` `javascript` | 2 | 2026-07-10 |
| [**herdr-goto**](https://github.com/asumaran/herdr-goto)<br><sub>asumaran</sub> | 跨 herdr 仓库、工作树和窗格的树形切换器 | `go` | 1 | 🆕 2026-07-28 |
| [**herdr-wait**](https://github.com/cdc-lst/herdr-wait)<br><sub>cdc-lst</sub> | 根据窗格的进程树判断闲置 Agent 窗格实际在做什么（例如 'waiting: build-api' 或 'waiting: codex'）并打上标签的可配置 herdr 插件 | `typescript` | 1 | 2026-07-03 |
| [**herdr-nvim**](https://github.com/ChmaraX/herdr-nvim)<br><sub>ChmaraX</sub> | 将 Neovim 完全集成到你的 herdr 工作区 | `lua` `neovim` `nvim` `nvim-plugin` `rust` | 1 | 🆕 2026-07-24 |
| [**herdr-terminal-file-manager**](https://github.com/robert-flo/herdr-terminal-file-manager)<br><sub>robert-flo</sub> | elio 文件管理器的轻量 herdr 封装。自动检测你当前的目录并原生启动 elio，将其流畅的预览、内联图片和批量操作直接带入你的 herdr 窗格 | `shell` | 1 | 2026-07-10 |
| [**herdr-fresh**](https://github.com/rvalledorjr/herdr-fresh)<br><sub>rvalledorjr</sub> | 在 herdr 窗格内将终端 IDE「Fresh」作为文件查看器和编辑器运行的 herdr 插件 | `developer-tools` `editor` `fresh` `ide` `terminal` | 1 | 🆕 2026-07-17 |
| [**herdr-flutter**](https://github.com/ablause/herdr-flutter)<br><sub>ablause</sub> | 在编程 Agent 旁边监视、热重载并检查运行中 Flutter 应用的 herdr 侧边栏 | `dart` | 0 | 🆕 2026-07-27 |
| [**herdr-numbered-workspaces**](https://github.com/abrose/herdr-numbered-workspaces)<br><sub>abrose</sub> | 在 herdr 侧边栏中为每个空间前面加上编号，与带索引的 switch_workspace 快捷键对应 | `shell` | 0 | 🆕 2026-07-21 |
| [**herdr-ctx**](https://github.com/aorumbayev/herdr-ctx)<br><sub>aorumbayev</sub> | 面向 herdr 侧边栏窗格的 Claude 上下文窗口指示器 | `typescript` | 0 | 🆕 2026-07-21 |
| [**herdr-workbench**](https://github.com/azizuysal/herdr-workbench)<br><sub>azizuysal</sub> | 精致的 Herdr 项目侧边栏，具备文件浏览器、实时文件/内容搜索、只读源代码管理、丰富的预览、文件图标和 Git 状态装饰 | `rust` | 0 | 🆕 2026-07-28 |
| [**herdr-codex-cost**](https://github.com/Coolsik/herdr-codex-cost)<br><sub>Coolsik</sub> | 在 Herdr 侧边栏中显示 Codex 会话的估算费用 | `codex` `shell` | 0 | 🆕 2026-07-27 |
| [**herdr-tab-badges**](https://github.com/CowboyVang/herdr-tab-badges)<br><sub>CowboyVang</sub> | 为持有多个标签页的 herdr 空间在侧边栏加上徽章 | `shell` | 0 | 🆕 2026-07-21 |
| [**herdr-claude-usage-multi**](https://github.com/iamhouser/herdr-claude-usage-multi)<br><sub>iamhouser</sub> | Herdr 侧边栏中的 Claude 套餐使用量表——会话/周 %、颜色随用量升级、重置倒计时，并通过 CLAUDE_CONFIG_DIR 配置支持多账号 | `claude-code` `python` | 0 | 🆕 2026-07-25 |
| [**herdr-plugin-agent-repo**](https://github.com/khatriafaz/herdr-plugin-agent-repo)<br><sub>khatriafaz</sub> | 在 Agent 窗格标题和侧边栏中显示 Agent、仓库和分支名称的 Herdr 插件 | `javascript` | 0 | 🆕 2026-07-24 |
| [**herdr-cmux-file-viewer**](https://github.com/linvald/herdr-cmux-file-viewer)<br><sub>linvald</sub> | 将 cmux 的文件查看器同步到当前聚焦 herdr 空间的 herdr 插件 | `python` | 0 | 🆕 2026-07-23 |
| [**herdr-agents-preview**](https://github.com/maedana/herdr-agents-preview)<br><sub>maedana</sub> | Herdr 的多 Agent 终端预览仪表盘：同时显示所有运行中的 Agent，所选 Agent 占据大部分宽度 | `rust` | 0 | 🆕 2026-07-17 |
| [**herdr-openmd**](https://github.com/RufusLin/herdr-openmd)<br><sub>RufusLin</sub> | 在 openmd 中打开选中的 Markdown——从 herdr 启动的丰富 Qt 预览 | `shell` | 0 | 🆕 2026-07-29 |
| [**herdr-gitui**](https://github.com/Shi1xin/herdr-gitui)<br><sub>Shi1xin</sub> | herdr plugin: gitui in a sidebar pane — open/toggle, expand, light/dark themes | `gitui` `python` | 0 | 🆕 2026-07-28 |
| [**meadow**](https://github.com/Tetat-Chulchue/meadow)<br><sub>Tetat-Chulchue</sub> | 面向 herdr 终端多路复用器的鼠标驱动文件浏览器窗格 | `python` | 0 | 🆕 2026-07-21 |
| [**herdr-launcher-pane**](https://github.com/y-hirakaw/herdr-launcher-pane)<br><sub>y-hirakaw</sub> | herdr 的固定式点击启动窗格——按工作区启动 Finder/资源管理器、VS Code，或你配置的任意命令 | `launcher` `launcher-pane` `productivity` `python` | 0 | 🆕 2026-07-20 |

<details><summary>与此目的也相关</summary>

- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) — herdr 的代码审查 + 文件查看器侧边栏——对 Agent 的差异发表评论并打回。同时提供 PR 及其检查、评论的只读视图
- [jsmenzies/mergr](https://github.com/jsmenzies/mergr) — GitHub pull request status for Herdr Space sidebar rows.
- [brianh20/herdr-stagr](https://github.com/brianh20/herdr-stagr) — Source Control sidebar for herdr: stage, unstage, and discard with side-by-side diffs
- [ChmaraX/herdr-gitview](https://github.com/ChmaraX/herdr-gitview) — herdr 的 Git 状态/差异面板——审查更改、在 nvim 中编辑、暂存/提交/丢弃，全部在终端内完成
- [ctbaum/herdr-deck](https://github.com/ctbaum/herdr-deck) — herdr-agents.nvim 的搭配工作区启动器：在预先搭好的 Neovim、Agent、shell 和 lazygit 组合面板中打开或恢复 Claude 和 Codex
- [kylezk777/herdr-file-explore](https://github.com/kylezk777/herdr-file-explore) — 在 herdr 窗格中运行的只读代码浏览与审查 TUI

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-cost"></a>

## Token 与费用管理

> 想看看 Agent 花费了多少，并想削减用量

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**llmtrim-herdr**](https://github.com/fkiene/llmtrim-herdr)<br><sub>fkiene</sub> | 降低 herdr 的 token 费用：压缩每个 Agent 窗格的请求（实测输入 -31% / 输出 -74%），并在每个窗格的徽章上显示节省的费用 | `llm-proxy` `llmtrim` `powershell` | 23 | 2026-07-02 |
| [**herdr-token-dashboard**](https://github.com/Davidcreador/herdr-token-dashboard)<br><sub>Davidcreador</sub> | 面向 Herdr Agent 窗格的实时 token 消耗仪表盘和通知 | `ai-agents` `bubbletea` `opencode` `pi-agent` `token-dashboard` | 10 | 🆕 2026-07-15 |
| [**herdr-agent-usage**](https://github.com/senna-lang/herdr-agent-usage)<br><sub>senna-lang</sub> | 为 Herdr 中运行的 Agent 显示上下文使用量表和服务商速率限制 | `ai-agents` `claude-code` `codex` `golang` `rate-limiting` | 8 | 🆕 2026-07-28 |
| [**herdr-claude-usage**](https://github.com/alejodelosrios/herdr-claude-usage)<br><sub>alejodelosrios</sub> | 不必再为了查配额而打开一个 Claude 会话。Claude 套餐使用情况（会话 % \| 周 %）始终显示在 Herdr 侧边栏中，同一账号下所有工作区共享。通过 Claude Code 自身的凭据获取与 /status 完全一致的精确数字：无需估算，无需额外登录，也不消耗套餐 token | `claude` `claude-code` `python` | 0 | 🆕 2026-07-21 |
| [**scopefuel**](https://github.com/mgh3326/scopefuel)<br><sub>mgh3326</sub> | 面向 AI 编程 Agent 套餐的范围感知余量表——显示实际被限制的是什么（账号/模型/分组）以及何时恢复 | `ai-agents` `antigravity` `claude-code` `cli` `codex` | 0 | 🆕 2026-07-28 |
| [**herdr-usage-bar**](https://github.com/silverwolfdoc/herdr-usage-bar)<br><sub>silverwolfdoc</sub> | 为 Herdr 中的 AI Agent 显示使用限额和上下文用量，紧凑的底部用量条形式呈现 | `go` | 0 | 🆕 2026-07-24 |

<details><summary>与此目的也相关</summary>

- [Coolsik/herdr-codex-cost](https://github.com/Coolsik/herdr-codex-cost) — 在 Herdr 侧边栏中显示 Codex 会话的估算费用

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-monitor"></a>

## 监控与仪表盘

> 想一目览尽 Agent 和机器的状态

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-telemetry**](https://github.com/DIodide/herdr-telemetry)<br><sub>DIodide</sub> | 将工作区和 Agent 遥测数据流式传输到你自己掌控的端点的 Herdr 插件——Go 编写的单一二进制文件，默认注重隐私 | `golang` `telemetry` `go` | 9 | 2026-07-10 |
| [**herdr-pc-ram-and-cpu-usage-overlay**](https://github.com/ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay)<br><sub>ezcorp-org</sub> | herdr 插件：按空间（工作区）实时显示 CPU/内存占用率，以占整机资源的比例呈现 | `rust` | 8 | 🆕 2026-07-21 |
| [**herdres**](https://github.com/luminexord/herdres)<br><sub>luminexord</sub> | 基于 Tendwire 构建的 Telegram 界面，用于监控和向 Herdr 编程 Agent 发送消息 | `coding-agents` `telegram` `python` | 7 | 🆕 2026-07-29 |
| [**herdr-f1**](https://github.com/hmu332233/herdr-f1)<br><sub>hmu332233</sub> | 为 Herdr Agent 打造的 F1 风格仪表盘 | `agent-dashboard` `typescript` | 4 | 🆕 2026-07-28 |
| [**herdr-kanban**](https://github.com/KokiKono/herdr-kanban)<br><sub>KokiKono</sub> | 将任务与 herdr 标签页关联的终端看板，数据持久化在 SQLite 中 | `rust` | 4 | 2026-07-10 |
| [**shepherd**](https://github.com/ryonakae/shepherd)<br><sub>ryonakae</sub> | 面向 Herdr 管理的编程 Agent 的 worker 可观测性守护进程和运行时桥接 | `pi-coding-agent` `pi-extension` `typescript` | 4 | 🆕 2026-07-22 |
| [**herdr-tally**](https://github.com/jasonrr/herdr-tally)<br><sub>jasonrr</sub> | 为你和你的 Agent 提供按项目划分的待办事项和速记板<br>📝 プロジェクト単位の TODO 管理 | `rust` `todo` | 3 | 🆕 2026-07-26 |
| [**herdr-workboard**](https://github.com/Phoobobo/herdr-workboard)<br><sub>Phoobobo</sub> | herdr 的看板式工作板 TUI：看板对应工作区，任务状态对应标签页，任务会话对应窗格 | `kanban` `tui` `typescript` | 3 | 🆕 2026-07-28 |
| [**herdr-agent-dashboard**](https://github.com/carsonjones/herdr-agent-dashboard)<br><sub>carsonjones</sub> | prefix+a 显示 herdr Agent 列表 | `typescript` | 2 | 🆕 2026-07-16 |
| [**herdr-sysmon**](https://github.com/getpipher/herdr-sysmon)<br><sub>getpipher</sub> | 在 Herdr 侧边栏显示系统指标——CPU、内存、电池、网络、磁盘、时钟。忠实地将 tmux-cpu/tmux-battery/tmux-online-status 状态栏移植为 Herdr 工作区 token。以 macOS 为主 | `battery` `catppuccin` `cpu` `getpipher` `macos` | 2 | 🆕 2026-07-26 |
| [**herdr-beads**](https://github.com/miiraheart/herdr-beads)<br><sub>miiraheart</sub> | herdr 的 beads（bd）任务面板：以列表、表格或看板形式展示你的 bd issue，可作为侧边栏或浮动窗口 | `bd` `beads` `kanban` `rust` `tui` | 2 | 🆕 2026-07-24 |
| [**herdr-tokscale-dashboard**](https://github.com/astkaasa/herdr-tokscale-dashboard)<br><sub>astkaasa</sub> | 将 Tokscale 作为本地 Herdr 仪表盘窗格打开 | `dashboard` `tokscale` `shell` | 1 | 2026-06-26 |
| [**herdr-telemetry-bridge**](https://github.com/CodyBontecou/herdr-telemetry-bridge)<br><sub>CodyBontecou</sub> | 将本地工作区、仓库、编程 Agent、模型和追踪遥测数据流式传输到外部客户端的 Herdr 插件 | `coding-agents` `telemetry` `time-md` `javascript` | 1 | 2026-06-26 |
| [**shepherd**](https://github.com/jwarykowski/shepherd)<br><sub>jwarykowski</sub> | 把你的待办事项统一「牧」起来 | `cli` `developer-tools` `go-lang` `productivity` `task-management` | 1 | 🆕 2026-07-27 |
| [**herdr-compose**](https://github.com/mattyan1053/herdr-compose)<br><sub>mattyan1053</sub> | 用于 docker compose 的 Herdr 插件 | `terminal` `tui` `shell` | 1 | 🆕 2026-07-24 |
| [**herdr-ports**](https://github.com/Numbered-com/herdr-ports)<br><sub>Numbered-com</sub> | 在 herdr 中呈现正在运行的开发服务器：为每个至少运行一个 TCP 监听器的空间显示通用的 $ports 徽章 | `pids` `ports` `shell` | 1 | 🆕 2026-07-23 |
| [**herdr-slurm**](https://github.com/quan-meng/herdr-slurm)<br><sub>quan-meng</sub> | 为 Slurm 分配任务创建 Herdr 工作区和受监控的 Agent 标签页 | `hpc` `slurm` `terminal-multiplexer` `python` | 1 | 🆕 2026-07-24 |
| [**herdr-phin-board**](https://github.com/phin-tech/herdr-phin-board)<br><sub>phin-tech</sub> | Herdr 插件：覆盖你所有空间的状态板——待办、进行中、等待他人、已完成，还可以自定义任意状态。支持列表或看板视图 | `bubbletea` `tui` `go` | 0 | 🆕 2026-07-25 |
| [**conflux-herdr**](https://github.com/tumf/conflux-herdr)<br><sub>tumf</sub> | 用于运行 Conflux TUI 并报告其生命周期状态的 Herdr 插件窗格 | `shell` | 0 | 🆕 2026-07-26 |
| [**adlc-herdr**](https://github.com/voodootikigod/adlc-herdr)<br><sub>voodootikigod</sub> | ADLC 的 herdr 插件——按窗格显示阶段/工单/关卡状态，附带待办看板、关卡操作和 adlc-fleet 运行可观测性。是 voodootikigod/adlc/plugins/adlc-herdr 的自动同步镜像 | `javascript` | 0 | 🆕 2026-07-28 |

<details><summary>与此目的也相关</summary>

- [nelsonPires5/herdr-board](https://github.com/nelsonPires5/herdr-board) — herdr 的看板工具——卡片就是提示词，会被派发给可见窗格中的 AI Agent
- [chouxcreams/herdr-dashboard](https://github.com/chouxcreams/herdr-dashboard) — herdr 工作区的 PR 状态仪表盘 TUI——一目了然地查看每个窗格对应的 PR 状态/CI/审查情况

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-finder"></a>

## 搜索与模糊查找器

> 只记得大概名字也想调出命令或项目

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-navigator**](https://github.com/thanhdat77/herdr-navigator)<br><sub>thanhdat77</sub> | 通过一个模糊导航器跳转到任意 Herdr 工作区、Agent、项目、会话、远程连接、目录或操作 | `fuzzy-finder` `rust` `terminal` `workspace-manager` | 32 | 🆕 2026-07-20 |
| [**termscope**](https://github.com/iurysza/termscope)<br><sub>iurysza</sub> | 打开终端屏幕上已经可见的文件和链接 | `python` `television` `terminal` `tmux` | 31 | 🆕 2026-07-18 |
| [**herdr-command-palette**](https://github.com/JanTvrdik/herdr-command-palette)<br><sub>JanTvrdik</sub> | herdr 的 fzf 命令面板——模糊选择并运行任意插件操作 | `shell` | 21 | 2026-06-29 |
| [**herdr-plugin-sesh**](https://github.com/fullerzz/herdr-plugin-sesh)<br><sub>fullerzz</sub> | 面向 Herdr 的 Sesh 风格工作区选择器 TUI，集成 zoxide，可从常用目录创建工作区 | `bubbletea` `sesh` `tui` `zoxide` `go` | 14 | 🆕 2026-07-26 |
| [**herdr-zoxide**](https://github.com/den-tanui/herdr-zoxide)<br><sub>den-tanui</sub> | 从 zoxide 记录的目录创建工作区、标签页和窗格的 Herdr 插件 | `zoxide` `shell` | 8 | 🆕 2026-07-25 |
| [**herdr-drovr**](https://github.com/AVGVSTVS96/herdr-drovr)<br><sub>AVGVSTVS96</sub> | 轻松将 Herdr 标签页移动到其他工作区 | `fzf` `terminal` `javascript` | 5 | 🆕 2026-07-21 |
| [**herdr-bar**](https://github.com/jeffarese/herdr-bar)<br><sub>jeffarese</sub> | herdr 的 Cmd+K：模糊跳转到任意标签页、Agent、仓库或分支。仅使用 Python 标准库 | `command-bar` `fuzzy-finder` `python` `terminal` `tui` | 5 | 🆕 2026-07-25 |
| [**herdr-grep-nvim**](https://github.com/cinco/herdr-grep-nvim)<br><sub>cinco</sub> | herdr 插件：用 fzf + ripgrep 进行实时搜索，并在你工作区旁边的分屏中用 nvim 打开匹配结果 | `shell` | 3 | 🆕 2026-07-17 |
| [**herdr-ghq**](https://github.com/crafts69guy/herdr-ghq)<br><sub>crafts69guy</sub> | Herdr 插件：在一个 Rust TUI 中模糊切换正在运行的 Agent、已打开的工作区和 ghq 仓库——并可在新工作区、标签页、分屏或当前窗格中打开仓库 | `developer-tools` `ghq` `ratatui` `rust` `terminal` | 3 | 🆕 2026-07-22 |
| [**herdr-palette**](https://github.com/ramarivera/herdr-palette)<br><sub>ramarivera</sub> | 面向 Herdr 工作区的 Rust/Ratatui 模糊命令面板 | `command-palette` `ratatui` `rust` `terminal` `tui` | 3 | 🆕 2026-07-24 |
| [**herdr-sessionizer**](https://github.com/salkhalil/herdr-sessionizer)<br><sub>salkhalil</sub> | herdr 的 tmux-sessionizer：用 fzf 搜索已打开的工作区和 zoxide 目录，创建或聚焦并附带模板标签页 | `shell` | 3 | 🆕 2026-07-27 |
| [**herdr-agent-recency**](https://github.com/ugurtarlig/herdr-agent-recency)<br><sub>ugurtarlig</sub> | 支持主题的 Herdr 选择器，按 Codex 和 Claude 有意义的活动情况排序 | `claude-code` `codex` `fzf` `python` | 3 | 🆕 2026-07-17 |
| [**herdr-configurable-picker**](https://github.com/yoshiori/herdr-configurable-picker)<br><sub>yoshiori</sub> | 面向 herdr 的树形跳转选择器，快捷键完全可配置 | `rust` | 3 | 2026-07-05 |
| [**herdr-launcher**](https://github.com/arjenblokzijl/herdr-launcher)<br><sub>arjenblokzijl</sub> | 模糊选择一个声明式 TOML 工作流，填写表单，在新的 herdr 空间中启动编程 Agent | `launcher` `ratatui` `rust` `tui` | 2 | 2026-07-10 |
| [**herdr-spotify**](https://github.com/iikjl/herdr-spotify)<br><sub>iikjl</sub> | herdr 的 Spotify 正在播放浮层插件——专辑封面、播放控制，并可通过 Spotify Web API 搜索/加入队列/点赞 | `spotify` `terminal` `go` | 2 | 2026-07-07 |
| [**herdr-recent-workspaces**](https://github.com/ismaelosuna7824/herdr-recent-workspaces)<br><sub>ismaelosuna7824</sub> | Herdr 的「打开最近使用的文件夹」——可模糊筛选你曾作为工作区打开过的文件夹列表。选择一个即可打开或重新聚焦该工作区，也可浏览文件系统打开新的 | `go` | 2 | 2026-07-10 |
| [**herdr-hunk**](https://github.com/JacquesvanWyk/herdr-hunk)<br><sub>JacquesvanWyk</sub> | herdr 中用于 Hunk 差异对比的交互式 fzf 选择器：支持提交、范围、stash，并可在 Agent 完成时自动打开 | `fzf` `hunk` `shell` | 2 | 2026-07-12 |
| [**herdr-keybind-search**](https://github.com/malone-c/herdr-keybind-search)<br><sub>malone-c</sub> | herdr 的可搜索快捷键浮层（基于 fzf）。按下一个键即可模糊搜索你的快捷键 | `shell` | 2 | 🆕 2026-07-15 |
| [**herdr-keymap**](https://github.com/The-Dave-Stack/herdr-keymap)<br><sub>The-Dave-Stack</sub> | herdr 插件：在浮层面板中展示所有快捷键，并可直接运行有对应 CLI 命令的那些 | `typescript` | 2 | 🆕 2026-07-17 |
| [**herdr-jump**](https://github.com/agustinvalencia/herdr-jump)<br><sub>agustinvalencia</sub> | 为 herdr 空间和 Agent 分别提供的浮层选择器——跳转到任意工作区或 Agent，并以颜色实时显示状态 | `go` | 1 | 🆕 2026-07-24 |
| [**herdr-command-palette**](https://github.com/alon-z/herdr-command-palette)<br><sub>alon-z</sub> | Herdr 插件：模糊搜索工作区/目录的命令面板 | `javascript` | 1 | 2026-06-22 |
| [**herdr-url-picker**](https://github.com/chouxcreams/herdr-url-picker)<br><sub>chouxcreams</sub> | Herdr 插件：从聚焦窗格中选取一个 URL 并在浏览器中打开 | `shell` | 1 | 🆕 2026-07-22 |
| [**herdr-simple-switcher**](https://github.com/haphamdev/herdr-simple-switcher)<br><sub>haphamdev</sub> | 通过模糊搜索在工作区和标签页之间切换的简易 herdr 插件 | `shell` | 1 | 2026-07-11 |
| [**herdr-workspace-launcher**](https://github.com/ImArtisann/herdr-workspace-launcher)<br><sub>ImArtisann</sub> | 面向 macOS 的 Herdr 插件，通过可搜索的键盘驱动目录选择器快速创建聚焦工作区 | `typescript` | 1 | 🆕 2026-07-16 |
| [**herdr-keys**](https://github.com/JacquesvanWyk/herdr-keys)<br><sub>JacquesvanWyk</sub> | 面向 herdr 的可模糊搜索快捷键速查表（支持功能包、发现和个人自定义覆盖） | `shell` | 1 | 2026-07-12 |
| [**herdr-kiosk**](https://github.com/thomasschafer/herdr-kiosk)<br><sub>thomasschafer</sub> | 模糊查找 Git 仓库和分支，并在 Herdr 中作为工作树打开 | `rust` | 1 | 🆕 2026-07-26 |
| [**herdr-pane-picker**](https://github.com/ugurtarlig/herdr-pane-picker)<br><sub>ugurtarlig</sub> | 输入窗格上显示的字符提示来选择 Herdr 窗格 | `terminal` `wezterm` `python` | 1 | 🆕 2026-07-17 |
| [**herdr-fzf-url**](https://github.com/x0d7x/herdr-fzf-url)<br><sub>x0d7x</sub> | 扫描 herdr 终端窗格中的 URL，并用 fzf 交互式选取一个 | `fzf` `go` `url` | 1 | 2026-06-26 |
| [**herdr-open-local-paths**](https://github.com/yigitkg/herdr-open-local-paths)<br><sub>yigitkg</sub> | 检测本地路径，并通过简易选择器在 Windows、Linux 和 WSL 上打开或显示的 Herdr 插件 | `developer-tools` `python` `terminal` `wsl` | 1 | 🆕 2026-07-28 |
| [**herdr-agents-picker**](https://github.com/yxhta/herdr-agents-picker)<br><sub>yxhta</sub> | Herdr 插件：类似工作区选择器的 Agent 窗格模糊选择器，带实时窗格预览（Rust + ratatui 编写） | `rust` | 1 | 🆕 2026-07-18 |
| [**herdr-url-picker**](https://github.com/abrose/herdr-url-picker)<br><sub>abrose</sub> | herdr 插件：用 fzf 选取当前窗格中显示的 URL，并用默认浏览器打开 | `shell` | 0 | 🆕 2026-07-22 |
| [**herdr-cast**](https://github.com/aliou/herdr-cast)<br><sub>aliou</sub> | Personal Herdr plugin for native macOS agent notifications, fuzzy workspace navigation, zoxide-backed workspace creation, and layout commands. | `developer-tools` `macos` `notifications` `ratatui` `rust` | 0 | 🆕 2026-07-28 |
| [**herdr-picker**](https://github.com/bkarpinos/herdr-picker)<br><sub>bkarpinos</sub> | 用于在 herdr 中搜索和预览工作区、Agent 和标签页的快速弹窗选择器 | `go` | 0 | 🆕 2026-07-25 |
| [**pj-herdr**](https://github.com/josephschmitt/pj-herdr)<br><sub>josephschmitt</sub> | 使用 PJ 选择器打开新工作区的 Herdr 插件 | `shell` | 0 | 🆕 2026-07-15 |
| [**herdr-cull**](https://github.com/krzysztoff1/herdr-cull)<br><sub>krzysztoff1</sub> | 查看并关闭 herdr 中闲置的 Agent 窗格——fzf 多选，未经确认绝不关闭 | `ai-agents` `claude` `codex` `fzf` `terminal` | 0 | 🆕 2026-07-20 |
| [**herdr-shortcut**](https://github.com/matheus3301/herdr-shortcut)<br><sub>matheus3301</sub> | 面向 Herdr 的快捷任务选择器兼编程 Agent 启动器 | `bubbletea` `claude-code` `codex` `coding-agents` `developer-tools` | 0 | 🆕 2026-07-24 |
| [**herdr-omarchy-theme-sync**](https://github.com/maxBRT/herdr-omarchy-theme-sync)<br><sub>maxBRT</sub> | 将 Herdr 的 UI 配色与当前使用的 Omarchy 主题同步 | `linux` `omarchy` `theme` `python` | 0 | 🆕 2026-07-28 |
| [**herdr-smart-workspace**](https://github.com/nicolasvasquez/herdr-smart-workspace)<br><sub>nicolasvasquez</sub> | 用于在会话内快速切换工作区，或通过浮层 fzf 选择器从 zoxide 创建新工作区的 Herdr 插件 | `python` | 0 | 2026-07-02 |
| [**herdr-launcher**](https://github.com/nicolegros/herdr-launcher)<br><sub>nicolegros</sub> | 提供模糊目录选择器以快速创建或切换工作区的 herdr 插件 | `go` | 0 | 🆕 2026-07-15 |
| [**mux-prompter**](https://github.com/phine-apps/mux-prompter)<br><sub>phine-apps</sub> | 模糊选取上下文相关的提示词，并注入到 Herdr 窗格中 | `fzf` `prompt-engineering` `terminal-multiplexer` `shell` | 0 | 🆕 2026-07-20 |
| [**herdr-claude-profile**](https://github.com/quinnjr/herdr-claude-profile)<br><sub>quinnjr</sub> | herdr 插件：通过浮层面板切换和管理 claude-profile 的配置 | `typescript` | 0 | 🆕 2026-07-20 |
| [**herdr-plugins**](https://github.com/shelken/herdr-plugins)<br><sub>shelken</sub> | Herdr 插件 monorepo（auto-pi：按区域打开 pi + 会话选择器） | `python` | 0 | 🆕 2026-07-17 |
| [**herdr-workspacex**](https://github.com/willfish/herdr-workspacex)<br><sub>willfish</sub> | Rust 原生的模糊 Herdr 工作区切换器，支持基于 zoxide 的工作区创建 | `rust` `workspace-manager` `zoxide` | 0 | 2026-07-07 |
| [**herdr-fzf-url**](https://github.com/willian/herdr-fzf-url)<br><sub>willian</sub> | Pick URLs from the focused pane with `fzf`, then open or copy them. | `fzf` `shell` | 0 | 🆕 2026-07-28 |

<details><summary>与此目的也相关</summary>

- [JacquesvanWyk/herdr-linear](https://github.com/JacquesvanWyk/herdr-linear) — 在 herdr 分屏窗格或标签页中运行的 fzf 驱动 Linear 面板：搜索 issue、深入项目、创建 issue、修改状态
- [beyondlex/herdr-recent-navigator](https://github.com/beyondlex/herdr-recent-navigator) — 面向 Herdr 的最近工作区/标签页/窗格切换器。弹出窗口列出最近聚焦过的工作区、标签页、窗格和 AI Agent，支持模糊搜索和键盘导航

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-automation"></a>

## 自动化、钩子与定时任务

> 想在创建工作树或指定时机自动运行固定的操作步骤

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-browser**](https://github.com/ogulcancelik/herdr-browser)<br><sub>ogulcancelik</sub> | 在 Herdr 窗格内渲染真实的 Chromium 视图，并通过 CDP 进行操控 | `browser` `browser-automation` `cdp` `chromium` `kitty-graphics` | 132 | 🆕 2026-07-28 |
| [**herdr-worktree-setup**](https://github.com/tdi/herdr-worktree-setup)<br><sub>tdi</sub> | herdr 插件：创建工作树时执行按项目定制的初始化步骤（从 main 复制 .env、mise trust、direnv allow、安装依赖等） | `javascript` | 14 | 🆕 2026-07-20 |
| [**zed-herdr**](https://github.com/ImArtisann/zed-herdr)<br><sub>ImArtisann</sub> | 自动将当前活动的 HerdR 工作区与已有的 Zed 会话保持同步 | `typescript` | 13 | 🆕 2026-07-16 |
| [**herdr-automatic-rename**](https://github.com/qu8n/herdr-automatic-rename)<br><sub>qu8n</sub> | 以 tmux 风格自动重命名 herdr 标签页，并为工作区/标签页/Agent 分配 1-9 的跳转快捷键编号 | `shell` | 8 | 🆕 2026-07-27 |
| [**herdr-routines**](https://github.com/mrcndz/herdr-routines)<br><sub>mrcndz</sub> | 运行定时任务的 Herdr 插件：按 cron 或固定间隔在工作区中打开标签页，运行命令或启动 Agent | `python` | 7 | 🆕 2026-07-18 |
| [**herdr-auto-pilot**](https://github.com/0xGosu/herdr-auto-pilot)<br><sub>0xGosu</sub> | 通过 Herdr API 代替你自动向运行中的 AI 编程 CLI 发送提示词的 Herdr 插件。插件具有从你的操作中学习的训练模式，并内置防止危险/恶意操作的防护机制。经过充分训练后，可让它以「完全自主提示（FSP）」模式运行 | `go` | 5 | 🆕 2026-07-29 |
| [**herdr-tab-title**](https://github.com/aarsh21/herdr-tab-title)<br><sub>aarsh21</sub> | 为 Herdr 提供类似 tmux 的自动标签页标题 | `rust` `terminal` `tmux` | 5 | 2026-07-08 |
| [**herdr-workflows**](https://github.com/aorumbayev/herdr-workflows)<br><sub>aorumbayev</sub> | 为 herdr 中的重复步骤提供声明式自动化 | `agentic-ai` `agentic-workflow` `agents` `ai` `claude` | 3 | 🆕 2026-07-29 |
| [**herdr-agent-config-manager**](https://github.com/Phoobobo/herdr-agent-config-manager)<br><sub>Phoobobo</sub> | 混合 CLI + Herdr 插件，用于检测并集中管理 Agent 的 skill、MCP、插件和 hook | `python` | 3 | 2026-07-06 |
| [**herdr-js-worktree-bootstrap**](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap)<br><sub>LeonardoTrapani</sub> | 为 JavaScript 和 TypeScript 自动初始化 Herdr 工作树，支持基于锁文件的安装和安全的环境变量还原 | `automation` `bun` `developer-tools` `git-worktree` `javascript` | 2 | 🆕 2026-07-15 |
| [**bermuda**](https://github.com/bon5co/bermuda)<br><sub>bon5co</sub> | 一个 Agent 运行框架：调度任务，并将每个任务作为交互式 herdr Agent 运行 | `agents` `golang` `tui` `go` | 1 | 🆕 2026-07-28 |
| [**say-hook**](https://github.com/HikaruEgashira/say-hook)<br><sub>HikaruEgashira</sub> | 使用 ElevenLabs 文字转语音朗读 Claude Code hook 事件的 macOS CLI | `typescript` | 1 | 🆕 2026-07-20 |
| [**herdr-plugin**](https://github.com/ppggff/herdr-plugin)<br><sub>ppggff</sub> | 自动记住并恢复每个 Herdr 窗格对应的正确 macOS 输入法（IME） | `ime` `input-method` `macos` `python` | 1 | 🆕 2026-07-27 |
| [**herdr-auto-tab-name**](https://github.com/dev-shimada/herdr-auto-tab-name)<br><sub>dev-shimada</sub> | herdr 插件：根据当前目录自动命名标签页 | `javascript` | 0 | 2026-07-12 |
| [**herdr-context-namer**](https://github.com/eabadim/herdr-context-namer)<br><sub>eabadim</sub> | Auto-name Herdr tabs and workspaces from pane context via OpenCode | `opencode` `python` | 0 | 🆕 2026-07-28 |
| [**herdr-fwd**](https://github.com/go-min/herdr-fwd)<br><sub>go-min</sub> | Automatic loopback port forwarding for remote Herdr sessions. | `port-forwarding` `ssh` `terminal` `rust` | 0 | 🆕 2026-07-29 |
| [**herdr-pane-name**](https://github.com/go-min/herdr-pane-name)<br><sub>go-min</sub> | 为你终端会话中的窗格自动命名的 Herdr 插件 | `pane-naming` `terminal` `terminal-multiplexer` `rust` | 0 | 🆕 2026-07-28 |
| [**herdr-plugin-auto-rename**](https://github.com/khatriafaz/herdr-plugin-auto-rename)<br><sub>khatriafaz</sub> | 根据 Pi 会话的第一条提示词，自动重命名新的 Herdr 工作区和 Git 分支 | `typescript` | 0 | 🆕 2026-07-24 |
| [**tendwire**](https://github.com/plotarmordev/tendwire)<br><sub>plotarmordev</sub> | Herdr 的本地 API：将编程 Agent 连接到应用、自动化流程和任意本地系统 | `agent-api` `local-first` `python` | 0 | 🆕 2026-07-26 |
| [**numberer-manager**](https://github.com/yuritada/numberer-manager)<br><sub>yuritada</sub> | 轻量级 Herdr 插件，自动在工作区和标签页标签前加上其在列表中的当前位置（例如「1: space」「1: tab」） | `python` | 0 | 🆕 2026-07-25 |

<details><summary>与此目的也相关</summary>

- [freethinkel/herdr-plugin-git-worktree-hooks](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks) — 在创建/移除 git 工作树时运行 shell 命令——一份 YAML 配置适用于所有项目，放在任何仓库之外
- [timofey-TK/herdr-worktree-hooks](https://github.com/timofey-TK/herdr-worktree-hooks) — herdr 插件：在创建、打开或删除 git 工作树时运行自定义的初始化/清理命令
- [Newt6611/herdr-tab-title](https://github.com/Newt6611/herdr-tab-title) — Herdr Tab Title 会将 Herdr 标签页自动重命名为整洁的、按工作区独立编号的名称，如「1. Codex」「2. Terminal」，格式可自定义

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-session"></a>

## 会话保存与恢复

> 关闭工作后，希望之后能从同一状态继续

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-session-parker**](https://github.com/iviaxpow3r/herdr-session-parker)<br><sub>iviaxpow3r</sub> | 用于暂存窗格/标签页，并在之后恢复受支持的 Agent 会话的 Herdr 插件 | `agent-tools` `python` | 9 | 2026-07-03 |
| [**herdr-resurrect**](https://github.com/ntindle/herdr-resurrect)<br><sub>ntindle</sub> | herdr 的 tmux-resurrect——快照工作区、标签页、窗格、当前目录、运行中的程序和 Agent，并在崩溃或重启后恢复 | `crash-recovery` `session-manager` `terminal-multiplexer` `tmux-resurrect` `javascript` | 6 | 2026-07-12 |
| [**herdr-agent-inbox**](https://github.com/douglascorrea/herdr-agent-inbox)<br><sub>douglascorrea</sub> | herdr 编程 Agent 的收件箱——会话标题、已读/未读标记、运行时长、工作区汇总、可续接的聊天记录 | `ai-agents` `terminal` `python` | 4 | 🆕 2026-07-28 |
| [**session-digger**](https://github.com/taxueseek/session-digger)<br><sub>taxueseek</sub> | 跨环境会话历史挖掘与知识管理。分析记录。支持 Claude/Grok/Kimi Code/Codex/WorkBuddy/Trae CN 等主流环境 | `python` | 4 | 🆕 2026-07-21 |
| [**herdr-claude-auto-retry**](https://github.com/mo-arvan/herdr-claude-auto-retry)<br><sub>mo-arvan</sub> | 等待 Anthropic 速率限制解除后自动恢复 Claude Code，herdr 原生实现：无需 tmux，无需 shell 包装 | `javascript` | 3 | 🆕 2026-07-16 |
| [**herdr-notes**](https://github.com/alexarthurs/herdr-notes)<br><sub>alexarthurs</sub> | 面向 herdr 的持久化 Markdown 笔记窗格——每个工作区一份笔记，支持预览渲染+编辑模式，自动保存且重启后仍保留 | `markdown` `notes` `ratatui` `rust` `terminal` | 2 | 🆕 2026-07-25 |
| [**herdr-synchronize-panes**](https://github.com/furuhashin/herdr-synchronize-panes)<br><sub>furuhashin</sub> | Herdr 插件：将一条命令广播到当前标签页内的所有窗格（类似 tmux 的 synchronize-panes） | `javascript` | 2 | 🆕 2026-07-14 |
| [**herdr_sync**](https://github.com/kamaaina/herdr_sync)<br><sub>kamaaina</sub> | 同步 herdr 中的窗格 | `zig` | 2 | 2026-07-01 |
| [**herdr-e2b**](https://github.com/tomasvarga/herdr-e2b)<br><sub>tomasvarga</sub> | 按需将 git 工作树镜像到全新的 E2B 云沙盒——直接上传快照（包括未提交的更改），无需 push 或 clone。一个 herdr 插件 | `cli` `cloud-dev` `e2b` `git-worktree` `sandbox` | 2 | 🆕 2026-07-18 |
| [**herdr-todos-windows**](https://github.com/aclima01/herdr-todos-windows)<br><sub>aclima01</sub> | 实时镜像 herdr Agent 任务列表（TaskCreate/TaskUpdate）的面板，方便你跟踪它的计划 | `powershell` | 1 | 🆕 2026-07-22 |
| [**herdr-thread-to-tab**](https://github.com/toyamarinyon/herdr-thread-to-tab)<br><sub>toyamarinyon</sub> | 让单窗格 Herdr 标签页标签与 Claude Code 和 Codex 的线程标题保持同步 | `rust` | 1 | 🆕 2026-07-24 |
| [**herdr-pane-id-labeler**](https://github.com/4Born/herdr-pane-id-labeler)<br><sub>4Born</sub> | 让窗格标签与如 w1:p2 之类的公开窗格 ID 保持同步的 Herdr 插件 | `developer-tools` `terminal` `javascript` | 0 | 🆕 2026-07-26 |
| [**herdr-flakes**](https://github.com/iQua/herdr-flakes)<br><sub>iQua</sub> | Herdr 的 Flakes 插件——将你的 Flakes 运行镜像到本地 Herdr 会话并进行操控 | `javascript` | 0 | 🆕 2026-07-22 |
| [**live-sync-panes**](https://github.com/wg1k/live-sync-panes)<br><sub>wg1k</sub> | Herdr 插件：将命令广播，或将按键实时同步到标签页内的所有窗格 | `javascript` | 0 | 2026-07-08 |

<details><summary>与此目的也相关</summary>

- [KokiKono/herdr-kanban](https://github.com/KokiKono/herdr-kanban) — 将任务与 herdr 标签页关联的终端看板，数据持久化在 SQLite 中
- [afogel/shepherdr](https://github.com/afogel/shepherdr) — 将委派出去的编程 Agent 收拢到可见、可审查的 herdr 窗格中，供你观察、恢复和接管的 herdr 插件
- [AkashJana18/herdr-scratch](https://github.com/AkashJana18/herdr-scratch) — 面向 Herdr 的持久化速记板，为浮动实用窗格铺路
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — 为 JavaScript 和 TypeScript 自动初始化 Herdr 工作树，支持基于锁文件的安装和安全的环境变量还原
- [ppggff/herdr-plugin](https://github.com/ppggff/herdr-plugin) — 自动记住并恢复每个 Herdr 窗格对应的正确 macOS 输入法（IME）
- [voodootikigod/adlc-herdr](https://github.com/voodootikigod/adlc-herdr) — ADLC 的 herdr 插件——按窗格显示阶段/工单/关卡状态，附带待办看板、关卡操作和 adlc-fleet 运行可观测性。是 voodootikigod/adlc/plugins/adlc-herdr 的自动同步…

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-naming"></a>

## 标题、命名与外观

> 想让标签页名称和终端标题自动变得清晰易懂，或想改变外观

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-window-title-sync**](https://github.com/rjyo/herdr-window-title-sync)<br><sub>rjyo</sub> | 将工作区、标签页和 Agent 会话同步到终端标题（可配合 Moshi 使用） | `moshi` `terminal-title` `javascript` | 22 | 2026-06-26 |
| [**herdr-tab-smart-rename**](https://github.com/iurysza/herdr-tab-smart-rename)<br><sub>iurysza</sub> | 为 Herdr 生成基于上下文的工作区和标签页名称 | `ai` `bun` `terminal` `typescript` | 21 | 🆕 2026-07-17 |
| [**herdr-flock**](https://github.com/ragamo/herdr-flock)<br><sub>ragamo</sub> | 将你的 AI 编程 Agent 可视化为生活在俯视视角农场里的像素风羊群的 herdr 插件 | `cli` `ratatui` `rust` `tui` | 10 | 2026-07-11 |
| [**herdr-auto-namer**](https://github.com/kakigakki/herdr-auto-namer)<br><sub>kakigakki</sub> | herdr 的 ChatGPT 风格自动命名：Agent 使用其 Claude 会话标题，工作区使用其工作目录名 | `claude-code` `python` | 4 | 2026-07-12 |
| [**herdr-claude-session-title**](https://github.com/bcihanc/herdr-claude-session-title)<br><sub>bcihanc</sub> | Herdr 插件：将 Claude Code 的会话标题（/rename 或自动摘要）同步到 herdr 窗格的元数据标题中 | `shell` | 3 | 2026-07-11 |
| [**herdr-in-your-face**](https://github.com/JYasha11/herdr-in-your-face)<br><sub>JYasha11</sub> | 如果你放着被阻塞的 AI Agent 不管，一个巨大的 ASCII 脸会对你怒吼。你无视得越久，警告就升级得越厉害 | `javascript` | 3 | 2026-07-10 |
| [**herdr-english-coach**](https://github.com/GranamyrBR/herdr-english-coach)<br><sub>GranamyrBR</sub> | herdr 插件：彩色标注的英语纠错面板——在你工作时，编程 Agent 将语法和开发行话的修正实时记录到侧边窗格 | `english` `language-learning` `shell` | 2 | 2026-07-06 |
| [**herdr-tab-rename**](https://github.com/lmilojevicc/herdr-tab-rename)<br><sub>lmilojevicc</sub> | 将每个 Herdr 标签页自动重命名为其聚焦窗格的工作目录名。手动重命名过的标签页不受影响 | `go` | 2 | 2026-07-02 |
| [**herdr-powershell-title-sync**](https://github.com/aclima01/herdr-powershell-title-sync)<br><sub>aclima01</sub> | window-title-sync 的 Windows/PowerShell 移植版：将终端标题同步为当前聚焦的 herdr 会话 | `powershell` | 1 | 🆕 2026-07-20 |
| [**herdr-git-tab-name**](https://github.com/blurname/herdr-git-tab-name)<br><sub>blurname</sub> | 将标签页重命名为聚焦窗格所在 Git 分支名的 Herdr 插件 | `shell` | 1 | 2026-07-06 |
| [**herdr-machine-title**](https://github.com/mikevalstar/herdr-machine-title)<br><sub>mikevalstar</sub> | herdr 插件：将外层终端标题固定为 herdr@<主机名> · <工作区> | `shell` | 0 | 2026-07-02 |
| [**herdr-tab-title**](https://github.com/Newt6611/herdr-tab-title)<br><sub>Newt6611</sub> | Herdr Tab Title 会将 Herdr 标签页自动重命名为整洁的、按工作区独立编号的名称，如「1. Codex」「2. Terminal」，格式可自定义 | `rust` | 0 | 2026-07-09 |
| [**tab-blank-number**](https://github.com/riq0h/tab-blank-number)<br><sub>riq0h</sub> | 将 herdr 默认的数字标签页标签（1、2、3…）清空为空白的 herdr 插件 | `javascript` | 0 | 🆕 2026-07-19 |
| [**tab-process-name**](https://github.com/riq0h/tab-process-name)<br><sub>riq0h</sub> | 为每个标签页标注其前台运行进程名称的 herdr 插件——相当于把 tmux 的 automatic-rename 行为带到 herdr | `javascript` | 0 | 🆕 2026-07-19 |

<details><summary>与此目的也相关</summary>

- [qu8n/herdr-automatic-rename](https://github.com/qu8n/herdr-automatic-rename) — 以 tmux 风格自动重命名 herdr 标签页，并为工作区/标签页/Agent 分配 1-9 的跳转快捷键编号
- [aarsh21/herdr-tab-title](https://github.com/aarsh21/herdr-tab-title) — 为 Herdr 提供类似 tmux 的自动标签页标题
- [wyattjoh/herdr-plugin-renamer](https://github.com/wyattjoh/herdr-plugin-renamer) — 根据 Agent 的第一条提示词，重命名自动生成的 herdr 工作树分支和工作区（通过设备端 Apple FoundationModels 或 Codex）
- [suisya-systems/herdr-agent-office](https://github.com/suisya-systems/herdr-agent-office) — 将你的 Agent 团队呈现为像素风办公室的 herdr 插件。查看谁在工作、谁卡住了，并可直接跳转过去
- [dev-shimada/herdr-auto-tab-name](https://github.com/dev-shimada/herdr-auto-tab-name) — herdr 插件：根据当前目录自动命名标签页
- [filoozom/herdr-title](https://github.com/filoozom/herdr-title) — 在终端标签页标题中显示所选工作树和 Agent 活动状态的 Herdr 插件
- [go-min/herdr-pane-name](https://github.com/go-min/herdr-pane-name) — 为你终端会话中的窗格自动命名的 Herdr 插件
- [KazBrekker1/herdr-hasr](https://github.com/KazBrekker1/herdr-hasr) — Hasr（حصر——意为「枚举、完整清点」）——herdr 的 goto 风格弹窗切换器：切换、重命名、删除并创建 Agent、标签页和空间，并实时追踪完成状态
- [khatriafaz/herdr-plugin-auto-rename](https://github.com/khatriafaz/herdr-plugin-auto-rename) — 根据 Pi 会话的第一条提示词，自动重命名新的 Herdr 工作区和 Git 分支
- [maxBRT/herdr-omarchy-theme-sync](https://github.com/maxBRT/herdr-omarchy-theme-sync) — 将 Herdr 的 UI 配色与当前使用的 Omarchy 主题同步

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-text"></a>

## 文本与 URL 提取

> 想不用鼠标就抓取屏幕上显示的字符串、路径或 URL

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-pluck**](https://github.com/rmarganti/herdr-pluck)<br><sub>rmarganti</sub> | 从 Herdr 窗格中快速复制匹配特定模式的字符串 | `rust` | 15 | 🆕 2026-07-24 |
| [**herdr-tiny-fingers**](https://github.com/hotchpotch/herdr-tiny-fingers)<br><sub>hotchpotch</sub> | 面向 Herdr 的 tmux-fingers 风格可见屏幕复制提示 | `rust` | 5 | 2026-07-10 |
| [**herdr-fingers**](https://github.com/hitaishi2222/herdr-fingers)<br><sub>hitaishi2222</sub> | Fingers to clipboard：从当前窗格中拾取信息的智能浮层 | `python` | 3 | 🆕 2026-07-16 |
| [**herdr-copy-search**](https://github.com/qq88976321/herdr-copy-search)<br><sub>qq88976321</sub> | 面向 herdr 回滚缓冲区的正则表达式和 copycat 模式搜索，配合 extrakto 令牌提取，落地到 tmux 风格的复制模式（OSC 52） | `copy-mode` `rust` `terminal` `tmux` | 2 | 🆕 2026-07-23 |
| [**herdr-scrollback-capture**](https://github.com/alexjsp/herdr-scrollback-capture)<br><sub>alexjsp</sub> | 将聚焦窗格的回滚缓冲区以 HTML 或文本形式保存到桌面的 Herdr 插件 | `shell` | 1 | 2026-06-30 |
| [**herdr-agent-copy-paste-fork**](https://github.com/calebcauthon/herdr-agent-copy-paste-fork)<br><sub>calebcauthon</sub> | 只需复制粘贴即可分叉，或用快捷键将分叉分到新窗格 | `claude-code` `codex` `shell` | 1 | 🆕 2026-07-24 |
| [**herdr-s3-clipboard**](https://github.com/jagzmz/herdr-s3-clipboard)<br><sub>jagzmz</sub> | 使用 S3 兼容存储，将 Herdr 中剪贴板的图片发布为可复用的公开链接或预签名链接 | `aws-s3` `clipboard` `cloudflare-r2` `developer-tools` `image-publishing` | 1 | 🆕 2026-07-16 |
| [**herdr-leap**](https://github.com/RooseveltAdvisors/herdr-leap)<br><sub>RooseveltAdvisors</sub> | 面向 Herdr 终端多路复用器的 EasyMotion/leap 风格字符跳转+选中复制 | `easymotion` `rust` `terminal` `tui` | 1 | 🆕 2026-07-24 |
| [**herdr-copy-hints**](https://github.com/rotemb-wond/herdr-copy-hints)<br><sub>rotemb-wond</sub> | 面向 Herdr 的 tmux-fingers 风格键盘复制提示：路径、Git SHA、URL 等 | `clipboard` `developer-tools` `keyboard-navigation` `productivity` `terminal` | 1 | 🆕 2026-07-23 |

<details><summary>与此目的也相关</summary>

- [iurysza/termscope](https://github.com/iurysza/termscope) — 打开终端屏幕上已经可见的文件和链接
- [tanshio/herdr-worktreeinclude](https://github.com/tanshio/herdr-worktreeinclude) — Herdr 插件：将匹配 .worktreeinclude 的被 gitignore 文件复制到新创建的工作树中
- [jlimas/herdr-worktree-seed](https://github.com/jlimas/herdr-worktree-seed) — 为新工作树植入 copy-on-write 的 node_modules 和可配置本地 dotfiles 的 Herdr 插件
- [Feasy01/herdr-allow](https://github.com/Feasy01/herdr-allow) — herdr 插件：通过 .herdr-allow 允许列表，将被 gitignore 的文件（.env、密钥、本地配置）复制到每个新工作树中
- [crexi/herdr-worktree-copy](https://github.com/crexi/herdr-worktree-copy) — Herdr plugin that copies and symlinks worktree-local files from a .worktree-copy manifest
- [eightHundreds/herdr-worktreeinclude](https://github.com/eightHundreds/herdr-worktreeinclude) — Herdr 插件：将 .worktreeinclude 指定的被 gitignore 文件复制到新工作树中
- [willian/herdr-fzf-url](https://github.com/willian/herdr-fzf-url) — Pick URLs from the focused pane with `fzf`, then open or copy them.

</details>

[⬆ 返回目的列表](#purposes)

<a id="cat-meta"></a>

## 插件管理与开发

> 想管理插件本身，或者自己动手做一个

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-plus**](https://github.com/cloudmanic/herdr-plus)<br><sub>cloudmanic</sub> | herdr 的扩展，作为原生插件构建——一组让 herdr 更好用的工具集：项目管理和快捷操作 | `go` | 172 | 🆕 2026-07-23 |
| [**herdr-lazy**](https://github.com/natori-hrj/herdr-lazy)<br><sub>natori-hrj</sub> | herdr 的声明式插件管理器兼精选发行版——一份清单、真正的锁文件、一个管理窗格 | `cli` `lockfile` `plugin-manager` `rust` `terminal` | 10 | 🆕 2026-07-29 |
| [**herdr-plugin-manager**](https://github.com/speardragon/herdr-plugin-manager)<br><sub>speardragon</sub> | 在弹窗中管理 herdr 插件——安装、更新、启用/禁用、卸载，并浏览 herdr-plugin 市场。推荐快捷键：prefix+p | `plugin-manager` `tui` `shell` | 5 | 🆕 2026-07-22 |
| [**house-of-herdr**](https://github.com/alasano/house-of-herdr)<br><sub>alasano</sub> | Herdr 插件合集 | `typescript` | 2 | 🆕 2026-07-24 |
| [**herdr-plugins-labs**](https://github.com/hmu332233/herdr-plugins-labs)<br><sub>hmu332233</sub> | Herdr 的实验性插件——在这里孵化，成熟后独立成自己的仓库 | `labs` `javascript` | 1 | 🆕 2026-07-18 |
| [**herdr-plugin-rust**](https://github.com/Newt6611/herdr-plugin-rust)<br><sub>Newt6611</sub> | 用于构建 Herdr 插件的 Rust 应用框架 | `rust` | 1 | 2026-07-09 |

[⬆ 返回目的列表](#purposes)

<a id="cat-other"></a>

## 其他与实用工具

> 不属于以上任何分类，但很实用的东西

| 插件 | 能做什么 | 标签 | ★ | 最后更新 |
| --- | --- | --- | --: | --- |
| [**herdr-plugins-directory**](https://github.com/MIDO-ruby7/herdr-plugins-directory)<br><sub>MIDO-ruby7</sub> | A link collection for finding herdr plugins by what you want to get done. | `python` | 4 | 🆕 2026-07-29 |
| [**wave-tui**](https://github.com/takemo101/wave-tui)<br><sub>takemo101</sub> | 适合工作时段的安静终端电台 | `rust` | 4 | 🆕 2026-07-20 |
| [**herdr-plugin-cmux**](https://github.com/lachieh/herdr-plugin-cmux)<br><sub>lachieh</sub> | 将每个由 herdr 管理的 Agent 镜像到 cmux 侧边栏中各自独立的一行——带状态徽标和可点击跳转的任务行 | `javascript` | 3 | 2026-07-01 |
| [**herdr-edit-windows**](https://github.com/aclima01/herdr-edit-windows)<br><sub>aclima01</sub> | 在编程 Agent 旁边的 herdr 窗格中运行的简易文本编辑器——文件树、语法高亮编辑器、未提交差异标签页。仅支持 Windows | `rust` | 1 | 🆕 2026-07-25 |
| [**herdr-stoplight**](https://github.com/BowlOfSoup/herdr-stoplight)<br><sub>BowlOfSoup</sub> | 根据 Herdr 的实时状态驱动一个物理 Arduino 红绿灯模块 | `go` | 1 | 2026-07-11 |
| [**herdr-suite-site**](https://github.com/StructuPath/herdr-suite-site)<br><sub>StructuPath</sub> | Landing page for the StructuPath Herdr Suite — herdr.structupath.ai | `herdr-integration` `html` | 1 | 🆕 2026-07-29 |
| [**herdr-commandcode-plugin**](https://github.com/TheMetalStorm/herdr-commandcode-plugin)<br><sub>TheMetalStorm</sub> | 将 Commandcode 集成到 Herdr 中 | `cli` `commandcode` `herdr-integration` `shell` | 1 | 🆕 2026-07-20 |
| [**herdr-freebuff-plugin**](https://github.com/TheMetalStorm/herdr-freebuff-plugin)<br><sub>TheMetalStorm</sub> | Herdr 的 Freebuff 生命周期集成插件——通过文件轮询和 PTY 内容抓取来报告闲置/工作中/被阻塞状态 | `cli` `freebuff` `herdr-integration` `shell` | 1 | 🆕 2026-07-22 |
| [**herdr-attach**](https://github.com/gilvanecesar/herdr-attach)<br><sub>gilvanecesar</sub> | 从 Herdr 弹窗中选择本地文件并发送给聚焦中的编程 Agent——无需离开终端即可附加文件上下文 | `javascript` | 0 | 🆕 2026-07-26 |
| [**herdr-llama**](https://github.com/hitaishi2222/herdr-llama)<br><sub>hitaishi2222</sub> | 在指尖操控你的 llama-server | `llama-cpp` `local-ai` `python` | 0 | 🆕 2026-07-16 |
| [**herdr-pane-update-timestamps**](https://github.com/johnlindquist/herdr-pane-update-timestamps)<br><sub>johnlindquist</sub> | Herdr plugin for timestamped, scrollable pane output observations | `rust` | 0 | 🆕 2026-07-29 |
| [**herdr-laravel-tinker**](https://github.com/lancodev/herdr-laravel-tinker)<br><sub>lancodev</sub> | herdr 的分屏式 Laravel tinker REPL——编辑器旁边实时显示运行结果，可作为窗格或弹窗使用 | `laravel` `tinker` `php` `repl` | 0 | 🆕 2026-07-16 |
| [**herdr-new-task**](https://github.com/leonho/herdr-new-task)<br><sub>leonho</sub> | herdr 插件：一键选择项目目录并在新标签页中启动 claude，标签页采用名词优先的命名方式 | `python` | 0 | 🆕 2026-07-16 |
| [**herdr-plugin-loopreview**](https://github.com/loopkeep/herdr-plugin-loopreview)<br><sub>loopkeep</sub> | 用于 loopreview 的 Herdr 插件 | `rust` | 0 | 🆕 2026-07-23 |
| [**herdr-hint**](https://github.com/maedana/herdr-hint)<br><sub>maedana</sub> | Herdr 的 Vimium 风格提示标签——按键后在标签页和 Agent 上显示标签，再按标签即可跳转 | `rust` | 0 | 🆕 2026-07-22 |
| [**herdr-whereami**](https://github.com/maedana/herdr-whereami)<br><sub>maedana</sub> | 自动重命名标签页以显示你当前所在位置的 Herdr 插件——在 git 仓库内会显示为「仓库名/分支名」 | `rust` | 0 | 🆕 2026-07-22 |
| [**herdr-phin-util**](https://github.com/phin-tech/herdr-phin-util)<br><sub>phin-tech</sub> | 个人 Herdr 实用工具集 | `bubbletea` `tui` `go` | 0 | 🆕 2026-07-29 |
| [**herdr-traex-integration**](https://github.com/Phoobobo/herdr-traex-integration)<br><sub>Phoobobo</sub> | 支持 traex 集成的 Herdr 插件 | `shell` | 0 | 2026-07-02 |
| [**herdr-handsfree**](https://github.com/RanolP/herdr-handsfree)<br><sub>RanolP</sub> | Hands-free herdr plugin: voice dictation (whisper.cpp) + webcam gaze mouse for macOS | `rust` | 0 | 🆕 2026-07-28 |
| [**herdr-browser**](https://github.com/redsquiggle/herdr-browser)<br><sub>redsquiggle</sub> | Keep Chromium tab groups aligned with Herdr workspaces | `chromium` `ratatui` `rust` | 0 | 🆕 2026-07-28 |
| [**herdr-plugins**](https://github.com/tomaszhanc/herdr-plugins)<br><sub>tomaszhanc</sub> | 个人的 herdr 插件 monorepo，每个插件都在自己的文件夹中，附带 herdr-plugin.toml 清单和可执行文件 | — | 0 | 🆕 2026-07-16 |

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
