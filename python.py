#-------------------------
#SIMULADOR DE ECOSISTEMA
#-------------------------
import pygame as py 
from pygame.locals import *
import numpy  as np
import random as ra
import time as ti
#-------------------------------------
#constantes
#---------------------------------------
ancho, largo = 1000 , 600 ; ncx,ncy = 5,5
dimCW= ancho / ncx ; dimCH= largo / ncy
posibles_estados = ["vivo","muelto"]
posibles_generos = ["macho","hembra","planti"] ; running = True
posibles_dietas  = ["carnivoro","herviro",]; all_sprites = py.sprite.Group()
mapa = [] ; clock = py.time.Clock()
ROWS, COLS = 14, 14;todos = py.sprite.Group()
cuadrado_SIZE = ancho // ROWS;FPS = 60;MAX_HIJOS = 6;TIEMPO_REPRODUCCION = FPS * 3;MAX_ANIMALES = 15
psiblecoloranimal=['rojo', 'azul', 'negro', 'amarillo', 'morado', 'verde', 'cafe', 'naranja', 'rosa', 'vino']

py.init()
#-------------------------
#CLASES Y METODOS
#-------------------------

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
        self.enrg  = int(self.enrg)  - 10
        self.water = int(self.water) - 10
        if self.enrg < 100:
            self.hp = self.hp - 10
        if self.water < 100:
            self.hp = self.hp - 10

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
            hijo = Animal(self.hp,self.dmg,self.enrg,self.water,self.estate,self.gender,self.diet,otro.color, self.rect.x, self.rect.y,self.postx,self.posty)
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
            self.water = min(100, self.water + 10)
            self.sed = max(0, self.sed - 10)


class Planta (Organismo):
    def __init__(self, vida, daño, energia, sed, estado, genero, posicionx, posiciony, dieta, color):
        super().__init__(vida, daño, energia, sed, estado, genero, posicionx, posiciony, dieta, color)
        self.cycles=0

    def desidratacion(self):
        if self.water < 50 or self.cycles % 12 == 0:
            self.hp = self.hp - 10

    def death(self):
        if self.hp < 1 or self.cycles >= 60 or ra.random() < 0.01: 
            self.estate = "Muerto"
        return super().death()
    def reproduction(self):
        if self.repcont >= 6:
            self.repcont = 0
            self.enrg = int(self.water) - 1
            self.death()
            if self.postx > 600 or self.postx < -600:
                if self.posty > 600 or self.posty < -600:
                    return [(self.postx, self.posty) for _ in range(ra.randint(0, 2))]
                else:
                    return [(self.postx, self.posty + ra.randint(-10, 10)) for _ in range(ra.randint(0, 2))]
            else:
                return [(self.postx + ra.randint(-10, 10), self.posty + ra.randint(-10, 10)) for _ in range(ra.randint(0, 2))]
        else:
            self.repcont += 1
            return []

    def dibujar(self, ventana):
        py.draw.polygon(ventana, self.color, [(self.postx, self.posty), (self.postx + 5, self.posty + 5), (self.postx, self.posty + 5)])

class ambiente:
    def __init__(self,agua,humedad,tipo,psy,psx):
        self.h2o   =    agua
        self.hume  = humedad
        self.type  =    tipo
        self.posy  =     psy
        self.posx  =     psx
    def humedads(self):
        if self.h2o < 100:
            self.hume = self.hume-1

    def sequia(self):
        if self.h2o < 1:
            self.h2o == 0
            self.hume = 0
            self.type = "arido"
    def water(self):
        liquido= self.h2o
        rehidratacion=ra.randint in range (0, 4)
        if self.hume > 33 :
            self.h2o=liquido + rehidratacion
#-------------------------
#FUNCIONES
#-------------------------
def cargar_imagenes():
    imagenes = []
    imagenes.append(py.image.load('f3.png')) # Verde claro 1
    imagenes.append(py.image.load('f5.png')) # Verde claro 2
    imagenes.append(py.image.load('f4.png')) # Verde oscuro

    imagenes.append(py.image.load('f2.png')) # Naranjo
    imagenes.append(py.image.load('f1.png')) # Rojo

    imagenes.append(py.image.load('f11.png'))# Blanco
    imagenes.append(py.image.load('f13.png')) # Crema
    imagenes.append(py.image.load('f6.png')) # Gris
    imagenes.append(py.image.load('f9.png')) # Celeste


    imagenes.append(py.image.load('f7.png')) # Rosa
    imagenes.append(py.image.load('f8.png')) # Purpura 1
    imagenes.append(py.image.load('f10.png')) # Purpura 2

    return imagenes

