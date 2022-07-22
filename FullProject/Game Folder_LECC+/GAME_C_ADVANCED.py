import winsound
import turtle
import math
from random import uniform
import time




turtle.title('C++ ADVANCED')


class Player(turtle.Turtle):
    def __init__(self, x, y, speed):
        turtle.Turtle.__init__(self)
        self.color('black')
        self.shape('turtle')
        self.speed = speed
        self.penup()
        self.goto(x,y)

    def turnLeft(self):
        self.left(30)

    def turnRight(self):
        self.right(30)

    def chkDist(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a**2) + (b**2))

        if distance < 30:

            winsound.Beep(440,50)
            self.setposition(uniform(-240,240),uniform(-240,240))
            other.setposition(uniform(-240,240),uniform(-240,240))
            return True
        else:
            return False

    def chkBoundary(self):
        if self.xcor() > 225:

            self.goto(225, self.ycor())
            self.left(uniform(0,90))
        if self.xcor() <-225:

            self.goto(-225, self.ycor())
            self.left(uniform(0,90))
        if self.ycor() > 225:

            self.goto(self.xcor(), 225)
            self.left(uniform(0,90))
        if self.ycor() <-225:
            self.goto(self.xcor(), -225)
            self.left(uniform(0,90))




window=turtle.Screen()
window.setup(600,600)
window.bgpic('LOGO_.png')
stop = False
speed = 7
scorelec = 0
score = 0

line = Player(-290, 290, 50)
line.shape('classic')
line.pensize(5)
line.pendown()

for i in range(4):
    line.forward(580)
    line.right(90)

line.hideturtle()


line2 = Player(-250, 250, 50)
line2.shape('classic')
line2.pensize(11)
line2.pendown()

for i in range(4):
    line2.forward(500)
    line2.right(90)

line2.hideturtle()




tr1 = Player(-10, -100, 10)
tr1.shapesize(1.5, 1.5, 1.5)
ourturtle = Player(10, 100, 1)
ourturtle.color('blue')
ourturtle.shapesize(1.5, 1.5, 1.5)


def left():
    ourturtle.left(30)

def right():
    ourturtle.right(30)

def speedUp():
    global speed
    speed += 1

def close():
    global stop
    stop = True







turtle.listen()
turtle.onkey(left,'Left' and 'a')
turtle.onkey(right,'Right' and 'd')
turtle.onkey(speedUp, 'Up' and 'w')
turtle.onkey(close,'q')

