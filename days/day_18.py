import math


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
        bounds = [[float("inf"), -float("inf")] for _ in range(3)]

        for cube in data:
            for axis in range(3):
                bounds[axis][0] = min(bounds[axis][0], cube[axis])
                bounds[axis][1] = max(bounds[axis][1], cube[axis])

        ans = 0
        outside = set()
        stack = [tuple(bounds[axis][0]-1 for axis in range(3))]
        while stack:
            pos = stack.pop()
            outside.add(pos)
            for axis in range(3):
                for direction in [-1, 1]:
                    adjecent_cube = list(pos)
                    adjecent_cube[axis] += direction
                    adjecent_cube = tuple(adjecent_cube)
                    # Airspace is next to a lava cube
                    # Add the direction we are checking to the number of external sides
                    if adjecent_cube in data:
                        ans += 1
                        continue
                    # Already searched or searching
                    if adjecent_cube in outside or adjecent_cube in stack:
                        continue
                    # Outside the search area
                    if adjecent_cube[axis] < bounds[axis][0] - 1 or bounds[axis][1] + 1 < adjecent_cube[axis]:
                        continue
                    stack.append(adjecent_cube)
        print(f"Ans: {ans}")
        return str(ans)