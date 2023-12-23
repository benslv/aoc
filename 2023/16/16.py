import sys
from collections import namedtuple

inp = sys.stdin.read().splitlines()

grid = {
    (y, x): inp[y][x] for y in range(len(inp)) for x in range(len(inp[y]))
}

DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

Ray = namedtuple("ray", "x y direction")


def process(rays=[Ray(0, 0, "right")]):

    seen_rays = set()

    while rays:
        ray = rays.pop(0)

        char = grid.get((ray.y, ray.x))

        if not char:
            continue

        if (ray.x, ray.y, ray.direction) in seen_rays:
            continue

        seen_rays.add((ray.x, ray.y, ray.direction))

        match grid[(ray.y, ray.x)]:
            case ".":
                y = ray.y + DIRECTIONS[ray.direction][0]
                x = ray.x + DIRECTIONS[ray.direction][1]

                rays.append(Ray(x, y, ray.direction))
            case "/":
                match ray.direction:
                    case "up":
                        x = ray.x + DIRECTIONS["right"][1]
                        rays.append(Ray(x, ray.y, "right"))
                    case "down":
                        x = ray.x + DIRECTIONS["left"][1]
                        rays.append(Ray(x, ray.y, "left"))
                    case "left":
                        y = ray.y + DIRECTIONS["down"][0]
                        rays.append(Ray(ray.x, y, "down"))
                    case "right":
                        y = ray.y + DIRECTIONS["up"][0]
                        rays.append(Ray(ray.x, y, "up"))
            case "\\":
                match ray.direction:
                    case "up":
                        x = ray.x + DIRECTIONS["left"][1]
                        rays.append(Ray(x, ray.y, "left"))
                    case "down":
                        x = ray.x + DIRECTIONS["right"][1]
                        rays.append(Ray(x, ray.y, "right"))
                    case "left":
                        y = ray.y + DIRECTIONS["up"][0]
                        rays.append(Ray(ray.x, y, "up"))
                    case "right":
                        y = ray.y + DIRECTIONS["down"][0]
                        rays.append(Ray(ray.x, y, "down"))
            case "|":
                match ray.direction:
                    case "up" | "down":
                        y = ray.y + DIRECTIONS[ray.direction][0]
                        rays.append(Ray(ray.x, y, ray.direction))
                    case "left" | "right":
                        up_y = ray.y + DIRECTIONS["up"][0]
                        down_y = ray.y + DIRECTIONS["down"][0]

                        rays.append(Ray(ray.x, up_y, "up"))
                        rays.append(Ray(ray.x, down_y, "down"))
            case "-":
                match ray.direction:
                    case "up" | "down":
                        left_x = ray.x + DIRECTIONS["left"][1]
                        right_x = ray.x + DIRECTIONS["right"][1]

                        rays.append(Ray(left_x, ray.y, "left"))
                        rays.append(Ray(right_x, ray.y, "right"))
                    case "left" | "right":
                        x = ray.x + DIRECTIONS[ray.direction][1]
                        rays.append(Ray(x, ray.y, ray.direction))

    energised_points = {(y, x) for (y, x, _) in seen_rays}

    return len(energised_points)


part_1 = process()
print(f"{part_1=}")

part_2 = max(
    *[process([Ray(x, 0, "down")]) for x in range(len(inp[0]))],
    *[process([Ray(x, len(inp)-1, "up")]) for x in range(len(inp[0]))],
    *[process([Ray(0, y, "down")]) for y in range(len(inp))],
    *[process([Ray(len(inp[0])-1, y, "down")]) for y in range(len(inp))]
)

print(f"{part_2=}")
