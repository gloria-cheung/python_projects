from player import HumanPlayer, RandomComputerPlayer
from game import TicTacToe


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()


tic_tac_toe = TicTacToe()
player = HumanPlayer("X")
computer = RandomComputerPlayer("O")

play(tic_tac_toe, player, computer)
