import sys

file_data = []
# priority = {num : val for num in range (1, 53) for val in range()}
def read_file(filename='input'):
    filedata = []
    try:
        with open(filename) as file:
            for line in file:
                filedata.append(line.rstrip())
    except FileNotFoundError:
        print("Wrong file or file path")
    return filedata

def parse_data():
    test = []
    for num in range (150):
        print(f'num {num}: {chr(num)}')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_data = read_file(sys.argv[1])
    else:
        file_data = read_file('3/input')

    # print(file_data)
    parse_data()

    