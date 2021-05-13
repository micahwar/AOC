import time
with open("input", "r") as f:
    originalString = [ord(x) for x in f.read()]
now = time.time()
i = 0
while i < len(originalString) - 2:
    if abs(originalString[i] - originalString[i+1])  == 32:
        del originalString[i:i+2]
        i -= 1
    else:
        i += 1
    if i < 0:
        i = 0
print "Part 1: " + str(len(originalString)) + " : " + str(time.time() - now)

now = time.time()
stringLengths = {}
for letter in xrange(26):
    currentString = [char for char in originalString if char != ord("a") + letter and char != ord("A") + letter]
    i = 0
    while i < len(currentString) - 2:
        if abs(currentString[i] - currentString[i+1]) == 32:
            del currentString[i:i+2]
            i -= 1
        else:
            i += 1
        if i < 0:
            i = 0
    stringLengths[letter] = len(currentString)
print "Part 2: " + str(sorted(stringLengths.values())[0]) + " : " + str(time.time() - now)
