print("welcome to game maggle")

#Useful imports
import pygame

#Method called needed by pygame
pygame.init()
pygame.key.set_repeat()

#Setting up window size
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

#Setting up clock
clock = pygame.time.Clock()

from homeScreen import HomeScreen
#Loading homescreen
homescreen = HomeScreen()
homescreen_group = pygame.sprite.Group()
homescreen_group.add(homescreen)

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
    if(menu):
        print("Displaying menu")
        homescreen_group.draw(screen)
        pygame.display.flip()
    else:
        
        pygame.display.flip()
        print("Displaying map")

    #Capping fps
    clock.tick(1)
