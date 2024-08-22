import pygame
from Mesh3D import  *
from pygame.locals import *
from OpenGL.GL import  *
pygame.init()
screen_width  = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height),DOUBLEBUF | OPENGL)
pygame.display.set_caption('Opengl in Python')
done = False
white = pygame.Color(255,255,255)
mesh = Mesh3D()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    mesh.draw()
    pygame.display.flip()
pygame.quit()