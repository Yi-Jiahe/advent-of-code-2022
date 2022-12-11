import re
import copy
import math


class Monkey:
    def __init__(self, i):
        self.i = i
        self.items = None
        self.operation = None
        self.test = None
        self.true = None
        self.false = None
        self.inspections = 0

    def play(self, relived=True) -> (int, int):
        while self.items:
            self.inspections += 1
            worry_level = self.items.pop(0)
            worry_level = self.operation(worry_level)
            if relived:
                worry_level = worry_level // 3
            reciepient = self.true if worry_level % self.test == 0 else self.false
            yield reciepient, worry_level



class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> []:
        # Example input:
        # Monkey 2:
        #  Starting items: 79, 60, 97
        #  Operation: new = old * old
        #  Test: divisible by 13
        #    If true: throw to monkey 1
        #    If false: throw to monkey 3

        monkey_pattern = re.compile(r"^Monkey (\d+):$")
        starting_pattern = re.compile(r"^\s*Starting items: (.*)$")
        operation_pattern = re.compile(r"^^\s*Operation: new = old ([\+\*]) ([\w]+)")
        test_pattern = re.compile(r"^\s*Test: divisible by (\d+)$")
        true_pattern = re.compile(r"^\s*If true: throw to monkey (\d+)$")
        false_pattern = re.compile(r"^\s*If false: throw to monkey (\d+)$")

        ret = {}
        monkey = None
        iterable = map(lambda line: line.strip(), iterable)
        for line in iterable:
            if monkey:
                raise ValueError("Something went wrong")
            
            match = monkey_pattern.match(line)
            if not match:
                continue
            
            i = int(match.group(1))
            monkey = Monkey(i)
            line = next(iterable)

            monkey.items = [int(worry_level) for worry_level in starting_pattern.match(line).group(1).split(", ")]
            line = next(iterable)

            op, right = operation_pattern.match(line).groups()

            def generate_function(op, right):
                if op == '+':
                    if right == "old":
                        return lambda x: x + x
                    else:
                        return lambda x: x + int(right)
                elif op == '*':
                    if right == "old":
                        return lambda x: x * x
                    else:
                        return lambda x: x * int(right)

            monkey.operation = generate_function(op, right)

            line = next(iterable)

            monkey.test = int(test_pattern.match(line).group(1))
            line = next(iterable)

            monkey.true = int(true_pattern.match(line).group(1))
            line = next(iterable)

            monkey.false = int(false_pattern.match(line).group(1))
            ret[monkey.i] = monkey
            monkey = None
            
        return ret

    def part_one(self, monkeys: dict) -> str:    
        monkeys = copy.deepcopy(monkeys)
    
        for round_i in range(1, 20+1):
            for _, monkey in sorted(monkeys.items()):
                for reciepient, worry_level in monkey.play():
                    monkeys[reciepient].items.append(worry_level)

        inspections = sorted([monkey.inspections for monkey in monkeys.values()])
        ans = inspections[-2] * inspections[-1]

        print(f"The level of monkey business is {ans}")

        return str(ans)


    def part_two(self, monkeys: dict) -> str:
        monkeys = copy.deepcopy(monkeys)
    
        max_worry = math.prod([monkey.test for monkey in monkeys.values()])

        for round_i in range(1, 10000+1):
            for _, monkey in sorted(monkeys.items()):
                for reciepient, worry_level in monkey.play(relived=False):
                    worry_level %= max_worry
                    monkeys[reciepient].items.append(worry_level)

        inspections = sorted([monkey.inspections for monkey in monkeys.values()])
        ans = inspections[-2] * inspections[-1]

        print(f"The level of monkey business is {ans}")

        return str(ans)
