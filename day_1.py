class Solution:
    def __init__(self):
        self.elves = []

    def load_data(self):
        with open('day_1_input.txt') as f:
            elf = []
            for line in map(lambda line: line.strip(), f):
                if line == '':
                    self.elves.append(elf)
                    elf = []
                else:
                    elf.append(int(line))

    def part_one(self):
        # Part 1
        elf_no, max_calories = None, 0
        for i, elf in enumerate(self.elves):
            calories = sum(elf)
            if calories > max_calories:
                elf_no = i
                max_calories = calories
        
        print(f"Elf {elf_no} has the most calories at {max_calories}cal.")

    def part_two(self):
        calories = sorted(map(sum, self.elves))
        print(f"Total calories of top three elves is {sum(calories[-3:])}cal.")