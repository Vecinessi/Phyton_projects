import time
import turtle

# Configurando o pincel
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.speed(5)

# Fazendo o circulo vermelho
tartaruga.color("red")
tartaruga.begin_fill()
tartaruga.left(180)
tartaruga.circle(500, 7)
tartaruga.right(90)
tartaruga.circle(17, 180)
tartaruga.right(90)
tartaruga.circle(500, 7)
tartaruga.right(90)
tartaruga.circle(-80, 195)
tartaruga.end_fill()

# Contornando a Pokebola
tartaruga.color("black")
tartaruga.pensize(4)
tartaruga.left(180)
tartaruga.circle(80, 360)
tartaruga.left(90)
tartaruga.circle(500, 7.2)
tartaruga.right(90)
tartaruga.circle(18, 540)
tartaruga.right(90)
tartaruga.circle(500, 7)
tartaruga.pensize(2)

# Deixando o pincel invisivel para facilitar visualização
tartaruga.shape("blank")

time.sleep(2)
