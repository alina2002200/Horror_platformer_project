import pygame
import pygame.draw
import sys
from platforms import *

pygame.init()
font = pygame.font.Font(None, 60)
font1 = pygame.font.Font(None, 30)
FPS = 70
width = 800
length = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
# creating display
screen = pygame.display.set_mode((width, length))
clock = pygame.time.Clock()
finished = False


def level_read(file_name):
    file = open(file_name, 'r')
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


def menu(screen):
    pygame.mixer.music.load('Jungle.mp3')
    pygame.mixer.music.play()
    forest_surf = pygame.image.load('forest.jpg')
    forest_rect = forest_surf.get_rect(
        bottomright=(width, length))
    screen.blit(forest_surf, forest_rect)
    tlevel_1 = font.render('Level 1', True, BLACK, WHITE)
    screen.blit(tlevel_1, (175, 50))
    tlevel_2 = font.render('Level 2', True, BLACK, WHITE)
    screen.blit(tlevel_2, (175, 150))
    tlevel_3 = font.render('Level 3', True, BLACK, WHITE)
    screen.blit(tlevel_3, (175, 250))
    tlevel_4 = font.render('Level 4', True, BLACK, WHITE)
    screen.blit(tlevel_4, (175, 350))
    tlevel_5 = font.render('Level 5', True, BLACK, WHITE)
    screen.blit(tlevel_5, (175, 450))
    tlevel_6 = font.render('Level 6', True, BLACK, WHITE)
    screen.blit(tlevel_6, (475, 50))
    tlevel_7 = font.render('Level 7', True, BLACK, WHITE)
    screen.blit(tlevel_7, (475, 150))
    tlevel_8 = font.render('Level 8', True, BLACK, WHITE)
    screen.blit(tlevel_8, (475, 250))
    tlevel_9 = font.render('Level 9', True, BLACK, WHITE)
    screen.blit(tlevel_9, (475, 350))
    tlevel_10 = font.render('Level 10', True, BLACK, WHITE)
    screen.blit(tlevel_10, (475, 450))
    tsettings = font.render('Settings', True, BLACK, WHITE)
    screen.blit(tsettings, (300, 525))


def quit_draw():
    tquit = font.render('Quit', True, WHITE, BLACK)
    screen.blit(tquit, (700, 0))


def quit_check(event, screen):
    x, y = event
    if x > 700 and x < 790 and y > 0 and y < 44:
        menu(screen)


def menu_choice(screen):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                x, y = i.pos
                if x > 175 and x < 320 and y > 50 and y < 94:
                    all = level_read('level_1.txt')
                    screen.fill(WHITE)
                    frame_draw(all)
                    quit_draw()
                    pygame.mixer.music.pause()
                    pygame.display.update()
                if x > 175 and x < 320 and y > 150 and y < 194:
                    all = level_read('level_2.txt')
                    screen.fill(WHITE)
                    frame_draw(all)
                    quit_draw()
                    pygame.mixer.music.pause()
                    pygame.display.update()
                if x > 175 and x < 320 and y > 250 and y < 294:
                    all = level_read('level_3.txt')
                    screen.fill(WHITE)
                    frame_draw(all)
                    quit_draw()
                    pygame.mixer.music.pause()
                    pygame.display.update()
                if x > 175 and x < 320 and y > 350 and y < 394:
                    all = level_read('level_4.txt')
                    screen.fill(WHITE)
                    frame_draw(all)
                    quit_draw()
                    pygame.mixer.music.pause()
                    pygame.display.update()
                if x > 175 and x < 320 and y > 450 and y < 494:
                    all = level_read('level_5.txt')
                    screen.fill(WHITE)
                    frame_draw(all)
                    quit_draw()
                    pygame.mixer.music.pause()
                    pygame.display.update()
                if x > 475 and x < 620 and y > 50 and y < 94:
                    all = level_read('level_6.txt')
                    screen.fill(WHITE)
                    frame_draw(all)
                    quit_draw()
                    pygame.mixer.music.pause()
                    pygame.display.update()
                if x > 475 and x < 620 and y > 150 and y < 194:
                    all = level_read('level_7.txt')
                    screen.fill(WHITE)
                    frame_draw(all)
                    quit_draw()
                    pygame.mixer.music.pause()
                    pygame.display.update()
                if x > 475 and x < 620 and y > 250 and y < 294:
                    all = level_read('level_8.txt')
                    screen.fill(WHITE)
                    frame_draw(all)
                    quit_draw()
                    pygame.mixer.music.pause()
                    pygame.display.update()
                if x > 475 and x < 620 and y > 350 and y < 394:
                    all = level_read('level_9.txt')
                    screen.fill(WHITE)
                    frame_draw(all)
                    quit_draw()
                    pygame.mixer.music.pause()
                    pygame.display.update()
                if x > 475 and x < 620 and y > 450 and y < 494:
                    all = level_read('level_10.txt')
                    screen.fill(WHITE)
                    frame_draw(all)
                    quit_draw()
                    pygame.mixer.music.pause()
                    pygame.display.update()
                if x > 300 and x < 475 and y > 525 and y < 569:
                    all = level_read('settings.txt')
                    screen.fill(WHITE)
                    frame_draw(all)
                    quit_draw()
                    pygame.mixer.music.pause()
                    pygame.display.update()
                quit_check(i.pos, screen)
                pygame.display.update()
    pygame.display.update()


menu(screen)
while not finished:
    clock.tick(FPS)
    menu_choice(screen)
pygame.quit()
