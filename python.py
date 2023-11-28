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
posibles_estados = ["vivo","muelto"]
posibles_generos = ["macho","hembra","planti"] ; running = True
posibles_dietas  = ["carnivoro","herviro",]; all_sprites = py.sprite.Group()
mapa = [] ; clock = py.time.Clock()
ROWS, COLS = 14, 14;todos = py.sprite.Group()
cuadrado_SIZE = ancho // ROWS;FPS = 60;MAX_HIJOS = 6;TIEMPO_REPRODUCCION = FPS * 3;MAX_ANIMALES = 15
py.init()
#-------------------------
#CLASES
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
            numerocromosomico=ra.randint in range (0,2)
            hervorcar=ra.randint in range (0,2)
            hijo = Animal(self.hp,self.dmg,self.enrg,self.water,self.estate,self.gender,self.diet,self.color, self.rect.x, self.rect.y,self.postx,self.posty)
            self.hijos.append(hijo)
            otro.hijos.append(hijo)
            self.tiempo_reproduccion = 0
            return hijo
        return None

    def mover(self):
        self.rect.x += ra.randint(-1, 1)
        self.rect.y += ra.randint(-1, 1)

        # If the animal is blue (a herbivore), check for collision with plants
        if self.color == (0, 0, 255):
            hit_list = py.sprite.spritecollide(self, todos, False)
            for hit in hit_list:
                if isinstance(hit, Planta):
                    # Eat the plant and remove it from the game
                    self.tiempo_reproduccion -= 10  # Eating a plant decreases the reproduction time
                    todos.remove(hit)

    def actualizar(self):
        self.tiempo_reproduccion += 1

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
            self.enrg = int(self.water) -1
            self.death()
            return [(self.postx + ra.randint(-10, 10), self.posty + ra.randint(-10, 10)) for _ in range(ra.randint(0, 2))]
        else:
            self.repcont += 1
            return []
    def dibujar(self, ventana):
        py.draw.polygon(ventana, self.color, [(self.postx, self.posty), (self.postx + 5, self.posty + 5), (self.postx, self.posty + 5)])

class ambiente:
    def __init__(self,agua,humedad,tipo):
        self.h2o   = agua
        self.hume  = humedad
        self.type = tipo
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
    imagenes.append(py.image.load('agua.png'))
    imagenes.append(py.image.load('tierra.png'))
    imagenes.append(py.image.load('arena.png'))
    imagenes.append(py.image.load('montaña.png'))
    return imagenes
imagenes = cargar_imagenes()

#--------------------------
#Matriz
#--------------------------
grid = [[(ra.randint(0, len(imagenes)-1), ambiente(ra.randint(0, 100), ra.randint(0, 100), ra.choice(['tierra', 'arena', 'montaña', 'agua']))) for ax in range(COLS)] for ay in range(ROWS)]
#-------------------------
#animales
#-------------------------
colores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
for color in colores:
    numerocromosomico=ra.randint in range (0,2)
    hervorcar=ra.randint in range (0,2)
    animal = Animal(100,10,100,100,"vivo","macho" if numerocromosomico < 1 else "hembra","hervivoros" if hervorcar > 0 else "carnivoro",color, ra.randint(ancho // 2 - 50, ancho // 2 + 50), ra.randint(largo // 2 - 50, largo // 2 + 50),0,0)
    todos.add(animal)
    animal = Animal(100,10,100,100,"vivo","macho" if numerocromosomico < 1 else "hembra","hervivoros" if hervorcar > 0 else "carnivoro",color, ra.randint(ancho // 2 - 50, ancho // 2 + 50), ra.randint(largo // 2 - 50, largo // 2 + 50),0,0)
    todos.add(animal)
#-------------------------
#MAIN
#-------------------------

def main(ancho,largo,grid,Planta):
    pantalla= py.display.set_mode((ancho,largo))
    all_sprites.draw(pantalla)
    coloores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
    plantas = [Planta(10, 0, 50, 50, "vivo", "planti", ra.randint(0, 700), ra.randint(0, 700), "fotosintetico", color) for color in coloores for _ in range(3)]
    contador_coloores = {color: 3 for color in coloores}

    for row in range(ROWS):
        for col in range(COLS):
            indice, ambiente = grid[row][col]
            pantalla.blit(imagenes[indice], (row*cuadrado_SIZE, col*cuadrado_SIZE))
            ambiente.humedads()
            ambiente.sequia()
            ambiente.water()

    py.display.update()

    #-------------------------
    # CICLO PRINCIPAL
    #-------------------------
    contadores_color = {color: 1 for color in colores}
    running=True
    while running:

        for animal in todos:
            animal.mover()
            animal.actualizar()
            for otro in todos:
                if animal != otro and py.sprite.collide_rect(animal, otro):
                    hijo = animal.reproduction(otro, todos)
                    if hijo is not None:
                        todos.add(hijo)
                        contadores_color[hijo.color] += 1
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
        clock.tick(60)
    py.quit()

#---------------------------------------------------------------------
# Inicializa Superficie del Super Extra Mega Mapa.-
#---------------------------------------------------------------------

def Get_Surface(ancho,alto):
    return py.Surface((ancho,alto))

if __name__ == "__main__":
    main(ancho,largo,grid,Planta)
