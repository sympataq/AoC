
file_data = []

def isVisibleVertical(data, row , column) -> bool:
    # border
    if row == 0 or row == (len(data)-1):
        return True

    #make "column"
    col = [data[x][column] for x in range(len(data))] 
    
    if max(col[0:row], default=0) < data[row][column]:
        return True
    if max(col[row+1:], default=0) < data[row][column]:
        return True

    return False                

def isVisibleHorizontal(data, row , column) -> bool:
    # border
    if  column == 0 or column == len(data[row])-1:
        return True
    #inside
    if max(data[row][0:column], default=0) < data[row][column]:
        return True
    if max(data[row][column+1:], default=0) < data[row][column]:
        return True
    return False                

def lookHorizontal(data, row , column) -> int:
    pass

def lookVertical(data, row , column) -> int:
    pass

def file_read(filename='input.txt'):
    file_data = []
    try:
        with open(filename) as f:
            for line in f:
                clearline = line.rstrip()
                file_data.append([int(i) for i in clearline])
    except FileNotFoundError:
        print("Wrong filename or path")
    return file_data        

if __name__=='__main__':
    file_data = file_read("8/input.txt")

visible = 0
for row in range (len(file_data)):
    for column in range (len(file_data[row])):
        if isVisibleHorizontal(file_data, row, column) or \
           isVisibleVertical(file_data, row, column):
            visible += 1
print(visible)

print(lookHorizontal)
