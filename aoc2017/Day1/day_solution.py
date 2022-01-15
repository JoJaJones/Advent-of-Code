import time
from util import *

data = load_and_parse("data.txt")[0]

def part_one(data):
    total = 0
    for i in range(-1, len(data) - 1):
        if data[i] == data[i+1]:
            total += int(data[i])

    return total

def part_two(data):
    total = 0
    length = len(data)
    for i in range(length):
        if data[i] == data[(i + length//2)%length]:
            total += int(data[i])

    return total

start = time.perf_counter()
target = part_one(data)
print(target)
print(part_two(data))
end = time.perf_counter()
print(end-start)
