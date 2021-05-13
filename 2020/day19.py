import itertools
def isList(obj):
    return not any([isinstance(obj[i], list) for i in range(len(obj))])
def getRule(rules, rule):
    possible = rule.split(" | ")
    if len(possible) > 1:
        possibilities = []
        for p in possible:
            possibilities.append(getRule(rules, p))
        return possibilities
    elif rule.find("\"") > -1:
        return rule.replace("\"", "")
    else:
        vals = [getRule(rules, x) for x in rule.split(" ")]
        values = vals[0]
        for x in range(1, len(vals)):
            if not isinstance(values, list):
                values = [values]
            if not isinstance(vals[x], list):
                vals[x] = [vals[x]]
            values = itertools.product(values, vals[x])
        print(values)
        input()
        return values
def part1(rules, messages):
    for rule in rules:
        rules[rule] = getRule(rules, rules[rule]) 
    match = rules["0"]
    print(match)
    
def part2(data):
    return 0

def main(inputdata = "input/input19.txt"):
    with open(inputdata, "r") as f:
        data = f.read().split("\n")
    data = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb""".split("\n\n")
    ndata = [x.split(": ") for x in data[0].split("\n")]
    rules = {}
    for y in ndata:
        rules[y[0]] = y[1].strip()
    print(rules)
    messages = data[1].split("\n")
    data = [rules, messages]
    print(part1(data[0], data[1]))
    print(part2(data))


if __name__ == "__main__":
    main()