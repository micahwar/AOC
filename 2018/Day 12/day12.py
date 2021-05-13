initial_state = "....##.##..#.#....#.##...###.##.#.#..###.#....##.###.#..###...#.##.#...#.#####.###.##..#######.####..#...."
index_zero = 4
keys = []
for x in open(r"G:\My Drive\School Work\Advent of Code\2018\Day 12\input.txt").read().split("\n"):
    keys.append([y.strip() for y in x.split("=>")])
newState = ""

for j in range(1, 1000000):
    newState = ""
    for i, char in enumerate(initial_state):
        if i > 1 and i < len(initial_state) - 2 :
            if initial_state[i - 2:i+3] in [x[0] for x in keys]:
                newState += keys[[x[0] for x in keys].index(initial_state[i - 2:i+3])][1]
            else:
                newState += "."
        else:
            newState += "."
    initial_state = newState
    if initial_state.index('#') < 4:
        initial_state = '....' + initial_state
        index_zero += 4
    if initial_state.count('#', len(initial_state) - 5) != 0:
        initial_state =  initial_stat   e + '....'
answer = 0
for i, char in enumerate(initial_state):
    if char == "#":
        answer += i - index_zero
print(answer)
print (initial_state)