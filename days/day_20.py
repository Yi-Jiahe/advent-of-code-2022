class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> [int]:
        ret = []
        for line in map(lambda line: line.strip(), iterable):
            ret.append(int(line))
        return ret

    def part_one(self, data: [int]) -> str:
        n = len(data)
        numbered_data = [(i, entry) for i, entry in enumerate(data)]
        for i, entry in enumerate(data):
            old_index = numbered_data.index((i, entry))
            numbered_data.pop(old_index)
            new_index = (old_index + entry) % (n-1)
            if new_index == 0:
                new_index = n-1
            elif new_index == n-1:
                new_index = 0
            numbered_data.insert(new_index, entry)

        zero_index = numbered_data.index(0)
        a = numbered_data[(zero_index + 1000) % n]
        b = numbered_data[(zero_index + 2000) % n]
        c = numbered_data[(zero_index + 3000) % n]
        ans = a + b + c

        print(f"Ans: {ans}")
        return str(ans)

    def part_two(self, data: [int]) -> str:
        n = len(data)

        decryption_key = 811589153
        decryption_key_base = decryption_key % (n-1)

        data_with_base = []
        for i, entry in enumerate(data):
            base = entry % (n-1) * decryption_key_base 
            while base >= n-1:
                base %= n-1
            data_with_base.append((entry, base))

        numbered_data = [(i, entry, base) for i, (entry, base) in enumerate(data_with_base)]

        for _ in range(10):
            for i, (entry, base) in enumerate(data_with_base):
                old_index = numbered_data.index((i, entry, base))
                numbered_data.pop(old_index)
                new_index = (old_index + base) % (n-1)
                if new_index == 0:
                    new_index = n-1
                elif new_index == n-1:
                    new_index = 0
                numbered_data.insert(new_index, (i, entry, base))
            
        data = [entry for _, entry, _ in numbered_data]

        zero_index = data.index(0)
        a = data[(zero_index + 1000) % n]
        b = data[(zero_index + 2000) % n]
        c = data[(zero_index + 3000) % n]
        ans = a + b + c
        ans *= decryption_key

        print(f"Ans: {ans}")
        return str(ans)