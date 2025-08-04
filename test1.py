from blessed import Terminal

term = Terminal()
# ...
# Inside the loop:
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
