from random import randint
import pygame
GREEN = (0, 255, 0)

class Platform():
    def __init__(self, screen, width, length, x, y, pl_width, pl_length):
        self.x = float(x)
        self.y = float(y)
        self.pl_width = float(pl_width)
        self.pl_length = float(pl_length)
        self.screen = screen
        self.color = GREEN
        self.rect = pygame.Rect((self.x, self.y, self.pl_width, self.pl_length))