import pytest
from aoc.solutions.day01 import solve_part_1, solve_part_2


@pytest.fixture()
def example_input() -> list[int]:
    return [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]


def test_part_1(example_input):
    assert solve_part_1(example_input) == 7


def test_part_2(example_input):
    assert solve_part_2(example_input) == 5
