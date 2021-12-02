from util import *
from int_code import IntCode

def parse_function(line):
    line = [int(x) for x in line.split(",")]

    return line

data = load_and_parse(parse_function)[0]
print(len(data))

def test_one():
    data = load_and_parse(parse_function, "example_data1.txt")[0]
    amp_a = IntCode(data[:], 0)
    amp_b = IntCode(data[:], 1)
    amp_c = IntCode(data[:], 2)
    amp_d = IntCode(data[:], 3)
    amp_e = IntCode(data[:], 4)
    res = amp_a.run(0)
    res = amp_b.run(res)
    res = amp_c.run(res)
    res = amp_d.run(res)
    res = amp_e.run(res)
    print(res)

def part_one(data):
    max_val = 0
    for i in range(5):
        for j in range(4):
            for k in range(3):
                for l in range(2):
                    configs = [0,1,2,3,4]
                    amp_a = IntCode(data[:], configs.pop(i))
                    amp_b = IntCode(data[:], configs.pop(j))
                    amp_c = IntCode(data[:], configs.pop(k))
                    amp_d = IntCode(data[:], configs.pop(l))
                    amp_e = IntCode(data[:], configs.pop())

                    res = amp_a.run(0)
                    res = amp_b.run(res)
                    res = amp_c.run(res)
                    res = amp_d.run(res)
                    res = amp_e.run(res)
                    if res > max_val:
                        max_val = res

    return max_val


def part_two(data):
    max_val = 0
    for i in range(5):
        for j in range(4):
            for k in range(3):
                for l in range(2):
                    configs = [0,1,2,3,4]
                    amp_a = IntCode(data[:], configs.pop(i) + 5)
                    amp_b = IntCode(data[:], configs.pop(j) + 5)
                    amp_c = IntCode(data[:], configs.pop(k) + 5)
                    amp_d = IntCode(data[:], configs.pop(l) + 5)
                    amp_e = IntCode(data[:], configs.pop() + 5)

                    res = amp_a.run(0)
                    out = -1
                    while res != False:
                        res = amp_b.run(res)
                        res = amp_c.run(res)
                        res = amp_d.run(res)
                        out = amp_e.run(res)
                        res = amp_a.run(out)
                    if out > max_val:
                        max_val = out

    return max_val

def test_two():
    data = data = load_and_parse(parse_function, "example_data2.txt")[0]
    amp_a = IntCode(data[:], 9)
    amp_b = IntCode(data[:], 7)
    amp_c = IntCode(data[:], 8)
    amp_d = IntCode(data[:], 5)
    amp_e = IntCode(data[:], 6)
    res = amp_a.run(0)
    out = -1
    while res != False:
        res = amp_b.run(res)
        res = amp_c.run(res)
        res = amp_d.run(res)
        out = amp_e.run(res)
        res = amp_a.run(out)

    print(out)

print(part_two(data))