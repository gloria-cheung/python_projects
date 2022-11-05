import random
import string
from words import words


def get_valid_word(words):
    # get word from list that does not contain hyphen or space
    word = random.choice(words)
    while " " in word or "-" in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    # user has up 5 wrong guesses to guess the letters of a randomly chosen word
    word = get_valid_word(words["data"])
    word_letters = set(word)
    wrong_letters = set()
    alphabet = set(string.ascii_uppercase)

    num_wrong_guesses = 5
    guessed_word = list("_" * len(word))

    while "".join(guessed_word) != word and num_wrong_guesses != 0:
        print("Word: ", "".join(guessed_word))
        if len(wrong_letters) > 0:
            print("Used letters: ", "".join(wrong_letters))
        guessed_letter = input(f"Guess a letter, you have {num_wrong_guesses} wrong guesses left: ").upper()
        if guessed_letter in alphabet:
            if guessed_letter in word_letters:
                for i in range(0, len(word)):
                    if guessed_letter == word[i]:
                        guessed_word[i] = guessed_letter
            else:
                if guessed_letter in wrong_letters:
                    print("You already guessed this letter, try again")
                    continue
                else:
                    wrong_letters.add(guessed_letter)
                num_wrong_guesses -= 1
        else:
            print("You did not choose a valid letter, try again")
    if "".join(guessed_word) == word:
        print(f"You won! The word was: {word}")
    else:
        print(f"Sorry you lost. The word was {word}")


hangman()
