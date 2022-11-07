class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.current_winner = None

    def print_board(self):
        board = [[self.board[i], self.board[i + 1], self.board[i + 2]] for i in range(0, 9, 3)]
        for row in board:
            result = "| "
            for i in row:
                result += f"{i} | "
            print(result)

    @staticmethod
    def print_board_nums():
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
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        else:
            return False