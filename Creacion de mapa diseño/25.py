import pygame,sys
from pygame.locals import *
import numpy as np
import random
import time


# Cargamos las imágenes
def cargar_imagenes():
    imagenes = []
    imagenes.append(pygame.image.load('25/f3.png')) # Verde claro 1 [0]
    imagenes.append(pygame.image.load('25/f5.png')) # Verde claro 2 [1]
    imagenes.append(pygame.image.load('25/f4.png')) # Verde oscuro [2]

    imagenes.append(pygame.image.load('25/f2.png')) # Naranjo [3]
    imagenes.append(pygame.image.load('25/f1.png')) # Rojo [4]

    imagenes.append(pygame.image.load('25/f11.png'))# Blanco [5]
    imagenes.append(pygame.image.load('25/f13.png')) # Crema [6]
    imagenes.append(pygame.image.load('25/f6.png')) # Gris [7]
    imagenes.append(pygame.image.load('25/f9.png')) # Celeste [8]


    imagenes.append(pygame.image.load('25/f7.png')) # Rosa [9]
    imagenes.append(pygame.image.load('25/f8.png')) # Purpura 1 [10]
    imagenes.append(pygame.image.load('25/f10.png')) # Purpura 2 [11]

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
Clock = pygame.time.Clock()


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

def Meteorito(meteoritos = 40):
    imagenes = cargar_imagenes()
    if meteoritos== 40:
        for x in range(40):
            zona_Afectada_X = random.randint(0,31)
            zona_Afectada_Y = random.randint(0,23)
            pantalla.blit(imagenes[4], (zona_Afectada_X * 25, zona_Afectada_Y * 25))
            pygame.display.update()
            time.sleep(0.1)
    if meteoritos == 10:
        for x in range(10):
            zona_Afectada_X = random.randint(0,31)
            zona_Afectada_Y = random.randint(0,23)
            pantalla.blit(imagenes[7], (zona_Afectada_X * 25, zona_Afectada_Y * 25))
            pygame.display.update()
            time.sleep(0.3)
            



def Terremoto():
    for x in range(len(matris)-1):
        for j in range(len(matris[x])):
            valor = matris[x][j]
            matris[x][j] = matris[x+1][j]
            matris[x+1][j] = valor
            # pantalla.blit(imagenes[matris[x][j]], (j * 25, x * 25))
            # time.sleep(0.003
    print('listo')

def Pinta_Mapa():
    for i in range(24):
        for j in range(32):
            pantalla.blit(imagenes[matris[i][j]], (j * 25, i * 25))
            pygame.display.update()
    print('laaaaaaaaaaaaaaaaa')


Ciclo_Transcurrido = 0
bucle = 0



## WHILE PRINCIPAL 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            Meteorito(10)
        if event.key == pygame.K_RIGHT:
            Terremoto()
            Pinta_Mapa()
# -----------------------------------------Cilco de meteoritos

    bucle += 1
    if bucle == 60:
        Ciclo_Transcurrido += 1
        bucle = 0
    if Ciclo_Transcurrido == 10:
        Meteorito()
        Ciclo_Transcurrido = 0
# -----------------------------------------Cilco de meteoritos
    pygame.display.update()
    pygame.display.flip()
    Clock.tick(60)
