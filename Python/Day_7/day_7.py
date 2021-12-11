print("Advent Of Code - Day 7")
PUZZLEINPUT = open('input.txt', 'r').read().split(',')
PUZZLEINPUT = [int(i) for i in PUZZLEINPUT]

cost = []
min_pos = min(PUZZLEINPUT) ## Min positsion is needed to not start af zero if it isn't neeeded
max_pos = max(PUZZLEINPUT)+1


def simple_crab_movement(input,max_pos):
    cost = []

    for i in range(max_pos):
        total_cost = 0
        for crab_sub in input:
            total_cost += abs(crab_sub-i)

        cost.append(total_cost)
    
    return cost

def sigma_sum(start, end, expression):
    return sum(expression(i) for i in range(start, end))

def get_advanced_cos(a, b):
    n = abs(a - b)
    return (n*(n+1))//2

def advanced_crab_movement(input,max_pos):
    cost = []

    for i in range(min_pos,max_pos):
        total_cost = 0
        for crab_sub in input:
            total_cost += get_advanced_cos(i,crab_sub)

        cost.append(total_cost)
    
    return cost

print(f'Part 1: Least fuel needed {min(simple_crab_movement(PUZZLEINPUT,max_pos))}')
print(f'Part 2: Least fuel needed {min(advanced_crab_movement(PUZZLEINPUT,max_pos))}')
