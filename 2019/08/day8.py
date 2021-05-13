with open("input.txt", "r") as f:
    data = [int(x) for x in list(f.read())]

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

subData = chunkIt(data, len(data)//(6*25))
smallestVal = float('inf')
smallest = -1
vals = []

for i, x in enumerate(subData):
    if x.count(0) < smallestVal:
        smallestVal = x.count(0)
        smallest = i
    vals.append(x.count(0))
    
print(smallest, ": ", smallestVal)
print(subData[smallest].count(1), ",", subData[smallest].count(2))
print(subData[smallest].count(2) * subData[smallest].count(1))

