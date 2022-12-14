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
    
    def print_filled_map(self, grains: set):
        min_x = float("inf")
        max_x = 0
        max_y = 0
        for x, y in (self.rocks | grains):
            min_x = min(x, min_x)
            max_x = max(x, max_x)
            max_y = max(y, max_y)
        ret = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y + 1)]
        ret[0][500-min_x] = '+'
        for x, y in self.rocks:
            ret[y][x-min_x] = '#'
        for x, y in grains:
            ret[y][x-min_x] = 'o'
        for row in ret:
            print(''.join(row))
        return ret
        


    def fill(self, void=True):
        settled_grains = set()
        grains = 0
        path = [(500, 0)]
        while True:
            if (500, 0) in settled_grains:
                self.print_filled_map(settled_grains)
                return grains
            grains += 1
            grain = path[-1]
            while True:
                if grain[1] == self.max_y + 1:
                    settled_grains.add((x, new_y))
                    path.pop()
                    break
                new_y = grain[1] + 1
                if void and new_y > self.max_y:
                    return grains - 1
                settled = True
                # Test centre, left, right
                for x in [grain[0], grain[0]-1, grain[0]+1]:
                    # No rocks beyond the min and max x so if there is no infinite floor, its over once it goes beyond the edge
                    if void and (x < self.min_x or x > self.max_x):
                        return grains - 1
                    # Check if there is a new space for the grain to fall
                    if (x, new_y) not in (self.rocks | settled_grains):
                        grain = [x, new_y]
                        settled = False
                        path.append((grain[0], grain[1]))
                        break
                # If the grain made it here it means that there is nowhere further to fall and the current position is where it will rest
                if settled:
                    settled_grains.add((grain[0], grain[1]))
                    path.pop()
                    break
        

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


    def part_two(self, rockMap: RockMap) -> str:
        ans = rockMap.fill(void=False)
        print(f"Ans: {ans}")
        return str(ans)