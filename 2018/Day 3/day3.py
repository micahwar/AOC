import time
with open("input", "r") as f:
    data = f.read().split("\n")
now = time.time()
rects = []
grid = [[0 for x in xrange(1000)] for x in xrange(1000)]
for line in data:
    ln = line.split(" ")
    ID = ln[0][1:]
    lr = ln[2][:-1].split(",")
    wh = ln[3].split("x")
    rects.append([int(lr[0]), int(lr[1]), int(wh[0]), int(wh[1]), int(ID)])
for rect in rects:
    bad = 0
    for x in range(rect[0], rect[0] + rect[2]):
        for y in range(rect[1], rect[1] + rect[3]):
            grid[x - 1][y - 1] += 1

count = 0
for x in range(0, len(grid)):
    for y in range(0, len(grid)):
        if grid[x][y] > 1:
            count += 1
print count

for i, rect in enumerate(rects):
    bad = 0
    for x in range(rect[0], rect[0] + rect[2]):
        for y in range(rect[1], rect[1] + rect[3]):
            if not grid[x - 1][y - 1] == 1:
                bad += 1
    if bad == 0:
        print data[i]
print "Total: " + str(time.time() - now)


