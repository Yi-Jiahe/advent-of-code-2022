class Piece:
    def __init__(self):
        self.rocks = None
        self.max_x = None

class HorizontalLine(Piece):
    def __init__(self, height):
        pass

class Game:
    # Left of piece is x=0, bottom of piece is y=0
    self.pieces = [
        # Hoizontal Line
        [[0, 0], [1, 0], [2, 0], [3, 0]],
        # Cross
        [[1, 0], [0, 1], [1, 1], [2, 1], [1, 2]],
        # L
        [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2]],
        # Vertical Line
        [[0, 0], [0, 1], [0, 2], [0, 3]],
        # Square
        [[0, 0], [0, 1], [1, 0], [1, 1]]
    ]

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
        ans = None
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)


    def part_two(self, data: []) -> str:
        ans = None
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)