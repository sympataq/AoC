from pathlib import Path
import re, sys

file_data = []

def read_file(filename='input'):
    filedata = []
    try:
        with open(filename) as f:
            for line in f:
                file_data.append(line.rstrip)
    except FileNotFoundError:
        print("Wrong filename or path")                
    return filedata            


if __name__ == '__main__':
    


    pass
