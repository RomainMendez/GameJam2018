import pygame
import worldObject
class LandObject(worldObject.WorldObject):
     def __init__(self, x, y):
        # Call the parent's constructor
        worldObject.WorldObject.__init__(self, x, y)
        self.image = pygame.image.load("ressources/bluesquare.png")
        self.rect = self.image.get_rect()
        self.passable=False
