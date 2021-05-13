#python 3.6
from itertools import accumulate, cycle
seen = set()
with open("input.txt", "r") as f:
    data = f.read().split("\n")
freqs = []
for i in range(0, len(data)):
    freqs.append(int(data[i]))
acc = 0
for f in accumulate(cycle(freqs)):
    if not f in seen:
        seen.add(f)
    else:
        print (f)
        break

        
        
