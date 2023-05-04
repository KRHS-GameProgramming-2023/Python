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

egg=Egg([random.randint(50,850), random.randint(50,650)])

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
        
        
            
    for i, bodypart in enumerate(snake):
        if i!=0:
            bodypart.setPos(snake[i-1].prevLocation)
        else:
            bodypart.move()
            
        
    if player.eggcolide(egg):
        snake+=[SnakeBody(player.maxspeed, snake[-1].rect.center)]
    egg.snakecolide(player)
    
    if not egg.living:
        egg=Egg([random.randint(50,850), random.randint(50,650)])
    
    screen.fill((64, 120, 255))
    screen.blit(bg,bgr)
    screen.blit(egg.image, egg.rect)
    for bodypart in reversed(snake):
        screen.blit(bodypart.image,bodypart.rect)
    pygame.display.flip()
    clock.tick(60)
    print(clock.get_fps())
