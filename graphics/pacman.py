import os
from tkinter import EventType
import pygame
pygame.init()



width = 500
height = 500


pacmanX = 100
pacmanY = 100
score = 0

screen = pygame.display.set_mode([width,height])
pygame.display.set_caption("pacman game")
running = True
while running:
    if EventType == pygame.quit:
        running = False
    screen.fill((0,0,0))
   

    #pygame.draw.circle(screen,(0,255,255),(255,255),75)

    ######################################

    ### draw image 2

    #######################################





    #pygame.draw.rect(screen,(255,0,0),((25,25),(50,200)))
    ##########################################
    
    
    ## draw image 1

    ##########################################

    # left top , width height




# 3 circles
    # for i in range (3):
    #      coords = (255,i*100 + 100)
    #      pygame.draw.circle(screen,(0,0,0),coords,30)


# movement
   # screen , color , centre , radius
    pacman = pygame.draw.circle(screen,(255,255,0),(pacmanX,pacmanY),20)
    
    





    # code to exit game on escape
    #
    keys = pygame.key.get_pressed()
    
    if(keys[pygame.K_ESCAPE]) :
        running = False

            # keyboard movments


    if (keys[pygame.K_w]):
        pacmanY = pacmanY - 1
    if (keys[pygame.K_d]):
        pacmanX = pacmanX + 1
    if (keys[pygame.K_a]):
        pacmanX = pacmanX - 1


    #############

    # complete the movements # 

    ##############


    # boundary code right side

    if pacman.right >= 500:
        running = False
        print("game over hit right side")


    ###########################

    ### create boundries for all sides
            
    ###############################



    ## create food ### 

    food = pygame.image.load('apple.jpg')
    foodX = 100
    foodY = 400
    food = pygame.transform.scale(food,(30,30)) # makes the image smaller
    screen.blit(food,(foodX,foodY))



    # Use random to choose location of food



    ##############








    #################################################################

    ### use for i in range to make lots of food in different locations

    ###################################################################












    #############################################################################

    # code the score system, 
    # if foodX and foodY == the pacman X and Y score +1

    ##############################################################################

    fontStyle = pygame.font.SysFont("comicsansms",15)
    scoreText = fontStyle.render("your score: " + str(score),True,(50, 153, 213))
    screen.blit(scoreText,(0,0))







    ################################
    
    # make the food move somewhere 
    # else after being eaten 

    ################################







    ################################

    # Create barriers

    ################################

    barrierOutSide = pygame.draw.rect(screen,(0,0,100),((25,25),(60,210)))
    barrierInside = pygame.draw.rect(screen,(20,20,20),((30,30),(50,200)))
    
    
    if barrierInside.collidepoint(pacmanX,pacmanY) == True:
        pacmanX = 255
        pacmanY = 255
    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False
    pygame.display.flip()  # draws the screen
    pygame.display.update() # refreshes the screen
pygame.quit()
quit()