# herdr plugins by purpose

🇯🇵 日本語 · [🇺🇸 English](README.en.md) · [🇨🇳 中文](README.zh.md)

**「◯◯したい」から herdr のプラグインを探すためのリンク集です。**

- 収録 **952** 件 / 最終更新 **2026-09-04 04:32 UTC**（6 時間ごとに自動更新）
- データ元: GitHub topic [`herdr-plugin`](https://github.com/topics/herdr-plugin) — 公式マーケットプレイス [herdr.dev/plugins](https://herdr.dev/plugins/) と同じ母集団
- 分類はリポジトリの説明文とトピックからの自動推定です。おかしなものは [`data/overrides.json`](data/overrides.json) の PR で直せます
- インストール: `herdr plugin install owner/repo` — [公式ドキュメント](https://herdr.dev/docs/plugins/)

> [!WARNING]
> ここは自動収集の索引で、審査済みカタログではありません。プラグインは自分のマシンでそのまま動くコードなので、入れる前にマニフェストと実行されるコマンドを確認してください。

<a id="purposes"></a>

## 目的から探す

- [**🆕 最近追加されたプラグイン**](#cat-new) (105) — 直近 7 日以内にこの一覧に加わったプラグインです。
- [**通知・アラート**](#cat-notify) (37) — エージェントが完了した / 入力待ちで止まったのを、席を外していても知りたい
- [**スマホ・リモート操作**](#cat-remote) (42) — 外出先やスマホからエージェントを監視して、承認だけ返したい
- [**エージェント統括・並列実行**](#cat-agents) (132) — 複数の AI エージェントをまとめて起動・分担・管理したい
- [**git worktree・ブランチ運用**](#cat-worktree) (48) — 作業ごとに worktree を切って、片付けまで自動でやりたい
- [**コードレビュー・差分確認**](#cat-review) (39) — エージェントが書いた差分を読んで、コメントを返したい
- [**GitHub / issue トラッカー連携**](#cat-forge) (33) — issue や PR を起点に作業を始めたい / PR の状態を追いたい
- [**ワークスペース・レイアウト構築**](#cat-layout) (34) — プロジェクトを開いたら、タブ・ペイン・起動コマンドまで一発で整えたい
- [**ペイン移動・キー操作**](#cat-navigate) (113) — ペインやワークスペース間の移動・リサイズを、エディタと同じキーで済ませたい
- [**ファイル閲覧・エディタ連携**](#cat-files) (59) — ペインの中でファイルツリーを開いたり、エディタ側と状態を揃えたい
- [**トークン・コスト管理**](#cat-cost) (24) — エージェントがいくら使っているかを見たい / 使用量を削りたい
- [**監視・ダッシュボード**](#cat-monitor) (72) — エージェントやマシンの状態を一覧で眺めたい
- [**検索・ファジーファインダー**](#cat-finder) (89) — コマンドやプロジェクトを、名前をうろ覚えのまま呼び出したい
- [**自動化・フック・定期実行**](#cat-automation) (51) — worktree 作成時やタイミングを決めて、決まった手順を自動で走らせたい
- [**セッション保存・復元**](#cat-session) (34) — 作業を閉じても、あとで同じ状態から再開したい
- [**タイトル・命名・見た目**](#cat-naming) (58) — タブ名やターミナルタイトルを自動で分かりやすくしたい / 見た目を変えたい
- [**テキスト・URL 抽出**](#cat-text) (25) — 画面に出ている文字列やパス・URL を、マウスなしで拾いたい
- [**プラグイン管理・開発**](#cat-meta) (9) — プラグイン自体を管理したい / 自分で作りたい
- [**その他・ユーティリティ**](#cat-other) (53) — 上のどれにも当てはまらない便利もの

<a id="cat-new"></a>

## 🆕 最近追加されたプラグイン

> 直近 7 日以内にこの一覧に加わったプラグインです。

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**🆕 ttt**](https://github.com/eugenioenko/ttt)<br><sub>eugenioenko</sub> | TTT Editor (Terminal Text Tool): A real alternative to VS Code, Zed, and Sublime that runs in your terminal. A TUI that feels like GUI. Single binary, zero con… | `cli` `code-editor` `developer-tools` `diff` `editor` | 217 | 2026-09-04 |
| [**🆕 herdr-mobile**](https://github.com/martebytes/herdr-mobile)<br><sub>martebytes</sub> | Mobile-first web UI for Herdr: see your agents, attach to panes, chat with Claude Code and Codex from your phone | `claude-code` `codex` `pwa` `python` | 1 | 2026-09-04 |
| [**🆕 herdr-muse**](https://github.com/akshat12/herdr-muse)<br><sub>akshat12</sub> | Herdr integration for Muse Code: idle/working/blocked pane state via lifecycle hooks (no Herdr fork needed) | `ai-agents` `cli` `coding-agents` `muse-code` `terminal` | 0 | 2026-09-04 |
| [**🆕 herdr-studio**](https://github.com/powerfooI/herdr-studio)<br><sub>powerfooI</sub> | Herdr 用の Web クライアント。モバイル体験を第一に考え、ブラウザ上のターミナル、ワークスペースと worktree の管理、ファイル・差分ビューア、AI エージェントのセッション確認までを提供します。 | `ai-agents` `dogfooding` `git-worktree` `herdr-client` `mobile-friendly` | 32 | 2026-09-03 |
| [**🆕 herdr-telegram-agents**](https://github.com/permgps/herdr-telegram-agents)<br><sub>permgps</sub> | ターミナルからと同じように、Telegram からコーディングエージェントを操作できます。エージェントごとにトピックを分け、トピックアイコンにライブステータスを表示、選択肢はインラインボタン付きの双方向チャットで行えます。 | `claude-code` `coding-agents` `go` `telegram` `telegram-bot` | 11 | 2026-09-04 |
| [**🆕 herdr-palette**](https://github.com/Binb1/herdr-palette)<br><sub>Binb1</sub> | Herdr 用のコマンドパレット。ワークスペースやエージェントへジャンプしたり、プラグインのアクションや Herdr のコマンドを実行できます。 | `go` | 2 | 2026-09-03 |
| [**🆕 herdr-shadow-pane**](https://github.com/shaozk/herdr-shadow-pane)<br><sub>shaozk</sub> | Herdr プラグイン「Shadow Clone Panel」——複数のパネルを同時に操作できます。 | `rust` `vibe-coding` | 2 | 2026-09-04 |
| [**🆕 herdr-workspace-prs**](https://github.com/andrewbrannan/herdr-workspace-prs)<br><sub>andrewbrannan</sub> | ワークスペースの GitHub プルリクエストを追跡する Herdr プラグインです。 | `typescript` | 1 | 2026-09-04 |
| [**🆕 Vincent**](https://github.com/chasereyn/Vincent)<br><sub>chasereyn</sub> | AI エージェントが書いたコードをレビューし、その場で修正できる、マウス操作を主体としたターミナルクライアントです。 | `go` | 1 | 2026-09-03 |
| [**🆕 tsk**](https://github.com/chrisg32/tsk)<br><sub>chrisg32</sub> | tsk——TaskPaper/PlainTasks 風のプレーンテキストタスク管理 TUI で、Rust で書かれています。単体でも herdr プラグインとしても動作します。 | `rust` `taskpaper` `todo` `tui` | 1 | 2026-09-03 |
| [**🆕 herdr-agent-titler**](https://github.com/killerz3/herdr-agent-titler)<br><sub>killerz3</sub> | 外部 API キーを使わず、ローカルの agy・claude・codex・opencode の各ハーネスを使って Herdr のタブに自動でタイトルを付けます。 | `antigravity` `claude-code` `python` | 1 | 2026-09-03 |
| [**🆕 omarchy-herd**](https://github.com/parker-brown-family/omarchy-herd)<br><sub>parker-brown-family</sub> | herdr 配下のどのコーディングエージェントがあなたを必要としているかを、Omarchy バーに表示します。 | `hyprland` `omarchy` `quickshell` `shell` | 1 | 2026-09-03 |
| [**🆕 herdr-achievements**](https://github.com/SerHappy/herdr-achievements)<br><sub>SerHappy</sub> | あなたのHerdr AIエージェントの群れに、実績とささやかなお祝いを追加する | `achievements` `ai-agents` `developer-tools` `gamification` `go` | 1 | 2026-07-30 |
| [**🆕 herdr-plugin-echo**](https://github.com/andischerer/herdr-plugin-echo)<br><sub>andischerer</sub> | 1つのペインから、マークした複数のペインにキー入力をブロードキャストするHerdrプラグイン | `typescript` | 0 | 2026-08-23 |
| [**🆕 herdr-plugin-dotfiles-dev-layout**](https://github.com/edmundmiller/herdr-plugin-dotfiles-dev-layout)<br><sub>edmundmiller</sub> | 自分のdotfilesの開発用ワークスペースレイアウトを開くためのHerdrプラグイン | `python` | 0 | 2026-06-23 |
| [**🆕 herdr-kitty-theme-sync**](https://github.com/enisbu/herdr-kitty-theme-sync)<br><sub>enisbu</sub> | Herdr で使用中のテーマを kitty の ANSI パレットに反映し、ペインの表示内容を Herdr の外観と一致させます。 | `kitty` `linux` `terminal` `theme` `shell` | 0 | 2026-09-03 |
| [**🆕 herdr-drover**](https://github.com/followbl/herdr-drover)<br><sub>followbl</sub> | Herdr 用の「牧羊犬」タブスイッチャー。Super+T を押し続けてタブを巡回し、離した位置で切り替わります。 | `linux` `python` | 0 | 2026-09-03 |
| [**🆕 subherd**](https://github.com/HalloSouf/subherd)<br><sub>HalloSouf</sub> | すべての Claude Code サブエージェントが何をしているかを、そのセッションが動いているワークスペースごとにまとめて表示する herdr プラグインです。 | `claude-code` `tui` `go` | 0 | 2026-09-03 |
| [**🆕 herdr-open-editor**](https://github.com/jimididit/herdr-open-editor)<br><sub>jimididit</sub> | fzf でファイルをあいまい検索して選び、設定済みのエディタで開きます。 | `herd` `text-editor` `tui` `shell` | 0 | 2026-09-03 |
| [**🆕 herdr-nnn**](https://github.com/linuxing3/herdr-nnn)<br><sub>linuxing3</sub> | herdr内でnnnを開く | `shell` | 0 | 2026-08-04 |
| [**🆕 herdr-tab-title**](https://github.com/Newt6611/herdr-tab-title)<br><sub>Newt6611</sub> | Herdr Tab Titleは、「1. Codex」「2. Terminal」のような、ワークスペース単位できれいに番号付けされた名前にHerdrのタブを自動リネームする。フォーマットはカスタマイズ可能 | `rust` | 0 | 2026-07-09 |
| [**🆕 agentic-box**](https://github.com/nicoRomeroCuruchet/agentic-box)<br><sub>nicoRomeroCuruchet</sub> | Claude Codeがローカルモデルのエージェントを操作する、隔離されたbox | `agent-orchestration` `agentic` `agentic-workflow` `docker` `ornith-1-0-35b` | 0 | 2026-08-17 |
| [**🆕 herdr-guard**](https://github.com/pauljohnchamberlain/herdr-guard)<br><sub>pauljohnchamberlain</sub> | Codex や Claude など、コーディングエージェントから Herdr を安全に外部制御できるようにします。 | `coding-agents` `typescript` | 0 | 2026-09-04 |
| [**🆕 herdr-display-workspace**](https://github.com/RickyMarou/herdr-display-workspace)<br><sub>RickyMarou</sub> | Herdr プラグイン：現在のワークスペース名をタブバーの右側に表示します。 | `shell` | 0 | 2026-09-03 |
| [**🆕 herdr-worktree-include**](https://github.com/scoussens-nthplusio/herdr-worktree-include)<br><sub>scoussens-nthplusio</sub> | リポジトリの.worktreeincludeを使って、.envなどgit管理外のファイルを新しいHerdr worktreeにコピーする——Claude Codeが使うのと同じファイル・同じルール | `dotenv` `git-worktree` `shell` | 0 | 2026-08-27 |
| [**🆕 herdr-plugins**](https://github.com/shubham-cpp/herdr-plugins)<br><sub>shubham-cpp</sub> | タブ・エージェントの命名と、方向キーによるペインフォーカスのための Herdr プラグイン集です。 | `rust` | 0 | 2026-09-03 |
| [**🆕 herdr-copy-conversation**](https://github.com/testy-cool/herdr-copy-conversation)<br><sub>testy-cool</sub> | Herdr 内で、ターミナルのスクロールバック全体やエージェントとの会話を、そのままクリップボードにコピーできます。 | `ai-agents` `claude-code` `clipboard` `codex` `developer-tools` | 0 | 2026-09-03 |
| [**🆕 herdr-focus**](https://github.com/trapple/herdr-focus)<br><sub>trapple</sub> | 次にブロック中/完了したエージェントペインにフォーカスし、ターミナルアプリを最前面に出す。グローバルホットキー付き | `shell` | 0 | 2026-07-19 |
| [**🆕 herdrctx**](https://github.com/j0urneyk/herdrctx)<br><sub>j0urneyk</sub> | ローカルの Herdr セッションを管理するためのターミナル UI です。 | `go` | 2 | 2026-09-02 |
| [**🆕 herdr-triggers**](https://github.com/cantona/herdr-triggers)<br><sub>cantona</sub> | ペインの出力を常駐監視して正規表現でトリガーを発動します。自動ログインなど、正規表現ベースのターミナルトリガーに対応します。 | `rust` `terminal` | 1 | 2026-09-02 |
| [**🆕 herdr-swipe-linux**](https://github.com/enisbu/herdr-swipe-linux)<br><sub>enisbu</sub> | Linux 版 Herdr 向けのトラックパッドジェスチャー。スワイプでペイン・タブ・スペースを移動し、タップで入力待ちのエージェントへジャンプできます。 | `evdev` `gestures` `gnome` `hyprland` `linux` | 1 | 2026-09-02 |
| [**🆕 herdr-pickers**](https://github.com/sagmans/herdr-pickers)<br><sub>sagmans</sub> | エージェント・worktree・ワークスペース・プロジェクト向けに、いくつかのカスタムなポップアップピッカーを提供します。 | `typescript` | 1 | 2026-09-03 |
| [**🆕 herdr-claude-lifecycle**](https://github.com/daocoding/herdr-claude-lifecycle)<br><sub>daocoding</sub> | herdr + Omarchy 向けの、フックを軸にした Claude Code のライフサイクル管理。Claude 自身のフックから working/blocked/idle の状態を取得し、Claude Code のアップデートのたびに動作を検証します。 | `claude-code` `omarchy` `python` | 0 | 2026-09-02 |
| [**🆕 herdr-oncall**](https://github.com/fulanto/herdr-oncall)<br><sub>fulanto</sub> | Herdr プラグイン：エージェントがブロックされたときに Telegram へ通知します。 | `javascript` | 0 | 2026-09-04 |
| [**🆕 herdr-pane-id-border**](https://github.com/Haichiu/herdr-pane-id-border)<br><sub>Haichiu</sub> | ペインの境界線に正規のペイン ID を表示する、ミニマルな Herdr プラグインです。 | `shell` | 0 | 2026-09-02 |
| [**🆕 herdr-cron**](https://github.com/huketo/herdr-cron)<br><sub>huketo</sub> | コーディングエージェント向けの自動化作業をスケジュール実行できます。Herdr のペイン内で、シェルコマンドやコーディングエージェントへのプロンプトを予約できます。 | `agent-skills` `automation` `bubbletea` `cli` `coding-agent` | 0 | 2026-09-03 |
| [**🆕 herdr-webhook**](https://github.com/jefflau/herdr-webhook)<br><sub>jefflau</sub> | Herdr プラグイン：エージェントの完了・ブロックイベントを Webhook へ POST します。 | `python` | 0 | 2026-09-03 |
| [**🆕 herdr-checkpoint**](https://github.com/lancodev/herdr-checkpoint)<br><sub>lancodev</sub> | herdr 版 tmux-resurrect——セッションの状態をそのままチェックポイントとして保存・復元し、チェックポイントに含まれないものは閉じます。 | `tmux-resurrect` `tui` `shell` | 0 | 2026-09-02 |
| [**🆕 herdr-plugin-project-finder**](https://github.com/mike-bronner/herdr-plugin-project-finder)<br><sub>mike-bronner</sub> | Herdr プラグイン：git リポジトリをあいまい検索で選び、ワークスペースとして開きます。 | `python` | 0 | 2026-09-04 |
| [**🆕 herdr-plugin-recent-spaces**](https://github.com/mike-bronner/herdr-plugin-recent-spaces)<br><sub>mike-bronner</sub> | Herdr プラグイン：スペースのサイドバーを、直近に使った順に並べ替えます。 | `python` | 0 | 2026-09-02 |
| [**🆕 herdr-agent-links**](https://github.com/OmarDadabhoy/herdr-agent-links)<br><sub>OmarDadabhoy</sub> | Herdr 内の Codex や Claude の出力にある、Markdown ラベルの裏に隠れたリンクを開けます。 | `claude-code` `codex` `productivity` `terminal` `python` | 0 | 2026-09-02 |
| [**🆕 herdr-orca**](https://github.com/rudironsoni/herdr-orca)<br><sub>rudironsoni</sub> | 標準の Orca タブを、Herdr が管理するターミナルにアタッチする Herdr プラグインです。 | `typescript` | 0 | 2026-09-03 |
| [**🆕 hither**](https://github.com/T0mSIlver/hither)<br><sub>T0mSIlver</sub> | リモートマシン上の herdr ペインでキーの組み合わせを押すと、Mac 側で Zed がそのディレクトリを開きます。 | `shell` | 0 | 2026-09-02 |
| [**🆕 herdr-hop**](https://github.com/utahta/herdr-hop)<br><sub>utahta</sub> | herdr プラグイン：1 つのポップアップから、リポジトリ・worktree・ワークスペースへ一気にジャンプできます。 | `git-worktree` `go` `terminal` `tui` | 0 | 2026-09-02 |
| [**🆕 herdr-git-dirty**](https://github.com/viko16/herdr-git-dirty)<br><sub>viko16</sub> | 各 Space の未コミットの Git ファイル数を表示する、軽量な Herdr プラグインです。 | `git` `shell` | 0 | 2026-09-02 |
| [**🆕 herdr-tab-jump**](https://github.com/cyperx84/herdr-tab-jump)<br><sub>cyperx84</sub> | 任意のキーバインドから、位置で指定した herdr のタブ N にフォーカスします——数字キーの列をタブとワークスペースに割り振れます。 | `shell` | 1 | 2026-09-01 |
| [**🆕 herdr-claude-usage**](https://github.com/anyaachan/herdr-claude-usage)<br><sub>anyaachan</sub> | Herdr でグローバルな Claude Code プランの使用状況を確認できます。タブバーでの要約表示とポップアップダッシュボードを備え、statusLine を利用してマルチアカウントにも対応します。 | `claude` `claude-code` `cli` `terminal` `shell` | 0 | 2026-09-01 |
| [**🆕 herdr-tab-command**](https://github.com/asermax/herdr-tab-command)<br><sub>asermax</sub> | 新しいタブに付けた名前に応じて、エージェントを起動したりコマンドを実行したりします。 | `typescript` | 0 | 2026-08-31 |
| [**🆕 herdr-agent-numbers**](https://github.com/DillonWall/herdr-agent-numbers)<br><sub>DillonWall</sub> | herdr のエージェントパネルに番号を振り、focus_agent（prefix+1〜9）に対応させます。 | `terminal-multiplexer` `shell` | 0 | 2026-09-01 |
| [**🆕 herdr-hitl**](https://github.com/huketo/herdr-hitl)<br><sub>huketo</sub> | Herdr のコーディングエージェントを、人の判断待ちで一時停止させ、Telegram や Discord 経由でスマホに通知します。 | `agent-skill` `ai-agents` `cli` `discord-bot` `go` | 0 | 2026-09-03 |
| [**🆕 herdr-pane-mark**](https://github.com/jovylle/herdr-pane-mark)<br><sub>jovylle</sub> | Herdr プラグイン——パレット/ポップアップから、Agents 配下にカスタムの $mark を設定できます（フォーク不要）。 | `terminal` `shell` | 0 | 2026-09-01 |
| [**🆕 herdr-jump**](https://github.com/lancodev/herdr-jump)<br><sub>lancodev</sub> | herdr のワークスペースとエージェントを、vim 風キー操作の 2 ペインあいまい検索スイッチャーで切り替えられます。 | `fzf` `tui` `shell` | 0 | 2026-09-01 |
| [**🆕 lasso**](https://github.com/skellleks/lasso)<br><sub>skellleks</sub> | herdr 用のレビューペイン。エージェントごとの差分をシンタックスハイライト付きで表示し、インラインコメントをエージェントへ送り返せます。 | `ai-agents` `claude-code` `code-review` `git-diff` `ratatui` | 0 | 2026-08-31 |
| [**🆕 herdr-jump**](https://github.com/solidsnakedev/herdr-jump)<br><sub>solidsnakedev</sub> | herdr 用のワークスペース・ペイン・タブのあいまい検索ピッカーに加え、直前のワークスペースへ切り替えるトグルも備えています。 | `shell` | 0 | 2026-09-01 |
| [**🆕 herdr-pane-tools**](https://github.com/solidsnakedev/herdr-pane-tools)<br><sub>solidsnakedev</sub> | herdr 向けに、Vim を意識したペイン移動、aerospace 風のペイン移動、tmux 風のローテーションを提供します。 | `shell` | 0 | 2026-09-01 |
| [**🆕 herdweb**](https://github.com/zlxlabs/herdweb)<br><sub>zlxlabs</sub> | スマホからコーディングエージェントを監視・操作できます。音声入力、画像の貼り付け、Webhook 通知、複数デバイス・サーバー対応。 | `typescript` | 5 | 2026-09-01 |
| [**🆕 herdr-codex-bridge**](https://github.com/ardasevinc/herdr-codex-bridge)<br><sub>ardasevinc</sub> | 一元化されたアプリサーバーを使い、Codex セッションに Herdr ネイティブのペイン識別情報を割り当てます。 | `ai-agents` `codex` `terminal` `go` | 3 | 2026-09-01 |
| [**🆕 herdr-mission-control**](https://github.com/vjeantet/herdr-mission-control)<br><sub>vjeantet</sub> | herdr 用のミッションコントロール。1 キーで、ワークスペースの全ペインをタブごとにまとめたライブタイルグリッドとして表示し、選んで切り替えられます。 | `expose` `mission-control` `terminal` `tui` `rust` | 3 | 2026-09-01 |
| [**🆕 herdr-pets**](https://github.com/abhishek944/herdr-pets)<br><sub>abhishek944</sub> | 稼働中の Herdr エージェントたちを、デスクトップに浮かぶ透明な村として表示します。 | `typescript` | 2 | 2026-08-31 |
| [**🆕 herdr-composer**](https://github.com/danieljvdm/herdr-composer)<br><sub>danieljvdm</sub> | タスクを組み立て、コンテキストを添付し、隔離された Herdr ワークスペースでコーディングエージェントを起動できます。 | `coding-agents` `git-worktree` `rust` | 1 | 2026-09-01 |
| [**🆕 herdr-mobile-app**](https://github.com/teasec4/herdr-mobile-app)<br><sub>teasec4</sub> | スマホから herdr の AI エージェントを操作できます。 | `ai` `devtools` `flutter` `herdr-integration` `herdr-mobile` | 1 | 2026-09-03 |
| [**🆕 herdr-hyprland**](https://github.com/aorumbayev/herdr-hyprland)<br><sub>aorumbayev</sub> | Hyprland に着想を得た、herdr 用の操作方法です。 | `ai-agents` `developer-tools` `golang` `hyprland` `keybindings` | 0 | 2026-08-31 |
| [**🆕 herdr-sheep**](https://github.com/huketo/herdr-sheep)<br><sub>huketo</sub> | Herdr のコーディングエージェントを、アニメーションする ASCII アートの羊の群れとして眺められます。 | `ascii-art` `rust` `tui` | 0 | 2026-08-31 |
| [**🆕 herdr-tab-titles**](https://github.com/kewah/herdr-tab-titles)<br><sub>kewah</sub> | 最初のコーディングエージェントへのプロンプトをもとに、ペインとタブに名前を付ける Herdr プラグインです。 | `javascript` | 0 | 2026-09-01 |
| [**🆕 precc-herdr-plugin**](https://github.com/peria-ai/precc-herdr-plugin)<br><sub>peria-ai</sub> | herdr 用の PRECC プラグイン。エージェント横断でのトークン節約状況を計測し、PRECC のセットアップをワンタッチで行えます。 | `claude-code` `precc` `shell` | 0 | 2026-09-02 |
| [**🆕 provider-usage**](https://github.com/ryus1234/provider-usage)<br><sub>ryus1234</sub> | Herdr 用の、プロバイダーの使用量とクォータを表示するバーです。 | `ai-usage` `quota-monitor` `rust` | 0 | 2026-08-31 |
| [**🆕 herdr-tab-new**](https://github.com/softwarecrafts/herdr-tab-new)<br><sub>softwarecrafts</sub> | このプロジェクトの herdr ワークスペースで、エージェントセッションを再開または開始します。herdr プラグインであると同時に、herdr の外のターミナルからも使える CLI でもあります。 | `typescript` | 0 | 2026-08-31 |
| [**🆕 herdr-grid**](https://github.com/WillHeather/herdr-grid)<br><sub>WillHeather</sub> | herdr ワークスペースのエージェントペインを画面いっぱいのグリッドに敷き詰め、また元に戻せます。 | `python` | 0 | 2026-08-31 |
| [**🆕 herdr-updater**](https://github.com/diegopzz/herdr-updater)<br><sub>diegopzz</sub> | Herdr本体とプラグインを、フリート全体にわたって安全に最新の状態に保つ | `rust` `updater` | 8 | 2026-09-01 |
| [**🆕 herdr-grid**](https://github.com/thuanlm215/herdr-grid)<br><sub>thuanlm215</sub> | ドラッグ＆ドロップ・新規シェル起動・均等な分割・固定プリセット・安全なワークスペース作成に対応した、Herdr向けのビジュアルペインレイアウトエディタ | `layout-presets` `pane-layout` `productivity` `ratatui` `rust` | 6 | 2026-09-01 |
| [**🆕 herdr-arrange**](https://github.com/crierr/herdr-arrange)<br><sub>crierr</sub> | herdrのペイン移動・入れ替え・再分割・レイアウト変更を行う、インタラクティブなポップアップUI | `go` | 4 | 2026-08-31 |
| [**🆕 agent-keep-awake**](https://github.com/happyeric77/agent-keep-awake)<br><sub>happyeric77</sub> | Herdrのエージェントが動作中は、macOSのスリープを防止する | `javascript` | 1 | 2026-08-12 |
| [**🆕 herdr-plugins**](https://github.com/narumiruna/herdr-plugins)<br><sub>narumiruna</sub> | _(説明なし)_ | `rust` | 1 | 2026-08-08 |
| [**🆕 herdr-tournament**](https://github.com/neospeed83/herdr-tournament)<br><sub>neospeed83</sub> | Herdr向けの、対抗的なマルチエージェントコードレビュー | `rust` | 1 | 2026-08-29 |
| [**🆕 herdr-undo-close**](https://github.com/pedroloch/herdr-undo-close)<br><sub>pedroloch</sub> | ブラウザのCmd+Shift+Tのように、herdrで閉じたタブを復元——ラベル、分割比率を含むペイン構成、各ペインの作業ディレクトリ、タブの位置までまとめて復元する | `python` | 1 | 2026-07-30 |
| [**🆕 herdr-copy-hints**](https://github.com/rotemb-wond/herdr-copy-hints)<br><sub>rotemb-wond</sub> | Herdr向けの、tmux-fingers風キーボードコピーヒント：パス・GitのSHA・URLなどに対応 | `clipboard` `developer-tools` `keyboard-navigation` `productivity` `terminal` | 1 | 2026-07-23 |
| [**🆕 herdr-rovo-dev**](https://github.com/usrivastava92/herdr-rovo-dev)<br><sub>usrivastava92</sub> | Rovo Dev CLIのセッションを検出し、Herdr上で稼働中のエージェントとして報告するHerdrプラグイン | `ai-agent` `rovo` `rovo-dev` `shell` | 1 | 2026-07-19 |
| [**🆕 reasonix-herdr**](https://github.com/uuie/reasonix-herdr)<br><sub>uuie</sub> | Herdr内でのライフサイクルのリアルタイム報告とワークスペース制御を行う、ネイティブなReasonixプラグイン | `reasonix` `python` | 1 | 2026-07-10 |
| [**🆕 herdr-activity-age**](https://github.com/1Morganmore/herdr-activity-age)<br><sub>1Morganmore</sub> | 各エージェントの最終状態変化からの経過時間を表示する、Windows版Herdrプラグイン | `powershell` `windows` | 0 | 2026-08-30 |
| [**🆕 herdr-dynamic-workflow**](https://github.com/andthezhang/herdr-dynamic-workflow)<br><sub>andthezhang</sub> | Herdr内でコーディングエージェントCLIをオーケストレーションするための、JavaScript製ワークフロー | `agent-fleet` `agent-orchestration` `agent-swarm` `agentic-ai` `agents` | 0 | 2026-08-30 |
| [**🆕 herdr-jetbrains**](https://github.com/chenyao0910/herdr-jetbrains)<br><sub>chenyao0910</sub> | アクティブなHerdrのワークスペースまたはworktreeを、Rider・WebStorm・IntelliJ IDEA・GoLandで開く | `developer-tools` `git-worktree` `goland` `intellij-idea` `jetbrains` | 0 | 2026-08-30 |
| [**🆕 herdr-keybinds**](https://github.com/gwelican/herdr-keybinds)<br><sub>gwelican</sub> | プラグインのものも含め、すべてのキーバインドを一覧表示・検索できる Herdr プラグインです。 | `python` | 0 | 2026-08-31 |
| [**🆕 herdr-positional-tabs**](https://github.com/juezhong/herdr-positional-tabs)<br><sub>juezhong</sub> | Herdr向けの、安定した位置ベースのタブラベルとAlt+数字によるナビゲーション | `rust` `terminal` | 0 | 2026-08-30 |
| [**🆕 herdr-worktree-guard**](https://github.com/takeaship/herdr-worktree-guard)<br><sub>takeaship</sub> | エージェントのworktreeを追跡・清掃する、安全性重視のHerdrプラグイン | `coding-agents` `git-worktree` | 0 | 2026-08-30 |
| [**🆕 cbds**](https://github.com/zqkra/cbds)<br><sub>zqkra</sub> | Herdrの群れ向けの、信頼性の高いマルチエージェントオーケストレーション。永続化されたタスク、権威あるワーカーレポート、ハングしない待機処理を提供する | `agents` `cli` `multi-agent` `orchestration` `javascript` | 0 | 2026-08-31 |
| [**🆕 herdr-world**](https://github.com/IvoryHeart/herdr-world)<br><sub>IvoryHeart</sub> | Herdr World——Herdr向けのマルチサーフェスなWeb体験 | `multi-agent` `observability` `pixel-art` `react` `rust` | 5 | 2026-09-03 |
| [**🆕 dotfiles**](https://github.com/tifandotme/dotfiles)<br><sub>tifandotme</sub> | ~/.*（ホームディレクトリ配下の設定ファイル） | `aerospace` `chezmoi` `cmux` `dotfiles` `ghostty` | 3 | 2026-09-03 |
| [**🆕 herdr-code-board**](https://github.com/sazardev/herdr-code-board)<br><sub>sazardev</sub> | Herdr内の、エージェント向けプロンプトのカンバンキュー——カードが実際のエージェントをペイン・worktree・ワークスペースに配置し、カード同士を連鎖させるルールも設定できる | `ai-agents` `kanban` `rust` `tui` | 2 | 2026-08-30 |
| [**🆕 harbr**](https://github.com/dev-town/harbr)<br><sub>dev-town</sub> | Harbour TUI | `typescript` | 1 | 2026-09-03 |
| [**🆕 herdr-plugin-atomic-workflows**](https://github.com/caner-akca/herdr-plugin-atomic-workflows)<br><sub>caner-akca</sub> | herdrプラグイン：隔離されたAtomicワークフロータスクを起動・監視する——キャンペーンボード、サイドバートークン、実行台帳、オプションのTelegramコックピットを備える | `javascript` | 0 | 2026-09-01 |
| [**🆕 herdr-pane-agent-unread**](https://github.com/NachoPal/herdr-pane-agent-unread)<br><sub>NachoPal</sub> | herdr向けの、ペインごとの「未読」通知＋サイドバーバッジ——見ていないペインで完了または入力待ちになったエージェントを浮かび上がらせる（herdrは「既読」をタブ単位で管理し、ペイン単位では管理しないため） | `python` | 0 | 2026-09-01 |
| [**🆕 herdr-bot**](https://github.com/Phoobobo/herdr-bot)<br><sub>Phoobobo</sub> | _(説明なし)_ | `tui` `typescript` | 0 | 2026-09-02 |
| [**🆕 herdr-cmd-agent-plugin**](https://github.com/thesimonharms/herdr-cmd-agent-plugin)<br><sub>thesimonharms</sub> | CommandCode（cmd）をエージェントとして認識するHerdrプラグイン——画面マニフェストとcmd modによるidle/working/blockedの判定に対応 | `cmd` `commandcode` `shell` | 0 | 2026-08-31 |
| [**🆕 herdr-space-groups**](https://github.com/yojahny55/herdr-space-groups)<br><sub>yojahny55</sub> | herdrプラグイン：Spaceを名前付き・色分けされたグループにまとめる——ピッカーのポップアップ（マウス＋キーボード対応）、サイドバーのグループ見出し、自動並べ替えに対応 | `javascript` | 0 | 2026-08-29 |
| [**🆕 herdr-ferry**](https://github.com/wavrin/herdr-ferry)<br><sub>wavrin</sub> | SSH経由で、Herdrのbox（マシン）とノートPCの間でファイルとクリップボードをやり取りする——クラウドバケット不要 | `rust` | 2 | 2026-08-29 |
| [**🆕 hermes-herdr-auto-reconcile**](https://github.com/chris-yyau/hermes-herdr-auto-reconcile)<br><sub>chris-yyau</sub> | Herdrのペインを監視するHermesスーパーバイザー向けの、ゲートウェイ生存監視プラグイン | `automation` `hermes-agent` `multi-agent` `python` | 1 | 2026-09-02 |
| [**🆕 herdr-overview**](https://github.com/iamgp/herdr-overview)<br><sub>iamgp</sub> | Herdr向けのMission Control / Exposé——全spaceをタイル状に並べたライブ一覧 | `terminal` `tui` `javascript` | 1 | 2026-08-28 |
| [**🆕 herdr-session-sync**](https://github.com/nengqi/herdr-session-sync)<br><sub>nengqi</sub> | Claude Code・Codex・エージェントのセッション名を、Herdrのペインラベル・PTYのウィンドウタイトル・モバイルコンパニオンアプリ（Heeler）にまたがって自動同期する | `agent` `claude-code` `codex` `heeler` `terminal-multiplexer` | 1 | 2026-09-03 |
| [**🆕 herdr-plugin-env-sync**](https://github.com/DecampsRenan/herdr-plugin-env-sync)<br><sub>DecampsRenan</sub> | Herdrプラグイン：env-syncは新しいGit worktreeをセットアップする（.envのコピー、リモートブランチの追跡、セットアップコマンドの実行）。ライブなステータスパネル付き | `developer-tools` `git-worktree` `shell` | 0 | 2026-08-28 |
| [**🆕 herdr-session-title-name**](https://github.com/jovylle/herdr-session-title-name)<br><sub>jovylle</sub> | herdrプラグイン：terminal_title_strippedをタブに永続化する（session_titleだけを上に残し、閉じた後もタブがそれを保持する） | `sidebar` `terminal` `html` | 0 | 2026-08-28 |
| [**🆕 herdr-nvim**](https://github.com/jtnovellis/herdr-nvim)<br><sub>jtnovellis</sub> | Herdr の中で動く Neovim——タブごとの全高サイドバーと、コーディングエージェントとの本物のやり取りを実現します。見ているコードについて質問し、Neovim を離れずに回答を読み、エージェントが加えた編集を1つずつ確認できます。 | `ai-agents` `claude-code` `developer-tools` `lua` `neovim` | 0 | 2026-08-31 |
| [**🆕 herdr-ccs**](https://github.com/KennethWKZ/herdr-ccs)<br><sub>KennethWKZ</sub> | `ccs claude`を、Herdr上のネイティブClaude Codeのように振る舞わせる——ペイン検出と、ccs経由のランチャーを意識した復元に対応 | `shell` | 0 | 2026-08-29 |
| [**🆕 herdr-rich-notifications**](https://github.com/liamwh/herdr-rich-notifications)<br><sub>liamwh</sub> | herdrのエージェント状態変化に対する、リッチなネイティブデスクトップ通知——LLM不要のコンテキスト拡充、クリックでフォーカス（herdrのエージェントフォーカス＋Niriウィンドウのターゲティング）に対応。quinnjr/herdr-notificationsのフォーク | `notifications` `rust` | 0 | 2026-08-28 |
| [**🆕 herdr-gh-issue-label**](https://github.com/polidog/herdr-gh-issue-label)<br><sub>polidog</sub> | ブランチに対応する GitHub issue の番号とタイトルを Herdr のスペースに表示するプラグイン | `github-issues` `shell` | 0 | 2026-08-28 |
| [**🆕 herdr-git-stack**](https://github.com/ubuntudroid/herdr-git-stack)<br><sub>ubuntudroid</sub> | herdrプラグイン：各spaceのgitブランチスタック内での位置をspacesサイドバーに表示し、親ブランチが移動したブランチにフラグを立て、スタックを連続した状態に保つ。ローカルのコミットグラフのみを使用——ネットワーク・forge API・スタッキングツール不要 | `bash` `developer-tools` `git` `stacked-branches` `shell` | 0 | 2026-09-03 |

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-notify"></a>

## 通知・アラート

> エージェントが完了した / 入力待ちで止まったのを、席を外していても知りたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-focus-notify**](https://github.com/yankewei/herdr-focus-notify)<br><sub>yankewei</sub> | Herdrのエージェント向けの、クリック可能なmacOS通知。エージェントがブロックまたは完了するとネイティブのトースト通知を送り、クリックするとターミナルを最前面に出して該当のHerdrペインにフォーカスする | `alerter` `macos` `notifications` `productivity` `rust` | 19 | 2026-08-18 |
| [**herdr-pings**](https://github.com/joelhooks/herdr-pings)<br><sub>joelhooks</sub> | herdrのペインで動くAIエージェント向けの、ターン単位のウェイクイベント通知——piエクステンション、waitコマンド、クラッシュブリッジ、ワーカー用のDiscworld風コールサイン付き | `ai-agents` `pi` `typescript` | 9 | 2026-08-09 |
| [**herdr-terminal-notifier**](https://github.com/dot/herdr-terminal-notifier)<br><sub>dot</sub> | terminal-notifier経由で、herdrエージェントの状態変化をカスタマイズ可能なmacOS通知として送る | `macos` `terminal-notifier` `shell` | 7 | 2026-07-14 |
| [**herdr-ntfy**](https://github.com/horn553/herdr-ntfy)<br><sub>horn553</sub> | 依存関係最小限（jq・curl・sh）——Herdrのエージェントが完了またはブロックされたときにntfy通知を送る | `shell` | 7 | 2026-08-01 |
| [**herdr-ntfy-notify**](https://github.com/zom-2018/herdr-ntfy-notify)<br><sub>zom-2018</sub> | Herdrのターミナルエージェント向けの、リアルタイムなntfyプッシュ通知 | `agent` `ntfy` `push-notifications` `tui` `javascript` | 7 | 2026-06-23 |
| [**herdr-hail**](https://github.com/natori-hrj/herdr-hail)<br><sub>natori-hrj</sub> | herdr向けのSlack/Discord双方向ブリッジ——エージェントがブロックされたら通知が来て、返信/タップでブロックを解除できる。トンネル不要 | `discord` `slack` `typescript` | 6 | 2026-07-19 |
| [**herdr-notify-windows**](https://github.com/aclima01/herdr-notify-windows)<br><sub>aclima01</sub> | herdrのエージェント向けのWindows 11トースト通知（ターン完了/入力待ち） | `powershell` | 4 | 2026-07-23 |
| [**herdr-telegram-bridge**](https://github.com/cokekitten/herdr-telegram-bridge)<br><sub>cokekitten</sub> | herdrのエージェントが完了またはブロックされたらTelegramにプッシュ通知が来る——返信すればテキストやファイルをそのままエージェントに送り返せる。サーバー・トンネル・アプリ不要 | `ai-agents` `chatops` `claude-code` `developer-tools` `notifications` | 4 | 2026-08-06 |
| [**herdr-telegram-plugin**](https://github.com/mvallebr/herdr-telegram-plugin)<br><sub>mvallebr</sub> | herdr向けのTelegramボットコンパニオン——Telegramのフォーラムトピック経由で任意のエージェントを遠隔操作。処理経路にLLMは介在しない | `typescript` | 4 | 🔄 2026-08-31 |
| [**herdr-cache-alert**](https://github.com/AltanS/herdr-cache-alert)<br><sub>AltanS</sub> | herdrプラグイン：全エージェントペインにプロンプトキャッシュのカウントダウンを表示——各キャッシュルールの出典と日付も併せて示す | `ai-agents` `ai-coding` `ai-tools` `claude-code` `multiplexing` | 3 | 🔄 2026-09-01 |
| [**herdr-announcer**](https://github.com/nhclink16/herdr-announcer)<br><sub>nhclink16</sub> | Herdrプラグイン：エージェントが完了または入力待ちになったら、LLMによる一文要約を音声で読み上げる——ローカルTTS、ElevenLabs、任意のカスタムコマンドに対応 | `tts` `python` | 3 | 🔄 2026-08-20 |
| [**herdr-discord-presence**](https://github.com/revanp/herdr-discord-presence)<br><sub>revanp</sub> | herdrプラグイン：Herdrのセッションとエージェントの状態を、Discord Rich Presenceとして表示する | `typescript` | 3 | 2026-08-14 |
| [**herdr-agent-notify**](https://github.com/A1exthegreat/herdr-agent-notify)<br><sub>A1exthegreat</sub> | herdrプラグイン：エージェントが作業を終えた、確認が必要になった、またはアイドルになったときにデスクトップ通知を送る | `javascript` | 2 | 2026-08-15 |
| [**buzzr**](https://github.com/candypoets/buzzr)<br><sub>candypoets</sub> | 稼働中のHerdrのspaceとエージェントを、Nostrアイデンティティとメンションルーティング付きでBuzzチャンネルにミラーする | `agents` `buzz` `nostr` `rust` | 2 | 2026-08-14 |
| [**agent-webhook-notify**](https://github.com/happyeric77/agent-webhook-notify)<br><sub>happyeric77</sub> | Herdrのエージェントが完了またはブロックされたときに、Webhook通知を送る | `javascript` | 2 | 2026-08-12 |
| [**herdr-guard**](https://github.com/StructuPath/herdr-guard)<br><sub>StructuPath</sub> | Herdr向けのエージェント横断コマンドポリシー：危険なシェルコマンドを監査・警告・中断する | `ai-agents` `command-policy` `security` `terminal` `javascript` | 2 | 🔄 2026-08-23 |
| [**herdr-telegram-notifications**](https://github.com/barnuri/herdr-telegram-notifications)<br><sub>barnuri</sub> | herdrプラグイン：エージェントがアイドルになった・ブロックされた・完了したときにTelegram通知を送る | `telegram` `javascript` | 1 | 🔄 2026-09-01 |
| [**herdr-prayer-times**](https://github.com/bayoudhi/herdr-prayer-times)<br><sub>bayoudhi</sub> | 次の礼拝時刻とカウントダウンをHerdrのサイドバーに表示——タイムテーブルのポップアップと通知付き | `rust` | 1 | 2026-08-13 |
| [**session-sounds**](https://github.com/ChrisPachulski/session-sounds)<br><sub>ChrisPachulski</sub> | macOSとLinux向けに、Herdrのエージェントごとに異なる完了音・注意喚起音を鳴らす | `coding-agents` `notifications` `rust` | 1 | 2026-07-19 |
| [**herdr-notify-wsl**](https://github.com/saeedrahimi/herdr-notify-wsl)<br><sub>saeedrahimi</sub> | WSL内で動くherdrエージェント向けのWindows 11トースト通知——aclima01/herdr-notify-windowsをベースにしている | `powershell` | 1 | 2026-07-23 |
| [**herdr-wsl-notify**](https://github.com/tkmct/herdr-wsl-notify)<br><sub>tkmct</sub> | WSL2上で動くエージェント（Claude Codeなど）が完了またはブロック（承認/入力待ち）になったときに、Windowsのデスクトップトースト通知を表示するHerdrプラグイン | `javascript` | 1 | 🔄 2026-08-27 |
| [**herdr-prompt-reply**](https://github.com/cedrus-8864/herdr-prompt-reply)<br><sub>cedrus-8864</sub> | herdrのエージェントの権限確認プロンプトに、macOS通知から直接答えられる——実際に押せる回答ボタン、単一のSwiftバイナリ、バックグラウンドで待機するものは何もない | `ai-agents` `claude-code` `macos` `macos-notifications` `notifications` | 0 | 2026-08-19 |
| [**herdr-telegram-notify**](https://github.com/elkraps/herdr-telegram-notify)<br><sub>elkraps</sub> | Herdrエージェントの状態変化に対する、カスタマイズ可能なTelegram通知——ステータスフィルタ、テンプレート、複数チャットへの配信、重複排除、Codex承認ボタン、完了サマリー、組み込みの診断機能に対応 | `ai-agents` `automation` `developer-tools` `javascript` `nodejs` | 0 | 🔄 2026-08-27 |
| [**🆕 herdr-oncall**](https://github.com/fulanto/herdr-oncall)<br><sub>fulanto</sub> | Herdr プラグイン：エージェントがブロックされたときに Telegram へ通知します。 | `javascript` | 0 | 🔄 2026-09-04 |
| [**herdr-random-sounds**](https://github.com/gridness/herdr-random-sounds)<br><sub>gridness</sub> | macOS版herdrで、エージェントの状態ごとにランダムな通知音を再生する | `herdr-integration` `macos` `notification` `notifications` `python` | 0 | 🔄 2026-08-23 |
| [**🆕 herdr-hitl**](https://github.com/huketo/herdr-hitl)<br><sub>huketo</sub> | Herdr のコーディングエージェントを、人の判断待ちで一時停止させ、Telegram や Discord 経由でスマホに通知します。 | `agent-skill` `ai-agents` `cli` `discord-bot` `go` | 0 | 🔄 2026-09-03 |
| [**🆕 herdr-webhook**](https://github.com/jefflau/herdr-webhook)<br><sub>jefflau</sub> | Herdr プラグイン：エージェントの完了・ブロックイベントを Webhook へ POST します。 | `python` | 0 | 🔄 2026-09-03 |
| [**herdr-slack-notify**](https://github.com/juninaba/herdr-slack-notify)<br><sub>juninaba</sub> | Herdrのエージェントが完了またはブロックされたら、Slack通知を送る | `javascript` | 0 | 2026-07-07 |
| [**drover-notify**](https://github.com/keinstn/drover-notify)<br><sub>keinstn</sub> | エージェントがブロックされたときにDroverのプッシュ通知を送るHerdrプラグイン | `javascript` | 0 | 2026-08-01 |
| [**🆕 herdr-rich-notifications**](https://github.com/liamwh/herdr-rich-notifications)<br><sub>liamwh</sub> | herdrのエージェント状態変化に対する、リッチなネイティブデスクトップ通知——LLM不要のコンテキスト拡充、クリックでフォーカス（herdrのエージェントフォーカス＋Niriウィンドウのターゲティング）に対応。quinnjr/herdr-notificationsのフォーク | `notifications` `rust` | 0 | 🔄 2026-08-28 |
| [**herdr-telegram-slack-bridge**](https://github.com/lsisoft/herdr-telegram-slack-bridge)<br><sub>lsisoft</sub> | Herdrのエージェントセッション向けの、TelegramとSlackボットの双方向ブリッジ——ブロックされたエージェントの通知やチャットの返信を、Herdrやtmuxのペインに転送する | `ai-agents` `slack-bot` `telegram-bot` `tmux` `python` | 0 | 2026-07-28 |
| [**🆕 herdr-pane-agent-unread**](https://github.com/NachoPal/herdr-pane-agent-unread)<br><sub>NachoPal</sub> | herdr向けの、ペインごとの「未読」通知＋サイドバーバッジ——見ていないペインで完了または入力待ちになったエージェントを浮かび上がらせる（herdrは「既読」をタブ単位で管理し、ペイン単位では管理しないため） | `python` | 0 | 🔄 2026-09-01 |
| [**herdr-plugin-telegram-notify**](https://github.com/OiAnthony/herdr-plugin-telegram-notify)<br><sub>OiAnthony</sub> | エージェントが完了またはブロックされたときにTelegram通知を送る、単体で動作するHerdrプラグイン | `javascript` | 0 | 2026-07-16 |
| [**herdr-apple-music-plugin**](https://github.com/perlporter/herdr-apple-music-plugin)<br><sub>perlporter</sub> | Apple Music（macOS）の再生曲が変わったときに、herdrでトースト通知を表示する | `shell` | 0 | 2026-07-28 |
| [**herdr-plugin-call-me**](https://github.com/radres/herdr-plugin-call-me)<br><sub>radres</sub> | herdrのエージェントがブロックされたら、実際の電話に着信させる——音声で応答すると、その返答がエージェントが待っていたキー入力になる | `ai-agents` `claude-code` `codex` `developer-tools` `notifications` | 0 | 🔄 2026-08-25 |
| [**herdr-notify-center**](https://github.com/ram4-dev/herdr-notify-center)<br><sub>ram4-dev</sub> | サーバー全体のエージェント通知を、永続化されたポップアップ受信箱でHerdrに提供する | `notifications` `typescript` | 0 | 2026-08-14 |
| [**herdr-cc-mac-notify**](https://github.com/y-hirakaw/herdr-cc-mac-notify)<br><sub>y-hirakaw</sub> | Claude Code向けのmacOS通知——「完了」だけでなく、エージェントの実際の最後のメッセージを表示する | `claude-code` `macos` `notifications` `python` | 0 | 2026-07-17 |

<details><summary>この目的にも関係するもの</summary>

- [donghaolicd/herdr-teams-notify](https://github.com/donghaolicd/herdr-teams-notify) — Microsoft Teamsへのエージェントライフサイクル通知を、送りすぎないように制御するHerdrプラグイン

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-remote"></a>

## スマホ・リモート操作

> 外出先やスマホからエージェントを監視して、承認だけ返したい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**collie**](https://github.com/AltanS/collie)<br><sub>AltanS</sub> | 外出先からherdrを管理できるPWA。Tailnet経由でアクセス可能、プッシュ通知やクイックアクションなど | `agent-orchestration` `ai` `ai-agents` `ai-coding` `ai-tools` | 746 | 🔄 2026-09-04 |
| [**herdr-remote**](https://github.com/dcolinmorgan/herdr-remote)<br><sub>dcolinmorgan</sub> | メニューバー・スマホ・Telegramからherdrのエージェントを監視・操作。ローカル設定不要、リモート接続用の無料トンネル付きでTailscaleも不要 | `macos` `mobile` `python` | 312 | 🔄 2026-09-01 |
| [**herdr-mobile-relay**](https://github.com/0cv/herdr-mobile-relay)<br><sub>0cv</sub> | スマホからHerdrのエージェントを遠隔で承認・監視できる、Android/iOS向けのモバイルWebアプリ。プッシュ通知・QRコードでの設定・複数PCへの中継に対応 | `android` `approvals` `cloudflare` `ios` `mobile` | 165 | 🔄 2026-09-03 |
| [**herdr-watch**](https://github.com/Unayung/herdr-watch)<br><sub>Unayung</sub> | herdrのエージェント状態をApple Watchで確認できる | `javascript` | 27 | 2026-08-14 |
| [**herdr-connect**](https://github.com/Tomyail/herdr-connect)<br><sub>Tomyail</sub> | この iPhone 用モバイルコンパニオンアプリで、Herdr の AI コーディングエージェントを監視・操作できます——出力を読み、追加の指示を送り、ジョブ完了時には通知を受け取れます。LAN や Tailscale 経由でプライベートに動作し、クラウドもアカウントも不要です。 | `agent` `mobile-app` `react-native` `typescript` | 12 | 🔄 2026-09-04 |
| [**herdr-plugin-mobile-relay**](https://github.com/benkraus/herdr-plugin-mobile-relay)<br><sub>benkraus</sub> | _(説明なし)_ | `typescript` | 11 | 2026-08-12 |
| [**🆕 herdr-telegram-agents**](https://github.com/permgps/herdr-telegram-agents)<br><sub>permgps</sub> | ターミナルからと同じように、Telegram からコーディングエージェントを操作できます。エージェントごとにトピックを分け、トピックアイコンにライブステータスを表示、選択肢はインラインボタン付きの双方向チャットで行えます。 | `claude-code` `coding-agents` `go` `telegram` `telegram-bot` | 11 | 🔄 2026-09-04 |
| [**herdr-push**](https://github.com/dcolinmorgan/herdr-push)<br><sub>dcolinmorgan</sub> | herdrプラグイン：依存なしでイベントをherdr-remoteにpushし、モバイルからの監視とワンタップ承認を可能にする | `shell` | 10 | 2026-07-09 |
| [**paddock**](https://github.com/lntvan166/paddock)<br><sub>lntvan166</sub> | herdr向けのモバイルファーストなダッシュボード——unixソケットを読み取る。設定不要でスマホ上で動く | `agent-orchestration` `coding-agents` `herdr-mobile` `paddock` `pwa` | 7 | 🔄 2026-09-03 |
| [**herdr-remote-panes**](https://github.com/Poor-Plebs/herdr-remote-panes)<br><sub>Poor-Plebs</sub> | 1つのHerdrから他のマシンで作業する——メニューからマシンを選ぶと、そのマシンのターミナルが得られる。実験的な双方向ミラーリングもオプションで利用可能 | `golang` `ssh` `terminal` `go` | 7 | 🔄 2026-09-04 |
| [**merino**](https://github.com/LoneExile/merino)<br><sub>LoneExile</sub> | Merino🐑——Herdrエージェント向けのリモートトンネルダッシュボード | `go` `macos` `menubar` `react` `wails` | 6 | 🔄 2026-08-23 |
| [**muqun-gateway**](https://github.com/osuki-dev/muqun-gateway)<br><sub>osuki-dev</sub> | Muqunが、あなた自身のコンピュータ上のターミナルにアクセスできるようにするプログラム。あなたのマシン上で動作し、tmuxまたはHerdrと通信し、あなたのスマホに直接応答する——アカウントも、間に入る当方のサーバーも存在しない | `rust` | 6 | 🔄 2026-09-03 |
| [**herdr-web**](https://github.com/barnuri/herdr-web)<br><sub>barnuri</sub> | herdr向けのモバイルファーストなWeb UIプラグイン——通知付きで、スマホからコーディングエージェントを操作できる | `pwa` `typescript` | 5 | 🔄 2026-09-01 |
| [**herdr-call**](https://github.com/eliasstravik/herdr-call)<br><sub>eliasstravik</sub> | Herdr向けの音声操作 | `elevenlabs` `tailscale` `voice` `typescript` | 5 | 2026-08-07 |
| [**herdr-web**](https://github.com/eyalev/herdr-web)<br><sub>eyalev</sub> | herdrのエージェントマルチプレクサ向けの、モバイルファーストなWeb UI——スマホからコーディングエージェントを操作できる | `claude-code` `mobile` `pwa` `terminal` `javascript` | 5 | 2026-07-29 |
| [**herdr-tether**](https://github.com/moneycaringcoder/herdr-tether)<br><sub>moneycaringcoder</sub> | Herdrのビューを閉じた後も、ローカル・リモートのターミナル処理を実行し続けさせる | `remote-development` `rust` `ssh` `terminal` `tmux` | 5 | 🔄 2026-09-01 |
| [**🆕 herdweb**](https://github.com/zlxlabs/herdweb)<br><sub>zlxlabs</sub> | スマホからコーディングエージェントを監視・操作できます。音声入力、画像の貼り付け、Webhook 通知、複数デバイス・サーバー対応。 | `typescript` | 5 | 🔄 2026-09-01 |
| [**herdr-portfwd**](https://github.com/miko-misa/herdr-portfwd)<br><sub>miko-misa</sub> | リモートマシン上のコーディングエージェント向けの自動SSHポートフォワーディング——エージェントが出力したlocalhost URLをCtrl+クリックすると、同じポートで手元のマシンにページが開く。Herdrプラグイン | `ai-agents` `claude-code` `cli` `coding-agents` `developer-tools` | 4 | 2026-08-11 |
| [**vscode-devcontainers-herdr**](https://github.com/scott-the-programmer/vscode-devcontainers-herdr)<br><sub>scott-the-programmer</sub> | devコンテナ内で動くエージェント向けのHerdrリレー | `container` `devcontainer` `rust` | 4 | 🔄 2026-09-03 |
| [**herdr-whistle**](https://github.com/amurru/herdr-whistle)<br><sub>amurru</sub> | リモートでのエージェント管理を行うHerdrプラグイン | `golang` `telegrambot` `go` | 3 | 2026-08-06 |
| [**herdr-mobile**](https://github.com/bsorescu/herdr-mobile)<br><sub>bsorescu</sub> | SSH経由でHerdrのコーディングエージェントを操作できる、スマホ向けTUI | `mobile` `ssh` `textual` `tui` `python` | 3 | 🔄 2026-08-25 |
| [**herdr-aws-ssm**](https://github.com/maayanyosef/herdr-aws-ssm)<br><sub>maayanyosef</sub> | EC2インスタンスを選択し、herdrの--remoteセッションでAWS SSM経由接続する——踏み台サーバーやパブリックIPは不要 | `aws-ssm` `terminal` `shell` | 3 | 2026-07-01 |
| [**herdr-farm**](https://github.com/mejiasd3v/herdr-farm)<br><sub>mejiasd3v</sub> | Herdrプラグイン：ワークスペースとエージェントを家畜として可視化する3D農場（three.js製Webアプリ） | `threejs` `javascript` | 3 | 2026-07-28 |
| [**herdr-devup**](https://github.com/alon-z/herdr-devup)<br><sub>alon-z</sub> | Herdrプラグイン：.herdr/dev.tomlからプロジェクトごとの開発用レイアウトを構築し、トンネルURLを環境変数に同期する | `typescript` | 2 | 2026-06-22 |
| [**herdr-topbar**](https://github.com/bigbug16/herdr-topbar)<br><sub>bigbug16</sub> | herdr向けのmacOSメニューバーアイコン——セッションに戻る、プロジェクトを開く、どのエージェントが入力待ちかを確認できる | `macos` `menubar` `swift` | 2 | 🔄 2026-08-24 |
| [**herdr-telegram-gate**](https://github.com/hkdom/herdr-telegram-gate)<br><sub>hkdom</sub> | herdrのAIエージェント群向けの、Telegram承認インボックス＋リスク階層別の自動承認——ブロックされたエージェントは承認/拒否ボタン付きのTelegramカードとして表示される（依存ライブラリなしのNode.js） | `approval-gate` `telegram` `javascript` | 2 | 2026-08-06 |
| [**herdr-remotedownloder**](https://github.com/kosuketut/herdr-remotedownloder)<br><sub>kosuketut</sub> | リモートのHerdrペインから、接続元のMacへファイルをダウンロードする | `rust` | 2 | 🔄 2026-08-24 |
| [**herdr-phone**](https://github.com/matheus3301/herdr-phone)<br><sub>matheus3301</sub> | Cloudflare TunnelとAccessを使った、Herdr向けのモバイルリモートコンソール | `cloudflare-tunnel` `coding-agents` `developer-tools` `golang` `mobile` | 2 | 🔄 2026-09-04 |
| [**herdr-web-tui**](https://github.com/tigorlazuardi/herdr-web-tui)<br><sub>tigorlazuardi</sub> | デーモン主体のHerdr向けブラウザ/PWAフロントエンド——オプションのプラグインランチャー付き | `go` | 2 | 🔄 2026-08-29 |
| [**herdr-hub**](https://github.com/alex-devdone/herdr-hub)<br><sub>alex-devdone</sub> | リモートアタッチしたペインで構成されるherdrセッションを、持ち運び可能なマニフェストとして記述し、どのマシンでも再構築できる | `python` | 1 | 🔄 2026-08-23 |
| [**herdrchat**](https://github.com/cobanov/herdrchat)<br><sub>cobanov</sub> | スマホ（iOS・Android）から herdr のコーディングエージェントを操作できます。 | `herdr-client` `herdr-integration` `herdr-mobile` `typescript` | 1 | 🔄 2026-08-27 |
| [**herdr-go**](https://github.com/herdr-go/herdr-go)<br><sub>herdr-go</sub> | どこからでもherdrのコーディングエージェントを操作できる——プライベートかつP2P、EasyTierによるセキュリティ付き | `dart` | 1 | 🔄 2026-09-02 |
| [**herdr-tunnel**](https://github.com/ivorpad/herdr-tunnel)<br><sub>ivorpad</sub> | herdrプラグイン：ローカルのポートを公開インターネットに公開し、URLをコピーし、また取り下げる | `tui` `python` | 1 | 🔄 2026-08-27 |
| [**🆕 herdr-mobile**](https://github.com/martebytes/herdr-mobile)<br><sub>martebytes</sub> | Mobile-first web UI for Herdr: see your agents, attach to panes, chat with Claude Code and Codex from your phone | `claude-code` `codex` `pwa` `python` | 1 | 🔄 2026-09-04 |
| [**herdview**](https://github.com/Orchard-Robotics/herdview)<br><sub>Orchard-Robotics</sub> | 自分の「herd」をWebから見る | `html` | 1 | 2026-07-17 |
| [**🆕 herdr-mobile-app**](https://github.com/teasec4/herdr-mobile-app)<br><sub>teasec4</sub> | スマホから herdr の AI エージェントを操作できます。 | `ai` `devtools` `flutter` `herdr-integration` `herdr-mobile` | 1 | 🔄 2026-09-03 |
| [**setnet**](https://github.com/chano-gpt/setnet)<br><sub>chano-gpt</sub> | スマホから複数harnessのコーディングエージェントを統率する——Herdrプラグイン | `typescript` | 0 | 🔄 2026-08-29 |
| [**herdr-slack**](https://github.com/egemenyildiz/herdr-slack)<br><sub>egemenyildiz</sub> | Slackからローカルのherdrエージェントを操作する——スマホから閲覧・プロンプト送信・起動ができる。トンネル不要 | `slack` `typescript` | 0 | 🔄 2026-09-03 |
| [**herdr-approval-gate**](https://github.com/Javamomma/herdr-approval-gate)<br><sub>Javamomma</sub> | herdr内のエージェントの操作に対する、人間による承認ゲート——専用ペインでタスクを実行し、その記録を判定チェックし、人間が「APPROVE <イニシャル>」と入力するまでブロックする | `shell` | 0 | 2026-07-15 |
| [**herdr-wechat-plugin**](https://github.com/LuYanFCP/herdr-wechat-plugin)<br><sub>LuYanFCP</sub> | WeChatによる遠隔操作を可能にするHerdrプラグイン | `rust` | 0 | 2026-07-17 |
| [**herdr-agents-bridge**](https://github.com/maedana/herdr-agents-bridge)<br><sub>maedana</sub> | ローカルのモバイル向けWeb UI経由で、スマホからコーディングエージェントを監視・操作する——QRコードをスキャンして接続 | `rust` | 0 | 2026-07-22 |
| [**🆕 hither**](https://github.com/T0mSIlver/hither)<br><sub>T0mSIlver</sub> | リモートマシン上の herdr ペインでキーの組み合わせを押すと、Mac 側で Zed がそのディレクトリを開きます。 | `shell` | 0 | 🔄 2026-09-02 |

<details><summary>この目的にも関係するもの</summary>

- [powerfooI/herdr-studio](https://github.com/powerfooI/herdr-studio) — Herdr 用の Web クライアント。モバイル体験を第一に考え、ブラウザ上のターミナル、ワークスペースと worktree の管理、ファイル・差分ビューア、AI エージェントのセッション確認までを提供します。
- [huketo/herdr-hitl](https://github.com/huketo/herdr-hitl) — Herdr のコーディングエージェントを、人の判断待ちで一時停止させ、Telegram や Discord 経由でスマホに通知します。
- [radres/herdr-plugin-call-me](https://github.com/radres/herdr-plugin-call-me) — herdrのエージェントがブロックされたら、実際の電話に着信させる——音声で応答すると、その返答がエージェントが待っていたキー入力になる

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-agents"></a>

## エージェント統括・並列実行

> 複数の AI エージェントをまとめて起動・分担・管理したい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**oh-my-opencode-slim**](https://github.com/alvinunreal/oh-my-opencode-slim)<br><sub>alvinunreal</sub> | 軽量でチューニング済みのOpencodeマルチエージェントスイート・どんなモデルでも組み合わせ可能・タスクを自動委任 | `agentic-ai` `antigravity` `cerebras` `oh-my-opencode` `opencode` | 8603 | 🔄 2026-09-02 |
| [**agentbox**](https://github.com/madarco/agentbox)<br><sub>madarco</sub> | コマンド一発で、サンドボックス化された複数のVM上にエージェントを並列実行（PCでもクラウドでも） | `claude` `claude-code` `cli` `cmux` `codex` | 384 | 🔄 2026-09-03 |
| [**pi-workflows**](https://github.com/osolmaz/pi-workflows)<br><sub>osolmaz</sub> | piコーディングエージェント向けの、ワークフローエンジン・JSON制御フローツール・ライブターミナルビューア | `typescript` | 261 | 🔄 2026-09-04 |
| [**pi-extensible-workflows**](https://github.com/vekexasia/pi-extensible-workflows)<br><sub>vekexasia</sub> | Pi向けの、決定論的なマルチエージェントワークフローオーケストレーション | `pi` `workflow` `workflows` `typescript` | 202 | 🔄 2026-09-03 |
| [**herdr-board**](https://github.com/nelsonPires5/herdr-board)<br><sub>nelsonPires5</sub> | herdr向けのカンバンボード——カードはそのままプロンプトになり、見えているペイン上のAIエージェントに割り振られる | `board` `kanban` `kanban-board` `tui` `rust` | 91 | 🔄 2026-08-23 |
| [**herdr-dagr**](https://github.com/aemrebarut/herdr-dagr)<br><sub>aemrebarut</sub> | エージェント群をライブなDAGとして表示——試行・レビューゲート・エビデンスを備えたオーケストレーショングラフを、herdrのスプリットペインに表示する | `agents` `dag` `multi-agent` `orchestration` `rust` | 60 | 🔄 2026-08-23 |
| [**herdr-file-annotator**](https://github.com/JonasBaeumer/herdr-file-annotator)<br><sub>JonasBaeumer</sub> | 実際のコードベースとの接点を失わずに、エージェントによる開発を最大限活用するためのherdrプラグイン | `rust` | 50 | 🔄 2026-09-01 |
| [**agentbox-herdr-plugin**](https://github.com/madarco/agentbox-herdr-plugin)<br><sub>madarco</sub> | コマンド一発で、サンドボックス化された複数のVM上にエージェントを並列実行（PCでもクラウドでも） | `claude-code` `codex-cli` `opencode` `sandbox` `shell` | 30 | 2026-06-24 |
| [**herdmates**](https://github.com/caioniehues/herdmates)<br><sub>caioniehues</sub> | herdrネイティブのClaude Codeエージェントチーム——teammuxシム、ミッションコントロールボード、フォーカスペイン | `agent-teams` `claude-code` `rust` `tui` | 24 | 🔄 2026-08-21 |
| [**pi-herd**](https://github.com/ribbons-digital/pi-herd)<br><sub>ribbons-digital</sub> | Herdrのペインとgit worktreeを使って、Piのセッションを可視化しながらオーケストレーションする | `typescript` | 17 | 2026-07-06 |
| [**herdr-agent-handoff**](https://github.com/sanirudh17/herdr-agent-handoff)<br><sub>sanirudh17</sub> | 進行中のエージェントセッションを、別のインストール済みコーディングエージェントの新規セッションに引き渡すHerdrプラグイン。セッション全体をプロンプト内にそのまま渡すため、要約や省略された履歴、追加の指示を書く必要がない | `agent-handoff` `claude-code` `codex` `coding-agents` `developer-tools` | 15 | 2026-08-14 |
| [**PromptPilot**](https://github.com/ivanarama/PromptPilot)<br><sub>ivanarama</sub> | Claude Codeやその他のAI CLI向けのバックグラウンドタスクキュー——Web UIとTelegramボット付き | `ai-agents` `claude-code` `telegram-bot` `python` | 14 | 🔄 2026-09-03 |
| [**herdr-vercel-sandbox-plugin**](https://github.com/vercel-labs/herdr-vercel-sandbox-plugin)<br><sub>vercel-labs</sub> | Herdrから、ターミナルベースのコーディングエージェントを隔離されたVercel Sandbox上で実行する | `javascript` | 13 | 2026-08-09 |
| [**herdr-browser**](https://github.com/StructuPath/herdr-browser)<br><sub>StructuPath</sub> | Herdr向けの操作可能なエージェントブラウザペイン——ライブストリーミング、実際の操作、アダプティブレンダリング、コンソール/ページエラー表示、録画、localhostルーティングに対応 | `terminal` `javascript` | 11 | 🔄 2026-08-23 |
| [**herdr-social-glass**](https://github.com/ythx-101/herdr-social-glass)<br><sub>ythx-101</sub> | macOS版Herdr向けの、スクリーンショット映えするSocial Glassテーマ＆ワークフロープラグイン | `macos` `multi-agent` `terminal-theme` `shell` | 11 | 🔄 2026-08-21 |
| [**agys**](https://github.com/quaywin/agys)<br><sub>quaywin</sub> | 汚染ゼロのサンドボックスにより、Herdr上のAntigravity CLIに手間いらずのマルチプロファイル分離とリアルタイムなクォータ追跡を提供する | `ai-agents` `antigravity` `cli` `context-window` `developer-tools` | 10 | 🔄 2026-09-03 |
| [**vibetty**](https://github.com/second-state/vibetty)<br><sub>second-state</sub> | MQTT経由でAIエージェントのターミナルをスマートデバイス（vibekeys、vibewatchなど）にライブ共有する。Herdrプラグインとしても利用可能 | `claude-code` `codex` `vibecoding` `rust` | 10 | 2026-08-17 |
| [**herdr-helpr**](https://github.com/sohanemon/herdr-helpr)<br><sub>sohanemon</sub> | プロンプトで操作する、herdr向けのワークスペース・ペイン管理 | `ai-agents` `bun` `cli` `developer-tools` `ink` | 8 | 2026-07-16 |
| [**herdr-catchup**](https://github.com/wilbeibi/herdr-catchup)<br><sub>wilbeibi</sub> | herdr向けのエージェント間コーディングセッション引き渡し：稼働中のペインから、Claude Code・Codex・Cursor・Cline・OpenCodeのセッションを要約・フォーク・他のエージェントへの引き渡しができる | `ai-agents` `claude-code` `codex` `coding-agents` `context-handoff` | 8 | 🔄 2026-08-28 |
| [**herdr-agent-messenger**](https://github.com/aashishd/herdr-agent-messenger)<br><sub>aashishd</sub> | 稼働中のHerdrペイン間で、AIエージェント同士が要点を絞った自己完結型のメッセージをやり取りできるようにする——1つのエージェントが、全コンテキストを共有せずに別のエージェントと作業を調整できる | `python` | 6 | 2026-08-02 |
| [**pier**](https://github.com/July24/pier)<br><sub>July24</sub> | Piはコーディングエージェントのキャリア、Herdrはターミナルワークスペースマネージャー。pierは、piがあえて省いている2つの機能——todoリストのループと対話的なサブエージェント——を追加し、herdrのペイン/タブ層をその見た目と操作の土台として与える | `pi-coding-agent` `typescript` | 6 | 🔄 2026-09-03 |
| [**herdr-triage**](https://github.com/natori-hrj/herdr-triage)<br><sub>natori-hrj</sub> | herdr向けの注意度トリアージ——あなたを最も必要としているエージェントを上位に並べる。長時間ブロックされたエージェントほど上に来る | `ai-agents` `triage` `rust` | 6 | 2026-07-23 |
| [**herdr-space-scoped-agents**](https://github.com/ShankyJS/herdr-space-scoped-agents)<br><sub>ShankyJS</sub> | エージェントパネルを、フォーカス中のスペースに限定して表示するherdrプラグイン | `coding-agents` `terminal` `go` | 6 | 2026-07-23 |
| [**herdr-swarm**](https://github.com/StructuPath/herdr-swarm)<br><sub>StructuPath</sub> | 1つのリポジトリで複数のコーディングエージェントを安全に並列実行：エージェントごとのworktree展開、変更のリアルタイム可視化、レビュー優先の成果回収をHerdr向けに提供 | `terminal` `javascript` | 6 | 🔄 2026-08-24 |
| [**herdr-scuttlebutt**](https://github.com/andybarilla/herdr-scuttlebutt)<br><sub>andybarilla</sub> | herdrセッション内のエージェントに、共有チャットルームを提供するherdrプラグイン | `rust` | 5 | 🔄 2026-08-31 |
| [**herdr-gamepad**](https://github.com/htlin222/herdr-gamepad)<br><sub>htlin222</sub> | ゲームコントローラーでHerdrを操作する。ソファに座ったままAIエージェントを見回り、ペインを分割し、ワークスペースを切り替えられる——どんなゲームパッドでも60秒で自分好みに割り当て可能 | `ai-agents` `gamepad` `macos` `swift` `terminal-multiplexer` | 5 | 2026-08-08 |
| [**🆕 herdr-world**](https://github.com/IvoryHeart/herdr-world)<br><sub>IvoryHeart</sub> | Herdr World——Herdr向けのマルチサーフェスなWeb体験 | `multi-agent` `observability` `pixel-art` `react` `rust` | 5 | 🔄 2026-09-03 |
| [**herdr-insight**](https://github.com/0x5c0f/herdr-insight)<br><sub>0x5c0f</sub> | エージェントの状態タイムラインパネル | `rust` | 4 | 2026-06-23 |
| [**shepherdr**](https://github.com/afogel/shepherdr)<br><sub>afogel</sub> | 委任したコーディングエージェントを、監視・再開・引き取りができる可視化されたherdrのペインに追い込むherdrプラグイン | `ai-agents` `claude-code` `codex` `cursor` `rust` | 4 | 2026-07-24 |
| [**herdr-orchestrate**](https://github.com/darjss/herdr-orchestrate)<br><sub>darjss</sub> | Pi向けのネイティブなオーケストレーション機能を、可視化されたHerdrのワーカーセッションで提供——実行状況ボード、永続的なプロンプト/レポート/状態、独立したgit worktree、明示的なモデルルーティングに対応 | `pi-package` `typescript` | 4 | 2026-07-13 |
| [**herdr-devcontainer**](https://github.com/gambtho/herdr-devcontainer)<br><sub>gambtho</sub> | 公式のDev Containers CLI経由で、リポジトリのDev Container内にシェルやコーディングエージェントを開くHerdrプラグイン | `coding-agents` `containers` `devcontainers` `developer-tools` `development-environment` | 4 | 2026-08-13 |
| [**herdr-espresso**](https://github.com/Hanyang-Li/herdr-espresso)<br><sub>Hanyang-Li</sub> | エージェントが動作中はMacBookを、蓋を閉じても眠らせない | `rust` | 4 | 2026-07-25 |
| [**herdr-fleet**](https://github.com/Northern-Lighthouse/herdr-fleet)<br><sub>Northern-Lighthouse</sub> | Tailscale経由でherdrマシンのフリートを管理——ダッシュボードプラグイン、自動検出、キャパシティを考慮したエージェント割り当て、ディスクレスなワークスペースに対応 | `ai-agents` `tailscale` `python` | 4 | 2026-08-14 |
| [**herdr-worker-orchestrator**](https://github.com/anhnd3005-infinity/herdr-worker-orchestrator)<br><sub>anhnd3005-infinity</sub> | Herdr管理下のペイン経由で、CLIエージェントワーカー（agy・codexなど）にタスクを割り振る——状態を持つタスク追跡、worktreeによる隔離、差分ベースのレビューに対応。Claude CodeとHerdrの両対応プラグイン | `html` | 3 | 🔄 2026-08-25 |
| [**herdr-theos-settler**](https://github.com/calebcauthon/herdr-theos-settler)<br><sub>calebcauthon</sub> | 完了したHerdrのエージェントタブやワークスペースを、作業中のものより下に沈めて視界から外す。Theoのアイデア | `rust` | 3 | 2026-07-23 |
| [**herdr-a2a**](https://github.com/IsaiasZc/herdr-a2a)<br><sub>IsaiasZc</sub> | A2A経由の、信頼性の高いHerdr向けエージェント間委任レイヤー | `typescript` | 3 | 🔄 2026-08-27 |
| [**herdr-walkietalkie**](https://github.com/jeffory/herdr-walkietalkie)<br><sub>jeffory</sub> | herdrプラグイン：トークン効率の良いエージェント間委任（wt）——オーケストレーター役のエージェントが、Claude/OpenCode/Antigravityのワーカーをタブやworktreeに立ち上げる | `shell` | 3 | 2026-08-12 |
| [**herdr-prompt-library**](https://github.com/jwkicklighter/herdr-prompt-library)<br><sub>jwkicklighter</sub> | ローカルまたはグローバルな再利用可能なMarkdownプロンプトを閲覧・管理し、フォーカス中のペインに挿入できるHerdrプラグイン | `go` `golang` `prompting` `snippets` `tui` | 3 | 🔄 2026-09-01 |
| [**herdr-agent-office**](https://github.com/suisya-systems/herdr-agent-office)<br><sub>suisya-systems</sub> | エージェント群をピクセルアートのオフィスとして表示するherdrプラグイン。誰が作業中で、誰が詰まっているかが分かり、そこにジャンプできる | `python` | 3 | 2026-07-25 |
| [**herdr-blaxel-sandbox-plugin**](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin)<br><sub>blaxel-ai</sub> | Herdrから、永続化されたBlaxel Sandbox上でコーディングエージェントを実行する | `blaxel` `claude-code` `codex` `coding-agents` `opencode` | 2 | 🔄 2026-09-03 |
| [**herdr-birdseye**](https://github.com/calebcauthon/herdr-birdseye)<br><sub>calebcauthon</sub> | herdr内のエージェントを鳥瞰図で見る | `rust` | 2 | 2026-07-24 |
| [**herdr-loop**](https://github.com/cyperx84/herdr-loop)<br><sub>cyperx84</sub> | herdr向けの宣言的でイベント駆動なループ＋グラフオーケストレーション——Claude Code・Codex・opencode・piをまとめて動かし、作業が収束するまで実行する | `ai-agents` `golang` `orchestration` `go` | 2 | 2026-08-12 |
| [**herdr-openclaw**](https://github.com/gejiliang/herdr-openclaw)<br><sub>gejiliang</sub> | herdrプラグイン：OpenClawのTUIペインを、herdrの正式なエージェントとして管理する | `openclaw` `terminal` `javascript` | 2 | 2026-08-13 |
| [**herdr-amphetamine-macos**](https://github.com/gw31415/herdr-amphetamine-macos)<br><sub>gw31415</sub> | エージェントが作業中の間、Amphetamineの持続時間を延長し続けるherdrプラグイン | `python` | 2 | 2026-07-09 |
| [**herdr-newtab-plus**](https://github.com/jeffarese/herdr-newtab-plus)<br><sub>jeffarese</sub> | どのフォルダとどのエージェントかを聞いてくるHerdrの新規タブ：実在するパスを補完し、作業場所を記憶し、代わりにエージェントを起動してくれる | `python` | 2 | 2026-07-26 |
| [**herdr-shame-report**](https://github.com/JYasha11/herdr-shame-report)<br><sub>JYasha11</sub> | AIエージェントをどれだけ待たせたかを、ずっと記録し続ける台帳。羊は忘れない | `javascript` | 2 | 2026-07-10 |
| [**herdr-orchestrator**](https://github.com/kylezk777/herdr-orchestrator)<br><sub>kylezk777</sub> | Herdr-orchは、Herdr上で動作するファイルベースのエージェントオーケストレーションツール | `agent-orchestration` `orchestrator` `rust` | 2 | 2026-07-26 |
| [**herdr-agents-status**](https://github.com/maedana/herdr-agents-status)<br><sub>maedana</sub> | Herdrのエージェントの状態を表示する、常に最前面の透明オーバーレイ——claudeyeの精神的後継で、tmuxではなくHerdr向けに作られた | `rust` | 2 | 2026-08-15 |
| [**chatter**](https://github.com/marcvermeeren/chatter)<br><sub>marcvermeeren</sub> | Chatterは、harnessをまたいだエージェント協働の実験的プロジェクト——Herdr上で同じGitリポジトリを扱うエージェント同士の、共有グループチャット＆コンテキストレイヤーを提供する | `agent-collaboration` `agentic-ai` `agentic-workflow` `ai-agents` `group-chat` | 2 | 2026-08-18 |
| [**herdr-agent-profiles**](https://github.com/mikeyobrien/herdr-agent-profiles)<br><sub>mikeyobrien</sub> | Herdr向けの、データ駆動のCLIハーネスとモデルプロファイル | `ai-agents` `terminal` `python` | 2 | 2026-08-10 |
| [**herdr-redact**](https://github.com/moneycaringcoder/herdr-redact)<br><sub>moneycaringcoder</sub> | エージェントのペインが認証情報を出力したときに警告する——スクリーンショットを撮ったり、配信したり、チャットウィンドウに貼り付けたりする前に気づける | `rust` `secret-detection` `security` `terminal` | 2 | 🔄 2026-09-01 |
| [**herdr-approve-all**](https://github.com/RenKoya1/herdr-approve-all)<br><sub>RenKoya1</sub> | herdrプラグイン：ブロックされている全エージェントを一括承認（1キーで、保留中の許可プロンプトすべてに応答） | `shell` | 2 | 2026-08-16 |
| [**🆕 herdr-code-board**](https://github.com/sazardev/herdr-code-board)<br><sub>sazardev</sub> | Herdr内の、エージェント向けプロンプトのカンバンキュー——カードが実際のエージェントをペイン・worktree・ワークスペースに配置し、カード同士を連鎖させるルールも設定できる | `ai-agents` `kanban` `rust` `tui` | 2 | 🔄 2026-08-30 |
| [**herdr-agents-history**](https://github.com/speardragon/herdr-agents-history)<br><sub>speardragon</sub> | AIコーディングエージェントが実際に何をしているかを見る——すべてのエージェント（Claude CodeとCodex）のツール呼び出しをリアルタイムに流し続ける、キーボード操作のherdr TUI | `ai-agents` `claude-code` `codex` `tui` `typescript` | 2 | 2026-07-19 |
| [**herdr-conductor**](https://github.com/StructuPath/herdr-conductor)<br><sub>StructuPath</sub> | 機能開発チームを、見えるHerdrのエージェントペインとしてオーケストレーションする——Conductorプラグイン | `orchestration` `javascript` | 2 | 🔄 2026-08-23 |
| [**herdr-wakeup**](https://github.com/usrivastava92/herdr-wakeup)<br><sub>usrivastava92</sub> | Herdrが管理するエージェントが作業中の間、macOSまたはLinuxをスリープさせないHerdrプラグイン | `power-management` `sleep-prevention` `wakeup` `rust` | 2 | 2026-07-17 |
| [**herdr-agent-timer**](https://github.com/Yemeni/herdr-agent-timer)<br><sub>Yemeni</sub> | 各エージェントのステータスラベルと経過時間を交互に表示するHerdrプラグイン | `shell` | 2 | 2026-08-14 |
| [**herdr-pouch**](https://github.com/AltanS/herdr-pouch)<br><sub>AltanS</sub> | herdrプラグイン：エージェント向けのプロンプトを事前に貯めておき、準備ができたら挿入する | `ai-agents` `ai-coding` `ai-tools` `multiplexing` `typescript` | 1 | 🔄 2026-09-02 |
| [**herdr-pi-reloader**](https://github.com/anrunt/herdr-pi-reloader)<br><sub>anrunt</sub> | Herdrのオーバーレイ TUIから、アイドル状態のPiエージェントセッションをリロードまたは再起動する | `rust` | 1 | 2026-07-18 |
| [**herdr-pane-topic-sync**](https://github.com/danbuhler/herdr-pane-topic-sync)<br><sub>danbuhler</sub> | herdrプラグイン：ペインとタブの名前を「1」「2」「3」ではなく、各エージェント（Claude Code、Codexなど）のリアルタイムのトピックから自動で付ける | `ai-agents` `claude-code` `terminal` `tmux-alternative` `javascript` | 1 | 🔄 2026-09-02 |
| [**herdr-handoff**](https://github.com/devops-fj/herdr-handoff)<br><sub>devops-fj</sub> | Herdrのコーディングエージェント間で、ローカルの作業コンテキストをプレビューし安全に引き継ぐ | `ai-agents` `coding-agents` `go` | 1 | 🔄 2026-08-21 |
| [**herdr-agent-team**](https://github.com/gdli6177/herdr-agent-team)<br><sub>gdli6177</sub> | Markdownでエージェントチームを定義できるHerdrプラグイン | `javascript` | 1 | 2026-08-16 |
| [**herdr-prompt-bucket**](https://github.com/GNURub/herdr-prompt-bucket)<br><sub>GNURub</sub> | Herdr上で動くコーディングエージェント向けの、永続化された順序付きプロンプトバケット | `claude-code` `codex` `coding-agents` `opencode` `typescript` | 1 | 2026-08-19 |
| [**LunaCrab**](https://github.com/GranamyrBR/LunaCrab)<br><sub>GranamyrBR</sub> | 別プロジェクト用に予約済み | `agents` `developer-tools` `multi-agent` `observability` `rust` | 1 | 2026-08-10 |
| [**🆕 agent-keep-awake**](https://github.com/happyeric77/agent-keep-awake)<br><sub>happyeric77</sub> | Herdrのエージェントが動作中は、macOSのスリープを防止する | `javascript` | 1 | 2026-08-12 |
| [**herdr-dispatch**](https://github.com/husniadil/herdr-dispatch)<br><sub>husniadil</sub> | herdr-tasksボード用のディスパッチャー——準備完了したタスクごとにワーカーエージェントのペインを立て、目標を伝え、ワーカーを追跡し、レビューで一旦止める。すべて1つのGoバイナリで実現 | `agent-orchestration` `ai-agents` `dispatcher` `mcp-server` `go` | 1 | 🔄 2026-08-31 |
| [**herdr-annotations**](https://github.com/IgorWarzocha/herdr-annotations)<br><sub>IgorWarzocha</sub> | ターミナルで選択した箇所に注釈を集め、Herdrのエージェントに投入する | `ai-agents` `annotations` `terminal` `javascript` | 1 | 2026-07-18 |
| [**herdr-plan-approve**](https://github.com/jerryfane/herdr-plan-approve)<br><sub>jerryfane</sub> | herdrでClaude Codeのplanモードダイアログを自動承認する——エージェントは計画を立て、キー入力なしでそのまま実行に移れる | `claude-code` `shell` | 1 | 🔄 2026-08-25 |
| [**corral**](https://github.com/jirathip-dev/corral)<br><sub>jirathip-dev</sub> | herdr のコーディングエージェント群を読み取り専用で監視できます（iOS・egui 製）。 | `agent-orchestration` `ai-agents` `coding-agents` `devtools` `fleet-management` | 1 | 🔄 2026-09-04 |
| [**herdr-watcher**](https://github.com/joshka0/herdr-watcher)<br><sub>joshka0</sub> | Herdrエージェント向けの、永続的な処理継続とデタッチされたワーカーコールバック | `rust` | 1 | 2026-08-02 |
| [**herdr-turn-coordinator**](https://github.com/KarthusLorin/herdr-turn-coordinator)<br><sub>KarthusLorin</sub> | モデル主導のステータスポーリングに頼らずに、対話的なHerdrエージェントTUIを維持する | `ai-agents` `python` | 1 | 🔄 2026-09-04 |
| [**herdr-island**](https://github.com/kay-ws/herdr-island)<br><sub>kay-ws</sub> | あなたの対応を待っているエージェントを見つける——各herdrエージェントが止まった理由を表示し、Agentsパネルを該当するものだけに絞り込む | `shell` | 1 | 2026-08-04 |
| [**herdr-link**](https://github.com/LZHcode1986/herdr-link)<br><sub>LZHcode1986</sub> | Herdrのセッション向けに、より高速でトークン効率が良く推論不要なエージェント間相互運用性を提供する。重量級のskillを、ピア発見・メッセージング・ペインのライフサイクルを扱う統一されたコントラクトで置き換える | `typescript` | 1 | 🔄 2026-09-01 |
| [**sheprd**](https://github.com/m-mohamed/sheprd)<br><sub>m-mohamed</sub> | Pi・Codex・Claude Code・OpenCodeを、可視化された1つの独立したHerdr「Flok」にまとめる | `agent-tools` `claude-code` `cli` `codex` `coding-agents` | 1 | 🔄 2026-08-25 |
| [**herdr-agents-preview**](https://github.com/maedana/herdr-agents-preview)<br><sub>maedana</sub> | Herdr向けのマルチエージェントターミナルプレビューダッシュボード：稼働中のすべてのエージェントを同時に表示し、選択中のエージェントが大部分の幅を占める | `rust` | 1 | 2026-08-14 |
| [**herdr-standup**](https://github.com/natori-hrj/herdr-standup)<br><sub>natori-hrj</sub> | herdr向けのエージェントスタンドアップ——各エージェントのリポジトリ全体で、コミットと未コミットの作業をエージェントごとに要約する | `ai-agents` `git` `standup` `rust` | 1 | 2026-07-23 |
| [**herdr-replay**](https://github.com/neospeed83/herdr-replay)<br><sub>neospeed83</sub> | マルチエージェントのHerdrコーディングセッションを、インタラクティブなタイムラインとして記録・再生する | `ai-agents` `developer-tools` `terminal-recording` `rust` | 1 | 🔄 2026-08-29 |
| [**🆕 herdr-tournament**](https://github.com/neospeed83/herdr-tournament)<br><sub>neospeed83</sub> | Herdr向けの、対抗的なマルチエージェントコードレビュー | `rust` | 1 | 🔄 2026-08-29 |
| [**herdr-caffeinate**](https://github.com/nwarwick/herdr-caffeinate)<br><sub>nwarwick</sub> | Herdrのエージェントが動作中は、macOSのシステムスリープを防止する | `caffeinate` `coding-agents` `macos` `shell` | 1 | 2026-07-29 |
| [**herdr-spawn**](https://github.com/nytafar/herdr-spawn)<br><sub>nytafar</sub> | 1つのMCPツールで、チャットからのプロンプトを、リモートコントロールを有効にした手元のホスト上の実際のClaude Codeセッションに渡す | `python` | 1 | 🔄 2026-08-21 |
| [**herdr-imebox**](https://github.com/Sawakee/herdr-imebox)<br><sub>Sawakee</sub> | herdr内のAIエージェントペインに日本語・CJKを入力しやすくする、IME対応のポップアップテキストボックス | `cjk` `ime` `input-method` `japanese` `ratatui` | 1 | 2026-07-17 |
| [**🆕 herdr-achievements**](https://github.com/SerHappy/herdr-achievements)<br><sub>SerHappy</sub> | あなたのHerdr AIエージェントの群れに、実績とささやかなお祝いを追加する | `achievements` `ai-agents` `developer-tools` `gamification` `go` | 1 | 2026-07-30 |
| [**herdr-awake**](https://github.com/susomejias/herdr-awake)<br><sub>susomejias</sub> | herdrプラグイン：Herdrのエージェントが作業中の間、マシンをスリープさせない | `shell` | 1 | 🔄 2026-08-26 |
| [**herdr-traex**](https://github.com/szrenwei/herdr-traex)<br><sub>szrenwei</sub> | TraeXエージェントのライフサイクルとメタデータをHerdr Marketplaceと連携させる | `traex` `python` | 1 | 2026-08-04 |
| [**herdr-orc**](https://github.com/tamdogood/herdr-orc)<br><sub>tamdogood</sub> | Herdr向けの、プロファイル駆動でカスタマイズ可能な最小構成のオーケストレーター | `ai-agents` `multi-agent` `orchestrator` `javascript` | 1 | 2026-08-11 |
| [**tinysend-herdr**](https://github.com/tiny-send/tinysend-herdr)<br><sub>tiny-send</sub> | herdrプラグイン：エージェントがブロック/完了したら自分にメールを送り、返信でブロック解除できる。tinysendを使用 | `ai-agents` `tinysend` `javascript` | 1 | 2026-06-26 |
| [**🆕 herdr-rovo-dev**](https://github.com/usrivastava92/herdr-rovo-dev)<br><sub>usrivastava92</sub> | Rovo Dev CLIのセッションを検出し、Herdr上で稼働中のエージェントとして報告するHerdrプラグイン | `ai-agent` `rovo` `rovo-dev` `shell` | 1 | 2026-07-19 |
| [**herdr-polyglot**](https://github.com/wazum/herdr-polyglot)<br><sub>wazum</sub> | コーディングエージェントへのプロンプトを自分の言語で書ける——DeepLまたはGoogle Cloud Translateが英語に翻訳し、Claude Code・Codex・その他任意のherdrエージェントペインに届ける | `ai-agents` `bubbletea` `bubbletea-tui` `claude-code` `codex` | 1 | 🔄 2026-09-01 |
| [**herdr-auto-yes-sir**](https://github.com/xlinx/herdr-auto-yes-sir)<br><sub>xlinx</sub> | herdr-auto-yes-sir——エージェントが承認を求めてきたときに、ブロックされずに実行を続けられるようにする。codexのような挙動 | `javascript` | 1 | 🔄 2026-08-20 |
| [**herdr-cadence**](https://github.com/zhenyufu/herdr-cadence)<br><sub>zhenyufu</sub> | 1人のLeadと複数のエージェント群からなる、軽量なエージェントオーケストレーター | `rust` | 1 | 🔄 2026-08-25 |
| [**🆕 herdr-muse**](https://github.com/akshat12/herdr-muse)<br><sub>akshat12</sub> | Herdr integration for Muse Code: idle/working/blocked pane state via lifecycle hooks (no Herdr fork needed) | `ai-agents` `cli` `coding-agents` `muse-code` `terminal` | 0 | 🔄 2026-09-04 |
| [**herdr-simple-prompts**](https://github.com/AlexSamarsky/herdr-simple-prompts)<br><sub>AlexSamarsky</sub> | CodexやClaudeとのやり取りから、自分のプロンプトと最終回答だけを表示する。入力用のコンポーザー付き | `rust` | 0 | 🔄 2026-08-31 |
| [**🆕 herdr-dynamic-workflow**](https://github.com/andthezhang/herdr-dynamic-workflow)<br><sub>andthezhang</sub> | Herdr内でコーディングエージェントCLIをオーケストレーションするための、JavaScript製ワークフロー | `agent-fleet` `agent-orchestration` `agent-swarm` `agentic-ai` `agents` | 0 | 🔄 2026-08-30 |
| [**unblock**](https://github.com/aneym/unblock)<br><sub>aneym</sub> | エージェントがあなたに求めるものすべてを1つのキューにまとめる。ブロッカーにはアクションが、grillには判断が必要——シークレットがモデルのコンテキストに入ることはない | `agents` `human-in-the-loop` `mcp` `javascript` | 0 | 🔄 2026-08-28 |
| [**hird**](https://github.com/aoprisan/hird)<br><sub>aoprisan</sub> | 複数のharnessをまたぐエージェントの作業キューと共有アサーションメモリを、1つのローカルSQLiteデータベースで支える | `ai-agents` `claude-code` `cli` `mcp` `rust` | 0 | 🔄 2026-08-22 |
| [**herdr-quick-prompt**](https://github.com/astwys/herdr-quick-prompt)<br><sub>astwys</sub> | あらかじめ定義したプロンプトをエージェントのペインに送信するHerdrプラグイン | `shell` | 0 | 🔄 2026-08-24 |
| [**otito-herdr-plugin**](https://github.com/BASHBOP/otito-herdr-plugin)<br><sub>BASHBOP</sub> | Herdrのエージェントワークスペース内で、Otitoのコンテキストと決定論的なマージ証跡を実行する | `ai-agents` `developer-tools` `merge-safety` `otito` `javascript` | 0 | 🔄 2026-08-21 |
| [**herdr-agent-manager**](https://github.com/bleedingfight/herdr-agent-manager)<br><sub>bleedingfight</sub> | fzfベースのファジー検索で、workspace・tab・pane・agentを扱うツール | `python` | 0 | 🔄 2026-08-27 |
| [**herdr-warp**](https://github.com/cdpath/herdr-warp)<br><sub>cdpath</sub> | Herdrのペイン内で対話型のWarp Agent CLI（warp）を操作するHerdrプラグイン：open/send/status/wait/read/approve/deny/new/stop/exitに対応し、画面をスクレイピングしてidle/working/blockedの状態を判定する | `shell` | 0 | 2026-08-13 |
| [**clawsouls-herdr-plugin**](https://github.com/clawsouls/clawsouls-herdr-plugin)<br><sub>clawsouls</sub> | _(説明なし)_ | `ai-agents` `persona` `shell` | 0 | 2026-08-11 |
| [**herdr-tuple-plugin**](https://github.com/doggyfish/herdr-tuple-plugin)<br><sub>doggyfish</sub> | 2つのコーディングエージェントを1つのタブに並べてペアにし、両者の間でテキストをやり取りできるherdrプラグイン | `javascript` | 0 | 2026-08-08 |
| [**herdr-chat**](https://github.com/eliasstravik/herdr-chat)<br><sub>eliasstravik</sub> | Herdr内で動くエージェント向けの、構造化されたライブチャットビュー | `typescript` | 0 | 🔄 2026-08-24 |
| [**herdr-nudge**](https://github.com/EricBois/herdr-nudge)<br><sub>EricBois</sub> | herdrのエージェントに「継続を促す通知」を仕掛ける——指定した時刻、またはアイドル/ブロック状態になったときに発火する | `shell` | 0 | 2026-07-17 |
| [**herdr-cursor**](https://github.com/gabriel-laet/herdr-cursor)<br><sub>gabriel-laet</sub> | Cursorのクラウドエージェントを、herdrの正式なペインとして扱う | `typescript` | 0 | 🔄 2026-08-21 |
| [**ezdras-herdr**](https://github.com/GranamyrBR/ezdras-herdr)<br><sub>GranamyrBR</sub> | Herdr向けの、複数エージェントをリアルタイムに可視化する仕組みとペイン操作機能 | `rust` | 0 | 2026-08-10 |
| [**herdr-mail**](https://github.com/husniadil/herdr-mail)<br><sub>husniadil</sub> | Herdr上のコーディングエージェント同士の非同期メール——ストアを正とするメールボックス、ヒントとなる1行のペインマーカー、追跡可能な依頼付きのask/replyを、1つのGoバイナリで実現 | `ai-agents` `mail` `mcp-server` `sqlite` `go` | 0 | 🔄 2026-08-30 |
| [**herdr-ai-memory**](https://github.com/iagogfe/herdr-ai-memory)<br><sub>iagogfe</sub> | Herdrプラグイン：ai-memoryが管理するワークストリーム経由でコーディングエージェントを起動する——エージェントをまたいだセッションの継続性を実現 | `ai-agents` `ai-memory` `terminal` `javascript` | 0 | 2026-07-24 |
| [**herdr-pane-id**](https://github.com/imtim/herdr-pane-id)<br><sub>imtim</sub> | herdrプラグイン：ペインにIDとエージェント名、さらにタブ・ワークスペースのIDラベルを付ける——あなたとエージェントの両方が、IDで任意のペインやエージェントを指定できるようになる。herdrのagentスキルと組み合わせると最も効果を発揮する | `ai-agents` `coding-agents` `developer-tools` `terminal-multiplexer` `tui` | 0 | 🔄 2026-08-24 |
| [**herdr-spawn**](https://github.com/JLighter/herdr-spawn)<br><sub>JLighter</sub> | herdrプラグイン：プロンプトを渡してコーディングエージェントを起動——エージェントごとに専用のgit worktreeを割り当てる | `shell` | 0 | 2026-08-03 |
| [**herdr-suffix-agent-filter**](https://github.com/kazimshah39/herdr-suffix-agent-filter)<br><sub>kazimshah39</sub> | HerdrのAgentsサイドバーを、正確なSpaceサフィックスによるグループ表示とデフォルト表示の間で切り替える | `coding-agents` `developer-tools` `terminal` `javascript` | 0 | 🔄 2026-08-27 |
| [**herdr-kit**](https://github.com/kevinWangSheng/herdr-kit)<br><sub>kevinWangSheng</sub> | Herdr向けの、宣言的レイアウト・イベントウォッチャー・プラグイン・ソケットクライアント——herdr CLIが公開していない部分を補う | `coding-agents` `terminal-multiplexer` `python` | 0 | 2026-08-14 |
| [**led-agent-status**](https://github.com/lfsmoura/led-agent-status)<br><sub>lfsmoura</sub> | herdrプラグイン：AIエージェントの状態をBLE LEDテープに表示する——作業中は青、ブロック中は赤の点滅、完了で緑 | `ble` `led` `swift` | 0 | 2026-08-10 |
| [**herdr-claude-launcher**](https://github.com/lucasleon2107/herdr-claude-launcher)<br><sub>lucasleon2107</sub> | Claude Codeが起動済みの新規タブを開くherdrプラグイン | `ai-agents` `claude-code` `terminal` `tmux` `shell` | 0 | 2026-08-03 |
| [**herdr-alias-setter**](https://github.com/m2selfA/herdr-alias-setter)<br><sub>m2selfA</sub> | ペイン名とエージェントのエイリアスを設定できるHerdrプラグイン（クイック入力またはフルメニュー） | `powershell` | 0 | 🔄 2026-08-21 |
| [**quickTUI**](https://github.com/marcjfj-vmlyr/quickTUI)<br><sub>marcjfj-vmlyr</sub> | OpenTUI上で動く、組み合わせるだけで素早くターミナルUIを作れるプリミティブ集。コーディングエージェントに/quicktuiスキルを与えるHerdrプラグインとして提供される | `bun` `opentui` `terminal` `tui` `typescript` | 0 | 2026-08-13 |
| [**herdr-agent-dash**](https://github.com/MartinBspheroid/herdr-agent-dash)<br><sub>MartinBspheroid</sub> | Herdr Agent Board：稼働中のコーディングエージェント、その状態・作業ディレクトリ・Gitコンテキストを一目で確認できる、ローカルでキーボード操作中心のHerdrプラグイン | `typescript` | 0 | 2026-07-21 |
| [**herdr-green**](https://github.com/natori-hrj/herdr-green)<br><sub>natori-hrj</sub> | herdr向けのエージェントごとのテスト状態表示——エージェントが完了したらプロジェクトのテストを実行し、成功/失敗を表示する | `ai-agents` `ci` `tests` `rust` | 0 | 2026-07-23 |
| [**🆕 agentic-box**](https://github.com/nicoRomeroCuruchet/agentic-box)<br><sub>nicoRomeroCuruchet</sub> | Claude Codeがローカルモデルのエージェントを操作する、隔離されたbox | `agent-orchestration` `agentic` `agentic-workflow` `docker` `ornith-1-0-35b` | 0 | 2026-08-17 |
| [**herdr-plugin-aos**](https://github.com/noctaIO/herdr-plugin-aos)<br><sub>noctaIO</sub> | 任意のワークスペースから、Agentic OS対応のClaude Codeエージェントをherdrのペインで起動する。非侵襲的なherdrプラグイン | `shell` | 0 | 2026-07-11 |
| [**herdr-prompts**](https://github.com/oppenheimor/herdr-prompts)<br><sub>oppenheimor</sub> | Herdr内の各コーディングエージェントをまたいで、プロンプトテンプレートを保存・検索・穴埋め・再利用できる。友人のbingguanqiに着想を得て制作 | `typescript` | 0 | 2026-08-19 |
| [**🆕 herdr-guard**](https://github.com/pauljohnchamberlain/herdr-guard)<br><sub>pauljohnchamberlain</sub> | Codex や Claude など、コーディングエージェントから Herdr を安全に外部制御できるようにします。 | `coding-agents` `typescript` | 0 | 🔄 2026-09-04 |
| [**herdr-sidekick**](https://github.com/qapquiz/herdr-sidekick)<br><sub>qapquiz</sub> | Herdr向けの、開閉切り替え可能なサイドキックAIエージェントペイン——選択したコードを、送信せずにエージェントのコンポーザーに貼り付けられる。qapquiz/herdr-sidekick.nvimと組み合わせて使う | `neovim` `terminal` `shell` | 0 | 2026-08-15 |
| [**ocean-herdr**](https://github.com/Risingtides-dev/ocean-herdr)<br><sub>Risingtides-dev</sub> | Herdr向けのOceanエージェント連携 | `coding-agent` `ocean` `rust` | 0 | 2026-07-17 |
| [**herdr-want-to-sleep**](https://github.com/scheron/herdr-want-to-sleep)<br><sub>scheron</sub> | コーディングエージェントが全て動作を終えたら、Macをスリープさせるherdrプラグイン。就寝前にセットしておけば全エージェントの完了を待ち、ブロックされたものも含めて各エージェントが何をしていたかを記録してくれる | `coding-agents` `macos` `shell` | 0 | 2026-07-28 |
| [**herdr-ask**](https://github.com/TaylorFinklea/herdr-ask)<br><sub>TaylorFinklea</sub> | Herdrや任意のターミナル向けの、軽量なコマンド生成とターミナルチャット | `cli` `rust` `terminal` `tui` | 0 | 2026-07-21 |
| [**herdr-restart-always**](https://github.com/terafin/herdr-restart-always)<br><sub>terafin</sub> | herdrのエージェントペインを監視し、エージェントが死んだら、そのペインで動いていたもの（claude・hermes・codex・pi・opencodeなど）を常に再起動する | `python` | 0 | 2026-08-15 |
| [**herdr-group-chat**](https://github.com/terry-li-hm/herdr-group-chat)<br><sub>terry-li-hm</sub> | Pi・Claude Code・Codex・Grok Buildのための、共有ローカルHerdrルーム | `ai-agents` `claude-code` `codex` `grok` `multi-agent` | 0 | 🔄 2026-09-03 |
| [**herdr-cline-plugin**](https://github.com/TheMetalStorm/herdr-cline-plugin)<br><sub>TheMetalStorm</sub> | 任意のペインから起動した素のCline CLIを、ネイティブのHerdrエージェントのように見せるHerdrプラグイン | `cli` `cline` `herdr-integration` `shell` | 0 | 2026-07-31 |
| [**🆕 herdr-cmd-agent-plugin**](https://github.com/thesimonharms/herdr-cmd-agent-plugin)<br><sub>thesimonharms</sub> | CommandCode（cmd）をエージェントとして認識するHerdrプラグイン——画面マニフェストとcmd modによるidle/working/blockedの判定に対応 | `cmd` `commandcode` `shell` | 0 | 🔄 2026-08-31 |
| [**herdr-agent-notes**](https://github.com/timjonez/herdr-agent-notes)<br><sub>timjonez</sub> | herdrプラグイン：エージェントに付箋メモを付けられるので、なぜアイドルになっているのかが分かる | `python` | 0 | 🔄 2026-08-20 |
| [**herdr-agent-topic**](https://github.com/wynemo/herdr-agent-topic)<br><sub>wynemo</sub> | herdrプラグイン：各エージェントカードに、直近のユーザープロンプトを表示する | `go` | 0 | 2026-08-20 |
| [**🆕 cbds**](https://github.com/zqkra/cbds)<br><sub>zqkra</sub> | Herdrの群れ向けの、信頼性の高いマルチエージェントオーケストレーション。永続化されたタスク、権威あるワーカーレポート、ハングしない待機処理を提供する | `agents` `cli` `multi-agent` `orchestration` `javascript` | 0 | 🔄 2026-08-31 |

<details><summary>この目的にも関係するもの</summary>

- [AltanS/collie](https://github.com/AltanS/collie) — 外出先からherdrを管理できるPWA。Tailnet経由でアクセス可能、プッシュ通知やクイックアクションなど
- [a2u/herdr-jira](https://github.com/a2u/herdr-jira) — herdr向けのJira TUIプラグイン——設定可能なJQLフィルタでissueを閲覧・検索・ステータス変更し、1キーでターミナル上のAIエージェントにissueを委任できる
- [walcew/herdr-assist](https://github.com/walcew/herdr-assist) — AIコーディングエージェント向けターミナルマルチプレクサHerdrのための、物理デスクパネル——セッションの状態を色で表示し、エージェントが判断を仰ぐために止まるとベルを鳴らす。ESP32-S3 + LVGL、ビルド済…
- [e2b-dev/herdr-e2b-sandbox](https://github.com/e2b-dev/herdr-e2b-sandbox) — git worktreeをE2B Sandboxにミラーするherdrプラグイン——単一のboxでも、エージェントごとにブランチを割り当てたフリートでも対応。TUIダッシュボード付き
- [miko-misa/herdr-portfwd](https://github.com/miko-misa/herdr-portfwd) — リモートマシン上のコーディングエージェント向けの自動SSHポートフォワーディング——エージェントが出力したlocalhost URLをCtrl+クリックすると、同じポートで手元のマシンにページが開く。Herdrプラグイン
- [JefeLabs/herdr-web-broker](https://github.com/JefeLabs/herdr-web-broker) — herdr向けの自己ホスト型REST/WS API——どこからでもコーディングエージェントを起動・操作できる。トークン、マルチユーザーのセッション所有権、gitコマンド、イベントストリーミング、親子間フェデレーションに…

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-worktree"></a>

## git worktree・ブランチ運用

> 作業ごとに worktree を切って、片付けまで自動でやりたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-worktrunk**](https://github.com/devashish2203/herdr-worktrunk)<br><sub>devashish2203</sub> | git worktree管理のためworktrunkを統合するHerdrプラグイン | `shell` | 124 | 🔄 2026-08-27 |
| [**herdr-plugin-jj-workspace**](https://github.com/NathanFlurry/herdr-plugin-jj-workspace)<br><sub>NathanFlurry</sub> | Jujutsu (jj) のワークスペースをHerdrのワークスペースとして作成・削除する | `jujutsu` `rust` | 47 | 🔄 2026-09-03 |
| [**🆕 herdr-studio**](https://github.com/powerfooI/herdr-studio)<br><sub>powerfooI</sub> | Herdr 用の Web クライアント。モバイル体験を第一に考え、ブラウザ上のターミナル、ワークスペースと worktree の管理、ファイル・差分ビューア、AI エージェントのセッション確認までを提供します。 | `ai-agents` `dogfooding` `git-worktree` `herdr-client` `mobile-friendly` | 32 | 🔄 2026-09-03 |
| [**herdr-plugin-renamer**](https://github.com/wyattjoh/herdr-plugin-renamer)<br><sub>wyattjoh</sub> | エージェントへの最初のプロンプトから、自動生成されたherdrのworktreeブランチとワークスペースをリネームする（デバイス上のApple FoundationModelsまたはCodexを利用） | `rust` | 12 | 2026-08-17 |
| [**jj-waltz**](https://github.com/EzraCerpac/jj-waltz)<br><sub>EzraCerpac</sub> | Worktrunkに触発されたJujutsuワークスペース切り替えツール | `cli` `jj` `jujitsu` `utility` `workspace` | 8 | 🔄 2026-08-21 |
| [**herdr-e2b-sandbox**](https://github.com/e2b-dev/herdr-e2b-sandbox)<br><sub>e2b-dev</sub> | git worktreeをE2B Sandboxにミラーするherdrプラグイン——単一のboxでも、エージェントごとにブランチを割り当てたフリートでも対応。TUIダッシュボード付き | `cli` `cloud-dev` `e2b` `git-worktree` `sandbox` | 6 | 🔄 2026-08-29 |
| [**herdr-plugin-git-worktree-hooks**](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks)<br><sub>freethinkel</sub> | git worktreeの作成/削除時にシェルコマンドを実行する——どのリポジトリの外にも置ける、全プロジェクト共通の1つのYAML設定 | `git-worktree` `javascript` | 6 | 2026-07-06 |
| [**herdr-worktree-from-pr**](https://github.com/tdi/herdr-worktree-from-pr)<br><sub>tdi</sub> | GitHubのPRからgit worktreeを作成し、herdrのワークスペースとして開く | `javascript` | 6 | 2026-07-20 |
| [**herdr-worktree-seed**](https://github.com/jlimas/herdr-worktree-seed)<br><sub>jlimas</sub> | コピーオンライトのnode_modulesと設定可能なローカルdotfilesを、新しいworktreeに投入するHerdrプラグイン | `developer-tools` `dotfiles` `git-worktree` `nodejs` `typescript` | 5 | 2026-07-28 |
| [**herdr-symlink-worktree**](https://github.com/hmu332233/herdr-symlink-worktree)<br><sub>hmu332233</sub> | メインのリポジトリにある共有ローカルファイルを、新しいworktreeにシンボリックリンクするherdrプラグイン | `shell` | 4 | 2026-07-16 |
| [**herdr-fresh-worktree**](https://github.com/persiyanov/herdr-fresh-worktree)<br><sub>persiyanov</sub> | 新しく作成したherdrのworktreeを、originのデフォルトブランチの最新状態にリセットする | `javascript` | 4 | 2026-06-25 |
| [**herdr-worktreeinclude**](https://github.com/tanshio/herdr-worktreeinclude)<br><sub>tanshio</sub> | Herdrプラグイン：.worktreeincludeにマッチするgit管理外ファイルを、新しく作成されたworktreeにコピーする | `worktree` `worktreeiclude` `shell` | 4 | 2026-07-11 |
| [**herdr-worktree-hooks**](https://github.com/timofey-TK/herdr-worktree-hooks)<br><sub>timofey-TK</sub> | herdrプラグイン：git worktreeの作成・オープン・削除時に、カスタムのセットアップ/後始末コマンドを実行する | `developer-tools` `git-worktree` `worktree` `python` | 4 | 2026-07-17 |
| [**herdr-remote-worktrunk**](https://github.com/ditwrd/herdr-remote-worktrunk)<br><sub>ditwrd</sub> | Herdr向けのリモートworktrunkワークスペース | `shell` | 3 | 2026-07-10 |
| [**herdr-jj**](https://github.com/OliverGilan/herdr-jj)<br><sub>OliverGilan</sub> | HerdrにJujutsuのワークスペースサポートを追加する | `jujutsu` `rust` | 3 | 2026-08-12 |
| [**herdr-branch-cleanup**](https://github.com/osolmaz/herdr-branch-cleanup)<br><sub>osolmaz</sub> | ペインのブランチがGitHub上でマージまたは削除されたら、デフォルトブランチにチェックアウトする | `git` `github` `rust` | 3 | 2026-07-26 |
| [**herdr-worktree-lifecycle**](https://github.com/qdentity/herdr-worktree-lifecycle)<br><sub>qdentity</sub> | Herdrプラグイン：worktreeのライフサイクルイベントを、リポジトリ側が持つセットアップ/後始末用のラッパーに配信する | `rust` | 3 | 2026-06-29 |
| [**herdr-multirepo**](https://github.com/jattento/herdr-multirepo)<br><sub>jattento</sub> | 複数のリポジトリにまたがる1つのフィーチャーブランチを、1つのHerdrワークスペースで扱う | `git-worktree` `python` | 2 | 2026-08-03 |
| [**herdr-shear**](https://github.com/moneycaringcoder/herdr-shear)<br><sub>moneycaringcoder</sub> | 安全に削除できるgit worktreeを見つけて削除する。herdr向けのworktree清掃係 | `cleanup` `git-worktree` `rust` `terminal` | 2 | 🔄 2026-09-01 |
| [**herdr-jj-status**](https://github.com/mroth/herdr-jj-status)<br><sub>mroth</sub> | herdrプラグイン：jjのワークスペースのJujutsuブックマーク/ステータスを、スペースのサイドバーに表示する | `shell` | 2 | 2026-07-28 |
| [**herdr-worktreeinclude**](https://github.com/serhii-chernenko/herdr-worktreeinclude)<br><sub>serhii-chernenko</sub> | 新しいworktreeにカスタムパスを許可し、Claude CLIと同様に`.worktreeinclude`ファイルを尊重する | `worktree` `shell` | 2 | 2026-07-23 |
| [**herdr-worktree-nav**](https://github.com/ShoMasegi/herdr-worktree-nav)<br><sub>ShoMasegi</sub> | _(説明なし)_ | `terminal` `rust` | 2 | 🔄 2026-09-04 |
| [**herdr-corral**](https://github.com/bfreed/herdr-corral)<br><sub>bfreed</sub> | Herdr内でGit worktreeをまとめて管理——envファイル、依存関係、エージェント/シェル/サーバー用のタブ、マージしても安全なクリーンアップに対応。Herdr向けのworkmux代替 | `git-worktree` `workmux` `python` | 1 | 2026-08-14 |
| [**herdr-worktree-copy**](https://github.com/crexi/herdr-worktree-copy)<br><sub>crexi</sub> | .worktree-copyマニフェストに基づき、worktreeローカルファイルをコピー・シンボリックリンクするHerdrプラグイン | `git-worktree` `shell` | 1 | 2026-07-28 |
| [**herdr-deck**](https://github.com/ctbaum/herdr-deck)<br><sub>ctbaum</sub> | herdr-agents.nvimと組み合わせて使うワークスペースランチャー：Neovim・エージェント・シェル・lazygitがあらかじめ用意された「デッキ」で、ClaudeやCodexを開始または再開できる | `claude-code` `codex` `coding-agents` `git-worktree` `neovim` | 1 | 🔄 2026-08-24 |
| [**🆕 herdr-composer**](https://github.com/danieljvdm/herdr-composer)<br><sub>danieljvdm</sub> | タスクを組み立て、コンテキストを添付し、隔離された Herdr ワークスペースでコーディングエージェントを起動できます。 | `coding-agents` `git-worktree` `rust` | 1 | 🔄 2026-09-01 |
| [**trunkr**](https://github.com/disintegrator/trunkr)<br><sub>disintegrator</sub> | Herdr🤝Worktrunk——HerdrとWorktrunkを連携させるプラグイン | `go` | 1 | 2026-08-12 |
| [**herdr-allow**](https://github.com/Feasy01/herdr-allow)<br><sub>Feasy01</sub> | herdrプラグイン：.herdr-allowの許可リストを使って、gitignore対象のファイル（.env、シークレット、ローカル設定）を新しいworktreeすべてにコピーする | `shell` | 1 | 2026-07-02 |
| [**herdr-plugin-gwm**](https://github.com/kbrdn1/herdr-plugin-gwm)<br><sub>kbrdn1</sub> | git worktree管理のためgwmを操作するherdrプラグイン——gwmを唯一の正とし、herdrはそれに追従する | `bash` `cli` `git-worktree` `gwm` `worktree` | 1 | 2026-07-27 |
| [**herdr-collide**](https://github.com/moneycaringcoder/herdr-collide)<br><sub>moneycaringcoder</sub> | 同じリポジトリの異なるgit worktreeで作業しているエージェント同士が衝突しそうなときに警告する——編集が単に重なっているだけか、実際に競合するのかも判定する | `conflict-detection` `git-worktree` `rust` `terminal` | 1 | 🔄 2026-09-01 |
| [**herdr-standup**](https://github.com/moneycaringcoder/herdr-standup)<br><sub>moneycaringcoder</sub> | エージェントが実際に何をしたかのダイジェスト。1つのコマンドで、指定した期間の全Herdrワークスペースについて、コミット・変更量・ブランチ・作業がどこかに着地したかを、読みやすい形でまとめて表示する | `git` `rust` `standup` `terminal` | 1 | 🔄 2026-09-01 |
| [**herdr-plugin-pr-board**](https://github.com/0xthc/herdr-plugin-pr-board)<br><sub>0xthc</sub> | 現在のリポジトリのGitHub PRをherdr内で扱う——ペインで一覧・閲覧し、選んだものをworktreeワークスペースとしてチェックアウトし、マージ済みのものを安全に回収する | `shell` | 0 | 🔄 2026-08-20 |
| [**herdr-plugin-worktree-bootstrap**](https://github.com/0xthc/herdr-plugin-worktree-bootstrap)<br><sub>0xthc</sub> | 新しいherdr worktreeを開いた瞬間に、.envファイルとnode_modulesを投入する | `shell` | 0 | 🔄 2026-08-22 |
| [**herdr**](https://github.com/AgentTeamsRun/herdr)<br><sub>AgentTeamsRun</sub> | herdrのworktreeライフサイクルイベントを、AgentTeamsレジストリに報告する | — | 0 | 2026-08-19 |
| [**herdr-worktree-provisioner**](https://github.com/arjenblokzijl/herdr-worktree-provisioner)<br><sub>arjenblokzijl</sub> | 新しいworktree専用の可視ペインで、リポジトリごとのセットアップを実行する——組み合わせ可能でガード不要 | `bootstrap` `git-worktree` `worktree` `shell` | 0 | 2026-07-08 |
| [**🆕 herdr-plugin-env-sync**](https://github.com/DecampsRenan/herdr-plugin-env-sync)<br><sub>DecampsRenan</sub> | Herdrプラグイン：env-syncは新しいGit worktreeをセットアップする（.envのコピー、リモートブランチの追跡、セットアップコマンドの実行）。ライブなステータスパネル付き | `developer-tools` `git-worktree` `shell` | 0 | 🔄 2026-08-28 |
| [**herdr-worktreeinclude**](https://github.com/eightHundreds/herdr-worktreeinclude)<br><sub>eightHundreds</sub> | Herdrプラグイン：.worktreeincludeで指定したgit管理外ファイルを、新しいworktreeにコピーする | `worktree` `rust` | 0 | 2026-07-28 |
| [**herdr-title**](https://github.com/filoozom/herdr-title)<br><sub>filoozom</sub> | 選択中のworktreeとエージェントの活動状況を、ターミナルのタブタイトルに表示するHerdrプラグイン | `rust` | 0 | 2026-07-24 |
| [**herdr-hub-worktrees**](https://github.com/klukacin/herdr-hub-worktrees)<br><sub>klukacin</sub> | herdrプラグイン：hubのworktreeを、ネストされた各サブリポジトリのクローンにミラーする | `git-worktree` `monorepo` `terminal-multiplexer` `shell` | 0 | 2026-08-12 |
| [**gren-herdr**](https://github.com/langtind/gren-herdr)<br><sub>langtind</sub> | grenを介してgit worktreeを作成・切り替え・削除するherdrプラグイン——grenの作成後セットアップにも対応 | `git-worktree` `gren` `shell` | 0 | 🔄 2026-09-02 |
| [**herdr-worktree-hooks-plugin**](https://github.com/m1sk9/herdr-worktree-hooks-plugin)<br><sub>m1sk9</sub> | Herdrのworktreeに、カスタマイズ可能なフックを追加するプラグイン | `rust` | 0 | 🔄 2026-09-01 |
| [**🆕 herdr-worktree-include**](https://github.com/scoussens-nthplusio/herdr-worktree-include)<br><sub>scoussens-nthplusio</sub> | リポジトリの.worktreeincludeを使って、.envなどgit管理外のファイルを新しいHerdr worktreeにコピーする——Claude Codeが使うのと同じファイル・同じルール | `dotenv` `git-worktree` `shell` | 0 | 🔄 2026-08-27 |
| [**herdr-jira-worktree**](https://github.com/spiritsack/herdr-jira-worktree)<br><sub>spiritsack</sub> | herdrプラグイン：Jiraチケットの入力を求め、対応するgit worktreeを開く/再利用し、新しいClaude Codeセッションに事前入力する | `shell` | 0 | 🔄 2026-08-24 |
| [**🆕 herdr-worktree-guard**](https://github.com/takeaship/herdr-worktree-guard)<br><sub>takeaship</sub> | エージェントのworktreeを追跡・清掃する、安全性重視のHerdrプラグイン | `coding-agents` `git-worktree` | 0 | 🔄 2026-08-30 |
| [**herdr-worktree**](https://github.com/tjg184/herdr-worktree)<br><sub>tjg184</sub> | worktrunkとネイティブのworktreeの両方に対応するHerdr worktreeプラグイン | `rust` | 0 | 2026-08-13 |
| [**herdr-coder-sessions**](https://github.com/ubuntudroid/herdr-coder-sessions)<br><sub>ubuntudroid</sub> | herdrで実行中のCoderエージェントセッションを閲覧し、それぞれを専用のワークスペースとして開く——セッションにagenttyで接続し、その変更をレビュー用にローカルのworktreeへミラーする | `agentapi` `coder` `coding-agents` `python` | 0 | 🔄 2026-09-02 |
| [**🆕 herdr-git-stack**](https://github.com/ubuntudroid/herdr-git-stack)<br><sub>ubuntudroid</sub> | herdrプラグイン：各spaceのgitブランチスタック内での位置をspacesサイドバーに表示し、親ブランチが移動したブランチにフラグを立て、スタックを連続した状態に保つ。ローカルのコミットグラフのみを使用——ネットワーク・forge API・スタッキングツール不要 | `bash` `developer-tools` `git` `stacked-branches` `shell` | 0 | 🔄 2026-09-03 |
| [**herdr-plugin-worktree-bootstrap**](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap)<br><sub>zerodice0</sub> | 新しいHerdrのGit worktreeに、無視されているローカルファイルを安全にコピーし、セットアップコマンドを実行する | `python` | 0 | 2026-08-03 |

<details><summary>この目的にも関係するもの</summary>

- [tdi/herdr-worktree-from-linear](https://github.com/tdi/herdr-worktree-from-linear) — Linearのissueからgit worktreeを作成し、herdrのワークスペースとして開く
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — JavaScript/TypeScript向けにHerdrのworktreeを自動でブートストラップ——ロックファイルを考慮したインストールと、安全な環境ファイルの復元に対応
- [tomasvarga/herdr-e2b](https://github.com/tomasvarga/herdr-e2b) — 必要なときにgit worktreeを新しいE2Bクラウドサンドボックスへミラーする——未コミットの変更も含めたスナップショットをアップロードするだけで、pushやcloneは不要なherdrプラグイン
- [JLighter/herdr-spawn](https://github.com/JLighter/herdr-spawn) — herdrプラグイン：プロンプトを渡してコーディングエージェントを起動——エージェントごとに専用のgit worktreeを割り当てる
- [jtnovellis/herdr-worktree-setup](https://github.com/jtnovellis/herdr-worktree-setup) — herdrプラグイン：新しいgit worktreeをすぐに使える状態にする——.envと開発状態のコピー、依存関係キャッシュのクローン（APFS/reflink）、mise trust、direnv allow、依存…
- [snics/herdr-worktree-from-gitlab](https://github.com/snics/herdr-worktree-from-gitlab) — herdrプラグイン：GitLabのissueから（glab経由で）git worktreeとワークスペースを作成する
- [untalfranfernandez/herdr-worktreeinclude](https://github.com/untalfranfernandez/herdr-worktreeinclude) — 新しいgit worktreeに必要なgitignore対象のローカルファイル（.env、settings.local.json、フィクスチャなど）を自動配置するHerdrプラグイン。.worktreeincludeフ…

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-review"></a>

## コードレビュー・差分確認

> エージェントが書いた差分を読んで、コメントを返したい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**crabbox**](https://github.com/openclaw/crabbox)<br><sub>openclaw</sub> | Crabbox：サンドボックスを温め、差分を同期し、テストスイートを実行する | `agent-skills` `remote-test-runner` `go` | 1363 | 🔄 2026-09-04 |
| [**herdr-reviewr**](https://github.com/persiyanov/herdr-reviewr)<br><sub>persiyanov</sub> | herdr向けのコードレビュー＋ファイルビューアのサイドバー。エージェントの差分にコメントして差し戻せる。PRとそのチェック・コメントの読み取り専用表示も付属 | `code-review` `rust` `tui` | 594 | 🔄 2026-08-29 |
| [**herdr-annotate**](https://github.com/plannotator/herdr-annotate)<br><sub>plannotator</sub> | Herdrでターミナルのテキスト・ドキュメント・エージェントの返答に注釈を付けてレビューし、そのフィードバックをそのままエージェントに送り返す | `annotation` `multiplexer` `rust` | 347 | 🔄 2026-08-31 |
| [**herdr-hunk-diff**](https://github.com/jhochenbaum/herdr-hunk-diff)<br><sub>jhochenbaum</sub> | herdrからHunkでエージェントが書いた変更をレビューし、インラインコメントを担当エージェントに送り返す | `code-review` `hunk` `typescript` | 104 | 🔄 2026-09-02 |
| [**herdr-plannotator**](https://github.com/plannotator/herdr-plannotator)<br><sub>plannotator</sub> | HerdrのBrowserペイン内でPlannotatorのレビューを開くプラグイン | `plannotator` `typescript` | 22 | 2026-07-29 |
| [**herdr-pickr**](https://github.com/tomasvarga/herdr-pickr)<br><sub>tomasvarga</sub> | herdr向けのPRレビュールーター——GitHubのPRやGitLabのMRリンクをCtrl+クリックしてレビュアー（tuicr・hunk・diff・ブラウザ・または独自ツール）を選択、AIによる一次レビューもオプションで利用可能 | `cli` `code-review` `pull-request` `tui` `shell` | 16 | 2026-07-13 |
| [**herdr-plugin-hunk**](https://github.com/edmundmiller/herdr-plugin-hunk)<br><sub>edmundmiller</sub> | Hunkの差分をスプリットペインやタブで開くHerdrプラグイン | `python` | 15 | 2026-06-23 |
| [**herdr-gitview**](https://github.com/ChmaraX/herdr-gitview)<br><sub>ChmaraX</sub> | herdr向けのGitステータス/差分パネル——変更のレビュー、nvimでの編集、ステージ/コミット/破棄をすべてターミナルから行える | `git` `git-diff` `git-tui` `neovim` `rust` | 9 | 🔄 2026-09-02 |
| [**herdr-plugin-hunk-autodiff**](https://github.com/scott306lr/herdr-plugin-hunk-autodiff)<br><sub>scott306lr</sub> | Herdrプラグイン：コーディングエージェントが未コミットの変更を残して完了したら、hunkの差分スプリットを自動で開く | `claude-code` `hunk` `python` | 5 | 2026-07-05 |
| [**herdr-extensions**](https://github.com/vonzelle-vzt/herdr-extensions)<br><sub>vonzelle-vzt</sub> | herdr向けの小さなVS Code——LSPによる診断・自動補完・リネーム・定義へジャンプに対応した本格エディタに加え、ソース管理・検索・問題一覧・テスト・デバッガ・アプリのライブプレビュー・実行時エラー捕捉・画像貼り付け・エージェント差分レビューまで搭載。12パネル構成、コマンド1つで冪等かつ元に戻せる導入 | `agent-tools` `autocomplete` `claude-code` `cli` `code-review` | 5 | 2026-08-03 |
| [**herdr-progressive-reviewer**](https://github.com/flupke/herdr-progressive-reviewer)<br><sub>flupke</sub> | Tidewaveに着想を得た、ターン制の差分レビューア | `rust` | 3 | 🔄 2026-09-02 |
| [**herdr-review.nvim**](https://github.com/inferst/herdr-review.nvim)<br><sub>inferst</sub> | GitとherdrをNeovimに統合したコードレビュー用UI | `lua` | 3 | 2026-08-01 |
| [**herdr-review**](https://github.com/quantk/herdr-review)<br><sub>quantk</sub> | エージェントが書いた変更をHunkでレビューし、インラインのフィードバックをHerdr経由で送り返す | `code-review` `hunk` `javascript` | 3 | 2026-07-28 |
| [**easy-review**](https://github.com/VilfredSikker/easy-review)<br><sub>VilfredSikker</sub> | AI支援によるコーディング向けのGit差分レビュー。ターミナルTUIとTauriデスクトップアプリの両方に対応 | `ai-code-review` `cli` `code-review` `desktop-app` `developer-tools` | 3 | 🔄 2026-09-03 |
| [**herdr-pr-tracker**](https://github.com/jakekroon/herdr-pr-tracker)<br><sub>jakekroon</sub> | あなたが作成したオープン中のプルリクエストをすべて、対応が必要な度合いで色分けしてドッキング表示する。Herdrプラグイン | `bun` `code-review` `developer-tools` `github` `pull-requests` | 2 | 🔄 2026-08-28 |
| [**herdr-scribe**](https://github.com/Javamomma/herdr-scribe)<br><sub>Javamomma</sub> | herdrプラグイン：録音せずにライブで会議を文字起こし——マイク入力をRAM上のみのトランスクリプトとライブ分析用ペインに変換。停止時には議事録・任意のポリシーゲート・レビュー可能な自動ドラフトを生成。Linux/WSL2およびmacOS対応 | `macos` `meeting-notes` `privacy` `speech-to-text` `terminal` | 2 | 2026-08-07 |
| [**herdr-comments**](https://github.com/shadowfax92/herdr-comments)<br><sub>shadowfax92</sub> | コピーしたHerdrのターミナル出力に注釈を付け、ペインごとのコメントを収集してNeovimでレビューできる | `ai-agents` `annotations` `neovim` `rust` `terminal` | 2 | 2026-08-19 |
| [**herdr-hunk**](https://github.com/yuucu/herdr-hunk)<br><sub>yuucu</sub> | herdrプラグイン：エージェントのワークスペースでHunkの差分レビューをトグルする | `diff` `hunk` `go` | 2 | 2026-07-20 |
| [**herdr-strays**](https://github.com/aleslanger/herdr-strays)<br><sub>aleslanger</sub> | 野良git worktreeを取りまとめるターミナルUI——プロジェクトを一覧し、変更ファイルをリアルタイム表示、差分を読み、パネルを離れずにClaudeへプロンプトを送れる | `rust` | 1 | 2026-08-12 |
| [**roboherd**](https://github.com/andschneider/roboherd)<br><sub>andschneider</sub> | herdrのワークスペース内で、roborevのレビュー状態とアクションを扱う | `rust` `tui` | 1 | 🔄 2026-08-25 |
| [**herdr-agent-diff**](https://github.com/baotran01/herdr-agent-diff)<br><sub>baotran01</sub> | エージェントのファイルシステムとGit差分を確認するHerdrプラグイン | `rust` | 1 | 2026-08-03 |
| [**herdr-stagr**](https://github.com/brianh20/herdr-stagr)<br><sub>brianh20</sub> | herdr向けのソース管理サイドバー——並列差分表示でステージ・アンステージ・破棄ができる | `git` `tui` `rust` | 1 | 2026-08-06 |
| [**🆕 Vincent**](https://github.com/chasereyn/Vincent)<br><sub>chasereyn</sub> | AI エージェントが書いたコードをレビューし、その場で修正できる、マウス操作を主体としたターミナルクライアントです。 | `go` | 1 | 🔄 2026-09-03 |
| [**herdr-peer-review**](https://github.com/Elio2000/herdr-peer-review)<br><sub>Elio2000</sub> | herdrのペインで2つ目のコーディングエージェントを開き、差分をレビューさせる——監視可能・自動承認・読み取り専用。レビュー↔修正↔判断の自律ループ用のClaude Codeスキルも同梱 | `agent-skills` `ai-agents` `claude-code` `code-review` `codex` | 1 | 2026-07-16 |
| [**herdr-tasks**](https://github.com/husniadil/herdr-tasks)<br><sub>husniadil</sub> | Herdr上のコーディングエージェント向けのタスクバックログ＋メモボード——リース付きのclaim、証跡に基づくレビュー、人間による決定ゲートを、1つのGoバイナリで実現 | `ai-agents` `mcp-server` `notes` `sqlite` `task-management` | 1 | 🔄 2026-08-30 |
| [**herdr-git-graph**](https://github.com/jorge-huxley/herdr-git-graph)<br><sub>jorge-huxley</sub> | Herdr向けの読み取り専用gitグラフTUIプラグイン——色付きASCIIレーン、ブランチフィルタ、検索、必要に応じた差分表示に対応 | `rust` | 1 | 2026-07-17 |
| [**agentflock**](https://github.com/neospark-sol/agentflock)<br><sub>neospark-sol</sub> | AIが調整するビルダー役とレビュアー役のグループを、永続的なマイルストーン管理とともに提供する | `ai-agents` `pair-programming` `typescript` | 1 | 🔄 2026-08-21 |
| [**herdr-hunk-viewer**](https://github.com/tareqmlx/herdr-hunk-viewer)<br><sub>tareqmlx</sub> | _(説明なし)_ | `code-review` `hunk` `rust` | 1 | 🔄 2026-08-21 |
| [**herdr-lazygit-viewer**](https://github.com/tareqmlx/herdr-lazygit-viewer)<br><sub>tareqmlx</sub> | その時々に適したHerdrの表示面で、files・branches・commits・stashのいずれかのパネルを開いた状態でlazygitを起動する | `code-review` `lazygit` `rust` | 1 | 2026-08-14 |
| [**herdr-hunk-gh-diff**](https://github.com/Allianaab2m/herdr-hunk-gh-diff)<br><sub>Allianaab2m</sub> | Herdrプラグイン：現在のペインでチェックアウトしているブランチと、そのGitHubプルリクエストのターゲットブランチとの間でHunkの差分を開く | `python` | 0 | 2026-07-15 |
| [**herdr-hunk**](https://github.com/cevr/herdr-hunk)<br><sub>cevr</sub> | Hunkのレビューコメントを、対応するHerdrエージェントペインに送る | `effect-ts` `hunk` `typescript` | 0 | 2026-07-28 |
| [**herdr-hunk**](https://github.com/goofansu/herdr-hunk)<br><sub>goofansu</sub> | 一時的なHunkオーバーレイを開く、素早いHerdrレビューアクションを提供する。Hunkを終了するとオーバーレイが閉じ、ワークスペースが元に戻る | `python` | 0 | 🔄 2026-08-25 |
| [**herdr-implement-review**](https://github.com/Idan-Levin/herdr-implement-review)<br><sub>Idan-Levin</sub> | Codexによる実装・セキュリティスキャン・親エージェントによるレビューを行うHerdrワークフロー | `claude-code` `codex` `security-review` `shell` | 0 | 2026-08-10 |
| [**herdr-plan-code-review**](https://github.com/inxx/herdr-plan-code-review)<br><sub>inxx</sub> | herdrプラグイン：Opusが計画し、Sonnetがコーディングし、Claude+Codexがレビューする——1つの操作で4つのエージェントペインを開く | `claude-code` `codex` `terminal` `shell` | 0 | 2026-07-06 |
| [**herdr-idle-panes**](https://github.com/leonho/herdr-idle-panes)<br><sub>leonho</sub> | herdrプラグイン：アイドル状態のシェルのままになっているペインを確認して閉じる、チェックリスト形式のポップアップ | `python` | 0 | 🔄 2026-08-22 |
| [**herdr-roborev**](https://github.com/phin-tech/herdr-roborev)<br><sub>phin-tech</sub> | roborevのレビューTUIをHerdrのペインで開く | `shell` | 0 | 2026-07-21 |
| [**herdr-diff-review.nvim**](https://github.com/rytkmt/herdr-diff-review.nvim)<br><sub>rytkmt</sub> | AIエージェントによるファイル変更を、適用前にNeovimのdiffモードでレビューする——Claude CodeやKiro CLIからの編集を、1つのコマンドで承認/拒否できる | `kiro-cli` `neovim` `neovim-plugin` `neovim-plugins` `nvim` | 0 | 2026-08-18 |
| [**🆕 lasso**](https://github.com/skellleks/lasso)<br><sub>skellleks</sub> | herdr 用のレビューペイン。エージェントごとの差分をシンタックスハイライト付きで表示し、インラインコメントをエージェントへ送り返せます。 | `ai-agents` `claude-code` `code-review` `git-diff` `ratatui` | 0 | 🔄 2026-08-31 |
| [**herdr-code-review**](https://github.com/txmed82/herdr-code-review)<br><sub>txmed82</sub> | 構造化されたAIコードレビューを行うHerdrプラグイン | `code-review` `javascript` | 0 | 2026-08-19 |

<details><summary>この目的にも関係するもの</summary>

- [powerfooI/herdr-studio](https://github.com/powerfooI/herdr-studio) — Herdr 用の Web クライアント。モバイル体験を第一に考え、ブラウザ上のターミナル、ワークスペースと worktree の管理、ファイル・差分ビューア、AI エージェントのセッション確認までを提供します。
- [anhnd3005-infinity/herdr-worker-orchestrator](https://github.com/anhnd3005-infinity/herdr-worker-orchestrator) — Herdr管理下のペイン経由で、CLIエージェントワーカー（agy・codexなど）にタスクを割り振る——状態を持つタスク追跡、worktreeによる隔離、差分ベースのレビューに対応。Claude CodeとHerdr…
- [elKei24/herdr-co-review](https://github.com/elKei24/herdr-co-review) — herdrでの分割画面PRレビュー——エージェントが問題を見つけ、あなたはTUIでコードの隣に並べて1件ずつ判断し、承認したものをエージェントが投稿する
- [itisbryan/herdr-gh-checks](https://github.com/itisbryan/herdr-gh-checks) — herdrプラグイン：現在のPRのCIをペインで監視・確認し、CI/マージ状態をサイドバーの行に表示する。Go + Bubble Tea製
- [JacquesvanWyk/herdr-hunk](https://github.com/JacquesvanWyk/herdr-hunk) — herdr向けの、Hunkの差分をfzfで対話的に選ぶピッカー：コミット・範囲・stashに対応し、エージェント完了時に自動オープンもできる
- [mikhail-angelov/herdr-review-loop](https://github.com/mikhail-angelov/herdr-review-loop) — herdrのワークスペース内でエージェント同士が自動的に相互レビューする——1体が書き、もう1体がレビューし、これを繰り返す
- [tomasvarga/herdr-sniffr](https://github.com/tomasvarga/herdr-sniffr) — レビューする前に、AIがPRの問題を検知する——エージェントによる一次チェックでtuicrにドラフトコメントを残す。特定のエージェントに依存しない（codex/claude/cursor/grok/…）
- [moneycaringcoder/herdr-collide](https://github.com/moneycaringcoder/herdr-collide) — 同じリポジトリの異なるgit worktreeで作業しているエージェント同士が衝突しそうなときに警告する——編集が単に重なっているだけか、実際に競合するのかも判定する
- [neospeed83/herdr-tournament](https://github.com/neospeed83/herdr-tournament) — Herdr向けの、対抗的なマルチエージェントコードレビュー
- [krzysztoff1/herdr-cull](https://github.com/krzysztoff1/herdr-cull) — herdr内のアイドル状態のエージェントペインを確認して閉じる——fzfによる複数選択、確認なしで閉じることはない
- [ubuntudroid/herdr-coder-sessions](https://github.com/ubuntudroid/herdr-coder-sessions) — herdrで実行中のCoderエージェントセッションを閲覧し、それぞれを専用のワークスペースとして開く——セッションにagenttyで接続し、その変更をレビュー用にローカルのworktreeへミラーする

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-forge"></a>

## GitHub / issue トラッカー連携

> issue や PR を起点に作業を始めたい / PR の状態を追いたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**ghzinga**](https://github.com/osolmaz/ghzinga)<br><sub>osolmaz</sub> | 1つのGitHub issueやPRをクリックだけで見られる、Rust製の簡単なTUI | `rust` | 83 | 2026-07-26 |
| [**herdr-plugin-gh-pr**](https://github.com/wyattjoh/herdr-plugin-gh-pr)<br><sub>wyattjoh</sub> | フォーカス中のエージェントペインのブランチに対応するGitHub PRの状態をサイドバーに表示するherdrプラグイン | `typescript` | 20 | 2026-07-16 |
| [**herdr-plugin-github-start**](https://github.com/ogulcancelik/herdr-plugin-github-start)<br><sub>ogulcancelik</sub> | GitHub issue・PR・ディスカッションからCodexやClaudeを起動するHerdrプラグイン | `javascript` | 17 | 🔄 2026-08-31 |
| [**herdr-worktree-from-linear**](https://github.com/tdi/herdr-worktree-from-linear)<br><sub>tdi</sub> | Linearのissueからgit worktreeを作成し、herdrのワークスペースとして開く | `javascript` | 14 | 🔄 2026-09-02 |
| [**herdr-jira**](https://github.com/a2u/herdr-jira)<br><sub>a2u</sub> | herdr向けのJira TUIプラグイン——設定可能なJQLフィルタでissueを閲覧・検索・ステータス変更し、1キーでターミナル上のAIエージェントにissueを委任できる | `ai-agents` `jira` `ratatui` `rust` `tui` | 12 | 2026-07-18 |
| [**herdr-pr-tracker**](https://github.com/Matovidlo/herdr-pr-tracker)<br><sub>Matovidlo</sub> | herdrプラグイン：各Claude Codeセッションが作成するGitHub PRを、gh状態とアクション付きで追跡する | `claude-code` `shell` | 12 | 2026-08-12 |
| [**herdr-linear**](https://github.com/JacquesvanWyk/herdr-linear)<br><sub>JacquesvanWyk</sub> | herdrのスプリットペインまたはタブ内で動くfzf駆動のLinearパネル：issue検索、プロジェクトの深掘り、issue作成、ステータス変更ができる | `shell` | 8 | 2026-07-12 |
| [**herdr-git-status**](https://github.com/krystof018/herdr-git-status)<br><sub>krystof018</sub> | herdr内にCIの状態を表示する——GitLab（パイプライン＋マージリクエスト）とGitHub（Actions＋プルリクエスト）の両方に対応し、リポジトリのoriginから自動検出する | `bash` `ci-cd` `ci-status` `developer-tools` `github-actions` | 5 | 2026-07-01 |
| [**herdr-plugin-github-dash**](https://github.com/kukv/herdr-plugin-github-dash)<br><sub>kukv</sub> | GitHubのプルリクエストとissueを閲覧・管理するHerdrプラグイン | `cli` `github` `go` | 4 | 🔄 2026-09-03 |
| [**herdr-linear**](https://github.com/talent-factory/herdr-linear)<br><sub>talent-factory</sub> | Herdr向けのLinear issueパネル。Enterキーで実装に着手できる | `rust` | 4 | 🔄 2026-08-21 |
| [**herdr-pr-board**](https://github.com/cdowell09/herdr-pr-board)<br><sub>cdowell09</sub> | 複数リポジトリを横断できる、設定可能なHerdr向けGitHubプルリクエストダッシュボード | `github` `tui` `go` | 3 | 🔄 2026-09-02 |
| [**herdr-co-review**](https://github.com/elKei24/herdr-co-review)<br><sub>elKei24</sub> | herdrでの分割画面PRレビュー——エージェントが問題を見つけ、あなたはTUIでコードの隣に並べて1件ずつ判断し、承認したものをエージェントが投稿する | `cli` `code-review` `pull-request` `rust` `tui` | 3 | 🔄 2026-09-02 |
| [**herdr-gh-checks**](https://github.com/itisbryan/herdr-gh-checks)<br><sub>itisbryan</sub> | herdrプラグイン：現在のPRのCIをペインで監視・確認し、CI/マージ状態をサイドバーの行に表示する。Go + Bubble Tea製 | `bubbletea` `ci` `github-actions` `tui` `go` | 3 | 🔄 2026-08-25 |
| [**mergr**](https://github.com/jsmenzies/mergr)<br><sub>jsmenzies</sub> | Herdr Spaceのサイドバー行にGitHubプルリクエストの状態を表示する | `github-pull-requests` `rust` | 3 | 2026-07-30 |
| [**herdr-plugin-gh-workflow**](https://github.com/kkckkc/herdr-plugin-gh-workflow)<br><sub>kkckkc</sub> | GitHubワークフロー向けのHerdrプラグイン | `javascript` | 3 | 2026-07-03 |
| [**herdr-beads**](https://github.com/hexsprite/herdr-beads)<br><sub>hexsprite</sub> | HerdrでbeadsのissueIDをCtrl+クリックすると、詳細をスプリットペインで開く | `beads` `issue-tracker` `terminal` `shell` | 2 | 2026-08-07 |
| [**herdr-sniffr**](https://github.com/tomasvarga/herdr-sniffr)<br><sub>tomasvarga</sub> | レビューする前に、AIがPRの問題を検知する——エージェントによる一次チェックでtuicrにドラフトコメントを残す。特定のエージェントに依存しない（codex/claude/cursor/grok/…） | `ai` `cli` `code-review` `pull-request` `tuicr` | 2 | 2026-07-14 |
| [**🆕 herdr-workspace-prs**](https://github.com/andrewbrannan/herdr-workspace-prs)<br><sub>andrewbrannan</sub> | ワークスペースの GitHub プルリクエストを追跡する Herdr プラグインです。 | `typescript` | 1 | 🔄 2026-09-04 |
| [**herdr-board**](https://github.com/bredebjorhovd/herdr-board)<br><sub>bredebjorhovd</sub> | コーディングエージェントが列に並び、自分の仕事を自律的にこなす場所——GitHub issueを入力に、herdrのペインで自律エージェントが動き、書いた本人にPRレビューが返ってくる | `rust` | 1 | 2026-08-14 |
| [**herdr-dashboard**](https://github.com/chouxcreams/herdr-dashboard)<br><sub>chouxcreams</sub> | herdrのワークスペース向けのPRステータスダッシュボードTUI——ペインごとのPRの状態・CI・レビューを一目で確認できる | `dashboard` `github` `pull-requests` `ratatui` `rust` | 1 | 2026-07-28 |
| [**herdr-plugin-dotfiles-github-link-preview**](https://github.com/edmundmiller/herdr-plugin-dotfiles-github-link-preview)<br><sub>edmundmiller</sub> | GitHubのissueやプルリクエストをサイドペインでプレビューするHerdrプラグイン | `python` | 1 | 2026-06-23 |
| [**worktender**](https://github.com/steig/worktender)<br><sub>steig</sub> | GitHubのissueから、専用worktreeで作業するコーディングエージェントまでを1コマンドでつなぐ | `ai-agents` `claude-code` `coding-agents` `git-worktree` `golang` | 1 | 🔄 2026-08-26 |
| [**herdr-github-pr**](https://github.com/woshahua/herdr-github-pr)<br><sub>woshahua</sub> | GitHubのPRの状態・チェック・レビュー・コメントを同期するHerdrプラグイン | `github` `javascript` | 1 | 🔄 2026-08-21 |
| [**herdr-pr**](https://github.com/yelsed/herdr-pr)<br><sub>yelsed</sub> | 対応待ちのプルリクエストを、herdrのペイン内でTodoとして表示する。すべてgh CLI経由で読み取る | `rust` | 1 | 🔄 2026-08-29 |
| [**herdr-plugin-jira-pr**](https://github.com/abtris/herdr-plugin-jira-pr)<br><sub>abtris</sub> | herdrプラグイン：現在のブランチのPRに紐づくJira issueを表示し、内容が食い違っていれば警告する | `github-pr` `jira` `shell` | 0 | 2026-08-04 |
| [**git-shepherd**](https://github.com/H3xept/git-shepherd)<br><sub>H3xept</sub> | 各Herdr Spaceの隣に、プルリクエストの状態（下書き/オープン/マージ済み/クローズ）をアイコンで表示する | `developer-tools` `github-cli` `tui` `javascript` | 0 | 🔄 2026-08-21 |
| [**herdr-spaces-pr-status**](https://github.com/jmarbutt/herdr-spaces-pr-status)<br><sub>jmarbutt</sub> | Conductor風のPRボードで、herdrのスペースにGitHubプルリクエストの状態を表示する | `github-pull-request` `javascript` | 0 | 2026-08-01 |
| [**herdr-pr-preview**](https://github.com/juninaba/herdr-pr-preview)<br><sub>juninaba</sub> | 現在のブランチのGitHubプルリクエストを、スプリットペインでプレビューするHerdrプラグイン | `shell` | 0 | 2026-07-08 |
| [**github-issue-herdr-plugin**](https://github.com/nyanyaon/github-issue-herdr-plugin)<br><sub>nyanyaon</sub> | GitHubのissueを「herd（統率）」するためのClaude Codeプラグイン | `rust` | 0 | 2026-07-27 |
| [**🆕 herdr-gh-issue-label**](https://github.com/polidog/herdr-gh-issue-label)<br><sub>polidog</sub> | ブランチに対応する GitHub issue の番号とタイトルを Herdr のスペースに表示するプラグイン | `github-issues` `shell` | 0 | 🔄 2026-08-28 |
| [**herdr-pr-tab-renamer**](https://github.com/ralphilius/herdr-pr-tab-renamer)<br><sub>ralphilius</sub> | 検出したプルリクエスト番号でタブ名を変更するHerdrプラグイン | `javascript` | 0 | 2026-08-03 |
| [**herdr-worktree-from-gitlab**](https://github.com/snics/herdr-worktree-from-gitlab)<br><sub>snics</sub> | herdrプラグイン：GitLabのissueから（glab経由で）git worktreeとワークスペースを作成する | `gitlab` `rust` `worktree` | 0 | 2026-07-09 |
| [**herdr-pr-workflow**](https://github.com/tamdogood/herdr-pr-workflow)<br><sub>tamdogood</sub> | フォーカス中のエージェントに、現在のブランチのプルリクエストを安全に作成またはマージするよう指示するHerdrアクション | `javascript` | 0 | 2026-08-10 |

<details><summary>この目的にも関係するもの</summary>

- [tomasvarga/herdr-pickr](https://github.com/tomasvarga/herdr-pickr) — herdr向けのPRレビュールーター——GitHubのPRやGitLabのMRリンクをCtrl+クリックしてレビュアー（tuicr・hunk・diff・ブラウザ・または独自ツール）を選択、AIによる一次レビューもオプシ…
- [tdi/herdr-worktree-from-pr](https://github.com/tdi/herdr-worktree-from-pr) — GitHubのPRからgit worktreeを作成し、herdrのワークスペースとして開く
- [jakekroon/herdr-pr-tracker](https://github.com/jakekroon/herdr-pr-tracker) — あなたが作成したオープン中のプルリクエストをすべて、対応が必要な度合いで色分けしてドッキング表示する。Herdrプラグイン
- [kiitosu/herdr-jira-board](https://github.com/kiitosu/herdr-jira-board) — herdr内で動くJiraカンバンボード。Claude Codeセッションランチャー付き
- [ukwhatn/taskherd](https://github.com/ukwhatn/taskherd) — herdrのエージェントセッション・PR・Jiraチケットに連携したタスクボード
- [0xthc/herdr-plugin-pr-board](https://github.com/0xthc/herdr-plugin-pr-board) — 現在のリポジトリのGitHub PRをherdr内で扱う——ペインで一覧・閲覧し、選んだものをworktreeワークスペースとしてチェックアウトし、マージ済みのものを安全に回収する
- [spiritsack/herdr-jira-worktree](https://github.com/spiritsack/herdr-jira-worktree) — herdrプラグイン：Jiraチケットの入力を求め、対応するgit worktreeを開く/再利用し、新しいClaude Codeセッションに事前入力する

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-layout"></a>

## ワークスペース・レイアウト構築

> プロジェクトを開いたら、タブ・ペイン・起動コマンドまで一発で整えたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-spreader**](https://github.com/yuk1ty/herdr-spreader)<br><sub>yuk1ty</sub> | 1つのYAMLファイルから、herdrのワークスペースレイアウト全体（タブ・ペイン・起動コマンドなど）を一括で立ち上げる | `rust` | 97 | 2026-08-16 |
| [**dotfiles**](https://github.com/lararosekelley/dotfiles)<br><sub>lararosekelley</sub> | Bashシェルでの使用を想定した個人用dotfiles | `bash` `bootstrap` `dotfiles` `homebrew` `macos` | 51 | 🔄 2026-08-31 |
| [**herdr-plugin-workspace-manager**](https://github.com/razajamil/herdr-plugin-workspace-manager)<br><sub>razajamil</sub> | worktree作成時にワークスペースごとのデフォルト設定を自動適用する、宣言的なタブ/ペインレイアウト | `rust` | 38 | 🔄 2026-08-23 |
| [**seshagy**](https://github.com/lmilojevicc/seshagy)<br><sub>lmilojevicc</sub> | tmuxとherdr向けのエージェント対応セッションマネージャー——プロジェクトを検出し、セッションを起動し、AIエージェントの作業を追跡する | `bubbletea` `go` `session-management` `session-manager` `terminal` | 16 | 🔄 2026-08-20 |
| [**🆕 herdr-grid**](https://github.com/thuanlm215/herdr-grid)<br><sub>thuanlm215</sub> | ドラッグ＆ドロップ・新規シェル起動・均等な分割・固定プリセット・安全なワークスペース作成に対応した、Herdr向けのビジュアルペインレイアウトエディタ | `layout-presets` `pane-layout` `productivity` `ratatui` `rust` | 6 | 🔄 2026-09-01 |
| [**herdr-warp**](https://github.com/HexSleeves/herdr-warp)<br><sub>HexSleeves</sub> | Herdrのワークスペースを、ネイティブのWarpペインとして開く | `shell` | 4 | 2026-07-25 |
| [**herdr-muster**](https://github.com/marcoskichel/herdr-muster)<br><sub>marcoskichel</sub> | エージェントの状態を認識するherdr向けプロジェクト切り替えツール | `rust` | 4 | 2026-07-03 |
| [**herdr-layout-tools**](https://github.com/edouard-andrei/herdr-layout-tools)<br><sub>edouard-andrei</sub> | herdrプラグイン：レイアウトをその場で変形（main-left＋グリッド）したり均等化したりする——タブIDやペインIDは変わらず、プロセスも維持される | `javascript` | 3 | 2026-08-06 |
| [**herdr-pane-layouts**](https://github.com/iurysza/herdr-pane-layouts)<br><sub>iurysza</sub> | Herdr向けの、tmux風のシームレスなペインリサイズとレイアウト | `pane-layout` `python` `terminal` | 3 | 2026-07-17 |
| [**herdr-setup-bootstrap**](https://github.com/shizlie/herdr-setup-bootstrap)<br><sub>shizlie</sub> | worktree_init.tomlから新しいworktreeをブートストラップするHerdrプラグイン | `shell` | 3 | 2026-06-17 |
| [**dsh-plugin-herdr**](https://github.com/sunny0826/dsh-plugin-herdr)<br><sub>sunny0826</sub> | DeepSeek Harness（DSH）向けのHerdrコントロールプレーンプラグイン——AIコーディングエージェント向けのターミナルワークスペースマネージャーであるHerdrを、DSHセッションから監視・操作する | `dsh-plugin` `typescript` | 3 | 🔄 2026-08-25 |
| [**herdr-google-gmail**](https://github.com/Tomatio13/herdr-google-gmail)<br><sub>Tomatio13</sub> | herdr-google-gmailは、ターミナルワークスペースツールherdr向けのGmail連携プラグイン | `shell` | 3 | 2026-07-22 |
| [**herdr-clone-layout**](https://github.com/danilolucasmd/herdr-clone-layout)<br><sub>danilolucasmd</sub> | 現在のワークスペースレイアウトを、新しいherdrのworktreeすべてに複製する。テンプレートも設定も不要——今いるレイアウトそのものがテンプレートになる | `shell` | 2 | 🔄 2026-08-27 |
| [**herdr-fork-from-message**](https://github.com/dmangla3/herdr-fork-from-message)<br><sub>dmangla3</sub> | 以前のメッセージの時点からCodexやClaude Codeをフォークし、新しいHerdrのタブ・ペイン・ワークスペースとして開く | `claude-code` `codex` `developer-tools` `terminal-multiplexer` `python` | 2 | 2026-08-10 |
| [**herdr-compose**](https://github.com/ropali/herdr-compose)<br><sub>ropali</sub> | herdr-composeは、Herdr向けの宣言的なワークスペースレイアウトマネージャー | `layout-manager` `python` | 2 | 2026-07-25 |
| [**herdr-google-calendar**](https://github.com/Tomatio13/herdr-google-calendar)<br><sub>Tomatio13</sub> | herdr-gog-calendarは、ターミナルワークスペースツールherdr向けのGoogleカレンダー連携プラグイン | `shell` | 2 | 2026-07-22 |
| [**herdr-layout**](https://github.com/3mmdrew/herdr-layout)<br><sub>3mmdrew</sub> | herdr向けのミニマルなワークスペースレイアウト定義——Luaファイルを渡すだけでワークスペースが立ち上がる。依存なし、デーモンなし、YAMLなし | `lua` `terminal` | 1 | 2026-08-04 |
| [**herdr-dwm-layout**](https://github.com/42lizard/herdr-dwm-layout)<br><sub>42lizard</sub> | Herdr向けの、DWM風master/stackレイアウト | `dwm` `fzf` `rust` `shell` `tiling` | 1 | 🔄 2026-08-28 |
| [**herdr-medieval**](https://github.com/gabrielbarretoo/herdr-medieval)<br><sub>gabrielbarretoo</sub> | ワークスペースとエージェントを、六角形マスの中世風大陸として3D表示するHerdrプラグイン——各ワークスペースは柵に囲まれた野営地、各ペインは冒険者として、エージェントの状態に応じて訓練したり、キャンプファイアで休んだり、塔で見張りをする。three.js組み込みで、通信・依存関係なし | `3d` `hex-grid` `threejs` `javascript` | 1 | 2026-08-06 |
| [**herdr-spinup**](https://github.com/Royal-lobster/herdr-spinup)<br><sub>Royal-lobster</sub> | herdrの新規タブごとに表示されるスタート画面——ツールを選ぶとそのタブで実行される。ツールはJSONで定義 | `javascript` | 1 | 2026-08-04 |
| [**🆕 reasonix-herdr**](https://github.com/uuie/reasonix-herdr)<br><sub>uuie</sub> | Herdr内でのライフサイクルのリアルタイム報告とワークスペース制御を行う、ネイティブなReasonixプラグイン | `reasonix` `python` | 1 | 2026-07-10 |
| [**herdr-sesh**](https://github.com/xheisenbugx/herdr-sesh)<br><sub>xheisenbugx</sub> | seshに着想を得た、賢いherdrワークスペースマネージャー | `go` | 1 | 🔄 2026-08-21 |
| [**herdr-workspace**](https://github.com/zackshen/herdr-workspace)<br><sub>zackshen</sub> | herdrプラグイン：中央に表示されるポップアップから、ワークスペースを作成しレイアウトプロファイルを適用する | `rust` | 1 | 🔄 2026-08-24 |
| [**🆕 herdr-tab-command**](https://github.com/asermax/herdr-tab-command)<br><sub>asermax</sub> | 新しいタブに付けた名前に応じて、エージェントを起動したりコマンドを実行したりします。 | `typescript` | 0 | 🔄 2026-08-31 |
| [**ccc-herdr-layout**](https://github.com/caoer/ccc-herdr-layout)<br><sub>caoer</sub> | herdr向けのビジュアルレイアウトピッカー——1キーでライブプレビューしながら選べる | `go` | 0 | 2026-08-01 |
| [**herdr-yoke**](https://github.com/dgnsrekt/herdr-yoke)<br><sub>dgnsrekt</sub> | get yoked——1キーで2つのタブを並べて表示。herdr版のChromeスプリットビュー | `split-view` `terminal` `shell` | 0 | 2026-08-09 |
| [**🆕 herdr-plugin-dotfiles-dev-layout**](https://github.com/edmundmiller/herdr-plugin-dotfiles-dev-layout)<br><sub>edmundmiller</sub> | 自分のdotfilesの開発用ワークスペースレイアウトを開くためのHerdrプラグイン | `python` | 0 | 2026-06-23 |
| [**herdr-notebook**](https://github.com/goofansu/herdr-notebook)<br><sub>goofansu</sub> | ワークスペースごとに1つの永続的なMarkdownノートブックを、アクティブなペインの上でエディタから開く | `python` | 0 | 🔄 2026-08-20 |
| [**herdr-follow-cwd**](https://github.com/hasuwini77/herdr-follow-cwd)<br><sub>hasuwini77</sub> | herdrプラグイン：ワークスペースのラベルが、ペインが実際にいるディレクトリに追従する | `javascript` | 0 | 2026-08-13 |
| [**herdr-pane-id-metadata**](https://github.com/limars874/herdr-pane-id-metadata)<br><sub>limars874</sub> | 正規化されたペインIDと、コンパクトなタブ/ペインのサイドバーメタデータのための、最小構成のHerdrプラグイン | `coding-agents` `terminal` `javascript` | 0 | 2026-08-17 |
| [**herdr-lastfocus**](https://github.com/pedrobarco/herdr-lastfocus)<br><sub>pedrobarco</sub> | herdr向けの、tmux風の直前フォーカスしていたペイン/タブ/ワークスペースへの切り替え——フォーカスイベント履歴デーモンを介して実現 | `terminal-multiplexer` `tmux` `go` | 0 | 2026-07-25 |
| [**herdr-workspace-description**](https://github.com/rstacruz/herdr-workspace-description)<br><sub>rstacruz</sub> | _(説明なし)_ | `typescript` | 0 | 2026-08-08 |
| [**herdr-active-agent-jump**](https://github.com/shoaibkhanz/herdr-active-agent-jump)<br><sub>shoaibkhanz</sub> | herdrプラグイン：作業中/ブロック中のエージェントを、レイアウトの順序で前後に巡回してフォーカスする——attention-jumpを補完するvim風の操作 | `javascript` | 0 | 2026-07-12 |
| [**herdr-dev-layout**](https://github.com/simoncrypta/herdr-dev-layout)<br><sub>simoncrypta</sub> | Herdr向けの常時表示エージェントペイン | `herdr-integration` `shell` | 0 | 🔄 2026-08-20 |

<details><summary>この目的にも関係するもの</summary>

- [andrewchng/herdr-sessionizer](https://github.com/andrewchng/herdr-sessionizer) — プロジェクトやworktreeをファジー検索で開き、宣言的なTOMLレイアウト（タブ・ペイン分割・起動コマンド・リポジトリごとの上書き設定）からワークスペースを立ち上げる
- [fullerzz/herdr-plugin-sesh](https://github.com/fullerzz/herdr-plugin-sesh) — Herdr向けのSesh風ワークスペースピッカーTUI。zoxideと連携し、よく使うディレクトリからワークスペースを作成できる
- [ntindle/herdr-resurrect](https://github.com/ntindle/herdr-resurrect) — herdr版tmux-resurrect——ワークスペース・タブ・ペイン・作業ディレクトリ・実行中のプログラムやエージェントをスナップショットし、クラッシュや再起動後に復元する
- [enekos/herdr-quick-actions](https://github.com/enekos/herdr-quick-actions) — herdr標準のタブ/ペイン/ワークスペース操作を、使用頻度順でfzfから選べる——キーバインドを覚える必要がなくなる
- [salkhalil/herdr-sessionizer](https://github.com/salkhalil/herdr-sessionizer) — herdr版tmux-sessionizer：開いているワークスペースとzoxideのディレクトリをfzfで検索し、テンプレートタブ付きで作成またはフォーカスする
- [crierr/herdr-arrange](https://github.com/crierr/herdr-arrange) — herdrのペイン移動・入れ替え・再分割・レイアウト変更を行う、インタラクティブなポップアップUI
- [aliou/herdr-cast](https://github.com/aliou/herdr-cast) — 個人用Herdrプラグイン——ネイティブmacOS通知、ファジーなワークスペース移動、zoxide連携のワークスペース作成、レイアウトコマンドをまとめて提供
- [42lizard/herdr-sessionizer](https://github.com/42lizard/herdr-sessionizer) — tmux-sessionizer風のherdr向けプラグイン
- [chandrasekharan98/herdr-workspace-save](https://github.com/chandrasekharan98/herdr-workspace-save) — Herdrのワークスペース（レイアウト・作業ディレクトリ・エージェントセッション・実行中のコマンド）を保存し、あとでfzfピッカーから再度開ける
- [asermax/herdr-suspend-workspace](https://github.com/asermax/herdr-suspend-workspace) — herdrのワークスペースをサスペンド——レイアウトとエージェントをスナップショットして閉じ、あとでポップアップから選んで復元できる
- [willfish/herdr-workspacex](https://github.com/willfish/herdr-workspacex) — Rustネイティブのファジー検索型Herdrワークスペース切り替えツール——zoxideを利用したワークスペース作成に対応

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-navigate"></a>

## ペイン移動・キー操作

> ペインやワークスペース間の移動・リサイズを、エディタと同じキーで済ませたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**vim-herdr-navigation**](https://github.com/paulbkim-dev/vim-herdr-navigation)<br><sub>paulbkim-dev</sub> | Ctrl+h/j/k/lでherdrのペインとVim/Neovimのスプリットをシームレスに移動——vim-tmux-navigatorのherdr版 | `neovim` `vim` `shell` | 100 | 🔄 2026-08-23 |
| [**herdr-splits.nvim**](https://github.com/lmilojevicc/herdr-splits.nvim)<br><sub>lmilojevicc</sub> | HerdrとNeovimのスプリットをスマートに移動・リサイズする | `lua` `neovim` `neovim-plugin` `neovim-plugins` `nvim` | 57 | 2026-08-17 |
| [**herdr-floax**](https://github.com/Tyru5/herdr-floax)<br><sub>Tyru5</sub> | herdr向けのフローティング作業用シェル——tmux-floax風に開閉できるポップアップで、ワークスペースごとに1つ、セッションは永続化される | `rust` `terminal` `tmux-floax` | 24 | 2026-07-26 |
| [**herdr-nvim-nav**](https://github.com/aimdevlee/herdr-nvim-nav)<br><sub>aimdevlee</sub> | herdrのペインとNeovimのスプリットをまたいだシームレスなCtrl+h/j/k/l移動——ソケットベースでキー入力ごとのプロセス起動なし | `neovim` `neovim-plugin` `lua` | 18 | 2026-08-02 |
| [**herdr-last-workspace**](https://github.com/third774/herdr-last-workspace)<br><sub>third774</sub> | 直前にフォーカスしていたワークスペースに切り替えるプラグイン | `rust` | 17 | 2026-06-22 |
| [**herdr-logbook**](https://github.com/Resetnak/herdr-logbook)<br><sub>Resetnak</sub> | ターミナルのための作業メモリ——オフラインでMarkdown中心のノート、決定事項、Herdr向けの現在タスクnow.mdを管理 | `adr` `bubbletea` `cli` `go` `markdown` | 12 | 🔄 2026-09-03 |
| [**herdr-pane-mover**](https://github.com/osamahbeig/herdr-pane-mover)<br><sub>osamahbeig</sub> | herdr向けのクリック可能なオーバーレイメニュー：タブやワークスペースを横断してペインの移動・再分割・入れ替えができる | `terminal` `tui` `javascript` | 11 | 2026-07-10 |
| [**herdr-recent-navigator**](https://github.com/beyondlex/herdr-recent-navigator)<br><sub>beyondlex</sub> | Herdr向けの、最近使ったワークスペース/タブ/ペインの切り替えツール。最近フォーカスしたワークスペース・タブ・ペイン・AIエージェントの一覧をポップアップ表示し、ファジー検索とキーボード操作に対応 | `agent` `mru` `navigator` `pane` `popup` | 10 | 2026-07-28 |
| [**herdr-paddock**](https://github.com/neyham/herdr-paddock)<br><sub>neyham</sub> | 🐑 herdrのエージェント向けカードウォール型フィード——群れ全体をざっと見渡し、1体にズームインして返信できる。すべて素のSSH経由 | `bubbletea` `go` `ssh` `tui` | 10 | 🔄 2026-08-25 |
| [**herdr-command-center**](https://github.com/speardragon/herdr-command-center)<br><sub>speardragon</sub> | すべてのコマンドを1つのキーバインドで——登録したコマンドを一覧表示するherdrのポップアップ。矢印キーや番号で実行し、コマンド実行前に自動で閉じる | `command-palette` `nodejs` `terminal` `toml` `tui` | 10 | 2026-08-19 |
| [**herdr-trail**](https://github.com/catoncat/herdr-trail)<br><sub>catoncat</sub> | herdr全体で共有するメモ——エージェントがフォローアップを書き留め、人間は1つのグローバルリストで管理し、各エントリから元の会話に直接ジャンプできる | `javascript` | 8 | 🔄 2026-08-26 |
| [**herdr-toggle-popup**](https://github.com/maro114510/herdr-toggle-popup)<br><sub>maro114510</sub> | 1つのキーバインドでオーバーレイのポップアップシェルを開閉できるHerdrターミナル向けプラグイン | `go` | 7 | 2026-08-12 |
| [**nvim-herdr-navigation**](https://github.com/bojackduy/nvim-herdr-navigation)<br><sub>bojackduy</sub> | vim-tmux-navigator風のctrl+h/j/k/lで、Neovimのスプリットとherdrのペイン間を移動する | `keyboard-shortcuts` `lazyvim` `lua` `navigation` `neovim` | 6 | 2026-07-20 |
| [**herdr-cliamp**](https://github.com/coryshaw1/herdr-cliamp)<br><sub>coryshaw1</sub> | 隠しても再生を続ける、herdr向けのフローティングcliamp——プレイヤーはデタッチされたherdrセッション内で動くため、フロートを閉じてもデタッチされるだけで再生は止まらない | `audiobook` `cliamp` `music-player` `podcast` `terminal` | 6 | 🔄 2026-08-24 |
| [**herdr-swipe**](https://github.com/husniadil/herdr-swipe)<br><sub>husniadil</sub> | Herdr向けのトラックパッドジェスチャー——ペイン・タブ・スペース間の移動と、対応待ちのエージェントへのジャンプができる | `cgeventtap` `gestures` `macos` `python` `terminal` | 6 | 🔄 2026-08-20 |
| [**herdr-equalize-panes**](https://github.com/shibayu36/herdr-equalize-panes)<br><sub>shibayu36</sub> | 分割やクローズのたびにペインサイズを自動的に均等化するherdrプラグイン（tmuxのselect-layout -Eを自動で行うイメージ） | `terminal` `perl` | 6 | 🔄 2026-08-22 |
| [**herdr-omnisearch**](https://github.com/dmnkf/herdr-omnisearch)<br><sub>dmnkf</sub> | Herdrのワークスペース・ペイン・アーカイブ済みエージェントセッションを高速にローカル検索・移動する | `python` | 5 | 🔄 2026-08-31 |
| [**nvim-herdr-navigator**](https://github.com/kaar/nvim-herdr-navigator)<br><sub>kaar</sub> | Neovimのスプリットとherdrのペインをシームレスに移動——1組の`ctrl+h/j/k/l`でvimとherdrのペインの両方を移動できる | `neovim` `neovim-plugin` `lua` | 5 | 2026-07-29 |
| [**herdr-scratch**](https://github.com/AkashJana18/herdr-scratch)<br><sub>AkashJana18</sub> | Herdr向けの永続化されたスクラッチパッド。フローティングのユーティリティペインへの足がかりとなる | `cli` `rust` `scratchpad` | 4 | 🔄 2026-08-30 |
| [**🆕 herdr-arrange**](https://github.com/crierr/herdr-arrange)<br><sub>crierr</sub> | herdrのペイン移動・入れ替え・再分割・レイアウト変更を行う、インタラクティブなポップアップUI | `go` | 4 | 🔄 2026-08-31 |
| [**herdr-annotations**](https://github.com/jagzmz/herdr-annotations)<br><sub>jagzmz</sub> | Herdr上で選択したターミナルのテキストに、高速なローカルファーストのポップアップと再利用可能なコレクションで注釈を付ける | `annotations` `cli` `coding-agents` `developer-tools` `local-first` | 4 | 2026-07-16 |
| [**herdr-harpoon**](https://github.com/KonstantinKai/herdr-harpoon)<br><sub>KonstantinKai</sub> | herdr版Harpoon：ペインにマークを付けてインデックスでジャンプする。Bashのみでビルド不要 | `bash` `harpoon` `tmux-harpoon` `shell` | 4 | 2026-07-29 |
| [**herdr-last**](https://github.com/lmilojevicc/herdr-last)<br><sub>lmilojevicc</sub> | Herdrで直前にアクティブだったワークスペースまたはタブに切り替え戻す | `go` `linux` `macos` `productivity` `tabs` | 4 | 2026-08-07 |
| [**herdr-equalize-splits**](https://github.com/markhuot/herdr-equalize-splits)<br><sub>markhuot</sub> | herdrプラグイン：現在のタブ内のすべてのスプリットを、行/列ごとに均等な幅に揃える（Ctrl+b =にバインド） | `terminal` `tmux` `javascript` | 4 | 2026-07-08 |
| [**herdr-attention**](https://github.com/milkyskies/herdr-attention)<br><sub>milkyskies</sub> | herdrプラグイン：1キーで、注意が必要な次のエージェント（ブロック中、次に完了済み）にフォーカスを移す | `javascript` | 4 | 2026-07-08 |
| [**herdr-navigator**](https://github.com/willfish/herdr-navigator)<br><sub>willfish</sub> | Vim/Neovimを意識したペイン移動のための、Herdr側のナビゲーション操作 | `navigation` `neovim` `rust` | 4 | 2026-07-07 |
| [**herdr-tmux-layout**](https://github.com/crierr/herdr-tmux-layout)<br><sub>crierr</sub> | 稼働中のHerdrペインに使える、tmux風のプリセットレイアウト——cycle・even-horizontal・even-vertical・main-horizontal・main-vertical・tiled・balanceに対応 | `go` | 3 | 🔄 2026-08-30 |
| [**herdr-convo-index**](https://github.com/dzwduan/herdr-convo-index)<br><sub>dzwduan</sub> | herdr内のClaude Codeペイン用のターン索引——過去の任意のターンにジャンプしてポップアップで読める | `python` | 3 | 2026-07-27 |
| [**herdr-popupx**](https://github.com/jeromychu23/herdr-popupx)<br><sub>jeromychu23</sub> | Herdr向けの、永続化されたネイティブのフローティング作業用ポップアップ | `rust` `terminal` `tui` | 3 | 2026-07-21 |
| [**herdr-unread-marker**](https://github.com/JoanGil/herdr-unread-marker)<br><sub>JoanGil</sub> | キーバインドでフォーカス中のエージェントを未読/既読にマークする（手動のみ） | `shell` | 3 | 2026-07-17 |
| [**herdr-confirm-close-pane**](https://github.com/poweroutlet2/herdr-confirm-close-pane)<br><sub>poweroutlet2</sub> | ペインを閉じる前に確認を求めるherdrプラグイン——tmuxのprefix+xのconfirm-beforeのような動作 | `shell` | 3 | 2026-07-06 |
| [**herdr-pretty-which**](https://github.com/ramarivera/herdr-pretty-which)<br><sub>ramarivera</sub> | Herdr向けの、Rust/Ratatui製which-key風キーバインドオーバーレイ | `ratatui` `rust` `terminal` `tui` `which-key` | 3 | 2026-08-14 |
| [**🆕 herdr-mission-control**](https://github.com/vjeantet/herdr-mission-control)<br><sub>vjeantet</sub> | herdr 用のミッションコントロール。1 キーで、ワークスペースの全ペインをタブごとにまとめたライブタイルグリッドとして表示し、選んで切り替えられます。 | `expose` `mission-control` `terminal` `tui` `rust` | 3 | 🔄 2026-09-01 |
| [**herdr-equalize-vsplit**](https://github.com/devoc09/herdr-equalize-vsplit)<br><sub>devoc09</sub> | 現在のペインを右に分割し、列の幅を均等にするHerdrプラグイン | `go` | 2 | 2026-07-15 |
| [**herdr-easymotion**](https://github.com/elliotekj/herdr-easymotion)<br><sub>elliotekj</sub> | 🦘 Herdrのペイン間を直接ジャンプする | `javascript` | 2 | 2026-07-20 |
| [**herdr-break-pane**](https://github.com/iuhoay/herdr-break-pane)<br><sub>iuhoay</sub> | フォーカス中のペインを新しいタブに移動する、小さなHerdrプラグイン | `pane` `javascript` | 2 | 🔄 2026-08-27 |
| [**herdr-prevtab**](https://github.com/joo-was-already-taken/herdr-prevtab)<br><sub>joo-was-already-taken</sub> | 直前にフォーカスしていたタブに切り替えるHerdrプラグイン | `rust` | 2 | 🔄 2026-09-01 |
| [**herdr-lazytask**](https://github.com/mdetweil/herdr-lazytask)<br><sub>mdetweil</sub> | herdrのスプリットペインでLazytaskを使う（開く/フォーカス/トグル）ほか、Taskwarriorのクイックアクションも提供 | `lazytask` `taskwarrior` `terminal` `rust` | 2 | 2026-08-02 |
| [**herdr-float**](https://github.com/meerzulee/herdr-float)<br><sub>meerzulee</sub> | Zellij風のALT+Fで開くフローティングペイン | `shell` | 2 | 2026-07-20 |
| [**herdr-quotr**](https://github.com/napalmpapalam/herdr-quotr)<br><sub>napalmpapalam</sub> | herdrのポップアップから、エージェント自身の回答を引用してそのエージェントに投げ返す | `claude-code` `rust` `tui` | 2 | 🔄 2026-09-01 |
| [**herdr-pane-mover**](https://github.com/ronly2460/herdr-pane-mover)<br><sub>ronly2460</sub> | 矢印キーで操作するインタラクティブなピッカーで、Herdrのペインをワークスペース間で移動する | `terminal` `workspace` `shell` | 2 | 🔄 2026-08-23 |
| [**herdr-pane-orientation-switcher**](https://github.com/sf1tzp/herdr-pane-orientation-switcher)<br><sub>sf1tzp</sub> | Herdrのスプリットペイン向けの、ワークフロー人間工学 | `shell` | 2 | 2026-07-25 |
| [**herdr-ask-inbox**](https://github.com/speardragon/herdr-ask-inbox)<br><sub>speardragon</sub> | すべてのherdrワークスペースからブロックされたClaudeのAskUserQuestionプロンプトを1つのポップアップに集約し、その場で回答できる。間違ったエージェントに回答を送ってしまう心配もない | `claude-code` `javascript` | 2 | 2026-07-25 |
| [**herdr-unread-jump**](https://github.com/to4iki/herdr-unread-jump)<br><sub>to4iki</sub> | 注意が必要な次のHerdrエージェントペイン（ブロック中、次に完了済み）にジャンプする | `agents` `bash` `shell` | 2 | 🔄 2026-08-30 |
| [**herdr-plugin-ide-jump**](https://github.com/agentience/herdr-plugin-ide-jump)<br><sub>agentience</sub> | IDEにすぐ戻れる——フォーカス中のペインのプロジェクトのエディタウィンドウを前面に出す、または絞り込み可能なポップアップから選ぶ。Herdrプラグイン | `python` | 1 | 🔄 2026-08-24 |
| [**herdr-voice**](https://github.com/aneym/herdr-voice)<br><sub>aneym</sub> | herdrの音声操作——話しかけるだけでスペース作成・ペイン分割・コーディングエージェントの操作ができる。OpenAI Realtimeを使用し、リアルタイムの文字起こしを表示するフローティングHUD付き | `openai-realtime-api` `voice` `javascript` | 1 | 2026-08-01 |
| [**herdr-plugin-tiles**](https://github.com/carsonjones/herdr-plugin-tiles)<br><sub>carsonjones</sub> | herdr向けのシンプルなペインマネージャー | `python` | 1 | 2026-06-19 |
| [**herdr-notes**](https://github.com/cyperx84/herdr-notes)<br><sub>cyperx84</sub> | Herdr向けの、ワークスペースごとに独立したMarkdownスクラッチノート。Go製 | `bubbletea` `golang` `markdown` `notes` `go` | 1 | 2026-08-16 |
| [**🆕 herdr-tab-jump**](https://github.com/cyperx84/herdr-tab-jump)<br><sub>cyperx84</sub> | 任意のキーバインドから、位置で指定した herdr のタブ N にフォーカスします——数字キーの列をタブとワークスペースに割り振れます。 | `shell` | 1 | 🔄 2026-09-01 |
| [**herdr-last-tab**](https://github.com/dantehemerson/herdr-last-tab)<br><sub>dantehemerson</sub> | 直前にフォーカスしていたタブに切り替えるプラグイン | `rust` | 1 | 2026-08-12 |
| [**🆕 herdr-swipe-linux**](https://github.com/enisbu/herdr-swipe-linux)<br><sub>enisbu</sub> | Linux 版 Herdr 向けのトラックパッドジェスチャー。スワイプでペイン・タブ・スペースを移動し、タップで入力待ちのエージェントへジャンプできます。 | `evdev` `gestures` `gnome` `hyprland` `linux` | 1 | 🔄 2026-09-02 |
| [**herdr-nav-history**](https://github.com/jugyo/herdr-nav-history)<br><sub>jugyo</sub> | herdr向けの、ブラウザ風の戻る/進むナビゲーション（ペイン・タブ・ワークスペースのフォーカス履歴を対象） | `javascript` | 1 | 2026-07-12 |
| [**herdr-plugin-switcher**](https://github.com/KadenThomp36/herdr-plugin-switcher)<br><sub>KadenThomp36</sub> | Ctrlを押しながらTabで、最近使った順にherdrのペインを切り替える。macOS版herdr向けの、Arc/Zen風ペインスイッチャー | `swift` | 1 | 🔄 2026-08-21 |
| [**herdr-nvim-aware**](https://github.com/KoalaVim/herdr-nvim-aware)<br><sub>KoalaVim</sub> | herdr向けのNvim対応キーバインド——移動・分割・クローズ・ズームに対応 | `rust` | 1 | 🔄 2026-08-20 |
| [**herdr-plugin-last**](https://github.com/m4salah/herdr-plugin-last)<br><sub>m4salah</sub> | tmux風の直前タブ・直前ワークスペースへの移動をHerdrに追加する | `rust` | 1 | 2026-07-30 |
| [**herdr-scratch**](https://github.com/macintacos/herdr-scratch)<br><sub>macintacos</sub> | herdr向けのスクラッチシェル——1つのコード（キーの組み合わせ）で開閉するポップアップ。裏側はtmuxなので、離れたときのまま正確に復元される | `go` | 1 | 🔄 2026-08-28 |
| [**herdr-normal-mode**](https://github.com/maedana/herdr-normal-mode)<br><sub>maedana</sub> | herdrのサイドバー向けのVim風ノーマルモード——j/kで行移動、h/lでタブ移動、0-9でペイン選択 | `rust` `tui` | 1 | 🔄 2026-08-24 |
| [**herdr-next-agent**](https://github.com/martin-ro/herdr-next-agent)<br><sub>martin-ro</sub> | Herdrプラグイン：設定可能な優先度に基づいて、注意が必要な次のエージェントにジャンプする | `python` | 1 | 2026-07-15 |
| [**herdr-touchbar**](https://github.com/omerturhan/herdr-touchbar)<br><sub>omerturhan</sub> | MacBookのTouch Barに作業中・ブロック中のherdrエージェントを表示——タップすると該当タブに直接移動する | `ai-agents` `macos` `touchbar` `swift` | 1 | 2026-07-30 |
| [**herdr-deck-navigation**](https://github.com/raghu-nandan-bs/herdr-deck-navigation)<br><sub>raghu-nandan-bs</sub> | herdr標準のフラットなワークスペース/タブ/ペインナビゲーターを、スクロールなしで任意のペインに素早くたどり着ける「デッキ」表示に置き換える | `rust` `terminal` `tui` | 1 | 🔄 2026-08-24 |
| [**herdr-account-switch**](https://github.com/rcosteira79/herdr-account-switch)<br><sub>rcosteira79</sub> | 再認証なしでClaude Code / Codexのログインをホットスワップする。オーバーレイピッカー、次へ切り替えるキーバインド、ペインごとのアカウントバッジ（$acct）を提供 | `python` | 1 | 🔄 2026-09-02 |
| [**herdr-smartnav**](https://github.com/retroaalto/herdr-smartnav)<br><sub>retroaalto</sub> | 方向を意識したペインナビゲーションを提供するHerdrプラグイン | `go` | 1 | 2026-08-01 |
| [**herdr-edge-nav**](https://github.com/sebcbi1/herdr-edge-nav)<br><sub>sebcbi1</sub> | ペインの端でタブやワークスペースをまたいで移動・リサイズできる、方向指定型のHerdrプラグイン。Neovimのスプリットもシームレスに認識する | `lua` | 1 | 2026-08-12 |
| [**herdr-ferry**](https://github.com/shadowfax92/herdr-ferry)<br><sub>shadowfax92</sub> | 稼働中のHerdrのペインやタブを複数まとめて移動したり、ワークスペースを統合したりできる、Rustネイティブのポップアップ | `productivity` `rust` `terminal` `tui` | 1 | 2026-08-19 |
| [**herdr-scratch**](https://github.com/shadowfax92/herdr-scratch)<br><sub>shadowfax92</sub> | 非公開のtmuxセッションを裏側で使う、永続化されたペインごとのHerdrスクラッチポップアップ | `neovim` `productivity` `rust` `terminal` `tmux` | 1 | 2026-08-04 |
| [**herdr-talon**](https://github.com/shadowfax92/herdr-talon)<br><sub>shadowfax92</sub> | 画面に見えているHerdrのターミナル要素に、空間的なキーボードヒントを表示する | `keyboard-navigation` `productivity` `rust` `terminal` `tmux-fingers` | 1 | 2026-08-20 |
| [**herdr-nav-plus**](https://github.com/shoaibkhanz/herdr-nav-plus)<br><sub>shoaibkhanz</sub> | Ctrl+h/j/k/lでherdrのペインを越えてワークスペースまで移動できるナビゲーション——vimを意識した動作で、両端でループする | `javascript` | 1 | 2026-07-18 |
| [**herdr-hintr**](https://github.com/wraithyy/herdr-hintr)<br><sub>wraithyy</sub> | herdrプラグイン：which-key風のキーバインド・チートシートをポップアップ表示——キーを押すとそのまま実行できる | `shell` | 1 | 2026-08-11 |
| [**herdr-notes**](https://github.com/0xfelixli/herdr-notes)<br><sub>0xfelixli</sub> | 選択したターミナルのテキストに、Rust製のポップアップテキストボックスで注釈を付ける——herdrプラグイン | `rust` `terminal` | 0 | 🔄 2026-08-27 |
| [**herdr-popup**](https://github.com/abelfubu/herdr-popup)<br><sub>abelfubu</sub> | その場限りのシェルコマンド実行のための、汎用的なHerdrポップアップペインプラグイン | `shell` | 0 | 🔄 2026-08-21 |
| [**herdr-layout-cycle**](https://github.com/amiramay/herdr-layout-cycle)<br><sub>amiramay</sub> | herdrプラグイン：あらかじめ用意したペインレイアウトを順番に切り替える。tmuxのprefix+space風 | `javascript` | 0 | 2026-08-08 |
| [**🆕 herdr-plugin-echo**](https://github.com/andischerer/herdr-plugin-echo)<br><sub>andischerer</sub> | 1つのペインから、マークした複数のペインにキー入力をブロードキャストするHerdrプラグイン | `typescript` | 0 | 🔄 2026-08-23 |
| [**🆕 herdr-hyprland**](https://github.com/aorumbayev/herdr-hyprland)<br><sub>aorumbayev</sub> | Hyprland に着想を得た、herdr 用の操作方法です。 | `ai-agents` `developer-tools` `golang` `hyprland` `keybindings` | 0 | 🔄 2026-08-31 |
| [**gotopr**](https://github.com/asumaran/gotopr)<br><sub>asumaran</sub> | ローカルのリポジトリとworktreeを横断して、開いているGitHub PRにジャンプするHerdrプラグイン | `go` | 0 | 🔄 2026-08-23 |
| [**herdr-confirm-close**](https://github.com/asumaran/herdr-confirm-close)<br><sub>asumaran</sub> | herdrプラグイン：フォーカス中のペインを閉じる際、その中でプロセスが実行中のときだけ確認を求める | `terminal` `go` | 0 | 🔄 2026-08-23 |
| [**herdr-auto-focus**](https://github.com/calorie/herdr-auto-focus)<br><sub>calorie</sub> | macOSの入力がアイドルになったら、注意が必要なHerdrのエージェントに自動でフォーカスする | `golang` `macos` `go` | 0 | 2026-07-27 |
| [**herdr-next-agent**](https://github.com/choplin/herdr-next-agent)<br><sub>choplin</sub> | 設定した意味的な状態にあるHerdrエージェント間を移動する | `go` | 0 | 🔄 2026-08-24 |
| [**herdr-split-pane**](https://github.com/choplin/herdr-split-pane)<br><sub>choplin</sub> | 呼び出し元が指定したコマンドを、Herdrのスプリットペインで直接開く | — | 0 | 🔄 2026-08-24 |
| [**herdr-nav**](https://github.com/codingfragments/herdr-nav)<br><sub>codingfragments</sub> | herdrのワークスペースとペインナビゲーション。herdr-navigationの現代版で、プレビュー機能の改善と新しいワークスペーステンプレート処理に対応 | `html` | 0 | 🔄 2026-08-27 |
| [**herdr-which-key**](https://github.com/CowboyVang/herdr-which-key)<br><sub>CowboyVang</sub> | herdr向けのwhich-key風キーマップオーバーレイ——1キー押すとprefix配下の全バインドがグループ化・ラベル付きで表示され、2つ目のキーで実行できる。長押し表示ではなく明示的な呼び出し方式。依存なし | `keybindings` `terminal` `which-key` `python` | 0 | 2026-08-02 |
| [**🆕 herdr-agent-numbers**](https://github.com/DillonWall/herdr-agent-numbers)<br><sub>DillonWall</sub> | herdr のエージェントパネルに番号を振り、focus_agent（prefix+1〜9）に対応させます。 | `terminal-multiplexer` `shell` | 0 | 🔄 2026-09-01 |
| [**🆕 herdr-drover**](https://github.com/followbl/herdr-drover)<br><sub>followbl</sub> | Herdr 用の「牧羊犬」タブスイッチャー。Super+T を押し続けてタブを巡回し、離した位置で切り替わります。 | `linux` `python` | 0 | 🔄 2026-09-03 |
| [**herdr-plugin-agents-usage**](https://github.com/gecm0/herdr-plugin-agents-usage)<br><sub>gecm0</sub> | 各プロバイダーの使用状況（Claude、Codex、OpenCode Go、Neuralwatt）をHerdrのモーダルポップアップに表示する | `claude` `codex` `opencode` `terminal` `usage` | 0 | 2026-07-26 |
| [**herdr-desktop-switcher**](https://github.com/gustavocaiano/herdr-desktop-switcher)<br><sub>gustavocaiano</sub> | Herdr向けの、実験的なmacOSデスクトップ切り替えツール | `rust` | 0 | 🔄 2026-08-26 |
| [**herdr-harpoon**](https://github.com/hadeson/herdr-harpoon)<br><sub>hadeson</sub> | herdr向けのHarpoon風ペインマーク：ペインをスロット1〜9にピン留めし、タブやワークスペースを越えて直接ジャンプできる | `harpoon` `pane-navigation` `terminal` `tmux` `python` | 0 | 2026-07-25 |
| [**herdr-counting-sheep**](https://github.com/inonprince/herdr-counting-sheep)<br><sub>inonprince</sub> | HerdrのSpaceとAgentをライブに一覧表示——直前のタブ・Space・Agentへジャンプするショートカット付き | `productivity` `terminal` `javascript` | 0 | 2026-08-03 |
| [**herdr-matter-wall**](https://github.com/Javamomma/herdr-matter-wall)<br><sub>Javamomma</sub> | herdrプラグイン：プロジェクト内で最も活発なサブディレクトリを、読み取り専用のAIステータスカードのライブウォールとしてタイル表示する | `claude-code` `shell` | 0 | 2026-07-14 |
| [**herdr-nav**](https://github.com/jmarcelomb/herdr-nav)<br><sub>jmarcelomb</sub> | herdr向けのペイン・タブ・ワークスペース間ナビゲーションプラグイン | `rust` | 0 | 2026-07-30 |
| [**🆕 herdr-pane-mark**](https://github.com/jovylle/herdr-pane-mark)<br><sub>jovylle</sub> | Herdr プラグイン——パレット/ポップアップから、Agents 配下にカスタムの $mark を設定できます（フォーク不要）。 | `terminal` `shell` | 0 | 🔄 2026-09-01 |
| [**🆕 herdr-positional-tabs**](https://github.com/juezhong/herdr-positional-tabs)<br><sub>juezhong</sub> | Herdr向けの、安定した位置ベースのタブラベルとAlt+数字によるナビゲーション | `rust` `terminal` | 0 | 🔄 2026-08-30 |
| [**herdr-last-tab**](https://github.com/k-narusawa/herdr-last-tab)<br><sub>k-narusawa</sub> | _(説明なし)_ | `shell` | 0 | 🔄 2026-08-22 |
| [**herdr-hasr**](https://github.com/KazBrekker1/herdr-hasr)<br><sub>KazBrekker1</sub> | Hasr（حصر — 「列挙・完全な集計」の意）——herdr向けのgoto風ポップアップ切り替えツール：エージェント・タブ・スペースの切り替え・リネーム・削除・作成ができ、完了状況もリアルタイムに追跡する | `tui` `go` | 0 | 2026-07-23 |
| [**herdr-cmd-marks**](https://github.com/leonho/herdr-cmd-marks)<br><sub>leonho</sub> | herdrプラグイン：プロジェクトごとのコマンドブックマークをポップアップ表示。エージェントが作業中でも、別のシェルでブックマーク済みのコマンドを実行できる（グローバル・プロジェクト・スマートセクションに対応） | `shell` | 0 | 2026-07-18 |
| [**herdr-reshape**](https://github.com/macintacos/herdr-reshape)<br><sub>macintacos</sub> | フォーカス中のペインをタブ内で移動させ、タブ全体を均等なグリッドに整えるherdrプラグイン | `go` | 0 | 🔄 2026-09-04 |
| [**herdr-pane-balancer**](https://github.com/malone-c/herdr-pane-balancer)<br><sub>malone-c</sub> | ペインの開閉に合わせて、herdrのペインを常に均等なサイズに保つ。スプリットするとフォーカス中のペインが半分になるが、このプラグインがタブ全体を再調整する | `python` | 0 | 2026-08-07 |
| [**herdr-focus-or-tab**](https://github.com/mholtzscher/herdr-focus-or-tab)<br><sub>mholtzscher</sub> | タブの境界をまたいでHerdrのペインを順に切り替える | `terminal-multiplexer` `rust` | 0 | 2026-07-31 |
| [**🆕 herdr-plugin-recent-spaces**](https://github.com/mike-bronner/herdr-plugin-recent-spaces)<br><sub>mike-bronner</sub> | Herdr プラグイン：スペースのサイドバーを、直近に使った順に並べ替えます。 | `python` | 0 | 🔄 2026-09-02 |
| [**herdr-plugins**](https://github.com/oullin/herdr-plugins)<br><sub>oullin</sub> | Herdr向けの、それぞれ独立してインストールできる、目的に特化したプラグイン集 | `typescript` | 0 | 2026-08-09 |
| [**herdr-equalize-panes**](https://github.com/ponko2/herdr-equalize-panes)<br><sub>ponko2</sub> | ペインが作成・クローズ・移動・終了するたびに、各タブ内のペインを自動的に均等サイズに保つ | `rust` | 0 | 🔄 2026-08-30 |
| [**herdr-focused-codex-fork**](https://github.com/potatoQi/herdr-focused-codex-fork)<br><sub>potatoQi</sub> | フォーカス中のHerdrペインのCodexセッションを、右側のペインにフォークする | `shell` | 0 | 2026-08-09 |
| [**herdr-whichkey**](https://github.com/Qu4tro/herdr-whichkey)<br><sub>Qu4tro</sub> | herdr向けの、blezz/which-key風のアクションメニュー——トリガーキーを押すだけで、あとは1アクション1キー操作。入力もEnterも不要 | `rust` | 0 | 2026-07-22 |
| [**herdr-close-other-panes**](https://github.com/reobin/herdr-close-other-panes)<br><sub>reobin</sub> | herdr版のvim ctrl-w o——フォーカス中のペイン以外をすべて閉じる | `shell` | 0 | 🔄 2026-08-25 |
| [**herdr-pane-equalizer**](https://github.com/shanefully-done/herdr-pane-equalizer)<br><sub>shanefully-done</sub> | herdrのペインを均等なサイズにリサイズする。自動でも手動でも実行可能 | `javascript` | 0 | 2026-08-20 |
| [**🆕 herdr-pane-tools**](https://github.com/solidsnakedev/herdr-pane-tools)<br><sub>solidsnakedev</sub> | herdr 向けに、Vim を意識したペイン移動、aerospace 風のペイン移動、tmux 風のローテーションを提供します。 | `shell` | 0 | 🔄 2026-09-01 |
| [**herdr-tabpick**](https://github.com/sushidesu/herdr-tabpick)<br><sub>sushidesu</sub> | 最近使った順にherdrのタブを選べる。ライブなペインプレビュー付き | `shell` | 0 | 2026-08-15 |
| [**herdr-confirm-close**](https://github.com/tajdien/herdr-confirm-close)<br><sub>tajdien</sub> | herdrプラグイン：ペインやタブを閉じる前に確認ポップアップを出す | `shell` | 0 | 2026-08-13 |
| [**herdr-jump**](https://github.com/tp6gw94/herdr-jump)<br><sub>tp6gw94</sub> | Herdrのワークスペース・タブ・ペイン・エージェント向けの、キーボードナビゲーション | `javascript` | 0 | 2026-08-16 |
| [**🆕 herdr-focus**](https://github.com/trapple/herdr-focus)<br><sub>trapple</sub> | 次にブロック中/完了したエージェントペインにフォーカスし、ターミナルアプリを最前面に出す。グローバルホットキー付き | `shell` | 0 | 2026-07-19 |
| [**herdr-golden-ratio**](https://github.com/vigneshwerv/herdr-golden-ratio)<br><sub>vigneshwerv</sub> | フォーカス中のHerdrペインを黄金比（約61.8%）にリサイズする | `go` `terminal` | 0 | 🔄 2026-08-24 |
| [**herdr-balance-panes**](https://github.com/willfish/herdr-balance-panes)<br><sub>willfish</sub> | 現在のHerdrタブ内のペインを均等な大きさに揃える（tmuxのselect-layout -E相当） | `rust` `terminal` `tmux` | 0 | 2026-08-05 |
| [**🆕 herdr-grid**](https://github.com/WillHeather/herdr-grid)<br><sub>WillHeather</sub> | herdr ワークスペースのエージェントペインを画面いっぱいのグリッドに敷き詰め、また元に戻せます。 | `python` | 0 | 🔄 2026-08-31 |
| [**herdr-compass**](https://github.com/ycros/herdr-compass)<br><sub>ycros</sub> | Herdrのペイン・タブ・ワークスペースを横断する、統一された方向キーナビゲーション | `python` | 0 | 2026-08-07 |
| [**herdr-kakoune-popup**](https://github.com/Yukaii/herdr-kakoune-popup)<br><sub>Yukaii</sub> | Herdrネイティブのポップアップで、Kakouneのターミナルコマンドを実行する | `kakoune` `shell` | 0 | 2026-08-20 |

<details><summary>この目的にも関係するもの</summary>

- [thanhdat77/herdr-navigator](https://github.com/thanhdat77/herdr-navigator) — 1つのファジーナビゲーターから、任意のHerdrのワークスペース・エージェント・プロジェクト・セッション・リモート・ディレクトリ・アクションにジャンプできる
- [qu8n/herdr-automatic-rename](https://github.com/qu8n/herdr-automatic-rename) — Smart tab names and numbered labels for a smooth herdr navigation
- [speardragon/herdr-plugin-manager](https://github.com/speardragon/herdr-plugin-manager) — ポップアップからherdrのプラグインを管理——インストール・更新・有効/無効化・アンインストール、herdr-pluginマーケットプレイスの閲覧も可能。推奨キー：prefix+p
- [jorge07RD/herdr-ssh-manager](https://github.com/jorge07RD/herdr-ssh-manager) — SSHホストを保存し、Herdr内のファジーポップアップから再接続する——Enterキーでポップアップからそのままsshに渡す
- [bayoudhi/herdr-prayer-times](https://github.com/bayoudhi/herdr-prayer-times) — 次の礼拝時刻とカウントダウンをHerdrのサイドバーに表示——タイムテーブルのポップアップと通知付き
- [black-atom-industries/helm.herdr](https://github.com/black-atom-industries/helm.herdr) — 1つのファジーナビゲーターから、任意のHerdrのワークスペース・エージェント・プロジェクト・セッション・リモート・ディレクトリ・アクションにジャンプできる
- [victor-software-house/herdr-stash](https://github.com/victor-software-house/herdr-stash) — Herdrのワークスペースをスタッシュ——エージェントを停止しつつ構成と会話内容は保持し、あとでクリック可能な2カラムポップアップから復元できる
- [Joxtacy/herdr-plugin-vault](https://github.com/Joxtacy/herdr-plugin-vault) — herdrのポップアップから過去のClaude Codeセッションを閲覧し、選んだものを新しいタブで再開する
- [leonho/herdr-idle-panes](https://github.com/leonho/herdr-idle-panes) — herdrプラグイン：アイドル状態のシェルのままになっているペインを確認して閉じる、チェックリスト形式のポップアップ
- [ram4-dev/herdr-notify-center](https://github.com/ram4-dev/herdr-notify-center) — サーバー全体のエージェント通知を、永続化されたポップアップ受信箱でHerdrに提供する
- [shoaibkhanz/herdr-active-agent-jump](https://github.com/shoaibkhanz/herdr-active-agent-jump) — herdrプラグイン：作業中/ブロック中のエージェントを、レイアウトの順序で前後に巡回してフォーカスする——attention-jumpを補完するvim風の操作
- [vgreg/herdr-padio](https://github.com/vgreg/herdr-padio) — herdrでフォーカスされているペインのアプリに応じて、PadIOコントローラーのモードを自動切り替えする
- [yojahny55/herdr-space-groups](https://github.com/yojahny55/herdr-space-groups) — herdrプラグイン：Spaceを名前付き・色分けされたグループにまとめる——ピッカーのポップアップ（マウス＋キーボード対応）、サイドバーのグループ見出し、自動並べ替えに対応

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-files"></a>

## ファイル閲覧・エディタ連携

> ペインの中でファイルツリーを開いたり、エディタ側と状態を揃えたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**terminal-code**](https://github.com/zenbu-labs/terminal-code)<br><sub>zenbu-labs</sub> | ターミナルの中で動くVS Code | `cli` `terminal` `vscode` `typescript` | 1870 | 🔄 2026-09-02 |
| [**herdr-file-viewer**](https://github.com/smarzban/herdr-file-viewer)<br><sub>smarzban</sub> | herdr向けのGit対応・読み取り専用ファイルビューア。マウス操作にも対応したキーボード駆動のTUIで、ツリー+コンテンツペインに差分表示・Markdownレンダリング・シンタックスハイライトを提供 | `file-viewer` `git` `ratatui` `rust` `terminal` | 523 | 🔄 2026-09-02 |
| [**herdr-sidebar**](https://github.com/alexarthurs/herdr-sidebar)<br><sub>alexarthurs</sub> | herdr向けのVS Code風サイドバー：ファイルエクスプローラーとGitのソース管理を1つのペインに統合——シンタックスハイライト付きプレビュー、VS Code風の差分表示、GitLens風の詳細パネル、AIによるコミットメッセージ生成 | `git` `ratatui` `rust` `sidebar` `terminal` | 268 | 🔄 2026-09-02 |
| [**🆕 ttt**](https://github.com/eugenioenko/ttt)<br><sub>eugenioenko</sub> | TTT Editor (Terminal Text Tool): A real alternative to VS Code, Zed, and Sublime that runs in your terminal. A TUI that feels like GUI. Single binary, zero con… | `cli` `code-editor` `developer-tools` `diff` `editor` | 217 | 🔄 2026-09-04 |
| [**herdr-mirror**](https://github.com/nikok6/herdr-mirror)<br><sub>nikok6</sub> | ローカルとリモートのセッションを1つのウィンドウに統合。リモートのherdrサーバーをローカルのサイドバーにミラーしてSSH経由で操作 | `rust` | 216 | 🔄 2026-08-29 |
| [**herdr-nvim**](https://github.com/ChmaraX/herdr-nvim)<br><sub>ChmaraX</sub> | Neovimをherdrのワークスペースに完全統合する | `lua` `neovim` `nvim` `nvim-plugin` `rust` | 130 | 🔄 2026-09-03 |
| [**dotfiles**](https://github.com/edmundmiller/dotfiles)<br><sub>edmundmiller</sub> | 自分のdotfilesを常に最新の状態に保つためのもの | `dotfiles` `emacs` `nix-dotfiles` `nixos` `nixos-configuration` | 80 | 🔄 2026-09-04 |
| [**herdr-lazygit**](https://github.com/Crokily/herdr-lazygit)<br><sub>Crokily</sub> | herdrのサイドバーペインでlazygitを実行し、AIによるコミットメッセージ生成にも対応——開くのも、展開するのも、コミットするのも、それぞれ1キーで | `git` `lazygit` `shell` | 28 | 2026-07-17 |
| [**herdr-yazi**](https://github.com/speardragon/herdr-yazi)<br><sub>speardragon</sub> | herdrのペイン内でYaziを開く | `shell` | 24 | 2026-08-19 |
| [**herdr-quicklook**](https://github.com/dwarvesf/herdr-quicklook)<br><sub>dwarvesf</sub> | herdr版Quick Look：クリップボード内のパスをオーバーレイでポップアップ表示し、1キーでファイルビューアに切り替えられる | `terminal` `shell` | 10 | 🔄 2026-08-26 |
| [**herdr-git-status**](https://github.com/ezcorp-org/herdr-git-status)<br><sub>ezcorp-org</sub> | herdrプラグイン：スペースごとのgitワーキングツリーの状態（ステージ済み/変更/未追跡/競合）をブランチ名の隣にサイドバー表示する | `rust` | 9 | 2026-08-10 |
| [**herdr-context.nvim**](https://github.com/makyinmars/herdr-context.nvim)<br><sub>makyinmars</sub> | Neovimからコードを選択またはカーソルを合わせ、稼働中のHerdrエージェントを選んで、構造化されたコンテキストをそのエージェントのプロンプトに（送信せずに）積み込む | `lua` | 8 | 🔄 2026-08-26 |
| [**herdr-workbench**](https://github.com/azizuysal/herdr-workbench)<br><sub>azizuysal</sub> | Herdr向けの洗練されたプロジェクトサイドバー——エクスプローラー、ファイル/コンテンツのリアルタイム検索、読み取り専用のソース管理、豊富なプレビュー、ファイルアイコン、Git装飾を備える | `rust` | 6 | 2026-08-07 |
| [**herdr-flist**](https://github.com/devskale/herdr-flist)<br><sub>devskale</sub> | herdr向けのファイル一覧プラグイン | `python` | 5 | 2026-07-10 |
| [**herdr-markdown-viewer**](https://github.com/arvindparmar-me/herdr-markdown-viewer)<br><sub>arvindparmar-me</sub> | Herdrプラグイン：Markdownファイルのパスをドラッグ選択してprefix+mを押すと、右側のスプリットペインでプレビューできる | `shell` | 4 | 2026-07-17 |
| [**herdr-fresh**](https://github.com/rvalledorjr/herdr-fresh)<br><sub>rvalledorjr</sub> | ターミナルIDEのFreshを、herdrのペイン内でファイルビューア兼エディタとして動かすherdrプラグイン | `developer-tools` `editor` `fresh` `ide` `terminal` | 4 | 2026-07-17 |
| [**herdr-plugin-mermaid-preview**](https://github.com/Volpestyle/herdr-plugin-mermaid-preview)<br><sub>Volpestyle</sub> | Herdr上でClaude CodeやCodexの出力中のMermaid図をリアルタイムプレビューする | `claude-code` `mermaid` `openai-codex` `terminal` `javascript` | 4 | 2026-07-10 |
| [**openloc.nvim**](https://github.com/Zamua/openloc.nvim)<br><sub>Zamua</sub> | すでにワークスペースに属しているNeovimでファイル参照を開く | `lua` | 4 | 🔄 2026-08-25 |
| [**herdr-wait**](https://github.com/cdc-lst/herdr-wait)<br><sub>cdc-lst</sub> | アイドル状態のエージェントペインに、実際に何をしているか（例：'waiting: build-api'、'waiting: codex'）をペインのプロセスツリーから判定してタグ付けする、設定可能なherdrプラグイン | `typescript` | 3 | 2026-07-03 |
| [**herdr-file-viewer**](https://github.com/ismaelosuna7824/herdr-file-viewer)<br><sub>ismaelosuna7824</sub> | 1つのHerdrペインに収まる、キーボード操作のファイルエクスプローラー・コードビューア・gitクライアント——Go + Bubble Tea製 | `bubbletea` `git` `golang` `tui` `go` | 3 | 2026-08-08 |
| [**herdr-lazygit**](https://github.com/JacquesvanWyk/herdr-lazygit)<br><sub>JacquesvanWyk</sub> | herdrのスプリットペインまたはタブでlazygitを開く。スマートトグル（開く/フォーカス/閉じる）に対応 | `lazygit` `shell` | 3 | 2026-07-12 |
| [**herdr-yazi-windows**](https://github.com/Only-Moon/herdr-yazi-windows)<br><sub>Only-Moon</sub> | herdr-yazi のWindows移植版。herdr v0.8以降のネイティブWindowsペイン生成に対応 | `file` `file-manager` `pidotdev` `python` `tui` | 3 | 2026-08-14 |
| [**herdr-x**](https://github.com/playsthisgame/herdr-x)<br><sub>playsthisgame</sub> | herdr内のターミナルスプリットでx.comを閲覧し、$EDITORで投稿を下書きして自分宛に送信できる | `cli` `terminal` `terminal-browser` `twitter` `shell` | 3 | 🔄 2026-08-20 |
| [**advanced-herdr-file-viewer**](https://github.com/thuanlm215/advanced-herdr-file-viewer)<br><sub>thuanlm215</sub> | Herdr向けのGit対応ファイルビューア——全文検索とファイル名検索（ワークスペースまたはフォルダ単位）、ワークスペースやペインを開くコンテキストアクション、Unicode/Nerdアイコン、独立スクロールするツリーに対応 | `file-viewer` `ripgrep` `rust` `tui` | 3 | 🔄 2026-09-04 |
| [**🆕 dotfiles**](https://github.com/tifandotme/dotfiles)<br><sub>tifandotme</sub> | ~/.*（ホームディレクトリ配下の設定ファイル） | `aerospace` `chezmoi` `cmux` `dotfiles` `ghostty` | 3 | 🔄 2026-09-03 |
| [**herdr-open-in-editor**](https://github.com/timofey-TK/herdr-open-in-editor)<br><sub>timofey-TK</sub> | ローカル・リモートのHerdrワークスペースをVS CodeまたはZedで開く | `vscode` `zed` `python` | 3 | 2026-07-30 |
| [**herdr-claude-usage-multi**](https://github.com/iamhouser/herdr-claude-usage-multi)<br><sub>iamhouser</sub> | Herdrのサイドバーに表示するClaudeプランの使用状況ゲージ——セッション/週の％、危険度に応じた色変化、リセットまでのカウントダウン、CLAUDE_CONFIG_DIRプロファイルによる複数アカウント対応 | `claude-code` `python` | 2 | 2026-07-25 |
| [**scp-explorer**](https://github.com/TinocoAI/scp-explorer)<br><sub>TinocoAI</sub> | MobaXterm風のSCPファイルエクスプローラーherdrプラグイン（macOS/Linux/Windowsクロスプラットフォーム対応） | `curses` `file-manager` `scp` `python` | 2 | 🔄 2026-09-03 |
| [**herdr-launcher-pane**](https://github.com/y-hirakaw/herdr-launcher-pane)<br><sub>y-hirakaw</sub> | herdr向けの、ドッキングされたクリック起動用ペイン——Finder/Explorer、VS Code、あるいはワークスペースごとに設定した任意のコマンドを起動できる | `launcher` `launcher-pane` `productivity` `python` | 2 | 2026-08-10 |
| [**herdr-flutter**](https://github.com/ablause/herdr-flutter)<br><sub>ablause</sub> | コーディングエージェントの隣で、稼働中のFlutterアプリを監視・ホットリロード・検査できるherdrサイドバー | `dart` | 1 | 2026-07-27 |
| [**herdr-cursor-open**](https://github.com/alex-devdone/herdr-cursor-open)<br><sub>alex-devdone</sub> | フォーカス中のherdrペインをCursorまたはVS Codeで開く——Remote-SSH経由のリモートherdrに接続したペインにも対応 | `cursor` `vscode` `shell` | 1 | 🔄 2026-08-23 |
| [**herdr-goto**](https://github.com/asumaran/herdr-goto)<br><sub>asumaran</sub> | herdrのリポジトリ・worktree・ペインを横断する、ツリー形式の切り替えツール | `go` | 1 | 🔄 2026-08-23 |
| [**herdr-file-viewer**](https://github.com/jomarmontuya/herdr-file-viewer)<br><sub>jomarmontuya</sub> | 右側に表示するHerdrのファイルツリープラグイン——ファイルタブ、作業ディレクトリの追従、git装飾、クリック可能なリンクに対応 | `go` | 1 | 2026-07-13 |
| [**herdr-yazi-explorer**](https://github.com/pjs-0457/herdr-yazi-explorer)<br><sub>pjs-0457</sub> | 呼び出したワークスペース内のherdrタブ/スプリットでYaziを開く（🗂 yaziというラベル付き）。終了すると自動的に再起動する | `yazi` `shell` | 1 | 2026-08-13 |
| [**herdr-terminal-file-manager**](https://github.com/robert-flo/herdr-terminal-file-manager)<br><sub>robert-flo</sub> | elioファイルマネージャーの薄いherdrラッパー。アクティブなディレクトリを検出してelioをネイティブに起動し、軽快なプレビュー・インライン画像表示・一括操作をherdrのペインにそのまま持ち込む | `shell` | 1 | 2026-07-10 |
| [**herdr-numbered-workspaces**](https://github.com/abrose/herdr-numbered-workspaces)<br><sub>abrose</sub> | herdrのサイドバーの各スペースの先頭に番号を付け、インデックス指定のswitch_workspaceショートカットと対応させる | `shell` | 0 | 2026-07-21 |
| [**herdr-preview**](https://github.com/AlexanderMakarov/herdr-preview)<br><sub>AlexanderMakarov</sub> | ホットキーで画面上に見えているファイル・フォルダのパスをハイライトし、file-viewer で開ける Herdr プラグインです。エージェント画面でもターミナルでも動作します。 | `rust` | 0 | 🔄 2026-08-29 |
| [**herdr_plugin**](https://github.com/Andreslvc/herdr_plugin)<br><sub>Andreslvc</sub> | herdrプラグイン：ペインのフォルダをVS Codeで開く、パスをコピーする、フォルダをspaceとして開く | `python` | 0 | 🔄 2026-08-24 |
| [**herdr-context**](https://github.com/Anthodev/herdr-context)<br><sub>Anthodev</sub> | herdr向けのプロジェクトコンテキストドック——git状態付きのファイルツリーとLLMの会話履歴を、常にエージェントのそばに表示する | `git` `jj` `ratatui` `rust` `sidebar` | 0 | 🔄 2026-08-31 |
| [**herdr-ctx**](https://github.com/aorumbayev/herdr-ctx)<br><sub>aorumbayev</sub> | herdrのサイドバーペイン向けの、Claudeコンテキストウィンドウ表示 | `typescript` | 0 | 2026-07-21 |
| [**Renderd**](https://github.com/Brutheron/Renderd)<br><sub>Brutheron</sub> | Herdr内で、完了したClaude CodeやCodexの応答をライブに読めるMarkdownリーダー | `go` | 0 | 2026-08-15 |
| [**herdr-sidebar-plugin**](https://github.com/caoool/herdr-sidebar-plugin)<br><sub>caoool</sub> | _(説明なし)_ | `typescript` | 0 | 🔄 2026-09-02 |
| [**herdr-sidebar-numbers**](https://github.com/cedrus-8864/herdr-sidebar-numbers)<br><sub>cedrus-8864</sub> | サイドバーにワークスペースとエージェントの位置番号を表示し、1〜9のショートカットキーと対応させるherdrプラグイン | `ai-agents` `bun` `sidebar` `terminal` `javascript` | 0 | 2026-08-04 |
| [**🆕 herdr-jetbrains**](https://github.com/chenyao0910/herdr-jetbrains)<br><sub>chenyao0910</sub> | アクティブなHerdrのワークスペースまたはworktreeを、Rider・WebStorm・IntelliJ IDEA・GoLandで開く | `developer-tools` `git-worktree` `goland` `intellij-idea` `jetbrains` | 0 | 🔄 2026-08-30 |
| [**herdr-codex-cost**](https://github.com/Coolsik/herdr-codex-cost)<br><sub>Coolsik</sub> | Herdrのサイドバーに、Codexセッションの推定コストを表示する | `codex` `shell` | 0 | 2026-07-31 |
| [**herdr-tab-badges**](https://github.com/CowboyVang/herdr-tab-badges)<br><sub>CowboyVang</sub> | 複数のタブを持つherdrのスペースに、サイドバーバッジを表示する | `shell` | 0 | 2026-07-21 |
| [**herdr-tab-git**](https://github.com/hasuwini77/herdr-tab-git)<br><sub>hasuwini77</sub> | Herdr Spacesのサイドバーに、最初のタブではなくアクティブなタブに追従する形でGitのブランチと状態を表示する | `git` `terminal` `tui` `javascript` | 0 | 🔄 2026-08-28 |
| [**herdr-plugin-mado**](https://github.com/hidekingerz/herdr-plugin-mado)<br><sub>hidekingerz</sub> | エージェントが書いたMarkdownを、それを書いているエージェントの隣でTUIビューアmadoを使って開くherdrプラグイン | `mado` `markdown` `tui` `shell` | 0 | 🔄 2026-09-02 |
| [**🆕 herdr-nvim**](https://github.com/jtnovellis/herdr-nvim)<br><sub>jtnovellis</sub> | Herdr の中で動く Neovim——タブごとの全高サイドバーと、コーディングエージェントとの本物のやり取りを実現します。見ているコードについて質問し、Neovim を離れずに回答を読み、エージェントが加えた編集を1つずつ確認できます。 | `ai-agents` `claude-code` `developer-tools` `lua` `neovim` | 0 | 🔄 2026-08-31 |
| [**herdr-plugin-agent-repo**](https://github.com/khatriafaz/herdr-plugin-agent-repo)<br><sub>khatriafaz</sub> | エージェント名・リポジトリ名・ブランチ名を、エージェントペインのヘッダーとサイドバーに表示するHerdrプラグイン | `javascript` | 0 | 2026-07-24 |
| [**🆕 herdr-nnn**](https://github.com/linuxing3/herdr-nnn)<br><sub>linuxing3</sub> | herdr内でnnnを開く | `shell` | 0 | 2026-08-04 |
| [**herdr-cmux-file-viewer**](https://github.com/linvald/herdr-cmux-file-viewer)<br><sub>linvald</sub> | cmuxのファイルビューアを、現在フォーカスしているherdrのスペースに同期させるherdrプラグイン | `python` | 0 | 2026-07-23 |
| [**herdr-openmd**](https://github.com/RufusLin/herdr-openmd)<br><sub>RufusLin</sub> | 選択したMarkdownをopenmdで開く——herdrから起動する、豊富な表現力を持つQt製プレビュー | `shell` | 0 | 2026-07-29 |
| [**herdr-git-detail**](https://github.com/sfroment/herdr-git-detail)<br><sub>sfroment</sub> | herdrプラグイン：詳細なgit状態（変更/ステージ/未追跡/進んでいる・遅れているコミット数/stash）を$git_detailというサイドバートークンとして表示する | `developer-tools` `git` `shell` `starship` `terminal` | 0 | 2026-08-05 |
| [**herdr-gitui**](https://github.com/Shi1xin/herdr-gitui)<br><sub>Shi1xin</sub> | サイドバーペインでgituiを動かすherdrプラグイン——開閉トグル、展開、ライト/ダークテーマに対応 | `gitui` `python` | 0 | 2026-07-28 |
| [**meadow**](https://github.com/Tetat-Chulchue/meadow)<br><sub>Tetat-Chulchue</sub> | herdrのターミナルマルチプレクサ向けの、マウス操作のファイルエクスプローラーペイン | `python` | 0 | 2026-07-21 |
| [**dotfiles**](https://github.com/Unique-Divine/dotfiles)<br><sub>Unique-Divine</sub> | Unique Divineのdotfilesと、その他の~（ホーム）配下の設定 | `dotfiles` `lua` `neovim` `neovim-dotfiles` `nvim` | 0 | 🔄 2026-08-31 |
| [**🆕 herdr-git-dirty**](https://github.com/viko16/herdr-git-dirty)<br><sub>viko16</sub> | 各 Space の未コミットの Git ファイル数を表示する、軽量な Herdr プラグインです。 | `git` `shell` | 0 | 🔄 2026-09-02 |
| [**herdr-cmux-cwd-sync**](https://github.com/WerrySs/herdr-cmux-cwd-sync)<br><sub>WerrySs</sub> | フォーカス中のHerdRペインに対して、干渉しない形でcmuxのファイルエクスプローラーを同期する | `cmux` `macos` `python` | 0 | 2026-08-14 |

<details><summary>この目的にも関係するもの</summary>

- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) — herdr向けのコードレビュー＋ファイルビューアのサイドバー。エージェントの差分にコメントして差し戻せる。PRとそのチェック・コメントの読み取り専用表示も付属
- [ChmaraX/herdr-gitview](https://github.com/ChmaraX/herdr-gitview) — herdr向けのGitステータス/差分パネル——変更のレビュー、nvimでの編集、ステージ/コミット/破棄をすべてターミナルから行える
- [vonzelle-vzt/herdr-extensions](https://github.com/vonzelle-vzt/herdr-extensions) — herdr向けの小さなVS Code——LSPによる診断・自動補完・リネーム・定義へジャンプに対応した本格エディタに加え、ソース管理・検索・問題一覧・テスト・デバッガ・アプリのライブプレビュー・実行時エラー捕捉・画像貼…
- [jsmenzies/mergr](https://github.com/jsmenzies/mergr) — Herdr Spaceのサイドバー行にGitHubプルリクエストの状態を表示する
- [maedana/herdr-whereami](https://github.com/maedana/herdr-whereami) — 今どこにいるかを示すよう、タブを自動でリネームするHerdrプラグイン——gitリポジトリ内なら「リポジトリ名/ブランチ名」のように表示
- [bayoudhi/herdr-prayer-times](https://github.com/bayoudhi/herdr-prayer-times) — 次の礼拝時刻とカウントダウンをHerdrのサイドバーに表示——タイムテーブルのポップアップと通知付き
- [brianh20/herdr-stagr](https://github.com/brianh20/herdr-stagr) — herdr向けのソース管理サイドバー——並列差分表示でステージ・アンステージ・破棄ができる
- [ctbaum/herdr-deck](https://github.com/ctbaum/herdr-deck) — herdr-agents.nvimと組み合わせて使うワークスペースランチャー：Neovim・エージェント・シェル・lazygitがあらかじめ用意された「デッキ」で、ClaudeやCodexを開始または再開できる
- [ZingerLittleBee/herdr-agent-pins](https://github.com/ZingerLittleBee/herdr-agent-pins) — Herdrのエージェントセッションを、Agentsサイドバーの最上部に永続的にピン留めする
- [caner-akca/herdr-plugin-atomic-workflows](https://github.com/caner-akca/herdr-plugin-atomic-workflows) — herdrプラグイン：隔離されたAtomicワークフロータスクを起動・監視する——キャンペーンボード、サイドバートークン、実行台帳、オプションのTelegramコックピットを備える
- [Gareth-Rouse/herdr-plugin-session-pruner](https://github.com/Gareth-Rouse/herdr-plugin-session-pruner) — herdrプラグイン：ワークスペースの最終使用日時を記録してSpacesのサイドバーに経過時間を表示し、使われていないワークスペースをセッション復元の対象から外す
- [jovylle/herdr-session-title-name](https://github.com/jovylle/herdr-session-title-name) — herdrプラグイン：terminal_title_strippedをタブに永続化する（session_titleだけを上に残し、閉じた後もタブがそれを保持する）
- [limars874/herdr-pane-id-metadata](https://github.com/limars874/herdr-pane-id-metadata) — 正規化されたペインIDと、コンパクトなタブ/ペインのサイドバーメタデータのための、最小構成のHerdrプラグイン
- [NachoPal/herdr-pane-agent-unread](https://github.com/NachoPal/herdr-pane-agent-unread) — herdr向けの、ペインごとの「未読」通知＋サイドバーバッジ——見ていないペインで完了または入力待ちになったエージェントを浮かび上がらせる（herdrは「既読」をタブ単位で管理し、ペイン単位では管理しないため）
- [ubuntudroid/herdr-git-stack](https://github.com/ubuntudroid/herdr-git-stack) — herdrプラグイン：各spaceのgitブランチスタック内での位置をspacesサイドバーに表示し、親ブランチが移動したブランチにフラグを立て、スタックを連続した状態に保つ。ローカルのコミットグラフのみを使用——ネッ…
- [yojahny55/herdr-space-groups](https://github.com/yojahny55/herdr-space-groups) — herdrプラグイン：Spaceを名前付き・色分けされたグループにまとめる——ピッカーのポップアップ（マウス＋キーボード対応）、サイドバーのグループ見出し、自動並べ替えに対応

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-cost"></a>

## トークン・コスト管理

> エージェントがいくら使っているかを見たい / 使用量を削りたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**memex**](https://github.com/nicosuave/memex)<br><sub>nicosuave</sub> | Claude Code・Codex・Pi・OpenCode・GitHub Copilot・Cursorのトランスクリプトを検索。セッションを再開。トークンを記録 | `bm25` `claude-code` `codex-cli` `hybrid-search` `rag` | 185 | 🔄 2026-09-02 |
| [**llmtrim-herdr**](https://github.com/fkiene/llmtrim-herdr)<br><sub>fkiene</sub> | herdrのトークン代を節約：各エージェントペインのリクエストを圧縮（実測で入力-31%/出力-74%）し、節約額をペインごとのバッジで表示 | `llm-proxy` `llmtrim` `powershell` | 44 | 2026-07-02 |
| [**herdr-agent-usage**](https://github.com/senna-lang/herdr-agent-usage)<br><sub>senna-lang</sub> | Herdrで動作するエージェントのコンテキスト使用量メーターと、プロバイダーのレート制限を表示する | `ai-agents` `claude-code` `codex` `golang` `rate-limiting` | 28 | 🔄 2026-09-03 |
| [**herdr-token-dashboard**](https://github.com/Davidcreador/herdr-token-dashboard)<br><sub>Davidcreador</sub> | Herdrのエージェントペイン向けの、トークン消費量をリアルタイムに表示するダッシュボードと通知 | `ai-agents` `bubbletea` `opencode` `pi-agent` `token-dashboard` | 18 | 2026-08-13 |
| [**herdr-claude-usage**](https://github.com/alejodelosrios/herdr-claude-usage)<br><sub>alejodelosrios</sub> | 使用量を確認するためだけにClaudeのセッションを開く必要はもうない。Claudeプランの使用状況（セッション％｜週％）を常にHerdrのサイドバーに表示し、そのアカウントの全ワークスペースで共有される。Claude Code自身の認証情報を使い/statusと同じ正確な数値を表示——推定値ではなく、追加ログインも… | `claude` `claude-code` `python` | 3 | 2026-07-21 |
| [**herdr-opentab**](https://github.com/hamidi-dev/herdr-opentab)<br><sub>hamidi-dev</sub> | OpenTabによる、エージェントごとのAI利用料をHerdrのサイドバーにリアルタイム表示する | `ai-agents` `opentab` `terminal` `python` | 3 | 2026-08-18 |
| [**herdr-gekiatsu-plugin**](https://github.com/yuuta1219/herdr-gekiatsu-plugin)<br><sub>yuuta1219</sub> | herdrプラグイン：Claude Codeの使用量カウンターを、パチスロ風にしたもの。大当たり確率1/99、毎日10:00 JSTにリセット | `claude` `claude-code` `python` `tui` | 3 | 2026-08-17 |
| [**herdr-api-credit-bar**](https://github.com/CristianPeralta/herdr-api-credit-bar)<br><sub>CristianPeralta</sub> | herdrプラグイン：従量課金制APIプロバイダーの残クレジットを表示する。まずはAlibaba Cloud Model Studioに対応 | `shell` | 2 | 2026-08-18 |
| [**herdr-quota**](https://github.com/kvkenyon/herdr-quota)<br><sub>kvkenyon</sub> | Herdr上で、Claude・Codex・Cursor・Kimiのサブスクリプション枠を一目で確認できる | `ai-tools` `claude-code` `cursor` `developer-tools` `kimi` | 2 | 🔄 2026-09-04 |
| [**herdr-whereami**](https://github.com/maedana/herdr-whereami)<br><sub>maedana</sub> | 今どこにいるかを示すよう、タブを自動でリネームするHerdrプラグイン——gitリポジトリ内なら「リポジトリ名/ブランチ名」のように表示 | `rust` | 2 | 2026-08-14 |
| [**scopefuel**](https://github.com/mgh3326/scopefuel)<br><sub>mgh3326</sub> | AIコーディングエージェントのプラン向けの、範囲を意識した残量ゲージ——実際に何（アカウント/モデル/グループ）がブロックされているか、いつ回復するかが分かる | `ai-agents` `antigravity` `claude-code` `cli` `codex` | 1 | 🔄 2026-09-02 |
| [**herdr-model-lanes**](https://github.com/terry-li-hm/herdr-model-lanes)<br><sub>terry-li-hm</sub> | herdrプラグイン：Codex・Claude Max・Grokのクォータをワークスペース行に表示し、新規エージェント向けにクォータを考慮したモデルクラスのレーン（ag）も提供する | `claude` `codex` `grok` `model-routing` `quota` | 1 | 🔄 2026-08-30 |
| [**herdr-usage**](https://github.com/Efeguclu1/herdr-usage)<br><sub>Efeguclu1</sub> | Claude・Codex・Cursor・OpenCode・Pi向けの、Herdrエージェントタブ上のコンパクトなアカウント使用量表示 | `claude-code` `cursor` `openai` `opencode` `python` | 0 | 🔄 2026-08-22 |
| [**herdr-web-broker**](https://github.com/JefeLabs/herdr-web-broker)<br><sub>JefeLabs</sub> | herdr向けの自己ホスト型REST/WS API——どこからでもコーディングエージェントを起動・操作できる。トークン、マルチユーザーのセッション所有権、gitコマンド、イベントストリーミング、親子間フェデレーションに対応。TypeScript SDK＋Reactパッケージ付き | `typescript` | 0 | 🔄 2026-09-01 |
| [**herdr-plugin-agent-quota**](https://github.com/kwanwooi25/herdr-plugin-agent-quota)<br><sub>kwanwooi25</sub> | Herdr向けのエージェントクォータ——Claude Code・Codex・Grok向けのトークン＆コストダッシュボード、サイドバーのクォータゲージ、タブバーのサマリーを提供 | `javascript` | 0 | 🔄 2026-08-30 |
| [**🆕 precc-herdr-plugin**](https://github.com/peria-ai/precc-herdr-plugin)<br><sub>peria-ai</sub> | herdr 用の PRECC プラグイン。エージェント横断でのトークン節約状況を計測し、PRECC のセットアップをワンタッチで行えます。 | `claude-code` `precc` `shell` | 0 | 🔄 2026-09-02 |
| [**🆕 provider-usage**](https://github.com/ryus1234/provider-usage)<br><sub>ryus1234</sub> | Herdr 用の、プロバイダーの使用量とクォータを表示するバーです。 | `ai-usage` `quota-monitor` `rust` | 0 | 🔄 2026-08-31 |
| [**herdr-burn**](https://github.com/samuelbaldwin05/herdr-burn)<br><sub>samuelbaldwin05</sub> | herdrのサイドバーに、ペインごとのClaude Codeのコスト/割当量をリアルタイム表示し、ワークスペース合計の消費量オーバーレイも提供する | `python` | 0 | 2026-08-12 |
| [**herdr-model-capacity**](https://github.com/shrivatsas/herdr-model-capacity)<br><sub>shrivatsas</sub> | アカウント単位のClaude・Codex/OpenAI・OpenRouterの利用可能量を表示するHerdrペイン | `claude` `codex` `openrouter` `rust` | 0 | 🔄 2026-08-28 |
| [**herdr-usage-bar**](https://github.com/silverwolfdoc/herdr-usage-bar)<br><sub>silverwolfdoc</sub> | Herdr内のAIエージェント向けの使用量上限とコンテキストメーターを、コンパクトな下部の使用量バーで表示する | `go` | 0 | 🔄 2026-08-27 |
| [**herdr-status-ui-bar**](https://github.com/speardragon/herdr-status-ui-bar)<br><sub>speardragon</sub> | herdrのタブバーに、AIエージェントのプラン使用量ゲージ（Claude Code / Codex / Grok）を表示する | `claude-code` `shell` | 0 | 🔄 2026-08-28 |
| [**herdr-context-display**](https://github.com/TheBrunoPetkovic/herdr-context-display)<br><sub>TheBrunoPetkovic</sub> | herdr内の各Claude Codeエージェント行に、コンテキストウィンドウの使用量を色分けして表示する | `claude-code` `terminal` `typescript` | 0 | 🔄 2026-08-26 |
| [**pi-agent-usage**](https://github.com/w784415/pi-agent-usage)<br><sub>w784415</sub> | OpenAI Codexのクォータとリセット時刻を表示するPi拡張機能。Herdrプラグインにも対応 | `openai-codex` `pi-extension` `pi-package` `quota` `typescript` | 0 | 🔄 2026-08-26 |
| [**claude-usage**](https://github.com/yuuta1219/claude-usage)<br><sub>yuuta1219</sub> | herdrプラグイン：Claude Codeの使用率（セッション%/週%）をサイドバー下部に常時表示する | `claude` `claude-code` `python` `tui` | 0 | 2026-08-01 |

<details><summary>この目的にも関係するもの</summary>

- [levi-qiao/herdr-agent-quota](https://github.com/levi-qiao/herdr-agent-quota) — Herdr 向けの、認証情報単位でスコープされた AI クォータ・コンテキスト・キャッシュ表示——Claude・Codex・Grok・Agy・OpenCode・Pi・OMP に対応
- [caner-akca/herdr-plugin-atomic-workflows](https://github.com/caner-akca/herdr-plugin-atomic-workflows) — herdrプラグイン：隔離されたAtomicワークフロータスクを起動・監視する——キャンペーンボード、サイドバートークン、実行台帳、オプションのTelegramコックピットを備える
- [Coolsik/herdr-codex-cost](https://github.com/Coolsik/herdr-codex-cost) — Herdrのサイドバーに、Codexセッションの推定コストを表示する

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-monitor"></a>

## 監視・ダッシュボード

> エージェントやマシンの状態を一覧で眺めたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**clauth**](https://github.com/uwuclxdy/clauth)<br><sub>uwuclxdy</sub> | Claude Codeのマルチアカウント管理・使用量モニター（CLI・TUI・MCPによるクロスアカウント委任に対応） | `account-manager` `account-switcher` `anthropic` `claude` `claude-code` | 96 | 🔄 2026-09-03 |
| [**herdr-agent-quota**](https://github.com/levi-qiao/herdr-agent-quota)<br><sub>levi-qiao</sub> | Herdr 向けの、認証情報単位でスコープされた AI クォータ・コンテキスト・キャッシュ表示——Claude・Codex・Grok・Agy・OpenCode・Pi・OMP に対応 | `agent-usage` `agy` `ai-agents` `antigravity` `claude-code` | 56 | 🔄 2026-09-04 |
| [**herdr-beads**](https://github.com/miiraheart/herdr-beads)<br><sub>miiraheart</sub> | herdr向けのbeads (bd) タスクボード：bdのissueをリスト・テーブル・カンバンで表示し、サイドバーまたはフローティングで表示できる | `bd` `beads` `kanban` `rust` `tui` | 17 | 🔄 2026-08-25 |
| [**herdr-pc-ram-and-cpu-usage-overlay**](https://github.com/ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay)<br><sub>ezcorp-org</sub> | herdrプラグイン：スペース（ワークスペース）ごとのCPU/RAM使用率を、マシン全体に対する割合としてリアルタイム表示 | `rust` | 15 | 🔄 2026-08-27 |
| [**herdr-telemetry**](https://github.com/DIodide/herdr-telemetry)<br><sub>DIodide</sub> | ワークスペースとエージェントのテレメトリを自分で管理するエンドポイントにストリーミングするHerdrプラグイン——Go製の単一バイナリ、プライバシー重視のデフォルト設定 | `golang` `telemetry` `go` | 12 | 2026-07-10 |
| [**herdr-f1**](https://github.com/hmu332233/herdr-f1)<br><sub>hmu332233</sub> | Herdrのエージェント向けの、F1風ダッシュボード | `agent-dashboard` `typescript` | 12 | 2026-08-13 |
| [**herdres**](https://github.com/luminexord/herdres)<br><sub>luminexord</sub> | Tendwireを利用した、Herdrのコーディングエージェントを監視・メッセージ送信できるTelegramインターフェース | `coding-agents` `telegram` `python` | 10 | 2026-08-09 |
| [**shepherd**](https://github.com/ryonakae/shepherd)<br><sub>ryonakae</sub> | Herdr管理下のコーディングエージェント向けの、ワーカー監視デーモンとランタイムブリッジ | `pi-coding-agent` `pi-extension` `typescript` | 8 | 🔄 2026-08-28 |
| [**herdr-sysmon**](https://github.com/getpipher/herdr-sysmon)<br><sub>getpipher</sub> | Herdrのサイドバーにシステムメトリクスを表示——CPU・メモリ・バッテリー・ネットワーク・ディスク・時計。tmux-cpu/tmux-battery/tmux-online-statusのステータスバーを、Herdrのワークスペーストークンに忠実に移植したもの。macOS優先対応 | `battery` `catppuccin` `cpu` `getpipher` `macos` | 7 | 2026-07-26 |
| [**herdr-workboard**](https://github.com/Phoobobo/herdr-workboard)<br><sub>Phoobobo</sub> | herdr向けのカンバン式ワークボードTUI：ボード＝ワークスペース、タスクの状態＝タブ、タスクのセッション＝ペインという構造 | `kanban` `tui` `typescript` | 7 | 2026-08-10 |
| [**herdr-tally**](https://github.com/jasonrr/herdr-tally)<br><sub>jasonrr</sub> | あなたとエージェントのための、プロジェクト単位のTodoとスクラッチパッド<br>📝 プロジェクト単位の TODO 管理 | `rust` `todo` | 6 | 🔄 2026-08-30 |
| [**herdr-devserver-status**](https://github.com/Razz21/herdr-devserver-status)<br><sub>Razz21</sub> | プラグイン可能な仕様に基づいてペイン内のdevサーバーを検出し、ライフサイクルの状態を報告するHerdrプラグイン | `astro` `cli` `deamon` `dev-server` `extensible` | 6 | 🔄 2026-08-25 |
| [**herdr-lazydocker**](https://github.com/sudoeren/herdr-lazydocker)<br><sub>sudoeren</sub> | herdrのスプリットペインまたは専用タブでlazydockerを実行する | `docker` `lazydocker` `shell` | 6 | 🔄 2026-08-27 |
| [**herdr-kanban**](https://github.com/KokiKono/herdr-kanban)<br><sub>KokiKono</sub> | タスクをherdrのタブに紐付けるターミナル上のカンバンボード。SQLiteに保存される | `rust` | 5 | 2026-07-10 |
| [**herdr-agent-watcher**](https://github.com/winoooops/herdr-agent-watcher)<br><sub>winoooops</sub> | Herdr向けのコーディングエージェント可観測性——ライブなサイドバーカード、ライフサイクル通知、設定不要のClaude Codeメトリクスブリッジを提供する | `claude-code` `rust` | 5 | 🔄 2026-08-31 |
| [**herdr-shell-progress**](https://github.com/bayoudhi/herdr-shell-progress)<br><sub>bayoudhi</sub> | herdrプラグイン：コーディングエージェントに限らず、時間のかかるシェルコマンドの進行状況もサイドバーにリアルタイム表示する | `rust` | 4 | 🔄 2026-09-02 |
| [**🆕 herdr-codex-bridge**](https://github.com/ardasevinc/herdr-codex-bridge)<br><sub>ardasevinc</sub> | 一元化されたアプリサーバーを使い、Codex セッションに Herdr ネイティブのペイン識別情報を割り当てます。 | `ai-agents` `codex` `terminal` `go` | 3 | 🔄 2026-09-01 |
| [**herdr-mise**](https://github.com/funsaized/herdr-mise)<br><sub>funsaized</sub> | プロンプトではなく「一手」を回す🧑‍🍳 herdr内のエージェント向けビジュアライザー | `agent` `agent-monitoring` `ai-agents` `cli-tool` `developer-tools` | 3 | 🔄 2026-09-03 |
| [**adlc-herdr**](https://github.com/voodootikigod/adlc-herdr)<br><sub>voodootikigod</sub> | ADLC向けのherdrプラグイン——ペインごとのフェーズ/チケット/ゲートの状態、バックログボード、ゲートアクション、adlc-fleetの実行状況の可視化に対応。voodootikigod/adlc/plugins/adlc-herdrの自動同期ミラー | `javascript` | 3 | 🔄 2026-08-31 |
| [**herdr-agent-dashboard**](https://github.com/carsonjones/herdr-agent-dashboard)<br><sub>carsonjones</sub> | prefix+aでherdrのエージェント一覧を表示する | `typescript` | 2 | 2026-07-16 |
| [**herdr-telemetry-bridge**](https://github.com/CodyBontecou/herdr-telemetry-bridge)<br><sub>CodyBontecou</sub> | ローカルのワークスペース・リポジトリ・コーディングエージェント・モデル・トレースのテレメトリを外部クライアントにストリーミングするHerdrプラグイン | `coding-agents` `telemetry` `time-md` `javascript` | 2 | 2026-06-26 |
| [**herdr-agentsview**](https://github.com/cpcloud/herdr-agentsview)<br><sub>cpcloud</sub> | AgentsViewのアクティビティを、1つの非常に賑やかなターミナルに凝縮して表示する | `rust` | 2 | 🔄 2026-08-24 |
| [**herdr-statusline**](https://github.com/iiii1224/herdr-statusline)<br><sub>iiii1224</sub> | herdrセッション向けのカスタマイズ可能なステータスライン | `cli` `statusbar` `statusline` `tmux` `python` | 2 | 2026-08-15 |
| [**shepherd**](https://github.com/jwarykowski/shepherd)<br><sub>jwarykowski</sub> | あなたのTodoを群れとしてまとめる | `cli` `developer-tools` `go-lang` `productivity` `task-management` | 2 | 🔄 2026-08-21 |
| [**herdr-jira-board**](https://github.com/kiitosu/herdr-jira-board)<br><sub>kiitosu</sub> | herdr内で動くJiraカンバンボード。Claude Codeセッションランチャー付き | `python` | 2 | 🔄 2026-09-02 |
| [**herdr-portal**](https://github.com/loofare/herdr-portal)<br><sub>loofare</sub> | herdr向けのミッションコントロールダッシュボード——全ワークスペース/タブ/ペインのエージェントを、ライブTUIカンバン（キーボード＋マウス対応）とWeb大画面表示に集約する。構造化された進捗表示、Ctrl+B Aで起動、クリックでジャンプ、ブラウザからエージェントに返信可能 | `agent-dashboard` `agent-monitor` `ai-agents` `claude-code` `codex` | 2 | 🔄 2026-08-20 |
| [**herdr-cache-ttl**](https://github.com/nytafar/herdr-cache-ttl)<br><sub>nytafar</sub> | herdrプラグイン：エージェントのペインごとに、プロンプトキャッシュのTTLをリアルタイムでカウントダウン表示する | `rust` | 2 | 2026-08-05 |
| [**herdr-slurm**](https://github.com/quan-meng/herdr-slurm)<br><sub>quan-meng</sub> | Slurmのアロケーション向けに、Herdrのワークスペースと監視付きエージェントタブを作成する | `hpc` `slurm` `terminal-multiplexer` `python` | 2 | 2026-08-13 |
| [**herdr-tilt**](https://github.com/the-inconvenience-store/herdr-tilt)<br><sub>the-inconvenience-store</sub> | Herdr向けの、キーボード操作対応Tiltダッシュボード | `k8s` `kubernetes` `tilt` `rust` | 2 | 🔄 2026-08-24 |
| [**herdr-agent-state**](https://github.com/Tyru5/herdr-agent-state)<br><sub>Tyru5</sub> | herdr向けのリアルタイムエージェント状態ペイン——ワークスペース内の各エージェントが何をしているかを、より人間に読みやすい形式で表示する | `claude-code` `rust` `terminal` | 2 | 2026-08-05 |
| [**herdr-memex-analytics**](https://github.com/vishnutskumar/herdr-memex-analytics)<br><sub>vishnutskumar</sub> | herdrプラグイン：memexの履歴を活用した、セッション効率の分析とリアルタイムなエージェントガイダンス | `rust` | 2 | 🔄 2026-09-01 |
| [**herdr-cache-timer**](https://github.com/ArteenHD/herdr-cache-timer)<br><sub>ArteenHD</sub> | 各エージェントのプロンプトキャッシュがいつ失効するかを、Herdrのサイドバーに直接表示する | `claude-code` `prompt-caching` `terminal` `javascript` | 1 | 2026-08-08 |
| [**herdr-glance**](https://github.com/arvmaan/herdr-glance)<br><sub>arvmaan</sub> | エージェントの状態を確認できる、デスクトップウィジェット | `rust` | 1 | 🔄 2026-08-26 |
| [**herdr-tokscale-dashboard**](https://github.com/astkaasa/herdr-tokscale-dashboard)<br><sub>astkaasa</sub> | TokscaleをローカルのHerdrダッシュボードペインとして開く | `dashboard` `tokscale` `shell` | 1 | 2026-06-26 |
| [**herdr-plugin-codex-subs**](https://github.com/benkraus/herdr-plugin-codex-subs)<br><sub>benkraus</sub> | CLIProxyAPIのCodexサブスクリプション枠とリセットクレジットを表示するHerdrダッシュボード | `go` | 1 | 2026-07-30 |
| [**🆕 tsk**](https://github.com/chrisg32/tsk)<br><sub>chrisg32</sub> | tsk——TaskPaper/PlainTasks 風のプレーンテキストタスク管理 TUI で、Rust で書かれています。単体でも herdr プラグインとしても動作します。 | `rust` `taskpaper` `todo` `tui` | 1 | 🔄 2026-09-03 |
| [**herdr-spinner**](https://github.com/hasuwini77/herdr-spinner)<br><sub>hasuwini77</sub> | 作業中状態のHerdrペインに、表示専用のペインメタデータ経由でアニメーションする点字スピナーを表示する | `spinner` `terminal` `tui` `javascript` | 1 | 🔄 2026-08-27 |
| [**🆕 herdr-overview**](https://github.com/iamgp/herdr-overview)<br><sub>iamgp</sub> | Herdr向けのMission Control / Exposé——全spaceをタイル状に並べたライブ一覧 | `terminal` `tui` `javascript` | 1 | 🔄 2026-08-28 |
| [**herdr-compose**](https://github.com/mattyan1053/herdr-compose)<br><sub>mattyan1053</sub> | docker compose向けのHerdrプラグイン | `terminal` `tui` `shell` | 1 | 2026-07-24 |
| [**herdr-pulse**](https://github.com/moneycaringcoder/herdr-pulse)<br><sub>moneycaringcoder</sub> | herdr向けの、ワークスペースごとのエージェント活動履歴——サイドバーのスパークラインとして表示する | `monitoring` `rust` `sparkline` `terminal` | 1 | 🔄 2026-09-01 |
| [**herdr-ports**](https://github.com/Numbered-com/herdr-ports)<br><sub>Numbered-com</sub> | herdrで稼働中の開発サーバーを可視化：TCPリスナーが1つ以上動いているすべてのスペースに$portsバッジを表示する | `pids` `ports` `shell` | 1 | 2026-07-23 |
| [**🆕 omarchy-herd**](https://github.com/parker-brown-family/omarchy-herd)<br><sub>parker-brown-family</sub> | herdr 配下のどのコーディングエージェントがあなたを必要としているかを、Omarchy バーに表示します。 | `hyprland` `omarchy` `quickshell` `shell` | 1 | 🔄 2026-09-03 |
| [**herdr-readpending**](https://github.com/rcosteira79/herdr-readpending)<br><sub>rcosteira79</sub> | まだ読み終えていないエージェントにマークを付ける。番号付きバッジ（$read）＋並べ替え可能なリストペインを提供。そのエージェントにフォーカスすると自動でクリアされる | `python` | 1 | 🔄 2026-08-24 |
| [**herdr-agent-metrics**](https://github.com/szrenwei/herdr-agent-metrics)<br><sub>szrenwei</sub> | Claude Code・Codex・TraeX向けの、軽量なHerdrコンテキスト・セッション使用量メトリクス | `claude-code` `openai-codex` `traex` `python` | 1 | 2026-08-04 |
| [**herdr-space-tab-metadata**](https://github.com/szrenwei/herdr-space-tab-metadata)<br><sub>szrenwei</sub> | 各Herdr Spaceのアクティブなタブをサイドバーに表示する | `terminal-ui` `python` | 1 | 2026-08-04 |
| [**taskherd**](https://github.com/ukwhatn/taskherd)<br><sub>ukwhatn</sub> | herdrのエージェントセッション・PR・Jiraチケットに連携したタスクボード | `claude-code` `kanban` `task-management` `tui` `go` | 1 | 🔄 2026-09-01 |
| [**🆕 herdr-activity-age**](https://github.com/1Morganmore/herdr-activity-age)<br><sub>1Morganmore</sub> | 各エージェントの最終状態変化からの経過時間を表示する、Windows版Herdrプラグイン | `powershell` `windows` | 0 | 🔄 2026-08-30 |
| [**herdr-docker**](https://github.com/abcxff/herdr-docker)<br><sub>abcxff</sub> | herdrでエージェントを追跡するのと同じように、dockerのビルドも追跡する | `docker` `javascript` | 0 | 2026-08-12 |
| [**🆕 herdr-claude-usage**](https://github.com/anyaachan/herdr-claude-usage)<br><sub>anyaachan</sub> | Herdr でグローバルな Claude Code プランの使用状況を確認できます。タブバーでの要約表示とポップアップダッシュボードを備え、statusLine を利用してマルチアカウントにも対応します。 | `claude` `claude-code` `cli` `terminal` `shell` | 0 | 🔄 2026-09-01 |
| [**herdr-ios-build-status-plugin**](https://github.com/atomsbaza/herdr-ios-build-status-plugin)<br><sub>atomsbaza</sub> | オンデマンドで確認できる、HerdrのiOSビルド＋テスト状況ペイン。失敗時のスクリーンショット付き | `shell` | 0 | 2026-08-06 |
| [**herdr-nodejs-center**](https://github.com/AZenking/herdr-nodejs-center)<br><sub>AZenking</sub> | ローカルのNode.js・Bun・Denoサービスを監視し、フォーカスできるHerdrのポップアップ | `developer-tools` `nodejs` `javascript` | 0 | 2026-08-20 |
| [**🆕 herdr-plugin-atomic-workflows**](https://github.com/caner-akca/herdr-plugin-atomic-workflows)<br><sub>caner-akca</sub> | herdrプラグイン：隔離されたAtomicワークフロータスクを起動・監視する——キャンペーンボード、サイドバートークン、実行台帳、オプションのTelegramコックピットを備える | `javascript` | 0 | 🔄 2026-09-01 |
| [**herdr-jcode-integration**](https://github.com/capt-marbles/herdr-jcode-integration)<br><sub>capt-marbles</sub> | Jcodeのライフサイクル状態とセッションレポーティングのためのHerdrプラグイン | `jcode` `shell` | 0 | 2026-08-09 |
| [**herdr-dev-servers**](https://github.com/carellano/herdr-dev-servers)<br><sub>carellano</sub> | Herdrのペインで動作している開発サーバーを検出し、安全に管理する | `developer-tools` `go` `terminal` | 0 | 2026-08-12 |
| [**herdr-agent-metadata**](https://github.com/choplin/herdr-agent-metadata)<br><sub>choplin</sub> | 各Herdrエージェントの意味的な状態が最後に変化したのがいつかを表示する | `go` | 0 | 🔄 2026-08-26 |
| [**herdr-repository-identity**](https://github.com/choplin/herdr-repository-identity)<br><sub>choplin</sub> | 各Herdrワークスペースが共有するGitリポジトリの識別情報を報告する | `go` | 0 | 🔄 2026-08-24 |
| [**🆕 herdr-claude-lifecycle**](https://github.com/daocoding/herdr-claude-lifecycle)<br><sub>daocoding</sub> | herdr + Omarchy 向けの、フックを軸にした Claude Code のライフサイクル管理。Claude 自身のフックから working/blocked/idle の状態を取得し、Claude Code のアップデートのたびに動作を検証します。 | `claude-code` `omarchy` `python` | 0 | 🔄 2026-09-02 |
| [**herdr-process-guard**](https://github.com/Efeguclu1/herdr-process-guard)<br><sub>Efeguclu1</sub> | コーディングエージェントが起動しっぱなしにしたdevサーバーの内容を説明し、安全に停止する | `claude-code` `codex` `coding-agents` `cursor` `macos` | 0 | 🔄 2026-08-24 |
| [**herdr-vitals**](https://github.com/ericcparsons/herdr-vitals)<br><sub>ericcparsons</sub> | macOS向けherdrプラグイン——サイドバーにエージェントごとのCPU/RAM使用率とスペースごとの稼働中devサーバーポートを表示し、ポップアップから終了操作もできる | `bun` `developer-tools` `terminal` `typescript` | 0 | 2026-07-29 |
| [**🆕 subherd**](https://github.com/HalloSouf/subherd)<br><sub>HalloSouf</sub> | すべての Claude Code サブエージェントが何をしているかを、そのセッションが動いているワークスペースごとにまとめて表示する herdr プラグインです。 | `claude-code` `tui` `go` | 0 | 🔄 2026-09-03 |
| [**herdr-kanban**](https://github.com/hassox/herdr-kanban)<br><sub>hassox</sub> | ワークスペースのペインをカンバンボードとして表示する | `go` | 0 | 🔄 2026-08-21 |
| [**herdr-ports**](https://github.com/ivorpad/herdr-ports)<br><sub>ivorpad</sub> | herdrプラグイン：待受中のポートを一覧表示し、それぞれの背後にあるプロジェクト名を示し、終了または開くことができるポップアップ | `tui` `python` | 0 | 🔄 2026-08-27 |
| [**herdr-reap**](https://github.com/ivorpad/herdr-reap)<br><sub>ivorpad</sub> | herdrプラグイン：全エージェントのライフサイクル状態を表示し、1キーで完了済みのものをまとめて閉じる | `tui` `python` | 0 | 🔄 2026-08-27 |
| [**herdr-metrics**](https://github.com/jordanhawkes/herdr-metrics)<br><sub>jordanhawkes</sub> | Claude Code・Codex・TraeX向けの、コンテキスト・セッショントークン・アカウント上限のメトリクスをHerdrのサイドバーに表示する。szrenwei/herdr-agent-metricsのメンテナンスを引き継いだもの | `claude-code` `openai-codex` `traex` `tui` `python` | 0 | 🔄 2026-08-22 |
| [**herdr-last-used**](https://github.com/MorganCollins/herdr-last-used)<br><sub>MorganCollins</sub> | 各herdrエージェントが最後にアクティブだった時刻を、経過時間に応じて色分けして表示し、Agentサイドバーを活動状況でフィルタする | `terminal` `shell` | 0 | 🔄 2026-08-24 |
| [**herdr-phin-board**](https://github.com/phin-tech/herdr-phin-board)<br><sub>phin-tech</sub> | Herdrプラグイン：スペース全体を対象とするステータスボード——todo・進行中・誰かの対応待ち・完了、さらに自分で定義したステータスにも対応。リストまたはカンバンで表示 | `bubbletea` `tui` `go` | 0 | 2026-07-29 |
| [**herdr-idle-shell-badge**](https://github.com/rcosteira79/herdr-idle-shell-badge)<br><sub>rcosteira79</sub> | バックグラウンドでシェルが動き続けている、アイドル状態のエージェントにバッジを表示する | `python` | 0 | 🔄 2026-08-26 |
| [**colloquy**](https://github.com/SoMaCoSF/colloquy)<br><sub>SoMaCoSF</sub> | エージェント群向けの、自己アドレス指定型・一時キャッシュされた因果関係DAG監査ログとテレメトリ | `colloquy` `gyst` `javascript` | 0 | 2026-07-29 |
| [**herdr-claude-context-meter**](https://github.com/tmastalirsch/herdr-claude-context-meter)<br><sub>tmastalirsch</sub> | herdrプラグイン：Claude Codeのコンテキスト使用量をバーで表示——ステータスラインとherdrのペインの両方に対応 | `claude-code` `context-window` `statusline` `shell` | 0 | 🔄 2026-08-27 |
| [**herdr-workspace-board**](https://github.com/tmastalirsch/herdr-workspace-board)<br><sub>tmastalirsch</sub> | herdrプラグイン：未完了の作業があるgitリポジトリを1行ずつ表示し、忘れられそうな順にランク付けする | `git` `productivity` `workspace` `shell` | 0 | 🔄 2026-08-27 |
| [**conflux-herdr**](https://github.com/tumf/conflux-herdr)<br><sub>tumf</sub> | Conflux TUIを実行し、そのライフサイクル状態を報告するHerdrプラグインペイン | `shell` | 0 | 2026-07-26 |
| [**herdr-hud**](https://github.com/zetlen/herdr-hud)<br><sub>zetlen</sub> | herdrプラグイン：キーバインドで開くポップアップに、ホスト・ネットワーク・エージェント・セッションの情報を表示——設定変更やカスタムスクリプトによる拡張が可能 | `bash` `terminal` `shell` | 0 | 2026-08-03 |

<details><summary>この目的にも関係するもの</summary>

- [nelsonPires5/herdr-board](https://github.com/nelsonPires5/herdr-board) — herdr向けのカンバンボード——カードはそのままプロンプトになり、見えているペイン上のAIエージェントに割り振られる
- [quaywin/agys](https://github.com/quaywin/agys) — 汚染ゼロのサンドボックスにより、Herdr上のAntigravity CLIに手間いらずのマルチプロファイル分離とリアルタイムなクォータ追跡を提供する
- [e2b-dev/herdr-e2b-sandbox](https://github.com/e2b-dev/herdr-e2b-sandbox) — git worktreeをE2B Sandboxにミラーするherdrプラグイン——単一のboxでも、エージェントごとにブランチを割り当てたフリートでも対応。TUIダッシュボード付き
- [IvoryHeart/herdr-world](https://github.com/IvoryHeart/herdr-world) — Herdr World——Herdr向けのマルチサーフェスなWeb体験
- [Northern-Lighthouse/herdr-fleet](https://github.com/Northern-Lighthouse/herdr-fleet) — Tailscale経由でherdrマシンのフリートを管理——ダッシュボードプラグイン、自動検出、キャパシティを考慮したエージェント割り当て、ディスクレスなワークスペースに対応
- [cdowell09/herdr-pr-board](https://github.com/cdowell09/herdr-pr-board) — 複数リポジトリを横断できる、設定可能なHerdr向けGitHubプルリクエストダッシュボード
- [bengemine/herdr-hibernate](https://github.com/bengemine/herdr-hibernate) — Herdr上のアイドル状態のコーディングエージェントペイン（Claude Code、Codex、Grok）をハイバネート——メモリを解放し、Enterキーで元のセッションをそのまま再開できる
- [Javamomma/herdr-scribe](https://github.com/Javamomma/herdr-scribe) — herdrプラグイン：録音せずにライブで会議を文字起こし——マイク入力をRAM上のみのトランスクリプトとライブ分析用ペインに変換。停止時には議事録・任意のポリシーゲート・レビュー可能な自動ドラフトを生成。Linux/W…
- [sazardev/herdr-code-board](https://github.com/sazardev/herdr-code-board) — Herdr内の、エージェント向けプロンプトのカンバンキュー——カードが実際のエージェントをペイン・worktree・ワークスペースに配置し、カード同士を連鎖させるルールも設定できる
- [chouxcreams/herdr-dashboard](https://github.com/chouxcreams/herdr-dashboard) — herdrのワークスペース向けのPRステータスダッシュボードTUI——ペインごとのPRの状態・CI・レビューを一目で確認できる
- [GranamyrBR/LunaCrab](https://github.com/GranamyrBR/LunaCrab) — 別プロジェクト用に予約済み
- [maedana/herdr-agents-preview](https://github.com/maedana/herdr-agents-preview) — Herdr向けのマルチエージェントターミナルプレビューダッシュボード：稼働中のすべてのエージェントを同時に表示し、選択中のエージェントが大部分の幅を占める
- [GranamyrBR/ezdras-herdr](https://github.com/GranamyrBR/ezdras-herdr) — Herdr向けの、複数エージェントをリアルタイムに可視化する仕組みとペイン操作機能
- [peria-ai/precc-herdr-plugin](https://github.com/peria-ai/precc-herdr-plugin) — herdr 用の PRECC プラグイン。エージェント横断でのトークン節約状況を計測し、PRECC のセットアップをワンタッチで行えます。
- [ryus1234/provider-usage](https://github.com/ryus1234/provider-usage) — Herdr 用の、プロバイダーの使用量とクォータを表示するバーです。

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-finder"></a>

## 検索・ファジーファインダー

> コマンドやプロジェクトを、名前をうろ覚えのまま呼び出したい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-navigator**](https://github.com/thanhdat77/herdr-navigator)<br><sub>thanhdat77</sub> | 1つのファジーナビゲーターから、任意のHerdrのワークスペース・エージェント・プロジェクト・セッション・リモート・ディレクトリ・アクションにジャンプできる | `fuzzy-finder` `rust` `terminal` `workspace-manager` | 129 | 🔄 2026-08-25 |
| [**termscope**](https://github.com/iurysza/termscope)<br><sub>iurysza</sub> | 分割ペインで、ターミナル画面に表示されているファイルやリンクを開く | `python` `television` `terminal` `tmux` | 50 | 2026-08-19 |
| [**herdr-sessionizer**](https://github.com/andrewchng/herdr-sessionizer)<br><sub>andrewchng</sub> | プロジェクトやworktreeをファジー検索で開き、宣言的なTOMLレイアウト（タブ・ペイン分割・起動コマンド・リポジトリごとの上書き設定）からワークスペースを立ち上げる | `bun` `fuzzy-finder` `fzf` `git-worktree` `sessionizer` | 45 | 🔄 2026-09-02 |
| [**herdr-plugin-sesh**](https://github.com/fullerzz/herdr-plugin-sesh)<br><sub>fullerzz</sub> | Herdr向けのSesh風ワークスペースピッカーTUI。zoxideと連携し、よく使うディレクトリからワークスペースを作成できる | `bubbletea` `sesh` `tui` `zoxide` `go` | 36 | 🔄 2026-09-04 |
| [**herdr-command-palette**](https://github.com/JanTvrdik/herdr-command-palette)<br><sub>JanTvrdik</sub> | herdr向けのfzfコマンドパレット——任意のプラグインアクションをファジー検索して実行 | `shell` | 35 | 2026-06-29 |
| [**herdr-bar**](https://github.com/jeffarese/herdr-bar)<br><sub>jeffarese</sub> | herdr版のCmd+K：任意のタブ・エージェント・リポジトリ・ブランチにファジー検索でジャンプ。Python標準ライブラリのみで動作 | `command-bar` `fuzzy-finder` `python` `terminal` `tui` | 33 | 🔄 2026-08-31 |
| [**herdr-drovr**](https://github.com/AVGVSTVS96/herdr-drovr)<br><sub>AVGVSTVS96</sub> | herdrのペインとタブを簡単に移動する | `fzf` `terminal` `javascript` | 15 | 2026-08-08 |
| [**herdr-zoxide**](https://github.com/den-tanui/herdr-zoxide)<br><sub>den-tanui</sub> | zoxideのディレクトリからワークスペース・タブ・ペインを作成するHerdrプラグイン | `zoxide` `shell` | 11 | 2026-07-25 |
| [**herdr-palette**](https://github.com/ramarivera/herdr-palette)<br><sub>ramarivera</sub> | Herdrのワークスペース向けの、Rust/Ratatui製ファジーコマンドパレット | `command-palette` `ratatui` `rust` `terminal` `tui` | 8 | 2026-08-14 |
| [**herdr-palette**](https://github.com/vjeantet/herdr-palette)<br><sub>vjeantet</sub> | Sublime Text / VS Code風の、herdr向けコマンドパレット——標準操作・プラグインのアクション・自分のコマンドを、1つのキーの裏にまとめる | `command-palette` `fuzzy-search` `terminal` `tui` `rust` | 7 | 🔄 2026-08-31 |
| [**herdr-quick-actions**](https://github.com/enekos/herdr-quick-actions)<br><sub>enekos</sub> | herdr標準のタブ/ペイン/ワークスペース操作を、使用頻度順でfzfから選べる——キーバインドを覚える必要がなくなる | `shell` | 6 | 2026-08-05 |
| [**herdr-switchboard**](https://github.com/crafts69guy/herdr-switchboard)<br><sub>crafts69guy</sub> | herdrプラグイン：稼働中のエージェント・開いているワークスペース・ghq管理下のリポジトリを、Rust製の1つのTUIでファジー切り替え——選んだリポジトリを新規ワークスペース・タブ・スプリット・現在のペインのいずれかで開ける | `developer-tools` `ghq` `ratatui` `rust` `terminal` | 5 | 🔄 2026-09-03 |
| [**herdr-sessionizer**](https://github.com/salkhalil/herdr-sessionizer)<br><sub>salkhalil</sub> | herdr版tmux-sessionizer：開いているワークスペースとzoxideのディレクトリをfzfで検索し、テンプレートタブ付きで作成またはフォーカスする | `shell` | 5 | 2026-07-27 |
| [**herdr-pane-navigator**](https://github.com/mr04vv/herdr-pane-navigator)<br><sub>mr04vv</sub> | Herdrのワークスペース・タブ・ペインを1つのファジーツリーとして横断移動——各ペインが実際に何をしているかを手がかりにする | `coding-agents` `fzf` `terminal` `tui` `shell` | 4 | 🔄 2026-08-24 |
| [**herdr-keymap**](https://github.com/The-Dave-Stack/herdr-keymap)<br><sub>The-Dave-Stack</sub> | herdrプラグイン：すべてのキーバインドをオーバーレイのパレットに表示し、CLI相当のものはそのまま実行できる | `typescript` | 4 | 2026-08-12 |
| [**herdr-kiosk**](https://github.com/thomasschafer/herdr-kiosk)<br><sub>thomasschafer</sub> | Gitのリポジトリとブランチをファジー検索し、Herdr内でworktreeとして開く | `rust` | 4 | 🔄 2026-08-27 |
| [**herdr-cast**](https://github.com/aliou/herdr-cast)<br><sub>aliou</sub> | 個人用Herdrプラグイン——ネイティブmacOS通知、ファジーなワークスペース移動、zoxide連携のワークスペース作成、レイアウトコマンドをまとめて提供 | `developer-tools` `macos` `notifications` `ratatui` `rust` | 3 | 🔄 2026-08-31 |
| [**herdr-palette**](https://github.com/cesarferreira/herdr-palette)<br><sub>cesarferreira</sub> | Herdr向けのポップアップ型コマンドパレット | `typescript` | 3 | 2026-08-14 |
| [**herdr-grep-nvim**](https://github.com/cinco/herdr-grep-nvim)<br><sub>cinco</sub> | herdrプラグイン：fzf + ripgrepでライブgrepし、マッチした箇所を作業の隣のスプリットでnvimで開く | `shell` | 3 | 2026-07-17 |
| [**herdr-spotify**](https://github.com/iikjl/herdr-spotify)<br><sub>iikjl</sub> | herdr向けのSpotify再生中オーバーレイプラグイン——アルバムアート・再生操作、Spotify Web API経由の検索/キュー追加/いいねにも対応 | `spotify` `terminal` `go` | 3 | 2026-07-07 |
| [**herdr-hunk**](https://github.com/JacquesvanWyk/herdr-hunk)<br><sub>JacquesvanWyk</sub> | herdr向けの、Hunkの差分をfzfで対話的に選ぶピッカー：コミット・範囲・stashに対応し、エージェント完了時に自動オープンもできる | `fzf` `hunk` `shell` | 3 | 2026-07-12 |
| [**herdr-ssh-manager**](https://github.com/jorge07RD/herdr-ssh-manager)<br><sub>jorge07RD</sub> | SSHホストを保存し、Herdr内のファジーポップアップから再接続する——Enterキーでポップアップからそのままsshに渡す | `rust` `ssh` `terminal` `tui` | 3 | 🔄 2026-08-24 |
| [**herdr-workspacer**](https://github.com/mcuste/herdr-workspacer)<br><sub>mcuste</sub> | zoxideでプロジェクトを見つけ、Herdrのワークスペースを切り替え・作成する | `rust` `tui` `zoxide` | 3 | 🔄 2026-09-03 |
| [**herdr-agent-recency**](https://github.com/ugurtarlig/herdr-agent-recency)<br><sub>ugurtarlig</sub> | テーマに対応したHerdrピッカー。CodexとClaudeの実質的なアクティビティで並び替える | `claude-code` `codex` `fzf` `python` | 3 | 2026-07-17 |
| [**herdr-openr**](https://github.com/wraithyy/herdr-openr)<br><sub>wraithyy</sub> | herdrプラグイン：ターミナルやAIエージェントが直前に言及したファイル/URLをファジー検索で開く——Claudeのペインではセッションのトランスクリプトを読み取る | `shell` | 3 | 2026-08-14 |
| [**herdr-configurable-picker**](https://github.com/yoshiori/herdr-configurable-picker)<br><sub>yoshiori</sub> | 完全にカスタマイズ可能なキーバインドを持つ、herdr向けのツリー形式gotoピッカー | `rust` | 3 | 2026-07-05 |
| [**herdr-command-palette**](https://github.com/alon-z/herdr-command-palette)<br><sub>alon-z</sub> | Herdrプラグイン：ワークスペース/ディレクトリのファジー検索コマンドパレット | `javascript` | 2 | 2026-06-22 |
| [**herdr-launcher**](https://github.com/arjenblokzijl/herdr-launcher)<br><sub>arjenblokzijl</sub> | 宣言的なTOMLワークフローをファジー検索で選び、フォームに入力して、新しいherdrのスペースでコーディングエージェントを起動する | `launcher` `ratatui` `rust` `tui` | 2 | 2026-07-10 |
| [**🆕 herdr-palette**](https://github.com/Binb1/herdr-palette)<br><sub>Binb1</sub> | Herdr 用のコマンドパレット。ワークスペースやエージェントへジャンプしたり、プラグインのアクションや Herdr のコマンドを実行できます。 | `go` | 2 | 🔄 2026-09-03 |
| [**herdr-sesh-bro**](https://github.com/cyperx84/herdr-sesh-bro)<br><sub>cyperx84</sub> | Herdr向けのsesh風ファジーセッションピッカー——ワークスペース・エージェント・zoxideのディレクトリを、ライブプレビュー付きの1つのfzfポップアップにまとめる | `go` | 2 | 2026-08-12 |
| [**herdr-simple-switcher**](https://github.com/haphamdev/herdr-simple-switcher)<br><sub>haphamdev</sub> | ワークスペース・タブ・AIエージェントをファジー検索する | `shell` | 2 | 2026-08-01 |
| [**herdr-workspace-launcher**](https://github.com/ImArtisann/herdr-workspace-launcher)<br><sub>ImArtisann</sub> | 検索可能でキーボード操作のディレクトリピッカーを使い、フォーカスしたワークスペースをすばやく作成するmacOS向けHerdrプラグイン | `typescript` | 2 | 2026-07-16 |
| [**herdr-recent-workspaces**](https://github.com/ismaelosuna7824/herdr-recent-workspaces)<br><sub>ismaelosuna7824</sub> | Herdr版「最近使ったフォルダを開く」——ワークスペースとして開いたフォルダをファジー検索できる一覧。選ぶとそのワークスペースを開くか再フォーカスでき、ファイルシステムを参照して新規に開くこともできる | `go` | 2 | 2026-07-10 |
| [**herdr-ghq-open-agent**](https://github.com/kenchan/herdr-ghq-open-agent)<br><sub>kenchan</sub> | herdrプラグイン：ghq管理下のリポジトリをfzfでインクリメンタル検索し、選んだものをワークスペース/タブで開いてclaudeを起動する | `fzf` `ghq` `shell` | 2 | 2026-08-03 |
| [**herdr-keybind-search**](https://github.com/malone-c/herdr-keybind-search)<br><sub>malone-c</sub> | herdr向けの検索可能なキーバインドオーバーレイ（fzf）。キーを押すと、自分のキーバインドをファジー検索できる | `shell` | 2 | 2026-07-15 |
| [**herdr-waypoint**](https://github.com/wraithyy/herdr-waypoint)<br><sub>wraithyy</sub> | フォルダに名前を付けて保存し、ファジー検索の一覧から選んで新しいherdrワークスペースとして開く | `shell` | 2 | 2026-08-12 |
| [**herdr-sessionizer**](https://github.com/42lizard/herdr-sessionizer)<br><sub>42lizard</sub> | tmux-sessionizer風のherdr向けプラグイン | `fzf` `shell` | 1 | 🔄 2026-08-28 |
| [**herdr-url-picker**](https://github.com/abrose/herdr-url-picker)<br><sub>abrose</sub> | herdrプラグイン：現在のペインに表示されたURLをfzfで選び、デフォルトブラウザで開く | `shell` | 1 | 2026-07-22 |
| [**herdr-jump**](https://github.com/agustinvalencia/herdr-jump)<br><sub>agustinvalencia</sub> | herdrのスペースとエージェント用に分かれたオーバーレイピッカー——任意のワークスペースやエージェントに、ステータスを色で示しながらジャンプできる | `go` | 1 | 2026-07-24 |
| [**helm.herdr**](https://github.com/black-atom-industries/helm.herdr)<br><sub>black-atom-industries</sub> | 1つのファジーナビゲーターから、任意のHerdrのワークスペース・エージェント・プロジェクト・セッション・リモート・ディレクトリ・アクションにジャンプできる | `rust` | 1 | 🔄 2026-09-03 |
| [**herdr-workspace-save**](https://github.com/chandrasekharan98/herdr-workspace-save)<br><sub>chandrasekharan98</sub> | Herdrのワークスペース（レイアウト・作業ディレクトリ・エージェントセッション・実行中のコマンド）を保存し、あとでfzfピッカーから再度開ける | `claude-code` `terminal` `tmux` `python` | 1 | 2026-08-19 |
| [**herdr-url-picker**](https://github.com/chouxcreams/herdr-url-picker)<br><sub>chouxcreams</sub> | Herdrプラグイン：フォーカス中のペインからURLを選び、ブラウザで開く | `shell` | 1 | 2026-07-22 |
| [**herdr-spotify**](https://github.com/DeepRuparel/herdr-spotify)<br><sub>DeepRuparel</sub> | Herdr向けのSpotify連携——Go製、設定不要のローカル操作に加え、PKCE経由で認可された検索・キュー追加・保存に対応 | `spotify` `go` | 1 | 🔄 2026-08-28 |
| [**herdr-plugin-command-palette**](https://github.com/haisi/herdr-plugin-command-palette)<br><sub>haisi</sub> | fzfを使った、herdr向けのファジー検索対応コマンドパレット | `fzf` `python` | 1 | 2026-08-17 |
| [**herdr-command-palette**](https://github.com/hota911/herdr-command-palette)<br><sub>hota911</sub> | herdr標準の操作（ワークスペース・タブ・ペイン・エージェント）向けの、fzfコマンドパレット | `command-palette` `fzf` `shell` | 1 | 2026-08-16 |
| [**herdr-turbo-palette**](https://github.com/jackfrancisdalton/herdr-turbo-palette)<br><sub>jackfrancisdalton</sub> | 任意のHerdrのspace・タブ・エージェント・ペインをファジー検索し、そのまま直接ジャンプする | `python` | 1 | 🔄 2026-08-22 |
| [**herdr-keys**](https://github.com/JacquesvanWyk/herdr-keys)<br><sub>JacquesvanWyk</sub> | herdr向けの、ファジー検索可能なキーバインド一覧（パック・発見機能・個人による上書き設定に対応） | `shell` | 1 | 2026-07-12 |
| [**herdr-fzf-url**](https://github.com/kaar/herdr-fzf-url)<br><sub>kaar</sub> | herdrペインのスクロールバックからURLをファジー検索して開く——tmux-fzf-urlのherdr移植版 | `shell` | 1 | 2026-07-29 |
| [**herdr-hint**](https://github.com/maedana/herdr-hint)<br><sub>maedana</sub> | Herdr向けのVimium風ヒントラベル——キーを押すとタブやエージェントにラベルが表示され、ラベルを押すとジャンプする | `rust` | 1 | 2026-08-11 |
| [**herdr-shortcut**](https://github.com/matheus3301/herdr-shortcut)<br><sub>matheus3301</sub> | Herdr向けのショートカットタスクピッカー兼コーディングエージェントランチャー | `bubbletea` `claude-code` `codex` `coding-agents` `developer-tools` | 1 | 2026-07-24 |
| [**🆕 herdr-pickers**](https://github.com/sagmans/herdr-pickers)<br><sub>sagmans</sub> | エージェント・worktree・ワークスペース・プロジェクト向けに、いくつかのカスタムなポップアップピッカーを提供します。 | `typescript` | 1 | 🔄 2026-09-03 |
| [**herdr-pane-picker**](https://github.com/ugurtarlig/herdr-pane-picker)<br><sub>ugurtarlig</sub> | ペイン上に表示される文字ヒントを入力して、Herdrのペインを選択する | `terminal` `wezterm` `python` | 1 | 2026-07-17 |
| [**herdr-bitwarden**](https://github.com/WillowMist/herdr-bitwarden)<br><sub>WillowMist</sub> | Bitwardenのボルトをファジー検索し、認証情報を貼り付け・コピーする——tmux-bitwardenのherdr移植版 | `bitwarden` `fzf` `terminal` `tmux` `shell` | 1 | 2026-08-11 |
| [**herdr-fzf-url**](https://github.com/x0d7x/herdr-fzf-url)<br><sub>x0d7x</sub> | herdrのターミナルペインをスキャンしてURLを検出し、fzfで対話的に選択する | `fzf` `go` `url` | 1 | 2026-06-26 |
| [**herdr-open-local-paths**](https://github.com/yigitkg/herdr-open-local-paths)<br><sub>yigitkg</sub> | ローカルパスを検出し、Windows・Linux・WSL上のシンプルなピッカーから開く/表示するHerdrプラグイン | `developer-tools` `python` `terminal` `wsl` | 1 | 2026-07-28 |
| [**herdr-agents-picker**](https://github.com/yxhta/herdr-agents-picker)<br><sub>yxhta</sub> | Herdrプラグイン：ワークスペースピッカー風のファジー検索で、エージェントペインをリアルタイムプレビュー付きで選ぶ（Rust + ratatui製） | `rust` | 1 | 2026-07-31 |
| [**herdr-telescope**](https://github.com/zackshen/herdr-telescope)<br><sub>zackshen</sub> | herdr向けのfzfコマンドテレスコープ——ネイティブアクション、プラグインアクション、ファイル検索（@）、ライブripgrep検索（/）に対応 | `fzf` `rust` | 1 | 🔄 2026-08-20 |
| [**herdr-iris**](https://github.com/a-curious-coder/herdr-iris)<br><sub>a-curious-coder</sub> | Iris——herdrプラグイン：ペインで検出したエージェントに絞り込んだ、AIエージェントスキルのファジー検索チートシート | `shell` | 0 | 2026-08-07 |
| [**herdr-command-palette**](https://github.com/barnuri/herdr-command-palette)<br><sub>barnuri</sub> | herdr向けのF1風コマンドパレット——インストール済みの全プラグインの全アクションを、ファジー検索して実行できる。依存関係なし | `command-palette` `terminal` `javascript` | 0 | 🔄 2026-09-01 |
| [**herdr-project-manager**](https://github.com/barnuri/herdr-project-manager)<br><sub>barnuri</sub> | herdr向けのプロジェクトマネージャープラグイン——globまたは手動でのプロジェクト検出、ファジーピッカー、タブまたはワークスペースとしてオープン | `javascript` | 0 | 🔄 2026-08-25 |
| [**herdr-worktree-picker**](https://github.com/BjoernSchotte/herdr-worktree-picker)<br><sub>BjoernSchotte</sub> | Herdr向けのファジーなGit worktreeピッカー——worktree-rapid-river-6486のような名前の代わりに、ブランチ名を入力するだけでよい。グループ化されたワークスペース、またはスプリットペインとして開ける | `bash` `cli` `developer-tools` `fzf` `git-worktree` | 0 | 🔄 2026-08-24 |
| [**herdr-locksmith**](https://github.com/bkarpinos/herdr-locksmith)<br><sub>bkarpinos</sub> | herdr向けのキーバインド・コマンドパレット | `go` | 0 | 🔄 2026-09-01 |
| [**herdr-picker**](https://github.com/bkarpinos/herdr-picker)<br><sub>bkarpinos</sub> | herdrのワークスペース・エージェント・タブを検索・プレビューできる、高速なポップアップピッカー | `go` | 0 | 2026-07-25 |
| [**herdr-opencode-sessions**](https://github.com/damianpoole/herdr-opencode-sessions)<br><sub>damianpoole</sub> | 過去のOpenCodeセッションを、タイトル・プロジェクト・パス・日付・トランスクリプトの内容でファジー検索できるHerdrプラグイン——会話プレビュー付きで、現在または新しいワークスペースでセッションを再開・フォークするショートカットも備える | `typescript` | 0 | 2026-08-14 |
| [**herdr-agents**](https://github.com/dleen/herdr-agents)<br><sub>dleen</sub> | herdr向けのfzfエージェントピッカー——全エージェントペインを対応優先度の高い順に並べ、セッションプレビューとワンキー起動に対応する | `coding-agents` `fzf` `python` `terminal` | 0 | 2026-08-20 |
| [**herdr-command-palette**](https://github.com/fabiogaliano/herdr-command-palette)<br><sub>fabiogaliano</sub> | Herdr向けのファジーコマンドパレット——あらゆるアクションを検索し、ショートカットを確認して実行できる | `command-palette` `fzf` `terminal` `python` | 0 | 2026-08-10 |
| [**🆕 herdr-keybinds**](https://github.com/gwelican/herdr-keybinds)<br><sub>gwelican</sub> | プラグインのものも含め、すべてのキーバインドを一覧表示・検索できる Herdr プラグインです。 | `python` | 0 | 🔄 2026-08-31 |
| [**herdr-control-panel**](https://github.com/iskwyuki/herdr-control-panel)<br><sub>iskwyuki</sub> | 1つのキーバインド、1つのパネルでherdrを操作——履歴や任意のパスからワークスペースを開き、独自のアクションも追加できる。純粋なbash + fzf製でビルド不要 | `bash` `fzf` `terminal` `shell` | 0 | 2026-08-11 |
| [**🆕 herdr-open-editor**](https://github.com/jimididit/herdr-open-editor)<br><sub>jimididit</sub> | fzf でファイルをあいまい検索して選び、設定済みのエディタで開きます。 | `herd` `text-editor` `tui` `shell` | 0 | 🔄 2026-09-03 |
| [**pj-herdr**](https://github.com/josephschmitt/pj-herdr)<br><sub>josephschmitt</sub> | PJピッカーを使って新しいワークスペースを開くHerdrプラグイン | `shell` | 0 | 2026-07-15 |
| [**herdr-finder-reveal**](https://github.com/klukacin/herdr-finder-reveal)<br><sub>klukacin</sub> | Herdrのペイン内のローカルファイルパスをクリックすると、macOSのFinderで表示する | `finder` `ghostty` `macos` `terminal-multiplexer` `shell` | 0 | 2026-08-10 |
| [**herdr-cull**](https://github.com/krzysztoff1/herdr-cull)<br><sub>krzysztoff1</sub> | herdr内のアイドル状態のエージェントペインを確認して閉じる——fzfによる複数選択、確認なしで閉じることはない | `ai-agents` `claude` `codex` `fzf` `terminal` | 0 | 2026-07-20 |
| [**🆕 herdr-jump**](https://github.com/lancodev/herdr-jump)<br><sub>lancodev</sub> | herdr のワークスペースとエージェントを、vim 風キー操作の 2 ペインあいまい検索スイッチャーで切り替えられます。 | `fzf` `tui` `shell` | 0 | 🔄 2026-09-01 |
| [**herdr-vscode-tasks**](https://github.com/lurepos/herdr-vscode-tasks)<br><sub>lurepos</sub> | プロジェクトの.vscodeフォルダを扱うときに便利なherdrピッカー | `typescript` | 0 | 🔄 2026-09-02 |
| [**herdr-omarchy-theme-sync**](https://github.com/maxBRT/herdr-omarchy-theme-sync)<br><sub>maxBRT</sub> | HerdrのUIパレットを、現在使用中のOmarchyテーマに同期させる | `linux` `omarchy` `theme` `python` | 0 | 2026-08-15 |
| [**🆕 herdr-plugin-project-finder**](https://github.com/mike-bronner/herdr-plugin-project-finder)<br><sub>mike-bronner</sub> | Herdr プラグイン：git リポジトリをあいまい検索で選び、ワークスペースとして開きます。 | `python` | 0 | 🔄 2026-09-04 |
| [**herdr-workspaces**](https://github.com/mikedclarke/herdr-workspaces)<br><sub>mikedclarke</sub> | ディレクトリをherdrのワークスペースとして扱う——よく使う場所を登録し、ファジー検索で選ぶと、そこに名前付きワークスペースが作られる | `go` `terminal` `tui` `workspaces` | 0 | 🔄 2026-09-02 |
| [**herdr-smart-workspace**](https://github.com/nicolasvasquez/herdr-smart-workspace)<br><sub>nicolasvasquez</sub> | セッション内でワークスペースをすばやく切り替えたり、zoxideからオーバーレイのfzfピッカーで新規作成したりできるHerdrプラグイン | `python` | 0 | 2026-07-02 |
| [**herdr-launcher**](https://github.com/nicolegros/herdr-launcher)<br><sub>nicolegros</sub> | ワークスペースの作成や切り替えをすばやく行える、ファジー検索ディレクトリピッカーを提供するherdrプラグイン | `go` | 0 | 2026-07-15 |
| [**mux-prompter**](https://github.com/phine-apps/mux-prompter)<br><sub>phine-apps</sub> | コンテキストに応じたプロンプトをファジー検索で選び、Herdrやtmuxのペインに注入する | `fzf` `prompt-engineering` `terminal-multiplexer` `tmux` `tmux-plugin` | 0 | 🔄 2026-08-31 |
| [**herdr-repo-picker**](https://github.com/princejoogie/herdr-repo-picker)<br><sub>princejoogie</sub> | OpenTUI製のピッカーから、Gitリポジトリをherdrのワークスペースとして開く | `git` `opentui` `typescript` | 0 | 2026-08-17 |
| [**herdr-claude-profile**](https://github.com/quinnjr/herdr-claude-profile)<br><sub>quinnjr</sub> | herdrプラグイン：オーバーレイのパレットからclaude-profileのプロファイルを切り替え・管理する | `typescript` | 0 | 2026-07-20 |
| [**herdr-plugins**](https://github.com/shelken/herdr-plugins)<br><sub>shelken</sub> | Herdrプラグインのモノレポ（auto-pi：エリアごとにpiを開く＋セッションピッカー） | `python` | 0 | 2026-07-17 |
| [**herdr-file-picker**](https://github.com/shivammehta25/herdr-file-picker)<br><sub>shivammehta25</sub> | tmux-file-pickerをherdr向けに移植した、いわゆる「vibe coding」製プラグイン | `shell` | 0 | 2026-07-29 |
| [**herdr-atuin-plugin**](https://github.com/smanickam01/herdr-atuin-plugin)<br><sub>smanickam01</sub> | herdrのポップアップでAtuinのシェル履歴を検索——prefix+aを押し、Enterで実行、Tabで編集できる。インストール時に自動でキーバインドされる | `atuin` `macos` `shell-history` `terminal` `zsh` | 0 | 2026-08-17 |
| [**🆕 herdr-jump**](https://github.com/solidsnakedev/herdr-jump)<br><sub>solidsnakedev</sub> | herdr 用のワークスペース・ペイン・タブのあいまい検索ピッカーに加え、直前のワークスペースへ切り替えるトグルも備えています。 | `shell` | 0 | 🔄 2026-09-01 |
| [**🆕 herdr-hop**](https://github.com/utahta/herdr-hop)<br><sub>utahta</sub> | herdr プラグイン：1 つのポップアップから、リポジトリ・worktree・ワークスペースへ一気にジャンプできます。 | `git-worktree` `go` `terminal` `tui` | 0 | 🔄 2026-09-02 |
| [**herdr-workspacex**](https://github.com/willfish/herdr-workspacex)<br><sub>willfish</sub> | Rustネイティブのファジー検索型Herdrワークスペース切り替えツール——zoxideを利用したワークスペース作成に対応 | `rust` `workspace-manager` `zoxide` | 0 | 2026-07-07 |
| [**herdr-fzf-url**](https://github.com/willian/herdr-fzf-url)<br><sub>willian</sub> | フォーカス中のペインから`fzf`でURLを選び、開く・コピーする | `fzf` `shell` | 0 | 2026-07-28 |

<details><summary>この目的にも関係するもの</summary>

- [beyondlex/herdr-recent-navigator](https://github.com/beyondlex/herdr-recent-navigator) — Herdr向けの、最近使ったワークスペース/タブ/ペインの切り替えツール。最近フォーカスしたワークスペース・タブ・ペイン・AIエージェントの一覧をポップアップ表示し、ファジー検索とキーボード操作に対応
- [JacquesvanWyk/herdr-linear](https://github.com/JacquesvanWyk/herdr-linear) — herdrのスプリットペインまたはタブ内で動くfzf駆動のLinearパネル：issue検索、プロジェクトの深掘り、issue作成、ステータス変更ができる
- [42lizard/herdr-dwm-layout](https://github.com/42lizard/herdr-dwm-layout) — Herdr向けの、DWM風master/stackレイアウト
- [adamwangxx/herdr-codex-resume](https://github.com/adamwangxx/herdr-codex-resume) — ネイティブのCodex resumeピッカーを、Herdrのコンテキストを保ったまま新しいスプリットで開く
- [caoer/ccc-herdr-layout](https://github.com/caoer/ccc-herdr-layout) — herdr向けのビジュアルレイアウトピッカー——1キーでライブプレビューしながら選べる
- [jovylle/herdr-pane-mark](https://github.com/jovylle/herdr-pane-mark) — Herdr プラグイン——パレット/ポップアップから、Agents 配下にカスタムの $mark を設定できます（フォーク不要）。

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-automation"></a>

## 自動化・フック・定期実行

> worktree 作成時やタイミングを決めて、決まった手順を自動で走らせたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-browser**](https://github.com/ogulcancelik/herdr-browser)<br><sub>ogulcancelik</sub> | Herdrのペイン内で実際のChromiumビューを描画し、CDP経由で操作する | `browser` `browser-automation` `cdp` `chromium` `kitty-graphics` | 348 | 🔄 2026-08-22 |
| [**herdr-automatic-rename**](https://github.com/qu8n/herdr-automatic-rename)<br><sub>qu8n</sub> | Smart tab names and numbered labels for a smooth herdr navigation | `shell` | 67 | 🔄 2026-08-31 |
| [**herdr-auto-title**](https://github.com/kryptamine/herdr-auto-title)<br><sub>kryptamine</sub> | 各タブでの作業内容に自動で追従するタブタイトル。Herdr でタブを整理された状態に保ち、何をしているかが一目でわかります。 | `go` | 62 | 🔄 2026-09-03 |
| [**herdr-auto-title**](https://github.com/sh1ma/herdr-auto-title)<br><sub>sh1ma</sub> | Claude CodeとCodexの会話内容から、herdrのタブタイトルを自動生成する | `claude-code` `codex` `python` | 53 | 2026-08-13 |
| [**zed-herdr**](https://github.com/ImArtisann/zed-herdr)<br><sub>ImArtisann</sub> | アクティブなHerdRワークスペースを、既存のZedセッションと自動的に同期する | `typescript` | 26 | 2026-08-17 |
| [**herdr-worktree-setup**](https://github.com/tdi/herdr-worktree-setup)<br><sub>tdi</sub> | herdrプラグイン：worktree作成時にプロジェクトごとのセットアップ手順を実行（mainから.envをコピー、mise trust、direnv allow、依存関係のインストールなど） | `javascript` | 24 | 2026-07-20 |
| [**herdr-auto-pilot**](https://github.com/0xGosu/herdr-auto-pilot)<br><sub>0xGosu</sub> | Herdr APIを介して、稼働中のAIコーディングCLIに代わって自動でプロンプトを送るHerdrプラグイン。あなたの操作から学習するトレーニングモードと、危険/悪意ある操作を防ぐガード機能を搭載。十分に学習させれば「Full-Self Prompting（FSP）」モードで自律動作させられる | `go` | 19 | 🔄 2026-09-03 |
| [**herdr-workflows**](https://github.com/aorumbayev/herdr-workflows)<br><sub>aorumbayev</sub> | herdrの繰り返し作業を宣言的に自動化する | `agentic-ai` `agentic-workflow` `agents` `ai` `claude` | 19 | 🔄 2026-09-02 |
| [**herdr-routines**](https://github.com/mrcndz/herdr-routines)<br><sub>mrcndz</sub> | スケジュールされたルーティンを実行するHerdrプラグイン：cronまたは一定間隔でワークスペースにタブを開き、コマンド実行やエージェント起動を行う | `python` | 10 | 2026-07-18 |
| [**🆕 herdr-updater**](https://github.com/diegopzz/herdr-updater)<br><sub>diegopzz</sub> | Herdr本体とプラグインを、フリート全体にわたって安全に最新の状態に保つ | `rust` `updater` | 8 | 🔄 2026-09-01 |
| [**herdr-agent-config-manager**](https://github.com/Phoobobo/herdr-agent-config-manager)<br><sub>Phoobobo</sub> | エージェントのスキル・MCP・プラグイン・フックを検出し一括管理する、CLIとHerdrプラグインのハイブリッド | `python` | 8 | 🔄 2026-09-03 |
| [**herdr-tab-title**](https://github.com/aarsh21/herdr-tab-title)<br><sub>aarsh21</sub> | Herdr向けの、tmux風タブタイトルの自動設定 | `rust` `terminal` `tmux` | 7 | 2026-07-08 |
| [**bermuda**](https://github.com/bon5co/bermuda)<br><sub>bon5co</sub> | herdr上のClaude Codeによるオーケストレーション——エージェントが飛ばせないフロー、時刻指定のジョブ、claim付きスレッド、あとでエージェントが検索できるフォーラムを提供する | `agent-orchestration` `agents` `ai-agents` `automation` `claude-code` | 5 | 🔄 2026-09-03 |
| [**herdr-pane-balancer**](https://github.com/jeph/herdr-pane-balancer)<br><sub>jeph</sub> | ペインの作成・終了・クローズ時に、Herdrのターミナルペインを自動でバランス調整・均等化・タイル配置する | `python` | 5 | 2026-08-02 |
| [**herdr-automations**](https://github.com/DnzzL/herdr-automations)<br><sub>DnzzL</sub> | ターミナル上で動く、コーディングエージェント向けのスケジュールタスク。1回の実行ごとにプロンプト・cron行・新しいgit worktreeを用意——Herdr上で動作。1つのYAMLファイルのみで、ストア不要、ビルド済みバイナリ、自動化ごとにモデルを指定可能、スリープ後のキャッチアップ、ライブボード付き | `ai-agents` `automation` `claude-code` `coding-agents` `cron` | 4 | 🔄 2026-09-01 |
| [**herdr-fwd**](https://github.com/go-min/herdr-fwd)<br><sub>go-min</sub> | リモートのHerdrセッション向けに、ループバックポートフォワーディングを自動設定する | `port-forwarding` `ssh` `terminal` `rust` | 3 | 🔄 2026-09-01 |
| [**tendwire**](https://github.com/plotarmordev/tendwire)<br><sub>plotarmordev</sub> | Herdr向けのローカルAPI：コーディングエージェントをアプリ・自動化・任意のローカルシステムに接続する | `agent-api` `local-first` `python` | 3 | 2026-08-10 |
| [**herdr-js-worktree-bootstrap**](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap)<br><sub>LeonardoTrapani</sub> | JavaScript/TypeScript向けにHerdrのworktreeを自動でブートストラップ——ロックファイルを考慮したインストールと、安全な環境ファイルの復元に対応 | `automation` `bun` `developer-tools` `git-worktree` `javascript` | 2 | 2026-07-15 |
| [**herdr-shepherd**](https://github.com/mikedclarke/herdr-shepherd)<br><sub>mikedclarke</sub> | herdr向けのスケジュールされたエージェントセッション——ハートビート・cronルーティン・スクリプトを、見えるherdrワークスペースとして起動する | `coding-agents` `cron` `go` `scheduler` `tui` | 2 | 🔄 2026-09-03 |
| [**herdr-review-loop**](https://github.com/mikhail-angelov/herdr-review-loop)<br><sub>mikhail-angelov</sub> | herdrのワークスペース内でエージェント同士が自動的に相互レビューする——1体が書き、もう1体がレビューし、これを繰り返す | `terminal` `go` | 2 | 2026-08-16 |
| [**herdr-plugin**](https://github.com/ppggff/herdr-plugin)<br><sub>ppggff</sub> | 各Herdrペインに適したmacOSの入力方式（IME）を自動的に記憶・復元する | `ime` `input-method` `macos` `python` | 2 | 2026-07-27 |
| [**herdr-labels**](https://github.com/Angel-O/herdr-labels)<br><sub>Angel-O</sub> | 手動で付けたラベルは維持したまま、タブに自動で名前と番号を付けるHerdrプラグイン | `rust` | 1 | 2026-08-17 |
| [**🆕 herdr-triggers**](https://github.com/cantona/herdr-triggers)<br><sub>cantona</sub> | ペインの出力を常駐監視して正規表現でトリガーを発動します。自動ログインなど、正規表現ベースのターミナルトリガーに対応します。 | `rust` `terminal` | 1 | 🔄 2026-09-02 |
| [**🆕 hermes-herdr-auto-reconcile**](https://github.com/chris-yyau/hermes-herdr-auto-reconcile)<br><sub>chris-yyau</sub> | Herdrのペインを監視するHermesスーパーバイザー向けの、ゲートウェイ生存監視プラグイン | `automation` `hermes-agent` `multi-agent` `python` | 1 | 🔄 2026-09-02 |
| [**herdr-auto-tab-name**](https://github.com/dev-shimada/herdr-auto-tab-name)<br><sub>dev-shimada</sub> | herdrプラグイン：タブに現在のディレクトリ名を自動で付ける | `javascript` | 1 | 🔄 2026-08-29 |
| [**herdr-auto-update**](https://github.com/dio16/herdr-auto-update)<br><sub>dio16</sub> | herdrプラグイン：インストール済みプラグインに新しいアップストリームのコミットがあるか起動時に確認し、あれば再インストールする | `rust` | 1 | 2026-08-16 |
| [**herdr-routines**](https://github.com/guidodinello/herdr-routines)<br><sub>guidodinello</sub> | _(説明なし)_ | `python` | 1 | 🔄 2026-09-04 |
| [**say-hook**](https://github.com/HikaruEgashira/say-hook)<br><sub>HikaruEgashira</sub> | Claude Codeのフックイベントを、ElevenLabsのText-to-Speechで読み上げるmacOS向けCLI | `typescript` | 1 | 🔄 2026-09-01 |
| [**herdr-sched**](https://github.com/husniadil/herdr-sched)<br><sub>husniadil</sub> | Herdr上のコーディングエージェント向けのスケジュールとトリガー——cronジョブとwebhook/ファイル監視トリガーが、隣接するプラグインへアクションを発火させる。各アクションは実行主体によって署名される。すべて1つのGoバイナリで実現 | `ai-agents` `cron` `mcp-server` `scheduler` `webhooks` | 1 | 🔄 2026-08-30 |
| [**herdr-automations**](https://github.com/ram4-dev/herdr-automations)<br><sub>ram4-dev</sub> | Herdr向けの宣言的なcron・インターバル・イベント自動化 | `automation` `bun` `typescript` | 1 | 2026-08-13 |
| [**herdr-autocontinue**](https://github.com/rcosteira79/herdr-autocontinue)<br><sub>rcosteira79</sub> | エージェントの利用上限到達を監視し、リセットまでのカウントダウンをバッジ表示（$wall）し、時間枠が再び開いたらセットしておいたエージェントに再度プロンプトを送る | `python` | 1 | 🔄 2026-08-31 |
| [**herdr-nixos-vm**](https://github.com/Slimydog21/herdr-nixos-vm)<br><sub>Slimydog21</sub> | herdr向けのNixOS VMペイン——Hashimoto流の開発用VMを起動・停止・監視・ssh接続できる。nixos-vm kitが必要 | `shell` | 1 | 2026-08-18 |
| [**herdr-agent-title-sync**](https://github.com/winoooops/herdr-agent-title-sync)<br><sub>winoooops</sub> | Claude Code・Codex・Kimi Code・OpenCodeなど各種コーディングエージェント向けの、Herdrペインタイトル自動同期 | `developer-tools` `typescript` | 1 | 2026-08-20 |
| [**herdr-plugin-orbstack**](https://github.com/AsgardMuninn/herdr-plugin-orbstack)<br><sub>AsgardMuninn</sub> | OrbStackのLinuxマシンをherdrのワークスペースとして開く（直接シェル接続、SSHフォールバック、自動同期） | `python` | 0 | 2026-08-11 |
| [**herdr-auto-update**](https://github.com/barnuri/herdr-auto-update)<br><sub>barnuri</sub> | herdrを常に最新に保つ——パッチ/マイナー/メジャーの自動更新を、ライブなハンドオフ付きで行う | `auto-update` `javascript` | 0 | 🔄 2026-08-25 |
| [**herdr-teams-notify**](https://github.com/donghaolicd/herdr-teams-notify)<br><sub>donghaolicd</sub> | Microsoft Teamsへのエージェントライフサイクル通知を、送りすぎないように制御するHerdrプラグイン | `automation` `microsoft-teams` `notifications` `javascript` | 0 | 2026-08-15 |
| [**herdr-context-namer**](https://github.com/eabadim/herdr-context-namer)<br><sub>eabadim</sub> | OpenCode経由でペインのコンテキストから、Herdrのタブ・ワークスペース名を自動生成する | `opencode` `python` | 0 | 2026-08-06 |
| [**herdr-claude-title-hook**](https://github.com/eduardoborges/herdr-claude-title-hook)<br><sub>eduardoborges</sub> | セッションタイトルをHerdrのタブタイトルに同期するClaude Codeプラグイン | `shell` | 0 | 🔄 2026-08-26 |
| [**herdr-pane-name**](https://github.com/go-min/herdr-pane-name)<br><sub>go-min</sub> | ターミナルセッションのペインに自動で名前を付けるHerdrプラグイン | `pane-naming` `terminal` `terminal-multiplexer` `rust` | 0 | 2026-08-16 |
| [**herdr-looper**](https://github.com/gurronen/herdr-looper)<br><sub>gurronen</sub> | 新しいHerdrのワークスペースとworktreeで、繰り返し実行可能なマシンローカルのPiジョブを起動する | `automation` `rust` `terminal` | 0 | 🔄 2026-08-26 |
| [**🆕 herdr-cron**](https://github.com/huketo/herdr-cron)<br><sub>huketo</sub> | コーディングエージェント向けの自動化作業をスケジュール実行できます。Herdr のペイン内で、シェルコマンドやコーディングエージェントへのプロンプトを予約できます。 | `agent-skills` `automation` `bubbletea` `cli` `coding-agent` | 0 | 🔄 2026-09-03 |
| [**herdr-worktree-setup**](https://github.com/jtnovellis/herdr-worktree-setup)<br><sub>jtnovellis</sub> | herdrプラグイン：新しいgit worktreeをすぐに使える状態にする——.envと開発状態のコピー、依存関係キャッシュのクローン（APFS/reflink）、mise trust、direnv allow、依存関係のインストールを、ライブTUI付きで行う | `git-worktree` `rust` | 0 | 🔄 2026-08-29 |
| [**herdr-plugin-auto-rename**](https://github.com/khatriafaz/herdr-plugin-auto-rename)<br><sub>khatriafaz</sub> | Piセッションへの最初のプロンプトから、新しいHerdrのワークスペースとGitブランチを自動でリネームする | `typescript` | 0 | 2026-08-14 |
| [**herdr-unrecoverable**](https://github.com/neilwashere/herdr-unrecoverable)<br><sub>neilwashere</sub> | ターミナルプロバイダー側のエラーからPiコーディングエージェントのセッションを復旧させる、Herdrのウォッチドッグ | `pi-coding-agent` `javascript` | 0 | 2026-08-14 |
| [**herdr-claude-safe-compact**](https://github.com/tmastalirsch/herdr-claude-safe-compact)<br><sub>tmastalirsch</sub> | herdrプラグイン：アイドル状態のClaude Codeペインをコンパクト化する。ただし引き継ぎ内容が安全にディスクへ保存された後にのみ実行する | `claude-code` `compaction` `shell` | 0 | 🔄 2026-08-31 |
| [**herdr-worktreeinclude**](https://github.com/untalfranfernandez/herdr-worktreeinclude)<br><sub>untalfranfernandez</sub> | 新しいgit worktreeに必要なgitignore対象のローカルファイル（.env、settings.local.json、フィクスチャなど）を自動配置するHerdrプラグイン。.worktreeincludeファイルにgitignore構文で一度宣言しておけば、Herdrが作るworktreeすべてに自動反映… | `claude-code` `dotenv` `git-worktree` `worktree` | 0 | 2026-07-29 |
| [**herdr-padio**](https://github.com/vgreg/herdr-padio)<br><sub>vgreg</sub> | herdrでフォーカスされているペインのアプリに応じて、PadIOコントローラーのモードを自動切り替えする | `game-controller` `macos` `padio` `python` | 0 | 2026-08-02 |
| [**🆕 herdr-space-groups**](https://github.com/yojahny55/herdr-space-groups)<br><sub>yojahny55</sub> | herdrプラグイン：Spaceを名前付き・色分けされたグループにまとめる——ピッカーのポップアップ（マウス＋キーボード対応）、サイドバーのグループ見出し、自動並べ替えに対応 | `javascript` | 0 | 🔄 2026-08-29 |
| [**numberer-manager**](https://github.com/yuritada/numberer-manager)<br><sub>yuritada</sub> | ワークスペースとタブのラベルに、現在のリスト上の位置（例：「1: space」「1: tab」）を自動で先頭に付ける、軽量なHerdrプラグイン | `python` | 0 | 2026-07-25 |
| [**herdr-pane-restart**](https://github.com/zap0xfce2/herdr-pane-restart)<br><sub>zap0xfce2</sub> | サーバー起動時に、名前付きペインで設定済みのコマンドを実行する | `python` | 0 | 2026-08-10 |
| [**herdr-booking-task-plugin**](https://github.com/zerodice0/herdr-booking-task-plugin)<br><sub>zerodice0</sub> | macOSとLinuxで、Herdrエージェントへのプロンプトやローカルのコマンド実行をスケジュールする | `golang` `scheduler` `go` | 0 | 2026-08-03 |

<details><summary>この目的にも関係するもの</summary>

- [freethinkel/herdr-plugin-git-worktree-hooks](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks) — git worktreeの作成/削除時にシェルコマンドを実行する——どのリポジトリの外にも置ける、全プロジェクト共通の1つのYAML設定
- [miko-misa/herdr-portfwd](https://github.com/miko-misa/herdr-portfwd) — リモートマシン上のコーディングエージェント向けの自動SSHポートフォワーディング——エージェントが出力したlocalhost URLをCtrl+クリックすると、同じポートで手元のマシンにページが開く。Herdrプラグイン
- [timofey-TK/herdr-worktree-hooks](https://github.com/timofey-TK/herdr-worktree-hooks) — herdrプラグイン：git worktreeの作成・オープン・削除時に、カスタムのセットアップ/後始末コマンドを実行する
- [itisbryan/herdr-gh-checks](https://github.com/itisbryan/herdr-gh-checks) — herdrプラグイン：現在のPRのCIをペインで監視・確認し、CI/マージ状態をサイドバーの行に表示する。Go + Bubble Tea製
- [akshat12/herdr-muse](https://github.com/akshat12/herdr-muse) — Herdr integration for Muse Code: idle/working/blocked pane state via lifecycle hooks (no Herdr fork needed)
- [elkraps/herdr-telegram-notify](https://github.com/elkraps/herdr-telegram-notify) — Herdrエージェントの状態変化に対する、カスタマイズ可能なTelegram通知——ステータスフィルタ、テンプレート、複数チャットへの配信、重複排除、Codex承認ボタン、完了サマリー、組み込みの診断機能に対応
- [m1sk9/herdr-worktree-hooks-plugin](https://github.com/m1sk9/herdr-worktree-hooks-plugin) — Herdrのworktreeに、カスタマイズ可能なフックを追加するプラグイン
- [Newt6611/herdr-tab-title](https://github.com/Newt6611/herdr-tab-title) — Herdr Tab Titleは、「1. Codex」「2. Terminal」のような、ワークスペース単位できれいに番号付けされた名前にHerdrのタブを自動リネームする。フォーマットはカスタマイズ可能

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-session"></a>

## セッション保存・復元

> 作業を閉じても、あとで同じ状態から再開したい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-resurrect**](https://github.com/ntindle/herdr-resurrect)<br><sub>ntindle</sub> | herdr版tmux-resurrect——ワークスペース・タブ・ペイン・作業ディレクトリ・実行中のプログラムやエージェントをスナップショットし、クラッシュや再起動後に復元する | `crash-recovery` `session-manager` `terminal-multiplexer` `tmux-resurrect` `javascript` | 27 | 🔄 2026-08-24 |
| [**session-digger**](https://github.com/taxueseek/session-digger)<br><sub>taxueseek</sub> | 複数環境をまたいだセッション履歴の掘り出しとナレッジ管理。ログを分析。Claude/Grok/Kimi Code/Codex/WorkBuddy/Trae CNなど主要な環境に対応 | `claude-code` `conversation-analysis` `jsonl` `knowledge-management` `log-analysis` | 17 | 2026-07-21 |
| [**herdr-notes**](https://github.com/alexarthurs/herdr-notes)<br><sub>alexarthurs</sub> | herdr向けの永続化されたMarkdownメモペイン——ワークスペースごとに1つのメモ、プレビュー表示＋編集モード、自動保存で再起動後も残る | `markdown` `notes` `ratatui` `rust` `terminal` | 16 | 2026-07-25 |
| [**herdr-claude-auto-retry**](https://github.com/mo-arvan/herdr-claude-auto-retry)<br><sub>mo-arvan</sub> | AnthropicのレートリミットをやりすごしてClaude Codeを自動的に再開する、herdrネイティブな仕組み——tmuxもシェルラッパーも不要 | `javascript` | 14 | 🔄 2026-09-03 |
| [**herdr-session-parker**](https://github.com/iviaxpow3r/herdr-session-parker)<br><sub>iviaxpow3r</sub> | ペイン/タブを一時保管し、対応するエージェントセッションを後で復元できるHerdrプラグイン | `agent-tools` `python` | 11 | 2026-07-03 |
| [**herdr-agent-inbox**](https://github.com/douglascorrea/herdr-agent-inbox)<br><sub>douglascorrea</sub> | herdrのコーディングエージェント用インボックス——セッションタイトル、既読/未読管理、実行時間、ワークスペース単位の集計、再開可能なチャット履歴 | `ai-agents` `terminal` `python` | 9 | 2026-07-28 |
| [**herdr-assist**](https://github.com/walcew/herdr-assist)<br><sub>walcew</sub> | AIコーディングエージェント向けターミナルマルチプレクサHerdrのための、物理デスクパネル——セッションの状態を色で表示し、エージェントが判断を仰ぐために止まるとベルを鳴らす。ESP32-S3 + LVGL、ビルド済みファームウェア付き | `ai-agents` `claude-code` `coding-agents` `embedded` `esp-idf` | 8 | 🔄 2026-08-27 |
| [**sheep**](https://github.com/gokay-ai/sheep)<br><sub>gokay-ai</sub> | AIコーディングエージェント向けのUndo。エージェントの各ターンが、復元可能なチェックポイントになる | `git` `rust` `tui` `undo` | 5 | 🔄 2026-08-28 |
| [**herdr-oh-my-agent**](https://github.com/GavinTomlins/herdr-oh-my-agent)<br><sub>GavinTomlins</sub> | oh-my-openagentのサブエージェント委任をそれぞれ専用のHerdrペイン/タブにミラー——セッション状態とスクロールバックを保持したままライブ表示 | `typescript` | 4 | 2026-07-31 |
| [**herdr-pane-id-labeler**](https://github.com/4Born/herdr-pane-id-labeler)<br><sub>4Born</sub> | ペインのラベルを、w1:p2のような公開ペインIDと同期させ続けるHerdrプラグイン | `developer-tools` `terminal` `javascript` | 2 | 2026-07-26 |
| [**herdr-hibernate**](https://github.com/bengemine/herdr-hibernate)<br><sub>bengemine</sub> | Herdr上のアイドル状態のコーディングエージェントペイン（Claude Code、Codex、Grok）をハイバネート——メモリを解放し、Enterキーで元のセッションをそのまま再開できる | `claude-code` `python` | 2 | 2026-08-03 |
| [**herdr-synchronize-panes**](https://github.com/furuhashin/herdr-synchronize-panes)<br><sub>furuhashin</sub> | Herdrプラグイン：現在のタブ内のすべてのペインに1つのコマンドを一斉送信する（tmuxのsynchronize-panes風） | `javascript` | 2 | 2026-07-14 |
| [**herdr_sync**](https://github.com/kamaaina/herdr_sync)<br><sub>kamaaina</sub> | herdrのペインを同期する | `zig` | 2 | 2026-07-01 |
| [**herdr-e2b**](https://github.com/tomasvarga/herdr-e2b)<br><sub>tomasvarga</sub> | 必要なときにgit worktreeを新しいE2Bクラウドサンドボックスへミラーする——未コミットの変更も含めたスナップショットをアップロードするだけで、pushやcloneは不要なherdrプラグイン | `cli` `cloud-dev` `e2b` `git-worktree` `sandbox` | 2 | 2026-07-18 |
| [**herdr-thread-to-tab**](https://github.com/toyamarinyon/herdr-thread-to-tab)<br><sub>toyamarinyon</sub> | 単一ペインのHerdrタブラベルを、Claude CodeやCodexのスレッドタイトルと同期させる | `rust` | 2 | 2026-08-06 |
| [**herdr-todos-windows**](https://github.com/aclima01/herdr-todos-windows)<br><sub>aclima01</sub> | herdrエージェントのタスクリスト（TaskCreate/TaskUpdate）をリアルタイムに映し出すパネル。エージェントの計画を追える | `powershell` | 1 | 2026-07-22 |
| [**mo-herdr**](https://github.com/momentohq/mo-herdr)<br><sub>momentohq</sub> | herdrのペイン内でmoを実行——herdr再起動後のセッション復元、起動アクション、SIGKILLによるクリーンアップに対応 | `python` | 1 | 🔄 2026-09-02 |
| [**🆕 herdr-undo-close**](https://github.com/pedroloch/herdr-undo-close)<br><sub>pedroloch</sub> | ブラウザのCmd+Shift+Tのように、herdrで閉じたタブを復元——ラベル、分割比率を含むペイン構成、各ペインの作業ディレクトリ、タブの位置までまとめて復元する | `python` | 1 | 2026-07-30 |
| [**attic**](https://github.com/TheThoughtagen/attic)<br><sub>TheThoughtagen</sub> | アイドル状態のAIコーディングセッションを自動的に閉じるが、その前に必ずアーカイブするので後で復元できる | `claude-code` `developer-tools` `python` `session-management` `tui` | 1 | 2026-08-14 |
| [**herdr-stash**](https://github.com/victor-software-house/herdr-stash)<br><sub>victor-software-house</sub> | Herdrのワークスペースをスタッシュ——エージェントを停止しつつ構成と会話内容は保持し、あとでクリック可能な2カラムポップアップから復元できる | `rust` `terminal` `tui` | 1 | 2026-07-29 |
| [**herdr-agent-pins**](https://github.com/ZingerLittleBee/herdr-agent-pins)<br><sub>ZingerLittleBee</sub> | Herdrのエージェントセッションを、Agentsサイドバーの最上部に永続的にピン留めする | `terminal` `javascript` | 1 | 🔄 2026-08-24 |
| [**herdr-codex-resume**](https://github.com/adamwangxx/herdr-codex-resume)<br><sub>adamwangxx</sub> | ネイティブのCodex resumeピッカーを、Herdrのコンテキストを保ったまま新しいスプリットで開く | `codex-cli` `terminal` `shell` | 0 | 🔄 2026-08-21 |
| [**herdr-agent-resume**](https://github.com/Angel-O/herdr-agent-resume)<br><sub>Angel-O</sub> | AIエージェントのセッションをスムーズに再開できるよう、再開用コマンドを挿入またはコピーするHerdrプラグイン | `rust` | 0 | 2026-08-15 |
| [**herdr-suspend-workspace**](https://github.com/asermax/herdr-suspend-workspace)<br><sub>asermax</sub> | herdrのワークスペースをサスペンド——レイアウトとエージェントをスナップショットして閉じ、あとでポップアップから選んで復元できる | `typescript` | 0 | 2026-07-31 |
| [**herdr-plugin-session-pruner**](https://github.com/Gareth-Rouse/herdr-plugin-session-pruner)<br><sub>Gareth-Rouse</sub> | herdrプラグイン：ワークスペースの最終使用日時を記録してSpacesのサイドバーに経過時間を表示し、使われていないワークスペースをセッション復元の対象から外す | `terminal-multiplexer` `shell` | 0 | 2026-08-07 |
| [**herdr-flakes**](https://github.com/iQua/herdr-flakes)<br><sub>iQua</sub> | Herdr向けのFlakesプラグイン——Flakesの実行状況をローカルのHerdrセッションにミラーし、操作できる | `javascript` | 0 | 2026-07-22 |
| [**🆕 herdr-session-title-name**](https://github.com/jovylle/herdr-session-title-name)<br><sub>jovylle</sub> | herdrプラグイン：terminal_title_strippedをタブに永続化する（session_titleだけを上に残し、閉じた後もタブがそれを保持する） | `sidebar` `terminal` `html` | 0 | 🔄 2026-08-28 |
| [**herdr-plugin-vault**](https://github.com/Joxtacy/herdr-plugin-vault)<br><sub>Joxtacy</sub> | herdrのポップアップから過去のClaude Codeセッションを閲覧し、選んだものを新しいタブで再開する | `shell` | 0 | 2026-08-11 |
| [**🆕 herdr-ccs**](https://github.com/KennethWKZ/herdr-ccs)<br><sub>KennethWKZ</sub> | `ccs claude`を、Herdr上のネイティブClaude Codeのように振る舞わせる——ペイン検出と、ccs経由のランチャーを意識した復元に対応 | `shell` | 0 | 🔄 2026-08-29 |
| [**🆕 herdr-checkpoint**](https://github.com/lancodev/herdr-checkpoint)<br><sub>lancodev</sub> | herdr 版 tmux-resurrect——セッションの状態をそのままチェックポイントとして保存・復元し、チェックポイントに含まれないものは閉じます。 | `tmux-resurrect` `tui` `shell` | 0 | 🔄 2026-09-02 |
| [**herdr-layout**](https://github.com/noviadi/herdr-layout)<br><sub>noviadi</sub> | Herdrのペインレイアウトを保存して再現する。Herdrターミナルマルチプレクサ向けのコンパニオンプラグイン（tmux-resurrect風） | `cli` `terminal` `tmux-resurrect` `shell` | 0 | 2026-08-13 |
| [**🆕 herdr-tab-new**](https://github.com/softwarecrafts/herdr-tab-new)<br><sub>softwarecrafts</sub> | このプロジェクトの herdr ワークスペースで、エージェントセッションを再開または開始します。herdr プラグインであると同時に、herdr の外のターミナルからも使える CLI でもあります。 | `typescript` | 0 | 🔄 2026-08-31 |
| [**herdr-event-log**](https://github.com/waynewu411/herdr-event-log)<br><sub>waynewu411</sub> | herdrプラグイン：pane.agent_status_changed（および今後のイベント種別）を、永続化されカーソルから再開可能なグローバルログに記録する。どの親エージェントからもtailできる | `shell` | 0 | 🔄 2026-08-24 |
| [**live-sync-panes**](https://github.com/wg1k/live-sync-panes)<br><sub>wg1k</sub> | Herdrプラグイン：タブ内のすべてのペインにコマンドを一斉送信、またはキー入力をリアルタイム同期する | `javascript` | 0 | 2026-08-11 |

<details><summary>この目的にも関係するもの</summary>

- [nicosuave/memex](https://github.com/nicosuave/memex) — Claude Code・Codex・Pi・OpenCode・GitHub Copilot・Cursorのトランスクリプトを検索。セッションを再開。トークンを記録
- [KokiKono/herdr-kanban](https://github.com/KokiKono/herdr-kanban) — タスクをherdrのタブに紐付けるターミナル上のカンバンボード。SQLiteに保存される
- [afogel/shepherdr](https://github.com/afogel/shepherdr) — 委任したコーディングエージェントを、監視・再開・引き取りができる可視化されたherdrのペインに追い込むherdrプラグイン
- [AkashJana18/herdr-scratch](https://github.com/AkashJana18/herdr-scratch) — Herdr向けの永続化されたスクラッチパッド。フローティングのユーティリティペインへの足がかりとなる
- [voodootikigod/adlc-herdr](https://github.com/voodootikigod/adlc-herdr) — ADLC向けのherdrプラグイン——ペインごとのフェーズ/チケット/ゲートの状態、バックログボード、ゲートアクション、adlc-fleetの実行状況の可視化に対応。voodootikigod/adlc/plugins…
- [blaxel-ai/herdr-blaxel-sandbox-plugin](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin) — Herdrから、永続化されたBlaxel Sandbox上でコーディングエージェントを実行する
- [LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) — JavaScript/TypeScript向けにHerdrのworktreeを自動でブートストラップ——ロックファイルを考慮したインストールと、安全な環境ファイルの復元に対応
- [ppggff/herdr-plugin](https://github.com/ppggff/herdr-plugin) — 各Herdrペインに適したmacOSの入力方式（IME）を自動的に記憶・復元する
- [shadowfax92/herdr-scratch](https://github.com/shadowfax92/herdr-scratch) — 非公開のtmuxセッションを裏側で使う、永続化されたペインごとのHerdrスクラッチポップアップ
- [damianpoole/herdr-opencode-sessions](https://github.com/damianpoole/herdr-opencode-sessions) — 過去のOpenCodeセッションを、タイトル・プロジェクト・パス・日付・トランスクリプトの内容でファジー検索できるHerdrプラグイン——会話プレビュー付きで、現在または新しいワークスペースでセッションを再開・フォーク…
- [goofansu/herdr-hunk](https://github.com/goofansu/herdr-hunk) — 一時的なHunkオーバーレイを開く、素早いHerdrレビューアクションを提供する。Hunkを終了するとオーバーレイが閉じ、ワークスペースが元に戻る

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-naming"></a>

## タイトル・命名・見た目

> タブ名やターミナルタイトルを自動で分かりやすくしたい / 見た目を変えたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-tab-smart-rename**](https://github.com/iurysza/herdr-tab-smart-rename)<br><sub>iurysza</sub> | Herdrのワークスペース名・タブ名を、コンテキストに応じて自動生成する | `ai` `bun` `terminal` `typescript` | 69 | 2026-08-19 |
| [**herdr-window-title-sync**](https://github.com/rjyo/herdr-window-title-sync)<br><sub>rjyo</sub> | ワークスペース・タブ・エージェントセッションからターミナルのタイトルを同期する（Moshiと併用可） | `moshi` `terminal-title` `javascript` | 35 | 2026-06-26 |
| [**herdr-flock**](https://github.com/ragamo/herdr-flock)<br><sub>ragamo</sub> | AIコーディングエージェントを、見下ろし視点の牧場に住むピクセルアートの羊として可視化するherdrプラグイン | `cli` `ratatui` `rust` `tui` | 31 | 🔄 2026-08-31 |
| [**herdr-claude-session-title**](https://github.com/bcihanc/herdr-claude-session-title)<br><sub>bcihanc</sub> | Herdrプラグイン：Claude Codeのセッションタイトル（/renameまたは自動要約）をherdrのペインのメタデータタイトルに反映する | `shell` | 8 | 2026-07-11 |
| [**herdr-canvas**](https://github.com/aorumbayev/herdr-canvas)<br><sub>aorumbayev</sub> | herdrのエージェント向けの、マウスで操作できるASCII図キャンバス——TUI上で描き、構造化されたJSONを共有し、AIに編集させることもできる | `agentic-ai` `agents` `ai-agents` `ascii-art` `bubbletea` | 7 | 🔄 2026-08-31 |
| [**herdr-pet**](https://github.com/allmight-ai/herdr-pet)<br><sub>allmight-ai</sub> | Herdr向けのコンパニオンV-Pet——あなたのコーディングエージェントの様子を映し出す | `companion` `rust` `v-pet` | 6 | 2026-08-20 |
| [**herdr-icon-agent-ui**](https://github.com/qintmb/herdr-icon-agent-ui)<br><sub>qintmb</sub> | Herdrのサイドバーに、縦位置を揃えたモノクロのAgentアイコンを描画する。ターミナルのキャップハイトに合わせて不均一にスケーリングされたカスタムフォントで描画され、小さな四角として表示される代わりにエージェント名・タブ・ワークスペースラベルにきれいに揃う | `python` | 6 | 🔄 2026-08-20 |
| [**herdr-town**](https://github.com/Efeguclu1/herdr-town)<br><sub>Efeguclu1</sub> | Herdrのコーディングエージェントを、8bit風の街として眺める。街を離れずに、エージェントの発言を読んで返答できる | `ai-agents` `pixel-art` `terminal` `tui` `javascript` | 5 | 2026-08-08 |
| [**herdr-theme-picker**](https://github.com/qintmb/herdr-theme-picker)<br><sub>qintmb</sub> | ターミナルの配色スキームと自分好みのカスタマイズに基づいた、herdr UI向けのテーマピッカー | `shell` | 5 | 🔄 2026-08-31 |
| [**herdr-ghostty-tab-title**](https://github.com/wjarka/herdr-ghostty-tab-title)<br><sub>wjarka</sub> | herdrプラグイン：Ghosttyのタブタイトルに、エージェントの状態別件数（ブロック中/完了/作業中/アイドル）を色分けして表示する | `ai-agents` `ghostty` `terminal` `python` | 5 | 2026-08-04 |
| [**herdr-in-your-face**](https://github.com/JYasha11/herdr-in-your-face)<br><sub>JYasha11</sub> | AIエージェントをブロックされたまま放置すると、巨大なASCIIアートの顔が叫んでくる。無視するほど段階的にエスカレートする | `javascript` | 4 | 2026-07-10 |
| [**herdr-auto-namer**](https://github.com/kakigakki/herdr-auto-namer)<br><sub>kakigakki</sub> | herdr向けのChatGPT風自動命名：エージェントにはClaudeのセッションタイトルを、ワークスペースには作業ディレクトリ名を付ける | `claude-code` `python` | 4 | 🔄 2026-08-27 |
| [**herdr-tab-rename**](https://github.com/lmilojevicc/herdr-tab-rename)<br><sub>lmilojevicc</sub> | 各Herdrタブを、フォーカス中のペインの作業ディレクトリ名に自動でリネームする。手動でリネームしたタブはそのまま残る | `go` | 4 | 2026-07-31 |
| [**herdr-questmancer**](https://github.com/opsydyn/herdr-questmancer)<br><sub>opsydyn</sub> | Herdrのコーディングエージェントのための、居心地の良い16bit風冒険者ギルド。作業中のエージェントはダンジョンに潜り、ブロックされたエージェントは助言を求め、完了した仕事は戦利品を持って帰ってくる | `coding-agents` `pixel-art` `ratatui` `tui` `rust` | 4 | 2026-08-11 |
| [**herdr-nerd-font-tab-name**](https://github.com/rohankewal/herdr-nerd-font-tab-name)<br><sub>rohankewal</sub> | herdrのタブにNerd Fontアイコンを付ける——joshmedeski/tmux-nerd-font-window-nameのherdr移植版 | `nerd-fonts` `python` `terminal` `tui` | 4 | 2026-07-31 |
| [**herdr-pet**](https://github.com/nikok6/herdr-pet)<br><sub>nikok6</sub> | herdrのペインにいる小さなデスクペット——エージェントと一緒にタイプし、待ち、お祝いする。任意のCodex petに対応 | `rust` | 3 | 🔄 2026-08-26 |
| [**🆕 herdr-pets**](https://github.com/abhishek944/herdr-pets)<br><sub>abhishek944</sub> | 稼働中の Herdr エージェントたちを、デスクトップに浮かぶ透明な村として表示します。 | `typescript` | 2 | 🔄 2026-08-31 |
| [**herdr-titles**](https://github.com/davidolrik/herdr-titles)<br><sub>davidolrik</sub> | 追従し続けるHerdrのタイトル。herdr-titlesは、AIエージェントのライブなセッションタイトルも含め、実際に動いているものに合わせてタブとウィンドウの名前を付け、ワークスペース・タブ・エージェントの要対応件数・シェル環境から、小さなHCLテンプレート経由でウィンドウタイトルを組み立てる。即座に反映され、C… | `ai-assisted` `go` | 2 | 2026-08-18 |
| [**herdr-english-coach**](https://github.com/GranamyrBR/herdr-english-coach)<br><sub>GranamyrBR</sub> | herdrプラグイン：色分けされた英語修正ボード——作業中、コーディングエージェントが文法や開発用語の修正をリアルタイムでサイドペインに記録する | `english` `language-learning` `shell` | 2 | 2026-07-06 |
| [**herdr-ai-tab-name**](https://github.com/ndom91/herdr-ai-tab-name)<br><sub>ndom91</sub> | ローカルLLMを使ってHerdrのタブ名を自動命名する | `local-llm` `python` | 2 | 2026-08-05 |
| [**herdr-powershell-title-sync**](https://github.com/aclima01/herdr-powershell-title-sync)<br><sub>aclima01</sub> | window-title-syncのWindows/PowerShell版：ターミナルのタイトルを、フォーカス中のherdrセッションに同期する | `powershell` | 1 | 2026-07-20 |
| [**herdr-git-tab-name**](https://github.com/blurname/herdr-git-tab-name)<br><sub>blurname</sub> | フォーカス中のペインのGitブランチ名にタブをリネームするHerdrプラグイン | `shell` | 1 | 2026-07-06 |
| [**herdr-hermes-session-title**](https://github.com/btorresgil/herdr-hermes-session-title)<br><sub>btorresgil</sub> | Hermes Agentのセッションタイトルを、Herdrのサイドバーに表示する | `python` | 1 | 2026-08-07 |
| [**herdr-tab-smart-rename-rs**](https://github.com/EmmetZ/herdr-tab-smart-rename-rs)<br><sub>EmmetZ</sub> | _(説明なし)_ | `rust` | 1 | 🔄 2026-08-24 |
| [**🆕 herdr-agent-titler**](https://github.com/killerz3/herdr-agent-titler)<br><sub>killerz3</sub> | 外部 API キーを使わず、ローカルの agy・claude・codex・opencode の各ハーネスを使って Herdr のタブに自動でタイトルを付けます。 | `antigravity` `claude-code` `python` | 1 | 🔄 2026-09-03 |
| [**herdr-tab-title-sync**](https://github.com/lucasleon2107/herdr-tab-title-sync)<br><sub>lucasleon2107</sub> | AIエージェントの会話タイトルにタブ名を同期するherdrプラグイン | `ai-agents` `claude-code` `terminal` `tmux` `shell` | 1 | 2026-08-04 |
| [**🆕 herdr-session-sync**](https://github.com/nengqi/herdr-session-sync)<br><sub>nengqi</sub> | Claude Code・Codex・エージェントのセッション名を、Herdrのペインラベル・PTYのウィンドウタイトル・モバイルコンパニオンアプリ（Heeler）にまたがって自動同期する | `agent` `claude-code` `codex` `heeler` `terminal-multiplexer` | 1 | 🔄 2026-09-03 |
| [**herdr-nerd-font-tab-name-windows**](https://github.com/Only-Moon/herdr-nerd-font-tab-name-windows)<br><sub>Only-Moon</sub> | herdr-nerd-font-tab-nameのWindows移植版：herdrのタブにNerd Fontアイコンを表示し、Windows・macOS・Linuxをクロスプラットフォームでサポート、フォルダに応じたアイコン解決にも対応 | `herdr-windows` `icons` `nerd-fonts` `python` `title` | 1 | 2026-08-10 |
| [**herdr-tab-renamer**](https://github.com/ryanlewis/herdr-tab-renamer)<br><sub>ryanlewis</sub> | herdrプラグイン：タブに実際の中身（エージェントのセッションタイトルやシェルのディレクトリ）に応じたラベルを付ける | `javascript` | 1 | 2026-08-08 |
| [**herdr-claude-tab-title**](https://github.com/tmn73/herdr-claude-tab-title)<br><sub>tmn73</sub> | 各Claude Codeのセッションタイトルとエージェントの状態を、対応するHerdrのタブに反映する | `claude-code` `tabs` `terminal` `typescript` | 1 | 🔄 2026-08-27 |
| [**workspace-basename**](https://github.com/42lizard/workspace-basename)<br><sub>42lizard</sub> | ワークスペース作成時のcwdのベースネームに基づいて、ワークスペース名を設定するherdrプラグイン | `shell` | 0 | 🔄 2026-08-27 |
| [**herdr-habitat**](https://github.com/chantlong/herdr-habitat)<br><sub>chantlong</sub> | herdr habitatは、エージェントの作業とともに育っていく生きたターミナル生態系。育てるには時間がかかるので、エージェントを詰め込みすぎないように。エージェントがエネルギーを大量消費するデータセンターでトークンを燃やし生態系を傷つける一方で、herdr habitatは皮肉にも仮想の植物を育て、仮想の野生生物… | `chill` `cozy` `javascript` | 0 | 2026-08-16 |
| [**herdr-tab-title-from-terminal**](https://github.com/christiangroth/herdr-tab-title-from-terminal)<br><sub>christiangroth</sub> | すべてのHerdrタブに、中で動いているエージェントのターミナルタイトルをそのまま名前として付ける。Claude Codeで/renameを1回実行すれば、セッションとタブの両方に名前が付く。手動で名前を付けたタブには手を出さない | `python` | 0 | 🔄 2026-08-25 |
| [**herdr-llm-summary-header**](https://github.com/dnf0/herdr-llm-summary-header)<br><sub>dnf0</sub> | herdrプラグイン：エージェントが完了すると、LLMによる一行要約をペインのタイトルに書き込む | `javascript` | 0 | 2026-08-03 |
| [**herdr-smart-rename**](https://github.com/edouard-andrei/herdr-smart-rename)<br><sub>edouard-andrei</sub> | herdrプラグイン：エージェントのトランスクリプトから、AIがタブとペインの名前を付ける——キー1つで、OpenAI互換の任意のモデルを使用可能 | `javascript` | 0 | 🔄 2026-08-20 |
| [**herdr-title-sync**](https://github.com/elKei24/herdr-title-sync)<br><sub>elKei24</sub> | herdrプラグイン：各エージェントのターミナルタイトルを、そのタブのラベルに反映する | `python` | 0 | 🔄 2026-09-01 |
| [**🆕 herdr-kitty-theme-sync**](https://github.com/enisbu/herdr-kitty-theme-sync)<br><sub>enisbu</sub> | Herdr で使用中のテーマを kitty の ANSI パレットに反映し、ペインの表示内容を Herdr の外観と一致させます。 | `kitty` `linux` `terminal` `theme` `shell` | 0 | 🔄 2026-09-03 |
| [**🆕 herdr-pane-id-border**](https://github.com/Haichiu/herdr-pane-id-border)<br><sub>Haichiu</sub> | ペインの境界線に正規のペイン ID を表示する、ミニマルな Herdr プラグインです。 | `shell` | 0 | 🔄 2026-09-02 |
| [**🆕 herdr-sheep**](https://github.com/huketo/herdr-sheep)<br><sub>huketo</sub> | Herdr のコーディングエージェントを、アニメーションする ASCII アートの羊の群れとして眺められます。 | `ascii-art` `rust` `tui` | 0 | 🔄 2026-08-31 |
| [**herdr-tab-session-name-sync**](https://github.com/itayo-m/herdr-tab-session-name-sync)<br><sub>itayo-m</sub> | エージェントのセッション名を、herdrのタブとペインのタイトルに同期する | `developer-tools` `github-copilot` `terminal` `javascript` | 0 | 2026-08-03 |
| [**herdr-chromatic-spaces**](https://github.com/jackfrancisdalton/herdr-chromatic-spaces)<br><sub>jackfrancisdalton</sub> | 各Herdr Spaceに独自の色と絵文字を付ける——サイドバーの色付きドット、エージェントのグループ化、Space切り替え時の任意のクローム着色に対応 | `python` | 0 | 🔄 2026-08-22 |
| [**🆕 herdr-tab-titles**](https://github.com/kewah/herdr-tab-titles)<br><sub>kewah</sub> | 最初のコーディングエージェントへのプロンプトをもとに、ペインとタブに名前を付ける Herdr プラグインです。 | `javascript` | 0 | 🔄 2026-09-01 |
| [**herdr-tab-numbers**](https://github.com/kokatsu/herdr-tab-numbers)<br><sub>kokatsu</sub> | 各タブの名前の先頭に、switch_tabの位置番号を付ける | `shell` | 0 | 🔄 2026-08-26 |
| [**herdr-window-title**](https://github.com/mackt/herdr-window-title)<br><sub>mackt</sub> | herdr向けの設定可能な外部ターミナルタイトル——テンプレート駆動でセッションを認識し、エージェントの状態（ブロック/完了/作業中）をリアルタイム表示する | `rust` | 0 | 2026-08-03 |
| [**herdr-agent-smart-rename**](https://github.com/malone-c/herdr-agent-smart-rename)<br><sub>malone-c</sub> | 各herdrエージェントセッションの名前を、実際にやっていることから付ける | `python` | 0 | 2026-08-14 |
| [**herdr-machine-title**](https://github.com/mikevalstar/herdr-machine-title)<br><sub>mikevalstar</sub> | herdrプラグイン：外側のターミナルタイトルを「herdr@<ホスト名>・<ワークスペース>」に固定する | `shell` | 0 | 2026-07-02 |
| [**🆕 herdr-tab-title**](https://github.com/Newt6611/herdr-tab-title)<br><sub>Newt6611</sub> | Herdr Tab Titleは、「1. Codex」「2. Terminal」のような、ワークスペース単位できれいに番号付けされた名前にHerdrのタブを自動リネームする。フォーマットはカスタマイズ可能 | `rust` | 0 | 2026-07-09 |
| [**🆕 herdr-display-workspace**](https://github.com/RickyMarou/herdr-display-workspace)<br><sub>RickyMarou</sub> | Herdr プラグイン：現在のワークスペース名をタブバーの右側に表示します。 | `shell` | 0 | 🔄 2026-09-03 |
| [**tab-blank-number**](https://github.com/riq0h/tab-blank-number)<br><sub>riq0h</sub> | herdrのデフォルトの数字タブラベル（1、2、3…）を空白にするherdrプラグイン | `javascript` | 0 | 2026-07-19 |
| [**tab-process-name**](https://github.com/riq0h/tab-process-name)<br><sub>riq0h</sub> | 各タブにフォアグラウンドで動いているプロセス名をラベル表示するherdrプラグイン——tmuxのautomatic-rename相当の機能をherdr向けに | `javascript` | 0 | 2026-07-19 |
| [**herdr-workspace-renamer**](https://github.com/ryanlewis/herdr-workspace-renamer)<br><sub>ryanlewis</sub> | herdrプラグイン：エージェントのセッション名をワークスペースのラベルに同期する | `javascript` | 0 | 2026-08-08 |
| [**herdr-codex-session-title**](https://github.com/sergeybataev/herdr-codex-session-title)<br><sub>sergeybataev</sub> | Codexのチャットタイトルをエージェント名に反映するHerdrプラグイン | `codex` `python` | 0 | 2026-08-01 |
| [**🆕 herdr-plugins**](https://github.com/shubham-cpp/herdr-plugins)<br><sub>shubham-cpp</sub> | タブ・エージェントの命名と、方向キーによるペインフォーカスのための Herdr プラグイン集です。 | `rust` | 0 | 🔄 2026-09-03 |
| [**herdr-title-wrap**](https://github.com/T0mSIlver/herdr-title-wrap)<br><sub>T0mSIlver</sub> | herdrプラグイン：Claude Codeのセッションタイトルをサイドバーの複数行に折り返し、サイドバー幅に自動フィットさせる | `python` | 0 | 2026-08-06 |
| [**herdr-agent-session-title**](https://github.com/the-inconvenience-store/herdr-agent-session-title)<br><sub>the-inconvenience-store</sub> | Claude CodeまたはCodexのセッションタイトル（/renameまたは自動要約）を、herdrペインのメタデータタイトルに反映するHerdrプラグイン | `python` | 0 | 🔄 2026-09-04 |
| [**herdr-ghostty-theme-sync**](https://github.com/themuuln/herdr-ghostty-theme-sync)<br><sub>themuuln</sub> | herdrのテーマとサイドバーの配色を、使用中のGhosttyのテーマに合わせる——herdr再起動をまたいでもサイドバーのトークン（配色設定）を維持する。herdr.dev製プラグイン | `python` | 0 | 2026-08-12 |
| [**tabby**](https://github.com/yersonargotev/tabby)<br><sub>yersonargotev</sub> | フォーカス中のタブに、重要なコマンドまたは作業ディレクトリ名でラベルを付けるHerdrプラグイン | `rust` | 0 | 🔄 2026-08-20 |
| [**herdr-auto-session-title**](https://github.com/zhangzujian/herdr-auto-session-title)<br><sub>zhangzujian</sub> | 簡潔なHerdrペインタイトルを生成し、ネイティブのCodexスレッド名と同期する | `javascript` | 0 | 2026-07-30 |

<details><summary>この目的にも関係するもの</summary>

- [qu8n/herdr-automatic-rename](https://github.com/qu8n/herdr-automatic-rename) — Smart tab names and numbered labels for a smooth herdr navigation
- [kryptamine/herdr-auto-title](https://github.com/kryptamine/herdr-auto-title) — 各タブでの作業内容に自動で追従するタブタイトル。Herdr でタブを整理された状態に保ち、何をしているかが一目でわかります。
- [sh1ma/herdr-auto-title](https://github.com/sh1ma/herdr-auto-title) — Claude CodeとCodexの会話内容から、herdrのタブタイトルを自動生成する
- [wyattjoh/herdr-plugin-renamer](https://github.com/wyattjoh/herdr-plugin-renamer) — エージェントへの最初のプロンプトから、自動生成されたherdrのworktreeブランチとワークスペースをリネームする（デバイス上のApple FoundationModelsまたはCodexを利用）
- [ythx-101/herdr-social-glass](https://github.com/ythx-101/herdr-social-glass) — macOS版Herdr向けの、スクリーンショット映えするSocial Glassテーマ＆ワークフロープラグイン
- [aarsh21/herdr-tab-title](https://github.com/aarsh21/herdr-tab-title) — Herdr向けの、tmux風タブタイトルの自動設定
- [IvoryHeart/herdr-world](https://github.com/IvoryHeart/herdr-world) — Herdr World——Herdr向けのマルチサーフェスなWeb体験
- [funsaized/herdr-mise](https://github.com/funsaized/herdr-mise) — プロンプトではなく「一手」を回す🧑‍🍳 herdr内のエージェント向けビジュアライザー
- [suisya-systems/herdr-agent-office](https://github.com/suisya-systems/herdr-agent-office) — エージェント群をピクセルアートのオフィスとして表示するherdrプラグイン。誰が作業中で、誰が詰まっているかが分かり、そこにジャンプできる
- [maedana/herdr-whereami](https://github.com/maedana/herdr-whereami) — 今どこにいるかを示すよう、タブを自動でリネームするHerdrプラグイン——gitリポジトリ内なら「リポジトリ名/ブランチ名」のように表示
- [dev-shimada/herdr-auto-tab-name](https://github.com/dev-shimada/herdr-auto-tab-name) — herdrプラグイン：タブに現在のディレクトリ名を自動で付ける
- [winoooops/herdr-agent-title-sync](https://github.com/winoooops/herdr-agent-title-sync) — Claude Code・Codex・Kimi Code・OpenCodeなど各種コーディングエージェント向けの、Herdrペインタイトル自動同期
- [eduardoborges/herdr-claude-title-hook](https://github.com/eduardoborges/herdr-claude-title-hook) — セッションタイトルをHerdrのタブタイトルに同期するClaude Codeプラグイン
- [filoozom/herdr-title](https://github.com/filoozom/herdr-title) — 選択中のworktreeとエージェントの活動状況を、ターミナルのタブタイトルに表示するHerdrプラグイン
- [go-min/herdr-pane-name](https://github.com/go-min/herdr-pane-name) — ターミナルセッションのペインに自動で名前を付けるHerdrプラグイン
- [jovylle/herdr-session-title-name](https://github.com/jovylle/herdr-session-title-name) — herdrプラグイン：terminal_title_strippedをタブに永続化する（session_titleだけを上に残し、閉じた後もタブがそれを保持する）
- [KazBrekker1/herdr-hasr](https://github.com/KazBrekker1/herdr-hasr) — Hasr（حصر — 「列挙・完全な集計」の意）——herdr向けのgoto風ポップアップ切り替えツール：エージェント・タブ・スペースの切り替え・リネーム・削除・作成ができ、完了状況もリアルタイムに追跡する
- [khatriafaz/herdr-plugin-auto-rename](https://github.com/khatriafaz/herdr-plugin-auto-rename) — Piセッションへの最初のプロンプトから、新しいHerdrのワークスペースとGitブランチを自動でリネームする
- [maxBRT/herdr-omarchy-theme-sync](https://github.com/maxBRT/herdr-omarchy-theme-sync) — HerdrのUIパレットを、現在使用中のOmarchyテーマに同期させる
- [ralphilius/herdr-pr-tab-renamer](https://github.com/ralphilius/herdr-pr-tab-renamer) — 検出したプルリクエスト番号でタブ名を変更するHerdrプラグイン

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-text"></a>

## テキスト・URL 抽出

> 画面に出ている文字列やパス・URL を、マウスなしで拾いたい

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**herdr-pluck**](https://github.com/rmarganti/herdr-pluck)<br><sub>rmarganti</sub> | Herdrのペインからパターンにマッチした文字列をすばやくコピーする | `rust` | 23 | 2026-08-07 |
| [**herdr-tiny-fingers**](https://github.com/hotchpotch/herdr-tiny-fingers)<br><sub>hotchpotch</sub> | Herdr向けの、tmux-fingers風の画面上コピーヒント表示 | `tools` `rust` | 9 | 2026-08-04 |
| [**herdr-scratchpad**](https://github.com/vjeantet/herdr-scratchpad)<br><sub>vjeantet</sub> | タブごとに1つのバッファでプロンプトを準備し、1キーでエージェントの入力欄に流し込む | `clipboard` `ratatui` `rust` `scratchpad` `terminal` | 5 | 🔄 2026-08-31 |
| [**herdr-fingers**](https://github.com/hitaishi2222/herdr-fingers)<br><sub>hitaishi2222</sub> | Fingers to clipboard：現在のペインから情報を選び取る、スマートなオーバーレイ | `python` | 4 | 2026-07-16 |
| [**herdr-copy-search**](https://github.com/qq88976321/herdr-copy-search)<br><sub>qq88976321</sub> | herdrのスクロールバックに対する正規表現・copycatパターン検索とextraktoによるトークン抽出、tmux風のコピーモード（OSC 52）に対応 | `copy-mode` `rust` `terminal` `tmux` | 3 | 2026-08-04 |
| [**herdr-flash**](https://github.com/youguanxinqing/herdr-flash)<br><sub>youguanxinqing</sub> | Herdrのペイン向けの、flash.nvim風の検索・選択・ヤンク | `rust` `terminal` | 3 | 🔄 2026-09-02 |
| [**herdr-agent-copy-paste-fork**](https://github.com/calebcauthon/herdr-agent-copy-paste-fork)<br><sub>calebcauthon</sub> | コピー＆ペーストだけでフォークできる、あるいはホットキーで新しいペインにフォークする | `claude-code` `codex` `shell` | 2 | 2026-07-24 |
| [**herdr-paste-image**](https://github.com/ddfonseca/herdr-paste-image)<br><sub>ddfonseca</sub> | クリップボードの画像をherdrのペインにファイルパスとして貼り付ける——tmux-paste-imageのherdr移植版 | `shell` | 2 | 2026-07-30 |
| [**herdr-s3-clipboard**](https://github.com/jagzmz/herdr-s3-clipboard)<br><sub>jagzmz</sub> | S3互換ストレージを使い、Herdrからクリップボードの画像を再利用可能な公開URLまたは署名付きURLとして公開する | `aws-s3` `clipboard` `cloudflare-r2` `developer-tools` `image-publishing` | 2 | 2026-07-16 |
| [**🆕 herdr-ferry**](https://github.com/wavrin/herdr-ferry)<br><sub>wavrin</sub> | SSH経由で、Herdrのbox（マシン）とノートPCの間でファイルとクリップボードをやり取りする——クラウドバケット不要 | `rust` | 2 | 🔄 2026-08-29 |
| [**herdr-scrollback-capture**](https://github.com/alexjsp/herdr-scrollback-capture)<br><sub>alexjsp</sub> | フォーカス中のペインのスクロールバックを、HTMLまたはテキストとしてデスクトップに保存するHerdrプラグイン | `shell` | 1 | 2026-06-30 |
| [**herdr-leap**](https://github.com/RooseveltAdvisors/herdr-leap)<br><sub>RooseveltAdvisors</sub> | Herdrのターミナルマルチプレクサ向けの、EasyMotion/leap風の文字ジャンプ＋選択コピー | `easymotion` `rust` `terminal` `tui` | 1 | 2026-07-24 |
| [**🆕 herdr-copy-hints**](https://github.com/rotemb-wond/herdr-copy-hints)<br><sub>rotemb-wond</sub> | Herdr向けの、tmux-fingers風キーボードコピーヒント：パス・GitのSHA・URLなどに対応 | `clipboard` `developer-tools` `keyboard-navigation` `productivity` `terminal` | 1 | 2026-07-23 |
| [**herdr-translate**](https://github.com/zackshen/herdr-translate)<br><sub>zackshen</sub> | herdrプラグイン：マウスで選択したターミナルのテキストを、中央のポップオーバーで翻訳する | `rust` | 1 | 🔄 2026-08-25 |
| [**herdr-quickselect**](https://github.com/choplin/herdr-quickselect)<br><sub>choplin</sub> | Herdrで画面に見えているターミナルのテキストを選択し、設定可能なアクションを実行する | `go` | 0 | 🔄 2026-08-24 |
| [**herdr-flash**](https://github.com/codingfragments/herdr-flash)<br><sub>codingfragments</sub> | zellij-flash（Zellijのプラグイン）を、ネイティブなHerdrプラグインとして移植したもの | `rust` | 0 | 🔄 2026-08-26 |
| [**herdr-zextract**](https://github.com/codingfragments/herdr-zextract)<br><sub>codingfragments</sub> | zextract（Zellijのプラグイン）を、ネイティブなHerdrプラグインとして移植したもの | `rust` | 0 | 2026-08-18 |
| [**herdr-vaultr**](https://github.com/connerohnesorge/herdr-vaultr)<br><sub>connerohnesorge</sub> | vaultrの公式herdrプラグイン——キャプチャしたエージェントセッションを、実行元のペインからコピー・表示・フォーク・検索できる | `vaultr` `shell` | 0 | 2026-08-13 |
| [**herdr-context-locator**](https://github.com/Dimon94/herdr-context-locator)<br><sub>Dimon94</sub> | Herdrエージェントの正規のネイティブセッションコンテキストを指す、自己記述型のロケーターをコピーする | `python` | 0 | 🔄 2026-08-26 |
| [**🆕 herdr-agent-links**](https://github.com/OmarDadabhoy/herdr-agent-links)<br><sub>OmarDadabhoy</sub> | Herdr 内の Codex や Claude の出力にある、Markdown ラベルの裏に隠れたリンクを開けます。 | `claude-code` `codex` `productivity` `terminal` `python` | 0 | 🔄 2026-09-02 |
| [**herdr-thumbs**](https://github.com/sd2k/herdr-thumbs)<br><sub>sd2k</sub> | Herdr版tmux-thumbs——画面上の何でもヒント選択でき、コピー・貼り付け・オープンができる | `tmux-thumbs` `shell` | 0 | 🔄 2026-08-21 |
| [**🆕 herdr-copy-conversation**](https://github.com/testy-cool/herdr-copy-conversation)<br><sub>testy-cool</sub> | Herdr 内で、ターミナルのスクロールバック全体やエージェントとの会話を、そのままクリップボードにコピーできます。 | `ai-agents` `claude-code` `clipboard` `codex` `developer-tools` | 0 | 🔄 2026-09-03 |
| [**herdr-lens**](https://github.com/VoidAxon/herdr-lens)<br><sub>VoidAxon</sub> | Herdrのペインでテキストを選択し、キーを押すと自分の言語で読める。翻訳・辞書引き・識別子の検索・要約に対応——標準ライブラリのみ、設定不要 | `ai` `cli` `terminal` `translation` `python` | 0 | 🔄 2026-08-25 |
| [**herdr-translate**](https://github.com/wenPKtalk/herdr-translate)<br><sub>wenPKtalk</sub> | herdrプラグイン：ペイン内で選択したテキストをtranslate-shellで翻訳し、フローティングポップアップで表示する（macOS・Linux対応） | `translate` `shell` | 0 | 2026-08-19 |
| [**herdr-copy-pane-id**](https://github.com/wine-fall/herdr-copy-pane-id)<br><sub>wine-fall</sub> | herdrプラグイン：フォーカス中のペインのIDをクリップボードにコピーする、または全ペインのIDを枠に表示する | `cli` `terminal` `python` | 0 | 🔄 2026-08-24 |

<details><summary>この目的にも関係するもの</summary>

- [nicosuave/memex](https://github.com/nicosuave/memex) — Claude Code・Codex・Pi・OpenCode・GitHub Copilot・Cursorのトランスクリプトを検索。セッションを再開。トークンを記録
- [iurysza/termscope](https://github.com/iurysza/termscope) — 分割ペインで、ターミナル画面に表示されているファイルやリンクを開く
- [jlimas/herdr-worktree-seed](https://github.com/jlimas/herdr-worktree-seed) — コピーオンライトのnode_modulesと設定可能なローカルdotfilesを、新しいworktreeに投入するHerdrプラグイン
- [tanshio/herdr-worktreeinclude](https://github.com/tanshio/herdr-worktreeinclude) — Herdrプラグイン：.worktreeincludeにマッチするgit管理外ファイルを、新しく作成されたworktreeにコピーする
- [shadowfax92/herdr-comments](https://github.com/shadowfax92/herdr-comments) — コピーしたHerdrのターミナル出力に注釈を付け、ペインごとのコメントを収集してNeovimでレビューできる
- [crexi/herdr-worktree-copy](https://github.com/crexi/herdr-worktree-copy) — .worktree-copyマニフェストに基づき、worktreeローカルファイルをコピー・シンボリックリンクするHerdrプラグイン
- [Feasy01/herdr-allow](https://github.com/Feasy01/herdr-allow) — herdrプラグイン：.herdr-allowの許可リストを使って、gitignore対象のファイル（.env、シークレット、ローカル設定）を新しいworktreeすべてにコピーする
- [Angel-O/herdr-agent-resume](https://github.com/Angel-O/herdr-agent-resume) — AIエージェントのセッションをスムーズに再開できるよう、再開用コマンドを挿入またはコピーするHerdrプラグイン
- [eightHundreds/herdr-worktreeinclude](https://github.com/eightHundreds/herdr-worktreeinclude) — Herdrプラグイン：.worktreeincludeで指定したgit管理外ファイルを、新しいworktreeにコピーする
- [itayo-m/herdr-tab-session-name-sync](https://github.com/itayo-m/herdr-tab-session-name-sync) — エージェントのセッション名を、herdrのタブとペインのタイトルに同期する
- [jtnovellis/herdr-worktree-setup](https://github.com/jtnovellis/herdr-worktree-setup) — herdrプラグイン：新しいgit worktreeをすぐに使える状態にする——.envと開発状態のコピー、依存関係キャッシュのクローン（APFS/reflink）、mise trust、direnv allow、依存…
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
| [**herdr-plus**](https://github.com/cloudmanic/herdr-plus)<br><sub>cloudmanic</sub> | herdr向けの拡張機能。正式なプラグインとして構築されたツール集（プロジェクト管理とクイックアクション）でherdrをより良くする | `go` | 286 | 🔄 2026-09-03 |
| [**herdr-lazy**](https://github.com/natori-hrj/herdr-lazy)<br><sub>natori-hrj</sub> | herdr向けの宣言的なプラグインマネージャー兼キュレーション済みディストリビューション——1つのリスト、実体のあるロックファイル、管理用ペイン | `cli` `lockfile` `plugin-manager` `rust` `terminal` | 22 | 🔄 2026-09-01 |
| [**herdr-plugin-manager**](https://github.com/speardragon/herdr-plugin-manager)<br><sub>speardragon</sub> | ポップアップからherdrのプラグインを管理——インストール・更新・有効/無効化・アンインストール、herdr-pluginマーケットプレイスの閲覧も可能。推奨キー：prefix+p | `plugin-manager` `tui` `shell` | 22 | 🔄 2026-09-04 |
| [**house-of-herdr**](https://github.com/alasano/house-of-herdr)<br><sub>alasano</sub> | Herdr向けのプラグイン集——Work Louder Codex Micro上にエージェントのステータスランプと操作パネルを表示するCodex Microを含む | `codex-micro` `work-louder` `typescript` | 4 | 2026-08-13 |
| [**herdr-plugin-rust**](https://github.com/Newt6611/herdr-plugin-rust)<br><sub>Newt6611</sub> | Herdrのプラグインを構築するためのRustアプリケーションフレームワーク | `rust` | 2 | 2026-07-09 |
| [**herdr-plugins**](https://github.com/alastairsounds/herdr-plugins)<br><sub>alastairsounds</sub> | herdr向けのプラグイン集 | `rust` | 1 | 🔄 2026-08-28 |
| [**herdr-plugins-labs**](https://github.com/hmu332233/herdr-plugins-labs)<br><sub>hmu332233</sub> | Herdr向けの実験的プラグイン集——ここで育て、成熟したら独立したリポジトリに卒業する | `labs` `javascript` | 1 | 🔄 2026-08-24 |
| [**herdr-plugin-manager**](https://github.com/a-curious-coder/herdr-plugin-manager)<br><sub>a-curious-coder</sub> | 1つのポップアップペインからherdrプラグインを管理・発見する——インストール/アンインストール/更新、アクションの実行やバインド、公開レジストリの閲覧ができる | `shell` | 0 | 2026-08-13 |
| [**herdr-plugins**](https://github.com/tyler-jewell/herdr-plugins)<br><sub>tyler-jewell</sub> | Rustのみで書かれたHerdrプラグインのモノレポ（標準ライブラリ優先）。インストールは herdr plugin install tyler-jewell/herdr-plugins/<subdir> で行う | `rust` `go` | 0 | 2026-08-10 |

<details><summary>この目的にも関係するもの</summary>

- [JefeLabs/herdr-web-broker](https://github.com/JefeLabs/herdr-web-broker) — herdr向けの自己ホスト型REST/WS API——どこからでもコーディングエージェントを起動・操作できる。トークン、マルチユーザーのセッション所有権、gitコマンド、イベントストリーミング、親子間フェデレーションに…

</details>

[⬆ 目的一覧に戻る](#purposes)

<a id="cat-other"></a>

## その他・ユーティリティ

> 上のどれにも当てはまらない便利もの

| プラグイン | できること | タグ | ★ | 最終更新 |
| --- | --- | --- | --: | --- |
| [**terminal-browser**](https://github.com/zenbu-labs/terminal-browser)<br><sub>zenbu-labs</sub> | ターミナルの中のブラウザ | `browser` `claude-code` `claude-skills` `cli` `codex` | 2571 | 🔄 2026-09-03 |
| [**herdr-lantern**](https://github.com/aigorahub/herdr-lantern)<br><sub>aigorahub</sub> | Lantern（Elves製）。Herdrプラグイン：群れは野に出ている——Lanternは、誰があなたを必要としていて、何に向けて作業しているのかを照らし出す | `shell` | 61 | 🔄 2026-08-26 |
| [**herdr-plugins-directory**](https://github.com/MIDO-ruby7/herdr-plugins-directory)<br><sub>MIDO-ruby7</sub> | やりたいことからherdrプラグインを探せるリンク集 | `python` | 10 | 🔄 2026-09-03 |
| [**neon-herdr**](https://github.com/neon-solutions/neon-herdr)<br><sub>neon-solutions</sub> | Neon公式のHerdrプラグイン | `typescript` | 10 | 2026-08-06 |
| [**herdr-commandcode-plugin**](https://github.com/TheMetalStorm/herdr-commandcode-plugin)<br><sub>TheMetalStorm</sub> | CommandcodeをHerdrに統合する | `cli` `commandcode` `herdr-integration` `shell` | 7 | 2026-07-30 |
| [**herdr-plugin-cmux**](https://github.com/lachieh/herdr-plugin-cmux)<br><sub>lachieh</sub> | herdrが管理するすべてのエージェントを、cmuxのサイドバーにそれぞれ独立した行としてミラーする——ステータスピルとクリックでジャンプできるタスク行付き | `javascript` | 6 | 2026-07-01 |
| [**wave-tui**](https://github.com/takemo101/wave-tui)<br><sub>takemo101</sub> | 作業中に流せる、静かなターミナルラジオ | `rust` | 4 | 2026-07-20 |
| [**herdr-freebuff-plugin**](https://github.com/TheMetalStorm/herdr-freebuff-plugin)<br><sub>TheMetalStorm</sub> | Herdr向けのFreebuffライフサイクル統合プラグイン——ファイルのポーリングとPTY内容のスクレイピングで、アイドル/作業中/ブロック中の状態を報告する | `cli` `freebuff` `herdr-integration` `shell` | 4 | 2026-07-22 |
| [**herdr-memory**](https://github.com/jatingargiitk/herdr-memory)<br><sub>jatingargiitk</sub> | コーディングセッションから「生きた脳」を構築するHerdrプラグイン——うまくいったこと、失敗したこと、あなたが下した判断を少しずつ学習していく | `shell` | 3 | 2026-08-11 |
| [**🆕 herdrctx**](https://github.com/j0urneyk/herdrctx)<br><sub>j0urneyk</sub> | ローカルの Herdr セッションを管理するためのターミナル UI です。 | `go` | 2 | 🔄 2026-09-02 |
| [**herdr-standup**](https://github.com/neospeed83/herdr-standup)<br><sub>neospeed83</sub> | Gitの活動とHerdrのコンテキストから、証跡に基づいたデイリースタンドアップを作成する | `developer-tools` `standup` `rust` | 2 | 🔄 2026-08-31 |
| [**herdr-streamdeck**](https://github.com/Pimpmuckl/herdr-streamdeck)<br><sub>Pimpmuckl</sub> | Elgato Stream Deck+によるHerdrの物理コントロール | `typescript` | 2 | 🔄 2026-09-02 |
| [**herdr-handsfree**](https://github.com/RanolP/herdr-handsfree)<br><sub>RanolP</sub> | ハンズフリーherdrプラグイン——whisper.cppによる音声入力とmacOS向けWebカメラ視線マウスを提供 | `rust` | 2 | 2026-07-30 |
| [**🆕 herdr-shadow-pane**](https://github.com/shaozk/herdr-shadow-pane)<br><sub>shaozk</sub> | Herdr プラグイン「Shadow Clone Panel」——複数のパネルを同時に操作できます。 | `rust` `vibe-coding` | 2 | 🔄 2026-09-04 |
| [**herdr-suite-site**](https://github.com/StructuPath/herdr-suite-site)<br><sub>StructuPath</sub> | StructuPath Herdr Suiteのランディングページ——herdr.structupath.ai | `herdr-integration` `html` | 2 | 2026-07-31 |
| [**herdr-edit-windows**](https://github.com/aclima01/herdr-edit-windows)<br><sub>aclima01</sub> | コーディングエージェントの隣、herdrのペイン内で動くシンプルなテキストエディタ——ファイルツリー、シンタックスハイライト付きエディタ、未コミット差分タブを備える。Windows専用 | `rust` | 1 | 2026-07-25 |
| [**herdr-stoplight**](https://github.com/BowlOfSoup/herdr-stoplight)<br><sub>BowlOfSoup</sub> | Herdrのリアルタイムな状態から、物理的なArduino製信号灯モジュールを動かす | `go` | 1 | 2026-07-11 |
| [**🆕 harbr**](https://github.com/dev-town/harbr)<br><sub>dev-town</sub> | Harbour TUI | `typescript` | 1 | 🔄 2026-09-03 |
| [**herdr-rainfrog**](https://github.com/fraction12/herdr-rainfrog)<br><sub>fraction12</sub> | 管理されたHerdRのペイン内でRainfrogを開く | `shell` | 1 | 2026-08-15 |
| [**herdr-openlogi**](https://github.com/giacolees/herdr-openlogi)<br><sub>giacolees</sub> | OpenLogiのバインディングオーバーレイ経由で、Logitechマウスをherdrに接続する | `ghostty` `logitech-mouse` `macos` `openlogi` `shell` | 1 | 🔄 2026-08-24 |
| [**hrd**](https://github.com/joshuadavidthomas/hrd)<br><sub>joshuadavidthomas</sub> | サンドボックスの群れと、その上で動くHerdrセッションを管理する | `go` | 1 | 🔄 2026-08-28 |
| [**🆕 herdr-plugins**](https://github.com/narumiruna/herdr-plugins)<br><sub>narumiruna</sub> | _(説明なし)_ | `rust` | 1 | 2026-08-08 |
| [**herdr-phin-util**](https://github.com/phin-tech/herdr-phin-util)<br><sub>phin-tech</sub> | 個人用のHerdrユーティリティ集 | `bubbletea` `tui` `go` | 1 | 2026-08-18 |
| [**herdr-api-client**](https://github.com/playsthisgame/herdr-api-client)<br><sub>playsthisgame</sub> | herdrのスプリットペインやタブで動くHTTP/REST APIクライアント——ターミナルを離れずにリクエストの閲覧・実行・テストができる | `http-client` `rest-client` `tui` `shell` | 1 | 2026-08-08 |
| [**pixtui**](https://github.com/RizRiyz/pixtui)<br><sub>RizRiyz</sub> | ターミナル上で動くピクセルアートエディタ | `bohay-module` `editor` `luvus-module` `pixel-art` `termina` | 1 | 2026-08-07 |
| [**herdr-jetbrains**](https://github.com/Soemii/herdr-jetbrains)<br><sub>Soemii</sub> | _(説明なし)_ | `go` | 1 | 2026-08-09 |
| [**herdr-sidepulse**](https://github.com/third774/herdr-sidepulse)<br><sub>third774</sub> | _(説明なし)_ | `javascript` | 1 | 2026-08-14 |
| [**herdr-plugin-k8s-context**](https://github.com/tkuchiki/herdr-plugin-k8s-context)<br><sub>tkuchiki</sub> | 隔離されたKubernetesのcontextとnamespaceを指定して、Herdrのタブを開く | `go` | 1 | 2026-08-15 |
| [**herdr-zen**](https://github.com/y4m3/herdr-zen)<br><sub>y4m3</sub> | 調整可能な中央寄せペイン幅を備えた、Herdr向けのZenモード | `rust` `terminal` `zen-mode` | 1 | 2026-08-19 |
| [**multitrunk-herdr-plugin**](https://github.com/yoyoyeti/multitrunk-herdr-plugin)<br><sub>yoyoyeti</sub> | multitrunkのタスクワークスペース向けのHerdrプラグイン | `git` `multitrunk` `rust` | 1 | 🔄 2026-08-31 |
| [**herdr-panes**](https://github.com/atm028/herdr-panes)<br><sub>atm028</sub> | _(説明なし)_ | `python` | 0 | 2026-08-01 |
| [**hrdr-azure-plugin**](https://github.com/gbaeke/hrdr-azure-plugin)<br><sub>gbaeke</sub> | herdrプラグイン：Azureのリソースグループとリソースを閲覧し、クリックするとAzureポータルで開く | `azure` `javascript` | 0 | 🔄 2026-08-23 |
| [**capslock-herdr-prefix**](https://github.com/GHJQ/capslock-herdr-prefix)<br><sub>GHJQ</sub> | macOSでCaps Lockキーをherdrのprefixキーにする | `capslock` `macos` `shell` | 0 | 2026-08-11 |
| [**herdr-attach**](https://github.com/gilvanecesar/herdr-attach)<br><sub>gilvanecesar</sub> | Herdrのポップアップからローカルファイルを選び、フォーカス中のコーディングエージェントに送る——ターミナルを離れずにファイルのコンテキストを添付できる | `javascript` | 0 | 2026-07-26 |
| [**herdr-llama**](https://github.com/hitaishi2222/herdr-llama)<br><sub>hitaishi2222</sub> | 手元の操作でllama-serverをコントロールする | `llama-cpp` `local-ai` `python` | 0 | 2026-07-16 |
| [**herdr-pane-update-timestamps**](https://github.com/johnlindquist/herdr-pane-update-timestamps)<br><sub>johnlindquist</sub> | ペイン出力をタイムスタンプ付きでスクロール観察できるHerdrプラグイン | `rust` | 0 | 2026-07-29 |
| [**herdr-status**](https://github.com/jrswab/herdr-status)<br><sub>jrswab</sub> | Linux版Herdr向けの、マシン状態を常時表示するペイン | `go` | 0 | 2026-07-30 |
| [**herdr-laravel-tinker**](https://github.com/lancodev/herdr-laravel-tinker)<br><sub>lancodev</sub> | herdr向けのスプリット表示Laravel tinker REPL——エディタの隣にライブの実行結果を表示、ペインまたはポップアップで利用可能 | `laravel` `tinker` `php` `repl` | 0 | 2026-07-16 |
| [**herdr-new-task**](https://github.com/leonho/herdr-new-task)<br><sub>leonho</sub> | herdrプラグイン：1回のキー操作でプロジェクトディレクトリを選び、新しいタブでclaudeを起動する。タブ名は名詞優先の命名 | `python` | 0 | 2026-07-16 |
| [**herdr-plugin-loopreview**](https://github.com/loopkeep/herdr-plugin-loopreview)<br><sub>loopkeep</sub> | loopreview向けのHerdrプラグイン | `rust` | 0 | 2026-07-23 |
| [**strays**](https://github.com/m1sk9/strays)<br><sub>m1sk9</sub> | Claude Codeを一元管理するためのTUI | `claude-code` `llm` `tui` `rust` | 0 | 🔄 2026-08-29 |
| [**herdr-source-control**](https://github.com/mariotmc/herdr-source-control)<br><sub>mariotmc</sub> | _(説明なし)_ | `go` | 0 | 2026-08-15 |
| [**herdr-brainrot**](https://github.com/marius-se/herdr-brainrot)<br><sub>marius-se</sub> | エージェントが作業している間、Herdrのペインの中でDOOMをプレイできる「brainrot」プラグイン。差し替え可能なアプリに対応 | `doom` `go` | 0 | 2026-08-06 |
| [**herdr-git-pull**](https://github.com/nimrc/herdr-git-pull)<br><sub>nimrc</sub> | _(説明なし)_ | `python` | 0 | 2026-08-13 |
| [**ayatsumugi**](https://github.com/nkwork9999/ayatsumugi)<br><sub>nkwork9999</sub> | AyatoriとTsumugi向けの、ローカルファーストなReact DOM・Fiber・状態グラフの可視化 | `cmux` `ghostty` `orca` `react-devtools` `javascript` | 0 | 🔄 2026-08-26 |
| [**herdr-action-launcher**](https://github.com/nnexai/herdr-action-launcher)<br><sub>nnexai</sub> | _(説明なし)_ | `javascript` | 0 | 2026-08-05 |
| [**🆕 herdr-bot**](https://github.com/Phoobobo/herdr-bot)<br><sub>Phoobobo</sub> | _(説明なし)_ | `tui` `typescript` | 0 | 🔄 2026-09-02 |
| [**herdr-traex-integration**](https://github.com/Phoobobo/herdr-traex-integration)<br><sub>Phoobobo</sub> | traexとの連携をサポートするHerdrプラグイン | `shell` | 0 | 2026-07-02 |
| [**herdr-browser**](https://github.com/redsquiggle/herdr-browser)<br><sub>redsquiggle</sub> | Chromiumのタブグループを、Herdrのワークスペースと同期させる | `chromium` `ratatui` `rust` | 0 | 2026-07-28 |
| [**🆕 herdr-orca**](https://github.com/rudironsoni/herdr-orca)<br><sub>rudironsoni</sub> | 標準の Orca タブを、Herdr が管理するターミナルにアタッチする Herdr プラグインです。 | `typescript` | 0 | 🔄 2026-09-03 |
| [**herdr-cwd-control**](https://github.com/skinp/herdr-cwd-control)<br><sub>skinp</sub> | 新しいワークスペース・タブ・ペインの初期作業ディレクトリを、より細かく制御できるherdrプラグイン | `python` | 0 | 2026-08-10 |
| [**herdr-now-playing**](https://github.com/spywhere/herdr-now-playing)<br><sub>spywhere</sub> | キーバインドで操作できる音楽プレイヤーをherdrに追加する | `shell` | 0 | 🔄 2026-08-22 |
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
