class Claim:
    def __init__(self, id_, squares):
        self.id = id_
        self.squares = squares


def getSquares(claim):
    squares = set()
    topLeft = list(map(int, claim[2].rstrip(":").split(",")))
    dimensions = list(map(int, claim[3].split("x")))
    for i in range(topLeft[1], topLeft[1] + dimensions[1]):
        for j in range(topLeft[0], topLeft[0] + dimensions[0]):
            squares.add((j, i))

    return squares


overlaps = set()

with open("day3.txt") as f:
    # claims = [Claim(, getSquares(x.split(" "))) for x in f.read().splitlines()]

    claims = []

    for x in f.read().splitlines():
        claim = x.split(" ")
        claims.append(
            Claim(
                id_=claim[0].lstrip("#"),
                squares=getSquares(claim)
            )
        )

for i in range(len(claims) - 1):
    for j in range(i+1, len(claims)):
        overlaps |= claims[i].squares & claims[j].squares

print(len(overlaps))
