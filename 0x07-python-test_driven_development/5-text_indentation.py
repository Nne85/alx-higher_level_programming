#!/usr/bin/python3
"""

This module contains a function that indents texts

"""


def text_indentation(text):
    '''This function prints a text with 2 new lines after each ".", "?", or ":"

    Args:
        text (str): The string to be printed

    Raises:
        TypeError: If text is not a string

    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove spaces from beginning and end of the text
    text = text.strip()

    # Initialize variables
    new_text = ""
    punctuation = [".", "?", ":"]
    add_newline = False

    # Loop through each character in the text
    for char in text:
        # Add the character to new_text
        new_text += char

        # Check if the character is a punctuation mark
        if char in punctuation:
            # Add two newlines to new_text
            new_text += "\n\n"
            # Set add_newline to False
            add_newline = False
        # Check if the character is a space
        elif char == " " and add_newline:
            # Remove the space from new_text
            new_text = new_text[:-1]
        # Check if the character is not a space
        elif char != " ":
            # Set add_newline to True
            add_newline = True

    # Print the new text
    print(new_text)
