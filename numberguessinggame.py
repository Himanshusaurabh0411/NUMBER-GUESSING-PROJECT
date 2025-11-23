import random

def guess_number_game():
    number = random.randint(1, 100)

    max_chances = 5
    chances_taken = 0

    print("Welcome to HIMANSHU Gaming Store ")
    print("My computer is thinking of a number between 1 and 100.")

    print("You will get hints to guess the number:")
    print("If you guess the number above the actual number it will show too high")
    print("If You guess the number below the actual number it will show too low")

    print(f"You have {max_chances} attempts to guess it.")
    print("All the best , you are good to go")

    while chances_taken < max_chances:
        try:
            guess = int(input(f"\nAttempt No:{chances_taken + 1}: Enter your guess: "))
            chances_taken += 1

            if guess == number:
                print(f"\n Congrats, You have guessed the number {number} correctly in {chances_taken} tries")
                return

            elif guess < number:
                print("Too low , Try a higher number.")

            else:
                print("Too high , Try a lower number.")

        except ValueError:
            print("Invalid input")

    print("\nGame Over")
    print(f"You have to try again you are out of {max_chances} attempts.")
    print(f"The number my computer was thinking of was {number}.")

# Start the game
if __name__ == "__main__":
    guess_number_game()

