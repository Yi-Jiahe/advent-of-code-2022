import functools
import re


class Blueprint:
    def __init__(self, id: int, costs: dict):
        self.id = id
        self.costs = costs

    def solve(self):
        max_robots_required = {
            'ore': max(self.costs['ore']['ore'], self.costs['clay']['ore'], self.costs['obsidian']['ore'], self.costs['geode']['ore']),
            'clay': self.costs['obsidian']['clay']
        }

        @functools.cache
        def step(time_left: int, robots: tuple, resources: tuple) -> int:
            if time_left == 0:
                return 0
            
            # Collect geodes first in case of early return
            geodes_mined = robots[3]

            if time_left == 1:
                return geodes_mined

            can_build = {
                'ore': resources[0] >= self.costs['ore']['ore'],
                'clay': resources[0] >= self.costs['clay']['ore'],
                'obsidian': resources[0] >= self.costs['obsidian']['ore'] and resources[1] >= self.costs['obsidian']['clay'],
                'geode': resources[0] >= self.costs['geode']['ore'] and resources[2] >= self.costs['geode']['obsidian']
            }

            # Collect resources
            resources = list(resources)
            for i, n in enumerate(robots[:3]):
                resources[i] += n

            # Cap resources
            if robots[0] >= max_robots_required['ore']:
                resources[0] = max_robots_required['ore']
            if robots[1] >= max_robots_required['clay']:
                resources[1] = max_robots_required['clay']

            # If resources permit, we always want to build a geode robot
            if can_build['geode'] and time_left >= 2:
                new_resources = resources.copy()
                if robots[0] < max_robots_required['ore']:
                    new_resources[0] -= self.costs['geode']['ore']
                new_resources[2] -= self.costs['geode']['obsidian']
                new_robots = list(robots)
                new_robots[3] += 1
                return geodes_mined + step(time_left-1, tuple(new_robots), tuple(new_resources))

            potential_geodes_mined = []

            # Do nothing
            potential_geodes_mined.append(step(time_left-1, robots, tuple(resources)))

            # Try building an ore robot if the resources permit and we don't have enough ore production to produce 1 robot per minute and it can possibly make an impact
            if can_build['ore'] and robots[0] < max_robots_required['ore'] and time_left >= 6:
                new_resources = resources.copy()
                new_resources[0] -= self.costs['ore']['ore']
                new_robots = list(robots)
                new_robots[0] += 1
                potential_geodes_mined.append(step(time_left-1, tuple(new_robots), tuple(new_resources)))

            # Try building a clay robot if the resources permit and we don't have enough clay production to produce 1 obsidian robot per minute and it can possibly make an impact
            if can_build['clay'] and robots[1] < max_robots_required['clay'] and time_left >= 6:
                new_resources = resources.copy()
                if robots[0] < max_robots_required['ore']:
                    new_resources[0] -= self.costs['clay']['ore']
                new_robots = list(robots)
                new_robots[1] += 1
                potential_geodes_mined.append(step(time_left-1, tuple(new_robots), tuple(new_resources)))

            # Build an obsidian robot if the resources permit and it can possibly make an impact
            if can_build['obsidian'] and time_left >= 4:
                new_resources = resources.copy()
                if robots[0] < max_robots_required['ore']:
                    new_resources[0] -= self.costs['obsidian']['ore']
                if robots[1] < max_robots_required['clay']:
                    new_resources[1] -= self.costs['obsidian']['clay']
                new_robots = list(robots)
                new_robots[2] += 1
                potential_geodes_mined.append(step(time_left-1, tuple(new_robots), tuple(new_resources)))

            return geodes_mined + max(potential_geodes_mined)

        return step(24, (1, 0, 0, 0), (0, 0, 0))

class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> []:
        ret = []
        pattern = re.compile(r"^Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.$")
        for line in map(lambda line: line.strip(), iterable):
            g = [int(x) for x in pattern.match(line).groups()]
            costs = {
                'ore': {
                    'ore': g[1]
                },
                'clay': {
                    'ore': g[2]
                },
                'obsidian': {
                    'ore': g[3],
                    'clay': g[4],
                },
                'geode': {
                    'ore': g[5],
                    'obsidian': g[6]
                }
            }
            ret.append(Blueprint(g[0], costs))
        return ret

    def part_one(self, data: []) -> str:
        ans = 0
        for blueprint in data:
            print(blueprint.costs)
            geodes = blueprint.solve()
            print(f"{blueprint.id}: {geodes}")
            ans += blueprint.id * geodes
            
        print(f"Ans: {ans}")
        return str(ans)


    def part_two(self, data: []) -> str:
        ans = None
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)