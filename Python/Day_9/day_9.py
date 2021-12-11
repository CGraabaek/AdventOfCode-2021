import numpy as np

PUZZLEINPUT_lines = open('test.txt', 'r').read().split('\n')
PUZZLEINPUT = [[char for char in n] for n in PUZZLEINPUT_lines]

matrix = np.array(PUZZLEINPUT).astype(np.int32)
max_y, max_x = np.shape(matrix)

total = 0
for y in range(max_y):
    for x in range(max_x):
        if x == 0:
           print(matrix[x,y])

print(matrix)

# print(max_x)
# print(max_y)
