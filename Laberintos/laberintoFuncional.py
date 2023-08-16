
# José Julián Martínez Romero A01254258
# Act laberinto

import pygame, sys
from pygame.locals import *
pygame.init()

# Pantalla
WIDTH = 600
HEIGHT = 600
SPEED = 4
FPS = 60
DisplaySurf = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Laberinto')
clock = pygame.time.Clock()

# Color
pink = (255,190, 255)
black = (0,0,0)
yellow = (255,255,0)

# Objeto con movimiento
cosito_x = 20
cosito_y = 20

cosito_width = 10 
cosito_height = 10
 
# Coordenadas de los muros
muros = [
    ([50, 0], [600, 5]),
    ([0, 0], [5, 600]),
    ([595, 0], [5, 550]),
    ([0, 595], [600, 5]),
    ([50, 0], [5, 400]),
    ([50, 445], [200, 5]),
    ([245, 445], [5, 50]),
    ([50, 495], [200, 5]),
    ([50, 545], [250, 5]),
    ([295, 100], [5, 450]),
    ([100, 45], [250, 5]),
    ([100, 95], [200, 5]),
    ([345, 50], [5, 400]),
    ([100, 100], [5, 300]),
    ([145, 150], [5, 200]),
    ([195, 150], [5, 250]),
    ([245, 150], [5, 200]),
    ([100, 395], [150, 5]),
    ([345, 550], [5, 600]),
    ([345, 500], [100, 5]),
    ([395, 550], [5, 600]),
    ([395, 550], [50, 5]),
    ([400, 250], [5, 200]),
    ([400, 100], [5, 100]),
    ([400, 45], [150, 5]),
    ([400, 100], [150, 5]),
    ([545, 50], [5, 50]),
    ([545, 150], [5, 100]),
    ([545, 300], [5, 250]),
    ([495, 350], [5, 250]),
    ([450, 150], [5, 50]),
    ([450, 195], [50, 5]),
    ([450, 145], [100, 5]),
    ([400, 245], [150, 5]),
    ([445, 295], [105, 5]),
    ([445, 300], [5, 205]),
    ([545, 550], [55, 5]),
]

# Función que arma el laberinto
def armarLaberinto():
    for muro in muros:
        # pygame.draw.line(DisplaySurf, pink, *muro, 5)    
        pygame.draw.rect(DisplaySurf, pink, muro, 5)    

cosito_rect = pygame.draw.rect(DisplaySurf, yellow, (cosito_x, cosito_y, cosito_width, cosito_height))
# cosito_rect = cosito.get_rect()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(FPS)
         
    keys = pygame.key.get_pressed()

    # Movimiento
    if keys[K_LEFT] and cosito_rect.left > 0:
        cosito_rect.x -= SPEED
    if keys[K_RIGHT] and cosito_rect.right < WIDTH:
        cosito_rect.x += SPEED
    if keys[K_UP] and cosito_rect.top > 0:
        cosito_rect.y -= SPEED
    if keys[K_DOWN] and cosito_rect.bottom < HEIGHT:
        cosito_rect.y += SPEED

    # Detener cuando choca con un muro
    for muro in muros:
        if cosito_rect.colliderect(pygame.Rect(muro)):

            if keys[K_LEFT] and cosito_rect.left > 0:
                cosito_rect.x += SPEED
            if keys[K_RIGHT] and cosito_rect.right < WIDTH:
                cosito_rect.x -= SPEED
            if keys[K_UP] and cosito_rect.top > 0:
                cosito_rect.y += SPEED
            if keys[K_DOWN] and cosito_rect.bottom < HEIGHT:
                cosito_rect.y -= SPEED
            print('colision')       
            
    DisplaySurf.fill(black)

    armarLaberinto()
    
    pygame.draw.rect(DisplaySurf, yellow, cosito_rect)  

    pygame.display.flip()

pygame.quit()
sys.exit()