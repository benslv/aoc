import re, time

lines = open("4.in").read().split("\n\n")

part_1 = 0
part_2 = 0

start = time.time_ns()

for passport in lines:
    if all([field in passport for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]]):
        part_1 += 1

        fields = [field.split(":") for field in passport.split()]
        fd = {k: v for (k, v) in fields}


        valid_fields = [
            1920 <= int(fd["byr"]) <= 2002,                                     # Birth year is between 1920 and 2002 inclusive.
            2010 <= int(fd["iyr"]) <= 2020,                                     # Issue year is between 2010 and 2020 inclusive.
            2020 <= int(fd["eyr"]) <= 2030,                                     # Expiration year is between 2020 and 2030 inclusive.
            (fd["hgt"][-2:] == "cm" and int(fd["hgt"][:-2]) in range(150, 194)       # Height is in cm and between 150 and 193, or...
             ) or (fd["hgt"][-2:] == "in" and int(fd["hgt"][:-2]) in range(59, 77)), # Height is in inches and between 59 and 76.
            re.match(r"^#[0-9a-z]{6}$", fd["hcl"]),                                  # Hair colour is a valid hexadecimal colour.
            fd["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],          # Eye colour is present in this list of colours.
            len(fd["pid"]) == 9                                                      # Passport ID is a nine-digit number.
        ]

        part_2 += all(valid_fields)

end = time.time_ns()

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")

print(f"Took: {end-start}ns")