print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = (
    input(
        "\nYou're at a crossroad. Where do you want to go? Type 'left' or 'right'.\n: "
    )
    .strip()
    .lower()
)
if choice1 == "left":
    choice2 = (
        input(
            "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or 'swim' to swim across.\n: "
        )
        .strip()
        .lower()
    )
    if choice2 == "wait":
        choice3 = (
            input(
                "You arrive at the island unharmed. There is a house with 3 doors: red, yellow, and blue. Which color do you choose?\n: "
            )
            .strip()
            .lower()
        )
        if choice3 == "yellow":
            print("\nYou found the treasure! You win!")
        elif choice3 == "red":
            print("\nIt's a room full of fire. Game Over.")
        elif choice3 == "blue":
            print("\nYou enter a room of beasts. Game Over.")
        else:
            print("\nYou chose a door that doesn't exist. Game Over.")
    else:
        print("\nYou get attacked by an angry trout. Game Over.")
else:
    print("\nYou fell into a hole. Game Over.")
