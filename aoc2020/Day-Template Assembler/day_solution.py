import time
from util import *
from Computer import *

data = load_and_parse("data.txt", assembler_parser)

def part_one(data):
    pass

def part_two(data):
    pass

start = time.perf_counter()
print(part_one(data))
print(part_two(data))
end = time.perf_counter()
print(end-start)
