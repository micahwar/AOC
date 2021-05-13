import math
from collections import OrderedDict
data = """....#.....#.#...##..........#.......#......
.....#...####..##...#......#.........#.....
.#.#...#..........#.....#.##.......#...#..#
.#..#...........#..#..#.#.......####.....#.
##..#.................#...#..........##.##.
#..##.#...#.....##.#..#...#..#..#....#....#
##...#.............#.#..........#...#.....#
#.#..##.#.#..#.#...#.....#.#.............#.
...#..##....#........#.....................
##....###..#.#.......#...#..........#..#..#
....#.#....##...###......#......#...#......
.........#.#.....#..#........#..#..##..#...
....##...#..##...#.....##.#..#....#........
............#....######......##......#...#.
#...........##...#.#......#....#....#......
......#.....#.#....#...##.###.....#...#.#..
..#.....##..........#..........#...........
..#.#..#......#......#.....#...##.......##.
.#..#....##......#.............#...........
..##.#.....#.........#....###.........#..#.
...#....#...#.#.......#...#.#.....#........
...####........#...#....#....#........##..#
.#...........#.................#...#...#..#
#................#......#..#...........#..#
..#.#.......#...........#.#......#.........
....#............#.............#.####.#.#..
.....##....#..#...........###........#...#.
.#.....#...#.#...#..#..........#..#.#......
.#.##...#........#..#...##...#...#...#.#.#.
#.......#...#...###..#....#..#...#.........
.....#...##...#.###.#...##..........##.###.
..#.....#.##..#.....#..#.....#....#....#..#
.....#.....#..............####.#.........#.
..#..#.#..#.....#..........#..#....#....#..
#.....#.#......##.....#...#...#.......#.#..
..##.##...........#..........#.............
...#..##....#...##..##......#........#....#
.....#..........##.#.##..#....##..#........
.#...#...#......#..#.##.....#...#.....##...
...##.#....#...........####.#....#.#....#..
...#....#.#..#.........#.......#..#...##...
...##..............#......#................
........................#....##..#........#""".split("\n")
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
    countSlopes = []
    for collisionAsteroid in asteroids:
        if not collisionAsteroid == asteroid:
            xdiff = (asteroid[0] - collisionAsteroid[0])
            ydiff = (asteroid[1] - collisionAsteroid[1])

            if xdiff > 0 and ydiff > 0:
                bearing = 360 - math.atan(xdiff/abs(ydiff))
            elif xdiff > 0 and ydiff < 0:
                bearing = 180 + math.atan(xdiff/ydiff)
            elif xdiff < 0 and ydiff > 0:
                bearing = math.atan(abs(xdiff) / abs(ydiff))
            elif xdiff < 0 and ydiff < 0:
                bearing = 360 - (180 + math.atan(abs(xdiff) / ydiff))
            elif ydiff == 0 and xdiff < 0:
                bearing = 90
            elif ydiff == 0 and xdiff > 0:
                bearing = 270
            elif xdiff == 0 and ydiff < 0:
                bearing = 180
            elif xdiff == 0 and ydiff > 0:
                bearing = 0

            if not bearing in countSlopes:
                countSlopes.append(bearing)

            
    counts[asteroid] = len(countSlopes)
#print(counts)
for count in counts:
    data[count[1]][count[0]] = counts[count]
#for x in data:
    #print(x)
counts = sorted(counts.items(), key=lambda x: x[1])
chosenAsteroid = counts[-1]
print(chosenAsteroid)
asteroid = chosenAsteroid[0]
linesOfSight = {}
for collisionAsteroid in asteroids:
        if not collisionAsteroid == asteroid:
            xdiff = (asteroid[0] - collisionAsteroid[0])
            ydiff = (asteroid[1] - collisionAsteroid[1])

            if xdiff > 0 and ydiff > 0:
                bearing = 360 - math.atan(xdiff/abs(ydiff))
            elif xdiff > 0 and ydiff < 0:
                bearing = 180 + math.atan(xdiff/ydiff)
            elif xdiff < 0 and ydiff > 0:
                bearing = math.atan(abs(xdiff) / abs(ydiff))
            elif xdiff < 0 and ydiff < 0:
                bearing = 360 - (180 + math.atan(abs(xdiff) / ydiff))
            elif ydiff == 0 and xdiff < 0:
                bearing = 90
            elif ydiff == 0 and xdiff > 0:
                bearing = 270
            elif xdiff == 0 and ydiff < 0:
                bearing = 180
            elif xdiff == 0 and ydiff > 0:
                bearing = 0

            dist = math.sqrt(abs(xdiff)**2 + abs(ydiff)**2)
            if bearing in linesOfSight:
                linesOfSight[bearing].append([dist, collisionAsteroid])
            else:
                linesOfSight[bearing] = [[dist, collisionAsteroid]]
print(linesOfSight)
linesOfSight = dict(OrderedDict(sorted(linesOfSight.items())))            

for element in linesOfSight:
    linesOfSight[element] = sorted(linesOfSight[element], key=lambda x: x[0])
count = 0
numDestroyed = 0
running = True
while running:
    
    for i, element in enumerate(linesOfSight):
        if len(linesOfSight[element]) > count:
                numDestroyed += 1
                if numDestroyed == 200:
                    running = False
                    print(element, ": ", linesOfSight[element])
                    print(linesOfSight[element][0][1][0]*100 + linesOfSight[element][0][1][1])
                    break
    count += 1
    



