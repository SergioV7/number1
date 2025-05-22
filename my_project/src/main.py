"""Simple program that doubles a number provided by the user."""

def double(number: int) -> int:
    """Return double the given number."""
    return number * 2

if __name__ == "__main__":
    name = input("What is your name? ")
    number = int(input("Enter a number to double: "))
    result = double(number)
    print(f"Hello {name}! {number} doubled is {result}.")
