import navalObject
import Constants
from ship import Ship

def euclidian_distance(x1, y1, x2, y2):
    return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)

class BasicEnnemy(navalObject.NavalObject):
    def __init__(self, ship, speed_x, speed_y, x, y, x_coeff, y_coeff, nb_tick, player):
        super().__init__(ship, speed_x, speed_y, x,y)
        self.x_coeff = x_coeff
        self.y_coeff = y_coeff
        self.nb_tick = nb_tick
        self.target = player
        self.chasing = False
    

    def update(self):
        distance = euclidian_distance(self.x, self.y, self.target.rect.x, self.target.rect.y)
        if distance < Constants.BASIC_ENNEMY_DETECTION_RANGE():
            self.chasing = True
        else:
            if distance > Constants.BASIC_ENNEMY_LOSING_RANGE():
                self.chasing = False

        if self.chasing: #i.e chasing the player
            if self.rect.x < self.target.rect.x :
                # Needs to accelerate on x-axis
                self.add_speed_x(self.ship.acceleration)
            else:
                self.add_speed_x(-self.ship.acceleration)
            if self.rect.y < self.target.rect.y :
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
