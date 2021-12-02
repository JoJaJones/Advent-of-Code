import time
from util import *

data = load_and_parse("data.txt")
for idx, line in enumerate(data):
    data[idx] = list(line)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, 1), (1, -1), (-1, -1)]

def process_step(old_data):
    occupied = set()
    data = []
    for row in old_data:
        data.append(row[:])
    for r in range(len(data)):
        for c in range(len(data[0])):
            cur_val = data[r][c]
            if cur_val != ".":
                count = 0
                valid_dir = 0
                for direction in DIRECTIONS:
                    rs, cs = direction
                    is_valid = False
                    if rs + r < len(data) and min(r+rs, c+cs) >= 0 and c+cs < len(data[0]):
                        valid_dir += 1
                        is_valid = True
                    if is_valid and old_data[r+rs][c+cs] == "#":
                        count += 1
                if count >= 4:
                    data[r][c] = "L"
                elif count == 0 and cur_val == "L":
                    data[r][c] = "#"
                    occupied.add((r, c))

    return occupied, data

def find_occupied(data, pos):
    vision_dict = {}
    # print_dict(vision_dict)
    r, c = pos
    if pos not in vision_dict:
        vision_dict[pos] = set()
    for i in range(-r, len(data) - r):
        for j in range(-c, len(data[0]) - c):
            if i ==0 and j == 0 or data[r + i][j + c] != "#":
                continue
            prime_dir = calc_rel_prime_pos(i, j)
            if type(prime_dir) == int:
                print(prime_dir, r, c, i, j)
            if prime_dir in vision_dict[pos]:
                continue
            vision_dict[pos].add(prime_dir)

            prime_dir = -prime_dir[0], -prime_dir[1]
            if type(prime_dir) == int:
                print(prime_dir, r, c, i, j)
            find_pos = (r + i, c + j)
            if find_pos not in vision_dict:
                vision_dict[find_pos] = set()

            vision_dict[find_pos].add(prime_dir)

    return len(vision_dict)

def calc_rel_prime_pos(home, other):
    hr, hc = home
    otr, otc = other
    r = hr-otr
    c = hc - otc
    min_val = min(abs(r), abs(c))
    if min_val == 0:
        if r != 0:
            r //= abs(r)

        if c != 0:
            c //= abs(c)

        return r, c

    i = 2
    while i <= min_val:
        while r % i == 0 and c % i == 0:
            r //= i
            c //= i
            min_val //= i
        i += 1



    return r, c

def process_step_two(old_data):
    data = []
    occupied = set()
    for row in old_data:
        data.append(row[:])

    for r in range(len(data)):
        # print(r)
        for c in range(len(data[0])):
            if data[r][c] != ".":
                seen_count = 0
                valid_dir = 0
                adj_count = 0
                for direction in DIRECTIONS:
                    rs, cs = direction
                    is_valid = False
                    if rs + r < len(data) and min(r+rs, c+cs) >= 0 and c+cs < len(data[0]):
                        valid_dir += 1
                        is_valid = True
                    if is_valid and seen_count < 5 and find_in_dir(direction, (r, c), old_data):
                        seen_count += 1
                if seen_count > 4 and data[r][c] == "#":
                    data[r][c] = "L"
                elif seen_count == 0 and data[r][c] == "L":
                    data[r][c] = "#"
                    occupied.add((r, c))

    return occupied, data

def find_in_dir(direction, pos, data):
    r, c = pos
    rs, cs = direction
    r += rs
    c += cs
    while min(r, c) >= 0 and r < len(data) and c < len(data[0]):
        if data[r][c] == "L":
            return False
        if data[r][c] == "#":
            return True

        r += rs
        c += cs

    return False

def count_seen(occupied, rel):
    vision = {}
    for pos in occupied:
        prime_pos = calc_rel_prime_pos(rel, pos)
        if prime_pos not in vision:
            vision[prime_pos] = True
            if len(vision) >= 5:
                break

    return len(vision)


def part_one(data):
    occupied = set()
    is_done = False
    while not is_done:
        res, data = process_step(data)
        # print_data(data)
        if res == occupied:
            is_done = True
        else:
            occupied = res
    count = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == "#":
                count += 1

    return count

def print_data(data):
    for row in data:
        print("".join(row))

    print()


def part_two(data):
    occupied = set()
    is_done = False
    while not is_done:
        res, data = process_step_two(data)
        print_data(data)
        if res == occupied:
            is_done = True
        else:
            occupied = res

    count = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == "#":
                count += 1

    return count


start = time.perf_counter()
# target = part_one(data)
# print(target)
print(part_two(data))
end = time.perf_counter()
print(end-start)
