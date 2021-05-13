with open("input", "r") as f:
    lines = f.read().split("\n")
state = lines[0].split()[3][0]
checksumSteps = int(lines[1].split()[5])
del lines[0:3]
tape = ["0"]
mousePos = 0
func = ""
states = {
    'A':[None, None],
    'B':[None, None,],
    'C':[None, None],
    'D':[None, None],
    'E':[None, None],
    'F':[None, None]
    }
def createFunction(MousePos, SetupWrite, SetupMove, SetupContinue):
    func = "["
    func += "\"tape[" + str(MousePos) + "]=\\\"" + str(SetupWrite) + "\\\"\","
    if SetupMove == "right":
        func += "\"tape.append(\\\"0\\\")\",\"mousePos+=1\", "
    elif SetupMove == "left":
        func += "\"tape.insert(0, \\\"0\\\")\", "
    func += "\"state=\\\"" + SetupContinue + "\\\"\"]"
    return func
for line in lines:
    if "In state" in line:
        setupState = line.split()[2][0]
    elif "current value is 0" in line:
        setupVal = int(line.split()[5][0])
    elif "current value is 1" in line:
        states[setupState][setupVal] = createFunction(mousePos, setupWrite, setupMove, setupContinue)
        setupVal = int(line.split()[5][0])
    elif "Write" in line:
        setupWrite = line.split()[4][:-1]
    elif "Move" in line:
        setupMove = line.split()[6][:-1]
    elif "Continue" in line:
        setupContinue = line.split()[4][:-1]
    elif line == "":
        states[setupState][setupVal] = createFunction(mousePos, setupWrite, setupMove, setupContinue)
arr = []
for i in xrange(checksumSteps):
    if i % 100000 == 0:
        print i
    arr = eval(states[state][int(tape[mousePos])])
    for i in arr:
        exec (i)
    
print "".join(tape).count("1")
