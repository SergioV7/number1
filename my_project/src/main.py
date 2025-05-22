def double(n):
    """Return double the input number."""
    return n * 2


def main():
    name = input("What is your name? ")
    number = input("Enter a number: ")
    try:
        num = float(number)
    except ValueError:
        print("That's not a valid number.")
        return
    doubled = double(num)
    print(f"Hello, {name}! {num} doubled is {doubled}.")


if __name__ == "__main__":
    main()
