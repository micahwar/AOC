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
workers = [0, 0, 0, 0, 0]
waitTime = 0
tick = 0
while done == False:
    tick += 1
    for worker in workers:
        if waitTime == 0:
            if nextLetter in letters:
                
                
                worker[0] = ord(nextLetter) - 4
                worker[1] = nextLetter
            else:
                done = True
        else:
            worker[0] -= 1
order = "".join(order)
print ("Part 2: " + order + " : " + str(time.time() - now))