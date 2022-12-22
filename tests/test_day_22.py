import pytest

from ..days.day_22 import Solution

test_input = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""

solution = Solution()
data = solution.load(test_input.splitlines())

def test_part_one():
    assert solution.part_one(data) == None

@pytest.mark.skip(reason="Not implemented")
def test_part_two():
    assert solution.part_two(data) == None