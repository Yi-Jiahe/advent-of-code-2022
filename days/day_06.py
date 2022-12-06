class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> str:
        for line in map(lambda line: line.strip(), iterable):
            return line

    def part_one(self, data: str) -> str:  
        ans = self.find_marker(data)
        print(f"{ans} chacarcters need to be processed before the first start-of-packet marker")
        return ans


    def part_two(self, data: []) -> str:
        ans = None
        raise NotImplementedError
        return ans

    def find_marker(self, buffer):
        last_four_characters = []
        for i, char in enumerate(buffer):
            last_four_characters.append(buffer[i])
            if i < 4:
                continue
            last_four_characters.pop(0)
            if len(set(last_four_characters)) == 4:
                return i + 1