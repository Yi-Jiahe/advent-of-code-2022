class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> []:
        ret = []
        for line in map(lambda line: line.strip(), iterable):
            half = len(line) // 2
            ret.append([line[:half], line[half:]])      
        return ret

    def part_one(self, data: []) -> str:    
        priority_sum = 0
        for rucksack in data:
            duplicates = set(rucksack[0]) & set(rucksack[1])
            for item in duplicates:
                priority_sum += self.priority(item)
        print(f"The sum of priorities of duplicate items is {priority_sum}")
        return priority_sum


    def part_two(self, data: []) -> str:
        ans = None
        raise NotImplementedError
        return ans

    def priority(self, item: str) -> int:
        ascii_repr = ord(item)
        if 97 <= ascii_repr <= 122:
            return ascii_repr - 96
        elif 65 <= ascii_repr <= 90:
            return ascii_repr - 64 + 26
        raise ValueError("Character not an alphabet")