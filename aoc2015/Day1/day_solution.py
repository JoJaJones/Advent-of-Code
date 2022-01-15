import time
from util import *

data = load_and_parse("data.txt")[0]

def part_one(data):
    count = 0
    for ltr in data:
        if ltr == "(":
            count += 1
        elif ltr == ")":
            count -= 1

    return count

def part_two(data):
    count = 0
    for idx, ltr in enumerate(data):
        if ltr == "(":
            count += 1
        elif ltr == ")":
            count -= 1
        
        if count == -1:
            return idx + 1


start = time.perf_counter()
target = part_one(data)
print(target)
print(part_two(data))
end = time.perf_counter()
print(end-start)
