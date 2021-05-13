with open("input.txt", "r") as f:
    moons = [dict([[int(z) if i == 1 else z for i, z in enumerate(y.strip().split("="))] for y in x[1:-1].split(",")]) for x in f.read().split("\n")[:-1]]
#data = """<x=-8, y=-10, z=0>
#<x=5, y=5, z=10>
#<x=2, y=-7, z=3>
#<x=9, y=-8, z=-3>"""
#moons = [dict([[int(z) if i == 1 else z for i, z in enumerate(y.strip().split("="))] for y in x[1:-1].split(",")]) for x in data.split("\n")]
print(moons)
moonVels = [{'x':0, 'y':0, 'z':0} for x in range(len(moons))]
print(moonVels)
for step in range(1000):
    for i, moon in enumerate(moons):
        for j in range(i, len(moons)):
            compMoon = moons[j]
            if not i == j:
                if moons[i]['x'] < moons[j]['x']:
                    moonVels[i]['x'] += 1
                    
                    moonVels[j]['x'] += -1
                    
                elif moons[i]['x'] > moons[j]['x']:
                    moonVels[i]['x'] += -1
                    moonVels[j]['x'] += 1
                
                if moons[i]['y'] < moons[j]['y']:
                    moonVels[i]['y'] += 1
                    moonVels[j]['y'] += -1
                elif moons[i]['y'] > moons[j]['y']:
                    moonVels[i]['y'] += -1
                    moonVels[j]['y'] += 1

                if moons[i]['z'] < moons[j]['z']:
                    moonVels[i]['z'] += 1
                    moonVels[j]['z'] += -1
                elif moons[i]['z'] > moons[j]['z']:
                    moonVels[i]['z'] += -1
                    moonVels[j]['z'] += 1
    for i, x in enumerate(moonVels):
        moons[i]['x'] += x['x']
        moons[i]['y'] += x['y']
        moons[i]['z'] += x['z']
    
    
for x in range(len(moons)):
    print("pos=", moons[x], ", ", "vel=", moonVels[x])
energy = [0 for x in range(len(moons))]
for x in range(len(moons)):
    energy[x] = sum([abs(y) for y in moons[x].values()]) * sum([abs(y) for y in moonVels[x].values()])
print(sum(energy))
