from collections import deque


class Computer:

    SIGNAL_BOOSTS = [20, 60, 100, 140, 180, 220]

    def __init__(self):
        self.cycle = 0
        self.register = 1
        self.CPU = {'Start': 0, 'Busy': False, 'CMD': {'noop': 1, 'addx': 2}}

    def load_program(self, commands):
        self.commands = deque(commands)

    def execute_command(self, command, cycle) -> bool:
        if not self.CPU['Busy']:
            self.CPU['Busy'] = True
            self.CPU['Start'] = cycle

        self.CPU['CMD'][command]

    def run(self):
        while self.commands:
            # if not self.busy:
            command = self.commands.popleft()
            self.execute_command(self.cycle, command)
            self.cycle += 1

        pass
