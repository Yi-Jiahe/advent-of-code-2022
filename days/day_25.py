class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> []:
        ret = []
        for line in map(lambda line: line.strip(), iterable):
            ret.append(line)
        return ret

    def part_one(self, data: []) -> str:
        ans = 0
        for s in data:
            ans += self.SNAFU_to_decimal(s)
        print(f"Ans: {ans}")
        return str(ans)


    def part_two(self, data: []) -> str:
        ans = None
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)

    def SNAFU_to_decimal(self, s: str):
        ret = 0
        for i, c in enumerate(s[::-1]):
            p = 5 ** i
            if c == '=':
                ret -= 2 * p
                continue
            if c == '-':
                ret -= p
                continue
            if c == '0':
                continue
            if c in ['1', '2']:
                ret += int(c) * p
                continue
            raise ValueError(f"Character not recognized: {c}")
        return ret