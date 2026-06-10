import subprocess
import time
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
USER_SCORE = 0
COMP_SCORE = 0
ROUND = 0


def get_user_choice():
    subprocess.run(["clear"])
    print("*** WELCOME TO ROCK PAPER SCISSORS ***\n")
    global ROUND
    ROUND += 1
    print(f"⭐️ ROUND: {ROUND}")
    print(f"⭐️ Your score: {USER_SCORE}")
    print(f"⭐️ Computer's score: {COMP_SCORE}\n")
    for key, value in CHOICES.items():
        print(f"{key}: {value}")

    while True:
        try:
            choice = int(input("Choose your move: "))
        except ValueError:
            print("\n⚠️ Please enter a numeric value.")
            continue
        if choice in CHOICES:
            return choice
        print("\n⚠️ Select one of the given options")


def decide_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a DRAW ⛔️"
    elif WIN_RULES[user_choice] == comp_choice:
        global USER_SCORE
        USER_SCORE += 1
        return "\nYou WIN 🏆"
    else:
        global COMP_SCORE
        COMP_SCORE += 1
        return "\nComputer WINS 😢🥀"


def main():
    user_choice = get_user_choice()
    comp_choice = random.choice(list(CHOICES))

    print(f"\nYou chose {CHOICES[user_choice]}")
    print(f"Computer chose {CHOICES[comp_choice]}")

    result = decide_winner(user_choice, comp_choice)
    print(result)
    time.sleep(2)
    do_continue = input("Do you want to play next round? [YES/NO]: ").lower().strip()
    if do_continue == "yes":
        main()
    return


if __name__ == "__main__":
    main()
