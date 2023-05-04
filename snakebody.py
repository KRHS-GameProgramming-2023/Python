import pygame, sys,math

class SnakeBody():
    def __init__(self,speed,pos=[50,50]):
        self.image = pygame.image.load("images/snake body.png")
        self.rect = self.image.get_rect(center = pos) 
        self.maxspeed=speed
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.rad = (self.rect.height/2 + self.rect.width/2)/2
        
        kind = "body"
        
        self.direction = "sleft"
        self.prevDirection = "sleft"
        self.prevLocation = self.rect.center
        
        
    def setPos(self, pos):
        self.prevLocation = self.rect.center
        self.rect.center = pos
    
    def move(self):
        self.prevLocation = self.rect.center
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def ballCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom>other.rect.top:
                        if self.rect.top< other.rect.bottom:
                            if self.getdist(other)<self.rad + other.rad:
                                self.speedx = -self.speedx
                                self.speedy = -self.speedy
                                return True
        return False
