import time

from player import HumanPlayer, RandomComputerPlayer
from game import TicTacToe


def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game(letter)..or None for a tie
    if print_game:
        game.print_board_nums()

    letter = "X"
    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print("") #empty line to break it up

            if game.current_winner:
                if print_game:
                    print(f"{letter} + wins!")
                return letter

            letter = "O" if letter == "X" else "X"

        #add break so computer doesn't make a move immediately
        time.sleep(0.7)

    print("It's a tie!")


tic_tac_toe = TicTacToe()
player = HumanPlayer("X")
computer = RandomComputerPlayer("O")

play(tic_tac_toe, player, computer)
