

class Node:

    def __init__(self, name :str, parent=None):
        self.parent = parent
        self.name = name
        self.dirs = []
        self.files = {}

    def add_dir(self, name):
        self.dirs.append(Node(name, self))

    def add_file(self, filename, size):
        self.files[filename] = size

    def __str__(self) -> str:
        return f"{self.name}"

    def ls(self) -> str:
        ret = ""
        for dir in self.dirs:
            gap = " "*(15-len(dir))
            ret += dir + gap + "<DIR>".rjust(10) + "\n"
        for filename,sizeoffile in self.files.items():
            gap = " "*(15-len(filename))
            ret += f'{filename}'+ gap + f'{sizeoffile}'.rjust(10) +"\n"
        return ret

    def file_size(self) -> int:
        return sum(self.files.values())
    