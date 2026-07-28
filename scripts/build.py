#!/usr/bin/env python3
"""Build a purpose-oriented index of herdr plugins from GitHub.

Data source: public GitHub repositories tagged with the topic `herdr-plugin`
(the same signal herdr.dev/plugins uses). No dependencies beyond the stdlib.

Outputs:
  data/plugins.json  machine-readable index (for a future web UI)
  README.md          human-readable link list grouped by purpose
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

# ---------------------------------------------------------------------------
# Purpose taxonomy
# ---------------------------------------------------------------------------
# Each category: (key, Japanese label, English label, "when you want to..." blurb,
#                 {keyword: weight})
# Keywords are matched against repo name + description + topics (lowercased).

CATEGORIES: list[tuple[str, str, str, str, dict[str, int]]] = [
    (
        "notify",
        "通知・アラート",
        "Notifications & Alerts",
        "エージェントが完了した / 入力待ちで止まったのを、席を外していても知りたい",
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
        "外出先やスマホからエージェントを監視して、承認だけ返したい",
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
        "複数の AI エージェントをまとめて起動・分担・管理したい",
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
        "作業ごとに worktree を切って、片付けまで自動でやりたい",
        {
            "worktree": 5, "jujutsu": 4, "jj*": 4, "branch": 3,
            "worktrunk": 4, "checkout": 2, "stacked": 2,
        },
    ),
    (
        "review",
        "コードレビュー・差分確認",
        "Code Review & Diffs",
        "エージェントが書いた差分を読んで、コメントを返したい",
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
        "issue や PR を起点に作業を始めたい / PR の状態を追いたい",
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
        "プロジェクトを開いたら、タブ・ペイン・起動コマンドまで一発で整えたい",
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
        "ペインやワークスペース間の移動・リサイズを、エディタと同じキーで済ませたい",
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
        "ペインの中でファイルツリーを開いたり、エディタ側と状態を揃えたい",
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
        "エージェントがいくら使っているかを見たい / 使用量を削りたい",
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
        "エージェントやマシンの状態を一覧で眺めたい",
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
        "コマンドやプロジェクトを、名前をうろ覚えのまま呼び出したい",
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
        "worktree 作成時やタイミングを決めて、決まった手順を自動で走らせたい",
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
        "作業を閉じても、あとで同じ状態から再開したい",
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
        "タブ名やターミナルタイトルを自動で分かりやすくしたい / 見た目を変えたい",
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
        "画面に出ている文字列やパス・URL を、マウスなしで拾いたい",
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
        "プラグイン自体を管理したい / 自分で作りたい",
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


COMPILED = {key: _compile(kw) for key, _ja, _en, _blurb, kw in CATEGORIES}
CATEGORY_KEYS = [c[0] for c in CATEGORIES]
OTHER = ("other", "その他・ユーティリティ", "Other & Utilities",
         "上のどれにも当てはまらない便利もの")

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


def one_line(text: str | None, limit: int = 160) -> str:
    if not text:
        return "_(説明なし / no description)_"
    text = re.sub(r"\s+", " ", text).strip()
    text = text.replace("|", "\\|")
    if len(text) > limit:
        text = text[: limit - 1].rstrip() + "…"
    return text


def build() -> None:
    overrides_path = DATA / "overrides.json"
    overrides = json.loads(overrides_path.read_text()) if overrides_path.exists() else {}

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
            {"key": k, "label_ja": ja, "label_en": en, "purpose": blurb}
            for k, ja, en, blurb, _ in CATEGORIES
        ] + [{"key": OTHER[0], "label_ja": OTHER[1], "label_en": OTHER[2],
              "purpose": OTHER[3]}],
        "plugins": entries,
    }, ensure_ascii=False, indent=2) + "\n")

    (ROOT / "README.md").write_text(render_readme(entries, generated, now))
    print(f"wrote README.md and data/plugins.json ({len(entries)} plugins)")


def render_readme(entries: list[dict], generated: str, now: datetime) -> str:
    cats = [(k, ja, en, blurb) for k, ja, en, blurb, _ in CATEGORIES]
    cats.append(OTHER)

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
    add("**「◯◯したい」から herdr のプラグインを探すためのリンク集です。**")
    add("Find [herdr](https://herdr.dev/) plugins by what you want to get done.")
    add("")
    add(f"- 収録 **{len(entries)}** 件 / 最終更新 **{generated}**（6 時間ごとに自動更新）")
    add(f"- データ元: GitHub topic [`{TOPIC}`](https://github.com/topics/{TOPIC})"
        " — 公式マーケットプレイス [herdr.dev/plugins](https://herdr.dev/plugins/) と同じ母集団")
    add("- 分類はリポジトリの説明文とトピックからの自動推定です。"
        "おかしなものは [`data/overrides.json`](data/overrides.json) の PR で直せます")
    add("- インストール: `herdr plugin install owner/repo`"
        " — [公式ドキュメント](https://herdr.dev/docs/plugins/)")
    add("")
    add("> [!WARNING]")
    add("> ここは自動収集の索引で、審査済みカタログではありません。"
        "プラグインは自分のマシンでそのまま動くコードなので、"
        "入れる前にマニフェストと実行されるコマンドを確認してください。")
    add("")
    add('<a id="purposes"></a>')
    add("")
    add("## 目的から探す · Browse by purpose")
    add("")
    for key, ja, en, blurb in cats:
        count = len(buckets[key])
        if not count:
            continue
        add(f"- [**{ja}**](#cat-{key}) ({count}) — {blurb}")
    add("")

    for key, ja, en, blurb in cats:
        items = buckets[key]
        if not items:
            continue
        add(f'<a id="cat-{key}"></a>')
        add("")
        add(f"## {ja} · {en}")
        add("")
        add(f"> {blurb}")
        add("")
        add("| プラグイン | できること | タグ | ★ | 最終更新 |")
        add("| --- | --- | --- | --: | --- |")
        for entry in items:
            add(row(entry, now))
        add("")
        extras = [e for e in secondary[key] if e["category"] != key]
        if extras:
            add("<details><summary>この目的にも関係するもの · also relevant</summary>")
            add("")
            for entry in extras:
                add(f"- [{entry['full_name']}]({entry['url']}) — {one_line(entry['description'], 110)}")
            add("")
            add("</details>")
            add("")
        add("[⬆ 目的一覧に戻る](#purposes)")
        add("")

    add("## 使い方 · Installing")
    add("")
    add("```sh")
    add("# 表の行にある owner/repo をそのまま渡す")
    add("herdr plugin install ogulcancelik/herdr-plugin-github-start")
    add("herdr plugin list")
    add("```")
    add("")
    add("サブディレクトリに入っているプラグインは `owner/repo/subdir` の形になります。"
        "詳細は [Plugins](https://herdr.dev/docs/plugins/) と"
        " [Marketplace](https://herdr.dev/docs/marketplace/) を参照。")
    add("")
    add("## 直したいとき · Fixing this list")
    add("")
    add("分類が変・タグを足したい・一言メモを付けたい場合は"
        " [`data/overrides.json`](data/overrides.json) にエントリを追加して PR してください。")
    add("")
    add("```json")
    add('{')
    add('  "owner/repo": {')
    add(f'    "category": "{CATEGORY_KEYS[0]}",')
    add('    "add_tags": ["macos"],')
    add('    "note": "セットアップに ntfy のトピック設定が必要"')
    add('  }')
    add('}')
    add("```")
    add("")
    add(f"カテゴリキー: `{'`, `'.join(CATEGORY_KEYS + [OTHER[0]])}`")
    add("")
    add("掲載自体は各リポジトリが GitHub topic `herdr-plugin` を付けた時点で自動的に入ります"
        "（このリストへの申請は不要）。")
    add("")
    add("---")
    add("")
    add("*README と `data/plugins.json` は"
        " [`scripts/build.py`](scripts/build.py) が生成しています。直接編集しないでください。*")
    add("")
    return "\n".join(lines)


RECENT_DAYS = 14


def row(entry: dict, now: datetime) -> str:
    tags = " ".join(f"`{t}`" for t in entry["tags"][:5]) or "—"
    desc = one_line(entry["description"])
    if entry["note"]:
        desc += f"<br>📝 {one_line(entry['note'], 90)}"
    pushed_at = datetime.fromisoformat(entry["pushed_at"].replace("Z", "+00:00"))
    pushed = pushed_at.strftime("%Y-%m-%d")
    if (now - pushed_at).days <= RECENT_DAYS:
        pushed = f"🆕 {pushed}"
    return (f"| [**{entry['name']}**]({entry['url']})<br><sub>{entry['owner']}</sub>"
            f" | {desc} | {tags} | {entry['stars']} | {pushed} |")


if __name__ == "__main__":
    build()
