class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> []:
        ret = []
        for line in map(lambda line: line.strip(), iterable):
            ret.append(list(map(lambda assignment: list(map(int, assignment.split('-'))), line.split(','))))
        return ret

    def part_one(self, data: []) -> str:
        full_overlaps = 0
        for first, second in data:
          if self.fully_contains(first, second):
            full_overlaps += 1
        print(f"{full_overlaps} pairs have one range fully containing the other")

        return full_overlaps


    def part_two(self, data: []) -> str:
        ans = None
        raise NotImplementedError
        return ans

    def fully_contains(self, first: [int], second: [int]) -> bool:
        if first[0] == second[0]:
            # One definately contains the other
            return True
        elif first[0] < second[0]:
            # First might contain the second
            if first[1] >= second[1]:
                return True
        elif first[0] > second[0]:
            # Second might contain the first
            if first[1] <= second[1]:
                return True
        return False