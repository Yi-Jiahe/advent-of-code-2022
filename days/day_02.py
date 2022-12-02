class Solution:
    symbols = {
        'A': 'Rock',
        'B': 'Paper',
        'C': 'Scissors',
        'X': 'Rock',
        'Y': 'Paper',
        'Z': 'Scissors'
    }
    scoring = {
        'shape': {
            'Rock': 1,
            'Paper': 2,
            'Scissors': 3, 
        },
        'outcome': {
            'lost': 0,
            'draw': 3,
            'won': 6,
        }
    }

    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> []:
        ret = []
        for line in map(lambda line: line.strip(), iterable):
            ret.append(line.split())
        return ret

    def part_one(self, data: []) -> str:
        total_score = 0

        for round in data:
            opponent, me = self.symbols[round[0]], self.symbols[round[1]]
        
            shape_score = self.scoring['shape'][me]
        
            outcome = None
            if me == opponent:
                outcome = 'draw'
            elif me == 'Rock':
                outcome = 'won' if opponent == 'Scissors' else 'lost'
            elif me == 'Scissors':
                outcome = 'won' if opponent == 'Paper' else 'lost'
            elif me == 'Paper':
                outcome = 'won' if opponent == 'Rock' else 'lost'
            outcome_score = self.scoring['outcome'][outcome]

            round_score = shape_score + outcome_score

            total_score += round_score
        print(f"The total score will be {total_score}")
        return total_score


    def part_two(self, elves: [int]) -> str:
        ans = None
        raise NotImplementedError
        return ans