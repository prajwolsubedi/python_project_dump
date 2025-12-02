import keyboard
import random

def get_user_guess():
    while True:
        try:
            return int(input("\nYour Guess: "))
        except ValueError:
            print("Please enter a valid number!")

def main():
    print("Press any key to start the game (or press 'c' to cancel)...")

    #Wait for key press

    event = keyboard.read_event()

    if event.name == 'c':
        print("Game cancelled.")
        return

    #Flush the keyboard buffer
    input()

    print("\nGame Started!")
    print("Guess the random number between 0 and 100")

    random_num = random.randint(0,100)
    attempts = 0

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess < random_num:
            print("Too low! Try again!")
        elif guess > random_num:
            print("Too high! Try again!")
        else:
            print(f"\nCongratulations! You guessed it in {attempts} attempts!")
            print(f"The number was {random_num}")
            break


if __name__ == "__main__":
    main()

