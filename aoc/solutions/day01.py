from typing import Sequence
from aoc.util.data import read


def solve_part_1(input_data: Sequence[int]) -> int:
    count = 0
    for previous, current in zip(input_data, input_data[1:]):
        if current > previous:
            count += 1
    return count


def solve_part_2(input_data: Sequence[int]) -> int:
    count = 0
    previous_sum = None
    for first, second, third in zip(input_data[0:], input_data[1:], input_data[2:]):
        current_sum = first + second + third
        if previous_sum and current_sum > previous_sum:
            count += 1
        previous_sum = current_sum
    return count


if __name__ == "__main__":
    input_data = [int(x) for x in read("day01")]

    result_day_1 = solve_part_1(input_data)
    print(f"Day 01, Part 1: {result_day_1}")

    result_day_2 = solve_part_2(input_data)
    print(f"Day 01, Part 2: {result_day_2}")
