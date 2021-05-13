def part1(data):
    pos = {"x": 0, "y": 0}
    direction = 0
    for line in data:
        if line[0] == "N":
            pos["y"] += line[1]
        elif line[0] == "E":
            pos["x"] += line[1]
        elif line[0] == "S":
            pos["y"] -= line[1]
        elif line[0] == "W":
            pos["x"] -= line[1]
        elif line[0] == "R":
            direction += line[1]
            direction = direction % 360
        elif line[0] == "L":
            direction -= line[1]
            direction = direction % 360
        elif line[0] == "F":
            if direction == 0:
                pos["x"] += line[1]
            elif direction == 90:
                pos["y"] -= line[1]
            elif direction == 180:
                pos["x"] -= line[1]
            elif direction == 270:
                pos["y"] += line[1]
    return abs(pos["x"] + abs(pos["y"]))
def part2(data):
    pos = {"x": 0, "y": 0}
    waypoint = [1, 10, 0, 0]
    for line in data:
        if line[0] == "N":
            waypoint[0] += line[1] - waypoint[2]
            waypoint[2] = 0
        elif line[0] == "E":
            waypoint[1] += line[1] - waypoint[3]
            waypoint[3] = 0
        elif line[0] == "S":
            waypoint[2] += line[1]  - waypoint[0]
            waypoint[0] = 0
        elif line[0] == "W":
            waypoint[3] += line[1] - waypoint[1]
            waypoint[1] = 0
        elif line[0] == "R":
            for x in range(line[1]//90):
                copy = [c for c in waypoint]
                waypoint =  [copy[-1]] + copy[:-1]
        elif line[0] == "L":
            for x in range(line[1]//90):
                copy = [c for c in waypoint]
                waypoint = copy[1:] + [copy[0]]
        elif line[0] == "F":
           for x in range(line[1]):
               pos["x"] += waypoint[1] - waypoint[3]
               pos["y"] += waypoint[0] - waypoint[2]
        if waypoint[0] < 0:
            waypoint[2] -= waypoint[0]
            waypoint[0] = 0
        elif waypoint[2] < 0:
            waypoint[0] -= waypoint[2]
            waypoint[2] = 0
        elif waypoint[1] < 0:
            waypoint[3] -= waypoint[1]
            waypoint[1] = 0
        elif waypoint[3] < 0:
            waypoint[1] -= waypoint[3]
            waypoint[3] = 0
    print(pos)
    return abs(pos["x"] + abs(pos["y"]))

def main(inputdata = "input/input12.txt"):
    with open(inputdata, "r") as f:
        data = f.read().split("\n")
#     data = """F10
# N3
# F7
# R90
# F11""".split("\n")
    data = [[x[0], int(x[1:])] for x in data]
    print(data)
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()