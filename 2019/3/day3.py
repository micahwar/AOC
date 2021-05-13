with open("input.txt", "r") as f:
    data = f.read().split("\n")
left = data[0].split(",")
right = data[1].split(",")

#left = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(",")

#right = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")
grid = [[0 for x in range(10000)] for y in range(10000)]
x = 0
y = 0
c = 1
for val in left:
    direction = val[0]
    mag = int(val[1:])

    for i in range(mag):
        if grid[x][y] == 0:
            grid[x][y] = c
        if direction == "U":
            y -= 1
        elif direction == "L":
            x -= 1
        elif direction == "R":
            x += 1
        elif direction == "D":
            y += 1
        c+=1
        
print("done")       
intersections = []
x = 0
y = 0
c = 1
for val in right:
    direction = val[0]
    mag = int(val[1:])
    
    for i in range(mag):
        if grid[x][y] > 0 and not(x == 0 and y == 0):
            intersections.append([[x,y], c+grid[x][y]])
        if direction == "U":
            y -= 1
        elif direction == "L":
            x -= 1
        elif direction == "R":
            x += 1
        elif direction == "D":
            y += 1
        c+=1
intersections = list(reversed(sorted(intersections, key=lambda thing: thing[1])))
print(intersections[0])
