import pygame
import basicEnnemy
import Constants

class Projectile(basicEnnemy.BasicEnnemy):
    def __init__(self, ship, speed_x, speed_y, x, y, player,ennemy_sprite_group):
        super().__init__(ship, speed_x, speed_y, x,y,0,0,0,player)
        self.image = pygame.image.load("ressources/missile.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.target = self.closest_ennemy(ennemy_sprite_group)
        self.player=player


        #local constants
        self.detection_range=Constants.BASIC_MISSILE_DETECTION_RANGE()
        self.losing_range=Constants.BASIC_MISSILE_LOSING_RANGE()

    def closest_ennemy(self,all_ennemy):
        range=1024
        res = None
        for sprite in all_ennemy:
            range0 = basicEnnemy.euclidian_distance(sprite.rect.x,sprite.rect.y,self.player.rect.x,self.player.y)
            if range0 <range:
                range=range0
                res=sprite

        return res
        

    
    def update(self):

        if target: #checks if target exists
            if self.rect.x < self.target.rect.x:
                # Needs to accelerate on x-axis
                self.add_speed_x(self.ship.acceleration)
            else:
                self.add_speed_x(-self.ship.acceleration)
            if self.rect.y < self.target.rect.y:
                # Needs to accelerate on x-axis
                self.add_speed_y(self.ship.acceleration)
            else:
                self.add_speed_y(-self.ship.acceleration)
            self.object_advance()


        



