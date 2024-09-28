# import modules necessery for the game

import random #for the random place of the food
import curses #for the shape of the snake

#creat our screen
screen = curses.initscr()

#hide the mouse cursor
curses.curs_set(0) #chose 0 to hide

#get max high and max width
screen_hight, screen_width = screen.getmaxyx()

#creat a window
window = curses.newwin(screen_hight, screen_width, 0, 0)

#allowed window to receive input from keyboard
window.keypad(1)

#set delay for updating the screen
window.timeout(100)

#set x,y cordinates for the position of the snake head
snake_x = screen_width//4
snake_y = screen_hight//2

#set position of the snake body
snake = [[snake_y, snake_x], [snake_y, snake_x-1], [snake_y, snake_x-2]]

#creat the food in the middle of the screen
food = [screen_hight // 2, screen_width // 2]
window.addch(food[0], food[1], curses.ACS_STERLING) #curses.ACS_STERLING: THE FOOD SHAPE IS THE BRITICH POUND

#Set move direction at the begining to the right
key = curses.KEY_RIGHT

#creat game loop that loop forever until player loses or quit the game
while True:
	#get the key that will be pressed by the user
	next_key = window.getch()
	
	#if user did not enter input key remains same
	#else key will be set to the new pressed key
	key = key if next_key == -1 else next_key
	
	#check if snake hit the wall or him self
	if snake[0][0] in [0, screen_hight] or 		snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
		curses.endwin() #close the window
		quit() #exit the program
		
	#set the new direction based on the direction of the snake head
	new_head = [snake[0][0], snake[0][1]]
	if key == curses.KEY_DOWN:
		new_head [0] += 1
	if key == curses.KEY_UP:
		new_head [0] -= 1
	if key == curses.KEY_RIGHT:
		new_head [0] += 1
	if key == curses.KEY_LEFT:
		new_head [0] -= 1
		
	#INSERT THE NEW HEAD TO THE FIRT POSITION OF SNAKE LIST
	snake.insert(0, new_head)
	
	#check if the snake ate the food
	if snake[0] == food:
		food = None #remove food if snake ate it
		
		#while food is remove generate new food in random place in screen
		while food == None:
			new_food = [random.randint(1, screen_hight-1),random.randint(1, screen_width-1)]
			food = new_food if new_food not in snake else None
		window.addch(food[0], food[1], curses.ACS_STERLING)
	else:
		tail = snake.pop()
		window.addch(tail[0], tail[1],' ')
	window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)














