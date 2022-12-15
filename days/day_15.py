import re


class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> []:
        pattern = re.compile(r"^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$")
        ret = []
        for line in map(lambda line: line.strip(), iterable):
            x_s, y_s, x_b, y_b = [int(s) for s in pattern.match(line).groups()]
            ret.append(((x_s, y_s), (x_b, y_b)))
        return ret

    def part_one(self, data: []) -> str:
        ans = self.overlapping_intervals(data, 2000000)
        print(f"{ans} positions cannot contain a beacon.")
        return str(ans)


    def part_two(self, data: []) -> str:
        ans = None
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)
    
    def overlapping_intervals(self, data, y: int):
        beacons_at_y = []
        intervals = []
        for sensor, beacon in data:
            if beacon[1] == y:
                beacons_at_y.append(beacon[0])

            manhattan_distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
            r = manhattan_distance - abs((sensor[1] - y))
            if r < 0:
                continue
            intervals.append((sensor[0] - r, sensor[0] + r))

        combined_intervals = self.combine_intervals(intervals)

        positions = 0
        for interval in combined_intervals:
            for x in range(interval[0], interval[1]+1):
                if x in beacons_at_y:
                    continue
                positions += 1

        return positions

    def combine_intervals(self, intervals):
        intervals.sort(key=lambda x: x[0])

        combined_intervals = []
        for interval in intervals:
            if not combined_intervals:
                combined_intervals.append(list(interval))
                continue
            if interval[0] > combined_intervals[-1][1]:
                combined_intervals.append(list(interval))
                continue
            combined_intervals[-1][1] = max(combined_intervals[-1][1], interval[1])
        
        return combined_intervals
