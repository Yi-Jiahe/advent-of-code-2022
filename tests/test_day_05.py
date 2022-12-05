import pytest

from ..days.day_05 import Solution

test_input = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

solution = Solution()
data = solution.load(test_input.splitlines())

solution.stacks = [
        ['Z', 'N'],
        ['M', 'C', 'D'],
        ['P']
    ]


def test_part_one():
    assert solution.part_one(data) == "CMZ"

def test_part_two():
    assert solution.part_two(data) == "MCD"