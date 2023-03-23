import pygame, sys,math, random
from snakehead import  *
from snakebody import  *
from egg import  *

pygame.init()

clock = pygame.time.Clock()

size = [900, 700]
screen = pygame.display.set_mode(size)

bg=pygame.image.load("images/pixel.png")
bgr=bg.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
            
    screen.fill((64, 120, 255))
    screen.blit(bg,bgr)
    pygame.display.flip()
    clock.tick(60)
    print(clock.get_fps())
