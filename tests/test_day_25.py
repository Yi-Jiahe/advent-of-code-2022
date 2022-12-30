import pytest

from ..days.day_25 import Solution

test_input = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""

solution = Solution()
data = solution.load(test_input.splitlines())


def test_part_one():
    assert solution.part_one(data) == "2=-1=0"


@pytest.mark.skip(reason="Not implemented")
def test_part_two():
    assert solution.part_two(data) == None


@pytest.mark.parametrize("test_input, expected", [
    ("1=-0-2", 1747),
    ("12111", 906),
    ("2=0=", 198),
    ("21",       11),
    ("2=01",      201),
    ("111",       31),
    ("20012",     1257),
    ("112",       32),
    ("1=-1=",      353),
    ("1-12",      107),
    ("12",        7),
    ("1=",        3),
    ("122",       37),
])
def test_SNAFU_to_decimal(test_input, expected):
    assert solution.SNAFU_to_decimal(test_input) == expected
