import pytest

from ..days.day_16 import Solution

test_input = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

solution = Solution()
data = solution.load(test_input.splitlines())

def test_part_one():
    assert solution.part_one(data) == "1651"

@pytest.mark.skip(reason="Dependent feature not yet ready")
def test_part_two():
    assert solution.part_two(data) == "1707"