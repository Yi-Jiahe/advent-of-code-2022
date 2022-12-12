class Heightmap:
    def __init__(self):
        self.heightmap = []
        self.start = None
        self.end = None

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
        return heightmap

    def part_one(self, heightmap: Heightmap) -> str:    
        print(heightmap.heightmap)
        print(heightmap.start)
        print(heightmap.end)
        ans = None
        raise NotImplementedError
        return ans


    def part_two(self, heightmap: Heightmap) -> str:
        ans = None
        raise NotImplementedError
        return ans