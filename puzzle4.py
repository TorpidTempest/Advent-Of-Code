# %% Puzzle 4 Part 1

# Storing and cleaning the data
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
    new_board = []
    for line in board:
        new_board.append(line.split())
    bingo_boards.append(new_board)

# Adding Boolean to each element to determine whether it has been called
# I think this is horrible, going to instead make an array of the same size to store booleans
# for board in bingo_boards:
#     for line in board:
#         for i in range(5):
#             line[i] = [line[i], False]


# Making a board to track which numbers have been called

called = []



def check_bingo(boards):
    for board in boards:
        bingo = False





# %%
