import time
from util import *

class LightDisplay:
    def __init__(self):
        self.lights = []
        for i in range(1000):
            self.lights.append([])
            for j in range(1000):
                self.lights[i].append(0)
    
    def execute_command(self, cmd, p_one = True):
        r1, c1 = cmd.pos1
        r2, c2 = cmd.pos2

        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if p_one:
                    self.adjust_one(i, j, cmd.cmd)
                else:
                    self.adjust_two(i, j, cmd.cmd)

    def adjust_one(self, i, j, cmd):
        if cmd == -1:
            self.lights[i][j] = 0
        elif cmd == 1:
            self.lights[i][j] = 1
        else:
            self.lights[i][j] ^= 1

    def adjust_two(self, i, j, cmd):
        if cmd == -1:
            self.lights[i][j] = max(0, self.lights[i][j]-1)
        elif cmd == 1:
            self.lights[i][j] += 1
        else:
            self.lights[i][j] += 2

    def execute_commands(self, cmds, p_one = True):
        for cmd in cmds:
            self.execute_command(cmd, p_one)
    
    def count_on(self):
        count = 0
        for line in self.lights:
            count += sum(line)
        
        return count

class LightCommand:
    def __init__(self, cmd, pos1, pos2):
        self.cmd = cmd
        self.pos1 = pos1
        self.pos2 = pos2

def parse_func(line):
    line = line.split(",")
    cmd = line[0].split()[:-1]
    if cmd[0] == "toggle":
        cmd = 0
    elif cmd[1] == "on":
        cmd = 1
    else:
        cmd = -1
    
    r1 = int(line[0].split()[-1])
    line[1] = line[1].split(" through ")
    c1 = int(line[1][0])
    r2 = int(line[1][1])
    c2 = int(line[2])

    return LightCommand(cmd, (r1,c1), (r2,c2))

data = load_and_parse("data.txt", parse_func)

lights = []


def part_one(data):
    l = LightDisplay()
    l.execute_commands(data)
    return l.count_on()

def part_two(data):
    l = LightDisplay()
    l.execute_commands(data, False)
    return l.count_on()

start = time.perf_counter()
target = part_one(data)
print(target)
print(part_two(data))
end = time.perf_counter()
print(end-start)
