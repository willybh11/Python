import turtle

window = turtle.Screen()

w = turtle.Turtle()
h = turtle.Turtle()
w.rt(75)
w.fd(200)
w.lt(157.5)
w.fd(100)
w.rt(150)
w.fd(100)
w.lt(157.5)

h.penup()
h.setpos(w.xcor()+74,w.ycor())
h.pendown()
h.lt(90)

w.fd(195)
h.fd(195)
w.bk(92)
h.bk(92)
w.rt(90)
h.lt(90)
w.fd(37)
h.fd(37)

window.exitonclick()
