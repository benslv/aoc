import math


def fuel(mass):
    return math.floor(mass/3)-2


def recurse_fuel(fuel):
    fuel = math.floor(fuel/3)-2

    if fuel <= 0:
        return 0

    return fuel + recurse_fuel(fuel)


lines = [int(x) for x in open("Day 1/1.in", "r").readlines()]


fuel = sum([fuel(x) for x in lines])
fuel_for_fuel = sum([recurse_fuel(x) for x in lines])

print(fuel)
print(fuel_for_fuel)
