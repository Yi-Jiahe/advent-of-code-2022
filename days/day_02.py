class Solution:
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
        symbols = {
            'A': 'Rock',
            'B': 'Paper',
            'C': 'Scissors',
            'X': 'Rock',
            'Y': 'Paper',
            'Z': 'Scissors'
        }

        total_score = 0

        for round in data:
            opponent, me = symbols[round[0]], symbols[round[1]]
        
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


    def part_two(self, data: []) -> str:
        symbols = {
            'A': 'Rock',
            'B': 'Paper',
            'C': 'Scissors',
            'X': 'lose',
            'Y': 'draw',
            'Z': 'win'
        }

        total_score = 0

        for round in data:
            opponent, outcome = symbols[round[0]], symbols[round[1]]
            
            me = None
            outcome_score = None
            if outcome == 'draw':
                outcome_score = self.scoring['outcome']['draw']
                me = opponent
            elif outcome == 'win':
                outcome_score = self.scoring['outcome']['won']
                if opponent == 'Rock':
                    me = 'Paper'
                elif opponent == 'Scissors':
                    me = 'Rock'
                elif opponent == 'Paper':
                    me = 'Scissors'
            elif outcome == 'lose':
                outcome_score = self.scoring['outcome']['lost']
                if opponent == 'Rock':
                    me = 'Scissors'
                elif opponent == 'Scissors':
                    me = 'Paper'
                elif opponent == 'Paper':
                    me = 'Rock'
            shape_score = self.scoring['shape'][me]

            total_score += shape_score + outcome_score

        print(f"The total score will be {total_score}")
        return total_score