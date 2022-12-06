import sys, pathlib, re

file_data =[]
data = []


def read_file(filename='input'):
    filedata = []
    try:
        with open(filename) as f:
            for line in f:
                filedata.append(line.rstrip())
    except FileNotFoundError:
        print("Wrong file or filepath")
    return filedata    
    
def parse_file(data):
        pars_data = []
        pattern = re.compile(r'[0-9]+')
        for line in data:
            go = pattern.findall(line)
            intList = [int(i) for i in go]
            pars_data.append(intList)
        return pars_data    

def check_in_interval(line):
    if (line[0] <= line[2] and line[1] >= line[3]) or \
       (line[0] >= line[2] and line[1] <= line[3]):
        return True
    else:
        return False

def check_overlap (line):
    if (line[0] >= line[2] and line[0] <= line[3]) or \
       (line[1] >= line[2] and line[1] <= line[3]) or \
       (line[2] >= line[0] and line[2] <= line[1]) or \
       (line[3] >= line[0] and line[3] <= line[1]):
        return True
    else:
        return False


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_data = read_file(sys.argv[1])
    else:
        file_data = read_file("4/input.txt")

    data = parse_file(file_data)

    score,score2 = 0,0
    for line in data:
        score += check_in_interval(line)
        score2 += check_overlap(line)
    print(f"score 1:{score}, score 2:{score2}")