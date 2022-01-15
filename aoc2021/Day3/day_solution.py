import time
from util import *

def pars_func(line):
    return int(line, 2)

def get_most_common_ith_bit(data, i, tie_val = 1):
    count = 0
    for num in data:
        if get_ith_from_left(num, i):
            count += 1


    print(i, count, len(data), ["0"*(12-len(format(x, "b"))) + format(x,"b") for x in data])
    if count > len(data) / 2:
        return 1
    elif count == len(data) / 2:
        return tie_val
    return 0


def get_most_common_bits(data):
    counts = [0] * 12

    for i in range(12):
        counts[i] = get_most_common_ith_bit(data, i)

    # print(counts)

    for i in range(12):
        if counts[i] >= len(data) // 2:
            counts[i] = 1
        else:
            counts[i] = 0

    return counts

data = load_and_parse("data.txt", parse_func=pars_func)
def part_one(data):
    counts = get_most_common_bits(data)

    for i in range(12):
        if counts[i] == 1:
            counts[i] = "1"
        else:
            counts[i] = "0"

    gamma = int("".join(counts[::-1]), 2)
    eps = int("".join(["1" if x == "0" else "0" for x in counts[::-1]]), 2)
    return gamma * eps

def part_two(data):
    oxy = []
    co = []

    common = get_most_common_ith_bit(data, 0)
    dest_dict = {common: oxy, (common ^ 1): co}

    for num in data:
        dest_dict[get_ith_from_left(num, 0)].append(num)


    i = 1
    print(f'\n{oxy}')
    while len(oxy) > 1:
        common = get_most_common_ith_bit(oxy, i)
        oxy = filter_list(oxy, common, i)
        # print(len(oxy), oxy, common)
        i += 1
    print(f'{["0"*(12-len(format(x, "b"))) + format(x,"b") for x in oxy]}')

    i = 1
    print(f"\n{co}")
    while len(co) > 1:
        common = get_most_common_ith_bit(co, i)
        co = filter_list(co, common^1, i)
        # print(len(co), co, common)
        i += 1
    print(f'{["0"*(12-len(format(x, "b"))) + format(x,"b") for x in co]}')

    return oxy[0] * co[0]

def filter_list(l, filter_val, idx):
    tmp = l[:]
    l = []
    for num in tmp:
        if get_ith_from_left(num, idx) == filter_val:
            l.append(num)

    return l

def get_ith_from_left(num, i):

    return 1 if (num & (1<<(11-i))) else 0

num = 2345
s = ""
for i in range(12):
    s += str(get_ith_from_left(num, i))

lead0num = "0" * (12-len(format(num, "b"))) + format(num, "b")
print(s==lead0num, s, lead0num)

start = time.perf_counter()
target = part_one(data)
print(target)
print(part_two(data))
end = time.perf_counter()
print(end-start)
