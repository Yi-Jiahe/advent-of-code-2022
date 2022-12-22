import re


class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> dict:
        ret = {
            'map': {
                'spaces': set(),
                'rocks': set()
            },
            'instructions': []
        }
        section = "map"
        row = 1
        for line in map(lambda line: line.strip(), iterable):
            if section == "map":
                if line == '':
                    section = "instructions"
                    continue

                for i, char in enumerate(line):
                    if char == ' ':
                        continue
                    position = (row, i+1)
                    if char == '.':
                        ret['map']['spaces'].add(position)
                    elif char == '#':
                        ret['map']['rocks'].add(position)
                row += 1    
                continue
            
            pattern = re.compile(r"^(\d+)?([RDLU])?(.*)$")
            instructions = line
            while instructions:
                steps, turn, instructions = pattern.match(instructions).groups()
                ret['instructions'].append(int(steps))
                if turn:
                    ret['instructions'].append(turn)
        return ret

    def part_one(self, data: dict) -> str:
        ans = None
        print(data['instructions'])
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)


    def part_two(self, data: dict) -> str:
        ans = None
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)