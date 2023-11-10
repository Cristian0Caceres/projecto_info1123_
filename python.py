import pygame as py 
import numpy  as np
import time   as ti 
import rxpy   as rp

class organismo:
    def __init__(self,vida,daño,energia,sed,movimiento,estado,genero,posicion):
        self.hp = vida
        self.dmg = daño
        self.enrg =energia
        self.water =sed
        self.move =movimiento
        self.estate=estado
        self.gender=genero
        self.post=posicion

    def inanicion_desidratacion(self):
        if self.enrg < 100:
            self.hp = self.hp - 1 
        if self.water < 100:
            self.hp = self.hp - 1 

    def death(self):
        if self.hp < 1:
            self.estate = "Muerto"

    def reproduction(self):
        pass #nose como continuar este codigo lo principal seria comprobar si 2 organismos de una mmisma
           #especies estan presentes cerca de si y son del genero opuesto se reproduscan creando otro
           #ser de la misma especie pero con los atrivutos reducidos por unos 3 ciclos aproximadamente
           #ademas de que por esos ciclos no se pueda reproducir y tanpoco sus padres
class carnivoro (organismo):
    def __init__(self, vida, daño, energia, sed, movimiento, estado, genero, posicion, contador_de_caza):
        super().__init__(vida, daño, energia, sed, movimiento, estado, genero, posicion)
        self.cdc=contador_de_caza
    def inanicion_desidratacion(self):
        return super().inanicion_desidratacion()
    def death(self):
        return super().death()
    def reproduction(self):
        return super().reproduction()
class hervivoro (organismo):
    def __init__(self, vida, daño, energia, sed, movimiento, estado, genero, posicion):
        super().__init__(vida, daño, energia, sed, movimiento, estado, genero, posicion)
    def inanicion_desidratacion(self):
        return super().inanicion_desidratacion()
    def death(self):
        return super().death()
    def reproduction(self):
        return super().reproduction()
class omnivoro (organismo):
    def __init__(self, vida, daño, energia, sed, movimiento, estado, genero, posicion, cotador_de_caza):
        super().__init__(vida, daño, energia, sed, movimiento, estado, genero, posicion)
        self.cdc=cotador_de_caza
    def inanicion_desidratacion(self):
        return super().inanicion_desidratacion()
    def death(self):
        return super().death()
    def reproduction(self):
        return super().reproduction()
class planta_01 (organismo):
    def __init__(self, vida, daño, sed, movimiento, estado, genero, posicion):
        super().__init__(vida, daño, sed, movimiento, estado, genero, posicion)
    def desidratacion(self):
        if super().water == 0:
            super().hp = super().hp - 1
    def death(self):
        return super().death()

class ambiente:
    def __init__(self,agua,fertilidad,temperatura,humedad,condiciones_meteorologicas,sotenibilidad):
        self.h2o   = agua
        self.fert  = fertilidad
        self.temp  = temperatura
        self.hume  = humedad
        self.cm    = condiciones_meteorologicas
        self.soste = sotenibilidad

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
