import pygame
import visualmap

class World():
    def __init__(self,sprite_list,screen):
        self.all_Sprite=sprite_list
        self.actual_map=visualmap.Map(self.all_Sprite,screen)

    def update(self):
        self.all_Sprite.update()