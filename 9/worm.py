from collections import deque


class Worm:

    FIELD_CHAR = '.'
    HEAD_CHAR = 'H'
    TAIL_CHAR = 'T'
    START_CHAR = 's'
    VISITED = '#'

    def __init__(self, bodyparts=0):
        self.head_position = (0, 0)
        self.tail_position = (0, 0)
        self.head_movement = deque()
        self.tail_movement = deque()
        self.head_movement.append(self.head_position)
        self.tail_movement.append(self.tail_position)

        # part 2
        self.bodyparts = bodyparts
        self.body_positions = []
        self.body_movements = []
        for i in range(bodyparts):
            self.body_positions.append((0, 0))
            self.body_movements.append(deque(self.body_positions[i]))

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
        if self.head_tail_distance(self.head_position, self.tail_position) >= 2:
            # go to the same position when head was 1 step ago
            self.tail_position = self.head_movement[-2]
            self.tail_movement.append(self.tail_position)

    def body_move(self):
        ''' move body when head distance >= 2'''

        # let's make first from head
        if self.head_tail_distance(self.head_position, self.body_positions[0]) >= 2:
            # go to the same position where head was 1 step ago
            self.body_positions[0] = self.head_movement[-2]
            self.body_movements[0].append(self.body_positions[0])

        # and rest
        for body in range(1, len(self.body_positions)):
            # print(f"body :{body} {self.body_positions[body-1]} {self.body_positions[body]}")
            if self.head_tail_distance(self.body_positions[body-1], self.body_positions[body]) >= 2:
                # go to the same position where previous body part was 1 step ago
                self.body_positions[body] = self.find_jump(
                    self.body_positions[body-1], self.body_positions[body])
                self.body_movements[body].append(self.body_positions[body])

    def find_jump(self, head, tail):
        ''' Always jump to be at least on 1 axe same'''
        head_x, head_y = head
        tail_x, tail_y = tail

        if head_x < tail_x:
            tail_x -= 1
        if head_x > tail_x:
            tail_x += 1

        if head_y < tail_y:
            tail_y -= 1
        if head_y > tail_y:
            tail_y += 1

        return (tail_x, tail_y)

    def movement_part1(self, movement, moves=0):
        ''' moves head and tail
            movement - list of lists
            moves - if not defined going throu all steps
        '''
        steps = len(movement) if moves == 0 else moves
        for i in range(steps):
            direction, distance = movement[i]
            if direction == 'L':
                step = self.head_move_left
            elif direction == 'R':
                step = self.head_move_right
            elif direction == 'U':
                step = self.head_move_up
            elif direction == 'D':
                step = self.head_move_down

            for j in range(distance):
                step()  # head move
                self.tail_move()  # tail move

    def movement_part2(self, movement, moves=0):
        ''' moves head and tail
            movement - list of lists
            moves - if not defined going throu all steps
        '''

        steps = len(movement) if moves == 0 else moves
        for i in range(steps):
            direction, distance = movement[i]
            if direction == 'L':
                step = self.head_move_left
            elif direction == 'R':
                step = self.head_move_right
            elif direction == 'U':
                step = self.head_move_up
            elif direction == 'D':
                step = self.head_move_down

            # print(f'going to move : {movement[i]}')
            for j in range(distance):
                step()  # head move
                self.body_move()  # body move

    def head_tail_distance(self, head, tail) -> int:
        '''return max distance of a tail from head
            head [2,3] and tail [1,1] will return 2  (y)
            head [2,3] and tail [-3,1] will return 5 (x)
        '''
        head_x, head_y = head
        tail_x, tail_y = tail
        # calculate distance
        x = abs(max(head_x, tail_x)-min(head_x, tail_x))
        y = abs(max(head_y, tail_y)-min(head_y, tail_y))
        return x if x > y else y

    def tail_visited(self) -> int:
        ''' return number of unique visited position for tail'''
        # convert to set
        return len(set(self.tail_movement))

    def body_visited(self) -> int:
        ''' return number of unique visited position for tail'''
        # convert to set
        print(self.body_movements[len(self.body_positions)-1])
        print("\n")
        print(set(self.body_movements[len(self.body_positions)-1]))
        return len(set(self.body_movements[len(self.body_positions)-1]))

    def __str__(self) -> str:
        return f'Head:{self.head_position}, Tail{self.tail_position}'

    def show_field(self) -> str:
        # TODO later
        pass

    def show_visit(self) -> str:
        # TODO later
        pass
