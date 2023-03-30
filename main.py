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

player = SnakeHead(5,[450,350])
snake=[player]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                player.go("up")
            if event.key==pygame.K_LEFT:
                player.go("left")
            if event.key==pygame.K_RIGHT:   
                player.go("right")
            if event.key==pygame.K_DOWN:
                player.go("down")
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                player.go("sup")
            if event.key==pygame.K_LEFT:
                player.go("sleft")
            if event.key==pygame.K_RIGHT:
                player.go("sright")
            if event.key==pygame.K_DOWN:
                player.go("sdown")
            
    for bodypart in snake:
        bodypart.move()
    
    screen.fill((64, 120, 255))
    screen.blit(bg,bgr)
    for bodypart in snake:
        screen.blit(bodypart.image,bodypart.rect)
    pygame.display.flip()
    clock.tick(60)
    print(clock.get_fps())
