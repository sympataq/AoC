from collections import deque


class Worm:

    FIELD_CHAR = '.'
    HEAD_CHAR = 'H'
    TAIL_CHAR = 'T'
    START_CHAR = 's'
    VISITED = '#'

    def __init__(self):
        self.head_position = (0, 0)
        self.tail_position = (0, 0)
        self.head_movement = deque()
        self.tail_movement = deque()

    def head_move_down(self):
        self.head_position = (self.head_position[0]-1, self.head_position[1])
        self.head_movement.append(self.head_position)

    def head_move_up(self):
        self.head_position = (self.head_position[0]+1, self.head_position[1])
        self.head_movement.append(self.head_position)

    def head_move_left(self):
        self.head_position = (self.head_position[0], self.head_position[1]-1)
        self.head_movement.append(self.head_position)

    def head_move_right(self):
        self.head_position = (self.head_position[0], self.head_position[1]+1)
        self.head_movement.append(self.head_position)

    def tail_move(self):
        ''' move tail when head distance >= 2'''
        if self.head_tail_distance() >= 2:
            # go to the same position when head was 1 step ago
            self.tail_position = self.head_movement.index(-2)
            self.tail_movement.append(self.tail_position)

    def movement(self, movement, moves=0):
        ''' moves head and tail
            movement - list of dictionaries
            moves - if not defined going throu all steps
        '''
        steps = len(movement) if moves == 0 else moves
        for i in range(steps):
            for direction, distance in movement[i].items():
                if direction == 'L':
                    step = self.head_move_left
                elif direction == 'R':
                    step = self.head_move_right
                elif direction == 'U':
                    step = self.head_move_up
                elif direction == 'D':
                    step = self.head_move_down

                for i in range(distance):
                    step()  # head move
                    self.tail_move()  # tail move

    def head_tail_distance(self) -> int:
        '''return max distance of a tail from head
            head [2,3] and tail [1,1] will return 2  (y)
            head [2,3] and tail [-3,1] will return 5 (x)
        '''
        head_x, head_y = self.head_position
        tail_x, tail_y = self.tail_position
        # calculate distance
        x = abs(max(head_x, tail_x)-min(head_x, tail_x))
        y = abs(max(head_y, tail_y)-min(head_y, tail_y))
        return x if x > y else y

    def tail_visited(self) -> int:
        ''' return number of unique visited position for tail'''
        # convert to set
        return len(set(self.tail_movement))

    def __str__(self) -> str:
        return f'Head:{self.head_position}, Tail{self.tail_position}'

    def show_field(self) -> str:
        pass

    def show_visit(self) -> str:
        pass
