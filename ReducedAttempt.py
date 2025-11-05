import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 20.")
    print("You have only 5 attempts. Good luck!\n")

    number_to_guess = random.randint(1, 20)
    attempts_left = 5

    while attempts_left > 0:
        try:
            guess = int(input(f"Attempt {6 - attempts_left}/5 - Enter your guess: "))
            
            if guess < 1 or guess > 20:
                print("Please guess within the range 1–20.")
                continue

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"🎉 Correct! You guessed it with {attempts_left} attempts left.")
                break

            attempts_left -= 1

            if attempts_left == 0:
                print(f"\n❌ Out of attempts! The correct number was {number_to_guess}. Better luck next time!")
            else:
                print(f"You have {attempts_left} attempts remaining.\n")

        except ValueError:
            print("Please enter a valid number.\n")

if __name__ == "__main__":
    guess_the_number()
