def maskNum(val, mask):
    val = list(str(str(val)[2:]).zfill(36))
    for n, character in enumerate(mask):
        if not character == "X":
            val[n] = character
    return int("".join(val), 2)

def part1(data):
    total = 0
    finalValues = {}
    for group in data:
        mask = group[0]
        mems = group[1]
        for mem in mems:
            value = bin(mem[1])
            value = maskNum(value, mask)
            finalValues[mem[0]] = value
    for x in finalValues:
        total += finalValues[x]
    return total

def getPossible(numString):
    possible = []
    if "X" in numString:
        
        for i in range(2):
            possible.append(numString.replace("X", str(i), 1))
            for x in getPossible(numString.replace("X", str(i), 1)):
                possible.append(x)

    
    return possible
def maskNum2(val, mask):
    val = list(str(str(bin(val))[2:]).zfill(36))
    locations = []
    for n, character in enumerate(mask):
        if character == "1":
            val[n] = character
        elif character == "X":
            val[n] = character
    locations = [int(x, 2) for x in getPossible("".join(val)) if x.find("X") == -1]
    return locations

def part2(data):
    total = 0
    finalValues = {}
    for group in data:
        mask = group[0]
        mems = group[1]
        for mem in mems:
            value = mem[1]
            for location in maskNum2(mem[0], mask):
                finalValues[location] = value
    for x in finalValues:
        total += finalValues[x]
    return total

def main(inputdata = "input/input14.txt"):
    with open(inputdata, "r") as f:
        data = f.read().split("\n")
    newData = []
    count = -1
    for line in data:
        if line.find("mask") == 0:
            newData.append([line.split("=")[1][1:], []])
            count += 1
        else:
            val = line.split(" = ")
            newData[count][1].append([int(val[0][4:].replace("]","")), int(val[1])])
    data = [x for x in newData]
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()