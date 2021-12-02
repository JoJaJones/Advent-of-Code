from util import load_and_parse

def parse_function(line):
    return int(line)

data = load_and_parse("data.txt", parse_function)

def part_one(data):
    count = 0
    for i in range(len(data) - 1):
        if data[i] < data[i+1]:
            count += 1
    
    return count


def part_two(data):
    count = 0
    cur_elems = [data[0], data[1], data[2]]
    for i in range(3,len(data)):
        prev_sum = sum(cur_elems)
        cur_elems.pop(0)
        cur_elems.append(data[i])
        if prev_sum < sum(cur_elems):
            count += 1
    
    return count

if __name__ == "__main__":
    print(part_two(data))
