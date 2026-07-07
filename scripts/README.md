# Collection scripts

Reproducible collection for this research repo. Everything under `../research/`
can be regenerated from the two manifest files in this folder.

## 1. YouTube / podcast transcripts

`fetch_youtube_transcripts.py` pulls caption tracks with the free
[`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/)
(no API key, no HTML scraping) for every video listed in
`collection_config.json`, and writes annotated Markdown to
`../research/youtube-transcripts/<expert-slug>/`.

```bash
pip install -r requirements.txt
python fetch_youtube_transcripts.py --config collection_config.json --out ../research/youtube-transcripts
```

The script is idempotent (re-running only fetches new videos) and tolerant of
videos that have captions disabled.

## 2. LinkedIn posts

LinkedIn exposes no public read API and its ToS forbids scraping, so posts are
collected **manually** from each author's *Activity* feed into
`linkedin_posts.json`. `format_linkedin_posts.py` then normalizes them into one
Markdown file per author.

```bash
python format_linkedin_posts.py --config linkedin_posts.json --out ../research/linkedin-posts
```

## Manifests

- `collection_config.json` — the 10 experts + the videos to transcribe.
- `linkedin_posts.json` — the 10 experts + their collected posts.

Keeping the source list in version-controlled manifests (rather than ad-hoc
downloads) is what makes the collection auditable and repeatable.
