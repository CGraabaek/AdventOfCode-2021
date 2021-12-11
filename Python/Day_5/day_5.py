import re
import numpy as np

print("Advent Of Code - Day 5")
PUZZLEINPUT = open('test.txt', 'r').read().split('\n')
print(PUZZLEINPUT)
print(PUZZLEINPUT.sort())

# Match with raw strings
regex_pattern = r"([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)"

def get_coordinates(line):
    match = re.match(regex_pattern,line)
    x1 = int(match.group(1))
    y1 = int(match.group(2))
    x2 = int(match.group(3))
    y2 = int(match.group(4))
    
    return x1,y1,x2,y2

def create_line_array(data,size,use_diagonal_lines):
    line_array = np.zeros((size, size))
    for line in range(len(data)):
        x1,y1,x2,y2 = get_coordinates(data[line])

        if x1 > x2:
            temp = x1
            x1 = x2
            x2 = temp 
        
        if y1 > y2:
            temp = y1
            y1 = y2
            y2 = temp 
    
        #Not working... 
        if use_diagonal_lines:
            if is_diagonal(x1,y1,x2,y2):
                print(f'Diagonal x1 {x1}, y1 {y1} - x2 {x2} y2 {y2}')
            #     for i in range(y1,y2+1):
            #         for j in range(x1,x2+1):
            #             if x1 == y1 and x2 == y2:
            #                 line_array[i,j] += 1
            #     print(line_array)
       # Only find horizontal or vertical lines
        else:
            if x1 == x2 or y1 == y2:
                print(f'Found match with:  x1 {x1}, y1 {y1} - x2 {x2} y2 {y2}' )
                for i in range(y1,y2+1):
                    for j in range(x1,x2+1):
                        line_array[i,j] += 1
    return line_array

def is_diagonal(x1,y1,x2,y2):
    """ Return true if line is diagonal """
    # return any([x1 + y2 == y1 + x2])
    return any([x1 + y2 == y1 + x2, x1 + x2 == y1 + y2, x1 + y1 == x2 + y2])


def get_overlaps(size,items): 
    print(items)
    overlaps = 0

    # Check for overlaps by checking for all arrays with 2 or more IDS
    for k in range(size):
            for l in range (size):
                    if items[k,l] >= 2:
                            overlaps += 1
    return overlaps

N = 10
line_array_p1 = create_line_array(PUZZLEINPUT,N,False)
line_array_p2 = create_line_array(PUZZLEINPUT,N,True)

print(f'Part 1: Overlaps {get_overlaps(N,line_array_p1)}')
print(f'Part 2: Overlaps {get_overlaps(N,line_array_p2)}')