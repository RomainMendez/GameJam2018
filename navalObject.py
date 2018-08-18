import worldObject
from ship import Ship
import pygame
    
def capspeed(speed, value, value2):
    speed += value
    final_value = min(abs(speed), abs(value2))
    if(speed < 0):
        final_value = -final_value
    return final_value

class NavalObject(worldObject.WorldObject):
    def __init__(self, ship, speed_x, speed_y, x, y):
        super().__init__(x,y)
        self.ship = ship
        self.speed_x = speed_x
        self.speed_y = speed_y

    #Methods to change the speed of the naval object
    def add_speed_x(self, value):
        self.speed_x = capspeed(self.speed_x, value, self.speed_x + value)
    def add_speed_y(self, value):
        self.speed_y = capspeed(self.speed_y, value, self.speed_y + value)
    
    def set_speed_x(self, value):
        self.speed_x = capspeed(self.speed_x, value, value)
    def set_speed_y(self, value):
        self.speed_y = capspeed(self.speed_y, value, value)



    def set_ship(self, ship):
        self.ship = ship

class Player(NavalObject):
    def __init__(self, ship, speed_x, speed_y, x, y, nb_migrants):
        super().__init__(ship, speed_x, speed_y, x, y)
        self.nb_migrants = nb_migrants
        self.left = False
        self.right = False
        self.top = False
        self.bottom = False

    #Method that returs the number of migrants that were kicked from the ship from the number given
    def add_migrant(self, n):
        self.nb_migrants += n
        kicked_out = 0
        if self.nb_migrants > self.ship.cargo:
            kicked_out = self.nb_migrants - self.ship.cargo
            self.nb_migrants = self.ship.cargo
        return kicked_out

    def update(self):
        if self.top:
            self.add_speed_y(-self.ship.acceleration)
        if self.left:
            self.add_speed_x(-self.ship.acceleration)
        if self.bottom:
            self.add_speed_y(self.ship.acceleration)
        if self.right:
            self.add_speed_x(self.ship.acceleration)
        if not self.top and not self.right and not self.left and not self.bottom:
            if abs(self.speed_x) < self.ship.decceleration:
                self.set_speed_x(0)
            else:
                final_speed = abs(self.speed_x) - self.ship.decceleration
                if self.speed_x < 0:
                    final_speed = - final_speed
                self.set_speed_x(final_speed)
            if abs(self.speed_y) < self.ship.decceleration:
                self.set_speed_y(0)
            else:
                final_speed = abs(self.speed_x) - self.ship.decceleration
                if self.speed_y < 0:
                    final_speed = - final_speed
                self.set_speed_y(final_speed)
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    