
# José Julián Martínez Romero A01254258
# Act laberinto

import pygame, sys
from pygame.locals import *
pygame.init()

# Pantalla
DisplaySurf = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Laberinto')

# Color
pink = (255,190, 255)
 
# Coordenadas de los muros
muros = [
	(0,0,0,600),
    (50,0,600,0),
    (0,600,600,600),
    (600,0,600,550),
    (50,0,50,400),
    (50,550,50,600),
    (50,550,300,550),
    (300,550,300,100),
    (50,500,250,500),
    (250,500,250,450),
    (50,450,250,450),
    (100,50,350,50),
    (100,400,250,400),
    (100,100,300,100),
    (100,400,100,100),
    (150,350,150,150),
    (200,400,200,150),
    (250,350,250,150),
    (350,50,350,50),
    (350,50,350,450),
    (350,500,450,500),
    (350,600,350,550),
    (400,550,400,600),
    (400,450,400,250),
    (400,200,400,100),
    (400,50,550,50),
    (400,100,550,100),
    (450,150,550,150),
    (450,200,500,200),
    (400,250,550,250),
    (450,200,450,150),
    (550,250,550,150),
    (550,100,550,50),
	(450,500,450,300),
	(450,300,550,300),
	(500,350,500,600),
	(400,550,450,550),
	(550,550,550,300),
	(550,550,600,550),    
]

# Función que arma el laberinto
def armarLaberinto():
	for muro in muros:
		pygame.draw.line(DisplaySurf, pink, (muro[0], muro[1]), (muro[2], muro[3]), 5)
		
while True:
	for event in pygame.event.get():
		armarLaberinto()                # Llamar a la función
		if event.type == QUIT:
			pygame.quit()
			sys.exit()			
	pygame.display.update()
	
