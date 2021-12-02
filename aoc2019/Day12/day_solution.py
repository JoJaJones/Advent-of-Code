import time

from util import *


class Moon:
    def __init__(self, x, y, z, name):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0
        self.initial_state = self.tuplify_stats()

    def apply_gravity(self, other_moon):
        diff_val_x = compare(self.x, other_moon.x)
        self.vx += diff_val_x

        diff_val_y = compare(self.y, other_moon.y)
        self.vy += diff_val_y

        diff_val_z = compare(self.z, other_moon.z)
        self.vz += diff_val_z

    def adjust_pos(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def calculate_energy(self):
        return (abs(self.x) + abs(self.y) + abs(self.z)) * (abs(self.vx) + abs(self.vy) + abs(self.vz))

    def print_stats(self):
        print(f"{self.name}: <x={self.x}, y={self.y}, z={self.z}>  <vx={self.vx}, vy={self.vy}, vz={self.vz}>")

    def is_back_to_start(self):
        if self.tuplify_stats() == self.initial_state:
            return True
        else:
            return False

    def tuplify_stats(self):
        return self.x, self.y, self.z, self.vx, self.vy, self.vz

def parse_function(line, names=["alpha", "bravo", "charlie", "delta"]):
    line = line.strip()[1:-1].split(", ")
    coords = []
    for item in line:
        coords.append(int(item.split("=")[1]))
    x, y, z=coords
    return Moon(x,y,z, names.pop(0))


data = load_and_parse(parse_function)
# moons = []
# for item in data:
#     x, y, z = item
#     moons.append()

def compare(a, b):
    if a > b:
        return -1
    if a == b:
        return 0
    if a < b:
        return 1

def process_step(data, debug=False, moon_name=None):
    start = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if i == j:
                continue
            data[i].apply_gravity(data[j])
    energy = 0
    for moon in data:
        moon.adjust_pos()
        energy += moon.calculate_energy()
        if debug:
            if moon_name is None or moon.name == moon_name:
                moon.print_stats()

            print(energy)


def part_one(data):
    # for moon in data:
    #     moon.print_stats()
    # print()

    for i in range(100):
        process_step(data, True, "asdasdsad")

    energy = 0
    for moon in data:
        energy += moon.calculate_energy()

    return energy

def part_two(data):
    is_repeat = False
    count = 0
    while not is_repeat:

        count += 1
        deja_vu = process_step(data, count)

    return count



# for i in range(1000000):
#     process_step(data, True, "sdasdsd")

start = time.perf_counter()
res = part_one(data)
end = time.perf_counter()
print(end-start)