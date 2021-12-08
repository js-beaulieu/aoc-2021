from collections import Counter
from dataclasses import dataclass
from typing import Sequence, Mapping
from functools import cached_property

from aoc.util.data import read


@dataclass(frozen=True)
class Submarine:
    diagnostic: Sequence[str]

    @cached_property
    def column_count(self) -> Mapping[int, Counter]:
        return {
            column: Counter(values)
            for column, values in enumerate(zip(*self.diagnostic))
        }

    @property
    def gamma_rate(self) -> int:
        # rofl that's what I get for trying to be clever
        val = [
            self.column_count[idx].most_common()[0][0]
            for idx in sorted(self.column_count.keys())
        ]
        return int("".join(val), 2)

    @property
    def epsilon_rate(self) -> int:
        # DRY amirite
        val = [
            self.column_count[idx].most_common()[1][0]
            for idx in sorted(self.column_count.keys())
        ]
        return int("".join(val), 2)


def solve_part_1(input_data: Sequence[str]) -> Submarine:
    return Submarine(diagnostic=input_data)


if __name__ == "__main__":
    input_data = read("day03part1")

    result_part_1 = solve_part_1(input_data)
    print(f"Day 02, Part 1: {result_part_1.gamma_rate * result_part_1.epsilon_rate}")
