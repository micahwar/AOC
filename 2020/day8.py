a = 0
i = -1
instructions = []

def part1(data):
    global i
    global a
    running = True
    while running:
        i += 1
        try:
            line = data[i].split(" ")
        except:
            return True
        if not i in instructions:
            if line[0] == "jmp":
                i += int(line[1]) - 1
            elif line[0] == "acc":
                a += (int(line[1]))
            elif line[0] == "hlt": 
                print(i)
                return True
        else:
            return False
        instructions.append(i)
    
def part2(data):
    for n, line in enumerate(data):
        line = line.split(" ")
        
        if line[0] == "jmp":
            print(n, line, n+int(line[1]))
    return 0

def main(inputdata = "input/input8.txt"):
    global i, a, instructions
    with open(inputdata, "r") as f:
        data = f.read().split("\n")
    # tmpdata = [x for x in data]
    # for x in range(len(data) - 1):
    #     i = 0
    #     a = 0
    #     instructions = []
    #     data = [y for y in tmpdata]
    #     data[x] =  data[x].replace("jmp", "nop")
    #     val = part1(data)
    #     if val:
    #         print(x)
    #         print(a)
    # print("otyher one")
    # for x in range(len(data) - 1):
    #     i = 0
    #     a = 0
    #     instructions = []
    #     data = [y for y in tmpdata]
    #     data[x] = data[x].replace("nop", "jmp")
    #     if part1(data):
    #         print(a)
    part1(data)
    
    print(a)
    #print(part2(data))


if __name__ == "__main__":
    main()