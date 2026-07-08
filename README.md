# B2B SaaS Cold Outreach — Research Repository

A curated research base on **cold outreach pipeline for B2B SaaS**: ten practitioner
voices, their recent LinkedIn posts and podcast/YouTube transcripts, organized so it can
support a real outbound playbook later.

> Take-home research project. Topic chosen from the provided list: *Cold outreach pipeline
> for B2B SaaS.*

## Why this topic

Cold outreach is the most "playbook-native" topic on the list — every source ties directly
to something you can operationalize (openers, sequences, email frameworks, SDR ops). It
also has an unusually strong bench of operators who publish on **both** a podcast/YouTube
(easy to transcribe via API) **and** LinkedIn, which makes for a well-rounded, verifiable
source base.

## The ten experts

Full annotations and links in [`research/sources.md`](research/sources.md).

| # | Expert | Practitioner proof | Primary angle |
|---|--------|--------------------|---------------|
| 1 | Armand Farrokh | Founder, 30 Minutes to President's Club; ex-VP Sales, Pave | Cold calling systems |
| 2 | Josh Braun | Founder, Josh Braun Sales Training | Anti-pushy email/call psychology |
| 3 | Jason Bay | Founder, Outbound Squad (trained 20k+ reps) | End-to-end outbound systems |
| 4 | Will Allred | Co-founder, Lavender | Data-backed cold-email copy |
| 5 | Becc Holland | Founder, Flip the Script; ex-Chorus.ai | Personalization at scale |
| 6 | Leslie Venetz | Founder, Sales-Led GTM Agency; bestselling author | Outbound strategy / "earn the right" |
| 7 | Jed Mahrle | Founder, Practical Prospecting; ex-Mailshake | Tactical multichannel sequences |
| 8 | Florin Tatulea | GTM Engineering, ZoomInfo (ex-Common Room) | Signal-based "Outbound 3.0" |
| 9 | Samantha McKenna | Founder, #samsales; ex-LinkedIn | "Show Me You Know Me" personalization |
| 10 | Tito Bohrt | CEO, AltiSales | Data-driven SDR operations |

## How the experts were chosen

- **Practitioners, not pundits** — each builds pipeline, runs an outbound agency/tool, or
  trains reps at scale (receipts in `sources.md`).
- **Two-channel** — active on LinkedIn *and* a podcast/YouTube/newsletter.
- **Current** — all publishing in 2025–2026.
- **Non-obvious but respected** — chosen for signal inside the outbound community rather
  than follower count. Kyle Coleman was considered but dropped after moving into a
  marketing-leadership role (less of a pure outbound practitioner).

## Repository structure

```
.
├── README.md                     # this file
├── research/
│   ├── sources.md                # the 10 experts: annotations, links, dates
│   ├── linkedin-posts/           # recent posts, one Markdown file per author
│   ├── youtube-transcripts/      # transcripts, grouped by expert then video
│   └── other/                    # foundational references, methodology notes
└── scripts/
    ├── fetch_youtube_transcripts.py   # transcript collection via youtube-transcript-api
    ├── format_linkedin_posts.py       # normalize manually-collected posts → Markdown
    ├── collection_config.json         # video manifest (per expert)
    ├── linkedin_posts.json            # LinkedIn post manifest (per expert)
    ├── requirements.txt
    └── README.md                      # how to run the collectors
```

## Collection methodology

- **YouTube / podcast transcripts** are pulled programmatically with the free
  [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/) — it reads
  the caption track directly (no API key, no HTML scraping). Video list lives in
  `scripts/collection_config.json`; output lands in `research/youtube-transcripts/`.
- **LinkedIn posts** are collected manually from each author's *Activity* feed, because
  LinkedIn exposes no public read API and its ToS forbids scraping. They're recorded in
  `scripts/linkedin_posts.json` and rendered to Markdown by `format_linkedin_posts.py`.

Everything under `research/` is regenerable from the two version-controlled manifests, so
the collection is auditable and repeatable rather than a pile of one-off downloads.

### Reproduce

```bash
cd scripts
pip install -r requirements.txt
python fetch_youtube_transcripts.py --config collection_config.json --out ../research/youtube-transcripts
python format_linkedin_posts.py     --config linkedin_posts.json   --out ../research/linkedin-posts
```

## Notes

- Commits are intentionally incremental (scaffold → scripts → sources → collected content)
  rather than one large drop.
- This is a source base, not the playbook itself; `sources.md` flags *what to mine* from
  each voice so a playbook can be built on top of it.

## Synthesis

- [PLAYBOOK.md](PLAYBOOK.md) - the ten experts plays stitched into one outbound cadence
- [research/insights.md](research/insights.md) - cross-cutting patterns across the ten
