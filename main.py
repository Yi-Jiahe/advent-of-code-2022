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
        module = importlib.import_module(f'day_{args.day}')
    except ModuleNotFoundError as e:
        print(f"Solution for day {args.day} not found")
        exit()

    solution = module.Solution()
    solution.load_data()

    if not args.part:
        solution.part_one()
        solution.part_two()
    elif args.part == 1:
        solution.part_one()
    elif args.part == 2:
        solution.part_two()


    