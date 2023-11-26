import pygame, sys 
from pygame.locals import *

pygame.init()

BLACK = (0,0,0)
red = (255,0,0)
ancho,alto = 800,500

windows = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Titulo de tu programa")
clock = pygame.time.Clock()

coord_x = 10
coord_y = 10
speend_x = 0
speend_y = 0

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if event.type == pygame.KEYDOWN:  # Tecla precionada
        if event.key == pygame.K_LEFT:
            speend_x = -3
        if event.key == pygame.K_RIGHT:
            speend_x = 3
    if event.type == pygame.KEYUP:  # Tecla NO presionada
        if event.key == pygame.K_LEFT:  #  <--- definir que tipo de tecla
            speend_x = 0
        if event.key == pygame.K_RIGHT:
            speend_x = 0

    windows.fill(BLACK)  # PINTA LA pantalla

    coord_x += speend_x  # Mostrar la animación
    pygame.draw.rect(windows,red,(coord_x,coord_y,100,100))


    pygame.display.flip()
    clock.tick(150)  # Tiempo de como se vera la animación 