import re
from Monkey import Monkey


class Game:

    def parse_items(self, data):
        intList = []
        pattern = re.compile(r'[0-9]+')
        find = pattern.findall(data)
        for r in find:
            intList.append(int(r))
        return intList

    def initMonkeys(self, data):
        j = 0
        for i in range(0, len(data), 6):
            items = self.parse_items(data[i+1])
            first, operation, second = data[i+2].split()[-3:]
            divisible = int(data[i+3].split()[-1:][0])
            monkey = Monkey(data[i], items, divisible)
            monkey.operation_init(operation, first, second)
            monkey.positive_throw_init(int(data[i+4][-1:]))
            monkey.negative_throw_init(int(data[i+5][-1:]))
            self.monkeys.append(monkey)
            print(self.monkeys[j])
            j += 1

        for i in range(len(self.monkeys)):
            self.monkeys[i].update_throws(
                self.monkeys[self.monkeys[i].positive_throw], self.monkeys[self.monkeys[i].negative_throw])

    def __init__(self, data):
        self.monkeys = []
        self.initMonkeys(data)

    def get_monkey(self, index) -> Monkey:
        try:
            m = self.monkeys[index]
        except IndexError:
            print(f'Invalid index:{index}')
            for i in range(len(self.monkeys)):
                print(
                    f'Monkey {i} inspected {self.monkeys[i].get_inspected()}')

    def play_game(self, games_to_play):
        for i in range(games_to_play):
            for monkey in self.monkeys:
                monkey.round()
            # print(i)
            for j in range(len(self.monkeys)):
                print(
                    f'{i} - Monkey {j} inspected {self.monkeys[j].get_inspected()}')

        m1, m2, *_ = sorted([x.get_inspected()
                            for x in self.monkeys], reverse=True)
        print(
            f'Monkey business:{m1 * m2}')
        # for i in range(len(self.monkeys)):
        #     print(self.monkeys[i])
