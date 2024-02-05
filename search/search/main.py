
"""Check for word inside a text."""

from pathlib import Path

from rich.console import Console

import typer

cli = typer.Typer()


def confirm_valid_file(file: Path) -> bool:
    """Confirm that the provided file is a valid path."""
    # Check if the file is not None and if it is a file
    if file is not None and file.is_file():
        # Return True if the file is valid
        return True
    else:
        # Return False if the file is None or not a valid file
        return False


def human_readable_boolean(answer: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    # determine if the boolean value is True or False
    if answer:
        # if the input variable answer is True, then return "Yes"
        return "Yes"
    # if the input variable answer is False, then return "No"
    return "No"


def word_search(text: str, word: str) -> bool:
    """Determine whether or not a word is found in the text in case-sensitive fashion."""
    # Perform a case-sensitive search for the word in the provided text
    return word in text


@cli.command()
def word(
    word: str = typer.Option(None),
    dir: Path = typer.Option(None),
    file: Path = typer.Option(None),
):
    """Process a file by searching for a specified word."""
    # create a console for rich text output
    console = Console()
    # add extra space after the command to run the program
    console.print()
    # create the full name of the file
    file_fully_qualified = dir / file
    console.print(f"😃 Searching through the file called {file_fully_qualified}!")
    if confirm_valid_file(file_fully_qualified):

        with open(file_fully_qualified, "r") as f:
            contents = f.read()

        word_found = word_search(contents, word)
        console.print(
            f"Was the word {word} found in the file {file_fully_qualified}? {human_readable_boolean(word_found)}"
        )
    # Display a message about whether the word was or was not found
    else:
        console.print(f"{file_fully_qualified} was not a valid file")
