import pytest

from ..days.day_14 import Solution

test_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

solution = Solution()
data = solution.load(test_input.splitlines())

def test_part_one():
    assert solution.part_one(data) == "24"

def test_part_two():
    with pytest.raises(NotImplementedError):
        assert solution.part_two(data) == "93"