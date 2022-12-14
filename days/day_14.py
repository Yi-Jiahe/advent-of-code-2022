class RockMap:
    def __init__(self, rocks: set):
        self.rocks = rocks
        self.min_x = float("inf")
        self.max_x = 0
        self.max_y = 0
        for x, y in self.rocks:
            self.min_x = min(x, self.min_x)
            self.max_x = max(x, self.max_x)
            self.max_y = max(y, self.max_y)
    

    def generate_map(self) -> [[str]]:
        ret = [['.' for _ in range(self.max_x - self.min_x + 1)] for _ in range(self.max_y + 1)]
        for x, y in self.rocks:
            ret[y][x-self.min_x] = '#'
        ret[0][500-self.min_x] = '+'
        return ret

    def print(self):
        for row in self.generate_map():
            print(''.join(row))
    
    def fill(self):
        fill_map = self.generate_map()

        grains = 0
        while True:
            grains += 1
            grain = [500, 0]
            while True:
                new_y = grain[1] + 1
                if new_y > self.max_y:
                    # for row in fill_map:
                    #     print(''.join(row))
                    return grains - 1
                settled = False
                for x in [grain[0], grain[0]-1, grain[0]+1]:
                    if x < self.min_x or x > self.max_x:
                        return grains - 1
                    if fill_map[new_y][x-self.min_x] == '.':
                        grain = [x, new_y]
                        settled = True
                        break
                if not settled:
                    fill_map[grain[1]][grain[0]-self.min_x] = 'o'
                    break
            # print(grains)
            # for row in fill_map:
            #     print(''.join(row))


                



class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> RockMap:
        rocks = set()
        for line in map(lambda line: line.strip(), iterable):
            path = [tuple([int(x) for x in cood.split(',')]) for cood in line.split(" -> ")]
            start = path.pop(0)
            while path:
                end = path.pop(0)
                # Up
                if end[1] < start[1]:
                    for y in range(start[1], end[1]-1, -1):
                        rocks.add((start[0], y))
                # Down
                if end[1] > start[1]:
                    for y in range(start[1], end[1]+1):
                        rocks.add((start[0], y))
                # Left
                if end[0] < start[0]:
                    for x in range(start[0], end[0]-1, -1):
                        rocks.add((x, start[1]))
                # Right
                if end[0] > start[0]:
                    for x in range(start[0], end[0]+1):
                        rocks.add((x, start[1]))
                start = end
        rocks.add(start)
        rockMap = RockMap(rocks)
        return rockMap

    def part_one(self, rockMap: RockMap) -> str:
        ans = rockMap.fill()
        print(f"Ans: {ans}")
        return str(ans)


    def part_two(self, data: RockMap) -> str:
        ans = None
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)