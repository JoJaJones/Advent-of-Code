from util import *
from int_code import IntCode

def parse_function(line):
    line = [int(x) for x in line.split(",")]

    return line

data = load_and_parse(parse_function)[0]

def part(data, input_val):
    comp = IntCode(data, input_val)
    comp.run_int_comp()

part(data[:], 1)
part(data[:], 5)

