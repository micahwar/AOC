def part1(data):
    IDs = []
    for line in data:
        row = [x for x in range(128)]
        col = [x for x in range(8)]
        for i in line:
            if i == "L":
                col = col[:len(col)//2]
            elif i == "R":
                col = col[len(col)//2:]
            else:
                if i == "F":
                    row = row[:len(row)//2]
                elif i == "B":
                    row = row[len(row)//2:]
        IDs.append(row[0]*8 + col[0])
    IDs = sorted(IDs)
    return sorted(IDs)
    
def part2(data):
    for n, x in enumerate(data):
        if x != n+data[0]:
            return(x-1)

def main(inputdata = "input/input5.txt"):
    with open(inputdata, "r") as f:
        data = f.read().split("\n")
    #print(data)
    print(max(part1(data)))
    print(part2(part1(data)))


if __name__ == "__main__":
    main()