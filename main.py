#Useful imports
import pygame
import math


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
from buyZone import BuyCargo,BuySpeed, BuyMissile

#Method called needed by pygame
pygame.init()
pygame.key.set_repeat()

pygame.font.init()

pygame.mixer.init()


                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Some Text', False, (0, 0, 0)) #rgba colors

#Sound theme
pygame.mixer.music.load('ressources/theme.mp3')
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.pause()

#Setting up window size

screen = pygame.display.set_mode([Constants.SCREEN_WIDTH(), Constants.SCREEN_HEIGHT()])

#Setting up clock
clock = pygame.time.Clock()

from staticScreens import HomeScreen
from staticScreens import GameOver
from staticScreens import LowerBar
from staticScreens import NextEnnemy

#Loading homescreen
bar = LowerBar()
bar_group = pygame.sprite.Group()
bar_group.add(bar)

homescreen = HomeScreen()
homescreen_group = pygame.sprite.Group()
homescreen_group.add(homescreen)

#For gameOver
gameover = GameOver()
gameover_group = pygame.sprite.Group()
gameover_group.add(gameover)

### Setting up all entities for level

#Data for generating ennemies
tick = Constants.SPAWN_RATE()
count_towards_new_ennemy = Constants.STARTING_COUNT()


def create_standard_world():
    player = Player(Ship(max_speed=5, cargo=3, acceleration=1, decceleration=3), speed_x=0, speed_y=0, x=10, y=360, 
        nb_pop=0, money=0, nb_missil=1)
    w = World([MapImage(), player], screen, player)
    w.add_starting_harbour(StartingHarbour(Constants.COAST_OFFSET()-10,100,25,1,player))
    w.add_starting_harbour(StartingHarbour(Constants.COAST_OFFSET()-2,200,12,2,player))
    w.add_starting_harbour(StartingHarbour(Constants.COAST_OFFSET()-5,560,5,3,player))
    w.add_ending_harbour(EndingHarbour(Constants.SCREEN_WIDTH()-Constants.COAST_OFFSET()-50,180,3,player))
    w.add_ending_harbour(EndingHarbour(Constants.SCREEN_WIDTH()-Constants.COAST_OFFSET()-55,500,3,player))
    w.add_sprite(BuySpeed(800,500,player))
    w.add_sprite(BuyCargo(654,300,player))
    w.add_sprite(BuyMissile(200,200,player))
    return w

world = create_standard_world()

def reset_world():
    return create_standard_world(), Constants.SPAWN_RATE(), Constants.STARTING_COUNT()


menu = True
done = False

#Handling of score
score = 0

def display_bar(screen):
    bar_group.draw(screen)
    textsurface = myfont.render(str(player.money), False, (0, 0, 0)) #Shows player money
    textsurface2 = myfont.render(str(player.nb_missil), False, (0, 0, 0)) #Shows player missiles
    textsurface3 = myfont.render(str(score), False, (0, 0, 0)) #for score

    speed = math.sqrt(world.player.speed_x*world.player.speed_x + world.player.speed_y*world.player.speed_y)
    textsurface4 = myfont.render("{:2.2f}".format(speed), False, (0, 0, 0)) #for speed

    nb_passenger = world.player.nb_pop
    textsurface5 = myfont.render(str(nb_passenger), False, (0, 0, 0)) #for speed

        
    screen.blit(textsurface5, (741,659))
    screen.blit(textsurface4, (921,659))
    screen.blit(textsurface3, (120,659)) #coordinates x, y
    screen.blit(textsurface, (430,659)) #coordinates x, y
    screen.blit(textsurface2,(1255,659)) #coordinates x, y

#showing where they'll spawn
x_rand=random.randint(300, 900)
y_rand=random.randint(10, 550)

marker = NextEnnemy()
marker_group = pygame.sprite.Group()
marker_group.add(marker)
marker.rect.x = x_rand
marker.rect.y = y_rand

while not done:
    player = world.player

    #Spawning new ennemies
    

    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu = False
                pygame.mixer.music.unpause()
                if(world.gameOver):
                    pygame.mixer.music.pause()
                    menu = True
                    world, tick, count_towards_new_ennemy = reset_world()
                print(world.gameOver)
            if event.key == pygame.K_ESCAPE:
                pygame.mixer.music.pause()
                menu = True   

            if event.key in [pygame.K_a, pygame.K_q]:
                player.left = True
            if event.key in [pygame.K_z, pygame.K_w]:
                player.top = True
            if event.key in [pygame.K_s]:
                player.bottom = True
            if event.key in [pygame.K_d]:
                player.right = True
            if event.key in [pygame.K_e]:
                world.shoot()
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
    elif(world.gameOver):
        gameover_group.draw(screen)
        pygame.display.flip()
    else:
        


        #Here starts the logic of the game

        

        count_towards_new_ennemy += 1
        if(count_towards_new_ennemy == tick):
            count_towards_new_ennemy = 0
            x_coeff = random.randint(-100, 100)/100
            y_coeff = random.randint(-100, 100)/100
            world.add_ennemy(BasicEnnemy(ship=Ship(1,0.1,0.1,0.1), speed_x=0, speed_y=0,x=x_rand,y=y_rand, 
                x_coeff=x_coeff, y_coeff=y_coeff, nb_tick=0, player=player))
            x_rand=random.randint(300, 900)
            y_rand=random.randint(10, 550)
            marker.rect.x = x_rand
            marker.rect.y = y_rand

        world.update()
        world.actual_map.show()

        #Showing important informations

        #render amount of migrants available
        for harbour in world.starting_harbours:
            nb_avaiable = myfont.render(str(harbour.pop), False, (0, 0, 0))
            screen.blit(nb_avaiable,(harbour.rect.x, harbour.rect.y - 50))
        score = world.player.score
        display_bar(screen)

        marker_group.draw(screen)
        pygame.display.flip()

    #Capping fps
    clock.tick(60)
