import pygame, sys,math, random
from snakebody import  *

class SnakeHead(SnakeBody):
    def __init__(self,speed=5,pos=[75,75]):
        SnakeBody.__init__(self, [0,0],pos)
        self.image = pygame.image.load("images/snake head.png")
        self.rect = self.image.get_rect(center = pos) 
        self.rad = (self.rect.height/2 + self.rect.width/2)/2
        self.maxspeed=speed
        kind = "player"
        
    def go(self,direction):
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
            
    def ballCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom>other.rect.top:
                        if self.rect.top< other.rect.bottom:
                            if self.getdist(other)<self.rad + other.rad:
                                return True
        return False
        
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        
        if self.rect.bottom > height:
            self.speedy = -self.speedy
            self.move()
            self.speedy = 0
        if self.rect.top < 0:
            self.speedy = -self.speedy
            self.move()
            self.speedy = 0
            
    
        if self.rect.left < 0:
            self.speedx = -self.speedx
            self.move()
            self.speedx = 0
        if self.rect.right > width:
            self.speedx = -self.speedx 
            self.move()
            self.speedx = 0

    def eggcolide(self,other):
        if self!=other:
            if self.rect.right > other.rect.left:
                if self.rect.left <other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            
                                return True
        return False
