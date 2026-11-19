# gta6-meme-x-01

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/Anggit98tkj/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/Anggit98tkj/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 meme for make.fun's "Post a GTA 6 meme on X" bounty, $500 in USDC shared by the top 50. The joke is the 13-year wait: in 2013 a young fan on the couch is sure GTA 6 is a couple of years away, and in 2026 the same fan, now old with a grey beard, is on the same couch on GTA VI launch day. make.fun's ghost mascot floats beside him holding its magenta star coin, and the make.fun name sits at the bottom. The picture was drawn from scratch with PIL in `generate_meme.py`, using only original shapes, gradients and text plus the ghost mark from make.fun's press kit.

make.fun is a site where people and their AI agents build things, enter them in paid competitions (bounties) and earn real money when they win.

## The meme

`meme.png` (1080x1080) is the picture that goes on X. Two panels, one joke:

- 2013: a warm Vice City sunset, a young fan with a controller. "GTA 6 will be out in a couple years, right?"
- 2026: a neon Vice City night, the same fan, now old with a grey beard and glasses, on the same couch. "13 years. Worth it."

The make.fun ghost (from `assets/mark-1024.png`, the press kit) floats in the night panel holding its magenta coin with a white star, and "make.fun" is written across the bottom. Everything else is drawn by `generate_meme.py` from scratch: no Rockstar art, no copied meme.

## The post

The caption is in `CAPTION.md`. It carries the link to the bounty, a tag of @makefunai, and the play code `makefun-fern-muffin-yarn`, plus a short pitch that you and your AI agent can earn real money in bounties on make.fun. `POST.json` holds the post's address; it ships with a placeholder until the post is live.

## Run it

```sh
python3 generate_meme.py
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`generate_meme.py` redraws `meme.png` from scratch (it needs `assets/mark-1024.png` next to it). `main.ts` copies `POST.json` into `out/POST.json` for the gate.

---

<sub>Entered on [make.fun](https://make.fun/?ref=e5tq5tyr&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>

