import worldObject
from ship import Ship
    
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
