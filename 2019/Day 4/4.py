from collections import Counter

ans = 0
for n in range(137683, 596253):
    n = str(n)
    digits = [int(x) for x in n]
    no_desc = sorted(digits) == digits
    has_double = 2 in Counter(n).values()
    if no_desc and has_double:
        ans += 1

print(ans)


# def check_double(n):
#     c = Counter(n)
#     if 2 in c.values():
#         return True
#     return False


# def no_desc(n):
#     for i in range(len(n)-1):
#         if n[i+1] >= n[i]:
#             continue
#         return False
#     return True


# ans = 0
# for n in range(137683, 596253):
#     n = str(n)
#     if no_desc(n):
#         if check_double(n):
#             ans += 1

# print(ans)
