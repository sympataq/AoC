import re
from Monkey import Monkey

class Game:

    def parse_items(self, data):
        print(data)
        pattern = re.compile(r'[0-9]+')
        ret = pattern.findall(data[2])
        print(ret)
        return ret

    def initMonkeys(self, data):
        for i in range(0, len(data), 6):
            items = self.parse_items(data[i+1])
            first, operation, second =  data[i+2][-3:]
            divisible =  int(str(data[i+3][-1:][0]))
            
            self.monkeys.append(Monkey(data[i], items, divisible))
            self.monkeys[i].operation_init(operation, first, second)
            self.monkeys[i].positive_throw_init(int(self.parse_int(data[i+4][-1:])))
            self.monkeys[i].negative_throw_init(int(self.parse_int(data[i+5][-1:])))

    def __init__(self, data):
        self.monkeys = []
        self.initMonkeys(data)

    def get_monkey(self, index) -> Monkey:
        try:
            m = self.monkeys[index]
        except IndexError:
            print(f'Invalid index:{index}')
    
    def play_game():
        pass
    

