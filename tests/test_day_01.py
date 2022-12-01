from ..days.day_01 import Solution

test_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

solution = Solution()
data = solution.load(test_input.splitlines())

def test_part_one():
    assert(solution.part_one(data) == 24000)

def test_part_two():
    assert(solution.part_two(data) == 45000)