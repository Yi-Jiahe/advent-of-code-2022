import re


class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> []:
        dir_pattern = re.compile(r"^dir (.*)$")
        file_pattern = re.compile(r"^(\d+) (.*)$")

        root = Node("/", children=dict())
        stack = []
        node = None
        for line in map(lambda line: line.strip(), iterable):
            if line[0] == '$':
                command, *args = line[2:].split()
                if command == "ls":
                    continue
                if command == "cd":
                    if args[0] == "/":
                        node = root
                        stack = [root]
                    elif args[0] == "..":
                        for child in node.children.values():
                            node.size += child.size
                        stack.pop()
                        node = stack[-1]
                    else:
                        node = node.children[args[0]]
                        stack.append(node)
            else:
                dir_match = dir_pattern.match(line)
                if dir_match:
                    dir_name = dir_match.group(1)
                    node.children[dir_name] = Node(dir_name, children=dict())
                    continue
                file_match = file_pattern.match(line)
                if file_match:
                    file_size = int(file_match.group(1))
                    file_name = file_match.group(2)
                    node.children[file_name] = Node(file_name, size=file_size)
                    continue
                raise ValueError("Line does not match any patterns")
        for child in node.children.values():
            node.size += child.size
        for child in root.children.values():
            root.size += child.size
        return root

    def part_one(self, data: []) -> str:    
        ans = 0
        node = None
        stack = [data]
        while stack:
            node = stack.pop()
            if node.size <= 100000:
                ans += node.size
            for child in node.children.values():
                if child.children:
                    stack.append(child)
        print(f"The sum of the total sizes of directories with size at most 100000 is {ans}.")
        return str(ans)


    def part_two(self, data: []) -> str:
        ans = None
        raise NotImplementedError
        return ans

class Node:
    def __init__(self, name, size=0, children=None):
        self.name = name
        self.size = size
        self.children = children
    
    def print(self, depth=0, print_dir_size=False):
        indentation = ' ' * depth
        if not self.children:
            print(f"{indentation}- {self.name} (file, size={self.size})")
        else:
            if print_dir_size:
                print(f"{indentation}- {self.name} (dir, size={self.size})")
            else:
                print(f"{indentation}- {self.name} (dir)")
            for child in self.children.values():
                child.print(depth=depth+1)
