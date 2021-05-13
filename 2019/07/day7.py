import itertools
with open("input.txt", "r") as f:
    ndata = [int(x) for x in f.read().split(",")]

def intCode(codes, inputs):
    data = codes
    ID = 5
    running = True
    index = 0
    inputIndex = 0
    while running:
        parameter = data[index]
        opcode = int(str(data[index])[-2:])
        mode = [int(x) for x in list(str(data[index])[:-2])]
        while len(mode) < 3:
            mode = [0] + mode
        if opcode == 1:
            val1 = data[data[index+1]] if mode[2] == 0 else data[index+1]
            val2 = data[data[index+2]] if mode[1] == 0 else data[index+2]
            data[data[index+3]] = val1 + val2
            index += 4
        elif opcode == 2:
            val1 = data[data[index+1]] if mode[2] == 0 else data[index+1]
            val2 = data[data[index+2]] if mode[1] == 0 else data[index+2]
            data[data[index+3]] = val1 * val2
            index += 4
        elif opcode == 3:
            data[data[index+1]] = inputs[inputIndex]
            inputIndex += 1
            index += 2
        elif opcode == 4:
            val = data[data[index+1]] if mode[2] == 0 else data[index+1]
            return val  
            index += 2
        elif opcode == 5:
            val1 = data[data[index+1]] if mode[2] == 0 else data[index+1]
            if val1 != 0:
                val2 = data[data[index+2]] if mode[1] == 0 else data[index+2]
                index = val2
            else:
                index += 3
        elif opcode == 6:
            val1 = data[data[index+1]] if mode[2] == 0 else data[index+1]
            if val1 == 0:
                val2 = data[data[index+2]] if mode[1] == 0 else data[index+2]
                index = val2
            else:
                index += 3
        elif opcode == 7:
            val1 = data[data[index+1]] if mode[2] == 0 else data[index+1]
            val2 = data[data[index+2]] if mode[1] == 0 else data[index+2]
            val3 = data[index+3] if mode[0] == 0 else index+3
            if val1 < val2:
                data[val3] = 1
            else:
                data[val3] = 0
            index += 4
        elif opcode == 8:
            val1 = data[data[index+1]] if mode[2] == 0 else data[index+1]
            val2 = data[data[index+2]] if mode[1] == 0 else data[index+2]
            val3 = data[index+3] if mode[0] == 0 else index+3
            if val1 == val2:
                data[val3] = 1
            else:
                data[val3] = 0
            index += 4
        if data[index] == 99:
            running = False
def getAmplifier(inputs, depth, prevAnswer):
    val = intCode(ndata, [inputs[depth], prevAnswer])
    if depth < 4:
        return getAmplifier(inputs, depth+1, val)
    else:
        return val
def findThrusterVals(inputs):
    return getAmplifier(inputs, 0, 0)

values = []
for combination in itertools.permutations(range(5), 5):
    values.append(findThrusterVals(list(combination)))
print(max(values))
