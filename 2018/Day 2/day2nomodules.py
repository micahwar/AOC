with open("input", "r") as f:
    data = f.read().split("\n")
def counter(string):
    occ = []
    for letter in range(97, 123):
        occ.append(string.count(chr(letter)))
    return occ
three = 0
two = 0
for word in data:
    vals = counter(word)
    if 2 in vals:
        two += 1
    if 3 in vals:
        three += 1
print two * three
been = set()
for a in data:
    been.add(a)
    for b in data:
        if not a == b and not b in been:
            diff = 0
            for i, char in enumerate(a):
                if not char == b[i]:
                    diff += 1
            if diff == 1:
                print "".join([char for i, char in enumerate(a) if b[i] == char])
