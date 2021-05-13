import numpy as np

def part1(data):
    return 0
def part2(data):
    return 0

def main(inputdata = "input/input20.txt"):
    with open(inputdata, "r") as f:
        data = f.read().split("\n")
    
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()