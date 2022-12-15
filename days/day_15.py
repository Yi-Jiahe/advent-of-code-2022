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
        ans = self.beaconless_positions(data, 2000000)
        print(f"{ans} positions cannot contain a beacon.")
        return str(ans)


    def part_two(self, data: []) -> str:
        distress_beacon_position = self.distress_beacon_position(data, 4000000)
        ans = self.tuning_frequency(distress_beacon_position)
        print(f"Tuning Frequency: {ans}")
        return str(ans)
    
    def beaconless_positions(self, data, y: int):
        scanned_positions = self.scanned_positions(data, y)

        beacons_at_y = []
        for _, beacon in data:
            if beacon[1] == y:
                beacons_at_y.append(beacon[0])

        positions = 0
        for interval in scanned_positions:
            for x in range(interval[0], interval[1]+1):
                if x in beacons_at_y:
                    continue
                positions += 1

        return positions

    def tuning_frequency(self, position):
        return position[0] * 4000000 + position[1]

    def distress_beacon_position(self, data, upper_bound: int):
        distress_beacon_position = None 
        for y in range(upper_bound+1):
            scanned_positions = self.scanned_positions(data, y)
            if len(scanned_positions) == 1:
                if scanned_positions[0][0] > 0:
                    distress_beacon_position = (0, y)
                    break
                if scanned_positions[0][1] < upper_bound:
                    distress_beacon_position = (upper_bound, y)
                    break
            else:
                found = False
                for interval in scanned_positions:
                    if interval[0] > 0:
                        found = True
                        distress_beacon_position = (interval[0]-1, y)
                        break
                    if interval[1] < upper_bound:
                        found = True
                        distress_beacon_position = (interval[1]+1, y)
                        break
                if found:
                    break
        print(y)
        if not distress_beacon_position:
            raise ValueError("No position found")
        
        return distress_beacon_position

    def scanned_positions(self, data, y: int):
        intervals = []
        for sensor, beacon in data:
            manhattan_distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
            r = manhattan_distance - abs((sensor[1] - y))
            if r < 0:
                continue
            intervals.append((sensor[0] - r, sensor[0] + r))

        return self.combine_intervals(intervals)

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
