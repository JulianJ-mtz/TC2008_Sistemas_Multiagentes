
# José Julián Marínez Romero A01254258
# Dinosaudioaltarin

import pygame, sys, random
from pygame.locals import *
pygame.init()

WIDTH, HEIGHT = 720, 600
SPEED, FPS = 5, 60

display = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("../Img/grass.png").convert_alpha()
dino_image = pygame.image.load("../Img/dino.png").convert_alpha()
dino_rect = dino_image.get_rect()
star_image = pygame.image.load("../Img/star.png").convert_alpha()
star_rect = star_image.get_rect()
star_rect.center = (WIDTH//2, HEIGHT//2)
clock = pygame.time.Clock()

# Colores
red = (180,55,50)

plataformas = [
    pygame.Rect(180, 460, 200, 20),
    pygame.Rect(400, 300, 200, 20),
    pygame.Rect(180, 140, 200, 20),
    pygame.Rect(0,595,720,20)
]

def colocarPlataformas():
    for plataforma in plataformas:
        pygame.draw.rect(display, red, plataforma)    

run = True
isJump = False
jumpCount = 10 

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    clock.tick(FPS)
    pygame.time.delay(25)
    keys = pygame.key.get_pressed()
    if keys[K_a] and dino_rect.left > 0:
        dino_rect.x -= SPEED
    if keys[K_d] and dino_rect.right < WIDTH:
        dino_rect.x += SPEED

    if not (isJump):
        if keys[K_w] and dino_rect.top > 0:
            dino_rect.y -= SPEED
        if keys[K_s] and dino_rect.bottom < HEIGHT:
            dino_rect.y += SPEED

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            dino_rect.y -= (jumpCount * abs(jumpCount)) * 0.3
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
    dino_rect.y += 3  

     # rect1 = pygame.draw.rect(display, (255,255,0),(180, 400, 200, 20))
    
    for plataforma in plataformas:
        if dino_rect.colliderect(plataforma):
            dino_rect.y = plataforma.top - dino_rect.height 
            # dino_rect.y = plataforma.bottom - dino_rect.height
            
        # if keys[K_a] and dino_rect.left > 0:
        #     dino_rect.x += SPEED
        # if keys[K_d] and dino_rect.right < WIDTH:
        #     dino_rect.x -= SPEEDrect1
        # if keys[K_w] and dino_rect.top > 0:
        #     dino_rect.y += SPEED
        # if keys[K_s] and dino_rect.bottom < HEIGHT:
        #     dino_rect.y -= SPEED

    if dino_rect.colliderect(star_rect):
        star_rect.x = random.randint(50, WIDTH - 50)
        star_rect.y = random.randint(50, HEIGHT - 50)
        print("COLISION")

    display.blit(background, (0, 0))
    display.blit(dino_image, dino_rect)
    display.blit(star_image, star_rect)
   
    colocarPlataformas()
    pygame.display.update()

pygame.quit()
sys.exit()
    
    