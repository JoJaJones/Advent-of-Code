print([[1,2,3], [2,3,4]] + [[5,6,7]])
from random import randint


def generate_net(length, prefix=""):
    addr = prefix
    net_mask = []
    for byte in prefix.split(" "):
        net_mask.append("1"*len(byte))
    net_mask = " ".join(net_mask)
    for i in range(len("".join(prefix.split(" "))), length):
        if (i) % 8 == 0 and i != 0:
            addr += " "
            net_mask += " "
        addr += str(randint(0, 1))
        net_mask += "1"


    while len(addr) < 35:
        cur_len = len(addr)
        if (cur_len - (cur_len // 8) + 1) % 8 == 0 and cur_len != 0:
            addr += " "
            net_mask += " "
        addr += "0"
        net_mask += "0"


    print(f"{calculate_ip(addr)}/{length}\n{addr}\n{net_mask}\n")

def calculate_ip(bits):
    bits = bits.split(" ")
    ip_string = ""
    for i in range(len(bits)):
        if i != 0:
            ip_string += "."
        ip_string += str(int(bits[i], 2))

    return ip_string

generate_net(32, "11001111 11011101 000001")
generate_net(32, "11010000 01100101 00011101")

print(calculate_ip("11 11111111"))