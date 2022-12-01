if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
                    prog = 'Advent of Code 2022',
                    description = 'Provides solution to challenges')
    parser.add_argument('day', type=int)
    parser.add_argument('--part', type=int)
    args = parser.parse_args()

    import importlib
    try:
        module = importlib.import_module(f'days.day_{args.day}')
    except ModuleNotFoundError as e:
        print(f"Solution for day {args.day} not found")
        exit()

    solution = module.Solution()
    data = solution.load_from_file(f'inputs/day_{args.day}_input.txt')

    if not args.part:
        solution.part_one(data)
        solution.part_two(data)
    elif args.part == 1:
        solution.part_one(data)
    elif args.part == 2:
        solution.part_two(data)