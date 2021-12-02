import time
from util import *

data = [0] + load_and_parse("data.txt", default_parse_int)
data.sort()
data.append(data[-1] + 3)


def part_one(data):
    data = data[::-1]
    counts = [0,0,0]
    count_3 = 0
    cur = None
    for val in data:
        if cur is None:
            cur = val
        if 0 < cur - val <= 3:
            counts[cur - val - 1] += 1
        cur = val

    print(counts[0] * counts[-1])


def part_two(data):
    memo = {}
    for val in data:
        if val == 0:
            memo[val] = 1
        else:
            memo[val] = 0
            for i in range(1, 4):
                if val - i in memo:
                    memo[val] += memo[val - i]

    return memo[data[-1]]

def part_two_td(data, val, memo=None):
    if memo is None:
        memo = {}

    if val in memo:
        return memo[val]

    if val not in data or val < 0:
        memo[val] = 0
        return 0

    if val == 0:
        memo[val] = 1
        return 1

    result = 0
    for i in range(3, 0, -1):
        result += part_two_td(data, val - i, memo)
    memo[val] = result

    return memo[val]



part_one(data)
print(part_two(data))
max_val = data[-1]
print(part_two_td(set(data), max_val))


