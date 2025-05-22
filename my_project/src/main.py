"""Main module for doubling numbers."""

def double(x: int) -> int:
    """Return double the input number."""
    return x * 2


def main() -> None:
    """Prompt user for a name and number, then print the doubled value."""
    name = input("What is your name? ")
    while True:
        number_str = input("Enter a number to double: ")
        try:
            number = int(number_str)
            break
        except ValueError:
            print("Please enter a valid integer.")
    result = double(number)
    print(f"Hello {name}, {number} doubled is {result}.")


if __name__ == "__main__":
    main()
