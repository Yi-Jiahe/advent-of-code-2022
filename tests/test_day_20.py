import pytest

from ..days.day_20 import Solution

test_input = """1
2
-3
3
-2
0
4"""

solution = Solution()
data = solution.load(test_input.splitlines())

def test_part_one():
    assert solution.part_one(data) == "3"

def test_part_two():
    assert solution.part_two(data) == "1623178306"