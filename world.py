import pygame
import visualmap
import basicEnnemy

class World():
    def __init__(self,sprite_list,screen, player):
        self.actual_map=visualmap.Map(sprite_list,screen)
        self.gameOver = False
        self.player = player
        self.shooted=False

        #Keeping track of starting harbours
        self.starting_harbours = []

    def shoot(self):
        self.shooted=True

    def update(self):
        if self.shooted:
            self.actual_map.add_missile(basicEnnemy.Projectile(0, 0, self.player.rect.x, self.player.rect.y, self.player, self.actual_map.ennemy_playlist))
            self.shooted = False
        for sprite in self.actual_map.playlist:
            sprite.update()
        to_delete = []
        for sprite in self.actual_map.missile_playlist:
            sprite.update()
            if sprite.exploded == True: #missile hit
                #hit_list = pygame.sprite.spritecollide(sprite, self.actual_map.ennemy_playlist, True)
                #print(hit_list)
                to_delete.append(sprite)
        for element in to_delete:
            self.actual_map.missile_playlist.remove(element)
        for sprite in self.actual_map.ennemy_playlist:
            sprite.update()

        
        #Checking collision with ennemies
        hit_list = pygame.sprite.spritecollide(self.player, self.actual_map.ennemy_playlist, True)
        if len(hit_list):
            self.gameOver = True


    def add_sprite(self, s):
        self.actual_map.all_list.append(s)
        self.actual_map.refresh()

    def add_ennemy(self, ennemy):
        self.actual_map.add_ennemy(ennemy)

    def add_starting_harbour(self, h):
        self.starting_harbours.append(h)
        self.actual_map.all_list.append(h)
        self.actual_map.refresh()

    def add_ending_harbour(self, h):
        self.actual_map.all_list.append(h)
        self.actual_map.refresh()




