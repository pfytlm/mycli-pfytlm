import argparse
import sys
from datetime import datetime

from .storage import load_items, save_items


def _next_id(items: list[dict]) -> int:
    return max((it["id"] for it in items), default=0) + 1


def cmd_add(args: argparse.Namespace) -> None:
    items = load_items()
    items.append({
        "id": _next_id(items),
        "title": args.title,
        "priority": args.priority,
        "done": False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    })
    save_items(items)
    print(f"已添加: [{args.priority}] {args.title}")


def cmd_list(args: argparse.Namespace) -> None:
    items = load_items()
    if not items:
        print("（暂无待办）")
        return
    for it in items:
        mark = "✅" if it["done"] else "⬜"
        print(f"{mark} #{it['id']}  [{it['priority']}]  {it['title']}")


def cmd_done(args: argparse.Namespace) -> None:
    items = load_items()
    for it in items:
        if it["id"] == args.id:
            it["done"] = True
            save_items(items)
            print(f"已完成 #{args.id}: {it['title']}")
            return
    print(f"未找到 #{args.id}")


def cmd_delete(args: argparse.Namespace) -> None:
    items = load_items()
    items = [it for it in items if it["id"] != args.id]
    save_items(items)
    print(f"已删除 #{args.id}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mycli",
        description="个人习惯 CLI demo",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="添加一个待办")
    p_add.add_argument("title", help="待办标题")
    p_add.add_argument(
        "--priority", choices=["high", "mid", "low"], default="mid",
    )
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="列出全部待办")
    p_list.set_defaults(func=cmd_list)

    p_done = sub.add_parser("done", help="把某个待办标记为完成")
    p_done.add_argument("id", type=int)
    p_done.set_defaults(func=cmd_done)

    p_del = sub.add_parser("delete", help="删除某个待办")
    p_del.add_argument("id", type=int)
    p_del.set_defaults(func=cmd_delete)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
