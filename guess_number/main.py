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

guess(int(input("enter a number: ")))
