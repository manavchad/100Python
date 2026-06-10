import random

CHOICES = {
    1: "Rock",
    2: "Paper",
    3: "Scissors",
}
WIN_RULES = {
    1: 3,
    2: 1,
    3: 2,
}


def get_user_choice():
    print("*** WELCOME TO ROCK PAPER SCISSORS ***\n")
    print("Choose your move:")
    for key, value in CHOICES.items():
        print(f"{key}: {value}")

    while True:
        try:
            choice = int(input("Enter 1, 2, or 3: "))
        except ValueError:
            print("\n⚠️ Please enter a numeric value.")
            continue
        if choice in CHOICES:
            return choice
        print("\n⚠️ Select one of the given options")


def decide_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a DRAW ⛔️"
    return (
        "You WIN 🏆" if WIN_RULES[user_choice] == comp_choice else "Computer WINS 😢🥀"
    )


def main():
    user_choice = get_user_choice()
    comp_choice = random.choice(list(CHOICES))

    print(f"\nYou chose {CHOICES[user_choice]}")
    print(f"Computer chose {CHOICES[comp_choice]}")

    result = decide_winner(user_choice, comp_choice)
    print(result)


if __name__ == "__main__":
    main()
