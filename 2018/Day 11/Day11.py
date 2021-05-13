serial_number = 18  
width = 300
height = 300
grid = [[0 for x in range(1, width + 2)] for y in range(1, height + 2)]
def getPowerLevel(rack_ID, y):
    power_level = rack_ID * y
    power_level += serial_number
    power_level *= rack_ID
    if power_level > 99:
        power_level = int(str(power_level)[-3])
    else:
        power_level = 0
    power_level -= 5
    return power_level
for x in range(1, 301):
    for y in range(1, 301):
        grid[x][y] = []
        grid[x][y].append(x + 10)
        grid[x][y].append(getPowerLevel(grid[x][y][0], y))
open(r"G:\My Drive\School Work\Advent of Code\2018\Day 11\output.txt", "w").write("\n".join(["".joingrid[x][y][1] for x in range(1, 301) for y in range(1, 301)]))
best_total = 0
best_total_pos = 0
best_total_siz = 0
for x in range(1, width - 1):
    print (x)
    for y in range(1, height - 1):
        print (y)
        for size in range(1, width + 1 - max([x, y])):
            total_power = sum([grid[x + i][y + j][1] for i in range(0, size) for j in range(0, size)])
            if total_power > best_total:
                best_total = total_power
                best_total_pos = [x, y]
                best_total_siz = size

print (best_total_pos)
print (best_total_siz)
