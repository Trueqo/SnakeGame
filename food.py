from turtle import Turtle

import random

#Aleatoria random

class Food(Turtle): 
    
    def __init__(self):
        super().__init__() #Herede de turtle y coja todo lo disponible.
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-200, 200) #esto me va a generar un numero entero
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)
