import functools
import re


class Blueprint:
    def __init__(self, id: int,  costs: dict):
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
            
            # Collect resources
            resources = list(resources)
            for i, n in enumerate(robots[:3]):
                resources[i] += n

            # Cap resources
            if robots[0] >= max_robots_required['ore']:
                resources[0] = max_robots_required['ore']
            if robots[1] >= max_robots_required['clay']:
                resources[1] = max_robots_required['clay']

            obsidian_mined = []
            # Do nothing
            obsidian_mined.append(step(time_left-1, robots, tuple(resources)))
            # Build an ore robot
            if resources[0] >= self.costs['ore']['ore'] and robots[0] < max_robots_required['ore']:
                new_resources = resources.copy()
                new_resources[0] -= self.costs['ore']['ore']
                new_robots = list(robots)
                new_robots[0] += 1
                obsidian_mined.append(step(time_left-1, tuple(new_robots), tuple(new_resources)))
            # Build a clay robot
            if resources[0] >= self.costs['clay']['ore'] and robots[1] < max_robots_required['clay']:
                new_resources = resources.copy()
                if robots[0] <= max_robots_required['ore']:
                    new_resources[0] -= self.costs['clay']['ore']
                new_robots = list(robots)
                new_robots[1] += 1
                obsidian_mined.append(step(time_left-1, tuple(new_robots), tuple(new_resources)))
            # Build an obsidian robot
            if resources[0] >= self.costs['obsidian']['ore'] and resources[1] >= self.costs['obsidian']['clay']:
                new_resources = resources.copy()
                if robots[0] <= max_robots_required['ore']:
                    new_resources[0] -= self.costs['obsidian']['ore']
                if robots[1] >= max_robots_required['clay']:
                    new_resources[1] -= self.costs['obsidian']['clay']
                new_robots = list(robots)
                new_robots[2] += 1
                obsidian_mined.append(step(time_left-1, tuple(new_robots), tuple(new_resources)))
            # Build a geode robot
            if resources[0] >= self.costs['geode']['ore'] and resources[2] >= self.costs['geode']['obsidian']:
                new_resources = resources.copy()
                if robots[0] <= max_robots_required['ore']:
                    new_resources[0] -= self.costs['geode']['ore']
                new_resources[2] -= self.costs['geode']['obsidian']
                new_robots = list(robots)
                new_robots[3] += 1
                obsidian_mined.append(step(time_left-1, tuple(new_robots), tuple(new_resources)))

            return robots[3] + max(obsidian_mined)

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
            ans += blueprint.id * blueprint.solve()
            
        print(f"Ans: {ans}")
        return str(ans)


    def part_two(self, data: []) -> str:
        ans = None
        raise NotImplementedError
        print(f"Ans: {ans}")
        return str(ans)