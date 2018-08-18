#Useful imports
import pygame

import Constants

#For random ennemies
import random
from basicEnnemy import BasicEnnemy

#Imports for the game logic
from world import World
from staticScreens import MapImage

#For player object
from navalObject import Player
from ship import Ship

#for land tile objects
from landObject import LandObject, StartingHarbour, EndingHarbour

#Method called needed by pygame
pygame.init()
pygame.key.set_repeat()

#Setting up window size

screen = pygame.display.set_mode([Constants.SCREEN_WIDTH(), Constants.SCREEN_HEIGHT()])

#Setting up clock
clock = pygame.time.Clock()

from staticScreens import HomeScreen
#Loading homescreen

homescreen = HomeScreen()
homescreen_group = pygame.sprite.Group()
homescreen_group.add(homescreen)

### Setting up all entities for level
player = Player(Ship(max_speed=5, cargo=3, acceleration=0.4, decceleration=3), speed_x=0, speed_y=0, x=10, y=360, 
    nb_pop=0, money=0)

#Data for generating ennemies
tick = 6000
count_towards_new_ennemy = 5940

world = World([MapImage(), player], screen)

world.add_sprite(StartingHarbour(Constants.COAST_OFFSET()-30,100,25,1,player))
world.add_sprite(EndingHarbour(Constants.SCREEN_WIDTH()-Constants.COAST_OFFSET()-30,500,3,player))


menu = True
done = False

while not done:

    #Spawning new ennemies
    

    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu = False
            if event.key == pygame.K_ESCAPE:
                menu = True   

            if event.key in [pygame.K_a, pygame.K_q]:
                player.left = True
            if event.key in [pygame.K_z, pygame.K_w]:
                player.top = True
            if event.key in [pygame.K_s]:
                player.bottom = True
            if event.key in [pygame.K_d]:
                player.right = True
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_a, pygame.K_q]:
                player.left = False
            if event.key in [pygame.K_z, pygame.K_w]:
                player.top = False
            if event.key in [pygame.K_s]:
                player.bottom = False
            if event.key in [pygame.K_d]:
                player.right = False

    if(menu):
        homescreen_group.draw(screen)
        pygame.display.flip()
    else:



        #Here starts the logic of the game

        

        count_towards_new_ennemy += 1
        if(count_towards_new_ennemy == tick):
            count_towards_new_ennemy = 0
            x_coeff = random.randint(-100, 100)/100
            y_coeff = random.randint(-100, 100)/100
            ennemy = BasicEnnemy(ship=Ship(1,0.1,0.1,0.1), speed_x=0, speed_y=0, x=500, y=100, x_coeff=x_coeff, y_coeff=y_coeff, nb_tick=0, player=player)
            world.add_sprite(ennemy)
            print("Ennemy spawned")

        world.update()
        world.actual_map.show()

        pygame.display.flip()

    #Capping fps
    clock.tick(60)
