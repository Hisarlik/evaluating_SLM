from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="slm-eval", description="Evaluate Small Language Models (SLMs)"
    )
    sub = parser.add_subparsers(dest="command", required=False)

    run = sub.add_parser("run", help="Run benchmarks (placeholder)")
    run.add_argument("--config", "-c", help="Path to config file", default="configs/default.yaml")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "run":
        print(f"[slm-eval] Would run benchmarks with config: {args.config}")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())

