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
colours = []
for x in range(6*25):
    colour = 2
    depth = 0
    while colour > 1:
        colour = subData[depth][x]
        depth += 1
    
    colours.append(colour)
colours = ["#" if x == 1 else "-" for x in colours ]
for x in range(6):
    print(colours[0+(x*25):(len(colours)//6)*(x+1)])
