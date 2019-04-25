import turtle

window = turtle.Screen()
window.setup(1365,720)
T = turtle.Turtle()

T.ht()
T.speed(0)
T.tracer(0,0)

for i in range(325):
    T.circle(i*1.01)
    T.left(5)
    if i%2 == 0:
    	turtle.update()
window.exitonclick()