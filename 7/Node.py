

class Node:

    def __init__(self, name: str, parent=None):
        self.parent = parent
        self.name = name
        self.dirs = {}
        self.files = {}

    def add_dir(self, name):
        self.dirs[name] =  Node(name, self)

    def add_file(self, filename, size):
        self.files[filename] =  int(size)

    def __str__(self) -> str:
        return f"{self.name}"

    def sub_folder_size(self, act_node) -> int:
        size = 0
        if len(act_node.dirs) < 1:
            return act_node.files_size(act_node)
        else:
            for nod in act_node.dirs.values():
                size += act_node.sub_folder_size(nod)
        return size + act_node.files_size(act_node)               

    def files_size(self, nod) -> int:
        return sum([x for x in nod.files.values()])

    def get_size(self) -> int:
        return self.sub_folder_size(self)
