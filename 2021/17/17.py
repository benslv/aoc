# target area: x=230..283, y=-107..-57

part_1 = 0
part_2 = 0

def solve(i, j, k):
    part_1 = 0
    part_2 = 0

    for DX in range(i):
        for DY in range(k, j):
            dx = DX
            dy = DY
            max_y = 0

            x = 0
            y = 0

            for t in range(500):
                x += dx
                y += dy

                if dx > 0:
                    dx -= 1
                elif dx < 0:
                    dx += 1

                dy -= 1

                max_y = max(max_y, y)

                if 230 <= x <= 283 and -107 <= y <= -57:
                    print(DX, DY, max_y)
                    part_2 += 1
                    part_1 = max(part_1, max_y)
                    break

                if x > 283 or y < -107:
                    break

    return (part_1, part_2)


for x in range(500):
    for y in range(500):
        for z in range(-500, 0, 1):
            if solve(x,y,z) == (5716, 4556):
                print(x,y,z)