import sys
import re

inp = sys.stdin.read().splitlines()

nums = [re.findall(r"[0-9]", line) for line in inp]

part_1 = sum(int(num[0]+num[-1]) for num in nums)

print(f"{part_1=}")

# Have to do a weird lookahead to catch overlapping numbers (e.g. "eighthree")
part_2_regex = r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))"

num_map = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9",
}

p2_nums = [re.findall(part_2_regex, line) for line in inp]

part_2 = sum(int(num_map.get(num[0], num[0]) + num_map.get(num[-1], num[-1])) for num in p2_nums)

print(f"{part_2=}")