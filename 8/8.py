
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

def look_up(data, row , column) -> int:
    if  row == 0:
        return 0
    # look up on column from actual row position
    for look in range(row-1,0,-1):
        if data[look][column] >= data[row][column]:
            return row-look
    return row

def look_down(data, row , column) -> int:
    if  row == len(data)-1:
        return 0
    # look down on column from actual row position
    for look in range(row+1, len(data)-1):
        if data[look][column] >= data[row][column]:
            return look-row
    return len(data)-1-row

def look_right(data, row , column) -> int:
    if  column == len(data[row])-1:
        return 0
    # look right from actual column position
    for look in range(column+1, len(data[row])):
        if data[row][look] >= data[row][column]:
            return look-column
    return len(data[row])-1-column
    
def look_left(data, row , column) -> int:
    if column == 0:
        return 0
    for look in range(column-1, 0, -1):
        if data[row][look] >= data[row][column]:
            return column - look
    return column

def look_all_direction(data, row, column):
    return  look_down(data, row, column) * \
            look_up(data, row, column) * \
            look_left(data, row, column) * \
            look_right(data, row, column)


def file_read(filename='input.txt'):
    filedata = []
    try:
        with open(filename) as f:
            for line in f:
                clearline = line.rstrip()
                filedata.append([int(i) for i in clearline])
    except FileNotFoundError:
        print("Wrong filename or path")
    return filedata

if __name__=='__main__':
    file_data = file_read("8/input.txt")

visible = 0
for row in range (len(file_data)):
    for column in range (len(file_data[row])):
        if isVisibleHorizontal(file_data, row, column) or \
           isVisibleVertical(file_data, row, column):
            visible += 1
print(visible)

max_score, actual_score = 0,0
for row in range (len(file_data)):
    for column in range (len(file_data[row])):
            actual_score = look_all_direction(file_data, row, column)
            if  actual_score > max_score:
                max_score = actual_score
print(max_score)
                 

