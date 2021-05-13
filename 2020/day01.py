def part1(data):
    for x in data:
        for y in data:
            if x + y == 2020:
                print(x*y)
def part2(data):
    for x in data:
        for y in data:
            for z in data:
                if x + y +z == 2020:
                    print(x*y*z)

def main(inputdata = "input/input1.txt"):
    with open(inputdata, "r") as f:
        data = [int(x) for x in  f.read().split("\n")]
    
    part1(data)
    part2(data)


if __name__ == "__main__":
    main()