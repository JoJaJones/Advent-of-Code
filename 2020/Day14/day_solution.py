import time
from util import *

data = load_and_parse("data.txt")

def to_bin_list(num, min_len=None):
    l = []
    while num > 0:
        l = [num & 1] + l
        num >>= 1
    if min_len is not None:
        while len(l) < min_len:
            l = [0] + l
    return l

def parse_data(data):
    op_dict = []
    for line in data:
        if "mask" in line:
            op_dict.append({"mask": list(line.split("=")[1].strip()), "ops": []})
        else:
            mem, val = line.split(" = ")
            mem = int(mem[4:-1])
            val = int(val)

            op_dict[-1]["ops"].append({"mem":mem, "val": val})

    return op_dict

data = parse_data(data)

def find_keep_idxs(mask):
    l = []
    for idx, datum in enumerate(mask):
        if datum == "X":
            l.append(idx)

    return l

def part_one(data):
    mem = {}

    for masks_ops in data:
        mask_copy = masks_ops["mask"][:]
        idxs = find_keep_idxs(mask_copy)
        for op in masks_ops["ops"]:
            mem_addr = op["mem"]
            num = to_bin_list(op["val"])
            for idx in idxs:
                adjusted_idx = (len(mask_copy)-idx)
                if adjusted_idx > len(num):
                    mask_copy[idx] = "0"
                else:
                    mask_copy[idx] = str(num[-adjusted_idx])

            mem[mem_addr] = int("".join(mask_copy), 2)
    total = 0
    for addr in mem:
        total += mem[addr]

    return total


def part_two(data):
    mem = {}
    for masks_ops in data:
        for op in masks_ops["ops"]:
            mask_copy = masks_ops["mask"][:]
            mem_addr = to_bin_list(op["mem"])
            num = op["val"]
            idxs = find_keep_idxs(mask_copy)
            for idx in range(1, len(mem_addr) + 1):
                if mask_copy[-idx] != "X":
                    mask_copy[-idx] = str(int(mask_copy[-idx])|mem_addr[-idx])
            for i in range(2**len(idxs)):
                bin_num = to_bin_list(i, len(idxs))
                for idx in range(len(bin_num)):
                    mask_copy[idxs[idx]] = str(bin_num[idx])
                mem["".join(mask_copy)] = num

    total = 0
    for val in mem.values():
        total += val
    return total

start = time.perf_counter()
target = part_one(data)
print(target)
print(part_two(data))
end = time.perf_counter()
print(end-start)