#--------------------------
#Matriz
#--------------------------
grid = [
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
def Crea_Mapa(grid):
    imagenes = cargar_imagenes()
    for i in range(24):
        for j in range(32):
            if grid[i][j] == 0:
                pantalla.blit(imagenes[0], (j * 25, i * 25))
                ambiente(70, 60, 'tierra',  j * 25, i * 25)
            if grid[i][j] == 1:
                pantalla.blit(imagenes[1], (j * 25, i * 25))
                ambiente(30, 30,"semi arido",  j * 25, i * 25)
            if grid[i][j] == 2:
                pantalla.blit(imagenes[2], (j * 25, i * 25))
                ambiente(60, 50,"terroso",  j * 25, i * 25)
            if grid[i][j] == 3:
                pantalla.blit(imagenes[3], (j * 25, i * 25))
                ambiente(30, 30,"semi arido",  j * 25, i * 25)
            if grid[i][j] == 4:
                pantalla.blit(imagenes[4], (j * 25, i * 25))
                ambiente(30, 30,"semi arido",  j * 25, i * 25)
            if grid[i][j] == 5:
                pantalla.blit(imagenes[5], (j * 25, i * 25))
                ambiente(30, 30,"semi arido",  j * 25, i * 25)
            if grid[i][j] == 6:
                pantalla.blit(imagenes[6], (j * 25, i * 25))
                ambiente(30, 30,"semi arido",  j * 25, i * 25)
            if grid[i][j] == 7:
                pantalla.blit(imagenes[7], (j * 25, i * 25))
                ambiente(30, 30,"semi arido",  j * 25, i * 25)
            if grid[i][j] == 8:
                pantalla.blit(imagenes[8], (j * 25, i * 25))
                ambiente(30, 30,"semi arido",  j * 25, i * 25)

#-------------------------
#animales
#-------------------------
for color in psiblecoloranimal:
    if color == "rojo":
        color =((255,0,0))
    if color == "azul":
        color =((0,0,255))
    if color == "negro":
        color =((0,0,0))
    if color == "amarillo":
        color =((255,255,0))
    if color == "morado":
        color =((120,40,140))
    if color == "verde":
        color =((0,143,57))
    if color == "cafe":
        color =((161,130,98))
    if color == "naranja":
        color =((255,128,0))
    if color == "rosa":
        color =((234,137,154))
    if color == "vino":
        color =((94,33,41))
    x = ra.choice([ra.randint(0, (ancho-400) // 2 - 25), ra.randint((ancho-400) // 2 + 25, (ancho-400))])
    y = ra.choice([ra.randint(0, largo // 2 - 25), ra.randint(largo // 2 + 25, largo)])
    numerocromosomico=ra.randint in range (0,2)
    hervorcar=ra.randint in range (0,2)
    animal = Animal(100,10,100,100,"vivo"
    ,"macho" if numerocromosomico < 1 else "hembra","hervivoros" if hervorcar > 0 else "carnivoro",color,x,y,0,0)
    todos.add(animal)
    animal = Animal(100,10,100,100,"vivo"
    ,"macho" if numerocromosomico < 1 else "hembra","hervivoros" if hervorcar > 0 else "carnivoro",color,x,y,0,0)
    todos.add(animal)
pantalla= py.display.set_mode((ancho,largo))
all_sprites.draw(pantalla)
coloores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
plantas = [Planta(10, 0, 50, 50, "vivo", "planti", ra.randint(0, 600)
, ra.randint(0, 600), "fotosintetico", color) for color in coloores for _ in range(3)]
contador_coloores = {color: 3 for color in coloores}



#-------------------------
# CICLO PRINCIPAL
#-------------------------
contadores_color = {color: 1 for color in psiblecoloranimal}
running=True
while running:
    pantalla.fill((128,128,128))
    Crea_Mapa(grid)
    for animal in todos:
        animal.beber_agua(grid)
        animal.mover()
        animal.actualizar()
        for otro in todos:
            if animal != otro and py.sprite.collide_rect(animal, otro):
                hijo = animal.reproduction(otro, todos)
                if hijo is not None:
                    todos.add(hijo)
                    try:
                        contadores_color[hijo.color] += 1
                    except Exception as e:
                        print("-----------------------------")
                        print("error code:",e)
                        print("-----------------------------")


                        print("Estoy cansado jefe")
    all_sprites.update()
    nuevas_plantas = []
    for planta in plantas:
        planta.cycles += 1
        planta.dibujar(pantalla)
        nuevas_posiciones = planta.reproduction()
        for pos in nuevas_posiciones:
            if contador_coloores[planta.color] < 600:
                nuevas_plantas.append(Planta(100, 0, 50, 50, "vivo", "planti", pos[0], pos[1], "fotosintetico", planta.color))
                contador_coloores[planta.color] += 1
        planta.desidratacion()
        planta.death()
        if planta.estate == "Muerto":
            plantas.remove(planta)
            contador_coloores[planta.color] -= 1
    plantas.extend(nuevas_plantas)
    todos.draw(pantalla)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    all_sprites.update()
    py.display.flip()
    ti.sleep(0)
    clock.tick(6000)
py.quit()
