import pygame
import worldObject
import navalObject
class LandObject(worldObject.WorldObject):
     def __init__(self, x, y, player):
        # Call the parent's constructor
        super().__init__(x, y)
        self.player=player
        self.image = pygame.image.load("ressources/bluesquare.png")
        self.occupied=False

        def update():
            if pygame.collide_rect(self, player):
                print('works')
                self.occupied=True
            else:
                self.occupied=False




class BuyZone(LandObject):
    def __init__(self,x,y,buyType,timer,player):
        super().__init__(x,y,player)
        self.buyType=buyType

class StartingHarbour(LandObject):
    def __init__(self,x,y,maxPop,popGrowth,player):
        super().__init__(x,y,player)
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
        if self.occupied:
            self.pop=player.add_pop()
        
class EndingHarbour(LandObject):
    def __init__(self,x,y,money,player):
        super().__init__(x,y,player)
        self.money=money
        self.image = pygame.image.load("ressources/purplesquare.png")

        





