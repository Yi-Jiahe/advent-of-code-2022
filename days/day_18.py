class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> set:
        ret = set()
        for line in map(lambda line: line.strip(), iterable):
            ret.add(tuple(int(x) for x in line.split(",")))
        return ret

    def part_one(self, data: set) -> str:
        ans = 0
        for cube in data:
            for axis in range(3):
                for direction in [-1, 1]:
                    adjecent_cube = list(cube)
                    adjecent_cube[axis] += direction
                    if tuple(adjecent_cube) not in data:
                        ans += 1
        print(f"Ans: {ans}")
        return str(ans)


    def part_two(self, data: []) -> str:
        ans = None
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)