from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from ctypes import windll
import pygame
import sys


#----------------------------------Setup----------------------------------------
windll.shcore.SetProcessDpiAwareness(1)
pygame.init()
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Drawing")
clock = pygame.time.Clock()
screen.fill((0, 0, 0))

a = 0
fullscreen = False
Erase = False
color = (255, 200, 200)
Erasor_Tool = pygame.draw.rect(screen, (255, 200, 200), (1574, 1, 25, 25))
Pen_Tool = pygame.draw.rect(screen, (255, 255, 255), (1574, 51, 25, 25))
#------------------------------------------------------------------------------


while True:
    if Erase:
        pygame.draw.circle(screen, (0, 0, 0), (pos1, pos2), (a+10))

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                screen = pygame.display.set_mode((1600, 900))
                Erasor_Tool = pygame.draw.rect(screen, (255, 200, 200), (1574, 1, 25, 25))
                Pen_Tool = pygame.draw.rect(screen, (255, 255, 255), (1574, 51, 25, 25))
                fullscreen = False
            if event.key == pygame.K_f:
                windll.shcore.SetProcessDpiAwareness(1)
                screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
                Erasor_Tool = pygame.draw.rect(screen, (255, 200, 200), (1894, 1, 25, 25))
                Pen_Tool = pygame.draw.rect(screen, (255, 255, 255), (1894, 51, 25, 25))
                fullscreen = True
            if event.key == pygame.K_RIGHTBRACKET:
                a += 1
            if event.key == pygame.K_LEFTBRACKET:
                a -= 1
                if a < 0:
                    a = 0

        cursor1, cursor2, cursor3 = pygame.mouse.get_pressed()
        if cursor1 == True:
            pos1, pos2 = pygame.mouse.get_pos()
            color = (255, 200, 200)
        else:
            color = (0, 0, 0)


#-------------------------------------------------------------------------------------------------------


    if Erase:
        pygame.draw.circle(screen, color, (pos1, pos2), (a+10))

    try:
        if Erasor_Tool.collidepoint((pos1, pos2)):
            Erase = True
        elif Pen_Tool.collidepoint((pos1, pos2)):
            pygame.draw.circle(screen, (0, 0, 0), (pos1, pos2), (a+10))
            Erase = False
        else:
            if Erase == False:
                pygame.draw.circle(screen, (255, 255, 255), (pos1, pos2), a)
    except NameError:
        pass

    if fullscreen:
        Erasor_Tool = pygame.draw.rect(screen, (255, 200, 200), (1894, 1, 25, 25))
        Pen_Tool = pygame.draw.rect(screen, (255, 255, 255), (1894, 51, 25, 25))
    else:
        Erasor_Tool = pygame.draw.rect(screen, (255, 200, 200), (1574, 1, 25, 25))
        Pen_Tool = pygame.draw.rect(screen, (255, 255, 255), (1574, 51, 25, 25))


#-------------------------------------------------------------------------------------------------------


    pygame.display.update()
    clock.tick(50000)          # I just chose an arbitrarily large number to ensure maximum frame rate








    
