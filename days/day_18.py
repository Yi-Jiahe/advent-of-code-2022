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


    def part_two(self, data: set) -> str:
        min_x, max_x = float("inf"), -float("inf")
        min_y, max_y = float("inf"), -float("inf")
        min_z, max_z = float("inf"), -float("inf")

        for x, y, z in data:
            min_x = min(x, min_x)
            max_x = max(x, max_x)
            min_y = min(y, min_y)
            max_y = max(y, max_y)
            min_z = min(z, min_z)
            max_z = max(z, max_z)
        
        print(min_x, max_x)
        print(min_y, max_y)
        print(min_z, max_z)

        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)