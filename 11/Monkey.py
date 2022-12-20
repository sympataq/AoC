
import math
from collections import deque


class Monkey:

    def worry_check(self, item) -> int:
        return self.operation(item)

    def div_check(self, num):
        return True if num % self.divisible == 0 else False

    def round(self):
        for i in range(len(self.items)):
            item = self.items.popleft()
            item = math.floor((self.worry_check(item)) / 3)
            if (self.div_check(item)):
                self.positive_throw.throw(item)
            else:
                self.negative_throw.throw(item)

    def receive(self, item):
        self.items.append(item)

    def negative_throw_init(self, monkey):
        self.negative_throw = monkey

    def positive_throw_init(self, monkey):
        self.positive_throw = monkey

    def operation_mul(self, first, second) -> int:
        a = first if not self.first_old else self.first
        b = second if not self.second_old else self.second
        return a * b

    def operation_plus(self, first, second) -> int:
        a = first if not self.first_old else self.first
        b = second if not self.second_old else self.second
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
        print(self.items)
        self.first = int(first) if not self.first_old else self.items[0]
        self.second = int(second) if not self.second_old else self.items[0]

    def __init__(self, name, items, divisible) -> None:
        self.name = name
        self.items = deque(items)
        self.divisible = divisible

    def __str__(self) -> str:
        ret = ''
        ret += f'{self.name}:'
        ret += f'  Starting items:{self.name}:'
        ret += f'  Operation: new = {self.first} {self.operation_sign} {self.second}:'
        ret += f'  Test : divisable by {self.divisible}'
        ret += f'    If true: throw to monkey {self.positive_throw}:'
        ret += f'    If false: throw to monkey{self.negative_throw}:'
        return ret
