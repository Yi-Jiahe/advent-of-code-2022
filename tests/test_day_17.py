import pytest

from ..days.day_17 import Solution

test_input = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

solution = Solution()
data = solution.load(test_input.splitlines())

@pytest.mark.skip(reason="Not implemented")
def test_part_one():
    assert solution.part_one(data) == None

@pytest.mark.skip(reason="Not implemented")
def test_part_two():
    assert solution.part_two(data) == None