import re
import functools

class Board:
    def __init__(self):
        self.start = None
        self.spaces = set()
        self.rocks = set()
        self.instructions = []
        self.max_size = [0, 0]

    def update_max_size(self, position: tuple):
        self.max_size[0] = max(self.max_size[0], position[1])
        self.max_size[1] = max(self.max_size[1], position[0])

    def add_space(self, position: tuple):
        self.spaces.add(position)
        self.update_max_size(position)

    def add_rock(self, position: tuple):
        self.rocks.add(position)
        self.update_max_size(position)

    @functools.cache
    def rollover_boundary(self, i, direction):
        """Gives the position of the first empty space when rolling over to the other side, if any.
        i is the row or column to be tested.
        direction is the direction in which to test."""

        if direction == 0:
            x = 1
            while x <= self.max_size[1]:
                position = (x, i)
                if position in self.spaces:
                    return position
                if position in self.rocks:
                    return
                x += 1            
            return
        
        if direction == 1:
            y = 1
            while y <= self.max_size[0]:
                position = (i, y)
                if position in self.spaces:
                    return position
                if position in self.rocks:
                    return
                y += 1            
            return
        
        if direction == 2:
            x = self.max_size[1]
            while x >= 1:
                position = (x, i)
                if position in self.spaces:
                    return position
                if position in self.rocks:
                    return
                x -= 1
            return
        
        if direction == 3:
            y = self.max_size[0]
            while y >= 1:
                position = (i, y)
                if position in self.spaces:
                    return position
                if position in self.rocks:
                    return
                y -= 1
            return

class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> Board:
        board = Board()
        section = "map"
        row = 1
        for line in map(lambda line: line.rstrip(), iterable):
            if section == "map":
                if line == '':
                    section = "instructions"
                    continue
                for i, char in enumerate(line):
                    if char == ' ':
                        continue
                    position = (i+1, row)
                    if char == '.':
                        # First . in the first row will be the start position
                        if not board.start:
                            board.start = position
                        board.add_space(position)
                    elif char == '#':
                        board.add_rock(position)
                row += 1
                continue
            
            pattern = re.compile(r"^(\d+)?([RL])?(.*)$")
            instructions = line
            while instructions:
                steps, turn, instructions = pattern.match(instructions).groups()
                board.instructions.append(int(steps))
                if turn:
                    board.instructions.append(turn)
        return board

    def part_one(self, board: Board()) -> str:
        position = board.start
        direction = 0
        instructions = board.instructions.copy()
        while instructions:
            instruction = instructions.pop(0)
            if isinstance(instruction, int):
                for _ in range(instruction):
                    new_position = list(position)
                    if direction == 0:
                        new_position[0] += 1
                    elif direction == 1:
                        new_position[1] += 1
                    elif direction == 2:
                        new_position[0] -= 1
                    elif direction == 3:
                        new_position[1] -= 1
                    new_position = tuple(new_position)

                    # Can move
                    if new_position in board.spaces:
                        position = new_position
                        continue
                    
                    # Rock in way
                    if new_position in board.rocks:
                        break
                    
                    # Time for rollover
                    new_position = board.rollover_boundary(position[0] if direction in (1, 3) else position[1], direction)
                    
                    if new_position:
                        position = new_position
                        continue        
                    break
                continue

            if instruction == 'R':
                direction += 1
            elif instruction == 'L':
                direction -= 1
            direction %= 4

        ans = 1000 * position[1] + 4 * position[0] + direction
        print(f"Ans: {ans}")
        return str(ans)


    def part_two(self, data: dict) -> str:
        ans = None
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)