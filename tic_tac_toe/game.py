import math


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.current_winner = None

    def print_board(self):
        # prints the board at current state of the game
        board = [[self.board[i], self.board[i + 1], self.board[i + 2]] for i in range(0, 9, 3)]
        for row in board:
            result = "| "
            for i in row:
                result += f"{i} | "
            print(result)

    @staticmethod
    def print_board_nums():
        # prints the board with index at each spot
        board = [[i, i + 1, i + 2] for i in range(0, 9, 3)]
        for row in board:
            result = "| "
            for i in row:
                result += f"{i} | "
            print(result)

    def available_moves(self):
        return [i for (i, spot) in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        # if square is empty, reassign board at that square to be letter and return True, otherwise False
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        else:
            return False

    def winner(self, square, letter):
        # checks to see if winner based on the move the player made onto the square
        # check row
        row_idx = square // 3
        target_row = self.board[row_idx * 3: row_idx * 3 + 3]
        if all([spot == letter for spot in target_row]):
            return True

        #check col
        col_idx = square // 3
        target_col = [self.board[i] for i in range(0,9) if (i - col_idx) % 3 == 0]
        if all([spot == letter for spot in target_col]):
            return True

        #check diagonal [0,2,4,6,8]
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal1]) or all([spot == letter for spot in diagonal2]):
                return True
        #if after checking row, col and diagonal and still fail:
        return False






