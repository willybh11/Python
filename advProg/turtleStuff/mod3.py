import turtle

def main():
	window = turtle.Screen()
	window.setup(1365,720)
	window.bgcolor('black')
	a = turtle.Turtle()
	b = turtle.Turtle()
	c = turtle.Turtle()
	d = turtle.Turtle()
	e = turtle.Turtle()
	turtles = [a,b,c,d,e]
	for T in turtles:
		T.tracer(0,0)
		T.ht()
		T.speed(0)
		T.goto(-5,0)

	a.bk(480)
	b.bk(270)

	d.fd(270)
	e.fd(480)

	Aturtles = [a,c,e]
	Bturtles = [b,d]

	rainbow = ['green','blue','indigo','violet','red','orange','yellow']

	for deg in range(1,362):
		for T in turtles:
			for side in range(6):	
				T.pendown()
				if side < ( 3 if (deg > 355) else 2 ):	T.penup()
				elif side in (2,3):
					T.pencolor(rainbow[((deg / 51) % 7 - 1) % 7])
				elif side == 4:			
					if deg % 2 == 0:	
						T.pencolor('gray')
					else:	T.pencolor('LightSteelBlue')
				else:	T.pencolor( rainbow[(deg / 51) % 7] )

				if T in Aturtles:
					if T == c:
						T.fd(30)
					T.fd(70)
				if T in Bturtles:	T.fd(30)
				T.left(60)
			T.left(1)
		if deg % 8	 == 0:
			turtle.update()
			

	window.exitonclick()
	
main()