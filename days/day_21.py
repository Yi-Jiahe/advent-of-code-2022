import re


class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> dict:
        pattern = re.compile(r"^(\w+): (.*)$")
        
        ret = {}
        for line in map(lambda line: line.strip(), iterable):
            name, value = pattern.match(line).groups()
            try:
                ret[name] = int(value)
            except ValueError:
                ret[name] = value.split(' ')
        return ret

    def part_one(self, data: []) -> str:
        def solve(name):
            value = data[name]
            if isinstance(value, int):
                return value
            else:
                a = solve(value[0])
                b = solve(value[2])
                operation = value[1]
                if operation == '+':
                    return a + b
                elif operation == '-':
                    return a - b
                elif operation == '*':
                    return a * b
                elif operation == '/':
                    return a / b
        ans = int(solve("root"))
        print(f"Ans: {ans}")
        return str(ans)


    def part_two(self, data: []) -> str:
        ans = None
        occurances = {}
        for name, value in data.items():
            if isinstance(value, int):
                continue
            for monkey in (value[0], value[2]):
                if monkey not in occurances:
                    occurances[monkey] = 0
                occurances[monkey] += 1
        for x in occurances.values():
            if x >= 2:
                raise ValueError("Monkey is reused")
        print(f"Ans: {ans}")
        return str(ans)