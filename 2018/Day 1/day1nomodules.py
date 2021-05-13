#python 3.6
seen = set()
with open("input.txt", "r") as f:
    data = f.read().split("\n")
freqs = []
for i in range(0, len(data)):
    freqs.append(int(data[i]))
acc = 0
while done == False:
    for f in freqs:
        acc += f
        if not acc in seen:
            seen.add(acc)
        else:
            print (acc)
            done = True
            break
        
