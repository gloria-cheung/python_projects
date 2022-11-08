import random


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # create board
        self.board = self.make_new_board()
        self.assign_values_to_board()

        # initial set to keep track of locations that have been uncovered
        # save (row,col) tuples into this set
        self.dug = set()  # if dug at 0,0 => self.board = {(0,0)}

    def make_new_board(self):
        # constructs new board based on dim_size and num_bombs => list of lists
        board = [[" " for square in range(self.dim_size)] for row in range(self.dim_size)]
        for num in range(self.num_bombs):
            row = random.randint(0, self.dim_size - 1)
            col = random.randint(0, self.dim_size - 1)

            while board[row][col] == "*":
                row = random.randint(0, self.dim_size - 1)
                col = random.randint(0, self.dim_size - 1)

            board[row][col] = "*"

        return board

    def assign_values_to_board(self):
        # once bombs are planted, need to assign num 0-8 for all empty spaces to represent num neighboring bombs
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == "*":
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        # make sure if don't go out of bounds such as negative row, negative col, etc
        for r in range(max(0, row - 1), min(row + 1, self.dim_size) + 1):
            for c in range(max(0, col - 1), min(col + 1, self.dim_size) + 1):
                # don't need to check the original location itself
                if r == row and c == col:
                    continue
                if self.board[r][c] == "*":
                    num_neighboring_bombs += 1

        return num_neighboring_bombs


def play(dim_size=10, num_bombs=10):
    # step1: create board and plant bombs
    board = Board(10, 5)
    # step2: show user the board and ask for where they want to dig
    # step3a: if location is a bomb, show game over message
    # step3b: if location is not a bomb, dig recursively until each square is at least next to a bomb
    # step4: repeat steps 2 and 3 until there are no places to dig => win!
    pass
