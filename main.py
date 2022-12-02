if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
                    prog = 'Advent of Code 2022',
                    description = 'Provides solution to challenges')
    parser.add_argument('day', type=int)
    parser.add_argument('--part', type=int)
    args = parser.parse_args()

    day = str(args.day).zfill(2)
    print(f"Running solution for day {day}")

    import importlib
    try:
        module = importlib.import_module(f'days.day_{day}')
    except ModuleNotFoundError as e:
        print(f"Solution for day {day} not found")
        exit()

    solution = module.Solution()
    data = solution.load_from_file(f'inputs/day_{day}_input.txt')

    if not args.part or args.part == 1:
        print("----------Part One----------")
        try:
            solution.part_one(data)
        except NotImplementedError:
            print("Solution for part one not yet implemented")
    if not args.part or args.part == 2:
        print("----------Part Two----------")
        try:
            solution.part_two(data)
        except NotImplementedError:
            print("Solution for part one not yet implemented")