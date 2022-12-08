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
    assert solution.part_two(data) == "8"

@pytest.mark.parametrize("test_input, expected", [
    ((1, 2), 4),
    ((3, 2), 8)
])
def test_scenic_score(test_input, expected):
    i, j = test_input
    assert data.scenic_score(i, j) == expected