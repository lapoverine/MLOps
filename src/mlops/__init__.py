from collections.abc import Sequence
from math import sqrt


def add_numbers(a: int, b: int) -> int:
    return a + b


def calculate_rmse(actual: Sequence[float], predicted: Sequence[float]) -> float:
    if len(actual) != len(predicted):
        raise ValueError("Arrays must have the same length")

    if not actual:
        raise ValueError("Arrays must not be empty")

    mse = sum((a - p) ** 2 for a, p in zip(actual, predicted)) / len(actual)
    return sqrt(mse)


def main() -> None:
    actual_energies = [-10.0, -15.0, -20.0]
    predicted_energies = [-9.5, -14.5, -19.5]

    error = calculate_rmse(actual_energies, predicted_energies)
    print(f"Energy RMSE: {error:.4f} eV")
