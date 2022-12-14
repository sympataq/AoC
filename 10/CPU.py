from collections import deque


class Computer:

    def __init__(self):
        self.cycle = 1
        self.register = 1
        self.CPU = {'Start': 0, 'Busy': False, 'Length': 0}
        self.boots = []
        self.SIGNAL_BOOSTS = [20, 60, 100, 140, 180, 220]
        self.INSTRUCTION_LENGTH = {'noop': 1, 'addx': 2}
        self.crt = []

    def load_program(self, commands):
        self.commands = deque(commands)

    def execute_command(self, cycle) -> bool:
        cmd = self.commands[0]

        # execution finished
        if (self.CPU['Busy']) and (self.CPU['Start'] + self.CPU['Length'] == cycle):
            self.CPU['Busy'] = False
            self.CPU['Start'] = 0
            if cmd[0] == 'addx':
                # print(cmd[1])
                self.register += cmd[1]
            cmd = self.commands.popleft()

        # execution start
        if not self.CPU['Busy']:
            self.CPU['Busy'] = True
            self.CPU['Start'] = cycle
            self.CPU['Length'] = self.INSTRUCTION_LENGTH[cmd[0]]

        print(self.CPU)

    def draw_sprite(self):
        act_pixel = self.cycle % 40
        delim = '' if act_pixel != 0 else '\n'
        if act_pixel >= (self.register - 1) and act_pixel <= (self.register + 1):
            self.crt += f'{delim}#'
        else:
            self.crt += f'{delim}.'

    def run(self):
        boosts = 0
        while self.commands:
            # check signal boost
            if (self.cycle in self.SIGNAL_BOOSTS):
                boosts += self.cycle * self.register
                print(f"cycle:{self.cycle} reg:{self.register}")
            # execute command
            self.execute_command(self.cycle)
            self.draw_sprite()
            self.cycle += 1
        return boosts
