from random import randint
print("Hello to my Guessing Game".center(50,"_"))
winning_number = randint(1,10)
tries = 5
while tries > 0:
	user_number = int(input("Write your Number: "))
	tries = tries - 1
	if user_number == winning_number:
		print("Congratilation You Won!!!")
		quit()
	elif user_number != winning_number:
		print("Wrong Choice :( ")
		print("#"*20)
	if tries == 1:
		print("Be careful This Is The Last Try")
		print("Hint".center(50,"_"))
		if winning_number%2 == 0:
			print("The Number is pair")
		else:
			print("The Number is Odd")
else:
	print(f'The winning number is {winning_number}')
	print("Tries Have over :( ")
