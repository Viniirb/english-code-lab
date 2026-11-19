#!/usr/bin/env python3
"""Show which modules are done. Runs the same validation as GitHub Actions.

    python scripts/progress.py          # all modules
    python scripts/progress.py 01 02    # only some
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main(selected: list) -> None:
    done = total = 0
    for line in (ROOT / "scripts" / "modules.txt").read_text(encoding="utf-8").splitlines():
        module, _slug, title, _level = line.split("|")
        if selected and module not in selected:
            continue
        total += 1
        ok = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_module.py"), module], capture_output=True
        ).returncode == 0
        done += ok
        print(f"{'✔' if ok else '·'} {module}  {title}")
    print(f"\n{done} of {total} modules done.")


if __name__ == "__main__":
    main(sys.argv[1:])
