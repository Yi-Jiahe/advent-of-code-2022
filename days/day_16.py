import re
import functools


class Volcano:
    def __init__(self, valves):
        self.valves = valves

    @functools.cache
    def total_flow_rate(self, open_valves: frozenset):
        ret = 0
        for valve in open_valves:
            ret += self.valves[valve].flow_rate
        return ret
    
    def most_pressure(self):
        @functools.cache
        def step(position: str, time_left: int, open_valves: frozenset):
            if time_left == 0:
                return 0

            valve = self.valves[position]

            released_pressures = []

            total_flow_rate = self.total_flow_rate(open_valves)

            # Open the valve
            if valve.flow_rate != 0 and valve.name not in open_valves:
                new_open_valves = set(open_valves)
                new_open_valves.add(position)
                new_open_valves = frozenset(new_open_valves)

                released_pressures.append(total_flow_rate + step(position, time_left-1, new_open_valves))

            # Move
            for neighbour in valve.neighbours:
                released_pressures.append(total_flow_rate + step(neighbour, time_left-1, open_valves))

            return max(released_pressures)
        
        return step("AA", 30, frozenset())



class Valve:
    def __init__(self, name: str, flow_rate: int, neighbours: [str]):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbours = neighbours
    
    def __repr__(self):
        return f"{self.name}: {self.flow_rate}, {self.neighbours}"

class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> dict:
        pattern = re.compile(r"^Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (.*)$")
        ret = {}
        for line in map(lambda line: line.strip(), iterable):
            valve, flow_rate, neighbours = pattern.match(line).groups()
            ret[valve] = Valve(valve, int(flow_rate), neighbours.split(", "))
        return Volcano(ret)

    def part_one(self, volcano: Volcano) -> str:
        ans = volcano.most_pressure()
        print(f"Ans: {ans}")
        return str(ans)


    def part_two(self, data: dict) -> str:
        ans = None
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)