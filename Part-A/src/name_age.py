"""TODO: Replace with a one-line summary of the program's purpose (<73 chars).

Input:
    TODO: Replace with a major input, including its type and source.
    TODO: Replace with another major input, or delete this TODO line.
    TODO: Replace with another major input, or delete this TODO line.

Process:
    TODO: Replace with a major processing step.

Output:
    TODO: Replace with a major output, including its type and destination.

Typical usage example:
    TODO: Replace with the input prompt and original name-input example.
    TODO: Replace with the input prompt and original age-input example.
    TODO: Replace with the resulting output from those inputs.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    # TODO: Replace with code to get user's name as a string. See zyBooks 1.3.
    name = input("Enter your name: ")
    # TODO: Replace with code to get user's age as an integer. See zyBooks 2.6.
    age = int(input("Enter your age: "))

    # Calculate user's approximate birth year.
    # TODO: Replace with code to process data. See zyBooks 1.16 & 1.17.
    birth_year = CURRENT_YEAR - age
    # Output personalized message with user's name and birth year.
    # TODO: Replace with code to output formatted results. zyBooks 1.3 & 2.7.
    print(f"Hello, {name}! You were born in approximately {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# TODO: Replace with an APA-style reference for a source you used, or delete.
# TODO: Replace with another APA-style reference, or delete this TODO line.
