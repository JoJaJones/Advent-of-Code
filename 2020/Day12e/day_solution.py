import time
from util import *

def parse_it(line):
    return line[0], int(line[1:])

DIRECTIONS = ["E", "S", "W", "N"]
DIR_DICT = {"E": (0,1), "N": (1, 0), "W": (0, -1), "S": (-1, 0)}

data = load_and_parse("data.txt", parse_it)

def part_one(data):
    r = 0
    c = 0
    heading = "E"
    for entry in data:
        move, val = entry
        if move == "F":
            rs, cs = DIR_DICT[heading]
            r += rs*val
            c += cs*val
        elif move not in ["R", "L"]:
            rs, cs = DIR_DICT[move]
            r += rs*val
            c += cs*val
        else:
            shift = (val // 90) % 4
            if move == "R":

                heading = DIRECTIONS[(DIRECTIONS.index(heading) + shift) % 4]
            else:
                heading = DIRECTIONS[(DIRECTIONS.index(heading) + 4-shift) % 4]
        # print(r, c)
    return abs(r) + abs(c)


def part_two(data):
    r = 0
    c = 0
    wr, wc = 1, 10
    heading = "E"
    for entry in data:
        move, val = entry
        if move == "F":

            r += wr * val
            c += wc * val
        elif move not in ["R", "L"]:
            rs, cs = DIR_DICT[move]
            wr += rs * val
            wc += cs * val
        else:
            shift = (val // 90) % 4
            wr, wc = rotate(move, shift, wr, wc)


        print(wr, wc, move, val, r, c)
    return abs(r) + abs(c)

def rotate(move, shift, r, c):
    if move == "R":
        for i in range(shift):
            r, c = -c, r
    else:
        for i in range(shift):
            r, c = c, -r

    return r, c

start = time.perf_counter()
target = part_one(data)
print(target)
print(part_two(data))
end = time.perf_counter()
print(end-start)
