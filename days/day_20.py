class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> []:
        ret = []
        for line in map(lambda line: line.strip(), iterable):
            ret.append(int(line))
        return ret

    def part_one(self, data: []) -> str:
        ans = None

        numbered_data = [(i, entry) for i, entry in enumerate(data)]

        for i, entry in enumerate(data):
            print(numbered_data.index((i, entry)))

        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)

    def part_two(self, data: []) -> str:
        ans = None
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)