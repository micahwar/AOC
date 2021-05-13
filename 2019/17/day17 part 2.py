from collections import defaultdict
with open("input.txt", "r") as f:
    data = [int(x) for x in f.read().split(",")]
running = True
output = []
tmpOutput = []
startIndex = 0
hasCreatedArray = False
tmpPos = [0, 0]
index = 0
relativeBase = 0
ndata = defaultdict(int)
for i,d in enumerate(data):
    ndata[i] = d
data = ndata.copy()



def findRoute(path):
    pass


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
        message = 0
        
        data[vals[0]] = message
        index += 2
    elif opcode == 4:
        vals = returnIndexes(mode, 1)
        char = (data[vals[0]])
        if not hasCreatedArray:
            move = True
            if char == 35:
                tmpOutput.append('X')
            elif char == 46:
                tmpOutput.append('-')
            elif char == 10:
                tmpPos[0] = 0
                tmpPos[1] += 1
                move = False
                output.append(tmpOutput)
                if len(output) == 33:
                    hasCreatedArray = True
                    output = output[:-2]
                    print("Started printing output...")
                    for x in output:
                        print(x)
                    print("Finished printing output.")
                    
                    findRoute(output, startIndex)
                else:
                    tmpOutput = []
            else:
                tmpOutput.append(char)
                if char == 94:
                    startIndex = tmpPos
                
            if move:
                tmpPos[0] += 1
        else:
            
            pass
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
























