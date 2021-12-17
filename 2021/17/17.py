# target area: x=230..283, y=-107..-57

part_1 = 0
part_2 = 0

for DX in range(284):
    for DY in range(-111, 107):
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
                part_2 += 1
                part_1 = max(part_1, max_y)
                break

            if x > 283 or y < -107:
                break

print("Part 1:", part_1)
print("Part 2:", part_2)