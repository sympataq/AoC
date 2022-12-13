from Node import Node
from Tree import Tree


def file_read(filename):
    file_data = []
    with open(filename) as f:
        for line in f:
            file_data.append(line.rstrip().split())
    return file_data

if __name__ == '__main__':
    data = file_read("7/input.txt")
    
    t = Tree()
    t.load_tree(data)
    t.traverse(t.root)
    # just for a show
    for key, val in t.count.items():
        print(f"{key}:{val}")

    print(sum([x for x in t.count.values() if x < 100_000]))
    


