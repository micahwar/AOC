data = open(r"G:\My Drive\School Work\Advent of Code\2018\Day 10\input.txt").read().split("\n")
newData = []
values = []
def strp(string):
    return int(string.strip())
for d in data:
    newData.append([strp(d[10:16]), strp(d[18:24])])
    values.append([strp(d[36:38]), strp(d[40:42])])

minDiff = 9999999999
minTime = 0
time = 10007
for i, d in enumerate(newData):
        newData[i] = [d[0] + values[i][0] * time, d[1] + values[i][1] * time]
with open(r"C:\Users\mpowa\Documents\Processing\AoC_Day10\data\output.txt", "w") as f:
            for i in newData:
                f.write(" ".join([str(x) for x in i]) + "\n")
# for time in range(1, 100000):
#     minx = 9999999    
#     miny = 9999999
#     maxx = 0
#     maxy = 0
#     for i, d in enumerate(newData):
#         newData[i] = [d[0] + values[i][0], d[1] + values[i][1]]
#     #for i in range(0, len(newData)):
#         if newData[i][0] > maxx:
#             maxx = newData[i][0]
#         elif newData[i][0] < minx:
#             minx = newData[i][0]
#         if newData[i][1] > maxy:
#             maxy = newData[i][1]
#         elif newData[i][1] < miny:
#             miny = newData[i][1]
#     if (abs(maxx - minx) + abs(maxy - miny)) < minDiff:
#         minDiff = abs(maxx - minx) + abs(maxy - miny)
#         minTime = time
#         #print(time)
#     else:
#         print (time)
#         with open(r"G:\My Drive\School Work\Advent of Code\2018\Day 10\output.txt", "w") as f:
#             for i in newData:
#                 f.write(" ".join([str(x) for x in i]) + "\n")
#         break
    
