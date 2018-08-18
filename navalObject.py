import worldObject
from ship import Ship
import pygame
import Constants
    
def capspeed(speed, value, max_speed):
    speed += value
    final_value = min(abs(speed), abs(max_speed))
    if(speed < 0):
        final_value = -final_value
    return final_value

class NavalObject(worldObject.WorldObject):
    def __init__(self, ship, speed_x, speed_y, x, y):
        super().__init__(x, y)
        self.ship = ship
        self.speed_x = speed_x
        self.speed_y = speed_y

    #Methods to change the speed of the naval object
    def add_speed_x(self, value):
        self.speed_x = capspeed(self.speed_x, value, self.ship.max_speed)
    def add_speed_y(self, value):
        self.speed_y = capspeed(self.speed_y, value, self.ship.max_speed)
    
    def set_speed_x(self, value):
        self.speed_x = value
    def set_speed_y(self, value):
        self.speed_y = value

    def object_advance(self):
        if self.rect.x < Constants.COAST_OFFSET():
            self.rect.x = Constants.COAST_OFFSET()
            self.set_speed_x(0)
        if self.rect.x > Constants.SCREEN_WIDTH() - self.rect.width - Constants.COAST_OFFSET():
            self.rect.x = Constants.SCREEN_WIDTH() - self.rect.width - Constants.COAST_OFFSET()
            self.set_speed_x(0)
        self.rect.x += self.speed_x
        if self.rect.y < 0:
            self.rect.y = 0
            self.set_speed_y(0)
        if self.rect.y > Constants.GAME_AREA_HEIGHT() - self.rect.height:
            self.rect.y = Constants.GAME_AREA_HEIGHT() - self.rect.height
            self.set_speed_y(0)
        self.rect.y += self.speed_y

    def set_ship(self, ship):
        self.ship = ship

class Player(NavalObject):
    def __init__(self, ship, speed_x, speed_y, x, y, nb_pop):
        super().__init__(ship, speed_x, speed_y, x, y)

        #Changing the size of the player
        self.image = pygame.image.load("ressources/bluesquare.png")
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect()

        self.nb_pop = nb_pop
        self.left = False
        self.right = False
        self.top = False
        self.bottom = False

    #Method that returs the number of migrants that were kicked from the ship from the number given
    def add_pop(self, n):
        self.nb_pop += n
        kicked_out = 0
        if self.nb_pop > self.ship.cargo:
            kicked_out = self.nb_pop - self.ship.cargo
            self.nb_pop = self.ship.cargo
        return kicked_out

    def update(self):
        self.object_advance()
        if self.top:
            self.add_speed_y(-self.ship.acceleration)
        if self.left:
            self.add_speed_x(-self.ship.acceleration)
        if self.bottom:
            self.add_speed_y(self.ship.acceleration)
        if self.right:
            self.add_speed_x(self.ship.acceleration)
        if not self.right and not self.left :
            if abs(self.speed_x) < self.ship.decceleration:
                self.set_speed_x(0)
            else:
                final_speed = abs(self.speed_x) - self.ship.decceleration
                if self.speed_x < 0:
                    final_speed = - final_speed
                self.set_speed_x(final_speed)
        if not self.top and not self.bottom:
            if abs(self.speed_y) < self.ship.decceleration:
                self.set_speed_y(0)
            else:
                final_speed = abs(self.speed_y) - self.ship.decceleration
                if self.speed_y < 0:
                    final_speed = - final_speed
                self.set_speed_y(final_speed)
        #print(str(self.rect.x) + ' and ' + str(self.rect.y))

    