# %%
# Storing and cleaning the data for called list
def main():

    file_1 = open("../input_data/puzzle4-1.txt", "r")
    call_data = file_1.read()
    call_list = call_data.split(",")
    file_1.close()

    # Storing and cleaning data for bingo_boards, splitting string into boards
    file_2 = open("../input_data/puzzle4-2.txt", "r")
    board_data = file_2.read()
    bingo_boards_messy = board_data.split("\n\n")
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

    final_boards = {}

    for i in range(len(bingo_boards)):
        final_boards.update({i + 1: bingo_boards[i]})

    called = {
        i + 1: [[False for _ in range(5)] for _ in range(5)]
        for i in range(len(bingo_boards))
    }
    run(call_list, final_boards, called, True)
    run(call_list, final_boards, called, False)


"""
Sub functions from original solution to check for bingo on rows and columns 
seperately. Perhaps not ideal but sufficient for now to test new
dictionary model of the bingo boards.
"""


def bingo_row(board):
    for i in range(5):
        if (
            board[i][0]
            == board[i][1]
            == board[i][2]
            == board[i][3]
            == board[i][4]
            == True
        ):
            return True


def bingo_column(board):
    for i in range(5):
        if (
            board[0][i]
            == board[1][i]
            == board[2][i]
            == board[3][i]
            == board[4][i]
            == True
        ):
            return True


# Creating a Function to check whether bingo has been achieved for a board


def check_bingo(board):
    bingo = False
    if bingo_row(board) or bingo_column(board):
        bingo = True
    return bingo


def check_all(boards: dict):
    complete = []
    for num, board in boards.items():
        bingo = check_bingo(board)
        if bingo == True:
            complete.append(num)
    return complete


# Function to simulate bingo gaames
def run(call_list: list, boards: dict, called: dict, win: bool):
    rows = len(boards[1])
    columns = len(boards[1][0])
    final_number = None
    for number in call_list:
        for board in boards:
            for i in range(5):
                for j in range(5):
                    if boards[board][i][j] == number:
                        called[board][i][j] = True
        complete = check_all(called)
        if complete != []:
            if win == True:
                final_number = int(number)
                remaining = 0
                winning_board = complete[0]
                for i in range(rows):
                    for j in range(columns):
                        if called[winning_board][i][j] == False:
                            remaining += int(boards[winning_board][i][j])
                output = f"""
                The winning board is {complete[0]}
                The final number called was {final_number}
                Sum of the remaining values is {remaining}
                Answer = {final_number * remaining}
                """
                return print(output)
            elif len(boards) == 1:
                final_number = int(number)
                remaining = 0
                key = list(boards.keys())[0]
                for i in range(rows):
                    for j in range(columns):
                        if called[key][i][j] == False:
                            remaining += int(boards[key][i][j])
                output = f"""
                The remaining board is {key}
                The final number called was {final_number}
                The sum of the remaining numbers on the board was {remaining}
                The answer is {final_number * remaining}
                """
                return print(output)
            else:
                for key in complete:
                    del boards[key], called[key]


if __name__ == "__main__":
    main()


# %%
