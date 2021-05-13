def part1(data):
    count = 0
    for group in data:
        letters = set("".join(group.split("\n")))
        count += len(letters)
    return count
def part2(data):
    c = 0
    for group in data:
        letters = set("".join(group.split("\n")))
        length = len(group.split("\n"))
        group = "".join(["".join(set(x)) for x in group.split("\n")])
        for letter in letters:
            if group.count(letter) == length:
                c+=1
    return c

def main(inputdata = "input/input6.txt"):
    with open(inputdata, "r") as f:
        data = f.read().split("\n\n")
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
