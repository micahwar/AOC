bags = {"light red": [[1, "bright white"], [2, "muted yellow"]], "dark orange": [[3, "bright white"], [4, "muted yellow"]], "bright white": [[1, "shiny gold"]], "muted yellow": [[2, "shiny gold"], [9, "faded blue"]], "shiny gold": [[1, "dark olive"], [2, "vibrant plum"]], "dark olive": [[3, "faded blue"], [4, "dotted black"]], "vibrant plum": [[5, "faded blue"], [6, "dotted black"]], "faded blue": [], "dotted black": []}

def part1(data):
    for val in bags.keys():
        for children in bags[val]:
            print(bags[children])
            if len(bags[children]) == 0:
                return 1
            else:
                return children[0] * part1(children[1])
def part2(data):
    return 0

def main(inputdata = "input/input7.txt"):
    with open(inputdata, "r") as f:
        data = f.read().split("\n")
    print(data)
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()