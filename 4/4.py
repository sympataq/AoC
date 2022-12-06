import sys, pathlib

file_data =[]


def read_file(filename='input'):
    filedata = []
    try:
        with open(filename) as f:
            for line in f:
                filedata.append(line.rstrip())
    except FileNotFoundError:
        print("Wrong file or filepath")
    return filedata    
    



if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_data = read_file(sys.argv[1])
    else:
        file_data = read_file("4/input.txt")

    print(file_data)