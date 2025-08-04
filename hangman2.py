import re
from pathlib import Path
from random import randint
from time import sleep

from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.theme import Theme

hangman_theme = Theme(
    {
        "display_word": "bold #ebcc0e",
        "_": "white",
        "guess": "bold #524556",
        "available_letters": "bold #ffffff",
        "prev_turn_message": "bold #ebcc0e",
        "derrick": "bold #8e6336 on #8bccff",
        "ground": "bold #8e6336 on #38761d",
        "felon": "bold #000000 on #8bccff",
        "grass": "bold #32b857",
        "lose": "bold #be4748 on #43270f",
        "win": "bold #06402b on #43270f",
    },
)

console = Console(color_system="truecolor", theme=hangman_theme, width=80, height=30)


def create_hangman_layout():
    layout = Layout(name="root")

    # Split main into 3 vertical sections
    layout.split(
        Layout(name="upp", size=18),
        Layout(name="mid", size=5),
        Layout(name="low", size=4),
        Layout(name="btm", size=3),
    )

    return layout


def render_layout(layout: Layout):
    layout["upp"].update(
        Panel(
            display_hangman(fail_count, win), title="Derrick", border_style="magenta"
        ),
    )
    layout["mid"].update(
        Panel(previous_turn_message, title="Player Team", border_style="green"),
    )
    (Layout["btm"].update(Panel(display_word, title="Word", border_style="yellow")),)
    (layout["low"].update(Panel(available_letters, title="Game", border_style="cyan")),)


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
previous_turn_message = ""
hangman_layout = create_hangman_layout()


def get_guess():
    while True:
        guess = input("Guess a letter: ")
        # guess blank, or not alphabetic, or more than one character
        if not guess or re.search(r"[^a-z]|.{2,}", guess, flags=re.IGNORECASE):
            console.print("Please enter a single letter.")
        return guess


def display_hangman(fail_count, win):
    # The backslash, \, is an exit(escape) character, and also needs to be exited. To console.print \ the string must look like '\\'
    # multi-line formatted string, code in brackets will be interpolated
    display_failure = {
        0: {
            "head": "[felon]           [/felon]",
            "torso": "[felon]           [/felon]",
            "gut": "[felon]           [/felon]",
            "legs": "[felon]           [/felon]",
        },
        1: {
            "head": "[felon]:cry:         [/felon]",
            "torso": "[felon]           [/felon]",
            "gut": "[felon]           [/felon]",
            "legs": "[felon]           [/felon]",
        },
        2: {
            "head": "[felon]:worried:         [/felon]",
            "torso": "[felon] |         [/felon]",
            "gut": "[felon] |         [/felon]",
            "legs": "[felon]           [/felon]",
        },
        3: {
            "head": "[felon]:hot_face:         [/felon]",
            "torso": "[felon]/|         [/felon]",
            "gut": "[felon] |         [/felon]",
            "legs": "[felon]           [/felon]",
        },
        4: {
            "head": "[felon]:nauseated_face:         [/felon]",
            "torso": "[felon]/|\\        [/felon]",
            "gut": "[felon] |         [/felon]",
            "legs": "[felon]           [/felon]",
        },
        5: {
            "head": "[felon]:scream:         [/felon]",
            "torso": "[felon]/|\\        [/felon]",
            "gut": "[felon] |         [/felon]",
            "legs": "[felon]/          [/felon]",
        },
        6: {
            "head": "[felon]:dizzy_face:         [/felon]",
            "torso": "[felon]/|\\        [/felon]",
            "gut": "[felon] |         [/felon]",
            "legs": "[felon]/ \\        [/felon]",
        },
    }

    return f"""
[derrick]                ┌───────┐         [/derrick]
[derrick]                │      {display_failure[fail_count].get("head", "           ")}[/derrick]
[derrick]                │      {display_failure[fail_count].get("torso", "           ")}[/derrick]
[derrick]                │      {display_failure[fail_count].get("gut", "           ")}[/derrick]
[derrick]                │      {display_failure[fail_count].get("legs", "           ")}[/derrick]
[on #38761d]  [grass]෴   [/grass] [ground]─────────┴─────────[/ground][grass]෴   [/grass]    [/on #38761d]
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

        # render_layout(
        #     hangman_layout,
        #     display_hangman(fail_count, win),
        #     previous_turn_message,
        #     display_word,
        #     available_letters,
        # )
        console.print(display_hangman(fail_count, False), justify="left")
        if not win:
            console.print(prev_turn_message)  # console.print error message
        prev_turn_message = ""  # reset error message
        console.print(" ".join(display_word), "\n")

        console.print(
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
        console.print("\n--------------------------------------------------\n")

    console.print(display_hangman(fail_count, win))
    sleep(1.5)


if __name__ == "__main__":
    while True:
        again = None
        play_hangman(words)
        # render_layout(create_game_layout(), "", "", "")

        again = input("Play again? (y/n): ").lower()
        if again in ("y", "yes"):
            play_hangman(words)
        else:
            word_file.close()
            console.print("Thanks for playing!")
            sleep(1.5)
            exit  # noqa: B018
