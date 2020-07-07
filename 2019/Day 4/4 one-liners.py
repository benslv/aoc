part_1 = len([x for x in range(137683, 596253) if sorted(str(x))
              == list(str(x)) and len(set(str(x))) != len(list(str(x)))])
print(part_1)

part_2 = len([x for x in range(137683, 596253) if sorted(str(x))
              == list(str(x)) and 2 in {str(x).count(i) for i in str(x)}])
print(part_2)
