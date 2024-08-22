import pygame
from pygame import MOUSEBUTTONDOWN

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
done = False
white = pygame.Color(255,255,255)
time = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == MOUSEBUTTONDOWN:
            if time == 0:
                point1 = pygame.mouse.get_pos()
            else:
                point2 = pygame.mouse.get_pos()
            time += 1
            if time >=2:
                pygame.draw.line(screen,white,point1,point2)
                time = 0
    pygame.display.update()
pygame.quit()

