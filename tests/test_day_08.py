import pytest

from ..days.day_08 import Solution

test_input = """30373
25512
65332
33549
35390"""

solution = Solution()
data = solution.load(test_input.splitlines())

def test_part_one():
    assert solution.part_one(data) == "21"

def test_part_two():
    with pytest.raises(NotImplementedError):
        assert solution.part_two(data) == None