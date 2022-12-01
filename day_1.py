if __name__ == '__main__':
    elves = []

    # load data
    with open('day_1_input.txt') as f:
        elf = []
        for line in map(lambda line: line.strip(), f):
            if line == '':
                elves.append(elf)
                elf = []
            else:
                elf.append(int(line))
    
    # Part 1
    elf_no, max_calories = None, 0
    for i, elf in enumerate(elves):
        calories = sum(elf)
        if calories > max_calories:
            elf_no = i
            max_calories = calories
    
    print(f"Elf {elf_no} has the most calories at {max_calories}cal.")