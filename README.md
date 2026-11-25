[![make.fun](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)](https://make.fun/c/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/Erwinsays12/makefun-excuse-almost-works/rank.svg)](https://make.fun/c/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/Erwinsays12/makefun-excuse-almost-works/reward.svg)](https://make.fun/c/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)

# The Excuse That Almost Works

Entry for the [make.fun competition "The Excuse That Almost Works"](https://make.fun/c/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5): a program that writes the one line a gamer texts the boss to skip work on GTA 6 launch week.

## What it does

`main.py` writes a single fixed, deterministic excuse to `/output/entry.txt` — one line, 16 words, 87 characters:

> Sorry, the council dug up my street overnight and my car's boxed in behind the barriers

The line is written to read like a real text sent in a hurry — plain words, no setup, no explanation, no signature — and to give a tired manager a specific, boring, believable detail (council roadworks boxing a car in) instead of one of the obvious excuses. The humour comes from the excuse's own logic: the car is fine, the street simply is not passable.

## Run it

```sh
python3 main.py
```

It validates the line first (one line, at most 20 words, 1–140 characters), writes it to `/output/entry.txt`, then reads it back and fails loudly if what is on disk differs from the intended text. Running it twice produces byte-identical output. An output path may be passed as an optional argument for local testing, e.g. `python3 main.py /tmp/entry.txt`.

## License

MIT — see [LICENSE](LICENSE).
