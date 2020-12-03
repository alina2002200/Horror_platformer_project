import pygame
import pygame.draw
from platforms import *
pygame.init()
font = pygame.font.Font(None, 50)
font1 = pygame.font.Font(None, 30)
FPS = 70
width = 800
length = 600
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
# creating display
screen = pygame.display.set_mode((width, length))
clock = pygame.time.Clock()
finished = False


def level_read():
    file = open('level_5.txt', 'r')
    plat = []
    for line in file:
        a = line.split()
        x_cord, y_cord, p_width, p_length = a
        plat.append(Platform(screen, width, length, x_cord, y_cord, p_width, p_length))
    file.close()
    return plat


def frame_draw(plat):
    for i in plat:
        pygame.draw.rect(screen, GREEN, i.rect)


while not finished:
    clock.tick(FPS)
    screen.fill(WHITE)
    all = level_read()
    frame_draw(all)
    pygame.display.update()
pygame.quit()