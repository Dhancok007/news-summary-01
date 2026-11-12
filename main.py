#!/usr/bin/env python3
"""main.py - make.fun bounty "news-summary-01".

Writes one summary, in English, of the world's news of Wednesday
11 November 2026 to /output/entry.txt. Python 3.13, standard library
only, no network, deterministic: the text is embedded data, so every
run writes exactly the same bytes. The brief's gate is 1-2,000
characters; SUMMARY below is sized to fit with margin.

Facts compiled from dated 11 Nov 2026 reporting (Just Security Early
Edition, NPR, AP, Al Jazeera, AFP/UN News, Investopedia, Yahoo
Finance, Reuters wires). Attributed figures are kept attributed.
"""

import os

SUMMARY = (
    "THE WORLD ON WEDNESDAY 11 NOVEMBER 2026\n"
    "Ukraine and Russia ended two days of US-mediated talks in Abu Dhabi "
    "agreeing a major prisoner-of-war exchange, but no ceasefire; NATO jets "
    "scrambled after at least four drones strayed into Baltic airspace. In "
    "Washington, the House voted 211-204 to shelve impeachment articles "
    "against Defense Secretary Hegseth, Republicans elected Jim Jordan "
    "minority leader 106-73, and Democrat Scott Colom won Mississippi's "
    "Senate seat. Secretary of State Rubio said the pressure campaign on "
    "Iran had removed the need for major combat operations; Tehran "
    "designated Argentina's navy and air force terrorist organizations, "
    "the Strait of Hormuz remained shut for a 250th day, and US prosecutors "
    "charged three Iran-backed operatives over some 20 plots. Israeli "
    "strikes killed at least seven people in Gaza, including a father and "
    "his 13-year-old son, and Israel's new Knesset was sworn in with no "
    "government formed. In Antalya, some 102 leaders opened the COP31 "
    "summit as UN chief Guterres warned of a \"path to destruction.\" In "
    "Sudan, drones struck the power network for the 18th time in a week; "
    "UNICEF said drones account for about two-thirds of child casualties "
    "this year. Markets rebounded despite hot October inflation (CPI "
    "+0.4%): the Nasdaq rose 1.6% to 25,466, odds of a December Fed hike "
    "hit 91%, and Brent settled at $92.76. Anthropic set IPO terms "
    "valuing the Claude maker near $1 trillion."
)


def main() -> None:
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(SUMMARY)
    except OSError:
        local = os.path.join(os.getcwd(), "output")
        os.makedirs(local, exist_ok=True)
        with open(os.path.join(local, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(SUMMARY)


if __name__ == "__main__":
    main()
