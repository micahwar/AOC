from collections import defaultdict
with open("input9.txt", "r") as f:
    data = [int(x) for x in f.read().split(",")]
#data = [int(x) for x in "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99".split(",")]
#data = [int(x) for x in "1102,34915192,34915192,7,4,7,99,0".split(",")]
ID = 2
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
        print(data[vals[0]])
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
