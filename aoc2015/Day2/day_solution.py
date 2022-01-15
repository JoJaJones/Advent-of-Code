import time
from util import *

class Box:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h
    
    def calc_area(self):
        w = self.w
        l = self.l
        h = self.h
        return 2*l*w + 2*w*h + 2*h*l

    def calc_min_side_area(self):
        return min(self.l*self.w, self.w*self.h, self.l*self.h)
    
    def calc_paper_needs(self):
        return self.calc_area() + self.calc_min_side_area()

    def calc_min_perim(self):
        w = self.w
        l = self.l
        h = self.h
        return 2*min(w+l, w+h, l+h)

    def calc_ribbon_needs(self):
        w = self.w
        l = self.l
        h = self.h
        return self.calc_min_perim() + l*w*h

def pars_func(line):
    l, w, h = [int(x) for x in line.split("x")]
    return Box(l, w, h)

data = load_and_parse("data.txt", pars_func)

def part_one(data):
    return sum([x.calc_paper_needs() for x in data])

def part_two(data):
    return sum([x.calc_ribbon_needs() for x in data])

start = time.perf_counter()
target = part_one(data)
print(target)
print(part_two(data))
end = time.perf_counter()
print(end-start)
