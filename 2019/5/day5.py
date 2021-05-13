with open("input.txt", "r") as f:
    data = [int(x) for x in f.read().split(",")]
#data = [int(x) for x in "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99".split(",")]
#data = [int(x) for x in "3,0,4,0,99".split(",")]
ID = 5
running = True
index = 0
while running:
    parameter = data[index]
    opcode = int(str(data[index])[-2:])
    mode = [int(x) for x in list(str(data[index])[:-2])]
    
    while len(mode) < 3:
        mode = [0] + mode
    #print(data[index], ",", data[index+1], ",", data[index+2], ",", data[index+3])
    #print(parameter, " : ", opcode, ", ", mode)
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
        
        data[data[index+1]] = ID   
        index += 2
    elif opcode == 4:
        val = data[data[index+1]] if mode[2] == 0 else data[index+1]
        print(val)   
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
