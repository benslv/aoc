def sig_AND(w1, w2):
    return w1.getSignal() & w2.getSignal()


def sig_OR(w1, w2):
    return w1.getSignal() | w2.getSignal()


def sig_LSHIFT(w1, y):
    return w1.getSignal() << y


def sig_RSHIFT(w1, y):
    return w1.getSignal() >> y


def sig_NOT(w1):
    return ~w1.getSignal()


with open("7.in", "r") as f:
    lines = f.readlines()

commands = ["AND", "NOT", "OR", "LSHIFT", "RSHIFT"]

wires = {}

"""
Thinking:
- Store wire names as keys, signal as value in dict.
- Search line for command word.
- If we find one, we can parse it differently depending on what the command is.
    - Split on space and index different parts for line names and command etc.
- Create entry in dictionary for new wire name, with signal as value
"""
