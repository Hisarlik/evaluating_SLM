#!/usr/bin/env python
"""Lightweight entrypoint to run benchmarks.

This is a placeholder that wires into the project CLI and can be
expanded as you implement evaluation logic.
"""

from __future__ import annotations

import pathlib
import sys

from evaluating_slm.cli import main

if __name__ == "__main__":
    # Example: run with default config
    cfg = pathlib.Path(__file__).parents[1] / "configs" / "default.yaml"
    sys.exit(main(["run", "-c", str(cfg)]))
