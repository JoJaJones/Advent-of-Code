from util import *
from int_code import IntCode
from hull_painter import HullPainter

def parse_function(line):
    line = [int(x) for x in line.split(",")]

    return line

data = load_and_parse(parse_function)[0]

robbie = HullPainter(data[:])
robbie.print_board()
robbie.run_program()