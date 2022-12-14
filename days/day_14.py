class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> set:
        ret = set()
        for line in map(lambda line: line.strip(), iterable):
            path = [tuple([int(x) for x in cood.split(',')]) for cood in line.split(" -> ")]
            start = path.pop(0)
            while path:
                end = path.pop(0)
                # Up
                if end[1] < start[1]:
                    for y in range(start[1], end[1], -1):
                        ret.add((start[0], y))
                # Down
                if end[1] > start[1]:
                    for y in range(start[1], end[1]):
                        ret.add((start[0], y))
                # Left
                if end[0] < start[0]:
                    for x in range(start[0], end[0], -1):
                        ret.add((x, start[1]))
                # Right
                if end[0] > start[0]:
                    for x in range(start[0], end[0]):
                        ret.add((x, start[1]))
                start = end
            ret.add(start)
        return ret

    def part_one(self, data: set) -> str:
        ans = None
        print(data)
        self.print_map(data)
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)


    def part_two(self, data: []) -> str:
        ans = None
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)

    def print_map(self, stones: set):
        min_x = float("inf")
        max_x = 0
        max_y = 0
        for x, y in stones:
            min_x = min(x, min_x)
            max_x = max(x, max_x)
            max_y = max(y, max_y)
        m = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y + 1)]
        for x, y in stones:
            m[y][x-min_x] = '#'
        m[0][500-min_x] = '+'
        for row in m:
            print(''.join(row))