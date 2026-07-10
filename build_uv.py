#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""构建 capswriter-client / capswriter-server 的 wheel 包（供 PyPI 或本地安装）。"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKAGES = (
    ROOT / "packages" / "capswriter-client",
    ROOT / "packages" / "capswriter-server",
)
DIST = ROOT / "dist" / "uv"


def run(cmd: list[str], cwd: Path) -> None:
    print(f"\n>>> {' '.join(cmd)}")
    subprocess.run(cmd, cwd=cwd, check=True)


def main() -> None:
    DIST.mkdir(parents=True, exist_ok=True)
    for pkg in PACKAGES:
        run([sys.executable, "-m", "build", "--outdir", str(DIST)], cwd=pkg)
    print("\n构建完成:")
    for whl in sorted(DIST.glob("*.whl")):
        print(f"  {whl.name}")


if __name__ == "__main__":
    main()
