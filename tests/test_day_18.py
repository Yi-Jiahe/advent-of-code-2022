import pytest

from ..days.day_18 import Solution

test_input = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""

solution = Solution()
data = solution.load(test_input.splitlines())

def test_part_one():
    assert solution.part_one(data) == "64"

def test_part_two():
    with pytest.raises(NotImplementedError):
        assert solution.part_two(data) == None