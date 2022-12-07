from myStack import myStack
from pathlib import Path
import sys, re

file_data = []

def read_file(filename='input.txt'):
    filedata = []
    try:
        with open(filename) as f:
            for line in f:
                filedata.append(line.rstrip())
    except FileNotFoundError:
        print("Wrong filename or path")                
    return filedata  

def parse_crates(data:list, lines:int, columns:int) -> list:
    ret = [[] for x in range(columns)]
    for i in range(lines-1, -1, -1):
        index = 0;
        for j in range(1, columns*4, 4):
            if len(data[i]) >= j:
                if str(data[i][j]).isalpha():
                    ret[index].append(data[i][j])
            index += 1
    return ret

def parse_movement(data:list, lines_from:int) -> list:
    movement_total = []
    pattern = re.compile(r"[0-9]+")
    for line in range(lines_from, len(data)):
        regexp = pattern.findall(data[line])
        movement_total.append([int(regexp[1]), int(regexp[2]), int(regexp[0])])
    return movement_total

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_data = read_file(sys.argv[1])
    else:
        file_data = read_file("5/input.txt")      
    
    stack = myStack(parse_crates(file_data, 8, 9))
    print(stack)
    stack.movement_1(parse_movement(file_data, 10))
    print(stack)
    
    stack = myStack(parse_crates(file_data, 8, 9))
    stack.movement_2(parse_movement(file_data, 10))
    print(stack)