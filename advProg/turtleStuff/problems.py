#Draw a square
#Draw a circle with a second turtle
#Repeat steps 1 and 2 with a different color background, different turtle color and shape
#Draw a circle out of squares
#Draw your initials
#Draw a flower
import turtle
def main():
	window = turtle.Screen()
	a = turtle.Turtle()
	b = turtle.Turtle()
	c = turtle.Turtle()

	for i in range(4): 	#p1
		a.fd(50)
		a.lt(90)

	b.circle(50,360)	#p2

	a.shape('square') 	#p3
	window.bgcolor('lightblue')
	a.pencolor('red')

	for degree in range(360):#p4
		c.speed(0)
		for i in range(4): 	#p1
			c.fd(20	)
			c.lt(90)
		c.lt(1)

	b.circle(50,360) 	#p5
	if i < 0:
		window.clear()



	window.exitonclick()


main()	



