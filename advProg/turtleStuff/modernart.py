import turtle

def main():
#Initialize screen and turtle
	window = turtle.Screen()
	window.setup(1365,720)
	window.bgcolor('black')
	T = turtle.Turtle()
	T.ht()
	T.speed(0)
	T.tracer(0,0)

#Initialize rainbow
	rainbow = ['green','blue','indigo','violet','red','orange','yellow']

#Actual function
	for deg in range(1,362):	#Repeat per degree
		for side in range(6):	#Repeat per side (of hexagon)
#Draw the shape
			T.pendown()
			if side < ( 3 if (deg > 355) else 2 ):	T.penup()	#Remove unintended overlap and unnecessary sides
			elif side in (2,3):
				T.pencolor(rainbow[((deg / 51) % 7 - 1) % 7])
			elif side == 4:			#Grey mid-section
				if deg % 2 == 0:	#Alternate every other line
					T.pencolor('gray')
				else:	T.pencolor('LightSteelBlue')
			else:	T.pencolor( rainbow[(deg / 51) % 7] )	#Make normal color

			T.forward(160)	#Draw the hexagon
			T.left(60)
		T.left(1)	#Onto the next degree!
		#if deg % 25 == 0 or deg == 361:	#un-comment this if you want it to run faster
		turtle.update()
	window.exitonclick()
	
main()