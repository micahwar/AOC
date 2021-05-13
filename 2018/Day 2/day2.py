from collections import Counter
from itertools import combinations
with open("input", "r") as f:
    data = f.read().split("\n")
three = 0
two = 0
for word in data:
    vals = Counter(word).values()
    if 2 in vals:
        two += 1
    if 3 in vals:
        three += 1
print two * three

for a, b in combinations(data, 2):
    diff = 0
    for i, char in enumerate(a):
        if not char == b[i]:
            diff += 1
    if diff == 1:
        print "".join([char for i, char in enumerate(a) if b[i] == char])
