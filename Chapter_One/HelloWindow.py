import pygame
pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
done = False
white = pygame.Color(255,255,255)
def draw_star(x,y,size):
    pygame.draw.rect(screen,white,(x,y,size,size))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        draw_star(121,320,15)
        pygame.display.update()
pygame.quit()