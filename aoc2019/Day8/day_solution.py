from util import *
from int_code import IntCode

def parse_function(line):
    line = [int(x) for x in line.split(",")]

    return line

data = load_and_parse(parse_function)[0]

def test_one():
    data = load_and_parse(parse_function, "example_data1.txt")[0]
    comp = IntCode(data)
    res = comp.run()
    while res:
        print(res)
        res= comp.run()


def part_one(data):
    comp = IntCode(data)
    comp.run_program()

part_one(data[:])