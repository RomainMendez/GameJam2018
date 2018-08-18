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
    '''don'''
    def __init__(self,x,y):
        super().__init__(x,y,False)

class BuyZone(LandObject):
    def __init__(self,x,y,buyType,timer):
        super().__init__(x,y,True)
        self.buyType=buyType

class Harbour(LandObject):
    def __init__(self,x,y,maxPop,popGrowth):
        super().__init__(x,y,True)
        self.maxPop=maxPop
        self.popGrowth=popGrowth
        self.pop=0
    def popGrowth():
        if self.pop<self.maxPop:
            pop+=self.popGrowth
    def update():
        self.popGrowth()
        




