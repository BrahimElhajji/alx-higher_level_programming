#!/usr/bin/python3

def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    characters = ['.', '?', ':']

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char = 0
    while char < len(text) and text[char] == ' ':
        char += 1

    while char < len(text):
        current_char = text[char]
        print(current_char, end='')

        if current_char in characters or current_char == "\n":
            if current_char in characters or char == len(text) - 1:
                print('\n')

            char += 1
            while char < len(text) and text[char] == ' ':
                char += 1
            continue

        char += 1
