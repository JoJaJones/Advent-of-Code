import time
import hashlib
from util import *

data = load_and_parse("data.txt")

def to_md5(src):
    return hashlib.md5(src).hexdigest()

def part_one(data):
    i = 1
    target = "000000"
    res = ""
    while target != res[:len(target)]:
        res = to_md5((data + str(i)).encode('utf-8'))
        i += 1

    return i - 1

def part_two(data):
    pass

start = time.perf_counter()
target = part_one(data[2])
# targets:: 0:609043, 1:1048970
print(target)
print(part_two(data))
end = time.perf_counter()
print(end-start)
