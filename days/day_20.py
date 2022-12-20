class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> [int]:
        ret = []
        for line in map(lambda line: line.strip(), iterable):
            ret.append(int(line))
        return ret

    def part_one(self, data: [int]) -> str:
        n = len(data)
        numbered_data = [(i, entry) for i, entry in enumerate(data)]
        for i, entry in enumerate(data):
            old_index = numbered_data.index((i, entry))
            numbered_data.pop(old_index)
            new_index = (old_index + entry) % (n-1)
            if new_index == 0:
                new_index = n-1
            elif new_index == n-1:
                new_index = 0
            numbered_data.insert(new_index, entry)

        zero_index = numbered_data.index(0)
        a = numbered_data[(zero_index + 1000) % n]
        b = numbered_data[(zero_index + 2000) % n]
        c = numbered_data[(zero_index + 3000) % n]
        ans = a + b + c

        print(f"Ans: {ans}")
        return str(ans)

    def part_two(self, data: [int]) -> str:
        ans = None
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)