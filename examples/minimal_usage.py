from __future__ import annotations

import pathlib
from evaluating_slm.cli import main


if __name__ == "__main__":
    # Demonstrate calling the CLI with the default config.
    cfg = pathlib.Path(__file__).parents[1] / "configs" / "default.yaml"
    raise SystemExit(main(["run", "-c", str(cfg)]))

