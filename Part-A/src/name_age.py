"""
Prompts the user for their name and age and estimates birth year.

Input:
    name (str) entered by the user from the keyboard.
    age (int) entered by the user from the keyboard.

Process:
    Calculate the user's birth year by subtracting age from the current year.

Output:
    Formatted message (str) displayed on the screen showing the user's
    estimated birth year.

Typical usage example:
    Enter your name: Alex
    Enter your age: 24
    Hello, Alex! You were born in approximately 2002.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age
    print(f"Hello, {name}! You were born in approximately {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# TODO: Replace with an APA-style reference for a source you used, or delete.
# TODO: Replace with another APA-style reference, or delete this TODO line.
