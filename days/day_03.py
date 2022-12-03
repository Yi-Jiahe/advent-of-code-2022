class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> []:
        '''
        Takes in a list of rucksacks given as characters all on a single line.
        A given rucksack always has the same number of items in each of its two compartments,
        so the first half of the characters represent items in the first compartment, 
        while the second half of the characters represent items in the second compartment.

        Returns a list of rucksacks split into two compartments.
        '''
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
        priority_sum = 0
        i = 1
        rucksacks = []
        for rucksack in data:
            rucksacks.append(set(rucksack[0] + rucksack[1]))
            if i == 3:
                # Find badge
                intersection = set.intersection(*rucksacks)
                if len(intersection) != 1:
                    raise RuntimeError("Unable to identify badge")
                priority_sum += self.priority(intersection.pop())
                # Reset group
                i = 1
                rucksacks = []
            else:
                i += 1

        print(f"The sum of priorities of badges is {priority_sum}")
        return priority_sum

    def priority(self, item: str) -> int:
        ascii_repr = ord(item)
        if 97 <= ascii_repr <= 122:
            return ascii_repr - 96
        elif 65 <= ascii_repr <= 90:
            return ascii_repr - 64 + 26
        raise ValueError("Character not an alphabet")