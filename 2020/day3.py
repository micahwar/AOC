#from itertools import cycle
def part1(data, slope=(3, 1)):
    index = (0, 0)
    count = 0
    while index[1] < len(data):
        if data[index[1]][index[0]%len(data[0])] == 1:
            count += 1
        index = (index[0] + slope[0], index[1] + slope[1])
    return count

def part2(data):
    slopes = [(1, 1),(3, 1),(5, 1),(7, 1),(1, 2)]
    inc = 1
    for slope in slopes:
        inc *= part1(data, slope)
    return inc

def main(inputdata = "input/input3.txt"):
    with open(inputdata, "r") as f:
        data = [[1  if y == '#' else 0 for y in x] for x in f.read().split("\n")]
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()