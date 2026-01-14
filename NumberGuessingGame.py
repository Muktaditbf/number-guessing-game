import random
secret_number = random.randint(1, 100)

print("---------------------------------------------------------------")
print("---------------------------------------------------------------")
print("-------------Welcome to the Number Guessing Game!--------------")
print("---------------------------------------------------------------")
print("---------------------------------------------------------------")

while True:
    guess = input("Guess a number between 1 and 100 (or type 'exit' to quit): ")
    if guess.lower() == 'exit':
        print("Thanks for playing! Goodbye.")
        break
    try:
        guess = int(guess)
        if guess < 1 or guess > 100:
            print("Please guess a number within the range of 1 to 100.")
            continue
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the correct number!")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")