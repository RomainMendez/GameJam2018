import pygame

class Map():
    def __init__(self, sprite_list, s):
        self.all_list = sprite_list
        self.screen = s
        self.playlist = pygame.sprite.Group()
        for sprite in self.all_list:
            self.playlist.add(sprite)
        print("Map initialized")

    def show(self):
        self.playlist.draw(self.screen)

    def refresh(self):
        self.playlist = pygame.sprite.Group()
        for sprite in self.all_list:
            self.playlist.add(sprite)

