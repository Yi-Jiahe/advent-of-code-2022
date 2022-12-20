import pytest

from ..days.day_19 import Solution

test_input = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""

solution = Solution()
data = solution.load(test_input.splitlines())

@pytest.mark.skip(reason="Solution not ready")
def test_part_one():
    assert solution.part_one(data) == "33"

@pytest.mark.skip(reason="Not implemented")
def test_part_two():
    assert solution.part_two(data) == None