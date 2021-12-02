from util import *

def parse_function(line):
    return line.split(",")

def make_edge_dict(data):
    pass

class Edge:
    def __init__(self, start, end, steps):
        srow, scol = start
        erow, ecol = end
        self.is_vertical = scol == ecol
        self.srow, self.scol = start
        self.erow, self.ecol = end
        self.steps_to_start = steps

    def is_perpendicular(self, other):
        return self.is_vertical ^ other.is_vertical

    def is_intersect(self, edge_dict):
        v_col = edge_dict["v"].scol
        v_rows, v_rowe = sorted([edge_dict["v"].srow, edge_dict["v"].erow])
        h_row = edge_dict["h"].srow
        h_cols, hcole = sorted([edge_dict["h"].scol, edge_dict["h"].ecol])

        if h_cols > v_col or hcole < v_col or v_rows > h_row or v_rowe < h_row:
            return False

        return h_row, v_col

    def calc_steps(self, pos):
        row, col = pos

        return abs(self.srow - row) + abs(self.scol - col) + self.steps_to_start

    def intersect(self, other):
        if not self.is_perpendicular(other):
            return False

        edge_dict = {}
        if self.is_vertical:
            edge_dict["v"] = self
            edge_dict["h"] = other
        else:
            edge_dict["v"] = other
            edge_dict["h"] = self

        isect = self.is_intersect(edge_dict)
        if not isect:
            return False

        row, col = isect

        return abs(row) + abs(col), self.calc_steps(isect) + other.calc_steps(isect)

data = load_and_parse(parse_function)

directions = {"U": (1, 0), "R": (0, 1), "L": (0, -1), "D": (-1, 0)}

def calc_next(move, pos):
    mrow, mcol = directions[move[0]]
    move = int(move[1:])
    srow, scol = pos
    erow = srow + mrow * move
    ecol = scol + mcol * move
    return erow, ecol

def create_edge(start, move, num_steps):
    next = calc_next(move, start)
    return Edge(start, next, num_steps), next, int(move[1:])

def load_edge_list(edges, moves):
    start = (0, 0)
    num_steps = 0
    for move in moves:
        new_edge, start, dist = create_edge(start, move, num_steps)
        num_steps += dist
        edges.append(new_edge)

def carrier_function(data, idx):
    min_dist = None
    move_list_one, move_list_two = data
    edge_list = []
    load_edge_list(edge_list, move_list_one)

    start = (0, 0)
    num_steps = 0
    for move in move_list_two:
        new_edge, start, dist = create_edge(start, move, num_steps)
        num_steps += dist
        for edge in edge_list:
            isect = edge.intersect(new_edge)
            if isect:
                val = isect[idx]
                if min_dist is None or val < min_dist:
                    min_dist = val

    return min_dist

def part_one(data):
    return carrier_function(data, 0)

def part_two(data):
    return carrier_function(data, 1)

print(part_one(data))
print(part_two(data))