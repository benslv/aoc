import fileinput

# s = "A(2x3)BC(1x2)D"  # decompresses to ABCBCBCDD with length 9

s = list(fileinput.input())[0]

part_2 = False


def decompress(s):
    if "(" not in s:
        return len(s)

    rtl = 0  # Running total length (RTL)
    while "(" in s:
        # Find index of first "(". Increases RTL by the number of normal characters preceding it.
        rtl += s.find("(")

        # Set the string to start from the first "("
        s = s[s.find("("):]

        # Work out where our marker ends, and split it into its two values.
        marker = [int(x) for x in s[1:s.find(")")].split("x")]

        # Set the string to start from after the marker.
        s = s[s.find(")")+1:]

        # Increase RTL by the repeated number of characters.
        if part_2:
            # Part 2 requires you to recursively decompress every section.
            rtl += decompress(s[:marker[0]]) * marker[1]
        else:
            rtl += len(s[:marker[0]] * marker[1])

        # Set the string to start after the end of the repeated substring.
        s = s[marker[0]:]

    # Any characters left remaining are added to the RTL.
    rtl += len(s)

    return rtl


print(decompress(s))

part_2 = True
print(decompress(s))
