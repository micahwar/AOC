from collections import defaultdict
import time
now = time.time()
steps = 12861455
states = {
    'A': ((1,  1, 'B'), (0, -1, 'B')),
    'B': ((1, -1, 'C'), (0,  1, 'E')),
    'C': ((1,  1, 'E'), (0, -1, 'D')),
    'D': ((1, -1, 'A'), (1, -1, 'A')),
    'E': ((0,  1, 'A'), (0,  1, 'F')),
    'F': ((1,  1, 'E'), (1,  1, 'A')),
}
tape = defaultdict(int)
position = 0
state = 'A'
for i in range(0, steps):
    currState = states[state][tape[position]]
    tape[position] = currState[0]
    position += currState[1]
    state = currState[2]
print (sum(tape.values()))
print (time.time() - now)
