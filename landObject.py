import pygame
import worldObject
class LandObject(worldObject.WorldObject):
    def __init__(self, x, y, player):
        # Call the parent's constructor
        super().__init__(x, y)
        self.player=player
        self.image = pygame.image.load("ressources/bluesquare.png")
        self.occupied=False

    def update(self):
        self.occupied = True
        if pygame.sprite.collide_rect(self, self.player):
            self.occupied=True
        else:
            self.occupied=False



class StartingHarbour(LandObject):
    def __init__(self,x,y,maxPop,popGrowth,player):
        super().__init__(x,y,player)
        self.maxPop=maxPop
        self.popGrowth=popGrowth
        self.pop=0
        self.counter=0
        self.image = pygame.image.load("ressources/greensquare.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    #applying growth rate
    def popGrowing(self):
        if self.pop<self.maxPop:
            self.pop+=self.popGrowth

    #update
    def update(self):
        super().update()
        self.counter+=1
        if self.counter == 300:
            self.counter = 0
            self.popGrowing()
            print(self.pop)
        if self.occupied:
            self.pop=self.player.add_pop(self.pop)
        
#italian harbour
class EndingHarbour(LandObject):
    def __init__(self,x,y,money,player):
        super().__init__(x,y,player)
        self.money=money
        self.image = pygame.image.load("ressources/purplesquare.png")

    #update
    def update(self):
        super().update()
        if self.occupied:
            self.unload()

    #unloads ship and gives money
    def unload(self):
        to_unload = self.player.nb_pop
        self.player.nb_pop = 0
        self.player.money += to_unload*self.money
        self.player.score += to_unload
        print(self.player.money)






