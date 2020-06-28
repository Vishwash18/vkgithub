import turtle

#Initilazing the screen
wn=turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Scoring Initilazing
score_a=0
score_b=0

#Creating Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)#Animation Speed of paddle
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()  #Avoiding of Drawing the line when Movement occurs
paddle_a.goto(-350,0)

#Creting Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)#Animation Speed of paddle
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)#Editing the required shape
paddle_b.penup()
paddle_b.goto(350,0)

#Creatig The Ball
Ball=turtle.Turtle()
Ball.speed(0)#Animation Speed of paddle
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)
Ball.dx=0.2  #Movement of the ball
Ball.dy=0.2

#Scoring
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,220)
pen.write("Player A: 0  Player B: 0",align="center",font=("Arial", 18, "bold"))

#Creating the functions
def paddle_a_up():
    y=paddle_a.ycor() #Getting the y-coord
    y+=35 #increasing the value to mv=ov eth paddle
    paddle_a.sety(y) #setting the new coordinates to the previous value
def paddle_a_down():
    y=paddle_a.ycor()
    y-=35
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    y+=35
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y-=35
    paddle_b.sety(y)

#Making input for the keyboard
wn.listen()#Input from the keyboard
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
#Main Loop
while True:
    wn.update()  #Update the screen every keypress

    #Moving the ball
    Ball.setx(Ball.xcor()+Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    #Border Checking
    if Ball.ycor()>290:
        Ball.sety(290)
        Ball.dy*=-1 #Reverse the Direction

    if Ball.ycor()<-290:
        Ball.sety(-290)
        Ball.dy*=-1

    if Ball.xcor()>390:
        Ball.goto(0,0)
        Ball.dx*=-1
        score_a+=1   #Incresing the Score
        pen.clear()  #to clear the Previous Text
        pen.write("Player A: {} Player B: {}".format(score_a, score_b) ,align="center", font=("Arial", 18, "bold"))

    if Ball.xcor()<-390:
        Ball.goto(0,0)
        Ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Ariel", 18, "bold"))

    #Collisions of Ball and Paddle
    if Ball.xcor()>330 and Ball.xcor()<340 and(Ball.ycor()<paddle_b.ycor() +50 and Ball.ycor()>paddle_b.ycor() -50):
        Ball.setx(330)
        Ball.dx*=-1
    if Ball.xcor()<-330 and Ball.xcor()>-340 and(Ball.ycor()<paddle_a.ycor() +50 and Ball.ycor()>paddle_a.ycor() -50):
        Ball.setx(-330)
        Ball.dx*=-1