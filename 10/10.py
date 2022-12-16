from CPU import Computer


def read_file(filename):
    data = []
    with open(filename) as f:
        for line in f:
            instructions = line.rstrip().split()
            if len(instructions) > 1:
                instructions[1] = int(instructions[1])
            data.append(instructions)
    return data


if __name__ == '__main__':
    file_data = read_file("10/input.txt")

    c = Computer()
    c.load_program(file_data)
    print(c.run())
    test = str(c.crt)
    print(''.join(c.crt))
