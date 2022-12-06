import pytest

from ..days.day_06 import Solution

test_input = """"""

solution = Solution()
data = solution.load(test_input.splitlines())

def test_part_one():
    pass

def test_part_two():
    with pytest.raises(NotImplementedError):
        assert solution.part_two(data) == None

@pytest.mark.parametrize("test_input, expected", [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)

])
def test_find_marker(test_input, expected):
    assert solution.find_marker(test_input) == expected