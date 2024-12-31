import random

# Generate a random number between 1 and 100
numberguess = random.randrange(1, 100)

print("Welcome to the Guess the Number game!")
print("I have selected a number between 1 and 100.")
print("Try to guess!")

attempts =0
while True:
# input the guess number
    user_guess = input("Enter your guess number : ")
    
    # Check if the input is a valid integer
    if not user_guess.isdigit():
        print(" enter a valid number.")
        continue
    
    user_guess = int(user_guess)
    
    attempts += 1
    
    #  the user's guess is correct chek it
    if user_guess < numberguess:
        print("Too low! Try again.")
    elif user_guess > numberguess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the correct number {numberguess} in {attempts} attempts!")
        break