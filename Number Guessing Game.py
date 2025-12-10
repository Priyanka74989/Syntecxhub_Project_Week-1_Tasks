import random
def get_difficulty():
    print("\nChoose Difficulty Level:")
    print("1. Easy   (1 - 20)")
    print("2. Medium (1 - 50)")
    print("3. Hard   (1 - 100)")

    while True:
        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            return 1, 20
        elif choice == "2":
            return 1, 50
        elif choice == "3":
            return 1, 100
        else:
            print("Invalid choice, try again.")

def play_game():
    low, high = get_difficulty()
    secret = random.randint(low, high)
    attempts = 0

    print(f"\nI'm thinking of a number between {low} and {high}. Start guessing!")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < secret:
                print("Too low! Try again.")
            elif guess > secret:
                print("Too high! Try again.")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                return attempts

        except ValueError:
            print("Please enter a valid number!")


def number_guessing_game():
    best_score = None

    while True:
        print("\n======= Number Guessing Game =======")
        attempts = play_game()

        # Track best (lowest) attempts
        if best_score is None or attempts < best_score:
            best_score = attempts
            print(f"New Best Score: {best_score} attempts!")

        print("\nDo you want to play again?")
        again = input("Type 'yes' to continue or anything else to exit: ").lower()

        if again != "yes":
            print("\nThanks for playing!")
            print(f"Your Best Score: {best_score} attempts")
            break

if __name__ == "__main__":
    number_guessing_game()