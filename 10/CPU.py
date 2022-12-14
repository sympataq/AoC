from collections import deque


class CPU:

    CPU_COMMANDS = {'noop': 1, 'addx': 2}
    SIGNAL_BOOSTS = [20, 60, 100, 140, 180, 220]

    def __init__(self):
        self.cycle = 0
        self.register = 1
        self.busy = False

    def load_program(self, commands):
        self.commands = deque(commands)

    def execute_command(self, command, cycle) -> bool:

        pass

    def run(self):
        while self.commands:
            if not self.busy:
                command = self.commands.popleft()
            if self.execute_command(self.cycle, command):
                self.cycle += 1

        pass
