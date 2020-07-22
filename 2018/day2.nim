import tables, sequtils, strutils


#[  ======
    PART 1
 ]#

var twos:   int = 0
var threes: int = 0

for line in lines("day2.txt"):
    let frequencies = toCountTable(line)

    var inced_two = false
    var inced_three = false

    for key, value in frequencies:
        case frequencies[key]:
            of 2:
                if not inced_two:
                    inc(twos)
                    inced_two = true
            of 3:
                if not inced_three:
                    inc(threes)
                    inced_three = true
            else:
                discard

echo(twos*threes)

#[  ======
    PART 2
 ]#

var letters: seq[string] = newSeq[string](0)

for line in lines("day2.txt"):
    letters.add(line)

proc getDiffChars(a: string, b: string): seq[char] =
    for i in 0..len(a)-1:
        if a[i] != b[i]:
            result.add(a[i])

for i in 0..<len(letters)-1:
    for j in i..<len(letters):
        var diffChars = getDiffChars(letters[i], letters[j])
        if len(diffChars) == 1:
            echo letters[i], "\n", letters[j]