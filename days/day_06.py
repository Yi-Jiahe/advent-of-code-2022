class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> str:
        for line in map(lambda line: line.strip(), iterable):
            return line

    def part_one(self, data: str) -> str:  
        ans = self.find_start_of_packet_marker(data)
        print(f"{ans} characters need to be processed before the first start-of-packet marker")
        return str(ans)


    def part_two(self, data: str) -> str:
        ans = self.find_start_of_message_marker(data)
        print(f"{ans} characters need to be processed before the first start-of-message marker")
        return str(ans)

    def find_start_of_packet_marker(self, buffer):
        last_four_characters = []
        for i, char in enumerate(buffer):
            last_four_characters.append(buffer[i])
            if i < 4:
                continue
            last_four_characters.pop(0)
            if len(set(last_four_characters)) == 4:
                return i + 1

    def find_start_of_message_marker(self, buffer):
        last_fourteen_characters = []
        for i, char in enumerate(buffer):
            last_fourteen_characters.append(buffer[i])
            if i < 14:
                continue
            last_fourteen_characters.pop(0)
            if len(set(last_fourteen_characters)) == 14:
                return i + 1