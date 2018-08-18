import pygame
class HomeScreen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ressources/homescreen.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

class MapImage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ressources/map.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0