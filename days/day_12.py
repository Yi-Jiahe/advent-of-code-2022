class Heightmap:
    def __init__(self):
        self.heightmap = []
        self.start = None
        self.end = None
        self.dimensions = None


class Dijkstra:
    def __init__(self, heightmap: Heightmap()):
        self.heightmap = heightmap
        self.costs = [[float('inf') for _ in range(self.heightmap.dimensions[1])] for _ in range(self.heightmap.dimensions[0])]
        self.costs[self.heightmap.start[0]][self.heightmap.start[1]] = 0

    def search(self):
        def valid(i, j):
            if i < 0 or i >= self.heightmap.dimensions[0]:
                return False
            if j < 0 or j >= self.heightmap.dimensions[1]:
                return False
            return True

        open_set = {self.heightmap.start}
        while open_set:
            i, j = open_set.pop()
            neighbours = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for i_new, j_new in neighbours:
                if not valid(i_new, j_new):
                    continue
                if self.heightmap.heightmap[i_new][j_new] - self.heightmap.heightmap[i][j] > 1:
                    continue
                if self.costs[i_new][j_new] - self.costs[i][j] >= 2:
                    self.costs[i_new][j_new] = self.costs[i][j] + 1
                    open_set.add((i_new, j_new))
        return self.costs[self.heightmap.end[0]][self.heightmap.end[1]]


class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> Heightmap:
        heightmap = Heightmap()
        for i, line in enumerate(map(lambda line: line.strip(), iterable)):
            heightmap.heightmap.append([])
            for j, char in enumerate(line):
                if char == 'S':
                    heightmap.start = (i, j)
                    char = 'a'
                elif char == 'E':
                    heightmap.end = (i, j)
                    char = 'z'
                heightmap.heightmap[i].append(ord(char)-97)
        heightmap.dimensions = (len(heightmap.heightmap), len(heightmap.heightmap[0]))
        return heightmap

    def part_one(self, heightmap: Heightmap) -> str:    
        search = Dijkstra(heightmap)
        ans = search.search()
        print(f"The fewest steps requred is {ans}")
        return str(ans)


    def part_two(self, heightmap: Heightmap) -> str:
        least_steps = float('inf')
        for i, row in enumerate(heightmap.heightmap):
            for j, point in enumerate(row):
                if point == 0:
                    heightmap.start = (i, j)
                    search = Dijkstra(heightmap)
                    steps = search.search()
                    if steps < least_steps:
                        least_steps = steps
        print(f"The fewest steps requred is {least_steps}")
        return str(least_steps)