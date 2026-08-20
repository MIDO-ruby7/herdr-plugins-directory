# herdr plugins by purpose

🇯🇵 日本語 · [🇺🇸 English](README.en.md) · [🇨🇳 中文](README.zh.md)

**「◯◯したい」から herdr のプラグインを探すためのリンク集です。**

- 収録 **716** 件 / 最終更新 **2026-08-20 01:51 UTC**（6 時間ごとに自動更新）
- データ元: GitHub topic [`herdr-plugin`](https://github.com/topics/herdr-plugin) — 公式マーケットプレイス [herdr.dev/plugins](https://herdr.dev/plugins/) と同じ母集団
- 分類はリポジトリの説明文とトピックからの自動推定です。おかしなものは [`data/overrides.json`](data/overrides.json) の PR で直せます
- インストール: `herdr plugin install owner/repo` — [公式ドキュメント](https://herdr.dev/docs/plugins/)

> [!WARNING]
> ここは自動収集の索引で、審査済みカタログではありません。プラグインは自分のマシンでそのまま動くコードなので、入れる前にマニフェストと実行されるコマンドを確認してください。

<a id="purposes"></a>

## 目的から探す

- [**🆕 最近追加されたプラグイン**](#cat-new) (118) — 直近 7 日以内にこの一覧に加わったプラグインです。
- [**通知・アラート**](#cat-notify) (26) — エージェントが完了した / 入力待ちで止まったのを、席を外していても知りたい
- [**スマホ・リモート操作**](#cat-remote) (30) — 外出先やスマホからエージェントを監視して、承認だけ返したい
- [**エージェント統括・並列実行**](#cat-agents) (99) — 複数の AI エージェントをまとめて起動・分担・管理したい
- [**git worktree・ブランチ運用**](#cat-worktree) (39) — 作業ごとに worktree を切って、片付けまで自動でやりたい
- [**コードレビュー・差分確認**](#cat-review) (32) — エージェントが書いた差分を読んで、コメントを返したい
- [**GitHub / issue トラッカー連携**](#cat-forge) (27) — issue や PR を起点に作業を始めたい / PR の状態を追いたい
- [**ワークスペース・レイアウト構築**](#cat-layout) (30) — プロジェクトを開いたら、タブ・ペイン・起動コマンドまで一発で整えたい
- [**ペイン移動・キー操作**](#cat-navigate) (82) — ペインやワークスペース間の移動・リサイズを、エディタと同じキーで済ませたい
- [**ファイル閲覧・エディタ連携**](#cat-files) (50) — ペインの中でファイルツリーを開いたり、エディタ側と状態を揃えたい
- [**トークン・コスト管理**](#cat-cost) (16) — エージェントがいくら使っているかを見たい / 使用量を削りたい
- [**監視・ダッシュボード**](#cat-monitor) (41) — エージェントやマシンの状態を一覧で眺めたい
- [**検索・ファジーファインダー**](#cat-finder) (72) — コマンドやプロジェクトを、名前をうろ覚えのまま呼び出したい
- [**自動化・フック・定期実行**](#cat-automation) (37) — worktree 作成時やタイミングを決めて、決まった手順を自動で走らせたい
- [**セッション保存・復元**](#cat-session) (29) — 作業を閉じても、あとで同じ状態から再開したい
- [**タイトル・命名・見た目**](#cat-naming) (39) — タブ名やターミナルタイトルを自動で分かりやすくしたい / 見た目を変えたい
- [**テキスト・URL 抽出**](#cat-text) (12) — 画面に出ている文字列やパス・URL を、マウスなしで拾いたい
- [**プラグイン管理・開発**](#cat-meta) (8) — プラグイン自体を管理したい / 自分で作りたい
- [**その他・ユーティリティ**](#cat-other) (47) — 上のどれにも当てはまらない便利もの

<a id="cat-new"></a>

## 🆕 最近追加されたプラグイン

> 直近 7 日以内にこの一覧に加わったプラグインです。

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**🆕 herdr-pane-orientation-switcher**](https://github.com/sf1tzp/herdr-pane-orientation-switcher)<br><sub>sf1tzp</sub> | Workflow Ergonomics for Split Panes in Herdr | `shell` | 1 | 2026-07-25 |
| [**🆕 herdr**](https://github.com/AgentTeamsRun/herdr)<br><sub>AgentTeamsRun</sub> | Report herdr worktree lifecycle events to the AgentTeams registry | — | 0 | 2026-08-19 |
| [**🆕 herdr-tilt**](https://github.com/the-inconvenience-store/herdr-tilt)<br><sub>the-inconvenience-store</sub> | _(説明なし)_ | `rust` | 0 | 2026-08-20 |
| [**🆕 herdr-kakoune-popup**](https://github.com/Yukaii/herdr-kakoune-popup)<br><sub>Yukaii</sub> | Run Kakoune terminal commands in native Herdr popups. | `kakoune` `shell` | 0 | 2026-08-20 |
| [**🆕 herdr-connect**](https://github.com/Tomyail/herdr-connect)<br><sub>Tomyail</sub> | Open-source LAN companion app for discovering and connecting to Herdr installations | `agent` `mobile-app` `react-native` `typescript` | 5 | 2026-08-19 |
| [**🆕 herdr-lantern**](https://github.com/aigorahub/herdr-lantern)<br><sub>aigorahub</sub> | Lantern, by Elves. A Herdr plugin: the herd is in the field; Lantern illuminates who needs you and what they are working toward. | `python` | 3 | 2026-08-19 |
| [**🆕 herdr-ssh-manager**](https://github.com/jorge07RD/herdr-ssh-manager)<br><sub>jorge07RD</sub> | Save SSH hosts and reconnect from a fuzzy popup inside Herdr — Enter hands the popup straight to ssh. | `rust` `ssh` `terminal` `tui` | 3 | 2026-08-19 |
| [**🆕 herdr-quota**](https://github.com/kvkenyon/herdr-quota)<br><sub>kvkenyon</sub> | See Claude, Codex, Cursor, and Kimi subscription quota at a glance in Herdr. | `ai-tools` `claude-code` `cursor` `developer-tools` `kimi` | 2 | 2026-08-19 |
| [**🆕 herdr-theme-picker**](https://github.com/qintmb/herdr-theme-picker)<br><sub>qintmb</sub> | Theme picker for herdr UI based terminalcolors scheme and your customization. | `shell` | 2 | 2026-08-19 |
| [**🆕 herdr-workspace-save**](https://github.com/chandrasekharan98/herdr-workspace-save)<br><sub>chandrasekharan98</sub> | Save a Herdr workspace — layout, cwds, agent sessions, running commands — and reopen it later from an fzf picker. | `claude-code` `terminal` `tmux` `python` | 1 | 2026-08-19 |
| [**🆕 herdr-cliamp**](https://github.com/coryshaw1/herdr-cliamp)<br><sub>coryshaw1</sub> | Floating cliamp for herdr that keeps playing when hidden: the player lives in a detached herdr session, so closing the float only detaches. | `audiobook` `cliamp` `music-player` `podcast` `terminal` | 1 | 2026-08-19 |
| [**🆕 herdr-zen**](https://github.com/y4m3/herdr-zen)<br><sub>y4m3</sub> | Zen mode for Herdr with an adjustable centered pane width | `rust` `terminal` `zen-mode` | 1 | 2026-08-19 |
| [**🆕 herdrchat**](https://github.com/cobanov/herdrchat)<br><sub>cobanov</sub> | HerdrChat — control your herdr coding agents from your phone (iOS + Android) | `herdr-client` `herdr-integration` `herdr-mobile` `typescript` | 0 | 2026-08-19 |
| [**🆕 herdr-prompt-bucket**](https://github.com/GNURub/herdr-prompt-bucket)<br><sub>GNURub</sub> | A durable, ordered prompt bucket for coding agents running in Herdr | `claude-code` `codex` `coding-agents` `opencode` `typescript` | 0 | 2026-08-19 |
| [**🆕 herdr-web-broker**](https://github.com/JefeLabs/herdr-web-broker)<br><sub>JefeLabs</sub> | REST/WS gateway and parent-child federation for herdr instances | `typescript` | 0 | 2026-08-19 |
| [**🆕 herdr-prompts**](https://github.com/oppenheimor/herdr-prompts)<br><sub>oppenheimor</sub> | Save, search, fill, and reuse prompt templates across coding agents in Herdr. Inspired by my friend: bingguanqi | `typescript` | 0 | 2026-08-19 |
| [**🆕 herdr-pane-equalizer**](https://github.com/shanefully-done/herdr-pane-equalizer)<br><sub>shanefully-done</sub> | Resize herdr panes equally; automatically or manually. | `javascript` | 0 | 2026-08-20 |
| [**🆕 herdr-fleece**](https://github.com/sjh9714/herdr-fleece)<br><sub>sjh9714</sub> | Know when your herd is fleecing you. Live tokens, dollars and burn rate for every herdr pane, one screen. herdr 实时成本与燃烧速率控制台. | `ai-agents` `burn-rate` `ccusage` `claude-code` `cli` | 0 | 2026-08-19 |
| [**🆕 herdr-translate**](https://github.com/wenPKtalk/herdr-translate)<br><sub>wenPKtalk</sub> | Herdr plugin: translate the selected text in a pane with translate-shell, shown in a floating popup (macOS and Linux) | `translate` `shell` | 0 | 2026-08-19 |
| [**🆕 clauth**](https://github.com/uwuclxdy/clauth)<br><sub>uwuclxdy</sub> | Claude Code multi-account manager, usage monitor (CLI, TUI & MCP task delegation) | `account-manager` `account-switcher` `anthropic` `claude` `claude-code` | 63 | 2026-08-19 |
| [**🆕 pi-workflows**](https://github.com/osolmaz/pi-workflows)<br><sub>osolmaz</sub> | Workflow engine, JSON control-flow tool, and live terminal viewer for the pi coding agent | `typescript` | 51 | 2026-08-19 |
| [**🆕 herdkit**](https://github.com/briankeegan1/herdkit)<br><sub>briankeegan1</sub> | Governance and parallelism for herdr-based agent workflows — a coordinator drains your backlog into isolated worktree builders (Claude Code, Codex, or Grok), a… | `shell` | 6 | 2026-08-19 |
| [**🆕 herdr-trail**](https://github.com/catoncat/herdr-trail)<br><sub>catoncat</sub> | Herd-wide shared memos for herdr: agents jot follow-ups, humans manage one global list, every entry jumps back to its source conversation | `javascript` | 6 | 2026-08-18 |
| [**🆕 herdr-swipe**](https://github.com/husniadil/herdr-swipe)<br><sub>husniadil</sub> | Trackpad gestures for Herdr: move between panes, tabs and spaces, and jump to the agent waiting on you | `cgeventtap` `gestures` `macos` `python` `terminal` | 3 | 2026-08-18 |
| [**🆕 herdr-e2b-sandbox**](https://github.com/e2b-dev/herdr-e2b-sandbox)<br><sub>e2b-dev</sub> | herdr plugin that mirrors a git worktree into an E2B sandbox — one box or a branch-per-agent fleet, with a TUI dashboard | `cli` `cloud-dev` `e2b` `git-worktree` `sandbox` | 2 | 2026-08-19 |
| [**🆕 herdr-prevtab**](https://github.com/joo-was-already-taken/herdr-prevtab)<br><sub>joo-was-already-taken</sub> | Herdr plugin for switching to the previously focused tab | `rust` | 2 | 2026-08-18 |
| [**🆕 herdr-portal**](https://github.com/loofare/herdr-portal)<br><sub>loofare</sub> | Mission-control dashboard for herdr — aggregates every workspace/tab/pane agent into a live TUI kanban (keyboard + mouse) plus a web big-screen: structured pro… | `agent-dashboard` `agent-monitor` `ai-agents` `claude-code` `codex` | 2 | 2026-08-18 |
| [**🆕 chatter**](https://github.com/marcvermeeren/chatter)<br><sub>marcvermeeren</sub> | Chatter is an experiment in cross-harness agent collaboration: a shared group chat and context layer for agents working on the same Git repository in Herdr. | `agent-collaboration` `agentic-ai` `agentic-workflow` `ai-agents` `group-chat` | 2 | 2026-08-18 |
| [**🆕 herdr-co-review**](https://github.com/elKei24/herdr-co-review)<br><sub>elKei24</sub> | Split-screen PR review in herdr: your agent finds issues, you triage each one next to its code in a TUI, the agent posts what you approve. | `cli` `code-review` `pull-request` `rust` `tui` | 1 | 2026-08-19 |
| [**🆕 herdr-icon-agent-ui**](https://github.com/qintmb/herdr-icon-agent-ui)<br><sub>qintmb</sub> | Renders Agent icon, vertically-aligned monochrome icons in the Herdr sidebar. rendered via a custom font with non-uniform glyph scaling that matches terminal c… | `python` | 1 | 2026-08-18 |
| [**🆕 herdr-nixos-vm**](https://github.com/Slimydog21/herdr-nixos-vm)<br><sub>Slimydog21</sub> | The NixOS VM pane for herdr — boot, stop, watch, and ssh into your Hashimoto-style dev VM. Requires the nixos-vm kit. | `shell` | 1 | 2026-08-18 |
| [**🆕 herdr-polyglot**](https://github.com/wazum/herdr-polyglot)<br><sub>wazum</sub> | Write coding-agent prompts in your own language — DeepL or Google Cloud Translate translates them to English and delivers them into Claude Code, Codex or any h… | `ai-agents` `bubbletea` `bubbletea-tui` `claude-code` `codex` | 1 | 2026-08-19 |
| [**🆕 herdr-confirm-close**](https://github.com/asumaran/herdr-confirm-close)<br><sub>asumaran</sub> | Herdr plugin: close the focused pane, asking first only when a process is running in it | `terminal` `go` | 0 | 2026-08-17 |
| [**🆕 herdr-locksmith**](https://github.com/bkarpinos/herdr-locksmith)<br><sub>bkarpinos</sub> | keybinding command palette for herdr | `typescript` | 0 | 2026-08-18 |
| [**🆕 herdr-pane-id**](https://github.com/imtim/herdr-pane-id)<br><sub>imtim</sub> | herdr plugin: label panes with their ID and agent name, plus tab and workspace id labels — so you and your agents can address any pane or agent by id. Works be… | `ai-agents` `coding-agents` `developer-tools` `terminal-multiplexer` `tui` | 0 | 2026-08-18 |
| [**🆕 herdr-tab-numbers**](https://github.com/kokatsu/herdr-tab-numbers)<br><sub>kokatsu</sub> | Prefix each tab name with its switch_tab position | `shell` | 0 | 2026-08-18 |
| [**🆕 herdr-diff-review.nvim**](https://github.com/rytkmt/herdr-diff-review.nvim)<br><sub>rytkmt</sub> | Review AI agent file changes in Neovim diff mode before applying — approve or deny edits from Claude Code and Kiro CLI with a single command. AIエージェントのファイル変更をN… | `kiro-cli` `neovim` `neovim-plugin` `neovim-plugins` `nvim` | 0 | 2026-08-18 |
| [**🆕 herdr-model-quota**](https://github.com/terry-li-hm/herdr-model-quota)<br><sub>terry-li-hm</sub> | Herdr plugin for compact Codex and Claude Max subscription quota visibility | `claude` `codex` `quota` `terminal` `python` | 0 | 2026-08-18 |
| [**🆕 herdr-telescope**](https://github.com/zackshen/herdr-telescope)<br><sub>zackshen</sub> | fzf command telescope for herdr: native actions, plugin actions, file finder (@), and live ripgrep search (/) | `fzf` `rust` | 0 | 2026-08-19 |
| [**🆕 herdr-opentab**](https://github.com/hamidi-dev/herdr-opentab)<br><sub>hamidi-dev</sub> | Live per-agent AI spend from OpenTab in the Herdr sidebar. | `ai-agents` `opentab` `terminal` `python` | 3 | 2026-08-18 |
| [**🆕 herdr-api-credit-bar**](https://github.com/CristianPeralta/herdr-api-credit-bar)<br><sub>CristianPeralta</sub> | Herdr plugin: remaining credit for pay-as-you-go API providers, starting with Alibaba Cloud Model Studio | `shell` | 2 | 2026-08-18 |
| [**🆕 herdr-pouch**](https://github.com/AltanS/herdr-pouch)<br><sub>AltanS</sub> | Herdr plugin: stash prompts for an agent ahead of time and insert them when it's ready | `typescript` | 1 | 2026-08-19 |
| [**🆕 herdr-simple-prompts**](https://github.com/AlexSamarsky/herdr-simple-prompts)<br><sub>AlexSamarsky</sub> | Only your prompts and the final answers from Codex or Claude, with a working composer | `rust` | 0 | 2026-08-18 |
| [**🆕 herdr-slack**](https://github.com/egemenyildiz/herdr-slack)<br><sub>egemenyildiz</sub> | Drive your local herdr agents from Slack — browse, prompt, and launch from your phone. No tunnel. | `slack` `typescript` | 0 | 2026-08-19 |
| [**🆕 herdr-plugin-command-palette**](https://github.com/haisi/herdr-plugin-command-palette)<br><sub>haisi</sub> | Fuzzy-searchable command palette for herdr, backed by fzf | `fzf` `python` | 0 | 2026-08-17 |
| [**🆕 agentic-box**](https://github.com/nicoRomeroCuruchet/agentic-box)<br><sub>nicoRomeroCuruchet</sub> | An isolated box where Claude Code drives local model agents. | `agent-orchestration` `agentic` `agentic-workflow` `docker` `ornith-1-0-35b` | 0 | 2026-08-17 |
| [**🆕 herdr-atuin-plugin**](https://github.com/smanickam01/herdr-atuin-plugin)<br><sub>smanickam01</sub> | Atuin shell history search in a herdr popup — press prefix+a, Enter to run or Tab to edit. Binds itself on install. | `atuin` `macos` `shell-history` `terminal` `zsh` | 0 | 2026-08-17 |
| [**🆕 herdr-lens**](https://github.com/VoidAxon/herdr-lens)<br><sub>VoidAxon</sub> | Select text in a Herdr pane, press a key, read it in your own language. Translation, dictionary, identifier lookup and summaries — stdlib-only, zero config. | `ai` `cli` `terminal` `translation` `python` | 0 | 2026-08-19 |
| [**🆕 herdr-paddock**](https://github.com/neyham/herdr-paddock)<br><sub>neyham</sub> | 🐑 A card-wall feed for your herdr agents — glance over the flock, zoom into one, reply, all over plain SSH | `bubbletea` `go` `ssh` `tui` | 4 | 2026-08-17 |
| [**🆕 herdr-rainfrog**](https://github.com/fraction12/herdr-rainfrog)<br><sub>fraction12</sub> | Open Rainfrog in a managed HerdR pane. | `shell` | 1 | 2026-08-15 |
| [**🆕 herdr-command-palette**](https://github.com/hota911/herdr-command-palette)<br><sub>hota911</sub> | fzf command palette for herdr's built-in operations — workspaces, tabs, panes, agents | `command-palette` `fzf` `shell` | 1 | 2026-08-16 |
| [**🆕 herdr-cursor-open**](https://github.com/alex-devdone/herdr-cursor-open)<br><sub>alex-devdone</sub> | Open the focused herdr pane in Cursor or VS Code — including panes attached to a remote herdr, over Remote-SSH | `cursor` `vscode` `shell` | 0 | 2026-08-15 |
| [**🆕 herdr-agent-team**](https://github.com/gdli6177/herdr-agent-team)<br><sub>gdli6177</sub> | A Herdr plugin for Markdown-defined agent teams | `javascript` | 0 | 2026-08-16 |
| [**🆕 herdr-agent-icons**](https://github.com/moneycaringcoder/herdr-agent-icons)<br><sub>moneycaringcoder</sub> | A minimal Herdr plugin that gives the sidebar recognizable monochrome harness marks for Claude, Codex, OpenCode, and OMP without taking over Herdr lifecycle st… | `icons` `python` `terminal` | 0 | 2026-08-16 |
| [**🆕 herdr-collide**](https://github.com/moneycaringcoder/herdr-collide)<br><sub>moneycaringcoder</sub> | Warns when agents working in different git worktrees of one repo are about to collide — and whether their edits merely overlap or will actually conflict. | `conflict-detection` `git-worktree` `rust` `terminal` | 0 | 2026-08-19 |
| [**🆕 herdr-pulse**](https://github.com/moneycaringcoder/herdr-pulse)<br><sub>moneycaringcoder</sub> | Per-workspace agent activity history for herdr, rendered as a sidebar sparkline. | `monitoring` `rust` `sparkline` `terminal` | 0 | 2026-08-16 |
| [**🆕 herdr-redact**](https://github.com/moneycaringcoder/herdr-redact)<br><sub>moneycaringcoder</sub> | Warns you when an agent pane has printed a credential — before you screenshot it, stream it, or paste it into a chat window. | `rust` `secret-detection` `security` `terminal` | 0 | 2026-08-18 |
| [**🆕 herdr-shear**](https://github.com/moneycaringcoder/herdr-shear)<br><sub>moneycaringcoder</sub> | Find the git worktrees that are safe to delete, and delete those. A worktree janitor for herdr. | `cleanup` `git-worktree` `rust` `terminal` | 0 | 2026-08-19 |
| [**🆕 herdr-standup**](https://github.com/moneycaringcoder/herdr-standup)<br><sub>moneycaringcoder</sub> | A digest of what your agents actually did. One command, one readable summary of every Herdr workspace over a time window — commits, change volume, branch, and… | `git` `rust` `standup` `terminal` | 0 | 2026-08-16 |
| [**🆕 dsh-plugin-herdr**](https://github.com/sunny0826/dsh-plugin-herdr)<br><sub>sunny0826</sub> | Herdr control-plane plugin for DeepSeek Harness (DSH): observe and drive Herdr — a terminal workspace manager for AI coding agents — from DSH sessions | `dsh-plugin` `typescript` | 0 | 2026-08-20 |
| [**🆕 herdr-jump**](https://github.com/tp6gw94/herdr-jump)<br><sub>tp6gw94</sub> | Keyboard navigation for Herdr workspaces, tabs, panes, and agents. | `javascript` | 0 | 2026-08-16 |
| [**🆕 oh-my-opencode-slim**](https://github.com/alvinunreal/oh-my-opencode-slim)<br><sub>alvinunreal</sub> | Lean, fine tuned Opencode multi agent suite · Mix any models · Auto delegate tasks | `agentic-ai` `antigravity` `cerebras` `oh-my-opencode` `opencode` | 8252 | 2026-08-19 |
| [**🆕 herdr-file-annotator**](https://github.com/JonasBaeumer/herdr-file-annotator)<br><sub>JonasBaeumer</sub> | A plugin for herder to maximize agentic development without losing touch with the actual codebase | `rust` | 12 | 2026-08-19 |
| [**🆕 herdr-agent-quota**](https://github.com/levi-qiao/herdr-agent-quota)<br><sub>levi-qiao</sub> | Never hit a quota limit mid-task: see Claude, Codex, Grok and Agy usage live in your Herdr sidebar. 5h and weekly percent remaining. | `agent-usage` `agy` `ai-agents` `antigravity` `claude-code` | 3 | 2026-08-17 |
| [**🆕 herdr-agent-watcher**](https://github.com/winoooops/herdr-agent-watcher)<br><sub>winoooops</sub> | Coding-agent observability for Herdr: live sidebar cards, lifecycle notifications, and a zero-config Claude Code metrics bridge. | `claude-code` `rust` | 3 | 2026-08-19 |
| [**🆕 herdr-prompt-library**](https://github.com/jwkicklighter/herdr-prompt-library)<br><sub>jwkicklighter</sub> | A Herdr plugin for browsing, managing, and inserting reusable local or global Markdown prompts into the focused pane. | `go` `golang` `prompting` `snippets` `tui` | 2 | 2026-08-14 |
| [**🆕 herdr-agent-notify**](https://github.com/A1exthegreat/herdr-agent-notify)<br><sub>A1exthegreat</sub> | Herdr plugin: desktop notifications when agents finish working, need confirmation, or go idle | `javascript` | 1 | 2026-08-15 |
| [**🆕 herdr-plugins**](https://github.com/alastairsounds/herdr-plugins)<br><sub>alastairsounds</sub> | Plugins for herdr | `rust` | 0 | 2026-08-14 |
| [**🆕 Renderd**](https://github.com/Brutheron/Renderd)<br><sub>Brutheron</sub> | Live Markdown reader for completed Claude Code and Codex responses in Herdr | `go` | 0 | 2026-08-15 |
| [**🆕 setnet**](https://github.com/chano-gpt/setnet)<br><sub>chano-gpt</sub> | Herd multi-harness coding agents from your phone — a Herdr plugin | `typescript` | 0 | 2026-08-15 |
| [**🆕 herdr-teams-notify**](https://github.com/donghaolicd/herdr-teams-notify)<br><sub>donghaolicd</sub> | Herdr plugin for bounded Microsoft Teams agent lifecycle notifications | `automation` `microsoft-teams` `notifications` `javascript` | 0 | 2026-08-15 |
| [**🆕 ayatsumugi**](https://github.com/nkwork9999/ayatsumugi)<br><sub>nkwork9999</sub> | Local-first React DOM, Fiber, and state graph visualization for Ayatori and Tsumugi | `cmux` `ghostty` `orca` `react-devtools` `javascript` | 0 | 2026-08-15 |
| [**🆕 herdr-sidekick**](https://github.com/qapquiz/herdr-sidekick)<br><sub>qapquiz</sub> | Toggleable sidekick AI-agent pane for Herdr — paste code selections into the agent's composer without submitting. Pairs with qapquiz/herdr-sidekick.nvim. | `neovim` `terminal` `shell` | 0 | 2026-08-15 |
| [**🆕 herdr-tabpick**](https://github.com/sushidesu/herdr-tabpick)<br><sub>sushidesu</sub> | Pick a herdr tab, most recently used first, with a live pane preview. | `shell` | 0 | 2026-08-15 |
| [**🆕 herdr-restart-always**](https://github.com/terafin/herdr-restart-always)<br><sub>terafin</sub> | Supervise herdr agent panes and always restart whatever the pane is running (claude, hermes, codex, pi, opencode, ...) whenever the agent dies. | `python` | 0 | 2026-08-15 |
| [**🆕 herdr-group-chat**](https://github.com/terry-li-hm/herdr-group-chat)<br><sub>terry-li-hm</sub> | A shared local Herdr room for Pi, Claude Code, Codex, and Grok Build. | `ai-agents` `claude-code` `codex` `grok` `multi-agent` | 0 | 2026-08-16 |
| [**🆕 herdr-plugin-k8s-context**](https://github.com/tkuchiki/herdr-plugin-k8s-context)<br><sub>tkuchiki</sub> | Open Herdr tabs with isolated Kubernetes contexts and namespaces. | `go` | 0 | 2026-08-15 |
| [**🆕 dotfiles**](https://github.com/Unique-Divine/dotfiles)<br><sub>Unique-Divine</sub> | Dotfiles and other ~ configuration from Unique Divine | `dotfiles` `lua` `neovim` `neovim-dotfiles` `nvim` | 0 | 2026-08-19 |
| [**🆕 herdr-event-log**](https://github.com/waynewu411/herdr-event-log)<br><sub>waynewu411</sub> | Herdr plugin: logs pane.agent_status_changed (and future event types) to a durable, cursor-resumable global log any parent agent can tail. | `go` | 0 | 2026-08-15 |
| [**🆕 herdr-hunk-diff**](https://github.com/jhochenbaum/herdr-hunk-diff)<br><sub>jhochenbaum</sub> | Review agent-authored changes in hunk from herdr and send inline comments back to the responsible agent. | `code-review` `hunk` `typescript` | 73 | 2026-08-19 |
| [**🆕 herdr-dagr**](https://github.com/aemrebarut/herdr-dagr)<br><sub>aemrebarut</sub> | Your agent swarm as a live DAG: an orchestration graph with attempts, review gates, and evidence, in a herdr split pane. | `agents` `dag` `multi-agent` `orchestration` `rust` | 18 | 2026-08-19 |
| [**🆕 herdr-tmux-layout**](https://github.com/crierr/herdr-tmux-layout)<br><sub>crierr</sub> | tmux-style preset layouts for live Herdr panes: cycle, even-horizontal, even-vertical, main-horizontal, main-vertical, tiled, and balance | `go` | 2 | 2026-08-14 |
| [**🆕 herdr-statusline**](https://github.com/iiii1224/herdr-statusline)<br><sub>iiii1224</sub> | herdrセッション向けのカスタマイズ可能なステータスライン | `cli` `statusbar` `statusline` `tmux` `python` | 2 | 2026-08-15 |
| [**🆕 herdr-discord-presence**](https://github.com/revanp/herdr-discord-presence)<br><sub>revanp</sub> | Herdr plugin: show your Herdr session and agent status as Discord Rich Presence | `typescript` | 2 | 2026-08-14 |
| [**🆕 herdr-prayer-times**](https://github.com/bayoudhi/herdr-prayer-times)<br><sub>bayoudhi</sub> | Next Islamic prayer and countdown in the Herdr sidebar, with a timetable popup and notifications | `rust` | 1 | 2026-08-13 |
| [**🆕 herdr-jira-board**](https://github.com/kiitosu/herdr-jira-board)<br><sub>kiitosu</sub> | Jira kanban board inside herdr with Claude Code session launcher | `python` | 1 | 2026-08-17 |
| [**🆕 herdr-fleet**](https://github.com/Northern-Lighthouse/herdr-fleet)<br><sub>Northern-Lighthouse</sub> | Manage a fleet of herdr machines over Tailscale: dashboard plugin, auto-discovery, capacity-aware agent dispatch, diskless workspaces | `ai-agents` `tailscale` `python` | 1 | 2026-08-14 |
| [**🆕 herdr-lazygit-viewer**](https://github.com/tareqmlx/herdr-lazygit-viewer)<br><sub>tareqmlx</sub> | Opens lazygit at the files, branches, commits, or stash panel, in whichever Herdr surface suits the moment. | `code-review` `lazygit` `rust` | 1 | 2026-08-14 |
| [**🆕 attic**](https://github.com/TheThoughtagen/attic)<br><sub>TheThoughtagen</sub> | Auto-closes idle AI coding sessions, but archives each one first so you can restore it. | `claude-code` `developer-tools` `python` `session-management` `tui` | 1 | 2026-08-14 |
| [**🆕 herdr-codex-resume**](https://github.com/adamwangxx/herdr-codex-resume)<br><sub>adamwangxx</sub> | Open the native Codex resume picker in a new Herdr split with live Herdr context. | `codex-cli` `terminal` `shell` | 0 | 2026-08-15 |
| [**🆕 buzzr**](https://github.com/candypoets/buzzr)<br><sub>candypoets</sub> | Mirror live Herdr spaces and agents into Buzz channels with Nostr identities and mention routing. | `agents` `buzz` `nostr` `rust` | 0 | 2026-08-14 |
| [**🆕 herdr-habitat**](https://github.com/chantlong/herdr-habitat)<br><sub>chantlong</sub> | herdr habitat is a living terminal habitat that grows alongside your agents’ work. Nurturing takes time, so no agentmaxxing please. As agents burn tokens in en… | `chill` `cozy` `javascript` | 0 | 2026-08-16 |
| [**🆕 herdr-opencode-sessions**](https://github.com/damianpoole/herdr-opencode-sessions)<br><sub>damianpoole</sub> | A Herdr plugin for fuzzy-searching previous OpenCode sessions by title, project, path, date, or transcript content, with conversation previews and shortcuts to… | `typescript` | 0 | 2026-08-14 |
| [**🆕 herdr-agents**](https://github.com/dleen/herdr-agents)<br><sub>dleen</sub> | An fzf agent picker for herdr: every agent pane, worst-first, with a session preview and one-key launching. | `coding-agents` `fzf` `python` `terminal` | 0 | 2026-08-20 |
| [**🆕 herdr-kit**](https://github.com/kevinWangSheng/herdr-kit)<br><sub>kevinWangSheng</sub> | Declarative layouts, an event watcher, plugins and a socket client for Herdr — the parts the herdr CLI does not expose | `coding-agents` `terminal-multiplexer` `python` | 0 | 2026-08-14 |
| [**🆕 herdr-agent-smart-rename**](https://github.com/malone-c/herdr-agent-smart-rename)<br><sub>malone-c</sub> | Names each herdr agent session from what it is actually doing | `python` | 0 | 2026-08-14 |
| [**🆕 herdr-unrecoverable**](https://github.com/neilwashere/herdr-unrecoverable)<br><sub>neilwashere</sub> | Herdr watchdog that recovers Pi coding-agent sessions from terminal provider errors | `pi-coding-agent` `javascript` | 0 | 2026-08-14 |
| [**🆕 herdr-worktree**](https://github.com/tjg184/herdr-worktree)<br><sub>tjg184</sub> | Herdr worktree plugin that works with worktrunk and native worktrees | `rust` | 0 | 2026-08-13 |
| [**🆕 herdr-cmux-cwd-sync**](https://github.com/WerrySs/herdr-cmux-cwd-sync)<br><sub>WerrySs</sub> | Non-invasive cmux file explorer sync for the focused HerdR pane | `cmux` `macos` `python` | 0 | 2026-08-14 |
| [**🆕 herdr-corral**](https://github.com/bfreed/herdr-corral)<br><sub>bfreed</sub> | Herdr内でGit worktreeをまとめて管理——envファイル、依存関係、エージェント/シェル/サーバー用のタブ、マージしても安全なクリーンアップに対応。Herdr向けのworkmux代替 | `git-worktree` `workmux` `python` | 1 | 2026-08-14 |
| [**🆕 herdr-openclaw**](https://github.com/gejiliang/herdr-openclaw)<br><sub>gejiliang</sub> | herdrプラグイン：OpenClawのTUIペインを、herdrの正式なエージェントとして管理する | `openclaw` `terminal` `javascript` | 1 | 2026-08-13 |
| [**🆕 herdr-yazi-explorer**](https://github.com/pjs-0457/herdr-yazi-explorer)<br><sub>pjs-0457</sub> | 呼び出したワークスペース内のherdrタブ/スプリットでYaziを開く（🗂 yaziというラベル付き）。終了すると自動的に再起動する | `yazi` `shell` | 1 | 2026-08-13 |
| [**🆕 herdr-automations**](https://github.com/ram4-dev/herdr-automations)<br><sub>ram4-dev</sub> | Herdr向けの宣言的なcron・インターバル・イベント自動化 | `automation` `bun` `typescript` | 1 | 2026-08-13 |
| [**🆕 herdr-sidepulse**](https://github.com/third774/herdr-sidepulse)<br><sub>third774</sub> | _(説明なし)_ | `javascript` | 1 | 2026-08-14 |
| [**🆕 herdr-claude-tab-title**](https://github.com/tmn73/herdr-claude-tab-title)<br><sub>tmn73</sub> | 各Claude Codeのセッションタイトルを、対応するHerdrのタブに反映する | `claude-code` `tabs` `terminal` `typescript` | 1 | 2026-08-13 |
| [**🆕 herdr-plugin-manager**](https://github.com/a-curious-coder/herdr-plugin-manager)<br><sub>a-curious-coder</sub> | 1つのポップアップペインからherdrプラグインを管理・発見する——インストール/アンインストール/更新、アクションの実行やバインド、公開レジストリの閲覧ができる | `shell` | 0 | 2026-08-13 |
| [**🆕 herdr-docker**](https://github.com/abcxff/herdr-docker)<br><sub>abcxff</sub> | herdrでエージェントを追跡するのと同じように、dockerのビルドも追跡する | `docker` `javascript` | 0 | 2026-08-12 |
| [**🆕 herdr-warp**](https://github.com/cdpath/herdr-warp)<br><sub>cdpath</sub> | Herdrのペイン内で対話型のWarp Agent CLI（warp）を操作するHerdrプラグイン：open/send/status/wait/read/approve/deny/new/stop/exitに対応し、画面をスクレイピングしてidle/working/blockedの状態を判定する | `shell` | 0 | 2026-08-13 |
| [**🆕 herdr-vaultr**](https://github.com/connerohnesorge/herdr-vaultr)<br><sub>connerohnesorge</sub> | vaultrの公式herdrプラグイン——キャプチャしたエージェントセッションを、実行元のペインからコピー・表示・フォーク・検索できる | `vaultr` `shell` | 0 | 2026-08-13 |
| [**🆕 herdr-hunk**](https://github.com/goofansu/herdr-hunk)<br><sub>goofansu</sub> | Hunk review actions | `python` | 0 | 2026-08-19 |
| [**🆕 herdr-follow-cwd**](https://github.com/hasuwini77/herdr-follow-cwd)<br><sub>hasuwini77</sub> | herdrプラグイン：ワークスペースのラベルが、ペインが実際にいるディレクトリに追従する | `javascript` | 0 | 2026-08-13 |
| [**🆕 herdr-suffix-agent-filter**](https://github.com/kazimshah39/herdr-suffix-agent-filter)<br><sub>kazimshah39</sub> | Herdrの Agentsサイドバーを、選択したSpaceと同じ名前サフィックスを持つSpaceのエージェントだけに絞り込む | `coding-agents` `developer-tools` `terminal` `javascript` | 0 | 2026-08-13 |
| [**🆕 strays**](https://github.com/m1sk9/strays)<br><sub>m1sk9</sub> | A TUI for Centralized Management of Claude Code | `claude-code` `llm` `tui` `rust` | 0 | 2026-08-16 |
| [**🆕 quickTUI**](https://github.com/marcjfj-vmlyr/quickTUI)<br><sub>marcjfj-vmlyr</sub> | OpenTUI上で動く、組み合わせるだけで素早くターミナルUIを作れるプリミティブ集。コーディングエージェントに/quicktuiスキルを与えるHerdrプラグインとして提供される | `bun` `opentui` `terminal` `tui` `typescript` | 0 | 2026-08-13 |
| [**🆕 herdr-git-pull**](https://github.com/nimrc/herdr-git-pull)<br><sub>nimrc</sub> | _(説明なし)_ | `python` | 0 | 2026-08-13 |
| [**🆕 herdr-layout**](https://github.com/noviadi/herdr-layout)<br><sub>noviadi</sub> | Herdrのペインレイアウトを保存して再現する。Herdrターミナルマルチプレクサ向けのコンパニオンプラグイン（tmux-resurrect風） | `cli` `terminal` `tmux-resurrect` `shell` | 0 | 2026-08-13 |
| [**🆕 herdr-notify-center**](https://github.com/ram4-dev/herdr-notify-center)<br><sub>ram4-dev</sub> | サーバー全体のエージェント通知を、永続化されたポップアップ受信箱でHerdrに提供する | `notifications` `typescript` | 0 | 2026-08-14 |
| [**🆕 herdr-confirm-close**](https://github.com/tajdien/herdr-confirm-close)<br><sub>tajdien</sub> | herdrプラグイン：ペインやタブを閉じる前に確認ポップアップを出す | `shell` | 0 | 2026-08-13 |

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-notify"></a>

## 通知・アラート

> エージェントが完了した / 入力待ちで止まったのを、席を外していても知りたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-focus-notify**](https://github.com/yankewei/herdr-focus-notify)<br><sub>yankewei</sub> | Herdrのエージェント向けの、クリック可能なmacOS通知。エージェントがブロックまたは完了するとネイティブのトースト通知を送り、クリックするとターミナルを最前面に出して該当のHerdrペインにフォーカスする | `alerter` `macos` `notifications` `productivity` `rust` | 14 | 🔄 2026-08-18 |
| [**herdr-pings**](https://github.com/joelhooks/herdr-pings)<br><sub>joelhooks</sub> | herdrのペインで動くAIエージェント向けの、ターン単位のウェイクイベント通知——piエクステンション、waitコマンド、クラッシュブリッジ、ワーカー用のDiscworld風コールサイン付き | `ai-agents` `pi` `typescript` | 9 | 🔄 2026-08-09 |
| [**herdr-terminal-notifier**](https://github.com/dot/herdr-terminal-notifier)<br><sub>dot</sub> | terminal-notifier経由で、herdrエージェントの状態変化をカスタマイズ可能なmacOS通知として送る | `macos` `terminal-notifier` `shell` | 6 | 2026-07-14 |
| [**herdr-ntfy**](https://github.com/horn553/herdr-ntfy)<br><sub>horn553</sub> | 依存関係最小限（jq・curl・sh）——Herdrのエージェントが完了またはブロックされたときにntfy通知を送る | `shell` | 6 | 2026-08-01 |
| [**herdr-hail**](https://github.com/natori-hrj/herdr-hail)<br><sub>natori-hrj</sub> | herdr向けのSlack/Discord双方向ブリッジ——エージェントがブロックされたら通知が来て、返信/タップでブロックを解除できる。トンネル不要 | `discord` `slack` `typescript` | 6 | 2026-07-19 |
| [**herdr-ntfy-notify**](https://github.com/zom-2018/herdr-ntfy-notify)<br><sub>zom-2018</sub> | Herdrのターミナルエージェント向けの、リアルタイムなntfyプッシュ通知 | `agent` `ntfy` `push-notifications` `tui` `javascript` | 6 | 2026-06-23 |
| [**herdr-telegram-plugin**](https://github.com/mvallebr/herdr-telegram-plugin)<br><sub>mvallebr</sub> | herdr向けのTelegramボットコンパニオン——Telegramのフォーラムトピック経由で任意のエージェントを遠隔操作。処理経路にLLMは介在しない | `typescript` | 4 | 2026-08-04 |
| [**herdr-notify-windows**](https://github.com/aclima01/herdr-notify-windows)<br><sub>aclima01</sub> | herdrのエージェント向けのWindows 11トースト通知（ターン完了/入力待ち） | `powershell` | 3 | 2026-07-23 |
| [**herdr-telegram-bridge**](https://github.com/cokekitten/herdr-telegram-bridge)<br><sub>cokekitten</sub> | herdrのエージェントが完了またはブロックされたらTelegramにプッシュ通知が来る——返信すればテキストやファイルをそのままエージェントに送り返せる。サーバー・トンネル・アプリ不要 | `ai-agents` `chatops` `claude-code` `developer-tools` `notifications` | 3 | 🔄 2026-08-06 |
| [**herdr-announcer**](https://github.com/nhclink16/herdr-announcer)<br><sub>nhclink16</sub> | Herdrプラグイン：エージェントが完了または入力待ちになったら、LLMによる一文要約を音声で読み上げる——ローカルTTS、ElevenLabs、任意のカスタムコマンドに対応 | `tts` `python` | 3 | 🔄 2026-08-18 |
| [**herdr-telegram-attention**](https://github.com/blockshiftnetwork/herdr-telegram-attention)<br><sub>blockshiftnetwork</sub> | Herdrのエージェントが対応を必要としているときに、多言語対応のTelegramアラートを送る | `python` | 2 | 🔄 2026-08-10 |
| [**🆕 herdr-discord-presence**](https://github.com/revanp/herdr-discord-presence)<br><sub>revanp</sub> | Herdr plugin: show your Herdr session and agent status as Discord Rich Presence | `typescript` | 2 | 🔄 2026-08-14 |
| [**herdr-guard**](https://github.com/StructuPath/herdr-guard)<br><sub>StructuPath</sub> | Herdr向けのエージェント横断コマンドポリシー：危険なシェルコマンドを監査・警告・中断する | `ai-agents` `command-policy` `security` `terminal` `javascript` | 2 | 2026-07-28 |
| [**🆕 herdr-agent-notify**](https://github.com/A1exthegreat/herdr-agent-notify)<br><sub>A1exthegreat</sub> | Herdr plugin: desktop notifications when agents finish working, need confirmation, or go idle | `javascript` | 1 | 🔄 2026-08-15 |
| [**🆕 herdr-prayer-times**](https://github.com/bayoudhi/herdr-prayer-times)<br><sub>bayoudhi</sub> | Next Islamic prayer and countdown in the Herdr sidebar, with a timetable popup and notifications | `rust` | 1 | 🔄 2026-08-13 |
| [**session-sounds**](https://github.com/ChrisPachulski/session-sounds)<br><sub>ChrisPachulski</sub> | macOSとLinux向けに、Herdrのエージェントごとに異なる完了音・注意喚起音を鳴らす | `coding-agents` `notifications` `rust` | 1 | 2026-07-19 |
| [**agent-webhook-notify**](https://github.com/happyeric77/agent-webhook-notify)<br><sub>happyeric77</sub> | Herdrのエージェントが完了またはブロックされたときに、Webhook通知を送る | `javascript` | 1 | 🔄 2026-08-12 |
| [**herdr-notify-wsl**](https://github.com/saeedrahimi/herdr-notify-wsl)<br><sub>saeedrahimi</sub> | WSL内で動くherdrエージェント向けのWindows 11トースト通知——aclima01/herdr-notify-windowsをベースにしている | `powershell` | 1 | 2026-07-23 |
| [**herdr-prompt-reply**](https://github.com/cedrus-8864/herdr-prompt-reply)<br><sub>cedrus-8864</sub> | herdrのエージェントの権限確認プロンプトに、macOS通知から直接答えられる——実際に押せる回答ボタン、単一のSwiftバイナリ、バックグラウンドで待機するものは何もない | `ai-agents` `claude-code` `macos` `macos-notifications` `notifications` | 0 | 🔄 2026-08-19 |
| [**herdr-slack-notify**](https://github.com/juninaba/herdr-slack-notify)<br><sub>juninaba</sub> | Herdrのエージェントが完了またはブロックされたら、Slack通知を送る | `javascript` | 0 | 2026-07-07 |
| [**drover-notify**](https://github.com/keinstn/drover-notify)<br><sub>keinstn</sub> | エージェントがブロックされたときにDroverのプッシュ通知を送るHerdrプラグイン | `javascript` | 0 | 2026-08-01 |
| [**herdr-telegram-slack-bridge**](https://github.com/lsisoft/herdr-telegram-slack-bridge)<br><sub>lsisoft</sub> | Herdrのエージェントセッション向けの、TelegramとSlackボットの双方向ブリッジ——ブロックされたエージェントの通知やチャットの返信を、Herdrやtmuxのペインに転送する | `ai-agents` `slack-bot` `telegram-bot` `tmux` `python` | 0 | 2026-07-28 |
| [**herdr-plugin-telegram-notify**](https://github.com/OiAnthony/herdr-plugin-telegram-notify)<br><sub>OiAnthony</sub> | エージェントが完了またはブロックされたときにTelegram通知を送る、単体で動作するHerdrプラグイン | `javascript` | 0 | 2026-07-16 |
| [**herdr-apple-music-plugin**](https://github.com/perlporter/herdr-apple-music-plugin)<br><sub>perlporter</sub> | Apple Music（macOS）の再生曲が変わったときに、herdrでトースト通知を表示する | `shell` | 0 | 2026-07-28 |
| [**🆕 herdr-notify-center**](https://github.com/ram4-dev/herdr-notify-center)<br><sub>ram4-dev</sub> | サーバー全体のエージェント通知を、永続化されたポップアップ受信箱でHerdrに提供する | `notifications` `typescript` | 0 | 🔄 2026-08-14 |
| [**herdr-cc-mac-notify**](https://github.com/y-hirakaw/herdr-cc-mac-notify)<br><sub>y-hirakaw</sub> | Claude Code向けのmacOS通知——「完了」だけでなく、エージェントの実際の最後のメッセージを表示する | `claude-code` `macos` `notifications` `python` | 0 | 2026-07-17 |

<details><summary>この目的にも関係するもの</summary>

- [donghaolicd/herdr-teams-notify](https://github.com/donghaolicd/herdr-teams-notify) — Herdr plugin for bounded Microsoft Teams agent lifecycle notifications

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-remote"></a>

## スマホ・リモート操作

> 外出先やスマホからエージェントを監視して、承認だけ返したい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**collie**](https://github.com/AltanS/collie)<br><sub>AltanS</sub> | 外出先からherdrを管理できるPWA。Tailnet経由でアクセス可能、プッシュ通知やクイックアクションなど | `agent-orchestration` `ai` `ai-agents` `ai-coding` `ai-tools` | 457 | 🔄 2026-08-19 |
| [**herdr-remote**](https://github.com/dcolinmorgan/herdr-remote)<br><sub>dcolinmorgan</sub> | メニューバー・スマホ・Telegramからherdrのエージェントを監視・操作。ローカル設定不要、リモート接続用の無料トンネル付きでTailscaleも不要 | `macos` `mobile` `python` | 268 | 🔄 2026-08-17 |
| [**herdr-mobile-relay**](https://github.com/0cv/herdr-mobile-relay)<br><sub>0cv</sub> | スマホからHerdrのエージェントを遠隔で承認・監視できる、Android/iOS向けのモバイルWebアプリ。プッシュ通知・QRコードでの設定・複数PCへの中継に対応 | `android` `approvals` `cloudflare` `ios` `mobile` | 93 | 🔄 2026-08-18 |
| [**herdr-watch**](https://github.com/Unayung/herdr-watch)<br><sub>Unayung</sub> | herdrのエージェント状態をApple Watchで確認できる | `javascript` | 23 | 🔄 2026-08-14 |
| [**herdr-plugin-mobile-relay**](https://github.com/benkraus/herdr-plugin-mobile-relay)<br><sub>benkraus</sub> | _(説明なし)_ | `typescript` | 10 | 🔄 2026-08-12 |
| [**herdr-push**](https://github.com/dcolinmorgan/herdr-push)<br><sub>dcolinmorgan</sub> | herdrプラグイン：依存なしでイベントをherdr-remoteにpushし、モバイルからの監視とワンタップ承認を可能にする | `shell` | 9 | 2026-07-09 |
| [**merino**](https://github.com/LoneExile/merino)<br><sub>LoneExile</sub> | Merino🐑——Herdrエージェント向けのリモートトンネルダッシュボード | `go` `macos` `menubar` `react` `wails` | 6 | 🔄 2026-08-20 |
| [**herdr-tether**](https://github.com/moneycaringcoder/herdr-tether)<br><sub>moneycaringcoder</sub> | Herdrのビューを閉じた後も、ローカル・リモートのターミナル処理を実行し続けさせる | `remote-development` `rust` `ssh` `terminal` `tmux` | 6 | 🔄 2026-08-16 |
| [**muqun-gateway**](https://github.com/osuki-dev/muqun-gateway)<br><sub>osuki-dev</sub> | Muqunが、あなた自身のコンピュータ上のターミナルにアクセスできるようにするプログラム。あなたのマシン上で動作し、tmuxまたはHerdrと通信し、あなたのスマホに直接応答する——アカウントも、間に入る当方のサーバーも存在しない | `rust` | 5 | 🔄 2026-08-19 |
| [**🆕 herdr-connect**](https://github.com/Tomyail/herdr-connect)<br><sub>Tomyail</sub> | Open-source LAN companion app for discovering and connecting to Herdr installations | `agent` `mobile-app` `react-native` `typescript` | 5 | 🔄 2026-08-19 |
| [**herdr-mobile**](https://github.com/bsorescu/herdr-mobile)<br><sub>bsorescu</sub> | SSH経由でHerdrのコーディングエージェントを操作できる、スマホ向けTUI | `mobile` `ssh` `textual` `tui` `python` | 3 | 🔄 2026-08-17 |
| [**herdr-call**](https://github.com/eliasstravik/herdr-call)<br><sub>eliasstravik</sub> | Herdr向けの音声操作 | `elevenlabs` `tailscale` `voice` `typescript` | 3 | 🔄 2026-08-07 |
| [**herdr-aws-ssm**](https://github.com/maayanyosef/herdr-aws-ssm)<br><sub>maayanyosef</sub> | EC2インスタンスを選択し、herdrの--remoteセッションでAWS SSM経由接続する——踏み台サーバーやパブリックIPは不要 | `aws-ssm` `terminal` `shell` | 3 | 2026-07-01 |
| [**herdr-farm**](https://github.com/mejiasd3v/herdr-farm)<br><sub>mejiasd3v</sub> | Herdrプラグイン：ワークスペースとエージェントを家畜として可視化する3D農場（three.js製Webアプリ） | `threejs` `javascript` | 3 | 2026-07-28 |
| [**herdr-devup**](https://github.com/alon-z/herdr-devup)<br><sub>alon-z</sub> | Herdrプラグイン：.herdr/dev.tomlからプロジェクトごとの開発用レイアウトを構築し、トンネルURLを環境変数に同期する | `typescript` | 2 | 2026-06-22 |
| [**herdr-whistle**](https://github.com/amurru/herdr-whistle)<br><sub>amurru</sub> | リモートでのエージェント管理を行うHerdrプラグイン | `golang` `telegrambot` `go` | 2 | 🔄 2026-08-06 |
| [**herdr-web**](https://github.com/eyalev/herdr-web)<br><sub>eyalev</sub> | herdrのエージェントマルチプレクサ向けの、モバイルファーストなWeb UI——スマホからコーディングエージェントを操作できる | `claude-code` `mobile` `pwa` `terminal` `javascript` | 2 | 2026-07-29 |
| [**herdr-telegram-gate**](https://github.com/hkdom/herdr-telegram-gate)<br><sub>hkdom</sub> | herdrのAIエージェント群向けの、Telegram承認インボックス＋リスク階層別の自動承認——ブロックされたエージェントは承認/拒否ボタン付きのTelegramカードとして表示される（依存ライブラリなしのNode.js） | `approval-gate` `telegram` `javascript` | 2 | 🔄 2026-08-06 |
| [**herdr-remotedownloder**](https://github.com/kosuketut/herdr-remotedownloder)<br><sub>kosuketut</sub> | リモートのHerdrペインから、接続元のMacへファイルをダウンロードする | `rust` | 2 | 2026-08-01 |
| [**herdr-phone**](https://github.com/matheus3301/herdr-phone)<br><sub>matheus3301</sub> | Cloudflare TunnelとAccessを使った、Herdr向けのモバイルリモートコンソール | `cloudflare-tunnel` `coding-agents` `developer-tools` `golang` `mobile` | 2 | 🔄 2026-08-14 |
| [**herdr-portfwd**](https://github.com/miko-misa/herdr-portfwd)<br><sub>miko-misa</sub> | リモートマシン上のコーディングエージェント向けの自動SSHポートフォワーディング——エージェントが出力したlocalhost URLをCtrl+クリックすると、同じポートで手元のマシンにページが開く。Herdrプラグイン | `ai-agents` `claude-code` `cli` `coding-agents` `developer-tools` | 1 | 🔄 2026-08-11 |
| [**herdr-web-tui**](https://github.com/tigorlazuardi/herdr-web-tui)<br><sub>tigorlazuardi</sub> | デーモン主体のHerdr向けブラウザ/PWAフロントエンド——オプションのプラグインランチャー付き | `go` | 1 | 🔄 2026-08-18 |
| [**🆕 setnet**](https://github.com/chano-gpt/setnet)<br><sub>chano-gpt</sub> | Herd multi-harness coding agents from your phone — a Herdr plugin | `typescript` | 0 | 🔄 2026-08-15 |
| [**🆕 herdrchat**](https://github.com/cobanov/herdrchat)<br><sub>cobanov</sub> | HerdrChat — control your herdr coding agents from your phone (iOS + Android) | `herdr-client` `herdr-integration` `herdr-mobile` `typescript` | 0 | 🔄 2026-08-19 |
| [**🆕 herdr-slack**](https://github.com/egemenyildiz/herdr-slack)<br><sub>egemenyildiz</sub> | Drive your local herdr agents from Slack — browse, prompt, and launch from your phone. No tunnel. | `slack` `typescript` | 0 | 🔄 2026-08-19 |
| [**herdr-approval-gate**](https://github.com/Javamomma/herdr-approval-gate)<br><sub>Javamomma</sub> | herdr内のエージェントの操作に対する、人間による承認ゲート——専用ペインでタスクを実行し、その記録を判定チェックし、人間が「APPROVE <イニシャル>」と入力するまでブロックする | `shell` | 0 | 2026-07-15 |
| [**herdr-wechat-plugin**](https://github.com/LuYanFCP/herdr-wechat-plugin)<br><sub>LuYanFCP</sub> | WeChatによる遠隔操作を可能にするHerdrプラグイン | `rust` | 0 | 2026-07-17 |
| [**herdr-agents-bridge**](https://github.com/maedana/herdr-agents-bridge)<br><sub>maedana</sub> | ローカルのモバイル向けWeb UI経由で、スマホからコーディングエージェントを監視・操作する——QRコードをスキャンして接続 | `rust` | 0 | 2026-07-22 |
| [**herdview**](https://github.com/Orchard-Robotics/herdview)<br><sub>Orchard-Robotics</sub> | 自分の「herd」をWebから見る | `html` | 0 | 2026-07-17 |
| [**vscode-devcontainers-herdr**](https://github.com/scott-the-programmer/vscode-devcontainers-herdr)<br><sub>scott-the-programmer</sub> | devコンテナ内で動くエージェント向けのHerdrリレー | `container` `devcontainer` `rust` | 0 | 🔄 2026-08-20 |

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-agents"></a>

## エージェント統括・並列実行

> 複数の AI エージェントをまとめて起動・分担・管理したい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**🆕 oh-my-opencode-slim**](https://github.com/alvinunreal/oh-my-opencode-slim)<br><sub>alvinunreal</sub> | Lean, fine tuned Opencode multi agent suite · Mix any models · Auto delegate tasks | `agentic-ai` `antigravity` `cerebras` `oh-my-opencode` `opencode` | 8252 | 🔄 2026-08-19 |
| [**agentbox**](https://github.com/madarco/agentbox)<br><sub>madarco</sub> | コマンド一発で、サンドボックス化された複数のVM上にエージェントを並列実行（PCでもクラウドでも） | `claude` `claude-code` `cli` `cmux` `codex` | 367 | 2026-08-03 |
| [**pi-extensible-workflows**](https://github.com/vekexasia/pi-extensible-workflows)<br><sub>vekexasia</sub> | Pi向けの、決定論的なマルチエージェントワークフローオーケストレーション | `pi` `workflow` `workflows` `typescript` | 182 | 🔄 2026-08-19 |
| [**🆕 pi-workflows**](https://github.com/osolmaz/pi-workflows)<br><sub>osolmaz</sub> | Workflow engine, JSON control-flow tool, and live terminal viewer for the pi coding agent | `typescript` | 51 | 🔄 2026-08-19 |
| [**herdr-board**](https://github.com/nelsonPires5/herdr-board)<br><sub>nelsonPires5</sub> | herdr向けのカンバンボード——カードはそのままプロンプトになり、見えているペイン上のAIエージェントに割り振られる | `board` `kanban` `kanban-board` `tui` `rust` | 45 | 🔄 2026-08-19 |
| [**agentbox-herdr-plugin**](https://github.com/madarco/agentbox-herdr-plugin)<br><sub>madarco</sub> | コマンド一発で、サンドボックス化された複数のVM上にエージェントを並列実行（PCでもクラウドでも） | `claude-code` `codex-cli` `opencode` `sandbox` `shell` | 26 | 2026-06-24 |
| [**herdmates**](https://github.com/caioniehues/herdmates)<br><sub>caioniehues</sub> | herdrネイティブのClaude Codeエージェントチーム——teammuxシム、ミッションコントロールボード、フォーカスペイン | `agent-teams` `claude-code` `rust` `tui` | 20 | 2026-07-17 |
| [**🆕 herdr-dagr**](https://github.com/aemrebarut/herdr-dagr)<br><sub>aemrebarut</sub> | Your agent swarm as a live DAG: an orchestration graph with attempts, review gates, and evidence, in a herdr split pane. | `agents` `dag` `multi-agent` `orchestration` `rust` | 18 | 🔄 2026-08-19 |
| [**pi-herd**](https://github.com/ribbons-digital/pi-herd)<br><sub>ribbons-digital</sub> | Herdrのペインとgit worktreeを使って、Piのセッションを可視化しながらオーケストレーションする | `typescript` | 15 | 2026-07-06 |
| [**🆕 herdr-file-annotator**](https://github.com/JonasBaeumer/herdr-file-annotator)<br><sub>JonasBaeumer</sub> | A plugin for herder to maximize agentic development without losing touch with the actual codebase | `rust` | 12 | 🔄 2026-08-19 |
| [**herdr-agent-handoff**](https://github.com/sanirudh17/herdr-agent-handoff)<br><sub>sanirudh17</sub> | 進行中のエージェントセッションを、別のインストール済みコーディングエージェントの新規セッションに引き渡すHerdrプラグイン。セッション全体をプロンプト内にそのまま渡すため、要約や省略された履歴、追加の指示を書く必要がない | `agent-handoff` `claude-code` `codex` `coding-agents` `developer-tools` | 10 | 🔄 2026-08-14 |
| [**herdr-browser**](https://github.com/StructuPath/herdr-browser)<br><sub>StructuPath</sub> | Herdr向けの操作可能なエージェントブラウザペイン——ライブストリーミング、実際の操作、アダプティブレンダリング、コンソール/ページエラー表示、録画、localhostルーティングに対応 | `terminal` `javascript` | 10 | 🔄 2026-08-06 |
| [**vibetty**](https://github.com/second-state/vibetty)<br><sub>second-state</sub> | MQTT経由でAIエージェントのターミナルをスマートデバイス（vibekeys、vibewatchなど）にライブ共有する。Herdrプラグインとしても利用可能 | `claude-code` `codex` `vibecoding` `rust` | 9 | 🔄 2026-08-17 |
| [**herdr-vercel-sandbox-plugin**](https://github.com/vercel-labs/herdr-vercel-sandbox-plugin)<br><sub>vercel-labs</sub> | Herdrから、ターミナルベースのコーディングエージェントを隔離されたVercel Sandbox上で実行する | `javascript` | 9 | 🔄 2026-08-09 |
| [**bermuda**](https://github.com/bon5co/bermuda)<br><sub>bon5co</sub> | Orchestration under Claude Code on herdr: flows an agent cannot skip, jobs on a clock, threads with claims, and a forum agents search later | `agents` `golang` `tui` `go` | 7 | 🔄 2026-08-19 |
| [**herdr-helpr**](https://github.com/sohanemon/herdr-helpr)<br><sub>sohanemon</sub> | プロンプトで操作する、herdr向けのワークスペース・ペイン管理 | `ai-agents` `bun` `cli` `developer-tools` `ink` | 7 | 2026-07-16 |
| [**herdr-catchup**](https://github.com/wilbeibi/herdr-catchup)<br><sub>wilbeibi</sub> | herdr向けのエージェント間コーディングセッション引き渡し：稼働中のペインから、Claude Code・Codex・Cursor・Cline・OpenCodeのセッションを要約・フォーク・他のエージェントへの引き渡しができる | `ai-agents` `claude-code` `codex` `coding-agents` `context-handoff` | 6 | 2026-07-27 |
| [**herdr-triage**](https://github.com/natori-hrj/herdr-triage)<br><sub>natori-hrj</sub> | herdr向けの注意度トリアージ——あなたを最も必要としているエージェントを上位に並べる。長時間ブロックされたエージェントほど上に来る | `ai-agents` `triage` `rust` | 5 | 2026-07-23 |
| [**herdr-swarm**](https://github.com/StructuPath/herdr-swarm)<br><sub>StructuPath</sub> | 1つのリポジトリで複数のコーディングエージェントを安全に並列実行：エージェントごとのworktree展開、変更のリアルタイム可視化、レビュー優先の成果回収をHerdr向けに提供 | `terminal` `javascript` | 5 | 2026-07-28 |
| [**herdr-insight**](https://github.com/0x5c0f/herdr-insight)<br><sub>0x5c0f</sub> | エージェントの状態タイムラインパネル | `rust` | 4 | 2026-06-23 |
| [**herdr-agent-messenger**](https://github.com/aashishd/herdr-agent-messenger)<br><sub>aashishd</sub> | 稼働中のHerdrペイン間で、AIエージェント同士が要点を絞った自己完結型のメッセージをやり取りできるようにする——1つのエージェントが、全コンテキストを共有せずに別のエージェントと作業を調整できる | `python` | 4 | 2026-08-02 |
| [**shepherdr**](https://github.com/afogel/shepherdr)<br><sub>afogel</sub> | 委任したコーディングエージェントを、監視・再開・引き取りができる可視化されたherdrのペインに追い込むherdrプラグイン | `ai-agents` `claude-code` `codex` `cursor` `rust` | 4 | 2026-07-24 |
| [**herdr-espresso**](https://github.com/Hanyang-Li/herdr-espresso)<br><sub>Hanyang-Li</sub> | エージェントが動作中はMacBookを、蓋を閉じても眠らせない | `rust` | 4 | 2026-07-25 |
| [**herdr-space-scoped-agents**](https://github.com/ShankyJS/herdr-space-scoped-agents)<br><sub>ShankyJS</sub> | エージェントパネルを、フォーカス中のスペースに限定して表示するherdrプラグイン | `coding-agents` `terminal` `go` | 4 | 2026-07-23 |
| [**herdr-theos-settler**](https://github.com/calebcauthon/herdr-theos-settler)<br><sub>calebcauthon</sub> | 完了したHerdrのエージェントタブやワークスペースを、作業中のものより下に沈めて視界から外す。Theoのアイデア | `rust` | 3 | 2026-07-23 |
| [**herdr-gamepad**](https://github.com/htlin222/herdr-gamepad)<br><sub>htlin222</sub> | ゲームコントローラーでHerdrを操作する。ソファに座ったままAIエージェントを見回り、ペインを分割し、ワークスペースを切り替えられる——どんなゲームパッドでも60秒で自分好みに割り当て可能 | `ai-agents` `gamepad` `macos` `swift` `terminal-multiplexer` | 3 | 🔄 2026-08-08 |
| [**herdr-walkietalkie**](https://github.com/jeffory/herdr-walkietalkie)<br><sub>jeffory</sub> | herdrプラグイン：トークン効率の良いエージェント間委任（wt）——オーケストレーター役のエージェントが、Claude/OpenCode/Antigravityのワーカーをタブやworktreeに立ち上げる | `shell` | 3 | 🔄 2026-08-12 |
| [**herdr-blaxel-sandbox-plugin**](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin)<br><sub>blaxel-ai</sub> | Herdrから、永続化されたBlaxel Sandbox上でコーディングエージェントを実行する | `blaxel` `claude-code` `codex` `coding-agents` `opencode` | 2 | 🔄 2026-08-18 |
| [**herdr-birdseye**](https://github.com/calebcauthon/herdr-birdseye)<br><sub>calebcauthon</sub> | herdr内のエージェントを鳥瞰図で見る | `rust` | 2 | 2026-07-24 |
| [**herdr-orchestrate**](https://github.com/darjss/herdr-orchestrate)<br><sub>darjss</sub> | Pi向けのネイティブなオーケストレーション機能を、可視化されたHerdrのワーカーセッションで提供——実行状況ボード、永続的なプロンプト/レポート/状態、独立したgit worktree、明示的なモデルルーティングに対応 | `pi-package` `typescript` | 2 | 2026-07-13 |
| [**herdr-devcontainer**](https://github.com/gambtho/herdr-devcontainer)<br><sub>gambtho</sub> | 公式のDev Containers CLI経由で、リポジトリのDev Container内にシェルやコーディングエージェントを開くHerdrプラグイン | `coding-agents` `containers` `devcontainers` `developer-tools` `development-environment` | 2 | 🔄 2026-08-13 |
| [**herdr-shame-report**](https://github.com/JYasha11/herdr-shame-report)<br><sub>JYasha11</sub> | AIエージェントをどれだけ待たせたかを、ずっと記録し続ける台帳。羊は忘れない | `javascript` | 2 | 2026-07-10 |
| [**herdr-agents-status**](https://github.com/maedana/herdr-agents-status)<br><sub>maedana</sub> | Herdrのエージェントの状態を表示する、常に最前面の透明オーバーレイ——claudeyeの精神的後継で、tmuxではなくHerdr向けに作られた | `rust` | 2 | 🔄 2026-08-15 |
| [**🆕 chatter**](https://github.com/marcvermeeren/chatter)<br><sub>marcvermeeren</sub> | Chatter is an experiment in cross-harness agent collaboration: a shared group chat and context layer for agents working on the same Git repository in Herdr. | `agent-collaboration` `agentic-ai` `agentic-workflow` `ai-agents` `group-chat` | 2 | 🔄 2026-08-18 |
| [**herdr-approve-all**](https://github.com/RenKoya1/herdr-approve-all)<br><sub>RenKoya1</sub> | herdrプラグイン：ブロックされている全エージェントを一括承認（1キーで、保留中の許可プロンプトすべてに応答） | `shell` | 2 | 🔄 2026-08-16 |
| [**herdr-agents-history**](https://github.com/speardragon/herdr-agents-history)<br><sub>speardragon</sub> | AIコーディングエージェントが実際に何をしているかを見る——すべてのエージェント（Claude CodeとCodex）のツール呼び出しをリアルタイムに流し続ける、キーボード操作のherdr TUI | `ai-agents` `claude-code` `codex` `tui` `typescript` | 2 | 2026-07-19 |
| [**herdr-wakeup**](https://github.com/usrivastava92/herdr-wakeup)<br><sub>usrivastava92</sub> | Herdrが管理するエージェントが作業中の間、macOSまたはLinuxをスリープさせないHerdrプラグイン | `power-management` `sleep-prevention` `wakeup` `rust` | 2 | 2026-07-17 |
| [**herdr-agent-timer**](https://github.com/Yemeni/herdr-agent-timer)<br><sub>Yemeni</sub> | 各エージェントのステータスラベルと経過時間を交互に表示するHerdrプラグイン | `shell` | 2 | 🔄 2026-08-14 |
| [**🆕 herdr-pouch**](https://github.com/AltanS/herdr-pouch)<br><sub>AltanS</sub> | Herdr plugin: stash prompts for an agent ahead of time and insert them when it's ready | `typescript` | 1 | 🔄 2026-08-19 |
| [**herdr-pi-reloader**](https://github.com/anrunt/herdr-pi-reloader)<br><sub>anrunt</sub> | Herdrのオーバーレイ TUIから、アイドル状態のPiエージェントセッションをリロードまたは再起動する | `rust` | 1 | 2026-07-18 |
| [**herdr-loop**](https://github.com/cyperx84/herdr-loop)<br><sub>cyperx84</sub> | herdr向けの宣言的でイベント駆動なループ＋グラフオーケストレーション——Claude Code・Codex・opencode・piをまとめて動かし、作業が収束するまで実行する | `ai-agents` `golang` `orchestration` `go` | 1 | 🔄 2026-08-12 |
| [**herdr-pane-topic-sync**](https://github.com/danbuhler/herdr-pane-topic-sync)<br><sub>danbuhler</sub> | herdrプラグイン：ペインとタブの名前を「1」「2」「3」ではなく、各エージェント（Claude Code、Codexなど）のリアルタイムのトピックから自動で付ける | `ai-agents` `claude-code` `terminal` `tmux-alternative` `javascript` | 1 | 2026-08-04 |
| [**herdr-mise**](https://github.com/funsaized/herdr-mise)<br><sub>funsaized</sub> | プロンプトではなく「一手」を回す🧑‍🍳 herdr内のエージェント向けビジュアライザー | `agent` `cli-tool` `macos` `mosh` `rust` | 1 | 🔄 2026-08-17 |
| [**🆕 herdr-openclaw**](https://github.com/gejiliang/herdr-openclaw)<br><sub>gejiliang</sub> | herdrプラグイン：OpenClawのTUIペインを、herdrの正式なエージェントとして管理する | `openclaw` `terminal` `javascript` | 1 | 🔄 2026-08-13 |
| [**LunaCrab**](https://github.com/GranamyrBR/LunaCrab)<br><sub>GranamyrBR</sub> | 別プロジェクト用に予約済み | `agents` `developer-tools` `multi-agent` `observability` `rust` | 1 | 🔄 2026-08-10 |
| [**herdr-amphetamine-macos**](https://github.com/gw31415/herdr-amphetamine-macos)<br><sub>gw31415</sub> | エージェントが作業中の間、Amphetamineの持続時間を延長し続けるherdrプラグイン | `python` | 1 | 2026-07-09 |
| [**agent-keep-awake**](https://github.com/happyeric77/agent-keep-awake)<br><sub>happyeric77</sub> | Herdrのエージェントが動作中は、macOSのスリープを防止する | `javascript` | 1 | 🔄 2026-08-12 |
| [**herdr-newtab-plus**](https://github.com/jeffarese/herdr-newtab-plus)<br><sub>jeffarese</sub> | どのフォルダとどのエージェントかを聞いてくるHerdrの新規タブ：実在するパスを補完し、作業場所を記憶し、代わりにエージェントを起動してくれる | `python` | 1 | 2026-07-26 |
| [**herdr-watcher**](https://github.com/joshka0/herdr-watcher)<br><sub>joshka0</sub> | Herdrエージェント向けの、永続的な処理継続とデタッチされたワーカーコールバック | `rust` | 1 | 2026-08-02 |
| [**herdr-island**](https://github.com/kay-ws/herdr-island)<br><sub>kay-ws</sub> | あなたの対応を待っているエージェントを見つける——各herdrエージェントが止まった理由を表示し、Agentsパネルを該当するものだけに絞り込む | `shell` | 1 | 2026-08-04 |
| [**herdr-agents-preview**](https://github.com/maedana/herdr-agents-preview)<br><sub>maedana</sub> | Herdr向けのマルチエージェントターミナルプレビューダッシュボード：稼働中のすべてのエージェントを同時に表示し、選択中のエージェントが大部分の幅を占める | `rust` | 1 | 🔄 2026-08-14 |
| [**herdr-standup**](https://github.com/natori-hrj/herdr-standup)<br><sub>natori-hrj</sub> | herdr向けのエージェントスタンドアップ——各エージェントのリポジトリ全体で、コミットと未コミットの作業をエージェントごとに要約する | `ai-agents` `git` `standup` `rust` | 1 | 2026-07-23 |
| [**herdr-caffeinate**](https://github.com/neefrehman/herdr-caffeinate)<br><sub>neefrehman</sub> | herdrのエージェントペインがどれか1つでも作業中の間、macOSをスリープさせない（ノートを閉じていても） | `javascript` | 1 | 🔄 2026-08-06 |
| [**🆕 herdr-fleet**](https://github.com/Northern-Lighthouse/herdr-fleet)<br><sub>Northern-Lighthouse</sub> | Manage a fleet of herdr machines over Tailscale: dashboard plugin, auto-discovery, capacity-aware agent dispatch, diskless workspaces | `ai-agents` `tailscale` `python` | 1 | 🔄 2026-08-14 |
| [**herdr-caffeinate**](https://github.com/nwarwick/herdr-caffeinate)<br><sub>nwarwick</sub> | Herdrのエージェントが動作中は、macOSのシステムスリープを防止する | `caffeinate` `coding-agents` `macos` `shell` | 1 | 2026-07-29 |
| [**herdr-imebox**](https://github.com/Sawakee/herdr-imebox)<br><sub>Sawakee</sub> | herdr内のAIエージェントペインに日本語・CJKを入力しやすくする、IME対応のポップアップテキストボックス | `cjk` `ime` `input-method` `japanese` `ratatui` | 1 | 2026-07-17 |
| [**herdr-conductor**](https://github.com/StructuPath/herdr-conductor)<br><sub>StructuPath</sub> | 機能開発チームを、見えるHerdrのエージェントペインとしてオーケストレーションする——Conductorプラグイン | `orchestration` `javascript` | 1 | 2026-07-31 |
| [**herdr-agent-office**](https://github.com/suisya-systems/herdr-agent-office)<br><sub>suisya-systems</sub> | エージェント群をピクセルアートのオフィスとして表示するherdrプラグイン。誰が作業中で、誰が詰まっているかが分かり、そこにジャンプできる | `python` | 1 | 2026-07-25 |
| [**herdr-traex**](https://github.com/szrenwei/herdr-traex)<br><sub>szrenwei</sub> | TraeXエージェントのライフサイクルとメタデータをHerdr Marketplaceと連携させる | `traex` `python` | 1 | 2026-08-04 |
| [**herdr-orc**](https://github.com/tamdogood/herdr-orc)<br><sub>tamdogood</sub> | Herdr向けの、プロファイル駆動でカスタマイズ可能な最小構成のオーケストレーター | `ai-agents` `multi-agent` `orchestrator` `javascript` | 1 | 🔄 2026-08-11 |
| [**tinysend-herdr**](https://github.com/tiny-send/tinysend-herdr)<br><sub>tiny-send</sub> | herdrプラグイン：エージェントがブロック/完了したら自分にメールを送り、返信でブロック解除できる。tinysendを使用 | `ai-agents` `tinysend` `javascript` | 1 | 2026-06-26 |
| [**herdr-rovo-dev**](https://github.com/usrivastava92/herdr-rovo-dev)<br><sub>usrivastava92</sub> | Rovo Dev CLIのセッションを検出し、Herdr上で稼働中のエージェントとして報告するHerdrプラグイン | `ai-agent` `rovo` `rovo-dev` `shell` | 1 | 2026-07-19 |
| [**🆕 herdr-polyglot**](https://github.com/wazum/herdr-polyglot)<br><sub>wazum</sub> | Write coding-agent prompts in your own language — DeepL or Google Cloud Translate translates them to English and delivers them into Claude Code, Codex or any h… | `ai-agents` `bubbletea` `bubbletea-tui` `claude-code` `codex` | 1 | 🔄 2026-08-19 |
| [**herdr-cadence**](https://github.com/zhenyufu/herdr-cadence)<br><sub>zhenyufu</sub> | 1人のLeadと複数のエージェント群からなる、軽量なエージェントオーケストレーター | `rust` | 1 | 🔄 2026-08-19 |
| [**🆕 herdr-simple-prompts**](https://github.com/AlexSamarsky/herdr-simple-prompts)<br><sub>AlexSamarsky</sub> | Only your prompts and the final answers from Codex or Claude, with a working composer | `rust` | 0 | 🔄 2026-08-18 |
| [**hird**](https://github.com/aoprisan/hird)<br><sub>aoprisan</sub> | 複数のharnessをまたぐエージェントの作業キューと共有アサーションメモリを、1つのローカルSQLiteデータベースで支える | `ai-agents` `claude-code` `cli` `mcp` `rust` | 0 | 🔄 2026-08-14 |
| [**herdr-agent-manager**](https://github.com/bleedingfight/herdr-agent-manager)<br><sub>bleedingfight</sub> | fzfベースのファジー検索で、workspace・tab・pane・agentを扱うツール | `python` | 0 | 🔄 2026-08-17 |
| [**🆕 herdr-warp**](https://github.com/cdpath/herdr-warp)<br><sub>cdpath</sub> | Herdrのペイン内で対話型のWarp Agent CLI（warp）を操作するHerdrプラグイン：open/send/status/wait/read/approve/deny/new/stop/exitに対応し、画面をスクレイピングしてidle/working/blockedの状態を判定する | `shell` | 0 | 🔄 2026-08-13 |
| [**clawsouls-herdr-plugin**](https://github.com/clawsouls/clawsouls-herdr-plugin)<br><sub>clawsouls</sub> | _(説明なし)_ | `ai-agents` `persona` `shell` | 0 | 🔄 2026-08-11 |
| [**herdr-tuple-plugin**](https://github.com/doggyfish/herdr-tuple-plugin)<br><sub>doggyfish</sub> | 2つのコーディングエージェントを1つのタブに並べてペアにし、両者の間でテキストをやり取りできるherdrプラグイン | `javascript` | 0 | 🔄 2026-08-08 |
| [**herdr-nudge**](https://github.com/EricBois/herdr-nudge)<br><sub>EricBois</sub> | herdrのエージェントに「継続を促す通知」を仕掛ける——指定した時刻、またはアイドル/ブロック状態になったときに発火する | `shell` | 0 | 2026-07-17 |
| [**🆕 herdr-agent-team**](https://github.com/gdli6177/herdr-agent-team)<br><sub>gdli6177</sub> | A Herdr plugin for Markdown-defined agent teams | `javascript` | 0 | 🔄 2026-08-16 |
| [**🆕 herdr-prompt-bucket**](https://github.com/GNURub/herdr-prompt-bucket)<br><sub>GNURub</sub> | A durable, ordered prompt bucket for coding agents running in Herdr | `claude-code` `codex` `coding-agents` `opencode` `typescript` | 0 | 🔄 2026-08-19 |
| [**ezdras-herdr**](https://github.com/GranamyrBR/ezdras-herdr)<br><sub>GranamyrBR</sub> | Herdr向けの、複数エージェントをリアルタイムに可視化する仕組みとペイン操作機能 | `rust` | 0 | 🔄 2026-08-10 |
| [**herdr-ai-memory**](https://github.com/iagogfe/herdr-ai-memory)<br><sub>iagogfe</sub> | Herdrプラグイン：ai-memoryが管理するワークストリーム経由でコーディングエージェントを起動する——エージェントをまたいだセッションの継続性を実現 | `ai-agents` `ai-memory` `terminal` `javascript` | 0 | 2026-07-24 |
| [**herdr-annotations**](https://github.com/IgorWarzocha/herdr-annotations)<br><sub>IgorWarzocha</sub> | ターミナルで選択した箇所に注釈を集め、Herdrのエージェントに投入する | `ai-agents` `annotations` `terminal` `javascript` | 0 | 2026-07-18 |
| [**🆕 herdr-pane-id**](https://github.com/imtim/herdr-pane-id)<br><sub>imtim</sub> | herdr plugin: label panes with their ID and agent name, plus tab and workspace id labels — so you and your agents can address any pane or agent by id. Works be… | `ai-agents` `coding-agents` `developer-tools` `terminal-multiplexer` `tui` | 0 | 🔄 2026-08-18 |
| [**herdr-spawn**](https://github.com/JLighter/herdr-spawn)<br><sub>JLighter</sub> | herdrプラグイン：プロンプトを渡してコーディングエージェントを起動——エージェントごとに専用のgit worktreeを割り当てる | `shell` | 0 | 2026-08-03 |
| [**🆕 herdr-suffix-agent-filter**](https://github.com/kazimshah39/herdr-suffix-agent-filter)<br><sub>kazimshah39</sub> | Herdrの Agentsサイドバーを、選択したSpaceと同じ名前サフィックスを持つSpaceのエージェントだけに絞り込む | `coding-agents` `developer-tools` `terminal` `javascript` | 0 | 🔄 2026-08-13 |
| [**🆕 herdr-kit**](https://github.com/kevinWangSheng/herdr-kit)<br><sub>kevinWangSheng</sub> | Declarative layouts, an event watcher, plugins and a socket client for Herdr — the parts the herdr CLI does not expose | `coding-agents` `terminal-multiplexer` `python` | 0 | 🔄 2026-08-14 |
| [**herdr-orchestrator**](https://github.com/kylezk777/herdr-orchestrator)<br><sub>kylezk777</sub> | Herdr-orchは、Herdr上で動作するファイルベースのエージェントオーケストレーションツール | `agent-orchestration` `orchestrator` `rust` | 0 | 2026-07-26 |
| [**led-agent-status**](https://github.com/lfsmoura/led-agent-status)<br><sub>lfsmoura</sub> | herdrプラグイン：AIエージェントの状態をBLE LEDテープに表示する——作業中は青、ブロック中は赤の点滅、完了で緑 | `ble` `led` `swift` | 0 | 🔄 2026-08-10 |
| [**herdr-claude-launcher**](https://github.com/lucasleon2107/herdr-claude-launcher)<br><sub>lucasleon2107</sub> | Claude Codeが起動済みの新規タブを開くherdrプラグイン | `ai-agents` `claude-code` `terminal` `tmux` `shell` | 0 | 2026-08-03 |
| [**sheprd**](https://github.com/m-mohamed/sheprd)<br><sub>m-mohamed</sub> | Pi・Codex・Claude Code・OpenCodeを、可視化された1つの独立したHerdr「Flok」にまとめる | `agent-tools` `claude-code` `cli` `codex` `coding-agents` | 0 | 🔄 2026-08-14 |
| [**herdr-alias-setter**](https://github.com/m2selfA/herdr-alias-setter)<br><sub>m2selfA</sub> | ペイン名とエージェントのエイリアスを設定できるHerdrプラグイン（クイック入力またはフルメニュー） | `powershell` | 0 | 2026-07-28 |
| [**🆕 quickTUI**](https://github.com/marcjfj-vmlyr/quickTUI)<br><sub>marcjfj-vmlyr</sub> | OpenTUI上で動く、組み合わせるだけで素早くターミナルUIを作れるプリミティブ集。コーディングエージェントに/quicktuiスキルを与えるHerdrプラグインとして提供される | `bun` `opentui` `terminal` `tui` `typescript` | 0 | 🔄 2026-08-13 |
| [**herdr-agent-dash**](https://github.com/MartinBspheroid/herdr-agent-dash)<br><sub>MartinBspheroid</sub> | Herdr Agent Board：稼働中のコーディングエージェント、その状態・作業ディレクトリ・Gitコンテキストを一目で確認できる、ローカルでキーボード操作中心のHerdrプラグイン | `typescript` | 0 | 2026-07-21 |
| [**herdr-agent-profiles**](https://github.com/mikeyobrien/herdr-agent-profiles)<br><sub>mikeyobrien</sub> | Herdr向けの、データ駆動のCLIハーネスとモデルプロファイル | `ai-agents` `terminal` `python` | 0 | 🔄 2026-08-10 |
| [**🆕 herdr-redact**](https://github.com/moneycaringcoder/herdr-redact)<br><sub>moneycaringcoder</sub> | Warns you when an agent pane has printed a credential — before you screenshot it, stream it, or paste it into a chat window. | `rust` `secret-detection` `security` `terminal` | 0 | 🔄 2026-08-18 |
| [**herdr-green**](https://github.com/natori-hrj/herdr-green)<br><sub>natori-hrj</sub> | herdr向けのエージェントごとのテスト状態表示——エージェントが完了したらプロジェクトのテストを実行し、成功/失敗を表示する | `ai-agents` `ci` `tests` `rust` | 0 | 2026-07-23 |
| [**🆕 agentic-box**](https://github.com/nicoRomeroCuruchet/agentic-box)<br><sub>nicoRomeroCuruchet</sub> | An isolated box where Claude Code drives local model agents. | `agent-orchestration` `agentic` `agentic-workflow` `docker` `ornith-1-0-35b` | 0 | 🔄 2026-08-17 |
| [**herdr-plugin-aos**](https://github.com/noctaIO/herdr-plugin-aos)<br><sub>noctaIO</sub> | 任意のワークスペースから、Agentic OS対応のClaude Codeエージェントをherdrのペインで起動する。非侵襲的なherdrプラグイン | `shell` | 0 | 2026-07-11 |
| [**ocean-herdr**](https://github.com/Risingtides-dev/ocean-herdr)<br><sub>Risingtides-dev</sub> | Herdr向けのOceanエージェント連携 | `coding-agent` `ocean` `rust` | 0 | 2026-07-17 |
| [**herdr-want-to-sleep**](https://github.com/scheron/herdr-want-to-sleep)<br><sub>scheron</sub> | コーディングエージェントが全て動作を終えたら、Macをスリープさせるherdrプラグイン。就寝前にセットしておけば全エージェントの完了を待ち、ブロックされたものも含めて各エージェントが何をしていたかを記録してくれる | `coding-agents` `macos` `shell` | 0 | 2026-07-28 |
| [**herdr-achievements**](https://github.com/SerHappy/herdr-achievements)<br><sub>SerHappy</sub> | あなたのHerdr AIエージェントの群れに、実績とささやかなお祝いを追加する | `achievements` `ai-agents` `developer-tools` `gamification` `go` | 0 | 2026-07-30 |
| [**herdr-ask**](https://github.com/TaylorFinklea/herdr-ask)<br><sub>TaylorFinklea</sub> | Herdrや任意のターミナル向けの、軽量なコマンド生成とターミナルチャット | `cli` `rust` `terminal` `tui` | 0 | 2026-07-21 |
| [**🆕 herdr-restart-always**](https://github.com/terafin/herdr-restart-always)<br><sub>terafin</sub> | Supervise herdr agent panes and always restart whatever the pane is running (claude, hermes, codex, pi, opencode, ...) whenever the agent dies. | `python` | 0 | 🔄 2026-08-15 |
| [**🆕 herdr-group-chat**](https://github.com/terry-li-hm/herdr-group-chat)<br><sub>terry-li-hm</sub> | A shared local Herdr room for Pi, Claude Code, Codex, and Grok Build. | `ai-agents` `claude-code` `codex` `grok` `multi-agent` | 0 | 🔄 2026-08-16 |
| [**herdr-cline-plugin**](https://github.com/TheMetalStorm/herdr-cline-plugin)<br><sub>TheMetalStorm</sub> | 任意のペインから起動した素のCline CLIを、ネイティブのHerdrエージェントのように見せるHerdrプラグイン | `cli` `cline` `herdr-integration` `shell` | 0 | 2026-07-31 |

<details><summary>この目的にも関係するもの</summary>

- [AltanS/collie](https://github.com/AltanS/collie) — 外出先からherdrを管理できるPWA。Tailnet経由でアクセス可能、プッシュ通知やクイックアクションなど
- [a2u/herdr-jira](https://github.com/a2u/herdr-jira) — herdr向けのJira TUIプラグイン——設定可能なJQLフィルタでissueを閲覧・検索・ステータス変更し、1キーでターミナル上のAIエージェントにissueを委任できる
- [walcew/herdr-assist](https://github.com/walcew/herdr-assist) — AIコーディングエージェント向けターミナルマルチプレクサHerdrのための、物理デスクパネル——セッションの状態を色で表示し、エージェントが判断を仰ぐために止まるとベルを鳴らす。ESP32-S3 + LVGL、ビルド済…
- [e2b-dev/herdr-e2b-sandbox](https://github.com/e2b-dev/herdr-e2b-sandbox) — herdr plugin that mirrors a git worktree into an E2B sandbox — one box or a branch-per-agent fleet, with a TU…
- [miko-misa/herdr-portfwd](https://github.com/miko-misa/herdr-portfwd) — リモートマシン上のコーディングエージェント向けの自動SSHポートフォワーディング——エージェントが出力したlocalhost URLをCtrl+クリックすると、同じポートで手元のマシンにページが開く。Herdrプラグイン

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-worktree"></a>

## git worktree・ブランチ運用

> 作業ごとに worktree を切って、片付けまで自動でやりたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-worktrunk**](https://github.com/devashish2203/herdr-worktrunk)<br><sub>devashish2203</sub> | git worktree管理のためworktrunkを統合するHerdrプラグイン | `shell` | 97 | 🔄 2026-08-19 |
| [**herdr-plugin-jj-workspace**](https://github.com/NathanFlurry/herdr-plugin-jj-workspace)<br><sub>NathanFlurry</sub> | Jujutsu (jj) のワークスペースをHerdrのワークスペースとして作成・削除する | `jujutsu` `rust` | 43 | 2026-07-08 |
| [**herdr-plugin-renamer**](https://github.com/wyattjoh/herdr-plugin-renamer)<br><sub>wyattjoh</sub> | エージェントへの最初のプロンプトから、自動生成されたherdrのworktreeブランチとワークスペースをリネームする（デバイス上のApple FoundationModelsまたはCodexを利用） | `rust` | 10 | 🔄 2026-08-17 |
| [**jj-waltz**](https://github.com/EzraCerpac/jj-waltz)<br><sub>EzraCerpac</sub> | Worktrunkに触発されたJujutsuワークスペース切り替えツール | `cli` `jj` `jujitsu` `utility` `workspace` | 7 | 🔄 2026-08-19 |
| [**🆕 herdkit**](https://github.com/briankeegan1/herdkit)<br><sub>briankeegan1</sub> | Governance and parallelism for herdr-based agent workflows — a coordinator drains your backlog into isolated worktree builders (Claude Code, Codex, or Grok), a… | `shell` | 6 | 🔄 2026-08-19 |
| [**herdr-plugin-git-worktree-hooks**](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks)<br><sub>freethinkel</sub> | git worktreeの作成/削除時にシェルコマンドを実行する——どのリポジトリの外にも置ける、全プロジェクト共通の1つのYAML設定 | `git-worktree` `javascript` | 6 | 2026-07-06 |
| [**herdr-worktree-from-pr**](https://github.com/tdi/herdr-worktree-from-pr)<br><sub>tdi</sub> | GitHubのPRからgit worktreeを作成し、herdrのワークスペースとして開く | `javascript` | 6 | 2026-07-20 |
| [**herdr-worktree-seed**](https://github.com/jlimas/herdr-worktree-seed)<br><sub>jlimas</sub> | コピーオンライトのnode_modulesと設定可能なローカルdotfilesを、新しいworktreeに投入するHerdrプラグイン | `developer-tools` `dotfiles` `git-worktree` `nodejs` `typescript` | 5 | 2026-07-28 |
| [**herdr-symlink-worktree**](https://github.com/hmu332233/herdr-symlink-worktree)<br><sub>hmu332233</sub> | メインのリポジトリにある共有ローカルファイルを、新しいworktreeにシンボリックリンクするherdrプラグイン | `shell` | 4 | 2026-07-16 |
| [**herdr-fresh-worktree**](https://github.com/persiyanov/herdr-fresh-worktree)<br><sub>persiyanov</sub> | 新しく作成したherdrのworktreeを、originのデフォルトブランチの最新状態にリセットする | `javascript` | 4 | 2026-06-25 |
| [**herdr-worktreeinclude**](https://github.com/tanshio/herdr-worktreeinclude)<br><sub>tanshio</sub> | Herdrプラグイン：.worktreeincludeにマッチするgit管理外ファイルを、新しく作成されたworktreeにコピーする | `worktree` `worktreeiclude` `shell` | 4 | 2026-07-11 |
| [**herdr-worktree-hooks**](https://github.com/timofey-TK/herdr-worktree-hooks)<br><sub>timofey-TK</sub> | herdrプラグイン：git worktreeの作成・オープン・削除時に、カスタムのセットアップ/後始末コマンドを実行する | `developer-tools` `git-worktree` `worktree` `python` | 4 | 2026-07-17 |
| [**herdr-branch-cleanup**](https://github.com/osolmaz/herdr-branch-cleanup)<br><sub>osolmaz</sub> | ペインのブランチがGitHub上でマージまたは削除されたら、デフォルトブランチにチェックアウトする | `git` `github` `rust` | 3 | 2026-07-26 |
| [**herdr-worktree-lifecycle**](https://github.com/qdentity/herdr-worktree-lifecycle)<br><sub>qdentity</sub> | Herdrプラグイン：worktreeのライフサイクルイベントを、リポジトリ側が持つセットアップ/後始末用のラッパーに配信する | `rust` | 3 | 2026-06-29 |
| [**herdr-remote-worktrunk**](https://github.com/ditwrd/herdr-remote-worktrunk)<br><sub>ditwrd</sub> | Herdr向けのリモートworktrunkワークスペース | `shell` | 2 | 2026-07-10 |
| [**🆕 herdr-e2b-sandbox**](https://github.com/e2b-dev/herdr-e2b-sandbox)<br><sub>e2b-dev</sub> | herdr plugin that mirrors a git worktree into an E2B sandbox — one box or a branch-per-agent fleet, with a TUI dashboard | `cli` `cloud-dev` `e2b` `git-worktree` `sandbox` | 2 | 🔄 2026-08-19 |
| [**herdr-multirepo**](https://github.com/jattento/herdr-multirepo)<br><sub>jattento</sub> | 複数のリポジトリにまたがる1つのフィーチャーブランチを、1つのHerdrワークスペースで扱う | `git-worktree` `python` | 2 | 2026-08-03 |
| [**herdr-jj-status**](https://github.com/mroth/herdr-jj-status)<br><sub>mroth</sub> | herdrプラグイン：jjのワークスペースのJujutsuブックマーク/ステータスを、スペースのサイドバーに表示する | `shell` | 2 | 2026-07-28 |
| [**herdr-worktreeinclude**](https://github.com/serhii-chernenko/herdr-worktreeinclude)<br><sub>serhii-chernenko</sub> | 新しいworktreeにカスタムパスを許可し、Claude CLIと同様に`.worktreeinclude`ファイルを尊重する | `worktree` `shell` | 2 | 2026-07-23 |
| [**🆕 herdr-corral**](https://github.com/bfreed/herdr-corral)<br><sub>bfreed</sub> | Herdr内でGit worktreeをまとめて管理——envファイル、依存関係、エージェント/シェル/サーバー用のタブ、マージしても安全なクリーンアップに対応。Herdr向けのworkmux代替 | `git-worktree` `workmux` `python` | 1 | 🔄 2026-08-14 |
| [**herdr-worktree-copy**](https://github.com/crexi/herdr-worktree-copy)<br><sub>crexi</sub> | .worktree-copyマニフェストに基づき、worktreeローカルファイルをコピー・シンボリックリンクするHerdrプラグイン | `git-worktree` `shell` | 1 | 2026-07-28 |
| [**trunkr**](https://github.com/disintegrator/trunkr)<br><sub>disintegrator</sub> | Herdr🤝Worktrunk——HerdrとWorktrunkを連携させるプラグイン | `go` | 1 | 🔄 2026-08-12 |
| [**herdr-allow**](https://github.com/Feasy01/herdr-allow)<br><sub>Feasy01</sub> | herdrプラグイン：.herdr-allowの許可リストを使って、gitignore対象のファイル（.env、シークレット、ローカル設定）を新しいworktreeすべてにコピーする | `shell` | 1 | 2026-07-02 |
| [**herdr-plugin-gwm**](https://github.com/kbrdn1/herdr-plugin-gwm)<br><sub>kbrdn1</sub> | git worktree管理のためgwmを操作するherdrプラグイン——gwmを唯一の正とし、herdrはそれに追従する | `bash` `cli` `git-worktree` `gwm` `worktree` | 1 | 2026-07-27 |
| [**🆕 herdr**](https://github.com/AgentTeamsRun/herdr)<br><sub>AgentTeamsRun</sub> | Report herdr worktree lifecycle events to the AgentTeams registry | — | 0 | 🔄 2026-08-19 |
| [**herdr-worktree-provisioner**](https://github.com/arjenblokzijl/herdr-worktree-provisioner)<br><sub>arjenblokzijl</sub> | 新しいworktree専用の可視ペインで、リポジトリごとのセットアップを実行する——組み合わせ可能でガード不要 | `bootstrap` `git-worktree` `worktree` `shell` | 0 | 2026-07-08 |
| [**herdr-deck**](https://github.com/ctbaum/herdr-deck)<br><sub>ctbaum</sub> | herdr-agents.nvimと組み合わせて使うワークスペースランチャー：Neovim・エージェント・シェル・lazygitがあらかじめ用意された「デッキ」で、ClaudeやCodexを開始または再開できる | `claude-code` `codex` `coding-agents` `git-worktree` `neovim` | 0 | 🔄 2026-08-12 |
| [**herdr-worktreeinclude**](https://github.com/eightHundreds/herdr-worktreeinclude)<br><sub>eightHundreds</sub> | Herdrプラグイン：.worktreeincludeで指定したgit管理外ファイルを、新しいworktreeにコピーする | `worktree` `rust` | 0 | 2026-07-28 |
| [**herdr-title**](https://github.com/filoozom/herdr-title)<br><sub>filoozom</sub> | 選択中のworktreeとエージェントの活動状況を、ターミナルのタブタイトルに表示するHerdrプラグイン | `rust` | 0 | 2026-07-24 |
| [**herdr-hub-worktrees**](https://github.com/klukacin/herdr-hub-worktrees)<br><sub>klukacin</sub> | herdrプラグイン：hubのworktreeを、ネストされた各サブリポジトリのクローンにミラーする | `git-worktree` `monorepo` `terminal-multiplexer` `shell` | 0 | 🔄 2026-08-12 |
| [**gren-herdr**](https://github.com/langtind/gren-herdr)<br><sub>langtind</sub> | grenを介してgit worktreeを作成・切り替え・削除するherdrプラグイン——grenの作成後セットアップにも対応 | `git-worktree` `gren` `shell` | 0 | 🔄 2026-08-18 |
| [**herdr-worktree-hooks-plugin**](https://github.com/m1sk9/herdr-worktree-hooks-plugin)<br><sub>m1sk9</sub> | Herdrのworktreeに、カスタマイズ可能なフックを追加するプラグイン | `rust` | 0 | 🔄 2026-08-16 |
| [**🆕 herdr-collide**](https://github.com/moneycaringcoder/herdr-collide)<br><sub>moneycaringcoder</sub> | Warns when agents working in different git worktrees of one repo are about to collide — and whether their edits merely overlap or will actually conflict. | `conflict-detection` `git-worktree` `rust` `terminal` | 0 | 🔄 2026-08-19 |
| [**🆕 herdr-shear**](https://github.com/moneycaringcoder/herdr-shear)<br><sub>moneycaringcoder</sub> | Find the git worktrees that are safe to delete, and delete those. A worktree janitor for herdr. | `cleanup` `git-worktree` `rust` `terminal` | 0 | 🔄 2026-08-19 |
| [**🆕 herdr-standup**](https://github.com/moneycaringcoder/herdr-standup)<br><sub>moneycaringcoder</sub> | A digest of what your agents actually did. One command, one readable summary of every Herdr workspace over a time window — commits, change volume, branch, and… | `git` `rust` `standup` `terminal` | 0 | 🔄 2026-08-16 |
| [**herdr-jj**](https://github.com/OliverGilan/herdr-jj)<br><sub>OliverGilan</sub> | HerdrにJujutsuのワークスペースサポートを追加する | `jujutsu` `rust` | 0 | 🔄 2026-08-12 |
| [**herdr-worktree-include**](https://github.com/scoussens-nthplusio/herdr-worktree-include)<br><sub>scoussens-nthplusio</sub> | リポジトリの.worktreeincludeを使って、.envなどgit管理外のファイルを新しいHerdr worktreeにコピーする——Claude Codeが使うのと同じファイル・同じルール | `dotenv` `git-worktree` `shell` | 0 | 🔄 2026-08-12 |
| [**🆕 herdr-worktree**](https://github.com/tjg184/herdr-worktree)<br><sub>tjg184</sub> | Herdr worktree plugin that works with worktrunk and native worktrees | `rust` | 0 | 🔄 2026-08-13 |
| [**herdr-plugin-worktree-bootstrap**](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap)<br><sub>zerodice0</sub> | 新しいHerdrのGit worktreeに、無視されているローカルファイルを安全にコピーし、セットアップコマンドを実行する | `python` | 0 | 2026-08-03 |

<details><summary>この目的にも関係するもの</summary>

- [tdi/herdr-worktree-from-linear](https://github.com/tdi/herdr-worktree-from-linear) — Linearのissueからgit worktreeを作成し、herdrのワークスペースとして開く
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — JavaScript/TypeScript向けにHerdrのworktreeを自動でブートストラップ——ロックファイルを考慮したインストールと、安全な環境ファイルの復元に対応
- [tomasvarga/herdr-e2b](https://github.com/tomasvarga/herdr-e2b) — 必要なときにgit worktreeを新しいE2Bクラウドサンドボックスへミラーする——未コミットの変更も含めたスナップショットをアップロードするだけで、pushやcloneは不要なherdrプラグイン
- [JLighter/herdr-spawn](https://github.com/JLighter/herdr-spawn) — herdrプラグイン：プロンプトを渡してコーディングエージェントを起動——エージェントごとに専用のgit worktreeを割り当てる
- [snics/herdr-worktree-from-gitlab](https://github.com/snics/herdr-worktree-from-gitlab) — herdrプラグイン：GitLabのissueから（glab経由で）git worktreeとワークスペースを作成する
- [untalfranfernandez/herdr-worktreeinclude](https://github.com/untalfranfernandez/herdr-worktreeinclude) — 新しいgit worktreeに必要なgitignore対象のローカルファイル（.env、settings.local.json、フィクスチャなど）を自動配置するHerdrプラグイン。.worktreeincludeフ…

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-review"></a>

## コードレビュー・差分確認

> エージェントが書いた差分を読んで、コメントを返したい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**crabbox**](https://github.com/openclaw/crabbox)<br><sub>openclaw</sub> | Crabbox：サンドボックスを温め、差分を同期し、テストスイートを実行する | `agent-skills` `remote-test-runner` `go` | 1322 | 🔄 2026-08-20 |
| [**herdr-reviewr**](https://github.com/persiyanov/herdr-reviewr)<br><sub>persiyanov</sub> | herdr向けのコードレビュー＋ファイルビューアのサイドバー。エージェントの差分にコメントして差し戻せる。PRとそのチェック・コメントの読み取り専用表示も付属 | `code-review` `rust` `tui` | 472 | 🔄 2026-08-19 |
| [**🆕 herdr-hunk-diff**](https://github.com/jhochenbaum/herdr-hunk-diff)<br><sub>jhochenbaum</sub> | Review agent-authored changes in hunk from herdr and send inline comments back to the responsible agent. | `code-review` `hunk` `typescript` | 73 | 🔄 2026-08-19 |
| [**herdr-plannotator**](https://github.com/plannotator/herdr-plannotator)<br><sub>plannotator</sub> | HerdrのBrowserペイン内でPlannotatorのレビューを開くプラグイン | `plannotator` `typescript` | 16 | 2026-07-29 |
| [**herdr-pickr**](https://github.com/tomasvarga/herdr-pickr)<br><sub>tomasvarga</sub> | herdr向けのPRレビュールーター——GitHubのPRやGitLabのMRリンクをCtrl+クリックしてレビュアー（tuicr・hunk・diff・ブラウザ・または独自ツール）を選択、AIによる一次レビューもオプションで利用可能 | `cli` `code-review` `pull-request` `tui` `shell` | 14 | 2026-07-13 |
| [**herdr-plugin-hunk**](https://github.com/edmundmiller/herdr-plugin-hunk)<br><sub>edmundmiller</sub> | Hunkの差分をスプリットペインやタブで開くHerdrプラグイン | `python` | 13 | 2026-06-23 |
| [**herdr-gitview**](https://github.com/ChmaraX/herdr-gitview)<br><sub>ChmaraX</sub> | herdr向けのGitステータス/差分パネル——変更のレビュー、nvimでの編集、ステージ/コミット/破棄をすべてターミナルから行える | `git` `git-diff` `git-tui` `neovim` `rust` | 7 | 🔄 2026-08-12 |
| [**herdr-plugin-hunk-autodiff**](https://github.com/scott306lr/herdr-plugin-hunk-autodiff)<br><sub>scott306lr</sub> | Herdrプラグイン：コーディングエージェントが未コミットの変更を残して完了したら、hunkの差分スプリットを自動で開く | `claude-code` `hunk` `python` | 5 | 2026-07-05 |
| [**herdr-progressive-reviewer**](https://github.com/flupke/herdr-progressive-reviewer)<br><sub>flupke</sub> | Tidewaveに着想を得た、ターン制の差分レビューア | `rust` | 3 | 🔄 2026-08-07 |
| [**herdr-review.nvim**](https://github.com/inferst/herdr-review.nvim)<br><sub>inferst</sub> | GitとherdrをNeovimに統合したコードレビュー用UI | `lua` | 3 | 2026-08-01 |
| [**herdr-extensions**](https://github.com/vonzelle-vzt/herdr-extensions)<br><sub>vonzelle-vzt</sub> | herdr向けの小さなVS Code——LSPによる診断・自動補完・リネーム・定義へジャンプに対応した本格エディタに加え、ソース管理・検索・問題一覧・テスト・デバッガ・アプリのライブプレビュー・実行時エラー捕捉・画像貼り付け・エージェント差分レビューまで搭載。12パネル構成、コマンド1つで冪等かつ元に戻せる導入 | `agent-tools` `autocomplete` `claude-code` `cli` `code-review` | 3 | 2026-08-03 |
| [**herdr-scribe**](https://github.com/Javamomma/herdr-scribe)<br><sub>Javamomma</sub> | herdrプラグイン：録音せずにライブで会議を文字起こし——マイク入力をRAM上のみのトランスクリプトとライブ分析用ペインに変換。停止時には議事録・任意のポリシーゲート・レビュー可能な自動ドラフトを生成。Linux/WSL2およびmacOS対応 | `macos` `meeting-notes` `privacy` `speech-to-text` `terminal` | 2 | 🔄 2026-08-07 |
| [**herdr-comments**](https://github.com/shadowfax92/herdr-comments)<br><sub>shadowfax92</sub> | コピーしたHerdrのターミナル出力に注釈を付け、ペインごとのコメントを収集してNeovimでレビューできる | `ai-agents` `annotations` `neovim` `rust` `terminal` | 2 | 🔄 2026-08-19 |
| [**herdr-hunk**](https://github.com/yuucu/herdr-hunk)<br><sub>yuucu</sub> | herdrプラグイン：エージェントのワークスペースでHunkの差分レビューをトグルする | `diff` `hunk` `go` | 2 | 2026-07-20 |
| [**herdr-strays**](https://github.com/aleslanger/herdr-strays)<br><sub>aleslanger</sub> | 野良git worktreeを取りまとめるターミナルUI——プロジェクトを一覧し、変更ファイルをリアルタイム表示、差分を読み、パネルを離れずにClaudeへプロンプトを送れる | `rust` | 1 | 🔄 2026-08-12 |
| [**roboherd**](https://github.com/andschneider/roboherd)<br><sub>andschneider</sub> | herdrのワークスペース内で、roborevのレビュー状態とアクションを扱う | `rust` `tui` | 1 | 🔄 2026-08-12 |
| [**herdr-agent-diff**](https://github.com/baotran01/herdr-agent-diff)<br><sub>baotran01</sub> | エージェントのファイルシステムとGit差分を確認するHerdrプラグイン | `rust` | 1 | 2026-08-03 |
| [**herdr-stagr**](https://github.com/brianh20/herdr-stagr)<br><sub>brianh20</sub> | herdr向けのソース管理サイドバー——並列差分表示でステージ・アンステージ・破棄ができる | `git` `tui` `rust` | 1 | 🔄 2026-08-06 |
| [**herdr-peer-review**](https://github.com/Elio2000/herdr-peer-review)<br><sub>Elio2000</sub> | herdrのペインで2つ目のコーディングエージェントを開き、差分をレビューさせる——監視可能・自動承認・読み取り専用。レビュー↔修正↔判断の自律ループ用のClaude Codeスキルも同梱 | `agent-skills` `ai-agents` `claude-code` `code-review` `codex` | 1 | 2026-07-16 |
| [**herdr-git-graph**](https://github.com/jorge-huxley/herdr-git-graph)<br><sub>jorge-huxley</sub> | Herdr向けの読み取り専用gitグラフTUIプラグイン——色付きASCIIレーン、ブランチフィルタ、検索、必要に応じた差分表示に対応 | `rust` | 1 | 2026-07-17 |
| [**herdr-review**](https://github.com/quantk/herdr-review)<br><sub>quantk</sub> | エージェントが書いた変更をHunkでレビューし、インラインのフィードバックをHerdr経由で送り返す | `code-review` `hunk` `javascript` | 1 | 2026-07-28 |
| [**🆕 herdr-lazygit-viewer**](https://github.com/tareqmlx/herdr-lazygit-viewer)<br><sub>tareqmlx</sub> | Opens lazygit at the files, branches, commits, or stash panel, in whichever Herdr surface suits the moment. | `code-review` `lazygit` `rust` | 1 | 🔄 2026-08-14 |
| [**herdr-hunk-gh-diff**](https://github.com/Allianaab2m/herdr-hunk-gh-diff)<br><sub>Allianaab2m</sub> | Herdrプラグイン：現在のペインでチェックアウトしているブランチと、そのGitHubプルリクエストのターゲットブランチとの間でHunkの差分を開く | `python` | 0 | 2026-07-15 |
| [**herdr-hunk**](https://github.com/cevr/herdr-hunk)<br><sub>cevr</sub> | Hunkのレビューコメントを、対応するHerdrエージェントペインに送る | `effect-ts` `hunk` `typescript` | 0 | 2026-07-28 |
| [**🆕 herdr-hunk**](https://github.com/goofansu/herdr-hunk)<br><sub>goofansu</sub> | Hunk review actions | `python` | 0 | 🔄 2026-08-19 |
| [**herdr-implement-review**](https://github.com/Idan-Levin/herdr-implement-review)<br><sub>Idan-Levin</sub> | Codexによる実装・セキュリティスキャン・親エージェントによるレビューを行うHerdrワークフロー | `claude-code` `codex` `security-review` `shell` | 0 | 🔄 2026-08-10 |
| [**herdr-plan-code-review**](https://github.com/inxx/herdr-plan-code-review)<br><sub>inxx</sub> | herdrプラグイン：Opusが計画し、Sonnetがコーディングし、Claude+Codexがレビューする——1つの操作で4つのエージェントペインを開く | `claude-code` `codex` `terminal` `shell` | 0 | 2026-07-06 |
| [**herdr-idle-panes**](https://github.com/leonho/herdr-idle-panes)<br><sub>leonho</sub> | herdrプラグイン：アイドル状態のシェルのままになっているペインを確認して閉じる、チェックリスト形式のポップアップ | `python` | 0 | 2026-07-18 |
| [**herdr-roborev**](https://github.com/phin-tech/herdr-roborev)<br><sub>phin-tech</sub> | roborevのレビューTUIをHerdrのペインで開く | `shell` | 0 | 2026-07-21 |
| [**🆕 herdr-diff-review.nvim**](https://github.com/rytkmt/herdr-diff-review.nvim)<br><sub>rytkmt</sub> | Review AI agent file changes in Neovim diff mode before applying — approve or deny edits from Claude Code and Kiro CLI with a single command. AIエージェントのファイル変更をN… | `kiro-cli` `neovim` `neovim-plugin` `neovim-plugins` `nvim` | 0 | 🔄 2026-08-18 |
| [**herdr-hunk-viewer**](https://github.com/tareqmlx/herdr-hunk-viewer)<br><sub>tareqmlx</sub> | _(説明なし)_ | `code-review` `hunk` `rust` | 0 | 🔄 2026-08-09 |
| [**herdr-code-review**](https://github.com/txmed82/herdr-code-review)<br><sub>txmed82</sub> | 構造化されたAIコードレビューを行うHerdrプラグイン | `code-review` `javascript` | 0 | 🔄 2026-08-19 |

<details><summary>この目的にも関係するもの</summary>

- [briankeegan1/herdkit](https://github.com/briankeegan1/herdkit) — Governance and parallelism for herdr-based agent workflows — a coordinator drains your backlog into isolated…
- [JacquesvanWyk/herdr-hunk](https://github.com/JacquesvanWyk/herdr-hunk) — herdr向けの、Hunkの差分をfzfで対話的に選ぶピッカー：コミット・範囲・stashに対応し、エージェント完了時に自動オープンもできる
- [tomasvarga/herdr-sniffr](https://github.com/tomasvarga/herdr-sniffr) — レビューする前に、AIがPRの問題を検知する——エージェントによる一次チェックでtuicrにドラフトコメントを残す。特定のエージェントに依存しない（codex/claude/cursor/grok/…）
- [elKei24/herdr-co-review](https://github.com/elKei24/herdr-co-review) — Split-screen PR review in herdr: your agent finds issues, you triage each one next to its code in a TUI, the…
- [krzysztoff1/herdr-cull](https://github.com/krzysztoff1/herdr-cull) — herdr内のアイドル状態のエージェントペインを確認して閉じる——fzfによる複数選択、確認なしで閉じることはない
- [mikhail-angelov/herdr-review-loop](https://github.com/mikhail-angelov/herdr-review-loop) — herdrのワークスペース内でエージェント同士が自動的に相互レビューする——1体が書き、もう1体がレビューし、これを繰り返す
- [moneycaringcoder/herdr-collide](https://github.com/moneycaringcoder/herdr-collide) — Warns when agents working in different git worktrees of one repo are about to collide — and whether their edi…

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-forge"></a>

## GitHub / issue トラッカー連携

> issue や PR を起点に作業を始めたい / PR の状態を追いたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**ghzinga**](https://github.com/osolmaz/ghzinga)<br><sub>osolmaz</sub> | 1つのGitHub issueやPRをクリックだけで見られる、Rust製の簡単なTUI | `rust` | 78 | 2026-07-26 |
| [**herdr-plugin-gh-pr**](https://github.com/wyattjoh/herdr-plugin-gh-pr)<br><sub>wyattjoh</sub> | フォーカス中のエージェントペインのブランチに対応するGitHub PRの状態をサイドバーに表示するherdrプラグイン | `typescript` | 18 | 2026-07-16 |
| [**herdr-plugin-github-start**](https://github.com/ogulcancelik/herdr-plugin-github-start)<br><sub>ogulcancelik</sub> | GitHub issue・PR・ディスカッションからCodexやClaudeを起動するHerdrプラグイン | `javascript` | 15 | 2026-06-30 |
| [**herdr-worktree-from-linear**](https://github.com/tdi/herdr-worktree-from-linear)<br><sub>tdi</sub> | Linearのissueからgit worktreeを作成し、herdrのワークスペースとして開く | `javascript` | 12 | 🔄 2026-08-11 |
| [**herdr-jira**](https://github.com/a2u/herdr-jira)<br><sub>a2u</sub> | herdr向けのJira TUIプラグイン——設定可能なJQLフィルタでissueを閲覧・検索・ステータス変更し、1キーでターミナル上のAIエージェントにissueを委任できる | `ai-agents` `jira` `ratatui` `rust` `tui` | 10 | 2026-07-18 |
| [**herdr-pr-tracker**](https://github.com/Matovidlo/herdr-pr-tracker)<br><sub>Matovidlo</sub> | herdrプラグイン：各Claude Codeセッションが作成するGitHub PRを、gh状態とアクション付きで追跡する | `claude-code` `shell` | 10 | 🔄 2026-08-12 |
| [**herdr-linear**](https://github.com/JacquesvanWyk/herdr-linear)<br><sub>JacquesvanWyk</sub> | herdrのスプリットペインまたはタブ内で動くfzf駆動のLinearパネル：issue検索、プロジェクトの深掘り、issue作成、ステータス変更ができる | `shell` | 7 | 2026-07-12 |
| [**herdr-git-status**](https://github.com/krystof018/herdr-git-status)<br><sub>krystof018</sub> | herdr内にCIの状態を表示する——GitLab（パイプライン＋マージリクエスト）とGitHub（Actions＋プルリクエスト）の両方に対応し、リポジトリのoriginから自動検出する | `bash` `ci-cd` `ci-status` `developer-tools` `github-actions` | 4 | 2026-07-01 |
| [**herdr-plugin-github-dash**](https://github.com/kukv/herdr-plugin-github-dash)<br><sub>kukv</sub> | GitHubのプルリクエストとissueを閲覧・管理するHerdrプラグイン | `cli` `github` `go` | 4 | 🔄 2026-08-15 |
| [**herdr-pr-board**](https://github.com/cdowell09/herdr-pr-board)<br><sub>cdowell09</sub> | 複数リポジトリを横断できる、設定可能なHerdr向けGitHubプルリクエストダッシュボード | `github` `tui` `go` | 3 | 🔄 2026-08-15 |
| [**mergr**](https://github.com/jsmenzies/mergr)<br><sub>jsmenzies</sub> | Herdr Spaceのサイドバー行にGitHubプルリクエストの状態を表示する | `github-pull-requests` `rust` | 3 | 2026-07-30 |
| [**herdr-plugin-gh-workflow**](https://github.com/kkckkc/herdr-plugin-gh-workflow)<br><sub>kkckkc</sub> | GitHubワークフロー向けのHerdrプラグイン | `javascript` | 3 | 2026-07-03 |
| [**herdr-linear**](https://github.com/talent-factory/herdr-linear)<br><sub>talent-factory</sub> | Herdr向けのLinear issueパネル。Enterキーで実装に着手できる | `rust` | 3 | 🔄 2026-08-17 |
| [**herdr-beads**](https://github.com/hexsprite/herdr-beads)<br><sub>hexsprite</sub> | HerdrでbeadsのissueIDをCtrl+クリックすると、詳細をスプリットペインで開く | `beads` `issue-tracker` `terminal` `shell` | 2 | 🔄 2026-08-07 |
| [**herdr-sniffr**](https://github.com/tomasvarga/herdr-sniffr)<br><sub>tomasvarga</sub> | レビューする前に、AIがPRの問題を検知する——エージェントによる一次チェックでtuicrにドラフトコメントを残す。特定のエージェントに依存しない（codex/claude/cursor/grok/…） | `ai` `cli` `code-review` `pull-request` `tuicr` | 2 | 2026-07-14 |
| [**herdr-board**](https://github.com/bredebjorhovd/herdr-board)<br><sub>bredebjorhovd</sub> | コーディングエージェントが列に並び、自分の仕事を自律的にこなす場所——GitHub issueを入力に、herdrのペインで自律エージェントが動き、書いた本人にPRレビューが返ってくる | `rust` | 1 | 🔄 2026-08-14 |
| [**herdr-dashboard**](https://github.com/chouxcreams/herdr-dashboard)<br><sub>chouxcreams</sub> | herdrのワークスペース向けのPRステータスダッシュボードTUI——ペインごとのPRの状態・CI・レビューを一目で確認できる | `dashboard` `github` `pull-requests` `ratatui` `rust` | 1 | 2026-07-28 |
| [**herdr-plugin-dotfiles-github-link-preview**](https://github.com/edmundmiller/herdr-plugin-dotfiles-github-link-preview)<br><sub>edmundmiller</sub> | GitHubのissueやプルリクエストをサイドペインでプレビューするHerdrプラグイン | `python` | 1 | 2026-06-23 |
| [**🆕 herdr-co-review**](https://github.com/elKei24/herdr-co-review)<br><sub>elKei24</sub> | Split-screen PR review in herdr: your agent finds issues, you triage each one next to its code in a TUI, the agent posts what you approve. | `cli` `code-review` `pull-request` `rust` `tui` | 1 | 🔄 2026-08-19 |
| [**worktender**](https://github.com/steig/worktender)<br><sub>steig</sub> | GitHubのissueから、専用worktreeで作業するコーディングエージェントまでを1コマンドでつなぐ | `ai-agents` `claude-code` `coding-agents` `git-worktree` `golang` | 1 | 🔄 2026-08-16 |
| [**herdr-plugin-jira-pr**](https://github.com/abtris/herdr-plugin-jira-pr)<br><sub>abtris</sub> | herdrプラグイン：現在のブランチのPRに紐づくJira issueを表示し、内容が食い違っていれば警告する | `github-pr` `jira` `shell` | 0 | 2026-08-04 |
| [**herdr-spaces-pr-status**](https://github.com/jmarbutt/herdr-spaces-pr-status)<br><sub>jmarbutt</sub> | Conductor風のPRボードで、herdrのスペースにGitHubプルリクエストの状態を表示する | `github-pull-request` `javascript` | 0 | 2026-08-01 |
| [**herdr-pr-preview**](https://github.com/juninaba/herdr-pr-preview)<br><sub>juninaba</sub> | 現在のブランチのGitHubプルリクエストを、スプリットペインでプレビューするHerdrプラグイン | `shell` | 0 | 2026-07-08 |
| [**github-issue-herdr-plugin**](https://github.com/nyanyaon/github-issue-herdr-plugin)<br><sub>nyanyaon</sub> | GitHubのissueを「herd（統率）」するためのClaude Codeプラグイン | `rust` | 0 | 2026-07-27 |
| [**herdr-pr-tab-renamer**](https://github.com/ralphilius/herdr-pr-tab-renamer)<br><sub>ralphilius</sub> | 検出したプルリクエスト番号でタブ名を変更するHerdrプラグイン | `javascript` | 0 | 2026-08-03 |
| [**herdr-worktree-from-gitlab**](https://github.com/snics/herdr-worktree-from-gitlab)<br><sub>snics</sub> | herdrプラグイン：GitLabのissueから（glab経由で）git worktreeとワークスペースを作成する | `gitlab` `rust` `worktree` | 0 | 2026-07-09 |
| [**herdr-pr-workflow**](https://github.com/tamdogood/herdr-pr-workflow)<br><sub>tamdogood</sub> | フォーカス中のエージェントに、現在のブランチのプルリクエストを安全に作成またはマージするよう指示するHerdrアクション | `javascript` | 0 | 🔄 2026-08-10 |

<details><summary>この目的にも関係するもの</summary>

- [tomasvarga/herdr-pickr](https://github.com/tomasvarga/herdr-pickr) — herdr向けのPRレビュールーター——GitHubのPRやGitLabのMRリンクをCtrl+クリックしてレビュアー（tuicr・hunk・diff・ブラウザ・または独自ツール）を選択、AIによる一次レビューもオプシ…
- [tdi/herdr-worktree-from-pr](https://github.com/tdi/herdr-worktree-from-pr) — GitHubのPRからgit worktreeを作成し、herdrのワークスペースとして開く
- [kiitosu/herdr-jira-board](https://github.com/kiitosu/herdr-jira-board) — Jira kanban board inside herdr with Claude Code session launcher

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-layout"></a>

## ワークスペース・レイアウト構築

> プロジェクトを開いたら、タブ・ペイン・起動コマンドまで一発で整えたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-spreader**](https://github.com/yuk1ty/herdr-spreader)<br><sub>yuk1ty</sub> | 1つのYAMLファイルから、herdrのワークスペースレイアウト全体（タブ・ペイン・起動コマンドなど）を一括で立ち上げる | `rust` | 78 | 🔄 2026-08-16 |
| [**dotfiles**](https://github.com/lararosekelley/dotfiles)<br><sub>lararosekelley</sub> | Bashシェルでの使用を想定した個人用dotfiles | `bash` `bootstrap` `dotfiles` `homebrew` `macos` | 51 | 🔄 2026-08-17 |
| [**herdr-plugin-workspace-manager**](https://github.com/razajamil/herdr-plugin-workspace-manager)<br><sub>razajamil</sub> | worktree作成時にワークスペースごとのデフォルト設定を自動適用する、宣言的なタブ/ペインレイアウト | `rust` | 31 | 🔄 2026-08-15 |
| [**seshagy**](https://github.com/lmilojevicc/seshagy)<br><sub>lmilojevicc</sub> | tmuxとherdr向けのエージェント対応セッションマネージャー——プロジェクトを検出し、セッションを起動し、AIエージェントの作業を追跡する | `bubbletea` `go` `session-management` `session-manager` `terminal` | 13 | 🔄 2026-08-15 |
| [**herdr-muster**](https://github.com/marcoskichel/herdr-muster)<br><sub>marcoskichel</sub> | エージェントの状態を認識するherdr向けプロジェクト切り替えツール | `rust` | 4 | 2026-07-03 |
| [**herdr-layout-tools**](https://github.com/edouard-andrei/herdr-layout-tools)<br><sub>edouard-andrei</sub> | herdrプラグイン：レイアウトをその場で変形（main-left＋グリッド）したり均等化したりする——タブIDやペインIDは変わらず、プロセスも維持される | `javascript` | 3 | 🔄 2026-08-06 |
| [**herdr-pane-layouts**](https://github.com/iurysza/herdr-pane-layouts)<br><sub>iurysza</sub> | Herdr向けの、tmux風のシームレスなペインリサイズとレイアウト | `pane-layout` `python` `terminal` | 3 | 2026-07-17 |
| [**herdr-setup-bootstrap**](https://github.com/shizlie/herdr-setup-bootstrap)<br><sub>shizlie</sub> | worktree_init.tomlから新しいworktreeをブートストラップするHerdrプラグイン | `shell` | 3 | 2026-06-17 |
| [**🆕 herdr-tmux-layout**](https://github.com/crierr/herdr-tmux-layout)<br><sub>crierr</sub> | tmux-style preset layouts for live Herdr panes: cycle, even-horizontal, even-vertical, main-horizontal, main-vertical, tiled, and balance | `go` | 2 | 🔄 2026-08-14 |
| [**herdr-clone-layout**](https://github.com/danilolucasmd/herdr-clone-layout)<br><sub>danilolucasmd</sub> | 現在のワークスペースレイアウトを、新しいherdrのworktreeすべてに複製する。テンプレートも設定も不要——今いるレイアウトそのものがテンプレートになる | `shell` | 2 | 2026-08-01 |
| [**herdr-warp**](https://github.com/HexSleeves/herdr-warp)<br><sub>HexSleeves</sub> | Herdrのワークスペースを、ネイティブのWarpペインとして開く | `shell` | 2 | 2026-07-25 |
| [**herdr-compose**](https://github.com/ropali/herdr-compose)<br><sub>ropali</sub> | herdr-composeは、Herdr向けの宣言的なワークスペースレイアウトマネージャー | `layout-manager` `python` | 2 | 2026-07-25 |
| [**herdr-google-calendar**](https://github.com/Tomatio13/herdr-google-calendar)<br><sub>Tomatio13</sub> | herdr-gog-calendarは、ターミナルワークスペースツールherdr向けのGoogleカレンダー連携プラグイン | `shell` | 2 | 2026-07-22 |
| [**herdr-google-gmail**](https://github.com/Tomatio13/herdr-google-gmail)<br><sub>Tomatio13</sub> | herdr-google-gmailは、ターミナルワークスペースツールherdr向けのGmail連携プラグイン | `shell` | 2 | 2026-07-22 |
| [**herdr-layout**](https://github.com/3mmdrew/herdr-layout)<br><sub>3mmdrew</sub> | herdr向けのミニマルなワークスペースレイアウト定義——Luaファイルを渡すだけでワークスペースが立ち上がる。依存なし、デーモンなし、YAMLなし | `lua` `terminal` | 1 | 2026-08-04 |
| [**herdr-fork-from-message**](https://github.com/dmangla3/herdr-fork-from-message)<br><sub>dmangla3</sub> | 以前のメッセージの時点からCodexやClaude Codeをフォークし、新しいHerdrのタブ・ペイン・ワークスペースとして開く | `claude-code` `codex` `developer-tools` `terminal-multiplexer` `python` | 1 | 🔄 2026-08-10 |
| [**herdr-medieval**](https://github.com/gabrielbarretoo/herdr-medieval)<br><sub>gabrielbarretoo</sub> | ワークスペースとエージェントを、六角形マスの中世風大陸として3D表示するHerdrプラグイン——各ワークスペースは柵に囲まれた野営地、各ペインは冒険者として、エージェントの状態に応じて訓練したり、キャンプファイアで休んだり、塔で見張りをする。three.js組み込みで、通信・依存関係なし | `3d` `hex-grid` `threejs` `javascript` | 1 | 🔄 2026-08-06 |
| [**herdr-spinup**](https://github.com/Royal-lobster/herdr-spinup)<br><sub>Royal-lobster</sub> | herdrの新規タブごとに表示されるスタート画面——ツールを選ぶとそのタブで実行される。ツールはJSONで定義 | `javascript` | 1 | 2026-08-04 |
| [**reasonix-herdr**](https://github.com/uuie/reasonix-herdr)<br><sub>uuie</sub> | Herdr内でのライフサイクルのリアルタイム報告とワークスペース制御を行う、ネイティブなReasonixプラグイン | `reasonix` `python` | 1 | 2026-07-10 |
| [**ccc-herdr-layout**](https://github.com/caoer/ccc-herdr-layout)<br><sub>caoer</sub> | herdr向けのビジュアルレイアウトピッカー——1キーでライブプレビューしながら選べる | `go` | 0 | 2026-08-01 |
| [**herdr-yoke**](https://github.com/dgnsrekt/herdr-yoke)<br><sub>dgnsrekt</sub> | get yoked——1キーで2つのタブを並べて表示。herdr版のChromeスプリットビュー | `split-view` `terminal` `shell` | 0 | 🔄 2026-08-09 |
| [**herdr-plugin-dotfiles-dev-layout**](https://github.com/edmundmiller/herdr-plugin-dotfiles-dev-layout)<br><sub>edmundmiller</sub> | 自分のdotfilesの開発用ワークスペースレイアウトを開くためのHerdrプラグイン | `python` | 0 | 2026-06-23 |
| [**🆕 herdr-follow-cwd**](https://github.com/hasuwini77/herdr-follow-cwd)<br><sub>hasuwini77</sub> | herdrプラグイン：ワークスペースのラベルが、ペインが実際にいるディレクトリに追従する | `javascript` | 0 | 🔄 2026-08-13 |
| [**herdr-pane-id-metadata**](https://github.com/limars874/herdr-pane-id-metadata)<br><sub>limars874</sub> | 正規化されたペインIDと、コンパクトなタブ/ペインのサイドバーメタデータのための、最小構成のHerdrプラグイン | `coding-agents` `terminal` `javascript` | 0 | 🔄 2026-08-17 |
| [**🆕 herdr-prompts**](https://github.com/oppenheimor/herdr-prompts)<br><sub>oppenheimor</sub> | Save, search, fill, and reuse prompt templates across coding agents in Herdr. Inspired by my friend: bingguanqi | `typescript` | 0 | 🔄 2026-08-19 |
| [**herdr-lastfocus**](https://github.com/pedrobarco/herdr-lastfocus)<br><sub>pedrobarco</sub> | herdr向けの、tmux風の直前フォーカスしていたペイン/タブ/ワークスペースへの切り替え——フォーカスイベント履歴デーモンを介して実現 | `terminal-multiplexer` `tmux` `go` | 0 | 2026-07-25 |
| [**herdr-workspace-description**](https://github.com/rstacruz/herdr-workspace-description)<br><sub>rstacruz</sub> | _(説明なし)_ | `typescript` | 0 | 🔄 2026-08-08 |
| [**herdr-active-agent-jump**](https://github.com/shoaibkhanz/herdr-active-agent-jump)<br><sub>shoaibkhanz</sub> | herdrプラグイン：作業中/ブロック中のエージェントを、レイアウトの順序で前後に巡回してフォーカスする——attention-jumpを補完するvim風の操作 | `javascript` | 0 | 2026-07-12 |
| [**herdr-dev-layout**](https://github.com/simoncrypta/herdr-dev-layout)<br><sub>simoncrypta</sub> | Herdr向けの常時表示エージェントペイン | `herdr-integration` `shell` | 0 | 🔄 2026-08-17 |
| [**🆕 dsh-plugin-herdr**](https://github.com/sunny0826/dsh-plugin-herdr)<br><sub>sunny0826</sub> | Herdr control-plane plugin for DeepSeek Harness (DSH): observe and drive Herdr — a terminal workspace manager for AI coding agents — from DSH sessions | `dsh-plugin` `typescript` | 0 | 🔄 2026-08-20 |

<details><summary>この目的にも関係するもの</summary>

- [andrewchng/herdr-sessionizer](https://github.com/andrewchng/herdr-sessionizer) — プロジェクトやworktreeをファジー検索で開き、宣言的なTOMLレイアウト（タブ・ペイン分割・起動コマンド・リポジトリごとの上書き設定）からワークスペースを立ち上げる
- [fullerzz/herdr-plugin-sesh](https://github.com/fullerzz/herdr-plugin-sesh) — Herdr向けのSesh風ワークスペースピッカーTUI。zoxideと連携し、よく使うディレクトリからワークスペースを作成できる
- [ntindle/herdr-resurrect](https://github.com/ntindle/herdr-resurrect) — herdr版tmux-resurrect——ワークスペース・タブ・ペイン・作業ディレクトリ・実行中のプログラムやエージェントをスナップショットし、クラッシュや再起動後に復元する
- [aliou/herdr-cast](https://github.com/aliou/herdr-cast) — 個人用Herdrプラグイン——ネイティブmacOS通知、ファジーなワークスペース移動、zoxide連携のワークスペース作成、レイアウトコマンドをまとめて提供
- [enekos/herdr-quick-actions](https://github.com/enekos/herdr-quick-actions) — herdr標準のタブ/ペイン/ワークスペース操作を、使用頻度順でfzfから選べる——キーバインドを覚える必要がなくなる
- [salkhalil/herdr-sessionizer](https://github.com/salkhalil/herdr-sessionizer) — herdr版tmux-sessionizer：開いているワークスペースとzoxideのディレクトリをfzfで検索し、テンプレートタブ付きで作成またはフォーカスする
- [chandrasekharan98/herdr-workspace-save](https://github.com/chandrasekharan98/herdr-workspace-save) — Save a Herdr workspace — layout, cwds, agent sessions, running commands — and reopen it later from an fzf pic…
- [asermax/herdr-suspend-workspace](https://github.com/asermax/herdr-suspend-workspace) — herdrのワークスペースをサスペンド——レイアウトとエージェントをスナップショットして閉じ、あとでポップアップから選んで復元できる
- [willfish/herdr-workspacex](https://github.com/willfish/herdr-workspacex) — Rustネイティブのファジー検索型Herdrワークスペース切り替えツール——zoxideを利用したワークスペース作成に対応

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-navigate"></a>

## ペイン移動・キー操作

> ペインやワークスペース間の移動・リサイズを、エディタと同じキーで済ませたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**vim-herdr-navigation**](https://github.com/paulbkim-dev/vim-herdr-navigation)<br><sub>paulbkim-dev</sub> | Ctrl+h/j/k/lでherdrのペインとVim/Neovimのスプリットをシームレスに移動——vim-tmux-navigatorのherdr版 | `neovim` `vim` `shell` | 90 | 2026-08-02 |
| [**herdr-splits.nvim**](https://github.com/lmilojevicc/herdr-splits.nvim)<br><sub>lmilojevicc</sub> | HerdrとNeovimのスプリットをスマートに移動・リサイズする | `lua` `neovim` `neovim-plugin` `neovim-plugins` `nvim` | 49 | 🔄 2026-08-17 |
| [**herdr-floax**](https://github.com/Tyru5/herdr-floax)<br><sub>Tyru5</sub> | herdr向けのフローティング作業用シェル——tmux-floax風に開閉できるポップアップで、ワークスペースごとに1つ、セッションは永続化される | `rust` `terminal` `tmux-floax` | 22 | 2026-07-26 |
| [**herdr-nvim-nav**](https://github.com/aimdevlee/herdr-nvim-nav)<br><sub>aimdevlee</sub> | herdrのペインとNeovimのスプリットをまたいだシームレスなCtrl+h/j/k/l移動——ソケットベースでキー入力ごとのプロセス起動なし | `neovim` `neovim-plugin` `lua` | 17 | 2026-08-02 |
| [**herdr-last-workspace**](https://github.com/third774/herdr-last-workspace)<br><sub>third774</sub> | 直前にフォーカスしていたワークスペースに切り替えるプラグイン | `rust` | 15 | 2026-06-22 |
| [**herdr-recent-navigator**](https://github.com/beyondlex/herdr-recent-navigator)<br><sub>beyondlex</sub> | Herdr向けの、最近使ったワークスペース/タブ/ペインの切り替えツール。最近フォーカスしたワークスペース・タブ・ペイン・AIエージェントの一覧をポップアップ表示し、ファジー検索とキーボード操作に対応 | `agent` `mru` `navigator` `pane` `popup` | 10 | 2026-07-28 |
| [**herdr-logbook**](https://github.com/Resetnak/herdr-logbook)<br><sub>Resetnak</sub> | ターミナルのための作業メモリ——オフラインでMarkdown中心のノート、決定事項、Herdr向けの現在タスクnow.mdを管理 | `adr` `bubbletea` `cli` `go` `markdown` | 9 | 🔄 2026-08-19 |
| [**herdr-pane-mover**](https://github.com/osamahbeig/herdr-pane-mover)<br><sub>osamahbeig</sub> | herdr向けのクリック可能なオーバーレイメニュー：タブやワークスペースを横断してペインの移動・再分割・入れ替えができる | `terminal` `tui` `javascript` | 8 | 2026-07-10 |
| [**herdr-command-center**](https://github.com/speardragon/herdr-command-center)<br><sub>speardragon</sub> | すべてのコマンドを1つのキーバインドで——登録したコマンドを一覧表示するherdrのポップアップ。矢印キーや番号で実行し、コマンド実行前に自動で閉じる | `command-palette` `nodejs` `terminal` `toml` `tui` | 7 | 🔄 2026-08-19 |
| [**🆕 herdr-trail**](https://github.com/catoncat/herdr-trail)<br><sub>catoncat</sub> | Herd-wide shared memos for herdr: agents jot follow-ups, humans manage one global list, every entry jumps back to its source conversation | `javascript` | 6 | 🔄 2026-08-18 |
| [**herdr-toggle-popup**](https://github.com/maro114510/herdr-toggle-popup)<br><sub>maro114510</sub> | 1つのキーバインドでオーバーレイのポップアップシェルを開閉できるHerdrターミナル向けプラグイン | `go` | 6 | 🔄 2026-08-12 |
| [**nvim-herdr-navigator**](https://github.com/kaar/nvim-herdr-navigator)<br><sub>kaar</sub> | Neovimのスプリットとherdrのペインをシームレスに移動——1組の`ctrl+h/j/k/l`でvimとherdrのペインの両方を移動できる | `neovim` `neovim-plugin` `lua` | 5 | 2026-07-29 |
| [**herdr-scratch**](https://github.com/AkashJana18/herdr-scratch)<br><sub>AkashJana18</sub> | Herdr向けの永続化されたスクラッチパッド。フローティングのユーティリティペインへの足がかりとなる | `cli` `rust` `scratchpad` | 4 | 🔄 2026-08-07 |
| [**nvim-herdr-navigation**](https://github.com/bojackduy/nvim-herdr-navigation)<br><sub>bojackduy</sub> | vim-tmux-navigator風のctrl+h/j/k/lで、Neovimのスプリットとherdrのペイン間を移動する | `keyboard-shortcuts` `lazyvim` `lua` `navigation` `neovim` | 4 | 2026-07-20 |
| [**herdr-omnisearch**](https://github.com/dmnkf/herdr-omnisearch)<br><sub>dmnkf</sub> | Herdrのワークスペース・ペイン・アーカイブ済みエージェントセッションを高速にローカル検索・移動する | `python` | 4 | 🔄 2026-08-12 |
| [**herdr-annotations**](https://github.com/jagzmz/herdr-annotations)<br><sub>jagzmz</sub> | Herdr上で選択したターミナルのテキストに、高速なローカルファーストのポップアップと再利用可能なコレクションで注釈を付ける | `annotations` `cli` `coding-agents` `developer-tools` `local-first` | 4 | 2026-07-16 |
| [**herdr-harpoon**](https://github.com/KonstantinKai/herdr-harpoon)<br><sub>KonstantinKai</sub> | herdr版Harpoon：ペインにマークを付けてインデックスでジャンプする。Bashのみでビルド不要 | `bash` `harpoon` `tmux-harpoon` `shell` | 4 | 2026-07-29 |
| [**herdr-equalize-splits**](https://github.com/markhuot/herdr-equalize-splits)<br><sub>markhuot</sub> | herdrプラグイン：現在のタブ内のすべてのスプリットを、行/列ごとに均等な幅に揃える（Ctrl+b =にバインド） | `terminal` `tmux` `javascript` | 4 | 2026-07-08 |
| [**🆕 herdr-paddock**](https://github.com/neyham/herdr-paddock)<br><sub>neyham</sub> | 🐑 A card-wall feed for your herdr agents — glance over the flock, zoom into one, reply, all over plain SSH | `bubbletea` `go` `ssh` `tui` | 4 | 🔄 2026-08-17 |
| [**🆕 herdr-swipe**](https://github.com/husniadil/herdr-swipe)<br><sub>husniadil</sub> | Trackpad gestures for Herdr: move between panes, tabs and spaces, and jump to the agent waiting on you | `cgeventtap` `gestures` `macos` `python` `terminal` | 3 | 🔄 2026-08-18 |
| [**herdr-unread-marker**](https://github.com/JoanGil/herdr-unread-marker)<br><sub>JoanGil</sub> | キーバインドでフォーカス中のエージェントを未読/既読にマークする（手動のみ） | `shell` | 3 | 2026-07-17 |
| [**herdr-last**](https://github.com/lmilojevicc/herdr-last)<br><sub>lmilojevicc</sub> | Herdrで直前にアクティブだったワークスペースまたはタブに切り替え戻す | `go` `linux` `macos` `productivity` `tabs` | 3 | 🔄 2026-08-07 |
| [**herdr-attention**](https://github.com/milkyskies/herdr-attention)<br><sub>milkyskies</sub> | herdrプラグイン：1キーで、注意が必要な次のエージェント（ブロック中、次に完了済み）にフォーカスを移す | `javascript` | 3 | 2026-07-08 |
| [**herdr-navigator**](https://github.com/willfish/herdr-navigator)<br><sub>willfish</sub> | Vim/Neovimを意識したペイン移動のための、Herdr側のナビゲーション操作 | `navigation` `neovim` `rust` | 3 | 2026-07-07 |
| [**herdr-equalize-vsplit**](https://github.com/devoc09/herdr-equalize-vsplit)<br><sub>devoc09</sub> | 現在のペインを右に分割し、列の幅を均等にするHerdrプラグイン | `go` | 2 | 2026-07-15 |
| [**herdr-convo-index**](https://github.com/dzwduan/herdr-convo-index)<br><sub>dzwduan</sub> | herdr内のClaude Codeペイン用のターン索引——過去の任意のターンにジャンプしてポップアップで読める | `python` | 2 | 2026-07-27 |
| [**herdr-popupx**](https://github.com/jeromychu23/herdr-popupx)<br><sub>jeromychu23</sub> | Herdr向けの、永続化されたネイティブのフローティング作業用ポップアップ | `rust` `terminal` `tui` | 2 | 2026-07-21 |
| [**🆕 herdr-prevtab**](https://github.com/joo-was-already-taken/herdr-prevtab)<br><sub>joo-was-already-taken</sub> | Herdr plugin for switching to the previously focused tab | `rust` | 2 | 🔄 2026-08-18 |
| [**🆕 herdr-prompt-library**](https://github.com/jwkicklighter/herdr-prompt-library)<br><sub>jwkicklighter</sub> | A Herdr plugin for browsing, managing, and inserting reusable local or global Markdown prompts into the focused pane. | `go` `golang` `prompting` `snippets` `tui` | 2 | 🔄 2026-08-14 |
| [**herdr-lazytask**](https://github.com/mdetweil/herdr-lazytask)<br><sub>mdetweil</sub> | herdrのスプリットペインでLazytaskを使う（開く/フォーカス/トグル）ほか、Taskwarriorのクイックアクションも提供 | `lazytask` `taskwarrior` `terminal` `rust` | 2 | 2026-08-02 |
| [**herdr-float**](https://github.com/meerzulee/herdr-float)<br><sub>meerzulee</sub> | Zellij風のALT+Fで開くフローティングペイン | `shell` | 2 | 2026-07-20 |
| [**herdr-confirm-close-pane**](https://github.com/poweroutlet2/herdr-confirm-close-pane)<br><sub>poweroutlet2</sub> | ペインを閉じる前に確認を求めるherdrプラグイン——tmuxのprefix+xのconfirm-beforeのような動作 | `shell` | 2 | 2026-07-06 |
| [**herdr-pretty-which**](https://github.com/ramarivera/herdr-pretty-which)<br><sub>ramarivera</sub> | Herdr向けの、Rust/Ratatui製which-key風キーバインドオーバーレイ | `ratatui` `rust` `terminal` `tui` `which-key` | 2 | 🔄 2026-08-14 |
| [**herdr-ask-inbox**](https://github.com/speardragon/herdr-ask-inbox)<br><sub>speardragon</sub> | すべてのherdrワークスペースからブロックされたClaudeのAskUserQuestionプロンプトを1つのポップアップに集約し、その場で回答できる。間違ったエージェントに回答を送ってしまう心配もない | `claude-code` `javascript` | 2 | 2026-07-25 |
| [**herdr-unread-jump**](https://github.com/to4iki/herdr-unread-jump)<br><sub>to4iki</sub> | 注意が必要な次のHerdrエージェントペイン（ブロック中、次に完了済み）にジャンプする | `agents` `bash` `shell` | 2 | 2026-07-22 |
| [**herdr-voice**](https://github.com/aneym/herdr-voice)<br><sub>aneym</sub> | herdrの音声操作——話しかけるだけでスペース作成・ペイン分割・コーディングエージェントの操作ができる。OpenAI Realtimeを使用し、リアルタイムの文字起こしを表示するフローティングHUD付き | `openai-realtime-api` `voice` `javascript` | 1 | 2026-08-01 |
| [**herdr-plugin-tiles**](https://github.com/carsonjones/herdr-plugin-tiles)<br><sub>carsonjones</sub> | herdr向けのシンプルなペインマネージャー | `python` | 1 | 2026-06-19 |
| [**🆕 herdr-cliamp**](https://github.com/coryshaw1/herdr-cliamp)<br><sub>coryshaw1</sub> | Floating cliamp for herdr that keeps playing when hidden: the player lives in a detached herdr session, so closing the float only detaches. | `audiobook` `cliamp` `music-player` `podcast` `terminal` | 1 | 🔄 2026-08-19 |
| [**herdr-notes**](https://github.com/cyperx84/herdr-notes)<br><sub>cyperx84</sub> | Herdr向けの、ワークスペースごとに独立したMarkdownスクラッチノート。Go製 | `bubbletea` `golang` `markdown` `notes` `go` | 1 | 🔄 2026-08-16 |
| [**herdr-last-tab**](https://github.com/dantehemerson/herdr-last-tab)<br><sub>dantehemerson</sub> | 直前にフォーカスしていたタブに切り替えるプラグイン | `rust` | 1 | 🔄 2026-08-12 |
| [**herdr-easymotion**](https://github.com/elliotekj/herdr-easymotion)<br><sub>elliotekj</sub> | 🦘 Herdrのペイン間を直接ジャンプする | `javascript` | 1 | 2026-07-20 |
| [**herdr-break-pane**](https://github.com/iuhoay/herdr-break-pane)<br><sub>iuhoay</sub> | フォーカス中のペインを新しいタブに移動する、小さなHerdrプラグイン | `pane` `javascript` | 1 | 2026-07-27 |
| [**herdr-nav-history**](https://github.com/jugyo/herdr-nav-history)<br><sub>jugyo</sub> | herdr向けの、ブラウザ風の戻る/進むナビゲーション（ペイン・タブ・ワークスペースのフォーカス履歴を対象） | `javascript` | 1 | 2026-07-12 |
| [**herdr-plugin-last**](https://github.com/m4salah/herdr-plugin-last)<br><sub>m4salah</sub> | tmux風の直前タブ・直前ワークスペースへの移動をHerdrに追加する | `rust` | 1 | 2026-07-30 |
| [**herdr-next-agent**](https://github.com/martin-ro/herdr-next-agent)<br><sub>martin-ro</sub> | Herdrプラグイン：設定可能な優先度に基づいて、注意が必要な次のエージェントにジャンプする | `python` | 1 | 2026-07-15 |
| [**herdr-quotr**](https://github.com/napalmpapalam/herdr-quotr)<br><sub>napalmpapalam</sub> | herdrのポップアップから、エージェント自身の回答を引用してそのエージェントに投げ返す | `claude-code` `rust` `tui` | 1 | 🔄 2026-08-11 |
| [**herdr-smartnav**](https://github.com/retroaalto/herdr-smartnav)<br><sub>retroaalto</sub> | 方向を意識したペインナビゲーションを提供するHerdrプラグイン | `go` | 1 | 2026-08-01 |
| [**herdr-edge-nav**](https://github.com/sebcbi1/herdr-edge-nav)<br><sub>sebcbi1</sub> | ペインの端でタブやワークスペースをまたいで移動・リサイズできる、方向指定型のHerdrプラグイン。Neovimのスプリットもシームレスに認識する | `lua` | 1 | 🔄 2026-08-12 |
| [**🆕 herdr-pane-orientation-switcher**](https://github.com/sf1tzp/herdr-pane-orientation-switcher)<br><sub>sf1tzp</sub> | Workflow Ergonomics for Split Panes in Herdr | `shell` | 1 | 2026-07-25 |
| [**herdr-ferry**](https://github.com/shadowfax92/herdr-ferry)<br><sub>shadowfax92</sub> | A native Rust popup for multi-moving live Herdr panes and tabs or merging workspaces. | `productivity` `rust` `terminal` `tui` | 1 | 🔄 2026-08-19 |
| [**herdr-scratch**](https://github.com/shadowfax92/herdr-scratch)<br><sub>shadowfax92</sub> | 非公開のtmuxセッションを裏側で使う、永続化されたペインごとのHerdrスクラッチポップアップ | `neovim` `productivity` `rust` `terminal` `tmux` | 1 | 2026-08-04 |
| [**herdr-talon**](https://github.com/shadowfax92/herdr-talon)<br><sub>shadowfax92</sub> | 画面に見えているHerdrのターミナル要素に、空間的なキーボードヒントを表示する | `keyboard-navigation` `productivity` `rust` `terminal` `tmux-fingers` | 1 | 🔄 2026-08-20 |
| [**herdr-nav-plus**](https://github.com/shoaibkhanz/herdr-nav-plus)<br><sub>shoaibkhanz</sub> | Ctrl+h/j/k/lでherdrのペインを越えてワークスペースまで移動できるナビゲーション——vimを意識した動作で、両端でループする | `javascript` | 1 | 2026-07-18 |
| [**herdr-hintr**](https://github.com/wraithyy/herdr-hintr)<br><sub>wraithyy</sub> | herdrプラグイン：which-key風のキーバインド・チートシートをポップアップ表示——キーを押すとそのまま実行できる | `shell` | 1 | 🔄 2026-08-11 |
| [**herdr-layout-cycle**](https://github.com/amiramay/herdr-layout-cycle)<br><sub>amiramay</sub> | herdrプラグイン：あらかじめ用意したペインレイアウトを順番に切り替える。tmuxのprefix+space風 | `javascript` | 0 | 🔄 2026-08-08 |
| [**gotopr**](https://github.com/asumaran/gotopr)<br><sub>asumaran</sub> | ローカルのリポジトリとworktreeを横断して、開いているGitHub PRにジャンプするHerdrプラグイン | `go` | 0 | 🔄 2026-08-06 |
| [**🆕 herdr-confirm-close**](https://github.com/asumaran/herdr-confirm-close)<br><sub>asumaran</sub> | Herdr plugin: close the focused pane, asking first only when a process is running in it | `terminal` `go` | 0 | 🔄 2026-08-17 |
| [**🆕 Renderd**](https://github.com/Brutheron/Renderd)<br><sub>Brutheron</sub> | Live Markdown reader for completed Claude Code and Codex responses in Herdr | `go` | 0 | 🔄 2026-08-15 |
| [**herdr-auto-focus**](https://github.com/calorie/herdr-auto-focus)<br><sub>calorie</sub> | macOSの入力がアイドルになったら、注意が必要なHerdrのエージェントに自動でフォーカスする | `golang` `macos` `go` | 0 | 2026-07-27 |
| [**herdr-which-key**](https://github.com/CowboyVang/herdr-which-key)<br><sub>CowboyVang</sub> | herdr向けのwhich-key風キーマップオーバーレイ——1キー押すとprefix配下の全バインドがグループ化・ラベル付きで表示され、2つ目のキーで実行できる。長押し表示ではなく明示的な呼び出し方式。依存なし | `keybindings` `terminal` `which-key` `python` | 0 | 2026-08-02 |
| [**herdr-plugin-agents-usage**](https://github.com/gecm0/herdr-plugin-agents-usage)<br><sub>gecm0</sub> | 各プロバイダーの使用状況（Claude、Codex、OpenCode Go、Neuralwatt）をHerdrのモーダルポップアップに表示する | `claude` `codex` `opencode` `terminal` `usage` | 0 | 2026-07-26 |
| [**herdr-harpoon**](https://github.com/hadeson/herdr-harpoon)<br><sub>hadeson</sub> | herdr向けのHarpoon風ペインマーク：ペインをスロット1〜9にピン留めし、タブやワークスペースを越えて直接ジャンプできる | `harpoon` `pane-navigation` `terminal` `tmux` `python` | 0 | 2026-07-25 |
| [**herdr-counting-sheep**](https://github.com/inonprince/herdr-counting-sheep)<br><sub>inonprince</sub> | HerdrのSpaceとAgentをライブに一覧表示——直前のタブ・Space・Agentへジャンプするショートカット付き | `productivity` `terminal` `javascript` | 0 | 2026-08-03 |
| [**herdr-matter-wall**](https://github.com/Javamomma/herdr-matter-wall)<br><sub>Javamomma</sub> | herdrプラグイン：プロジェクト内で最も活発なサブディレクトリを、読み取り専用のAIステータスカードのライブウォールとしてタイル表示する | `claude-code` `shell` | 0 | 2026-07-14 |
| [**herdr-nav**](https://github.com/jmarcelomb/herdr-nav)<br><sub>jmarcelomb</sub> | herdr向けのペイン・タブ・ワークスペース間ナビゲーションプラグイン | `rust` | 0 | 2026-07-30 |
| [**herdr-hasr**](https://github.com/KazBrekker1/herdr-hasr)<br><sub>KazBrekker1</sub> | Hasr（حصر — 「列挙・完全な集計」の意）——herdr向けのgoto風ポップアップ切り替えツール：エージェント・タブ・スペースの切り替え・リネーム・削除・作成ができ、完了状況もリアルタイムに追跡する | `tui` `go` | 0 | 2026-07-23 |
| [**herdr-cmd-marks**](https://github.com/leonho/herdr-cmd-marks)<br><sub>leonho</sub> | herdrプラグイン：プロジェクトごとのコマンドブックマークをポップアップ表示。エージェントが作業中でも、別のシェルでブックマーク済みのコマンドを実行できる（グローバル・プロジェクト・スマートセクションに対応） | `shell` | 0 | 2026-07-18 |
| [**herdr-pane-balancer**](https://github.com/malone-c/herdr-pane-balancer)<br><sub>malone-c</sub> | ペインの開閉に合わせて、herdrのペインを常に均等なサイズに保つ。スプリットするとフォーカス中のペインが半分になるが、このプラグインがタブ全体を再調整する | `python` | 0 | 🔄 2026-08-07 |
| [**herdr-focus-or-tab**](https://github.com/mholtzscher/herdr-focus-or-tab)<br><sub>mholtzscher</sub> | タブの境界をまたいでHerdrのペインを順に切り替える | `terminal-multiplexer` `rust` | 0 | 2026-07-31 |
| [**herdr-touchbar**](https://github.com/omerturhan/herdr-touchbar)<br><sub>omerturhan</sub> | MacBookのTouch Barに作業中・ブロック中のherdrエージェントを表示——タップすると該当タブに直接移動する | `ai-agents` `macos` `touchbar` `swift` | 0 | 2026-07-30 |
| [**herdr-plugins**](https://github.com/oullin/herdr-plugins)<br><sub>oullin</sub> | Herdr向けの、それぞれ独立してインストールできる、目的に特化したプラグイン集 | `typescript` | 0 | 🔄 2026-08-09 |
| [**herdr-focused-codex-fork**](https://github.com/potatoQi/herdr-focused-codex-fork)<br><sub>potatoQi</sub> | フォーカス中のHerdrペインのCodexセッションを、右側のペインにフォークする | `shell` | 0 | 🔄 2026-08-09 |
| [**herdr-whichkey**](https://github.com/Qu4tro/herdr-whichkey)<br><sub>Qu4tro</sub> | herdr向けの、blezz/which-key風のアクションメニュー——トリガーキーを押すだけで、あとは1アクション1キー操作。入力もEnterも不要 | `rust` | 0 | 2026-07-22 |
| [**herdr-deck-navigation**](https://github.com/raghu-nandan-bs/herdr-deck-navigation)<br><sub>raghu-nandan-bs</sub> | herdr標準のフラットなワークスペース/タブ/ペインナビゲーターを、スクロールなしで任意のペインに素早くたどり着ける「デッキ」表示に置き換える | `rust` `terminal` `tui` | 0 | 2026-07-21 |
| [**🆕 herdr-atuin-plugin**](https://github.com/smanickam01/herdr-atuin-plugin)<br><sub>smanickam01</sub> | Atuin shell history search in a herdr popup — press prefix+a, Enter to run or Tab to edit. Binds itself on install. | `atuin` `macos` `shell-history` `terminal` `zsh` | 0 | 🔄 2026-08-17 |
| [**🆕 herdr-confirm-close**](https://github.com/tajdien/herdr-confirm-close)<br><sub>tajdien</sub> | herdrプラグイン：ペインやタブを閉じる前に確認ポップアップを出す | `shell` | 0 | 🔄 2026-08-13 |
| [**🆕 herdr-jump**](https://github.com/tp6gw94/herdr-jump)<br><sub>tp6gw94</sub> | Keyboard navigation for Herdr workspaces, tabs, panes, and agents. | `javascript` | 0 | 🔄 2026-08-16 |
| [**herdr-focus**](https://github.com/trapple/herdr-focus)<br><sub>trapple</sub> | 次にブロック中/完了したエージェントペインにフォーカスし、ターミナルアプリを最前面に出す。グローバルホットキー付き | `shell` | 0 | 2026-07-19 |
| [**🆕 herdr-translate**](https://github.com/wenPKtalk/herdr-translate)<br><sub>wenPKtalk</sub> | Herdr plugin: translate the selected text in a pane with translate-shell, shown in a floating popup (macOS and Linux) | `translate` `shell` | 0 | 🔄 2026-08-19 |
| [**herdr-balance-panes**](https://github.com/willfish/herdr-balance-panes)<br><sub>willfish</sub> | 現在のHerdrタブ内のペインを均等な大きさに揃える（tmuxのselect-layout -E相当） | `rust` `terminal` `tmux` | 0 | 🔄 2026-08-05 |
| [**herdr-compass**](https://github.com/ycros/herdr-compass)<br><sub>ycros</sub> | Herdrのペイン・タブ・ワークスペースを横断する、統一された方向キーナビゲーション | `python` | 0 | 🔄 2026-08-07 |
| [**🆕 herdr-kakoune-popup**](https://github.com/Yukaii/herdr-kakoune-popup)<br><sub>Yukaii</sub> | Run Kakoune terminal commands in native Herdr popups. | `kakoune` `shell` | 0 | 🔄 2026-08-20 |

<details><summary>この目的にも関係するもの</summary>

- [thanhdat77/herdr-navigator](https://github.com/thanhdat77/herdr-navigator) — 1つのファジーナビゲーターから、任意のHerdrのワークスペース・エージェント・プロジェクト・セッション・リモート・ディレクトリ・アクションにジャンプできる
- [qu8n/herdr-automatic-rename](https://github.com/qu8n/herdr-automatic-rename) — herdrのタブをtmux風に自動リネームし、スペース/タブ/エージェントに1〜9のジャンプキー番号を付ける
- [speardragon/herdr-plugin-manager](https://github.com/speardragon/herdr-plugin-manager) — ポップアップからherdrのプラグインを管理——インストール・更新・有効/無効化・アンインストール、herdr-pluginマーケットプレイスの閲覧も可能。推奨キー：prefix+p
- [jorge07RD/herdr-ssh-manager](https://github.com/jorge07RD/herdr-ssh-manager) — Save SSH hosts and reconnect from a fuzzy popup inside Herdr — Enter hands the popup straight to ssh.
- [bayoudhi/herdr-prayer-times](https://github.com/bayoudhi/herdr-prayer-times) — Next Islamic prayer and countdown in the Herdr sidebar, with a timetable popup and notifications
- [black-atom-industries/helm.herdr](https://github.com/black-atom-industries/helm.herdr) — 1つのファジーナビゲーターから、任意のHerdrのワークスペース・エージェント・プロジェクト・セッション・リモート・ディレクトリ・アクションにジャンプできる
- [Joxtacy/herdr-plugin-vault](https://github.com/Joxtacy/herdr-plugin-vault) — herdrのポップアップから過去のClaude Codeセッションを閲覧し、選んだものを新しいタブで再開する
- [leonho/herdr-idle-panes](https://github.com/leonho/herdr-idle-panes) — herdrプラグイン：アイドル状態のシェルのままになっているペインを確認して閉じる、チェックリスト形式のポップアップ
- [ram4-dev/herdr-notify-center](https://github.com/ram4-dev/herdr-notify-center) — サーバー全体のエージェント通知を、永続化されたポップアップ受信箱でHerdrに提供する
- [shoaibkhanz/herdr-active-agent-jump](https://github.com/shoaibkhanz/herdr-active-agent-jump) — herdrプラグイン：作業中/ブロック中のエージェントを、レイアウトの順序で前後に巡回してフォーカスする——attention-jumpを補完するvim風の操作
- [vgreg/herdr-padio](https://github.com/vgreg/herdr-padio) — herdrでフォーカスされているペインのアプリに応じて、PadIOコントローラーのモードを自動切り替えする
- [victor-software-house/herdr-stash](https://github.com/victor-software-house/herdr-stash) — Herdrのワークスペースをスタッシュ——エージェントを停止しつつ構成と会話内容は保持し、あとでクリック可能な2カラムポップアップから復元できる

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-files"></a>

## ファイル閲覧・エディタ連携

> ペインの中でファイルツリーを開いたり、エディタ側と状態を揃えたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-file-viewer**](https://github.com/smarzban/herdr-file-viewer)<br><sub>smarzban</sub> | herdr向けのGit対応・読み取り専用ファイルビューア。マウス操作にも対応したキーボード駆動のTUIで、ツリー+コンテンツペインに差分表示・Markdownレンダリング・シンタックスハイライトを提供 | `file-viewer` `git` `ratatui` `rust` `terminal` | 444 | 🔄 2026-08-15 |
| [**herdr-mirror**](https://github.com/nikok6/herdr-mirror)<br><sub>nikok6</sub> | ローカルとリモートのセッションを1つのウィンドウに統合。リモートのherdrサーバーをローカルのサイドバーにミラーしてSSH経由で操作 | `rust` | 153 | 🔄 2026-08-15 |
| [**herdr-sidebar**](https://github.com/alexarthurs/herdr-sidebar)<br><sub>alexarthurs</sub> | herdr向けのVS Code風サイドバー：ファイルエクスプローラーとGitのソース管理を1つのペインに統合——シンタックスハイライト付きプレビュー、VS Code風の差分表示、GitLens風の詳細パネル、AIによるコミットメッセージ生成 | `git` `ratatui` `rust` `sidebar` `terminal` | 133 | 🔄 2026-08-15 |
| [**dotfiles**](https://github.com/edmundmiller/dotfiles)<br><sub>edmundmiller</sub> | 自分のdotfilesを常に最新の状態に保つためのもの | `dotfiles` `emacs` `nix-dotfiles` `nixos` `nixos-configuration` | 78 | 🔄 2026-08-20 |
| [**herdr-nvim**](https://github.com/ChmaraX/herdr-nvim)<br><sub>ChmaraX</sub> | Neovimをherdrのワークスペースに完全統合する | `lua` `neovim` `nvim` `nvim-plugin` `rust` | 32 | 🔄 2026-08-13 |
| [**herdr-lazygit**](https://github.com/Crokily/herdr-lazygit)<br><sub>Crokily</sub> | herdrのサイドバーペインでlazygitを実行し、AIによるコミットメッセージ生成にも対応——開くのも、展開するのも、コミットするのも、それぞれ1キーで | `git` `lazygit` `shell` | 19 | 2026-07-17 |
| [**herdr-yazi**](https://github.com/speardragon/herdr-yazi)<br><sub>speardragon</sub> | herdrのペイン内でYaziを開く | `shell` | 17 | 🔄 2026-08-19 |
| [**herdr-git-status**](https://github.com/ezcorp-org/herdr-git-status)<br><sub>ezcorp-org</sub> | herdrプラグイン：スペースごとのgitワーキングツリーの状態（ステージ済み/変更/未追跡/競合）をブランチ名の隣にサイドバー表示する | `rust` | 9 | 🔄 2026-08-10 |
| [**herdr-quicklook**](https://github.com/dwarvesf/herdr-quicklook)<br><sub>dwarvesf</sub> | herdr版Quick Look：クリップボード内のパスをオーバーレイでポップアップ表示し、1キーでファイルビューアに切り替えられる | `terminal` `shell` | 8 | 2026-07-27 |
| [**herdr-context.nvim**](https://github.com/makyinmars/herdr-context.nvim)<br><sub>makyinmars</sub> | Neovimからコードを選択またはカーソルを合わせ、稼働中のHerdrエージェントを選んで、構造化されたコンテキストをそのエージェントのプロンプトに（送信せずに）積み込む | `lua` | 7 | 🔄 2026-08-08 |
| [**herdr-flist**](https://github.com/devskale/herdr-flist)<br><sub>devskale</sub> | herdr向けのファイル一覧プラグイン | `python` | 5 | 2026-07-10 |
| [**herdr-workbench**](https://github.com/azizuysal/herdr-workbench)<br><sub>azizuysal</sub> | Herdr向けの洗練されたプロジェクトサイドバー——エクスプローラー、ファイル/コンテンツのリアルタイム検索、読み取り専用のソース管理、豊富なプレビュー、ファイルアイコン、Git装飾を備える | `rust` | 4 | 🔄 2026-08-07 |
| [**herdr-file-viewer**](https://github.com/ismaelosuna7824/herdr-file-viewer)<br><sub>ismaelosuna7824</sub> | 1つのHerdrペインに収まる、キーボード操作のファイルエクスプローラー・コードビューア・gitクライアント——Go + Bubble Tea製 | `bubbletea` `git` `golang` `tui` `go` | 4 | 🔄 2026-08-08 |
| [**herdr-markdown-viewer**](https://github.com/arvindparmar-me/herdr-markdown-viewer)<br><sub>arvindparmar-me</sub> | Herdrプラグイン：Markdownファイルのパスをドラッグ選択してprefix+mを押すと、右側のスプリットペインでプレビューできる | `shell` | 3 | 2026-07-17 |
| [**herdr-wait**](https://github.com/cdc-lst/herdr-wait)<br><sub>cdc-lst</sub> | アイドル状態のエージェントペインに、実際に何をしているか（例：'waiting: build-api'、'waiting: codex'）をペインのプロセスツリーから判定してタグ付けする、設定可能なherdrプラグイン | `typescript` | 3 | 2026-07-03 |
| [**🆕 herdr-opentab**](https://github.com/hamidi-dev/herdr-opentab)<br><sub>hamidi-dev</sub> | Live per-agent AI spend from OpenTab in the Herdr sidebar. | `ai-agents` `opentab` `terminal` `python` | 3 | 🔄 2026-08-18 |
| [**herdr-lazygit**](https://github.com/JacquesvanWyk/herdr-lazygit)<br><sub>JacquesvanWyk</sub> | herdrのスプリットペインまたはタブでlazygitを開く。スマートトグル（開く/フォーカス/閉じる）に対応 | `lazygit` `shell` | 3 | 2026-07-12 |
| [**advanced-herdr-file-viewer**](https://github.com/thuanlm215/advanced-herdr-file-viewer)<br><sub>thuanlm215</sub> | herdr向けの高機能・Git対応ファイルビューア——高速なファイル名/全文検索、豊富なUnicodeアイコン、独立スクロールするツリー、コンテキストアクション、Git差分表示、Markdownレンダリング、シンタックスハイライトに対応。マウス操作にも対応したキーボード駆動 | `rust` | 3 | 🔄 2026-08-19 |
| [**herdr-claude-usage-multi**](https://github.com/iamhouser/herdr-claude-usage-multi)<br><sub>iamhouser</sub> | Herdrのサイドバーに表示するClaudeプランの使用状況ゲージ——セッション/週の％、危険度に応じた色変化、リセットまでのカウントダウン、CLAUDE_CONFIG_DIRプロファイルによる複数アカウント対応 | `claude-code` `python` | 2 | 2026-07-25 |
| [**herdr-file-viewer**](https://github.com/jomarmontuya/herdr-file-viewer)<br><sub>jomarmontuya</sub> | 右側に表示するHerdrのファイルツリープラグイン——ファイルタブ、作業ディレクトリの追従、git装飾、クリック可能なリンクに対応 | `go` | 2 | 2026-07-13 |
| [**herdr-yazi-windows**](https://github.com/Only-Moon/herdr-yazi-windows)<br><sub>Only-Moon</sub> | herdr-yazi のWindows移植版。herdr v0.8以降のネイティブWindowsペイン生成に対応 | `file` `file-manager` `pidotdev` `python` `tui` | 2 | 🔄 2026-08-14 |
| [**herdr-fresh**](https://github.com/rvalledorjr/herdr-fresh)<br><sub>rvalledorjr</sub> | ターミナルIDEのFreshを、herdrのペイン内でファイルビューア兼エディタとして動かすherdrプラグイン | `developer-tools` `editor` `fresh` `ide` `terminal` | 2 | 2026-07-17 |
| [**herdr-open-in-editor**](https://github.com/timofey-TK/herdr-open-in-editor)<br><sub>timofey-TK</sub> | ローカル・リモートのHerdrワークスペースをVS CodeまたはZedで開く | `vscode` `zed` `python` | 2 | 2026-07-30 |
| [**herdr-plugin-mermaid-preview**](https://github.com/Volpestyle/herdr-plugin-mermaid-preview)<br><sub>Volpestyle</sub> | Herdr上でClaude CodeやCodexの出力中のMermaid図をリアルタイムプレビューする | `claude-code` `mermaid` `openai-codex` `terminal` `javascript` | 2 | 2026-07-10 |
| [**herdr-launcher-pane**](https://github.com/y-hirakaw/herdr-launcher-pane)<br><sub>y-hirakaw</sub> | herdr向けの、ドッキングされたクリック起動用ペイン——Finder/Explorer、VS Code、あるいはワークスペースごとに設定した任意のコマンドを起動できる | `launcher` `launcher-pane` `productivity` `python` | 2 | 🔄 2026-08-10 |
| [**herdr-goto**](https://github.com/asumaran/herdr-goto)<br><sub>asumaran</sub> | herdrのリポジトリ・worktree・ペインを横断する、ツリー形式の切り替えツール | `go` | 1 | 2026-07-28 |
| [**🆕 herdr-yazi-explorer**](https://github.com/pjs-0457/herdr-yazi-explorer)<br><sub>pjs-0457</sub> | 呼び出したワークスペース内のherdrタブ/スプリットでYaziを開く（🗂 yaziというラベル付き）。終了すると自動的に再起動する | `yazi` `shell` | 1 | 🔄 2026-08-13 |
| [**🆕 herdr-icon-agent-ui**](https://github.com/qintmb/herdr-icon-agent-ui)<br><sub>qintmb</sub> | Renders Agent icon, vertically-aligned monochrome icons in the Herdr sidebar. rendered via a custom font with non-uniform glyph scaling that matches terminal c… | `python` | 1 | 🔄 2026-08-18 |
| [**herdr-terminal-file-manager**](https://github.com/robert-flo/herdr-terminal-file-manager)<br><sub>robert-flo</sub> | elioファイルマネージャーの薄いherdrラッパー。アクティブなディレクトリを検出してelioをネイティブに起動し、軽快なプレビュー・インライン画像表示・一括操作をherdrのペインにそのまま持ち込む | `shell` | 1 | 2026-07-10 |
| [**herdr-flutter**](https://github.com/ablause/herdr-flutter)<br><sub>ablause</sub> | コーディングエージェントの隣で、稼働中のFlutterアプリを監視・ホットリロード・検査できるherdrサイドバー | `dart` | 0 | 2026-07-27 |
| [**herdr-numbered-workspaces**](https://github.com/abrose/herdr-numbered-workspaces)<br><sub>abrose</sub> | herdrのサイドバーの各スペースの先頭に番号を付け、インデックス指定のswitch_workspaceショートカットと対応させる | `shell` | 0 | 2026-07-21 |
| [**🆕 herdr-cursor-open**](https://github.com/alex-devdone/herdr-cursor-open)<br><sub>alex-devdone</sub> | Open the focused herdr pane in Cursor or VS Code — including panes attached to a remote herdr, over Remote-SSH | `cursor` `vscode` `shell` | 0 | 🔄 2026-08-15 |
| [**herdr-preview**](https://github.com/AlexanderMakarov/herdr-preview)<br><sub>AlexanderMakarov</sub> | herdrプラグイン：表示中のペイン内のファイルパスにアルファベットのヒントを付け、file-viewerまたはlessで開く | `rust` | 0 | 🔄 2026-08-16 |
| [**herdr-ctx**](https://github.com/aorumbayev/herdr-ctx)<br><sub>aorumbayev</sub> | herdrのサイドバーペイン向けの、Claudeコンテキストウィンドウ表示 | `typescript` | 0 | 2026-07-21 |
| [**herdr-sidebar-numbers**](https://github.com/cedrus-8864/herdr-sidebar-numbers)<br><sub>cedrus-8864</sub> | サイドバーにワークスペースとエージェントの位置番号を表示し、1〜9のショートカットキーと対応させるherdrプラグイン | `ai-agents` `bun` `sidebar` `terminal` `javascript` | 0 | 2026-08-04 |
| [**herdr-codex-cost**](https://github.com/Coolsik/herdr-codex-cost)<br><sub>Coolsik</sub> | Herdrのサイドバーに、Codexセッションの推定コストを表示する | `codex` `shell` | 0 | 2026-07-31 |
| [**herdr-tab-badges**](https://github.com/CowboyVang/herdr-tab-badges)<br><sub>CowboyVang</sub> | 複数のタブを持つherdrのスペースに、サイドバーバッジを表示する | `shell` | 0 | 2026-07-21 |
| [**herdr-plugin-agent-repo**](https://github.com/khatriafaz/herdr-plugin-agent-repo)<br><sub>khatriafaz</sub> | エージェント名・リポジトリ名・ブランチ名を、エージェントペインのヘッダーとサイドバーに表示するHerdrプラグイン | `javascript` | 0 | 2026-07-24 |
| [**herdr-nnn**](https://github.com/linuxing3/herdr-nnn)<br><sub>linuxing3</sub> | herdr内でnnnを開く | `shell` | 0 | 2026-08-04 |
| [**herdr-cmux-file-viewer**](https://github.com/linvald/herdr-cmux-file-viewer)<br><sub>linvald</sub> | cmuxのファイルビューアを、現在フォーカスしているherdrのスペースに同期させるherdrプラグイン | `python` | 0 | 2026-07-23 |
| [**🆕 herdr-agent-icons**](https://github.com/moneycaringcoder/herdr-agent-icons)<br><sub>moneycaringcoder</sub> | A minimal Herdr plugin that gives the sidebar recognizable monochrome harness marks for Claude, Codex, OpenCode, and OMP without taking over Herdr lifecycle st… | `icons` `python` `terminal` | 0 | 🔄 2026-08-16 |
| [**🆕 herdr-pulse**](https://github.com/moneycaringcoder/herdr-pulse)<br><sub>moneycaringcoder</sub> | Per-workspace agent activity history for herdr, rendered as a sidebar sparkline. | `monitoring` `rust` `sparkline` `terminal` | 0 | 🔄 2026-08-16 |
| [**🆕 herdr-sidekick**](https://github.com/qapquiz/herdr-sidekick)<br><sub>qapquiz</sub> | Toggleable sidekick AI-agent pane for Herdr — paste code selections into the agent's composer without submitting. Pairs with qapquiz/herdr-sidekick.nvim. | `neovim` `terminal` `shell` | 0 | 🔄 2026-08-15 |
| [**herdr-openmd**](https://github.com/RufusLin/herdr-openmd)<br><sub>RufusLin</sub> | 選択したMarkdownをopenmdで開く——herdrから起動する、豊富な表現力を持つQt製プレビュー | `shell` | 0 | 2026-07-29 |
| [**herdr-git-detail**](https://github.com/sfroment/herdr-git-detail)<br><sub>sfroment</sub> | herdrプラグイン：詳細なgit状態（変更/ステージ/未追跡/進んでいる・遅れているコミット数/stash）を$git_detailというサイドバートークンとして表示する | `git` `shell` `starship` `terminal` | 0 | 🔄 2026-08-05 |
| [**herdr-gitui**](https://github.com/Shi1xin/herdr-gitui)<br><sub>Shi1xin</sub> | サイドバーペインでgituiを動かすherdrプラグイン——開閉トグル、展開、ライト/ダークテーマに対応 | `gitui` `python` | 0 | 2026-07-28 |
| [**🆕 herdr-tabpick**](https://github.com/sushidesu/herdr-tabpick)<br><sub>sushidesu</sub> | Pick a herdr tab, most recently used first, with a live pane preview. | `shell` | 0 | 🔄 2026-08-15 |
| [**meadow**](https://github.com/Tetat-Chulchue/meadow)<br><sub>Tetat-Chulchue</sub> | herdrのターミナルマルチプレクサ向けの、マウス操作のファイルエクスプローラーペイン | `python` | 0 | 2026-07-21 |
| [**🆕 dotfiles**](https://github.com/Unique-Divine/dotfiles)<br><sub>Unique-Divine</sub> | Dotfiles and other ~ configuration from Unique Divine | `dotfiles` `lua` `neovim` `neovim-dotfiles` `nvim` | 0 | 🔄 2026-08-19 |
| [**🆕 herdr-cmux-cwd-sync**](https://github.com/WerrySs/herdr-cmux-cwd-sync)<br><sub>WerrySs</sub> | Non-invasive cmux file explorer sync for the focused HerdR pane | `cmux` `macos` `python` | 0 | 🔄 2026-08-14 |

<details><summary>この目的にも関係するもの</summary>

- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) — herdr向けのコードレビュー＋ファイルビューアのサイドバー。エージェントの差分にコメントして差し戻せる。PRとそのチェック・コメントの読み取り専用表示も付属
- [ChmaraX/herdr-gitview](https://github.com/ChmaraX/herdr-gitview) — herdr向けのGitステータス/差分パネル——変更のレビュー、nvimでの編集、ステージ/コミット/破棄をすべてターミナルから行える
- [jsmenzies/mergr](https://github.com/jsmenzies/mergr) — Herdr Spaceのサイドバー行にGitHubプルリクエストの状態を表示する
- [vonzelle-vzt/herdr-extensions](https://github.com/vonzelle-vzt/herdr-extensions) — herdr向けの小さなVS Code——LSPによる診断・自動補完・リネーム・定義へジャンプに対応した本格エディタに加え、ソース管理・検索・問題一覧・テスト・デバッガ・アプリのライブプレビュー・実行時エラー捕捉・画像貼…
- [maedana/herdr-whereami](https://github.com/maedana/herdr-whereami) — 今どこにいるかを示すよう、タブを自動でリネームするHerdrプラグイン——gitリポジトリ内なら「リポジトリ名/ブランチ名」のように表示
- [bayoudhi/herdr-prayer-times](https://github.com/bayoudhi/herdr-prayer-times) — Next Islamic prayer and countdown in the Herdr sidebar, with a timetable popup and notifications
- [brianh20/herdr-stagr](https://github.com/brianh20/herdr-stagr) — herdr向けのソース管理サイドバー——並列差分表示でステージ・アンステージ・破棄ができる
- [ctbaum/herdr-deck](https://github.com/ctbaum/herdr-deck) — herdr-agents.nvimと組み合わせて使うワークスペースランチャー：Neovim・エージェント・シェル・lazygitがあらかじめ用意された「デッキ」で、ClaudeやCodexを開始または再開できる
- [Gareth-Rouse/herdr-plugin-session-pruner](https://github.com/Gareth-Rouse/herdr-plugin-session-pruner) — herdrプラグイン：ワークスペースの最終使用日時を記録してSpacesのサイドバーに経過時間を表示し、使われていないワークスペースをセッション復元の対象から外す
- [limars874/herdr-pane-id-metadata](https://github.com/limars874/herdr-pane-id-metadata) — 正規化されたペインIDと、コンパクトなタブ/ペインのサイドバーメタデータのための、最小構成のHerdrプラグイン

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-cost"></a>

## トークン・コスト管理

> エージェントがいくら使っているかを見たい / 使用量を削りたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**memex**](https://github.com/nicosuave/memex)<br><sub>nicosuave</sub> | Search Claude Code, Codex, Pi, OpenCode, Github Copilot & Cursor transcripts. Resume sessions. Track tokens. | `bm25` `claude-code` `codex-cli` `hybrid-search` `rag` | 148 | 🔄 2026-08-19 |
| [**llmtrim-herdr**](https://github.com/fkiene/llmtrim-herdr)<br><sub>fkiene</sub> | herdrのトークン代を節約：各エージェントペインのリクエストを圧縮（実測で入力-31%/出力-74%）し、節約額をペインごとのバッジで表示 | `llm-proxy` `llmtrim` `powershell` | 36 | 2026-07-02 |
| [**herdr-agent-usage**](https://github.com/senna-lang/herdr-agent-usage)<br><sub>senna-lang</sub> | Herdrで動作するエージェントのコンテキスト使用量メーターと、プロバイダーのレート制限を表示する | `ai-agents` `claude-code` `codex` `golang` `rate-limiting` | 22 | 🔄 2026-08-16 |
| [**herdr-token-dashboard**](https://github.com/Davidcreador/herdr-token-dashboard)<br><sub>Davidcreador</sub> | Herdrのエージェントペイン向けの、トークン消費量をリアルタイムに表示するダッシュボードと通知 | `ai-agents` `bubbletea` `opencode` `pi-agent` `token-dashboard` | 14 | 🔄 2026-08-13 |
| [**herdr-claude-usage**](https://github.com/alejodelosrios/herdr-claude-usage)<br><sub>alejodelosrios</sub> | 使用量を確認するためだけにClaudeのセッションを開く必要はもうない。Claudeプランの使用状況（セッション％｜週％）を常にHerdrのサイドバーに表示し、そのアカウントの全ワークスペースで共有される。Claude Code自身の認証情報を使い/statusと同じ正確な数値を表示——推定値ではなく、追加ログインも… | `claude` `claude-code` `python` | 3 | 2026-07-21 |
| [**🆕 herdr-quota**](https://github.com/kvkenyon/herdr-quota)<br><sub>kvkenyon</sub> | See Claude, Codex, Cursor, and Kimi subscription quota at a glance in Herdr. | `ai-tools` `claude-code` `cursor` `developer-tools` `kimi` | 2 | 🔄 2026-08-19 |
| [**herdr-whereami**](https://github.com/maedana/herdr-whereami)<br><sub>maedana</sub> | 今どこにいるかを示すよう、タブを自動でリネームするHerdrプラグイン——gitリポジトリ内なら「リポジトリ名/ブランチ名」のように表示 | `rust` | 2 | 🔄 2026-08-14 |
| [**scopefuel**](https://github.com/mgh3326/scopefuel)<br><sub>mgh3326</sub> | AIコーディングエージェントのプラン向けの、範囲を意識した残量ゲージ——実際に何（アカウント/モデル/グループ）がブロックされているか、いつ回復するかが分かる | `ai-agents` `antigravity` `claude-code` `cli` `codex` | 1 | 🔄 2026-08-15 |
| [**herdr-usage-bar**](https://github.com/silverwolfdoc/herdr-usage-bar)<br><sub>silverwolfdoc</sub> | Herdr内のAIエージェント向けの使用量上限とコンテキストメーターを、コンパクトな下部の使用量バーで表示する | `go` | 1 | 🔄 2026-08-13 |
| [**herdr-gekiatsu-plugin**](https://github.com/yuuta1219/herdr-gekiatsu-plugin)<br><sub>yuuta1219</sub> | herdrプラグイン：Claude Codeの使用量カウンターを、パチスロ風にしたもの。大当たり確率1/99、毎日10:00 JSTにリセット | `claude` `claude-code` `python` `tui` | 1 | 🔄 2026-08-17 |
| [**🆕 herdr-habitat**](https://github.com/chantlong/herdr-habitat)<br><sub>chantlong</sub> | herdr habitat is a living terminal habitat that grows alongside your agents’ work. Nurturing takes time, so no agentmaxxing please. As agents burn tokens in en… | `chill` `cozy` `javascript` | 0 | 🔄 2026-08-16 |
| [**herdr-burn**](https://github.com/samuelbaldwin05/herdr-burn)<br><sub>samuelbaldwin05</sub> | herdrのサイドバーに、ペインごとのClaude Codeのコスト/割当量をリアルタイム表示し、ワークスペース合計の消費量オーバーレイも提供する | `python` | 0 | 🔄 2026-08-12 |
| [**herdr-model-capacity**](https://github.com/shrivatsas/herdr-model-capacity)<br><sub>shrivatsas</sub> | アカウント単位のClaude・Codex/OpenAI・OpenRouterの利用可能量を表示するHerdrペイン | `claude` `codex` `openrouter` `rust` | 0 | 🔄 2026-08-19 |
| [**🆕 herdr-fleece**](https://github.com/sjh9714/herdr-fleece)<br><sub>sjh9714</sub> | Know when your herd is fleecing you. Live tokens, dollars and burn rate for every herdr pane, one screen. herdr 实时成本与燃烧速率控制台. | `ai-agents` `burn-rate` `ccusage` `claude-code` `cli` | 0 | 🔄 2026-08-19 |
| [**🆕 herdr-model-quota**](https://github.com/terry-li-hm/herdr-model-quota)<br><sub>terry-li-hm</sub> | Herdr plugin for compact Codex and Claude Max subscription quota visibility | `claude` `codex` `quota` `terminal` `python` | 0 | 🔄 2026-08-18 |
| [**claude-usage**](https://github.com/yuuta1219/claude-usage)<br><sub>yuuta1219</sub> | herdrプラグイン：Claude Codeの使用率（セッション%/週%）をサイドバー下部に常時表示する | `claude` `claude-code` `python` `tui` | 0 | 2026-08-01 |

<details><summary>この目的にも関係するもの</summary>

- [hamidi-dev/herdr-opentab](https://github.com/hamidi-dev/herdr-opentab) — Live per-agent AI spend from OpenTab in the Herdr sidebar.
- [levi-qiao/herdr-agent-quota](https://github.com/levi-qiao/herdr-agent-quota) — Never hit a quota limit mid-task: see Claude, Codex, Grok and Agy usage live in your Herdr sidebar. 5h and we…
- [Coolsik/herdr-codex-cost](https://github.com/Coolsik/herdr-codex-cost) — Herdrのサイドバーに、Codexセッションの推定コストを表示する

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-monitor"></a>

## 監視・ダッシュボード

> エージェントやマシンの状態を一覧で眺めたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**🆕 clauth**](https://github.com/uwuclxdy/clauth)<br><sub>uwuclxdy</sub> | Claude Code multi-account manager, usage monitor (CLI, TUI & MCP task delegation) | `account-manager` `account-switcher` `anthropic` `claude` `claude-code` | 63 | 🔄 2026-08-19 |
| [**herdr-pc-ram-and-cpu-usage-overlay**](https://github.com/ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay)<br><sub>ezcorp-org</sub> | herdrプラグイン：スペース（ワークスペース）ごとのCPU/RAM使用率を、マシン全体に対する割合としてリアルタイム表示 | `rust` | 12 | 🔄 2026-08-12 |
| [**herdr-beads**](https://github.com/miiraheart/herdr-beads)<br><sub>miiraheart</sub> | herdr向けのbeads (bd) タスクボード：bdのissueをリスト・テーブル・カンバンで表示し、サイドバーまたはフローティングで表示できる | `bd` `beads` `kanban` `rust` `tui` | 11 | 2026-07-24 |
| [**herdr-telemetry**](https://github.com/DIodide/herdr-telemetry)<br><sub>DIodide</sub> | ワークスペースとエージェントのテレメトリを自分で管理するエンドポイントにストリーミングするHerdrプラグイン——Go製の単一バイナリ、プライバシー重視のデフォルト設定 | `golang` `telemetry` `go` | 9 | 2026-07-10 |
| [**herdres**](https://github.com/luminexord/herdres)<br><sub>luminexord</sub> | Tendwireを利用した、Herdrのコーディングエージェントを監視・メッセージ送信できるTelegramインターフェース | `coding-agents` `telegram` `python` | 9 | 🔄 2026-08-09 |
| [**herdr-workboard**](https://github.com/Phoobobo/herdr-workboard)<br><sub>Phoobobo</sub> | herdr向けのカンバン式ワークボードTUI：ボード＝ワークスペース、タスクの状態＝タブ、タスクのセッション＝ペインという構造 | `kanban` `tui` `typescript` | 7 | 🔄 2026-08-10 |
| [**shepherd**](https://github.com/ryonakae/shepherd)<br><sub>ryonakae</sub> | Herdr管理下のコーディングエージェント向けの、ワーカー監視デーモンとランタイムブリッジ | `pi-coding-agent` `pi-extension` `typescript` | 7 | 2026-07-22 |
| [**herdr-f1**](https://github.com/hmu332233/herdr-f1)<br><sub>hmu332233</sub> | Herdrのエージェント向けの、F1風ダッシュボード | `agent-dashboard` `typescript` | 6 | 🔄 2026-08-13 |
| [**herdr-tally**](https://github.com/jasonrr/herdr-tally)<br><sub>jasonrr</sub> | あなたとエージェントのための、プロジェクト単位のTodoとスクラッチパッド<br>📝 プロジェクト単位の TODO 管理 | `rust` `todo` | 5 | 🔄 2026-08-14 |
| [**herdr-kanban**](https://github.com/KokiKono/herdr-kanban)<br><sub>KokiKono</sub> | タスクをherdrのタブに紐付けるターミナル上のカンバンボード。SQLiteに保存される | `rust` | 5 | 2026-07-10 |
| [**herdr-sysmon**](https://github.com/getpipher/herdr-sysmon)<br><sub>getpipher</sub> | Herdrのサイドバーにシステムメトリクスを表示——CPU・メモリ・バッテリー・ネットワーク・ディスク・時計。tmux-cpu/tmux-battery/tmux-online-statusのステータスバーを、Herdrのワークスペーストークンに忠実に移植したもの。macOS優先対応 | `battery` `catppuccin` `cpu` `getpipher` `macos` | 4 | 2026-07-26 |
| [**🆕 herdr-agent-quota**](https://github.com/levi-qiao/herdr-agent-quota)<br><sub>levi-qiao</sub> | Never hit a quota limit mid-task: see Claude, Codex, Grok and Agy usage live in your Herdr sidebar. 5h and weekly percent remaining. | `agent-usage` `agy` `ai-agents` `antigravity` `claude-code` | 3 | 🔄 2026-08-17 |
| [**adlc-herdr**](https://github.com/voodootikigod/adlc-herdr)<br><sub>voodootikigod</sub> | ADLC向けのherdrプラグイン——ペインごとのフェーズ/チケット/ゲートの状態、バックログボード、ゲートアクション、adlc-fleetの実行状況の可視化に対応。voodootikigod/adlc/plugins/adlc-herdrの自動同期ミラー | `javascript` | 3 | 🔄 2026-08-10 |
| [**🆕 herdr-agent-watcher**](https://github.com/winoooops/herdr-agent-watcher)<br><sub>winoooops</sub> | Coding-agent observability for Herdr: live sidebar cards, lifecycle notifications, and a zero-config Claude Code metrics bridge. | `claude-code` `rust` | 3 | 🔄 2026-08-19 |
| [**herdr-agent-dashboard**](https://github.com/carsonjones/herdr-agent-dashboard)<br><sub>carsonjones</sub> | prefix+aでherdrのエージェント一覧を表示する | `typescript` | 2 | 2026-07-16 |
| [**herdr-telemetry-bridge**](https://github.com/CodyBontecou/herdr-telemetry-bridge)<br><sub>CodyBontecou</sub> | ローカルのワークスペース・リポジトリ・コーディングエージェント・モデル・トレースのテレメトリを外部クライアントにストリーミングするHerdrプラグイン | `coding-agents` `telemetry` `time-md` `javascript` | 2 | 2026-06-26 |
| [**🆕 herdr-statusline**](https://github.com/iiii1224/herdr-statusline)<br><sub>iiii1224</sub> | herdrセッション向けのカスタマイズ可能なステータスライン | `cli` `statusbar` `statusline` `tmux` `python` | 2 | 🔄 2026-08-15 |
| [**shepherd**](https://github.com/jwarykowski/shepherd)<br><sub>jwarykowski</sub> | あなたのTodoを群れとしてまとめる | `cli` `developer-tools` `go-lang` `productivity` `task-management` | 2 | 🔄 2026-08-13 |
| [**🆕 herdr-portal**](https://github.com/loofare/herdr-portal)<br><sub>loofare</sub> | Mission-control dashboard for herdr — aggregates every workspace/tab/pane agent into a live TUI kanban (keyboard + mouse) plus a web big-screen: structured pro… | `agent-dashboard` `agent-monitor` `ai-agents` `claude-code` `codex` | 2 | 🔄 2026-08-18 |
| [**herdr-cache-ttl**](https://github.com/nytafar/herdr-cache-ttl)<br><sub>nytafar</sub> | herdrプラグイン：エージェントのペインごとに、プロンプトキャッシュのTTLをリアルタイムでカウントダウン表示する | `rust` | 2 | 🔄 2026-08-05 |
| [**herdr-slurm**](https://github.com/quan-meng/herdr-slurm)<br><sub>quan-meng</sub> | Slurmのアロケーション向けに、Herdrのワークスペースと監視付きエージェントタブを作成する | `hpc` `slurm` `terminal-multiplexer` `python` | 2 | 🔄 2026-08-13 |
| [**herdr-agent-state**](https://github.com/Tyru5/herdr-agent-state)<br><sub>Tyru5</sub> | herdr向けのリアルタイムエージェント状態ペイン——ワークスペース内の各エージェントが何をしているかを、より人間に読みやすい形式で表示する | `claude-code` `rust` `terminal` | 2 | 🔄 2026-08-05 |
| [**herdr-cache-timer**](https://github.com/ArteenHD/herdr-cache-timer)<br><sub>ArteenHD</sub> | 各エージェントのプロンプトキャッシュがいつ失効するかを、Herdrのサイドバーに直接表示する | `claude-code` `prompt-caching` `terminal` `javascript` | 1 | 🔄 2026-08-08 |
| [**herdr-tokscale-dashboard**](https://github.com/astkaasa/herdr-tokscale-dashboard)<br><sub>astkaasa</sub> | TokscaleをローカルのHerdrダッシュボードペインとして開く | `dashboard` `tokscale` `shell` | 1 | 2026-06-26 |
| [**herdr-shell-progress**](https://github.com/bayoudhi/herdr-shell-progress)<br><sub>bayoudhi</sub> | herdrプラグイン：コーディングエージェントに限らず、時間のかかるシェルコマンドの進行状況もサイドバーにリアルタイム表示する | `rust` | 1 | 🔄 2026-08-05 |
| [**herdr-plugin-codex-subs**](https://github.com/benkraus/herdr-plugin-codex-subs)<br><sub>benkraus</sub> | CLIProxyAPIのCodexサブスクリプション枠とリセットクレジットを表示するHerdrダッシュボード | `go` | 1 | 2026-07-30 |
| [**🆕 herdr-jira-board**](https://github.com/kiitosu/herdr-jira-board)<br><sub>kiitosu</sub> | Jira kanban board inside herdr with Claude Code session launcher | `python` | 1 | 🔄 2026-08-17 |
| [**herdr-compose**](https://github.com/mattyan1053/herdr-compose)<br><sub>mattyan1053</sub> | docker compose向けのHerdrプラグイン | `terminal` `tui` `shell` | 1 | 2026-07-24 |
| [**herdr-ports**](https://github.com/Numbered-com/herdr-ports)<br><sub>Numbered-com</sub> | herdrで稼働中の開発サーバーを可視化：TCPリスナーが1つ以上動いているすべてのスペースに$portsバッジを表示する | `pids` `ports` `shell` | 1 | 2026-07-23 |
| [**herdr-agent-metrics**](https://github.com/szrenwei/herdr-agent-metrics)<br><sub>szrenwei</sub> | Claude Code・Codex・TraeX向けの、軽量なHerdrコンテキスト・セッション使用量メトリクス | `claude-code` `openai-codex` `traex` `python` | 1 | 2026-08-04 |
| [**herdr-space-tab-metadata**](https://github.com/szrenwei/herdr-space-tab-metadata)<br><sub>szrenwei</sub> | 各Herdr Spaceのアクティブなタブをサイドバーに表示する | `terminal-ui` `python` | 1 | 2026-08-04 |
| [**🆕 herdr-docker**](https://github.com/abcxff/herdr-docker)<br><sub>abcxff</sub> | herdrでエージェントを追跡するのと同じように、dockerのビルドも追跡する | `docker` `javascript` | 0 | 🔄 2026-08-12 |
| [**herdr-ios-build-status-plugin**](https://github.com/atomsbaza/herdr-ios-build-status-plugin)<br><sub>atomsbaza</sub> | オンデマンドで確認できる、HerdrのiOSビルド＋テスト状況ペイン。失敗時のスクリーンショット付き | `shell` | 0 | 🔄 2026-08-06 |
| [**herdr-jcode-integration**](https://github.com/capt-marbles/herdr-jcode-integration)<br><sub>capt-marbles</sub> | Jcodeのライフサイクル状態とセッションレポーティングのためのHerdrプラグイン | `jcode` `shell` | 0 | 🔄 2026-08-09 |
| [**herdr-dev-servers**](https://github.com/carellano/herdr-dev-servers)<br><sub>carellano</sub> | Herdrのペインで動作している開発サーバーを検出し、安全に管理する | `developer-tools` `go` `terminal` | 0 | 🔄 2026-08-12 |
| [**herdr-agentsview**](https://github.com/cpcloud/herdr-agentsview)<br><sub>cpcloud</sub> | AgentsViewのアクティビティを、1つの非常に賑やかなターミナルに凝縮して表示する | `rust` | 0 | 🔄 2026-08-19 |
| [**herdr-vitals**](https://github.com/ericcparsons/herdr-vitals)<br><sub>ericcparsons</sub> | macOS向けherdrプラグイン——サイドバーにエージェントごとのCPU/RAM使用率とスペースごとの稼働中devサーバーポートを表示し、ポップアップから終了操作もできる | `bun` `developer-tools` `terminal` `typescript` | 0 | 2026-07-29 |
| [**herdr-phin-board**](https://github.com/phin-tech/herdr-phin-board)<br><sub>phin-tech</sub> | Herdrプラグイン：スペース全体を対象とするステータスボード——todo・進行中・誰かの対応待ち・完了、さらに自分で定義したステータスにも対応。リストまたはカンバンで表示 | `bubbletea` `tui` `go` | 0 | 2026-07-29 |
| [**colloquy**](https://github.com/SoMaCoSF/colloquy)<br><sub>SoMaCoSF</sub> | エージェント群向けの、自己アドレス指定型・一時キャッシュされた因果関係DAG監査ログとテレメトリ | `colloquy` `gyst` `javascript` | 0 | 2026-07-29 |
| [**conflux-herdr**](https://github.com/tumf/conflux-herdr)<br><sub>tumf</sub> | Conflux TUIを実行し、そのライフサイクル状態を報告するHerdrプラグインペイン | `shell` | 0 | 2026-07-26 |
| [**herdr-hud**](https://github.com/zetlen/herdr-hud)<br><sub>zetlen</sub> | herdrプラグイン：キーバインドで開くポップアップに、ホスト・ネットワーク・エージェント・セッションの情報を表示——設定変更やカスタムスクリプトによる拡張が可能 | `bash` `terminal` `shell` | 0 | 2026-08-03 |

<details><summary>この目的にも関係するもの</summary>

- [nelsonPires5/herdr-board](https://github.com/nelsonPires5/herdr-board) — herdr向けのカンバンボード——カードはそのままプロンプトになり、見えているペイン上のAIエージェントに割り振られる
- [cdowell09/herdr-pr-board](https://github.com/cdowell09/herdr-pr-board) — 複数リポジトリを横断できる、設定可能なHerdr向けGitHubプルリクエストダッシュボード
- [bengemine/herdr-hibernate](https://github.com/bengemine/herdr-hibernate) — Herdr上のアイドル状態のコーディングエージェントペイン（Claude Code、Codex、Grok）をハイバネート——メモリを解放し、Enterキーで元のセッションをそのまま再開できる
- [e2b-dev/herdr-e2b-sandbox](https://github.com/e2b-dev/herdr-e2b-sandbox) — herdr plugin that mirrors a git worktree into an E2B sandbox — one box or a branch-per-agent fleet, with a TU…
- [Javamomma/herdr-scribe](https://github.com/Javamomma/herdr-scribe) — herdrプラグイン：録音せずにライブで会議を文字起こし——マイク入力をRAM上のみのトランスクリプトとライブ分析用ペインに変換。停止時には議事録・任意のポリシーゲート・レビュー可能な自動ドラフトを生成。Linux/W…
- [chouxcreams/herdr-dashboard](https://github.com/chouxcreams/herdr-dashboard) — herdrのワークスペース向けのPRステータスダッシュボードTUI——ペインごとのPRの状態・CI・レビューを一目で確認できる
- [GranamyrBR/LunaCrab](https://github.com/GranamyrBR/LunaCrab) — 別プロジェクト用に予約済み
- [maedana/herdr-agents-preview](https://github.com/maedana/herdr-agents-preview) — Herdr向けのマルチエージェントターミナルプレビューダッシュボード：稼働中のすべてのエージェントを同時に表示し、選択中のエージェントが大部分の幅を占める
- [Northern-Lighthouse/herdr-fleet](https://github.com/Northern-Lighthouse/herdr-fleet) — Manage a fleet of herdr machines over Tailscale: dashboard plugin, auto-discovery, capacity-aware agent dispa…
- [GranamyrBR/ezdras-herdr](https://github.com/GranamyrBR/ezdras-herdr) — Herdr向けの、複数エージェントをリアルタイムに可視化する仕組みとペイン操作機能
- [moneycaringcoder/herdr-pulse](https://github.com/moneycaringcoder/herdr-pulse) — Per-workspace agent activity history for herdr, rendered as a sidebar sparkline.

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-finder"></a>

## 検索・ファジーファインダー

> コマンドやプロジェクトを、名前をうろ覚えのまま呼び出したい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-navigator**](https://github.com/thanhdat77/herdr-navigator)<br><sub>thanhdat77</sub> | 1つのファジーナビゲーターから、任意のHerdrのワークスペース・エージェント・プロジェクト・セッション・リモート・ディレクトリ・アクションにジャンプできる | `fuzzy-finder` `rust` `terminal` `workspace-manager` | 95 | 🔄 2026-08-11 |
| [**termscope**](https://github.com/iurysza/termscope)<br><sub>iurysza</sub> | 分割ペインで、ターミナル画面に表示されているファイルやリンクを開く | `python` `television` `terminal` `tmux` | 47 | 🔄 2026-08-19 |
| [**herdr-sessionizer**](https://github.com/andrewchng/herdr-sessionizer)<br><sub>andrewchng</sub> | プロジェクトやworktreeをファジー検索で開き、宣言的なTOMLレイアウト（タブ・ペイン分割・起動コマンド・リポジトリごとの上書き設定）からワークスペースを立ち上げる | `bun` `fuzzy-finder` `fzf` `git-worktree` `sessionizer` | 37 | 🔄 2026-08-16 |
| [**herdr-command-palette**](https://github.com/JanTvrdik/herdr-command-palette)<br><sub>JanTvrdik</sub> | herdr向けのfzfコマンドパレット——任意のプラグインアクションをファジー検索して実行 | `shell` | 28 | 2026-06-29 |
| [**herdr-plugin-sesh**](https://github.com/fullerzz/herdr-plugin-sesh)<br><sub>fullerzz</sub> | Herdr向けのSesh風ワークスペースピッカーTUI。zoxideと連携し、よく使うディレクトリからワークスペースを作成できる | `bubbletea` `sesh` `tui` `zoxide` `go` | 27 | 🔄 2026-08-20 |
| [**herdr-bar**](https://github.com/jeffarese/herdr-bar)<br><sub>jeffarese</sub> | herdr版のCmd+K：任意のタブ・エージェント・リポジトリ・ブランチにファジー検索でジャンプ。Python標準ライブラリのみで動作 | `command-bar` `fuzzy-finder` `python` `terminal` `tui` | 21 | 🔄 2026-08-07 |
| [**herdr-zoxide**](https://github.com/den-tanui/herdr-zoxide)<br><sub>den-tanui</sub> | zoxideのディレクトリからワークスペース・タブ・ペインを作成するHerdrプラグイン | `zoxide` `shell` | 11 | 2026-07-25 |
| [**herdr-drovr**](https://github.com/AVGVSTVS96/herdr-drovr)<br><sub>AVGVSTVS96</sub> | herdrのペインとタブを簡単に移動する | `fzf` `terminal` `javascript` | 9 | 🔄 2026-08-08 |
| [**herdr-palette**](https://github.com/ramarivera/herdr-palette)<br><sub>ramarivera</sub> | Herdrのワークスペース向けの、Rust/Ratatui製ファジーコマンドパレット | `command-palette` `ratatui` `rust` `terminal` `tui` | 7 | 🔄 2026-08-14 |
| [**herdr-switchboard**](https://github.com/crafts69guy/herdr-switchboard)<br><sub>crafts69guy</sub> | herdrプラグイン：稼働中のエージェント・開いているワークスペース・ghq管理下のリポジトリを、Rust製の1つのTUIでファジー切り替え——選んだリポジトリを新規ワークスペース・タブ・スプリット・現在のペインのいずれかで開ける | `developer-tools` `ghq` `ratatui` `rust` `terminal` | 5 | 🔄 2026-08-19 |
| [**herdr-kiosk**](https://github.com/thomasschafer/herdr-kiosk)<br><sub>thomasschafer</sub> | Gitのリポジトリとブランチをファジー検索し、Herdr内でworktreeとして開く | `rust` | 4 | 🔄 2026-08-12 |
| [**herdr-cast**](https://github.com/aliou/herdr-cast)<br><sub>aliou</sub> | 個人用Herdrプラグイン——ネイティブmacOS通知、ファジーなワークスペース移動、zoxide連携のワークスペース作成、レイアウトコマンドをまとめて提供 | `developer-tools` `macos` `notifications` `ratatui` `rust` | 3 | 🔄 2026-08-13 |
| [**herdr-grep-nvim**](https://github.com/cinco/herdr-grep-nvim)<br><sub>cinco</sub> | herdrプラグイン：fzf + ripgrepでライブgrepし、マッチした箇所を作業の隣のスプリットでnvimで開く | `shell` | 3 | 2026-07-17 |
| [**herdr-quick-actions**](https://github.com/enekos/herdr-quick-actions)<br><sub>enekos</sub> | herdr標準のタブ/ペイン/ワークスペース操作を、使用頻度順でfzfから選べる——キーバインドを覚える必要がなくなる | `shell` | 3 | 🔄 2026-08-05 |
| [**🆕 herdr-ssh-manager**](https://github.com/jorge07RD/herdr-ssh-manager)<br><sub>jorge07RD</sub> | Save SSH hosts and reconnect from a fuzzy popup inside Herdr — Enter hands the popup straight to ssh. | `rust` `ssh` `terminal` `tui` | 3 | 🔄 2026-08-19 |
| [**herdr-pane-navigator**](https://github.com/mr04vv/herdr-pane-navigator)<br><sub>mr04vv</sub> | Herdrのワークスペース・タブ・ペインを1つのファジーツリーとして横断移動——各ペインが実際に何をしているかを手がかりにする | `coding-agents` `fzf` `terminal` `tui` `shell` | 3 | 🔄 2026-08-16 |
| [**herdr-sessionizer**](https://github.com/salkhalil/herdr-sessionizer)<br><sub>salkhalil</sub> | herdr版tmux-sessionizer：開いているワークスペースとzoxideのディレクトリをfzfで検索し、テンプレートタブ付きで作成またはフォーカスする | `shell` | 3 | 2026-07-27 |
| [**herdr-keymap**](https://github.com/The-Dave-Stack/herdr-keymap)<br><sub>The-Dave-Stack</sub> | herdrプラグイン：すべてのキーバインドをオーバーレイのパレットに表示し、CLI相当のものはそのまま実行できる | `typescript` | 3 | 🔄 2026-08-12 |
| [**herdr-agent-recency**](https://github.com/ugurtarlig/herdr-agent-recency)<br><sub>ugurtarlig</sub> | テーマに対応したHerdrピッカー。CodexとClaudeの実質的なアクティビティで並び替える | `claude-code` `codex` `fzf` `python` | 3 | 2026-07-17 |
| [**herdr-configurable-picker**](https://github.com/yoshiori/herdr-configurable-picker)<br><sub>yoshiori</sub> | 完全にカスタマイズ可能なキーバインドを持つ、herdr向けのツリー形式gotoピッカー | `rust` | 3 | 2026-07-05 |
| [**herdr-launcher**](https://github.com/arjenblokzijl/herdr-launcher)<br><sub>arjenblokzijl</sub> | 宣言的なTOMLワークフローをファジー検索で選び、フォームに入力して、新しいherdrのスペースでコーディングエージェントを起動する | `launcher` `ratatui` `rust` `tui` | 2 | 2026-07-10 |
| [**herdr-simple-switcher**](https://github.com/haphamdev/herdr-simple-switcher)<br><sub>haphamdev</sub> | ワークスペース・タブ・AIエージェントをファジー検索する | `shell` | 2 | 2026-08-01 |
| [**herdr-spotify**](https://github.com/iikjl/herdr-spotify)<br><sub>iikjl</sub> | herdr向けのSpotify再生中オーバーレイプラグイン——アルバムアート・再生操作、Spotify Web API経由の検索/キュー追加/いいねにも対応 | `spotify` `terminal` `go` | 2 | 2026-07-07 |
| [**herdr-workspace-launcher**](https://github.com/ImArtisann/herdr-workspace-launcher)<br><sub>ImArtisann</sub> | 検索可能でキーボード操作のディレクトリピッカーを使い、フォーカスしたワークスペースをすばやく作成するmacOS向けHerdrプラグイン | `typescript` | 2 | 2026-07-16 |
| [**herdr-recent-workspaces**](https://github.com/ismaelosuna7824/herdr-recent-workspaces)<br><sub>ismaelosuna7824</sub> | Herdr版「最近使ったフォルダを開く」——ワークスペースとして開いたフォルダをファジー検索できる一覧。選ぶとそのワークスペースを開くか再フォーカスでき、ファイルシステムを参照して新規に開くこともできる | `go` | 2 | 2026-07-10 |
| [**herdr-hunk**](https://github.com/JacquesvanWyk/herdr-hunk)<br><sub>JacquesvanWyk</sub> | herdr向けの、Hunkの差分をfzfで対話的に選ぶピッカー：コミット・範囲・stashに対応し、エージェント完了時に自動オープンもできる | `fzf` `hunk` `shell` | 2 | 2026-07-12 |
| [**herdr-ghq-open-agent**](https://github.com/kenchan/herdr-ghq-open-agent)<br><sub>kenchan</sub> | herdrプラグイン：ghq管理下のリポジトリをfzfでインクリメンタル検索し、選んだものをワークスペース/タブで開いてclaudeを起動する | `fzf` `ghq` `shell` | 2 | 2026-08-03 |
| [**herdr-vscode-tasks**](https://github.com/lurepos/herdr-vscode-tasks)<br><sub>lurepos</sub> | プロジェクトの.vscodeフォルダを扱うときに便利なherdrピッカー | `typescript` | 2 | 🔄 2026-08-12 |
| [**herdr-keybind-search**](https://github.com/malone-c/herdr-keybind-search)<br><sub>malone-c</sub> | herdr向けの検索可能なキーバインドオーバーレイ（fzf）。キーを押すと、自分のキーバインドをファジー検索できる | `shell` | 2 | 2026-07-15 |
| [**🆕 herdr-theme-picker**](https://github.com/qintmb/herdr-theme-picker)<br><sub>qintmb</sub> | Theme picker for herdr UI based terminalcolors scheme and your customization. | `shell` | 2 | 🔄 2026-08-19 |
| [**herdr-openr**](https://github.com/wraithyy/herdr-openr)<br><sub>wraithyy</sub> | herdrプラグイン：ターミナルやAIエージェントが直前に言及したファイル/URLをファジー検索で開く——Claudeのペインではセッションのトランスクリプトを読み取る | `shell` | 2 | 🔄 2026-08-14 |
| [**herdr-waypoint**](https://github.com/wraithyy/herdr-waypoint)<br><sub>wraithyy</sub> | フォルダに名前を付けて保存し、ファジー検索の一覧から選んで新しいherdrワークスペースとして開く | `shell` | 2 | 🔄 2026-08-12 |
| [**herdr-url-picker**](https://github.com/abrose/herdr-url-picker)<br><sub>abrose</sub> | herdrプラグイン：現在のペインに表示されたURLをfzfで選び、デフォルトブラウザで開く | `shell` | 1 | 2026-07-22 |
| [**herdr-jump**](https://github.com/agustinvalencia/herdr-jump)<br><sub>agustinvalencia</sub> | herdrのスペースとエージェント用に分かれたオーバーレイピッカー——任意のワークスペースやエージェントに、ステータスを色で示しながらジャンプできる | `go` | 1 | 2026-07-24 |
| [**herdr-command-palette**](https://github.com/alon-z/herdr-command-palette)<br><sub>alon-z</sub> | Herdrプラグイン：ワークスペース/ディレクトリのファジー検索コマンドパレット | `javascript` | 1 | 2026-06-22 |
| [**🆕 herdr-workspace-save**](https://github.com/chandrasekharan98/herdr-workspace-save)<br><sub>chandrasekharan98</sub> | Save a Herdr workspace — layout, cwds, agent sessions, running commands — and reopen it later from an fzf picker. | `claude-code` `terminal` `tmux` `python` | 1 | 🔄 2026-08-19 |
| [**herdr-url-picker**](https://github.com/chouxcreams/herdr-url-picker)<br><sub>chouxcreams</sub> | Herdrプラグイン：フォーカス中のペインからURLを選び、ブラウザで開く | `shell` | 1 | 2026-07-22 |
| [**herdr-sesh-bro**](https://github.com/cyperx84/herdr-sesh-bro)<br><sub>cyperx84</sub> | Herdr向けのsesh風ファジーセッションピッカー——ワークスペース・エージェント・zoxideのディレクトリを、ライブプレビュー付きの1つのfzfポップアップにまとめる | `go` | 1 | 🔄 2026-08-12 |
| [**🆕 herdr-command-palette**](https://github.com/hota911/herdr-command-palette)<br><sub>hota911</sub> | fzf command palette for herdr's built-in operations — workspaces, tabs, panes, agents | `command-palette` `fzf` `shell` | 1 | 🔄 2026-08-16 |
| [**herdr-keys**](https://github.com/JacquesvanWyk/herdr-keys)<br><sub>JacquesvanWyk</sub> | herdr向けの、ファジー検索可能なキーバインド一覧（パック・発見機能・個人による上書き設定に対応） | `shell` | 1 | 2026-07-12 |
| [**herdr-fzf-url**](https://github.com/kaar/herdr-fzf-url)<br><sub>kaar</sub> | herdrペインのスクロールバックからURLをファジー検索して開く——tmux-fzf-urlのherdr移植版 | `shell` | 1 | 2026-07-29 |
| [**herdr-hint**](https://github.com/maedana/herdr-hint)<br><sub>maedana</sub> | Herdr向けのVimium風ヒントラベル——キーを押すとタブやエージェントにラベルが表示され、ラベルを押すとジャンプする | `rust` | 1 | 🔄 2026-08-11 |
| [**herdr-pane-picker**](https://github.com/ugurtarlig/herdr-pane-picker)<br><sub>ugurtarlig</sub> | ペイン上に表示される文字ヒントを入力して、Herdrのペインを選択する | `terminal` `wezterm` `python` | 1 | 2026-07-17 |
| [**herdr-fzf-url**](https://github.com/x0d7x/herdr-fzf-url)<br><sub>x0d7x</sub> | herdrのターミナルペインをスキャンしてURLを検出し、fzfで対話的に選択する | `fzf` `go` `url` | 1 | 2026-06-26 |
| [**herdr-open-local-paths**](https://github.com/yigitkg/herdr-open-local-paths)<br><sub>yigitkg</sub> | ローカルパスを検出し、Windows・Linux・WSL上のシンプルなピッカーから開く/表示するHerdrプラグイン | `developer-tools` `python` `terminal` `wsl` | 1 | 2026-07-28 |
| [**herdr-agents-picker**](https://github.com/yxhta/herdr-agents-picker)<br><sub>yxhta</sub> | Herdrプラグイン：ワークスペースピッカー風のファジー検索で、エージェントペインをリアルタイムプレビュー付きで選ぶ（Rust + ratatui製） | `rust` | 1 | 2026-07-31 |
| [**herdr-iris**](https://github.com/a-curious-coder/herdr-iris)<br><sub>a-curious-coder</sub> | Iris——herdrプラグイン：ペインで検出したエージェントに絞り込んだ、AIエージェントスキルのファジー検索チートシート | `shell` | 0 | 🔄 2026-08-07 |
| [**🆕 herdr-locksmith**](https://github.com/bkarpinos/herdr-locksmith)<br><sub>bkarpinos</sub> | keybinding command palette for herdr | `typescript` | 0 | 🔄 2026-08-18 |
| [**herdr-picker**](https://github.com/bkarpinos/herdr-picker)<br><sub>bkarpinos</sub> | herdrのワークスペース・エージェント・タブを検索・プレビューできる、高速なポップアップピッカー | `go` | 0 | 2026-07-25 |
| [**helm.herdr**](https://github.com/black-atom-industries/helm.herdr)<br><sub>black-atom-industries</sub> | 1つのファジーナビゲーターから、任意のHerdrのワークスペース・エージェント・プロジェクト・セッション・リモート・ディレクトリ・アクションにジャンプできる | `rust` | 0 | 🔄 2026-08-18 |
| [**🆕 herdr-opencode-sessions**](https://github.com/damianpoole/herdr-opencode-sessions)<br><sub>damianpoole</sub> | A Herdr plugin for fuzzy-searching previous OpenCode sessions by title, project, path, date, or transcript content, with conversation previews and shortcuts to… | `typescript` | 0 | 🔄 2026-08-14 |
| [**🆕 herdr-agents**](https://github.com/dleen/herdr-agents)<br><sub>dleen</sub> | An fzf agent picker for herdr: every agent pane, worst-first, with a session preview and one-key launching. | `coding-agents` `fzf` `python` `terminal` | 0 | 🔄 2026-08-20 |
| [**herdr-command-palette**](https://github.com/fabiogaliano/herdr-command-palette)<br><sub>fabiogaliano</sub> | Herdr向けのファジーコマンドパレット——あらゆるアクションを検索し、ショートカットを確認して実行できる | `command-palette` `fzf` `terminal` `python` | 0 | 🔄 2026-08-10 |
| [**🆕 herdr-plugin-command-palette**](https://github.com/haisi/herdr-plugin-command-palette)<br><sub>haisi</sub> | Fuzzy-searchable command palette for herdr, backed by fzf | `fzf` `python` | 0 | 🔄 2026-08-17 |
| [**herdr-control-panel**](https://github.com/iskwyuki/herdr-control-panel)<br><sub>iskwyuki</sub> | 1つのキーバインド、1つのパネルでherdrを操作——履歴や任意のパスからワークスペースを開き、独自のアクションも追加できる。純粋なbash + fzf製でビルド不要 | `bash` `fzf` `terminal` `shell` | 0 | 🔄 2026-08-11 |
| [**pj-herdr**](https://github.com/josephschmitt/pj-herdr)<br><sub>josephschmitt</sub> | PJピッカーを使って新しいワークスペースを開くHerdrプラグイン | `shell` | 0 | 2026-07-15 |
| [**herdr-finder-reveal**](https://github.com/klukacin/herdr-finder-reveal)<br><sub>klukacin</sub> | Herdrのペイン内のローカルファイルパスをクリックすると、macOSのFinderで表示する | `finder` `ghostty` `macos` `terminal-multiplexer` `shell` | 0 | 🔄 2026-08-10 |
| [**herdr-cull**](https://github.com/krzysztoff1/herdr-cull)<br><sub>krzysztoff1</sub> | herdr内のアイドル状態のエージェントペインを確認して閉じる——fzfによる複数選択、確認なしで閉じることはない | `ai-agents` `claude` `codex` `fzf` `terminal` | 0 | 2026-07-20 |
| [**herdr-shortcut**](https://github.com/matheus3301/herdr-shortcut)<br><sub>matheus3301</sub> | Herdr向けのショートカットタスクピッカー兼コーディングエージェントランチャー | `bubbletea` `claude-code` `codex` `coding-agents` `developer-tools` | 0 | 2026-07-24 |
| [**herdr-omarchy-theme-sync**](https://github.com/maxBRT/herdr-omarchy-theme-sync)<br><sub>maxBRT</sub> | HerdrのUIパレットを、現在使用中のOmarchyテーマに同期させる | `linux` `omarchy` `theme` `python` | 0 | 🔄 2026-08-15 |
| [**herdr-workspaces**](https://github.com/mikedclarke/herdr-workspaces)<br><sub>mikedclarke</sub> | ディレクトリをherdrのワークスペースとして扱う——よく使う場所を登録し、ファジー検索で選ぶと、そこに名前付きワークスペースが作られる | `go` `terminal` `tui` `workspaces` | 0 | 2026-08-02 |
| [**herdr-smart-workspace**](https://github.com/nicolasvasquez/herdr-smart-workspace)<br><sub>nicolasvasquez</sub> | セッション内でワークスペースをすばやく切り替えたり、zoxideからオーバーレイのfzfピッカーで新規作成したりできるHerdrプラグイン | `python` | 0 | 2026-07-02 |
| [**herdr-launcher**](https://github.com/nicolegros/herdr-launcher)<br><sub>nicolegros</sub> | ワークスペースの作成や切り替えをすばやく行える、ファジー検索ディレクトリピッカーを提供するherdrプラグイン | `go` | 0 | 2026-07-15 |
| [**mux-prompter**](https://github.com/phine-apps/mux-prompter)<br><sub>phine-apps</sub> | コンテキストに応じたプロンプトをファジー検索で選び、Herdrやtmuxのペインに注入する | `fzf` `prompt-engineering` `terminal-multiplexer` `tmux` `tmux-plugin` | 0 | 🔄 2026-08-12 |
| [**herdr-repo-picker**](https://github.com/princejoogie/herdr-repo-picker)<br><sub>princejoogie</sub> | OpenTUI製のピッカーから、Gitリポジトリをherdrのワークスペースとして開く | `git` `opentui` `typescript` | 0 | 🔄 2026-08-17 |
| [**herdr-claude-profile**](https://github.com/quinnjr/herdr-claude-profile)<br><sub>quinnjr</sub> | herdrプラグイン：オーバーレイのパレットからclaude-profileのプロファイルを切り替え・管理する | `typescript` | 0 | 2026-07-20 |
| [**herdr-plugins**](https://github.com/shelken/herdr-plugins)<br><sub>shelken</sub> | Herdrプラグインのモノレポ（auto-pi：エリアごとにpiを開く＋セッションピッカー） | `python` | 0 | 2026-07-17 |
| [**herdr-file-picker**](https://github.com/shivammehta25/herdr-file-picker)<br><sub>shivammehta25</sub> | tmux-file-pickerをherdr向けに移植した、いわゆる「vibe coding」製プラグイン | `shell` | 0 | 2026-07-29 |
| [**herdr-workspacex**](https://github.com/willfish/herdr-workspacex)<br><sub>willfish</sub> | Rustネイティブのファジー検索型Herdrワークスペース切り替えツール——zoxideを利用したワークスペース作成に対応 | `rust` `workspace-manager` `zoxide` | 0 | 2026-07-07 |
| [**herdr-fzf-url**](https://github.com/willian/herdr-fzf-url)<br><sub>willian</sub> | フォーカス中のペインから`fzf`でURLを選び、開く・コピーする | `fzf` `shell` | 0 | 2026-07-28 |
| [**herdr-bitwarden**](https://github.com/WillowMist/herdr-bitwarden)<br><sub>WillowMist</sub> | Bitwardenのボルトをファジー検索し、認証情報を貼り付け・コピーする——tmux-bitwardenのherdr移植版 | `bitwarden` `fzf` `terminal` `tmux` `shell` | 0 | 🔄 2026-08-11 |
| [**🆕 herdr-telescope**](https://github.com/zackshen/herdr-telescope)<br><sub>zackshen</sub> | fzf command telescope for herdr: native actions, plugin actions, file finder (@), and live ripgrep search (/) | `fzf` `rust` | 0 | 🔄 2026-08-19 |

<details><summary>この目的にも関係するもの</summary>

- [beyondlex/herdr-recent-navigator](https://github.com/beyondlex/herdr-recent-navigator) — Herdr向けの、最近使ったワークスペース/タブ/ペインの切り替えツール。最近フォーカスしたワークスペース・タブ・ペイン・AIエージェントの一覧をポップアップ表示し、ファジー検索とキーボード操作に対応
- [JacquesvanWyk/herdr-linear](https://github.com/JacquesvanWyk/herdr-linear) — herdrのスプリットペインまたはタブ内で動くfzf駆動のLinearパネル：issue検索、プロジェクトの深掘り、issue作成、ステータス変更ができる
- [adamwangxx/herdr-codex-resume](https://github.com/adamwangxx/herdr-codex-resume) — Open the native Codex resume picker in a new Herdr split with live Herdr context.
- [caoer/ccc-herdr-layout](https://github.com/caoer/ccc-herdr-layout) — herdr向けのビジュアルレイアウトピッカー——1キーでライブプレビューしながら選べる

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-automation"></a>

## 自動化・フック・定期実行

> worktree 作成時やタイミングを決めて、決まった手順を自動で走らせたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-browser**](https://github.com/ogulcancelik/herdr-browser)<br><sub>ogulcancelik</sub> | Herdrのペイン内で実際のChromiumビューを描画し、CDP経由で操作する | `browser` `browser-automation` `cdp` `chromium` `kitty-graphics` | 333 | 2026-07-28 |
| [**herdr-auto-title**](https://github.com/sh1ma/herdr-auto-title)<br><sub>sh1ma</sub> | Claude CodeとCodexの会話内容から、herdrのタブタイトルを自動生成する | `claude-code` `codex` `python` | 50 | 🔄 2026-08-13 |
| [**herdr-automatic-rename**](https://github.com/qu8n/herdr-automatic-rename)<br><sub>qu8n</sub> | herdrのタブをtmux風に自動リネームし、スペース/タブ/エージェントに1〜9のジャンプキー番号を付ける | `shell` | 32 | 🔄 2026-08-18 |
| [**zed-herdr**](https://github.com/ImArtisann/zed-herdr)<br><sub>ImArtisann</sub> | アクティブなHerdRワークスペースを、既存のZedセッションと自動的に同期する | `typescript` | 21 | 🔄 2026-08-17 |
| [**herdr-worktree-setup**](https://github.com/tdi/herdr-worktree-setup)<br><sub>tdi</sub> | herdrプラグイン：worktree作成時にプロジェクトごとのセットアップ手順を実行（mainから.envをコピー、mise trust、direnv allow、依存関係のインストールなど） | `javascript` | 20 | 2026-07-20 |
| [**herdr-auto-pilot**](https://github.com/0xGosu/herdr-auto-pilot)<br><sub>0xGosu</sub> | Herdr APIを介して、稼働中のAIコーディングCLIに代わって自動でプロンプトを送るHerdrプラグイン。あなたの操作から学習するトレーニングモードと、危険/悪意ある操作を防ぐガード機能を搭載。十分に学習させれば「Full-Self Prompting（FSP）」モードで自律動作させられる | `go` | 13 | 🔄 2026-08-18 |
| [**herdr-workflows**](https://github.com/aorumbayev/herdr-workflows)<br><sub>aorumbayev</sub> | herdrの繰り返し作業を宣言的に自動化する | `agentic-ai` `agentic-workflow` `agents` `ai` `claude` | 12 | 🔄 2026-08-19 |
| [**herdr-routines**](https://github.com/mrcndz/herdr-routines)<br><sub>mrcndz</sub> | スケジュールされたルーティンを実行するHerdrプラグイン：cronまたは一定間隔でワークスペースにタブを開き、コマンド実行やエージェント起動を行う | `python` | 10 | 2026-07-18 |
| [**herdr-tab-title**](https://github.com/aarsh21/herdr-tab-title)<br><sub>aarsh21</sub> | Herdr向けの、tmux風タブタイトルの自動設定 | `rust` `terminal` `tmux` | 6 | 2026-07-08 |
| [**herdr-automations**](https://github.com/DnzzL/herdr-automations)<br><sub>DnzzL</sub> | コーディングエージェント向けのcron。プロンプトをスケジュールしておけば、寝ている間にHerdrが新しいgit worktreeでエージェントを起こして実行してくれる。Herdrランタイムのトリガー層として、cron＋プロンプト、MCP設定、重複実行防止、実行履歴、ライブボードを提供 | `ai-agents` `automation` `claude-code` `coding-agents` `cron` | 3 | 🔄 2026-08-19 |
| [**herdr-pane-balancer**](https://github.com/jeph/herdr-pane-balancer)<br><sub>jeph</sub> | ペインの作成・終了・クローズ時に、Herdrのターミナルペインを自動でバランス調整・均等化・タイル配置する | `python` | 3 | 2026-08-02 |
| [**herdr-agent-config-manager**](https://github.com/Phoobobo/herdr-agent-config-manager)<br><sub>Phoobobo</sub> | エージェントのスキル・MCP・プラグイン・フックを検出し一括管理する、CLIとHerdrプラグインのハイブリッド | `python` | 3 | 🔄 2026-08-18 |
| [**tendwire**](https://github.com/plotarmordev/tendwire)<br><sub>plotarmordev</sub> | Herdr向けのローカルAPI：コーディングエージェントをアプリ・自動化・任意のローカルシステムに接続する | `agent-api` `local-first` `python` | 3 | 🔄 2026-08-10 |
| [**herdr-fwd**](https://github.com/go-min/herdr-fwd)<br><sub>go-min</sub> | リモートのHerdrセッション向けに、ループバックポートフォワーディングを自動設定する | `port-forwarding` `ssh` `terminal` `rust` | 2 | 🔄 2026-08-05 |
| [**herdr-js-worktree-bootstrap**](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap)<br><sub>LeonardoTrapani</sub> | JavaScript/TypeScript向けにHerdrのworktreeを自動でブートストラップ——ロックファイルを考慮したインストールと、安全な環境ファイルの復元に対応 | `automation` `bun` `developer-tools` `git-worktree` `javascript` | 2 | 2026-07-15 |
| [**herdr-auto-tab-name**](https://github.com/dev-shimada/herdr-auto-tab-name)<br><sub>dev-shimada</sub> | herdrプラグイン：タブに現在のディレクトリ名を自動で付ける | `javascript` | 1 | 🔄 2026-08-15 |
| [**herdr-auto-update**](https://github.com/dio16/herdr-auto-update)<br><sub>dio16</sub> | herdrプラグイン：インストール済みプラグインに新しいアップストリームのコミットがあるか起動時に確認し、あれば再インストールする | `rust` | 1 | 🔄 2026-08-16 |
| [**say-hook**](https://github.com/HikaruEgashira/say-hook)<br><sub>HikaruEgashira</sub> | Claude Codeのフックイベントを、ElevenLabsのText-to-Speechで読み上げるmacOS向けCLI | `typescript` | 1 | 2026-08-01 |
| [**herdr-shepherd**](https://github.com/mikedclarke/herdr-shepherd)<br><sub>mikedclarke</sub> | herdr向けのスケジュールされたエージェントセッション——ハートビート・cronルーティン・スクリプトを、見えるherdrワークスペースとして起動する | `coding-agents` `cron` `go` `scheduler` `tui` | 1 | 🔄 2026-08-18 |
| [**herdr-plugin**](https://github.com/ppggff/herdr-plugin)<br><sub>ppggff</sub> | 各Herdrペインに適したmacOSの入力方式（IME）を自動的に記憶・復元する | `ime` `input-method` `macos` `python` | 1 | 2026-07-27 |
| [**🆕 herdr-automations**](https://github.com/ram4-dev/herdr-automations)<br><sub>ram4-dev</sub> | Herdr向けの宣言的なcron・インターバル・イベント自動化 | `automation` `bun` `typescript` | 1 | 🔄 2026-08-13 |
| [**🆕 herdr-nixos-vm**](https://github.com/Slimydog21/herdr-nixos-vm)<br><sub>Slimydog21</sub> | The NixOS VM pane for herdr — boot, stop, watch, and ssh into your Hashimoto-style dev VM. Requires the nixos-vm kit. | `shell` | 1 | 🔄 2026-08-18 |
| [**herdr-labels**](https://github.com/Angel-O/herdr-labels)<br><sub>Angel-O</sub> | 手動で付けたラベルは維持したまま、タブに自動で名前と番号を付けるHerdrプラグイン | `rust` | 0 | 🔄 2026-08-17 |
| [**herdr-plugin-orbstack**](https://github.com/AsgardMuninn/herdr-plugin-orbstack)<br><sub>AsgardMuninn</sub> | OrbStackのLinuxマシンをherdrのワークスペースとして開く（直接シェル接続、SSHフォールバック、自動同期） | `python` | 0 | 🔄 2026-08-11 |
| [**🆕 herdr-teams-notify**](https://github.com/donghaolicd/herdr-teams-notify)<br><sub>donghaolicd</sub> | Herdr plugin for bounded Microsoft Teams agent lifecycle notifications | `automation` `microsoft-teams` `notifications` `javascript` | 0 | 🔄 2026-08-15 |
| [**herdr-context-namer**](https://github.com/eabadim/herdr-context-namer)<br><sub>eabadim</sub> | OpenCode経由でペインのコンテキストから、Herdrのタブ・ワークスペース名を自動生成する | `opencode` `python` | 0 | 🔄 2026-08-06 |
| [**herdr-pane-name**](https://github.com/go-min/herdr-pane-name)<br><sub>go-min</sub> | ターミナルセッションのペインに自動で名前を付けるHerdrプラグイン | `pane-naming` `terminal` `terminal-multiplexer` `rust` | 0 | 🔄 2026-08-16 |
| [**herdr-plugin-auto-rename**](https://github.com/khatriafaz/herdr-plugin-auto-rename)<br><sub>khatriafaz</sub> | Piセッションへの最初のプロンプトから、新しいHerdrのワークスペースとGitブランチを自動でリネームする | `typescript` | 0 | 🔄 2026-08-14 |
| [**herdr-review-loop**](https://github.com/mikhail-angelov/herdr-review-loop)<br><sub>mikhail-angelov</sub> | herdrのワークスペース内でエージェント同士が自動的に相互レビューする——1体が書き、もう1体がレビューし、これを繰り返す | `terminal` `go` | 0 | 🔄 2026-08-16 |
| [**🆕 herdr-unrecoverable**](https://github.com/neilwashere/herdr-unrecoverable)<br><sub>neilwashere</sub> | Herdr watchdog that recovers Pi coding-agent sessions from terminal provider errors | `pi-coding-agent` `javascript` | 0 | 🔄 2026-08-14 |
| [**🆕 herdr-pane-equalizer**](https://github.com/shanefully-done/herdr-pane-equalizer)<br><sub>shanefully-done</sub> | Resize herdr panes equally; automatically or manually. | `javascript` | 0 | 🔄 2026-08-20 |
| [**herdr-worktreeinclude**](https://github.com/untalfranfernandez/herdr-worktreeinclude)<br><sub>untalfranfernandez</sub> | 新しいgit worktreeに必要なgitignore対象のローカルファイル（.env、settings.local.json、フィクスチャなど）を自動配置するHerdrプラグイン。.worktreeincludeファイルにgitignore構文で一度宣言しておけば、Herdrが作るworktreeすべてに自動反映… | `claude-code` `dotenv` `git-worktree` `worktree` | 0 | 2026-07-29 |
| [**herdr-padio**](https://github.com/vgreg/herdr-padio)<br><sub>vgreg</sub> | herdrでフォーカスされているペインのアプリに応じて、PadIOコントローラーのモードを自動切り替えする | `game-controller` `macos` `padio` `python` | 0 | 2026-08-02 |
| [**herdr-agent-title-sync**](https://github.com/winoooops/herdr-agent-title-sync)<br><sub>winoooops</sub> | Claude Code・Codex・Kimi Code・OpenCodeなど各種コーディングエージェント向けの、Herdrペインタイトル自動同期 | `developer-tools` `typescript` | 0 | 🔄 2026-08-15 |
| [**numberer-manager**](https://github.com/yuritada/numberer-manager)<br><sub>yuritada</sub> | ワークスペースとタブのラベルに、現在のリスト上の位置（例：「1: space」「1: tab」）を自動で先頭に付ける、軽量なHerdrプラグイン | `python` | 0 | 2026-07-25 |
| [**herdr-pane-restart**](https://github.com/zap0xfce2/herdr-pane-restart)<br><sub>zap0xfce2</sub> | サーバー起動時に、名前付きペインで設定済みのコマンドを実行する | `python` | 0 | 🔄 2026-08-10 |
| [**herdr-booking-task-plugin**](https://github.com/zerodice0/herdr-booking-task-plugin)<br><sub>zerodice0</sub> | macOSとLinuxで、Herdrエージェントへのプロンプトやローカルのコマンド実行をスケジュールする | `golang` `scheduler` `go` | 0 | 2026-08-03 |

<details><summary>この目的にも関係するもの</summary>

- [freethinkel/herdr-plugin-git-worktree-hooks](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks) — git worktreeの作成/削除時にシェルコマンドを実行する——どのリポジトリの外にも置ける、全プロジェクト共通の1つのYAML設定
- [timofey-TK/herdr-worktree-hooks](https://github.com/timofey-TK/herdr-worktree-hooks) — herdrプラグイン：git worktreeの作成・オープン・削除時に、カスタムのセットアップ/後始末コマンドを実行する
- [miko-misa/herdr-portfwd](https://github.com/miko-misa/herdr-portfwd) — リモートマシン上のコーディングエージェント向けの自動SSHポートフォワーディング——エージェントが出力したlocalhost URLをCtrl+クリックすると、同じポートで手元のマシンにページが開く。Herdrプラグイン
- [m1sk9/herdr-worktree-hooks-plugin](https://github.com/m1sk9/herdr-worktree-hooks-plugin) — Herdrのworktreeに、カスタマイズ可能なフックを追加するプラグイン
- [Newt6611/herdr-tab-title](https://github.com/Newt6611/herdr-tab-title) — Herdr Tab Titleは、「1. Codex」「2. Terminal」のような、ワークスペース単位できれいに番号付けされた名前にHerdrのタブを自動リネームする。フォーマットはカスタマイズ可能

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-session"></a>

## セッション保存・復元

> 作業を閉じても、あとで同じ状態から再開したい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**session-digger**](https://github.com/taxueseek/session-digger)<br><sub>taxueseek</sub> | 複数環境をまたいだセッション履歴の掘り出しとナレッジ管理。ログを分析。Claude/Grok/Kimi Code/Codex/WorkBuddy/Trae CNなど主要な環境に対応 | `python` | 15 | 2026-07-21 |
| [**herdr-resurrect**](https://github.com/ntindle/herdr-resurrect)<br><sub>ntindle</sub> | herdr版tmux-resurrect——ワークスペース・タブ・ペイン・作業ディレクトリ・実行中のプログラムやエージェントをスナップショットし、クラッシュや再起動後に復元する | `crash-recovery` `session-manager` `terminal-multiplexer` `tmux-resurrect` `javascript` | 14 | 2026-07-12 |
| [**herdr-notes**](https://github.com/alexarthurs/herdr-notes)<br><sub>alexarthurs</sub> | herdr向けの永続化されたMarkdownメモペイン——ワークスペースごとに1つのメモ、プレビュー表示＋編集モード、自動保存で再起動後も残る | `markdown` `notes` `ratatui` `rust` `terminal` | 11 | 2026-07-25 |
| [**herdr-claude-auto-retry**](https://github.com/mo-arvan/herdr-claude-auto-retry)<br><sub>mo-arvan</sub> | AnthropicのレートリミットをやりすごしてClaude Codeを自動的に再開する、herdrネイティブな仕組み——tmuxもシェルラッパーも不要 | `javascript` | 11 | 2026-07-16 |
| [**herdr-session-parker**](https://github.com/iviaxpow3r/herdr-session-parker)<br><sub>iviaxpow3r</sub> | ペイン/タブを一時保管し、対応するエージェントセッションを後で復元できるHerdrプラグイン | `agent-tools` `python` | 9 | 2026-07-03 |
| [**herdr-agent-inbox**](https://github.com/douglascorrea/herdr-agent-inbox)<br><sub>douglascorrea</sub> | herdrのコーディングエージェント用インボックス——セッションタイトル、既読/未読管理、実行時間、ワークスペース単位の集計、再開可能なチャット履歴 | `ai-agents` `terminal` `python` | 7 | 2026-07-28 |
| [**herdr-assist**](https://github.com/walcew/herdr-assist)<br><sub>walcew</sub> | AIコーディングエージェント向けターミナルマルチプレクサHerdrのための、物理デスクパネル——セッションの状態を色で表示し、エージェントが判断を仰ぐために止まるとベルを鳴らす。ESP32-S3 + LVGL、ビルド済みファームウェア付き | `ai-agents` `claude-code` `coding-agents` `embedded` `esp-idf` | 5 | 🔄 2026-08-17 |
| [**herdr-pane-id-labeler**](https://github.com/4Born/herdr-pane-id-labeler)<br><sub>4Born</sub> | ペインのラベルを、w1:p2のような公開ペインIDと同期させ続けるHerdrプラグイン | `developer-tools` `terminal` `javascript` | 2 | 2026-07-26 |
| [**herdr-hibernate**](https://github.com/bengemine/herdr-hibernate)<br><sub>bengemine</sub> | Herdr上のアイドル状態のコーディングエージェントペイン（Claude Code、Codex、Grok）をハイバネート——メモリを解放し、Enterキーで元のセッションをそのまま再開できる | `claude-code` `python` | 2 | 2026-08-03 |
| [**herdr-synchronize-panes**](https://github.com/furuhashin/herdr-synchronize-panes)<br><sub>furuhashin</sub> | Herdrプラグイン：現在のタブ内のすべてのペインに1つのコマンドを一斉送信する（tmuxのsynchronize-panes風） | `javascript` | 2 | 2026-07-14 |
| [**herdr-oh-my-agent**](https://github.com/GavinTomlins/herdr-oh-my-agent)<br><sub>GavinTomlins</sub> | oh-my-openagentのサブエージェント委任をそれぞれ専用のHerdrペイン/タブにミラー——セッション状態とスクロールバックを保持したままライブ表示 | `typescript` | 2 | 2026-07-31 |
| [**herdr_sync**](https://github.com/kamaaina/herdr_sync)<br><sub>kamaaina</sub> | herdrのペインを同期する | `zig` | 2 | 2026-07-01 |
| [**herdr-e2b**](https://github.com/tomasvarga/herdr-e2b)<br><sub>tomasvarga</sub> | 必要なときにgit worktreeを新しいE2Bクラウドサンドボックスへミラーする——未コミットの変更も含めたスナップショットをアップロードするだけで、pushやcloneは不要なherdrプラグイン | `cli` `cloud-dev` `e2b` `git-worktree` `sandbox` | 2 | 2026-07-18 |
| [**herdr-thread-to-tab**](https://github.com/toyamarinyon/herdr-thread-to-tab)<br><sub>toyamarinyon</sub> | 単一ペインのHerdrタブラベルを、Claude CodeやCodexのスレッドタイトルと同期させる | `rust` | 2 | 🔄 2026-08-06 |
| [**herdr-todos-windows**](https://github.com/aclima01/herdr-todos-windows)<br><sub>aclima01</sub> | herdrエージェントのタスクリスト（TaskCreate/TaskUpdate）をリアルタイムに映し出すパネル。エージェントの計画を追える | `powershell` | 1 | 2026-07-22 |
| [**herdr-undo-close**](https://github.com/pedroloch/herdr-undo-close)<br><sub>pedroloch</sub> | ブラウザのCmd+Shift+Tのように、herdrで閉じたタブを復元——ラベル、分割比率を含むペイン構成、各ペインの作業ディレクトリ、タブの位置までまとめて復元する | `python` | 1 | 2026-07-30 |
| [**🆕 attic**](https://github.com/TheThoughtagen/attic)<br><sub>TheThoughtagen</sub> | Auto-closes idle AI coding sessions, but archives each one first so you can restore it. | `claude-code` `developer-tools` `python` `session-management` `tui` | 1 | 🔄 2026-08-14 |
| [**🆕 herdr-codex-resume**](https://github.com/adamwangxx/herdr-codex-resume)<br><sub>adamwangxx</sub> | Open the native Codex resume picker in a new Herdr split with live Herdr context. | `codex-cli` `terminal` `shell` | 0 | 🔄 2026-08-15 |
| [**herdr-agent-resume**](https://github.com/Angel-O/herdr-agent-resume)<br><sub>Angel-O</sub> | AIエージェントのセッションをスムーズに再開できるよう、再開用コマンドを挿入またはコピーするHerdrプラグイン | `rust` | 0 | 🔄 2026-08-15 |
| [**herdr-suspend-workspace**](https://github.com/asermax/herdr-suspend-workspace)<br><sub>asermax</sub> | herdrのワークスペースをサスペンド——レイアウトとエージェントをスナップショットして閉じ、あとでポップアップから選んで復元できる | `typescript` | 0 | 2026-07-31 |
| [**🆕 buzzr**](https://github.com/candypoets/buzzr)<br><sub>candypoets</sub> | Mirror live Herdr spaces and agents into Buzz channels with Nostr identities and mention routing. | `agents` `buzz` `nostr` `rust` | 0 | 🔄 2026-08-14 |
| [**herdr-plugin-session-pruner**](https://github.com/Gareth-Rouse/herdr-plugin-session-pruner)<br><sub>Gareth-Rouse</sub> | herdrプラグイン：ワークスペースの最終使用日時を記録してSpacesのサイドバーに経過時間を表示し、使われていないワークスペースをセッション復元の対象から外す | `terminal-multiplexer` `shell` | 0 | 🔄 2026-08-07 |
| [**herdr-flakes**](https://github.com/iQua/herdr-flakes)<br><sub>iQua</sub> | Herdr向けのFlakesプラグイン——Flakesの実行状況をローカルのHerdrセッションにミラーし、操作できる | `javascript` | 0 | 2026-07-22 |
| [**herdr-codex-app**](https://github.com/jievince/herdr-codex-app)<br><sub>jievince</sub> | Herdrをターミナル中心のCodexアプリに変える——プロジェクトを同期し、チャットを再開できる | `codex` `terminal` `javascript` | 0 | 🔄 2026-08-11 |
| [**herdr-plugin-vault**](https://github.com/Joxtacy/herdr-plugin-vault)<br><sub>Joxtacy</sub> | herdrのポップアップから過去のClaude Codeセッションを閲覧し、選んだものを新しいタブで再開する | `shell` | 0 | 🔄 2026-08-11 |
| [**🆕 herdr-layout**](https://github.com/noviadi/herdr-layout)<br><sub>noviadi</sub> | Herdrのペインレイアウトを保存して再現する。Herdrターミナルマルチプレクサ向けのコンパニオンプラグイン（tmux-resurrect風） | `cli` `terminal` `tmux-resurrect` `shell` | 0 | 🔄 2026-08-13 |
| [**herdr-stash**](https://github.com/victor-software-house/herdr-stash)<br><sub>victor-software-house</sub> | Herdrのワークスペースをスタッシュ——エージェントを停止しつつ構成と会話内容は保持し、あとでクリック可能な2カラムポップアップから復元できる | `rust` `terminal` `tui` | 0 | 2026-07-29 |
| [**🆕 herdr-event-log**](https://github.com/waynewu411/herdr-event-log)<br><sub>waynewu411</sub> | Herdr plugin: logs pane.agent_status_changed (and future event types) to a durable, cursor-resumable global log any parent agent can tail. | `go` | 0 | 🔄 2026-08-15 |
| [**live-sync-panes**](https://github.com/wg1k/live-sync-panes)<br><sub>wg1k</sub> | Herdrプラグイン：タブ内のすべてのペインにコマンドを一斉送信、またはキー入力をリアルタイム同期する | `javascript` | 0 | 🔄 2026-08-11 |

<details><summary>この目的にも関係するもの</summary>

- [nicosuave/memex](https://github.com/nicosuave/memex) — Search Claude Code, Codex, Pi, OpenCode, Github Copilot & Cursor transcripts. Resume sessions. Track tokens.
- [KokiKono/herdr-kanban](https://github.com/KokiKono/herdr-kanban) — タスクをherdrのタブに紐付けるターミナル上のカンバンボード。SQLiteに保存される
- [afogel/shepherdr](https://github.com/afogel/shepherdr) — 委任したコーディングエージェントを、監視・再開・引き取りができる可視化されたherdrのペインに追い込むherdrプラグイン
- [AkashJana18/herdr-scratch](https://github.com/AkashJana18/herdr-scratch) — Herdr向けの永続化されたスクラッチパッド。フローティングのユーティリティペインへの足がかりとなる
- [voodootikigod/adlc-herdr](https://github.com/voodootikigod/adlc-herdr) — ADLC向けのherdrプラグイン——ペインごとのフェーズ/チケット/ゲートの状態、バックログボード、ゲートアクション、adlc-fleetの実行状況の可視化に対応。voodootikigod/adlc/plugins…
- [blaxel-ai/herdr-blaxel-sandbox-plugin](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin) — Herdrから、永続化されたBlaxel Sandbox上でコーディングエージェントを実行する
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — JavaScript/TypeScript向けにHerdrのworktreeを自動でブートストラップ——ロックファイルを考慮したインストールと、安全な環境ファイルの復元に対応
- [ppggff/herdr-plugin](https://github.com/ppggff/herdr-plugin) — 各Herdrペインに適したmacOSの入力方式（IME）を自動的に記憶・復元する
- [shadowfax92/herdr-scratch](https://github.com/shadowfax92/herdr-scratch) — 非公開のtmuxセッションを裏側で使う、永続化されたペインごとのHerdrスクラッチポップアップ
- [damianpoole/herdr-opencode-sessions](https://github.com/damianpoole/herdr-opencode-sessions) — A Herdr plugin for fuzzy-searching previous OpenCode sessions by title, project, path, date, or transcript co…

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-naming"></a>

## タイトル・命名・見た目

> タブ名やターミナルタイトルを自動で分かりやすくしたい / 見た目を変えたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-tab-smart-rename**](https://github.com/iurysza/herdr-tab-smart-rename)<br><sub>iurysza</sub> | Herdrのワークスペース名・タブ名を、コンテキストに応じて自動生成する | `ai` `bun` `terminal` `typescript` | 51 | 🔄 2026-08-19 |
| [**herdr-window-title-sync**](https://github.com/rjyo/herdr-window-title-sync)<br><sub>rjyo</sub> | ワークスペース・タブ・エージェントセッションからターミナルのタイトルを同期する（Moshiと併用可） | `moshi` `terminal-title` `javascript` | 34 | 2026-06-26 |
| [**herdr-flock**](https://github.com/ragamo/herdr-flock)<br><sub>ragamo</sub> | AIコーディングエージェントを、見下ろし視点の牧場に住むピクセルアートの羊として可視化するherdrプラグイン | `cli` `ratatui` `rust` `tui` | 24 | 2026-07-11 |
| [**herdr-claude-session-title**](https://github.com/bcihanc/herdr-claude-session-title)<br><sub>bcihanc</sub> | Herdrプラグイン：Claude Codeのセッションタイトル（/renameまたは自動要約）をherdrのペインのメタデータタイトルに反映する | `shell` | 5 | 2026-07-11 |
| [**herdr-pet**](https://github.com/allmight-ai/herdr-pet)<br><sub>allmight-ai</sub> | Herdr向けのコンパニオンV-Pet——あなたのコーディングエージェントの様子を映し出す | `companion` `rust` `v-pet` | 4 | 🔄 2026-08-20 |
| [**herdr-in-your-face**](https://github.com/JYasha11/herdr-in-your-face)<br><sub>JYasha11</sub> | AIエージェントをブロックされたまま放置すると、巨大なASCIIアートの顔が叫んでくる。無視するほど段階的にエスカレートする | `javascript` | 4 | 2026-07-10 |
| [**herdr-auto-namer**](https://github.com/kakigakki/herdr-auto-namer)<br><sub>kakigakki</sub> | herdr向けのChatGPT風自動命名：エージェントにはClaudeのセッションタイトルを、ワークスペースには作業ディレクトリ名を付ける | `claude-code` `python` | 4 | 2026-07-12 |
| [**herdr-tab-rename**](https://github.com/lmilojevicc/herdr-tab-rename)<br><sub>lmilojevicc</sub> | 各Herdrタブを、フォーカス中のペインの作業ディレクトリ名に自動でリネームする。手動でリネームしたタブはそのまま残る | `go` | 4 | 2026-07-31 |
| [**herdr-ghostty-tab-title**](https://github.com/wjarka/herdr-ghostty-tab-title)<br><sub>wjarka</sub> | herdrプラグイン：Ghosttyのタブタイトルに、エージェントの状態別件数（ブロック中/完了/作業中/アイドル）を色分けして表示する | `ai-agents` `ghostty` `terminal` `python` | 4 | 2026-08-04 |
| [**herdr-town**](https://github.com/Efeguclu1/herdr-town)<br><sub>Efeguclu1</sub> | Herdrのコーディングエージェントを、8bit風の街として眺める。街を離れずに、エージェントの発言を読んで返答できる | `ai-agents` `pixel-art` `terminal` `tui` `javascript` | 3 | 🔄 2026-08-08 |
| [**herdr-questmancer**](https://github.com/opsydyn/herdr-questmancer)<br><sub>opsydyn</sub> | Herdrのコーディングエージェントのための、居心地の良い16bit風冒険者ギルド。作業中のエージェントはダンジョンに潜り、ブロックされたエージェントは助言を求め、完了した仕事は戦利品を持って帰ってくる | `coding-agents` `pixel-art` `ratatui` `tui` `rust` | 3 | 🔄 2026-08-11 |
| [**herdr-nerd-font-tab-name**](https://github.com/rohankewal/herdr-nerd-font-tab-name)<br><sub>rohankewal</sub> | herdrのタブにNerd Fontアイコンを付ける——joshmedeski/tmux-nerd-font-window-nameのherdr移植版 | `nerd-fonts` `python` `terminal` `tui` | 3 | 2026-07-31 |
| [**herdr-titles**](https://github.com/davidolrik/herdr-titles)<br><sub>davidolrik</sub> | 追従し続けるHerdrのタイトル。herdr-titlesは、AIエージェントのライブなセッションタイトルも含め、実際に動いているものに合わせてタブとウィンドウの名前を付け、ワークスペース・タブ・エージェントの要対応件数・シェル環境から、小さなHCLテンプレート経由でウィンドウタイトルを組み立てる。即座に反映され、C… | `ai-assisted` `go` | 2 | 🔄 2026-08-18 |
| [**herdr-english-coach**](https://github.com/GranamyrBR/herdr-english-coach)<br><sub>GranamyrBR</sub> | herdrプラグイン：色分けされた英語修正ボード——作業中、コーディングエージェントが文法や開発用語の修正をリアルタイムでサイドペインに記録する | `english` `language-learning` `shell` | 2 | 2026-07-06 |
| [**herdr-ai-tab-name**](https://github.com/ndom91/herdr-ai-tab-name)<br><sub>ndom91</sub> | ローカルLLMを使ってHerdrのタブ名を自動命名する | `local-llm` `python` | 2 | 🔄 2026-08-05 |
| [**herdr-powershell-title-sync**](https://github.com/aclima01/herdr-powershell-title-sync)<br><sub>aclima01</sub> | window-title-syncのWindows/PowerShell版：ターミナルのタイトルを、フォーカス中のherdrセッションに同期する | `powershell` | 1 | 2026-07-20 |
| [**herdr-git-tab-name**](https://github.com/blurname/herdr-git-tab-name)<br><sub>blurname</sub> | フォーカス中のペインのGitブランチ名にタブをリネームするHerdrプラグイン | `shell` | 1 | 2026-07-06 |
| [**herdr-hermes-session-title**](https://github.com/btorresgil/herdr-hermes-session-title)<br><sub>btorresgil</sub> | Hermes Agentのセッションタイトルを、Herdrのサイドバーに表示する | `python` | 1 | 🔄 2026-08-07 |
| [**herdr-tab-title-sync**](https://github.com/lucasleon2107/herdr-tab-title-sync)<br><sub>lucasleon2107</sub> | AIエージェントの会話タイトルにタブ名を同期するherdrプラグイン | `ai-agents` `claude-code` `terminal` `tmux` `shell` | 1 | 2026-08-04 |
| [**herdr-nerd-font-tab-name-windows**](https://github.com/Only-Moon/herdr-nerd-font-tab-name-windows)<br><sub>Only-Moon</sub> | herdr-nerd-font-tab-nameのWindows移植版：herdrのタブにNerd Fontアイコンを表示し、Windows・macOS・Linuxをクロスプラットフォームでサポート、フォルダに応じたアイコン解決にも対応 | `herdr-windows` `icons` `nerd-fonts` `python` `title` | 1 | 🔄 2026-08-10 |
| [**herdr-tab-renamer**](https://github.com/ryanlewis/herdr-tab-renamer)<br><sub>ryanlewis</sub> | herdrプラグイン：タブに実際の中身（エージェントのセッションタイトルやシェルのディレクトリ）に応じたラベルを付ける | `javascript` | 1 | 🔄 2026-08-08 |
| [**🆕 herdr-claude-tab-title**](https://github.com/tmn73/herdr-claude-tab-title)<br><sub>tmn73</sub> | 各Claude Codeのセッションタイトルを、対応するHerdrのタブに反映する | `claude-code` `tabs` `terminal` `typescript` | 1 | 🔄 2026-08-13 |
| [**herdr-llm-summary-header**](https://github.com/dnf0/herdr-llm-summary-header)<br><sub>dnf0</sub> | herdrプラグイン：エージェントが完了すると、LLMによる一行要約をペインのタイトルに書き込む | `javascript` | 0 | 2026-08-03 |
| [**herdr-title-sync**](https://github.com/elKei24/herdr-title-sync)<br><sub>elKei24</sub> | herdrプラグイン：各エージェントのターミナルタイトルを、そのタブのラベルに反映する | `python` | 0 | 🔄 2026-08-11 |
| [**herdr-tab-session-name-sync**](https://github.com/itayo-m/herdr-tab-session-name-sync)<br><sub>itayo-m</sub> | エージェントのセッション名を、herdrのタブとペインのタイトルに同期する | `developer-tools` `github-copilot` `terminal` `javascript` | 0 | 2026-08-03 |
| [**🆕 herdr-tab-numbers**](https://github.com/kokatsu/herdr-tab-numbers)<br><sub>kokatsu</sub> | Prefix each tab name with its switch_tab position | `shell` | 0 | 🔄 2026-08-18 |
| [**herdr-window-title**](https://github.com/mackt/herdr-window-title)<br><sub>mackt</sub> | herdr向けの設定可能な外部ターミナルタイトル——テンプレート駆動でセッションを認識し、エージェントの状態（ブロック/完了/作業中）をリアルタイム表示する | `rust` | 0 | 2026-08-03 |
| [**🆕 herdr-agent-smart-rename**](https://github.com/malone-c/herdr-agent-smart-rename)<br><sub>malone-c</sub> | Names each herdr agent session from what it is actually doing | `python` | 0 | 🔄 2026-08-14 |
| [**herdr-machine-title**](https://github.com/mikevalstar/herdr-machine-title)<br><sub>mikevalstar</sub> | herdrプラグイン：外側のターミナルタイトルを「herdr@<ホスト名>・<ワークスペース>」に固定する | `shell` | 0 | 2026-07-02 |
| [**herdr-tab-title**](https://github.com/Newt6611/herdr-tab-title)<br><sub>Newt6611</sub> | Herdr Tab Titleは、「1. Codex」「2. Terminal」のような、ワークスペース単位できれいに番号付けされた名前にHerdrのタブを自動リネームする。フォーマットはカスタマイズ可能 | `rust` | 0 | 2026-07-09 |
| [**tab-blank-number**](https://github.com/riq0h/tab-blank-number)<br><sub>riq0h</sub> | herdrのデフォルトの数字タブラベル（1、2、3…）を空白にするherdrプラグイン | `javascript` | 0 | 2026-07-19 |
| [**tab-process-name**](https://github.com/riq0h/tab-process-name)<br><sub>riq0h</sub> | 各タブにフォアグラウンドで動いているプロセス名をラベル表示するherdrプラグイン——tmuxのautomatic-rename相当の機能をherdr向けに | `javascript` | 0 | 2026-07-19 |
| [**herdr-workspace-renamer**](https://github.com/ryanlewis/herdr-workspace-renamer)<br><sub>ryanlewis</sub> | herdrプラグイン：エージェントのセッション名をワークスペースのラベルに同期する | `javascript` | 0 | 🔄 2026-08-08 |
| [**herdr-codex-session-title**](https://github.com/sergeybataev/herdr-codex-session-title)<br><sub>sergeybataev</sub> | Codexのチャットタイトルをエージェント名に反映するHerdrプラグイン | `codex` `python` | 0 | 2026-08-01 |
| [**herdr-title-wrap**](https://github.com/T0mSIlver/herdr-title-wrap)<br><sub>T0mSIlver</sub> | herdrプラグイン：Claude Codeのセッションタイトルをサイドバーの複数行に折り返し、サイドバー幅に自動フィットさせる | `python` | 0 | 🔄 2026-08-06 |
| [**herdr-agent-session-title**](https://github.com/the-inconvenience-store/herdr-agent-session-title)<br><sub>the-inconvenience-store</sub> | Claude CodeまたはCodexのセッションタイトル（/renameまたは自動要約）を、herdrペインのメタデータタイトルに反映するHerdrプラグイン | `python` | 0 | 2026-07-30 |
| [**herdr-ghostty-theme-sync**](https://github.com/themuuln/herdr-ghostty-theme-sync)<br><sub>themuuln</sub> | herdrのテーマとサイドバーの配色を、使用中のGhosttyのテーマに合わせる——herdr再起動をまたいでもサイドバーのトークン（配色設定）を維持する。herdr.dev製プラグイン | `python` | 0 | 🔄 2026-08-12 |
| [**tabby**](https://github.com/yersonargotev/tabby)<br><sub>yersonargotev</sub> | フォーカス中のタブに、重要なコマンドまたは作業ディレクトリ名でラベルを付けるHerdrプラグイン | `rust` | 0 | 🔄 2026-08-19 |
| [**herdr-auto-session-title**](https://github.com/zhangzujian/herdr-auto-session-title)<br><sub>zhangzujian</sub> | 簡潔なHerdrペインタイトルを生成し、ネイティブのCodexスレッド名と同期する | `javascript` | 0 | 2026-07-30 |

<details><summary>この目的にも関係するもの</summary>

- [sh1ma/herdr-auto-title](https://github.com/sh1ma/herdr-auto-title) — Claude CodeとCodexの会話内容から、herdrのタブタイトルを自動生成する
- [qu8n/herdr-automatic-rename](https://github.com/qu8n/herdr-automatic-rename) — herdrのタブをtmux風に自動リネームし、スペース/タブ/エージェントに1〜9のジャンプキー番号を付ける
- [wyattjoh/herdr-plugin-renamer](https://github.com/wyattjoh/herdr-plugin-renamer) — エージェントへの最初のプロンプトから、自動生成されたherdrのworktreeブランチとワークスペースをリネームする（デバイス上のApple FoundationModelsまたはCodexを利用）
- [aarsh21/herdr-tab-title](https://github.com/aarsh21/herdr-tab-title) — Herdr向けの、tmux風タブタイトルの自動設定
- [maedana/herdr-whereami](https://github.com/maedana/herdr-whereami) — 今どこにいるかを示すよう、タブを自動でリネームするHerdrプラグイン——gitリポジトリ内なら「リポジトリ名/ブランチ名」のように表示
- [qintmb/herdr-theme-picker](https://github.com/qintmb/herdr-theme-picker) — Theme picker for herdr UI based terminalcolors scheme and your customization.
- [dev-shimada/herdr-auto-tab-name](https://github.com/dev-shimada/herdr-auto-tab-name) — herdrプラグイン：タブに現在のディレクトリ名を自動で付ける
- [suisya-systems/herdr-agent-office](https://github.com/suisya-systems/herdr-agent-office) — エージェント群をピクセルアートのオフィスとして表示するherdrプラグイン。誰が作業中で、誰が詰まっているかが分かり、そこにジャンプできる
- [filoozom/herdr-title](https://github.com/filoozom/herdr-title) — 選択中のworktreeとエージェントの活動状況を、ターミナルのタブタイトルに表示するHerdrプラグイン
- [go-min/herdr-pane-name](https://github.com/go-min/herdr-pane-name) — ターミナルセッションのペインに自動で名前を付けるHerdrプラグイン
- [KazBrekker1/herdr-hasr](https://github.com/KazBrekker1/herdr-hasr) — Hasr（حصر — 「列挙・完全な集計」の意）——herdr向けのgoto風ポップアップ切り替えツール：エージェント・タブ・スペースの切り替え・リネーム・削除・作成ができ、完了状況もリアルタイムに追跡する
- [khatriafaz/herdr-plugin-auto-rename](https://github.com/khatriafaz/herdr-plugin-auto-rename) — Piセッションへの最初のプロンプトから、新しいHerdrのワークスペースとGitブランチを自動でリネームする
- [maxBRT/herdr-omarchy-theme-sync](https://github.com/maxBRT/herdr-omarchy-theme-sync) — HerdrのUIパレットを、現在使用中のOmarchyテーマに同期させる
- [ralphilius/herdr-pr-tab-renamer](https://github.com/ralphilius/herdr-pr-tab-renamer) — 検出したプルリクエスト番号でタブ名を変更するHerdrプラグイン
- [winoooops/herdr-agent-title-sync](https://github.com/winoooops/herdr-agent-title-sync) — Claude Code・Codex・Kimi Code・OpenCodeなど各種コーディングエージェント向けの、Herdrペインタイトル自動同期

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-text"></a>

## テキスト・URL 抽出

> 画面に出ている文字列やパス・URL を、マウスなしで拾いたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-pluck**](https://github.com/rmarganti/herdr-pluck)<br><sub>rmarganti</sub> | Herdrのペインからパターンにマッチした文字列をすばやくコピーする | `rust` | 20 | 🔄 2026-08-07 |
| [**herdr-tiny-fingers**](https://github.com/hotchpotch/herdr-tiny-fingers)<br><sub>hotchpotch</sub> | Herdr向けの、tmux-fingers風の画面上コピーヒント表示 | `tools` `rust` | 6 | 2026-08-04 |
| [**herdr-fingers**](https://github.com/hitaishi2222/herdr-fingers)<br><sub>hitaishi2222</sub> | Fingers to clipboard：現在のペインから情報を選び取る、スマートなオーバーレイ | `python` | 3 | 2026-07-16 |
| [**herdr-copy-search**](https://github.com/qq88976321/herdr-copy-search)<br><sub>qq88976321</sub> | herdrのスクロールバックに対する正規表現・copycatパターン検索とextraktoによるトークン抽出、tmux風のコピーモード（OSC 52）に対応 | `copy-mode` `rust` `terminal` `tmux` | 3 | 2026-08-04 |
| [**herdr-agent-copy-paste-fork**](https://github.com/calebcauthon/herdr-agent-copy-paste-fork)<br><sub>calebcauthon</sub> | コピー＆ペーストだけでフォークできる、あるいはホットキーで新しいペインにフォークする | `claude-code` `codex` `shell` | 2 | 2026-07-24 |
| [**herdr-paste-image**](https://github.com/ddfonseca/herdr-paste-image)<br><sub>ddfonseca</sub> | クリップボードの画像をherdrのペインにファイルパスとして貼り付ける——tmux-paste-imageのherdr移植版 | `shell` | 2 | 2026-07-30 |
| [**herdr-s3-clipboard**](https://github.com/jagzmz/herdr-s3-clipboard)<br><sub>jagzmz</sub> | S3互換ストレージを使い、Herdrからクリップボードの画像を再利用可能な公開URLまたは署名付きURLとして公開する | `aws-s3` `clipboard` `cloudflare-r2` `developer-tools` `image-publishing` | 2 | 2026-07-16 |
| [**herdr-scrollback-capture**](https://github.com/alexjsp/herdr-scrollback-capture)<br><sub>alexjsp</sub> | フォーカス中のペインのスクロールバックを、HTMLまたはテキストとしてデスクトップに保存するHerdrプラグイン | `shell` | 1 | 2026-06-30 |
| [**herdr-leap**](https://github.com/RooseveltAdvisors/herdr-leap)<br><sub>RooseveltAdvisors</sub> | Herdrのターミナルマルチプレクサ向けの、EasyMotion/leap風の文字ジャンプ＋選択コピー | `easymotion` `rust` `terminal` `tui` | 1 | 2026-07-24 |
| [**herdr-copy-hints**](https://github.com/rotemb-wond/herdr-copy-hints)<br><sub>rotemb-wond</sub> | Herdr向けの、tmux-fingers風キーボードコピーヒント：パス・GitのSHA・URLなどに対応 | `clipboard` `developer-tools` `keyboard-navigation` `productivity` `terminal` | 1 | 2026-07-23 |
| [**🆕 herdr-vaultr**](https://github.com/connerohnesorge/herdr-vaultr)<br><sub>connerohnesorge</sub> | vaultrの公式herdrプラグイン——キャプチャしたエージェントセッションを、実行元のペインからコピー・表示・フォーク・検索できる | `vaultr` `shell` | 0 | 🔄 2026-08-13 |
| [**🆕 herdr-lens**](https://github.com/VoidAxon/herdr-lens)<br><sub>VoidAxon</sub> | Select text in a Herdr pane, press a key, read it in your own language. Translation, dictionary, identifier lookup and summaries — stdlib-only, zero config. | `ai` `cli` `terminal` `translation` `python` | 0 | 🔄 2026-08-19 |

<details><summary>この目的にも関係するもの</summary>

- [nicosuave/memex](https://github.com/nicosuave/memex) — Search Claude Code, Codex, Pi, OpenCode, Github Copilot & Cursor transcripts. Resume sessions. Track tokens.
- [iurysza/termscope](https://github.com/iurysza/termscope) — 分割ペインで、ターミナル画面に表示されているファイルやリンクを開く
- [jlimas/herdr-worktree-seed](https://github.com/jlimas/herdr-worktree-seed) — コピーオンライトのnode_modulesと設定可能なローカルdotfilesを、新しいworktreeに投入するHerdrプラグイン
- [tanshio/herdr-worktreeinclude](https://github.com/tanshio/herdr-worktreeinclude) — Herdrプラグイン：.worktreeincludeにマッチするgit管理外ファイルを、新しく作成されたworktreeにコピーする
- [shadowfax92/herdr-comments](https://github.com/shadowfax92/herdr-comments) — コピーしたHerdrのターミナル出力に注釈を付け、ペインごとのコメントを収集してNeovimでレビューできる
- [crexi/herdr-worktree-copy](https://github.com/crexi/herdr-worktree-copy) — .worktree-copyマニフェストに基づき、worktreeローカルファイルをコピー・シンボリックリンクするHerdrプラグイン
- [Feasy01/herdr-allow](https://github.com/Feasy01/herdr-allow) — herdrプラグイン：.herdr-allowの許可リストを使って、gitignore対象のファイル（.env、シークレット、ローカル設定）を新しいworktreeすべてにコピーする
- [Angel-O/herdr-agent-resume](https://github.com/Angel-O/herdr-agent-resume) — AIエージェントのセッションをスムーズに再開できるよう、再開用コマンドを挿入またはコピーするHerdrプラグイン
- [eightHundreds/herdr-worktreeinclude](https://github.com/eightHundreds/herdr-worktreeinclude) — Herdrプラグイン：.worktreeincludeで指定したgit管理外ファイルを、新しいworktreeにコピーする
- [itayo-m/herdr-tab-session-name-sync](https://github.com/itayo-m/herdr-tab-session-name-sync) — エージェントのセッション名を、herdrのタブとペインのタイトルに同期する
- [scoussens-nthplusio/herdr-worktree-include](https://github.com/scoussens-nthplusio/herdr-worktree-include) — リポジトリの.worktreeincludeを使って、.envなどgit管理外のファイルを新しいHerdr worktreeにコピーする——Claude Codeが使うのと同じファイル・同じルール
- [willian/herdr-fzf-url](https://github.com/willian/herdr-fzf-url) — フォーカス中のペインから`fzf`でURLを選び、開く・コピーする
- [zerodice0/herdr-plugin-worktree-bootstrap](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap) — 新しいHerdrのGit worktreeに、無視されているローカルファイルを安全にコピーし、セットアップコマンドを実行する

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-meta"></a>

## プラグイン管理・開発

> プラグイン自体を管理したい / 自分で作りたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-plus**](https://github.com/cloudmanic/herdr-plus)<br><sub>cloudmanic</sub> | herdr向けの拡張機能。正式なプラグインとして構築されたツール集（プロジェクト管理とクイックアクション）でherdrをより良くする | `go` | 247 | 2026-07-23 |
| [**herdr-lazy**](https://github.com/natori-hrj/herdr-lazy)<br><sub>natori-hrj</sub> | herdr向けの宣言的なプラグインマネージャー兼キュレーション済みディストリビューション——1つのリスト、実体のあるロックファイル、管理用ペイン | `cli` `lockfile` `plugin-manager` `rust` `terminal` | 19 | 🔄 2026-08-19 |
| [**herdr-plugin-manager**](https://github.com/speardragon/herdr-plugin-manager)<br><sub>speardragon</sub> | ポップアップからherdrのプラグインを管理——インストール・更新・有効/無効化・アンインストール、herdr-pluginマーケットプレイスの閲覧も可能。推奨キー：prefix+p | `plugin-manager` `tui` `shell` | 13 | 🔄 2026-08-19 |
| [**house-of-herdr**](https://github.com/alasano/house-of-herdr)<br><sub>alasano</sub> | Herdr向けのプラグイン集——Work Louder Codex Micro上にエージェントのステータスランプと操作パネルを表示するCodex Microを含む | `codex-micro` `work-louder` `typescript` | 3 | 🔄 2026-08-13 |
| [**herdr-plugin-rust**](https://github.com/Newt6611/herdr-plugin-rust)<br><sub>Newt6611</sub> | Herdrのプラグインを構築するためのRustアプリケーションフレームワーク | `rust` | 2 | 2026-07-09 |
| [**herdr-plugins-labs**](https://github.com/hmu332233/herdr-plugins-labs)<br><sub>hmu332233</sub> | Herdr向けの実験的プラグイン集——ここで育て、成熟したら独立したリポジトリに卒業する | `labs` `javascript` | 1 | 2026-07-18 |
| [**🆕 herdr-plugin-manager**](https://github.com/a-curious-coder/herdr-plugin-manager)<br><sub>a-curious-coder</sub> | 1つのポップアップペインからherdrプラグインを管理・発見する——インストール/アンインストール/更新、アクションの実行やバインド、公開レジストリの閲覧ができる | `shell` | 0 | 🔄 2026-08-13 |
| [**herdr-plugins**](https://github.com/tyler-jewell/herdr-plugins)<br><sub>tyler-jewell</sub> | Rustのみで書かれたHerdrプラグインのモノレポ（標準ライブラリ優先）。インストールは herdr plugin install tyler-jewell/herdr-plugins/<subdir> で行う | `rust` `go` | 0 | 🔄 2026-08-10 |

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-other"></a>

## その他・ユーティリティ

> 上のどれにも当てはまらない便利もの

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-plugins-directory**](https://github.com/MIDO-ruby7/herdr-plugins-directory)<br><sub>MIDO-ruby7</sub> | やりたいことからherdrプラグインを探せるリンク集 | `python` | 9 | 🔄 2026-08-19 |
| [**neon-herdr**](https://github.com/neon-solutions/neon-herdr)<br><sub>neon-solutions</sub> | Neon公式のHerdrプラグイン | `typescript` | 9 | 🔄 2026-08-06 |
| [**wave-tui**](https://github.com/takemo101/wave-tui)<br><sub>takemo101</sub> | 作業中に流せる、静かなターミナルラジオ | `rust` | 4 | 2026-07-20 |
| [**herdr-commandcode-plugin**](https://github.com/TheMetalStorm/herdr-commandcode-plugin)<br><sub>TheMetalStorm</sub> | CommandcodeをHerdrに統合する | `cli` `commandcode` `herdr-integration` `shell` | 4 | 2026-07-30 |
| [**🆕 herdr-lantern**](https://github.com/aigorahub/herdr-lantern)<br><sub>aigorahub</sub> | Lantern, by Elves. A Herdr plugin: the herd is in the field; Lantern illuminates who needs you and what they are working toward. | `python` | 3 | 🔄 2026-08-19 |
| [**herdr-plugin-cmux**](https://github.com/lachieh/herdr-plugin-cmux)<br><sub>lachieh</sub> | herdrが管理するすべてのエージェントを、cmuxのサイドバーにそれぞれ独立した行としてミラーする——ステータスピルとクリックでジャンプできるタスク行付き | `javascript` | 3 | 2026-07-01 |
| [**🆕 herdr-api-credit-bar**](https://github.com/CristianPeralta/herdr-api-credit-bar)<br><sub>CristianPeralta</sub> | Herdr plugin: remaining credit for pay-as-you-go API providers, starting with Alibaba Cloud Model Studio | `shell` | 2 | 🔄 2026-08-18 |
| [**herdr-streamdeck**](https://github.com/Pimpmuckl/herdr-streamdeck)<br><sub>Pimpmuckl</sub> | Elgato Stream Deck+によるHerdrの物理コントロール | `typescript` | 2 | 🔄 2026-08-15 |
| [**herdr-freebuff-plugin**](https://github.com/TheMetalStorm/herdr-freebuff-plugin)<br><sub>TheMetalStorm</sub> | Herdr向けのFreebuffライフサイクル統合プラグイン——ファイルのポーリングとPTY内容のスクレイピングで、アイドル/作業中/ブロック中の状態を報告する | `cli` `freebuff` `herdr-integration` `shell` | 2 | 2026-07-22 |
| [**herdr-edit-windows**](https://github.com/aclima01/herdr-edit-windows)<br><sub>aclima01</sub> | コーディングエージェントの隣、herdrのペイン内で動くシンプルなテキストエディタ——ファイルツリー、シンタックスハイライト付きエディタ、未コミット差分タブを備える。Windows専用 | `rust` | 1 | 2026-07-25 |
| [**herdr-stoplight**](https://github.com/BowlOfSoup/herdr-stoplight)<br><sub>BowlOfSoup</sub> | Herdrのリアルタイムな状態から、物理的なArduino製信号灯モジュールを動かす | `go` | 1 | 2026-07-11 |
| [**🆕 herdr-rainfrog**](https://github.com/fraction12/herdr-rainfrog)<br><sub>fraction12</sub> | Open Rainfrog in a managed HerdR pane. | `shell` | 1 | 🔄 2026-08-15 |
| [**herdr-memory**](https://github.com/jatingargiitk/herdr-memory)<br><sub>jatingargiitk</sub> | コーディングセッションから「生きた脳」を構築するHerdrプラグイン——うまくいったこと、失敗したこと、あなたが下した判断を少しずつ学習していく | `shell` | 1 | 🔄 2026-08-11 |
| [**hrd**](https://github.com/joshuadavidthomas/hrd)<br><sub>joshuadavidthomas</sub> | サンドボックスの群れと、その上で動くHerdrセッションを管理する | `go` | 1 | 🔄 2026-08-15 |
| [**herdr-plugins**](https://github.com/narumiruna/herdr-plugins)<br><sub>narumiruna</sub> | _(説明なし)_ | `rust` | 1 | 🔄 2026-08-08 |
| [**herdr-phin-util**](https://github.com/phin-tech/herdr-phin-util)<br><sub>phin-tech</sub> | 個人用のHerdrユーティリティ集 | `bubbletea` `tui` `go` | 1 | 🔄 2026-08-18 |
| [**herdr-api-client**](https://github.com/playsthisgame/herdr-api-client)<br><sub>playsthisgame</sub> | herdrのスプリットペインやタブで動くHTTP/REST APIクライアント——ターミナルを離れずにリクエストの閲覧・実行・テストができる | `http-client` `rest-client` `tui` `shell` | 1 | 🔄 2026-08-08 |
| [**pixtui**](https://github.com/RizRiyz/pixtui)<br><sub>RizRiyz</sub> | ターミナル上で動くピクセルアートエディタ | `bohay-module` `editor` `luvus-module` `pixel-art` `termina` | 1 | 🔄 2026-08-07 |
| [**herdr-suite-site**](https://github.com/StructuPath/herdr-suite-site)<br><sub>StructuPath</sub> | StructuPath Herdr Suiteのランディングページ——herdr.structupath.ai | `herdr-integration` `html` | 1 | 2026-07-31 |
| [**🆕 herdr-sidepulse**](https://github.com/third774/herdr-sidepulse)<br><sub>third774</sub> | _(説明なし)_ | `javascript` | 1 | 🔄 2026-08-14 |
| [**🆕 herdr-zen**](https://github.com/y4m3/herdr-zen)<br><sub>y4m3</sub> | Zen mode for Herdr with an adjustable centered pane width | `rust` `terminal` `zen-mode` | 1 | 🔄 2026-08-19 |
| [**🆕 herdr-plugins**](https://github.com/alastairsounds/herdr-plugins)<br><sub>alastairsounds</sub> | Plugins for herdr | `rust` | 0 | 🔄 2026-08-14 |
| [**herdr-panes**](https://github.com/atm028/herdr-panes)<br><sub>atm028</sub> | _(説明なし)_ | `python` | 0 | 2026-08-01 |
| [**capslock-herdr-prefix**](https://github.com/GHJQ/capslock-herdr-prefix)<br><sub>GHJQ</sub> | macOSでCaps Lockキーをherdrのprefixキーにする | `capslock` `macos` `shell` | 0 | 🔄 2026-08-11 |
| [**herdr-attach**](https://github.com/gilvanecesar/herdr-attach)<br><sub>gilvanecesar</sub> | Herdrのポップアップからローカルファイルを選び、フォーカス中のコーディングエージェントに送る——ターミナルを離れずにファイルのコンテキストを添付できる | `javascript` | 0 | 2026-07-26 |
| [**herdr-llama**](https://github.com/hitaishi2222/herdr-llama)<br><sub>hitaishi2222</sub> | 手元の操作でllama-serverをコントロールする | `llama-cpp` `local-ai` `python` | 0 | 2026-07-16 |
| [**🆕 herdr-web-broker**](https://github.com/JefeLabs/herdr-web-broker)<br><sub>JefeLabs</sub> | REST/WS gateway and parent-child federation for herdr instances | `typescript` | 0 | 🔄 2026-08-19 |
| [**herdr-pane-update-timestamps**](https://github.com/johnlindquist/herdr-pane-update-timestamps)<br><sub>johnlindquist</sub> | ペイン出力をタイムスタンプ付きでスクロール観察できるHerdrプラグイン | `rust` | 0 | 2026-07-29 |
| [**herdr-status**](https://github.com/jrswab/herdr-status)<br><sub>jrswab</sub> | Linux版Herdr向けの、マシン状態を常時表示するペイン | `go` | 0 | 2026-07-30 |
| [**herdr-laravel-tinker**](https://github.com/lancodev/herdr-laravel-tinker)<br><sub>lancodev</sub> | herdr向けのスプリット表示Laravel tinker REPL——エディタの隣にライブの実行結果を表示、ペインまたはポップアップで利用可能 | `laravel` `tinker` `php` `repl` | 0 | 2026-07-16 |
| [**herdr-new-task**](https://github.com/leonho/herdr-new-task)<br><sub>leonho</sub> | herdrプラグイン：1回のキー操作でプロジェクトディレクトリを選び、新しいタブでclaudeを起動する。タブ名は名詞優先の命名 | `python` | 0 | 2026-07-16 |
| [**herdr-plugin-loopreview**](https://github.com/loopkeep/herdr-plugin-loopreview)<br><sub>loopkeep</sub> | loopreview向けのHerdrプラグイン | `rust` | 0 | 2026-07-23 |
| [**🆕 strays**](https://github.com/m1sk9/strays)<br><sub>m1sk9</sub> | A TUI for Centralized Management of Claude Code | `claude-code` `llm` `tui` `rust` | 0 | 🔄 2026-08-16 |
| [**herdr-source-control**](https://github.com/mariotmc/herdr-source-control)<br><sub>mariotmc</sub> | _(説明なし)_ | `go` | 0 | 🔄 2026-08-15 |
| [**herdr-brainrot**](https://github.com/marius-se/herdr-brainrot)<br><sub>marius-se</sub> | エージェントが作業している間、Herdrのペインの中でDOOMをプレイできる「brainrot」プラグイン。差し替え可能なアプリに対応 | `doom` `go` | 0 | 🔄 2026-08-06 |
| [**🆕 herdr-git-pull**](https://github.com/nimrc/herdr-git-pull)<br><sub>nimrc</sub> | _(説明なし)_ | `python` | 0 | 🔄 2026-08-13 |
| [**🆕 ayatsumugi**](https://github.com/nkwork9999/ayatsumugi)<br><sub>nkwork9999</sub> | Local-first React DOM, Fiber, and state graph visualization for Ayatori and Tsumugi | `cmux` `ghostty` `orca` `react-devtools` `javascript` | 0 | 🔄 2026-08-15 |
| [**herdr-action-launcher**](https://github.com/nnexai/herdr-action-launcher)<br><sub>nnexai</sub> | _(説明なし)_ | `javascript` | 0 | 🔄 2026-08-05 |
| [**herdr-traex-integration**](https://github.com/Phoobobo/herdr-traex-integration)<br><sub>Phoobobo</sub> | traexとの連携をサポートするHerdrプラグイン | `shell` | 0 | 2026-07-02 |
| [**herdr-handsfree**](https://github.com/RanolP/herdr-handsfree)<br><sub>RanolP</sub> | ハンズフリーherdrプラグイン——whisper.cppによる音声入力とmacOS向けWebカメラ視線マウスを提供 | `rust` | 0 | 2026-07-30 |
| [**herdr-browser**](https://github.com/redsquiggle/herdr-browser)<br><sub>redsquiggle</sub> | Chromiumのタブグループを、Herdrのワークスペースと同期させる | `chromium` `ratatui` `rust` | 0 | 2026-07-28 |
| [**herdr-cwd-control**](https://github.com/skinp/herdr-cwd-control)<br><sub>skinp</sub> | 新しいワークスペース・タブ・ペインの初期作業ディレクトリを、より細かく制御できるherdrプラグイン | `python` | 0 | 🔄 2026-08-10 |
| [**herdr-jetbrains**](https://github.com/Soemii/herdr-jetbrains)<br><sub>Soemii</sub> | _(説明なし)_ | `go` | 0 | 🔄 2026-08-09 |
| [**herdr-now-playing**](https://github.com/spywhere/herdr-now-playing)<br><sub>spywhere</sub> | キーバインドで操作できる音楽プレイヤーをherdrに追加する | `shell` | 0 | 🔄 2026-08-13 |
| [**🆕 herdr-tilt**](https://github.com/the-inconvenience-store/herdr-tilt)<br><sub>the-inconvenience-store</sub> | _(説明なし)_ | `rust` | 0 | 🔄 2026-08-20 |
| [**🆕 herdr-plugin-k8s-context**](https://github.com/tkuchiki/herdr-plugin-k8s-context)<br><sub>tkuchiki</sub> | Open Herdr tabs with isolated Kubernetes contexts and namespaces. | `go` | 0 | 🔄 2026-08-15 |
| [**herdr-plugins**](https://github.com/tomaszhanc/herdr-plugins)<br><sub>tomaszhanc</sub> | 個人用のherdrプラグインのモノレポ。各プラグインは自分のフォルダに、herdr-plugin.tomlマニフェストと実行ファイルを持つ | — | 0 | 2026-07-16 |

[⬆ 目的一覧に戻る](#purposes)

## 使い方

```sh
# 表の行にある owner/repo をそのまま渡す
herdr plugin install ogulcancelik/herdr-plugin-github-start
herdr plugin list
```

サブディレクトリに入っているプラグインは `owner/repo/subdir` の形になります。詳細は [Plugins](https://herdr.dev/docs/plugins/) と [Marketplace](https://herdr.dev/docs/marketplace/) を参照。

## 直したいとき

分類が変・タグを足したい・一言メモを付けたい場合は [`data/overrides.json`](data/overrides.json) にエントリを追加して PR してください。

```json
{
  "owner/repo": {
    "category": "notify",
    "add_tags": ["macos"],
    "note": "セットアップに ntfy のトピック設定が必要"
  }
}
```

カテゴリキー: `notify`, `remote`, `agents`, `worktree`, `review`, `forge`, `layout`, `navigate`, `files`, `cost`, `monitor`, `finder`, `automation`, `session`, `naming`, `text`, `meta`, `other`

GitHub 上に説明文が無いリポジトリは、`description` キーで上書きできます（英語で。ja/zh ページの訳文は `data/translations.json` に追加してください）。

掲載自体は各リポジトリが GitHub topic `herdr-plugin` を付けた時点で自動的に入ります（このリストへの申請は不要）。

---

*README と `data/plugins.json` は [`scripts/build.py`](scripts/build.py) が生成しています。直接編集しないでください。*
