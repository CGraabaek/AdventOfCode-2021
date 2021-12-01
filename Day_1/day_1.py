import time

print("Advent Of Code - Day 1")

tic = time.perf_counter()

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")
data = [int(i) for i in PUZZLEINPUT]


## Part 1 - Get number of times the depth has increased
increased = 0
last_val = data[0]

for i in data[1:]:
    if i > last_val:
        increased += 1

    last_val = i


windows = []
increased2 = 0


for (i, val) in enumerate(data):
    windows.append(sum(data[i:i+3]))

last_val2 = windows[0]
for i in windows[1:]:
    if i > last_val2:
        increased2 += 1

    last_val2 = i

print(f'Part 1: Depth increased {increased} times')
print(f'Part 2: Depth increased {increased2} times')