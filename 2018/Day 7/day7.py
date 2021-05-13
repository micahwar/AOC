from collections import defaultdict
import time
data = open(r"G:\My Drive\School Work\Advent of Code\2018\Day 7\input.txt", "r").read().split("\n")
letters = defaultdict(list)
preReq = defaultdict(list)
for d in data:
    words = d.split()
    letters[words[1]].append(words[7])
    preReq[words[7]].append(words[1])
now = time.time()
allPreReqs = [x for x in preReq]
allLetters = [x for x in letters]
available = [x for x in allLetters if not x in allPreReqs]
start = 'B'
order = []
nextLetter = start
done = False
while done == False:
    if nextLetter in letters:
        nextLetters = letters[nextLetter]
        available += [x for x in nextLetters if not x in available]
        available = sorted(available)
        for i, j in enumerate(available):
            IN = True
            #print preReq[j]
            for x in preReq[j]:
                if not x in order:
                    IN = False
            if preReq[j] == []:
                IN == True
            if IN == True:
                nextLetter = j
                break            
        del available[available.index(nextLetter)]
        order.append(nextLetter)
        
    else:
        done = True
print ("Part 1: " + "".join(order) + " : " + str(time.time() - now))
