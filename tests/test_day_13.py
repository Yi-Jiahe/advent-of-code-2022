import pytest

from ..days.day_13 import Solution

test_input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

solution = Solution()
data = solution.load(test_input.splitlines())

def test_part_one():
    assert solution.part_one(data) == "13"

def test_part_two():
    with pytest.raises(NotImplementedError):
        assert solution.part_two(data) == None

@pytest.mark.parametrize("test_input, expected", [
    (([1,1,3,1,1], [1,1,5,1,1]), 1),
    (([[1],[2,3,4]], [[1],4]), 1),
    (([9], [[8,7,6]]), -1),
    (([[4,4],4,4], [[4,4],4,4,4]), 1),
    (([7,7,7,7], [7,7,7]), -1),
    (([], [3]), 1),
    (([[[]]], [[]]), -1),
    (([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]), -1)
])
def test_compare(test_input, expected):
    left, right = test_input
    assert solution.compare(left, right) == expected