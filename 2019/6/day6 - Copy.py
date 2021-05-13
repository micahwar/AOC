with open("input.txt", "r") as f:
    data = f.read().split("\n")

def getOrbits(planet, c):
    hasSomething = False
    for x in orbits:
        if x[0] == planet:
            hasSomething = True
            c.append(x[1])
            return getOrbits(x[1], c)
    if hasSomething == False:
        return c
    
orbits = [list(reversed(x.split(")"))) for x in data]
planets = []
for orbit in orbits:
    planets.append(orbit[0])
    planets.append(orbit[1])
planets = sorted(set(planets))
print(planets)

you = (getOrbits("YOU", []))
san = (getOrbits("SAN", []))
print(you)
print(san)
both = [x for x in you if x in san]
print(both)
total = (len(you) - len(both))
for x in san:
    if not x in both:
        total += 1
    else:
        break
print(total)
