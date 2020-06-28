import random
import curses

#Initialising The screen
s=curses.initscr()

#Setting Cursor to Zero
curses.curs_set(0)

#Setting Width and Height
sh, sw=s.getmaxyx()

#Creating a new Window
w= curses.newwin(sh,sw,0,0)
w.keypad(1)
w.timeout(100)

snk_x=sw/4
snk_y=sh/2

#Creating the body part for Snake
snake=[
    [snk_y,snk_x],
    [snk_y,snk_x-1],
    [snk_y,snk_x-2]
]

#Creating Food for the Snake
food=[sh/2,sw/2]
w.addch(food[0],food[1], curses.ACS_PI)

#Starting The Start
key =curses.KEY_RIGHT

#Checking for the input from Keyboard
while True:
    next_key=w.getch()
    key= key if next_key==-1 else next_key

#To check if Player lost the game
    if snake[0][0] in [0,sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]:
        curses.endein()
        quit()

#New head of the snake
new_head= [snake[0][0], snake[0][1]]

#Y-Axis
if key==curses.KEY_DOWN:
    new_head[0]+=1
if key == curses.KEY_Up:
    new_head[0] -= 1

#X-Axis
if key == curses.KEY_LEFT:
    new_head[1] -= 1
if key == curses.KEY_RIGHT:
    new_head[1] += 1

snake.insert(0,new_head)

#To Check if snake got the food
if snake[0]==food:
    food=None
    while food is None:
        #New Location of the food
        nf=[
            random.randint(1, sh-1),
            random.randint(1, sw-1)
        ]
        food=nf if nf not in snake else None
    w.addch(food[0],food[1],curses.ACS_PI)
else:
    tail= snake.pop()
    w.addch(tail[0],tail[1],' ')

#Adding to the Snake
w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)