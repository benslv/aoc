import re

lines = open("4.in").read().split("\n\n")

part_1 = 0
part_2 = 0

for passport in lines:
    if all([field in passport for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]]):
        part_1 += 1

        fields = [field.split(":") for field in passport.split()]
        fd = {k: v for (k, v) in fields}


        valid_fields = [
            int(fd["byr"]) in range(1920, 2003),                                     # Birth year is between 1920 and 2002 inclusive.
            int(fd["iyr"]) in range(2010, 2021),                                     # Issue year is between 2010 and 2020 inclusive.
            int(fd["eyr"]) in range(2020, 2031),                                     # Expiration year is between 2020 and 2030 inclusive.
            (fd["hgt"][-2:] == "cm" and int(fd["hgt"][:-2]) in range(150, 194)       # Height is in cm and between 150 and 193, or...
             ) or (fd["hgt"][-2:] == "in" and int(fd["hgt"][:-2]) in range(59, 77)), # Height is in inches and between 59 and 76.
            re.match(r"^#[0-9a-z]{6}$", fd["hcl"]),                                  # Hair colour is a valid hexadecimal colour.
            fd["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],          # Eye colour is present in this list of colours.
            re.match(r"^\d{9}$", fd["pid"])                                          # Passport ID is a nine-digit number (including leading zeroes).
        ]

        part_2 += all(valid_fields)


print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
