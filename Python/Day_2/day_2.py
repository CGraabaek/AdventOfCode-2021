print("Advent Of Code - Day 2")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")

#Part 1
depth = 0
horizontal = 0

for line in PUZZLEINPUT:
    direction = line.split(' ')[0]
    value = int(line.split(' ')[1])
    
    if direction == 'forward':
        horizontal += value
    elif direction == 'up':
        depth -= value
    elif direction == 'down':
        depth += value


#Part 2
depth2 = 0
horizontal2 = 0
aim = 0

for line in PUZZLEINPUT:
    direction = line.split(' ')[0]
    value = int(line.split(' ')[1])
    
    if direction == 'forward':
        horizontal2 += value
        depth2 += aim*value
    elif direction == 'up':
        aim -= value
    elif direction == 'down':
        aim += value

print(f'Part 1: Location {depth} x {horizontal} = {depth*horizontal}')
print(f'Part 2: Location {depth2} x {horizontal2} ={depth2*horizontal2}')