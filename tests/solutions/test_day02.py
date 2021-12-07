import pytest
from aoc.solutions.day02 import solve_part_1, solve_part_2


@pytest.fixture()
def example_input() -> list[str]:
    return ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def test_part_1(example_input: list[str]) -> None:
    result = solve_part_1(example_input)
    assert result.position * result.depth == 150


def test_part_2(example_input: list[str]) -> None:
    result = solve_part_2(example_input)
    assert result.position * result.depth == 900
