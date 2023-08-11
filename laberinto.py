

import pygame, sys
from pygame.locals import *
pygame.init()
DisplaySurf = pygame.display.set_mode((600, 600))
pygame.display.set_caption('AAAAAAAAAA!')

ColorCuadrado01 = (100,255,100)
ColorCuadrado02 = (255,190, 255)
 
muros = [
	()
]

def armarMuro():
	for muro in muros:
		pygame.draw.line()
		
while True:
	for event in pygame.event.get():
		
		cuadrado01 = pygame.draw.rect( #X1, Y1, Ancho, Largo
		DisplaySurf, ColorCuadrado01, (0,0,600,600))
		cuadrado02 = pygame.draw.rect( #X1, Y1, Ancho, Largo
		DisplaySurf, ColorCuadrado02, (110,110,100,100))

		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()