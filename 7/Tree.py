from Node import Node

from collections import deque


class Tree:

    def __init__(self):
        self.root = Node('/')
        self.act_dir = '/'
        self.act_dir_node = self.root
        self.count = {}

    def cmd_dir(self, cmd):
        # print (cmd        )
        if cmd:
            if cmd == '/':
                self.act_dir_node = self.root
            elif cmd == '..' and self.act_dir_node != self.root:
                self.act_dir_node = self.act_dir_node.parent
            else:
                self.act_dir_node = self.act_dir_node.dirs[cmd]

    def load_tree(self, commands, num=0):

        load_lines = len(commands) if num == 0 else num
        for line in commands:
            if line[0] == '$':
                if line[1] == 'ls':
                    pass
                elif line[1] == 'cd':
                    self.cmd_dir(line[2])
            elif line[0] == 'dir':
                self.act_dir_node.add_dir(line[1])
            else:
                self.act_dir_node.add_file(line[1], line[0])

    def traverse(self, act_node: Node):
        ''' Traverse whole tree and return result '''
        self.count.setdefault(self.pwd(act_node), act_node.get_size())
        for node in act_node.dirs.values():
            self.traverse(node)

    def pwd(self, def_node) -> str:
        ''' Print working directory or defined directory'''
        ret = ''
        node = self.act_dir_node if def_node == None else def_node
        while node:
            if node == self.root:
                ret += (node.name)
            else:
                ret = ("/" + node.name) + ret
            node = node.parent
        return ret.strip()

# ├└──
