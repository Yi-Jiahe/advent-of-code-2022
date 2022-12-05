import re

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
        for number, from_stack, to_stack in data:
            for _ in range(number):
                self.stacks[to_stack-1].append(self.stacks[from_stack-1].pop())
        ans = ""
        for stack in self.stacks:
            ans += stack[-1]
        print(f"The top of each stack spells: {ans}")
        return ans


    def part_two(self, data: []) -> str:
        ans = None
        raise NotImplementedError
        return ans