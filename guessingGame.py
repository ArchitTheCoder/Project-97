import random

# Title
print("Number Guessing Game\nGuess a number (between 1 and 10): ")

# Number
num = random.randint(0, 10)
chances = 0

# User Input
message = "Enter your guess: "
userNum = int(input(message))

# Logic
while chances < 5:
    if (userNum < num):
        print(f"Your guess was too low: Guess a number higher than {str(userNum)}")
        userNum = int(input(message))
        chances = chances + 1
    elif (userNum > num):
        print(f"Your guess was too high: Guess a number lower than {str(userNum)}")
        userNum = int(input(message))
        chances = chances + 1
    else:
        print("Congratulations YOU WON!!!")
        break

if not chances < 5:
    print(f"YOU LOSE!!! The number is {str(num)}")