class Intcode:
    def __init__(self, phase, tape):
        self.phase = phase
        self.t = tape
        self.i = 0
        self.isHalted = False
        self.output = 0
        # Incremented to keep track of how many inputs have been entered before.
        self.input_cycle = 0

    def halted(self):
        return self.isHalted

    def getOutput(self):
        return self.output

    def run(self, inp):
        while True:
            # Allows the instruction tape to loop continuously even if it reaches the end
            self.i %= len(self.t)

            # These check to see if the current op needs direct or immediate addressing
            try:
                a = self.t[self.i+1] if (self.t[self.i] //
                                         100) % 10 == 1 else self.t[self.t[self.i+1]]
            except IndexError:
                a = None
            try:
                b = self.t[self.i+2] if (self.t[self.i] //
                                         1000) % 10 == 1 else self.t[self.t[self.i+2]]
            except IndexError:
                b = None
            try:
                c = self.t[self.i+3] if (self.t[self.i] //
                                         10000) % 10 == 1 else self.t[self.t[self.i+3]]
            except IndexError:
                c = None

            # Calculates the opcode for the given instruction.
            op = self.t[self.i] % 100

            # Halt on opcode 99
            if self.t[self.i] == 99:
                self.isHalted = True
                break

            # SUM
            if op == 1:
                self.t[self.t[self.i+3]] = a + b
                self.i += 4

            # MULTIPLY
            elif op == 2:
                self.t[self.t[self.i+3]] = a * b
                self.i += 4

            # INPUT
            elif op == 3:
                # If this is the first input opcode we've come across, use the phase number as the input.
                if self.input_cycle == 0:
                    self.t[self.t[self.i+1]] = self.phase
                    self.input_cycle += 1

                # Otherwise, we use the input from the previous amplifier as the input.
                elif self.input_cycle >= 1:
                    self.t[self.t[self.i+1]] = inp
                    self.input_cycle += 1
                self.i += 2

            # OUTPUT
            # Upon encountering the output opcode, store it and pause the machine so we can pass the output as input to the next machine.
            elif op == 4:
                self.output = a
                # print("Output:", self.output)
                self.i += 2
                break

            # JUMP IF TRUE
            elif op == 5:
                self.i = b if a != 0 else self.i + 3

            # JUMP IF FALSE
            elif op == 6:
                self.i = b if a == 0 else self.i + 3

            # LESS THAN
            elif op == 7:
                self.t[self.t[self.i+3]] = 1 if a < b else 0
                self.i += 4

            # EQUAL TO
            elif op == 8:
                self.t[self.t[self.i+3]] = 1 if a == b else 0
                self.i += 4
            else:
                # We should never reach this state, so if we do then print a bunch of stuff to help me work out what went wrong.
                print("Error", self.i, self.t[self.i:self.i+4])
