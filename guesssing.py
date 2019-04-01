
import random as rand
import tensorflow
number = rand.randint(1,10)
tries = 1

user_name = input("Hello, what is your name?")

print("Hi, ",user_name)
choice = input("You want to play a game ? [Y/N]")
if choice == "N":
    print("Have a nice day")
if choice == "Y":
    guess = int(input("Guess number between 1 to 10"))
    if guess < number:
        print("Your guess is lower to the number")
    elif guess > number:
        print(" Your guess is higher")
    while guess != number:
        tries += 1
        guess = int(input("Try again: "))
        if guess < number:
            print(" guess higher...")
        elif guess > number:
            print("guess lower...")
        elif guess == number:
             print("You win :), the number is: ",number,"and you guessed in ",tries,"tries!" )