import pytest

from ..days.day_06 import Solution

test_input = """"""

solution = Solution()
data = solution.load(test_input.splitlines())

def test_part_one():
    pass

def test_part_two():
    pass

@pytest.mark.parametrize("test_input, expected", [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)

])
def test_find_start_of_packet_marker(test_input, expected):
    assert solution.find_start_of_packet_marker(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26)
])
def test_find_start_of_message_marker(test_input, expected):
    assert solution.find_start_of_message_marker(test_input) == expected