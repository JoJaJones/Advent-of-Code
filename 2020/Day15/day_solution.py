import time
from util import *

data = [0,1,5,10,3,12,19]

# data = [2,1,3]

def part_one(data):
    order_dict = {}
    prev = 0
    for i in range(30000000):
        if i < len(data):
            prev = data[i]
        elif prev in order_dict and len(order_dict[prev]) > 1:
            prev = order_dict[prev][-1] - order_dict[prev][-2]
        else:
            prev = 0

        if prev in order_dict:
            order_dict[prev].append(i)
        else:
            order_dict[prev] = [i]

    return prev




def part_two(data):
    pass

start = time.perf_counter()
target = part_one(data)
print(target)
print(part_two(data))
end = time.perf_counter()
print(end-start)
