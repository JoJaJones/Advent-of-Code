import time
from util import *

data = load_and_parse("data.txt")

def is_nice(s):
    idx = 0
    count = 0
    while count < 3 and idx < len(s):
        if s[idx] in "aeiou":
            count += 1
        
        idx += 1
    
    if count < 3:
        return False

    has_double = False
    idx = 0
    while idx < len(s) - 1 and not has_double:
        if s[idx] == s[idx + 1]:
            has_double = True
        
        idx += 1
    
    if not has_double: 
        return False

    for sub in ["ab", "cd", "pq", "xy"]:
        if sub in s:
            return False

    return True

def is_nice_two(s):
    i = 1
    has_repeat = False
    has_palindrome = False
    while i < len(s) - 2 and (not has_palindrome or not has_repeat):
        if not has_repeat:
            has_repeat = s[i-1:i+1] in s[i+1:]
        
        if not has_palindrome:
            has_palindrome = s[i-1] == s[i+1]
        
        i += 1

    if i == len(s) - 2 and not has_palindrome:
        if has_repeat:
            return s[i-1] == s[i+1]
        
    return has_repeat and has_palindrome



def part_one(data):
    count = 0
    for s in data:
        count += 1 if is_nice(s) else 0
    
    return count

def part_two(data):
    count = 0
    for s in data:
        count += 1 if is_nice_two(s) else 0
    
    return count

# print(is_nice_two("qjhvhtzxzqqjkmpb"), is_nice_two("xxyxx"), is_nice_two("uurcxstgmygtbstg"), is_nice_two("ieodomkazucvgmuy"))

start = time.perf_counter()
target = part_one(data)
print(target)
print(part_two(data))
end = time.perf_counter()
print(end-start)
