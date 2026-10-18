# MLOps Basics

An educational Python project for the MLOps Basics course.

Currently includes an implementation of Root Mean Squared Error (RMSE) for evaluating energy predictions, with input validation and type annotations.

## Getting Started

Install [uv](https://docs.astral.sh/uv/), then clone the repository and install the dependencies:

```bash
git clone https://github.com/lapoverine/MLOps.git
cd MLOps
uv sync
```

Run the project:

```bash
uv run mlops
```

Expected output:

```text
Energy RMSE: 0.5000 eV
```

## Code Quality

The project uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting and [ty](https://docs.astral.sh/ty/) for static type checking.

```bash
uv run ruff check .
uv run ruff format --check .
uv run ty check
```