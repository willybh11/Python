import turtle

w = turtle.Screen()
T = turtle.Turtle()
T.speed(0)
turtle.tracer(0,0)

for i in range(1000):
	for j in range(4):
		T.fd(200)
		T.lt(90)
	T.lt(1)
	if i % 1 == 0:
		turtle.update()
w.exitonclick()