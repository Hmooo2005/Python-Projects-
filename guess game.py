from random import *

top_number = input("Type the top range of the numbers: ")

if top_number.isdigit():
    top_number = int(top_number)
    if top_number <= 0:
        print("please write a number larger than zero")
        quit()
elif not top_number.isdigit():
    print("please write a number")
    quit()

win_number = randint(1, top_number)
tries = 0
while True:
    guess_number = input("write your guess number: ")
    tries += 1
    if guess_number.isdigit():
        guess_number = int(guess_number)
    elif not guess_number.isdigit():
        print("please write a number")
        continue
    if guess_number == win_number:
        print("Congratilation!!")
        break
    elif guess_number != win_number:
        print("Wrong Guess")
        if guess_number > win_number:
            print("Your number is begger than the winning number!")
        elif guess_number < win_number:
            print("Your number is less than the winning number!")

if guess_number == win_number:
    print(f"You got it in {tries} guesses")