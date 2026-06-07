#!/usr/bin/env python3
"""Refresh the ★ counts in the flagship table of README.md from the GitHub API.

Any table row whose last cell is a bare integer and whose first cell links to a
github.com/<owner>/<repo> is treated as a flagship row and its star count is
updated. Also prints a notice if any other linked repo has crossed 100★ so it
can be promoted into the flagship band by hand.
"""

import json
import re
import subprocess
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"
REPO = re.compile(r"github\.com/([\w.\-]+/[\w.\-]+?)(?:\)|\s|/|$)")
ROW = re.compile(r"^\|(?P<first>[^|]*\]\([^)]+\)[^|]*)\|(?P<mid>.*)\|\s*(?P<stars>\d[\d,]*)\s*\|\s*$")
FLAGSHIP_MIN = 100


def stars_for(slugs):
    out = {}
    for i in range(0, len(slugs), 50):
        batch = slugs[i:i + 50]
        frags = " ".join(
            f'r{j}: repository(owner: "{s.split("/")[0]}", name: "{s.split("/")[1]}") {{ stargazerCount }}'
            for j, s in enumerate(batch)
        )
        r = subprocess.run(["gh", "api", "graphql", "-f", f"query={{ {frags} }}"],
                           capture_output=True, text=True, timeout=60)
        data = (json.loads(r.stdout).get("data") or {}) if r.returncode == 0 else {}
        for j, s in enumerate(batch):
            node = data.get(f"r{j}")
            if node:
                out[s] = node["stargazerCount"]
    return out


def main():
    lines = README.read_text().split("\n")
    # collect every linked yigitkonur repo so we can also flag promotions
    slugs = sorted({m.group(1) for ln in lines for m in REPO.finditer(ln)
                    if m.group(1).lower().startswith("yigitkonur/")})
    stars = stars_for(slugs)

    flagship = set()
    changed = 0
    out = []
    for ln in lines:
        m = ROW.match(ln)
        rm = REPO.search(ln)
        if m and rm and rm.group(1) in stars:
            flagship.add(rm.group(1))
            new = stars[rm.group(1)]
            if str(new) != m.group("stars").replace(",", ""):
                ln = f"|{m.group('first')}|{m.group('mid')}| {new} |"
                changed += 1
        out.append(ln)

    if changed:
        README.write_text("\n".join(out))
    print(f"updated {changed} flagship star count(s)")

    promote = sorted((s for s, n in stars.items() if n >= FLAGSHIP_MIN and s not in flagship),
                     key=lambda s: -stars[s])
    for s in promote:
        print(f"::notice::{s} has {stars[s]}★ — consider promoting it to the flagship table")


if __name__ == "__main__":
    main()
