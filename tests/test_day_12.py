import pytest

from ..days.day_12 import Solution

test_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

solution = Solution()
data = solution.load(test_input.splitlines())

def test_part_one():
    assert solution.part_one(data) == "31"

def test_part_two():
    with pytest.raises(NotImplementedError):
        assert solution.part_two(data) == None