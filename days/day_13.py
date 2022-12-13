class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> []:
        ret = []
        for line in map(lambda line: line.strip(), iterable):
            pass
        return ret

    def part_one(self, data: []) -> str:    
        ans = None
        raise NotImplementedError
        return ans


    def part_two(self, data: []) -> str:
        ans = None
        raise NotImplementedError
        return ans

    def compare(self, left, right) -> int:
        """
        returns 1 if left comes first, -1 if right comes first and 0 if they are equal.
        """
        if isinstance(left, int) and isinstance(right, int):
            if left == right:
                return 0
            return 1 if left < right else -1
        # Convert non-list to list
        if isinstance(left, int):
            left = [left]
        if isinstance(right, int):
            right = [right]
        left = iter(left)
        right = iter(right)
        while True:
            exhausted = [None, None]
            try:
                a = next(left)
            except StopIteration:
                exhausted[0] = True
            try:
                b = next(right)
            except StopIteration:
                exhausted[1] = True
            if exhausted[0] and exhausted[1]:
                return 0
            if exhausted[0]:
                return 1
            if exhausted[1]:
                return -1
            result = self.compare(a, b)
            if result == 0:
                continue
            else:
                return result