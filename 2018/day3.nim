import strutils

#[ 
    1. Write function to generate a set of points for each square inch of fabric.
    2. Set intersect each square's set of points to work out if/where they overlap. Potentially use Nim's `foldr/foldl` to handle this?
    3. Set union that result with a "main" set to track the total points that are overlapped.
    4. Return the length of that main set as the answer.
 ]#

proc getSquares(input: var seq[string]) =
    var
        squares: set[]
        topLeft = split(input[2], ",")
        dimensions = split(input[3], "x")
    
    topLeft[1].removeSuffix(":")

    for i in topLeft[1]..dimensions[1]:
        for j in topLeft[0]..dimensions[0]:
            squares.incl([j, i])

    



var claims: seq[seq[string]] = @[]

for line in lines("day3.txt"):
    claims.add(split(line, " "))

for claim in claims:
    getSquares(claim)
