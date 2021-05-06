#Game1

#Colors of lines:
#b = Blue, r = Red, g = Green, p = Purple

import pygame, sys
from pygame.locals import *
pygame.init()

#Color
Silver = (192, 192, 192)
Blue = (0, 0, 255)
Purple = (125, 0, 120)
Red = (255, 0, 0)
Green = (0, 255, 0)

###
x = 300
y = 300
Width = 800
Height = 600
Vel = 20
linecolor = Blue

#Display
DISPLAYSURF = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Press B-G-R-P to Change Color')
DISPLAYSURF.fill(Silver)


#sound
pygame.mixer.music.load('tetrisb.mid')
pygame.mixer.music.play(-1, 0.0)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
        mx, my = pygame.mouse.get_pos()
        if keys[pygame.K_p]:
            linecolor = Purple
        if keys[pygame.K_r]:
            linecolor = Red
        if keys[pygame.K_g]:
            linecolor = Green
        if keys[pygame.K_b]:
            linecolor = Blue
    DISPLAYSURF.fill(Silver)
    pygame.draw.line(DISPLAYSURF, linecolor, (1, my), (Width-1, my), 5)
    pygame.draw.line(DISPLAYSURF, linecolor, (mx, 1), (mx, Height-1), 5)
    pygame.display.update()
