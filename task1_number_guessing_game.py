import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")
    
    secret_number = random.randint(1, 20)
    attempts = 5

    for i in range(attempts):
        print(f"\nAttempt {i+1} of {attempts}")
        
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == secret_number:
            print(f"Congratulations! You guessed it. The number was {secret_number}.")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

        if i == attempts - 1:
            print(f"\nGame Over! You've run out of attempts. The number was {secret_number}.")

while True:
    start_game()
    choice = input("Do you want to play again? (y/n): ").lower()
    if choice != 'y':
        print("Thanks for playing!")
        break