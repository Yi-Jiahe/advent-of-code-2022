class Piece:
    def spawn(self, height):
        for rock in self.rocks:
            rock[0] += 2
            rock[1] += height + 3

    def move(self, direction):
        new_rocks = self.rocks.copy()
        for rock in self.rocks:
            rock[0] += direction[0]
            rock[1] += direction[1]

class HorizontalLine(Piece):
    def __init__(self, height):
        self.rocks = [[0, 0], [1, 0], [2, 0], [3, 0]]
        super().spawn(height)

class Cross(Piece):
    def __init__(self, height):
        self.rocks = [[1, 0], [0, 1], [1, 1], [2, 1], [1, 2]]
        super().spawn(height)


class MirroredL(Piece):
    def __init__(self, height):
        self.rocks = [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2]]
        super().spawn(height)

class VerticalLine(Piece):
    def __init__(self, height):
        self.rocks = [[0, 0], [0, 1], [0, 2], [0, 3]]
        super().spawn(height)

class Square(Piece):
    def __init__(self, height):
        self.rocks = [[0, 0], [0, 1], [1, 0], [1, 1]]
        super().spawn(height)

class Game:
    def __init__(self):
        self.max_height = 0
        self.turn = 0
        self.tower = set()

    def check_collision_piece(self, piece: Piece):
        for rock in piece.rocks:
            if rock[0] < 0 or 7 <= rock[0]:
                return True
            if tuple(rock) in self.tower:
                pass


class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> []:
        ret = []
        for line in map(lambda line: line.strip(), iterable):
            pass
        return ret

    def part_one(self, data: []) -> str:
        def generate_new_position(rock, direction):
            new_position = rock.copy()
            for block in rock:
                for axis in range(2):
                    block[axis] += direction[axis]
            return block

        rocks = [
            [[0, 0], [1, 0], [2, 0], [3, 0]],
            [[1, 0], [0, 1], [1, 1], [2, 1], [1, 2]],
            [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2]],
            [[0, 0], [0, 1], [0, 2], [0, 3]],
            [[0, 0], [0, 1], [1, 0], [1, 1]]
        ]

        tower = set()
        top = 0
        rock = None

        def check_collision(rock):
            for block in rock:
                if block[0] < 0 or 7 <= block[0]:
                    return True
            if tuple(block) in tower:
                return True
            if block[1] < 0:
                return True
            return False

        i = 0
        j = 0
        n_moves = len(data)
        while i < 2022:
            rock = rocks[i%len(rocks)].copy()
            for block in rock:
                block[0] += 2
                block[1] += top + 3
            while True:
                j %= n_moves
                direction = data[j]
                if direction == '<':
                    new_position = generate_new_position(rock, (-1, 0))
                elif direction == '>':
                    new_position = generate_new_position(rock, (1, 0))
                
                    
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)


    def part_two(self, data: []) -> str:
        ans = None
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)