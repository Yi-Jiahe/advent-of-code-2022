import pytest

from ..days.day_03 import Solution

test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

solution = Solution()
data = solution.load(test_input.splitlines())

def test_part_one():
    assert(solution.part_one(data) == 157)

def test_part_two():
    assert(solution.part_two(data) == 70)