from collections import defaultdict
with open("input.txt", "r") as f:
    data = [int(x) for x in f.read().split("\n")[0].split(",")]
data[0] = 2
joyStickData = []
board = []
running = True
index = 0
relativeBase = 0
ndata = defaultdict(int)
for i,d in enumerate(data):
    ndata[i] = d
data = ndata.copy()
#print(data)
def returnIndexes(mode, numParameters):
    returnVals = []
    for x in range(3):
        if mode[2-x] == 0:
            val = data[index+x+1]
        elif mode[2-x] == 1:
            val = index+x+1
        elif mode[2-x] == 2:
            val = data[index+x+1]+relativeBase
        returnVals.append(val)
    return returnVals[:numParameters]
while running:
    #print(data)
    parameter = data[index]
    opcode = int(str(data[index])[-2:])
    mode = [int(x) for x in list(str(data[index])[:-2])]
    
    while len(mode) < 3:
        mode = [0] + mode
    #print(data[index], ",", data[index+1], ",", data[index+2], ",", data[index+3])
    #print(parameter, " : ", opcode, ", ", mode)
    if opcode == 1:
        vals = returnIndexes(mode, 3)
        data[vals[2]] = data[vals[0]] + data[vals[1]]
        index += 4
    elif opcode == 2:
        vals = returnIndexes(mode, 3)
        data[vals[2]] =data[vals[0]] * data[vals[1]]
        index += 4
    elif opcode == 3:
        vals = returnIndexes(mode, 1)
        data[vals[0]] = ID
        index += 2
    elif opcode == 4:
        vals = returnIndexes(mode, 1)
        board.append(data[vals[0]])
        index += 2
    elif opcode == 5:
        vals = returnIndexes(mode, 2)        
        if data[vals[0]] != 0:
            index = data[vals[1]]
        else:
            index += 3
    elif opcode == 6:
        vals = returnIndexes(mode, 2)        
        if data[vals[0]] == 0:
            index = data[vals[1]]
        else:
            index += 3
    elif opcode == 7:
        vals = returnIndexes(mode, 3)
        if data[vals[0]] < data[vals[1]]:
            data[vals[2]] = 1
        else:
             data[vals[2]] = 0
        index += 4
    elif opcode == 8:
        vals = returnIndexes(mode, 3)
        if data[vals[0]] == data[vals[1]]:
            data[vals[2]] = 1
        else:
             data[vals[2]] = 0
        index += 4
    elif opcode == 9:
        vals = returnIndexes(mode, 1)
        relativeBase += data[vals[0]]
        index += 2
    if data[index] == 99:
        running = False
running = True
index = 0
count = 0
grid = [[0 for x in range(max(board)+1)] for y in range(max(board)+1)]
while running:
    if index < len(board):
        x = board[index]
        y = board[index+1]
        tileId = board[index+2]
        if tileId == 0:
            grid[x][y] = ' '
        elif tileId == 1:
            grid[x][y] = '+'
        elif tileId == 2:
            grid[x][y] = 'X'
        elif tileId == 3:
            grid[x][y] = '-'
        elif tileId == 4:
            grid[x][y] = 'O'    
        
        index += 3
    else:
        running = False

for x in range(43):
    for y in range(43):
        print(grid[x][y], end = '')

    print('')
