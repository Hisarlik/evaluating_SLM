# evaluating_SLM

Evaluation scaffolding for Small Language Models (SLMs). This repository provides a clean, opinionated project structure for running benchmarks, managing data and notebooks, and iterating on evaluation code.

## Structure

```
.
├── benchmark/           # Benchmark specs, scripts, and results guidelines
├── configs/             # YAML/JSON configs for experiments and benchmarks
├── data/                # Data folders (ignored by git except keepers)
│   ├── external/
│   ├── interim/
│   ├── processed/
│   └── raw/
├── examples/            # Minimal runnable examples / usage patterns
├── notebooks/           # Jupyter notebooks for exploration
├── scripts/             # CLI scripts, automation, and utilities
├── src/                 # Python source code (package: evaluating_slm)
│   └── evaluating_slm/
├── tests/               # Tests (optional; placeholder)
├── .gitignore           # Common ignores + data protections
├── Makefile             # Dev conveniences (format, lint, test)
├── pyproject.toml       # Project metadata + tooling configuration
└── .pre-commit-config.yaml
```

## Quickstart

- Create and activate a virtual environment, then install in editable mode:

```
uv pip install -e '.[dev]'
pre-commit install
```

- Format and lint:

```
make format
make lint
```

- Run placeholder example:

```
python examples/minimal_usage.py
```

### Install evaluation dependencies

- Core evaluation stack (Transformers, Datasets, Evaluate, metrics, LM harness):
  - `uv pip install -e '.[eval]'`
- Local inference with PyTorch (optional; choose the right wheel for your platform):
  - `uv pip install -e '.[torch]'`
- Hosted API clients (optional):
  - `uv pip install -e '.[apis]'`
Example (dev + torch in one go):
`uv pip install -e '.[dev,torch]'`

## Notes

- The `data/` directory contains nested `.gitignore` rules to prevent large datasets from entering version control while allowing metadata files to be tracked.
- Use the `configs/` directory to store benchmark and evaluation settings; pair each config with a short README entry describing intent.
