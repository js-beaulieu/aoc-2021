from typing import Sequence
from dataclasses import dataclass
from aoc.util.data import read


@dataclass(frozen=True)
class Submarine:
    position: int
    depth: int


@dataclass(frozen=True)
class SubmarineWithAim(Submarine):
    aim: int


def solve_part_1(input_data: Sequence[str]) -> Submarine:
    result = Submarine(position=0, depth=0)
    for row in input_data:
        direction, value = row.split(" ")
        value_numeric = int(value)
        position, depth = result.position, result.depth

        if direction == "forward":
            position += value_numeric
        elif direction == "down":
            depth += value_numeric
        elif direction == "up":
            depth -= value_numeric
        result = Submarine(position=position, depth=depth)

    return result


def solve_part_2(input_data: Sequence[str]) -> SubmarineWithAim:
    result = SubmarineWithAim(position=0, depth=0, aim=0)
    for row in input_data:
        direction, value = row.split(" ")
        value_numeric = int(value)
        position, depth, aim = result.position, result.depth, result.aim

        if direction == "down":
            aim += value_numeric
        elif direction == "up":
            aim -= value_numeric
        elif direction == "forward":
            position += value_numeric
            depth += aim * value_numeric

        result = SubmarineWithAim(position=position, depth=depth, aim=aim)

    return result


if __name__ == "__main__":
    input_data = read("day02part1")

    result_part_1 = solve_part_1(input_data)
    print(f"Day 02, Part 1: {result_part_1.position * result_part_1.depth}")

    result_part_2 = solve_part_2(input_data)
    print(f"Day 02, Part 2: {result_part_2.position * result_part_2.depth}")
