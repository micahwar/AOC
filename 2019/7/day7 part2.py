import itertools
with open("input.txt", "r") as f:
    memory = [[int(x) for x in f.read().split(",")]] *5
indexes = [0, 0, 0, 0, 0]
memory = [[int(x) for x in "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5".split(",")]]*5
EOuputs = []
def returnIndexes(mode, numParameters, i, data, index):
    global indexes
    global memory
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
def intCode(codes, inputs, isFirstIteration, i):
    running = True
    global indexes
    global memory
    data = memory[i]
    index = indexes[i]
    #print(indexes)
    inputIndex = 0
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
            vals = returnIndexes(mode, 3, i, data, index)
            #print(vals)
            data[vals[2]] = data[vals[0]] + data[vals[1]]
            index += 4
        elif opcode == 2:
            vals = returnIndexes(mode, 3, i, data, index)
            data[vals[2]] =data[vals[0]] * data[vals[1]]
            index += 4
        elif opcode == 3:
            vals = returnIndexes(mode, 1, i, data, index)
            data[vals[0]] = inputs[inputIndex] if isFirstIteration else inputs[0]
            inputIndex += 1
            index += 2
        elif opcode == 4:
            vals = returnIndexes(mode, 1, i, data, index)
            memory[i] = data
            indexes[i] = index
            index += 2
            return (data[vals[0]])
            
        elif opcode == 5:
            vals = returnIndexes(mode, 2, i, data, index)        
            if data[vals[0]] != 0:
                index = data[vals[1]]
            else:
                index += 3
        elif opcode == 6:
            vals = returnIndexes(mode, 2, i, data, index)        
            if data[vals[0]] == 0:
                index = data[vals[1]]
            else:
                index += 3
        elif opcode == 7:
            vals = returnIndexes(mode, 3, i, data, index)
            if data[vals[0]] < data[vals[1]]:
                data[vals[2]] = 1
            else:
                 data[vals[2]] = 0
            index += 4
        elif opcode == 8:
            vals = returnIndexes(mode, 3, i, data, index)
            if data[vals[0]] == data[vals[1]]:
                data[vals[2]] = 1
            else:
                 data[vals[2]] = 0
            index += 4
        elif opcode == 9:
            vals = returnIndexes(mode, 1, i, data, index)
            relativeBase += data[vals[0]]
            index += 2
        if data[index] == 99:
            running = False
            memory[i] = data
            indexes[i] = index
            return -1
    
            
def getAmplifier(inputs, depth, prevAnswer):
    global memory
    global indexes
    global EOutputs
    i = [inputs[depth%5], prevAnswer] if depth < 5 else [prevAnswer]
    isFirstIter = True if depth < 5 else False
    result = intCode(memory[depth%5], i, isFirstIter, depth%5)
    if not result == -1:
        val = result
        
    else:
        return EOuputs[-1]
    if depth % 5 == 4:
        #print(indexes)
        #print(memory)
        #input()
        #print(memory[depth%5][indexes[depth%5]])
        EOuputs.append(val)
    return getAmplifier(inputs, (depth+1), val)
    
def findThrusterVals(inputs):
    global memory
    global indexes
    global EOutputs
    return getAmplifier(inputs, 0, 0)
values = []
for combination in itertools.permutations(range(5,10), 5):
    indexes = [0, 0, 0, 0, 0]
    memory = [[int(x) for x in "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5".split(",")]]*5
    EOuputs = []
    values.append(findThrusterVals(list(combination)))
print(max(values))
