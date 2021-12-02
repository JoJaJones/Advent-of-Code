from util import *
from time import sleep
from os import system
from math import acos, sqrt, pi

def parse_function(line):
    return line.strip()

data = load_and_parse(parse_function)
NUM_ROW = len(data)
NUM_COL = len(data[0])
# print(14-NUM_ROW, 19-NUM_COL)
def find_asteroids(data, pos, vision_dict):
    # print_dict(vision_dict)
    r, c = pos
    if pos not in vision_dict:
        vision_dict[pos] = set()
    for i in range(-r, NUM_ROW - r):
        for j in range(-c, NUM_COL - c):
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

def print_dict(dict_to_print):
    for key in dict_to_print:
        print(f"{key}: {len(dict_to_print[key])} {dict_to_print[key]}")

def calc_rel_prime_pos(r, c):
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

vision_dict = {}

def part_one(data, vision_dict):

    max_count = 0
    for r, row in enumerate(data):
        for c in range(len(row)):
            if row[c] == "#":
                find_asteroids(data, (r, c), vision_dict)

    for asteroid in vision_dict.values():
        if len(asteroid) > max_count:
            max_count = len(asteroid)

    # print_dict(vision_dict)

    return max_count

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def tuple_comparator(tup1, tup2):
    print(tup1, tup2)
    t1r, t1c = tup1
    t2r, t2c = tup2
    if t1r < t2r:
        return -1
    elif t1r == t2r:
        if t1c < t2c:
            return -1
        elif t1c == t2c:
            return 0
        else:
            return 1
    else:
        return 1

answer_one = part_one(data, vision_dict)
# print(answer_one)
def part_two(data, vision_dict, max_asteroids):
    max_count = max_asteroids
    home_base = None
    for item in vision_dict:
        if len(vision_dict[item]) == max_count:
            home_base = item

    # print(home_base)
    home_list = list(vision_dict[home_base])
    home_list = [(x[1], x[0]) for x in home_list]
    degree_dict = {}
    for coord in home_list:
        calc_degree(coord, degree_dict)

    ordered_degrees = sorted(degree_dict.keys())
    print(degree_dict[ordered_degrees[199]])
    return degree_dict, home_base

def calc_degree(coord, degree_dict):
    x, y = coord
    h = sqrt(x ** 2 + y ** 2)

    degree = acos(y/h)*360/(2*pi)
    if x > 0:
        degree = 180 - degree
    elif x < 0:
        degree = 180 + degree
    elif x == 0 and y < 0:
        degree = 0

    else:
        degree = 180

    degree_dict[int(degree*1000)] = coord

def count(xy_list, x_range=(0, 25), y_range=(0, 25)):
    count = 0
    a, b = x_range
    c, d = y_range
    for item in list:
        x, y = item
        if x in range(a, b) and y in range(c, d):
            count += 1
    return count

def extrapolate_slope(home_list, source):
    ret = []

    for pos in home_list:
        r, c = pos
        hr, hc = source
        while 0 <= hc + c < NUM_COL and 0 <= hr + r < NUM_ROW:
            hc += c
            hr += r

        ret.append((hr-source[0], hc-source[1]))

    return ret

def calc_score(coord):
    return coord[0]*100 + coord[1]

def print_data(data):
    system("cls")
    for line in data:
        print(line)

    print("\n")

def find_asteroid(data, source, coord, num):
    sy, sx = source
    x, y = coord
    try:
        while data[sy][sx] != "#":
            sx += x
            sy += y
    except:
        print(coord, sx, sy)
        exit(0)

    data[sy] = data[sy][:sx] + f"{num%10}" + data[sy][sx + 1:]

def print_process(data, source, point_dict):
    sy, sx = source
    data[sy] = data[sy][:sx] + f"@" + data[sy][sx + 1:]
    sorted_coords = sorted(point_dict.keys())
    print_data(data)
    for idx, coord in enumerate(sorted_coords):
        find_asteroid(data, source, point_dict[coord], idx)
        print_data(data)


points, source = part_two(data, vision_dict, answer_one)

# print_process(data[:], source, points)

print()