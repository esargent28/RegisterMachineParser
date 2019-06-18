# =========================================================================== #
#                                                                             #
#                Erik Sargent --- Register Machine Simulator                  #
#                                                                             #
# =========================================================================== #

# --- begin class RegisterMachineState ---

class RegisterMachineState:

    def __init__(self, isIncr, r, k, l=-1):
        self.isIncr = isIncr
        self.register = r
        self.state1 = k
        self.state2 = l

    def isIncrement(self):
        return self.isIncr

    def getRegister(self):
        return self.register
    
    def getGotoStates(self):
        if (self.isIncrement()):
            return [self.state1]
        else:
            return [self.state1, self.state2]

# --- end class RegisterMachineState ---

# --- begin class RegisterMachine ---

class RegisterMachine:

    def __init__(self, filepath):
        # Initialize registers & states
        self.registers = []
        self.states = []

        # Read instructions & config for register machine from input file
        file = open(filepath)
        s = file.readline()
        readingStates = False
        while (s):
            if (readingStates):
                if (s.startswith("#END STATES")):
                    readingStates = False
                else:
                    splits = [int(i) for i in s.split(' ')[1:]]
                    isIncr = s.startswith("inc")
                    isDecr = s.startswith("dec")
                    endBound = 2 if isIncr else 3
                    # Only add in new state if instruction starts with 'inc' or 'dec'
                    if (isIncr or isDecr):
                        self.states += [RegisterMachineState(isIncr, *(splits[0:endBound]))]
            else:
                if s.startswith("#INPUT"):
                    self.inputRegisters = [int(i) for i in s.split(' ')[1:]]
                elif s.startswith("#OUTPUT"):
                    self.outputRegisters = [int(i) for i in s.split(' ')[1:]]
                elif s.startswith("#REGISTERS"):
                    numRegisters = int(s.split(' ')[-1])
                    self.registers = [0] * numRegisters
                elif s.startswith("#BEGIN STATES"):
                    readingStates = True
            s = file.readline()
        file.close()
        self.stateIndex = 0

    # Resets register machine to initial state.
    def reset(self):
        self.stateIndex = 0
        for i in range(len(self.registers)):
            self.registers[i] = 0

    # Returns number of registers.
    def getNumRegisters(self):
        return len(self.registers)

    # Returns number of states.
    def getNumStates(self):
        return len(self.states)

    # Returns list of input registers.
    def getInputRegisterIndexes(self):
        return self.inputRegisters

    # Returns list of output registers.
    def getOutputRegisterIndexes(self):
        return self.outputRegisters

    # Increments register r by 1 and goes to state k.
    def incr(self, r, k):
        assert(0 <= r and r < self.getNumRegisters())
        assert(0 <= k and k <= self.getNumStates())
        self.registers[r] += 1
        self.stateIndex = k

    # If register r has value > 0, decrements it by 1 and goes to state k. Otherwise, goes to state l.
    def decr(self, r, k, l):
        assert(0 <= r and r < self.getNumRegisters())
        assert(0 <= k and k <= self.getNumStates())
        assert(0 <= l and l <= self.getNumStates())
        if (self.registers[r] > 0):
            self.registers[r] -= 1
            self.stateIndex = k
        else:
            self.stateIndex = l

    # Takes one step. Returns True if the machine has halted this step and False otherwise.
    def step(self):
        if (self.stateIndex == self.getNumStates()):
            return True

        assert(0 <= self.stateIndex and self.stateIndex < self.getNumStates())
        currentState = self.states[self.stateIndex]
        if (currentState.isIncrement()):
            self.incr(currentState.getRegister(), currentState.getGotoStates()[0])
        else:
            self.decr(currentState.getRegister(), currentState.getGotoStates()[0], currentState.getGotoStates()[1])
        return False

    # Runs the register machine to completion and returns the output. May loop forever if the register
    #   machine construction does so.
    def run(self, *args):
        # Ensure that we don't have any partial computation still in one of the registers
        self.reset()
        # Initialize input registers to provided values
        assert(len(args) == len(self.getInputRegisterIndexes()))
        for i in range(0, len(args)):
            self.registers[self.getInputRegisterIndexes()[i]] = args[i]

        # Keep stepping until machine halts
        while (not self.step()): pass
        
        # Return values from all output registers
        return [self.registers[i] for i in self.getOutputRegisterIndexes()]

    # --- end class RegisterMachine ---
