from math import floor, ceil
from copy import deepcopy
from itertools import permutations
with open("input.txt", "r") as f:
    data = f.read().split("\n")[:-1]

def depth(L):
    return (isinstance(L, (list))) and max(map(depth, L))+1

def add(a, b):
    return reduce([a, b])

def mag(arr):
    answer = 0
    for i in range(2):
        if type(arr[i]) == int:
            answer += arr[i] * (3-i)
        else:
            answer += mag(arr[i]) * (3-i)
    return answer

def getArrToExplode(a, path=[]):
    depths = list(map(depth, a))
    maxDepth = max(depths)
    index = depths.index(maxDepth)
    arr = a[index]
    path.append(index)
    if maxDepth == 1:
        return {"array": arr, "indexes": path}
    else:
        return getArrToExplode(arr, path)

def getFromIndexList(L, indexes):
    L = L
    for index in indexes:
        L = L[index]
    return L

def setFromIndexList(L, indexes, value):
    a = "L"
    for index in indexes:
        a = a + "[" + str(index) + "]"
    a = a + " = " + str(value) + ""
    exec(compile(a, 'setFromIndex', 'exec'))
    return L
def toTheLeft(L, indexes):
    indexes = "".join([str(x) for x in indexes])

    binary = int(indexes, 2)
    binary -= 1
    binary = bin(binary)
    binary = "0" * (4-len(binary[2:])) + binary[2:]
    indexes = [int(x) for x in list(binary)]
    for i in range(len(indexes)):
        if type(getFromIndexList(L, indexes[0:i+1])) == int:
            indexes = indexes[0:i+1]
            break
    if type(getFromIndexList(L, indexes)) != int:
        indexes.append(1)
    return indexes

def toTheRight(L, indexes):
    indexes = "".join([str(x) for x in indexes])
    
    binary = int(indexes, 2)
    binary += 1
    binary = bin(binary)[2:]
    
    nb = ""
    for i in range(0, len(indexes) - len(binary)):
        nb = nb + "0"
    binary = nb + binary
    indexes = [int(x) for x in list(binary)]
    
    for i in range(len(indexes)):
        if type(getFromIndexList(L, indexes[0:i+1])) == int:
            indexes = indexes[0:i+1]
            break
    if type(getFromIndexList(L, indexes)) != int:
        indexes.append(0)
    return indexes

def explode(L, indexes):
    pairToExplode = getFromIndexList(L, indexes)

    L = setFromIndexList(L, indexes, 0)
    if not sum(indexes) == 0:
        left = toTheLeft(L, indexes)
        L = setFromIndexList(L, left, getFromIndexList(L, left) + pairToExplode[0])
    if not sum(indexes) == len(indexes):
        right = toTheRight(L, indexes)
        L = setFromIndexList(L, right, getFromIndexList(L, right) + pairToExplode[1])
    return {"array": L}

def split(L, indexes):
    numToSplit = getFromIndexList(L, indexes)
    L = setFromIndexList(L, indexes, [floor(numToSplit/2), ceil(numToSplit/2)])
    return L

def reduceAction(a, count):
    changed = False
    if depth(a) > 4:
        changed = True
        arrToExplode = getArrToExplode(a, [])
        exploded = explode(a, arrToExplode["indexes"])
        a = exploded["array"]
    else:
        indexesList = []
        for i in range(16):
            indexesList.append([int(x) for x in list(bin(i)[2:])])
            indexesList[i] = [0] * (4-len(indexesList[i])) + indexesList[i]
        checked = []
        for indexes in indexesList:
            for i in range(len(indexes)):
                if type(getFromIndexList(a, indexes[0:i+1])) == int:
                    indexes = indexes[0:i+1]
                    break
            if not indexes in checked:
                if getFromIndexList(a, indexes) >= 10:
                    changed = True
                    a = split(a, indexes)
                    break
                checked.append(indexes)
    return {"changed": changed, "array": a}

def sumSnails(arr):
    answer = arr[0]
    for element in arr[1:]:
        answer = add(answer, element)
    return answer
count = 0
def reduce(a):
    global count
    count = 0
    beingReduced = True
    while beingReduced:
        arr = reduceAction(a, 0)
        beingReduced = arr["changed"]
        a = arr["array"]
    return a
check = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""".split("\n")
#check = data
check = [eval(x) for x in check]

largestMag = 0
for (x, y) in permutations(check, 2):
        a = deepcopy(x)
        b = deepcopy(y)
        if a != b:
            m = mag(add(a, b))
            if m > largestMag:
                largestMag = m
print(largestMag)

