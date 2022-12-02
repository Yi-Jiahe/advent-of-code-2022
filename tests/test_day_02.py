import pytest

from ..days.day_02 import Solution

test_input = """A Y
B X
C Z"""

solution = Solution()
data = solution.load(test_input.splitlines())

def test_part_one():
    assert(solution.part_one(data) == 15)

def test_part_two():
    assert(solution.part_two(data) == 12)