##NUMBER GUESSING GAME
import random

def number_guessing_game():
    print("Welvome to the NUmber Guessing Game!")
    print("You have 10 attempts to guess the number")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1,100)
    attempts = 10

    while attempts > 0:
        try:
            guess = int(input(f"Enter your guess ({attempts}) attempt(s) left: "))

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100\n")
                continue

            difference = abs(secret_number - guess)

            if difference == 0:
                print(f"Correct! You guessed the right number with {attempts} attempts remaining.")
                return
            elif difference <= 5:
                print("Warmer!\n")
            elif difference <= 20:
                print("Warm\n")
            elif difference <= 40:
                print("Cold\n")
            else:
                print("Colder\n") 

            attempts = attempts - 1    

        except ValueError:
            print("Invalid input! Please enter a number\n")

    print(f"Game Over! The correct number was {secret_number}") 

def main():
    while True:
        number_guessing_game()
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing!")
            break

main()        
