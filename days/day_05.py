import re
import copy


class Solution:
    def __init__(self):
        self.stacks = [
            ['S', 'T', 'H', 'F', 'W', 'R'],
            ['S', 'G', 'D', 'Q', 'W'],
            ['B', 'T', 'W'],
            ['D', 'R', 'W', 'T', 'N', 'Q', 'Z', 'J'],
            ['F', 'B', 'H', 'G', 'L', 'V', 'T', 'Z'],
            ['L', 'P', 'T', 'C', 'V', 'B', 'S', 'G'],
            ['Z', 'B', 'R', 'T', 'W', 'G', 'P'],
            ['N', 'G', 'M', 'T', 'C', 'J', 'R'],
            ['L', 'G', 'B', 'W']
        ]

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> []:
        ret = []

        prog = re.compile(r"^move (\d+) from (\d+) to (\d+)$")
        for line in map(lambda line: line.strip(), iterable):
            result = prog.match(line)
            if not result:
                raise ValueError("Line does not match expected format")
            ret.append(tuple(map(int, result.groups())))
        return ret

    def part_one(self, data: []) -> str:
        stacks = copy.deepcopy(self.stacks)
        for number, from_stack, to_stack in data:
            for _ in range(number):
                stacks[to_stack-1].append(stacks[from_stack-1].pop())
        ans = self.top_crates(stacks)
        print(f"The top of each stack spells: {ans}")
        return ans


    def part_two(self, data: []) -> str:
        stacks = copy.deepcopy(self.stacks)
        for number, from_stack, to_stack in data:
            # print(f"move {number} from {stacks[from_stack-1]} to {stacks[to_stack-1]}")
            moving = stacks[from_stack-1][-number:]
            stacks[from_stack-1] = stacks[from_stack-1][:-number]
            stacks[to_stack-1] = stacks[to_stack-1] + moving
            # print(f"Result: from: {stacks[from_stack-1]}, to: {stacks[to_stack-1]}")
        ans = self.top_crates(stacks)
        print(f"The top of each stack spells: {ans}")
        return ans

    def top_crates(self, stacks):
        ret = ""
        for stack in stacks:
            ret += stack[-1]
        return ret