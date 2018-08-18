#Useful imports
import pygame

#Imports for the game logic
from world import World
from staticScreens import MapImage

#For player object
from navalObject import Player
from ship import Ship

#Method called needed by pygame
pygame.init()
pygame.key.set_repeat()

#Setting up window size
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

#Setting up clock
clock = pygame.time.Clock()

from staticScreens import HomeScreen
#Loading homescreen

homescreen = HomeScreen()
homescreen_group = pygame.sprite.Group()
homescreen_group.add(homescreen)

### Setting up all entities for level
player = Player(Ship(max_speed=2, cargo=3, acceleration=0.4, decceleration=1), speed_x=0, speed_y=0, x=10, y=360, nb_migrants=0)

world = World([MapImage(), player], screen)


menu = True
done = False

while not done:
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
        print("Displaying menu")
        homescreen_group.draw(screen)
        pygame.display.flip()
    else:
        #Here starts the logic of the game

        world.update()
        world.actual_map.show()

        pygame.display.flip()
        print("Displaying map")

    #Capping fps
    clock.tick(60)
