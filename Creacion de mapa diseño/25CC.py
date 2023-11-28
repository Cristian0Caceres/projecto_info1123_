# --------------------------------------------------
#SIMULADOR DE ECOSISTEMA
#------------------------------------------------------
import pygame as py 
from pygame.locals import *
import numpy  as np
import random as ra
import time as ti
import sys
#-------------------------
#   CONSTANTES
#-------------------------

ancho, largo = 700 , 700 ; 
ncx,ncy = 5,5
dimCW= ancho / ncx ; 
dimCH= largo / ncy
posibles_ambientes = ["arido", "humedo", "templado", "frio", "caluroso"]
posibles_estados = ["vivo","muelto"]
posibles_generos = ["macho","hembra","planti"] ; running = True
posibles_dietas  = ["carnivoro","herviro",];
all_sprites = py.sprite.Group()

clock = py.time.Clock()
ROWS, COLS = 14, 14;todos = py.sprite.Group()
cuadrado_SIZE = ancho // ROWS;FPS = 60;MAX_HIJOS = 6;TIEMPO_REPRODUCCION = FPS * 3;MAX_ANIMALES = 15
# -----------------------------------------------
# INICIALIZAR PYgame
# ------------------------------------------------
py.init()
pantalla = py.display.set_mode((1000, 600))
py.display.set_caption("Simulador de ecosistema")

class Organismo:
    def __init__(self,vida,daño,energia,sed,estado,genero,posicionx,posiciony,dieta,color):
        self.hp      =       vida
        self.dmg     =       daño
        self.enrg    =    energia
        self.water   =        sed
        self.estate  =     estado
        self.gender  =     genero
        self.postx   =  posicionx
        self.posty   =  posiciony
        self.diet    =      dieta
        self.repcont =          0
        self.color   =      color


    def death(self):
        if self.hp < 1:
            self.estate = "Muerto"

    def inanicion_desidratacion(self):
        self.enrg  = int(self.enrg)  - 1
        self.water = int(self.water) - 1
        if self.enrg < 100:
            self.hp = self.hp - 1
        if self.water < 100:
            self.hp = self.hp - 1
