import random
secret = random.randint(1,50)
attempt = 0
max_attempts = 5
has_won = False
print("Welcome to the Number Guess Game")
print("I'm thinking of a number between 0 and 50")
print("")
while attempt < max_attempts and not has_won:
    guess = int(input("\nEnter your guess: "))
    attempt += 1
    if guess == secret:
        print("Congratulations, you guessed the number!")
        has_won = True
    else:
        difference = abs(guess - secret)
        if difference <= 5:
            hint = "Hot!"
        elif difference <=10:
            hint = "Warm!"
        elif difference <= 15:
            hint = "Cold!"
        else:
            hint = "Ice Cold!"
        print(f"Wrong guess! Hint: {hint}")
        remaining_lives = max_attempts - attempt
        if remaining_lives > 0:
            print("Remaining hearts: ", end="")
            for _ in range(remaining_lives):
                print("*", end=" ")
            print()
if not has_won:
    print(f"/nGame Over! The secret number was {secret}")
            