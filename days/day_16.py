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
            if time_left <= 0:
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
            for neighbour, weight in valve.neighbours.items():
                if weight <= time_left:
                    released_pressures.append(total_flow_rate * weight + step(neighbour, time_left-weight, open_valves))
                else:
                    released_pressures.append(total_flow_rate * time_left + step(neighbour, 0, open_valves))
            return max(released_pressures)
        
        return step("AA", 30, frozenset())
    
    def most_with_elephant(self):
        @functools.cache
        def step(positions: tuple, time_left: int, open_valves: frozenset):
            if time_left == 0:
                return 0

            valve_me = self.valves[positions[0]]
            valve_elephant = self.valves[positions[1]]

            released_pressures = []

            total_flow_rate = self.total_flow_rate(open_valves)

            actions_me = valve_me.neighbours
            if valve_me.flow_rate != 0 and valve_me.name not in open_valves:
                actions_me.append(valve_me.name)
            actions_elephant = valve_elephant.neighbours
            if valve_elephant.flow_rate != 0 and valve_elephant.name not in open_valves:
                actions_elephant.append(valve_elephant.name)
            
            for action_me in actions_me:
                for action_elephant in actions_elephant:
                        if action_me == valve_me.name and action_elephant == valve_elephant and action_me == action_elephant:
                            break
                        new_open_valves = set(open_valves)
                        if action_me == valve_me.name:
                            new_open_valves.add(valve_me.name)
                        if action_elephant == valve_elephant.name:
                            new_open_valves.add(valve_elephant.name)
                        new_open_valves = frozenset(new_open_valves)
                        released_pressures.append(total_flow_rate + step(tuple(sorted([action_me, action_elephant])), time_left-1, new_open_valves))
            return max(released_pressures)
        
        return step(tuple(["AA", "AA"]), 26, frozenset())



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
            ret[valve] = Valve(valve, int(flow_rate), {neighbour: 1 for neighbour in neighbours.split(", ")})

        # Assumption is that AA (start) has more than 2 neighbours
        for valve in ret.values():
            if len(valve.neighbours) == 2 and valve.flow_rate == 0:
                neighbours = [neighbour for neighbour in valve.neighbours.keys()]
                new_length = ret[neighbours[0]].neighbours[valve.name] + ret[neighbours[1]].neighbours[valve.name]
                ret[neighbours[0]].neighbours[neighbours[1]] = new_length
                ret[neighbours[1]].neighbours[neighbours[0]] = new_length
                del ret[neighbours[0]].neighbours[valve.name]
                del ret[neighbours[1]].neighbours[valve.name]

        valves = {name: valve for name, valve in ret.items() if not (len(valve.neighbours) == 2 and valve.flow_rate == 0)}

        return Volcano(valves)

    def part_one(self, volcano: Volcano) -> str:
        ans = volcano.most_pressure()
        print(f"Ans: {ans}")
        return str(ans)


    def part_two(self, volcano: Volcano) -> str:
        ans = volcano.most_with_elephant()
        print(f"Ans: {ans}")
        return str(ans)