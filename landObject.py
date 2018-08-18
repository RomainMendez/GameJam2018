import pygame
import worldObject
class LandObject(worldObject.WorldObject):
     def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__(x, y)
        self.image = pygame.image.load("ressources/bluesquare.png")




class BuyZone(LandObject):
    def __init__(self,x,y,buyType,timer):
        super().__init__(x,y)
        self.buyType=buyType

class StartingHarbour(LandObject):
    def __init__(self,x,y,maxPop,popGrowth):
        super().__init__(x,y)
        self.maxPop=maxPop
        self.popGrowth=popGrowth
        self.pop=0
        self.counter=0
        self.image = pygame.image.load("ressources/greensquare.png")

    def popGrowing(self):
        if self.pop<self.maxPop:
            self.pop+=self.popGrowth

    def popEmbarks(self):
        self.pop=0

    def popeEmbarks(self):
        self.pop-=1

    def update(self):
        self.counter+=1
        if self.counter % 10==0:
            self.popGrowing()
            print(self.pop)
        
class EndingHarbour(LandObject):
    def __init__(self,x,y,money):
        super().__init__(x,y)
        self.money=money
        self.image = pygame.image.load("ressources/purplesquare.png")

        





