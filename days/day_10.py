class CPU:
    def __init__(self):
        self.registers = {
            'X': 1
        }
        self.cycle = 0
        self.program = None

    def load_program(self, program: [(str, (str))]):
        self.program = program

    def run_program(self):
        self.cycle = 1
        yield
        for _ in self.__run_cycle():
            self.cycle += 1
            yield
        
    def signal_strength(self):
        return self.cycle * self.registers['X']

    def __run_cycle(self):
        for op, args in self.program:
            if op == "noop":
                yield
            elif op == "addx":
                yield
                self.registers['X'] += int(args[0])
                yield
        return False

class CRT:
    def __init__(self):
        # 40 pixels wide x 6 pixels high
        # '.' represents a dark pixel
        # '#' represents a lit pixel
        self.screen = [['.' for _ in range(40)] for _ in range(6)]

    def draw(self, position: int):
        self.screen[position // 40][position % 40] = '#'

    def print(self):
        for row in self.screen:
            print(row)


class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> []:
        ret = []
        for line in map(lambda line: line.strip(), iterable):
            op, *args = line.split(' ')
            ret.append((op, args))
        return ret

    def part_one(self, program: [(str, (str))]) -> str:
        ans = 0

        cpu = CPU()
        cpu.load_program(program)
        
        for _ in cpu.run_program():
            if cpu.cycle in [20, 60, 100, 140, 180, 220]:
                ans += cpu.signal_strength()

        print(f"The sum of the six signal strengths is {ans}")
        return str(ans)


    def part_two(self, program: [(str, (str))]) -> str:
        cpu = CPU()
        cpu.load_program(program)
        
        crt = CRT()

        for _ in cpu.run_program():
            middle = cpu.registers['X'] % 40
            window = [
                middle - 1,
                middle + 1 
            ]
            if window[0] <= (cpu.cycle - 1) % 40 <= window[1]:
                crt.draw(cpu.cycle - 1)

        crt.print()
        return