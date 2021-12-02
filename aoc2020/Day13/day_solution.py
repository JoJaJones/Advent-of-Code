import time
from util import *

def parse_it(line):
    lines = line.strip().split(",")
    for idx, line in enumerate(lines):
        if line != "x":
            lines[idx] = int(line)
    return lines

data = load_and_parse("data.txt")
# data = load_and_parse("data.txt", parse_it)

def part_one(data):
    time, lines = data
    time = int(time)
    lines = parse_it(lines)
    min_lines = [line for line in lines if line != "x"]
    max_wait = time
    max_wait_idx = -1
    for idx, line in enumerate(min_lines):
        print(line, line - time%line, max_wait, idx)
        if line - time % line < max_wait:
            max_wait = line - time % line
            max_wait_idx = idx
    print(time, min_lines)
    return min_lines[max_wait_idx] * max_wait

def part_two(data):
    time, lines = data
    time = int(time)
    raw_lines = parse_it(lines)
    lines = raw_lines[:]
    while lines[0] == "x":
        lines.pop(0)

    idxs = []
    raw_idxs = []
    lines = [line for line in lines if line != "x"]
    min_line = lines[0]
    print(min_line, lines)
    for i in range(len(raw_lines)):
        if raw_lines[i] != "x":
            print(i)
            raw_idxs.append(i)

    for i, idx in enumerate(raw_idxs):
        while idx >= lines[i]:
            idx -= lines[i]

        idxs.append(idx)

    mods = []
    for i, idx in enumerate(idxs[1:]):
        mods.append(lines[i+1] - idx)
    print("",[0]+mods, "\n", idxs, "\n", lines)

    N = 1
    for val in mods:
        N *= val



    return time


start = time.perf_counter()
target = part_one(data)
print(target)
print(part_two(data))
end = time.perf_counter()
# print(end-start)
