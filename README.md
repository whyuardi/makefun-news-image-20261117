# makefun-news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/whyuardi/makefun-news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/whyuardi/makefun-news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

The World in One Day — one image that sums up the world's news of Tuesday
17 November 2026: a night-side globe ringed by six vignettes, each with one
short bold label, titled in a footer band
`TUESDAY 17 NOVEMBER 2026 - THE WORLD IN ONE DAY`.

## The six stories (all first reported 17 November 2026)

1. **Gaza aid plea** — the UK, Australia, Canada and Italy jointly urged
   Israel to open Gaza crossings for humanitarian aid; UN agencies warned
   of a worsening winter emergency (1.7M displaced, 1.4M in acute hunger).
2. **Crimean Bridge hit** — a Ukrainian strike closed the Crimean Bridge;
   Russia struck bridges over the Dnipro in Kyiv the same day.
3. **Hormuz tanker mined** — a fourth oil tanker caught fire in the Strait
   of Hormuz after striking a naval mine; Iran's Revolutionary Guards also
   said they seized a US drone.
4. **COP31 climate deal** — negotiators in Antalya published a draft deal
   calling for a faster fossil-fuel phase-out and $120bn climate finance
   by 2035.
5. **Japan scrambles jets** — Japan launched fighter jets after two
   suspected Russian aircraft violated its airspace.
6. **Xi-Trump-Putin summit** — China confirmed a first-ever trilateral
   meeting of Xi Jinping, Donald Trump and Vladimir Putin, set for
   Thursday in Shenzhen on the APEC sidelines.

## How it was made

The illustration was generated text-free (an image model garbles words),
then the title and six labels were composited with PIL (DejaVu Sans Bold)
so every word is spelled exactly and legible at ~300 px. The image is
stored as single-line base64 in `entry.b64`; `main.py` (stdlib only)
decodes it to `/output/entry.png`.

## Gate figures

- Format: JPEG bytes (name stays `entry.png`), 1024 x 1024 px
- Size: 252,134 bytes (limit 1,048,576)
- Deterministic: two runs write identical bytes

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
