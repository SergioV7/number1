from random import choice
from . import terms
from .progress import load_progress, save_progress


def show_menu():
    print("Sailing Learning Tool")
    print("1. Look up a term")
    print("2. Take a quiz")
    print("3. Navigation exercise")
    print("4. Exit")


def lookup_term(progress):
    term = input("Enter a sailing term: ").strip().lower()
    definition = terms.TERMS.get(term)
    if definition:
        print(f"{term}: {definition}")
        progress.setdefault("terms_viewed", {}).setdefault(term, 0)
        progress["terms_viewed"][term] += 1
        save_progress(progress)
    else:
        print("Term not found.")


def quiz(progress):
    term = choice(list(terms.TERMS.keys()))
    answer = input(f"What does '{term}' mean? ").strip().lower()
    if answer in terms.TERMS[term].lower():
        print("Correct!")
        progress.setdefault("quizzes_passed", 0)
        progress["quizzes_passed"] += 1
    else:
        print(f"Incorrect. {term}: {terms.TERMS[term]}")
    save_progress(progress)


def navigation_exercise():
    print("You are approaching a buoy marking a channel. Should you leave it to port or starboard?")
    choice_in = input("Enter 'port' or 'starboard': ").strip().lower()
    if choice_in == "starboard":
        print("Correct! Green buoys are left to starboard when returning from sea.")
    else:
        print("Incorrect. The correct answer is 'starboard'.")


def main():
    progress = load_progress()
    while True:
        show_menu()
        option = input("Choose an option: ").strip()
        if option == "1":
            lookup_term(progress)
        elif option == "2":
            quiz(progress)
        elif option == "3":
            navigation_exercise()
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

