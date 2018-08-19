import pygame
import landObject



class BuyZone(landObject.LandObject):
    def __init__(self,x,y,type,player):
        super().__init__(x,y,player)
        self.image = pygame.image.load("ressources/bonuszone.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.d={'max_speed' : 0,'cargo' : 1, 'accel' :2, 'deccel' : 3}
        self.d.get('key','default')

    
    def update(self):
        super().update()
        if self.occupied and self.player.money > 9:
            self.player.ship.max_speed+=5
            self.player.money-=10




