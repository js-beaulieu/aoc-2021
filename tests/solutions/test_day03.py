import pytest
from aoc.solutions.day03 import solve_part_1


@pytest.fixture()
def example_input() -> list[str]:
    return [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]


def test_part_1(example_input: list[str]) -> None:
    result = solve_part_1(example_input)
    assert result.gamma_rate * result.epsilon_rate == 198
