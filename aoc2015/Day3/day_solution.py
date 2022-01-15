import time
from util import *

data = load_and_parse("data.txt")[0]

def calc_pos(x, y, move):
    if move == ">":
        x += 1
    elif move == "^":
        y += 1
    elif move == "v":
        y -= 1
    elif move == "<":
        x -= 1
    
    return x, y

def part_one(data):
    visited = set()
    x,y = 0,0
    visited.add((x,y))
    for move in data:
        x, y = calc_pos(x, y, move)
        visited.add((x,y))

    return len(visited)

def part_two(data):
    visited = set()
    xs, ys = 0, 0
    xr, yr = 0, 0
    visited.add((xs,ys))
    for i in range(0,len(data), 2):
        xs, ys = calc_pos(xs, ys, data[i])
        visited.add((xs, ys))
        if i + 1 < len(data):
            xr, yr = calc_pos(xr, yr, data[i+1])
            visited.add((xr, yr))

    return len(visited)

start = time.perf_counter()
target = part_one(data)
print(target)
print(part_two(data))
end = time.perf_counter()
print(end-start)
