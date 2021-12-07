# %% Puzzle 4 Part 1
"""
    Storing and cleaning the input data to be used later in the
    task. Called numbers will be stored in call_list and each bingo 
    boards will be stored in bingo_boards (a 3-d array). Finally a 
    2nd 3d array 'called' is created to store whether each number is
    called. I believe this is a simpler way to track this than adding
    an additional level to the array. Maybe a class creation to store 
    called as an attribute would be better but I'm not sure.
"""

class board_class():
    """
        A class to store a bingo board, track which numbers have been called on the
        board and to tell whether a bingo has been achieved on the board.
    """

    def __init__(self, number, boards):
        self.number = number
        self.bingo = False
        self.board = boards[number]
        self.called = [[False for _ in range(5)] for _ in range(5)]

    def bingo_row(self):
        check_for = [True for _ in range(5)]
        for row in self.called:
            if row == check_for:
                self.bingo = True
                return

    def bingo_column(self):
        check_for = [True for _ in range(5)]
        for column in range(5):
            new_column = []
            for row in self.called:
                new_column.append(row[column])
            if new_column == check_for:
                self.bingo = True
                return

    def check_bingo(self):
        bingo_row(self)
        if self.bingo == True:
            return True
        bingo_column(self)
        if self.bingo == True:
            return True
        return False




# Storing and cleaning the data for called list
file_1 = open("input_data/puzzle4-1.txt", "r")
call_data = file_1.read()
call_list = call_data.split(',')
file_1.close()

# Storing and cleaning data for bingo_boards, splitting string into boards
file_2 = open("input_data/puzzle4-2.txt", "r")
board_data = file_2.read()
bingo_boards_messy = board_data.split('\n\n')
file_2.close()

# Splitting boards into lines

bingo_boards_interim = []

for board in bingo_boards_messy:
    bingo_boards_interim.append(board.splitlines())

# Splitting lines into elements
bingo_boards = []

for board in bingo_boards_interim:
    new_board = []
    for line in board:
        new_board.append(line.split())
    bingo_boards.append(new_board)

# Making a board to track which numbers have been called

# called = [[[False for _ in range(5)] for _ in range(5)] for _ in range(len(bingo_boards))]






# Sub functions to check for bingo on rows and columns seperately
# Messy AF but I'm getting frustrated, maybe clean this up later, maybe not

# def bingo_row(board):
#     for i in range(5):
#         if board[i][0] == board[i][1] == board[i][2] == board[i][3] == \
#         board[i][4] == True:
#             return True

# def bingo_column(board):
#     for i in range(5):
#         if board[0][i] == board[1][i] == board[2][i] == board[3][i] == \
#         board[4][i] == True:
#             return True

# Creating a Function to check whether bingo has been achieved for each board
# If bingo is acheived it returns the winning board (-1) due to python indexing ofc

def check_bingo(boards):
    for i in range(len(boards)):
        bingo = False
        if bingo_row(boards[i]) or bingo_column(boards[i]):
            bingo = True
            winning_board = i
            break
    if bingo == True:
        return winning_board
    else:
        return bingo
    

# Creating a function to call successive numbers then check for winners

def run_bingo(call_list, bingo_boards, called):
    boards = len(bingo_boards)
    rows = len(bingo_boards[0])
    columns = len(bingo_boards[0][0])
    bingo = False
    final = None
    for number in call_list:
        for i in range(boards):
            for j in range(rows):
                for k in range(columns):
                    if bingo_boards[i][j][k] == number:
                        called[i][j][k] = True
        bingo = check_bingo(called)
        if bingo != False:
            final = int(number)
            break
    output = f"The winning board is board {bingo}"
    print(output)
    winner = bingo_boards[bingo]
    winner_called = called[bingo]
    remaining = 0
    for i in range(rows):
        for j in range(columns):
            if winner_called[i][j] == False:
                remaining += int(winner[i][j])
    return bingo_boards[bingo], called[bingo],  \
        f"Remaining = {remaining}", f"Final number = {final}" , \
        f"Answer = {remaining * final}"
    


# Run the Bingo machine to see which board will win
run_bingo(call_list, bingo_boards, called)


# %%
