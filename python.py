#-------------------------
#SIMULADOR DE ECOSISTEMA
#-------------------------
import pygame as py 
import numpy  as np
import rxpy   as rp
import random as ra
#-------------------------
#CONSTANTES
#-------------------------

ancho, largo = 700 , 1000 ; ncx,ncy = 5,5
dimCW= ancho / ncx ; dimCH= largo / ncy
posibles_ambientes = ["arido", "humedo", "templado", "frio", "caluroso"]
posibles_estados = ["vivo","muelto","cazando","bebiendo","reproduciendoce","diambulando",]
posibles_generos = ["macho","hembra","planti"] ; running = True
posibles_dietas  = ["carnivoro","herviro","fotosintetico"]; all_sprites = py.sprite.Group()
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
        if self.enrg < 100:
            self.hp = self.hp - 1
        if self.water < 100:
            self.hp = self.hp - 1

    def death(self):
        if self.hp < 1:
            self.estate = "Muerto"

    def reproduction (self):
        pass
    def max_move(self):
        if self.postx > 25:
            self.postx = 25
            self.postx = 25
        if self.posty > 25:
            self.posty = 25

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
    def __init__(self,agua,fertilidad,temperatura,humedad,condiciones_meteorologicas,sotenibilidad,tipo):
        self.h2o   = agua
        self.fert  = fertilidad
        self.temp  = temperatura
        self.hume  = humedad
        self.cm    = condiciones_meteorologicas
        self.soste = sotenibilidad
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
#Mapa
#--------------------------

for i in range(5):
    fila = []
    for j in range(5):
        agua = ra.randint(0, 100);fertilidad = ra.randint(0, 100)
        temperatura = ra.randint(-30, 50);humedad = ra.randint(0, 100)
        condiciones_meteorologicas = ra.choice(["soleado", "nublado", "lluvioso", "nevado"]);sostenibilidad = ra.randint(0, 100)
        tipo = ra.choice(posibles_ambientes)
        fila.append(ambiente(agua, fertilidad, temperatura, humedad, condiciones_meteorologicas, sostenibilidad, tipo))
    mapa.append(fila)

#-------------------------
#animales
#-------------------------

for i in range(10):
    colour = (ra.randrange(256), ra.randrange(256), ra.randrange(256))
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
def Load_Image(sFile,transp = False):
    try: image = py.image.load(sFile)
    except py.error as message:
            raise SystemExit.message
    image = image.convert()
    if transp:
        color = image.get_at((0,0))
        image.set_colorkey(color.RLEACCEL)
    return image

def Img_Init():
    aImg = []
    aImg.append(Load_Image('T02.png',False )) # Tierra
    aImg.append(Load_Image('T03.png',False )) # montaña
    aImg.append(Load_Image('T04.png',False )) # ¿hielo?
    return aImg

#-------------------------
#MAIN
#-------------------------
py.init()

def main(ancho,largo,mapa):
    pantalla= py.display.set_mode((ancho,largo))
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            mapa[i][j].humedads()
            mapa[i][j].sequia()
            mapa[i][j].water()
            color = (0, mapa[i][j].fert, mapa[i][j].h2o)
            py.draw.rect(pantalla, color, py.Rect(i*dimCW, j*dimCH, dimCW, dimCH))
            all_sprites.draw(pantalla)

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
    clock.tick(5)
py.quit()
