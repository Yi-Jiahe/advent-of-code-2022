import pytest

from ..days.day_21 import Solution

test_input = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""

solution = Solution()
data = solution.load(test_input.splitlines())

def test_part_one():
    assert solution.part_one(data) == "152"

def test_part_two():
    assert solution.part_two(data) == None