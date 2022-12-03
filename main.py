import datetime
import zoneinfo

def get_curr_day():
    now = datetime.datetime.now(zoneinfo.ZoneInfo("America/New_York"))
    if now < datetime.datetime.fromisoformat("2022-12-01 00:00:00.000000-05:00"):
        return "01"
    elif now < datetime.datetime.fromisoformat("2022-12-25 23:59:59.999999-05:00"):
        return now.strftime("%d")
    else:
        return "25"

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
                    prog = 'Advent of Code 2022',
                    description = 'Provides solution to challenges')
    parser.add_argument('day', type=int, nargs='?', default=get_curr_day())
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