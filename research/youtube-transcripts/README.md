# YouTube / podcast transcripts

Transcripts are collected with [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/)
via `../../scripts/fetch_youtube_transcripts.py`, driven by
`../../scripts/collection_config.json`. Output is one folder per expert.

## What's here

- **`josh-braun/`** — a fully collected, timestamped transcript
  (*Multi-Million Dollar Cold Email Prospecting Template*), captured as the worked example.

## Fetch the rest

The video manifest (`collection_config.json`) lists additional episodes (e.g. the 30MPC
*Cold Calling Masterclass*). To pull them:

```bash
cd ../../scripts
pip install -r requirements.txt
python fetch_youtube_transcripts.py --config collection_config.json --out ../research/youtube-transcripts
```

New transcripts land here automatically, grouped by expert slug. Add more videos by
appending to the `videos` array for any expert in the manifest and re-running (the script
skips anything already downloaded).

## Why podcasts matter for this topic

Several of these experts do their most tactical teaching in long-form audio/video —
30 Minutes to President's Club and Outbound Squad especially — so transcripts are where the
step-by-step cold-call and sequencing frameworks live in full.
