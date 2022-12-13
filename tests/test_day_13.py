import pytest

from ..days.day_13 import Solution

test_input = """"""

solution = Solution()
data = solution.load(test_input.splitlines())

def test_part_one():
    with pytest.raises(NotImplementedError):
        assert solution.part_one(data) == None

def test_part_two():
    with pytest.raises(NotImplementedError):
        assert solution.part_two(data) == None

def test_compare():
    assert solution.compare([1], [2]) == 1