import pytest

from ..days.day_09 import Solution


solution = Solution()

def test_part_one():
    data = solution.load("""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines())
    assert solution.part_one(data) == "13"

def test_part_two():
    data = solution.load("""R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".splitlines())
    assert solution.part_two(data) == "36"