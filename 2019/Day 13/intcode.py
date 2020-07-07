class Machine:
    def __init__(self, mem):
        self.mem = mem  # Memory of the machine.
        self.pc = 0  # Program Counter
        self.output = None
        self.input = []
        self.base = 0  # Relative base (used for relative addressing)
        self.halted = False

    def isHalted(self):
        return self.halted

    def idx(self, pos):
        """
        Calculates the addressing mode for the
        parameter and returns the index (idx)
        of its resultant value
        """
        adm = (self.mem[self.pc] // (10*10**pos)) % 10

        if adm == 0:
            return self.mem[self.pc + pos]
        elif adm == 1:
            return self.pc + pos
        elif adm == 2:
            return self.mem[self.pc + pos] + self.base

    def val(self, pos):
        """
        Calls idx() with a position of a paramater
        and returns the value at the returned index.
        """
        return self.mem[self.idx(pos)]

    def run(self, inp=None):
        """
        Opcodes:
        1 - SUM: a+b -> c
        2 - PROD: a*b -> c
        3 - INPUT: a -> self.input
        4 - OUTPUT: a -> self.output, print(self.output)
        5 - JIT: pc = b if a != 0
        6 - JIF: pc = b if a == 0
        7 - LESS: c = 1 if a < b
        8 - EQUAL: c = 1 if a == b
        9 - ADJUST BASE: self.base += a
        """

        self.input = inp
        # print("INPUTS:", self.input)

        while True:
            # Keep PC within scope of memory.
            self.pc %= len(self.mem)

            # Calculate opcode for data at current address.
            op = self.mem[self.pc] % 100

            # Halt machine if opcode==99
            if op == 99:
                self.halted = True
                break

            if op == 1:  # SUM
                a = self.val(1)
                b = self.val(2)
                c = self.idx(3)

                self.mem[c] = a + b
                self.pc += 4
            elif op == 2:  # PROD
                a = self.val(1)
                b = self.val(2)
                c = self.idx(3)

                self.mem[c] = a * b
                self.pc += 4
            elif op == 3:  # INPUT
                a = self.idx(1)
                # print(f"Input before: {self.mem[a]}")
                self.mem[a] = self.input.pop(0)
                # print(f"Input after: {self.mem[a]}")
                self.pc += 2
            elif op == 4:  # OUTPUT
                a = self.val(1)
                self.output = a
                self.pc += 2
                # print("OUTPUT:", self.output)
                return self.output
            elif op == 5:  # JIT
                a = self.val(1)
                b = self.val(2)

                self.pc = b if a != 0 else self.pc + 3
            elif op == 6:  # JIF
                a = self.val(1)
                b = self.val(2)

                self.pc = b if a == 0 else self.pc + 3
            elif op == 7:  # LESS
                a = self.val(1)
                b = self.val(2)
                c = self.idx(3)

                self.mem[c] = 1 if a < b else 0

                self.pc += 4
            elif op == 8:  # EQUAL
                a = self.val(1)
                b = self.val(2)
                c = self.idx(3)

                self.mem[c] = 1 if a == b else 0

                self.pc += 4
            elif op == 9:  # ADJUST BASE
                a = self.val(1)

                self.base += a

                self.pc += 2
            else:
                print("Error:", self.pc, self.mem[self.pc: self.pc+4])
