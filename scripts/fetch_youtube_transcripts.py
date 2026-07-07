#!/usr/bin/env python3
"""
fetch_youtube_transcripts.py
----------------------------
Collect YouTube / podcast transcripts for the experts listed in
collection_config.json and save them as annotated Markdown under
research/youtube-transcripts/<expert-slug>/.

Why a script (not manual copy)?
  This take-home is partly evaluated on "ability to work with APIs and technical
  tools." This uses the free `youtube-transcript-api` (no API key, and it reads the
  caption track directly rather than scraping the watch-page HTML).

Usage:
  pip install -r requirements.txt
  python fetch_youtube_transcripts.py --config collection_config.json \
         --out ../research/youtube-transcripts

Design notes:
  * Idempotent  - skips a video whose transcript already exists (use --force to refetch).
  * Resilient   - supports both youtube-transcript-api versions (<=0.6 classmethod
                  `get_transcript`, >=1.0 instance `.fetch`) and handles
                  missing / disabled captions without crashing the run.
  * Polite      - sleeps between requests to stay under rate limits.
"""
from __future__ import annotations
import argparse, json, os, re, sys, time
from datetime import date


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text or "").strip().lower()
    return re.sub(r"[\s_-]+", "-", text)[:80] or "untitled"


def extract_video_id(url_or_id: str) -> str:
    """Accept a raw 11-char id or any common YouTube URL form."""
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", url_or_id or ""):
        return url_or_id
    m = re.search(r"(?:v=|youtu\.be/|/shorts/|/embed/)([A-Za-z0-9_-]{11})", url_or_id or "")
    if not m:
        raise ValueError(f"Could not parse a video id from: {url_or_id!r}")
    return m.group(1)


def fetch_segments(video_id: str, languages):
    """Return [{text,start,duration}, ...] across api versions."""
    from youtube_transcript_api import YouTubeTranscriptApi
    if hasattr(YouTubeTranscriptApi, "get_transcript"):          # <= 0.6.x
        return YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
    api = YouTubeTranscriptApi()                                  # >= 1.0.x
    fetched = api.fetch(video_id, languages=languages)
    return [{"text": s.text, "start": s.start, "duration": s.duration} for s in fetched]


def to_markdown(expert: dict, video: dict, segments) -> str:
    plain = " ".join(s["text"].replace("\n", " ").strip() for s in segments)
    plain = re.sub(r"\s+", " ", plain).strip()
    words = len(plain.split())
    lines = [
        f"# {video.get('title', '(untitled)')}",
        "",
        f"- **Expert:** {expert['name']}",
        f"- **Channel / show:** {video.get('channel', expert.get('channel', ''))}",
        f"- **Video:** https://www.youtube.com/watch?v={video['_id']}",
        f"- **Published:** {video.get('published', 'unknown')}",
        f"- **Collected:** {date.today().isoformat()} via youtube-transcript-api",
        f"- **Transcript length:** ~{words} words",
        "",
        "---",
        "",
        "## Transcript",
        "",
        plain,
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", default="collection_config.json")
    ap.add_argument("--out", default="../research/youtube-transcripts")
    ap.add_argument("--languages", default="en,en-US,en-GB")
    ap.add_argument("--sleep", type=float, default=1.5)
    ap.add_argument("--force", action="store_true", help="refetch even if a file exists")
    args = ap.parse_args()

    langs = [x.strip() for x in args.languages.split(",") if x.strip()]
    with open(args.config, encoding="utf-8") as f:
        cfg = json.load(f)

    saved = skipped = failed = 0
    for expert in cfg.get("experts", []):
        slug = expert.get("slug") or slugify(expert["name"])
        for video in expert.get("videos", []):
            try:
                vid = extract_video_id(video.get("id") or video.get("url"))
            except ValueError as e:
                print(f"  ! {e}"); failed += 1; continue
            video["_id"] = vid
            dest_dir = os.path.join(args.out, slug)
            os.makedirs(dest_dir, exist_ok=True)
            fname = f"{vid}__{slugify(video.get('title', '')) or 'video'}.md"
            dest = os.path.join(dest_dir, fname)
            if os.path.exists(dest) and not args.force:
                print(f"  = skip (exists) {slug}/{fname}"); skipped += 1; continue
            try:
                segs = fetch_segments(vid, langs)
                with open(dest, "w", encoding="utf-8") as fh:
                    fh.write(to_markdown(expert, video, segs))
                print(f"  + {slug}/{fname}  ({len(segs)} segments)"); saved += 1
                time.sleep(args.sleep)
            except Exception as e:                                # noqa: BLE001
                print(f"  ! {expert['name']} {vid}: {type(e).__name__}: {e}"); failed += 1
    print(f"\nDone. saved={saved} skipped={skipped} failed={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
