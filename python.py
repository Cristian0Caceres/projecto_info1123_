#-------------------------
#SIMULADOR DE ECOSISTEMA
#-------------------------
import pygame as py 
from pygame.locals import *
import numpy  as np
import random as ra
import time as ti
#-------------------------
#CONSTANTES
#-------------------------

ancho, largo = 700 , 700 ; ncx,ncy = 5,5
dimCW= ancho / ncx ; dimCH= largo / ncy
posibles_ambientes = ["arido", "humedo", "templado", "frio", "caluroso"]
posibles_estados = ["vivo","muelto","cazando","bebiendo","reproduciendoce","diambulando",]
posibles_generos = ["macho","hembra","planti"] ; running = True
posibles_dietas  = ["carnivoro","herviro",]; all_sprites = py.sprite.Group()
mapa = [] ; clock = py.time.Clock()

#-------------------------
#CLASES
#-------------------------

class organismo:
    def __init__(self,vida,daño,energia,sed,movimiento,estado,genero,posicionx,posiciony,dieta):
        self.hp      =       vida
        self.dmg     =       daño
        self.enrg    =    energia
        self.water   =        sed
        self.move    = movimiento
        self.estate  =     estado
        self.gender  =     genero
        self.postx   =  posicionx
        self.posty   =  posiciony
        self.diet    =      dieta
        self.repcont =          0

    def inanicion_desidratacion(self):
        self.enrg  = int(self.enrg)  - 1
        self.water = int(self.water) - 1
        if self.enrg < 100:
            self.hp = self.hp - 1
        if self.water < 100:
            self.hp = self.hp - 1
        death(self)
    def death(self):
        if self.hp < 1:
            self.estate = "Muerto"

    def reproduction (self):
        pass

class Animal(organismo, py.sprite.Sprite):
    def __init__(self, vida, daño, energia, sed, movimiento, estado, genero, posicionx, posiciony, dieta,colour):
        super().__init__(vida, daño, energia, sed, movimiento, estado, genero, posicionx, posiciony, dieta)
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface([10, 10])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = ra.randrange(700)
        self.rect.y = ra.randrange(700)

    def update(self):
        self.rect.x += ra.choice([-20, 20])
        self.rect.y += ra.choice([-20, 20])
        if self.rect.x < 0 or self.rect.x > 690:
            self.rect.x = ra.randrange(700)
        if self.rect.y < 0 or self.rect.y > 690:
            self.rect.y = ra.randrange(700)

    def inanicion_desidratacion(self):
        return super().inanicion_desidratacion()
    def death(self):
        return super().death()
    def max_move(self):
        return super().max_move()

class planta (organismo):
    def __init__(self, vida, daño, energia, sed, movimiento, estado, genero, posicionx, posiciony, dieta):
        super().__init__(vida, daño, energia, sed, movimiento, estado, genero, posicionx, posiciony, dieta)
    def desidratacion(self):
        if super().water == 0:
            super().hp = super().hp - 1
    def death(self):
        return super().death()

class ambiente:
    def __init__(self,agua,humedad,condiciones_meteorologicas,tipo):
        self.h2o   = agua
        self.hume  = humedad
        self.cm    = condiciones_meteorologicas
        self.type = tipo
    def humedads(self):
        if self.h2o < 100:
            self.hume = self.hume-1

    def sequia(self):
        if self.h2o < 1:
            self.h2o == 0
            self.fert = self.fert - 1
            self.hume = 0
            self.temp = self.temp + 1
            self.type = "arido"
    def water(self):
        liquido= self.h2o
        rehidratacion=ra.randint in range (0, 4)
        if self.hume > 33 :
            self.h2o=liquido + rehidratacion

#--------------------------
#Matriz
#--------------------------
matriz = np.random.choice([0, 1, 2,3], (44, 44))
#-------------------------
#animales
#-------------------------

for i in range(30):
    colour = (ra.randrange(256), ra.randrange(150), ra.randrange(120))
    vida = 100
    daño = 10 if i < 5 else 0  # Los primeros 5 animales son agresivos
    energia = 100
    sed = 100
    movimiento = 1
    estado = "Vivo"
    genero = "Macho" if i % 2 == 0 else "Hembra"
    posicionx = ra.randrange(700)
    posiciony = ra.randrange(700)
    dieta = "Carnívoro" if i < 5 else "Herbívoro"
    animal = Animal( vida, daño, energia, sed, movimiento, estado, genero, posicionx, posiciony, dieta,colour)
    all_sprites.add(animal)

#-------------------------
#FUNCIONES
#-------------------------
def cargar_imagenes():
    imagenes = []
    imagenes.append(py.image.load('agua.png'))
    imagenes.append(py.image.load('tierra.png'))
    imagenes.append(py.image.load('arena.png'))
    imagenes.append(py.image.load('montaña.png'))
    return imagenes
imagenes = cargar_imagenes()
#-------------------------
#MAIN
#-------------------------
py.init()

def main(ancho,largo,mapa):
    pantalla= py.display.set_mode((ancho,largo))
    for i in range(14):
        for j in range(14):
            pantalla.blit(imagenes[matriz[i, j]], (j * 50, i * 50))
            all_sprites.draw(pantalla)
    py.display.update()

#---------------------------------------------------------------------
# Inicializa Superficie del Super Extra Mega Mapa.-
#---------------------------------------------------------------------

def Get_Surface(ancho,alto):
    return py.Surface((ancho,alto))

#-------------------------
# CICLO PRINCIPAL
#-------------------------

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    all_sprites.update()
    main(largo,ancho,mapa)
    py.display.flip()
    ti.sleep(0)
    clock.tick(6)
py.quit()
