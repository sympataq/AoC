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

def parse_data2(data ):
    res = []
    for i in range(0, len(data), 3 ):
        comp1 = set(data[i])
        comp2 = set(data[i+1])
        comp3 = set(data[i+2])
        intersection = comp1.intersection(comp2,comp3)
        if (intersection):
            res.append(intersection.pop())
    print(res)
    return res   

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_data = read_file(sys.argv[1])
    else:
        file_data = read_file('3/input')

    score = 0
    data = parse_data1(file_data)
    for char in data:
        if ord(char) > 96: # a -> 97
            score += ord(char) - 96
        else:
            score += ord(char)- 64 + 26 # A -> 65
    print(f"score 1: {score}")

    score = 0
    data2 = parse_data2(file_data)
    for char in data2:
        if ord(char) > 96: # a -> 97
            score += ord(char) - 96
        else:
            score += ord(char) - 64 + 26 # A -> 65
    print(f"score 2 :{score}")
    




    