import pygame
from pygame.examples.video import backgrounds
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
done = False
background = pygame.image.load('../Images/20240613-202834-2.jpeg')
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(background,(0,0))
    pygame.display.update()
pygame.quit()