start = time.time()
while stop != True:

    turtle.onkey(left,'Left')
    turtle.onkey(right,'Right')
    turtle.onkey(speedUp, 'Up')
    turtle.onkey(close,'q')

    ourturtle.forward(speed)
    tr1.forward(5)

    tr1.chkBoundary()
    ourturtle.chkBoundary()



    if Player.chkDist(tr1, ourturtle):
       score += 1

    duration = time.time() - start
    print(duration)


    if (duration > 10) and (duration < 10.999):
        tr1.hideturtle()
        ourturtle.hideturtle()

        window.bgpic('question1advc.png')
        answer1=turtle.textinput("Question 1","STRING")

        if answer1=='char last_name[] = "Doe";':
            tr1.showturtle()
            ourturtle.showturtle()
            window.bgpic('LOGO_.png')
            scorelec += 1
            start = time.time()-11
            turtle.listen()
            turtle.onkey(left,'Left')
            turtle.onkey(right,'Right')
            turtle.onkey(speedUp, "Up")
            turtle.onkey(close,"q")



        else:
            tr1.showturtle()
            ourturtle.showturtle()
            window.bgpic('LOGO_.png')
            print("INCORRECT!")
            start = time.time()-11
            turtle.listen()
            turtle.onkey(left,'Left')
            turtle.onkey(right,'Right')
            turtle.onkey(speedUp, "Up")
            turtle.onkey(close,"q")




    if (duration > 20) and (duration < 20.999):
        tr1.hideturtle()
        ourturtle.hideturtle()
        window.bgpic('question2advc.png')
        answer2=turtle.textinput("Question 2","FOR LOOPS")

        if answer2=='for(i=0;i<10;i++){':
            tr1.showturtle()
            ourturtle.showturtle()
            window.bgpic('LOGO_.png')
            scorelec += 1
            start = time.time()-21
            turtle.listen()
            turtle.onkey(left,'Left')
            turtle.onkey(right,'Right')
            turtle.onkey(speedUp, "Up")
            turtle.onkey(close,"q")

        else:
            tr1.showturtle()
            ourturtle.showturtle()
            window.bgpic('LOGO_.png')
            print("INCORRECT!")
            start = time.time()-21
            turtle.listen()
            turtle.onkey(left,'Left')
            turtle.onkey(right,'Right')
            turtle.onkey(speedUp, "Up")
            turtle.onkey(close,"q")


    if (duration > 30) and (duration < 30.999):
        tr1.hideturtle()
        ourturtle.hideturtle()
        window.bgpic('question3advc.png')
        answer3=turtle.textinput("Question 3","WHILE LOOPS")

        if answer3=='if(array[i] > 10){':
            tr1.showturtle()
            ourturtle.showturtle()
            window.bgpic('LOGO_.png')
            scorelec += 1
            start = time.time()-31
            turtle.listen()
            turtle.onkey(left,'Left')
            turtle.onkey(right,'Right')
            turtle.onkey(speedUp, "Up")
            turtle.onkey(close,"q")

        else:
            tr1.showturtle()
            ourturtle.showturtle()
            window.bgpic('LOGO_.png')
            print("INCORRECT!")
            start = time.time()-31
            turtle.listen()
            turtle.onkey(left,'Left')
            turtle.onkey(right,'Right')
            turtle.onkey(speedUp, "Up")
            turtle.onkey(close,"q")





    if (duration > 40) and (duration < 40.999):
        tr1.hideturtle()
        ourturtle.hideturtle()
        window.bgpic('question4advc.png')
        answer4=turtle.textinput("Question 4","FUNCTIONS")

        if answer4=='void print_big(int number){':
            tr1.showturtle()
            ourturtle.showturtle()
            window.bgpic('LOGO_.png')
            scorelec += 1
            start = time.time()-41
            turtle.listen()
            turtle.onkey(left,'Left')
            turtle.onkey(right,'Right')
            turtle.onkey(speedUp, "Up")
            turtle.onkey(close,"q")

        else:
            tr1.showturtle()
            ourturtle.showturtle()
            window.bgpic('LOGO_.png')
            print("INCORRECT!")
            start = time.time()-41
            turtle.listen()
            turtle.onkey(left,'Left')
            turtle.onkey(right,'Right')
            turtle.onkey(speedUp, "Up")
            turtle.onkey(close,"q")



    if (duration > 50) and (duration < 50.999):
        tr1.hideturtle()
        ourturtle.hideturtle()
        window.bgpic('question5advc.png')
        answer5=turtle.textinput("Question 5","STATIC")

        if answer5=='total += num;':
            tr1.showturtle()
            ourturtle.showturtle()
            window.bgpic('LOGO_.png')
            scorelec += 1
            start = time.time()-51
            turtle.listen()
            turtle.onkey(left,'Left')
            turtle.onkey(right,'Right')
            turtle.onkey(speedUp, "Up")
            turtle.onkey(close,"q")

        else:
            tr1.showturtle()
            ourturtle.showturtle()
            window.bgpic('LOGO_.png')
            print("INCORRECT!")
            start = time.time()-51
            turtle.listen()
            turtle.onkey(left,'Left')
            turtle.onkey(right,'Right')
            turtle.onkey(speedUp, "Up")
            turtle.onkey(close,"q")



    if duration > 60:
        stop = True



percentage=(scorelec/5)*100


tr1.hideturtle()
ourturtle.hideturtle()

window.bgpic('white.png')
turtle.pencolor('red')
turtle.penup()
turtle.goto(0,160)
turtle.write("GAME IS OVER!", align = 'center',font=("Arial", 25,'bold'))
turtle.hideturtle()

turtle.penup()
turtle.goto(0,125)
turtle.write("You got total score: {} points.".format(str(score+scorelec)), align='center', font=("Arial",19,'bold'))
turtle.hideturtle()


turtle.penup()
turtle.goto(0,-30)
turtle.write("Correct answers--> {} out of 5.".format(str(scorelec)), align='center', font=("Arial",19,'bold'))


turtle.penup()
turtle.goto(0,-65)
turtle.write("You are {}% a good programmer !!!".format(str(percentage)), align='center', font=("Arial",19,'bold'))
turtle.hideturtle()


turtle.done()