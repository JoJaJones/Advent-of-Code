import time
from util import *

data = load_and_parse("data.txt")

sections = []
tickets = []


class TicketRules:
    def __init__(self, sections):
        self.sections = dict()
        self.validated_sections = set()
        for section in sections:
            section = section.split(": ")
            category = section[0]
            section = section[1].split(" or ")
            section_ranges = [0,0,0,0]
            section_ranges[0], section_ranges[1] = section[0].split("-")
            section_ranges[2], section_ranges[3] = section[1].split("-")
            section_ranges = [int(x) for x in section_ranges]
            self.sections[category] = SectionRules(section_ranges)

    def validate_section(self, tickets):
        section_map = dict()
        for i in range(len(tickets[0].section_values)):
            section_map[i] = set(self.sections.keys())

        for i in range(len(tickets[0].section_values)):
            for ticket in tickets:

                cur_idx_set = set()
                for key, value in self.sections.items():
                    if value.is_valid(ticket.section_values[i]):
                        cur_idx_set.add(key)

                section_map[i] = section_map[i].intersection(cur_idx_set)

        return section_map

    def __str__(self):
        ret = ""
        for key, value in self.sections.items():
            ret += f'{key}: {value}\n'

        return ret

    def get_min(self):
        return min(self.sections.values(), key=lambda x: x.low_range_low).low_range_low

    def get_max(self):
        return max(self.sections.values(), key=lambda x: x.high_range_high).high_range_high

class SectionRules:
    def __init__(self, section):
        self.low_range_low = section[0]
        self.low_range_high = section[1]
        self.high_range_low = section[2]
        self.high_range_high = section[3]

    def __str__(self):
        return f"{self.low_range_low}-{self.low_range_high} {self.high_range_low}-{self.high_range_high}"

    def is_valid(self, num):
        return self.low_range_low <= num <= self.low_range_high or self.high_range_low <= num <= self.high_range_high


class Ticket:
    def __init__(self, data):
        self.section_values = []
        for num in data.split(","):
            self.section_values.append(int(num))

    def is_invalid(self, rules):
        low = min(self.section_values)
        high = max(self.section_values)
        if low < rules.get_min():
            # print(low, high)
            return low
        elif high > rules.get_max():
            # print(low, high)
            return high

        return None

def section_data(data):
    idx = 0
    while len(data[idx]) > 1:
        sections.append(data[idx])
        idx += 1
    rules = TicketRules(sections)

    idx += 2
    ticket = Ticket(data[idx])
    idx += 3
    for i in range(idx, len(data)):
        tickets.append(Ticket(data[i]))

    return rules, ticket, tickets


def part_one(data):
    r, m, t = section_data(data)
    count = 0
    for ticket in t:
        val = ticket.is_invalid(r)
        if val is not None:
            count += val

    return count


def part_two(data):
    r, m, t = section_data(data)
    idx = 0
    while idx < len(t):
        if t[idx].is_invalid(r) is not None:
            t.pop(idx)
        else:
            idx += 1

    res = r.validate_section(t)
    # for i in range(len(res)):
    #     print(f'{i}: {res[i]}')

    idxes = []
    while len(res) > 0:
        cur = min(res, key=lambda x: len(res[x]))
        cur_data = res[cur]
        if "departure" in list(cur_data)[0]:
            idxes.append(cur)

        del res[cur]
        for val in res.values():
            val -= cur_data

    res = m.section_values[idxes[0]]
    for i in range(1, len(idxes)):
        res *= m.section_values[idxes[i]]

    return res


start = time.perf_counter()
target = part_one(data)
print(target)
print(part_two(data))
end = time.perf_counter()
print(end-start)
