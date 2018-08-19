import pygame
import landObject



class BuySpeed(landObject.LandObject):
    def __init__(self,x,y,player):
        super().__init__(x,y,player)
        self.image = pygame.image.load("ressources/bonuszone.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self):
        super().update()
        if self.occupied and self.player.money > 9:
            self.player.ship.max_speed+=5
            self.player.money-=10

            



class BuyCargo(landObject.LandObject):
    def __init__(self,x,y,player):
        super().__init__(x,y,player)
        self.image = pygame.image.load("ressources/bonuszone.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self):
        super().update()
        if self.occupied and self.player.money > 14:
            self.player.ship.cargo+=2
            self.player.money-=15
            

    

            
        





