'''
Creating the Ball class for the game of Pong!
'''

import pygame

class Ball:  
    VELOCITY = 5
    COLOR = (255,255,255)

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.r = radius
        self.dx = self.VELOCITY
        self.dy = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x,self.y), self.r)

    def move(self):
        self.x += self.dx
        self.y += self.dy