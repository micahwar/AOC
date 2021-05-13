length = 25
def containsPair(aim, l):
    return any(a + b == aim for a in l for b in l)

def part1(data):
    for x in range(len(data)-length):
        if not containsPair(data[length+x], data[x:length+x]):
            return (data[length+x])

def part2(data, invalid):
    for n in range(len(data)):
        i = 0
        acc = 0
        while acc < invalid:
            acc = sum(data[n:n+i+1])
            if acc == invalid:
                return min(data[n:n+i+1]) + max(data[n:n+i+1])
            i+=1
    return 0

def main(inputdata = "input/input9.txt"):
    with open(inputdata, "r") as f:
        data = f.read().split("\n")
    data = [int(y) for y in data]
    invalid = part1(data)
    print(invalid)
    print(part2(data, invalid))


if __name__ == "__main__":
    main()