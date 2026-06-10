#!/usr/bin/env python3
"""极简版 CLI —— 单文件、零依赖，直接 `python simple_cli.py add xxx`。"""
import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).parent / "todos.json"


def load():
    if not DATA_FILE.exists():
        return []
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def save(items):
    DATA_FILE.write_text(
        json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def add(args):
    items = load()
    items.append({
        "id": max((i["id"] for i in items), default=0) + 1,
        "title": args.title,
        "priority": args.priority,
        "done": False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    })
    save(items)
    print(f"已添加: [{args.priority}] {args.title}")


def list_all(_args):
    items = load()
    if not items:
        print("（暂无待办）")
        return
    for it in items:
        mark = "✅" if it["done"] else "⬜"
        print(f"{mark} #{it['id']}  [{it['priority']}]  {it['title']}")


def done(args):
    items = load()
    for it in items:
        if it["id"] == args.id:
            it["done"] = True
            save(items)
            print(f"已完成 #{args.id}")
            return
    print(f"未找到 #{args.id}")


def delete(args):
    items = [i for i in load() if i["id"] != args.id]
    save(items)
    print(f"已删除 #{args.id}")


def main():
    p = argparse.ArgumentParser(description="极简版 CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add"); a.add_argument("title")
    a.add_argument("--priority", choices=["high","mid","low"], default="mid")
    a.set_defaults(func=add)

    l = sub.add_parser("list"); l.set_defaults(func=list_all)

    d = sub.add_parser("done"); d.add_argument("id", type=int); d.set_defaults(func=done)

    x = sub.add_parser("delete"); x.add_argument("id", type=int); x.set_defaults(func=delete)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
