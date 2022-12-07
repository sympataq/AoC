from collections import deque

class myStack:
    def __init__(self,data):
        self._stack = deque(data)

    def one_move_1(self, fromm:int, where:int, amount=0):
        for i in range(amount):
            self._stack[where].append(self._stack[fromm].pop())

    def one_move_2(self, fromm:int, where:int, amount=0):
        d = deque()
        for i in range(amount):
            d.appendleft(self._stack[fromm].pop())
        self._stack[where].extend(d)
            
    def movement_1(self, movements:list):
        for move in movements:
            self.one_move_1(move[0]-1, move[1]-1, move[2])

    def movement_2(self, movements:list):
        for move in movements:
            self.one_move_2(move[0]-1, move[1]-1, move[2])

    # override to string to have nice formating
    def __str__(self) -> str:
        ret = ""
        for i in range (len(self._stack)):
            ret += str(i+1).center(3) +":"
            for j in range(len(self._stack[i])):
                ret += str(self._stack[i][j]).center(3)
            ret += "\n"
        return ret
