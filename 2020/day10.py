import functools
def part1(data):
    diffs = []
    for n in range(len(data)):
        if n > 0:
            diffs.append(data[n] - data[n-1])
    return sum([1 for x in diffs if x == 3]) * sum([1 for x in diffs if x == 1])

@functools.lru_cache(10)
def findWays(n, acc=0):
    global data
    if n + 1 == len(data):
        acc += 1
    else:
        #acc += sum([findWays(n+x) for x in range(1, 4) if n+x <len(data) and data[n+x] - data[n] <= 3 and data[n+x] - data[n] >= 1])
        for i in range(1, 4):
            if n+i < len(data):
                diff = data[n+i] - data[n]
                if diff >= 1 and diff <= 3:
                    acc += findWays(n+i)
            else:
                break
            
    return acc

def findWays1(n, acc=1):
    i = 1
    while data[n-i] > data[n] - 3:
        i+=1
        print(data[n-i], data[n] -3)
        if data[n-i] <= 0:
            break
    return [acc, i]
def part2(data):
    return findWays(0)

def main(inputdata = "input/input10.txt"):
    global data
    with open(inputdata, "r") as f:
        data = [int(x) for x in f.read().split("\n")]
    data.sort()
    
    data = [0] + data
    data.append(max(data)+3)
    print(part1(data))
    print(part2(data[1:]))


if __name__ == "__main__":
    main()