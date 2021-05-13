with open("input6.txt", "r") as f:
    data = f.read().split("\n")

def getOrbits(planet, c):
    hasSomething = False
    for x in orbits:
        if x[0] == planet:
            hasSomething = True
            c += 1
            return getOrbits(x[1], c)
    if hasSomething == False:
        return c
    
orbits = [list(reversed(x.split(")"))) for x in data]
planets = []
for orbit in orbits:
    planets.append(orbit[0])
    planets.append(orbit[1])
planets = sorted(set(planets))

total = 0
for planet in planets:
    total += getOrbits(planet, 0)


print(total)
