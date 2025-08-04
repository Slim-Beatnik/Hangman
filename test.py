from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
import time

from blessed import Terminal

term = Terminal()

console = Console(
    color_system="truecolor", width=80, height=30
)  # Removed theme for broader compatibility


def create_game_layout() -> Layout:
    layout = Layout(name="root")
    layout.split(
        Layout(name="board", size=18), Layout(name="mid", size=3), Layout(name="low")
    )
    return layout


def get_simulated_input(current_input: Text) -> str | None:
    # This is a placeholder for actual non-blocking input
    # In a real application, you'd use getchlib.getkey or similar
    # For now, we'll simulate a user typing a guess and pressing enter
    if len(current_input.plain) < 1:
        return "a"  # Simulate first input
    elif len(current_input.plain) < 2:
        return "b"
    elif len(current_input.plain) < 3:
        return "\n"  # Simulate Enter
    return None


def main():
    layout = create_game_layout()
    current_input_text = Text("")

    # Initial panel states
    # Note: previous_turn_message, available_letters, and display_hangman
    # would be actual variables in your game logic
    previous_turn_message = "Start guessing!"
    available_letters = "[green]A-Z[/green]"

    # Use a Panel to display the prompt and user input
    input_panel = Panel(
        f"Enter your guess: {current_input_text}",
        title="Player Team",
        border_style="green",
    )
    layout["mid"].update(input_panel)
    layout["board"].update(
        Panel("Hangman Board", title="Derrick", border_style="magenta")
    )
    layout["low"].update(Panel(available_letters, title="Game", border_style="cyan"))

    # Live context
    with Live(layout, screen=True, refresh_per_second=10, console=console) as live:
        user_guess = None
        while user_guess is None:
            char = term.inkey(timeout=0)  # Non-blocking input with no timeout
            if char:
                if char.is_sequence:  # Handle special keys like arrow keys, etc.
                    if char.name == "KEY_BACKSPACE":
                        if len(current_input_text) > 0:
                            current_input_text.pop()
                    elif char.name == "KEY_ENTER":
                        user_guess = current_input_text.plain.strip()
                        break
                elif char.isprintable():
                    current_input_text.append(char)

                    # Update the input panel with the current input
                    input_panel.renderable = f"Enter your guess: {current_input_text}"
                    live.update(layout)  # Refresh the Live display

                    time.sleep(0.1)  # Small delay to prevent busy-waiting

        # Once user_guess is obtained, you can update the panels accordingly
        previous_turn_message = (
            f"You guessed: [bold yellow]{user_guess.upper()}[/bold yellow]"
        )
        layout["mid"].update(
            Panel(previous_turn_message, title="Player Team", border_style="green"),
        )
        live.update(layout)  # Final refresh

        time.sleep(2)  # Show the result for a bit


if __name__ == "__main__":
    main()
