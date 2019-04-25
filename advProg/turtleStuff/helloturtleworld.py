import turtle
import time

window = turtle.Screen()

def test():
	allturtles = []
	for i in range(4):
			t1 = turtle.Turtle()
			t2 = turtle.Turtle()
			t3 = turtle.Turtle()
			t4 = turtle.Turtle()
			t1.speed(0)
			t2.speed(0)
			t3.speed(0)
			t4.speed(0)
			t1.penup()
			t2.penup()
			t3.penup()
			t4.penup()
			t1.setx(50*i)
			t1.sety(50*i)
			t2.setx(50*i)
			t2.sety(-50*i)
			t3.setx(-50*i)
			t3.sety(50*i)
			t4.setx(-50*i)
			t4.sety(-50*i)
			t1.pendown()
			t2.pendown()
			t3.pendown()
			t4.pendown()
			t1.ht()
			t2.ht()
			t3.ht()
			t4.ht()

			allturtles.append([t1,t2,t3,t4])

	start = time.clock()
	for degrees in range(360):
		for line in allturtles:
			for t in line:
				for repeat in range(2):
					t.fd(200)
					t.lt(90)
				t.lt(1)

	print "That took %f seconds." %(time.clock()-start)
test()

window.exitonclick()
