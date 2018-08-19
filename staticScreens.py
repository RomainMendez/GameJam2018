import pygame
class HomeScreen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ressources/homescreen.jpg")
        #self.image = pygame.transform.scale(self.image, (640, 360))
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
        
class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ressources/gameover.jpg")
        self.image = pygame.transform.scale(self.image, (1280, 720))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0