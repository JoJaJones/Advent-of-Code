import time
from util import *

data = load_and_parse("data.txt")

def part_one(data):
    x, y = 0, 0
    for inst in data:
        dir, qty = inst.split()
        qty = int(qty)
        if dir[0] == 'f':
            x += qty
        elif dir[0] == 'd':
            y += qty
        elif dir[0] == 'u':
            y -= qty


    return x*y

def part_two(data):
    x, y = 0, 0
    aim = 0
    for inst in data:
        dir, qty = inst.split()
        qty = int(qty)
        if dir[0] == 'f':
            x += qty
            y += aim * qty
        elif dir[0] == 'd':
            aim += qty
        elif dir[0] == 'u':
            aim -= qty
    return x * y

start = time.perf_counter()
target = part_one(data)
print(target)
print(part_two(data))
end = time.perf_counter()
print(end-start)
