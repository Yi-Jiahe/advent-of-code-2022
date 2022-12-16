import re


class Node:
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
            ret[valve] = Node(valve, int(flow_rate), neighbours.split(", "))
        return ret

    def part_one(self, data: dict) -> str:
        ans = None
        print(data)
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)


    def part_two(self, data: dict) -> str:
        ans = None
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)