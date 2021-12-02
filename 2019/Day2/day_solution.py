from util import *
from int_code import IntCode

def parse_function(line):
    line = [int(x) for x in line.split(",")]

    return line

def part_one():
    data = load_and_parse(parse_function)[0]
    data[1] = 12
    data[2] = 2
    comp = IntCode(data)
    comp.run_int_comp()
    print(comp.get_pos_value(0))

def part_two():
    data = load_and_parse(parse_function)[0]

    val_one = None
    val_two = None
    for i in range(100):
        for j in range(100):
            mem = list(data)
            mem[1] = i
            mem[2] = j
            comp = IntCode(mem)
            comp.run_int_comp()
            if comp.get_pos_value(0) == 19690720:
                val_one = i
                val_two = j
    print(100*val_one + val_two)

part_two()