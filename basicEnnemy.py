import navalObject
import pygame
import Constants
from ship import Ship

def euclidian_distance(x1, y1, x2, y2):
    return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)

class BasicEnnemy(navalObject.NavalObject):
    def __init__(self, ship, speed_x, speed_y, x, y, x_coeff, y_coeff, nb_tick, player):
        super().__init__(ship, speed_x, speed_y, x,y)
        #Keeping old coordinates
        self.image = pygame.transform.scale(self.image, (28, 28)) #Transforming the size of the ennemy
        #Correcting hitbox
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.x_coeff = x_coeff
        self.y_coeff = y_coeff
        self.nb_tick = nb_tick
        self.target = player
        self.chasing = False

        #local constants
        self.detection_range=Constants.BASIC_ENNEMY_DETECTION_RANGE()
        self.losing_range=Constants.BASIC_ENNEMY_LOSING_RANGE()
    

    def update(self):
        distance = euclidian_distance(self.rect.x, self.rect.y, self.target.rect.x, self.target.rect.y)
        if distance < self.detection_range:
            self.chasing = True
        else:
            if distance > self.losing_range:
                self.chasing = False

        if self.chasing: #i.e chasing the player
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
        else:
            if self.speed_x == 0 or self.speed_y == 0:
                self.x_coeff = -self.x_coeff
                self.y_coeff = -self.y_coeff
            self.add_speed_x(self.ship.acceleration*self.x_coeff)
            self.add_speed_y(self.ship.acceleration*self.y_coeff)
        self.object_advance()


def closest_ennemy(player,all_ennemy):
    range=10000000000000000
    res = None
    for sprite in all_ennemy:
        x = player.rect.x
        y = player.rect.y
        range0 = euclidian_distance(sprite.rect.x,sprite.rect.y, x, y)
        if range0 <range:
            range=range0
            res=sprite

    return res

        
class Projectile(navalObject.NavalObject):
    def __init__(self, speed_x, speed_y, x, y, player,ennemy_sprite_group):
        super().__init__(Ship(5,0,10,0), speed_x, speed_y, x,y)
        self.image = pygame.image.load("ressources/missile.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.target = closest_ennemy(player, ennemy_sprite_group)
        self.player = player
        self.exploded = False


        

    
    def update(self):
        if self.target != None: #checks if target exists
            if euclidian_distance(self.target.rect.x, self.target.rect.y, self.rect.x, self.rect.y) < 40:
                self.exploded = True
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
