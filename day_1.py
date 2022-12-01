class Solution:
    def __init__(self):
        self.elves = []

    def load_data(self):
        with open('day_1_input.txt') as f:
            calories = 0
            for line in map(lambda line: line.strip(), f):
                if line == '':
                    self.elves.append(calories)
                    calories = 0
                else:
                    calories += int(line)

        self.elves.sort()

    def part_one(self):    
        print(f"The most calories carried by an elf is {self.elves[-1]}cal.")

    def part_two(self):
        print(f"Total calories of top three elves is {sum(self.elves[-3:])}cal.")