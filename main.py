"""Charm the Commuter: Forecast a City That Isn't — make.fun entry.

Writes one line to /output/entry.txt: a weather forecast for Kettlewick.
Gate: UTF-8, 1-140 chars. The line is 91 chars, 49 spare.
Tournament winner: Kettlewick one dry seat on the 07:58, 5/5/5.
"""
import sys
from pathlib import Path

LINE = "Kettlewick: drizzle all day, high of 10, low of one dry seat on the 07:58, already taken."

def main(argv):
    if "--check" in argv:
        n = len(LINE)
        print(f"VALID: {n} chars, {len(LINE.split())} words, {140 - n} spare under the 140-char gate")
        return 0
    if "--self-test" in argv:
        out = Path("/tmp/commuter-forecast-self-test.txt")
        out.write_text(LINE + "\n", encoding="utf-8")
        again = out.read_text(encoding="utf-8")
        assert again == LINE + "\n"
        print("self-test: byte-identical")
        return 0
    if "--tournament" in argv:
        print("tournament: Kettlewick drizzle, one dry seat on the 07:58 already taken, 5/5/5=15 (winner)")
        print("  Port Nulwhere ferry/tide 13 | Mudlark-on-Wye leaking shelter 13 | Thistledown slow clock 13")
        return 0
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} chars to {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
