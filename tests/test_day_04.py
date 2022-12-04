import pytest

from ..days.day_04 import Solution

test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

solution = Solution()
data = solution.load(test_input.splitlines())

def test_part_one():
    assert(solution.part_one(data) == 2)

def test_part_two():
    with pytest.raises(NotImplementedError):
        solution.part_two(data)

@pytest.mark.parametrize("test_input, expected", [
    ([[1, 1], [1, 1]], True),
    ([[1, 2], [1, 3]], True),
    ([[1, 4], [2, 3]], True),
    ([[1, 2], [2, 3]], False),
    ([[1, 2], [3, 4]], False),
    ([[21, 21], [21, 21]], True),
    ([[21, 22], [21, 23]], True),
    ([[21, 24], [22, 23]], True),
    ([[21, 22], [22, 23]], False),
    ([[21, 22], [23, 24]], False)
])
def test_fully_contains(test_input, expected):
    first, second = test_input
    assert solution.fully_contains(first, second) == expected
    assert solution.fully_contains(second, first) == expected