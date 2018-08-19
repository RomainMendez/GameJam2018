import pygame
import visualmap

class World():
    def __init__(self,sprite_list,screen, player):
        self.actual_map=visualmap.Map(sprite_list,screen)
        self.gameOver = False
        self.player = player

    def update(self):
        for sprite in self.actual_map.playlist:
            sprite.update()
        for sprite in self.actual_map.ennemy_playlist:
            sprite.update()
        
        #Checking collision with ennemies
        hit_list = pygame.sprite.spritecollide(self.player, self.actual_map.ennemy_playlist, True)
        if len(hit_list):
            self.gameOver = True

        print(self.gameOver)

    def add_sprite(self, s):
        self.actual_map.all_list.append(s)
        self.actual_map.refresh()

    def add_ennemy(self, ennemy):
        self.actual_map.add_ennemy(ennemy)




