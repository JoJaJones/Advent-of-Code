from util import *

def parse_function(line):
    return int(line)

data = load_and_parse(parse_function)

def part_one(data):
    total = 0
    for val in data:
        total += (val//3) - 2

    return total

print(part_one(data))

def part_two(data):
    total = 0
    for val in data:
        fuel = (val // 3) - 2
        while fuel > 0:
            total += fuel
            fuel = (fuel // 3) - 2

    return total

print(part_two(data))