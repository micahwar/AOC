class intcode:
    
    def __init__(self, data, inputs):
        self.program = data
        self.inputs = inputs
        self.relativeBase = 0
        self.index = 0
        self.running = True
        self.finished = False

    def returnIndexes(mode, numParameters):
        self.returnVals = []
        for x in range(3):
            if mode[2-x] == 0:
                val = self.program[self.index+x+1]
            elif mode[2-x] == 1:
                val = self.index+x+1
            elif mode[2-x] == 2:
                val = self.program[self.index+x+1]+self.relativeBase
            self.returnVals.append(val)
        return returnVals[:numParameters]
    
    def instructionOne(mode):
        vals = returnIndexes(mode, 3)
        self.program[vals[2]] = self.program[vals[0]] + self.program[vals[1]]
        self.index += 4

    def instructionTwo(mode):
        vals = returnIndexes(mode, 3)
        self.program[vals[2]] = self.program[vals[0]] * self.program[vals[1]]
        self.index += 4

    def instructionThree(mode):
        vals = returnIndexes(mode, 1)
        self.program[vals[0]] = self.inputs[0]
        del self.inputs[0]
        self.index += 2
        
    def instructionFour(mode):
        vals = returnIndexes(mode, 1)
        self.running = False
        self.index += 2
        return (self.program[vals[0]])
        
        
    def instructionFive(mode):
        vals = returnIndexes(mode, 2)        
        if self.program[vals[0]] != 0:
            self.index = self.program[vals[1]]
        else:
            self.index += 3
        
    def instructionSix(mode):
        vals = returnIndexes(mode, 2)        
        if self.program[vals[0]] == 0:
            self.index = self.program[vals[1]]
        else:
            self.index += 3
        
    def instructionSeven(mode):
        vals = returnIndexes(mode, 3)
        if self.program[vals[0]] < self.program[vals[1]]:
            self.program[vals[2]] = 1
        else:
            self.program[vals[2]] = 0
        self.index += 4
        
    def instructionEight(mode):
        vals = returnIndexes(mode, 3)
        if self.program[vals[0]] == self.program[vals[1]]:
            self.program[vals[2]] = 1
        else:
             self.program[vals[2]] = 0
        self.index += 4
        
    def instructionNine(mode):
        vals = returnIndexes(mode, 1)
        self.relativeBase += self.program[vals[0]]
        self.index += 2
        
    def run():
        while self.running:
            parameter = self.program[self.index]
            opcode = int(str(self.program[self.index])[-2:])
            mode = [int(x) for x in list(str(self.program[self.index])[:-2])]
            
            while len(mode) < 3:
                mode = [0] + mode
            if opcode == 1:
                instructionOne(mode)
            elif opcode == 2:
                instructionTwo(mode)
            elif opcode == 3:
                instructionThree(mode)
            elif opcode == 4:
                return instructionFour(mode)
            elif opcode == 5:
                instructionFive(mode)
            elif opcode == 6:
                instructionSix(mode)
            elif opcode == 7:
                instructionSeven(mode)
            elif opcode == 8:
                instructionEight(mode)
            elif opcode == 9:
                instructionNine(mode)
            if self.program[self.index] == 99:
                self.running = False
                self.finished = True
