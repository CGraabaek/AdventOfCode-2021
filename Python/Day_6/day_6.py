print("Advent Of Code - Day 6")
PUZZLEINPUT = open('input.txt', 'r').read().split(',')
PUZZLEINPUT = [int(i) for i in PUZZLEINPUT]


day_array = [0,0,0,0,0,0,0,0,0]

for fish in PUZZLEINPUT:
    day_array[fish] += 1

def breed_fish(fish_array):
    new_fish_array = [0,0,0,0,0,0,0,0,0]
    fish_to_add = 0
    for idx in range(len(fish_array)):
        
        if idx == 0 and fish_array[idx] > 0:
            fish_to_add = 1*fish_array[0]
            new_fish_array[0] = 0
        else: 
            new_fish_array[idx-1] = fish_array[idx]

    new_fish_array[6] += fish_to_add
    new_fish_array[8] += fish_to_add
    return new_fish_array

def simulate_fish_population(days,day_array):
    for day in range(days):
        day_array = breed_fish(day_array)
    return day_array

print(f'Part 1: There are {sum(simulate_fish_population(80,day_array))} fish after 80 days')
print(f'Part 2: There are {sum(simulate_fish_population(256,day_array))} fish after 256 days')