# Write your code here :-)
import turtle as t

window = t.Screen()
window.title("Pong")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)

p1=t.Turtle()
p1.speed(0)
p1.shape("sqaure")
p1.color("blue")
p1.shapesize(strech_wid=5, stretch_len=1)
p1.penup()
p1.goto(-350,0)

p2=t.Turtle()
p2.speed(0)
p2.shape("sqaure")
p2.color("blue")
p2.shapesize(strech_wid=5, stretch_len=1)
p2.penup()
p2.goto(-350,0)

ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2
