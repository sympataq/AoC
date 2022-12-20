from Monkey import Monkey
from Game import Game

def read_file(filename):
    file_data = []
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            line = line.replace(',','')
            if line:
                file_data.append(line)
    return file_data                

def fill_data(data):
    pass


if __name__ == '__main__':
    file_data = read_file("11/input.txt")
    g = Game(file_data)
