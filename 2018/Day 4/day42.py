def cleanLine(line):
    line = line.replace("[", "").replace("]", "").replace("#", "")
    arr = line.split()

    date = arr[0].split("-")
    arr.pop(0)
    x = 0
    for item in date:
        arr.insert(x, item)
        x += 1

    time = arr[3].split(":")
    arr.pop(3)
    x = 3
    for item in time:
        arr.insert(x, item)
        x += 1

    for i in range(0, 5):
        arr[i] = int(arr[i])

    return arr

def getDataValue(line):
    month = line[1]
    day = line[2]

    hour = line[3]
    minute = line[4]

    total = (month * 30) + (day) + (hour / 24) + ((minute / 60) / 24)

    return total

def part1and2():
    lineInfo = []
    data = {}
    values = []
    lines = 0
    with open("input") as f:
        lines = f.readlines()

    newF = open("ordered4.txt", "w+")
    for i in range(0, len(lines)):
        line = cleanLine(lines[i])
        value = getDataValue(line)
        lineInfo.append(line)
        data[value] = i
        values.append(value)

    values.sort()
    for value in values:
        lineStr = data[value]
        lineStr = lineInfo[lineStr]
        for i in range(0, len(lineStr)):
            lineStr[i] = str(lineStr[i])

        lineStr = " ".join(lineStr)
        newF.write(lineStr + "\n")

    newF.close()

    newF = open("ordered4.txt")
    linesN = newF.readlines()
    currentID = 0
    timeAsleep = {}
    currentSleep = 0
    startSleepM = 0
    startSleepH = 0
    IDs = []
    times = []
    minutes = []
    for i in range(0, 23):
        minute = []
        minutes.append(minute)
        times.append(0)
    for line in linesN:
        lineArr = line.split()
        for i in range(0, 5):
            lineArr[i] = int(lineArr[i])
        if lineArr[5] == "Guard":
            currentID = lineArr[6]
            if currentID not in IDs:
                IDs.append(currentID)
        if lineArr[5] == "falls":
            startSleepM = lineArr[4]
            startSleepH = lineArr[3]

        if lineArr[5] == "wakes":
            differenceM = 0
            differenceH = 0
            if lineArr[4] > startSleepM:
                differenceM = lineArr[4] - startSleepM
                for i in range(startSleepM, lineArr[4]):
                    minutes[IDs.index(currentID)].append(i)

            times[IDs.index(currentID)] += differenceM

    best = 0
    bestIndex = 0
    for i in range(0, len(times)):
        if times[i] > best:
            best = times[i]
            bestIndex = i

    mostCommon = 0
    mostCount = 0
    for item in minutes[bestIndex]:
        if minutes[bestIndex].count(item) > mostCount:
            mostCommon = item
            mostCount = minutes[bestIndex].count(item)

    print("day 4, part 1: " + str(int(mostCommon) * int(IDs[bestIndex])))

    mostCommon = 0
    mostCount = 0
    mostID = 0
    for i in range(0, len(minutes)):
        for item in minutes[i]:
            if minutes[i].count(item) > mostCount:
                mostCount = minutes[i].count(item)
                mostCommon = item
                mostID = i

    print("day 4, part 2: " + str(int(IDs[mostID]) * int(mostCommon)))

def main():
    part1and2()

if __name__ == "__main__":
    main()
