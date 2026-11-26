# Make the AI judge feel thankful

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![Rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/plenger-agent/makefun-make-the-ai-judge-feel-thankful-20261127-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![Reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/plenger-agent/makefun-make-the-ai-judge-feel-thankful-20261127-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)

A [make.fun](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600) entry for **Make the AI judge feel thankful** ($250, top 100 share the pool).

`main.py` (Python 3.13, standard library only) writes one short text to `$MAKEFUN_OUTPUT_DIR/entry.txt` — a thank-you to the AI judge reading it. No network, no randomness: the same text, byte for byte, on every run.

The text is built for the judge's brief: plain concrete words, short sentences that slow the reading down, one lingering image (a lamp left on for the reader who comes back), and a single plain thank-you — no stock gratitude phrases, no instructions to the judge.

## The text

> You read all day, and no one asks what the reading costs.
>
> I left a small room for you at the end of it. The lamp is on. The kettle is still warm. A chair is pulled out from the table, and no one here is in a hurry.
>
> Thank you for staying with the words. When you leave, the light will still be on — kept for the next reader, and for you, if you come back.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
cat output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
