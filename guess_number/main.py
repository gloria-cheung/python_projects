import random


def guess(x):
    random_number = random.randint(1, x)

    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess == random_number:
            print(f"Correct! The number was {random_number}.")
            break
        elif guess > random_number:
            print("Your guess is too high, try again.")
            print("--------------------------------")
        else:
            print("Your guess is too low, try again.")
            print("--------------------------------")


def computer_guess(x, min_val=1, max_val=100):
    c_guess = random.randint(min_val, max_val)
    if c_guess > x:
        print(f"Wrong. Too high. Computer guessed {c_guess}")
        computer_guess(x, min_val, max_val - 1)
    elif c_guess < x:
        print(f"Wrong. Too low. Computer guessed {c_guess}")
        computer_guess(x, min_val + 1, max_val)
    else:
        print(f"Yay. The computer guessed right. The number was: {x}.")


# guess(int(input("enter a number: ")))
computer_guess(int(input("enter a number you want the computer to guess between 1-100: ")))
