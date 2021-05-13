data = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""".split("\n")
data = [[1 if letter == "#" else 0 for letter in list(line)]for line in data]
for x in data:
    print(x)
asteroids = []
for i, x in enumerate(data):
    for j, y in enumerate(x):
        if y == 1:
            asteroids.append((j, i))
counts = {}
for asteroid in asteroids:
    count = 0
    #print("\n\n\n\n")
    for collisionAsteroid in asteroids:
        
        xdiff = (asteroid[0] - collisionAsteroid[0])
        ydiff = (asteroid[1] - collisionAsteroid[1])
        
        # y = mx + c
        gradient = ydiff/xdiff if not xdiff == 0 else 0
        #y - mx = c
        c = asteroid[1] - (gradient * asteroid[0])
        #print()
        #print(asteroid, ": ", collisionAsteroid, ": ", "y = ", gradient, "x + ", c)
        
        xdiff = abs(xdiff)
        ydiff = abs(ydiff)
        valid = True
        if xdiff == 0:
            val1 = asteroid[1] if asteroid[1] < collisionAsteroid[1] else collisionAsteroid[1]
            val2 = collisionAsteroid[1] if asteroid[1] < collisionAsteroid[1] else asteroid[1]
            for y in range(val1+1, val2):
                if data[y][asteroid[0]] == 1:
                    #print("xdiff: ", asteroid, ": ", collisionAsteroid, ": ", (asteroid[0], y))
                    
                    valid = False
                    break
        val1 = asteroid[0] if asteroid[0] < collisionAsteroid[0] else collisionAsteroid[0]
        val2 = collisionAsteroid[0] if asteroid[0] < collisionAsteroid[0] else asteroid[0]
        #print(val1, ": ", val2)
        if ydiff == 0:
            
            for x in range(val1+1, val2):
                #print((x, asteroid[1]), data[asteroid[1]][x])
                if data[asteroid[1]][x] == 1:
                    #print("ydiff: ", asteroid, ": ", collisionAsteroid, ": ", (x, asteroid[1]))
                    valid = False
                    break
        if valid and xdiff != 0 and ydiff != 0:
            for x in range(val1, val2):
                collision = (x,((gradient*x)+c))
                if not collision == asteroid and collision[1] < len(data) and collision[1] == int(collision[1]) and collision[1] >= 0 and not collision == collisionAsteroid:
                    if data[int(collision[1])][x] == 1:
                        #print("line: ", asteroid, ": ", collisionAsteroid, ": ", collision)
                        valid = False
                        break
        
        if (valid or xdiff == 1 or ydiff == 1) and asteroid != collisionAsteroid:
            count += 1
    #print(count)
    counts[asteroid] = count
    if count == 4:
        asdf
print(counts)
for count in counts:
    data[count[1]][count[0]] = counts[count]
for x in data:
    print(x)
counts = sorted(counts.items(), key=lambda x: x[1])
print(counts[-1])
