from collections import defaultdict
with open("input4", "r") as f:
    lines = sorted(f.read().split("\n"))
guards = defaultdict(lambda:[0 for x in range(60)])
for line in lines:
    if "Guard" in line:
        guard = line.split()[3]
    elif "falls" in line:
        startMinute = int(line[15:17])
    elif "wakes" in line:
        endMinute = int(line[15:17])
        for i in range(startMinute,endMinute):
            guards[guard][i] += 1
    	
sumID = 0
sumBest = 0
sums = []
for guard in guards:
    if sum(guards[guard]) > sumBest:
        sumBest = sum(guards[guard])
        sumID = guard
maxMinute = guards[sumID].index(max(guards[sumID]))
print maxMinute
print int(sumID[1:]) * maxMinute

maxID = 0
maxBest = 0
maxs = []
for guard in guards:
    if max(guards[guard]) > maxBest:
        maxBest = max(guards[guard])
        maxID = guard
maxMinute = guards[maxID].index(max(guards[maxID]))
print int(maxID[1:]) * maxMinute
