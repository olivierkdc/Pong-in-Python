'''
Creating the Ball class for the game of Pong!
'''

import pygame

class Ball:  
    VELOCITY = 10
    COLOR = (255,255,255)

    def __init__(self, x, y, radius):
        #for resetting the ball
        self.set_x = x
        self.set_y = y

        #to get current ball position
        self.x = x
        self.y = y

        #ball size, speed
        self.r = radius
        self.dx = self.VELOCITY
        self.dy = 0

    def initialize(self):
        self.x  = self.set_x
        self.y = self.set_y
        self.dx = -self.dx
        self.dy = 0


    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x,self.y), self.r)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    