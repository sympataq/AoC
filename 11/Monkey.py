

from collections import deque


class Monkey:

    def test(self, denominator: int) -> int:
        return 0

    def operation_mul(self, first, second) -> int:
        return 0

    def operation_plus(self, first, second) -> int:
        return 0

    def operation(self):
        if self.operation == '*':
            pass
        elif self.operation == '+':
            pass

        pass

    def operation_init(self, operation, first, second):
        self.operation = operation
        self.first = first
        self. second = second
        pass

    def __init__(self, items, divisible, monkey_throw) -> None:
        self.items = deque(items)
        self.divisible = divisible
        self.monkey_throw = monkey_throw
