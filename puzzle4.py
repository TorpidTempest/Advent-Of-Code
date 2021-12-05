# %% Puzzle 4 Part 1

file_1 = open("input_data/puzzle4-1.txt", "r")
call_data = file_1.read()
call_list = call_data.split(',')
file_1.close()

file_2 = open("input_data/puzzle4-2.txt", "r")
board_data = file_2.read()
bingo_boards_messy = board_data.split('\n\n')
file_2.close()

bingo_boards_interim = []

for board in bingo_boards_messy:
    bingo_boards_interim.append(board.splitlines())

bingo_boards = []

for board in bingo_boards_interim:
    for line in board:
        bingo_boards.append(line.split())
# %%
