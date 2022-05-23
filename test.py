
from cmath import rect
from tkinter import EventType
import pygame
pygame.init

width = 500
height = 500
screen = pygame.display.set_mode([width,height])
running = True
while running:
    if EventType == pygame.quit:
        running = False
    screen.fill((255,255,255))
   

    #pygame.draw.circle(screen,(0,255,255),(255,255),75)

    #pygame.draw.rect(screen,(255,0,0),((25,25),(50,200)))

    
    # for i in range(4):
    #     pygame.draw.rect(screen,(255,0,0),(((i*100)+100,25),(20,300)))

    # left top , width height





    # for i in range (3):
    #      coords = (255,i*100 + 100)
    #      pygame.draw.circle(screen,(0,0,0),coords,30)






    pygame.display.flip()  # draws the screen
    pygame.display.update() # refreshes the screen




    events = pygame.event.get()
    # code to exit game on escape
    #
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
