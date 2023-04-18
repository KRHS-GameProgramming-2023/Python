import pygame,sys,math

class Egg():
    def __init__(self, pos=[50,50]):
        self.image = pygame.image.load("images/egg.png")
        self.rect = self.image.get_rect(center=pos)
        self.rad = self.rect.height/2

        self.kind="Egg"
        self.living=True
        
    def ballcolide(self,other):
        if self!=other:
            if self.rect.right > other.rect.left:
                if self.rect.left <other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.dist(other)<self.rad+other.rad:
                                
                                return True
        return False
        
    def dist(self,other):
        x1=self.rect.center[0]
        x2=other.rect.center[0]
        y1=self.rect.center[1]
        y2=other.rect.center[1]
        return math.sqrt((x2-x1)**2+(y2-y1)**2)
        
    def snakecolide(self,other):
        if self!=other:
            if self.rect.right > other.rect.left:
                if self.rect.left <other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            self.living=False
                            return True
        return False
