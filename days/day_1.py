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
        elves.sort()
        return elves

    def part_one(self, elves: [int]):    
        print(f"The most calories carried by an elf is {elves[-1]}cal.")

    def part_two(self, elves: [int]):
        print(f"Total calories of top three elves is {sum(elves[-3:])}cal.")