class Animal(Organismo, py.sprite.Sprite):
    def __init__(self, vida, daño, energia, sed, estado, genero,dieta, color, x, y,posicionx,posiciony):
        super().__init__(vida, daño, energia, sed, estado, genero,dieta,color,posicionx,posiciony)
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface([10, 10])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hijos = []
        self.tiempo_reproduccion = 0

    def inanicion_desidratacion(self):
        return super().inanicion_desidratacion()
    def death(self):
        return super().death()
    def reproduction (self, otro, todos):
        if (self.color == otro.color and otro not in self.hijos and self not in otro.hijos and
            self.tiempo_reproduccion >= TIEMPO_REPRODUCCION and len(self.hijos) < MAX_HIJOS and
            len([x for x in todos if x.color == self.color]) < MAX_ANIMALES):
            hijo = Animal(self.hp,self.dmg,self.enrg,self.water,self.estate,self.gender,self.diet,self.color, self.rect.x, self.rect.y,self.postx,self.posty)
            self.hijos.append(hijo)
            otro.hijos.append(hijo)
            self.tiempo_reproduccion = 0
            return hijo
        return None

    def mover(self):
        self.rect.x += ra.randint(-1, 1)
        self.rect.y += ra.randint(-1, 1)


        if self.color == (0, 0, 255):
            hit_list = py.sprite.spritecollide(self, todos, False)
            for hit in hit_list:
                if isinstance(hit, Planta):

                    self.tiempo_reproduccion -= 10
                    todos.remove(hit)

    def actualizar(self):
        self.tiempo_reproduccion += 1

    def beber_agua(self, grid):
        celda_x = int(self.rect.x // dimCW)
        celda_y = int(self.rect.y // dimCH)

        if grid[celda_y][celda_x] == 0:
            self.agua = min(100, self.agua + 10)
            self.sed = max(0, self.sed - 10)


# Cargamos las imágenes
def cargar_imagenes():
    imagenes = []
    imagenes.append(py.image.load('25CC/f5.jpg')) # VERDE  [0]
    imagenes.append(py.image.load('25CC/f7.jpg')) # NARANJA [1]
    imagenes.append(py.image.load('25CC/f4.jpg')) # ROJO [2]
    imagenes.append(py.image.load('25CC/f3.jpg')) # MORADO 1[3]
    imagenes.append(py.image.load('25CC/f6.jpg')) # AMARILLO [4]
    imagenes.append(py.image.load('25CC/f1.jpg')) # GRIS [5]
    imagenes.append(py.image.load('25CC/f2.jpg')) # CELESTE 1 [6] 
    imagenes.append(py.image.load('25CC/f9.jpg')) # CELESTE 2 [7]
    imagenes.append(py.image.load('25CC/f8.jpg')) # MORADO 2[8]
    return imagenes


def MATRIS_SIMULADOR():
    imagenes = cargar_imagenes()
    matris = [
        [3,3,3,3,7,7,7,7,7,7,7,7,7,7,7,1,1,1,1,1,1,1,4,4,4,4,4,4,4,4,4,4],
        [3,3,3,7,7,7,7,7,7,7,7,7,7,7,7,7,1,1,1,1,1,1,1,4,4,4,4,4,4,4,4,4],
        [3,3,7,7,7,7,7,7,7,7,7,7,7,7,7,7,1,1,1,1,1,1,1,1,1,1,1,4,4,4,4,4],
        [3,7,7,7,7,0,7,7,7,7,7,7,7,7,7,7,7,1,1,1,1,1,1,1,1,1,4,4,4,4,4,4],
        [7,7,7,0,0,0,0,2,7,7,7,7,7,7,7,7,7,7,1,1,1,1,1,1,1,4,4,4,4,4,4,4],
        [7,7,7,0,0,0,0,2,7,7,7,7,7,7,7,7,7,7,7,1,1,1,1,1,4,4,4,4,4,4,4,4],
        [7,7,7,2,0,0,0,2,7,7,7,7,7,7,7,7,7,7,7,7,7,1,1,4,4,4,4,4,4,4,4,4],
        [7,7,7,7,2,0,0,2,7,7,7,7,7,7,7,7,7,7,7,1,1,1,1,4,4,4,4,4,4,4,4,4],
        [7,7,7,7,2,2,2,7,7,7,7,7,7,7,7,7,7,7,1,1,1,4,4,4,7,4,4,4,4,4,4,4],
        [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,1,4,4,4,7,7,7,7,4,4,4,4,4],
        [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,4,4,7,7,7,0,7,7,7,7,7,7],
        [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,4,7,0,0,0,0,7,7,7,7,7],
        [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,0,0,0,0,0,0,0,0,0],
        [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [3,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [3,3,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0],
        [3,3,3,7,7,7,7,7,7,7,7,7,7,7,7,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0],
        [3,3,3,3,7,7,7,7,7,7,7,7,7,7,3,2,2,2,2,2,2,0,0,7,0,0,0,0,0,0,0,0],
        [3,3,3,3,3,7,7,7,7,7,7,7,7,7,3,2,2,2,2,2,2,2,7,7,7,0,0,0,0,0,0,0],
        [3,3,3,3,3,3,7,7,7,7,7,7,7,3,3,2,2,2,2,2,2,7,7,7,7,7,7,7,7,0,0,0],
        [3,3,3,7,3,3,3,7,7,7,7,7,7,7,3,3,2,2,2,2,2,2,7,7,7,7,7,7,0,0,0,0],
        [3,3,7,7,3,3,3,7,7,7,7,7,7,3,3,3,2,2,7,7,2,2,2,2,7,2,7,0,0,0,0,0],
        [3,3,3,3,3,3,3,7,7,7,7,7,3,3,3,3,2,2,7,2,2,2,2,2,2,2,2,0,0,0,0,0],
        [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0]
    ]
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

MATRIS_SIMULADOR()
py.display.update()

# Mantenemos la ventana abierta hasta que el usuario la cierre
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()
    if event.type == py.KEYDOWN:
        if event.key == py.K_m:
            py.draw.rect()
            if event.key == py.K_RIGHT:
                speend_x = 3
        if event.type == py.KEYUP:
            if event.key == py.K_LEFT:
                speend_x = 0
            if event.key == py.K_RIGHT:
                speend_x = 0

    MATRIS_SIMULADOR()


    py.display.update()
    py.display.flip()
    clock.tick(150)  
