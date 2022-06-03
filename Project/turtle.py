# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 11:52:55 2022

@author: Asus
"""

# minimax algo here:
# def minimax()

import turtle

screen = turtle.Screen()

screen.bgcolor('lightblue')

player = turtle.Turtle()

player.color('blue')

player.shape('turtle')

ai = player.clone()

ai.color('red')

player.penup()

player.goto(-250, 100)

ai.penup()

ai.goto(250, 100)

true = 1

while true == 1:

    steps = screen.numinput("Enter steps:",100)
    
    player.forward(10*steps)
    if(player.pos()==ai.pos()):
        screen.title("Player lost the game!")
        break
    if(player.pos()>ai.pos()):
        screen.title("Player won the game!")
        break
    
    # from minimax:
    # steps_ai = minimax()
    
    steps_ai = screen.numinput("Enter steps:",100)
    
    ai.backward(steps_ai*10)
    if(player.pos()==ai.pos()):
        screen.title("Player lost the game!")
        break
    if(player.pos()>ai.pos()):
        screen.title("Player won the game!")
        break
    
    

turtle.done()