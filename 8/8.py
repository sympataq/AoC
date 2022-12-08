
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

def lookNorth(data, row , column) -> int:
    if  row == 0:
        return 0
    # look on north column from actual row position
    for look in range(row-1,0,-1):
        if data[look][column] > data[row][column]:
            return row-look
    return row

def lookSouth(data, row , column) -> int:
    if  row == len(data)-1:
        return 0
    # look on south column from actual row position
    for look in range(row+1,len(data)-1):
        if data[look][column] > data[row][column]:
            return look-row
    return row

def lookWest(data, row , column) -> int:
    if  column == len(data[row])-1:
        return 0
    # look on west from actual column position
    for look in range(column+1,len(data[row])):
        print(f"{row}{column} c:{look}:{data[row][look]}")
        if data[row][look] > data[row][column]:
            return look-row
    return len(data[row])-1-column
    
def lookEeast(data, row , column) -> int:
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
# print(visible)

# print (lookNorth(file_data,1 ,4))
# print (lookSouth(file_data,0 ,3))
# print (lookWest(file_data,1 ,2))
