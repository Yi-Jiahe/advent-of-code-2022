class Piece:
    def spawn(self, height):
        for rock in self.rocks:
            rock[0] += 2
            rock[1] += height + 3

    
class HorizontalLine(Piece):
    def __init__(self, height):
        self.rocks = [[0, 0], [1, 0], [2, 0], [3, 0]]
        super().spawn(height)

class Cross(Piece):
    def __init__(self, height):
        self.rocks = [[1, 0], [0, 1], [1, 1], [2, 1], [1, 2]]
        super().spawn(height)


class L(Piece):
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
        ans = None
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)


    def part_two(self, data: []) -> str:
        ans = None
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)