import strutils, timeit

var total: int = 0
var freqs: seq[int] = @[0] # Create new (dynamically-sized) list
var dup_freq: bool = false

timeGo(100, 10):
    while not dup_freq:
        for line in lines("day1.txt"):
            total += parseInt(line)

            if total in freqs:
                echo("First duplicate frequency was ", total)
                dup_freq = true
                break
            else:
                freqs.add(total)