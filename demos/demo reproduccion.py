import pygame
import random

ANCHO, ALTO = 700, 700
NEGRO = (0, 0, 0)
FPS = 60
MAX_HIJOS = 4
TIEMPO_REPRODUCCION = FPS * 3
MAX_ANIMALES = 15

class Animal(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        self.hijos = []
        self.tiempo_reproduccion = 0

    def mover(self):
        self.rect.x += random.randint(-1, 1)
        self.rect.y += random.randint(-1, 1)

    def reproducir(self, otro, todos):
        if (self.color != otro.color and otro not in self.hijos and self not in otro.hijos and
            self.tiempo_reproduccion >= TIEMPO_REPRODUCCION and len(self.hijos) < MAX_HIJOS and
            len([x for x in todos if x.color == self.color]) < MAX_ANIMALES):
            hijo = Animal(self.color, self.rect.x, self.rect.y)
            self.hijos.append(hijo)
            otro.hijos.append(hijo)
            self.tiempo_reproduccion = 0
            return hijo
        return None

    def actualizar(self):
        self.tiempo_reproduccion += 1

pygame.init()
pantalla = pygame.display.set_mode([ANCHO, ALTO])
todos = pygame.sprite.Group()
animal1 = Animal((255, 0, 0), random.randint(ANCHO // 2 - 50, ANCHO // 2 + 50), random.randint(ALTO // 2 - 50, ALTO // 2 + 50))
animal2 = Animal((0, 255, 0), random.randint(ANCHO // 2 - 50, ANCHO // 2 + 50), random.randint(ALTO // 2 - 50, ALTO // 2 + 50))
todos.add(animal1)
todos.add(animal2)

ejecutando = True
reloj = pygame.time.Clock()
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill(NEGRO)
    for animal in todos:
        animal.mover()
        animal.actualizar()
        for otro in todos:
            if animal != otro and pygame.sprite.collide_rect(animal, otro):
                hijo = animal.reproducir(otro, todos)
                if hijo is not None:
                    todos.add(hijo)
    todos.draw(pantalla)
    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()
