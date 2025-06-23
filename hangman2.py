import re
from pathlib import Path
from random import randint
from time import sleep

from rich.color import Color
from rich.console import Console
from rich.panel import Panel

c = Console(color_system="truecolor", theme="monokai", width=80)


# text file with list of 7-letter long words - open - r = readonly
word_file = Path.open("seven_letter_words.txt", "r")
# we want words to disclude \n (readlines includes newline character)
words = [word[:-1] for word in word_file.readlines()]


# initialize variables
guessed_letters = []
win = False
fail_count = 0
prev_turn_message = ""
display_word = "_ " * 7
available_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_guess():
    while True:
        guess = input("Guess a letter: ")
        if not guess or re.search(r"[^a-z]|.{2,}", guess, flags=re.IGNORECASE):
            print("Please enter a single letter.")
        return guess


def display_hangman(fail_count, win):
    # The backslash, \, is an exit(escape) character, and also needs to be exited. To print \ the string must look like '\\'
    # multi-line formatted string, code in brackets will be interpolated
    return f"""
        -----
        |   |
        |   {"O" if fail_count > 0 else ""}
        |  {"/|" if fail_count == 3 else ""}{" |" if fail_count == 2 else ""}{"/|\\" if fail_count >= 4 else ""}
        |   {"|" if fail_count > 1 else ""}
        |  {"/" if fail_count == 5 else ""}{"/ \\" if fail_count == 6 else ""}
    ----------
{"Sorry, you lost.\nJeff died." if fail_count > 5 else ""}{"You saved a murderer from certain death.\nI hope you're happy!" if win else ""}
    """


def play_hangman(words):
    word = words.pop(randint(0, len(words) - 1)).upper()

    # initialize variables
    guessed_letters = []
    win = False
    fail_count = 0
    prev_turn_message = ""
    display_word = "_ " * len(word)
    available_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Game starts
    while fail_count != 6 and not win:
        # Show the word progress
        # The underscore or the letter to show the progress of how many has been guessed
        print(display_hangman(fail_count, False))
        if not win:
            print(prev_turn_message)  # print error message
        prev_turn_message = ""  # reset error message
        print(" ".join(display_word), "\n")

        print(
            " ".join(
                [
                    letter
                    for letter in available_letters
                    if letter not in guessed_letters
                ],
            ),
        )

        guess = get_guess().upper()

        # Add it to our guessed letters
        if guess in guessed_letters:
            prev_turn_message = f"You already guessed this letter: {guess}"
        else:
            guessed_letters.append(guess)
            if guess in word:
                count = word.count(guess)
                prev_turn_message = f"Correct! {guess} is in the word exactly {count} time{'s' if count > 1 else ''}"
                display_word = " ".join(
                    (ch if ch in guessed_letters else "_" for ch in word),
                )
                win = "_" not in display_word

            else:
                fail_count += 1
        print("\n--------------------------------------------------\n")

    print(display_hangman(fail_count, win))
    sleep(1.5)


if __name__ == "__main__":
    while True:
        again = None
        play_hangman(words)

        again = input("Play again? (y/n): ").lower()
        if again in ("y", "yes"):
            play_hangman(words)
        else:
            word_file.close()
            print("Thanks for playing!")
            sleep(1.5)
            exit  # noqa: B018
