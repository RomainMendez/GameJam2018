import pygame

class Map():
    def __init__(self, sprite_list, s):
        self.all_list = sprite_list
        self.screen = s
        print("Map initialized")

    def show(self):
        playlist = pygame.sprite.Group()
        for sprite in self.all_list:
            playlist.add(sprite)
        playlist.draw(self.screen)
