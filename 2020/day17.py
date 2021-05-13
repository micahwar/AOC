data = []
data4d = []
def getNeighbours(x, y, z):
    global data
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if z+k in data and y+i >= 0 and x+j >= 0 and y+i<len(data[z+k]) and x+j<len(data[z+k][y+i]):
                    if data[z+k][y+i][x+j] == '#':
                        count += 1
    if data[z][y][x] == "#":
        count -= 1
    return count

def update():
    global data
    newGrid = {}
    print(newGrid)
    data[min(data)-1] = [["."]*len(data[0][0])]*len(data[0])
    data[max(data)+1] = [["."]*len(data[0][0])]*len(data[0])
    for z in data:
        data[z] = [["."]*(len(data[z][0])+2)] + [["."]*1+[x for x in y]+["."]*1 for y in data[z]] + [["."]*(len(data[z][0])+2)]
    for z in data:
        newGrid[z] = [[x for x in y] for y in data[z]]
    for z in data:
        for y in range(len(data[z])):
            for x in range(len(data[z][y])):
                neightbours = getNeighbours(x, y, z)
                if data[z][y][x] == "#" and not(neightbours == 2 or neightbours == 3):
                    newGrid[z][y][x] = "."
                elif data[z][y][x] == "." and neightbours == 3:
                    newGrid[z][y][x] = "#"
    for z in newGrid:
        data[z] = [[y for y in x] for x in newGrid[z]]

def getNeighbours4d(x, y, z, w):
    global data4d
    count = 0
    for a in range(-1, 2):
        for k in range(-1, 2):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if w+a in data4d and z+k in data4d[w+a] and y+i >= 0 and x+j >= 0 and y+i<len(data4d[w+a][z+k]) and x+j<len(data4d[w+a][z+k][y+i]):
                        if data4d[w+a][z+k][y+i][x+j] == '#':
                            count += 1
    if data4d[w][z][y][x] == "#":
        count -= 1
    return count

def newW():
    global data4d
    new = {}
    for z in data4d[0]:
        new[z] = [["."]*len(data4d[0][0][0])]*len(data4d[0][0])
    return new

def update4d():
    global data4d
    newGrid = {}
    print(newGrid)
    data4d[min(data4d)-1] = newW()
    data4d[max(data4d)+1] = newW()
    for w in data4d:
        data4d[w][min(data4d[w])-1] = [["."]*len(data4d[0][0][0])]*len(data4d[0][0])
        data4d[w][max(data4d[w])+1] = [["."]*len(data4d[0][0][0])]*len(data4d[0][0])
    for w in data4d:
        for z in data4d[w]:
            # for y in data4d[w][z]:
            #     print("".join(y))
            data4d[w][z] = [["."]*(len(data4d[0][0][0])+2)] + [["."]*1+[x for x in y]+["."]*1 for y in data4d[w][z]] + [["."]*(len(data4d[0][0][0])+2)]
            # print("----")
            # for y in data4d[w][z]:
            #     print("".join(y))
    for w in data4d:
        newGrid[w] = {}
        for z in data4d[w]:
            newGrid[w][z] = [[x for x in y] for y in data4d[w][z]]
    for w in data4d:
        for z in data4d[w]:
            for y in range(len(data4d[w][z])):
                for x in range(len(data4d[w][z][y])):
                    neightbours = getNeighbours4d(x, y, z, w)
                    if data4d[w][z][y][x] == "#" and not(neightbours == 2 or neightbours == 3):
                        newGrid[w][z][y][x] = "."
                    elif data4d[w][z][y][x] == "." and neightbours == 3:
                        newGrid[w][z][y][x] = "#"
    
    for w in newGrid:
        for z in newGrid[w]:
            data4d[w][z] = [[x for x in y] for y in newGrid[w][z]]
    
def part1():
    global data
    for n in range(6):
        update()
    total = 0
    for z in data:
        for y in data[z]:
            total += "".join(y).count("#")
    return total

def part2():
    global data4d
    for n in range(6):
        update4d()
        print()
        print()
        for w in data4d:
            for z in data4d[w]:
                print(w, z)

                for y in data4d[w][z]:
                    print("".join(y))
    total = 0
    for w in data4d:
        for z in data4d[w]:
            for y in data4d[w][z]:
                total += y.count("#")
    return total

def main(inputdata = "input/input17.txt"):
    global data, data4d
    with open(inputdata, "r") as f:
        ndata = f.read().split("\n")
#     ndata = [list(x) for x in """.#.
# ..#
# ###""".split("\n")]
    
    ndata = [list(x) for x in ndata]
    #ndata = [["."]*(len(ndata[0][0])+8)] + [["."]*4+[x for x in y]+["."]*4 for y in data[z]] + [["."]*(len(data[z][0][0])+8)]
    data = {}
    data4d = {}
    data[0] = ndata
    data4d[0] = {}
    data4d[0][0] = ndata
    print(data)
    #print(part1())
    print(part2())


if __name__ == "__main__":
    main()