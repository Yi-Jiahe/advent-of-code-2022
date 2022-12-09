class Rope:
    def __init__(self, n_knots: int):
        self.n_knots = n_knots
        self.knots = [[0, 0] for _ in range(self.n_knots)]
    
    def move(self, direction: str, steps: int):
        for _ in range(steps):
            self.__move_head(direction)
            for i in range(1, self.n_knots):
                self.__move_knot(i)
            yield

    def __move_head(self, direction: str):
        if direction == 'U':
            self.knots[0][1] += 1
        elif direction == 'D':
            self.knots[0][1] -= 1
        elif direction == 'L':
            self.knots[0][0] -= 1
        elif direction == 'R':
            self.knots[0][0] += 1
        else:
            raise ValueError("Invalid direction")

    def __move_knot(self, i: int):
        if self.touching(i-1, i):
            return

        error = [c_i_minus_1 - c_i for c_i_minus_1, c_i in zip(self.knots[i-1], self.knots[i])]

        # If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:
        if 0 in error:
            for axis in range(2):
                abs_error = abs(error[axis])
                if abs_error == 0:
                    continue
                if abs_error == 1:
                    return
                elif abs_error == 2:
                    self.knots[i][axis] += error[axis]//abs_error
                    return
                raise ValueError("Error too large")

        # Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:
        for axis in range(2):
            abs_error = abs(error[axis])
            self.knots[i][axis] += error[axis]//abs_error

    def touching(self, i, j) -> bool:
        for c_i, c_j in zip(self.knots[i], self.knots[j]):
            if abs(c_i - c_j) >= 2:
                return False
        return True




class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> [(str, int)]:
        ret = []
        for line in map(lambda line: line.strip(), iterable):
            direction, steps = line.split()
            ret.append((direction, int(steps)))
        return ret

    def part_one(self, data: [(str, int)]) -> str:
        rope = Rope(2)

        visited_positions = set()
        for direction, steps in data:
            for _ in rope.move(direction, steps):
                visited_positions.add(tuple(rope.knots[-1]))

        ans = len(visited_positions)
        print(f"The tail visits {ans} positions at least once.")

        return str(ans)


    def part_two(self, data: [(str, int)]) -> str:
        rope = Rope(10)

        visited_positions = set()
        for direction, steps in data:
            for _ in rope.move(direction, steps):
                visited_positions.add(tuple(rope.knots[-1]))

        ans = len(visited_positions)
        print(f"The tail visits {ans} positions at least once.")

        return str(ans)
