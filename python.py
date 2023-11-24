#-------------------------
#Simulador De Ecosistema
#-------------------------
import pygame as py 
import numpy  as np
import time   as ti
from pygame.sprite import _Group
import rxpy   as rp
import random as ra

#-------------------------
#clases
#-------------------------
class organismo(py.sprite.Sprite):
    def __init__(self,vida,daño,energia,sed,movimiento,estado,genero,posicionx,posiciony,dieta, *groups: _Group) -> None:
        super().__init__(*groups)
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

class animal(organismo):
    def __init__(self, vida, daño, energia, sed, movimiento, estado, genero, posicionx, posiciony, dieta, *groups: _Group) -> None:
        super().__init__(vida, daño, energia, sed, movimiento, estado, genero, posicionx, posiciony, dieta, *groups)

    def inanicion_desidratacion(self):
        return super().inanicion_desidratacion()
    def death(self):
        return super().death()
    def max_move(self):
        return super().max_move()




class planta (organismo):
    def __init__(self, vida, daño, energia, sed, movimiento, estado, genero, posicionx, posiciony, dieta, *groups: _Group) -> None:
        super().__init__(vida, daño, energia, sed, movimiento, estado, genero, posicionx, posiciony, dieta, *groups)
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
        if self.hume > 33 :
            self.h2o=self.h2o + ra.randint in range (0, 4)

#-------------------------
#funciones
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
# Creacion de la pantalla
#-------------------------
ancho, largo = 700 , 800
pantalla= py.display.set_mode((ancho,largo))
bg=25,25,25
pantalla.fill(bg)
ncx,ncy = 5,5
dimCW= ancho / ncx
dimCH= largo / ncy









while True:
    ti.sleep(0.1)
    for y in range(0,ncx):
        for x in range(0,ncy):
            poly =    [((x)  * dimCW, y     * dimCH),
                        ((x+1)* dimCW, y     * dimCH),
                        ((x+1)* dimCW, (y+1) * dimCH),
                        ((x)  * dimCW, (y+1) * dimCH)]
            py.draw.polygon(pantalla,(128,128,128),poly,1)
    py.display.flip()
