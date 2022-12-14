from worm import Worm


def read_file(filename):
    data = []
    with open(filename) as f:
        for line in f:
            line.rstrip()
            direction, movement = line.split()
            data.append([direction, int(movement)])
    return data


if __name__ == '__main__':
    file_data = read_file("9/input.txt")

    worm = Worm()
    worm.movement_part1(file_data)
    print(f'tail visited:{worm.tail_visited()}')

    # add 9 body pieces
    worm2 = Worm(9)
    worm2.movement_part2(file_data)
    print(f'tail visited:{worm2.body_visited()}')
