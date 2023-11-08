import pygame as py 
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
        if self.hp < 0:
            self.estate = "Muerto"

    def reproduction(self):
        if #nose como continuar este codigo lo principal seria comprobar si 2 organismos de una mmisma
           #especies estan presentes cerca de si y son del genero opuesto se reproduscan creando otro
           #ser de la misma especie pero con los atrivutos reducidos por unos 3 ciclos aproximadamente
           #ademas de que por esos ciclos no se pueda reproducir y tanpoco sus padres