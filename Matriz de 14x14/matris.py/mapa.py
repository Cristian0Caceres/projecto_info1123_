import pygame,sys
from pygame.locals import *
import numpy as np

# Cargamos las imágenes
def cargar_imagenes():
    imagenes = []
    imagenes.append(pygame.image.load('f1.png')) # Tierra
    imagenes.append(pygame.image.load('f5.png')) # Montaña
    imagenes.append(pygame.image.load('f7.png')) # Hielo
    return imagenes

# Creamos la matriz
matriz = np.random.choice([0, 1, 2], (35, 35))

# Inicializamos Pygame
pygame.init()

# Creamos la pantalla
pantalla = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Simulador de ecosistema")


# Cargamos las imágenes
imagenes = cargar_imagenes()

# Dibujamos la matriz
for i in range(14):
    for j in range(14):
        pantalla.blit(imagenes[matriz[i, j]], (j * 50, i * 50))

# Actualizamos la pantalla
pygame.display.update()

# Mantenemos la ventana abierta hasta que el usuario la cierre
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
            quit()
