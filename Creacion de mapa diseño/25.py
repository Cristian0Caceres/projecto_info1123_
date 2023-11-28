import pygame,sys
from pygame.locals import *
import numpy as np

# Cargamos las imágenes
def cargar_imagenes():
    imagenes = []
    imagenes.append(pygame.image.load('25/f3.png')) # Verde claro 1
    imagenes.append(pygame.image.load('25/f5.png')) # Verde claro 2
    imagenes.append(pygame.image.load('25/f4.png')) # Verde oscuro

    imagenes.append(pygame.image.load('25/f2.png')) # Naranjo
    imagenes.append(pygame.image.load('25/f1.png')) # Rojo

    imagenes.append(pygame.image.load('25/f11.png'))# Blanco
    imagenes.append(pygame.image.load('25/f13.png')) # Crema
    imagenes.append(pygame.image.load('25/f6.png')) # Gris
    imagenes.append(pygame.image.load('25/f9.png')) # Celeste


    imagenes.append(pygame.image.load('25/f7.png')) # Rosa
    imagenes.append(pygame.image.load('25/f8.png')) # Purpura 1
    imagenes.append(pygame.image.load('25/f10.png')) # Purpura 2

    return imagenes


# Inicializamos Pygame
pygame.init()

matris = [
    [3,3,3,3,8,8,8,8,8,8,8,8,8,8,8,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0],
    [3,3,3,8,8,8,8,8,8,8,8,8,8,8,8,8,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0],
    [3,3,8,8,8,8,8,8,8,8,8,8,8,8,8,8,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0],
    [3,8,8,8,8,4,8,8,8,8,8,8,8,8,8,8,8,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0],
    [8,8,8,4,4,4,4,7,8,8,8,8,8,8,8,8,8,8,3,3,3,3,3,3,3,0,0,0,0,0,0,0],
    [8,8,8,4,4,4,4,7,8,8,8,8,8,8,8,8,8,8,8,3,3,3,3,3,0,0,0,0,0,0,0,0],
    [8,8,8,7,4,4,4,7,8,8,8,8,8,8,8,8,8,8,8,8,8,3,3,0,0,0,0,0,0,0,0,0],
    [8,8,8,8,7,4,4,7,8,8,8,8,8,8,8,8,8,8,8,8,3,3,3,0,0,0,0,0,0,0,0,0],
    [8,8,8,8,7,7,7,7,8,8,8,8,8,8,8,8,8,8,8,3,3,3,0,0,0,8,0,0,0,0,0,0],
    [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,3,0,0,0,8,8,8,8,0,0,0,0],
    [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,0,0,8,8,8,1,8,8,8,8,8],
    [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,0,8,1,1,1,1,8,8,8,8],
    [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,1,1,1,1,1,1,1,1],
    [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,1,1,1,1,1,1,1,1,1,1,1,1],
    [3,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,2,1,1,1,1,1,1,1,1,1,1,1,1],
    [5,3,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1],
    [5,5,3,8,8,8,8,8,8,8,8,8,8,8,8,8,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1],
    [5,5,5,3,8,8,8,8,8,8,8,8,8,8,8,3,2,2,2,2,2,2,1,1,8,1,1,1,1,1,1,1],
    [5,5,5,5,3,8,8,8,8,8,8,8,8,8,8,3,2,2,2,2,2,2,2,8,8,8,1,1,1,1,1,1],
    [5,5,5,5,5,3,8,8,8,8,8,8,8,8,3,3,2,2,2,2,2,2,8,8,8,8,8,8,8,1,1,1],
    [5,5,5,5,5,3,3,8,8,8,8,8,8,8,8,3,3,2,2,2,2,2,2,8,8,8,8,8,1,1,1,1],
    [5,5,5,8,5,5,3,3,8,8,8,8,8,8,3,3,3,2,2,8,8,2,2,2,8,2,8,1,1,1,1,1],
    [5,5,8,8,8,5,5,3,8,8,8,8,8,3,3,3,3,2,2,8,2,2,2,2,2,2,2,1,1,1,1,1],
    [5,5,5,5,5,5,5,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1]
]
# Creamos la pantalla
pantalla = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Simulador de ecosistema")


# Cargamos las imágenes
imagenes = cargar_imagenes()

for i in range(24):
    for j in range(32):
        if matris[i][j] == 0:
            pantalla.blit(imagenes[0], (j * 25, i * 25))
        if matris[i][j] == 1:
            pantalla.blit(imagenes[1], (j * 25, i * 25))
        if matris[i][j] == 2:
            pantalla.blit(imagenes[2], (j * 25, i * 25))
        if matris[i][j] == 3:
            pantalla.blit(imagenes[3], (j * 25, i * 25))
        if matris[i][j] == 4:
            pantalla.blit(imagenes[4], (j * 25, i * 25))
        if matris[i][j] == 5:
            pantalla.blit(imagenes[5], (j * 25, i * 25))
        if matris[i][j] == 6:
            pantalla.blit(imagenes[6], (j * 25, i * 25))
        if matris[i][j] == 7:
            pantalla.blit(imagenes[7], (j * 25, i * 25))
        if matris[i][j] == 8:
            pantalla.blit(imagenes[8], (j * 25, i * 25))
# Actualizamos la pantalla
pygame.display.update()

# Mantenemos la ventana abierta hasta que el usuario la cierre
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
            quit()
