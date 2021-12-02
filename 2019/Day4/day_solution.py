def load_array():
    arr = []
    for i in range(193651, 649730):
        arr.append(str(i))

    return arr

def filter_increasing(data):
    filtered_data = []
    for num in data:
        match_found = False
        val_one = int(num[0])
        for idx in range(1, len(num)):
            val_two = int(num[idx])
            if val_one > val_two:
                match_found = False
                break

            if val_one == val_two:
                match_found = True

            val_one = val_two

        if match_found:
            filtered_data.append(num)

    return filtered_data

data = filter_increasing(load_array())
print(len(data))

def filter_over_repeats(data):
    filtered_data = []
    for num in data:
        counts = {}
        for digit in num:
            if digit in counts:
                counts[digit] += 1
            else:
                counts[digit] = 1

        if 2 in counts.values():
            filtered_data.append(num)

    return filtered_data

print(len(filter_over_repeats(data)))