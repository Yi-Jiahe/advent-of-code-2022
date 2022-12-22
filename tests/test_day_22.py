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
board = solution.load(test_input.splitlines())

def test_load():
        assert board.max_size == [12, 16]

@pytest.mark.parametrize("test_input, expected", [
    ((7, 0), (1, 7)),
    ((6, 1), (6, 5)),
    ((9, 2), (16, 9)),
    ((15, 3), None)
])
def test_rollover_boundary(test_input, expected):
    print(test_input)
    assert board.rollover_boundary(*test_input) == expected

def test_part_one():
    assert solution.part_one(board) == "6032"

@pytest.mark.skip(reason="Not implemented")
def test_part_two():
    assert solution.part_two(board) == None