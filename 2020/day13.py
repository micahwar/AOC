from sympy.ntheory.modular import crt
def part1(data):
    earliest = int(data[0])
    times = [int(x) for x in data[1].split(",") if x.isnumeric()]
    lowest = float('inf')
    lowestThing = 0
    for time in times:
        if time - (earliest % time)  < lowest:
            lowest = time - (earliest % time)
            lowestThing = time
    print(lowestThing)
    return lowest* lowestThing


def part2(data):
    times = [int(x) if x.isnumeric() else "x" for x in data[1].split(",")]
    n = []
    a = []
    for i,x in enumerate(times):
        if x == "x":
            continue
        n.append(int(x))
        a.append(int(x)-i)
    print(crt(n, a))

    return 0
def main(inputdata = "input/input13.txt"):
    with open(inputdata, "r") as f:
        data = f.read().split("\n")
    print(data)
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()