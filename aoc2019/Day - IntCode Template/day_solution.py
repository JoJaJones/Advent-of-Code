from util import *
from int_code import IntCode

def parse_function(line):
    line = [int(x) for x in line.split(",")]

    return line

data = load_and_parse(parse_function)[0]