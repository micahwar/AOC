bags = {}
def part1(data):
    count = 0
    for val in bags.keys():
        #print(val)
        if hasGold(val):
            count += 1
    return count - 1

def hasGold(bag):
    return any(bag == "shiny gold bag" or hasGold(colours[1]) for colours in bags[bag])

def countBags(bag):
    if len(bags[bag]) == 0:
        return 1
    else:
        num = 1 + sum(colours[0] * countBags(colours[1]) for colours in bags[bag])
        return num
def part2(data):
    return countBags("shiny gold bag") - 1

def main(inputdata = "input/input7.txt"):
    with open(inputdata, "r") as f:
        data = f.read().split("\n")
    for line in data:
        part = line.split(" contain ")
        #print(part)
        if part[1] == "no other bags.":
            bags[part[0].replace("bags", "bag")] = []
        else:
            bags[part[0].replace("bags", "bag")] = [[int(x[0]), x[2:].replace(".", "").replace("bags", "bag")] for x in part[1].split(", ")]
    #print(bags)
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()