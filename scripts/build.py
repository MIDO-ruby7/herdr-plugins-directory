#!/usr/bin/env python3
"""Build a purpose-oriented index of herdr plugins from GitHub.

Data source: public GitHub repositories tagged with the topic `herdr-plugin`
(the same signal herdr.dev/plugins uses). No dependencies beyond the stdlib.

Outputs:
  data/plugins.json  machine-readable index (for a future web UI)
  README.md          human-readable link list grouped by purpose (Japanese)
  README.en.md       same list, in English
  README.zh.md       same list, in Chinese
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TOPIC = "herdr-plugin"
API = "https://api.github.com/search/repositories"

LANGS = ["ja", "en", "zh"]
README_PATH = {"ja": "README.md", "en": "README.en.md", "zh": "README.zh.md"}

# ---------------------------------------------------------------------------
# Purpose taxonomy
# ---------------------------------------------------------------------------
# Each category: (key, label_ja, label_en, label_zh,
#                 blurb_ja, blurb_en, blurb_zh, {keyword: weight})
# Keywords are matched against repo name + description + topics (lowercased).

CATEGORIES: list[tuple[str, str, str, str, str, str, str, dict[str, int]]] = [
    (
        "notify",
        "通知・アラート",
        "Notifications & Alerts",
        "通知与提醒",
        "エージェントが完了した / 入力待ちで止まったのを、席を外していても知りたい",
        "I want to know when an agent finishes or gets stuck waiting for input, even when I'm away from my desk",
        "即使离开座位，也想知道 Agent 何时完成或卡在等待输入",
        {
            "ntfy": 4, "notif*": 4, "alerter": 4,
            "pushover": 4, "push notification": 4, "toast": 3, "alert*": 3, "bell": 3,
            "telegram": 3, "discord": 3, "slack": 3, "whatsapp": 3, "sms": 3,
            "wake": 2, "ping": 2, "blocked or done": 3, "needs your input": 3,
            "when an agent finishes": 3,
        },
    ),
    (
        "remote",
        "スマホ・リモート操作",
        "Mobile & Remote Control",
        "手机与远程操控",
        "外出先やスマホからエージェントを監視して、承認だけ返したい",
        "I want to monitor agents from my phone or while away, and just send back approvals",
        "想在外出或用手机时监控 Agent，只需回传批准即可",
        {
            "mobile": 4, "phone": 4, "pwa": 4, "android": 3, "ios": 3,
            "remote": 3, "tunnel*": 3, "tailscale": 3, "tailnet": 3, "cloudflare": 2,
            "menu bar": 3, "menubar": 3, "relay": 3, "web app": 2, "webapp": 2,
            "approv*": 2, "on the go": 3, "from your phone": 4, "companion app": 3,
        },
    ),
    (
        "agents",
        "エージェント統括・並列実行",
        "Agent Orchestration",
        "Agent 编排与并行执行",
        "複数の AI エージェントをまとめて起動・分担・管理したい",
        "I want to launch, split up, and manage multiple AI agents together",
        "想统一启动、分工并管理多个 AI Agent",
        {
            "orchestrat*": 4, "parallel": 4, "multi-agent": 4, "agent teams": 4,
            "agent-teams": 4, "mission control": 3, "swarm": 4, "fleet": 3,
            "sandbox": 3, "dispatch*": 3, "spawn*": 3, "queue*": 2, "supervisor": 3,
            "multiple agents": 4, "agent manager": 4, "delegat*": 3, "worker": 2,
            "coding-agents": 2, "ai-agents": 1, "agent*": 1, "prompt*": 1,
        },
    ),
    (
        "worktree",
        "git worktree・ブランチ運用",
        "Git Worktrees & Branches",
        "git 工作树与分支管理",
        "作業ごとに worktree を切って、片付けまで自動でやりたい",
        "I want to spin up a worktree for each piece of work, and have the cleanup handled automatically too",
        "想为每项工作单独开一个工作树，收尾清理也自动完成",
        {
            "worktree": 5, "jujutsu": 4, "jj*": 4, "branch": 3,
            "worktrunk": 4, "checkout": 2, "stacked": 2,
        },
    ),
    (
        "review",
        "コードレビュー・差分確認",
        "Code Review & Diffs",
        "代码审查与差异对比",
        "エージェントが書いた差分を読んで、コメントを返したい",
        "I want to read the diff an agent wrote and send comments back on it",
        "想阅读 Agent 写的差异并对其发表评论",
        {
            "code review": 5, "code-review": 5, "review*": 4,
            "diff*": 4, "hunk*": 4, "difftastic": 3, "delta": 2, "patch*": 2,
            "merge request": 3, "approv* the diff": 3, "blame": 2,
        },
    ),
    (
        "forge",
        "GitHub / issue トラッカー連携",
        "GitHub & Issue Trackers",
        "GitHub / issue 跟踪工具集成",
        "issue や PR を起点に作業を始めたい / PR の状態を追いたい",
        "I want to kick off work from an issue or PR, and track PR status",
        "想以 issue 或 PR 为起点开始工作，并追踪 PR 状态",
        {
            "github issue": 5, "issue*": 4, "pull request": 4, "pull-request": 4,
            "pr status": 4, "pr-tracker": 4, "gitlab": 3, "linear": 4, "jira": 4,
            "notion": 3, "asana": 3, "github": 2, "pr": 2, "gh": 2,
        },
    ),
    (
        "layout",
        "ワークスペース・レイアウト構築",
        "Workspaces & Layouts",
        "工作区与布局搭建",
        "プロジェクトを開いたら、タブ・ペイン・起動コマンドまで一発で整えたい",
        "When I open a project, I want tabs, panes, and startup commands all set up in one shot",
        "打开项目时，希望标签页、窗格和启动命令一次性就位",
        {
            "layout": 5, "sessionizer": 4, "session manager": 4, "session-manager": 4,
            "sesh": 4, "workspace manager": 4, "workspace-manager": 4,
            "bootstrap*": 3, "declarative": 3, "template*": 3, "scaffold": 2,
            "tabs, panes": 4, "tab/pane": 4, "from a single yaml": 4,
            "workspace": 2, "project switcher": 3, "per-project setup": 3,
        },
    ),
    (
        "navigate",
        "ペイン移動・キー操作",
        "Pane Navigation & Keys",
        "窗格导航与快捷键",
        "ペインやワークスペース間の移動・リサイズを、エディタと同じキーで済ませたい",
        "I want to move and resize between panes and workspaces using the same keys as my editor",
        "想用和编辑器一样的快捷键在窗格、工作区之间移动和调整大小",
        {
            "navigat*": 5, "splits": 4, "split-navigation": 5,
            "hjkl": 4, "ctrl+h": 4, "vim-tmux-navigator": 4, "resiz*": 3,
            "jump*": 3, "keybinding*": 3, "last workspace": 4, "last tab": 4,
            "switch*": 2, "focus*": 2, "zoom*": 2, "numbering": 2,
            "swap*": 3, "mark*": 2, "pane manager": 4,
            "float*": 4, "popup*": 4, "tile*": 3, "scratch*": 3,
            "closing a pane": 4, "close pane": 4, "whichkey": 4, "which-key": 4,
        },
    ),
    (
        "files",
        "ファイル閲覧・エディタ連携",
        "File Viewers & Editors",
        "文件浏览与编辑器联动",
        "ペインの中でファイルツリーを開いたり、エディタ側と状態を揃えたい",
        "I want to open a file tree inside a pane, or keep it in sync with my editor",
        "想在窗格中打开文件树，或与编辑器的状态保持一致",
        {
            "file viewer": 5, "file-viewer": 5, "file explorer": 5, "explorer": 4,
            "sidebar": 4, "yazi": 4, "quick look": 4, "quicklook": 4, "explorer*": 4,
            "preview*": 3, "syntax-highlight*": 3, "open file*": 3, "tree*": 3, "zed": 3,
            "vs code": 3, "vscode": 3, "neovim": 2, "nvim": 2, "vim": 1,
            "lazygit": 3, "editor*": 2,
        },
    ),
    (
        "cost",
        "トークン・コスト管理",
        "Tokens & Cost",
        "Token 与费用管理",
        "エージェントがいくら使っているかを見たい / 使用量を削りたい",
        "I want to see how much an agent is spending, and cut down on usage",
        "想看看 Agent 花费了多少，并想削减用量",
        {
            "token*": 5, "cost": 4, "spend": 4, "billing": 4, "token bill": 5,
            "budget": 4, "usage": 3, "llm-proxy": 4, "llm proxy": 4,
            "compress*": 3, "context window": 3, "quota": 3, "rate limit": 2,
        },
    ),
    (
        "monitor",
        "監視・ダッシュボード",
        "Monitoring & Dashboards",
        "监控与仪表盘",
        "エージェントやマシンの状態を一覧で眺めたい",
        "I want an at-a-glance overview of agent and machine status",
        "想一目览尽 Agent 和机器的状态",
        {
            "dashboard*": 5, "telemetr*": 5, "monitor*": 4, "observability": 4,
            "metrics": 4, "statusline": 4, "status bar": 3, "cpu": 4, "ram": 4,
            "memory usage": 4, "overview": 2, "board*": 2, "kanban*": 3,
            "health": 3, "live view": 3, "progress": 2, "dev servers": 4,
            "ports": 4, "docker": 3, "compose": 3, "badge": 3, "lifecycle state": 3,
        },
    ),
    (
        "finder",
        "検索・ファジーファインダー",
        "Fuzzy Finders & Palettes",
        "搜索与模糊查找器",
        "コマンドやプロジェクトを、名前をうろ覚えのまま呼び出したい",
        "I want to invoke commands or projects even when I only half-remember their names",
        "只记得大概名字也想调出命令或项目",
        {
            "fzf": 5, "fuzzy": 5, "command palette": 5, "palette": 4,
            "picker": 4, "television": 4, "zoxide": 4, "finder": 3,
            "search*": 3, "quick-open": 3, "jump to any": 4,
        },
    ),
    (
        "automation",
        "自動化・フック・定期実行",
        "Automation, Hooks & Schedules",
        "自动化、钩子与定时任务",
        "worktree 作成時やタイミングを決めて、決まった手順を自動で走らせたい",
        "I want a fixed set of steps to run automatically on worktree creation or at a chosen time",
        "想在创建工作树或指定时机自动运行固定的操作步骤",
        {
            "cron": 5, "schedul*": 5, "routine*": 4, "automat*": 4,
            "hook*": 4, "on worktree": 4, "watch*": 3, "trigger*": 3,
            "setup steps": 4, "direnv": 3, "mise": 3, "auto*": 2, "ci": 2,
            "test runner": 3, "run the suite": 3,
        },
    ),
    (
        "session",
        "セッション保存・復元",
        "Session State & Restore",
        "会话保存与恢复",
        "作業を閉じても、あとで同じ状態から再開したい",
        "I want to close my work and later resume from exactly the same state",
        "关闭工作后，希望之后能从同一状态继续",
        {
            "restor*": 5, "persist*": 5, "resum*": 5, "park*": 4, "session state": 5,
            "session-state": 5, "snapshot": 4, "detach": 3, "reattach": 4,
            "save session": 4, "sync*": 2, "mirror*": 3,
        },
    ),
    (
        "naming",
        "タイトル・命名・見た目",
        "Titles, Naming & Looks",
        "标题、命名与外观",
        "タブ名やターミナルタイトルを自動で分かりやすくしたい / 見た目を変えたい",
        "I want tab names and terminal titles to be automatically clear, or want to change how things look",
        "想让标签页名称和终端标题自动变得清晰易懂，或想改变外观",
        {
            "renam*": 5, "tab name": 5, "window title": 5, "terminal title": 5,
            "title": 4, "naming": 4, "theme": 4, "color": 3, "icon": 3,
            "emoji": 3, "pixel-art": 4, "ascii": 3, "banner": 3, "cosmetic": 4,
        },
    ),
    (
        "text",
        "テキスト・URL 抽出",
        "Text & URL Grabbing",
        "文本与 URL 提取",
        "画面に出ている文字列やパス・URL を、マウスなしで拾いたい",
        "I want to grab strings, paths, or URLs shown on screen without touching the mouse",
        "想不用鼠标就抓取屏幕上显示的字符串、路径或 URL",
        {
            "clipboard": 5, "cop*": 4, "yank*": 4, "pluck*": 4, "extract*": 4,
            "pattern-matched": 5, "open links": 4, "urls on screen": 5,
            "already visible": 4, "select text": 4, "regex": 3, "ocr": 4,
        },
    ),
    (
        "meta",
        "プラグイン管理・開発",
        "Plugin Management & Authoring",
        "插件管理与开发",
        "プラグイン自体を管理したい / 自分で作りたい",
        "I want to manage plugins themselves, or build my own",
        "想管理插件本身，或者自己动手做一个",
        {
            "plugin manager": 5, "plugin-manager": 5, "lockfile": 4, "distro": 4,
            "plugin template": 5, "starter": 4, "boilerplate": 4, "sdk": 4,
            "manifest": 3, "example plugin": 4, "cookbook": 3, "curated": 3,
            "awesome": 3, "registry": 3, "collection of plugins": 5,
            "collection of tools": 4, "experimental plugins": 5, "monorepo": 3,
        },
    ),
]


def _compile(keywords: dict[str, int]) -> list[tuple[re.Pattern, int]]:
    """`foo` matches the whole word only; `foo*` matches any word starting with it."""
    out = []
    for word, weight in keywords.items():
        word = word.strip()
        if word.endswith("*"):
            pattern = r"\b" + re.escape(word[:-1])
        else:
            pattern = r"\b" + re.escape(word) + r"\b"
        out.append((re.compile(pattern), weight))
    return out


COMPILED = {key: _compile(kw) for key, *_labels, kw in CATEGORIES}
CATEGORY_KEYS = [c[0] for c in CATEGORIES]
OTHER = (
    "other",
    "その他・ユーティリティ",
    "Other & Utilities",
    "其他与实用工具",
    "上のどれにも当てはまらない便利もの",
    "Handy things that don't fit any of the categories above",
    "不属于以上任何分类，但很实用的东西",
)

# Topics that carry no signal for a reader of this list.
NOISE_TOPICS = {"herdr", "herdr-plugin", "plugin", "plugins", "herdr-plugins"}


def gh_get(url: str) -> dict:
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "herdr-plugins-by-purpose",
    })
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as res:
                return json.loads(res.read().decode())
        except urllib.error.HTTPError as err:
            if err.code in (403, 429) and attempt < 4:
                wait = 20 * (attempt + 1)
                print(f"  rate limited, retrying in {wait}s", file=sys.stderr)
                time.sleep(wait)
                continue
            raise
    raise RuntimeError("unreachable")


def fetch_repos() -> list[dict]:
    repos: dict[str, dict] = {}
    page = 1
    while page <= 10:
        url = f"{API}?q=topic:{TOPIC}+fork:false&per_page=100&page={page}&sort=stars"
        payload = gh_get(url)
        items = payload.get("items", [])
        print(f"  page {page}: {len(items)} repos (total {payload.get('total_count')})")
        for item in items:
            if item.get("fork") or item.get("archived"):
                continue
            repos[item["full_name"]] = item
        if len(items) < 100:
            break
        page += 1
        time.sleep(2)
    return list(repos.values())


def classify(repo: dict, overrides: dict) -> tuple[str, list[str]]:
    full = repo["full_name"]
    override = overrides.get(full, {})
    if override.get("category") in CATEGORY_KEYS + [OTHER[0]]:
        return override["category"], []

    haystack = " ".join([
        " " + repo["name"].replace("-", " ").replace("_", " ") + " ",
        " " + (repo.get("description") or "") + " ",
        " ".join(repo.get("topics", [])),
    ]).lower()

    scores: dict[str, int] = {}
    for key, patterns in COMPILED.items():
        score = sum(weight for pattern, weight in patterns if pattern.search(haystack))
        if score:
            scores[key] = score

    if not scores:
        return OTHER[0], []
    best = max(scores.items(), key=lambda kv: (kv[1], -CATEGORY_KEYS.index(kv[0])))
    # Secondary categories: strong-but-not-winning matches, so a notifier that
    # also works from your phone shows up in both places.
    also = [k for k, v in sorted(scores.items(), key=lambda kv: -kv[1])
            if k != best[0] and v >= 4 and v >= best[1] * 0.6][:2]
    return best[0], also


def tags_for(repo: dict, overrides: dict) -> list[str]:
    tags = [t for t in repo.get("topics", []) if t not in NOISE_TOPICS]
    lang = repo.get("language")
    if lang and lang.lower() not in [t.lower() for t in tags]:
        tags.append(lang.lower())
    tags += overrides.get(repo["full_name"], {}).get("add_tags", [])
    seen, out = set(), []
    for tag in tags:
        if tag not in seen:
            seen.add(tag)
            out.append(tag)
    return out[:8]


NO_DESCRIPTION = {
    "ja": "_(説明なし)_",
    "en": "_(no description)_",
    "zh": "_(暂无描述)_",
}


def one_line(text: str | None, lang: str = "en", limit: int = 160) -> str:
    if not text:
        return NO_DESCRIPTION[lang]
    text = re.sub(r"\s+", " ", text).strip()
    text = text.replace("|", "\\|")
    if len(text) > limit:
        text = text[: limit - 1].rstrip() + "…"
    return text


def localized_description(entry: dict, lang: str, translations: dict) -> str:
    """Japanese/Chinese pages show a translated description when one is cached
    and still matches the current English source text; otherwise fall back to
    the raw English description (new/changed repos, until someone adds a
    translation via a PR to data/translations.json)."""
    if lang == "en":
        return entry["description"]
    cached = translations.get(entry["full_name"])
    if cached and cached.get("en") == entry["description"] and cached.get(lang):
        return cached[lang]
    return entry["description"]


def build() -> None:
    overrides_path = DATA / "overrides.json"
    overrides = json.loads(overrides_path.read_text()) if overrides_path.exists() else {}
    translations_path = DATA / "translations.json"
    translations = json.loads(translations_path.read_text()) if translations_path.exists() else {}

    print("fetching repositories…")
    repos = fetch_repos()
    print(f"  {len(repos)} active repositories")

    entries = []
    for repo in repos:
        category, also = classify(repo, overrides)
        entries.append({
            "full_name": repo["full_name"],
            "name": repo["name"],
            "owner": repo["owner"]["login"],
            "url": repo["html_url"],
            "description": (repo.get("description") or "").strip(),
            "note": overrides.get(repo["full_name"], {}).get("note", ""),
            "stars": repo["stargazers_count"],
            "language": repo.get("language"),
            "tags": tags_for(repo, overrides),
            "category": category,
            "also": also,
            "pushed_at": repo["pushed_at"],
            "install": f"herdr plugin install {repo['full_name']}",
        })

    entries.sort(key=lambda e: (-e["stars"], e["full_name"].lower()))
    now = datetime.now(timezone.utc)
    generated = now.strftime("%Y-%m-%d %H:%M UTC")

    DATA.mkdir(exist_ok=True)
    (DATA / "plugins.json").write_text(json.dumps({
        "generated_at": generated,
        "source": f"GitHub repositories tagged `{TOPIC}`",
        "categories": [
            {"key": k, "label_ja": ja, "label_en": en, "label_zh": zh,
             "purpose_ja": bja, "purpose_en": ben, "purpose_zh": bzh}
            for k, ja, en, zh, bja, ben, bzh, _kw in CATEGORIES
        ] + [{"key": OTHER[0], "label_ja": OTHER[1], "label_en": OTHER[2],
              "label_zh": OTHER[3], "purpose_ja": OTHER[4], "purpose_en": OTHER[5],
              "purpose_zh": OTHER[6]}],
        "plugins": entries,
    }, ensure_ascii=False, indent=2) + "\n")

    for lang in LANGS:
        (ROOT / README_PATH[lang]).write_text(
            render_readme(entries, generated, now, lang, translations)
        )
    print(f"wrote {', '.join(README_PATH.values())} and data/plugins.json ({len(entries)} plugins)")


UI = {
    "ja": {
        "switcher": "🇯🇵 日本語 · [🇺🇸 English](README.en.md) · [🇨🇳 中文](README.zh.md)",
        "tagline": "**「◯◯したい」から herdr のプラグインを探すためのリンク集です。**",
        "stats": "- 収録 **{n}** 件 / 最終更新 **{generated}**（6 時間ごとに自動更新）",
        "source": "- データ元: GitHub topic [`{topic}`]({topic_url}) — "
                   "公式マーケットプレイス [herdr.dev/plugins](https://herdr.dev/plugins/) と同じ母集団",
        "classify_note": "- 分類はリポジトリの説明文とトピックからの自動推定です。"
                          "おかしなものは [`data/overrides.json`](data/overrides.json) の PR で直せます",
        "install_line": "- インストール: `herdr plugin install owner/repo`"
                         " — [公式ドキュメント](https://herdr.dev/docs/plugins/)",
        "warning": "> ここは自動収集の索引で、審査済みカタログではありません。"
                    "プラグインは自分のマシンでそのまま動くコードなので、"
                    "入れる前にマニフェストと実行されるコマンドを確認してください。",
        "browse_heading": "## 目的から探す",
        "table_header": "| プラグイン | できること | タグ | ★ | 最終更新 |",
        "also_relevant": "この目的にも関係するもの",
        "back_to_top": "[⬆ 目的一覧に戻る](#purposes)",
        "installing_heading": "## 使い方",
        "install_comment": "# 表の行にある owner/repo をそのまま渡す",
        "subdir_note": "サブディレクトリに入っているプラグインは `owner/repo/subdir` の形になります。"
                        "詳細は [Plugins](https://herdr.dev/docs/plugins/) と"
                        " [Marketplace](https://herdr.dev/docs/marketplace/) を参照。",
        "fixing_heading": "## 直したいとき",
        "fixing_note": "分類が変・タグを足したい・一言メモを付けたい場合は"
                        " [`data/overrides.json`](data/overrides.json) にエントリを追加して PR してください。",
        "example_note": "セットアップに ntfy のトピック設定が必要",
        "category_keys": "カテゴリキー:",
        "auto_listing": "掲載自体は各リポジトリが GitHub topic `herdr-plugin` を付けた時点で自動的に入ります"
                         "（このリストへの申請は不要）。",
        "footer": "*README と `data/plugins.json` は"
                   " [`scripts/build.py`](scripts/build.py) が生成しています。直接編集しないでください。*",
    },
    "en": {
        "switcher": "[🇯🇵 日本語](README.md) · 🇺🇸 English · [🇨🇳 中文](README.zh.md)",
        "tagline": "**A link collection for finding [herdr](https://herdr.dev/) plugins "
                    "by what you want to get done.**",
        "stats": "- **{n}** plugins indexed / last updated **{generated}** (auto-refreshed every 6 hours)",
        "source": "- Source: GitHub repositories tagged [`{topic}`]({topic_url}) — "
                   "the same population as the official [herdr.dev/plugins](https://herdr.dev/plugins/) marketplace",
        "classify_note": "- Categories are auto-inferred from each repo's description and topics. "
                          "If one looks wrong, fix it with a PR to [`data/overrides.json`](data/overrides.json)",
        "install_line": "- Install: `herdr plugin install owner/repo`"
                         " — [official docs](https://herdr.dev/docs/plugins/)",
        "warning": "> This is an auto-collected index, not a vetted catalog. "
                    "Plugins are code that runs directly on your machine, so check the manifest "
                    "and the commands it runs before installing.",
        "browse_heading": "## Browse by purpose",
        "table_header": "| Plugin | What it does | Tags | ★ | Last updated |",
        "also_relevant": "Also relevant to this purpose",
        "back_to_top": "[⬆ Back to purposes](#purposes)",
        "installing_heading": "## Installing",
        "install_comment": "# pass the owner/repo from any row in the table above",
        "subdir_note": "Plugins that live in a subdirectory use the `owner/repo/subdir` form. "
                        "See [Plugins](https://herdr.dev/docs/plugins/) and "
                        "[Marketplace](https://herdr.dev/docs/marketplace/) for details.",
        "fixing_heading": "## Fixing this list",
        "fixing_note": "If a category looks off, you want to add tags, or attach a short note, "
                        "add an entry to [`data/overrides.json`](data/overrides.json) and send a PR.",
        "example_note": "needs ntfy topic configured during setup",
        "category_keys": "Category keys:",
        "auto_listing": "Listing is fully automatic — any repo gets included as soon as it's tagged "
                         "with the GitHub topic `herdr-plugin` (no need to submit it here).",
        "footer": "*README.en.md and `data/plugins.json` are generated by "
                   "[`scripts/build.py`](scripts/build.py). Please don't edit them directly.*",
    },
    "zh": {
        "switcher": "[🇯🇵 日本語](README.md) · [🇺🇸 English](README.en.md) · 🇨🇳 中文",
        "tagline": "**一个按照「你想做什么」来查找 [herdr](https://herdr.dev/) 插件的链接合集。**",
        "stats": "- 收录 **{n}** 个插件 / 最后更新 **{generated}**（每 6 小时自动刷新）",
        "source": "- 数据来源：打了 GitHub 话题标签 [`{topic}`]({topic_url}) 的仓库——"
                   "与官方市场 [herdr.dev/plugins](https://herdr.dev/plugins/) 的数据来源相同",
        "classify_note": "- 分类是根据仓库描述和话题标签自动推断的。"
                          "如果分类不准确，可以通过 PR 修改 [`data/overrides.json`](data/overrides.json)",
        "install_line": "- 安装：`herdr plugin install owner/repo`"
                         " —— [官方文档](https://herdr.dev/docs/plugins/)",
        "warning": "> 这是自动采集的索引，不是经过审核的目录。"
                    "插件是直接在你的电脑上运行的代码，安装前请检查其 manifest 和会执行的命令。",
        "browse_heading": "## 按目的浏览",
        "table_header": "| 插件 | 能做什么 | 标签 | ★ | 最后更新 |",
        "also_relevant": "与此目的也相关",
        "back_to_top": "[⬆ 返回目的列表](#purposes)",
        "installing_heading": "## 使用方法",
        "install_comment": "# 直接使用表格中某一行的 owner/repo",
        "subdir_note": "位于子目录中的插件使用 `owner/repo/subdir` 的形式。"
                        "详情参见 [Plugins](https://herdr.dev/docs/plugins/) 和"
                        " [Marketplace](https://herdr.dev/docs/marketplace/)。",
        "fixing_heading": "## 想要修正时",
        "fixing_note": "如果分类不对、想加标签、或想加一句备注，"
                        "请在 [`data/overrides.json`](data/overrides.json) 中添加条目并提交 PR。",
        "example_note": "安装时需要配置 ntfy 的 topic",
        "category_keys": "分类键：",
        "auto_listing": "收录是全自动的——只要仓库打上 GitHub 话题标签 `herdr-plugin` "
                         "就会自动出现在此列表中（无需在这里申请）。",
        "footer": "*README.zh.md 和 `data/plugins.json` 由"
                   " [`scripts/build.py`](scripts/build.py) 自动生成，请勿直接编辑。*",
    },
}

LABEL_INDEX = {"ja": 1, "en": 2, "zh": 3}
BLURB_INDEX = {"ja": 4, "en": 5, "zh": 6}


def render_readme(entries: list[dict], generated: str, now: datetime,
                   lang: str, translations: dict) -> str:
    ui = UI[lang]
    li, bi = LABEL_INDEX[lang], BLURB_INDEX[lang]
    cats = [(c[0], c[li], c[bi]) for c in CATEGORIES]
    cats.append((OTHER[0], OTHER[li], OTHER[bi]))

    buckets: dict[str, list[dict]] = {k: [] for k, *_ in cats}
    for entry in entries:
        buckets[entry["category"]].append(entry)
    secondary: dict[str, list[dict]] = {k: [] for k, *_ in cats}
    for entry in entries:
        for key in entry["also"]:
            secondary[key].append(entry)

    lines: list[str] = []
    add = lines.append

    add("# herdr plugins by purpose")
    add("")
    add(ui["switcher"])
    add("")
    add(ui["tagline"])
    add("")
    add(ui["stats"].format(n=len(entries), generated=generated))
    topic_url = f"https://github.com/topics/{TOPIC}"
    add(ui["source"].format(topic=TOPIC, topic_url=topic_url))
    add(ui["classify_note"])
    add(ui["install_line"])
    add("")
    add("> [!WARNING]")
    add(ui["warning"])
    add("")
    add('<a id="purposes"></a>')
    add("")
    add(ui["browse_heading"])
    add("")
    for key, label, blurb in cats:
        count = len(buckets[key])
        if not count:
            continue
        add(f"- [**{label}**](#cat-{key}) ({count}) — {blurb}")
    add("")

    for key, label, blurb in cats:
        items = buckets[key]
        if not items:
            continue
        add(f'<a id="cat-{key}"></a>')
        add("")
        add(f"## {label}")
        add("")
        add(f"> {blurb}")
        add("")
        add(ui["table_header"])
        add("| --- | --- | --- | --: | --- |")
        for entry in items:
            add(row(entry, now, lang, translations))
        add("")
        extras = [e for e in secondary[key] if e["category"] != key]
        if extras:
            add(f"<details><summary>{ui['also_relevant']}</summary>")
            add("")
            for entry in extras:
                desc = one_line(localized_description(entry, lang, translations), lang, 110)
                add(f"- [{entry['full_name']}]({entry['url']}) — {desc}")
            add("")
            add("</details>")
            add("")
        add(ui["back_to_top"])
        add("")

    add(ui["installing_heading"])
    add("")
    add("```sh")
    add(ui["install_comment"])
    add("herdr plugin install ogulcancelik/herdr-plugin-github-start")
    add("herdr plugin list")
    add("```")
    add("")
    add(ui["subdir_note"])
    add("")
    add(ui["fixing_heading"])
    add("")
    add(ui["fixing_note"])
    add("")
    add("```json")
    add('{')
    add('  "owner/repo": {')
    add(f'    "category": "{CATEGORY_KEYS[0]}",')
    add('    "add_tags": ["macos"],')
    add(f'    "note": "{ui["example_note"]}"')
    add('  }')
    add('}')
    add("```")
    add("")
    add(f"{ui['category_keys']} `{'`, `'.join(CATEGORY_KEYS + [OTHER[0]])}`")
    add("")
    add(ui["auto_listing"])
    add("")
    add("---")
    add("")
    add(ui["footer"])
    add("")
    return "\n".join(lines)


RECENT_DAYS = 14


def row(entry: dict, now: datetime, lang: str, translations: dict) -> str:
    tags = " ".join(f"`{t}`" for t in entry["tags"][:5]) or "—"
    desc = one_line(localized_description(entry, lang, translations), lang)
    if entry["note"]:
        desc += f"<br>📝 {one_line(entry['note'], lang, 90)}"
    pushed_at = datetime.fromisoformat(entry["pushed_at"].replace("Z", "+00:00"))
    pushed = pushed_at.strftime("%Y-%m-%d")
    if (now - pushed_at).days <= RECENT_DAYS:
        pushed = f"🆕 {pushed}"
    return (f"| [**{entry['name']}**]({entry['url']})<br><sub>{entry['owner']}</sub>"
            f" | {desc} | {tags} | {entry['stars']} | {pushed} |")


if __name__ == "__main__":
    build()
