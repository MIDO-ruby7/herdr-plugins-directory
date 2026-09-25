# herdr plugins by purpose

🇯🇵 日本語 · [🇺🇸 English](README.en.md) · [🇨🇳 中文](README.zh.md)

**「◯◯したい」から herdr のプラグインを探すためのリンク集です。**

- 収録 **994** 件 / 最終更新 **2026-09-25 11:50 UTC**（6 時間ごとに自動更新）
- データ元: GitHub topic [`herdr-plugin`](https://github.com/topics/herdr-plugin) — 公式マーケットプレイス [herdr.dev/plugins](https://herdr.dev/plugins/) と同じ母集団
- 分類はリポジトリの説明文とトピックからの自動推定です。おかしなものは [`data/overrides.json`](data/overrides.json) の PR で直せます
- インストール: `herdr plugin install owner/repo` — [公式ドキュメント](https://herdr.dev/docs/plugins/)

> [!WARNING]
> ここは自動収集の索引で、審査済みカタログではありません。プラグインは自分のマシンでそのまま動くコードなので、入れる前にマニフェストと実行されるコマンドを確認してください。

<a id="purposes"></a>

## 目的から探す

- [**🆕 最近追加されたプラグイン**](#cat-new) (184) — 直近 7 日以内にこの一覧に加わったプラグインです。
- [**通知・アラート**](#cat-notify) (42) — エージェントが完了した / 入力待ちで止まったのを、席を外していても知りたい
- [**スマホ・リモート操作**](#cat-remote) (51) — 外出先やスマホからエージェントを監視して、承認だけ返したい
- [**エージェント統括・並列実行**](#cat-agents) (146) — 複数の AI エージェントをまとめて起動・分担・管理したい
- [**git worktree・ブランチ運用**](#cat-worktree) (51) — 作業ごとに worktree を切って、片付けまで自動でやりたい
- [**コードレビュー・差分確認**](#cat-review) (40) — エージェントが書いた差分を読んで、コメントを返したい
- [**GitHub / issue トラッカー連携**](#cat-forge) (48) — issue や PR を起点に作業を始めたい / PR の状態を追いたい
- [**ワークスペース・レイアウト構築**](#cat-layout) (40) — プロジェクトを開いたら、タブ・ペイン・起動コマンドまで一発で整えたい
- [**ペイン移動・キー操作**](#cat-navigate) (119) — ペインやワークスペース間の移動・リサイズを、エディタと同じキーで済ませたい
- [**ファイル閲覧・エディタ連携**](#cat-files) (54) — ペインの中でファイルツリーを開いたり、エディタ側と状態を揃えたい
- [**トークン・コスト管理**](#cat-cost) (25) — エージェントがいくら使っているかを見たい / 使用量を削りたい
- [**監視・ダッシュボード**](#cat-monitor) (77) — エージェントやマシンの状態を一覧で眺めたい
- [**検索・ファジーファインダー**](#cat-finder) (83) — コマンドやプロジェクトを、名前をうろ覚えのまま呼び出したい
- [**自動化・フック・定期実行**](#cat-automation) (48) — worktree 作成時やタイミングを決めて、決まった手順を自動で走らせたい
- [**セッション保存・復元**](#cat-session) (30) — 作業を閉じても、あとで同じ状態から再開したい
- [**タイトル・命名・見た目**](#cat-naming) (48) — タブ名やターミナルタイトルを自動で分かりやすくしたい / 見た目を変えたい
- [**テキスト・URL 抽出**](#cat-text) (20) — 画面に出ている文字列やパス・URL を、マウスなしで拾いたい
- [**プラグイン管理・開発**](#cat-meta) (8) — プラグイン自体を管理したい / 自分で作りたい
- [**その他・ユーティリティ**](#cat-other) (64) — 上のどれにも当てはまらない便利もの

<a id="cat-new"></a>

## 🆕 最近追加されたプラグイン

> 直近 7 日以内にこの一覧に加わったプラグインです。

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**🆕 proqi**](https://github.com/oborchers/proqi)<br><sub>oborchers</sub> | A terminal-native prompt composer for power users running multiple coding agents. | `ai-agents` `cli` `coding-agents` `developer-tools` `local-first` | 40 | 2026-09-25 |
| [**🆕 termaxa**](https://github.com/termaxa/termaxa)<br><sub>termaxa</sub> | A cooperative gate for the shell commands AI agents run. Previews, backups, policy, audit. Claude Code + Cursor. A windshield, not a sandbox. | `agent-safety` `ai-agents` `claude-code` `cli` `developer-tools` | 22 | 2026-09-24 |
| [**🆕 captains-deck**](https://github.com/Enk1do/captains-deck)<br><sub>Enk1do</sub> | Captain's Deck - a read-only Firstmate flow kanban plugin for Herdr | `firstmate` `python` | 17 | 2026-09-24 |
| [**🆕 yeet**](https://github.com/adriankarlen/yeet)<br><sub>adriankarlen</sub> | a minimal sesh style picker inside herdr | `sesh` `session-management` `yeet` `go` | 1 | 2026-09-25 |
| [**🆕 mu-herdr**](https://github.com/AndresMpa/mu-herdr)<br><sub>AndresMpa</sub> | A herdr configuration made to work with MμVim | `herdr-integration` `muvim` `shell` | 1 | 2026-09-24 |
| [**🆕 herdr-palette**](https://github.com/iancharters/herdr-palette)<br><sub>iancharters</sub> | Fuzzy command palette for Herdr — core commands plus auto-discovered plugin actions, run where you can see them. Fast, keyboard-first, terminal-native. | `go` | 1 | 2026-09-25 |
| [**🆕 forestr**](https://github.com/ludoroo/forestr)<br><sub>ludoroo</sub> | A Herdr plugin that manages Git branch worktrees from one fast, modal fzf popup — list, open, create, and safely remove worktrees across every repository Herdr… | `git-worktree` `worktrunk` `shell` | 1 | 2026-09-25 |
| [**🆕 terminal-browser-relay**](https://github.com/maynewong/terminal-browser-relay)<br><sub>maynewong</sub> | terminal-browser on herdr remote without the slideshow | `javascript` | 1 | 2026-09-25 |
| [**🆕 herdr-ci-checks**](https://github.com/tdi/herdr-ci-checks)<br><sub>tdi</sub> | herdr plugin: live GitHub/GitLab CI checks for the current branch in a pane on the right | `javascript` | 1 | 2026-09-25 |
| [**🆕 herdr-codex-autoresume**](https://github.com/UN-9BOT/herdr-codex-autoresume)<br><sub>UN-9BOT</sub> | Herdr plugin that automatically resumes Codex CLI /goal after usage limits reset | `typescript` | 1 | 2026-09-24 |
| [**🆕 herdr-ctx**](https://github.com/aorumbayev/herdr-ctx)<br><sub>aorumbayev</sub> | herdrのサイドバーペイン向けの、Claudeコンテキストウィンドウ表示 | `typescript` | 0 | 2026-07-21 |
| [**🆕 herdr-priority-view**](https://github.com/asermax/herdr-priority-view)<br><sub>asermax</sub> | 3 段階の優先度と「古いものを先に」というルールで並び替える、herdr 用のカスタム優先度ビューです。 | `typescript` | 0 | 2026-09-12 |
| [**🆕 herdr-repository-identity**](https://github.com/choplin/herdr-repository-identity)<br><sub>choplin</sub> | 各Herdrワークスペースが共有するGitリポジトリの識別情報を報告する | `go` | 0 | 2026-08-24 |
| [**🆕 herdr-context-namer**](https://github.com/eabadim/herdr-context-namer)<br><sub>eabadim</sub> | OpenCode経由でペインのコンテキストから、Herdrのタブ・ワークスペース名を自動生成する | `opencode` `python` | 0 | 2026-08-06 |
| [**🆕 hrdr-azure-plugin**](https://github.com/gbaeke/hrdr-azure-plugin)<br><sub>gbaeke</sub> | herdrプラグイン：Azureのリソースグループとリソースを閲覧し、クリックするとAzureポータルで開く | `azure` `javascript` | 0 | 2026-08-23 |
| [**🆕 herdr-pane-id-border**](https://github.com/Haichiu/herdr-pane-id-border)<br><sub>Haichiu</sub> | ペインの境界線に正規のペイン ID を表示する、ミニマルな Herdr プラグインです。 | `shell` | 0 | 2026-09-02 |
| [**🆕 herdr-worktree-include**](https://github.com/heyfirst/herdr-worktree-include)<br><sub>heyfirst</sub> | herdr plugin that copies .worktreeinclude files into new worktrees. Built with Bun. 🍞 | `bun` `claude-code` `git-worktree` `worktree` `typescript` | 0 | 2026-09-23 |
| [**🆕 herdr-jira-peek**](https://github.com/hilmimuktitama/herdr-jira-peek)<br><sub>hilmimuktitama</sub> | 現在の Herdr ペインから、Jira Cloud を読み取り専用でプレビューできます。 | `jira` `terminal` `shell` | 0 | 2026-09-25 |
| [**🆕 herdr-ai-memory**](https://github.com/iagogfe/herdr-ai-memory)<br><sub>iagogfe</sub> | Herdrプラグイン：ai-memoryが管理するワークストリーム経由でコーディングエージェントを起動する——エージェントをまたいだセッションの継続性を実現 | `ai-agents` `ai-memory` `terminal` `javascript` | 0 | 2026-07-24 |
| [**🆕 herdr-busywatch**](https://github.com/KamalF/herdr-busywatch)<br><sub>KamalF</sub> | A herdr plugin: is anything still running, and does it need me? | `python` | 0 | 2026-09-23 |
| [**🆕 herdr-new-task**](https://github.com/leonho/herdr-new-task)<br><sub>leonho</sub> | herdrプラグイン：1回のキー操作でプロジェクトディレクトリを選び、新しいタブでclaudeを起動する。タブ名は名詞優先の命名 | `python` | 0 | 2026-07-16 |
| [**🆕 herdr-git-pull**](https://github.com/nimrc/herdr-git-pull)<br><sub>nimrc</sub> | _(説明なし)_ | `python` | 0 | 2026-08-13 |
| [**🆕 herdr-notify-router**](https://github.com/pradyb/herdr-notify-router)<br><sub>pradyb</sub> | Rules for herdr agent notifications: when to alert and where it goes (webhook, ntfy, desktop), with quiet hours and dedupe | `python` | 0 | 2026-09-22 |
| [**🆕 herdr-github-metadata**](https://github.com/ralphilius/herdr-github-metadata)<br><sub>ralphilius</sub> | Herdr plugin: GitHub metadata for the sidebar — the PR each agent is working on | `github` `python` | 0 | 2026-09-25 |
| [**🆕 herdr-file-picker**](https://github.com/shivammehta25/herdr-file-picker)<br><sub>shivammehta25</sub> | tmux-file-pickerをherdr向けに移植した、いわゆる「vibe coding」製プラグイン | `shell` | 0 | 2026-07-29 |
| [**🆕 colloquy**](https://github.com/SoMaCoSF/colloquy)<br><sub>SoMaCoSF</sub> | エージェント群向けの、自己アドレス指定型・一時キャッシュされた因果関係DAG監査ログとテレメトリ | `colloquy` `gyst` `javascript` | 0 | 2026-07-29 |
| [**🆕 herdr-telegram-bridge**](https://github.com/spancerxing/herdr-telegram-bridge)<br><sub>spancerxing</sub> | Approve Herdr coding agents (Claude Code, Codex, agy, pi) from Telegram — per-agent topics, approval buttons, status dashboard, completion notices, and desk-si… | `go` | 0 | 2026-09-24 |
| [**🆕 hither**](https://github.com/T0mSIlver/hither)<br><sub>T0mSIlver</sub> | リモートマシン上の herdr ペインでキーの組み合わせを押すと、Mac 側で Zed がそのディレクトリを開きます。 | `shell` | 0 | 2026-09-18 |
| [**🆕 herdr-pr-workflow**](https://github.com/tamdogood/herdr-pr-workflow)<br><sub>tamdogood</sub> | フォーカス中のエージェントに、現在のブランチのプルリクエストを安全に作成またはマージするよう指示するHerdrアクション | `javascript` | 0 | 2026-08-10 |
| [**🆕 herdr-ghostty-theme-sync**](https://github.com/themuuln/herdr-ghostty-theme-sync)<br><sub>themuuln</sub> | herdrのテーマとサイドバーの配色を、使用中のGhosttyのテーマに合わせる——herdr再起動をまたいでもサイドバーのトークン（配色設定）を維持する。herdr.dev製プラグイン | `python` | 0 | 2026-08-12 |
| [**🆕 herdr-hunks**](https://github.com/winoooops/herdr-hunks)<br><sub>winoooops</sub> | A Git hunk viewer for Herdr. Review committed and uncommitted changes, compare branches, and explore diffs in your terminal. | `git` `rust` `tui` | 0 | 2026-09-25 |
| [**🆕 herdr-space-groups**](https://github.com/yojahny55/herdr-space-groups)<br><sub>yojahny55</sub> | herdrプラグイン：Spaceを名前付き・色分けされたグループにまとめる——ピッカーのポップアップ（マウス＋キーボード対応）、サイドバーのグループ見出し、自動並べ替えに対応 | `javascript` | 0 | 2026-08-29 |
| [**🆕 herdr-desktop-bridge**](https://github.com/yonatangross/herdr-desktop-bridge)<br><sub>yonatangross</sub> | Claude Desktop が herdr のフロアを読み取り、メッセージを残せるようにする stdio MCP サーバーです。あくまでメールボックスと呼び鈴であり、指揮席にはなりません。 | `claude-desktop` `mcp` `python` | 0 | 2026-09-11 |
| [**🆕 herdr-kakoune-popup**](https://github.com/Yukaii/herdr-kakoune-popup)<br><sub>Yukaii</sub> | Herdrネイティブのポップアップで、Kakouneのターミナルコマンドを実行する | `kakoune` `shell` | 0 | 2026-08-20 |
| [**🆕 herdr-plugin-pane-move**](https://github.com/yuloop/herdr-plugin-pane-move)<br><sub>yuloop</sub> | Herdr プラグイン：ショートカットキーでペインを移動します。 | `shell` | 0 | 2026-09-04 |
| [**🆕 claude-usage**](https://github.com/yuuta1219/claude-usage)<br><sub>yuuta1219</sub> | herdrプラグイン：Claude Codeの使用率（セッション%/週%）をサイドバー下部に常時表示する | `claude` `claude-code` `python` `tui` | 0 | 2026-08-01 |
| [**🆕 lazyherd**](https://github.com/chriopter/lazyherd)<br><sub>chriopter</sub> | Cockpit over all your Git repos, with a jump into lazygit and Herdr workspaces | `git` `lazygit` `tui` `go` | 1 | 2026-09-20 |
| [**🆕 herdr-plugin-omp-state**](https://github.com/dk3775/herdr-plugin-omp-state)<br><sub>dk3775</sub> | Report omp agent state to Herdr from its terminal title, for panes the official integration does not cover | `coding-agents` `omp` `python` | 1 | 2026-09-24 |
| [**🆕 relevo**](https://github.com/fuad-daoud/relevo)<br><sub>fuad-daoud</sub> | Automates the plan/report handoff between planner and builder AI coding agent panes running under herdr | `go` | 1 | 2026-09-25 |
| [**🆕 herdr-linear**](https://github.com/mrolafsson/herdr-linear)<br><sub>mrolafsson</sub> | Linear issues and projects in a herdr popup: status icons, rendered descriptions, status changes, one key to a worktree, and Start hands the issue to your codi… | `bubbletea` `claude-code` `coding-agents` `git-worktree` `go` | 1 | 2026-09-24 |
| [**🆕 herdr-estate**](https://github.com/andrewdunndev/herdr-estate)<br><sub>andrewdunndev</sub> | Long-running campaigns for herdr: threads of agent work, addressed as estate/campaign, that outlive every conversation. Mirror of gitlab.com/dunn.dev/herdr-est… | `ai-agents` `claude-code` `cli` `rust` `terminal` | 0 | 2026-09-24 |
| [**🆕 herdr-dynamic-workflow**](https://github.com/andthezhang/herdr-dynamic-workflow)<br><sub>andthezhang</sub> | Herdr内でコーディングエージェントCLIをオーケストレーションするための、JavaScript製ワークフロー | `agent-fleet` `agent-orchestration` `agent-swarm` `agentic-ai` `agents` | 0 | 2026-08-30 |
| [**🆕 herdr-pr-status**](https://github.com/anthonykimm/herdr-pr-status)<br><sub>anthonykimm</sub> | サイドバーの各ワークスペース行に、GitHub の PR 番号・レビュー状況・CI ステータスを、色分けされたアイコンで表示します。 | `python` | 0 | 2026-09-10 |
| [**🆕 herdr-agent-cli**](https://github.com/azyu/herdr-agent-cli)<br><sub>azyu</sub> | 各ペインでどの CLI が動いているかを、ランタイムごとに色分けできるサイドバートークンとして表示する Herdr プラグインです。 | `coding-agents` `developer-tools` `terminal` `python` | 0 | 2026-09-11 |
| [**🆕 herdr-project-manager**](https://github.com/barnuri/herdr-project-manager)<br><sub>barnuri</sub> | herdr向けのプロジェクトマネージャープラグイン——globまたは手動でのプロジェクト検出、ファジーピッカー、タブまたはワークスペースとしてオープン | `javascript` | 0 | 2026-08-25 |
| [**🆕 herdr-cwd**](https://github.com/bonanyan/herdr-cwd)<br><sub>bonanyan</sub> | Mirror the focused herdr pane's working directory to the host terminal with OSC 7, so terminal file panels, titles, and new splits follow herdr. | `osc7` `terminal` `javascript` | 0 | 2026-09-20 |
| [**🆕 herdr-split-pane**](https://github.com/choplin/herdr-split-pane)<br><sub>choplin</sub> | 呼び出し元が指定したコマンドを、Herdrのスプリットペインで直接開く | — | 0 | 2026-08-24 |
| [**🆕 herdr-tab-title-from-terminal**](https://github.com/christiangroth/herdr-tab-title-from-terminal)<br><sub>christiangroth</sub> | すべてのHerdrタブに、中で動いているエージェントのターミナルタイトルをそのまま名前として付ける。Claude Codeで/renameを1回実行すれば、セッションとタブの両方に名前が付く。手動で名前を付けたタブには手を出さない | `python` | 0 | 2026-08-25 |
| [**🆕 herdr-agent-numbers**](https://github.com/DillonWall/herdr-agent-numbers)<br><sub>DillonWall</sub> | herdr のエージェントパネルに番号を振り、focus_agent（prefix+1〜9）に対応させます。 | `terminal-multiplexer` `shell` | 0 | 2026-09-14 |
| [**🆕 herdr-zed-follow**](https://github.com/dlwr/herdr-zed-follow)<br><sub>dlwr</sub> | herdr plugin: Zed follows the focused herdr workspace | `zed` `shell` | 0 | 2026-09-24 |
| [**🆕 shahi**](https://github.com/iYassr/shahi)<br><sub>iYassr</sub> | Your herdr agents as a chat on your phone. Install the plugin, scan a QR, continue Claude Code, Codex and Cursor work anywhere. End-to-end encrypted. | `ai-agents` `claude-code` `codex` `expo` `react-native` | 0 | 2026-09-25 |
| [**🆕 herdr-pr-preview**](https://github.com/juninaba/herdr-pr-preview)<br><sub>juninaba</sub> | 現在のブランチのGitHubプルリクエストを、スプリットペインでプレビューするHerdrプラグイン | `shell` | 0 | 2026-07-08 |
| [**🆕 herdr-session-fork**](https://github.com/mackt/herdr-session-fork)<br><sub>mackt</sub> | Herdr plugin: fork the focused Claude Code / Codex / Pi / Grok session into another workspace or worktree, picked from a fuzzy list | `shell` | 0 | 2026-09-24 |
| [**🆕 pi-herdr-sidebar**](https://github.com/mastnacek/pi-herdr-sidebar)<br><sub>mastnacek</sub> | Native Rust Herdr plugin sidebar for the Pi coding agent: status telemetry, live skills, gates — VSA slices in Rust/Ratatui | `pi` `ratatui` `rust` | 0 | 2026-09-25 |
| [**🆕 herdr-green**](https://github.com/natori-hrj/herdr-green)<br><sub>natori-hrj</sub> | herdr向けのエージェントごとのテスト状態表示——エージェントが完了したらプロジェクトのテストを実行し、成功/失敗を表示する | `ai-agents` `ci` `tests` `rust` | 0 | 2026-07-23 |
| [**🆕 herdr-plugin-aos**](https://github.com/noctaIO/herdr-plugin-aos)<br><sub>noctaIO</sub> | 任意のワークスペースから、Agentic OS対応のClaude Codeエージェントをherdrのペインで起動する。非侵襲的なherdrプラグイン | `shell` | 0 | 2026-07-11 |
| [**🆕 herdr-notify-center**](https://github.com/ram4-dev/herdr-notify-center)<br><sub>ram4-dev</sub> | サーバー全体のエージェント通知を、永続化されたポップアップ受信箱でHerdrに提供する | `notifications` `typescript` | 0 | 2026-08-14 |
| [**🆕 herdr-pane-equalizer**](https://github.com/shanefully-done/herdr-pane-equalizer)<br><sub>shanefully-done</sub> | herdrのペインを均等なサイズにリサイズする。自動でも手動でも実行可能 | `javascript` | 0 | 2026-08-20 |
| [**🆕 herdr-hud**](https://github.com/sharonbrownw330/herdr-hud)<br><sub>sharonbrownw330</sub> | Keep coding agents visible and responsive while gaming with a draggable Herdr HUD overlay on your desktop. | `agent` `agentic-ai` `antigravity` `bash` `claude-code` | 0 | 2026-09-25 |
| [**🆕 herdr-web-ui**](https://github.com/devswha/herdr-web-ui)<br><sub>devswha</sub> | herdr in the browser: your live herdr workspaces, tabs and panes in a web UI / PWA, bridged over herdr's socket API | `bun` `pwa` `react` `terminal` `xterm` | 2 | 2026-09-25 |
| [**🆕 herdr-plugin-odysseus**](https://github.com/jpolec/herdr-plugin-odysseus)<br><sub>jpolec</sub> | Governed multi-agent workflows for Herdr: tasks → agents in Herdr panes → checks, retries, review, policy, approvals, audit, draft PR | `ai-agents` `rust` | 2 | 2026-09-25 |
| [**🆕 herdr-wrapped-tabs**](https://github.com/AlexeyKrotkov/herdr-wrapped-tabs)<br><sub>AlexeyKrotkov</sub> | Always-visible wrapped tabs for Herdr | `python` | 1 | 2026-09-24 |
| [**🆕 huicr**](https://github.com/claytonjschneider/huicr)<br><sub>claytonjschneider</sub> | Herdr User Interface for Code Review | `python` | 1 | 2026-09-24 |
| [**🆕 herdr-jira-worktree**](https://github.com/hanbong5938/herdr-jira-worktree)<br><sub>hanbong5938</sub> | Jira TUI plugin for herdr (fork of a2u/herdr-jira) — JQL filters, search, status transitions, delegate issues to AI agents, and check out issues into git workt… | `jira` `tui` `rust` | 1 | 2026-09-23 |
| [**🆕 herdr-plugins**](https://github.com/JJLiebig/herdr-plugins)<br><sub>JJLiebig</sub> | Herdr plugin that starts Codex or Claude from a GitHub issue, PR, or discussion | `javascript` | 1 | 2026-09-22 |
| [**🆕 herdr-usage**](https://github.com/kalbhor/herdr-usage)<br><sub>kalbhor</sub> | herdr plugin that shows coding-agent subscription usage (Claude Code) | `python` | 1 | 2026-09-17 |
| [**🆕 herdr-observr**](https://github.com/nabutabu/herdr-observr)<br><sub>nabutabu</sub> | A telemetry daemon subscribed to Herdr's live event stream that tracks agent runtime health, where agents are stuck, how long they wait for a human, how much c… | `go` | 1 | 2026-09-22 |
| [**🆕 herdr-claude-tab-rename**](https://github.com/oronbz/herdr-claude-tab-rename)<br><sub>oronbz</sub> | Herdr plugin: keep each tab named after its Claude Code session title (/rename or auto title) | `shell` | 1 | 2026-09-23 |
| [**🆕 herdr-pr-modal**](https://github.com/Tarektouati/herdr-pr-modal)<br><sub>Tarektouati</sub> | Open any pull request in its own worktree, straight from a Herdr | `rust` | 1 | 2026-09-24 |
| [**🆕 herdr-virtualboard**](https://github.com/virtualboard/herdr-virtualboard)<br><sub>virtualboard</sub> | Kanban board for VirtualBoard feature specs inside Herdr: columns are the lifecycle, cards are specs, and dispatching a card starts a role agent in a pane. | `go` | 1 | 2026-09-16 |
| [**🆕 herdr-draft**](https://github.com/ZviBaratz/herdr-draft)<br><sub>ZviBaratz</sub> | herdr プラグイン：新規セッション作成ダイアログです。Linear の issue・worktree・配置場所・エージェントの種類・clauth アカウント・最初のプロンプトを、一度の送信でまとめて設定できます。 | `bubbletea` `claude-code` `go` `linear` `tui` | 1 | 2026-09-23 |
| [**🆕 herdr-plugin-worktree-bootstrap**](https://github.com/0xthc/herdr-plugin-worktree-bootstrap)<br><sub>0xthc</sub> | 新しいherdr worktreeを開いた瞬間に、.envファイルとnode_modulesを投入する | `shell` | 0 | 2026-08-22 |
| [**🆕 herdr-agent-manager**](https://github.com/bleedingfight/herdr-agent-manager)<br><sub>bleedingfight</sub> | fzfベースのファジー検索で、workspace・tab・pane・agentを扱うツール | `python` | 0 | 2026-09-04 |
| [**🆕 herdr-dup-tab**](https://github.com/bonkey/herdr-dup-tab)<br><sub>bonkey</sub> | Herdr プラグイン：フォーカス中のペインで実行しているコマンドを、新しいタブに複製します。 | `shell` | 0 | 2026-09-06 |
| [**🆕 herdr-auto-claude**](https://github.com/Delitefully/herdr-auto-claude)<br><sub>Delitefully</sub> | Start Claude Code in the first pane of every new herdr space. New tabs and splits stay plain shells. | `claude-code` `shell` | 0 | 2026-09-23 |
| [**🆕 herdr-sheep**](https://github.com/huketo/herdr-sheep)<br><sub>huketo</sub> | Herdr のコーディングエージェントを、アニメーションする ASCII アートの羊の群れとして眺められます。 | `ascii-art` `rust` `tui` | 0 | 2026-09-04 |
| [**🆕 herdr-slack-notify**](https://github.com/juninaba/herdr-slack-notify)<br><sub>juninaba</sub> | Herdrのエージェントが完了またはブロックされたら、Slack通知を送る | `javascript` | 0 | 2026-07-07 |
| [**🆕 herdr-awst**](https://github.com/kedwards/herdr-awst)<br><sub>kedwards</sub> | herdr と AWST の連携機能です。 | `shell` | 0 | 2026-09-06 |
| [**🆕 herdr-agent-dash**](https://github.com/MartinBspheroid/herdr-agent-dash)<br><sub>MartinBspheroid</sub> | Herdr Agent Board：稼働中のコーディングエージェント、その状態・作業ディレクトリ・Gitコンテキストを一目で確認できる、ローカルでキーボード操作中心のHerdrプラグイン | `typescript` | 0 | 2026-07-21 |
| [**🆕 herdr-smart-split**](https://github.com/mcostasilva/herdr-smart-split)<br><sub>mcostasilva</sub> | Smart pane splitting for Herdr: automatically split right or down based on pane geometry. | `terminal` `javascript` | 0 | 2026-09-23 |
| [**🆕 tab-blank-number**](https://github.com/riq0h/tab-blank-number)<br><sub>riq0h</sub> | herdrのデフォルトの数字タブラベル（1、2、3…）を空白にするherdrプラグイン | `javascript` | 0 | 2026-07-19 |
| [**🆕 herdr-schlepr**](https://github.com/saiyajosh/herdr-schlepr)<br><sub>saiyajosh</sub> | 洗練されたポップアップから、実行中の Herdr ペインやタブ全体をワークスペース間で移動できます。 | `terminal` `tui` `typescript` | 0 | 2026-09-15 |
| [**🆕 herdr-launcher**](https://github.com/Tatendaz/herdr-launcher)<br><sub>Tatendaz</sub> | herdr TUI 用の非公式 macOS Dock ランチャーです。ラム（Herdr のマスコット）をクリックすれば、ターミナルで herdr が起動します。 | `applescript` `developer-tools` `dock` `launcher` `macos` | 0 | 2026-09-24 |
| [**🆕 herdr-cline-plugin**](https://github.com/TheMetalStorm/herdr-cline-plugin)<br><sub>TheMetalStorm</sub> | 任意のペインから起動した素のCline CLIを、ネイティブのHerdrエージェントのように見せるHerdrプラグイン | `cli` `cline` `herdr-integration` `shell` | 0 | 2026-07-31 |
| [**🆕 herdr-space-branch**](https://github.com/unstable-code/herdr-space-branch)<br><sub>unstable-code</sub> | Focus-aware branch and ahead/behind for herdr's spaces sidebar. | `shell` | 0 | 2026-09-19 |
| [**🆕 live-sync-panes**](https://github.com/wg1k/live-sync-panes)<br><sub>wg1k</sub> | Herdrプラグイン：タブ内のすべてのペインにコマンドを一斉送信、またはキー入力をリアルタイム同期する | `javascript` | 0 | 2026-08-11 |
| [**🆕 herdr-cc-mac-notify**](https://github.com/y-hirakaw/herdr-cc-mac-notify)<br><sub>y-hirakaw</sub> | Claude Code向けのmacOS通知——「完了」だけでなく、エージェントの実際の最後のメッセージを表示する | `claude-code` `macos` `notifications` `python` | 0 | 2026-07-17 |
| [**🆕 herdr-hud**](https://github.com/zetlen/herdr-hud)<br><sub>zetlen</sub> | herdrプラグイン：キーバインドで開くポップアップに、ホスト・ネットワーク・エージェント・セッションの情報を表示——設定変更やカスタムスクリプトによる拡張が可能 | `bash` `terminal` `shell` | 0 | 2026-08-03 |
| [**🆕 herdr-fingers**](https://github.com/nathan-poncet/herdr-fingers)<br><sub>nathan-poncet</sub> | 👉 tmux-fingers for Herdr — type a short hint to copy, paste or open any path, URL, hash or number on screen. Rust, Clean Architecture. | `clean-architecture` `clipboard` `rust` `terminal` `tmux-fingers` | 7 | 2026-09-24 |
| [**🆕 herdr-pane-issue**](https://github.com/ilazaridis/herdr-pane-issue)<br><sub>ilazaridis</sub> | Herdr plugin: shows the GitHub issue each agent pane is working on in the Agents sidebar, and opens it with one key. | `shell` | 3 | 2026-09-24 |
| [**🆕 herdr-pinpoint**](https://github.com/navishachiku/herdr-pinpoint)<br><sub>navishachiku</sub> | Pick a Herdr space, tab, or pane and type its id into the agent you were talking to | `javascript` | 2 | 2026-09-22 |
| [**🆕 herdr_agents_tracker**](https://github.com/VHemanth45/herdr_agents_tracker)<br><sub>VHemanth45</sub> | Herdr plugin that shows your AI subscription usage: account limits in the tab bar, a context meter per agent, low-limit alerts and a token dashboard for Claude… | `chatgpt` `claude` `claude-code` `codex` `herdr-integration` | 2 | 2026-09-24 |
| [**🆕 herdr-pointr**](https://github.com/aristeoibarra/herdr-pointr)<br><sub>aristeoibarra</sub> | Point at a DOM element on a localhost page and it lands in the coding agent that owns that project, with its React component, selector and an optional screensh… | `coding-agent` `devtools` `react` `typescript` | 1 | 2026-09-25 |
| [**🆕 herdr-drop**](https://github.com/ecylmz/herdr-drop)<br><sub>ecylmz</sub> | Drag a file onto a Herdr pane and it lands in that pane's directory, through the ssh session you already have | `file-transfer` `ssh` `terminal` `python` | 1 | 2026-09-18 |
| [**🆕 herdr-paste-image**](https://github.com/grooni/herdr-paste-image)<br><sub>grooni</sub> | Paste images from clipboard into herdr panes (Codex, Gemini CLI) — F8 + clipboard cleanup tools (F9/F10) | `shell` | 1 | 2026-09-21 |
| [**🆕 herdr-opencodex**](https://github.com/nordz0r/herdr-opencodex)<br><sub>nordz0r</sub> | OpenCodex Herdr plugins: spend stats and remaining 5h/7d quota | `opencodex` `quota` `rust` | 1 | 2026-09-23 |
| [**🆕 twig-herdr**](https://github.com/PolyphonyRequiem/twig-herdr)<br><sub>PolyphonyRequiem</sub> | Native Twig bench and digest review panel for Herdr; requires Twig 0.93.0+ and Node.js 22+. | `terminal` `twig` `go` | 0 | 2026-09-24 |
| [**🆕 herdr-agent-usage**](https://github.com/levi-qiao/herdr-agent-usage)<br><sub>levi-qiao</sub> | Credential-scoped AI usage, context, and cache in Herdr for Claude, Codex, Grok, Agy, OpenCode, Pi, omp, Devin, Muse, and Cursor. | `agent-usage` `ai-agents` `antigravity` `claude-code` `codex` | 140 | 2026-09-24 |
| [**🆕 herdr-space-topic**](https://github.com/panuhorsmalahti/herdr-space-topic)<br><sub>panuhorsmalahti</sub> | herdr plugin: name each Space after the work happening inside it — the live topic of its primary agent pane. | `ai-agents` `terminal-multiplexer` `javascript` | 3 | 2026-09-21 |
| [**🆕 herdr-opendeck**](https://github.com/Resilient-Software/herdr-opendeck)<br><sub>Resilient-Software</sub> | Mirror Herdr workspaces onto a Stream Deck. Live tiles with repository, branch and agent status. | `elgato` `opendeck` `stream-deck` `typescript` | 3 | 2026-09-21 |
| [**🆕 spoolway**](https://github.com/marvingygas/spoolway)<br><sub>marvingygas</sub> | Minimalistic agent state machine for software development: a dispatcher that drives agent sessions through defined pipelines | `agent` `automation` `cli` `dispatcher` `llm` | 2 | 2026-09-25 |
| [**🆕 sightr**](https://github.com/bartholomewtj/sightr)<br><sub>bartholomewtj</sub> | Sightr — phone web UI for a Herdr agent herd, over Tailscale | `typescript` | 1 | 2026-09-21 |
| [**🆕 herdr-pane-mover**](https://github.com/dimitri4d/herdr-pane-mover)<br><sub>dimitri4d</sub> | キーボードでもマウスでも使いやすい移動先ピッカーで、実行中の Herdr ペインをタブやワークスペース間で移動できます。 | `go` | 1 | 2026-09-13 |
| [**🆕 herdr-tab-git**](https://github.com/hasuwini77/herdr-tab-git)<br><sub>hasuwini77</sub> | Herdr Spacesのサイドバーに、最初のタブではなくアクティブなタブに追従する形でGitのブランチと状態を表示する | `git` `terminal` `tui` `javascript` | 1 | 2026-08-28 |
| [**🆕 herdr-plugin**](https://github.com/juscribe/herdr-plugin)<br><sub>juscribe</sub> | File and transition Juscribe tickets from a Herdr pane, and see which ticket each agent is on. | `juscribe` `shell` | 1 | 2026-09-21 |
| [**🆕 diskzap**](https://github.com/longwind48/diskzap)<br><sub>longwind48</sub> | Agent skill, Rust CLI and herdr plugin that reclaims GBs of regenerable package caches, build artifacts and Docker cruft. Gated deletion from an explicit catal… | `agent-skills` `ai-agents` `cache` `claude-code` `cleanup` | 1 | 2026-09-21 |
| [**🆕 herdr-snooze**](https://github.com/mrolafsson/herdr-snooze)<br><sub>mrolafsson</sub> | Snooze agents in herdr's Agents panel for 15 minutes, an hour, a day or a week; they come back on their own. A herdr plugin. | `claude-code` `coding-agents` `python` `terminal` `tui` | 1 | 2026-09-24 |
| [**🆕 herdr-which-key**](https://github.com/pradyb/herdr-which-key)<br><sub>pradyb</sub> | Neovim-style which-key popup for herdr: press a leader, see the next keys, run herdr actions | `python` | 1 | 2026-09-21 |
| [**🆕 herdr-plugins**](https://github.com/shelken/herdr-plugins)<br><sub>shelken</sub> | Herdrプラグインのモノレポ（auto-pi：エリアごとにpiを開く＋セッションピッカー） | `python` | 1 | 2026-07-17 |
| [**🆕 herdr-pinned-workspaces**](https://github.com/skydiver/herdr-pinned-workspaces)<br><sub>skydiver</sub> | A Herdr plugin that keeps declared workspaces alive. | `terminal` `tui` `workspaces` `python` | 1 | 2026-09-21 |
| [**🆕 paneMorph**](https://github.com/Jenish-Shobhit/paneMorph)<br><sub>Jenish-Shobhit</sub> | Move live Herdr panes between tabs without restarting their processes. | `terminal-multiplexer` `python` | 0 | 2026-09-21 |
| [**🆕 herdr-lcars**](https://github.com/jlcases/herdr-lcars)<br><sub>jlcases</sub> | Command up to 2,000 Herdr AI agents from one LCARS bridge, track Claude/Codex quota per account, and hand off verified context without losing work. | `agent-observability` `ai-agents` `claude-code` `lcars` `openai-codex` | 9 | 2026-09-22 |
| [**🆕 AgentRadio**](https://github.com/detailles/AgentRadio)<br><sub>detailles</sub> | Local message bus for AI coding agents running in Herdr panes — join, DM, presence, offline delivery | `agent-orchestration` `multi-agent` `radio` `python` | 5 | 2026-09-25 |
| [**🆕 herdr-plugin-cow-worktree**](https://github.com/khatriafaz/herdr-plugin-cow-worktree)<br><sub>khatriafaz</sub> | Herdr plugin for strict copy-on-write Git worktrees that include ignored local files | `typescript` | 3 | 2026-09-20 |
| [**🆕 herdr-disp-model**](https://github.com/pdalinis/herdr-disp-model)<br><sub>pdalinis</sub> | Display active Codex, Claude Code, Pi, and Hermes models in the Herdr agent sidebar. | `ai-agents` `claude-code` `codex` `developer-tools` `hermes-agent` | 3 | 2026-09-19 |
| [**🆕 herdr-commander**](https://github.com/lurepos/herdr-commander)<br><sub>lurepos</sub> | Fast palette to discover/launch npm, cargo, .vscode tasks and commands from herdr | `rust` | 2 | 2026-09-20 |
| [**🆕 herdr-tasks**](https://github.com/Eslsamu/herdr-tasks)<br><sub>Eslsamu</sub> | Herdr 向けの、エージェントが所有するローカルタスクキューです。読み取り専用のライブブラウザビューも備えます。 | `ai-agents` `codex` `local-first` `python` `sqlite` | 1 | 2026-09-09 |
| [**🆕 herdr-reach**](https://github.com/Luisalt20/herdr-reach)<br><sub>Luisalt20</sub> | Read-only network doctor for Herdr remote machines: measures what your network actually allows and recommends a transport with evidence. No writes, no third-pa… | `cli` `cloudflare-tunnel` `connectivity` `egress` `go` | 1 | 2026-09-21 |
| [**🆕 herdr-agent-gateway**](https://github.com/pikujs/herdr-agent-gateway)<br><sub>pikujs</sub> | Secure HTTP remote dispatch gateway, skill, and MCP server for Herdr terminal multiplexer | `javascript` | 1 | 2026-09-24 |
| [**🆕 herdr-llm-lint**](https://github.com/shindakun/herdr-llm-lint)<br><sub>shindakun</sub> | Lints CLAUDE.md, AGENTS.md, and agent instruction files for stale paths, commands, facts, and drift | `agents-md` `ai-agents` `claude-code` `claude-md` `cli` | 1 | 2026-09-21 |
| [**🆕 herdr-rss**](https://github.com/shindakun/herdr-rss)<br><sub>shindakun</sub> | An RSS reader plugin for herdr, cuz why not | `rss` `rss-reader` `rust` | 1 | 2026-09-24 |
| [**🆕 herdr-testrun**](https://github.com/shindakun/herdr-testrun)<br><sub>shindakun</sub> | Herdr plugin. Runs a project's tests in a pane, lists the failures, sends them to the agent on one key. | `go` `nodejs` `rust` | 1 | 2026-09-20 |
| [**🆕 herdr-webhook-notify**](https://github.com/zgxme/herdr-webhook-notify)<br><sub>zgxme</sub> | Herdr plugin that forwards agent notifications to Slack, Discord, Teams, Google Chat, Feishu, Lark, DingTalk, WeCom, Telegram, ntfy or any HTTP webhook | `dingtalk` `discord` `feishu` `lark` `notifications` | 1 | 2026-09-21 |
| [**🆕 herdr-agent-index**](https://github.com/kadaliao/herdr-agent-index)<br><sub>kadaliao</sub> | Show each Herdr agent's panel number in the sidebar, so focus_agent = prefix+alt+1..9 has visible targets. | `sidebar` `terminal` `python` | 0 | 2026-09-20 |
| [**🆕 herdr-plugin-workspace-groups**](https://github.com/kwanwooi25/herdr-plugin-workspace-groups)<br><sub>kwanwooi25</sub> | Keyboard-first workspace grouping and colored sidebar badges for Herdr | `python` `terminal` `workspace-manager` | 0 | 2026-09-20 |
| [**🆕 pet-town**](https://github.com/abhishek944/pet-town)<br><sub>abhishek944</sub> | A transparent desktop village for live Herdr agents | `rust` | 3 | 2026-09-21 |
| [**🆕 kubeflock**](https://github.com/LoriKarikari/kubeflock)<br><sub>LoriKarikari</sub> | Herdr 内で Kubernetes のサンドボックスを作成・接続できます。 | `agent-sandbox` `gvisor` `kubernetes` `sandbox` `go` | 3 | 2026-09-11 |
| [**🆕 herdr-ctx-bar**](https://github.com/pdalinis/herdr-ctx-bar)<br><sub>pdalinis</sub> | Color-coded context-window usage bars for Codex, Claude Code, Pi, and Hermes Agent in Herdr's Agents sidebar. | `ai-agents` `claude-code` `codex` `context-window` `hermes-agent` | 3 | 2026-09-19 |
| [**🆕 asconfirmclose**](https://github.com/asumaran/asconfirmclose)<br><sub>asumaran</sub> | Herdr plugin: close the focused pane, asking first only when a process is running in it | `terminal` `go` | 1 | 2026-09-20 |
| [**🆕 asgoto**](https://github.com/asumaran/asgoto)<br><sub>asumaran</sub> | Tree-style switcher across herdr repos, worktrees and panes | `go` | 1 | 2026-09-24 |
| [**🆕 shop-plugin**](https://github.com/kyrosle/shop-plugin)<br><sub>kyrosle</sub> | A visible multi-agent workstation for Pi + Herdr, with configurable Lead/Worker models, file-based task handoffs, and explicit review. Local alpha. | `coding-agent` `developer-tools` `human-in-the-loop` `multi-agent` `pi-coding-agent` | 1 | 2026-09-21 |
| [**🆕 herdr-tasks**](https://github.com/pinkpixel-dev/herdr-tasks)<br><sub>pinkpixel-dev</sub> | A Herdr plugin that puts your agent's task list in a split pane beside it, checked off as the agent works. | `ai` `ai-agents` `antigravity` `claude-code` `cli` | 1 | 2026-09-19 |
| [**🆕 goat-herdr**](https://github.com/shindakun/goat-herdr)<br><sub>shindakun</sub> | 🐐 Herdr plugin: alerts to Telegram, Slack, ntfy, Pushover/bullet or any webhook when an agent needs you | `ntfy` `rust` `slack` `telegram` `webhook` | 1 | 2026-09-24 |
| [**🆕 herdr-issues**](https://github.com/zamarrowski/herdr-issues)<br><sub>zamarrowski</sub> | herdr plugin: browse the GitHub issues of the repo you're in and hand one to any coding agent (Claude Code, Codex, Gemini…) in its own git worktree. | `coding-agents` `github-issues` `javascript` | 1 | 2026-09-19 |
| [**🆕 herdr-ai-notify**](https://github.com/8liang/herdr-ai-notify)<br><sub>8liang</sub> | _(説明なし)_ | `notifications` `shell` | 0 | 2026-09-09 |
| [**🆕 herdr-ipc**](https://github.com/adihex/herdr-ipc)<br><sub>adihex</sub> | Herdr plugin + Agent Plugin: workspace-scoped Unix-socket IPC for pane workers | `ipc` `python` | 0 | 2026-09-20 |
| [**🆕 herdr-plugin-echo**](https://github.com/andischerer/herdr-plugin-echo)<br><sub>andischerer</sub> | 1つのペインから、マークした複数のペインにキー入力をブロードキャストするHerdrプラグイン | `typescript` | 0 | 2026-08-23 |
| [**🆕 asgotopr**](https://github.com/asumaran/asgotopr)<br><sub>asumaran</sub> | Herdr plugin: jump to your open GitHub PRs across local repos and worktrees | `go` | 0 | 2026-09-24 |
| [**🆕 herdr-links**](https://github.com/dima-m711/herdr-links)<br><sub>dima-m711</sub> | Herdr と Pi 向けの、セッションに紐づいたナビゲーションリンクです。 | `typescript` | 0 | 2026-09-13 |
| [**🆕 herdr-plugin-dotfiles-dev-layout**](https://github.com/edmundmiller/herdr-plugin-dotfiles-dev-layout)<br><sub>edmundmiller</sub> | 自分のdotfilesの開発用ワークスペースレイアウトを開くためのHerdrプラグイン | `python` | 0 | 2026-06-23 |
| [**🆕 herdr-terminal-scripts**](https://github.com/Fadi729/herdr-terminal-scripts)<br><sub>Fadi729</sub> | Herdr plugin that runs named Scripts from a popup or numbered slots | `typescript` | 0 | 2026-09-21 |
| [**🆕 herdr-drover**](https://github.com/followbl/herdr-drover)<br><sub>followbl</sub> | Herdr 用の「牧羊犬」タブスイッチャー。Super+T を押し続けてタブを巡回し、離した位置で切り替わります。 | `linux` `python` | 0 | 2026-09-03 |
| [**🆕 herdr-reap**](https://github.com/ivorpad/herdr-reap)<br><sub>ivorpad</sub> | herdrプラグイン：全エージェントのライフサイクル状態を表示し、1キーで完了済みのものをまとめて閉じる | `tui` `python` | 0 | 2026-08-27 |
| [**🆕 herdr-ntfy-notify**](https://github.com/jjuraszek/herdr-ntfy-notify)<br><sub>jjuraszek</sub> | Herdr プラグイン：エージェントがブロックされたり完了したりしたときに、ntfy でスマホへプッシュ通知します。 | `ntfy` `javascript` | 0 | 2026-09-13 |
| [**🆕 herdr-nnn**](https://github.com/linuxing3/herdr-nnn)<br><sub>linuxing3</sub> | herdr内でnnnを開く | `shell` | 0 | 2026-08-04 |
| [**🆕 herdr-spaces**](https://github.com/lukecameron/herdr-spaces)<br><sub>lukecameron</sub> | Agent counts and model-generated names for Herdr spaces | `go` | 0 | 2026-09-24 |
| [**🆕 herdr-tab-title**](https://github.com/Newt6611/herdr-tab-title)<br><sub>Newt6611</sub> | Herdr Tab Titleは、「1. Codex」「2. Terminal」のような、ワークスペース単位できれいに番号付けされた名前にHerdrのタブを自動リネームする。フォーマットはカスタマイズ可能 | `rust` | 0 | 2026-07-09 |
| [**🆕 agentic-box**](https://github.com/nicoRomeroCuruchet/agentic-box)<br><sub>nicoRomeroCuruchet</sub> | Claude Codeがローカルモデルのエージェントを操作する、隔離されたbox | `agent-orchestration` `agentic` `agentic-workflow` `docker` `ornith-1-0-35b` | 0 | 2026-08-17 |
| [**🆕 herdr-bot**](https://github.com/Phoobobo/herdr-bot)<br><sub>Phoobobo</sub> | _(説明なし)_ | `tui` `typescript` | 0 | 2026-09-02 |
| [**🆕 herdr-worktree-include**](https://github.com/scoussens-nthplusio/herdr-worktree-include)<br><sub>scoussens-nthplusio</sub> | リポジトリの.worktreeincludeを使って、.envなどgit管理外のファイルを新しいHerdr worktreeにコピーする——Claude Codeが使うのと同じファイル・同じルール | `dotenv` `git-worktree` `shell` | 0 | 2026-08-27 |
| [**🆕 herdr-tab-new**](https://github.com/softwarecrafts/herdr-tab-new)<br><sub>softwarecrafts</sub> | このプロジェクトの herdr ワークスペースで、エージェントセッションを再開または開始します。herdr プラグインであると同時に、herdr の外のターミナルからも使える CLI でもあります。 | `typescript` | 0 | 2026-08-31 |
| [**🆕 herdr-worktrees**](https://github.com/SpaceK33z/herdr-worktrees)<br><sub>SpaceK33z</sub> | Switch, create, and remove Git worktrees from a Herdr popup | `rust` | 0 | 2026-09-17 |
| [**🆕 herdr-focus**](https://github.com/trapple/herdr-focus)<br><sub>trapple</sub> | 次にブロック中/完了したエージェントペインにフォーカスし、ターミナルアプリを最前面に出す。グローバルホットキー付き | `shell` | 0 | 2026-07-19 |
| [**🆕 herdr-projects**](https://github.com/eliasstravik/herdr-projects)<br><sub>eliasstravik</sub> | A coordinator conversation, parallel worker threads, shared memory and an overview of what needs you. A Herdr plugin. | `rust` | 444 | 2026-09-25 |
| [**🆕 entwurf**](https://github.com/junghan0611/entwurf)<br><sub>junghan0611</sub> | Herdr and tmux sibling AI sessions: pi, Claude Code, Codex, Copilot, OMP and Antigravity can message and spawn each other while keeping their own auth, tools a… | `acp` `agent-client-protocol` `ai-agent` `claude-code` `codex` | 28 | 2026-09-23 |
| [**🆕 herdr-omni**](https://github.com/mmjang/herdr-omni)<br><sub>mmjang</sub> | One search for Herdr workspaces, actions, and live or saved Codex & Claude sessions. Fuzzy-find by name, search conversation content, and resume where you left… | `claude-code` `codex` `opencode` `rust` | 9 | 2026-09-22 |
| [**🆕 herdr-transcripts**](https://github.com/hxreborn/herdr-transcripts)<br><sub>hxreborn</sub> | Search your coding-agent sessions, past and live, by any word you remember, then jump to them or resume them | `claude-code` `codex` `coding-agents` `droid` `fzf` | 6 | 2026-09-21 |
| [**🆕 herdr-tmux-session-navigator**](https://github.com/caneppelevitor/herdr-tmux-session-navigator)<br><sub>caneppelevitor</sub> | tmux choose-tree for herdr. Written by someone who left tmux but never gave up prefix+s. | `bubbletea` `terminal` `tmux` `go` | 4 | 2026-09-18 |
| [**🆕 herdr-chat**](https://github.com/eliasstravik/herdr-chat)<br><sub>eliasstravik</sub> | Herdr内で動くエージェント向けの、構造化されたライブチャットビュー | `typescript` | 2 | 2026-08-24 |
| [**🆕 herdr-stt**](https://github.com/xtwist/herdr-stt)<br><sub>xtwist</sub> | Speech-to-text for Herdr | `rust` | 2 | 2026-09-18 |
| [**🆕 herdr-agent-icons**](https://github.com/adihex/herdr-agent-icons)<br><sub>adihex</sub> | Herdr plugin: real per-agent logo icons in the sidebar via a generated PUA font | `python` | 1 | 2026-09-18 |
| [**🆕 herdr-revive**](https://github.com/cantona/herdr-revive)<br><sub>cantona</sub> | Restore Herdr commands, layouts and exact agent sessions with preview, named workspaces and explicit recovery. | `rust` `session-management` `terminal` `terminal-based` `terminal-multiplexer` | 1 | 2026-09-19 |
| [**🆕 herdr-hosts**](https://github.com/ecylmz/herdr-hosts)<br><sub>ecylmz</sub> | Hierarchical SSH host picker for Herdr, with folders and notes straight from ~/.ssh/config | `ratatui` `rust` `ssh` `terminal` `tui` | 1 | 2026-09-18 |
| [**🆕 herdr-visuals**](https://github.com/hx-w/herdr-visuals)<br><sub>hx-w</sub> | Herdr 向けに、セッション単位で Mermaid・LaTeX・ローカル画像のプレビューを表示します。Kitty のグラフィックプロキシにも対応。 | `javascript` | 1 | 2026-09-19 |
| [**🆕 nexus**](https://github.com/IniZio/nexus)<br><sub>IniZio</sub> | Herdr plugin for running worktree in Cloud-Hypervisor sandboxes, with mem/cpu/disk hotplug and auto port-forwarding | `cloud-hypervisor` `go` | 1 | 2026-09-25 |
| [**🆕 herdr-tiling**](https://github.com/jaeheonji/herdr-tiling)<br><sub>jaeheonji</sub> | Hyprland-style pane movement and tmux-style layouts for Herdr | `rust` | 1 | 2026-09-18 |
| [**🆕 herdr-equalize-panes**](https://github.com/ponko2/herdr-equalize-panes)<br><sub>ponko2</sub> | ペインが作成・クローズ・移動・終了するたびに、各タブ内のペインを自動的に均等サイズに保つ | `rust` | 1 | 2026-09-23 |
| [**🆕 herdr-pane-resurrect**](https://github.com/unstable-code/herdr-pane-resurrect)<br><sub>unstable-code</sub> | Save the commands running in your herdr panes and bring them back after a restart. | `shell` | 1 | 2026-09-19 |
| [**🆕 herdr-plugins**](https://github.com/VladPatr96/herdr-plugins)<br><sub>VladPatr96</sub> | Plugins for Herdr, the terminal workspace manager for AI coding agents | `javascript` | 1 | 2026-09-22 |
| [**🆕 herdr-numbered-workspaces**](https://github.com/abrose/herdr-numbered-workspaces)<br><sub>abrose</sub> | herdrのサイドバーの各スペースの先頭に番号を付け、インデックス指定のswitch_workspaceショートカットと対応させる | `shell` | 0 | 2026-07-21 |
| [**🆕 herdr-better-worktrees**](https://github.com/bearylabs/herdr-better-worktrees)<br><sub>bearylabs</sub> | A fast Herdr popup for managing Git worktrees in a predictable embedded-bare layout: create, clone, open, inspect, fetch, and safely remove worktrees while kee… | `typescript` | 0 | 2026-09-18 |
| [**🆕 herdr-tabline**](https://github.com/btj93/herdr-tabline)<br><sub>btj93</sub> | 安全なテンプレートとプロジェクトを認識するプロファイルで、Herdr のタブラベルを描画します。 | `golang` `tabline` `terminal` `tui` `go` | 0 | 2026-09-04 |
| [**🆕 herdr-pi-slack-notify**](https://github.com/DylanG5/herdr-pi-slack-notify)<br><sub>DylanG5</sub> | Herdr plugin that sends Slack notifications when unseen Pi agent runs finish. | `pi` `slack-notifications` `javascript` | 0 | 2026-09-18 |
| [**🆕 herdr-menu**](https://github.com/leonardoacosta/herdr-menu)<br><sub>leonardoacosta</sub> | Pane, tab, and workspace management actions for Herdr | `menu` `pane` `tab` `workspace` `shell` | 0 | 2026-09-16 |
| [**🆕 herdr-idle-panes**](https://github.com/leonho/herdr-idle-panes)<br><sub>leonho</sub> | herdrプラグイン：アイドル状態のシェルのままになっているペインを確認して閉じる、チェックリスト形式のポップアップ | `python` | 0 | 2026-08-22 |
| [**🆕 herdr-pane-id-metadata**](https://github.com/limars874/herdr-pane-id-metadata)<br><sub>limars874</sub> | 正規化されたペインIDと、コンパクトなタブ/ペインのサイドバーメタデータのための、最小構成のHerdrプラグイン | `coding-agents` `terminal` `javascript` | 0 | 2026-08-17 |
| [**🆕 herdr-linear-launcher**](https://github.com/logocode/herdr-linear-launcher)<br><sub>logocode</sub> | Linear の issue から、バックグラウンドの Herdr worktree で Codex や Claude を起動します。 | `javascript` | 0 | 2026-09-17 |
| [**🆕 herdr-battery**](https://github.com/morphysh/herdr-battery)<br><sub>morphysh</sub> | Laptop battery status for the herdr tab bar (⚡charging 🔋on-battery 🔌held), plus a health/power details popup. Linux sysfs, zero dependencies. | `battery` `linux` `status-bar` `shell` | 0 | 2026-09-23 |
| [**🆕 nvim-ascii-on-focus**](https://github.com/NathanymousFu/nvim-ascii-on-focus)<br><sub>NathanymousFu</sub> | Switch to a Latin input source when a Herdr pane running Neovim gains focus | `input-method` `macos` `neovim` `shell` | 0 | 2026-09-18 |
| [**🆕 herdr-claude-profile**](https://github.com/quinnjr/herdr-claude-profile)<br><sub>quinnjr</sub> | herdrプラグイン：オーバーレイのパレットからclaude-profileのプロファイルを切り替え・管理する | `typescript` | 0 | 2026-09-11 |
| [**🆕 ocean-herdr**](https://github.com/Risingtides-dev/ocean-herdr)<br><sub>Risingtides-dev</sub> | Herdr向けのOceanエージェント連携 | `coding-agent` `ocean` `rust` | 0 | 2026-07-17 |
| [**🆕 tmurdr**](https://github.com/sergiopx/tmurdr)<br><sub>sergiopx</sub> | Herdr で tmux の指の記憶をそのまま使えます。ctrl+space プレフィックスと tmux のキーマップ全体を、あなたの config.toml に適用します。 | `keybindings` `terminal` `tmux` `shell` | 0 | 2026-09-14 |
| [**🆕 herdr-worktree-from-gitlab**](https://github.com/snics/herdr-worktree-from-gitlab)<br><sub>snics</sub> | herdrプラグイン：GitLabのissueから（glab経由で）git worktreeとワークスペースを作成する | `gitlab` `rust` `worktree` | 0 | 2026-07-09 |
| [**🆕 herdr-pane-restart**](https://github.com/zap0xfce2/herdr-pane-restart)<br><sub>zap0xfce2</sub> | サーバー起動時に、名前付きペインで設定済みのコマンドを実行する | `python` | 0 | 2026-09-15 |

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-notify"></a>

## 通知・アラート

> エージェントが完了した / 入力待ちで止まったのを、席を外していても知りたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**Heeler**](https://github.com/ZingerLittleBee/Heeler)<br><sub>ZingerLittleBee</sub> | herdr 用のネイティブ iOS エージェントコンソールです。SSH 経由でお使いのマシン上のコーディングエージェントを監視・操作できます。本物の libghostty ターミナル、QR コードによるペアリング、エージェントがあなたを必要とするときのプッシュ通知を備えます。 | `ai-agents` `apns` `coding-agents` `ios` `libghostty` | 404 | 🔄 2026-09-24 |
| [**herdr-ohmyzsh**](https://github.com/robbyrussell/herdr-ohmyzsh)<br><sub>robbyrussell</sub> | Herdr 用の Oh My Zsh プラグインです。時間のかかるコマンドをサイドバーに表示し、完了通知やシェルヘルパーを提供、さらにキー一つでアイドル中の全ペインの Oh My Zsh をリロードできます。 | `oh-my-zsh` `zsh` `shell` | 77 | 2026-09-09 |
| [**herdr-focus-notify**](https://github.com/yankewei/herdr-focus-notify)<br><sub>yankewei</sub> | Herdrのエージェント向けの、クリック可能なmacOS通知。エージェントがブロックまたは完了するとネイティブのトースト通知を送り、クリックするとターミナルを最前面に出して該当のHerdrペインにフォーカスする | `alerter` `macos` `notifications` `productivity` `rust` | 26 | 🔄 2026-09-24 |
| [**herdr-terminal-notifier**](https://github.com/dot/herdr-terminal-notifier)<br><sub>dot</sub> | terminal-notifier経由で、herdrエージェントの状態変化をカスタマイズ可能なmacOS通知として送る | `macos` `terminal-notifier` `shell` | 9 | 2026-09-07 |
| [**herdr-pings**](https://github.com/joelhooks/herdr-pings)<br><sub>joelhooks</sub> | herdrのペインで動くAIエージェント向けの、ターン単位のウェイクイベント通知——piエクステンション、waitコマンド、クラッシュブリッジ、ワーカー用のDiscworld風コールサイン付き | `ai-agents` `pi` `typescript` | 9 | 2026-08-09 |
| [**herdr-ntfy**](https://github.com/horn553/herdr-ntfy)<br><sub>horn553</sub> | 依存関係最小限（jq・curl・sh）——Herdrのエージェントが完了またはブロックされたときにntfy通知を送る | `shell` | 8 | 🔄 2026-09-16 |
| [**herdr-ntfy-notify**](https://github.com/zom-2018/herdr-ntfy-notify)<br><sub>zom-2018</sub> | Herdrのターミナルエージェント向けの、リアルタイムなntfyプッシュ通知 | `agent` `ntfy` `push-notifications` `tui` `javascript` | 8 | 2026-06-23 |
| [**herdr-hail**](https://github.com/natori-hrj/herdr-hail)<br><sub>natori-hrj</sub> | herdr向けのSlack/Discord双方向ブリッジ——エージェントがブロックされたら通知が来て、返信/タップでブロックを解除できる。トンネル不要 | `discord` `slack` `typescript` | 7 | 2026-07-19 |
| [**herdr-telegram-bridge**](https://github.com/cokekitten/herdr-telegram-bridge)<br><sub>cokekitten</sub> | herdrのエージェントが完了またはブロックされたらTelegramにプッシュ通知が来る——返信すればテキストやファイルをそのままエージェントに送り返せる。サーバー・トンネル・アプリ不要 | `ai-agents` `chatops` `claude-code` `developer-tools` `notifications` | 5 | 2026-08-06 |
| [**herdr-telegram-plugin**](https://github.com/mvallebr/herdr-telegram-plugin)<br><sub>mvallebr</sub> | herdr向けのTelegramボットコンパニオン——Telegramのフォーラムトピック経由で任意のエージェントを遠隔操作。処理経路にLLMは介在しない | `typescript` | 5 | 2026-08-31 |
| [**herdr-notify-windows**](https://github.com/aclima01/herdr-notify-windows)<br><sub>aclima01</sub> | herdrのエージェント向けのWindows 11トースト通知（ターン完了/入力待ち） | `powershell` | 4 | 2026-07-23 |
| [**herdr-cache-alert**](https://github.com/AltanS/herdr-cache-alert)<br><sub>AltanS</sub> | herdrプラグイン：全エージェントペインにプロンプトキャッシュのカウントダウンを表示——各キャッシュルールの出典と日付も併せて示す | `ai-agents` `ai-coding` `ai-tools` `claude-code` `multiplexing` | 4 | 🔄 2026-09-17 |
| [**session-sounds**](https://github.com/ChrisPachulski/session-sounds)<br><sub>ChrisPachulski</sub> | macOSとLinux向けに、Herdrのエージェントごとに異なる完了音・注意喚起音を鳴らす | `coding-agents` `notifications` `rust` | 3 | 2026-07-19 |
| [**herdr-announcer**](https://github.com/nhclink16/herdr-announcer)<br><sub>nhclink16</sub> | Herdrプラグイン：エージェントが完了または入力待ちになったら、LLMによる一文要約を音声で読み上げる——ローカルTTS、ElevenLabs、任意のカスタムコマンドに対応 | `tts` `rust` | 3 | 2026-09-09 |
| [**herdr-discord-presence**](https://github.com/revanp/herdr-discord-presence)<br><sub>revanp</sub> | herdrプラグイン：Herdrのセッションとエージェントの状態を、Discord Rich Presenceとして表示する | `typescript` | 3 | 2026-08-14 |
| [**herdr-agent-notify**](https://github.com/A1exthegreat/herdr-agent-notify)<br><sub>A1exthegreat</sub> | herdrプラグイン：エージェントが作業を終えた、確認が必要になった、またはアイドルになったときにデスクトップ通知を送る | `javascript` | 2 | 2026-08-15 |
| [**buzzr**](https://github.com/candypoets/buzzr)<br><sub>candypoets</sub> | 稼働中のHerdrのspaceとエージェントを、Nostrアイデンティティとメンションルーティング付きでBuzzチャンネルにミラーする | `agents` `buzz` `nostr` `rust` | 2 | 2026-08-14 |
| [**agent-webhook-notify**](https://github.com/happyeric77/agent-webhook-notify)<br><sub>happyeric77</sub> | Herdrのエージェントが完了またはブロックされたときに、Webhook通知を送る | `javascript` | 2 | 2026-08-12 |
| [**herdr-bar**](https://github.com/openalon-org/herdr-bar)<br><sub>openalon-org</sub> | Herdr 用の macOS メニューバーアプリ。エージェントの件数をリアルタイムに表示し、ワンクリックであなたを必要としているペインへ移動できます。 | `herdr-notify` `menu-bar` `menu-bar-app` `notification` `notify` | 2 | 🔄 2026-09-18 |
| [**herdr-guard**](https://github.com/StructuPath/herdr-guard)<br><sub>StructuPath</sub> | Herdr向けのエージェント横断コマンドポリシー：危険なシェルコマンドを監査・警告・中断する | `ai-agents` `command-policy` `security` `terminal` `javascript` | 2 | 🔄 2026-09-14 |
| [**herdr-wsl-notify**](https://github.com/tkmct/herdr-wsl-notify)<br><sub>tkmct</sub> | WSL2上で動くエージェント（Claude Codeなど）が完了またはブロック（承認/入力待ち）になったときに、Windowsのデスクトップトースト通知を表示するHerdrプラグイン | `javascript` | 2 | 2026-08-27 |
| [**herdr-notifications**](https://github.com/barnuri/herdr-notifications)<br><sub>barnuri</sub> | herdr プラグイン：エージェントがアイドルになったとき、ブロックされたとき、完了したときに Telegram で通知します。 | `telegram` `javascript` | 1 | 2026-09-08 |
| [**herdr-prayer-times**](https://github.com/bayoudhi/herdr-prayer-times)<br><sub>bayoudhi</sub> | 次の礼拝時刻とカウントダウンをHerdrのサイドバーに表示——タイムテーブルのポップアップと通知付き | `rust` | 1 | 2026-08-13 |
| [**herdr-random-sounds**](https://github.com/gridness/herdr-random-sounds)<br><sub>gridness</sub> | macOS版herdrで、エージェントの状態ごとにランダムな通知音を再生する | `herdr-integration` `macos` `notification` `notifications` `python` | 1 | 2026-08-23 |
| [**herdr-telegram-slack-bridge**](https://github.com/lsisoft/herdr-telegram-slack-bridge)<br><sub>lsisoft</sub> | Herdrのエージェントセッション向けの、TelegramとSlackボットの双方向ブリッジ——ブロックされたエージェントの通知やチャットの返信を、Herdrやtmuxのペインに転送する | `ai-agents` `slack-bot` `telegram-bot` `tmux` `python` | 1 | 2026-07-28 |
| [**herdr-telegram-notify**](https://github.com/naturalmoods/herdr-telegram-notify)<br><sub>naturalmoods</sub> | Herdr プラグイン：エージェントが完了またはブロックされたときに Telegram へ通知します——セッションタイトル、プロジェクト、所要時間、トークン使用量、最後のメッセージを含みます。チャットで返信すれば、その内容はそのエージェントへ送り返されます。 | `claude-code` `notifications` `telegram` `javascript` | 1 | 🔄 2026-09-22 |
| [**herdr-notify-wsl**](https://github.com/saeedrahimi/herdr-notify-wsl)<br><sub>saeedrahimi</sub> | WSL内で動くherdrエージェント向けのWindows 11トースト通知——aclima01/herdr-notify-windowsをベースにしている | `powershell` | 1 | 2026-07-23 |
| [**🆕 goat-herdr**](https://github.com/shindakun/goat-herdr)<br><sub>shindakun</sub> | 🐐 Herdr plugin: alerts to Telegram, Slack, ntfy, Pushover/bullet or any webhook when an agent needs you | `ntfy` `rust` `slack` `telegram` `webhook` | 1 | 🔄 2026-09-24 |
| [**🆕 herdr-webhook-notify**](https://github.com/zgxme/herdr-webhook-notify)<br><sub>zgxme</sub> | Herdr plugin that forwards agent notifications to Slack, Discord, Teams, Google Chat, Feishu, Lark, DingTalk, WeCom, Telegram, ntfy or any HTTP webhook | `dingtalk` `discord` `feishu` `lark` `notifications` | 1 | 🔄 2026-09-21 |
| [**🆕 herdr-ai-notify**](https://github.com/8liang/herdr-ai-notify)<br><sub>8liang</sub> | _(説明なし)_ | `notifications` `shell` | 0 | 2026-09-09 |
| [**🆕 herdr-pi-slack-notify**](https://github.com/DylanG5/herdr-pi-slack-notify)<br><sub>DylanG5</sub> | Herdr plugin that sends Slack notifications when unseen Pi agent runs finish. | `pi` `slack-notifications` `javascript` | 0 | 🔄 2026-09-18 |
| [**herdr-telegram-notify**](https://github.com/elkraps/herdr-telegram-notify)<br><sub>elkraps</sub> | Herdrエージェントの状態変化に対する、カスタマイズ可能なTelegram通知——ステータスフィルタ、テンプレート、複数チャットへの配信、重複排除、Codex承認ボタン、完了サマリー、組み込みの診断機能に対応 | `ai-agents` `automation` `developer-tools` `javascript` `nodejs` | 0 | 2026-08-27 |
| [**herdr-oncall**](https://github.com/fulanto/herdr-oncall)<br><sub>fulanto</sub> | 浮動する macOS パネルまたは Telegram から、コーディングエージェントの権限確認プロンプトに答えられます——Claude Code と Codex 向けの Herdr プラグインです。 | `ai-agents` `claude-code` `cli` `codex` `coding-agent` | 0 | 🔄 2026-09-24 |
| [**herdr-hitl**](https://github.com/huketo/herdr-hitl)<br><sub>huketo</sub> | Herdr のコーディングエージェントを、人の判断待ちで一時停止させ、Telegram や Discord 経由でスマホに通知します。 | `agent-skill` `ai-agents` `cli` `discord-bot` `go` | 0 | 🔄 2026-09-21 |
| [**🆕 herdr-ntfy-notify**](https://github.com/jjuraszek/herdr-ntfy-notify)<br><sub>jjuraszek</sub> | Herdr プラグイン：エージェントがブロックされたり完了したりしたときに、ntfy でスマホへプッシュ通知します。 | `ntfy` `javascript` | 0 | 🔄 2026-09-13 |
| [**🆕 herdr-slack-notify**](https://github.com/juninaba/herdr-slack-notify)<br><sub>juninaba</sub> | Herdrのエージェントが完了またはブロックされたら、Slack通知を送る | `javascript` | 0 | 2026-07-07 |
| [**herdr-apple-music-plugin**](https://github.com/perlporter/herdr-apple-music-plugin)<br><sub>perlporter</sub> | Apple Music（macOS）の再生曲が変わったときに、herdrでトースト通知を表示する | `shell` | 0 | 2026-07-28 |
| [**🆕 herdr-notify-router**](https://github.com/pradyb/herdr-notify-router)<br><sub>pradyb</sub> | Rules for herdr agent notifications: when to alert and where it goes (webhook, ntfy, desktop), with quiet hours and dedupe | `python` | 0 | 🔄 2026-09-22 |
| [**🆕 herdr-notify-center**](https://github.com/ram4-dev/herdr-notify-center)<br><sub>ram4-dev</sub> | サーバー全体のエージェント通知を、永続化されたポップアップ受信箱でHerdrに提供する | `notifications` `typescript` | 0 | 2026-08-14 |
| [**herdr-kaku-bell**](https://github.com/Rockheung/herdr-kaku-bell)<br><sub>Rockheung</sub> | エージェントが手（入力）を待っているとき、kaku タブにドットを点灯させます——herdr プラグイン。 | `kaku` `terminal` `python` | 0 | 2026-09-06 |
| [**🆕 herdr-cc-mac-notify**](https://github.com/y-hirakaw/herdr-cc-mac-notify)<br><sub>y-hirakaw</sub> | Claude Code向けのmacOS通知——「完了」だけでなく、エージェントの実際の最後のメッセージを表示する | `claude-code` `macos` `notifications` `python` | 0 | 2026-07-17 |
| [**herdr-wake_on_lan**](https://github.com/zbyhoo/herdr-wake_on_lan)<br><sub>zbyhoo</sub> | Wake sleeping Herdr SSH machines with Wake-on-LAN — terminal app and Herdr plugin | `cli` `terminal` `tui` `typescript` `wake-on-lan` | 0 | 🔄 2026-09-17 |

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-remote"></a>

## スマホ・リモート操作

> 外出先やスマホからエージェントを監視して、承認だけ返したい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**collie**](https://github.com/AltanS/collie)<br><sub>AltanS</sub> | Self-hosted mobile terminal for coding agents on herdr (or tmux/zellij). PWA with push alerts + tailnet accessible | `agent-orchestration` `ai` `ai-agents` `ai-coding` `ai-tools` | 1095 | 🔄 2026-09-24 |
| [**herdr-remote**](https://github.com/dcolinmorgan/herdr-remote)<br><sub>dcolinmorgan</sub> | メニューバー・スマホ・Telegramからherdrのエージェントを監視・操作。ローカル設定不要、リモート接続用の無料トンネル付きでTailscaleも不要 | `macos` `mobile` `python` | 386 | 🔄 2026-09-24 |
| [**herdr-mobile-relay**](https://github.com/0cv/herdr-mobile-relay)<br><sub>0cv</sub> | スマホからHerdrのエージェントを遠隔で承認・監視できる、Android/iOS向けのモバイルWebアプリ。プッシュ通知・QRコードでの設定・複数PCへの中継に対応 | `android` `approvals` `cloudflare` `ios` `mobile` | 252 | 🔄 2026-09-25 |
| [**pairfob**](https://github.com/arronKler/pairfob)<br><sub>arronKler</sub> | Herdr のスマホ用インターフェースです。Codex・Claude・Grok はそのままパソコン上で動き続け、スマホからは同じ稼働中のセッションを開けます。ペアリングは一度だけ——パソコン側から発信する仕組みなので、受信ポートの開放も Tailscale も不要です。 | `herdr-mobile` `typescript` | 78 | 🔄 2026-09-25 |
| [**herdr-telegram-agents**](https://github.com/permgps/herdr-telegram-agents)<br><sub>permgps</sub> | ターミナルからと同じように、Telegram からコーディングエージェントを操作できます。エージェントごとにトピックを分け、トピックアイコンにライブステータスを表示、選択肢はインラインボタン付きの双方向チャットで行えます。 | `claude-code` `coding-agents` `go` `telegram` `telegram-bot` | 72 | 🔄 2026-09-24 |
| [**herdr-watch**](https://github.com/Unayung/herdr-watch)<br><sub>Unayung</sub> | herdrのエージェント状態をApple Watchで確認できる | `javascript` | 28 | 2026-08-14 |
| [**herdr-connect**](https://github.com/Tomyail/herdr-connect)<br><sub>Tomyail</sub> | この iPhone 用モバイルコンパニオンアプリで、Herdr の AI コーディングエージェントを監視・操作できます——出力を読み、追加の指示を送り、ジョブ完了時には通知を受け取れます。LAN や Tailscale 経由でプライベートに動作し、クラウドもアカウントも不要です。 | `agent` `mobile-app` `react-native` `typescript` | 18 | 🔄 2026-09-25 |
| [**herdr-web**](https://github.com/barnuri/herdr-web)<br><sub>barnuri</sub> | herdr向けのモバイルファーストなWeb UIプラグイン——通知付きで、スマホからコーディングエージェントを操作できる | `pwa` `typescript` | 12 | 2026-09-10 |
| [**herdr-plugin-mobile-relay**](https://github.com/benkraus/herdr-plugin-mobile-relay)<br><sub>benkraus</sub> | _(説明なし)_ | `typescript` | 11 | 2026-08-12 |
| [**vscode-devcontainers-herdr**](https://github.com/scott-the-programmer/vscode-devcontainers-herdr)<br><sub>scott-the-programmer</sub> | devコンテナ内で動くエージェント向けのHerdrリレー | `container` `devcontainer` `rust` | 11 | 🔄 2026-09-20 |
| [**herdr-push**](https://github.com/dcolinmorgan/herdr-push)<br><sub>dcolinmorgan</sub> | herdrプラグイン：依存なしでイベントをherdr-remoteにpushし、モバイルからの監視とワンタップ承認を可能にする | `shell` | 10 | 2026-07-09 |
| [**herdr-office**](https://github.com/michaellandi/herdr-office)<br><sub>michaellandi</sub> | エージェントをオープンオフィスにいる人物として描く Herdr プラグインです。承認が必要なときには手を挙げます。 | `javascript` | 9 | 🔄 2026-09-24 |
| [**herdr-call**](https://github.com/eliasstravik/herdr-call)<br><sub>eliasstravik</sub> | Herdr向けの音声操作 | `elevenlabs` `tailscale` `voice` `typescript` | 8 | 2026-08-07 |
| [**paddock**](https://github.com/lntvan166/paddock)<br><sub>lntvan166</sub> | herdr向けのモバイルファーストなダッシュボード——unixソケットを読み取る。設定不要でスマホ上で動く | `agent-orchestration` `coding-agents` `herdr-mobile` `paddock` `pwa` | 8 | 2026-09-03 |
| [**herdr-remote-panes**](https://github.com/Poor-Plebs/herdr-remote-panes)<br><sub>Poor-Plebs</sub> | 1つのHerdrから他のマシンで作業する——メニューからマシンを選ぶと、そのマシンのターミナルが得られる。実験的な双方向ミラーリングもオプションで利用可能 | `golang` `ssh` `terminal` `go` | 7 | 🔄 2026-09-11 |
| [**herdr-mobile**](https://github.com/bsorescu/herdr-mobile)<br><sub>bsorescu</sub> | SSH経由でHerdrのコーディングエージェントを操作できる、スマホ向けTUI | `mobile` `ssh` `textual` `tui` `python` | 6 | 2026-08-25 |
| [**merino**](https://github.com/LoneExile/merino)<br><sub>LoneExile</sub> | Merino🐑——Herdrエージェント向けのリモートトンネルダッシュボード | `go` `macos` `menubar` `react` `wails` | 6 | 🔄 2026-09-21 |
| [**muqun-gateway**](https://github.com/osuki-dev/muqun-gateway)<br><sub>osuki-dev</sub> | Muqunが、あなた自身のコンピュータ上のターミナルにアクセスできるようにするプログラム。あなたのマシン上で動作し、tmuxまたはHerdrと通信し、あなたのスマホに直接応答する——アカウントも、間に入る当方のサーバーも存在しない | `rust` | 6 | 🔄 2026-09-25 |
| [**herdr-web**](https://github.com/eyalev/herdr-web)<br><sub>eyalev</sub> | herdrのエージェントマルチプレクサ向けの、モバイルファーストなWeb UI——スマホからコーディングエージェントを操作できる | `claude-code` `mobile` `pwa` `terminal` `javascript` | 5 | 2026-07-29 |
| [**herdr-go**](https://github.com/herdr-go/herdr-go)<br><sub>herdr-go</sub> | どこからでもherdrのコーディングエージェントを操作できる——プライベートかつP2P、EasyTierによるセキュリティ付き | `dart` | 5 | 2026-09-08 |
| [**herdr-tether**](https://github.com/moneycaringcoder/herdr-tether)<br><sub>moneycaringcoder</sub> | Herdrのビューを閉じた後も、ローカル・リモートのターミナル処理を実行し続けさせる | `remote-development` `rust` `ssh` `terminal` `tmux` | 5 | 2026-09-01 |
| [**herdweb**](https://github.com/zlxlabs/herdweb)<br><sub>zlxlabs</sub> | スマホからコーディングエージェントを監視・操作できます。音声入力、画像の貼り付け、Webhook 通知、複数デバイス・サーバー対応。 | `typescript` | 5 | 🔄 2026-09-22 |
| [**herdr-aws-ssm**](https://github.com/maayanyosef/herdr-aws-ssm)<br><sub>maayanyosef</sub> | EC2インスタンスを選択し、herdrの--remoteセッションでAWS SSM経由接続する——踏み台サーバーやパブリックIPは不要 | `aws-ssm` `terminal` `shell` | 4 | 2026-07-01 |
| [**herdr-portfwd**](https://github.com/miko-misa/herdr-portfwd)<br><sub>miko-misa</sub> | リモートマシン上のコーディングエージェント向けの自動SSHポートフォワーディング——エージェントが出力したlocalhost URLをCtrl+クリックすると、同じポートで手元のマシンにページが開く。Herdrプラグイン | `ai-agents` `claude-code` `cli` `coding-agents` `developer-tools` | 4 | 🔄 2026-09-20 |
| [**herdr-whistle**](https://github.com/amurru/herdr-whistle)<br><sub>amurru</sub> | リモートでのエージェント管理を行うHerdrプラグイン | `golang` `telegrambot` `go` | 3 | 2026-08-06 |
| [**herdrchat**](https://github.com/cobanov/herdrchat)<br><sub>cobanov</sub> | Control your herdr coding agents from your phone. On the App Store for iPhone and iPad. | `app-store` `herdr-client` `herdr-integration` `herdr-mobile` `ios` | 3 | 🔄 2026-09-23 |
| [**herdr-telegram-gate**](https://github.com/hkdom/herdr-telegram-gate)<br><sub>hkdom</sub> | herdrのAIエージェント群向けの、Telegram承認インボックス＋リスク階層別の自動承認——ブロックされたエージェントは承認/拒否ボタン付きのTelegramカードとして表示される（依存ライブラリなしのNode.js） | `approval-gate` `telegram` `javascript` | 3 | 2026-08-06 |
| [**herdr-phone**](https://github.com/matheus3301/herdr-phone)<br><sub>matheus3301</sub> | Cloudflare TunnelとAccessを使った、Herdr向けのモバイルリモートコンソール | `cloudflare-tunnel` `coding-agents` `developer-tools` `golang` `mobile` | 3 | 2026-09-04 |
| [**herdr-farm**](https://github.com/mejiasd3v/herdr-farm)<br><sub>mejiasd3v</sub> | Herdrプラグイン：ワークスペースとエージェントを家畜として可視化する3D農場（three.js製Webアプリ） | `threejs` `javascript` | 3 | 2026-07-28 |
| [**herdr-devup**](https://github.com/alon-z/herdr-devup)<br><sub>alon-z</sub> | Herdrプラグイン：.herdr/dev.tomlからプロジェクトごとの開発用レイアウトを構築し、トンネルURLを環境変数に同期する | `typescript` | 2 | 2026-06-22 |
| [**herdr-topbar**](https://github.com/bigbug16/herdr-topbar)<br><sub>bigbug16</sub> | herdr向けのmacOSメニューバーアイコン——セッションに戻る、プロジェクトを開く、どのエージェントが入力待ちかを確認できる | `macos` `menubar` `swift` | 2 | 2026-08-24 |
| [**🆕 herdr-web-ui**](https://github.com/devswha/herdr-web-ui)<br><sub>devswha</sub> | herdr in the browser: your live herdr workspaces, tabs and panes in a web UI / PWA, bridged over herdr's socket API | `bun` `pwa` `react` `terminal` `xterm` | 2 | 🔄 2026-09-25 |
| [**herdr-remote**](https://github.com/dibin666/herdr-remote)<br><sub>dibin666</sub> | ブラウザから Herdr のターミナルワークスペースへリモートアクセスできます。 | `claude-code` `codex` `pi` `vibe-coding` `typescript` | 2 | 🔄 2026-09-25 |
| [**herdr-remotedownloder**](https://github.com/kosuketut/herdr-remotedownloder)<br><sub>kosuketut</sub> | リモートのHerdrペインから、接続元のMacへファイルをダウンロードする | `rust` | 2 | 2026-09-10 |
| [**herdr-mobile-pro**](https://github.com/spad-0x/herdr-mobile-pro)<br><sub>spad-0x</sub> | Cyber-Dark デザインの、高性能でモバイルファーストな PWA ダッシュボード。スマホから直接 Herdr と自律型 AI エージェントをオーケストレーションできます。セキュアな HTTPS、音声入力、画像アップロード、ターミナル出力をチャット中心のインターフェースへリアルタイムに意味解析する機能を備えます。 | `javascript` | 2 | 🔄 2026-09-12 |
| [**herdr-mobile-app**](https://github.com/teasec4/herdr-mobile-app)<br><sub>teasec4</sub> | ネイティブのコンパニオンアプリと軽量な Go 製リレーです。エージェントのターミナル出力をスマホへライブ配信し、ステータス確認やプロンプト送信ができます——LAN・Tailscale・Funnel 経由に対応。 | `ai` `devtools` `flutter` `herdr-integration` `herdr-mobile` | 2 | 2026-09-05 |
| [**herdr-web-tui**](https://github.com/tigorlazuardi/herdr-web-tui)<br><sub>tigorlazuardi</sub> | デーモン主体のHerdr向けブラウザ/PWAフロントエンド——オプションのプラグインランチャー付き | `go` | 2 | 🔄 2026-09-25 |
| [**herdr-hub**](https://github.com/alex-devdone/herdr-hub)<br><sub>alex-devdone</sub> | リモートアタッチしたペインで構成されるherdrセッションを、持ち運び可能なマニフェストとして記述し、どのマシンでも再構築できる | `python` | 1 | 2026-08-23 |
| [**shep**](https://github.com/ArtMoreno/shep)<br><sub>ArtMoreno</sub> | スマホで Herdr のターミナルを使えます。デスクトップ側のセットアップ、プライベートなペアリング、テーマ、QuotaDeck に対応。 | `pwa` `terminal` `javascript` | 1 | 2026-09-09 |
| [**🆕 sightr**](https://github.com/bartholomewtj/sightr)<br><sub>bartholomewtj</sub> | Sightr — phone web UI for a Herdr agent herd, over Tailscale | `typescript` | 1 | 🔄 2026-09-21 |
| [**herdr-mobile**](https://github.com/carsol/herdr-mobile)<br><sub>carsol</sub> | Herdr 用のモバイルファースト Web UI。スマホからエージェントを確認し、ペインにアタッチして、Claude Code や Codex とチャットできます。 | `claude-code` `codex` `mobile` `pwa` `python` | 1 | 🔄 2026-09-15 |
| [**setnet**](https://github.com/chano-gpt/setnet)<br><sub>chano-gpt</sub> | スマホから複数harnessのコーディングエージェントを統率する——Herdrプラグイン | `typescript` | 1 | 2026-08-29 |
| [**herdr-tunnel**](https://github.com/ivorpad/herdr-tunnel)<br><sub>ivorpad</sub> | herdrプラグイン：ローカルのポートを公開インターネットに公開し、URLをコピーし、また取り下げる | `tui` `python` | 1 | 2026-08-27 |
| [**🆕 herdr-reach**](https://github.com/Luisalt20/herdr-reach)<br><sub>Luisalt20</sub> | Read-only network doctor for Herdr remote machines: measures what your network actually allows and recommends a transport with evidence. No writes, no third-pa… | `cli` `cloudflare-tunnel` `connectivity` `egress` `go` | 1 | 🔄 2026-09-21 |
| [**🆕 terminal-browser-relay**](https://github.com/maynewong/terminal-browser-relay)<br><sub>maynewong</sub> | terminal-browser on herdr remote without the slideshow | `javascript` | 1 | 🔄 2026-09-25 |
| [**herdview**](https://github.com/Orchard-Robotics/herdview)<br><sub>Orchard-Robotics</sub> | 自分の「herd」をWebから見る | `html` | 1 | 🔄 2026-09-24 |
| [**🆕 shahi**](https://github.com/iYassr/shahi)<br><sub>iYassr</sub> | Your herdr agents as a chat on your phone. Install the plugin, scan a QR, continue Claude Code, Codex and Cursor work anywhere. End-to-end encrypted. | `ai-agents` `claude-code` `codex` `expo` `react-native` | 0 | 🔄 2026-09-25 |
| [**herdr-agents-bridge**](https://github.com/maedana/herdr-agents-bridge)<br><sub>maedana</sub> | ローカルのモバイル向けWeb UI経由で、スマホからコーディングエージェントを監視・操作する——QRコードをスキャンして接続 | `rust` | 0 | 2026-07-22 |
| [**herdr-osx-menubar**](https://github.com/marcelpanse/herdr-osx-menubar)<br><sub>marcelpanse</sub> | herdr 用の macOS メニューバーアイコンです。セッションへすぐ戻ったり、プロジェクトを開いたり、どのエージェントが入力を待っているかを確認したりできます。 | `swift` | 0 | 2026-09-08 |
| [**🆕 hither**](https://github.com/T0mSIlver/hither)<br><sub>T0mSIlver</sub> | リモートマシン上の herdr ペインでキーの組み合わせを押すと、Mac 側で Zed がそのディレクトリを開きます。 | `shell` | 0 | 🔄 2026-09-18 |
| [**herdr-codex-confirm**](https://github.com/utahta/herdr-codex-confirm)<br><sub>utahta</sub> | 選択した Codex のシェルコマンドを承認・拒否できる Herdr プラグインです。拒否時にはフィードバックを添えることもできます。 | `go` | 0 | 🔄 2026-09-12 |

<details><summary>この目的にも関係するもの</summary>

- [powerfooI/roamgate](https://github.com/powerfooI/roamgate) — A Herdr client for any screen. Control terminals, monitor coding agents, and review files and diffs from desk…
- [huketo/herdr-hitl](https://github.com/huketo/herdr-hitl) — Herdr のコーディングエージェントを、人の判断待ちで一時停止させ、Telegram や Discord 経由でスマホに通知します。

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-agents"></a>

## エージェント統括・並列実行

> 複数の AI エージェントをまとめて起動・分担・管理したい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**agentbox**](https://github.com/madarco/agentbox)<br><sub>madarco</sub> | コマンド一発で、サンドボックス化された複数のVM上にエージェントを並列実行（PCでもクラウドでも） | `claude` `claude-code` `cli` `cmux` `codex` | 489 | 🔄 2026-09-24 |
| [**🆕 herdr-projects**](https://github.com/eliasstravik/herdr-projects)<br><sub>eliasstravik</sub> | A coordinator conversation, parallel worker threads, shared memory and an overview of what needs you. A Herdr plugin. | `rust` | 444 | 🔄 2026-09-25 |
| [**pi-workflows**](https://github.com/osolmaz/pi-workflows)<br><sub>osolmaz</sub> | piコーディングエージェント向けの、ワークフローエンジン・JSON制御フローツール・ライブターミナルビューア | `typescript` | 311 | 🔄 2026-09-21 |
| [**pi-extensible-workflows**](https://github.com/vekexasia/pi-extensible-workflows)<br><sub>vekexasia</sub> | Pi向けの、決定論的なマルチエージェントワークフローオーケストレーション | `pi` `workflow` `workflows` `typescript` | 233 | 🔄 2026-09-23 |
| [**herdr-board**](https://github.com/nelsonPires5/herdr-board)<br><sub>nelsonPires5</sub> | herdr向けのカンバンボード——カードはそのままプロンプトになり、見えているペイン上のAIエージェントに割り振られる | `board` `kanban` `kanban-board` `tui` `rust` | 153 | 🔄 2026-09-23 |
| [**herdr-dagr**](https://github.com/aemrebarut/herdr-dagr)<br><sub>aemrebarut</sub> | エージェント群をライブなDAGとして表示——試行・レビューゲート・エビデンスを備えたオーケストレーショングラフを、herdrのスプリットペインに表示する | `agents` `dag` `multi-agent` `orchestration` `rust` | 87 | 2026-08-23 |
| [**agent-router**](https://github.com/nidhi-singh02/agent-router)<br><sub>nidhi-singh02</sub> | CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr | `agents` `ai` `claude-code` `cli` `codex` | 78 | 🔄 2026-09-25 |
| [**herdr-file-annotator**](https://github.com/JonasBaeumer/herdr-file-annotator)<br><sub>JonasBaeumer</sub> | 実際のコードベースとの接点を失わずに、エージェントによる開発を最大限活用するためのherdrプラグイン | `rust` | 61 | 🔄 2026-09-24 |
| [**🆕 proqi**](https://github.com/oborchers/proqi)<br><sub>oborchers</sub> | A terminal-native prompt composer for power users running multiple coding agents. | `ai-agents` `cli` `coding-agents` `developer-tools` `local-first` | 40 | 🔄 2026-09-25 |
| [**agentbox-herdr-plugin**](https://github.com/madarco/agentbox-herdr-plugin)<br><sub>madarco</sub> | コマンド一発で、サンドボックス化された複数のVM上にエージェントを並列実行（PCでもクラウドでも） | `claude-code` `codex-cli` `opencode` `sandbox` `shell` | 32 | 2026-06-24 |
| [**🆕 entwurf**](https://github.com/junghan0611/entwurf)<br><sub>junghan0611</sub> | Herdr and tmux sibling AI sessions: pi, Claude Code, Codex, Copilot, OMP and Antigravity can message and spawn each other while keeping their own auth, tools a… | `acp` `agent-client-protocol` `ai-agent` `claude-code` `codex` | 28 | 🔄 2026-09-23 |
| [**herdmates**](https://github.com/caioniehues/herdmates)<br><sub>caioniehues</sub> | herdrネイティブのClaude Codeエージェントチーム——teammuxシム、ミッションコントロールボード、フォーカスペイン | `agent-teams` `claude-code` `rust` `tui` | 24 | 2026-08-21 |
| [**🆕 termaxa**](https://github.com/termaxa/termaxa)<br><sub>termaxa</sub> | A cooperative gate for the shell commands AI agents run. Previews, backups, policy, audit. Claude Code + Cursor. A windshield, not a sandbox. | `agent-safety` `ai-agents` `claude-code` `cli` `developer-tools` | 22 | 🔄 2026-09-24 |
| [**pi-herd**](https://github.com/ribbons-digital/pi-herd)<br><sub>ribbons-digital</sub> | Herdrのペインとgit worktreeを使って、Piのセッションを可視化しながらオーケストレーションする | `typescript` | 21 | 2026-07-06 |
| [**herdr-browser**](https://github.com/StructuPath/herdr-browser)<br><sub>StructuPath</sub> | Herdr向けの操作可能なエージェントブラウザペイン——ライブストリーミング、実際の操作、アダプティブレンダリング、コンソール/ページエラー表示、録画、localhostルーティングに対応 | `terminal` `javascript` | 20 | 🔄 2026-09-16 |
| [**herdr-world**](https://github.com/IvoryHeart/herdr-world)<br><sub>IvoryHeart</sub> | Herdr World——Herdr向けのマルチサーフェスなWeb体験 | `multi-agent` `observability` `pixel-art` `react` `rust` | 17 | 🔄 2026-09-25 |
| [**herdr-agent-handoff**](https://github.com/sanirudh17/herdr-agent-handoff)<br><sub>sanirudh17</sub> | 進行中のエージェントセッションを、別のインストール済みコーディングエージェントの新規セッションに引き渡すHerdrプラグイン。セッション全体をプロンプト内にそのまま渡すため、要約や省略された履歴、追加の指示を書く必要がない | `agent-handoff` `claude-code` `codex` `coding-agents` `developer-tools` | 17 | 🔄 2026-09-14 |
| [**PromptPilot**](https://github.com/ivanarama/PromptPilot)<br><sub>ivanarama</sub> | Claude Codeやその他のAI CLI向けのバックグラウンドタスクキュー——Web UIとTelegramボット付き | `ai-agents` `claude-code` `telegram-bot` `python` | 16 | 🔄 2026-09-23 |
| [**herdr-vercel-sandbox-plugin**](https://github.com/vercel-labs/herdr-vercel-sandbox-plugin)<br><sub>vercel-labs</sub> | Herdrから、ターミナルベースのコーディングエージェントを隔離されたVercel Sandbox上で実行する | `javascript` | 13 | 2026-08-09 |
| [**herdr-social-glass**](https://github.com/ythx-101/herdr-social-glass)<br><sub>ythx-101</sub> | macOS版Herdr向けの、スクリーンショット映えするSocial Glassテーマ＆ワークフロープラグイン | `macos` `multi-agent` `terminal-theme` `shell` | 12 | 2026-08-21 |
| [**vibetty**](https://github.com/second-state/vibetty)<br><sub>second-state</sub> | MQTT経由でAIエージェントのターミナルをスマートデバイス（vibekeys、vibewatchなど）にライブ共有する。Herdrプラグインとしても利用可能 | `claude-code` `codex` `vibecoding` `rust` | 11 | 2026-08-17 |
| [**deevs-pi-kit**](https://github.com/DeevsDeevs/deevs-pi-kit)<br><sub>DeevsDeevs</sub> | Deevs のエンジニアを 10 倍優秀にする、完璧な pi キットです。 | `agents` `pi` `pi-agent` `pi-extension` `pi-package` | 10 | 🔄 2026-09-20 |
| [**agys**](https://github.com/quaywin/agys)<br><sub>quaywin</sub> | 汚染ゼロのサンドボックスにより、Herdr上のAntigravity CLIに手間いらずのマルチプロファイル分離とリアルタイムなクォータ追跡を提供する | `ai-agents` `antigravity` `cli` `context-window` `developer-tools` | 10 | 🔄 2026-09-25 |
| [**herdr-catchup**](https://github.com/wilbeibi/herdr-catchup)<br><sub>wilbeibi</sub> | herdr向けのエージェント間コーディングセッション引き渡し：稼働中のペインから、Claude Code・Codex・Cursor・Cline・OpenCodeのセッションを要約・フォーク・他のエージェントへの引き渡しができる | `ai-agents` `claude-code` `codex` `coding-agents` `context-handoff` | 10 | 🔄 2026-09-20 |
| [**herdr-agent-messenger**](https://github.com/aashishd/herdr-agent-messenger)<br><sub>aashishd</sub> | 稼働中のHerdrペイン間で、AIエージェント同士が要点を絞った自己完結型のメッセージをやり取りできるようにする——1つのエージェントが、全コンテキストを共有せずに別のエージェントと作業を調整できる | `python` | 8 | 🔄 2026-09-23 |
| [**herdr-helpr**](https://github.com/sohanemon/herdr-helpr)<br><sub>sohanemon</sub> | プロンプトで操作する、herdr向けのワークスペース・ペイン管理 | `ai-agents` `bun` `cli` `developer-tools` `ink` | 8 | 2026-07-16 |
| [**herdr-swarm**](https://github.com/StructuPath/herdr-swarm)<br><sub>StructuPath</sub> | 1つのリポジトリで複数のコーディングエージェントを安全に並列実行：エージェントごとのworktree展開、変更のリアルタイム可視化、レビュー優先の成果回収をHerdr向けに提供 | `terminal` `javascript` | 8 | 🔄 2026-09-14 |
| [**shepherdr**](https://github.com/afogel/shepherdr)<br><sub>afogel</sub> | 委任したコーディングエージェントを、監視・再開・引き取りができる可視化されたherdrのペインに追い込むherdrプラグイン | `ai-agents` `claude-code` `codex` `cursor` `rust` | 7 | 2026-07-24 |
| [**herdr-scuttlebutt**](https://github.com/andybarilla/herdr-scuttlebutt)<br><sub>andybarilla</sub> | herdrセッション内のエージェントに、共有チャットルームを提供するherdrプラグイン | `rust` | 6 | 🔄 2026-09-22 |
| [**herdr-orchestrate**](https://github.com/darjss/herdr-orchestrate)<br><sub>darjss</sub> | Pi向けのネイティブなオーケストレーション機能を、可視化されたHerdrのワーカーセッションで提供——実行状況ボード、永続的なプロンプト/レポート/状態、独立したgit worktree、明示的なモデルルーティングに対応 | `pi-package` `typescript` | 6 | 2026-07-13 |
| [**herdr-devcontainer**](https://github.com/gambtho/herdr-devcontainer)<br><sub>gambtho</sub> | 公式のDev Containers CLI経由で、リポジトリのDev Container内にシェルやコーディングエージェントを開くHerdrプラグイン | `coding-agents` `containers` `devcontainers` `developer-tools` `development-environment` | 6 | 2026-08-13 |
| [**pier**](https://github.com/July24/pier)<br><sub>July24</sub> | Piはコーディングエージェントのキャリア、Herdrはターミナルワークスペースマネージャー。pierは、piがあえて省いている2つの機能——todoリストのループと対話的なサブエージェント——を追加し、herdrのペイン/タブ層をその見た目と操作の土台として与える | `pi-coding-agent` `typescript` | 6 | 🔄 2026-09-24 |
| [**chatter**](https://github.com/marcvermeeren/chatter)<br><sub>marcvermeeren</sub> | Chatterは、harnessをまたいだエージェント協働の実験的プロジェクト——Herdr上で同じGitリポジトリを扱うエージェント同士の、共有グループチャット＆コンテキストレイヤーを提供する | `agent-collaboration` `agentic-ai` `agentic-workflow` `ai-agents` `group-chat` | 6 | 2026-08-18 |
| [**herdr-triage**](https://github.com/natori-hrj/herdr-triage)<br><sub>natori-hrj</sub> | herdr向けの注意度トリアージ——あなたを最も必要としているエージェントを上位に並べる。長時間ブロックされたエージェントほど上に来る | `ai-agents` `triage` `rust` | 6 | 2026-07-23 |
| [**herdr-space-scoped-agents**](https://github.com/ShankyJS/herdr-space-scoped-agents)<br><sub>ShankyJS</sub> | エージェントパネルを、フォーカス中のスペースに限定して表示するherdrプラグイン | `coding-agents` `terminal` `go` | 6 | 2026-07-23 |
| [**herdr-insight**](https://github.com/0x5c0f/herdr-insight)<br><sub>0x5c0f</sub> | エージェントの状態タイムラインパネル | `rust` | 5 | 2026-06-23 |
| [**herdr-pane-topic-sync**](https://github.com/danbuhler/herdr-pane-topic-sync)<br><sub>danbuhler</sub> | herdrプラグイン：ペインとタブの名前を「1」「2」「3」ではなく、各エージェント（Claude Code、Codexなど）のリアルタイムのトピックから自動で付ける | `ai-agents` `claude-code` `terminal` `tmux-alternative` `javascript` | 5 | 2026-09-02 |
| [**🆕 AgentRadio**](https://github.com/detailles/AgentRadio)<br><sub>detailles</sub> | Local message bus for AI coding agents running in Herdr panes — join, DM, presence, offline delivery | `agent-orchestration` `multi-agent` `radio` `python` | 5 | 🔄 2026-09-25 |
| [**herdr-gamepad**](https://github.com/htlin222/herdr-gamepad)<br><sub>htlin222</sub> | ゲームコントローラーでHerdrを操作する。ソファに座ったままAIエージェントを見回り、ペインを分割し、ワークスペースを切り替えられる——どんなゲームパッドでも60秒で自分好みに割り当て可能 | `ai-agents` `gamepad` `macos` `swift` `terminal-multiplexer` | 5 | 2026-09-09 |
| [**herdr-fleet**](https://github.com/Northern-Lighthouse/herdr-fleet)<br><sub>Northern-Lighthouse</sub> | Tailscale経由でherdrマシンのフリートを管理——ダッシュボードプラグイン、自動検出、キャパシティを考慮したエージェント割り当て、ディスクレスなワークスペースに対応 | `ai-agents` `tailscale` `python` | 5 | 2026-08-14 |
| [**herdr-worker-orchestrator**](https://github.com/anhnd3005-infinity/herdr-worker-orchestrator)<br><sub>anhnd3005-infinity</sub> | Herdr管理下のペイン経由で、CLIエージェントワーカー（agy・codexなど）にタスクを割り振る——状態を持つタスク追跡、worktreeによる隔離、差分ベースのレビューに対応。Claude CodeとHerdrの両対応プラグイン | `html` | 4 | 2026-08-25 |
| [**herdr-openclaw**](https://github.com/gejiliang/herdr-openclaw)<br><sub>gejiliang</sub> | herdrプラグイン：OpenClawのTUIペインを、herdrの正式なエージェントとして管理する | `openclaw` `terminal` `javascript` | 4 | 2026-08-13 |
| [**herdr-espresso**](https://github.com/Hanyang-Li/herdr-espresso)<br><sub>Hanyang-Li</sub> | エージェントが動作中はMacBookを、蓋を閉じても眠らせない | `rust` | 4 | 2026-07-25 |
| [**herdr-a2a**](https://github.com/IsaiasZc/herdr-a2a)<br><sub>IsaiasZc</sub> | A2A経由の、信頼性の高いHerdr向けエージェント間委任レイヤー | `typescript` | 4 | 2026-08-27 |
| [**herdr-walkietalkie**](https://github.com/jeffory/herdr-walkietalkie)<br><sub>jeffory</sub> | herdrプラグイン：トークン効率の良いエージェント間委任（wt）——オーケストレーター役のエージェントが、Claude/OpenCode/Antigravityのワーカーをタブやworktreeに立ち上げる | `shell` | 4 | 2026-08-12 |
| [**herdr-prompt-library**](https://github.com/jwkicklighter/herdr-prompt-library)<br><sub>jwkicklighter</sub> | ローカルまたはグローバルな再利用可能なMarkdownプロンプトを閲覧・管理し、フォーカス中のペインに挿入できるHerdrプラグイン | `go` `golang` `prompting` `snippets` `tui` | 4 | 2026-09-01 |
| [**herdr-agent-profiles**](https://github.com/mikeyobrien/herdr-agent-profiles)<br><sub>mikeyobrien</sub> | Herdr向けの、データ駆動のCLIハーネスとモデルプロファイル | `ai-agents` `terminal` `python` | 4 | 2026-08-10 |
| [**🆕 pet-town**](https://github.com/abhishek944/pet-town)<br><sub>abhishek944</sub> | A transparent desktop village for live Herdr agents | `rust` | 3 | 🔄 2026-09-21 |
| [**herdr-blaxel-sandbox-plugin**](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin)<br><sub>blaxel-ai</sub> | Herdrから、永続化されたBlaxel Sandbox上でコーディングエージェントを実行する | `blaxel` `claude-code` `codex` `coding-agents` `opencode` | 3 | 🔄 2026-09-23 |
| [**herdr-theos-settler**](https://github.com/calebcauthon/herdr-theos-settler)<br><sub>calebcauthon</sub> | 完了したHerdrのエージェントタブやワークスペースを、作業中のものより下に沈めて視界から外す。Theoのアイデア | `rust` | 3 | 2026-07-23 |
| [**herdr-loop**](https://github.com/cyperx84/herdr-loop)<br><sub>cyperx84</sub> | herdr向けの宣言的でイベント駆動なループ＋グラフオーケストレーション——Claude Code・Codex・opencode・piをまとめて動かし、作業が収束するまで実行する | `ai-agents` `golang` `orchestration` `go` | 3 | 2026-09-10 |
| [**herdr-sbx-plugin**](https://github.com/dirien/herdr-sbx-plugin)<br><sub>dirien</sub> | コーディングエージェントを Docker Sandboxes（sbx）内で実行する Herdr プラグインです。エージェントごとに 1 つの microVM を使います。 | `coding-agents` `docker-sandboxes` `javascript` | 3 | 🔄 2026-09-13 |
| [**herdr-cursor**](https://github.com/gabriel-laet/herdr-cursor)<br><sub>gabriel-laet</sub> | Cursorのクラウドエージェントを、herdrの正式なペインとして扱う | `typescript` | 3 | 2026-09-08 |
| [**herdr-agent-restart**](https://github.com/hmu332233/herdr-agent-restart)<br><sub>hmu332233</sub> | 表示が崩れたときに、ショートカット一つで Herdr のエージェントを再起動し、同じ会話を続けられます。 | `agent-restart` `javascript` | 3 | 2026-09-08 |
| [**herdr-newtab-plus**](https://github.com/jeffarese/herdr-newtab-plus)<br><sub>jeffarese</sub> | どのフォルダとどのエージェントかを聞いてくるHerdrの新規タブ：実在するパスを補完し、作業場所を記憶し、代わりにエージェントを起動してくれる | `python` | 3 | 2026-07-26 |
| [**herdr-orchestrator**](https://github.com/kylezk777/herdr-orchestrator)<br><sub>kylezk777</sub> | Herdr-orchは、Herdr上で動作するファイルベースのエージェントオーケストレーションツール | `agent-orchestration` `orchestrator` `rust` | 3 | 2026-07-26 |
| [**🆕 kubeflock**](https://github.com/LoriKarikari/kubeflock)<br><sub>LoriKarikari</sub> | Herdr 内で Kubernetes のサンドボックスを作成・接続できます。 | `agent-sandbox` `gvisor` `kubernetes` `sandbox` `go` | 3 | 🔄 2026-09-11 |
| [**muster**](https://github.com/ofelcan164/muster)<br><sub>ofelcan164</sub> | あらゆるリポジトリのあらゆるエージェントを、1 画面にまとめます。herdr プラグインです。 | `go` | 3 | 🔄 2026-09-25 |
| [**🆕 herdr-space-topic**](https://github.com/panuhorsmalahti/herdr-space-topic)<br><sub>panuhorsmalahti</sub> | herdr plugin: name each Space after the work happening inside it — the live topic of its primary agent pane. | `ai-agents` `terminal-multiplexer` `javascript` | 3 | 🔄 2026-09-21 |
| [**herdr-approve-all**](https://github.com/RenKoya1/herdr-approve-all)<br><sub>RenKoya1</sub> | herdrプラグイン：ブロックされている全エージェントを一括承認（1キーで、保留中の許可プロンプトすべてに応答） | `shell` | 3 | 2026-08-16 |
| [**herdr-agents-history**](https://github.com/speardragon/herdr-agents-history)<br><sub>speardragon</sub> | AIコーディングエージェントが実際に何をしているかを見る——すべてのエージェント（Claude CodeとCodex）のツール呼び出しをリアルタイムに流し続ける、キーボード操作のherdr TUI | `ai-agents` `claude-code` `codex` `tui` `typescript` | 3 | 2026-07-19 |
| [**herdr-conductor**](https://github.com/StructuPath/herdr-conductor)<br><sub>StructuPath</sub> | 機能開発チームを、見えるHerdrのエージェントペインとしてオーケストレーションする——Conductorプラグイン | `orchestration` `javascript` | 3 | 🔄 2026-09-14 |
| [**herdr-agent-office**](https://github.com/suisya-systems/herdr-agent-office)<br><sub>suisya-systems</sub> | エージェント群をピクセルアートのオフィスとして表示するherdrプラグイン。誰が作業中で、誰が詰まっているかが分かり、そこにジャンプできる | `python` | 3 | 2026-07-25 |
| [**herdr-upstash-box**](https://github.com/upstash/herdr-upstash-box)<br><sub>upstash</sub> | Herdr プラグイン：今見ている worktree から、Upstash Box 上でコーディングエージェントを実行します。 | `claude-code` `coding-agents` `sandbox` `upstash` `typescript` | 3 | 🔄 2026-09-10 |
| [**herdr-cadence**](https://github.com/zhenyufu/herdr-cadence)<br><sub>zhenyufu</sub> | 1人のLeadと複数のエージェント群からなる、軽量なエージェントオーケストレーター | `rust` | 3 | 2026-09-07 |
| [**herdr-birdseye**](https://github.com/calebcauthon/herdr-birdseye)<br><sub>calebcauthon</sub> | herdr内のエージェントを鳥瞰図で見る | `rust` | 2 | 2026-07-24 |
| [**🆕 herdr-chat**](https://github.com/eliasstravik/herdr-chat)<br><sub>eliasstravik</sub> | Herdr内で動くエージェント向けの、構造化されたライブチャットビュー | `typescript` | 2 | 2026-08-24 |
| [**🆕 herdr-plugin-odysseus**](https://github.com/jpolec/herdr-plugin-odysseus)<br><sub>jpolec</sub> | Governed multi-agent workflows for Herdr: tasks → agents in Herdr panes → checks, retries, review, policy, approvals, audit, draft PR | `ai-agents` `rust` | 2 | 🔄 2026-09-25 |
| [**herdr-shame-report**](https://github.com/JYasha11/herdr-shame-report)<br><sub>JYasha11</sub> | AIエージェントをどれだけ待たせたかを、ずっと記録し続ける台帳。羊は忘れない | `javascript` | 2 | 2026-07-10 |
| [**herdr-link**](https://github.com/LZHcode1986/herdr-link)<br><sub>LZHcode1986</sub> | Herdrのセッション向けに、より高速でトークン効率が良く推論不要なエージェント間相互運用性を提供する。重量級のskillを、ピア発見・メッセージング・ペインのライフサイクルを扱う統一されたコントラクトで置き換える | `typescript` | 2 | 🔄 2026-09-21 |
| [**herdr-agents-status**](https://github.com/maedana/herdr-agents-status)<br><sub>maedana</sub> | Herdrのエージェントの状態を表示する、常に最前面の透明オーバーレイ——claudeyeの精神的後継で、tmuxではなくHerdr向けに作られた | `rust` | 2 | 2026-08-15 |
| [**herdr-redact**](https://github.com/moneycaringcoder/herdr-redact)<br><sub>moneycaringcoder</sub> | エージェントのペインが認証情報を出力したときに警告する——スクリーンショットを撮ったり、配信したり、チャットウィンドウに貼り付けたりする前に気づける | `rust` `secret-detection` `security` `terminal` | 2 | 2026-09-01 |
| [**🆕 herdr-pinpoint**](https://github.com/navishachiku/herdr-pinpoint)<br><sub>navishachiku</sub> | Pick a Herdr space, tab, or pane and type its id into the agent you were talking to | `javascript` | 2 | 🔄 2026-09-22 |
| [**herdr-code-board**](https://github.com/sazardev/herdr-code-board)<br><sub>sazardev</sub> | Herdr内の、エージェント向けプロンプトのカンバンキュー——カードが実際のエージェントをペイン・worktree・ワークスペースに配置し、カード同士を連鎖させるルールも設定できる | `ai-agents` `kanban` `rust` `tui` | 2 | 2026-08-30 |
| [**herdr-achievements**](https://github.com/SerHappy/herdr-achievements)<br><sub>SerHappy</sub> | あなたのHerdr AIエージェントの群れに、実績とささやかなお祝いを追加する | `achievements` `ai-agents` `developer-tools` `gamification` `go` | 2 | 2026-07-30 |
| [**herdr-wakeup**](https://github.com/usrivastava92/herdr-wakeup)<br><sub>usrivastava92</sub> | Herdrが管理するエージェントが作業中の間、macOSまたはLinuxをスリープさせないHerdrプラグイン | `power-management` `sleep-prevention` `wakeup` `rust` | 2 | 2026-07-17 |
| [**herdr-auto-yes-sir**](https://github.com/xlinx/herdr-auto-yes-sir)<br><sub>xlinx</sub> | herdr-auto-yes-sir——エージェントが承認を求めてきたときに、ブロックされずに実行を続けられるようにする。codexのような挙動 | `javascript` | 2 | 2026-08-20 |
| [**herdr-agent-timer**](https://github.com/Yemeni/herdr-agent-timer)<br><sub>Yemeni</sub> | 各エージェントのステータスラベルと経過時間を交互に表示するHerdrプラグイン | `shell` | 2 | 2026-08-14 |
| [**herdr-pouch**](https://github.com/AltanS/herdr-pouch)<br><sub>AltanS</sub> | herdrプラグイン：エージェント向けのプロンプトを事前に貯めておき、準備ができたら挿入する | `ai-agents` `ai-coding` `ai-tools` `multiplexing` `typescript` | 1 | 2026-09-02 |
| [**herdr-pi-reloader**](https://github.com/anrunt/herdr-pi-reloader)<br><sub>anrunt</sub> | Herdrのオーバーレイ TUIから、アイドル状態のPiエージェントセッションをリロードまたは再起動する | `rust` | 1 | 2026-07-18 |
| [**🆕 herdr-pointr**](https://github.com/aristeoibarra/herdr-pointr)<br><sub>aristeoibarra</sub> | Point at a DOM element on a localhost page and it lands in the coding agent that owns that project, with its React component, selector and an optional screensh… | `coding-agent` `devtools` `react` `typescript` | 1 | 🔄 2026-09-25 |
| [**herdr-convo**](https://github.com/arvemy/herdr-convo)<br><sub>arvemy</sub> | 他のコーディングエージェントの会話を、正規化されたターン形式で読み取れます——Claude Code・Codex・OpenCode・Pi を横断して同じ形式で扱えます。 | `ai-agents` `claude-code` `cli` `codex` `coding-agents` | 1 | 🔄 2026-09-11 |
| [**herdr-quick-prompt**](https://github.com/astwys/herdr-quick-prompt)<br><sub>astwys</sub> | あらかじめ定義したプロンプトをエージェントのペインに送信するHerdrプラグイン | `shell` | 1 | 2026-08-24 |
| [**herdr-handoff**](https://github.com/devops-fj/herdr-handoff)<br><sub>devops-fj</sub> | Herdrのコーディングエージェント間で、ローカルの作業コンテキストをプレビューし安全に引き継ぐ | `ai-agents` `coding-agents` `go` | 1 | 2026-08-21 |
| [**herdr-docket**](https://github.com/DnzzL/herdr-docket)<br><sub>DnzzL</sub> | The software factory your Herdr fleet runs: a shared task queue worked by coding agents — Backlog.md, Basecamp or GitHub Projects. Assign a task, the daemon ru… | `agent-fleet` `ai-agents` `autonomous-agents` `software-factory` `task-queue` | 1 | 🔄 2026-09-21 |
| [**🆕 herdr-tasks**](https://github.com/Eslsamu/herdr-tasks)<br><sub>Eslsamu</sub> | Herdr 向けの、エージェントが所有するローカルタスクキューです。読み取り専用のライブブラウザビューも備えます。 | `ai-agents` `codex` `local-first` `python` `sqlite` | 1 | 2026-09-09 |
| [**herdr-state-icons**](https://github.com/flowreaction/herdr-state-icons)<br><sub>flowreaction</sub> | HerdR のスペースとエージェント向けの、アニメーション付きで色を変えられるライフサイクルアイコンです。 | `python` | 1 | 2026-09-10 |
| [**herdr-agent-team**](https://github.com/gdli6177/herdr-agent-team)<br><sub>gdli6177</sub> | Markdownでエージェントチームを定義できるHerdrプラグイン | `javascript` | 1 | 2026-08-16 |
| [**herdr-prompt-bucket**](https://github.com/GNURub/herdr-prompt-bucket)<br><sub>GNURub</sub> | Herdr上で動くコーディングエージェント向けの、永続化された順序付きプロンプトバケット | `claude-code` `codex` `coding-agents` `opencode` `typescript` | 1 | 2026-08-19 |
| [**herdr-agent-chat**](https://github.com/GODVvVZzz/herdr-agent-chat)<br><sub>GODVvVZzz</sub> | Herdr 上のターミナルエージェント同士で、チャットのように処理を委譲できます——ノンブロッキングなディスパッチと、確実な報告を保証します。 | `ai-agents` `claude-code` `python` | 1 | 🔄 2026-09-23 |
| [**LunaCrab**](https://github.com/GranamyrBR/LunaCrab)<br><sub>GranamyrBR</sub> | 別プロジェクト用に予約済み | `agents` `developer-tools` `multi-agent` `observability` `rust` | 1 | 2026-08-10 |
| [**herdr-plugin-done-timer**](https://github.com/hanjm93/herdr-plugin-done-timer)<br><sub>hanjm93</sub> | herdr のエージェントパネルに、各エージェントのトランスクリプトから読み取ったプロンプトキャッシュのカウントダウンを表示します。 | `ai-agents` `claude-code` `shell` | 1 | 🔄 2026-09-15 |
| [**agent-keep-awake**](https://github.com/happyeric77/agent-keep-awake)<br><sub>happyeric77</sub> | Herdrのエージェントが動作中は、macOSのスリープを防止する | `javascript` | 1 | 2026-08-12 |
| [**herdr-dispatch**](https://github.com/husniadil/herdr-dispatch)<br><sub>husniadil</sub> | herdr-tasksボード用のディスパッチャー——準備完了したタスクごとにワーカーエージェントのペインを立て、目標を伝え、ワーカーを追跡し、レビューで一旦止める。すべて1つのGoバイナリで実現 | `agent-orchestration` `ai-agents` `dispatcher` `mcp-server` `go` | 1 | 2026-08-31 |
| [**herdr-annotations**](https://github.com/IgorWarzocha/herdr-annotations)<br><sub>IgorWarzocha</sub> | ターミナルで選択した箇所に注釈を集め、Herdrのエージェントに投入する | `ai-agents` `annotations` `terminal` `javascript` | 1 | 2026-07-18 |
| [**herdr-agent-prompt**](https://github.com/jeffbking/herdr-agent-prompt)<br><sub>jeffbking</sub> | Herdr プラグイン：prefix+p でオーバーレイを開き、フォーカス中のコーディングエージェント（Claude Code・Codex・Antigravity・Pi）の元のプロンプトを確認できます。 | `claude-code` `codex` `python` | 1 | 2026-09-08 |
| [**herdr-plan-approve**](https://github.com/jerryfane/herdr-plan-approve)<br><sub>jerryfane</sub> | herdrでClaude Codeのplanモードダイアログを自動承認する——エージェントは計画を立て、キー入力なしでそのまま実行に移れる | `claude-code` `shell` | 1 | 2026-08-25 |
| [**corral**](https://github.com/jirathip-dev/corral)<br><sub>jirathip-dev</sub> | herdr のコーディングエージェント群を読み取り専用で監視できます。 | `agent-orchestration` `ai-agents` `coding-agents` `devtools` `fleet-management` | 1 | 🔄 2026-09-22 |
| [**herdr-watcher**](https://github.com/joshka0/herdr-watcher)<br><sub>joshka0</sub> | Herdrエージェント向けの、永続的な処理継続とデタッチされたワーカーコールバック | `rust` | 1 | 2026-08-02 |
| [**🆕 herdr-plugin**](https://github.com/juscribe/herdr-plugin)<br><sub>juscribe</sub> | File and transition Juscribe tickets from a Herdr pane, and see which ticket each agent is on. | `juscribe` `shell` | 1 | 🔄 2026-09-21 |
| [**herdr-attention-queue**](https://github.com/justmytwospence/herdr-attention-queue)<br><sub>justmytwospence</sub> | herdr プラグイン：あなたが対応するまで「完了」状態を保持し、対応が必要な順に並べた Agents パネルを提供します。 | `python` | 1 | 🔄 2026-09-14 |
| [**herdr-turn-coordinator**](https://github.com/KarthusLorin/herdr-turn-coordinator)<br><sub>KarthusLorin</sub> | モデル主導のステータスポーリングに頼らずに、対話的なHerdrエージェントTUIを維持する | `ai-agents` `python` | 1 | 🔄 2026-09-18 |
| [**herdr-island**](https://github.com/kay-ws/herdr-island)<br><sub>kay-ws</sub> | あなたの対応を待っているエージェントを見つける——各herdrエージェントが止まった理由を表示し、Agentsパネルを該当するものだけに絞り込む | `shell` | 1 | 2026-08-04 |
| [**🆕 shop-plugin**](https://github.com/kyrosle/shop-plugin)<br><sub>kyrosle</sub> | A visible multi-agent workstation for Pi + Herdr, with configurable Lead/Worker models, file-based task handoffs, and explicit review. Local alpha. | `coding-agent` `developer-tools` `human-in-the-loop` `multi-agent` `pi-coding-agent` | 1 | 🔄 2026-09-21 |
| [**herdr-math**](https://github.com/liambern/herdr-math)<br><sub>liambern</sub> | Herdr のターミナルペイン内で LaTeX の数式を表示します。ハーネスに依存しないエージェントスキルとしても使えます。 | `ai-agents` `latex` `mathjax` `terminal` `javascript` | 1 | 🔄 2026-09-14 |
| [**sheprd**](https://github.com/m-mohamed/sheprd)<br><sub>m-mohamed</sub> | Pi・Codex・Claude Code・OpenCodeを、可視化された1つの独立したHerdr「Flok」にまとめる | `agent-tools` `claude-code` `cli` `codex` `coding-agents` | 1 | 2026-08-25 |
| [**herdr-agents-preview**](https://github.com/maedana/herdr-agents-preview)<br><sub>maedana</sub> | Herdr向けのマルチエージェントターミナルプレビューダッシュボード：稼働中のすべてのエージェントを同時に表示し、選択中のエージェントが大部分の幅を占める | `rust` | 1 | 2026-08-14 |
| [**🆕 herdr-snooze**](https://github.com/mrolafsson/herdr-snooze)<br><sub>mrolafsson</sub> | Snooze agents in herdr's Agents panel for 15 minutes, an hour, a day or a week; they come back on their own. A herdr plugin. | `claude-code` `coding-agents` `python` `terminal` `tui` | 1 | 🔄 2026-09-24 |
| [**herdr-standup**](https://github.com/natori-hrj/herdr-standup)<br><sub>natori-hrj</sub> | herdr向けのエージェントスタンドアップ——各エージェントのリポジトリ全体で、コミットと未コミットの作業をエージェントごとに要約する | `ai-agents` `git` `standup` `rust` | 1 | 2026-07-23 |
| [**herdr-replay**](https://github.com/neospeed83/herdr-replay)<br><sub>neospeed83</sub> | マルチエージェントのHerdrコーディングセッションを、インタラクティブなタイムラインとして記録・再生する | `ai-agents` `developer-tools` `terminal-recording` `rust` | 1 | 2026-08-29 |
| [**herdr-tournament**](https://github.com/neospeed83/herdr-tournament)<br><sub>neospeed83</sub> | Herdr向けの、対抗的なマルチエージェントコードレビュー | `rust` | 1 | 2026-08-29 |
| [**herdr-caffeinate**](https://github.com/nwarwick/herdr-caffeinate)<br><sub>nwarwick</sub> | Herdrのエージェントが動作中は、macOSのシステムスリープを防止する | `caffeinate` `coding-agents` `macos` `shell` | 1 | 2026-07-29 |
| [**herdr-spawn**](https://github.com/nytafar/herdr-spawn)<br><sub>nytafar</sub> | 1つのMCPツールで、チャットからのプロンプトを、リモートコントロールを有効にした手元のホスト上の実際のClaude Codeセッションに渡す | `python` | 1 | 2026-08-21 |
| [**🆕 herdr-agent-gateway**](https://github.com/pikujs/herdr-agent-gateway)<br><sub>pikujs</sub> | Secure HTTP remote dispatch gateway, skill, and MCP server for Herdr terminal multiplexer | `javascript` | 1 | 🔄 2026-09-24 |
| [**🆕 herdr-tasks**](https://github.com/pinkpixel-dev/herdr-tasks)<br><sub>pinkpixel-dev</sub> | A Herdr plugin that puts your agent's task list in a split pane beside it, checked off as the agent works. | `ai` `ai-agents` `antigravity` `claude-code` `cli` | 1 | 🔄 2026-09-19 |
| [**herdr-imebox**](https://github.com/Sawakee/herdr-imebox)<br><sub>Sawakee</sub> | herdr内のAIエージェントペインに日本語・CJKを入力しやすくする、IME対応のポップアップテキストボックス | `cjk` `ime` `input-method` `japanese` `ratatui` | 1 | 2026-07-17 |
| [**🆕 herdr-llm-lint**](https://github.com/shindakun/herdr-llm-lint)<br><sub>shindakun</sub> | Lints CLAUDE.md, AGENTS.md, and agent instruction files for stale paths, commands, facts, and drift | `agents-md` `ai-agents` `claude-code` `claude-md` `cli` | 1 | 🔄 2026-09-21 |
| [**🆕 herdr-testrun**](https://github.com/shindakun/herdr-testrun)<br><sub>shindakun</sub> | Herdr plugin. Runs a project's tests in a pane, lists the failures, sends them to the agent on one key. | `go` `nodejs` `rust` | 1 | 🔄 2026-09-20 |
| [**herdr-awake**](https://github.com/susomejias/herdr-awake)<br><sub>susomejias</sub> | herdrプラグイン：Herdrのエージェントが作業中の間、マシンをスリープさせない | `shell` | 1 | 2026-08-26 |
| [**herdr-traex**](https://github.com/szrenwei/herdr-traex)<br><sub>szrenwei</sub> | TraeXエージェントのライフサイクルとメタデータをHerdr Marketplaceと連携させる | `traex` `python` | 1 | 2026-08-04 |
| [**herdr-forkr**](https://github.com/t4t5/herdr-forkr)<br><sub>t4t5</sub> | エージェントの会話を、新しい herdr ペインへフォークします。 | `shell` | 1 | 🔄 2026-09-10 |
| [**herdr-orc**](https://github.com/tamdogood/herdr-orc)<br><sub>tamdogood</sub> | Herdr向けの、プロファイル駆動でカスタマイズ可能な最小構成のオーケストレーター | `ai-agents` `multi-agent` `orchestrator` `javascript` | 1 | 2026-08-11 |
| [**tinysend-herdr**](https://github.com/tiny-send/tinysend-herdr)<br><sub>tiny-send</sub> | herdrプラグイン：エージェントがブロック/完了したら自分にメールを送り、返信でブロック解除できる。tinysendを使用 | `ai-agents` `tinysend` `javascript` | 1 | 2026-06-26 |
| [**herdr-rovo-dev**](https://github.com/usrivastava92/herdr-rovo-dev)<br><sub>usrivastava92</sub> | Rovo Dev CLIのセッションを検出し、Herdr上で稼働中のエージェントとして報告するHerdrプラグイン | `ai-agent` `rovo` `rovo-dev` `shell` | 1 | 2026-07-19 |
| [**herdr-polyglot**](https://github.com/wazum/herdr-polyglot)<br><sub>wazum</sub> | コーディングエージェントへのプロンプトを自分の言語で書ける——DeepLまたはGoogle Cloud Translateが英語に翻訳し、Claude Code・Codex・その他任意のherdrエージェントペインに届ける | `ai-agents` `bubbletea` `bubbletea-tui` `claude-code` `codex` | 1 | 2026-09-01 |
| [**herdr-session-titles**](https://github.com/wxomi/herdr-session-titles)<br><sub>wxomi</sub> | Herdr 上の Devin・Cursor・Agy・Kiro・Claude に対して、リッチなセッションタイトルとタスクのコンテキストを提供します。 | `ai-agents` `terminal` `python` | 1 | 🔄 2026-09-17 |
| [**cbds**](https://github.com/zqkra/cbds)<br><sub>zqkra</sub> | Herdrの群れ向けの、信頼性の高いマルチエージェントオーケストレーション。永続化されたタスク、権威あるワーカーレポート、ハングしない待機処理を提供する | `agents` `cli` `multi-agent` `orchestration` `javascript` | 1 | 2026-08-31 |
| [**🆕 herdr-dynamic-workflow**](https://github.com/andthezhang/herdr-dynamic-workflow)<br><sub>andthezhang</sub> | Herdr内でコーディングエージェントCLIをオーケストレーションするための、JavaScript製ワークフロー | `agent-fleet` `agent-orchestration` `agent-swarm` `agentic-ai` `agents` | 0 | 2026-08-30 |
| [**🆕 herdr-agent-manager**](https://github.com/bleedingfight/herdr-agent-manager)<br><sub>bleedingfight</sub> | fzfベースのファジー検索で、workspace・tab・pane・agentを扱うツール | `python` | 0 | 2026-09-04 |
| [**herdr-warp**](https://github.com/cdpath/herdr-warp)<br><sub>cdpath</sub> | Herdrのペイン内で対話型のWarp Agent CLI（warp）を操作するHerdrプラグイン：open/send/status/wait/read/approve/deny/new/stop/exitに対応し、画面をスクレイピングしてidle/working/blockedの状態を判定する | `shell` | 0 | 2026-08-13 |
| [**clawsouls-herdr-plugin**](https://github.com/clawsouls/clawsouls-herdr-plugin)<br><sub>clawsouls</sub> | _(説明なし)_ | `ai-agents` `persona` `shell` | 0 | 2026-08-11 |
| [**herdr-supervisor**](https://github.com/Ejlonn/herdr-supervisor)<br><sub>Ejlonn</sub> | Herdr 上で動くコーディングエージェントに対する、永続的な human-in-the-loop オーケストレーションとリモート制御を提供します。 | `python` | 0 | 🔄 2026-09-12 |
| [**herdr-nudge**](https://github.com/EricBois/herdr-nudge)<br><sub>EricBois</sub> | herdrのエージェントに「継続を促す通知」を仕掛ける——指定した時刻、またはアイドル/ブロック状態になったときに発火する | `shell` | 0 | 2026-07-17 |
| [**herdr-mail**](https://github.com/husniadil/herdr-mail)<br><sub>husniadil</sub> | Herdr上のコーディングエージェント同士の非同期メール——ストアを正とするメールボックス、ヒントとなる1行のペインマーカー、追跡可能な依頼付きのask/replyを、1つのGoバイナリで実現 | `ai-agents` `mail` `mcp-server` `sqlite` `go` | 0 | 2026-08-30 |
| [**🆕 herdr-ai-memory**](https://github.com/iagogfe/herdr-ai-memory)<br><sub>iagogfe</sub> | Herdrプラグイン：ai-memoryが管理するワークストリーム経由でコーディングエージェントを起動する——エージェントをまたいだセッションの継続性を実現 | `ai-agents` `ai-memory` `terminal` `javascript` | 0 | 2026-07-24 |
| [**🆕 herdr-spaces**](https://github.com/lukecameron/herdr-spaces)<br><sub>lukecameron</sub> | Agent counts and model-generated names for Herdr spaces | `go` | 0 | 🔄 2026-09-24 |
| [**🆕 herdr-agent-dash**](https://github.com/MartinBspheroid/herdr-agent-dash)<br><sub>MartinBspheroid</sub> | Herdr Agent Board：稼働中のコーディングエージェント、その状態・作業ディレクトリ・Gitコンテキストを一目で確認できる、ローカルでキーボード操作中心のHerdrプラグイン | `typescript` | 0 | 2026-07-21 |
| [**🆕 herdr-green**](https://github.com/natori-hrj/herdr-green)<br><sub>natori-hrj</sub> | herdr向けのエージェントごとのテスト状態表示——エージェントが完了したらプロジェクトのテストを実行し、成功/失敗を表示する | `ai-agents` `ci` `tests` `rust` | 0 | 2026-07-23 |
| [**🆕 agentic-box**](https://github.com/nicoRomeroCuruchet/agentic-box)<br><sub>nicoRomeroCuruchet</sub> | Claude Codeがローカルモデルのエージェントを操作する、隔離されたbox | `agent-orchestration` `agentic` `agentic-workflow` `docker` `ornith-1-0-35b` | 0 | 2026-08-17 |
| [**🆕 herdr-plugin-aos**](https://github.com/noctaIO/herdr-plugin-aos)<br><sub>noctaIO</sub> | 任意のワークスペースから、Agentic OS対応のClaude Codeエージェントをherdrのペインで起動する。非侵襲的なherdrプラグイン | `shell` | 0 | 2026-07-11 |
| [**herdr-zcode**](https://github.com/Nofuture123/herdr-zcode)<br><sub>Nofuture123</sub> | Herdr 上の ZCode：TUI ペインと委譲ブリッジを提供し、任意の CLI エージェントからネイティブの ZCode エグゼキューターへ処理を委ねられます。 | `zcode` `python` | 0 | 🔄 2026-09-19 |
| [**🆕 ocean-herdr**](https://github.com/Risingtides-dev/ocean-herdr)<br><sub>Risingtides-dev</sub> | Herdr向けのOceanエージェント連携 | `coding-agent` `ocean` `rust` | 0 | 2026-07-17 |
| [**🆕 herdr-hud**](https://github.com/sharonbrownw330/herdr-hud)<br><sub>sharonbrownw330</sub> | Keep coding agents visible and responsive while gaming with a draggable Herdr HUD overlay on your desktop. | `agent` `agentic-ai` `antigravity` `bash` `claude-code` | 0 | 🔄 2026-09-25 |
| [**herdr-quick-prompt**](https://github.com/Taanviir/herdr-quick-prompt)<br><sub>Taanviir</sub> | Herdr plugin — press a key, pick a coding agent, type a prompt, and it launches in a new tab or split. | `coding-agents` `terminal` `tui` `javascript` | 0 | 🔄 2026-09-24 |
| [**herdr-group-chat**](https://github.com/terry-li-hm/herdr-group-chat)<br><sub>terry-li-hm</sub> | Pi・Claude Code・Codex・Grok Buildのための、共有ローカルHerdrルーム | `ai-agents` `claude-code` `codex` `grok` `multi-agent` | 0 | 2026-09-08 |
| [**🆕 herdr-cline-plugin**](https://github.com/TheMetalStorm/herdr-cline-plugin)<br><sub>TheMetalStorm</sub> | 任意のペインから起動した素のCline CLIを、ネイティブのHerdrエージェントのように見せるHerdrプラグイン | `cli` `cline` `herdr-integration` `shell` | 0 | 2026-07-31 |

<details><summary>この目的にも関係するもの</summary>

- [ZingerLittleBee/Heeler](https://github.com/ZingerLittleBee/Heeler) — herdr 用のネイティブ iOS エージェントコンソールです。SSH 経由でお使いのマシン上のコーディングエージェントを監視・操作できます。本物の libghostty ターミナル、QR コードによるペアリング、エー…
- [a2u/herdr-jira](https://github.com/a2u/herdr-jira) — herdr向けのJira TUIプラグイン——設定可能なJQLフィルタでissueを閲覧・検索・ステータス変更し、1キーでターミナル上のAIエージェントにissueを委任できる
- [e2b-dev/herdr-e2b-sandbox](https://github.com/e2b-dev/herdr-e2b-sandbox) — git worktreeをE2B Sandboxにミラーするherdrプラグイン——単一のboxでも、エージェントごとにブランチを割り当てたフリートでも対応。TUIダッシュボード付き
- [walcew/herdr-assist](https://github.com/walcew/herdr-assist) — AIコーディングエージェント向けターミナルマルチプレクサHerdrのための、物理デスクパネル——セッションの状態を色で表示し、エージェントが判断を仰ぐために止まるとベルを鳴らす。ESP32-S3 + LVGL、ビルド済…
- [miko-misa/herdr-portfwd](https://github.com/miko-misa/herdr-portfwd) — リモートマシン上のコーディングエージェント向けの自動SSHポートフォワーディング——エージェントが出力したlocalhost URLをCtrl+クリックすると、同じポートで手元のマシンにページが開く。Herdrプラグイン
- [marvingygas/spoolway](https://github.com/marvingygas/spoolway) — Minimalistic agent state machine for software development: a dispatcher that drives agent sessions through de…
- [spad-0x/herdr-mobile-pro](https://github.com/spad-0x/herdr-mobile-pro) — Cyber-Dark デザインの、高性能でモバイルファーストな PWA ダッシュボード。スマホから直接 Herdr と自律型 AI エージェントをオーケストレーションできます。セキュアな HTTPS、音声入力、画像アッ…
- [virtualboard/herdr-virtualboard](https://github.com/virtualboard/herdr-virtualboard) — Kanban board for VirtualBoard feature specs inside Herdr: columns are the lifecycle, cards are specs, and dis…

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-worktree"></a>

## git worktree・ブランチ運用

> 作業ごとに worktree を切って、片付けまで自動でやりたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-worktrunk**](https://github.com/devashish2203/herdr-worktrunk)<br><sub>devashish2203</sub> | git worktree管理のためworktrunkを統合するHerdrプラグイン | `shell` | 160 | 🔄 2026-09-21 |
| [**herdr-plugin-jj-workspace**](https://github.com/NathanFlurry/herdr-plugin-jj-workspace)<br><sub>NathanFlurry</sub> | Jujutsu (jj) のワークスペースをHerdrのワークスペースとして作成・削除する | `jujutsu` `rust` | 48 | 2026-09-03 |
| [**herdr-plugin-renamer**](https://github.com/wyattjoh/herdr-plugin-renamer)<br><sub>wyattjoh</sub> | エージェントへの最初のプロンプトから、自動生成されたherdrのworktreeブランチとワークスペースをリネームする（デバイス上のApple FoundationModelsまたはCodexを利用） | `rust` | 15 | 2026-08-17 |
| [**herdr-e2b-sandbox**](https://github.com/e2b-dev/herdr-e2b-sandbox)<br><sub>e2b-dev</sub> | git worktreeをE2B Sandboxにミラーするherdrプラグイン——単一のboxでも、エージェントごとにブランチを割り当てたフリートでも対応。TUIダッシュボード付き | `cli` `cloud-dev` `e2b` `git-worktree` `sandbox` | 12 | 2026-09-10 |
| [**jj-waltz**](https://github.com/EzraCerpac/jj-waltz)<br><sub>EzraCerpac</sub> | Worktrunkに触発されたJujutsuワークスペース切り替えツール | `cli` `jj` `jujitsu` `utility` `workspace` | 9 | 🔄 2026-09-22 |
| [**herdr-plugin-git-worktree-hooks**](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks)<br><sub>freethinkel</sub> | git worktreeの作成/削除時にシェルコマンドを実行する——どのリポジトリの外にも置ける、全プロジェクト共通の1つのYAML設定 | `git-worktree` `javascript` | 7 | 2026-07-06 |
| [**bercail**](https://github.com/simoncrypta/bercail)<br><sub>simoncrypta</sub> | Herdr をベースにした、エージェント駆動の開発環境です。 | `agentic-coding` `agentic-development` `agentic-development-environment` `agentic-ide` `agentic-workflow` | 7 | 2026-09-10 |
| [**herdr-symlink-worktree**](https://github.com/hmu332233/herdr-symlink-worktree)<br><sub>hmu332233</sub> | メインのリポジトリにある共有ローカルファイルを、新しいworktreeにシンボリックリンクするherdrプラグイン | `shell` | 6 | 2026-07-16 |
| [**herdr-worktree-setup**](https://github.com/lamngockhuong/herdr-worktree-setup)<br><sub>lamngockhuong</sub> | 新しい worktree ごとに準備を整える Herdr プラグインです。設定ファイルの自動検出、共有ディレクトリへのリンク、任意のセットアップコマンドに対応します。 | `dotenv` `git-worktree` `monorepo` `javascript` | 6 | 🔄 2026-09-24 |
| [**herdr-worktree-from-pr**](https://github.com/tdi/herdr-worktree-from-pr)<br><sub>tdi</sub> | GitHubのPRからgit worktreeを作成し、herdrのワークスペースとして開く | `javascript` | 6 | 🔄 2026-09-11 |
| [**herdr-worktree-hooks**](https://github.com/timofey-TK/herdr-worktree-hooks)<br><sub>timofey-TK</sub> | herdrプラグイン：git worktreeの作成・オープン・削除時に、カスタムのセットアップ/後始末コマンドを実行する | `developer-tools` `git-worktree` `worktree` `python` | 6 | 2026-07-17 |
| [**herdr-worktree-seed**](https://github.com/jlimas/herdr-worktree-seed)<br><sub>jlimas</sub> | コピーオンライトのnode_modulesと設定可能なローカルdotfilesを、新しいworktreeに投入するHerdrプラグイン | `developer-tools` `dotfiles` `git-worktree` `nodejs` `typescript` | 5 | 2026-07-28 |
| [**herdr-jj-status**](https://github.com/mroth/herdr-jj-status)<br><sub>mroth</sub> | herdrプラグイン：jjのワークスペースのJujutsuブックマーク/ステータスを、スペースのサイドバーに表示する | `shell` | 5 | 2026-07-28 |
| [**herdr-worktreeinclude**](https://github.com/tanshio/herdr-worktreeinclude)<br><sub>tanshio</sub> | Herdrプラグイン：.worktreeincludeにマッチするgit管理外ファイルを、新しく作成されたworktreeにコピーする | `worktree` `worktreeiclude` `shell` | 5 | 2026-07-11 |
| [**herdr-pi-tree**](https://github.com/edxeth/herdr-pi-tree)<br><sub>edxeth</sub> | Pi のエージェントをツリー表示するサイドバーです——誰が誰を生成したか、どの worktree がどのブランチか、誰があなたを待っているかが分かります。 | `git-worktrees` `pi` `pi-coding-agent` `sidebar` `terminal` | 4 | 🔄 2026-09-18 |
| [**herdr-jj**](https://github.com/OliverGilan/herdr-jj)<br><sub>OliverGilan</sub> | HerdrにJujutsuのワークスペースサポートを追加する | `jujutsu` `rust` | 4 | 2026-08-12 |
| [**herdr-fresh-worktree**](https://github.com/persiyanov/herdr-fresh-worktree)<br><sub>persiyanov</sub> | 新しく作成したherdrのworktreeを、originのデフォルトブランチの最新状態にリセットする | `javascript` | 4 | 2026-06-25 |
| [**herdr-remote-worktrunk**](https://github.com/ditwrd/herdr-remote-worktrunk)<br><sub>ditwrd</sub> | Herdr向けのリモートworktrunkワークスペース | `shell` | 3 | 2026-07-10 |
| [**🆕 herdr-plugin-cow-worktree**](https://github.com/khatriafaz/herdr-plugin-cow-worktree)<br><sub>khatriafaz</sub> | Herdr plugin for strict copy-on-write Git worktrees that include ignored local files | `typescript` | 3 | 🔄 2026-09-20 |
| [**herdr-wish**](https://github.com/MovieHolic-Plex/herdr-wish)<br><sub>MovieHolic-Plex</sub> | Herdr プラグイン。願いごとを伝えると omo が PR をコミットします。omo-10 と唱えれば、worktree を 10 個開きます。 | `omo` `wish` `javascript` | 3 | 2026-09-04 |
| [**herdr-branch-cleanup**](https://github.com/osolmaz/herdr-branch-cleanup)<br><sub>osolmaz</sub> | ペインのブランチがGitHub上でマージまたは削除されたら、デフォルトブランチにチェックアウトする | `git` `github` `rust` | 3 | 2026-07-26 |
| [**herdr-worktree-lifecycle**](https://github.com/qdentity/herdr-worktree-lifecycle)<br><sub>qdentity</sub> | Herdrプラグイン：worktreeのライフサイクルイベントを、リポジトリ側が持つセットアップ/後始末用のラッパーに配信する | `rust` | 3 | 2026-06-29 |
| [**🆕 herdr-opendeck**](https://github.com/Resilient-Software/herdr-opendeck)<br><sub>Resilient-Software</sub> | Mirror Herdr workspaces onto a Stream Deck. Live tiles with repository, branch and agent status. | `elgato` `opendeck` `stream-deck` `typescript` | 3 | 🔄 2026-09-21 |
| [**herdr-worktree-nav**](https://github.com/ShoMasegi/herdr-worktree-nav)<br><sub>ShoMasegi</sub> | _(説明なし)_ | `terminal` `rust` | 3 | 🔄 2026-09-25 |
| [**herdr-deck**](https://github.com/ctbaum/herdr-deck)<br><sub>ctbaum</sub> | The companion workspace launcher for herdr-agents.nvim: open or resume Claude, Codex, and Pi in a ready-made Neovim, agent, and shell deck. | `claude-code` `codex` `coding-agents` `git-worktree` `neovim` | 2 | 🔄 2026-09-23 |
| [**trunkr**](https://github.com/disintegrator/trunkr)<br><sub>disintegrator</sub> | Herdr🤝Worktrunk——HerdrとWorktrunkを連携させるプラグイン | `go` | 2 | 2026-08-12 |
| [**herdr-tagr**](https://github.com/dvoets/herdr-tagr)<br><sub>dvoets</sub> | herdr 向けの簡潔でアイコン優先のタブタイトルです。アプリアイコン＋git ブランチ＋フォルダを表示します。 | `rust` `terminal` | 2 | 🔄 2026-09-14 |
| [**herdr-worktreeinclude**](https://github.com/eightHundreds/herdr-worktreeinclude)<br><sub>eightHundreds</sub> | Herdrプラグイン：.worktreeincludeで指定したgit管理外ファイルを、新しいworktreeにコピーする | `worktree` `rust` | 2 | 2026-07-28 |
| [**herdr-multirepo**](https://github.com/jattento/herdr-multirepo)<br><sub>jattento</sub> | 複数のリポジトリにまたがる1つのフィーチャーブランチを、1つのHerdrワークスペースで扱う | `git-worktree` `python` | 2 | 2026-08-03 |
| [**herdr-shear**](https://github.com/moneycaringcoder/herdr-shear)<br><sub>moneycaringcoder</sub> | 安全に削除できるgit worktreeを見つけて削除する。herdr向けのworktree清掃係 | `cleanup` `git-worktree` `rust` `terminal` | 2 | 2026-09-01 |
| [**herdr-worktreeinclude**](https://github.com/serhii-chernenko/herdr-worktreeinclude)<br><sub>serhii-chernenko</sub> | 新しいworktreeにカスタムパスを許可し、Claude CLIと同様に`.worktreeinclude`ファイルを尊重する | `worktree` `shell` | 2 | 2026-07-23 |
| [**herdr-corral**](https://github.com/bfreed/herdr-corral)<br><sub>bfreed</sub> | Herdr内でGit worktreeをまとめて管理——envファイル、依存関係、エージェント/シェル/サーバー用のタブ、マージしても安全なクリーンアップに対応。Herdr向けのworkmux代替 | `git-worktree` `workmux` `python` | 1 | 2026-08-14 |
| [**herdr-keep-root**](https://github.com/bonkey/herdr-keep-root)<br><sub>bonkey</sub> | Herdr プラグイン：リポジトリの worktree ワークスペースがどれか開いている間、そのメインチェックアウトのワークスペースを開いたままにします。これにより Spaces パネルで worktree グループが崩れて表示されることを防ぎます。 | `shell` | 1 | 2026-09-08 |
| [**herdr-worktree-copy**](https://github.com/crexi/herdr-worktree-copy)<br><sub>crexi</sub> | .worktree-copyマニフェストに基づき、worktreeローカルファイルをコピー・シンボリックリンクするHerdrプラグイン | `git-worktree` `shell` | 1 | 2026-07-28 |
| [**herdr-composer**](https://github.com/danieljvdm/herdr-composer)<br><sub>danieljvdm</sub> | タスクを組み立て、コンテキストを添付し、隔離された Herdr ワークスペースでコーディングエージェントを起動できます。 | `coding-agents` `git-worktree` `rust` | 1 | 🔄 2026-09-25 |
| [**herdr-plugin-jj-workspace**](https://github.com/expnn/herdr-plugin-jj-workspace)<br><sub>expnn</sub> | A Herdr plugin to create and remove Jujutsu (jj) workspaces | `rust` | 1 | 🔄 2026-09-22 |
| [**herdr-allow**](https://github.com/Feasy01/herdr-allow)<br><sub>Feasy01</sub> | herdrプラグイン：.herdr-allowの許可リストを使って、gitignore対象のファイル（.env、シークレット、ローカル設定）を新しいworktreeすべてにコピーする | `shell` | 1 | 2026-07-02 |
| [**🆕 nexus**](https://github.com/IniZio/nexus)<br><sub>IniZio</sub> | Herdr plugin for running worktree in Cloud-Hypervisor sandboxes, with mem/cpu/disk hotplug and auto port-forwarding | `cloud-hypervisor` `go` | 1 | 🔄 2026-09-25 |
| [**herdr-plugin-gwm**](https://github.com/kbrdn1/herdr-plugin-gwm)<br><sub>kbrdn1</sub> | git worktree管理のためgwmを操作するherdrプラグイン——gwmを唯一の正とし、herdrはそれに追従する | `bash` `cli` `git-worktree` `gwm` `worktree` | 1 | 2026-07-27 |
| [**🆕 forestr**](https://github.com/ludoroo/forestr)<br><sub>ludoroo</sub> | A Herdr plugin that manages Git branch worktrees from one fast, modal fzf popup — list, open, create, and safely remove worktrees across every repository Herdr… | `git-worktree` `worktrunk` `shell` | 1 | 🔄 2026-09-25 |
| [**herdr-collide**](https://github.com/moneycaringcoder/herdr-collide)<br><sub>moneycaringcoder</sub> | 同じリポジトリの異なるgit worktreeで作業しているエージェント同士が衝突しそうなときに警告する——編集が単に重なっているだけか、実際に競合するのかも判定する | `conflict-detection` `git-worktree` `rust` `terminal` | 1 | 2026-09-01 |
| [**herdr-standup**](https://github.com/moneycaringcoder/herdr-standup)<br><sub>moneycaringcoder</sub> | エージェントが実際に何をしたかのダイジェスト。1つのコマンドで、指定した期間の全Herdrワークスペースについて、コミット・変更量・ブランチ・作業がどこかに着地したかを、読みやすい形でまとめて表示する | `git` `rust` `standup` `terminal` | 1 | 2026-09-01 |
| [**herdr-pr-worktree**](https://github.com/poislagarde/herdr-pr-worktree)<br><sub>poislagarde</sub> | GitHub のプルリクエストを、既存のチェックアウトを再利用しながら Herdr の worktree スペースとして開きます。 | `git-worktree` `python` | 1 | 🔄 2026-09-23 |
| [**herdr-jira-worktree**](https://github.com/spiritsack/herdr-jira-worktree)<br><sub>spiritsack</sub> | herdrプラグイン：Jiraチケットの入力を求め、対応するgit worktreeを開く/再利用し、新しいClaude Codeセッションに事前入力する | `shell` | 1 | 2026-08-24 |
| [**herdr-worktree-include**](https://github.com/tupton/herdr-worktree-include)<br><sub>tupton</sub> | herdr が作成した git worktree に、未追跡のファイルをシンボリックリンクまたはコピーします。 | `shell` | 1 | 🔄 2026-09-14 |
| [**herdr-plugin-worktree-bootstrap**](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap)<br><sub>zerodice0</sub> | 新しいHerdrのGit worktreeに、無視されているローカルファイルを安全にコピーし、セットアップコマンドを実行する | `python` | 1 | 2026-08-03 |
| [**herdr-plugin-pr-board**](https://github.com/0xthc/herdr-plugin-pr-board)<br><sub>0xthc</sub> | 現在のリポジトリのGitHub PRをherdr内で扱う——ペインで一覧・閲覧し、選んだものをworktreeワークスペースとしてチェックアウトし、マージ済みのものを安全に回収する | `shell` | 0 | 2026-08-20 |
| [**🆕 herdr-plugin-worktree-bootstrap**](https://github.com/0xthc/herdr-plugin-worktree-bootstrap)<br><sub>0xthc</sub> | 新しいherdr worktreeを開いた瞬間に、.envファイルとnode_modulesを投入する | `shell` | 0 | 2026-08-22 |
| [**🆕 herdr-worktree-include**](https://github.com/heyfirst/herdr-worktree-include)<br><sub>heyfirst</sub> | herdr plugin that copies .worktreeinclude files into new worktrees. Built with Bun. 🍞 | `bun` `claude-code` `git-worktree` `worktree` `typescript` | 0 | 🔄 2026-09-23 |
| [**🆕 herdr-session-fork**](https://github.com/mackt/herdr-session-fork)<br><sub>mackt</sub> | Herdr plugin: fork the focused Claude Code / Codex / Pi / Grok session into another workspace or worktree, picked from a fuzzy list | `shell` | 0 | 🔄 2026-09-24 |
| [**🆕 herdr-worktree-include**](https://github.com/scoussens-nthplusio/herdr-worktree-include)<br><sub>scoussens-nthplusio</sub> | リポジトリの.worktreeincludeを使って、.envなどgit管理外のファイルを新しいHerdr worktreeにコピーする——Claude Codeが使うのと同じファイル・同じルール | `dotenv` `git-worktree` `shell` | 0 | 2026-08-27 |

<details><summary>この目的にも関係するもの</summary>

- [tdi/herdr-worktree-from-linear](https://github.com/tdi/herdr-worktree-from-linear) — Linearのissueからgit worktreeを作成し、herdrのワークスペースとして開く
- [upstash/herdr-upstash-box](https://github.com/upstash/herdr-upstash-box) — Herdr プラグイン：今見ている worktree から、Upstash Box 上でコーディングエージェントを実行します。
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — JavaScript/TypeScript向けにHerdrのworktreeを自動でブートストラップ——ロックファイルを考慮したインストールと、安全な環境ファイルの復元に対応
- [tomasvarga/herdr-e2b](https://github.com/tomasvarga/herdr-e2b) — 必要なときにgit worktreeを新しいE2Bクラウドサンドボックスへミラーする——未コミットの変更も含めたスナップショットをアップロードするだけで、pushやcloneは不要なherdrプラグイン
- [hanbong5938/herdr-jira-worktree](https://github.com/hanbong5938/herdr-jira-worktree) — Jira TUI plugin for herdr (fork of a2u/herdr-jira) — JQL filters, search, status transitions, delegate issues…
- [mrolafsson/herdr-linear](https://github.com/mrolafsson/herdr-linear) — Linear issues and projects in a herdr popup: status icons, rendered descriptions, status changes, one key to…
- [poislagarde/herdr-worktree-cleanup](https://github.com/poislagarde/herdr-worktree-cleanup) — Herdr のスペースが閉じられたとき、安全な GitHub PR の worktree を自動的にクリーンアップします。Python 製、依存なし、MIT ライセンス。
- [Tarektouati/herdr-pr-modal](https://github.com/Tarektouati/herdr-pr-modal) — Open any pull request in its own worktree, straight from a Herdr
- [zamarrowski/herdr-issues](https://github.com/zamarrowski/herdr-issues) — herdr plugin: browse the GitHub issues of the repo you're in and hand one to any coding agent (Claude Code, C…
- [ZviBaratz/herdr-draft](https://github.com/ZviBaratz/herdr-draft) — herdr プラグイン：新規セッション作成ダイアログです。Linear の issue・worktree・配置場所・エージェントの種類・clauth アカウント・最初のプロンプトを、一度の送信でまとめて設定できます。
- [logocode/herdr-linear-launcher](https://github.com/logocode/herdr-linear-launcher) — Linear の issue から、バックグラウンドの Herdr worktree で Codex や Claude を起動します。
- [snics/herdr-worktree-from-gitlab](https://github.com/snics/herdr-worktree-from-gitlab) — herdrプラグイン：GitLabのissueから（glab経由で）git worktreeとワークスペースを作成する
- [untalfranfernandez/herdr-worktreeinclude](https://github.com/untalfranfernandez/herdr-worktreeinclude) — 新しいgit worktreeに必要なgitignore対象のローカルファイル（.env、settings.local.json、フィクスチャなど）を自動配置するHerdrプラグイン。.worktreeincludeフ…

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-review"></a>

## コードレビュー・差分確認

> エージェントが書いた差分を読んで、コメントを返したい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**crabbox**](https://github.com/openclaw/crabbox)<br><sub>openclaw</sub> | Crabbox：サンドボックスを温め、差分を同期し、テストスイートを実行する | `agent-skills` `remote-test-runner` `go` | 1429 | 🔄 2026-09-25 |
| [**herdr-reviewr**](https://github.com/persiyanov/herdr-reviewr)<br><sub>persiyanov</sub> | herdr 用のコードレビュー＋ファイルビューアのサイドバーです。差分にコメントしてエージェントへ送り返せます。差分・ファイル・PR の状態を確認できます。 | `code-review` `rust` `tui` | 773 | 🔄 2026-09-23 |
| [**herdr-annotate**](https://github.com/plannotator/herdr-annotate)<br><sub>plannotator</sub> | Herdrでターミナルのテキスト・ドキュメント・エージェントの返答に注釈を付けてレビューし、そのフィードバックをそのままエージェントに送り返す | `annotation` `multiplexer` `rust` | 564 | 🔄 2026-09-25 |
| [**roamgate**](https://github.com/powerfooI/roamgate)<br><sub>powerfooI</sub> | A Herdr client for any screen. Control terminals, monitor coding agents, and review files and diffs from desktop or mobile. | `ai-agents` `bun` `code-review` `developer-tools` `git-worktree` | 247 | 🔄 2026-09-25 |
| [**herdr-hunk-diff**](https://github.com/jhochenbaum/herdr-hunk-diff)<br><sub>jhochenbaum</sub> | herdrからHunkでエージェントが書いた変更をレビューし、インラインコメントを担当エージェントに送り返す | `code-review` `hunk` `typescript` | 132 | 🔄 2026-09-23 |
| [**herdr-plannotator**](https://github.com/plannotator/herdr-plannotator)<br><sub>plannotator</sub> | HerdrのBrowserペイン内でPlannotatorのレビューを開くプラグイン | `plannotator` `typescript` | 26 | 2026-07-29 |
| [**herdr-pickr**](https://github.com/tomasvarga/herdr-pickr)<br><sub>tomasvarga</sub> | herdr向けのPRレビュールーター——GitHubのPRやGitLabのMRリンクをCtrl+クリックしてレビュアー（tuicr・hunk・diff・ブラウザ・または独自ツール）を選択、AIによる一次レビューもオプションで利用可能 | `cli` `code-review` `pull-request` `tui` `shell` | 20 | 2026-07-13 |
| [**herdr-plugin-hunk**](https://github.com/edmundmiller/herdr-plugin-hunk)<br><sub>edmundmiller</sub> | Hunkの差分をスプリットペインやタブで開くHerdrプラグイン | `python` | 15 | 2026-06-23 |
| [**herdr-gitview**](https://github.com/ChmaraX/herdr-gitview)<br><sub>ChmaraX</sub> | herdr向けのGitステータス/差分パネル——変更のレビュー、nvimでの編集、ステージ/コミット/破棄をすべてターミナルから行える | `git` `git-diff` `git-tui` `neovim` `rust` | 11 | 2026-09-06 |
| [**herdr-extensions**](https://github.com/vonzelle-vzt/herdr-extensions)<br><sub>vonzelle-vzt</sub> | herdr向けの小さなVS Code——LSPによる診断・自動補完・リネーム・定義へジャンプに対応した本格エディタに加え、ソース管理・検索・問題一覧・テスト・デバッガ・アプリのライブプレビュー・実行時エラー捕捉・画像貼り付け・エージェント差分レビューまで搭載。12パネル構成、コマンド1つで冪等かつ元に戻せる導入 | `agent-tools` `autocomplete` `claude-code` `cli` `code-review` | 6 | 2026-08-03 |
| [**herdr-plugin-hunk-autodiff**](https://github.com/scott306lr/herdr-plugin-hunk-autodiff)<br><sub>scott306lr</sub> | Herdrプラグイン：コーディングエージェントが未コミットの変更を残して完了したら、hunkの差分スプリットを自動で開く | `claude-code` `hunk` `python` | 5 | 2026-07-05 |
| [**herdr-progressive-reviewer**](https://github.com/flupke/herdr-progressive-reviewer)<br><sub>flupke</sub> | Tidewaveに着想を得た、ターン制の差分レビューア | `rust` | 3 | 🔄 2026-09-23 |
| [**herdr-tasks**](https://github.com/husniadil/herdr-tasks)<br><sub>husniadil</sub> | Herdr上のコーディングエージェント向けのタスクバックログ＋メモボード——リース付きのclaim、証跡に基づくレビュー、人間による決定ゲートを、1つのGoバイナリで実現 | `ai-agents` `mcp-server` `notes` `sqlite` `task-management` | 3 | 2026-08-30 |
| [**herdr-review.nvim**](https://github.com/inferst/herdr-review.nvim)<br><sub>inferst</sub> | GitとherdrをNeovimに統合したコードレビュー用UI | `lua` | 3 | 2026-08-01 |
| [**herdr-review**](https://github.com/quantk/herdr-review)<br><sub>quantk</sub> | エージェントが書いた変更をHunkでレビューし、インラインのフィードバックをHerdr経由で送り返す | `code-review` `hunk` `javascript` | 3 | 2026-07-28 |
| [**easy-review**](https://github.com/VilfredSikker/easy-review)<br><sub>VilfredSikker</sub> | AI支援によるコーディング向けのGit差分レビュー。ターミナルTUIとTauriデスクトップアプリの両方に対応 | `ai-code-review` `cli` `code-review` `desktop-app` `developer-tools` | 3 | 🔄 2026-09-22 |
| [**herdr-stagr**](https://github.com/brianh20/herdr-stagr)<br><sub>brianh20</sub> | herdr向けのソース管理サイドバー——並列差分表示でステージ・アンステージ・破棄ができる | `git` `tui` `rust` | 2 | 2026-08-06 |
| [**herdr-pr-tracker**](https://github.com/jakekroon/herdr-pr-tracker)<br><sub>jakekroon</sub> | あなたが作成したオープン中のプルリクエストをすべて、対応が必要な度合いで色分けしてドッキング表示する。Herdrプラグイン | `bun` `code-review` `developer-tools` `github` `pull-requests` | 2 | 🔄 2026-09-25 |
| [**herdr-scribe**](https://github.com/Javamomma/herdr-scribe)<br><sub>Javamomma</sub> | herdrプラグイン：録音せずにライブで会議を文字起こし——マイク入力をRAM上のみのトランスクリプトとライブ分析用ペインに変換。停止時には議事録・任意のポリシーゲート・レビュー可能な自動ドラフトを生成。Linux/WSL2およびmacOS対応 | `macos` `meeting-notes` `privacy` `speech-to-text` `terminal` | 2 | 2026-08-07 |
| [**herdr-comments**](https://github.com/shadowfax92/herdr-comments)<br><sub>shadowfax92</sub> | コピーしたHerdrのターミナル出力に注釈を付け、ペインごとのコメントを収集してNeovimでレビューできる | `ai-agents` `annotations` `neovim` `rust` `terminal` | 2 | 🔄 2026-09-22 |
| [**herdr-lazygit-viewer**](https://github.com/tareqmlx/herdr-lazygit-viewer)<br><sub>tareqmlx</sub> | その時々に適したHerdrの表示面で、files・branches・commits・stashのいずれかのパネルを開いた状態でlazygitを起動する | `code-review` `lazygit` `rust` | 2 | 2026-08-14 |
| [**herdr-hunk**](https://github.com/yuucu/herdr-hunk)<br><sub>yuucu</sub> | herdrプラグイン：エージェントのワークスペースでHunkの差分レビューをトグルする | `diff` `hunk` `go` | 2 | 2026-07-20 |
| [**herdr-strays**](https://github.com/aleslanger/herdr-strays)<br><sub>aleslanger</sub> | 野良git worktreeを取りまとめるターミナルUI——プロジェクトを一覧し、変更ファイルをリアルタイム表示、差分を読み、パネルを離れずにClaudeへプロンプトを送れる | `rust` | 1 | 2026-08-12 |
| [**roboherd**](https://github.com/andschneider/roboherd)<br><sub>andschneider</sub> | herdrのワークスペース内で、roborevのレビュー状態とアクションを扱う | `rust` `tui` | 1 | 🔄 2026-09-20 |
| [**herdr-agent-diff**](https://github.com/baotran01/herdr-agent-diff)<br><sub>baotran01</sub> | エージェントのファイルシステムとGit差分を確認するHerdrプラグイン | `rust` | 1 | 2026-08-03 |
| [**Vincent**](https://github.com/chasereyn/Vincent)<br><sub>chasereyn</sub> | AI エージェントが書いたコードをレビューし、その場で修正できる、マウス操作を主体としたターミナルクライアントです。 | `go` | 1 | 2026-09-03 |
| [**🆕 huicr**](https://github.com/claytonjschneider/huicr)<br><sub>claytonjschneider</sub> | Herdr User Interface for Code Review | `python` | 1 | 🔄 2026-09-24 |
| [**herdr-peer-review**](https://github.com/Elio2000/herdr-peer-review)<br><sub>Elio2000</sub> | herdrのペインで2つ目のコーディングエージェントを開き、差分をレビューさせる——監視可能・自動承認・読み取り専用。レビュー↔修正↔判断の自律ループ用のClaude Codeスキルも同梱 | `agent-skills` `ai-agents` `claude-code` `code-review` `codex` | 1 | 2026-07-16 |
| [**herdr-git-graph**](https://github.com/jorge-huxley/herdr-git-graph)<br><sub>jorge-huxley</sub> | Herdr向けの読み取り専用gitグラフTUIプラグイン——色付きASCIIレーン、ブランチフィルタ、検索、必要に応じた差分表示に対応 | `rust` | 1 | 2026-07-17 |
| [**agentflock**](https://github.com/neospark-sol/agentflock)<br><sub>neospark-sol</sub> | AIが調整するビルダー役とレビュアー役のグループを、永続的なマイルストーン管理とともに提供する | `ai-agents` `pair-programming` `typescript` | 1 | 2026-08-21 |
| [**codey**](https://github.com/rodeyseijkens/codey)<br><sub>rodeyseijkens</sub> | レビューを主眼に置いた Git TUI（ターミナル UI）です。ステージ済み／変更ありの 2 セクション構成の差分ビューアに、一時的なコメントと実際の Git ステージングを組み合わせています。OpenTUI 上に構築。 | `code-review` `opentui` `review-tool` `tui` `typescript` | 1 | 🔄 2026-09-22 |
| [**herdr-git-graph**](https://github.com/sjlee06/herdr-git-graph)<br><sub>sjlee06</sub> | Herdr 用のインタラクティブな Git ブランチ・コミットグラフです。Rust と Ratatui で構築され、滑らかな曲線・検索・差分表示に対応します。 | `git` `git-graph` `ratatui` `rust` `terminal` | 1 | 🔄 2026-09-14 |
| [**herdr-hunk-viewer**](https://github.com/tareqmlx/herdr-hunk-viewer)<br><sub>tareqmlx</sub> | _(説明なし)_ | `code-review` `hunk` `rust` | 1 | 2026-08-21 |
| [**herdr-hunk**](https://github.com/cevr/herdr-hunk)<br><sub>cevr</sub> | Hunkのレビューコメントを、対応するHerdrエージェントペインに送る | `effect-ts` `hunk` `typescript` | 0 | 🔄 2026-09-23 |
| [**herdr-hunk**](https://github.com/goofansu/herdr-hunk)<br><sub>goofansu</sub> | 一時的なHunkオーバーレイを開く、素早いHerdrレビューアクションを提供する。Hunkを終了するとオーバーレイが閉じ、ワークスペースが元に戻る | `python` | 0 | 🔄 2026-09-17 |
| [**🆕 herdr-idle-panes**](https://github.com/leonho/herdr-idle-panes)<br><sub>leonho</sub> | herdrプラグイン：アイドル状態のシェルのままになっているペインを確認して閉じる、チェックリスト形式のポップアップ | `python` | 0 | 2026-08-22 |
| [**🆕 twig-herdr**](https://github.com/PolyphonyRequiem/twig-herdr)<br><sub>PolyphonyRequiem</sub> | Native Twig bench and digest review panel for Herdr; requires Twig 0.93.0+ and Node.js 22+. | `terminal` `twig` `go` | 0 | 🔄 2026-09-24 |
| [**herdr-diff-review.nvim**](https://github.com/rytkmt/herdr-diff-review.nvim)<br><sub>rytkmt</sub> | AIエージェントによるファイル変更を、適用前にNeovimのdiffモードでレビューする——Claude CodeやKiro CLIからの編集を、1つのコマンドで承認/拒否できる | `kiro-cli` `neovim` `neovim-plugin` `neovim-plugins` `nvim` | 0 | 🔄 2026-09-25 |
| [**🆕 herdr-hunks**](https://github.com/winoooops/herdr-hunks)<br><sub>winoooops</sub> | A Git hunk viewer for Herdr. Review committed and uncommitted changes, compare branches, and explore diffs in your terminal. | `git` `rust` `tui` | 0 | 🔄 2026-09-25 |
| [**herdr-review-pack**](https://github.com/YmlyZA/herdr-review-pack)<br><sub>YmlyZA</sub> | 実験的な Herdr プラグイン：人によるレビューのために、タスクの概要・Git の差分・スナップショットに紐づいたチェック結果をまとめます。 | `code-review` `developer-tools` `python` | 0 | 2026-09-09 |

<details><summary>この目的にも関係するもの</summary>

- [JacquesvanWyk/herdr-hunk](https://github.com/JacquesvanWyk/herdr-hunk) — herdr向けの、Hunkの差分をfzfで対話的に選ぶピッカー：コミット・範囲・stashに対応し、エージェント完了時に自動オープンもできる
- [anhnd3005-infinity/herdr-worker-orchestrator](https://github.com/anhnd3005-infinity/herdr-worker-orchestrator) — Herdr管理下のペイン経由で、CLIエージェントワーカー（agy・codexなど）にタスクを割り振る——状態を持つタスク追跡、worktreeによる隔離、差分ベースのレビューに対応。Claude CodeとHerdr…
- [tomasvarga/herdr-sniffr](https://github.com/tomasvarga/herdr-sniffr) — レビューする前に、AIがPRの問題を検知する——エージェントによる一次チェックでtuicrにドラフトコメントを残す。特定のエージェントに依存しない（codex/claude/cursor/grok/…）
- [elKei24/herdr-co-review](https://github.com/elKei24/herdr-co-review) — herdrでの分割画面PRレビュー——エージェントが問題を見つけ、あなたはTUIでコードの隣に並べて1件ずつ判断し、承認したものをエージェントが投稿する
- [itisbryan/herdr-gh-checks](https://github.com/itisbryan/herdr-gh-checks) — herdrプラグイン：現在のPRのCIをペインで監視・確認し、CI/マージ状態をサイドバーの行に表示する。Go + Bubble Tea製
- [mikhail-angelov/herdr-review-loop](https://github.com/mikhail-angelov/herdr-review-loop) — herdrのワークスペース内でエージェント同士が自動的に相互レビューする——1体が書き、もう1体がレビューし、これを繰り返す
- [jpolec/herdr-plugin-odysseus](https://github.com/jpolec/herdr-plugin-odysseus) — Governed multi-agent workflows for Herdr: tasks → agents in Herdr panes → checks, retries, review, policy, ap…
- [moneycaringcoder/herdr-collide](https://github.com/moneycaringcoder/herdr-collide) — 同じリポジトリの異なるgit worktreeで作業しているエージェント同士が衝突しそうなときに警告する——編集が単に重なっているだけか、実際に競合するのかも判定する
- [neospeed83/herdr-tournament](https://github.com/neospeed83/herdr-tournament) — Herdr向けの、対抗的なマルチエージェントコードレビュー

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-forge"></a>

## GitHub / issue トラッカー連携

> issue や PR を起点に作業を始めたい / PR の状態を追いたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**tsk**](https://github.com/smarzban/tsk)<br><sub>smarzban</sub> | tsk, a Linear alternative that stays in the terminal: a shared task board for you and your agents. TUI for you, CLI for them. | `cli` `productivity` `rust` `task-manager` `terminal` | 126 | 🔄 2026-09-22 |
| [**ghzinga**](https://github.com/osolmaz/ghzinga)<br><sub>osolmaz</sub> | 1つのGitHub issueやPRをクリックだけで見られる、Rust製の簡単なTUI | `rust` | 87 | 2026-09-06 |
| [**herdr-plugin-gh-pr**](https://github.com/wyattjoh/herdr-plugin-gh-pr)<br><sub>wyattjoh</sub> | フォーカス中のエージェントペインのブランチに対応するGitHub PRの状態をサイドバーに表示するherdrプラグイン | `typescript` | 22 | 2026-07-16 |
| [**herdr-worktree-from-linear**](https://github.com/tdi/herdr-worktree-from-linear)<br><sub>tdi</sub> | Linearのissueからgit worktreeを作成し、herdrのワークスペースとして開く | `javascript` | 19 | 🔄 2026-09-11 |
| [**herdr-plugin-github-start**](https://github.com/ogulcancelik/herdr-plugin-github-start)<br><sub>ogulcancelik</sub> | GitHub issue・PR・ディスカッションからCodexやClaudeを起動するHerdrプラグイン | `javascript` | 17 | 2026-08-31 |
| [**herdr-jira**](https://github.com/a2u/herdr-jira)<br><sub>a2u</sub> | herdr向けのJira TUIプラグイン——設定可能なJQLフィルタでissueを閲覧・検索・ステータス変更し、1キーでターミナル上のAIエージェントにissueを委任できる | `ai-agents` `jira` `ratatui` `rust` `tui` | 12 | 2026-09-05 |
| [**herdr-pr-tracker**](https://github.com/Matovidlo/herdr-pr-tracker)<br><sub>Matovidlo</sub> | herdrプラグイン：各Claude Codeセッションが作成するGitHub PRを、gh状態とアクション付きで追跡する | `claude-code` `shell` | 12 | 2026-08-12 |
| [**herdr-linear**](https://github.com/JacquesvanWyk/herdr-linear)<br><sub>JacquesvanWyk</sub> | herdrのスプリットペインまたはタブ内で動くfzf駆動のLinearパネル：issue検索、プロジェクトの深掘り、issue作成、ステータス変更ができる | `shell` | 8 | 2026-07-12 |
| [**herdr-git-status**](https://github.com/krystof018/herdr-git-status)<br><sub>krystof018</sub> | herdr内にCIの状態を表示する——GitLab（パイプライン＋マージリクエスト）とGitHub（Actions＋プルリクエスト）の両方に対応し、リポジトリのoriginから自動検出する | `bash` `ci-cd` `ci-status` `developer-tools` `github-actions` | 6 | 🔄 2026-09-20 |
| [**herdr-pr-board**](https://github.com/cdowell09/herdr-pr-board)<br><sub>cdowell09</sub> | 複数リポジトリを横断できる、設定可能なHerdr向けGitHubプルリクエストダッシュボード | `github` `tui` `go` | 4 | 🔄 2026-09-10 |
| [**mergr**](https://github.com/jsmenzies/mergr)<br><sub>jsmenzies</sub> | Herdr Spaceのサイドバー行にGitHubプルリクエストの状態を表示する | `github-pull-requests` `rust` | 4 | 2026-07-30 |
| [**herdr-linear**](https://github.com/talent-factory/herdr-linear)<br><sub>talent-factory</sub> | Herdr向けのLinear issueパネル。Enterキーで実装に着手できる | `rust` | 4 | 🔄 2026-09-16 |
| [**herdr-sniffr**](https://github.com/tomasvarga/herdr-sniffr)<br><sub>tomasvarga</sub> | レビューする前に、AIがPRの問題を検知する——エージェントによる一次チェックでtuicrにドラフトコメントを残す。特定のエージェントに依存しない（codex/claude/cursor/grok/…） | `ai` `cli` `code-review` `pull-request` `tuicr` | 4 | 2026-07-14 |
| [**herdr-co-review**](https://github.com/elKei24/herdr-co-review)<br><sub>elKei24</sub> | herdrでの分割画面PRレビュー——エージェントが問題を見つけ、あなたはTUIでコードの隣に並べて1件ずつ判断し、承認したものをエージェントが投稿する | `cli` `code-review` `pull-request` `rust` `tui` | 3 | 🔄 2026-09-23 |
| [**🆕 herdr-pane-issue**](https://github.com/ilazaridis/herdr-pane-issue)<br><sub>ilazaridis</sub> | Herdr plugin: shows the GitHub issue each agent pane is working on in the Agents sidebar, and opens it with one key. | `shell` | 3 | 🔄 2026-09-24 |
| [**herdr-gh-checks**](https://github.com/itisbryan/herdr-gh-checks)<br><sub>itisbryan</sub> | herdrプラグイン：現在のPRのCIをペインで監視・確認し、CI/マージ状態をサイドバーの行に表示する。Go + Bubble Tea製 | `bubbletea` `ci` `github-actions` `tui` `go` | 3 | 2026-08-25 |
| [**herdr-plugin-gh-workflow**](https://github.com/kkckkc/herdr-plugin-gh-workflow)<br><sub>kkckkc</sub> | GitHubワークフロー向けのHerdrプラグイン | `javascript` | 3 | 2026-07-03 |
| [**herdr-beads**](https://github.com/hexsprite/herdr-beads)<br><sub>hexsprite</sub> | HerdrでbeadsのissueIDをCtrl+クリックすると、詳細をスプリットペインで開く | `beads` `issue-tracker` `terminal` `shell` | 2 | 2026-08-07 |
| [**herdr-pr-watch**](https://github.com/maxguzenski/herdr-pr-watch)<br><sub>maxguzenski</sub> | Herdr プラグイン：各ワークスペースとエージェントペインの GitHub PR ステータスをサイドバーに表示します。 | `github-pull-requests` `python` | 2 | 2026-09-06 |
| [**herdr-plugin-jira-pr**](https://github.com/abtris/herdr-plugin-jira-pr)<br><sub>abtris</sub> | herdrプラグイン：現在のブランチのPRに紐づくJira issueを表示し、内容が食い違っていれば警告する | `github-pr` `jira` `shell` | 1 | 2026-08-04 |
| [**herdr-workspace-prs**](https://github.com/andrewbrannan/herdr-workspace-prs)<br><sub>andrewbrannan</sub> | ワークスペースの GitHub プルリクエストを追跡する Herdr プラグインです。 | `typescript` | 1 | 2026-09-04 |
| [**herdr-board**](https://github.com/bredebjorhovd/herdr-board)<br><sub>bredebjorhovd</sub> | コーディングエージェントが列に並び、自分の仕事を自律的にこなす場所——GitHub issueを入力に、herdrのペインで自律エージェントが動き、書いた本人にPRレビューが返ってくる | `rust` | 1 | 2026-08-14 |
| [**herdr-dashboard**](https://github.com/chouxcreams/herdr-dashboard)<br><sub>chouxcreams</sub> | herdrのワークスペース向けのPRステータスダッシュボードTUI——ペインごとのPRの状態・CI・レビューを一目で確認できる | `dashboard` `github` `pull-requests` `ratatui` `rust` | 1 | 2026-07-28 |
| [**herdr-plugin-dotfiles-github-link-preview**](https://github.com/edmundmiller/herdr-plugin-dotfiles-github-link-preview)<br><sub>edmundmiller</sub> | GitHubのissueやプルリクエストをサイドペインでプレビューするHerdrプラグイン | `python` | 1 | 2026-06-23 |
| [**🆕 herdr-jira-worktree**](https://github.com/hanbong5938/herdr-jira-worktree)<br><sub>hanbong5938</sub> | Jira TUI plugin for herdr (fork of a2u/herdr-jira) — JQL filters, search, status transitions, delegate issues to AI agents, and check out issues into git workt… | `jira` `tui` `rust` | 1 | 🔄 2026-09-23 |
| [**🆕 herdr-plugins**](https://github.com/JJLiebig/herdr-plugins)<br><sub>JJLiebig</sub> | Herdr plugin that starts Codex or Claude from a GitHub issue, PR, or discussion | `javascript` | 1 | 🔄 2026-09-22 |
| [**herdr-spaces-pr-status**](https://github.com/jmarbutt/herdr-spaces-pr-status)<br><sub>jmarbutt</sub> | Conductor風のPRボードで、herdrのスペースにGitHubプルリクエストの状態を表示する | `github-pull-request` `javascript` | 1 | 2026-09-09 |
| [**herdr-glab-status**](https://github.com/jpwallace22/herdr-glab-status)<br><sub>jpwallace22</sub> | 各ワークスペースの GitLab マージリクエストの状態を、スペースのサイドバーに $mr トークンとしてワークスペース行に表示する [Herdr](https://herdr.dev) プラグインです。 | `typescript` | 1 | 2026-09-09 |
| [**herdr-revdiff**](https://github.com/mikhail-angelov/herdr-revdiff)<br><sub>mikhail-angelov</sub> | revdiff（https://github.com/umputun/revdiff）の TUI 用 herdr プラグインです。 | `revdiff` `tui` `shell` | 1 | 🔄 2026-09-16 |
| [**🆕 herdr-linear**](https://github.com/mrolafsson/herdr-linear)<br><sub>mrolafsson</sub> | Linear issues and projects in a herdr popup: status icons, rendered descriptions, status changes, one key to a worktree, and Start hands the issue to your codi… | `bubbletea` `claude-code` `coding-agents` `git-worktree` `go` | 1 | 🔄 2026-09-24 |
| [**worktender**](https://github.com/steig/worktender)<br><sub>steig</sub> | GitHubのissueから、専用worktreeで作業するコーディングエージェントまでを1コマンドでつなぐ | `ai-agents` `claude-code` `coding-agents` `git-worktree` `golang` | 1 | 🔄 2026-09-16 |
| [**🆕 herdr-pr-modal**](https://github.com/Tarektouati/herdr-pr-modal)<br><sub>Tarektouati</sub> | Open any pull request in its own worktree, straight from a Herdr | `rust` | 1 | 🔄 2026-09-24 |
| [**🆕 herdr-ci-checks**](https://github.com/tdi/herdr-ci-checks)<br><sub>tdi</sub> | herdr plugin: live GitHub/GitLab CI checks for the current branch in a pane on the right | `javascript` | 1 | 🔄 2026-09-25 |
| [**herdr-github-pr**](https://github.com/woshahua/herdr-github-pr)<br><sub>woshahua</sub> | GitHubのPRの状態・チェック・レビュー・コメントを同期するHerdrプラグイン | `github` `javascript` | 1 | 2026-08-21 |
| [**herdr-pr**](https://github.com/yelsed/herdr-pr)<br><sub>yelsed</sub> | 対応待ちのプルリクエストを、herdrのペイン内でTodoとして表示する。すべてgh CLI経由で読み取る | `rust` | 1 | 2026-08-29 |
| [**🆕 herdr-issues**](https://github.com/zamarrowski/herdr-issues)<br><sub>zamarrowski</sub> | herdr plugin: browse the GitHub issues of the repo you're in and hand one to any coding agent (Claude Code, Codex, Gemini…) in its own git worktree. | `coding-agents` `github-issues` `javascript` | 1 | 🔄 2026-09-19 |
| [**🆕 herdr-draft**](https://github.com/ZviBaratz/herdr-draft)<br><sub>ZviBaratz</sub> | herdr プラグイン：新規セッション作成ダイアログです。Linear の issue・worktree・配置場所・エージェントの種類・clauth アカウント・最初のプロンプトを、一度の送信でまとめて設定できます。 | `bubbletea` `claude-code` `go` `linear` `tui` | 1 | 🔄 2026-09-23 |
| [**🆕 herdr-estate**](https://github.com/andrewdunndev/herdr-estate)<br><sub>andrewdunndev</sub> | Long-running campaigns for herdr: threads of agent work, addressed as estate/campaign, that outlive every conversation. Mirror of gitlab.com/dunn.dev/herdr-est… | `ai-agents` `claude-code` `cli` `rust` `terminal` | 0 | 🔄 2026-09-24 |
| [**🆕 herdr-pr-status**](https://github.com/anthonykimm/herdr-pr-status)<br><sub>anthonykimm</sub> | サイドバーの各ワークスペース行に、GitHub の PR 番号・レビュー状況・CI ステータスを、色分けされたアイコンで表示します。 | `python` | 0 | 2026-09-10 |
| [**🆕 herdr-jira-peek**](https://github.com/hilmimuktitama/herdr-jira-peek)<br><sub>hilmimuktitama</sub> | 現在の Herdr ペインから、Jira Cloud を読み取り専用でプレビューできます。 | `jira` `terminal` `shell` | 0 | 🔄 2026-09-25 |
| [**🆕 herdr-pr-preview**](https://github.com/juninaba/herdr-pr-preview)<br><sub>juninaba</sub> | 現在のブランチのGitHubプルリクエストを、スプリットペインでプレビューするHerdrプラグイン | `shell` | 0 | 2026-07-08 |
| [**herdr-plugin-github-status**](https://github.com/jwanga/herdr-plugin-github-status)<br><sub>jwanga</sub> | herdr プラグイン：マイルストーン・issue・PR・Actions といったリアルタイムの GitHub プロジェクトステータスを、サイドバー幅で右側にドッキング表示します。 | `github` `rust` `tui` | 0 | 🔄 2026-09-19 |
| [**🆕 herdr-linear-launcher**](https://github.com/logocode/herdr-linear-launcher)<br><sub>logocode</sub> | Linear の issue から、バックグラウンドの Herdr worktree で Codex や Claude を起動します。 | `javascript` | 0 | 🔄 2026-09-17 |
| [**github-issue-herdr-plugin**](https://github.com/nyanyaon/github-issue-herdr-plugin)<br><sub>nyanyaon</sub> | GitHubのissueを「herd（統率）」するためのClaude Codeプラグイン | `rust` | 0 | 2026-07-27 |
| [**herdr-gh-issue-label**](https://github.com/polidog/herdr-gh-issue-label)<br><sub>polidog</sub> | ブランチに対応する GitHub issue の番号とタイトルを Herdr のスペースに表示するプラグイン | `github-issues` `shell` | 0 | 2026-08-28 |
| [**🆕 herdr-github-metadata**](https://github.com/ralphilius/herdr-github-metadata)<br><sub>ralphilius</sub> | Herdr plugin: GitHub metadata for the sidebar — the PR each agent is working on | `github` `python` | 0 | 🔄 2026-09-25 |
| [**🆕 herdr-worktree-from-gitlab**](https://github.com/snics/herdr-worktree-from-gitlab)<br><sub>snics</sub> | herdrプラグイン：GitLabのissueから（glab経由で）git worktreeとワークスペースを作成する | `gitlab` `rust` `worktree` | 0 | 2026-07-09 |
| [**🆕 herdr-pr-workflow**](https://github.com/tamdogood/herdr-pr-workflow)<br><sub>tamdogood</sub> | フォーカス中のエージェントに、現在のブランチのプルリクエストを安全に作成またはマージするよう指示するHerdrアクション | `javascript` | 0 | 2026-08-10 |

<details><summary>この目的にも関係するもの</summary>

- [tomasvarga/herdr-pickr](https://github.com/tomasvarga/herdr-pickr) — herdr向けのPRレビュールーター——GitHubのPRやGitLabのMRリンクをCtrl+クリックしてレビュアー（tuicr・hunk・diff・ブラウザ・または独自ツール）を選択、AIによる一次レビューもオプシ…
- [tdi/herdr-worktree-from-pr](https://github.com/tdi/herdr-worktree-from-pr) — GitHubのPRからgit worktreeを作成し、herdrのワークスペースとして開く
- [jakekroon/herdr-pr-tracker](https://github.com/jakekroon/herdr-pr-tracker) — あなたが作成したオープン中のプルリクエストをすべて、対応が必要な度合いで色分けしてドッキング表示する。Herdrプラグイン
- [kiitosu/herdr-jira-board](https://github.com/kiitosu/herdr-jira-board) — herdr内で動くJiraカンバンボード。Claude Codeセッションランチャー付き
- [poislagarde/herdr-pr-worktree](https://github.com/poislagarde/herdr-pr-worktree) — GitHub のプルリクエストを、既存のチェックアウトを再利用しながら Herdr の worktree スペースとして開きます。
- [poislagarde/herdr-worktree-cleanup](https://github.com/poislagarde/herdr-worktree-cleanup) — Herdr のスペースが閉じられたとき、安全な GitHub PR の worktree を自動的にクリーンアップします。Python 製、依存なし、MIT ライセンス。
- [spiritsack/herdr-jira-worktree](https://github.com/spiritsack/herdr-jira-worktree) — herdrプラグイン：Jiraチケットの入力を求め、対応するgit worktreeを開く/再利用し、新しいClaude Codeセッションに事前入力する
- [ukwhatn/taskherd](https://github.com/ukwhatn/taskherd) — herdrのエージェントセッション・PR・Jiraチケットに連携したタスクボード
- [0xthc/herdr-plugin-pr-board](https://github.com/0xthc/herdr-plugin-pr-board) — 現在のリポジトリのGitHub PRをherdr内で扱う——ペインで一覧・閲覧し、選んだものをworktreeワークスペースとしてチェックアウトし、マージ済みのものを安全に回収する

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-layout"></a>

## ワークスペース・レイアウト構築

> プロジェクトを開いたら、タブ・ペイン・起動コマンドまで一発で整えたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-spreader**](https://github.com/yuk1ty/herdr-spreader)<br><sub>yuk1ty</sub> | 1つのYAMLファイルから、herdrのワークスペースレイアウト全体（タブ・ペイン・起動コマンドなど）を一括で立ち上げる | `rust` | 129 | 2026-08-16 |
| [**dotfiles**](https://github.com/lararosekelley/dotfiles)<br><sub>lararosekelley</sub> | Bashシェルでの使用を想定した個人用dotfiles | `bash` `bootstrap` `dotfiles` `homebrew` `macos` | 51 | 🔄 2026-09-22 |
| [**herdr-plugin-workspace-manager**](https://github.com/razajamil/herdr-plugin-workspace-manager)<br><sub>razajamil</sub> | worktree作成時にワークスペースごとのデフォルト設定を自動適用する、宣言的なタブ/ペインレイアウト | `rust` | 44 | 2026-08-23 |
| [**seshagy**](https://github.com/lmilojevicc/seshagy)<br><sub>lmilojevicc</sub> | tmuxとherdr向けのエージェント対応セッションマネージャー——プロジェクトを検出し、セッションを起動し、AIエージェントの作業を追跡する | `bubbletea` `go` `session-management` `session-manager` `terminal` | 20 | 🔄 2026-09-10 |
| [**herdr-grid**](https://github.com/thuanlm215/herdr-grid)<br><sub>thuanlm215</sub> | Herdr 用のビジュアルなペインレイアウトエディタです。ドラッグ＆ドロップ、新規シェルの追加、レイアウトの再利用、タブやワークスペースをまたいだペインの送信に対応します。 | `layout-presets` `pane-layout` `productivity` `ratatui` `rust` | 10 | 🔄 2026-09-12 |
| [**herdr-sidebar-config**](https://github.com/testy-cool/herdr-sidebar-config)<br><sub>testy-cool</sub> | Herdr 用の、ワークスペース → タブ → エージェントというサイドバー構成のプリセットです。1 タブだけのグループをコンパクトにまとめ、読みやすいタスクラベルとプロバイダーアイコンを表示します。 | `ai-agents` `claude-code` `codex` `configuration` `ghostty` | 9 | 🔄 2026-09-16 |
| [**glyph**](https://github.com/fru-dev3/glyph)<br><sub>fru-dev3</sub> | One identity for every coding agent you run. Marks each Claude Code, Antigravity, Codex or Gemini session with your label, the project, the machine and the mom… | `ai-agents` `claude-code` `cli` `codex` `developer-tools` | 5 | 🔄 2026-09-21 |
| [**herdr-warp**](https://github.com/HexSleeves/herdr-warp)<br><sub>HexSleeves</sub> | Herdrのワークスペースを、ネイティブのWarpペインとして開く | `shell` | 5 | 2026-07-25 |
| [**herdr-pane-layouts**](https://github.com/iurysza/herdr-pane-layouts)<br><sub>iurysza</sub> | Herdr向けの、tmux風のシームレスなペインリサイズとレイアウト | `pane-layout` `python` `terminal` | 4 | 🔄 2026-09-21 |
| [**herdr-muster**](https://github.com/marcoskichel/herdr-muster)<br><sub>marcoskichel</sub> | エージェントの状態を認識するherdr向けプロジェクト切り替えツール | `rust` | 4 | 2026-07-03 |
| [**herdr-fork-from-message**](https://github.com/dmangla3/herdr-fork-from-message)<br><sub>dmangla3</sub> | 以前のメッセージの時点からCodexやClaude Codeをフォークし、新しいHerdrのタブ・ペイン・ワークスペースとして開く | `claude-code` `codex` `developer-tools` `terminal-multiplexer` `python` | 3 | 2026-08-10 |
| [**herdr-layout-tools**](https://github.com/edouard-andrei/herdr-layout-tools)<br><sub>edouard-andrei</sub> | herdrプラグイン：レイアウトをその場で変形（main-left＋グリッド）したり均等化したりする——タブIDやペインIDは変わらず、プロセスも維持される | `javascript` | 3 | 2026-08-06 |
| [**herdr-compose**](https://github.com/ropali/herdr-compose)<br><sub>ropali</sub> | herdr-composeは、Herdr向けの宣言的なワークスペースレイアウトマネージャー | `layout-manager` `python` | 3 | 2026-07-25 |
| [**herdr-setup-bootstrap**](https://github.com/shizlie/herdr-setup-bootstrap)<br><sub>shizlie</sub> | worktree_init.tomlから新しいworktreeをブートストラップするHerdrプラグイン | `shell` | 3 | 2026-06-17 |
| [**herdr-google-gmail**](https://github.com/Tomatio13/herdr-google-gmail)<br><sub>Tomatio13</sub> | herdr-google-gmailは、ターミナルワークスペースツールherdr向けのGmail連携プラグイン | `shell` | 3 | 2026-07-22 |
| [**herdr-session-manager**](https://github.com/umutciloglu/herdr-session-manager)<br><sub>umutciloglu</sub> | herdr 向けのエージェントセッションマネージャーで、異なるハーネス間のメッセージングにも対応します。 | `rust` | 3 | 🔄 2026-09-18 |
| [**herdr-clone-layout**](https://github.com/danilolucasmd/herdr-clone-layout)<br><sub>danilolucasmd</sub> | 現在のワークスペースレイアウトを、新しいherdrのworktreeすべてに複製する。テンプレートも設定も不要——今いるレイアウトそのものがテンプレートになる | `shell` | 2 | 2026-08-27 |
| [**herdr-better-workspace**](https://github.com/hamzahraihan/herdr-better-workspace)<br><sub>hamzahraihan</sub> | AI コーディングエージェント向けのターミナルワークスペースマネージャー herdr 用の、インタラクティブな「ワークスペースを開く」ピッカープラグインです。 | `go` | 2 | 2026-09-09 |
| [**dsh-plugin-herdr**](https://github.com/sunny0826/dsh-plugin-herdr)<br><sub>sunny0826</sub> | DeepSeek Harness（DSH）向けのHerdrコントロールプレーンプラグイン——AIコーディングエージェント向けのターミナルワークスペースマネージャーであるHerdrを、DSHセッションから監視・操作する | `dsh-plugin` `typescript` | 2 | 2026-08-25 |
| [**herdr-google-calendar**](https://github.com/Tomatio13/herdr-google-calendar)<br><sub>Tomatio13</sub> | herdr-gog-calendarは、ターミナルワークスペースツールherdr向けのGoogleカレンダー連携プラグイン | `shell` | 2 | 2026-07-22 |
| [**reasonix-herdr**](https://github.com/uuie/reasonix-herdr)<br><sub>uuie</sub> | Herdr内でのライフサイクルのリアルタイム報告とワークスペース制御を行う、ネイティブなReasonixプラグイン | `reasonix` `python` | 2 | 2026-07-10 |
| [**herdr-workspace**](https://github.com/zackshen/herdr-workspace)<br><sub>zackshen</sub> | herdrプラグイン：中央に表示されるポップアップから、ワークスペースを作成しレイアウトプロファイルを適用する | `rust` | 2 | 2026-08-24 |
| [**herdr-layout**](https://github.com/3mmdrew/herdr-layout)<br><sub>3mmdrew</sub> | herdr向けのミニマルなワークスペースレイアウト定義——Luaファイルを渡すだけでワークスペースが立ち上がる。依存なし、デーモンなし、YAMLなし | `lua` `terminal` | 1 | 2026-08-04 |
| [**herdr-dwm-layout**](https://github.com/42lizard/herdr-dwm-layout)<br><sub>42lizard</sub> | Herdr向けの、DWM風master/stackレイアウト | `dwm` `fzf` `rust` `shell` `tiling` | 1 | 2026-08-28 |
| [**🆕 yeet**](https://github.com/adriankarlen/yeet)<br><sub>adriankarlen</sub> | a minimal sesh style picker inside herdr | `sesh` `session-management` `yeet` `go` | 1 | 🔄 2026-09-25 |
| [**herdr-scm**](https://github.com/dkbo/herdr-scm)<br><sub>dkbo</sub> | herdr プラグイン：現在の herdr ワークスペースに対する、読み取り専用のマルチリポジトリ・ソースコントロール概要パネルです。 | `git` `rust` `terminal` `tui` | 1 | 2026-09-10 |
| [**herdr-medieval**](https://github.com/gabrielbarretoo/herdr-medieval)<br><sub>gabrielbarretoo</sub> | ワークスペースとエージェントを、六角形マスの中世風大陸として3D表示するHerdrプラグイン——各ワークスペースは柵に囲まれた野営地、各ペインは冒険者として、エージェントの状態に応じて訓練したり、キャンプファイアで休んだり、塔で見張りをする。three.js組み込みで、通信・依存関係なし | `3d` `hex-grid` `threejs` `javascript` | 1 | 2026-08-06 |
| [**herdr-opendde-harness**](https://github.com/mrzzmrzz/herdr-opendde-harness)<br><sub>mrzzmrzz</sub> | ddeharness 用の Herdr サイドバー連携です。ネイティブなステータス表示、アニメーション付きのエージェント名、デフォルトレイアウトでの要約を、リモートクライアントも含めて提供します。 | `python` | 1 | 2026-09-10 |
| [**herdr-lastfocus**](https://github.com/pedrobarco/herdr-lastfocus)<br><sub>pedrobarco</sub> | herdr向けの、tmux風の直前フォーカスしていたペイン/タブ/ワークスペースへの切り替え——フォーカスイベント履歴デーモンを介して実現 | `terminal-multiplexer` `tmux` `go` | 1 | 2026-07-25 |
| [**herdr-spinup**](https://github.com/Royal-lobster/herdr-spinup)<br><sub>Royal-lobster</sub> | herdrの新規タブごとに表示されるスタート画面——ツールを選ぶとそのタブで実行される。ツールはJSONで定義 | `javascript` | 1 | 2026-08-04 |
| [**🆕 herdr-plugins**](https://github.com/VladPatr96/herdr-plugins)<br><sub>VladPatr96</sub> | Plugins for Herdr, the terminal workspace manager for AI coding agents | `javascript` | 1 | 🔄 2026-09-22 |
| [**herdr-sesh**](https://github.com/xheisenbugx/herdr-sesh)<br><sub>xheisenbugx</sub> | seshに着想を得た、賢いherdrワークスペースマネージャー | `go` | 1 | 2026-09-09 |
| [**🆕 herdr-ipc**](https://github.com/adihex/herdr-ipc)<br><sub>adihex</sub> | Herdr plugin + Agent Plugin: workspace-scoped Unix-socket IPC for pane workers | `ipc` `python` | 0 | 🔄 2026-09-20 |
| [**🆕 herdr-better-worktrees**](https://github.com/bearylabs/herdr-better-worktrees)<br><sub>bearylabs</sub> | A fast Herdr popup for managing Git worktrees in a predictable embedded-bare layout: create, clone, open, inspect, fetch, and safely remove worktrees while kee… | `typescript` | 0 | 🔄 2026-09-18 |
| [**herdr-yoke**](https://github.com/dgnsrekt/herdr-yoke)<br><sub>dgnsrekt</sub> | get yoked——1キーで2つのタブを並べて表示。herdr版のChromeスプリットビュー | `split-view` `terminal` `shell` | 0 | 2026-08-09 |
| [**🆕 herdr-plugin-dotfiles-dev-layout**](https://github.com/edmundmiller/herdr-plugin-dotfiles-dev-layout)<br><sub>edmundmiller</sub> | 自分のdotfilesの開発用ワークスペースレイアウトを開くためのHerdrプラグイン | `python` | 0 | 2026-06-23 |
| [**🆕 herdr-plugin-workspace-groups**](https://github.com/kwanwooi25/herdr-plugin-workspace-groups)<br><sub>kwanwooi25</sub> | Keyboard-first workspace grouping and colored sidebar badges for Herdr | `python` `terminal` `workspace-manager` | 0 | 🔄 2026-09-20 |
| [**🆕 herdr-menu**](https://github.com/leonardoacosta/herdr-menu)<br><sub>leonardoacosta</sub> | Pane, tab, and workspace management actions for Herdr | `menu` `pane` `tab` `workspace` `shell` | 0 | 🔄 2026-09-16 |
| [**🆕 herdr-pane-id-metadata**](https://github.com/limars874/herdr-pane-id-metadata)<br><sub>limars874</sub> | 正規化されたペインIDと、コンパクトなタブ/ペインのサイドバーメタデータのための、最小構成のHerdrプラグイン | `coding-agents` `terminal` `javascript` | 0 | 2026-08-17 |
| [**herdr-active-agent-jump**](https://github.com/shoaibkhanz/herdr-active-agent-jump)<br><sub>shoaibkhanz</sub> | herdrプラグイン：作業中/ブロック中のエージェントを、レイアウトの順序で前後に巡回してフォーカスする——attention-jumpを補完するvim風の操作 | `javascript` | 0 | 2026-07-12 |

<details><summary>この目的にも関係するもの</summary>

- [andrewchng/herdr-sessionizer](https://github.com/andrewchng/herdr-sessionizer) — プロジェクトやworktreeをファジー検索で開き、宣言的なTOMLレイアウト（タブ・ペイン分割・起動コマンド・リポジトリごとの上書き設定）からワークスペースを立ち上げる
- [fullerzz/herdr-plugin-sesh](https://github.com/fullerzz/herdr-plugin-sesh) — Herdr向けのSesh風ワークスペースピッカーTUI。zoxideと連携し、よく使うディレクトリからワークスペースを作成できる
- [ntindle/herdr-resurrect](https://github.com/ntindle/herdr-resurrect) — herdr版tmux-resurrect——ワークスペース・タブ・ペイン・作業ディレクトリ・実行中のプログラムやエージェントをスナップショットし、クラッシュや再起動後に復元する
- [enekos/herdr-quick-actions](https://github.com/enekos/herdr-quick-actions) — herdr標準のタブ/ペイン/ワークスペース操作を、使用頻度順でfzfから選べる——キーバインドを覚える必要がなくなる
- [salkhalil/herdr-sessionizer](https://github.com/salkhalil/herdr-sessionizer) — herdr版tmux-sessionizer：開いているワークスペースとzoxideのディレクトリをfzfで検索し、テンプレートタブ付きで作成またはフォーカスする
- [crierr/herdr-arrange](https://github.com/crierr/herdr-arrange) — herdrのペイン移動・入れ替え・再分割・レイアウト変更を行う、インタラクティブなポップアップUI
- [aliou/herdr-cast](https://github.com/aliou/herdr-cast) — 個人用Herdrプラグイン——ネイティブmacOS通知、ファジーなワークスペース移動、zoxide連携のワークスペース作成、レイアウトコマンドをまとめて提供
- [chandrasekharan98/herdr-workspace-save](https://github.com/chandrasekharan98/herdr-workspace-save) — Herdrのワークスペース（レイアウト・作業ディレクトリ・エージェントセッション・実行中のコマンド）を保存し、あとでfzfピッカーから再度開ける
- [42lizard/herdr-sessionizer](https://github.com/42lizard/herdr-sessionizer) — tmux-sessionizer風のherdr向けプラグイン

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-navigate"></a>

## ペイン移動・キー操作

> ペインやワークスペース間の移動・リサイズを、エディタと同じキーで済ませたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**vim-herdr-navigation**](https://github.com/paulbkim-dev/vim-herdr-navigation)<br><sub>paulbkim-dev</sub> | Ctrl+h/j/k/lでherdrのペインとVim/Neovimのスプリットをシームレスに移動——vim-tmux-navigatorのherdr版 | `neovim` `vim` `shell` | 108 | 2026-08-23 |
| [**herdr-splits.nvim**](https://github.com/lmilojevicc/herdr-splits.nvim)<br><sub>lmilojevicc</sub> | HerdrとNeovimのスプリットをスマートに移動・リサイズする | `lua` `neovim` `neovim-plugin` `neovim-plugins` `nvim` | 65 | 2026-08-17 |
| [**herdr-floax**](https://github.com/Tyru5/herdr-floax)<br><sub>Tyru5</sub> | herdr向けのフローティング作業用シェル——tmux-floax風に開閉できるポップアップで、ワークスペースごとに1つ、セッションは永続化される | `rust` `terminal` `tmux-floax` | 27 | 2026-07-26 |
| [**herdr-nvim-nav**](https://github.com/aimdevlee/herdr-nvim-nav)<br><sub>aimdevlee</sub> | herdrのペインとNeovimのスプリットをまたいだシームレスなCtrl+h/j/k/l移動——ソケットベースでキー入力ごとのプロセス起動なし | `neovim` `neovim-plugin` `lua` | 19 | 2026-08-02 |
| [**herdr-recent-navigator**](https://github.com/beyondlex/herdr-recent-navigator)<br><sub>beyondlex</sub> | 最近使ったワークスペース・タブ・ペイン・エージェントを MRU（最近使った順）で切り替えられます——JetBrains の「最近使ったファイル」のような感覚です。さらに、任意のペインの内容をあいまい検索でき、すべてキーボードだけで操作できます。 | `agent` `mru` `navigator` `pane` `popup` | 18 | 🔄 2026-09-22 |
| [**herdr-last-workspace**](https://github.com/third774/herdr-last-workspace)<br><sub>third774</sub> | 直前にフォーカスしていたワークスペースに切り替えるプラグイン | `rust` | 18 | 2026-06-22 |
| [**herdr-pane-mover**](https://github.com/osamahbeig/herdr-pane-mover)<br><sub>osamahbeig</sub> | herdr向けのクリック可能なオーバーレイメニュー：タブやワークスペースを横断してペインの移動・再分割・入れ替えができる | `terminal` `tui` `javascript` | 13 | 2026-07-10 |
| [**herdr-cliamp**](https://github.com/coryshaw1/herdr-cliamp)<br><sub>coryshaw1</sub> | 隠しても再生を続ける、herdr向けのフローティングcliamp——プレイヤーはデタッチされたherdrセッション内で動くため、フロートを閉じてもデタッチされるだけで再生は止まらない | `audiobook` `cliamp` `music-player` `podcast` `terminal` | 12 | 2026-08-24 |
| [**herdr-profiles**](https://github.com/GiorgiTarsaidze/herdr-profiles)<br><sub>GiorgiTarsaidze</sub> | Herdr 用の Chrome 風プロファイルです。ポップアップの選択画面から、独立したスペースの集合を切り替えられます。 | `rust` `terminal` | 12 | 🔄 2026-09-14 |
| [**herdr-logbook**](https://github.com/Resetnak/herdr-logbook)<br><sub>Resetnak</sub> | ターミナルのための作業メモリ——オフラインでMarkdown中心のノート、決定事項、Herdr向けの現在タスクnow.mdを管理 | `adr` `bubbletea` `cli` `go` `markdown` | 12 | 2026-09-03 |
| [**herdr-command-center**](https://github.com/speardragon/herdr-command-center)<br><sub>speardragon</sub> | すべてのコマンドを1つのキーバインドで——登録したコマンドを一覧表示するherdrのポップアップ。矢印キーや番号で実行し、コマンド実行前に自動で閉じる | `command-palette` `nodejs` `terminal` `toml` `tui` | 12 | 2026-08-19 |
| [**herdr-equalize-panes**](https://github.com/shibayu36/herdr-equalize-panes)<br><sub>shibayu36</sub> | 分割やクローズのたびにペインサイズを自動的に均等化するherdrプラグイン（tmuxのselect-layout -Eを自動で行うイメージ） | `terminal` `perl` | 11 | 2026-08-22 |
| [**herdr-paddock**](https://github.com/neyham/herdr-paddock)<br><sub>neyham</sub> | 🐑 herdrのエージェント向けカードウォール型フィード——群れ全体をざっと見渡し、1体にズームインして返信できる。すべて素のSSH経由 | `bubbletea` `go` `ssh` `tui` | 9 | 🔄 2026-09-23 |
| [**herdr-trail**](https://github.com/catoncat/herdr-trail)<br><sub>catoncat</sub> | herdr全体で共有するメモ——エージェントがフォローアップを書き留め、人間は1つのグローバルリストで管理し、各エントリから元の会話に直接ジャンプできる | `javascript` | 8 | 2026-08-26 |
| [**herdr-toggle-popup**](https://github.com/maro114510/herdr-toggle-popup)<br><sub>maro114510</sub> | 1つのキーバインドでオーバーレイのポップアップシェルを開閉できるHerdrターミナル向けプラグイン | `go` | 8 | 🔄 2026-09-23 |
| [**herdr-omnisearch**](https://github.com/dmnkf/herdr-omnisearch)<br><sub>dmnkf</sub> | Fast search and navigation for Herdr workspaces, panes, and archived agent sessions across all your connected machines | `python` | 7 | 🔄 2026-09-25 |
| [**herdr-scratch**](https://github.com/AkashJana18/herdr-scratch)<br><sub>AkashJana18</sub> | Herdr向けの永続化されたスクラッチパッド。フローティングのユーティリティペインへの足がかりとなる | `cli` `rust` `scratchpad` | 6 | 🔄 2026-09-20 |
| [**nvim-herdr-navigation**](https://github.com/bojackduy/nvim-herdr-navigation)<br><sub>bojackduy</sub> | vim-tmux-navigator風のctrl+h/j/k/lで、Neovimのスプリットとherdrのペイン間を移動する | `keyboard-shortcuts` `lazyvim` `lua` `navigation` `neovim` | 6 | 2026-07-20 |
| [**herdr-swipe**](https://github.com/husniadil/herdr-swipe)<br><sub>husniadil</sub> | Herdr向けのトラックパッドジェスチャー——ペイン・タブ・スペース間の移動と、対応待ちのエージェントへのジャンプができる | `cgeventtap` `gestures` `macos` `python` `terminal` | 6 | 2026-08-20 |
| [**nvim-herdr-navigator**](https://github.com/kaar/nvim-herdr-navigator)<br><sub>kaar</sub> | Neovimのスプリットとherdrのペインをシームレスに移動——1組の`ctrl+h/j/k/l`でvimとherdrのペインの両方を移動できる | `neovim` `neovim-plugin` `lua` | 6 | 2026-07-29 |
| [**herdr-last**](https://github.com/lmilojevicc/herdr-last)<br><sub>lmilojevicc</sub> | Herdrで直前にアクティブだったワークスペースまたはタブに切り替え戻す | `go` `linux` `macos` `productivity` `tabs` | 6 | 2026-08-07 |
| [**herdr-arrange**](https://github.com/crierr/herdr-arrange)<br><sub>crierr</sub> | herdrのペイン移動・入れ替え・再分割・レイアウト変更を行う、インタラクティブなポップアップUI | `go` | 5 | 2026-09-05 |
| [**herdr-attention**](https://github.com/milkyskies/herdr-attention)<br><sub>milkyskies</sub> | herdrプラグイン：1キーで、注意が必要な次のエージェント（ブロック中、次に完了済み）にフォーカスを移す | `javascript` | 5 | 2026-07-08 |
| [**🆕 herdr-tmux-session-navigator**](https://github.com/caneppelevitor/herdr-tmux-session-navigator)<br><sub>caneppelevitor</sub> | tmux choose-tree for herdr. Written by someone who left tmux but never gave up prefix+s. | `bubbletea` `terminal` `tmux` `go` | 4 | 🔄 2026-09-18 |
| [**herdr-annotations**](https://github.com/jagzmz/herdr-annotations)<br><sub>jagzmz</sub> | Herdr上で選択したターミナルのテキストに、高速なローカルファーストのポップアップと再利用可能なコレクションで注釈を付ける | `annotations` `cli` `coding-agents` `developer-tools` `local-first` | 4 | 2026-07-16 |
| [**herdr-unread-marker**](https://github.com/JoanGil/herdr-unread-marker)<br><sub>JoanGil</sub> | キーバインドでフォーカス中のエージェントを未読/既読にマークする（手動のみ） | `shell` | 4 | 2026-07-17 |
| [**herdr-harpoon**](https://github.com/KonstantinKai/herdr-harpoon)<br><sub>KonstantinKai</sub> | herdr版Harpoon：ペインにマークを付けてインデックスでジャンプする。Bashのみでビルド不要 | `bash` `harpoon` `tmux-harpoon` `shell` | 4 | 2026-07-29 |
| [**herdr-equalize-splits**](https://github.com/markhuot/herdr-equalize-splits)<br><sub>markhuot</sub> | herdrプラグイン：現在のタブ内のすべてのスプリットを、行/列ごとに均等な幅に揃える（Ctrl+b =にバインド） | `terminal` `tmux` `javascript` | 4 | 2026-07-08 |
| [**herdr-smart-nav**](https://github.com/odiumuniverse/herdr-smart-nav)<br><sub>odiumuniverse</sub> | nvim のウィンドウ、herdr のペイン・タブ・ワークスペースを横断する、スマートな Ctrl+h/j/k/l です。 | `navigation` `neovim` `neovim-plugin` `nvim` `nvim-lua` | 4 | 🔄 2026-09-14 |
| [**herdr-pretty-which**](https://github.com/ramarivera/herdr-pretty-which)<br><sub>ramarivera</sub> | Herdr向けの、Rust/Ratatui製which-key風キーバインドオーバーレイ | `ratatui` `rust` `terminal` `tui` `which-key` | 4 | 🔄 2026-09-18 |
| [**herdr-navigator**](https://github.com/willfish/herdr-navigator)<br><sub>willfish</sub> | Vim/Neovimを意識したペイン移動のための、Herdr側のナビゲーション操作 | `navigation` `neovim` `rust` | 4 | 2026-07-07 |
| [**herdr-easyjump**](https://github.com/xzedx/herdr-easyjump)<br><sub>xzedx</sub> | キーを押して文字を入力すれば、任意のスペース・エージェント・ペイン・タブへジャンプできます。EasyMotion・Vimium・vim-choosewin 風のヒントラベルを、Herdr のサイドバーに直接表示します。 | `choosewin` `easymotion` `hints` `navigation` `rust` | 4 | 🔄 2026-09-14 |
| [**herdr-pane-switcher**](https://github.com/AlexanderGrooff/herdr-pane-switcher)<br><sub>AlexanderGrooff</sub> | 優先度の高い Herdr ペインへ、ショートカットで注目を切り替えられます。 | `rust` | 3 | 2026-08-27 |
| [**herdr-voice**](https://github.com/aneym/herdr-voice)<br><sub>aneym</sub> | herdrの音声操作——話しかけるだけでスペース作成・ペイン分割・コーディングエージェントの操作ができる。OpenAI Realtimeを使用し、リアルタイムの文字起こしを表示するフローティングHUD付き | `openai-realtime-api` `voice` `javascript` | 3 | 🔄 2026-09-17 |
| [**herdr-which-key**](https://github.com/CowboyVang/herdr-which-key)<br><sub>CowboyVang</sub> | herdr向けのwhich-key風キーマップオーバーレイ——1キー押すとprefix配下の全バインドがグループ化・ラベル付きで表示され、2つ目のキーで実行できる。長押し表示ではなく明示的な呼び出し方式。依存なし | `keybindings` `terminal` `which-key` `python` | 3 | 🔄 2026-09-15 |
| [**herdr-tmux-layout**](https://github.com/crierr/herdr-tmux-layout)<br><sub>crierr</sub> | 稼働中のHerdrペインに使える、tmux風のプリセットレイアウト——cycle・even-horizontal・even-vertical・main-horizontal・main-vertical・tiled・balanceに対応 | `go` | 3 | 2026-08-30 |
| [**herdr-convo-index**](https://github.com/dzwduan/herdr-convo-index)<br><sub>dzwduan</sub> | herdr内のClaude Codeペイン用のターン索引——過去の任意のターンにジャンプしてポップアップで読める | `python` | 3 | 2026-07-27 |
| [**herdr-popupx**](https://github.com/jeromychu23/herdr-popupx)<br><sub>jeromychu23</sub> | Herdr向けの、永続化されたネイティブのフローティング作業用ポップアップ | `rust` `terminal` `tui` | 3 | 2026-07-21 |
| [**herdr-normal-mode**](https://github.com/maedana/herdr-normal-mode)<br><sub>maedana</sub> | herdrのサイドバー向けのVim風ノーマルモード——j/kで行移動、h/lでタブ移動、0-9でペイン選択 | `rust` `tui` | 3 | 2026-08-24 |
| [**herdr-next-agent**](https://github.com/martin-ro/herdr-next-agent)<br><sub>martin-ro</sub> | Herdrプラグイン：設定可能な優先度に基づいて、注意が必要な次のエージェントにジャンプする | `python` | 3 | 🔄 2026-09-10 |
| [**herdr-float**](https://github.com/meerzulee/herdr-float)<br><sub>meerzulee</sub> | Zellij風のALT+Fで開くフローティングペイン | `shell` | 3 | 2026-07-20 |
| [**herdr-confirm-close-pane**](https://github.com/poweroutlet2/herdr-confirm-close-pane)<br><sub>poweroutlet2</sub> | ペインを閉じる前に確認を求めるherdrプラグイン——tmuxのprefix+xのconfirm-beforeのような動作 | `shell` | 3 | 2026-07-06 |
| [**herdr-mission-control**](https://github.com/vjeantet/herdr-mission-control)<br><sub>vjeantet</sub> | herdr 用のミッションコントロール。1 キーで、ワークスペースの全ペインをタブごとにまとめたライブタイルグリッドとして表示し、選んで切り替えられます。 | `expose` `mission-control` `terminal` `tui` `rust` | 3 | 🔄 2026-09-20 |
| [**herdr-next-agent**](https://github.com/choplin/herdr-next-agent)<br><sub>choplin</sub> | 設定した意味的な状態にあるHerdrエージェント間を移動する | `go` | 2 | 2026-08-24 |
| [**herdr-equalize-vsplit**](https://github.com/devoc09/herdr-equalize-vsplit)<br><sub>devoc09</sub> | 現在のペインを右に分割し、列の幅を均等にするHerdrプラグイン | `go` | 2 | 2026-07-15 |
| [**herdr-easymotion**](https://github.com/elliotekj/herdr-easymotion)<br><sub>elliotekj</sub> | 🦘 Herdrのペイン間を直接ジャンプする | `javascript` | 2 | 2026-07-20 |
| [**herdr-break-pane**](https://github.com/iuhoay/herdr-break-pane)<br><sub>iuhoay</sub> | フォーカス中のペインを新しいタブに移動する、小さなHerdrプラグイン | `pane` `javascript` | 2 | 2026-08-27 |
| [**herdr-prevtab**](https://github.com/joo-was-already-taken/herdr-prevtab)<br><sub>joo-was-already-taken</sub> | 直前にフォーカスしていたタブに切り替えるHerdrプラグイン | `rust` | 2 | 2026-09-08 |
| [**herdr-lazytask**](https://github.com/mdetweil/herdr-lazytask)<br><sub>mdetweil</sub> | herdrのスプリットペインでLazytaskを使う（開く/フォーカス/トグル）ほか、Taskwarriorのクイックアクションも提供 | `lazytask` `taskwarrior` `terminal` `rust` | 2 | 2026-08-02 |
| [**herdr-quotr**](https://github.com/napalmpapalam/herdr-quotr)<br><sub>napalmpapalam</sub> | herdrのポップアップから、エージェント自身の回答を引用してそのエージェントに投げ返す | `claude-code` `rust` `tui` | 2 | 2026-09-01 |
| [**herdr-topstrip**](https://github.com/orcchg/herdr-topstrip)<br><sub>orcchg</sub> | すべてのスペース、または既存スペース上のタブを 2 つのペインで開きます——上部には細いストリップ（ディレクトリ移動・シェルコマンド・git 用）、下部には広いペイン（エージェントとのセッション用）を配置します。 | `shell` | 2 | 🔄 2026-09-15 |
| [**herdr-plugin-agent-attention**](https://github.com/peterwiebe/herdr-plugin-agent-attention)<br><sub>peterwiebe</sub> | 最近ブロックされた、または完了したエージェントへジャンプする Herdr プラグインです。 | `python` | 2 | 2026-09-04 |
| [**herdr-account-switch**](https://github.com/rcosteira79/herdr-account-switch)<br><sub>rcosteira79</sub> | 再認証なしでClaude Code / Codexのログインをホットスワップする。オーバーレイピッカー、次へ切り替えるキーバインド、ペインごとのアカウントバッジ（$acct）を提供 | `python` | 2 | 🔄 2026-09-23 |
| [**herdr-pane-mover**](https://github.com/ronly2460/herdr-pane-mover)<br><sub>ronly2460</sub> | 矢印キーで操作するインタラクティブなピッカーで、Herdrのペインをワークスペース間で移動する | `terminal` `workspace` `shell` | 2 | 2026-08-23 |
| [**herdr-pane-orientation-switcher**](https://github.com/sf1tzp/herdr-pane-orientation-switcher)<br><sub>sf1tzp</sub> | Herdrのスプリットペイン向けの、ワークフロー人間工学 | `shell` | 2 | 2026-07-25 |
| [**herdr-ask-inbox**](https://github.com/speardragon/herdr-ask-inbox)<br><sub>speardragon</sub> | すべてのherdrワークスペースからブロックされたClaudeのAskUserQuestionプロンプトを1つのポップアップに集約し、その場で回答できる。間違ったエージェントに回答を送ってしまう心配もない | `claude-code` `javascript` | 2 | 2026-07-25 |
| [**herdr-unread-jump**](https://github.com/to4iki/herdr-unread-jump)<br><sub>to4iki</sub> | 注意が必要な次のHerdrエージェントペイン（ブロック中、次に完了済み）にジャンプする | `agents` `bash` `shell` | 2 | 2026-08-30 |
| [**herdr-machine-manager**](https://github.com/vika2603/herdr-machine-manager)<br><sub>vika2603</sub> | ポップアップの TUI から、herdr に保存された SSH マシンを管理できます。~/.ssh/config のエイリアスから追加したり、設定を失わずに切断したり、接続先を編集したりできます。 | `bubbletea` `go` `ssh` `ssh-config` `terminal` | 2 | 🔄 2026-09-15 |
| [**herdr-plugin-ide-jump**](https://github.com/agentience/herdr-plugin-ide-jump)<br><sub>agentience</sub> | IDEにすぐ戻れる——フォーカス中のペインのプロジェクトのエディタウィンドウを前面に出す、または絞り込み可能なポップアップから選ぶ。Herdrプラグイン | `python` | 1 | 2026-08-24 |
| [**herdr-hyprland**](https://github.com/aorumbayev/herdr-hyprland)<br><sub>aorumbayev</sub> | Hyprland に着想を得た、herdr 用の操作方法です。 | `ai-agents` `developer-tools` `golang` `hyprland` `keybindings` | 1 | 2026-09-04 |
| [**🆕 asconfirmclose**](https://github.com/asumaran/asconfirmclose)<br><sub>asumaran</sub> | Herdr plugin: close the focused pane, asking first only when a process is running in it | `terminal` `go` | 1 | 🔄 2026-09-20 |
| [**herdr-launch-default-agent**](https://github.com/blauerberg/herdr-launch-default-agent)<br><sub>blauerberg</sub> | Omarchy に着想を得た Herdr 用のデフォルトエージェントワークフローです。お好みの AI エージェントを専用タブでフォーカスまたは起動します。 | `agents` `herdr-integration` `shell` | 1 | 🔄 2026-09-11 |
| [**herdr-scratchpad**](https://github.com/brunohq/herdr-scratchpad)<br><sub>brunohq</sub> | herdr 向けの、タブごとに使える最小限の Markdown スクラッチパッドです。チェックボックス付き ToDo にも対応します。 | `python` `scratchpad` `tui` | 1 | 🔄 2026-09-12 |
| [**herdr-plugin-tiles**](https://github.com/carsonjones/herdr-plugin-tiles)<br><sub>carsonjones</sub> | herdr向けのシンプルなペインマネージャー | `python` | 1 | 2026-06-19 |
| [**🆕 lazyherd**](https://github.com/chriopter/lazyherd)<br><sub>chriopter</sub> | Cockpit over all your Git repos, with a jump into lazygit and Herdr workspaces | `git` `lazygit` `tui` `go` | 1 | 🔄 2026-09-20 |
| [**herdr-notes**](https://github.com/cyperx84/herdr-notes)<br><sub>cyperx84</sub> | Herdr向けの、ワークスペースごとに独立したMarkdownスクラッチノート。Go製 | `bubbletea` `golang` `markdown` `notes` `go` | 1 | 2026-08-16 |
| [**herdr-tab-jump**](https://github.com/cyperx84/herdr-tab-jump)<br><sub>cyperx84</sub> | 任意のキーバインドから、位置で指定した herdr のタブ N にフォーカスします——数字キーの列をタブとワークスペースに割り振れます。 | `shell` | 1 | 2026-09-01 |
| [**herdr-last-tab**](https://github.com/dantehemerson/herdr-last-tab)<br><sub>dantehemerson</sub> | 直前にフォーカスしていたタブに切り替えるプラグイン | `rust` | 1 | 2026-08-12 |
| [**herdr-swipe-linux**](https://github.com/enisbu/herdr-swipe-linux)<br><sub>enisbu</sub> | Linux 版 Herdr 向けのトラックパッドジェスチャー。スワイプでペイン・タブ・スペースを移動し、タップで入力待ちのエージェントへジャンプできます。 | `evdev` `gestures` `gnome` `hyprland` `linux` | 1 | 2026-09-02 |
| [**herdr-nav-history**](https://github.com/jugyo/herdr-nav-history)<br><sub>jugyo</sub> | herdr向けの、ブラウザ風の戻る/進むナビゲーション（ペイン・タブ・ワークスペースのフォーカス履歴を対象） | `javascript` | 1 | 2026-07-12 |
| [**herdr-plan-meter**](https://github.com/JunSeo99/herdr-plan-meter)<br><sub>JunSeo99</sub> | Claude Code と Codex のプラン上限を herdr のタブバーに表示し、詳細はポップアップで確認できます。標準ライブラリのみの Python 1 ファイル、認証情報は読み取り専用です。 | `claude-code` `codex` `rate-limit` `usage` `python` | 1 | 🔄 2026-09-16 |
| [**herdr-plugin-switcher**](https://github.com/KadenThomp36/herdr-plugin-switcher)<br><sub>KadenThomp36</sub> | Ctrlを押しながらTabで、最近使った順にherdrのペインを切り替える。macOS版herdr向けの、Arc/Zen風ペインスイッチャー | `swift` | 1 | 2026-08-21 |
| [**herdr-nvim-aware**](https://github.com/KoalaVim/herdr-nvim-aware)<br><sub>KoalaVim</sub> | herdr向けのNvim対応キーバインド——移動・分割・クローズ・ズームに対応 | `rust` | 1 | 2026-08-20 |
| [**herdr-plugin-last**](https://github.com/m4salah/herdr-plugin-last)<br><sub>m4salah</sub> | tmux風の直前タブ・直前ワークスペースへの移動をHerdrに追加する | `rust` | 1 | 2026-07-30 |
| [**herdr-scratch**](https://github.com/macintacos/herdr-scratch)<br><sub>macintacos</sub> | herdr向けのスクラッチシェル——1つのコード（キーの組み合わせ）で開閉するポップアップ。裏側はtmuxなので、離れたときのまま正確に復元される | `go` | 1 | 2026-08-28 |
| [**herdr-prompt-deck**](https://github.com/matdac12/herdr-prompt-deck)<br><sub>matdac12</sub> | Herdr 用の下部プロンプトバーです。ファイルパス・スニペット・下書きテキストを、フォーカス中のエージェントへ挿入できます。 | `rust` | 1 | 🔄 2026-09-12 |
| [**grove-herdr**](https://github.com/nicksenap/grove-herdr)<br><sub>nicksenap</sub> | Herdr プラグイン：Grove のワークスペース作成ポップアップと、Herdr ワークスペースとのブリッジです。 | `grove` `shell` | 1 | 2026-09-09 |
| [**herdr-touchbar**](https://github.com/omerturhan/herdr-touchbar)<br><sub>omerturhan</sub> | MacBookのTouch Barに作業中・ブロック中のherdrエージェントを表示——タップすると該当タブに直接移動する | `ai-agents` `macos` `touchbar` `swift` | 1 | 🔄 2026-09-14 |
| [**herdr-plugins**](https://github.com/oullin/herdr-plugins)<br><sub>oullin</sub> | Herdr向けの、それぞれ独立してインストールできる、目的に特化したプラグイン集 | `typescript` | 1 | 2026-08-09 |
| [**🆕 herdr-equalize-panes**](https://github.com/ponko2/herdr-equalize-panes)<br><sub>ponko2</sub> | ペインが作成・クローズ・移動・終了するたびに、各タブ内のペインを自動的に均等サイズに保つ | `rust` | 1 | 🔄 2026-09-23 |
| [**🆕 herdr-which-key**](https://github.com/pradyb/herdr-which-key)<br><sub>pradyb</sub> | Neovim-style which-key popup for herdr: press a leader, see the next keys, run herdr actions | `python` | 1 | 🔄 2026-09-21 |
| [**herdr-deck-navigation**](https://github.com/raghu-nandan-bs/herdr-deck-navigation)<br><sub>raghu-nandan-bs</sub> | herdr標準のフラットなワークスペース/タブ/ペインナビゲーターを、スクロールなしで任意のペインに素早くたどり着ける「デッキ」表示に置き換える | `rust` `terminal` `tui` | 1 | 2026-08-24 |
| [**herdr-smartnav**](https://github.com/retroaalto/herdr-smartnav)<br><sub>retroaalto</sub> | 方向を意識したペインナビゲーションを提供するHerdrプラグイン | `go` | 1 | 2026-08-01 |
| [**herdr-edge-nav**](https://github.com/sebcbi1/herdr-edge-nav)<br><sub>sebcbi1</sub> | ペインの端でタブやワークスペースをまたいで移動・リサイズできる、方向指定型のHerdrプラグイン。Neovimのスプリットもシームレスに認識する | `lua` | 1 | 2026-08-12 |
| [**herdr-ferry**](https://github.com/shadowfax92/herdr-ferry)<br><sub>shadowfax92</sub> | 稼働中のHerdrのペインやタブを複数まとめて移動したり、ワークスペースを統合したりできる、Rustネイティブのポップアップ | `productivity` `rust` `terminal` `tui` | 1 | 🔄 2026-09-22 |
| [**herdr-scratch**](https://github.com/shadowfax92/herdr-scratch)<br><sub>shadowfax92</sub> | 非公開のtmuxセッションを裏側で使う、永続化されたペインごとのHerdrスクラッチポップアップ | `neovim` `productivity` `rust` `terminal` `tmux` | 1 | 🔄 2026-09-22 |
| [**herdr-talon**](https://github.com/shadowfax92/herdr-talon)<br><sub>shadowfax92</sub> | 画面に見えているHerdrのターミナル要素に、空間的なキーボードヒントを表示する | `keyboard-navigation` `productivity` `rust` `terminal` `tmux-fingers` | 1 | 🔄 2026-09-22 |
| [**herdr-nav-plus**](https://github.com/shoaibkhanz/herdr-nav-plus)<br><sub>shoaibkhanz</sub> | Ctrl+h/j/k/lでherdrのペインを越えてワークスペースまで移動できるナビゲーション——vimを意識した動作で、両端でループする | `javascript` | 1 | 2026-07-18 |
| [**herdr-clock**](https://github.com/Tyru5/herdr-clock)<br><sub>Tyru5</sub> | herdr 向けの tmux クロックモードです——ブロック文字で大きく表示される時計のポップアップで、現地時刻を示します。任意のキーで閉じられます。 | `rust` `terminal` `tmux` | 1 | 🔄 2026-09-15 |
| [**herdr-hintr**](https://github.com/wraithyy/herdr-hintr)<br><sub>wraithyy</sub> | herdrプラグイン：which-key風のキーバインド・チートシートをポップアップ表示——キーを押すとそのまま実行できる | `shell` | 1 | 2026-08-11 |
| [**🆕 herdr-plugin-echo**](https://github.com/andischerer/herdr-plugin-echo)<br><sub>andischerer</sub> | 1つのペインから、マークした複数のペインにキー入力をブロードキャストするHerdrプラグイン | `typescript` | 0 | 2026-08-23 |
| [**🆕 asgotopr**](https://github.com/asumaran/asgotopr)<br><sub>asumaran</sub> | Herdr plugin: jump to your open GitHub PRs across local repos and worktrees | `go` | 0 | 🔄 2026-09-24 |
| [**🆕 herdr-cwd**](https://github.com/bonanyan/herdr-cwd)<br><sub>bonanyan</sub> | Mirror the focused herdr pane's working directory to the host terminal with OSC 7, so terminal file panels, titles, and new splits follow herdr. | `osc7` `terminal` `javascript` | 0 | 🔄 2026-09-20 |
| [**🆕 herdr-dup-tab**](https://github.com/bonkey/herdr-dup-tab)<br><sub>bonkey</sub> | Herdr プラグイン：フォーカス中のペインで実行しているコマンドを、新しいタブに複製します。 | `shell` | 0 | 2026-09-06 |
| [**🆕 herdr-split-pane**](https://github.com/choplin/herdr-split-pane)<br><sub>choplin</sub> | 呼び出し元が指定したコマンドを、Herdrのスプリットペインで直接開く | — | 0 | 2026-08-24 |
| [**🆕 herdr-auto-claude**](https://github.com/Delitefully/herdr-auto-claude)<br><sub>Delitefully</sub> | Start Claude Code in the first pane of every new herdr space. New tabs and splits stay plain shells. | `claude-code` `shell` | 0 | 🔄 2026-09-23 |
| [**🆕 herdr-agent-numbers**](https://github.com/DillonWall/herdr-agent-numbers)<br><sub>DillonWall</sub> | herdr のエージェントパネルに番号を振り、focus_agent（prefix+1〜9）に対応させます。 | `terminal-multiplexer` `shell` | 0 | 🔄 2026-09-14 |
| [**🆕 herdr-links**](https://github.com/dima-m711/herdr-links)<br><sub>dima-m711</sub> | Herdr と Pi 向けの、セッションに紐づいたナビゲーションリンクです。 | `typescript` | 0 | 🔄 2026-09-13 |
| [**🆕 herdr-terminal-scripts**](https://github.com/Fadi729/herdr-terminal-scripts)<br><sub>Fadi729</sub> | Herdr plugin that runs named Scripts from a popup or numbered slots | `typescript` | 0 | 🔄 2026-09-21 |
| [**🆕 herdr-drover**](https://github.com/followbl/herdr-drover)<br><sub>followbl</sub> | Herdr 用の「牧羊犬」タブスイッチャー。Super+T を押し続けてタブを巡回し、離した位置で切り替わります。 | `linux` `python` | 0 | 2026-09-03 |
| [**herdr-desktop-switcher**](https://github.com/gustavocaiano/herdr-desktop-switcher)<br><sub>gustavocaiano</sub> | Herdr向けの、実験的なmacOSデスクトップ切り替えツール | `rust` | 0 | 2026-08-26 |
| [**herdr-harpoon**](https://github.com/hadeson/herdr-harpoon)<br><sub>hadeson</sub> | herdr向けのHarpoon風ペインマーク：ペインをスロット1〜9にピン留めし、タブやワークスペースを越えて直接ジャンプできる | `harpoon` `pane-navigation` `terminal` `tmux` `python` | 0 | 2026-07-25 |
| [**herdr-agent-nav**](https://github.com/julianbonomini/herdr-agent-nav)<br><sub>julianbonomini</sub> | herdr 向けの、シンプルなエージェントナビゲーションです。 | `javascript` | 0 | 🔄 2026-09-13 |
| [**herdr-last-tab**](https://github.com/k-narusawa/herdr-last-tab)<br><sub>k-narusawa</sub> | _(説明なし)_ | `shell` | 0 | 2026-08-22 |
| [**herdr-hasr**](https://github.com/KazBrekker1/herdr-hasr)<br><sub>KazBrekker1</sub> | Hasr（حصر — 「列挙・完全な集計」の意）——herdr向けのgoto風ポップアップ切り替えツール：エージェント・タブ・スペースの切り替え・リネーム・削除・作成ができ、完了状況もリアルタイムに追跡する | `tui` `go` | 0 | 2026-07-23 |
| [**herdr-focus-attention**](https://github.com/kuwa72/herdr-focus-attention)<br><sub>kuwa72</sub> | Herdr プラグイン：対応が必要なエージェントを順に切り替えて表示します。 | `python` | 0 | 🔄 2026-09-21 |
| [**herdr-pane-balancer**](https://github.com/malone-c/herdr-pane-balancer)<br><sub>malone-c</sub> | ペインの開閉に合わせて、herdrのペインを常に均等なサイズに保つ。スプリットするとフォーカス中のペインが半分になるが、このプラグインがタブ全体を再調整する | `python` | 0 | 2026-08-07 |
| [**🆕 herdr-battery**](https://github.com/morphysh/herdr-battery)<br><sub>morphysh</sub> | Laptop battery status for the herdr tab bar (⚡charging 🔋on-battery 🔌held), plus a health/power details popup. Linux sysfs, zero dependencies. | `battery` `linux` `status-bar` `shell` | 0 | 🔄 2026-09-23 |
| [**herdr-pane-memo**](https://github.com/NakasamaJ/herdr-pane-memo)<br><sub>NakasamaJ</sub> | Herdr 用の、ペインごとのスクラッチパッドメモです。自分で追加したキーバインドから、モーダルポップアップで開けます。非公式のコミュニティ製ヘルパーです。 | `shell` | 0 | 🔄 2026-09-13 |
| [**🆕 nvim-ascii-on-focus**](https://github.com/NathanymousFu/nvim-ascii-on-focus)<br><sub>NathanymousFu</sub> | Switch to a Latin input source when a Herdr pane running Neovim gains focus | `input-method` `macos` `neovim` `shell` | 0 | 🔄 2026-09-18 |
| [**🆕 herdr-schlepr**](https://github.com/saiyajosh/herdr-schlepr)<br><sub>saiyajosh</sub> | 洗練されたポップアップから、実行中の Herdr ペインやタブ全体をワークスペース間で移動できます。 | `terminal` `tui` `typescript` | 0 | 🔄 2026-09-15 |
| [**🆕 tmurdr**](https://github.com/sergiopx/tmurdr)<br><sub>sergiopx</sub> | Herdr で tmux の指の記憶をそのまま使えます。ctrl+space プレフィックスと tmux のキーマップ全体を、あなたの config.toml に適用します。 | `keybindings` `terminal` `tmux` `shell` | 0 | 🔄 2026-09-14 |
| [**🆕 herdr-pane-equalizer**](https://github.com/shanefully-done/herdr-pane-equalizer)<br><sub>shanefully-done</sub> | herdrのペインを均等なサイズにリサイズする。自動でも手動でも実行可能 | `javascript` | 0 | 2026-08-20 |
| [**🆕 herdr-worktrees**](https://github.com/SpaceK33z/herdr-worktrees)<br><sub>SpaceK33z</sub> | Switch, create, and remove Git worktrees from a Herdr popup | `rust` | 0 | 🔄 2026-09-17 |
| [**herdr-jump**](https://github.com/tp6gw94/herdr-jump)<br><sub>tp6gw94</sub> | Herdrのワークスペース・タブ・ペイン・エージェント向けの、キーボードナビゲーション | `javascript` | 0 | 2026-08-16 |
| [**🆕 herdr-focus**](https://github.com/trapple/herdr-focus)<br><sub>trapple</sub> | 次にブロック中/完了したエージェントペインにフォーカスし、ターミナルアプリを最前面に出す。グローバルホットキー付き | `shell` | 0 | 2026-07-19 |
| [**herdr-tab-notes**](https://github.com/yang3kc/herdr-tab-notes)<br><sub>yang3kc</sub> | Herdr のタブごとに、プレーンな Markdown スクラッチパッドを 1 つ用意し、右側の細い分割ペインに切り替えて表示できます。ビルド不要、デーモン不要です。 | `shell` | 0 | 🔄 2026-09-15 |
| [**🆕 herdr-kakoune-popup**](https://github.com/Yukaii/herdr-kakoune-popup)<br><sub>Yukaii</sub> | Herdrネイティブのポップアップで、Kakouneのターミナルコマンドを実行する | `kakoune` `shell` | 0 | 2026-08-20 |
| [**🆕 herdr-plugin-pane-move**](https://github.com/yuloop/herdr-plugin-pane-move)<br><sub>yuloop</sub> | Herdr プラグイン：ショートカットキーでペインを移動します。 | `shell` | 0 | 2026-09-04 |

<details><summary>この目的にも関係するもの</summary>

- [thanhdat77/herdr-navigator](https://github.com/thanhdat77/herdr-navigator) — 1つのファジーナビゲーターから、任意のHerdrのワークスペース・エージェント・プロジェクト・セッション・リモート・ディレクトリ・アクションにジャンプできる
- [speardragon/herdr-plugin-manager](https://github.com/speardragon/herdr-plugin-manager) — ポップアップからherdrのプラグインを管理——インストール・更新・有効/無効化・アンインストール、herdr-pluginマーケットプレイスの閲覧も可能。推奨キー：prefix+p
- [jorge07RD/herdr-ssh-manager](https://github.com/jorge07RD/herdr-ssh-manager) — SSHホストを保存し、Herdr内のファジーポップアップから再接続する——Enterキーでポップアップからそのままsshに渡す
- [karanpatel1993/herdr-nav](https://github.com/karanpatel1993/herdr-nav) — File navigation, code search and jdb debugging inside herdr — fzf, ripgrep and a Java debugger wired into you…
- [purehate/herdr-plugin-picker](https://github.com/purehate/herdr-plugin-picker) — Herdr 用の浮動ポップアップピッカーです——任意のスペース・エージェント・タブ・ペインへジャンプでき、マークした全ペインへ 1 つのコマンドを一斉送信でき、~/.ssh/config からリアルタイムの疎通確認付き…
- [victor-software-house/herdr-stash](https://github.com/victor-software-house/herdr-stash) — Herdrのワークスペースをスタッシュ——エージェントを停止しつつ構成と会話内容は保持し、あとでクリック可能な2カラムポップアップから復元できる
- [bayoudhi/herdr-prayer-times](https://github.com/bayoudhi/herdr-prayer-times) — 次の礼拝時刻とカウントダウンをHerdrのサイドバーに表示——タイムテーブルのポップアップと通知付き
- [black-atom-industries/helm.herdr](https://github.com/black-atom-industries/helm.herdr) — 1つのファジーナビゲーターから、任意のHerdrのワークスペース・エージェント・プロジェクト・セッション・リモート・ディレクトリ・アクションにジャンプできる
- [bearylabs/herdr-better-worktrees](https://github.com/bearylabs/herdr-better-worktrees) — A fast Herdr popup for managing Git worktrees in a predictable embedded-bare layout: create, clone, open, ins…
- [leonho/herdr-idle-panes](https://github.com/leonho/herdr-idle-panes) — herdrプラグイン：アイドル状態のシェルのままになっているペインを確認して閉じる、チェックリスト形式のポップアップ
- [ram4-dev/herdr-notify-center](https://github.com/ram4-dev/herdr-notify-center) — サーバー全体のエージェント通知を、永続化されたポップアップ受信箱でHerdrに提供する
- [shoaibkhanz/herdr-active-agent-jump](https://github.com/shoaibkhanz/herdr-active-agent-jump) — herdrプラグイン：作業中/ブロック中のエージェントを、レイアウトの順序で前後に巡回してフォーカスする——attention-jumpを補完するvim風の操作
- [yojahny55/herdr-space-groups](https://github.com/yojahny55/herdr-space-groups) — herdrプラグイン：Spaceを名前付き・色分けされたグループにまとめる——ピッカーのポップアップ（マウス＋キーボード対応）、サイドバーのグループ見出し、自動並べ替えに対応

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-files"></a>

## ファイル閲覧・エディタ連携

> ペインの中でファイルツリーを開いたり、エディタ側と状態を揃えたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**terminal-code**](https://github.com/zenbu-labs/terminal-code)<br><sub>zenbu-labs</sub> | ターミナルの中で動くVS Code | `cli` `terminal` `vscode` `typescript` | 2068 | 🔄 2026-09-11 |
| [**herdr-file-viewer**](https://github.com/smarzban/herdr-file-viewer)<br><sub>smarzban</sub> | herdr向けのGit対応・読み取り専用ファイルビューア。マウス操作にも対応したキーボード駆動のTUIで、ツリー+コンテンツペインに差分表示・Markdownレンダリング・シンタックスハイライトを提供 | `file-viewer` `git` `ratatui` `rust` `terminal` | 601 | 🔄 2026-09-16 |
| [**herdr-sidebar**](https://github.com/alexarthurs/herdr-sidebar)<br><sub>alexarthurs</sub> | herdr向けのVS Code風サイドバー：ファイルエクスプローラーとGitのソース管理を1つのペインに統合——シンタックスハイライト付きプレビュー、VS Code風の差分表示、GitLens風の詳細パネル、AIによるコミットメッセージ生成 | `git` `ratatui` `rust` `sidebar` `terminal` | 386 | 🔄 2026-09-19 |
| [**ttt**](https://github.com/eugenioenko/ttt)<br><sub>eugenioenko</sub> | TTT Editor（Terminal Text Tool）——ターミナルで動く、VS Code・Zed・Sublime の本物の代替エディタです。GUI のような使い心地の TUI で、単一バイナリ・ゼロコンフィグで動作します。 | `cli` `code-editor` `developer-tools` `diff` `editor` | 329 | 🔄 2026-09-25 |
| [**token**](https://github.com/ThorstenRhau/token)<br><sub>ThorstenRhau</sub> | Neovim のカラースキームで、ターミナル全体向けのコントリビューションテーマも含みます。 | `bat-theme` `delta-theme` `emacs-theme` `fish-theme` `fzf-theme` | 309 | 🔄 2026-09-13 |
| [**herdr-mirror**](https://github.com/nikok6/herdr-mirror)<br><sub>nikok6</sub> | ローカルとリモートのセッションを1つのウィンドウに統合。リモートのherdrサーバーをローカルのサイドバーにミラーしてSSH経由で操作 | `rust` | 243 | 2026-09-06 |
| [**herdr-nvim**](https://github.com/ChmaraX/herdr-nvim)<br><sub>ChmaraX</sub> | Neovimをherdrのワークスペースに完全統合する | `lua` `neovim` `nvim` `nvim-plugin` `rust` | 208 | 🔄 2026-09-21 |
| [**dotfiles**](https://github.com/edmundmiller/dotfiles)<br><sub>edmundmiller</sub> | 自分のdotfilesを常に最新の状態に保つためのもの | `dotfiles` `emacs` `nix-dotfiles` `nixos` `nixos-configuration` | 80 | 🔄 2026-09-25 |
| [**herdr-lazygit**](https://github.com/Crokily/herdr-lazygit)<br><sub>Crokily</sub> | herdrのサイドバーペインでlazygitを実行し、AIによるコミットメッセージ生成にも対応——開くのも、展開するのも、コミットするのも、それぞれ1キーで | `git` `lazygit` `shell` | 35 | 🔄 2026-09-14 |
| [**herdr-agent-progress**](https://github.com/eliasstravik/herdr-agent-progress)<br><sub>eliasstravik</sub> | Agent-reported task progress and activity for the Herdr sidebar | `rust` | 29 | 🔄 2026-09-15 |
| [**herdr-yazi**](https://github.com/speardragon/herdr-yazi)<br><sub>speardragon</sub> | herdrのペイン内でYaziを開く | `shell` | 28 | 2026-08-19 |
| [**herdr-quicklook**](https://github.com/dwarvesf/herdr-quicklook)<br><sub>dwarvesf</sub> | herdr版Quick Look：クリップボード内のパスをオーバーレイでポップアップ表示し、1キーでファイルビューアに切り替えられる | `terminal` `shell` | 12 | 2026-08-26 |
| [**herdr-context.nvim**](https://github.com/makyinmars/herdr-context.nvim)<br><sub>makyinmars</sub> | Neovimからコードを選択またはカーソルを合わせ、稼働中のHerdrエージェントを選んで、構造化されたコンテキストをそのエージェントのプロンプトに（送信せずに）積み込む | `lua` | 12 | 🔄 2026-09-17 |
| [**herdr-git-status**](https://github.com/ezcorp-org/herdr-git-status)<br><sub>ezcorp-org</sub> | herdrプラグイン：スペースごとのgitワーキングツリーの状態（ステージ済み/変更/未追跡/競合）をブランチ名の隣にサイドバー表示する | `rust` | 9 | 2026-08-10 |
| [**herdr-workbench**](https://github.com/azizuysal/herdr-workbench)<br><sub>azizuysal</sub> | Herdr向けの洗練されたプロジェクトサイドバー——エクスプローラー、ファイル/コンテンツのリアルタイム検索、読み取り専用のソース管理、豊富なプレビュー、ファイルアイコン、Git装飾を備える | `rust` | 7 | 🔄 2026-09-19 |
| [**herdr-fresh**](https://github.com/rvalledorjr/herdr-fresh)<br><sub>rvalledorjr</sub> | ターミナルIDEのFreshを、herdrのペイン内でファイルビューア兼エディタとして動かすherdrプラグイン | `developer-tools` `editor` `fresh` `ide` `terminal` | 6 | 2026-07-17 |
| [**advanced-herdr-file-viewer**](https://github.com/thuanlm215/advanced-herdr-file-viewer)<br><sub>thuanlm215</sub> | Git-aware, read-only herdr file viewer: tree, diffs, markdown, syntax, and inline image preview. | `file-viewer` `ripgrep` `rust` `tui` | 6 | 🔄 2026-09-19 |
| [**herdr-markdown-viewer**](https://github.com/arvindparmar-me/herdr-markdown-viewer)<br><sub>arvindparmar-me</sub> | Herdrプラグイン：Markdownファイルのパスをドラッグ選択してprefix+mを押すと、右側のスプリットペインでプレビューできる | `shell` | 5 | 2026-07-17 |
| [**herdr-flist**](https://github.com/devskale/herdr-flist)<br><sub>devskale</sub> | herdr向けのファイル一覧プラグイン | `python` | 5 | 2026-07-10 |
| [**dotfiles**](https://github.com/tifandotme/dotfiles)<br><sub>tifandotme</sub> | ~/.*（ホームディレクトリ配下の設定ファイル） | `aerospace` `chezmoi` `cmux` `dotfiles` `ghostty` | 5 | 🔄 2026-09-25 |
| [**herdr-file-viewer**](https://github.com/ismaelosuna7824/herdr-file-viewer)<br><sub>ismaelosuna7824</sub> | 1つのHerdrペインに収まる、キーボード操作のファイルエクスプローラー・コードビューア・gitクライアント——Go + Bubble Tea製 | `bubbletea` `git` `golang` `tui` `go` | 4 | 2026-08-08 |
| [**herdr-lazygit**](https://github.com/JacquesvanWyk/herdr-lazygit)<br><sub>JacquesvanWyk</sub> | herdrのスプリットペインまたはタブでlazygitを開く。スマートトグル（開く/フォーカス/閉じる）に対応 | `lazygit` `shell` | 4 | 2026-07-12 |
| [**herdr-plugin-mermaid-preview**](https://github.com/Volpestyle/herdr-plugin-mermaid-preview)<br><sub>Volpestyle</sub> | Herdr上でClaude CodeやCodexの出力中のMermaid図をリアルタイムプレビューする | `claude-code` `mermaid` `openai-codex` `terminal` `javascript` | 4 | 2026-07-10 |
| [**openloc.nvim**](https://github.com/Zamua/openloc.nvim)<br><sub>Zamua</sub> | すでにワークスペースに属しているNeovimでファイル参照を開く | `lua` | 4 | 2026-08-25 |
| [**herdr-wait**](https://github.com/cdc-lst/herdr-wait)<br><sub>cdc-lst</sub> | アイドル状態のエージェントペインに、実際に何をしているか（例：'waiting: build-api'、'waiting: codex'）をペインのプロセスツリーから判定してタグ付けする、設定可能なherdrプラグイン | `typescript` | 3 | 2026-07-03 |
| [**herdr-yazi-windows**](https://github.com/Only-Moon/herdr-yazi-windows)<br><sub>Only-Moon</sub> | herdr-yazi のWindows移植版。herdr v0.8以降のネイティブWindowsペイン生成に対応 | `file` `file-manager` `pidotdev` `python` `tui` | 3 | 2026-08-14 |
| [**🆕 herdr-disp-model**](https://github.com/pdalinis/herdr-disp-model)<br><sub>pdalinis</sub> | Display active Codex, Claude Code, Pi, and Hermes models in the Herdr agent sidebar. | `ai-agents` `claude-code` `codex` `developer-tools` `hermes-agent` | 3 | 🔄 2026-09-19 |
| [**herdr-x**](https://github.com/playsthisgame/herdr-x)<br><sub>playsthisgame</sub> | herdr内のターミナルスプリットでx.comを閲覧し、$EDITORで投稿を下書きして自分宛に送信できる | `cli` `terminal` `terminal-browser` `twitter` `shell` | 3 | 2026-08-20 |
| [**herdr-open-in-editor**](https://github.com/timofey-TK/herdr-open-in-editor)<br><sub>timofey-TK</sub> | ローカル・リモートのHerdrワークスペースをVS CodeまたはZedで開く | `vscode` `zed` `python` | 3 | 2026-07-30 |
| [**scp-explorer**](https://github.com/TinocoAI/scp-explorer)<br><sub>TinocoAI</sub> | MobaXterm風のSCPファイルエクスプローラーherdrプラグイン（macOS/Linux/Windowsクロスプラットフォーム対応） | `curses` `file-manager` `scp` `python` | 3 | 2026-09-03 |
| [**herdr-flutter**](https://github.com/ablause/herdr-flutter)<br><sub>ablause</sub> | コーディングエージェントの隣で、稼働中のFlutterアプリを監視・ホットリロード・検査できるherdrサイドバー | `dart` | 2 | 2026-07-27 |
| [**herdr-footprint**](https://github.com/harpal-singh-qp/herdr-footprint)<br><sub>harpal-singh-qp</sub> | Herdr のサイドバーに、スペースごとのディスク使用量とコンテキスト使用量を表示します。 | `python` | 2 | 🔄 2026-09-16 |
| [**herdr-claude-usage-multi**](https://github.com/iamhouser/herdr-claude-usage-multi)<br><sub>iamhouser</sub> | Herdrのサイドバーに表示するClaudeプランの使用状況ゲージ——セッション/週の％、危険度に応じた色変化、リセットまでのカウントダウン、CLAUDE_CONFIG_DIRプロファイルによる複数アカウント対応 | `claude-code` `python` | 2 | 2026-09-04 |
| [**herdr-launcher-pane**](https://github.com/y-hirakaw/herdr-launcher-pane)<br><sub>y-hirakaw</sub> | herdr向けの、ドッキングされたクリック起動用ペイン——Finder/Explorer、VS Code、あるいはワークスペースごとに設定した任意のコマンドを起動できる | `launcher` `launcher-pane` `productivity` `python` | 2 | 2026-08-10 |
| [**herdr-yazi-links**](https://github.com/yakovlevs01/herdr-yazi-links)<br><sub>yakovlevs01</sub> | Herdr からファイルのハイパーリンクを Yazi で開けます。オプションのパッチを当てるとプレーンテキストのパスにも対応します。 | `yazi` `python` | 2 | 🔄 2026-09-24 |
| [**🆕 herdr-agent-icons**](https://github.com/adihex/herdr-agent-icons)<br><sub>adihex</sub> | Herdr plugin: real per-agent logo icons in the sidebar via a generated PUA font | `python` | 1 | 🔄 2026-09-18 |
| [**herdr-cursor-open**](https://github.com/alex-devdone/herdr-cursor-open)<br><sub>alex-devdone</sub> | フォーカス中のherdrペインをCursorまたはVS Codeで開く——Remote-SSH経由のリモートherdrに接続したペインにも対応 | `cursor` `vscode` `shell` | 1 | 2026-09-07 |
| [**herdr-context**](https://github.com/Anthodev/herdr-context)<br><sub>Anthodev</sub> | herdr向けのプロジェクトコンテキストドック——git状態付きのファイルツリーとLLMの会話履歴を、常にエージェントのそばに表示する | `git` `jj` `ratatui` `rust` `sidebar` | 1 | 🔄 2026-09-22 |
| [**🆕 asgoto**](https://github.com/asumaran/asgoto)<br><sub>asumaran</sub> | Tree-style switcher across herdr repos, worktrees and panes | `go` | 1 | 🔄 2026-09-24 |
| [**herdr-jetbrains**](https://github.com/chenyao0910/herdr-jetbrains)<br><sub>chenyao0910</sub> | アクティブなHerdrのワークスペースまたはworktreeを、Rider・WebStorm・IntelliJ IDEA・GoLandで開く | `developer-tools` `git-worktree` `goland` `intellij-idea` `jetbrains` | 1 | 2026-08-30 |
| [**herdr-usage-line**](https://github.com/hanbong5938/herdr-usage-line)<br><sub>hanbong5938</sub> | サブスクリプションのレート制限期間とリセットまでのカウントダウンを、Herdr サイドバーの 1 行で表示します。 | `cli` `usage` `go` | 1 | 🔄 2026-09-10 |
| [**🆕 herdr-tab-git**](https://github.com/hasuwini77/herdr-tab-git)<br><sub>hasuwini77</sub> | Herdr Spacesのサイドバーに、最初のタブではなくアクティブなタブに追従する形でGitのブランチと状態を表示する | `git` `terminal` `tui` `javascript` | 1 | 2026-08-28 |
| [**🆕 herdr-visuals**](https://github.com/hx-w/herdr-visuals)<br><sub>hx-w</sub> | Herdr 向けに、セッション単位で Mermaid・LaTeX・ローカル画像のプレビューを表示します。Kitty のグラフィックプロキシにも対応。 | `javascript` | 1 | 🔄 2026-09-19 |
| [**herdr-file-viewer**](https://github.com/jomarmontuya/herdr-file-viewer)<br><sub>jomarmontuya</sub> | 右側に表示するHerdrのファイルツリープラグイン——ファイルタブ、作業ディレクトリの追従、git装飾、クリック可能なリンクに対応 | `go` | 1 | 2026-07-13 |
| [**herdr-scratchdock**](https://github.com/mvaios/herdr-scratchdock)<br><sub>mvaios</sub> | herdr でコーディングエージェントのスクラッチパッドフォルダを隣にドッキング表示します——リアルタイムのツリー表示、テキスト・画像プレビューを備え、エージェントが作業を始めると自動的に開きます。 | `claude-code` `tui` `python` | 1 | 🔄 2026-09-13 |
| [**herdr-yazi-explorer**](https://github.com/pjs-0457/herdr-yazi-explorer)<br><sub>pjs-0457</sub> | 呼び出したワークスペース内のherdrタブ/スプリットでYaziを開く（🗂 yaziというラベル付き）。終了すると自動的に再起動する | `yazi` `shell` | 1 | 2026-08-13 |
| [**herdr-branch-labels**](https://github.com/poislagarde/herdr-branch-labels)<br><sub>poislagarde</sub> | Herdr サイドバーのブランチラベルを、正規表現で設定可能な形式に整形します。 | `git` `regex` `rust` | 1 | 🔄 2026-09-10 |
| [**herdr-gitui**](https://github.com/Shi1xin/herdr-gitui)<br><sub>Shi1xin</sub> | サイドバーペインでgituiを動かすherdrプラグイン——開閉トグル、展開、ライト/ダークテーマに対応 | `gitui` `python` | 1 | 2026-07-28 |
| [**🆕 herdr-numbered-workspaces**](https://github.com/abrose/herdr-numbered-workspaces)<br><sub>abrose</sub> | herdrのサイドバーの各スペースの先頭に番号を付け、インデックス指定のswitch_workspaceショートカットと対応させる | `shell` | 0 | 2026-07-21 |
| [**🆕 herdr-ctx**](https://github.com/aorumbayev/herdr-ctx)<br><sub>aorumbayev</sub> | herdrのサイドバーペイン向けの、Claudeコンテキストウィンドウ表示 | `typescript` | 0 | 2026-07-21 |
| [**🆕 herdr-zed-follow**](https://github.com/dlwr/herdr-zed-follow)<br><sub>dlwr</sub> | herdr plugin: Zed follows the focused herdr workspace | `zed` `shell` | 0 | 🔄 2026-09-24 |
| [**🆕 herdr-agent-index**](https://github.com/kadaliao/herdr-agent-index)<br><sub>kadaliao</sub> | Show each Herdr agent's panel number in the sidebar, so focus_agent = prefix+alt+1..9 has visible targets. | `sidebar` `terminal` `python` | 0 | 🔄 2026-09-20 |
| [**🆕 herdr-nnn**](https://github.com/linuxing3/herdr-nnn)<br><sub>linuxing3</sub> | herdr内でnnnを開く | `shell` | 0 | 2026-08-04 |
| [**🆕 herdr-space-branch**](https://github.com/unstable-code/herdr-space-branch)<br><sub>unstable-code</sub> | Focus-aware branch and ahead/behind for herdr's spaces sidebar. | `shell` | 0 | 🔄 2026-09-19 |

<details><summary>この目的にも関係するもの</summary>

- [robbyrussell/herdr-ohmyzsh](https://github.com/robbyrussell/herdr-ohmyzsh) — Herdr 用の Oh My Zsh プラグインです。時間のかかるコマンドをサイドバーに表示し、完了通知やシェルヘルパーを提供、さらにキー一つでアイドル中の全ペインの Oh My Zsh をリロードできます。
- [ChmaraX/herdr-gitview](https://github.com/ChmaraX/herdr-gitview) — herdr向けのGitステータス/差分パネル——変更のレビュー、nvimでの編集、ステージ/コミット/破棄をすべてターミナルから行える
- [vonzelle-vzt/herdr-extensions](https://github.com/vonzelle-vzt/herdr-extensions) — herdr向けの小さなVS Code——LSPによる診断・自動補完・リネーム・定義へジャンプに対応した本格エディタに加え、ソース管理・検索・問題一覧・テスト・デバッガ・アプリのライブプレビュー・実行時エラー捕捉・画像貼…
- [edxeth/herdr-pi-tree](https://github.com/edxeth/herdr-pi-tree) — Pi のエージェントをツリー表示するサイドバーです——誰が誰を生成したか、どの worktree がどのブランチか、誰があなたを待っているかが分かります。
- [jsmenzies/mergr](https://github.com/jsmenzies/mergr) — Herdr Spaceのサイドバー行にGitHubプルリクエストの状態を表示する
- [xzedx/herdr-easyjump](https://github.com/xzedx/herdr-easyjump) — キーを押して文字を入力すれば、任意のスペース・エージェント・ペイン・タブへジャンプできます。EasyMotion・Vimium・vim-choosewin 風のヒントラベルを、Herdr のサイドバーに直接表示します。
- [brianh20/herdr-stagr](https://github.com/brianh20/herdr-stagr) — herdr向けのソース管理サイドバー——並列差分表示でステージ・アンステージ・破棄ができる
- [maedana/herdr-whereami](https://github.com/maedana/herdr-whereami) — 今どこにいるかを示すよう、タブを自動でリネームするHerdrプラグイン——gitリポジトリ内なら「リポジトリ名/ブランチ名」のように表示
- [bayoudhi/herdr-prayer-times](https://github.com/bayoudhi/herdr-prayer-times) — 次の礼拝時刻とカウントダウンをHerdrのサイドバーに表示——タイムテーブルのポップアップと通知付き
- [mrzzmrzz/herdr-opendde-harness](https://github.com/mrzzmrzz/herdr-opendde-harness) — ddeharness 用の Herdr サイドバー連携です。ネイティブなステータス表示、アニメーション付きのエージェント名、デフォルトレイアウトでの要約を、リモートクライアントも含めて提供します。
- [ZingerLittleBee/herdr-agent-pins](https://github.com/ZingerLittleBee/herdr-agent-pins) — Herdrのエージェントセッションを、Agentsサイドバーの最上部に永続的にピン留めする
- [azyu/herdr-agent-cli](https://github.com/azyu/herdr-agent-cli) — 各ペインでどの CLI が動いているかを、ランタイムごとに色分けできるサイドバートークンとして表示する Herdr プラグインです。
- [jovylle/herdr-session-title-name](https://github.com/jovylle/herdr-session-title-name) — herdrプラグイン：terminal_title_strippedをタブに永続化する（session_titleだけを上に残し、閉じた後もタブがそれを保持する）
- [jwanga/herdr-plugin-github-status](https://github.com/jwanga/herdr-plugin-github-status) — herdr プラグイン：マイルストーン・issue・PR・Actions といったリアルタイムの GitHub プロジェクトステータスを、サイドバー幅で右側にドッキング表示します。
- [kwanwooi25/herdr-plugin-workspace-groups](https://github.com/kwanwooi25/herdr-plugin-workspace-groups) — Keyboard-first workspace grouping and colored sidebar badges for Herdr
- [limars874/herdr-pane-id-metadata](https://github.com/limars874/herdr-pane-id-metadata) — 正規化されたペインIDと、コンパクトなタブ/ペインのサイドバーメタデータのための、最小構成のHerdrプラグイン
- [mastnacek/pi-herdr-sidebar](https://github.com/mastnacek/pi-herdr-sidebar) — Native Rust Herdr plugin sidebar for the Pi coding agent: status telemetry, live skills, gates — VSA slices i…
- [NathanymousFu/nvim-ascii-on-focus](https://github.com/NathanymousFu/nvim-ascii-on-focus) — Switch to a Latin input source when a Herdr pane running Neovim gains focus
- [ralphilius/herdr-github-metadata](https://github.com/ralphilius/herdr-github-metadata) — Herdr plugin: GitHub metadata for the sidebar — the PR each agent is working on
- [yojahny55/herdr-space-groups](https://github.com/yojahny55/herdr-space-groups) — herdrプラグイン：Spaceを名前付き・色分けされたグループにまとめる——ピッカーのポップアップ（マウス＋キーボード対応）、サイドバーのグループ見出し、自動並べ替えに対応

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-cost"></a>

## トークン・コスト管理

> エージェントがいくら使っているかを見たい / 使用量を削りたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**memex**](https://github.com/nicosuave/memex)<br><sub>nicosuave</sub> | Claude Code・Codex・Pi・OpenCode・GitHub Copilot・Cursorのトランスクリプトを検索。セッションを再開。トークンを記録 | `bm25` `claude-code` `codex-cli` `copilot` `hermes-agent` | 228 | 🔄 2026-09-22 |
| [**llmtrim-herdr**](https://github.com/fkiene/llmtrim-herdr)<br><sub>fkiene</sub> | herdrのトークン代を節約：各エージェントペインのリクエストを圧縮（実測で入力-31%/出力-74%）し、節約額をペインごとのバッジで表示 | `llm-proxy` `llmtrim` `powershell` | 51 | 2026-07-02 |
| [**herdr-agent-usage**](https://github.com/senna-lang/herdr-agent-usage)<br><sub>senna-lang</sub> | Herdrで動作するエージェントのコンテキスト使用量メーターと、プロバイダーのレート制限を表示する | `ai-agents` `claude-code` `codex` `golang` `rate-limiting` | 44 | 🔄 2026-09-22 |
| [**herdr-token-dashboard**](https://github.com/Davidcreador/herdr-token-dashboard)<br><sub>Davidcreador</sub> | Herdrのエージェントペイン向けの、トークン消費量をリアルタイムに表示するダッシュボードと通知 | `ai-agents` `bubbletea` `opencode` `pi-agent` `token-dashboard` | 23 | 🔄 2026-09-14 |
| [**quota**](https://github.com/pinkpixel-dev/quota)<br><sub>pinkpixel-dev</sub> | GitHub Copilot・Codex・Claude Code・Antigravity・Kiro・Grok・Cursor にまたがる AI 利用状況を追跡できる、デスクトップアプリ・VSCode 拡張・Herdr プラグインです。 | `ai-tools` `antigravity` `claude` `codex` `cursor` | 9 | 🔄 2026-09-11 |
| [**herdr-claude-usage**](https://github.com/alejodelosrios/herdr-claude-usage)<br><sub>alejodelosrios</sub> | 使用量を確認するためだけにClaudeのセッションを開く必要はもうない。Claudeプランの使用状況（セッション％｜週％）を常にHerdrのサイドバーに表示し、そのアカウントの全ワークスペースで共有される。Claude Code自身の認証情報を使い/statusと同じ正確な数値を表示——推定値ではなく、追加ログインも… | `claude` `claude-code` `python` | 3 | 2026-07-21 |
| [**herdr-opentab**](https://github.com/hamidi-dev/herdr-opentab)<br><sub>hamidi-dev</sub> | OpenTabによる、エージェントごとのAI利用料をHerdrのサイドバーにリアルタイム表示する | `ai-agents` `opentab` `terminal` `python` | 3 | 🔄 2026-09-11 |
| [**🆕 herdr-ctx-bar**](https://github.com/pdalinis/herdr-ctx-bar)<br><sub>pdalinis</sub> | Color-coded context-window usage bars for Codex, Claude Code, Pi, and Hermes Agent in Herdr's Agents sidebar. | `ai-agents` `claude-code` `codex` `context-window` `hermes-agent` | 3 | 🔄 2026-09-19 |
| [**herdr-grazr**](https://github.com/wazum/herdr-grazr)<br><sub>wazum</sub> | シンプルで信頼できる Claude Code 用のアカウント自動切り替えツールです。5 時間または週次のレート制限に達する前に別アカウントへローテーションし、使用量上限でペインが止まることをなくします。Herdr プラグインです。 | `account-rotation` `account-switcher` `account-switching` `anthropic` `claude` | 3 | 🔄 2026-09-25 |
| [**herdr-gekiatsu-plugin**](https://github.com/yuuta1219/herdr-gekiatsu-plugin)<br><sub>yuuta1219</sub> | herdrプラグイン：Claude Codeの使用量カウンターを、パチスロ風にしたもの。大当たり確率1/99、毎日10:00 JSTにリセット | `claude` `claude-code` `python` `tui` | 3 | 2026-08-17 |
| [**herdr-api-credit-bar**](https://github.com/CristianPeralta/herdr-api-credit-bar)<br><sub>CristianPeralta</sub> | herdrプラグイン：従量課金制APIプロバイダーの残クレジットを表示する。まずはAlibaba Cloud Model Studioに対応 | `shell` | 2 | 2026-09-05 |
| [**herdr-quota**](https://github.com/kvkenyon/herdr-quota)<br><sub>kvkenyon</sub> | Herdr上で、Claude・Codex・Cursor・Kimiのサブスクリプション枠を一目で確認できる | `ai-tools` `claude-code` `cursor` `developer-tools` `kimi` | 2 | 2026-09-05 |
| [**herdr-whereami**](https://github.com/maedana/herdr-whereami)<br><sub>maedana</sub> | 今どこにいるかを示すよう、タブを自動でリネームするHerdrプラグイン——gitリポジトリ内なら「リポジトリ名/ブランチ名」のように表示 | `rust` | 2 | 🔄 2026-09-14 |
| [**quota-deck**](https://github.com/ArtMoreno/quota-deck)<br><sub>ArtMoreno</sub> | quota-deck：Windows・macOS・Linux 上の Herdr で、認証情報単位の AI クォータとコンテキストを表示します。 | `rust` | 1 | 🔄 2026-09-22 |
| [**🆕 herdr-usage**](https://github.com/kalbhor/herdr-usage)<br><sub>kalbhor</sub> | herdr plugin that shows coding-agent subscription usage (Claude Code) | `python` | 1 | 🔄 2026-09-17 |
| [**scopefuel**](https://github.com/mgh3326/scopefuel)<br><sub>mgh3326</sub> | AIコーディングエージェントのプラン向けの、範囲を意識した残量ゲージ——実際に何（アカウント/モデル/グループ）がブロックされているか、いつ回復するかが分かる | `ai-agents` `antigravity` `claude-code` `cli` `codex` | 1 | 🔄 2026-09-25 |
| [**🆕 herdr-opencodex**](https://github.com/nordz0r/herdr-opencodex)<br><sub>nordz0r</sub> | OpenCodex Herdr plugins: spend stats and remaining 5h/7d quota | `opencodex` `quota` `rust` | 1 | 🔄 2026-09-23 |
| [**herdr-model-lanes**](https://github.com/terry-li-hm/herdr-model-lanes)<br><sub>terry-li-hm</sub> | herdrプラグイン：Codex・Claude Max・Grokのクォータをワークスペース行に表示し、新規エージェント向けにクォータを考慮したモデルクラスのレーン（ag）も提供する | `claude` `codex` `grok` `model-routing` `quota` | 1 | 2026-08-30 |
| [**🆕 herdr-agent-cli**](https://github.com/azyu/herdr-agent-cli)<br><sub>azyu</sub> | 各ペインでどの CLI が動いているかを、ランタイムごとに色分けできるサイドバートークンとして表示する Herdr プラグインです。 | `coding-agents` `developer-tools` `terminal` `python` | 0 | 🔄 2026-09-11 |
| [**herdr-usage**](https://github.com/Efeguclu1/herdr-usage)<br><sub>Efeguclu1</sub> | Claude・Codex・Cursor・OpenCode・Pi向けの、Herdrエージェントタブ上のコンパクトなアカウント使用量表示 | `claude-code` `cursor` `openai` `opencode` `python` | 0 | 2026-08-22 |
| [**herdr-tokenlens**](https://github.com/KeithMoc/herdr-tokenlens)<br><sub>KeithMoc</sub> | AI コーディングエージェントの継続コストと、コンパクト化による損益分岐点をリアルタイムに表示する herdr ペインです。 | `ai-agents` `claude-code` `llm-cost` `tui` `python` | 0 | 2026-09-04 |
| [**herdr-plugin-agent-quota**](https://github.com/kwanwooi25/herdr-plugin-agent-quota)<br><sub>kwanwooi25</sub> | Herdr向けのエージェントクォータ——Claude Code・Codex・Grok向けのトークン＆コストダッシュボード、サイドバーのクォータゲージ、タブバーのサマリーを提供 | `javascript` | 0 | 2026-08-30 |
| [**provider-usage**](https://github.com/ryus1234/provider-usage)<br><sub>ryus1234</sub> | Herdr 用の、プロバイダーの使用量とクォータを表示するバーです。 | `ai-usage` `quota-monitor` `rust` | 0 | 2026-08-31 |
| [**herdr-usage-bar**](https://github.com/silverwolfdoc/herdr-usage-bar)<br><sub>silverwolfdoc</sub> | Herdr内のAIエージェント向けの使用量上限とコンテキストメーターを、コンパクトな下部の使用量バーで表示する | `go` | 0 | 🔄 2026-09-24 |
| [**🆕 claude-usage**](https://github.com/yuuta1219/claude-usage)<br><sub>yuuta1219</sub> | herdrプラグイン：Claude Codeの使用率（セッション%/週%）をサイドバー下部に常時表示する | `claude` `claude-code` `python` `tui` | 0 | 2026-08-01 |

<details><summary>この目的にも関係するもの</summary>

- [ThorstenRhau/token](https://github.com/ThorstenRhau/token) — Neovim のカラースキームで、ターミナル全体向けのコントリビューションテーマも含みます。
- [levi-qiao/herdr-agent-usage](https://github.com/levi-qiao/herdr-agent-usage) — Credential-scoped AI usage, context, and cache in Herdr for Claude, Codex, Grok, Agy, OpenCode, Pi, omp, Devi…
- [VHemanth45/herdr_agents_tracker](https://github.com/VHemanth45/herdr_agents_tracker) — Herdr plugin that shows your AI subscription usage: account limits in the tab bar, a context meter per agent,…

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-monitor"></a>

## 監視・ダッシュボード

> エージェントやマシンの状態を一覧で眺めたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**zoetrope**](https://github.com/furkankly/zoetrope)<br><sub>furkankly</sub> | Claude Code や Codex のセッションを、ターミナルまたはブラウザでライブのフローグラフとして眺められます。 | `agent-visualization` `claude-code` `codex` `coding-agents` `flow` | 945 | 🔄 2026-09-15 |
| [**clauth**](https://github.com/uwuclxdy/clauth)<br><sub>uwuclxdy</sub> | Claude Codeのマルチアカウント管理・使用量モニター（CLI・TUI・MCPによるクロスアカウント委任に対応） | `account-manager` `account-switcher` `anthropic` `claude` `claude-code` | 219 | 🔄 2026-09-24 |
| [**🆕 herdr-agent-usage**](https://github.com/levi-qiao/herdr-agent-usage)<br><sub>levi-qiao</sub> | Credential-scoped AI usage, context, and cache in Herdr for Claude, Codex, Grok, Agy, OpenCode, Pi, omp, Devin, Muse, and Cursor. | `agent-usage` `ai-agents` `antigravity` `claude-code` `codex` | 140 | 🔄 2026-09-24 |
| [**herdr-radar**](https://github.com/hhdebb/herdr-radar)<br><sub>hhdebb</sub> | Who's working, who's waiting on you — grouped by project, each agent in its vendor's logo and colour. Worktrees nest under their repo, rows order by activity,… | `claudecode` `codex-cli` `coding-agents-plugins` `developer-tools-ai-agent` `terminal-multiplexers` | 89 | 🔄 2026-09-24 |
| [**herdr-beads**](https://github.com/miiraheart/herdr-beads)<br><sub>miiraheart</sub> | herdr向けのbeads (bd) タスクボード：bdのissueをリスト・テーブル・カンバンで表示し、サイドバーまたはフローティングで表示できる | `bd` `beads` `kanban` `rust` `tui` | 30 | 2026-08-25 |
| [**herdr-pc-ram-and-cpu-usage-overlay**](https://github.com/ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay)<br><sub>ezcorp-org</sub> | herdrプラグイン：スペース（ワークスペース）ごとのCPU/RAM使用率を、マシン全体に対する割合としてリアルタイム表示 | `rust` | 20 | 🔄 2026-09-13 |
| [**🆕 captains-deck**](https://github.com/Enk1do/captains-deck)<br><sub>Enk1do</sub> | Captain's Deck - a read-only Firstmate flow kanban plugin for Herdr | `firstmate` `python` | 17 | 🔄 2026-09-24 |
| [**herdr-f1**](https://github.com/hmu332233/herdr-f1)<br><sub>hmu332233</sub> | Herdrのエージェント向けの、F1風ダッシュボード | `agent-dashboard` `typescript` | 15 | 2026-09-10 |
| [**herdr-shell-progress**](https://github.com/bayoudhi/herdr-shell-progress)<br><sub>bayoudhi</sub> | herdrプラグイン：コーディングエージェントに限らず、時間のかかるシェルコマンドの進行状況もサイドバーにリアルタイム表示する | `rust` | 13 | 🔄 2026-09-23 |
| [**herdr-telemetry**](https://github.com/DIodide/herdr-telemetry)<br><sub>DIodide</sub> | ワークスペースとエージェントのテレメトリを自分で管理するエンドポイントにストリーミングするHerdrプラグイン——Go製の単一バイナリ、プライバシー重視のデフォルト設定 | `golang` `telemetry` `go` | 12 | 2026-07-10 |
| [**herdres**](https://github.com/luminexord/herdres)<br><sub>luminexord</sub> | Tendwireを利用した、Herdrのコーディングエージェントを監視・メッセージ送信できるTelegramインターフェース | `coding-agents` `telegram` `python` | 11 | 2026-08-09 |
| [**shepherd**](https://github.com/ryonakae/shepherd)<br><sub>ryonakae</sub> | Herdr管理下のコーディングエージェント向けの、ワーカー監視デーモンとランタイムブリッジ | `pi-coding-agent` `pi-extension` `typescript` | 11 | 2026-08-28 |
| [**🆕 herdr-lcars**](https://github.com/jlcases/herdr-lcars)<br><sub>jlcases</sub> | Command up to 2,000 Herdr AI agents from one LCARS bridge, track Claude/Codex quota per account, and hand off verified context without losing work. | `agent-observability` `ai-agents` `claude-code` `lcars` `openai-codex` | 9 | 🔄 2026-09-22 |
| [**herdr-sysmon**](https://github.com/getpipher/herdr-sysmon)<br><sub>getpipher</sub> | Herdrのサイドバーにシステムメトリクスを表示——CPU・メモリ・バッテリー・ネットワーク・ディスク・時計。tmux-cpu/tmux-battery/tmux-online-statusのステータスバーを、Herdrのワークスペーストークンに忠実に移植したもの。macOS優先対応 | `battery` `catppuccin` `cpu` `getpipher` `macos` | 7 | 2026-07-26 |
| [**herdr-tally**](https://github.com/jasonrr/herdr-tally)<br><sub>jasonrr</sub> | あなたとエージェントのための、プロジェクト単位のTodoとスクラッチパッド<br>📝 プロジェクト単位の TODO 管理 | `rust` `todo` | 7 | 🔄 2026-09-22 |
| [**herdr-workboard**](https://github.com/Phoobobo/herdr-workboard)<br><sub>Phoobobo</sub> | herdr向けのカンバン式ワークボードTUI：ボード＝ワークスペース、タスクの状態＝タブ、タスクのセッション＝ペインという構造 | `kanban` `tui` `typescript` | 7 | 2026-08-10 |
| [**herdr-devserver-status**](https://github.com/Razz21/herdr-devserver-status)<br><sub>Razz21</sub> | プラグイン可能な仕様に基づいてペイン内のdevサーバーを検出し、ライフサイクルの状態を報告するHerdrプラグイン | `astro` `cli` `deamon` `dev-server` `extensible` | 7 | 2026-08-25 |
| [**herdr-lazydocker**](https://github.com/sudoeren/herdr-lazydocker)<br><sub>sudoeren</sub> | herdrのスプリットペインまたは専用タブでlazydockerを実行する | `docker` `lazydocker` `shell` | 6 | 2026-08-27 |
| [**herdr-kanban**](https://github.com/KokiKono/herdr-kanban)<br><sub>KokiKono</sub> | タスクをherdrのタブに紐付けるターミナル上のカンバンボード。SQLiteに保存される | `rust` | 5 | 2026-07-10 |
| [**herdr-agent-watcher**](https://github.com/winoooops/herdr-agent-watcher)<br><sub>winoooops</sub> | Herdr向けのコーディングエージェント可観測性——ライブなサイドバーカード、ライフサイクル通知、設定不要のClaude Codeメトリクスブリッジを提供する | `claude-code` `rust` | 5 | 🔄 2026-09-21 |
| [**herdr-portal**](https://github.com/loofare/herdr-portal)<br><sub>loofare</sub> | herdr向けのミッションコントロールダッシュボード——全ワークスペース/タブ/ペインのエージェントを、ライブTUIカンバン（キーボード＋マウス対応）とWeb大画面表示に集約する。構造化された進捗表示、Ctrl+B Aで起動、クリックでジャンプ、ブラウザからエージェントに返信可能 | `agent-dashboard` `agent-monitor` `ai-agents` `claude-code` `codex` | 4 | 2026-08-20 |
| [**herdr-codex-bridge**](https://github.com/ardasevinc/herdr-codex-bridge)<br><sub>ardasevinc</sub> | 一元化されたアプリサーバーを使い、Codex セッションに Herdr ネイティブのペイン識別情報を割り当てます。 | `ai-agents` `codex` `terminal` `go` | 3 | 🔄 2026-09-13 |
| [**herdr-mise**](https://github.com/funsaized/herdr-mise)<br><sub>funsaized</sub> | プロンプトではなく、パス（成功）を積み重ねよう 🧑‍🍳 herdr 上でエージェントを可視化するツールです。意図的に小さなフットプリントに抑えています。 | `agent` `agent-monitoring` `ai-agents` `cli-tool` `developer-tools` | 3 | 🔄 2026-09-25 |
| [**shepherd**](https://github.com/jwarykowski/shepherd)<br><sub>jwarykowski</sub> | あなたのTodoを群れとしてまとめる | `cli` `developer-tools` `go-lang` `productivity` `task-management` | 3 | 2026-08-21 |
| [**herdr-jcode**](https://github.com/leonardoacosta/herdr-jcode)<br><sub>leonardoacosta</sub> | Jcode の working/idle というライフサイクル状態とセッション識別情報を報告する、独立した Herdr プラグインです。独自実装のため、フォークへの依存はありません。 | `jcode` `rust` | 3 | 🔄 2026-09-16 |
| [**herdr-ports**](https://github.com/Numbered-com/herdr-ports)<br><sub>Numbered-com</sub> | herdrで稼働中の開発サーバーを可視化：TCPリスナーが1つ以上動いているすべてのスペースに$portsバッジを表示する | `kill` `pids` `ports` `processes` `space` | 3 | 🔄 2026-09-19 |
| [**herdr-slurm**](https://github.com/quan-meng/herdr-slurm)<br><sub>quan-meng</sub> | Slurmのアロケーション向けに、Herdrのワークスペースと監視付きエージェントタブを作成する | `hpc` `slurm` `terminal-multiplexer` `python` | 3 | 2026-08-13 |
| [**herdr-status-ui-bar**](https://github.com/speardragon/herdr-status-ui-bar)<br><sub>speardragon</sub> | herdrのタブバーに、AIエージェントのプラン使用量ゲージ（Claude Code / Codex / Grok）を表示する | `claude-code` `codex` `grok` `python` `tab-bar` | 3 | 🔄 2026-09-21 |
| [**herdr-mem-cpu-load**](https://github.com/thewtex/herdr-mem-cpu-load)<br><sub>thewtex</sub> | herdr 用の CPU・メモリ・ロードアベレージモニターです。 | `rust` | 3 | 2026-09-07 |
| [**herdr-agent-state**](https://github.com/Tyru5/herdr-agent-state)<br><sub>Tyru5</sub> | herdr向けのリアルタイムエージェント状態ペイン——ワークスペース内の各エージェントが何をしているかを、より人間に読みやすい形式で表示する | `claude-code` `rust` `terminal` | 3 | 🔄 2026-09-22 |
| [**adlc-herdr**](https://github.com/voodootikigod/adlc-herdr)<br><sub>voodootikigod</sub> | ADLC向けのherdrプラグイン——ペインごとのフェーズ/チケット/ゲートの状態、バックログボード、ゲートアクション、adlc-fleetの実行状況の可視化に対応。voodootikigod/adlc/plugins/adlc-herdrの自動同期ミラー | `javascript` | 3 | 🔄 2026-09-23 |
| [**herdr-claude-usage**](https://github.com/anyaachan/herdr-claude-usage)<br><sub>anyaachan</sub> | Herdr でグローバルな Claude Code プランの使用状況を確認できます。タブバーでの要約表示とポップアップダッシュボードを備え、statusLine を利用してマルチアカウントにも対応します。 | `claude` `claude-code` `cli` `terminal` `shell` | 2 | 2026-09-01 |
| [**herdr-cache-timer**](https://github.com/ArteenHD/herdr-cache-timer)<br><sub>ArteenHD</sub> | 各エージェントのプロンプトキャッシュがいつ失効するかを、Herdrのサイドバーに直接表示する | `claude-code` `prompt-caching` `terminal` `javascript` | 2 | 2026-08-08 |
| [**herdr-agent-dashboard**](https://github.com/carsonjones/herdr-agent-dashboard)<br><sub>carsonjones</sub> | prefix+aでherdrのエージェント一覧を表示する | `typescript` | 2 | 2026-07-16 |
| [**herdr-telemetry-bridge**](https://github.com/CodyBontecou/herdr-telemetry-bridge)<br><sub>CodyBontecou</sub> | ローカルのワークスペース・リポジトリ・コーディングエージェント・モデル・トレースのテレメトリを外部クライアントにストリーミングするHerdrプラグイン | `coding-agents` `telemetry` `time-md` `javascript` | 2 | 2026-06-26 |
| [**herdr-agentsview**](https://github.com/cpcloud/herdr-agentsview)<br><sub>cpcloud</sub> | AgentsViewのアクティビティを、1つの非常に賑やかなターミナルに凝縮して表示する | `rust` | 2 | 2026-08-24 |
| [**herdr-spinner**](https://github.com/hasuwini77/herdr-spinner)<br><sub>hasuwini77</sub> | 作業中状態のHerdrペインに、表示専用のペインメタデータ経由でアニメーションする点字スピナーを表示する | `ai-agents` `claude-code` `herdr-theme` `spinner` `terminal` | 2 | 🔄 2026-09-25 |
| [**herdr-statusline**](https://github.com/iiii1224/herdr-statusline)<br><sub>iiii1224</sub> | herdrセッション向けのカスタマイズ可能なステータスライン | `cli` `statusbar` `statusline` `tmux` `python` | 2 | 2026-08-15 |
| [**herdr-jira-board**](https://github.com/kiitosu/herdr-jira-board)<br><sub>kiitosu</sub> | herdr内で動くJiraカンバンボード。Claude Codeセッションランチャー付き | `python` | 2 | 2026-09-08 |
| [**herdr-tasks**](https://github.com/MatheusBBarni/herdr-tasks)<br><sub>MatheusBBarni</sub> | Herdr 用のカンバンタスクランナーです。OpenTUI 製のボードと htasks CLI を備えます。 | `typescript` | 2 | 🔄 2026-09-11 |
| [**herdr-cache-ttl**](https://github.com/nytafar/herdr-cache-ttl)<br><sub>nytafar</sub> | herdrプラグイン：エージェントのペインごとに、プロンプトキャッシュのTTLをリアルタイムでカウントダウン表示する | `rust` | 2 | 2026-08-05 |
| [**herdr-ports**](https://github.com/randomradio/herdr-ports)<br><sub>randomradio</sub> | Herdr plugin: forward a remote workspace port to http://herdr.{workspace}.localhost:{port} | `rust` | 2 | 🔄 2026-09-20 |
| [**herdr-tilt**](https://github.com/the-inconvenience-store/herdr-tilt)<br><sub>the-inconvenience-store</sub> | Herdr向けの、キーボード操作対応Tiltダッシュボード | `k8s` `kubernetes` `tilt` `rust` | 2 | 2026-08-24 |
| [**🆕 herdr_agents_tracker**](https://github.com/VHemanth45/herdr_agents_tracker)<br><sub>VHemanth45</sub> | Herdr plugin that shows your AI subscription usage: account limits in the tab bar, a context meter per agent, low-limit alerts and a token dashboard for Claude… | `chatgpt` `claude` `claude-code` `codex` `herdr-integration` | 2 | 🔄 2026-09-24 |
| [**herdr-memex-analytics**](https://github.com/vishnutskumar/herdr-memex-analytics)<br><sub>vishnutskumar</sub> | herdrプラグイン：memexの履歴を活用した、セッション効率の分析とリアルタイムなエージェントガイダンス | `rust` | 2 | 2026-09-01 |
| [**herdr-docker**](https://github.com/abcxff/herdr-docker)<br><sub>abcxff</sub> | herdrでエージェントを追跡するのと同じように、dockerのビルドも追跡する | `docker` `javascript` | 1 | 2026-08-12 |
| [**herdr-muse**](https://github.com/akshat12/herdr-muse)<br><sub>akshat12</sub> | Muse Code 用の Herdr 連携。ライフサイクルフックを通じて、ペインの idle・working・blocked 状態を取得します（Herdr のフォークは不要）。 | `ai-agents` `cli` `coding-agents` `muse-code` `terminal` | 1 | 🔄 2026-09-12 |
| [**herdr-glance**](https://github.com/arvmaan/herdr-glance)<br><sub>arvmaan</sub> | エージェントの状態を確認できる、デスクトップウィジェット | `rust` | 1 | 2026-09-08 |
| [**herdr-tokscale-dashboard**](https://github.com/astkaasa/herdr-tokscale-dashboard)<br><sub>astkaasa</sub> | TokscaleをローカルのHerdrダッシュボードペインとして開く | `dashboard` `tokscale` `shell` | 1 | 2026-06-26 |
| [**herdr-nodejs-center**](https://github.com/AZenking/herdr-nodejs-center)<br><sub>AZenking</sub> | ローカルのNode.js・Bun・Denoサービスを監視し、フォーカスできるHerdrのポップアップ | `developer-tools` `nodejs` `javascript` | 1 | 2026-08-20 |
| [**herdr-plugin-codex-subs**](https://github.com/benkraus/herdr-plugin-codex-subs)<br><sub>benkraus</sub> | CLIProxyAPIのCodexサブスクリプション枠とリセットクレジットを表示するHerdrダッシュボード | `go` | 1 | 2026-07-30 |
| [**tsk**](https://github.com/chrisg32/tsk)<br><sub>chrisg32</sub> | tsk——TaskPaper/PlainTasks 風のプレーンテキストタスク管理 TUI で、Rust で書かれています。単体でも herdr プラグインとしても動作します。 | `rust` `taskpaper` `todo` `tui` | 1 | 2026-09-03 |
| [**herdr-model-badge**](https://github.com/dkbo/herdr-model-badge)<br><sub>dkbo</sub> | herdr プラグイン：エージェントサイドバーに、各エージェントのモデルと推論エフォートを表示します。 | `ai-agents` `terminal` `tui` `python` | 1 | 2026-09-08 |
| [**herdr-overview**](https://github.com/iamgp/herdr-overview)<br><sub>iamgp</sub> | Herdr向けのMission Control / Exposé——全spaceをタイル状に並べたライブ一覧 | `terminal` `tui` `javascript` | 1 | 2026-08-28 |
| [**herdr-ports**](https://github.com/ivorpad/herdr-ports)<br><sub>ivorpad</sub> | herdrプラグイン：待受中のポートを一覧表示し、それぞれの背後にあるプロジェクト名を示し、終了または開くことができるポップアップ | `tui` `python` | 1 | 2026-08-27 |
| [**herdr-metrics**](https://github.com/jordanhawkes/herdr-metrics)<br><sub>jordanhawkes</sub> | Claude Code・Codex・TraeX向けの、コンテキスト・セッショントークン・アカウント上限のメトリクスをHerdrのサイドバーに表示する。szrenwei/herdr-agent-metricsのメンテナンスを引き継いだもの | `claude-code` `openai-codex` `traex` `tui` `python` | 1 | 2026-08-22 |
| [**🆕 diskzap**](https://github.com/longwind48/diskzap)<br><sub>longwind48</sub> | Agent skill, Rust CLI and herdr plugin that reclaims GBs of regenerable package caches, build artifacts and Docker cruft. Gated deletion from an explicit catal… | `agent-skills` `ai-agents` `cache` `claude-code` `cleanup` | 1 | 🔄 2026-09-21 |
| [**herdr-compose**](https://github.com/mattyan1053/herdr-compose)<br><sub>mattyan1053</sub> | docker compose向けのHerdrプラグイン | `terminal` `tui` `shell` | 1 | 2026-07-24 |
| [**herdr-pulse**](https://github.com/moneycaringcoder/herdr-pulse)<br><sub>moneycaringcoder</sub> | herdr向けの、ワークスペースごとのエージェント活動履歴——サイドバーのスパークラインとして表示する | `monitoring` `rust` `sparkline` `terminal` | 1 | 2026-09-01 |
| [**🆕 herdr-observr**](https://github.com/nabutabu/herdr-observr)<br><sub>nabutabu</sub> | A telemetry daemon subscribed to Herdr's live event stream that tracks agent runtime health, where agents are stuck, how long they wait for a human, how much c… | `go` | 1 | 🔄 2026-09-22 |
| [**omarchy-crook**](https://github.com/parker-brown-family/omarchy-crook)<br><sub>parker-brown-family</sub> | Crook——どのコーディングエージェントがあなたを必要としているかを Omarchy バーに表示します。何かがあなたを待った瞬間にアイコンが緊急表示に変わり、トレイにはどのエージェントかが表示されます。 | `agents` `bar-widget` `claude-code` `hyprland` `omarchy` | 1 | 2026-09-07 |
| [**herdr-readpending**](https://github.com/rcosteira79/herdr-readpending)<br><sub>rcosteira79</sub> | まだ読み終えていないエージェントにマークを付ける。番号付きバッジ（$read）＋並べ替え可能なリストペインを提供。そのエージェントにフォーカスすると自動でクリアされる | `python` | 1 | 🔄 2026-09-15 |
| [**herdr-agent-metrics**](https://github.com/szrenwei/herdr-agent-metrics)<br><sub>szrenwei</sub> | Claude Code・Codex・TraeX向けの、軽量なHerdrコンテキスト・セッション使用量メトリクス | `claude-code` `openai-codex` `traex` `python` | 1 | 2026-08-04 |
| [**herdr-space-tab-metadata**](https://github.com/szrenwei/herdr-space-tab-metadata)<br><sub>szrenwei</sub> | 各Herdr Spaceのアクティブなタブをサイドバーに表示する | `terminal-ui` `python` | 1 | 2026-08-04 |
| [**taskherd**](https://github.com/ukwhatn/taskherd)<br><sub>ukwhatn</sub> | herdrのエージェントセッション・PR・Jiraチケットに連携したタスクボード | `claude-code` `kanban` `task-management` `tui` `go` | 1 | 2026-09-01 |
| [**🆕 herdr-virtualboard**](https://github.com/virtualboard/herdr-virtualboard)<br><sub>virtualboard</sub> | Kanban board for VirtualBoard feature specs inside Herdr: columns are the lifecycle, cards are specs, and dispatching a card starts a role agent in a pane. | `go` | 1 | 🔄 2026-09-16 |
| [**herdr-ios-build-status-plugin**](https://github.com/atomsbaza/herdr-ios-build-status-plugin)<br><sub>atomsbaza</sub> | オンデマンドで確認できる、HerdrのiOSビルド＋テスト状況ペイン。失敗時のスクリーンショット付き | `shell` | 0 | 2026-08-06 |
| [**herdr-dev-servers**](https://github.com/carellano/herdr-dev-servers)<br><sub>carellano</sub> | Herdrのペインで動作している開発サーバーを検出し、安全に管理する | `developer-tools` `go` `terminal` | 0 | 2026-08-12 |
| [**🆕 herdr-repository-identity**](https://github.com/choplin/herdr-repository-identity)<br><sub>choplin</sub> | 各Herdrワークスペースが共有するGitリポジトリの識別情報を報告する | `go` | 0 | 2026-08-24 |
| [**herdr-process-guard**](https://github.com/Efeguclu1/herdr-process-guard)<br><sub>Efeguclu1</sub> | コーディングエージェントが起動しっぱなしにしたdevサーバーの内容を説明し、安全に停止する | `claude-code` `codex` `coding-agents` `cursor` `macos` | 0 | 2026-08-24 |
| [**herdr-kanban**](https://github.com/hassox/herdr-kanban)<br><sub>hassox</sub> | ワークスペースのペインをカンバンボードとして表示する | `go` | 0 | 2026-08-21 |
| [**🆕 herdr-reap**](https://github.com/ivorpad/herdr-reap)<br><sub>ivorpad</sub> | herdrプラグイン：全エージェントのライフサイクル状態を表示し、1キーで完了済みのものをまとめて閉じる | `tui` `python` | 0 | 2026-08-27 |
| [**🆕 pi-herdr-sidebar**](https://github.com/mastnacek/pi-herdr-sidebar)<br><sub>mastnacek</sub> | Native Rust Herdr plugin sidebar for the Pi coding agent: status telemetry, live skills, gates — VSA slices in Rust/Ratatui | `pi` `ratatui` `rust` | 0 | 🔄 2026-09-25 |
| [**herdr-idle-shell-badge**](https://github.com/rcosteira79/herdr-idle-shell-badge)<br><sub>rcosteira79</sub> | バックグラウンドでシェルが動き続けている、アイドル状態のエージェントにバッジを表示する | `python` | 0 | 2026-08-26 |
| [**🆕 colloquy**](https://github.com/SoMaCoSF/colloquy)<br><sub>SoMaCoSF</sub> | エージェント群向けの、自己アドレス指定型・一時キャッシュされた因果関係DAG監査ログとテレメトリ | `colloquy` `gyst` `javascript` | 0 | 2026-07-29 |
| [**🆕 herdr-telegram-bridge**](https://github.com/spancerxing/herdr-telegram-bridge)<br><sub>spancerxing</sub> | Approve Herdr coding agents (Claude Code, Codex, agy, pi) from Telegram — per-agent topics, approval buttons, status dashboard, completion notices, and desk-si… | `go` | 0 | 🔄 2026-09-24 |
| [**🆕 herdr-hud**](https://github.com/zetlen/herdr-hud)<br><sub>zetlen</sub> | herdrプラグイン：キーバインドで開くポップアップに、ホスト・ネットワーク・エージェント・セッションの情報を表示——設定変更やカスタムスクリプトによる拡張が可能 | `bash` `terminal` `shell` | 0 | 2026-08-03 |

<details><summary>この目的にも関係するもの</summary>

- [nelsonPires5/herdr-board](https://github.com/nelsonPires5/herdr-board) — herdr向けのカンバンボード——カードはそのままプロンプトになり、見えているペイン上のAIエージェントに割り振られる
- [IvoryHeart/herdr-world](https://github.com/IvoryHeart/herdr-world) — Herdr World——Herdr向けのマルチサーフェスなWeb体験
- [e2b-dev/herdr-e2b-sandbox](https://github.com/e2b-dev/herdr-e2b-sandbox) — git worktreeをE2B Sandboxにミラーするherdrプラグイン——単一のboxでも、エージェントごとにブランチを割り当てたフリートでも対応。TUIダッシュボード付き
- [quaywin/agys](https://github.com/quaywin/agys) — 汚染ゼロのサンドボックスにより、Herdr上のAntigravity CLIに手間いらずのマルチプロファイル分離とリアルタイムなクォータ追跡を提供する
- [Northern-Lighthouse/herdr-fleet](https://github.com/Northern-Lighthouse/herdr-fleet) — Tailscale経由でherdrマシンのフリートを管理——ダッシュボードプラグイン、自動検出、キャパシティを考慮したエージェント割り当て、ディスクレスなワークスペースに対応
- [cdowell09/herdr-pr-board](https://github.com/cdowell09/herdr-pr-board) — 複数リポジトリを横断できる、設定可能なHerdr向けGitHubプルリクエストダッシュボード
- [bengemine/herdr-hibernate](https://github.com/bengemine/herdr-hibernate) — Herdr上のアイドル状態のコーディングエージェントペイン（Claude Code、Codex、Grok）をハイバネート——メモリを解放し、Enterキーで元のセッションをそのまま再開できる
- [Javamomma/herdr-scribe](https://github.com/Javamomma/herdr-scribe) — herdrプラグイン：録音せずにライブで会議を文字起こし——マイク入力をRAM上のみのトランスクリプトとライブ分析用ペインに変換。停止時には議事録・任意のポリシーゲート・レビュー可能な自動ドラフトを生成。Linux/W…
- [sazardev/herdr-code-board](https://github.com/sazardev/herdr-code-board) — Herdr内の、エージェント向けプロンプトのカンバンキュー——カードが実際のエージェントをペイン・worktree・ワークスペースに配置し、カード同士を連鎖させるルールも設定できる
- [spad-0x/herdr-mobile-pro](https://github.com/spad-0x/herdr-mobile-pro) — Cyber-Dark デザインの、高性能でモバイルファーストな PWA ダッシュボード。スマホから直接 Herdr と自律型 AI エージェントをオーケストレーションできます。セキュアな HTTPS、音声入力、画像アッ…
- [chouxcreams/herdr-dashboard](https://github.com/chouxcreams/herdr-dashboard) — herdrのワークスペース向けのPRステータスダッシュボードTUI——ペインごとのPRの状態・CI・レビューを一目で確認できる
- [GranamyrBR/LunaCrab](https://github.com/GranamyrBR/LunaCrab) — 別プロジェクト用に予約済み
- [IniZio/nexus](https://github.com/IniZio/nexus) — Herdr plugin for running worktree in Cloud-Hypervisor sandboxes, with mem/cpu/disk hotplug and auto port-forw…
- [maedana/herdr-agents-preview](https://github.com/maedana/herdr-agents-preview) — Herdr向けのマルチエージェントターミナルプレビューダッシュボード：稼働中のすべてのエージェントを同時に表示し、選択中のエージェントが大部分の幅を占める
- [ryus1234/provider-usage](https://github.com/ryus1234/provider-usage) — Herdr 用の、プロバイダーの使用量とクォータを表示するバーです。

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-finder"></a>

## 検索・ファジーファインダー

> コマンドやプロジェクトを、名前をうろ覚えのまま呼び出したい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-navigator**](https://github.com/thanhdat77/herdr-navigator)<br><sub>thanhdat77</sub> | 1つのファジーナビゲーターから、任意のHerdrのワークスペース・エージェント・プロジェクト・セッション・リモート・ディレクトリ・アクションにジャンプできる | `fuzzy-finder` `rust` `terminal` `workspace-manager` | 166 | 🔄 2026-09-24 |
| [**termscope**](https://github.com/iurysza/termscope)<br><sub>iurysza</sub> | 分割ペインで、ターミナル画面に表示されているファイルやリンクを開く | `python` `television` `terminal` `tmux` | 56 | 🔄 2026-09-21 |
| [**herdr-sessionizer**](https://github.com/andrewchng/herdr-sessionizer)<br><sub>andrewchng</sub> | プロジェクトやworktreeをファジー検索で開き、宣言的なTOMLレイアウト（タブ・ペイン分割・起動コマンド・リポジトリごとの上書き設定）からワークスペースを立ち上げる | `bun` `fuzzy-finder` `fzf` `git-worktree` `sessionizer` | 47 | 🔄 2026-09-23 |
| [**herdr-plugin-sesh**](https://github.com/fullerzz/herdr-plugin-sesh)<br><sub>fullerzz</sub> | Herdr向けのSesh風ワークスペースピッカーTUI。zoxideと連携し、よく使うディレクトリからワークスペースを作成できる | `bubbletea` `sesh` `tui` `zoxide` `go` | 45 | 🔄 2026-09-25 |
| [**herdr-bar**](https://github.com/jeffarese/herdr-bar)<br><sub>jeffarese</sub> | Cmd+K and auto tab title for herdr: fuzzy-jump to any tab, agent, repo or branch. | `command-bar` `fuzzy-finder` `python` `terminal` `tui` | 45 | 🔄 2026-09-24 |
| [**herdr-command-palette**](https://github.com/JanTvrdik/herdr-command-palette)<br><sub>JanTvrdik</sub> | herdr向けのfzfコマンドパレット——任意のプラグインアクションをファジー検索して実行 | `shell` | 38 | 2026-06-29 |
| [**herdr-drovr**](https://github.com/AVGVSTVS96/herdr-drovr)<br><sub>AVGVSTVS96</sub> | herdrのペインとタブを簡単に移動する | `fzf` `terminal` `javascript` | 19 | 2026-08-08 |
| [**herdr-palette**](https://github.com/vjeantet/herdr-palette)<br><sub>vjeantet</sub> | Sublime Text / VS Code風の、herdr向けコマンドパレット——標準操作・プラグインのアクション・自分のコマンドを、1つのキーの裏にまとめる | `command-palette` `fuzzy-search` `terminal` `tui` `rust` | 13 | 🔄 2026-09-10 |
| [**herdr-zoxide**](https://github.com/den-tanui/herdr-zoxide)<br><sub>den-tanui</sub> | zoxideのディレクトリからワークスペース・タブ・ペインを作成するHerdrプラグイン | `zoxide` `shell` | 11 | 2026-07-25 |
| [**🆕 herdr-omni**](https://github.com/mmjang/herdr-omni)<br><sub>mmjang</sub> | One search for Herdr workspaces, actions, and live or saved Codex & Claude sessions. Fuzzy-find by name, search conversation content, and resume where you left… | `claude-code` `codex` `opencode` `rust` | 9 | 🔄 2026-09-22 |
| [**herdr-palette**](https://github.com/ramarivera/herdr-palette)<br><sub>ramarivera</sub> | Herdrのワークスペース向けの、Rust/Ratatui製ファジーコマンドパレット | `command-palette` `ratatui` `rust` `terminal` `tui` | 9 | 🔄 2026-09-11 |
| [**herdr-quick-actions**](https://github.com/enekos/herdr-quick-actions)<br><sub>enekos</sub> | herdr標準のタブ/ペイン/ワークスペース操作を、使用頻度順でfzfから選べる——キーバインドを覚える必要がなくなる | `shell` | 8 | 2026-08-05 |
| [**🆕 herdr-transcripts**](https://github.com/hxreborn/herdr-transcripts)<br><sub>hxreborn</sub> | Search your coding-agent sessions, past and live, by any word you remember, then jump to them or resume them | `claude-code` `codex` `coding-agents` `droid` `fzf` | 6 | 🔄 2026-09-21 |
| [**herdr-hunk**](https://github.com/JacquesvanWyk/herdr-hunk)<br><sub>JacquesvanWyk</sub> | herdr向けの、Hunkの差分をfzfで対話的に選ぶピッカー：コミット・範囲・stashに対応し、エージェント完了時に自動オープンもできる | `fzf` `hunk` `shell` | 6 | 2026-07-12 |
| [**herdr-sessionizer**](https://github.com/salkhalil/herdr-sessionizer)<br><sub>salkhalil</sub> | herdr版tmux-sessionizer：開いているワークスペースとzoxideのディレクトリをfzfで検索し、テンプレートタブ付きで作成またはフォーカスする | `shell` | 6 | 2026-07-27 |
| [**herdr-openr**](https://github.com/wraithyy/herdr-openr)<br><sub>wraithyy</sub> | herdrプラグイン：ターミナルやAIエージェントが直前に言及したファイル/URLをファジー検索で開く——Claudeのペインではセッションのトランスクリプトを読み取る | `shell` | 6 | 2026-08-14 |
| [**herdr-palette**](https://github.com/cesarferreira/herdr-palette)<br><sub>cesarferreira</sub> | Herdr向けのポップアップ型コマンドパレット | `typescript` | 5 | 2026-09-08 |
| [**herdr-switchboard**](https://github.com/crafts69guy/herdr-switchboard)<br><sub>crafts69guy</sub> | herdrプラグイン：稼働中のエージェント・開いているワークスペース・ghq管理下のリポジトリを、Rust製の1つのTUIでファジー切り替え——選んだリポジトリを新規ワークスペース・タブ・スプリット・現在のペインのいずれかで開ける | `developer-tools` `ghq` `ratatui` `rust` `terminal` | 5 | 🔄 2026-09-18 |
| [**herdr-pickr**](https://github.com/javoscript/herdr-pickr)<br><sub>javoscript</sub> | YAP！ Herdr マルチプレクサ用の、また一つのピッカーです。 | `fzf` `lua` | 5 | 🔄 2026-09-23 |
| [**herdr-ssh-manager**](https://github.com/jorge07RD/herdr-ssh-manager)<br><sub>jorge07RD</sub> | SSHホストを保存し、Herdr内のファジーポップアップから再接続する——Enterキーでポップアップからそのままsshに渡す | `rust` `ssh` `terminal` `tui` | 5 | 2026-08-24 |
| [**herdr-kiosk**](https://github.com/thomasschafer/herdr-kiosk)<br><sub>thomasschafer</sub> | Gitのリポジトリとブランチをファジー検索し、Herdr内でworktreeとして開く | `rust` | 5 | 🔄 2026-09-24 |
| [**herdr-cast**](https://github.com/aliou/herdr-cast)<br><sub>aliou</sub> | 個人用Herdrプラグイン——ネイティブmacOS通知、ファジーなワークスペース移動、zoxide連携のワークスペース作成、レイアウトコマンドをまとめて提供 | `developer-tools` `macos` `notifications` `ratatui` `rust` | 4 | 🔄 2026-09-20 |
| [**herdr-pane-navigator**](https://github.com/mr04vv/herdr-pane-navigator)<br><sub>mr04vv</sub> | Herdrのワークスペース・タブ・ペインを1つのファジーツリーとして横断移動——各ペインが実際に何をしているかを手がかりにする | `coding-agents` `fzf` `terminal` `tui` `shell` | 4 | 2026-09-07 |
| [**herdr-keymap**](https://github.com/The-Dave-Stack/herdr-keymap)<br><sub>The-Dave-Stack</sub> | herdrプラグイン：すべてのキーバインドをオーバーレイのパレットに表示し、CLI相当のものはそのまま実行できる | `typescript` | 4 | 2026-08-12 |
| [**herdr-configurable-picker**](https://github.com/yoshiori/herdr-configurable-picker)<br><sub>yoshiori</sub> | 完全にカスタマイズ可能なキーバインドを持つ、herdr向けのツリー形式gotoピッカー | `rust` | 4 | 2026-07-05 |
| [**herdr-grep-nvim**](https://github.com/cinco/herdr-grep-nvim)<br><sub>cinco</sub> | herdrプラグイン：fzf + ripgrepでライブgrepし、マッチした箇所を作業の隣のスプリットでnvimで開く | `shell` | 3 | 2026-07-17 |
| [**herdr-spotify**](https://github.com/iikjl/herdr-spotify)<br><sub>iikjl</sub> | herdr向けのSpotify再生中オーバーレイプラグイン——アルバムアート・再生操作、Spotify Web API経由の検索/キュー追加/いいねにも対応 | `spotify` `terminal` `go` | 3 | 2026-07-07 |
| [**herdr-workspacer**](https://github.com/mcuste/herdr-workspacer)<br><sub>mcuste</sub> | zoxideでプロジェクトを見つけ、Herdrのワークスペースを切り替え・作成する | `rust` `tui` `zoxide` | 3 | 🔄 2026-09-16 |
| [**herdr-fzf-terminal-browser**](https://github.com/to4iki/herdr-fzf-terminal-browser)<br><sub>to4iki</sub> | herdr プラグイン：キーを押すと、現在のペインに表示されている URL を fzf で選べ、terminal-browser で開きます。 | `fzf` `rust` `terminal-browser` | 3 | 🔄 2026-09-12 |
| [**herdr-agent-recency**](https://github.com/ugurtarlig/herdr-agent-recency)<br><sub>ugurtarlig</sub> | テーマに対応したHerdrピッカー。CodexとClaudeの実質的なアクティビティで並び替える | `claude-code` `codex` `fzf` `python` | 3 | 2026-07-17 |
| [**herdr-command-palette**](https://github.com/alon-z/herdr-command-palette)<br><sub>alon-z</sub> | Herdrプラグイン：ワークスペース/ディレクトリのファジー検索コマンドパレット | `javascript` | 2 | 🔄 2026-09-22 |
| [**herdr-launcher**](https://github.com/arjenblokzijl/herdr-launcher)<br><sub>arjenblokzijl</sub> | 宣言的なTOMLワークフローをファジー検索で選び、フォームに入力して、新しいherdrのスペースでコーディングエージェントを起動する | `launcher` `ratatui` `rust` `tui` | 2 | 2026-07-10 |
| [**herdr-palette**](https://github.com/Binb1/herdr-palette)<br><sub>Binb1</sub> | Herdr 用のコマンドパレット。ワークスペースやエージェントへジャンプしたり、プラグインのアクションや Herdr のコマンドを実行できます。 | `go` | 2 | 🔄 2026-09-24 |
| [**herdr-workspace-save**](https://github.com/chandrasekharan98/herdr-workspace-save)<br><sub>chandrasekharan98</sub> | Herdrのワークスペース（レイアウト・作業ディレクトリ・エージェントセッション・実行中のコマンド）を保存し、あとでfzfピッカーから再度開ける | `claude-code` `terminal` `tmux` `python` | 2 | 2026-08-19 |
| [**herdr-sesh-bro**](https://github.com/cyperx84/herdr-sesh-bro)<br><sub>cyperx84</sub> | Herdr向けのsesh風ファジーセッションピッカー——ワークスペース・エージェント・zoxideのディレクトリを、ライブプレビュー付きの1つのfzfポップアップにまとめる | `go` | 2 | 🔄 2026-09-19 |
| [**herdr-simple-switcher**](https://github.com/haphamdev/herdr-simple-switcher)<br><sub>haphamdev</sub> | ワークスペース・タブ・AIエージェントをファジー検索する | `shell` | 2 | 2026-08-01 |
| [**herdr-command-palette**](https://github.com/hota911/herdr-command-palette)<br><sub>hota911</sub> | herdr標準の操作（ワークスペース・タブ・ペイン・エージェント）向けの、fzfコマンドパレット | `command-palette` `fzf` `shell` | 2 | 2026-08-16 |
| [**herdr-workspace-launcher**](https://github.com/ImArtisann/herdr-workspace-launcher)<br><sub>ImArtisann</sub> | 検索可能でキーボード操作のディレクトリピッカーを使い、フォーカスしたワークスペースをすばやく作成するmacOS向けHerdrプラグイン | `typescript` | 2 | 2026-07-16 |
| [**herdr-recent-workspaces**](https://github.com/ismaelosuna7824/herdr-recent-workspaces)<br><sub>ismaelosuna7824</sub> | Herdr版「最近使ったフォルダを開く」——ワークスペースとして開いたフォルダをファジー検索できる一覧。選ぶとそのワークスペースを開くか再フォーカスでき、ファイルシステムを参照して新規に開くこともできる | `go` | 2 | 2026-07-10 |
| [**herdr-nav**](https://github.com/karanpatel1993/herdr-nav)<br><sub>karanpatel1993</sub> | File navigation, code search and jdb debugging inside herdr — fzf, ripgrep and a Java debugger wired into your terminal workspace | `shell` | 2 | 🔄 2026-09-17 |
| [**herdr-ghq-open-agent**](https://github.com/kenchan/herdr-ghq-open-agent)<br><sub>kenchan</sub> | herdrプラグイン：ghq管理下のリポジトリをfzfでインクリメンタル検索し、選んだものをワークスペース/タブで開いてclaudeを起動する | `fzf` `ghq` `shell` | 2 | 2026-08-03 |
| [**🆕 herdr-commander**](https://github.com/lurepos/herdr-commander)<br><sub>lurepos</sub> | Fast palette to discover/launch npm, cargo, .vscode tasks and commands from herdr | `rust` | 2 | 🔄 2026-09-20 |
| [**herdr-keybind-search**](https://github.com/malone-c/herdr-keybind-search)<br><sub>malone-c</sub> | herdr向けの検索可能なキーバインドオーバーレイ（fzf）。キーを押すと、自分のキーバインドをファジー検索できる | `shell` | 2 | 2026-07-15 |
| [**herdr-plugin-picker**](https://github.com/purehate/herdr-plugin-picker)<br><sub>purehate</sub> | Herdr 用の浮動ポップアップピッカーです——任意のスペース・エージェント・タブ・ペインへジャンプでき、マークした全ペインへ 1 つのコマンドを一斉送信でき、~/.ssh/config からリアルタイムの疎通確認付きで SSH 接続もできます。すべてキーボードで操作します。 | `broadcast` `fuzzy-finder` `golang` `picker` `ssh` | 2 | 🔄 2026-09-18 |
| [**herdr-flash-picker**](https://github.com/TinyWhite1997/herdr-flash-picker)<br><sub>TinyWhite1997</sub> | 1〜2 文字の整列したジャンプラベルで、すばやくペインを選べる Herdr 用ピッカーです。 | `rust` `tui` | 2 | 2026-09-07 |
| [**herdr-waypoint**](https://github.com/wraithyy/herdr-waypoint)<br><sub>wraithyy</sub> | フォルダに名前を付けて保存し、ファジー検索の一覧から選んで新しいherdrワークスペースとして開く | `shell` | 2 | 2026-08-12 |
| [**herdr-sessionizer**](https://github.com/42lizard/herdr-sessionizer)<br><sub>42lizard</sub> | tmux-sessionizer風のherdr向けプラグイン | `fzf` `shell` | 1 | 2026-08-28 |
| [**herdr-url-picker**](https://github.com/abrose/herdr-url-picker)<br><sub>abrose</sub> | herdrプラグイン：現在のペインに表示されたURLをfzfで選び、デフォルトブラウザで開く | `shell` | 1 | 2026-07-22 |
| [**herdr-jump**](https://github.com/agustinvalencia/herdr-jump)<br><sub>agustinvalencia</sub> | herdrのスペースとエージェント用に分かれたオーバーレイピッカー——任意のワークスペースやエージェントに、ステータスを色で示しながらジャンプできる | `go` | 1 | 2026-07-24 |
| [**herdr-command-palette**](https://github.com/barnuri/herdr-command-palette)<br><sub>barnuri</sub> | herdr向けのF1風コマンドパレット——インストール済みの全プラグインの全アクションを、ファジー検索して実行できる。依存関係なし | `command-palette` `terminal` `javascript` | 1 | 2026-09-01 |
| [**helm.herdr**](https://github.com/black-atom-industries/helm.herdr)<br><sub>black-atom-industries</sub> | 1つのファジーナビゲーターから、任意のHerdrのワークスペース・エージェント・プロジェクト・セッション・リモート・ディレクトリ・アクションにジャンプできる | `rust` | 1 | 2026-09-03 |
| [**herdr-url-picker**](https://github.com/chouxcreams/herdr-url-picker)<br><sub>chouxcreams</sub> | Herdrプラグイン：フォーカス中のペインからURLを選び、ブラウザで開く | `shell` | 1 | 2026-07-22 |
| [**herdr-spotify**](https://github.com/DeepRuparel/herdr-spotify)<br><sub>DeepRuparel</sub> | Herdr向けのSpotify連携——Go製、設定不要のローカル操作に加え、PKCE経由で認可された検索・キュー追加・保存に対応 | `spotify` `go` | 1 | 2026-08-28 |
| [**🆕 herdr-pane-mover**](https://github.com/dimitri4d/herdr-pane-mover)<br><sub>dimitri4d</sub> | キーボードでもマウスでも使いやすい移動先ピッカーで、実行中の Herdr ペインをタブやワークスペース間で移動できます。 | `go` | 1 | 🔄 2026-09-13 |
| [**herdr-agents**](https://github.com/dleen/herdr-agents)<br><sub>dleen</sub> | herdr向けのfzfエージェントピッカー——全エージェントペインを対応優先度の高い順に並べ、セッションプレビューとワンキー起動に対応する | `coding-agents` `fzf` `python` `terminal` | 1 | 2026-08-20 |
| [**🆕 herdr-hosts**](https://github.com/ecylmz/herdr-hosts)<br><sub>ecylmz</sub> | Hierarchical SSH host picker for Herdr, with folders and notes straight from ~/.ssh/config | `ratatui` `rust` `ssh` `terminal` `tui` | 1 | 🔄 2026-09-18 |
| [**herdr-plugin-command-palette**](https://github.com/haisi/herdr-plugin-command-palette)<br><sub>haisi</sub> | fzfを使った、herdr向けのファジー検索対応コマンドパレット | `fzf` `python` | 1 | 2026-08-17 |
| [**🆕 herdr-palette**](https://github.com/iancharters/herdr-palette)<br><sub>iancharters</sub> | Fuzzy command palette for Herdr — core commands plus auto-discovered plugin actions, run where you can see them. Fast, keyboard-first, terminal-native. | `go` | 1 | 🔄 2026-09-25 |
| [**herdr-turbo-palette**](https://github.com/jackfrancisdalton/herdr-turbo-palette)<br><sub>jackfrancisdalton</sub> | 任意のHerdrのspace・タブ・エージェント・ペインをファジー検索し、そのまま直接ジャンプする | `python` | 1 | 2026-08-22 |
| [**herdr-keys**](https://github.com/JacquesvanWyk/herdr-keys)<br><sub>JacquesvanWyk</sub> | herdr向けの、ファジー検索可能なキーバインド一覧（パック・発見機能・個人による上書き設定に対応） | `shell` | 1 | 2026-07-12 |
| [**herdr-open-editor**](https://github.com/jimididit/herdr-open-editor)<br><sub>jimididit</sub> | fzf でファイルをあいまい検索して選び、設定済みのエディタで開きます。 | `herd` `text-editor` `tui` `shell` | 1 | 2026-09-03 |
| [**herdr-fzf-url**](https://github.com/kaar/herdr-fzf-url)<br><sub>kaar</sub> | herdrペインのスクロールバックからURLをファジー検索して開く——tmux-fzf-urlのherdr移植版 | `shell` | 1 | 2026-07-29 |
| [**herdr-hint**](https://github.com/maedana/herdr-hint)<br><sub>maedana</sub> | Herdr向けのVimium風ヒントラベル——キーを押すとタブやエージェントにラベルが表示され、ラベルを押すとジャンプする | `rust` | 1 | 2026-08-11 |
| [**herdr-shortcut**](https://github.com/matheus3301/herdr-shortcut)<br><sub>matheus3301</sub> | Herdr向けのショートカットタスクピッカー兼コーディングエージェントランチャー | `bubbletea` `claude-code` `codex` `coding-agents` `developer-tools` | 1 | 2026-07-24 |
| [**herdr-pickers**](https://github.com/sagmans/herdr-pickers)<br><sub>sagmans</sub> | エージェント・worktree・ワークスペース・プロジェクト向けに、いくつかのカスタムなポップアップピッカーを提供します。 | `typescript` | 1 | 🔄 2026-09-22 |
| [**🆕 herdr-plugins**](https://github.com/shelken/herdr-plugins)<br><sub>shelken</sub> | Herdrプラグインのモノレポ（auto-pi：エリアごとにpiを開く＋セッションピッカー） | `python` | 1 | 2026-07-17 |
| [**herdr-jump**](https://github.com/solidsnakedev/herdr-jump)<br><sub>solidsnakedev</sub> | herdr 用のワークスペース・ペイン・タブのあいまい検索ピッカーに加え、直前のワークスペースへ切り替えるトグルも備えています。 | `shell` | 1 | 2026-09-01 |
| [**herdr-pane-picker**](https://github.com/ugurtarlig/herdr-pane-picker)<br><sub>ugurtarlig</sub> | ペイン上に表示される文字ヒントを入力して、Herdrのペインを選択する | `terminal` `wezterm` `python` | 1 | 2026-07-17 |
| [**herdr-palette**](https://github.com/vika2603/herdr-palette)<br><sub>vika2603</sub> | herdr 用のコマンドパレットです。一つのポップアップから、herdr のコマンド・インストール済み全プラグインのアクション・自分で定義したコマンド・セッション内で開いているものすべてを検索し、選んだものを実行できます。 | `bubbletea` `command-palette` `fzf` `go` `terminal` | 1 | 🔄 2026-09-13 |
| [**herdr-bitwarden**](https://github.com/WillowMist/herdr-bitwarden)<br><sub>WillowMist</sub> | Bitwardenのボルトをファジー検索し、認証情報を貼り付け・コピーする——tmux-bitwardenのherdr移植版 | `bitwarden` `fzf` `terminal` `tmux` `shell` | 1 | 2026-08-11 |
| [**herdr-fzf-url**](https://github.com/x0d7x/herdr-fzf-url)<br><sub>x0d7x</sub> | herdrのターミナルペインをスキャンしてURLを検出し、fzfで対話的に選択する | `fzf` `go` `url` | 1 | 2026-06-26 |
| [**herdr-open-local-paths**](https://github.com/yigitkg/herdr-open-local-paths)<br><sub>yigitkg</sub> | ローカルパスを検出し、Windows・Linux・WSL上のシンプルなピッカーから開く/表示するHerdrプラグイン | `developer-tools` `python` `terminal` `wsl` | 1 | 2026-07-28 |
| [**herdr-agents-picker**](https://github.com/yxhta/herdr-agents-picker)<br><sub>yxhta</sub> | Herdrプラグイン：ワークスペースピッカー風のファジー検索で、エージェントペインをリアルタイムプレビュー付きで選ぶ（Rust + ratatui製） | `rust` | 1 | 2026-09-08 |
| [**herdr-telescope**](https://github.com/zackshen/herdr-telescope)<br><sub>zackshen</sub> | herdr向けのfzfコマンドテレスコープ——ネイティブアクション、プラグインアクション、ファイル検索（@）、ライブripgrep検索（/）に対応 | `fzf` `rust` | 1 | 2026-08-20 |
| [**🆕 herdr-project-manager**](https://github.com/barnuri/herdr-project-manager)<br><sub>barnuri</sub> | herdr向けのプロジェクトマネージャープラグイン——globまたは手動でのプロジェクト検出、ファジーピッカー、タブまたはワークスペースとしてオープン | `javascript` | 0 | 2026-08-25 |
| [**herdr-locksmith**](https://github.com/bkarpinos/herdr-locksmith)<br><sub>bkarpinos</sub> | herdr向けのキーバインド・コマンドパレット | `go` | 0 | 2026-09-01 |
| [**herdr-opencode-sessions**](https://github.com/damianpoole/herdr-opencode-sessions)<br><sub>damianpoole</sub> | 過去のOpenCodeセッションを、タイトル・プロジェクト・パス・日付・トランスクリプトの内容でファジー検索できるHerdrプラグイン——会話プレビュー付きで、現在または新しいワークスペースでセッションを再開・フォークするショートカットも備える | `typescript` | 0 | 2026-08-14 |
| [**herdr-rbw**](https://github.com/ibanks42/herdr-rbw)<br><sub>ibanks42</sub> | Bitwarden のボルトをあいまい検索し、herdr 内で認証情報を貼り付け・コピーできます——rbw 版。 | `shell` | 0 | 🔄 2026-09-14 |
| [**herdr-repo-picker**](https://github.com/mayaton/herdr-repo-picker)<br><sub>mayaton</sub> | A herdr plugin that opens an overlay pane to fuzzy-pick a ghq repository and jump to its workspace. | `fuzzy-finder` `ghq` `ratatui` `rust` `tui` | 0 | 🔄 2026-09-17 |
| [**herdr-repo-picker**](https://github.com/princejoogie/herdr-repo-picker)<br><sub>princejoogie</sub> | OpenTUI製のピッカーから、Gitリポジトリをherdrのワークスペースとして開く | `git` `opentui` `typescript` | 0 | 2026-08-17 |
| [**🆕 herdr-claude-profile**](https://github.com/quinnjr/herdr-claude-profile)<br><sub>quinnjr</sub> | herdrプラグイン：オーバーレイのパレットからclaude-profileのプロファイルを切り替え・管理する | `typescript` | 0 | 🔄 2026-09-11 |
| [**🆕 herdr-file-picker**](https://github.com/shivammehta25/herdr-file-picker)<br><sub>shivammehta25</sub> | tmux-file-pickerをherdr向けに移植した、いわゆる「vibe coding」製プラグイン | `shell` | 0 | 2026-07-29 |
| [**herdr-fzf-url**](https://github.com/willian/herdr-fzf-url)<br><sub>willian</sub> | フォーカス中のペインから`fzf`でURLを選び、開く・コピーする | `fzf` `shell` | 0 | 2026-07-28 |

<details><summary>この目的にも関係するもの</summary>

- [ThorstenRhau/token](https://github.com/ThorstenRhau/token) — Neovim のカラースキームで、ターミナル全体向けのコントリビューションテーマも含みます。
- [beyondlex/herdr-recent-navigator](https://github.com/beyondlex/herdr-recent-navigator) — 最近使ったワークスペース・タブ・ペイン・エージェントを MRU（最近使った順）で切り替えられます——JetBrains の「最近使ったファイル」のような感覚です。さらに、任意のペインの内容をあいまい検索でき、すべてキー…
- [JacquesvanWyk/herdr-linear](https://github.com/JacquesvanWyk/herdr-linear) — herdrのスプリットペインまたはタブ内で動くfzf駆動のLinearパネル：issue検索、プロジェクトの深掘り、issue作成、ステータス変更ができる
- [hamzahraihan/herdr-better-workspace](https://github.com/hamzahraihan/herdr-better-workspace) — AI コーディングエージェント向けのターミナルワークスペースマネージャー herdr 用の、インタラクティブな「ワークスペースを開く」ピッカープラグインです。
- [42lizard/herdr-dwm-layout](https://github.com/42lizard/herdr-dwm-layout) — Herdr向けの、DWM風master/stackレイアウト
- [adriankarlen/yeet](https://github.com/adriankarlen/yeet) — a minimal sesh style picker inside herdr
- [adamwangxx/herdr-codex-resume](https://github.com/adamwangxx/herdr-codex-resume) — ネイティブのCodex resumeピッカーを、Herdrのコンテキストを保ったまま新しいスプリットで開く
- [mackt/herdr-session-fork](https://github.com/mackt/herdr-session-fork) — Herdr plugin: fork the focused Claude Code / Codex / Pi / Grok session into another workspace or worktree, pi…

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-automation"></a>

## 自動化・フック・定期実行

> worktree 作成時やタイミングを決めて、決まった手順を自動で走らせたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-browser**](https://github.com/ogulcancelik/herdr-browser)<br><sub>ogulcancelik</sub> | Herdrのペイン内で実際のChromiumビューを描画し、CDP経由で操作する | `browser` `browser-automation` `cdp` `chromium` `kitty-graphics` | 354 | 2026-08-22 |
| [**herdr-auto-title**](https://github.com/kryptamine/herdr-auto-title)<br><sub>kryptamine</sub> | Automatically name Herdr tabs and panes from your current work, Git branch, terminal activity, and Claude Code sessions. | `claude-code` `coding-agents` `developer-tools` `terminal` `terminal-multiplexer` | 201 | 🔄 2026-09-25 |
| [**herdr-automatic-rename**](https://github.com/qu8n/herdr-automatic-rename)<br><sub>qu8n</sub> | エージェントとシェルをすばやく切り替えられる、スマートな herdr タブ名です。 | `shell` | 177 | 🔄 2026-09-14 |
| [**herdr-auto-title**](https://github.com/sh1ma/herdr-auto-title)<br><sub>sh1ma</sub> | Claude CodeとCodexの会話内容から、herdrのタブタイトルを自動生成する | `claude-code` `codex` `python` | 51 | 🔄 2026-09-11 |
| [**zed-herdr**](https://github.com/ImArtisann/zed-herdr)<br><sub>ImArtisann</sub> | アクティブなHerdRワークスペースを、既存のZedセッションと自動的に同期する | `typescript` | 28 | 2026-08-17 |
| [**herdr-worktree-setup**](https://github.com/tdi/herdr-worktree-setup)<br><sub>tdi</sub> | herdrプラグイン：worktree作成時にプロジェクトごとのセットアップ手順を実行（mainから.envをコピー、mise trust、direnv allow、依存関係のインストールなど） | `javascript` | 27 | 🔄 2026-09-11 |
| [**herdr-workflows**](https://github.com/aorumbayev/herdr-workflows)<br><sub>aorumbayev</sub> | herdrの繰り返し作業を宣言的に自動化する | `agentic-ai` `agentic-workflow` `agents` `ai` `claude` | 25 | 🔄 2026-09-25 |
| [**herdr-auto-pilot**](https://github.com/0xGosu/herdr-auto-pilot)<br><sub>0xGosu</sub> | Herdr APIを介して、稼働中のAIコーディングCLIに代わって自動でプロンプトを送るHerdrプラグイン。あなたの操作から学習するトレーニングモードと、危険/悪意ある操作を防ぐガード機能を搭載。十分に学習させれば「Full-Self Prompting（FSP）」モードで自律動作させられる | `go` | 24 | 🔄 2026-09-21 |
| [**herdr-routines**](https://github.com/mrcndz/herdr-routines)<br><sub>mrcndz</sub> | スケジュールされたルーティンを実行するHerdrプラグイン：cronまたは一定間隔でワークスペースにタブを開き、コマンド実行やエージェント起動を行う | `python` | 11 | 2026-07-18 |
| [**herdr-updater**](https://github.com/diegopzz/herdr-updater)<br><sub>diegopzz</sub> | Herdr本体とプラグインを、フリート全体にわたって安全に最新の状態に保つ | `rust` `updater` | 9 | 🔄 2026-09-17 |
| [**herdr-automations**](https://github.com/DnzzL/herdr-automations)<br><sub>DnzzL</sub> | ターミナル上で動く、コーディングエージェント向けのスケジュールタスク。1回の実行ごとにプロンプト・cron行・新しいgit worktreeを用意——Herdr上で動作。1つのYAMLファイルのみで、ストア不要、ビルド済みバイナリ、自動化ごとにモデルを指定可能、スリープ後のキャッチアップ、ライブボード付き | `ai-agents` `automation` `claude-code` `coding-agents` `cron` | 9 | 🔄 2026-09-14 |
| [**herdr-agent-config-manager**](https://github.com/Phoobobo/herdr-agent-config-manager)<br><sub>Phoobobo</sub> | エージェントのスキル・MCP・プラグイン・フックを検出し一括管理する、CLIとHerdrプラグインのハイブリッド | `python` | 9 | 2026-09-06 |
| [**herdr-tab-title**](https://github.com/aarsh21/herdr-tab-title)<br><sub>aarsh21</sub> | Herdr向けの、tmux風タブタイトルの自動設定 | `rust` `terminal` `tmux` | 8 | 2026-07-08 |
| [**bermuda**](https://github.com/bon5co/bermuda)<br><sub>bon5co</sub> | herdr上のClaude Codeによるオーケストレーション——エージェントが飛ばせないフロー、時刻指定のジョブ、claim付きスレッド、あとでエージェントが検索できるフォーラムを提供する | `agent-orchestration` `agents` `ai-agents` `automation` `claude-code` | 8 | 2026-09-08 |
| [**herdr-shepherd**](https://github.com/mikedclarke/herdr-shepherd)<br><sub>mikedclarke</sub> | herdr向けのスケジュールされたエージェントセッション——ハートビート・cronルーティン・スクリプトを、見えるherdrワークスペースとして起動する | `coding-agents` `cron` `go` `scheduler` `tui` | 7 | 🔄 2026-09-13 |
| [**herdr-pane-balancer**](https://github.com/jeph/herdr-pane-balancer)<br><sub>jeph</sub> | ペインの作成・終了・クローズ時に、Herdrのターミナルペインを自動でバランス調整・均等化・タイル配置する | `python` | 5 | 2026-08-02 |
| [**herdr-sched**](https://github.com/husniadil/herdr-sched)<br><sub>husniadil</sub> | Herdr上のコーディングエージェント向けのスケジュールとトリガー——cronジョブとwebhook/ファイル監視トリガーが、隣接するプラグインへアクションを発火させる。各アクションは実行主体によって署名される。すべて1つのGoバイナリで実現 | `ai-agents` `cron` `mcp-server` `scheduler` `webhooks` | 4 | 2026-08-30 |
| [**herdr-fwd**](https://github.com/go-min/herdr-fwd)<br><sub>go-min</sub> | リモートのHerdrセッション向けに、ループバックポートフォワーディングを自動設定する | `port-forwarding` `ssh` `terminal` `rust` | 3 | 2026-09-09 |
| [**herdr-review-loop**](https://github.com/mikhail-angelov/herdr-review-loop)<br><sub>mikhail-angelov</sub> | herdrのワークスペース内でエージェント同士が自動的に相互レビューする——1体が書き、もう1体がレビューし、これを繰り返す | `terminal` `go` | 3 | 🔄 2026-09-19 |
| [**herdr-plugin**](https://github.com/ppggff/herdr-plugin)<br><sub>ppggff</sub> | 各Herdrペインに適したmacOSの入力方式（IME）を自動的に記憶・復元する | `ime` `input-method` `macos` `python` | 3 | 2026-07-27 |
| [**herdr-autocontinue**](https://github.com/rcosteira79/herdr-autocontinue)<br><sub>rcosteira79</sub> | エージェントの利用上限到達を監視し、リセットまでのカウントダウンをバッジ表示（$wall）し、時間枠が再び開いたらセットしておいたエージェントに再度プロンプトを送る | `python` | 3 | 🔄 2026-09-23 |
| [**herdr-labels**](https://github.com/Angel-O/herdr-labels)<br><sub>Angel-O</sub> | 手動で付けたラベルは維持したまま、タブに自動で名前と番号を付けるHerdrプラグイン | `rust` | 2 | 🔄 2026-09-20 |
| [**hermes-herdr-auto-reconcile**](https://github.com/chris-yyau/hermes-herdr-auto-reconcile)<br><sub>chris-yyau</sub> | Herdrのペインを監視するHermesスーパーバイザー向けの、ゲートウェイ生存監視プラグイン | `automation` `hermes-agent` `multi-agent` `python` | 2 | 🔄 2026-09-16 |
| [**herdr-auto-update**](https://github.com/dio16/herdr-auto-update)<br><sub>dio16</sub> | herdrプラグイン：インストール済みプラグインに新しいアップストリームのコミットがあるか起動時に確認し、あれば再インストールする | `rust` | 2 | 2026-08-16 |
| [**herdr-routines**](https://github.com/guidodinello/herdr-routines)<br><sub>guidodinello</sub> | _(説明なし)_ | `python` | 2 | 🔄 2026-09-25 |
| [**herdr-js-worktree-bootstrap**](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap)<br><sub>LeonardoTrapani</sub> | JavaScript/TypeScript向けにHerdrのworktreeを自動でブートストラップ——ロックファイルを考慮したインストールと、安全な環境ファイルの復元に対応 | `automation` `bun` `developer-tools` `git-worktree` `javascript` | 2 | 2026-07-15 |
| [**🆕 spoolway**](https://github.com/marvingygas/spoolway)<br><sub>marvingygas</sub> | Minimalistic agent state machine for software development: a dispatcher that drives agent sessions through defined pipelines | `agent` `automation` `cli` `dispatcher` `llm` | 2 | 🔄 2026-09-25 |
| [**herdr-triggers**](https://github.com/cantona/herdr-triggers)<br><sub>cantona</sub> | ペインの出力を常駐監視して正規表現でトリガーを発動します。自動ログインなど、正規表現ベースのターミナルトリガーに対応します。 | `rust` `terminal` `terminal-based` `terminal-multiplexer` `trigger` | 1 | 🔄 2026-09-18 |
| [**herdr-auto-tab-name**](https://github.com/dev-shimada/herdr-auto-tab-name)<br><sub>dev-shimada</sub> | herdrプラグイン：タブに現在のディレクトリ名を自動で付ける | `javascript` | 1 | 🔄 2026-09-19 |
| [**🆕 relevo**](https://github.com/fuad-daoud/relevo)<br><sub>fuad-daoud</sub> | Automates the plan/report handoff between planner and builder AI coding agent panes running under herdr | `go` | 1 | 🔄 2026-09-25 |
| [**herdr-tab-autorun**](https://github.com/hanbong5938/herdr-tab-autorun)<br><sub>hanbong5938</sub> | TOML ルールに基づいて、新しいタブごとにシェルコマンドを実行したりコーディングエージェントを起動したりする Herdr プラグインです。 | `ai-agents` `automation` `nodejs` `terminal` `javascript` | 1 | 2026-09-10 |
| [**say-hook**](https://github.com/HikaruEgashira/say-hook)<br><sub>HikaruEgashira</sub> | Claude Codeのフックイベントを、ElevenLabsのText-to-Speechで読み上げるmacOS向けCLI | `typescript` | 1 | 🔄 2026-09-12 |
| [**herdr-cron**](https://github.com/huketo/herdr-cron)<br><sub>huketo</sub> | コーディングエージェント向けの自動化作業をスケジュール実行できます。Herdr のペイン内で、シェルコマンドやコーディングエージェントへのプロンプトを予約できます。 | `agent-skills` `automation` `bubbletea` `cli` `coding-agent` | 1 | 🔄 2026-09-18 |
| [**herdr-worktree-cleanup**](https://github.com/poislagarde/herdr-worktree-cleanup)<br><sub>poislagarde</sub> | Herdr のスペースが閉じられたとき、安全な GitHub PR の worktree を自動的にクリーンアップします。Python 製、依存なし、MIT ライセンス。 | `git-worktree` `python` | 1 | 🔄 2026-09-11 |
| [**herdr-automations**](https://github.com/ram4-dev/herdr-automations)<br><sub>ram4-dev</sub> | Herdr向けの宣言的なcron・インターバル・イベント自動化 | `automation` `bun` `typescript` | 1 | 2026-08-13 |
| [**herdr-callsigns**](https://github.com/reobin/herdr-callsigns)<br><sub>reobin</sub> | すべての herdr ペインに短く覚えやすいコールサインを自動で付けます。あなたとエージェントは、ID の代わりにペイン名を使えるようになります。 | `shell` | 1 | 🔄 2026-09-14 |
| [**herdr-nixos-vm**](https://github.com/Slimydog21/herdr-nixos-vm)<br><sub>Slimydog21</sub> | herdr向けのNixOS VMペイン——Hashimoto流の開発用VMを起動・停止・監視・ssh接続できる。nixos-vm kitが必要 | `shell` | 1 | 2026-08-18 |
| [**herdr-autoname**](https://github.com/thejiajun/herdr-autoname)<br><sub>thejiajun</sub> | 最近のエージェントセッションをもとに、Herdr のワークスペース・タブ・ペインを自動的に命名します。 | `python` | 1 | 🔄 2026-09-22 |
| [**🆕 herdr-codex-autoresume**](https://github.com/UN-9BOT/herdr-codex-autoresume)<br><sub>UN-9BOT</sub> | Herdr plugin that automatically resumes Codex CLI /goal after usage limits reset | `typescript` | 1 | 🔄 2026-09-24 |
| [**herdr-jump-number**](https://github.com/voice0726/herdr-jump-number)<br><sub>voice0726</sub> | Herdr の自動ワークスペースラベルを崩すことなく、ワークスペースやタブにジャンプキーの番号を表示する Herdr プラグインです。 | `typescript` | 1 | 🔄 2026-09-19 |
| [**herdr-agent-title-sync**](https://github.com/winoooops/herdr-agent-title-sync)<br><sub>winoooops</sub> | Claude Code・Codex・Kimi Code・OpenCodeなど各種コーディングエージェント向けの、Herdrペインタイトル自動同期 | `developer-tools` `typescript` | 1 | 2026-08-20 |
| [**🆕 herdr-context-namer**](https://github.com/eabadim/herdr-context-namer)<br><sub>eabadim</sub> | OpenCode経由でペインのコンテキストから、Herdrのタブ・ワークスペース名を自動生成する | `opencode` `python` | 0 | 2026-08-06 |
| [**🆕 herdr-smart-split**](https://github.com/mcostasilva/herdr-smart-split)<br><sub>mcostasilva</sub> | Smart pane splitting for Herdr: automatically split right or down based on pane geometry. | `terminal` `javascript` | 0 | 🔄 2026-09-23 |
| [**herdr-kitchen-brigade**](https://github.com/Operator-create/herdr-kitchen-brigade)<br><sub>Operator-create</sub> | Herdr のコーディングエージェントが完了したときに、リポジトリのチェックを実行します。ローカルレポート、簡潔な失敗フィードバック、Python の依存関係ゼロを実現します。 | `ai-agents` `automation` `developer-tools` `python` `testing` | 0 | 🔄 2026-09-10 |
| [**herdr-worktreeinclude**](https://github.com/untalfranfernandez/herdr-worktreeinclude)<br><sub>untalfranfernandez</sub> | 新しいgit worktreeに必要なgitignore対象のローカルファイル（.env、settings.local.json、フィクスチャなど）を自動配置するHerdrプラグイン。.worktreeincludeファイルにgitignore構文で一度宣言しておけば、Herdrが作るworktreeすべてに自動反映… | `claude-code` `dotenv` `git-worktree` `worktree` | 0 | 2026-07-29 |
| [**🆕 herdr-space-groups**](https://github.com/yojahny55/herdr-space-groups)<br><sub>yojahny55</sub> | herdrプラグイン：Spaceを名前付き・色分けされたグループにまとめる——ピッカーのポップアップ（マウス＋キーボード対応）、サイドバーのグループ見出し、自動並べ替えに対応 | `javascript` | 0 | 2026-08-29 |
| [**numberer-manager**](https://github.com/yuritada/numberer-manager)<br><sub>yuritada</sub> | ワークスペースとタブのラベルに、現在のリスト上の位置（例：「1: space」「1: tab」）を自動で先頭に付ける、軽量なHerdrプラグイン | `python` | 0 | 2026-07-25 |
| [**🆕 herdr-pane-restart**](https://github.com/zap0xfce2/herdr-pane-restart)<br><sub>zap0xfce2</sub> | サーバー起動時に、名前付きペインで設定済みのコマンドを実行する | `python` | 0 | 🔄 2026-09-15 |

<details><summary>この目的にも関係するもの</summary>

- [freethinkel/herdr-plugin-git-worktree-hooks](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks) — git worktreeの作成/削除時にシェルコマンドを実行する——どのリポジトリの外にも置ける、全プロジェクト共通の1つのYAML設定
- [timofey-TK/herdr-worktree-hooks](https://github.com/timofey-TK/herdr-worktree-hooks) — herdrプラグイン：git worktreeの作成・オープン・削除時に、カスタムのセットアップ/後始末コマンドを実行する
- [miko-misa/herdr-portfwd](https://github.com/miko-misa/herdr-portfwd) — リモートマシン上のコーディングエージェント向けの自動SSHポートフォワーディング——エージェントが出力したlocalhost URLをCtrl+クリックすると、同じポートで手元のマシンにページが開く。Herdrプラグイン
- [itisbryan/herdr-gh-checks](https://github.com/itisbryan/herdr-gh-checks) — herdrプラグイン：現在のPRのCIをペインで監視・確認し、CI/マージ状態をサイドバーの行に表示する。Go + Bubble Tea製
- [elkraps/herdr-telegram-notify](https://github.com/elkraps/herdr-telegram-notify) — Herdrエージェントの状態変化に対する、カスタマイズ可能なTelegram通知——ステータスフィルタ、テンプレート、複数チャットへの配信、重複排除、Codex承認ボタン、完了サマリー、組み込みの診断機能に対応
- [Newt6611/herdr-tab-title](https://github.com/Newt6611/herdr-tab-title) — Herdr Tab Titleは、「1. Codex」「2. Terminal」のような、ワークスペース単位できれいに番号付けされた名前にHerdrのタブを自動リネームする。フォーマットはカスタマイズ可能

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-session"></a>

## セッション保存・復元

> 作業を閉じても、あとで同じ状態から再開したい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-resurrect**](https://github.com/ntindle/herdr-resurrect)<br><sub>ntindle</sub> | herdr版tmux-resurrect——ワークスペース・タブ・ペイン・作業ディレクトリ・実行中のプログラムやエージェントをスナップショットし、クラッシュや再起動後に復元する | `crash-recovery` `session-manager` `terminal-multiplexer` `tmux-resurrect` `javascript` | 33 | 2026-08-24 |
| [**session-digger**](https://github.com/taxueseek/session-digger)<br><sub>taxueseek</sub> | 複数環境をまたいだセッション履歴の掘り出しとナレッジ管理。ログを分析。Claude/Grok/Kimi Code/Codex/WorkBuddy/Trae CNなど主要な環境に対応 | `claude-code` `conversation-analysis` `jsonl` `knowledge-management` `log-analysis` | 18 | 🔄 2026-09-23 |
| [**herdr-notes**](https://github.com/alexarthurs/herdr-notes)<br><sub>alexarthurs</sub> | herdr向けの永続化されたMarkdownメモペイン——ワークスペースごとに1つのメモ、プレビュー表示＋編集モード、自動保存で再起動後も残る | `markdown` `notes` `ratatui` `rust` `terminal` | 17 | 2026-07-25 |
| [**herdr-claude-auto-retry**](https://github.com/mo-arvan/herdr-claude-auto-retry)<br><sub>mo-arvan</sub> | AnthropicのレートリミットをやりすごしてClaude Codeを自動的に再開する、herdrネイティブな仕組み——tmuxもシェルラッパーも不要 | `javascript` | 15 | 2026-09-03 |
| [**herdr-session-parker**](https://github.com/iviaxpow3r/herdr-session-parker)<br><sub>iviaxpow3r</sub> | ペイン/タブを一時保管し、対応するエージェントセッションを後で復元できるHerdrプラグイン | `agent-tools` `python` | 12 | 2026-07-03 |
| [**herdr-agent-inbox**](https://github.com/douglascorrea/herdr-agent-inbox)<br><sub>douglascorrea</sub> | herdrのコーディングエージェント用インボックス——セッションタイトル、既読/未読管理、実行時間、ワークスペース単位の集計、再開可能なチャット履歴 | `ai-agents` `terminal` `python` | 9 | 2026-07-28 |
| [**herdr-assist**](https://github.com/walcew/herdr-assist)<br><sub>walcew</sub> | AIコーディングエージェント向けターミナルマルチプレクサHerdrのための、物理デスクパネル——セッションの状態を色で表示し、エージェントが判断を仰ぐために止まるとベルを鳴らす。ESP32-S3 + LVGL、ビルド済みファームウェア付き | `ai-agents` `claude-code` `coding-agents` `embedded` `esp-idf` | 8 | 2026-08-27 |
| [**sheep**](https://github.com/gokay-ai/sheep)<br><sub>gokay-ai</sub> | AIコーディングエージェント向けのUndo。エージェントの各ターンが、復元可能なチェックポイントになる | `ai-agents` `git` `llm` `rust` `tui` | 6 | 2026-08-28 |
| [**herdr-oh-my-agent**](https://github.com/GavinTomlins/herdr-oh-my-agent)<br><sub>GavinTomlins</sub> | oh-my-openagentのサブエージェント委任をそれぞれ専用のHerdrペイン/タブにミラー——セッション状態とスクロールバックを保持したままライブ表示 | `typescript` | 5 | 2026-07-31 |
| [**herdr-hibernate**](https://github.com/bengemine/herdr-hibernate)<br><sub>bengemine</sub> | Herdr上のアイドル状態のコーディングエージェントペイン（Claude Code、Codex、Grok）をハイバネート——メモリを解放し、Enterキーで元のセッションをそのまま再開できる | `claude-code` `python` | 3 | 2026-09-10 |
| [**herdr-pane-id-labeler**](https://github.com/4Born/herdr-pane-id-labeler)<br><sub>4Born</sub> | ペインのラベルを、w1:p2のような公開ペインIDと同期させ続けるHerdrプラグイン | `developer-tools` `terminal` `javascript` | 2 | 2026-07-26 |
| [**herdr-synchronize-panes**](https://github.com/furuhashin/herdr-synchronize-panes)<br><sub>furuhashin</sub> | Herdrプラグイン：現在のタブ内のすべてのペインに1つのコマンドを一斉送信する（tmuxのsynchronize-panes風） | `javascript` | 2 | 2026-07-14 |
| [**herdr_sync**](https://github.com/kamaaina/herdr_sync)<br><sub>kamaaina</sub> | herdrのペインを同期する | `zig` | 2 | 2026-07-01 |
| [**herdr-e2b**](https://github.com/tomasvarga/herdr-e2b)<br><sub>tomasvarga</sub> | 必要なときにgit worktreeを新しいE2Bクラウドサンドボックスへミラーする——未コミットの変更も含めたスナップショットをアップロードするだけで、pushやcloneは不要なherdrプラグイン | `cli` `cloud-dev` `e2b` `git-worktree` `sandbox` | 2 | 2026-07-18 |
| [**herdr-thread-to-tab**](https://github.com/toyamarinyon/herdr-thread-to-tab)<br><sub>toyamarinyon</sub> | 単一ペインのHerdrタブラベルを、Claude CodeやCodexのスレッドタイトルと同期させる | `rust` | 2 | 2026-08-06 |
| [**herdr-stash**](https://github.com/victor-software-house/herdr-stash)<br><sub>victor-software-house</sub> | Herdrのワークスペースをスタッシュ——エージェントを停止しつつ構成と会話内容は保持し、あとでクリック可能な2カラムポップアップから復元できる | `rust` `terminal` `tui` | 2 | 2026-07-29 |
| [**herdr-todos-windows**](https://github.com/aclima01/herdr-todos-windows)<br><sub>aclima01</sub> | herdrエージェントのタスクリスト（TaskCreate/TaskUpdate）をリアルタイムに映し出すパネル。エージェントの計画を追える | `powershell` | 1 | 2026-07-22 |
| [**herdr-agent-auto-naming**](https://github.com/azyu/herdr-agent-auto-naming)<br><sub>azyu</sub> | 検出したすべてのエージェントに、読みやすい 2 単語の名前を付ける Herdr プラグインです。ペインラベルとして永続化されるため、再起動後も引き継がれます。 | `coding-agents` `developer-tools` `terminal` `python` | 1 | 🔄 2026-09-22 |
| [**🆕 herdr-revive**](https://github.com/cantona/herdr-revive)<br><sub>cantona</sub> | Restore Herdr commands, layouts and exact agent sessions with preview, named workspaces and explicit recovery. | `rust` `session-management` `terminal` `terminal-based` `terminal-multiplexer` | 1 | 🔄 2026-09-19 |
| [**mo-herdr**](https://github.com/momentohq/mo-herdr)<br><sub>momentohq</sub> | herdrのペイン内でmoを実行——herdr再起動後のセッション復元、起動アクション、SIGKILLによるクリーンアップに対応 | `python` | 1 | 2026-09-02 |
| [**herdr-undo-close**](https://github.com/pedroloch/herdr-undo-close)<br><sub>pedroloch</sub> | ブラウザのCmd+Shift+Tのように、herdrで閉じたタブを復元——ラベル、分割比率を含むペイン構成、各ペインの作業ディレクトリ、タブの位置までまとめて復元する | `python` | 1 | 2026-07-30 |
| [**herdr-pane-reopen**](https://github.com/rchougule/herdr-pane-reopen)<br><sub>rchougule</sub> | herdr plugin: undo close — reopen the last closed pane, tab or workspace in place and resume its agent | `rust` | 1 | 🔄 2026-09-17 |
| [**attic**](https://github.com/TheThoughtagen/attic)<br><sub>TheThoughtagen</sub> | アイドル状態のAIコーディングセッションを自動的に閉じるが、その前に必ずアーカイブするので後で復元できる | `claude-code` `developer-tools` `python` `session-management` `tui` | 1 | 2026-08-14 |
| [**herdr-agent-pins**](https://github.com/ZingerLittleBee/herdr-agent-pins)<br><sub>ZingerLittleBee</sub> | Herdrのエージェントセッションを、Agentsサイドバーの最上部に永続的にピン留めする | `terminal` `javascript` | 1 | 2026-08-24 |
| [**herdr-codex-resume**](https://github.com/adamwangxx/herdr-codex-resume)<br><sub>adamwangxx</sub> | ネイティブのCodex resumeピッカーを、Herdrのコンテキストを保ったまま新しいスプリットで開く | `codex-cli` `terminal` `shell` | 0 | 2026-08-21 |
| [**herdr-session-title-name**](https://github.com/jovylle/herdr-session-title-name)<br><sub>jovylle</sub> | herdrプラグイン：terminal_title_strippedをタブに永続化する（session_titleだけを上に残し、閉じた後もタブがそれを保持する） | `sidebar` `terminal` `html` | 0 | 2026-08-28 |
| [**resume-globally**](https://github.com/muscaiu/resume-globally)<br><sub>muscaiu</sub> | Herdr プラグイン：Claude Code・Cursor・OpenCode を横断して、最近のセッションを閲覧・再開できます。 | `shell` | 0 | 🔄 2026-09-13 |
| [**herdr-layout**](https://github.com/noviadi/herdr-layout)<br><sub>noviadi</sub> | Herdrのペインレイアウトを保存して再現する。Herdrターミナルマルチプレクサ向けのコンパニオンプラグイン（tmux-resurrect風） | `cli` `terminal` `tmux-resurrect` `shell` | 0 | 2026-08-13 |
| [**🆕 herdr-tab-new**](https://github.com/softwarecrafts/herdr-tab-new)<br><sub>softwarecrafts</sub> | このプロジェクトの herdr ワークスペースで、エージェントセッションを再開または開始します。herdr プラグインであると同時に、herdr の外のターミナルからも使える CLI でもあります。 | `typescript` | 0 | 2026-08-31 |
| [**🆕 live-sync-panes**](https://github.com/wg1k/live-sync-panes)<br><sub>wg1k</sub> | Herdrプラグイン：タブ内のすべてのペインにコマンドを一斉送信、またはキー入力をリアルタイム同期する | `javascript` | 0 | 2026-08-11 |

<details><summary>この目的にも関係するもの</summary>

- [nicosuave/memex](https://github.com/nicosuave/memex) — Claude Code・Codex・Pi・OpenCode・GitHub Copilot・Cursorのトランスクリプトを検索。セッションを再開。トークンを記録
- [mmjang/herdr-omni](https://github.com/mmjang/herdr-omni) — One search for Herdr workspaces, actions, and live or saved Codex & Claude sessions. Fuzzy-find by name, sear…
- [afogel/shepherdr](https://github.com/afogel/shepherdr) — 委任したコーディングエージェントを、監視・再開・引き取りができる可視化されたherdrのペインに追い込むherdrプラグイン
- [AkashJana18/herdr-scratch](https://github.com/AkashJana18/herdr-scratch) — Herdr向けの永続化されたスクラッチパッド。フローティングのユーティリティペインへの足がかりとなる
- [hxreborn/herdr-transcripts](https://github.com/hxreborn/herdr-transcripts) — Search your coding-agent sessions, past and live, by any word you remember, then jump to them or resume them
- [KokiKono/herdr-kanban](https://github.com/KokiKono/herdr-kanban) — タスクをherdrのタブに紐付けるターミナル上のカンバンボード。SQLiteに保存される
- [blaxel-ai/herdr-blaxel-sandbox-plugin](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin) — Herdrから、永続化されたBlaxel Sandbox上でコーディングエージェントを実行する
- [ppggff/herdr-plugin](https://github.com/ppggff/herdr-plugin) — 各Herdrペインに適したmacOSの入力方式（IME）を自動的に記憶・復元する
- [voodootikigod/adlc-herdr](https://github.com/voodootikigod/adlc-herdr) — ADLC向けのherdrプラグイン——ペインごとのフェーズ/チケット/ゲートの状態、バックログボード、ゲートアクション、adlc-fleetの実行状況の可視化に対応。voodootikigod/adlc/plugins…
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — JavaScript/TypeScript向けにHerdrのworktreeを自動でブートストラップ——ロックファイルを考慮したインストールと、安全な環境ファイルの復元に対応
- [shadowfax92/herdr-scratch](https://github.com/shadowfax92/herdr-scratch) — 非公開のtmuxセッションを裏側で使う、永続化されたペインごとのHerdrスクラッチポップアップ
- [UN-9BOT/herdr-codex-autoresume](https://github.com/UN-9BOT/herdr-codex-autoresume) — Herdr plugin that automatically resumes Codex CLI /goal after usage limits reset
- [damianpoole/herdr-opencode-sessions](https://github.com/damianpoole/herdr-opencode-sessions) — 過去のOpenCodeセッションを、タイトル・プロジェクト・パス・日付・トランスクリプトの内容でファジー検索できるHerdrプラグイン——会話プレビュー付きで、現在または新しいワークスペースでセッションを再開・フォーク…
- [goofansu/herdr-hunk](https://github.com/goofansu/herdr-hunk) — 一時的なHunkオーバーレイを開く、素早いHerdrレビューアクションを提供する。Hunkを終了するとオーバーレイが閉じ、ワークスペースが元に戻る

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-naming"></a>

## タイトル・命名・見た目

> タブ名やターミナルタイトルを自動で分かりやすくしたい / 見た目を変えたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-tab-smart-rename**](https://github.com/iurysza/herdr-tab-smart-rename)<br><sub>iurysza</sub> | Herdrのワークスペース名・タブ名を、コンテキストに応じて自動生成する | `ai` `bun` `terminal` `typescript` | 77 | 🔄 2026-09-21 |
| [**herdr-flock**](https://github.com/ragamo/herdr-flock)<br><sub>ragamo</sub> | AIコーディングエージェントを、見下ろし視点の牧場に住むピクセルアートの羊として可視化するherdrプラグイン | `cli` `ratatui` `rust` `tui` | 38 | 2026-08-31 |
| [**herdr-window-title-sync**](https://github.com/rjyo/herdr-window-title-sync)<br><sub>rjyo</sub> | ワークスペース・タブ・エージェントセッションからターミナルのタイトルを同期する（Moshiと併用可） | `moshi` `terminal-title` `javascript` | 36 | 2026-06-26 |
| [**herdr-pet**](https://github.com/nikok6/herdr-pet)<br><sub>nikok6</sub> | herdrのペインにいる小さなデスクペット——エージェントと一緒にタイプし、待ち、お祝いする。任意のCodex petに対応 | `rust` | 14 | 2026-08-26 |
| [**herdr-icon-agent-ui**](https://github.com/qintmb/herdr-icon-agent-ui)<br><sub>qintmb</sub> | Herdrのサイドバーに、縦位置を揃えたモノクロのAgentアイコンを描画する。ターミナルのキャップハイトに合わせて不均一にスケーリングされたカスタムフォントで描画され、小さな四角として表示される代わりにエージェント名・タブ・ワークスペースラベルにきれいに揃う | `python` | 12 | 🔄 2026-09-25 |
| [**herdr-theme-picker**](https://github.com/qintmb/herdr-theme-picker)<br><sub>qintmb</sub> | ターミナルの配色スキームと自分好みのカスタマイズに基づいた、herdr UI向けのテーマピッカー | `shell` | 12 | 2026-08-31 |
| [**herdr-canvas**](https://github.com/aorumbayev/herdr-canvas)<br><sub>aorumbayev</sub> | herdrのエージェント向けの、マウスで操作できるASCII図キャンバス——TUI上で描き、構造化されたJSONを共有し、AIに編集させることもできる | `agentic-ai` `agents` `ai-agents` `ascii-art` `bubbletea` | 8 | 2026-08-31 |
| [**herdr-claude-session-title**](https://github.com/bcihanc/herdr-claude-session-title)<br><sub>bcihanc</sub> | Herdrプラグイン：Claude Codeのセッションタイトル（/renameまたは自動要約）をherdrのペインのメタデータタイトルに反映する | `shell` | 8 | 2026-07-11 |
| [**herdr-pet**](https://github.com/allmight-ai/herdr-pet)<br><sub>allmight-ai</sub> | Herdr向けのコンパニオンV-Pet——あなたのコーディングエージェントの様子を映し出す | `companion` `rust` `v-pet` | 6 | 2026-08-20 |
| [**herdr-ghostty-tab-title**](https://github.com/wjarka/herdr-ghostty-tab-title)<br><sub>wjarka</sub> | herdrプラグイン：Ghosttyのタブタイトルに、エージェントの状態別件数（ブロック中/完了/作業中/アイドル）を色分けして表示する | `ai-agents` `ghostty` `terminal` `python` | 6 | 2026-08-04 |
| [**herdr-pixel-office**](https://github.com/devangchhajed/herdr-pixel-office)<br><sub>devangchhajed</sub> | Watch your AI coding agents work as pixel-art characters in a tiny top-down office — a herdr plugin | `typescript` | 5 | 🔄 2026-09-21 |
| [**herdr-town**](https://github.com/Efeguclu1/herdr-town)<br><sub>Efeguclu1</sub> | Herdrのコーディングエージェントを、8bit風の街として眺める。街を離れずに、エージェントの発言を読んで返答できる | `ai-agents` `pixel-art` `terminal` `tui` `javascript` | 5 | 2026-08-08 |
| [**herdr-agent-titler**](https://github.com/killerz3/herdr-agent-titler)<br><sub>killerz3</sub> | 外部 API キーを使わず、ローカルの agy・claude・codex・opencode の各ハーネスを使って Herdr のタブに自動でタイトルを付けます。 | `antigravity` `claude-code` `python` | 5 | 2026-09-03 |
| [**herdr-in-your-face**](https://github.com/JYasha11/herdr-in-your-face)<br><sub>JYasha11</sub> | AIエージェントをブロックされたまま放置すると、巨大なASCIIアートの顔が叫んでくる。無視するほど段階的にエスカレートする | `javascript` | 4 | 2026-07-10 |
| [**herdr-auto-namer**](https://github.com/kakigakki/herdr-auto-namer)<br><sub>kakigakki</sub> | herdr向けのChatGPT風自動命名：エージェントにはClaudeのセッションタイトルを、ワークスペースには作業ディレクトリ名を付ける | `claude-code` `python` | 4 | 2026-08-27 |
| [**herdr-tab-rename**](https://github.com/lmilojevicc/herdr-tab-rename)<br><sub>lmilojevicc</sub> | 各Herdrタブを、フォーカス中のペインの作業ディレクトリ名に自動でリネームする。手動でリネームしたタブはそのまま残る | `go` | 4 | 2026-07-31 |
| [**herdr-questmancer**](https://github.com/opsydyn/herdr-questmancer)<br><sub>opsydyn</sub> | Herdrのコーディングエージェントのための、居心地の良い16bit風冒険者ギルド。作業中のエージェントはダンジョンに潜り、ブロックされたエージェントは助言を求め、完了した仕事は戦利品を持って帰ってくる | `coding-agents` `pixel-art` `ratatui` `tui` `rust` | 4 | 2026-09-09 |
| [**herdr-nerd-font-tab-name**](https://github.com/rohankewal/herdr-nerd-font-tab-name)<br><sub>rohankewal</sub> | herdrのタブにNerd Fontアイコンを付ける——joshmedeski/tmux-nerd-font-window-nameのherdr移植版 | `nerd-fonts` `python` `terminal` `tui` | 4 | 2026-07-31 |
| [**herdr-powershell-title-sync**](https://github.com/aclima01/herdr-powershell-title-sync)<br><sub>aclima01</sub> | window-title-syncのWindows/PowerShell版：ターミナルのタイトルを、フォーカス中のherdrセッションに同期する | `powershell` | 2 | 2026-07-20 |
| [**herdr-pane-autorename**](https://github.com/b12o/herdr-pane-autorename)<br><sub>b12o</sub> | 現在実行中のプロセス名で、ペインを自動的にリネームする Herdr プラグインです。 | `shell` | 2 | 2026-09-07 |
| [**herdr-titles**](https://github.com/davidolrik/herdr-titles)<br><sub>davidolrik</sub> | 追従し続けるHerdrのタイトル。herdr-titlesは、AIエージェントのライブなセッションタイトルも含め、実際に動いているものに合わせてタブとウィンドウの名前を付け、ワークスペース・タブ・エージェントの要対応件数・シェル環境から、小さなHCLテンプレート経由でウィンドウタイトルを組み立てる。即座に反映され、C… | `ai-assisted` `go` | 2 | 2026-09-06 |
| [**herdr-english-coach**](https://github.com/GranamyrBR/herdr-english-coach)<br><sub>GranamyrBR</sub> | herdrプラグイン：色分けされた英語修正ボード——作業中、コーディングエージェントが文法や開発用語の修正をリアルタイムでサイドペインに記録する | `english` `language-learning` `shell` | 2 | 2026-07-06 |
| [**herdr-ai-tab-name**](https://github.com/ndom91/herdr-ai-tab-name)<br><sub>ndom91</sub> | ローカルLLMを使ってHerdrのタブ名を自動命名する | `local-llm` `python` | 2 | 🔄 2026-09-19 |
| [**herdr-agent-tab-titles**](https://github.com/ajaykumarMohite/herdr-agent-tab-titles)<br><sub>ajaykumarMohite</sub> | Renames each Herdr tab to the task its coding agent is working on | `claude-code` `developer-tools` `terminal` `python` | 1 | 🔄 2026-09-17 |
| [**herdr-git-tab-name**](https://github.com/blurname/herdr-git-tab-name)<br><sub>blurname</sub> | フォーカス中のペインのGitブランチ名にタブをリネームするHerdrプラグイン | `shell` | 1 | 2026-07-06 |
| [**herdr-hermes-session-title**](https://github.com/btorresgil/herdr-hermes-session-title)<br><sub>btorresgil</sub> | Hermes Agentのセッションタイトルを、Herdrのサイドバーに表示する | `python` | 1 | 2026-08-07 |
| [**🆕 herdr-plugin-omp-state**](https://github.com/dk3775/herdr-plugin-omp-state)<br><sub>dk3775</sub> | Report omp agent state to Herdr from its terminal title, for panes the official integration does not cover | `coding-agents` `omp` `python` | 1 | 🔄 2026-09-24 |
| [**herdr-tab-smart-rename-rs**](https://github.com/EmmetZ/herdr-tab-smart-rename-rs)<br><sub>EmmetZ</sub> | _(説明なし)_ | `rust` | 1 | 2026-08-24 |
| [**pane-identity**](https://github.com/Ghost-LZW/pane-identity)<br><sub>Ghost-LZW</sub> | エージェントを一切変更することなく、Herdr にペイン ID・ホスト名・ラベルを表示します。 | `python` `terminal` | 1 | 2026-09-05 |
| [**herdr-emoji-time**](https://github.com/hotnugs/herdr-emoji-time)<br><sub>hotnugs</sub> | Herdr のスペース・エージェント・タブに絵文字を付けられます。ターミナルにちょっとした遊び心を。 | `emoji` `terminal` `tui` `python` | 1 | 🔄 2026-09-12 |
| [**herdr-chromatic-spaces**](https://github.com/jackfrancisdalton/herdr-chromatic-spaces)<br><sub>jackfrancisdalton</sub> | 各Herdr Spaceに独自の色と絵文字を付ける——サイドバーの色付きドット、エージェントのグループ化、Space切り替え時の任意のクローム着色に対応 | `python` | 1 | 2026-08-22 |
| [**herdr-tab-title-sync**](https://github.com/lucasleon2107/herdr-tab-title-sync)<br><sub>lucasleon2107</sub> | AIエージェントの会話タイトルにタブ名を同期するherdrプラグイン | `ai-agents` `claude-code` `terminal` `tmux` `shell` | 1 | 2026-08-04 |
| [**herdr-agent-smart-rename**](https://github.com/malone-c/herdr-agent-smart-rename)<br><sub>malone-c</sub> | 各herdrエージェントセッションの名前を、実際にやっていることから付ける | `python` | 1 | 2026-08-14 |
| [**ZimMux**](https://github.com/Mr-Destroyer/ZimMux)<br><sub>Mr-Destroyer</sub> | ZimMux：herdr の Ink スタイルを模した、1 ファイルの tmux テーマです。ラベンダー色のフォーカス枠、控えめなステータスバー、プレフィックス不要の Alt キーバインド、バックアップ付きのワンコマンドインストールに対応。プラグイン不要。 | `agent` `agent-framework` `agent-workflows` `agentic-ai` `agentic-workflow` | 1 | 🔄 2026-09-15 |
| [**herdr-session-sync**](https://github.com/nengqi/herdr-session-sync)<br><sub>nengqi</sub> | Claude Code・Codex・エージェントのセッション名を、Herdrのペインラベル・PTYのウィンドウタイトル・モバイルコンパニオンアプリ（Heeler）にまたがって自動同期する | `agent` `claude-code` `codex` `heeler` `terminal-multiplexer` | 1 | 🔄 2026-09-15 |
| [**herdr-nerd-font-tab-name-windows**](https://github.com/Only-Moon/herdr-nerd-font-tab-name-windows)<br><sub>Only-Moon</sub> | herdr-nerd-font-tab-nameのWindows移植版：herdrのタブにNerd Fontアイコンを表示し、Windows・macOS・Linuxをクロスプラットフォームでサポート、フォルダに応じたアイコン解決にも対応 | `herdr-windows` `icons` `nerd-fonts` `python` `title` | 1 | 2026-08-10 |
| [**🆕 herdr-claude-tab-rename**](https://github.com/oronbz/herdr-claude-tab-rename)<br><sub>oronbz</sub> | Herdr plugin: keep each tab named after its Claude Code session title (/rename or auto title) | `shell` | 1 | 🔄 2026-09-23 |
| [**herdr-workspace-renamer**](https://github.com/ryanlewis/herdr-workspace-renamer)<br><sub>ryanlewis</sub> | herdrプラグイン：エージェントのセッション名をワークスペースのラベルに同期する | `javascript` | 1 | 🔄 2026-09-24 |
| [**herdr-pomodoro**](https://github.com/sazardev/herdr-pomodoro)<br><sub>sazardev</sub> | ミニマルでエレガント、テーマに合わせて変化する Herdr 用のポモドーロタイマープラグインです。 | `rust` | 1 | 2026-09-08 |
| [**herdr-claude-tab-title**](https://github.com/tmn73/herdr-claude-tab-title)<br><sub>tmn73</sub> | 各Claude Codeのセッションタイトルとエージェントの状態を、対応するHerdrのタブに反映する | `claude-code` `tabs` `terminal` `typescript` | 1 | 2026-09-07 |
| [**herdr-stack-icon**](https://github.com/bonkey/herdr-stack-icon)<br><sub>bonkey</sub> | Herdr プラグイン：リポジトリのファイルから検出した技術スタックのアイコン（🍏 🤖 🦀 🐹 🟩 🐍）を、各ワークスペースの横に表示します。 | `python` | 0 | 🔄 2026-09-10 |
| [**🆕 herdr-tabline**](https://github.com/btj93/herdr-tabline)<br><sub>btj93</sub> | 安全なテンプレートとプロジェクトを認識するプロファイルで、Herdr のタブラベルを描画します。 | `golang` `tabline` `terminal` `tui` `go` | 0 | 2026-09-04 |
| [**🆕 herdr-tab-title-from-terminal**](https://github.com/christiangroth/herdr-tab-title-from-terminal)<br><sub>christiangroth</sub> | すべてのHerdrタブに、中で動いているエージェントのターミナルタイトルをそのまま名前として付ける。Claude Codeで/renameを1回実行すれば、セッションとタブの両方に名前が付く。手動で名前を付けたタブには手を出さない | `python` | 0 | 2026-08-25 |
| [**🆕 herdr-pane-id-border**](https://github.com/Haichiu/herdr-pane-id-border)<br><sub>Haichiu</sub> | ペインの境界線に正規のペイン ID を表示する、ミニマルな Herdr プラグインです。 | `shell` | 0 | 2026-09-02 |
| [**🆕 herdr-sheep**](https://github.com/huketo/herdr-sheep)<br><sub>huketo</sub> | Herdr のコーディングエージェントを、アニメーションする ASCII アートの羊の群れとして眺められます。 | `ascii-art` `rust` `tui` | 0 | 2026-09-04 |
| [**🆕 herdr-tab-title**](https://github.com/Newt6611/herdr-tab-title)<br><sub>Newt6611</sub> | Herdr Tab Titleは、「1. Codex」「2. Terminal」のような、ワークスペース単位できれいに番号付けされた名前にHerdrのタブを自動リネームする。フォーマットはカスタマイズ可能 | `rust` | 0 | 2026-07-09 |
| [**🆕 tab-blank-number**](https://github.com/riq0h/tab-blank-number)<br><sub>riq0h</sub> | herdrのデフォルトの数字タブラベル（1、2、3…）を空白にするherdrプラグイン | `javascript` | 0 | 2026-07-19 |
| [**🆕 herdr-ghostty-theme-sync**](https://github.com/themuuln/herdr-ghostty-theme-sync)<br><sub>themuuln</sub> | herdrのテーマとサイドバーの配色を、使用中のGhosttyのテーマに合わせる——herdr再起動をまたいでもサイドバーのトークン（配色設定）を維持する。herdr.dev製プラグイン | `python` | 0 | 2026-08-12 |

<details><summary>この目的にも関係するもの</summary>

- [kryptamine/herdr-auto-title](https://github.com/kryptamine/herdr-auto-title) — Automatically name Herdr tabs and panes from your current work, Git branch, terminal activity, and Claude Cod…
- [qu8n/herdr-automatic-rename](https://github.com/qu8n/herdr-automatic-rename) — エージェントとシェルをすばやく切り替えられる、スマートな herdr タブ名です。
- [sh1ma/herdr-auto-title](https://github.com/sh1ma/herdr-auto-title) — Claude CodeとCodexの会話内容から、herdrのタブタイトルを自動生成する
- [IvoryHeart/herdr-world](https://github.com/IvoryHeart/herdr-world) — Herdr World——Herdr向けのマルチサーフェスなWeb体験
- [wyattjoh/herdr-plugin-renamer](https://github.com/wyattjoh/herdr-plugin-renamer) — エージェントへの最初のプロンプトから、自動生成されたherdrのworktreeブランチとワークスペースをリネームする（デバイス上のApple FoundationModelsまたはCodexを利用）
- [ythx-101/herdr-social-glass](https://github.com/ythx-101/herdr-social-glass) — macOS版Herdr向けの、スクリーンショット映えするSocial Glassテーマ＆ワークフロープラグイン
- [aarsh21/herdr-tab-title](https://github.com/aarsh21/herdr-tab-title) — Herdr向けの、tmux風タブタイトルの自動設定
- [funsaized/herdr-mise](https://github.com/funsaized/herdr-mise) — プロンプトではなく、パス（成功）を積み重ねよう 🧑‍🍳 herdr 上でエージェントを可視化するツールです。意図的に小さなフットプリントに抑えています。
- [suisya-systems/herdr-agent-office](https://github.com/suisya-systems/herdr-agent-office) — エージェント群をピクセルアートのオフィスとして表示するherdrプラグイン。誰が作業中で、誰が詰まっているかが分かり、そこにジャンプできる
- [maedana/herdr-whereami](https://github.com/maedana/herdr-whereami) — 今どこにいるかを示すよう、タブを自動でリネームするHerdrプラグイン——gitリポジトリ内なら「リポジトリ名/ブランチ名」のように表示
- [azyu/herdr-agent-auto-naming](https://github.com/azyu/herdr-agent-auto-naming) — 検出したすべてのエージェントに、読みやすい 2 単語の名前を付ける Herdr プラグインです。ペインラベルとして永続化されるため、再起動後も引き継がれます。
- [dev-shimada/herdr-auto-tab-name](https://github.com/dev-shimada/herdr-auto-tab-name) — herdrプラグイン：タブに現在のディレクトリ名を自動で付ける
- [winoooops/herdr-agent-title-sync](https://github.com/winoooops/herdr-agent-title-sync) — Claude Code・Codex・Kimi Code・OpenCodeなど各種コーディングエージェント向けの、Herdrペインタイトル自動同期
- [jovylle/herdr-session-title-name](https://github.com/jovylle/herdr-session-title-name) — herdrプラグイン：terminal_title_strippedをタブに永続化する（session_titleだけを上に残し、閉じた後もタブがそれを保持する）
- [KazBrekker1/herdr-hasr](https://github.com/KazBrekker1/herdr-hasr) — Hasr（حصر — 「列挙・完全な集計」の意）——herdr向けのgoto風ポップアップ切り替えツール：エージェント・タブ・スペースの切り替え・リネーム・削除・作成ができ、完了状況もリアルタイムに追跡する

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-text"></a>

## テキスト・URL 抽出

> 画面に出ている文字列やパス・URL を、マウスなしで拾いたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-pluck**](https://github.com/rmarganti/herdr-pluck)<br><sub>rmarganti</sub> | Herdrのペインからパターンにマッチした文字列をすばやくコピーする | `rust` | 24 | 🔄 2026-09-21 |
| [**herdr-tiny-fingers**](https://github.com/hotchpotch/herdr-tiny-fingers)<br><sub>hotchpotch</sub> | Herdr向けの、tmux-fingers風の画面上コピーヒント表示 | `tools` `rust` | 15 | 🔄 2026-09-15 |
| [**🆕 herdr-fingers**](https://github.com/nathan-poncet/herdr-fingers)<br><sub>nathan-poncet</sub> | 👉 tmux-fingers for Herdr — type a short hint to copy, paste or open any path, URL, hash or number on screen. Rust, Clean Architecture. | `clean-architecture` `clipboard` `rust` `terminal` `tmux-fingers` | 7 | 🔄 2026-09-24 |
| [**herdr-scratchpad**](https://github.com/vjeantet/herdr-scratchpad)<br><sub>vjeantet</sub> | タブごとに1つのバッファでプロンプトを準備し、1キーでエージェントの入力欄に流し込む | `clipboard` `ratatui` `rust` `scratchpad` `terminal` | 5 | 2026-08-31 |
| [**herdr-flash**](https://github.com/youguanxinqing/herdr-flash)<br><sub>youguanxinqing</sub> | Herdrのペイン向けの、flash.nvim風の検索・選択・ヤンク | `rust` `terminal` | 5 | 🔄 2026-09-16 |
| [**herdr-fingers**](https://github.com/hitaishi2222/herdr-fingers)<br><sub>hitaishi2222</sub> | Fingers to clipboard：現在のペインから情報を選び取る、スマートなオーバーレイ | `python` | 4 | 2026-07-16 |
| [**herdr-agent-copy-paste-fork**](https://github.com/calebcauthon/herdr-agent-copy-paste-fork)<br><sub>calebcauthon</sub> | コピー＆ペーストだけでフォークできる、あるいはホットキーで新しいペインにフォークする | `claude-code` `codex` `shell` | 3 | 2026-07-24 |
| [**herdr-paste-image**](https://github.com/ddfonseca/herdr-paste-image)<br><sub>ddfonseca</sub> | クリップボードの画像をherdrのペインにファイルパスとして貼り付ける——tmux-paste-imageのherdr移植版 | `shell` | 3 | 2026-07-30 |
| [**herdr-copy-search**](https://github.com/qq88976321/herdr-copy-search)<br><sub>qq88976321</sub> | herdrのスクロールバックに対する正規表現・copycatパターン検索とextraktoによるトークン抽出、tmux風のコピーモード（OSC 52）に対応 | `copy-mode` `rust` `terminal` `tmux` | 3 | 2026-08-04 |
| [**herdr-ferry**](https://github.com/wavrin/herdr-ferry)<br><sub>wavrin</sub> | SSH経由で、Herdrのbox（マシン）とノートPCの間でファイルとクリップボードをやり取りする——クラウドバケット不要 | `rust` | 3 | 2026-08-29 |
| [**herdr-s3-clipboard**](https://github.com/jagzmz/herdr-s3-clipboard)<br><sub>jagzmz</sub> | S3互換ストレージを使い、Herdrからクリップボードの画像を再利用可能な公開URLまたは署名付きURLとして公開する | `aws-s3` `clipboard` `cloudflare-r2` `developer-tools` `image-publishing` | 2 | 2026-07-16 |
| [**scoopr**](https://github.com/TawfiqAbubaker/scoopr)<br><sub>TawfiqAbubaker</sub> | マウスを使わずに何でもターミナルへコピーできる Herdr プラグインです。tmux の extrakto に着想を得ています。 | `rust` | 2 | 2026-09-06 |
| [**herdr-scrollback-capture**](https://github.com/alexjsp/herdr-scrollback-capture)<br><sub>alexjsp</sub> | フォーカス中のペインのスクロールバックを、HTMLまたはテキストとしてデスクトップに保存するHerdrプラグイン | `shell` | 1 | 2026-06-30 |
| [**herdr-link-browser**](https://github.com/bonkey/herdr-link-browser)<br><sub>bonkey</sub> | Herdr プラグイン：http(s) の URL を Ctrl クリックすると、ペインの隣にスプリットした terminal-browser で開きます。 | `terminal-browser` `shell` | 1 | 2026-09-07 |
| [**herdr-fleece**](https://github.com/dmazlum/herdr-fleece)<br><sub>dmazlum</sub> | Herdr でエージェントの最後の回答を切り取り、コピー・保存・送信できます。 | `typescript` | 1 | 🔄 2026-09-11 |
| [**🆕 herdr-paste-image**](https://github.com/grooni/herdr-paste-image)<br><sub>grooni</sub> | Paste images from clipboard into herdr panes (Codex, Gemini CLI) — F8 + clipboard cleanup tools (F9/F10) | `shell` | 1 | 🔄 2026-09-21 |
| [**herdr-leap**](https://github.com/RooseveltAdvisors/herdr-leap)<br><sub>RooseveltAdvisors</sub> | Herdrのターミナルマルチプレクサ向けの、EasyMotion/leap風の文字ジャンプ＋選択コピー | `easymotion` `rust` `terminal` `tui` | 1 | 2026-07-24 |
| [**herdr-copy-hints**](https://github.com/rotemb-wond/herdr-copy-hints)<br><sub>rotemb-wond</sub> | Herdr向けの、tmux-fingers風キーボードコピーヒント：パス・GitのSHA・URLなどに対応 | `clipboard` `developer-tools` `keyboard-navigation` `productivity` `terminal` | 1 | 2026-07-23 |
| [**herdr-copy-pane-id**](https://github.com/wine-fall/herdr-copy-pane-id)<br><sub>wine-fall</sub> | herdrプラグイン：フォーカス中のペインのIDをクリップボードにコピーする、または全ペインのIDを枠に表示する | `cli` `terminal` `python` | 1 | 2026-08-24 |
| [**herdr-translate**](https://github.com/zackshen/herdr-translate)<br><sub>zackshen</sub> | herdrプラグイン：マウスで選択したターミナルのテキストを、中央のポップオーバーで翻訳する | `rust` | 1 | 2026-08-25 |

<details><summary>この目的にも関係するもの</summary>

- [nicosuave/memex](https://github.com/nicosuave/memex) — Claude Code・Codex・Pi・OpenCode・GitHub Copilot・Cursorのトランスクリプトを検索。セッションを再開。トークンを記録
- [iurysza/termscope](https://github.com/iurysza/termscope) — 分割ペインで、ターミナル画面に表示されているファイルやリンクを開く
- [junghan0611/entwurf](https://github.com/junghan0611/entwurf) — Herdr and tmux sibling AI sessions: pi, Claude Code, Codex, Copilot, OMP and Antigravity can message and spaw…
- [pinkpixel-dev/quota](https://github.com/pinkpixel-dev/quota) — GitHub Copilot・Codex・Claude Code・Antigravity・Kiro・Grok・Cursor にまたがる AI 利用状況を追跡できる、デスクトップアプリ・VSCode 拡張・Herdr プ…
- [jlimas/herdr-worktree-seed](https://github.com/jlimas/herdr-worktree-seed) — コピーオンライトのnode_modulesと設定可能なローカルdotfilesを、新しいworktreeに投入するHerdrプラグイン
- [tanshio/herdr-worktreeinclude](https://github.com/tanshio/herdr-worktreeinclude) — Herdrプラグイン：.worktreeincludeにマッチするgit管理外ファイルを、新しく作成されたworktreeにコピーする
- [khatriafaz/herdr-plugin-cow-worktree](https://github.com/khatriafaz/herdr-plugin-cow-worktree) — Herdr plugin for strict copy-on-write Git worktrees that include ignored local files
- [eightHundreds/herdr-worktreeinclude](https://github.com/eightHundreds/herdr-worktreeinclude) — Herdrプラグイン：.worktreeincludeで指定したgit管理外ファイルを、新しいworktreeにコピーする
- [shadowfax92/herdr-comments](https://github.com/shadowfax92/herdr-comments) — コピーしたHerdrのターミナル出力に注釈を付け、ペインごとのコメントを収集してNeovimでレビューできる
- [crexi/herdr-worktree-copy](https://github.com/crexi/herdr-worktree-copy) — .worktree-copyマニフェストに基づき、worktreeローカルファイルをコピー・シンボリックリンクするHerdrプラグイン
- [Feasy01/herdr-allow](https://github.com/Feasy01/herdr-allow) — herdrプラグイン：.herdr-allowの許可リストを使って、gitignore対象のファイル（.env、シークレット、ローカル設定）を新しいworktreeすべてにコピーする
- [tupton/herdr-worktree-include](https://github.com/tupton/herdr-worktree-include) — herdr が作成した git worktree に、未追跡のファイルをシンボリックリンクまたはコピーします。
- [zerodice0/herdr-plugin-worktree-bootstrap](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap) — 新しいHerdrのGit worktreeに、無視されているローカルファイルを安全にコピーし、セットアップコマンドを実行する
- [heyfirst/herdr-worktree-include](https://github.com/heyfirst/herdr-worktree-include) — herdr plugin that copies .worktreeinclude files into new worktrees. Built with Bun. 🍞
- [scoussens-nthplusio/herdr-worktree-include](https://github.com/scoussens-nthplusio/herdr-worktree-include) — リポジトリの.worktreeincludeを使って、.envなどgit管理外のファイルを新しいHerdr worktreeにコピーする——Claude Codeが使うのと同じファイル・同じルール
- [willian/herdr-fzf-url](https://github.com/willian/herdr-fzf-url) — フォーカス中のペインから`fzf`でURLを選び、開く・コピーする

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-meta"></a>

## プラグイン管理・開発

> プラグイン自体を管理したい / 自分で作りたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-plus**](https://github.com/cloudmanic/herdr-plus)<br><sub>cloudmanic</sub> | herdr向けの拡張機能。正式なプラグインとして構築されたツール集（プロジェクト管理とクイックアクション）でherdrをより良くする | `go` | 332 | 2026-09-04 |
| [**herdr-plugin-manager**](https://github.com/speardragon/herdr-plugin-manager)<br><sub>speardragon</sub> | ポップアップからherdrのプラグインを管理——インストール・更新・有効/無効化・アンインストール、herdr-pluginマーケットプレイスの閲覧も可能。推奨キー：prefix+p | `plugin-manager` `tui` `shell` | 40 | 🔄 2026-09-21 |
| [**herdr-lazy**](https://github.com/natori-hrj/herdr-lazy)<br><sub>natori-hrj</sub> | Declarative, reproducible plugin manager and curated distro for Herdr — one list, a lockfile, and a safe manage pane. | `cli` `lockfile` `plugin-manager` `rust` `terminal` | 25 | 🔄 2026-09-25 |
| [**house-of-herdr**](https://github.com/alasano/house-of-herdr)<br><sub>alasano</sub> | Herdr向けのプラグイン集——Work Louder Codex Micro上にエージェントのステータスランプと操作パネルを表示するCodex Microを含む | `codex-micro` `work-louder` `typescript` | 8 | 2026-08-13 |
| [**herdr-plugins-labs**](https://github.com/hmu332233/herdr-plugins-labs)<br><sub>hmu332233</sub> | Herdr向けの実験的プラグイン集——ここで育て、成熟したら独立したリポジトリに卒業する | `labs` `javascript` | 2 | 🔄 2026-09-23 |
| [**herdr-plugin-rust**](https://github.com/Newt6611/herdr-plugin-rust)<br><sub>Newt6611</sub> | Herdrのプラグインを構築するためのRustアプリケーションフレームワーク | `rust` | 2 | 2026-07-09 |
| [**herdr-plugins**](https://github.com/alastairsounds/herdr-plugins)<br><sub>alastairsounds</sub> | herdr向けのプラグイン集 | `rust` | 1 | 2026-08-28 |
| [**herdr-client**](https://github.com/vika2603/herdr-client)<br><sub>vika2603</sub> | Herdr のソケット API 向けの Go クライアント兼プラグインツールキットです。全 102 メソッド、セッションミラー、プラグインランタイムを備え、herdr が出力するスキーマから生成されています。herdr 0.9.0、プロトコル 22 対応。 | `coding-agents` `go` `golang` `sdk` `terminal-multiplexer` | 1 | 🔄 2026-09-23 |

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-other"></a>

## その他・ユーティリティ

> 上のどれにも当てはまらない便利もの

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**terminal-browser**](https://github.com/zenbu-labs/terminal-browser)<br><sub>zenbu-labs</sub> | ターミナルの中のブラウザ | `browser` `claude-code` `claude-code-plugin` `claude-skills` `cli` | 3386 | 🔄 2026-09-20 |
| [**herdr-lantern**](https://github.com/aigorahub/herdr-lantern)<br><sub>aigorahub</sub> | Lantern（Elves製）。Herdrプラグイン：群れは野に出ている——Lanternは、誰があなたを必要としていて、何に向けて作業しているのかを照らし出す | `shell` | 67 | 🔄 2026-09-24 |
| [**herdr-gui**](https://github.com/undivisible/herdr-gui)<br><sub>undivisible</sub> | herdr 用の GUI サーフェスに加え、その他の機能も備えます。crepuscular gpui で構築されています。 | `crepuscularity` `gpui` `rust` | 19 | 2026-07-27 |
| [**herdr-commandcode-plugin**](https://github.com/TheMetalStorm/herdr-commandcode-plugin)<br><sub>TheMetalStorm</sub> | CommandcodeをHerdrに統合する | `cli` `commandcode` `herdr-integration` `shell` | 13 | 2026-07-30 |
| [**herdr-plugins-directory**](https://github.com/MIDO-ruby7/herdr-plugins-directory)<br><sub>MIDO-ruby7</sub> | やりたいことからherdrプラグインを探せるリンク集 | `python` | 11 | 🔄 2026-09-25 |
| [**neon-herdr**](https://github.com/neon-solutions/neon-herdr)<br><sub>neon-solutions</sub> | Neon公式のHerdrプラグイン | `typescript` | 11 | 2026-08-06 |
| [**herdr-plugin-cmux**](https://github.com/lachieh/herdr-plugin-cmux)<br><sub>lachieh</sub> | herdrが管理するすべてのエージェントを、cmuxのサイドバーにそれぞれ独立した行としてミラーする——ステータスピルとクリックでジャンプできるタスク行付き | `javascript` | 10 | 2026-07-01 |
| [**herdr-freebuff-plugin**](https://github.com/TheMetalStorm/herdr-freebuff-plugin)<br><sub>TheMetalStorm</sub> | Herdr向けのFreebuffライフサイクル統合プラグイン——ファイルのポーリングとPTY内容のスクレイピングで、アイドル/作業中/ブロック中の状態を報告する | `cli` `freebuff` `herdr-integration` `shell` | 6 | 2026-07-22 |
| [**wave-tui**](https://github.com/takemo101/wave-tui)<br><sub>takemo101</sub> | 作業中に流せる、静かなターミナルラジオ | `rust` | 5 | 2026-07-20 |
| [**herdr-memory**](https://github.com/jatingargiitk/herdr-memory)<br><sub>jatingargiitk</sub> | コーディングセッションから「生きた脳」を構築するHerdrプラグイン——うまくいったこと、失敗したこと、あなたが下した判断を少しずつ学習していく | `shell` | 3 | 2026-08-11 |
| [**hrd**](https://github.com/joshuadavidthomas/hrd)<br><sub>joshuadavidthomas</sub> | サンドボックスの群れと、その上で動くHerdrセッションを管理する | `go` | 3 | 2026-09-04 |
| [**herdr-rails**](https://github.com/codergeek121/herdr-rails)<br><sub>codergeek121</sub> | Herdr と Rails の連携です。 | `ai` `rails` `shell` | 2 | 🔄 2026-09-22 |
| [**herdrctx**](https://github.com/j0urneyk/herdrctx)<br><sub>j0urneyk</sub> | ローカルの Herdr セッションを管理するためのターミナル UI です。 | `go` | 2 | 🔄 2026-09-23 |
| [**shipframe**](https://github.com/juanitourquiza/shipframe)<br><sub>juanitourquiza</sub> | AI coding workflows for teams that plan, prove, and ship. | `ai` `ai-coding` `ai-tools` `claude` `claude-code` | 2 | 🔄 2026-09-25 |
| [**herdr-standup**](https://github.com/neospeed83/herdr-standup)<br><sub>neospeed83</sub> | Gitの活動とHerdrのコンテキストから、証跡に基づいたデイリースタンドアップを作成する | `developer-tools` `standup` `rust` | 2 | 2026-08-31 |
| [**herdr-handsfree**](https://github.com/RanolP/herdr-handsfree)<br><sub>RanolP</sub> | ハンズフリーherdrプラグイン——whisper.cppによる音声入力とmacOS向けWebカメラ視線マウスを提供 | `rust` | 2 | 2026-07-30 |
| [**herdr-orca**](https://github.com/rudironsoni/herdr-orca)<br><sub>rudironsoni</sub> | 標準の Orca タブを、Herdr が管理するターミナルにアタッチする Herdr プラグインです。 | `typescript` | 2 | 2026-09-03 |
| [**herdr-shadow-pane**](https://github.com/shaozk/herdr-shadow-pane)<br><sub>shaozk</sub> | Herdr プラグイン「Shadow Clone Panel」——複数のパネルを同時に操作できます。 | `rust` `vibe-coding` | 2 | 🔄 2026-09-14 |
| [**herdr-suite-site**](https://github.com/StructuPath/herdr-suite-site)<br><sub>StructuPath</sub> | StructuPath Herdr Suiteのランディングページ——herdr.structupath.ai | `herdr-integration` `html` | 2 | 🔄 2026-09-16 |
| [**herdr-sprites-plugin**](https://github.com/superfly/herdr-sprites-plugin)<br><sub>superfly</sub> | Fly.io Sprites 用の公式 Herdr プラグインです。 | `sandboxes` `sprites` `javascript` | 2 | 2026-09-09 |
| [**🆕 herdr-stt**](https://github.com/xtwist/herdr-stt)<br><sub>xtwist</sub> | Speech-to-text for Herdr | `rust` | 2 | 🔄 2026-09-18 |
| [**herdr-zen**](https://github.com/y4m3/herdr-zen)<br><sub>y4m3</sub> | 調整可能な中央寄せペイン幅を備えた、Herdr向けのZenモード | `rust` `terminal` `zen-mode` | 2 | 2026-08-19 |
| [**herdr-edit-windows**](https://github.com/aclima01/herdr-edit-windows)<br><sub>aclima01</sub> | コーディングエージェントの隣、herdrのペイン内で動くシンプルなテキストエディタ——ファイルツリー、シンタックスハイライト付きエディタ、未コミット差分タブを備える。Windows専用 | `rust` | 1 | 2026-07-25 |
| [**herdr-tts**](https://github.com/Aktrov/herdr-tts)<br><sub>Aktrov</sub> | 選択したターミナルのテキストを、自然なニューラル音声（Piper）で読み上げる Herdr プラグインです。右クリックまたはショートカットで実行でき、停止用のキーもあります。 | `tts` `python` | 1 | 2026-09-07 |
| [**🆕 herdr-wrapped-tabs**](https://github.com/AlexeyKrotkov/herdr-wrapped-tabs)<br><sub>AlexeyKrotkov</sub> | Always-visible wrapped tabs for Herdr | `python` | 1 | 🔄 2026-09-24 |
| [**🆕 mu-herdr**](https://github.com/AndresMpa/mu-herdr)<br><sub>AndresMpa</sub> | A herdr configuration made to work with MμVim | `herdr-integration` `muvim` `shell` | 1 | 🔄 2026-09-24 |
| [**herdr-quotabar**](https://github.com/ArnaudRinquin/herdr-quotabar)<br><sub>ArnaudRinquin</sub> | Claude プランのクォータ（5 時間・7 日・モデル別）を、Herdr のタブバーに 1 行でコンパクトに表示します。プロバイダーは差し替え可能です。 | `claude-code` `python` | 1 | 2026-09-08 |
| [**herdr-stoplight**](https://github.com/BowlOfSoup/herdr-stoplight)<br><sub>BowlOfSoup</sub> | Herdrのリアルタイムな状態から、物理的なArduino製信号灯モジュールを動かす | `go` | 1 | 2026-07-11 |
| [**harbr**](https://github.com/dev-town/harbr)<br><sub>dev-town</sub> | Harbour TUI | `typescript` | 1 | 2026-09-03 |
| [**🆕 herdr-drop**](https://github.com/ecylmz/herdr-drop)<br><sub>ecylmz</sub> | Drag a file onto a Herdr pane and it lands in that pane's directory, through the ssh session you already have | `file-transfer` `ssh` `terminal` `python` | 1 | 🔄 2026-09-18 |
| [**herdr-rainfrog**](https://github.com/fraction12/herdr-rainfrog)<br><sub>fraction12</sub> | 管理されたHerdRのペイン内でRainfrogを開く | `shell` | 1 | 2026-08-15 |
| [**herdr-openlogi**](https://github.com/giacolees/herdr-openlogi)<br><sub>giacolees</sub> | OpenLogiのバインディングオーバーレイ経由で、Logitechマウスをherdrに接続する | `ghostty` `logitech-mouse` `macos` `openlogi` `shell` | 1 | 2026-08-24 |
| [**🆕 herdr-tiling**](https://github.com/jaeheonji/herdr-tiling)<br><sub>jaeheonji</sub> | Hyprland-style pane movement and tmux-style layouts for Herdr | `rust` | 1 | 🔄 2026-09-18 |
| [**herdr-services**](https://github.com/lucidstack/herdr-services)<br><sub>lucidstack</sub> | Plugin to track services running inside herdr workspaces | `rust` | 1 | 🔄 2026-09-16 |
| [**herdr-plugins**](https://github.com/narumiruna/herdr-plugins)<br><sub>narumiruna</sub> | _(説明なし)_ | `rust` | 1 | 2026-08-08 |
| [**herdr-docs**](https://github.com/natori-hrj/herdr-docs)<br><sub>natori-hrj</sub> | 落ち着いた表示で整形されたドキュメントを読める、Herdr 用のリーダーペインです。 | `docs` `rust` | 1 | 2026-09-10 |
| [**herdr-phin-util**](https://github.com/phin-tech/herdr-phin-util)<br><sub>phin-tech</sub> | 個人用のHerdrユーティリティ集 | `bubbletea` `tui` `go` | 1 | 2026-08-18 |
| [**herdr-api-client**](https://github.com/playsthisgame/herdr-api-client)<br><sub>playsthisgame</sub> | herdrのスプリットペインやタブで動くHTTP/REST APIクライアント——ターミナルを離れずにリクエストの閲覧・実行・テストができる | `http-client` `rest-client` `tui` `shell` | 1 | 2026-08-08 |
| [**herdr-browser**](https://github.com/redsquiggle/herdr-browser)<br><sub>redsquiggle</sub> | Chromiumのタブグループを、Herdrのワークスペースと同期させる | `chromium` `ratatui` `rust` | 1 | 2026-07-28 |
| [**pixtui**](https://github.com/RizRiyz/pixtui)<br><sub>RizRiyz</sub> | ターミナル上で動くピクセルアートエディタ | `bohay-module` `editor` `luvus-module` `pixel-art` `termina` | 1 | 2026-08-07 |
| [**🆕 herdr-rss**](https://github.com/shindakun/herdr-rss)<br><sub>shindakun</sub> | An RSS reader plugin for herdr, cuz why not | `rss` `rss-reader` `rust` | 1 | 🔄 2026-09-24 |
| [**🆕 herdr-pinned-workspaces**](https://github.com/skydiver/herdr-pinned-workspaces)<br><sub>skydiver</sub> | A Herdr plugin that keeps declared workspaces alive. | `terminal` `tui` `workspaces` `python` | 1 | 🔄 2026-09-21 |
| [**herdr-sidepulse**](https://github.com/third774/herdr-sidepulse)<br><sub>third774</sub> | _(説明なし)_ | `javascript` | 1 | 2026-08-14 |
| [**herdr-pdf**](https://github.com/tim80411/herdr-pdf)<br><sub>tim80411</sub> | PDF viewer plugin for herdr: renders pages into a split pane through the pane.graphics stream API | `go` `pdf` `terminal` | 1 | 🔄 2026-09-17 |
| [**herdr-plugin-k8s-context**](https://github.com/tkuchiki/herdr-plugin-k8s-context)<br><sub>tkuchiki</sub> | 隔離されたKubernetesのcontextとnamespaceを指定して、Herdrのタブを開く | `go` | 1 | 2026-08-15 |
| [**🆕 herdr-pane-resurrect**](https://github.com/unstable-code/herdr-pane-resurrect)<br><sub>unstable-code</sub> | Save the commands running in your herdr panes and bring them back after a restart. | `shell` | 1 | 🔄 2026-09-19 |
| [**multitrunk-herdr-plugin**](https://github.com/yoyoyeti/multitrunk-herdr-plugin)<br><sub>yoyoyeti</sub> | multitrunkのタスクワークスペース向けのHerdrプラグイン | `git` `multitrunk` `rust` | 1 | 2026-08-31 |
| [**🆕 herdr-priority-view**](https://github.com/asermax/herdr-priority-view)<br><sub>asermax</sub> | 3 段階の優先度と「古いものを先に」というルールで並び替える、herdr 用のカスタム優先度ビューです。 | `typescript` | 0 | 🔄 2026-09-12 |
| [**herdr-sort-spaces-plugin**](https://github.com/dorzey/herdr-sort-spaces-plugin)<br><sub>dorzey</sub> | ワークスペースをラベルの辞書順で並び替えて維持します。 | `shell` | 0 | 🔄 2026-09-16 |
| [**herdr-reliable-messaging**](https://github.com/feelautom/herdr-reliable-messaging)<br><sub>feelautom</sub> | Windows 上で、名前付き Herdr ペイン間の永続的かつ決定論的なメッセージ配信を実現します。 | `developer-tools` `nodejs` `windows` `javascript` | 0 | 🔄 2026-09-20 |
| [**🆕 hrdr-azure-plugin**](https://github.com/gbaeke/hrdr-azure-plugin)<br><sub>gbaeke</sub> | herdrプラグイン：Azureのリソースグループとリソースを閲覧し、クリックするとAzureポータルで開く | `azure` `javascript` | 0 | 2026-08-23 |
| [**🆕 paneMorph**](https://github.com/Jenish-Shobhit/paneMorph)<br><sub>Jenish-Shobhit</sub> | Move live Herdr panes between tabs without restarting their processes. | `terminal-multiplexer` `python` | 0 | 🔄 2026-09-21 |
| [**🆕 herdr-busywatch**](https://github.com/KamalF/herdr-busywatch)<br><sub>KamalF</sub> | A herdr plugin: is anything still running, and does it need me? | `python` | 0 | 🔄 2026-09-23 |
| [**🆕 herdr-awst**](https://github.com/kedwards/herdr-awst)<br><sub>kedwards</sub> | herdr と AWST の連携機能です。 | `shell` | 0 | 2026-09-06 |
| [**🆕 herdr-new-task**](https://github.com/leonho/herdr-new-task)<br><sub>leonho</sub> | herdrプラグイン：1回のキー操作でプロジェクトディレクトリを選び、新しいタブでclaudeを起動する。タブ名は名詞優先の命名 | `python` | 0 | 2026-07-16 |
| [**🆕 herdr-git-pull**](https://github.com/nimrc/herdr-git-pull)<br><sub>nimrc</sub> | _(説明なし)_ | `python` | 0 | 2026-08-13 |
| [**ayatsumugi**](https://github.com/nkwork9999/ayatsumugi)<br><sub>nkwork9999</sub> | AyatoriとTsumugi向けの、ローカルファーストなReact DOM・Fiber・状態グラフの可視化 | `cmux` `ghostty` `orca` `react-devtools` `javascript` | 0 | 2026-09-05 |
| [**🆕 herdr-bot**](https://github.com/Phoobobo/herdr-bot)<br><sub>Phoobobo</sub> | _(説明なし)_ | `tui` `typescript` | 0 | 2026-09-02 |
| [**herdr-traex-integration**](https://github.com/Phoobobo/herdr-traex-integration)<br><sub>Phoobobo</sub> | traexとの連携をサポートするHerdrプラグイン | `shell` | 0 | 🔄 2026-09-18 |
| [**herdr-plugins**](https://github.com/RadeJR/herdr-plugins)<br><sub>RadeJR</sub> | _(説明なし)_ | `shell` | 0 | 🔄 2026-09-11 |
| [**herdr-now-playing**](https://github.com/spywhere/herdr-now-playing)<br><sub>spywhere</sub> | キーバインドで操作できる音楽プレイヤーをherdrに追加する | `shell` | 0 | 2026-08-22 |
| [**🆕 herdr-launcher**](https://github.com/Tatendaz/herdr-launcher)<br><sub>Tatendaz</sub> | herdr TUI 用の非公式 macOS Dock ランチャーです。ラム（Herdr のマスコット）をクリックすれば、ターミナルで herdr が起動します。 | `applescript` `developer-tools` `dock` `launcher` `macos` | 0 | 🔄 2026-09-24 |
| [**🆕 herdr-desktop-bridge**](https://github.com/yonatangross/herdr-desktop-bridge)<br><sub>yonatangross</sub> | Claude Desktop が herdr のフロアを読み取り、メッセージを残せるようにする stdio MCP サーバーです。あくまでメールボックスと呼び鈴であり、指揮席にはなりません。 | `claude-desktop` `mcp` `python` | 0 | 🔄 2026-09-11 |
| [**herdr-image-gallery**](https://github.com/zbyhoo/herdr-image-gallery)<br><sub>zbyhoo</sub> | Browse AI-generated images, screenshots, and whole image folders in a Herdr terminal pane | `python` | 0 | 🔄 2026-09-25 |

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
