import time
data = open(r"G:\My Drive\School Work\Advent of Code\2018\Day 8\input.txt", "r").read().split()
#data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split()
def get_metadata(index):
    num_child_nodes = int(data[index])
    index          += 1
    num_metad_entry = int(data[index])
    total_meta      = 0
    index          += 1
    children = [None for x in range(0, num_child_nodes)]
    if num_child_nodes != 0:
        for i in range(0, num_child_nodes):
            children[i] = get_metadata(index)
            total_meta += children[i][0]
            index       = children[i][1]
    for i in range(0, num_metad_entry):
        total_meta += int(data[index])
        index += 1
    return [total_meta, index]
now = time.time()
print(str(get_metadata(0)[0]) + " : " + str(time.time() - now))