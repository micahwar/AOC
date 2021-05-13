with open("input.txt", "r") as f:
    ndata = [int(x) for x in f.read().split(",")]
def part1(noun, verb, data):
    data[1] = noun
    data[2] = verb
    going = True
    index = 0
    result = 0
    while going:
        opcode = data[index]
        if opcode == 1:
            result = data[data[index+1]]+data[data[index+2]]
        elif opcode == 2:
            result = data[data[index+1]]*data[data[index+2]]
        data[data[index+3]] = result
        index += 4
        if data[index] == 99:
            going = False
    return data[0]

def part2():
    for x in range(0,100):
        for y in range(0,100):
            wdata = ndata.copy()
            if part1(x, y, wdata) == 19690720:
                print(x)
                print(y)
part2()
