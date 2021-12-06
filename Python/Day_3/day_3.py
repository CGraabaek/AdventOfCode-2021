import numpy as np

print("Advent Of Code - Day 3")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")

gamma_rate = ''
epsilon_rate = ''

for i in range(len(PUZZLEINPUT[0])):
    elem = [line[i] for line in PUZZLEINPUT]
    unique, counts = np.unique(elem, return_counts=True)    
    #result = dict(zip(unique, counts))
    zeroes = counts[0]
    ones = counts[1]
    
    if zeroes > ones:
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'

## Part 2
def get_rating(input, rating_type):
    # type 0 = o2, type 1 = co2
    rating_arr = input

    for i in range(len(rating_arr[0])):
        elem = [w[i] for w in rating_arr]

        unique, counts = np.unique(elem, return_counts=True)

        zeroes = int(counts[0])
        if len(counts) > 1:
            ones = int(counts[1])
        else: 
            ones = 0
    
        if len(rating_arr) > 1:
            if zeroes > ones:
                if rating_type == 0:
                    rating_arr = list(filter(lambda x: int(x[i])==0, rating_arr))
                else:
                    rating_arr = list(filter(lambda x: int(x[i])==1, rating_arr))
                    
            elif ones > zeroes:
                if rating_type == 0:
                    rating_arr = list(filter(lambda x: int(x[i])==1, rating_arr))
                else:
                    rating_arr = list(filter(lambda x: int(x[i])==0, rating_arr))

            elif ones == zeroes:
                if rating_type == 0:
                    rating_arr = list(filter(lambda x: int(x[i])==1, rating_arr))
                else:
                    rating_arr = list(filter(lambda x: int(x[i])==0, rating_arr))
    
    return rating_arr


print(f'Part 1: Power consumption is {int(gamma_rate, 2)*int(epsilon_rate, 2)}')
print(f'Part 2: Power consumption is {int(get_rating(PUZZLEINPUT,0)[0], 2)*int(get_rating(PUZZLEINPUT,1)[0], 2)}')



