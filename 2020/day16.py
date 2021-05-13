part2Tickets = []
def part1(tickets, rules):
    global part2Tickets
    invalid = []
    for ticket in tickets:
        ticketValid = True
        for value in ticket:
            isValid = False
            for rule in rules:
                for subRule in rule:
                    if (value >= subRule[0] and value <= subRule[1]):
                        isValid = True
            if not isValid:
                ticketValid = False 
                invalid.append(value)
        if ticketValid:
            part2Tickets.append(ticket)
    return sum(invalid)

def part2(tickets, rules, myTicket):
    positions = [[] for x in range(len(tickets[0]))]
    for x in range(len(tickets[0])):
        for ticket in tickets:
            positions[x].append(ticket[x])
    positionRules = []
    for position in positions:
        validRules = [x for x in rules]
        for value in position:
            for rule in rules:
                isValid = False
                for subRule in rules[rule]:
                    if (value >= subRule[0] and value <= subRule[1]):
                        isValid = True
                if not isValid:
                    if rule in validRules:
                        validRules.remove(rule)
        positionRules.append(validRules)
    sortedRules = sorted(positionRules, key=lambda x: len(x))
    for x in sortedRules:
        for n, y in enumerate(positionRules):
            if y != x and x[0] in y and x[0] in sortedRules[sortedRules.index(y)]:
                positionRules[n].remove(x[0])
    total = 1
    print(positionRules)
    for n, x in enumerate(positionRules):
        
        if "departure" in x[0]:
            print(x)
            total *= int(myTicket[n])
    return total

def main(inputdata = "input/input16.txt"):
    with open(inputdata, "r") as f:
        data = f.read().split("\n\n")
    rules = [[[int(z) for z in y.split("-")] for y in x.split(" ")[1:] if y != "or" and not ":" in y] for x in data[0].split("\n")]
    tickets = [[int(y) for y in x.split(",")] for x in data[2].split("\n")[1:]]
    myTicket = data[1].split("\n")[1].split(",")
    print(part1(tickets, rules))
    rules = [[x.split(":")[0]]+[[int(z) for z in y.split("-")] for y in x.split(" ")[1:] if y != "or" and not ":" in y] for x in data[0].split("\n")]
    newRules = {}
    for x in rules:
        newRules[x[0]] = x[1:]
    print(part2(part2Tickets, newRules, myTicket))


if __name__ == "__main__":
    main()