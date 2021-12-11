import numpy as np

print("Advent Of Code - Day 4")

PUZZLEINPUT = open('input.txt', 'r').read().replace('  ',' ').split('\n')

bingo_numbers = [int(n) for n in PUZZLEINPUT[0].split(',')]
data = PUZZLEINPUT[2:]

def parse_input(data):
    boards = list(filter(None, data))
    num_boards = len(boards) // 5
    boards2 = list(map(lambda el:[int(n) for n in el.split()], boards))
    bingo_boards = np.array(boards2).reshape((num_boards, 5, 5))

    return num_boards,bingo_boards

num_boards,bingo_boards = parse_input(data)
marked = np.zeros((num_boards, 5, 5), dtype=int)  # Change to 1 when marked.
winner_boards = []
winning_numbers = []
winning_sums = []

def check_number(n):
    for i in range(num_boards):
        for x in range(5):
            for y in range(5):
                if bingo_boards[i,x,y] == n:
                    marked[i,x,y] = 1

def check_board_for_winner(number):
    for board in range(num_boards):
        for i in range(5):
            if np.sum(marked[board, i, 0:]) == 5 or np.sum(marked[board, 0:, i]) == 5: #Row and Columns
                if board not in winner_boards:
                    winning_sums.append(get_board_unmarked_sum(bingo_boards,board,marked)*number)
                    winner_boards.append(board)
                    

def get_board_unmarked_sum(boards,board,marked):
    not_marked = []
    for y in range(5):
        for x in range(5):
            if not marked[board, y, x]:
                not_marked.append(boards[board, y, x])
    return sum(not_marked)

for number in bingo_numbers:
    check_number(number)
    check_board_for_winner(number)
    if len(winner_boards) > 0:
        winning_numbers.append(number)
    if len(winner_boards) == len(bingo_boards):
        break;

print(f'Part 1: Winning sum is {winning_sums[0]} on board {winner_boards[0]}')
print(f'Part 2: Winning sum is {winning_sums[len(winning_sums)-1]} on board {winner_boards[len(winner_boards)-1]}')