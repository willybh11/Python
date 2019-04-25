import turtle
import time

def goRight():
	global hor
	hor = 1 if hor != 1 else 0

def goLeft():
	global hor
	hor = -1 if hor != -1 else 0

def jump():
	global yv
	yv += 5 * gravity

def revgrav():
	global gravity
	gravity = -1 * gravity
	global T
	if gravity == -1:
		T.pencolor('blue')
	elif gravity == 1:
		T.pencolor('red')

def teleport():
	global tele
	tele = not tele


if 1:
	window = turtle.Screen()
	window.setup(1365,720)
	T = turtle.Turtle()
	T.shape('circle')
	T.pencolor('red')
	xv = 0
	yv = 0
	tele = False
	hor = 0
	gravity = 1

	walls = turtle.Turtle()
	walls.tracer(0,0)
	walls.penup()
	walls.goto(-600,-300)
	walls.pendown()
	walls.fd(1200)
	walls.penup()
	walls.ht()
	walls.penup()
	walls.goto(-600,-300)
	walls.seth(90)
	walls.pendown()
	walls.fd(600)
	walls.penup()
	walls.goto(600,-300)
	walls.pendown()
	walls.fd(600)
	walls.penup()
	walls.goto(600,300)
	walls.seth(180)
	walls.pendown()
	walls.fd(1200)
	walls.penup()
	walls.ht()
	turtle.update()	# setup borders

window.onkey(goRight,"d")
window.onkey(goLeft,"a")
window.onkey(jump,"w")
window.onkey(revgrav,"r")
window.onkey(teleport,"t")
window.listen()

while True:
	time.sleep(1/20)
	if hor != 0:
		xv += (hor * 0.5) - xv
	else:
		xv = xv*.999
	yv = yv - (0.01 * gravity)
	
	yv = yv*.99
	if T.ycor() + yv > 300 or T.ycor() + yv <= -300:
		yv = -0.9 * yv
		T.sety(300*(-1 if T.ycor() < 0 else 1))
	if T.xcor() + xv > 600 or T.xcor() + xv < -600:
		if tele == False:
			xv = xv * -1
			hor = -1 * hor
			T.setx(600*(-1 if T.xcor() < 0 else 1))
		elif tele == True:
			T.pu()
			T.setx(T.xcor()*-1)
			T.pd()
	T.goto(T.xcor()+xv,T.ycor()+yv)
	turtle.update()
