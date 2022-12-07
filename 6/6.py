import sys
from Comm_device import Comm_device

file_data = []

def read_file(filename='input.txt'):
    try:
        with open(filename) as f:
           filedata = f.read()
    except FileNotFoundError:
        print("Wrong filename or path")                
    return filedata  

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_data = read_file(sys.argv[1])
    else:
        file_data = read_file("6/input.txt")     

    cd = Comm_device(file_data)
    print(cd.detect_packet(4))
    print(cd.detect_packet(14))