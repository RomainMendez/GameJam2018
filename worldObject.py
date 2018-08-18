import pygame
class WorldObject(pygame.sprite.Sprite):

    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
        self.image = pygame.image.load("ressources/redsquare.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
