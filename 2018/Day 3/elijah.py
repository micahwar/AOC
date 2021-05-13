import numpy

def cleanLine(line):
    newLine = []
    lineArr = line.split()
    ID = int(lineArr[0].replace("#", ""))

    left = int(lineArr[2].split(",")[0])
    right = int(lineArr[2].split(",")[1].replace(":", ""))
    newLine.append(left)
    newLine.append(right)


    width = int(lineArr[3].split("x")[0])
    height = int(lineArr[3].split("x")[1])
    newLine.append(width)
    newLine.append(height)

    newLine.append(ID)

    return newLine

def main():
    arr = numpy.zeros((1000, 1000), dtype = int)
    lines = 0
    with open("input") as f:
        lines = [cleanLine(x) for x in f.readlines()]

    for line in lines:
        for i in range(line[0], line[0] + line[2]):
            for j in range(line[1], line[1] + line[3]):
                arr[i][j] += 1

    count = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            if arr[i][j] > 1:
                count += 1

    print(count)

    for line in lines:
        okay = True
        for i in range(line[0], line[0] + line[2]):
            for j in range(line[1], line[1] + line[3]):
                if arr[i][j] > 1:
                    okay = False
        if okay == True:
            print(line[4])


if __name__ == "__main__":
    main()
