# Sarah Abdeen
# Project 1
# Lab 3
# October 30, 2023

# import random in order to generate a number within 'randomNumber'
import random

def main():
    guessingGame()

def guessingGame():
    while True:
        randomNumber = random.randint(1, 100)
        count = 0
# keep count of the amount of tries it takes to get the number
        while True:
            userInput = getUserInput()
            count += 1
# the output in which if the user gets it right or wrong
            if userInput == randomNumber:
                print(f"Congrats! It took you {count} tries to guess that the number is {randomNumber}")
                break
            elif userInput > randomNumber:
                print("Too high, try again")
            else:
                print("Too low, try again")

# option to continue playing if the user would like to
        restart = input("Would you like to play the guessing game again? (yes/no): ")
        if restart.lower() != "yes":
            print("Thanks and I hope you play again soon!")
            break

# function in which the user gives input and also determines if the number meets the range
def getUserInput():
    while True:
        try:
            userInput = int(input("Pick and guess a number between 1 and 100: "))
            if 1 <= userInput <= 100:
                return userInput
            else:
                print("Choose a number that is between 1 and 100")
        except ValueError:
            print("Try a different number.")

if __name__ == "__main__":
    main()
