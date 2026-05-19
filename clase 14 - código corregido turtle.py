import turtle
import random

def dibujar_circulos():
    colores = ['red', 'green', 'blue', 'yellow', 'purple']
    turtle.speed(10)

    for i in range(10):
        turtle.penup()
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        turtle.goto(x, y)
        turtle.pendown()

        color = random.choice(colores)
        turtle.color(color)
        radio = random.randint(10, 50)
        turtle.begin_fill()
        turtle.circle(radio)
        turtle.end_fill()

def mover_tortuga(distancia):
    angulo = random.randint(0, 360)
    turtle.setheading(angulo)
    turtle.forward(distancia)

def main():
    turtle.bgcolor("black")
    turtle.title("Dibujo Aleatorio")
    dibujar_circulos()

    for _ in range(5):
        mover_tortuga(100)
        dibujar_circulos()

    turtle.hideturtle()
    turtle.done()

main()