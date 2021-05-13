def part1(data):
    i = 0
    cups = [x for x in data]
    for x in range(100):
        print(cups)
        original = cups[i]
        print("\"" + original + "\"")
        destination = int(cups[i]) - 1
        if not i+1+3 > len(cups):
            pickUp = cups[i+1:i+1+3]
            print(pickUp)
            del cups[i+1:i+1+3]
        else:
            pickUp = cups[i+1:]
            length = len(pickUp)
            pickUp += cups[:3-length]
            print(pickUp)
            del cups[i+1:]
            del cups[:3-length]
        target = -1
        while target == -1:
            try: 
                target = cups.index(str(destination))
            except ValueError:
                target = -1
            destination -= 1
            if destination <= 0:
                destination = 9
        print(cups[target])
        target += 1
        
        for cup in reversed(pickUp):
            cups.insert(target, cup)
        i = (1 + cups.index(original))% len(cups)
    return "".join(cups)
def part2(data):
    return 0

def main(inputdata = "input/input23.txt"):
    with open(inputdata, "r") as f:
        data = f.read().split("\n")
    data = list("389547612")
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()