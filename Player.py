'''
Creating the Player class for the game of Pong!
'''
import pygame


class Player:
    COLOR = (255,255,255)
    VELOCITY = 3.5
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x,self.y,self.width,self.height))

    def move(self, up = True):
        if up:
            self.y -= self.VELOCITY
        else: self.y += self.VELOCITY