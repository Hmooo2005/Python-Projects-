from random import *

user_score = 0
computer_score = 0
choices_list = ["Rock", "Paper", "Scissor"]
tries = 0

while True:
    user_enter = input("Type Rock/Paper/Scissor or Q to quit the game: ")
    random_index = randint(0,2)
    computer_choice = choices_list[random_index]
    if user_enter.upper() == "Q":
        break
    elif user_enter.capitalize() in choices_list:
        print(f"Computer picked {computer_choice}")
        if user_enter.capitalize() == computer_choice:
            print("Drawn!!")
            tries += 1
        elif user_enter.capitalize() != computer_choice:
            if (user_enter.capitalize() == "Rock") and (computer_choice == choices_list[2]):
                print("You win!!")
                user_score += 1
                tries += 1
            elif (user_enter.capitalize() == "Rock") and (computer_choice == choices_list[1]):
                print("Computer win!!")
                computer_score += 1
                tries += 1
            elif (user_enter.capitalize() == "Scissor") and (computer_choice == choices_list[1]):
                print("You win!!")
                user_score += 1
                tries += 1
            elif (user_enter.capitalize() == "Scissor") and (computer_choice == choices_list[0]):
                print("Computer win!!")
                computer_score += 1
                tries += 1
            elif (user_enter.capitalize() == "Paper") and (computer_choice == choices_list[0]):
                print("You win!!")
                user_score += 1
                tries += 1
            elif (user_enter.capitalize() == "Paper") and (computer_choice == choices_list[2]):
                print("Computer win!!")
                computer_score += 1
                tries += 1
        print("#"*50)
        print(f"#Your score is     ==> {user_score}")
        print(f"#computer score is ==> {computer_score}")
        print("#"*50)
    else:
        print("please write one of the three choices")

print(f"You Have play {tries} time \nYou Have win {user_score}")
print(f"You Have Draw {tries-(user_score+computer_score)}\nYour Win Percentage is {(user_score/tries)*100:.2f}%")
print("GoodBye!!")