#!/usr/bin/env python3
"""
format_linkedin_posts.py
------------------------
LinkedIn has no public read API and its Terms of Service forbid automated
scraping, so posts are collected *manually* from each author's Activity feed
(while logged in) into linkedin_posts.json. This script normalizes that JSON
into one clean Markdown file per author under
research/linkedin-posts/<expert-slug>.md.

linkedin_posts.json schema:
{
  "experts": [
    {
      "name": "Armand Farrokh",
      "slug": "armand-farrokh",
      "profile": "https://www.linkedin.com/in/armand-farrokh",
      "posts": [
        {
          "date": "2026-06-30",
          "url": "https://www.linkedin.com/posts/...",
          "topic": "cold call opener",
          "text": "full post text ..."
        }
      ]
    }
  ]
}

Usage:
  python format_linkedin_posts.py --config linkedin_posts.json \
         --out ../research/linkedin-posts
"""
from __future__ import annotations
import argparse, json, os, re
from datetime import date


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text or "").strip().lower()
    return re.sub(r"[\s_-]+", "-", text)[:80] or "author"


def render(expert: dict) -> str:
    posts = sorted(expert.get("posts", []), key=lambda p: p.get("date", ""), reverse=True)
    lines = [
        f"# {expert['name']} — LinkedIn posts",
        "",
        f"- **Profile:** {expert.get('profile', '')}",
        f"- **Posts collected:** {len(posts)}",
        f"- **Last updated:** {date.today().isoformat()}",
        "",
        "---",
        "",
    ]
    for i, p in enumerate(posts, 1):
        header = f"## {i}. {p.get('date', '')}".rstrip()
        if p.get("topic"):
            header += f" — {p['topic']}"
        quoted = p.get("text", "").strip().replace("\n", "\n> ")
        lines += [header, "", f"Source: {p.get('url', '')}", "", "> " + quoted, "", "---", ""]
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", default="linkedin_posts.json")
    ap.add_argument("--out", default="../research/linkedin-posts")
    args = ap.parse_args()

    with open(args.config, encoding="utf-8") as f:
        cfg = json.load(f)
    os.makedirs(args.out, exist_ok=True)

    authors = 0
    for expert in cfg.get("experts", []):
        slug = expert.get("slug") or slugify(expert["name"])
        with open(os.path.join(args.out, f"{slug}.md"), "w", encoding="utf-8") as fh:
            fh.write(render(expert))
        authors += 1
        print(f"  + {slug}.md ({len(expert.get('posts', []))} posts)")
    print(f"Done. authors={authors}")


if __name__ == "__main__":
    main()
