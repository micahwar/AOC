def getNeighbours(x, y):
    global data
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if y+i >= 0 and x+j >= 0 and y+i<len(data) and x+j<len(data[0]):
                if data[y+i][x+j] == '#':
                    count += 1
    if data[y][x] == "#":
        count -= 1
    return count

def updateSeats():
    global data
    newGrid = [[y for y in x] for x in data]
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "L" and getNeighbours(x, y) == 0:
                newGrid[y][x] = "#"
            elif data[y][x] == "#" and getNeighbours(x, y) >= 4:
                newGrid[y][x] = "L"
    data = [[y for y in x] for x in newGrid]

def part1():
    global data
    shouldLoop = True
    count = 0
    while shouldLoop:
        previousData = [[y for y in x] for x in data]
        updateSeats()
        count += 1
        if previousData == data:
            shouldLoop = False
    occupied = sum([x.count("#") for x in data])
    for line in data:
        print("".join(line))
    return occupied

def updateSeatsPart2():
    global data
    newGrid = [[y for y in x] for x in data]
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "L" and getNeighboursPart2(x, y) == 0:
                newGrid[y][x] = "#"
            elif data[y][x] == "#" and getNeighboursPart2(x, y) >= 5:
                newGrid[y][x] = "L"
    data = [[y for y in x] for x in newGrid]
    
def getNeighboursPart2(x, y):
    global data
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            mult = 1
            exiting = False
            while not exiting:
                if y+i*mult >= 0 and x+j*mult >= 0 and y+i*mult<len(data) and x+j*mult<len(data[0]):
                    if data[y+i*mult][x+j*mult] == '#':
                        count += 1
                        exiting = True
                    elif data[y+i*mult][x+j*mult] == 'L':
                        exiting = True
                    elif data[y+i*mult][x+j*mult] == '.':
                        mult += 1
                else:
                    exiting = True
    if data[y][x] == "#":
        count -= 1
    return count

def part2():
    global data
    shouldLoop = True
    count = 0
    while shouldLoop:
        previousData = [[y for y in x] for x in data]
        updateSeatsPart2()
        count += 1
        if previousData == data:
            shouldLoop = False
    occupied = sum([x.count("#") for x in data])
    for line in data:
        print("".join(line))
    return occupied

def main(inputdata = "input/input11.txt"):
    global data
    with open(inputdata, "r") as f:
        data = f.read().split("\n")
    data = [list(x) for x in data]
    print(part1())
    #need to reset data list before part2 or comment out part 1 to get part 2
    print(part2())

if __name__ == "__main__":
    main()