class Solution:
    def __init__(self):
        self.elves = []

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> []:
        elves = []
        calories = 0
        for line in map(lambda line: line.strip(), iterable):
            if line == '':
                elves.append(calories)
                calories = 0
            else:
                calories += int(line)
        elves.append(calories)

        elves.sort()
        return elves

    def part_one(self, elves: [int]) -> str:    
        ans = elves[-1]
        print(f"The most calories carried by an elf is {ans}cal.")
        return ans


    def part_two(self, elves: [int]) -> str:
        ans = sum(elves[-3:])
        print(f"Total calories of top three elves is {ans}cal.")
        return ans