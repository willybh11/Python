import turtle
turtle.setup(200,20)

window = turtle.Screen()
window.bgcolor('black')
T = turtle.Turtle()
T.ht()
T.pencolor('orange')
T.speed(0)
turtle.setup(100,100)


T.tracer((0,0)
for degree in range(360):
	for side in range(4):
		T.fd(20)
		T.lt(90)
	T.lt(1)
turtle.update()
window.exitonclick()
