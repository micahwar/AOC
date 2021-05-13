from collections import defaultdict
with open("input.txt", "r") as f:
    data = [int(x) for x in f.read().split(",")]
running = True
output = []
tmpOutput = []
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
        data[vals[0]] = 0
        input("Something went wrong")
        index += 2
    elif opcode == 4:
        vals = returnIndexes(mode, 1)
        char = (data[vals[0]])
        if char == 35:
            tmpOutput.append(1)
        elif char == 46:
            tmpOutput.append(0)
        elif char == 10:
            output.append(tmpOutput)
            tmpOutput = []
        else:
            tmpOutput.append(char)
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

for x in output:
    print(x)
print(output[16][36])
grid = [[0 for x in range(len(output))] for y in range(len(output[0]))]
total = 0
for i, line in enumerate(output):
    for j, value in enumerate(line):
        grid[j][i] = value
def isOnEdge(x1, y1, x2, y2):
    return (x1 - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y);

for i, x in enumerate(grid):
    for j, y in enumerate(x):
        valid = False
        
        if i > 0 and j > 0 and i < len(grid)-1 and j < len(x)-1:
            valid = grid[i+1][j] == 1 and grid[i-1][j] and grid[i][j+1] == 1 and grid[i][j-1]
        if valid:
            total += i*j
print(total)






















