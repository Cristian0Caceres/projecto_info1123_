import pygame,sys
from pygame.locals import *
import numpy as np

# Cargamos las imágenes
def cargar_imagenes():
    imagenes = []
    imagenes.append(pygame.image.load('25/f1.png'))
    imagenes.append(pygame.image.load('25/f2.png'))
    imagenes.append(pygame.image.load('25/f3.png'))
    imagenes.append(pygame.image.load('25/f4.png'))
    imagenes.append(pygame.image.load('25/f5.png'))
    imagenes.append(pygame.image.load('25/f6.png'))
    imagenes.append(pygame.image.load('25/f7.png'))
    imagenes.append(pygame.image.load('25/f8.png'))
    imagenes.append(pygame.image.load('25/f9.png'))
    imagenes.append(pygame.image.load('25/f10.png'))
    imagenes.append(pygame.image.load('25/f11.png'))
    imagenes.append(pygame.image.load('25/f13.png'))
    return imagenes


# Inicializamos Pygame
pygame.init()

# Creamos la pantalla
pantalla = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Simulador de ecosistema")


# Cargamos las imágenes
imagenes = cargar_imagenes()
## Crear la matriz , Primera capa , es el mar 
for i in range(24):
    for j in range(32):
        pantalla.blit(imagenes[8], (j * 25, i * 25))
#-----------------------------------------------
# Primer: DECIERTO
#-----------------------------------------------
Decierto_1 = [[0,0,0,0,1,1,1,2,2,3],[0,1,2,3,0,1,2,0,1,0]]

for x in range(2):
    for y in range(len(Decierto_1[0])):
        pantalla.blit(imagenes[1],(Decierto_1[0][y]*25,Decierto_1[1][y]*25))

Decierto_2 = [[0,0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,6,6,7,7,7,8,8,8,9],[15,16,17,18,19,20,21,16,17,18,19,20,21,22,16,17,18,19,20,21,22,23,24,25,26,17,18,19,20,21,22,23,24,25,18,19,20,21,22,23,24,19,20,21,22,23,21,22,20,21,22,21,19,20,20]]

for x in range(2):
    for y in range(len(Decierto_2[0])):
        pantalla.blit(imagenes[1],(Decierto_2[1][y]*25,Decierto_2[0][y]*25))


borde_inferior_decierto = [[14,15,16,17,18,19,19,19,20,20,20,20,21,21,21,21,22,22,22,22,23,23,23,23],[0,1,2,15,15,5,14,15,5,6,15,16,6,7,14,15,8,13,14,15,9,12,13,14]]
for x in range(2):
    for y in range(len(borde_inferior_decierto[0])):
        pantalla.blit(imagenes[1],(borde_inferior_decierto[1][y]*25,borde_inferior_decierto[0][y]*25))

## MAPA ANTARTICA:
Antartica = ([0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4,5,5,5,6,6,7,7,8],[15,16,17,18,19,20,21,22,23,16,17,18,19,20,21,22,23,17,18,19,20,21,23,17,18,19,20,18,19,20,21,22,23,21,22,23,22,23,22,23,23])
for x in range(2):
    for y in range(len(Antartica[0])):
        pantalla.blit(imagenes[11],(Antartica[0][y]*25,Antartica[1][y]*25))

## MAPA DE SELVA:
Selva = [[15,16,16,16,16,16,16,16,17,17,17,17,17,17,17,17,17,18,18,18,18,18,18,18,19,19,19,19,19,19,19,19,19,20,20,20,20,20,20,20,20,20,21,21,21,21,21,21,21,21,22,22,22,22,22,23,23,23,24,24,25,25,25,26,26],[23,16,17,18,19,21,22,23,15,16,17,18,19,20,21,22,23,15,16,17,18,19,20,23,14,15,16,17,18,19,20,22,23,15,16,17,18,19,20,21,22,23,16,17,18,19,20,21,22,23,18,20,21,22,23,21,22,23,22,23,21,22,23,22,23]]
for x in range(2):
    for y in range(len(Selva[0])):
        pantalla.blit(imagenes[2],(Selva[0][y]*25,Selva[1][y]*25))
## MAPA DE BOSQUE:
Bosque_S = [[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,10,10,11],[22,23,24,25,26,27,28,29,30,31,23,24,25,26,27,28,29,30,31,28,29,30,31,27,28,29,30,31,26,27,28,29,30,31,25,26,27,28,29,30,31,24,25,26,27,28,29,30,31,23,24,25,26,27,28,29,30,31,23,24,25,26,27,28,29,30,31,22,23,24,26,27,21,22,23,28,29,30,31,21,22,22]]

for x in range(2):
    for y in range(len(Bosque_S[0])):
        pantalla.blit(imagenes[4],(Bosque_S[1][y]*25,Bosque_S[0][y]*25))


Bosque_I = [[20,20,21,21,21,22,22,22,22,22,23,23,23,23,23,24,24,24,24,24,24,25,25,25,25,25,25,25,26,26,26,26,26,26,26,26,26,27,27,27,27,27,27,27,27,27,27,27,28,28,28,28,28,28,28,28,28,28,28,29,29,29,29,29,29,29,29,29,29,29,29,30,30,30,30,30,30,30,30,30,30,30,30,31,31,31,31,31,31,31,31,31,31,31,31],[13,14,13,14,15,13,14,15,16,17,13,14,15,16,17,11,12,13,14,15,16,11,12,13,14,15,16,17,10,11,12,13,14,15,16,17,18,11,12,13,14,15,16,17,18,21,22,23,12,13,14,15,16,17,18,20,21,22,23,12,13,14,15,16,17,18,19,20,21,22,23,12,13,14,15,16,17,18,19,20,21,22,23,12,13,14,15,16,17,18,19,20,21,22,23]]
for x in range(2):
    for y in range(len(Bosque_I[0])):
        pantalla.blit(imagenes[3],(Bosque_I[0][y]*25,Bosque_I[1][y]*25))


# ## MAPA DE ISLA:
Isla_S = [[3,3,4,4,4,5,5,5,5,5,6,6,6,6],[4,5,4,5,6,3,4,5,6,7,4,5,6,7]]
for x in range(2):
    for y in range(len(Isla_S[0])):
        pantalla.blit(imagenes[0],(Isla_S[0][y]*25,Isla_S[1][y]*25))

Isla_I = [[3,4,4,5,6,7,7,7,7],[6,7,8,8,8,4,5,6,7]]
for x in range(2):
    for y in range(len(Isla_I[0])):
        pantalla.blit(imagenes[5],(Isla_I[0][y]*25,Isla_I[1][y]*25))
# Actualizamos la pantalla
pygame.display.update()

# Mantenemos la ventana abierta hasta que el usuario la cierre
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
            quit()
