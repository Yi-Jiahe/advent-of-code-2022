import json
from itertools import zip_longest


def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == 'fill':
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == 'strict':
        return zip(*args, strict=True)
    if incomplete == 'ignore':
        return zip(*args)
    else:
        raise ValueError('Expected fill, strict, or ignore')


class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> []:
        ret = []
        for line in map(lambda line: line.strip(), iterable):
            if line == "":
                continue
            ret.append(json.loads(line))
        return ret

    def part_one(self, data: []) -> str:    
        ans = 0
        for i, (left, right) in enumerate(grouper(data, 2, incomplete='strict')):
            print(i, left, right)
            if self.compare(left, right) == 1:
                ans += i + 1
        return str(ans)


    def part_two(self, data: []) -> str:
        ans = None
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