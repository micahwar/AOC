def calculate(expression, ops):
    lbc = 0
    lbp = -1
    rbc = 0
    if not expression[0].isnumeric():
        expression = "0+" + expression
    for n in range(1, len(expression)):
        letter = expression[n]
        if letter == "(":
            lbc += 1
            if lbc == 1:
                lbp = n
        elif letter == ")":
            rbc += 1
        if lbc == 0 and letter.isnumeric():
            ops.append([int(letter), expression[n-1]])
            n += 1
        elif lbc >= 1 and lbc == rbc:
            lbc = 0
            rbc = 0
            if expression[lbp+1:n][0].isnumeric():
                ops.append([calculate(expression[lbp+1:n], [expression[lbp+1:n][0]]), expression[lbp-1]])
            else:
                ops.append([calculate(expression[lbp+1:n], [0]), expression[lbp-1]])
    t = int(ops[0])
    for i in range(1, len(ops)):
        if ops[i][1] == "+":
            t += int(ops[i][0])
        elif ops[i][1] == "*":
            t *= int(ops[i][0])
    return t

def calculatep2(expression, ops):
    lbc = 0
    lbp = -1
    rbc = 0
    if not expression[0].isnumeric():
        expression = "0+" + expression
    for n in range(1, len(expression)):
        letter = expression[n]
        if letter == "(":
            lbc += 1
            if lbc == 1:
                lbp = n
        elif letter == ")":
            rbc += 1
        if lbc == 0 and letter.isnumeric():
            ops.append([int(letter), expression[n-1]])
            n += 1
        elif lbc >= 1 and lbc == rbc:
            lbc = 0
            rbc = 0
            if expression[lbp+1:n][0].isnumeric():
                ops.append([calculatep2(expression[lbp+1:n], [expression[lbp+1:n][0]]), expression[lbp-1]])
            else:
                ops.append([calculatep2(expression[lbp+1:n], [0]), expression[lbp-1]])
    print(ops)
    running = True
    while running:
        hasBroken = False
        for n, op in enumerate(ops):
            if isinstance(op, list) and op[1] == "+":
                if isinstance(ops[n-1], list):
                    
                    ops[n-1][0] += op[0]
                else:
                    ops[n-1] = int(ops[n-1]) + op[0]
                del ops[n]
                hasBroken = True
                break
        if not hasBroken:
            running = False

    print(ops)
    t = int(ops[0])
    for i in range(1, len(ops)):
        if ops[i][1] == "+":
            t += int(ops[i][0])
        elif ops[i][1] == "*":
            t *= int(ops[i][0])
    return t

    

def part1(data):
    s = 0
    for line in data:
        if line[0].isnumeric():
            s += calculate(line, [int(line[0])])
        else:
            s += calculate(line, [0])
    return s

def part2(data):
    s = 0
    for line in data:
        if line[0].isnumeric():
            s += calculatep2(line, [int(line[0])])
        else:
            s += calculatep2(line, [0])
    return s

def main(inputdata = "input/input18.txt"):
    with open(inputdata, "r") as f:
        data = [x.replace(" ", "") for x in f.read().split("\n")]
    #data = "5 + (8 * 3 + 9 + 3 * 4 * 3)".replace(" ", "")
    print(data)
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()