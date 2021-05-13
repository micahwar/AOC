def part1(data):
    nums = [x for x in data]
    for x in range(2020-len(data)):
        if nums.count(nums[-1]) == 1:
            nums.append(0)
        else:
            nums.append(list(reversed(nums)).index(nums[-1], 1))
    
    return (nums[-1])

def part2(data):
    nums = [x for x in data]
    prev = None
    lastOcc = {}
    for n, num in enumerate(nums):
        lastOcc[prev] = n -1
        prev = num    
    for x in range(n+1, 30000000):
        if not prev in lastOcc:
            num = 0
        else:
            num = x - 1 - lastOcc[prev]
        lastOcc[prev] = x - 1
        prev = num

    return (num)

def main(inputdata = "input/input15.txt"):
    with open(inputdata, "r") as f:
        data = f.read().split("\n")[0]
    data = "11,18,0,20,1,7,16"
    data = [int(x) for x in data.split(",")]
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()