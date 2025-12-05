import random

print("Welcome to Kay's Number Guessing Game!")
while True:
    secret = random.randint(1, 50)

    attempts = 0
    max_attempts = 5
    
    print("I'm thinking of a number betwwn 1 and 50.")
    print(f"You have {max_attempts} attempts to guess it.")
# start the guessing loop
    while True:
        players_guess = input("Enter your guess: ")
# Handling invalid input 
        try:
            guess = int(players_guess)
        except ValueError:
            print("Invalid input: Please enter a number.")
            continue

        attempts += 1
# compare the guess with the generated secret number
        if guess == secret:
            print(f"Congratulations! You guessed right in {attempts} tries. The number was {secret}")
            break
        elif guess < secret:
            print("Number is too low, please try again.")
        else:
            print("Number is too high, please try again.")
            
#Handling the number of player's attempts.    
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {secret}")
            break
#The Play Again Feature 
    play_again = input("Do you want to play again?(Yes/No): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye.")
        break 
