
import math
from collections import deque


class Monkey:

    def worry_check(self) -> int:
        return self.operation()

    def div_check(self, num):
        return True if num % self.divisible == 0 else False

    def round(self):
        for i in range(len(self.items)):
            #item = math.floor((self.worry_check()) / 3)
            item = self.worry_check()
            if (self.div_check(item)):
                self.pos_throw.throw(item)
            else:
                self.neg_throw.throw(item)
            self.items.popleft()
            self.inspected += 1

    def get_inspected(self) -> int:
        return self.inspected

    def throw(self, item):
        self.items.append(item)

    def negative_throw_init(self, monkey):
        self.negative_throw = monkey

    def positive_throw_init(self, monkey):
        self.positive_throw = monkey

    def update_throws(self, monkey_pos, monkey_neg):
        self.pos_throw = monkey_pos
        self.neg_throw = monkey_neg

    def operation_mul(self) -> int:
        a = self.first if not self.first_old else self.items[0]
        b = self.second if not self.second_old else self.items[0]
        return a * b

    def operation_plus(self) -> int:
        a = self.first if not self.first_old else self.items[0]
        b = self.second if not self.second_old else self.items[0]
        return a + b

    def operation_init(self, operation, first, second):
        self.operation_sign = operation
        if self.operation_sign == '*':
            self.operation = self.operation_mul
        elif self.operation_sign == '+':
            self.operation = self.operation_plus

        if first == 'old':
            self.first_old = True
        else:
            self.first_old = False

        if second == 'old':
            self.second_old = True
        else:
            self.second_old = False
        self.first = int(first) if not self.first_old else self.items[0]
        self.second = int(second) if not self.second_old else self.items[0]

    def __init__(self, name, items, divisible) -> None:
        self.name = name
        self.items = deque(items)
        self.divisible = divisible
        self.inspected = 0

    def __str__(self) -> str:
        ret = ''
        ret += f'{self.name}:\n'
        ret += f'  Starting items:{self.items}\n'
        ret += f'  Operation: new = {self.first} {self.operation_sign} {self.second}:\n'
        ret += f'  Test : divisable by {self.divisible}\n'
        ret += f'    If true: throw to monkey {self.positive_throw}:\n'
        ret += f'    If false: throw to monkey {self.negative_throw}:\n'
        return ret
