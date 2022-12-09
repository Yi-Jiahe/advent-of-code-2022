import pytest

from ..days.day_09 import Solution

test_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

solution = Solution()
data = solution.load(test_input.splitlines())

def test_part_one():
    assert solution.part_one(data) == "13"

def test_part_two():
    with pytest.raises(NotImplementedError):
        assert solution.part_two(data) == None