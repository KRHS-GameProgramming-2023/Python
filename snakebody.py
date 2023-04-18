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
        
        
    def go(self,direction):
        self.prevDirection = self.direction
        self.direction = direction
        if direction=="up":
            self.speedy=-self.maxspeed
        if direction=="left":
            self.speedx=-self.maxspeed
        if direction=="right":
            self.speedx=self.maxspeed
        if direction=="down":
            self.speedy=self.maxspeed
            
        if direction=="sup":
            self.speedy=0
        if direction=="sleft":
            self.speedx=0
        if direction=="sright":
            self.speedx=0
        if direction=="sdown":
            self.speedy=0
    
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
