import time
from util import *

def parse_func(line):
    l_data = [False]*len(line)
    for c in line.strip():
        if c == '#':
            l_data = True

    return l_data

data = load_and_parse("data.txt")
print(data)
def part_one(data):
    for i in range(1, 7):
        pass
    pass

def part_two(data):
    pass


start = time.perf_counter()
target = part_one(data)
print(target)
print(part_two(data))
end = time.perf_counter()
print(end-start)
