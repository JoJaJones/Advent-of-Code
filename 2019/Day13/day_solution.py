from util import *
from int_code import IntCode

def parse_function(line):
    line = [int(x) for x in line.split(",")]

    return line

data = load_and_parse(parse_function)[0]

def part_one(data):
    comp = IntCode(data[:])
    count = 0
    screen = []
    res = 1
    draw = [0,0,0]
    max_len = 0
    while res is not False:
        res = comp.run()
        if count < 2:
            draw[count] = res
            count += 1
        else:
            count = 0
            if 0 < len(screen) and max_len < draw[0] + 1:
                for i in range(len(screen)):
                    screen[i] += (draw[0] - len(screen[i]) + 1) * [0]

            while len(screen) < draw[1] + 1:
                screen.append([0]*(draw[0]+1))
            try:
                screen[draw[1]][draw[0]] = res
            except IndexError:
                print(draw, len(screen), len(screen[0]), screen)

    print(len(screen), len(screen[0]))
    count = 0
    for row in screen:
        for col in row:
            if col == 2:
                count += 1
    return count

print(part_one(data))

def print_screen(screen):
    for row in screen:
        print("".join(row))

def part_two(data):
    space_dict = {0: " ", 1: "#", 2: "x", 3: "=", 4: "*"}
    data[0] = 2
    comp = IntCode(data)
    count = 0
    screen = [[" "]*37 for _ in range(22)]
    res = 1
    draw = [0, 0, 0]
    max_len = 0
    output = 0
    while res is not False:
        res = comp.run()
        if count < 2:
            draw[count] = res
            count += 1
        elif draw[0] == -1 and draw[1] == 0:
            output = res
            print(output)
            count = 0
        else:
            count = 0
            screen[draw[1]][draw[0]] = space_dict[res]

        print_screen(screen)

part_two(data)