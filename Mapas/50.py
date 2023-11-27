import pygame,sys
from pygame.locals import *
import numpy as np

# Cargamos las imágenes
def cargar_imagenes():
    imagenes = []
    # imagenes.append(pygame.image.load('10/f1.png'))
    # imagenes.append(pygame.image.load('10/f2.png'))
    # imagenes.append(pygame.image.load('10/f3.png'))
    # imagenes.append(pygame.image.load('10/f4.png'))
    # imagenes.append(pygame.image.load('10/f5.png'))
    # imagenes.append(pygame.image.load('10/f6.png'))
    # imagenes.append(pygame.image.load('10/f7.png'))
    # imagenes.append(pygame.image.load('10/f8.png'))
    # imagenes.append(pygame.image.load('10/f9.png'))
    # imagenes.append(pygame.image.load('10/f10.png'))
    # imagenes.append(pygame.image.load('10/f11.png'))
    # imagenes.append(pygame.image.load('10/f13.png'))

    # imagenes.append(pygame.image.load('20/f1.png'))
    # imagenes.append(pygame.image.load('20/f2.png'))
    # imagenes.append(pygame.image.load('20/f3.png'))
    # imagenes.append(pygame.image.load('20/f4.png'))
    # imagenes.append(pygame.image.load('20/f5.png'))
    # imagenes.append(pygame.image.load('20/f6.png'))
    # imagenes.append(pygame.image.load('20/f7.png'))
    # imagenes.append(pygame.image.load('20/f8.png'))
    # imagenes.append(pygame.image.load('20/f9.png'))
    # imagenes.append(pygame.image.load('20/f10.png'))
    # imagenes.append(pygame.image.load('20/f11.png'))
    # imagenes.append(pygame.image.load('20/f13.png'))

    # imagenes.append(pygame.image.load('25/f1.png'))
    # imagenes.append(pygame.image.load('25/f2.png'))
    # imagenes.append(pygame.image.load('25/f3.png'))
    # imagenes.append(pygame.image.load('25/f4.png'))
    # imagenes.append(pygame.image.load('25/f5.png'))
    # imagenes.append(pygame.image.load('25/f6.png'))
    # imagenes.append(pygame.image.load('25/f7.png'))
    # imagenes.append(pygame.image.load('25/f8.png'))
    # imagenes.append(pygame.image.load('25/f9.png'))
    # imagenes.append(pygame.image.load('25/f10.png'))
    # imagenes.append(pygame.image.load('25/f11.png'))
    # imagenes.append(pygame.image.load('25/f13.png'))

    imagenes.append(pygame.image.load('50/f1.jpg'))
    imagenes.append(pygame.image.load('50/f2.jpg'))
    imagenes.append(pygame.image.load('50/f3.jpg'))
    imagenes.append(pygame.image.load('50/f4.jpg'))
    imagenes.append(pygame.image.load('50/f5.jpg'))
    imagenes.append(pygame.image.load('50/f6.jpg'))
    imagenes.append(pygame.image.load('50/f7.jpg'))
    imagenes.append(pygame.image.load('50/f8.jpg'))
    imagenes.append(pygame.image.load('50/f9.jpg'))
    imagenes.append(pygame.image.load('50/f10.jpg'))
    imagenes.append(pygame.image.load('50/f11.jpg'))
    imagenes.append(pygame.image.load('50/f13.jpg'))
    return imagenes

# Creamos la matriz
matriz = np.random.choice([0,1,2,3,4,5,6,7,8,9,10,11], (14, 14))

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
