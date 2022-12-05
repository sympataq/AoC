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

def parse_data1(data):
    res = []
    for line in data:
        comp1 = line[:len(line) // 2]
        comp2 = line[len(line) // 2:]
        for char in comp1:
            if char in comp2:
                res.append(char)
                break
    print(res)
    return res        

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_data = read_file(sys.argv[1])
    else:
        file_data = read_file('3/input')

    score = 0
    for char in parse_data1(file_data):
        if ord(char) > 96: # a -> 97
            score += ord(char) - 96
        else:
            score += ord(char)- 64 + 26 # A -> 65
    print(score)



    