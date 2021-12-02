import time

print("Advent Of Code - Day 1")

tic = time.perf_counter()

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")
data = [int(i) for i in PUZZLEINPUT]

def check_depth(list):
    increased = 0
    last_val = data[0]
    for i in list[1:]:
        if i > last_val:
            increased += 1

        last_val = i
    
    return increased

## Part 2 - Depth increses with rolling window sum
windows = []
for (i, val) in enumerate(data):
    windows.append(sum(data[i:i+3]))

print(f'Part 1: Depth increased {check_depth(data)} times')
print(f'Part 2: Depth increased {check_depth(windows)} times')