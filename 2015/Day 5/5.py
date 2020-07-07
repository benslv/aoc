with open("5.in", "r") as f:
    words = f.read().splitlines()

# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

part_1 = []

for word in words:
    three_vowels = sum([word.count(v) for v in "aeiou"]) >= 3
    double_letter = any([word[i] == word[i+1] for i in range(len(word)-1)])
    no_banned = all([b not in word for b in ["ab", "cd", "pq", "xy"]])

    if three_vowels and double_letter and no_banned:
        part_1.append(word)

print(len(part_1))

part_2 = []

for word in words:
    two_pair = any([word[i:i+2] in word[i+2:] for i in range(len(word)-1)])
    spaced_double = any([word[i] == word[i+2] for i in range(len(word)-2)])

    if two_pair and spaced_double:
        part_2.append(word)

print(len(part_2))
