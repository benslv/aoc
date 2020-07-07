with open("2.in", "r") as f:
    boxes = [list(map(int, b.split("x"))) for b in f.read().splitlines()]


def find_paper(box):
    l, w, h = [*box]
    return 2*(l*w + l*h + w*h) + min(l*w, l*h, w*h)


part_1 = sum([find_paper(box) for box in boxes])
print(part_1)


def find_ribbon(box):
    v = 1
    for d in box:
        v *= d

    box.remove(max(box))
    print(box)
    p = 2*sum(box)

    return p + v


part_2 = sum([find_ribbon(box) for box in boxes])
print(part_2)
