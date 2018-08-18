import pygame
import worldObject
class LandObject(worldObject.WorldObject):
     def __init__(self, x, y, passable):
        # Call the parent's constructor
        super().__init__(x, y)
        self.image = pygame.image.load("ressources/bluesquare.png")
        self.rect = self.image.get_rect()
        self.passable=passable

class Coast(LandObject):
    def __init__(self,x,y):
        super().__init__(self,x,y,False)

class BonusZone(LandObject):
    def __init__(self,x,y,bonusType,timer):
        super().__init__(x,y,True)
        self.bonusType=bonusType

        

