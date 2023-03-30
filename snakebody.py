import pygame, sys,math

class SnakeBody():
    def __init__(self,speed=[0,0],pos=[50,50]):
        self.image = pygame.image.load("images/snake body.png")
        self.rect = self.image.get_rect(center = pos) 
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.rad = (self.rect.height/2 + self.rect.width/2)/2
        
        kind = "body"
        
    
    def move(self):
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
