import turtle
import time

window = turtle.Screen()

n = 2

while 1:
	n = n * 4
	print n
	turtles = []

	for i in range(n):
		turtles.append(turtle.Turtle()) # len(turtles) always == n

	for i in turtles:
		if 1:
			i.ht()
			i.pencolor('blue')
			i.shape('circle')
			i.speed('fastest')
			i.pu()

		turn = (360 / n) if ( turtles.index(i) % 2 ) != 0 else 0

		i.seth(((360 / n / 2) + turn) if turtles.index(i) > 1 else turn)
		i.st()
		i.speed('slow')
		i.pd()
		i.fd(100)
		i.bk(200)

	for i in turtles:
		i.ht()
	
		


window.exitonclick()
