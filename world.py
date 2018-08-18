import pygame
import visualmap

class World():
    def __init__(self,sprite_list,screen):
        self.all_Sprite=sprite_list
        self.actual_map=visualmap.Map(self.all_Sprite,screen)

    def update(self):
        for sprite in self.all_Sprite:
            sprite.update()
        #self.all_Sprite.update()

    def add_sprite(self, s):
        self.all_Sprite.append(s)
        self.actual_map.all_list.append(s)
        self.actual_map.refresh()




