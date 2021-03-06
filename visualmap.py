import pygame

class Map():
    def __init__(self, sprite_list, s):
        self.all_list = sprite_list
        self.screen = s
        self.playlist = pygame.sprite.Group()
        self.ennemy_playlist = pygame.sprite.Group()
        self.missile_playlist = pygame.sprite.Group()
        for sprite in self.all_list:
            self.playlist.add(sprite)
        print("Map initialized")

    def add_missile(self, missile):
        self.missile_playlist.add(missile)

    def show(self):
        self.playlist.draw(self.screen)
        self.ennemy_playlist.draw(self.screen)
        self.missile_playlist.draw(self.screen)

    def refresh(self):
        self.playlist = pygame.sprite.Group()
        for sprite in self.all_list:
            self.playlist.add(sprite)

    def add_ennemy(self, ennemy):
        self.ennemy_playlist.add(ennemy)
