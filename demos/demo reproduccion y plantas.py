import pygame
import random

ANCHO, ALTO = 700, 700
NEGRO = (0, 0, 0)
FPS = 60
MAX_HIJOS = 4
TIEMPO_REPRODUCCION = FPS * 3
MAX_ANIMALES = 15
pygame.init()
class Organismo:
    def __init__(self, vida, daño, energia, sed, movimiento, estado, genero, posicionx, posiciony, dieta, color):
        self.hp = vida
        self.dmg = daño
        self.enrg = energia
        self.water = sed
        self.move = movimiento
        self.estate = estado
        self.gender = genero
        self.postx = posicionx
        self.posty = posiciony
        self.diet = dieta
        self.repcont = 0
        self.color = color

    def inanicion_desidratacion(self):
        if self.enrg < 100:
            self.hp = self.hp - 1
        if self.water < 100:
            self.hp = self.hp - 1

    def death(self):
        if self.hp < 1:
            self.estate = "Muerto"

    def reproduction(self):
        pass

    def max_move(self):
        if self.postx > 25:
            self.postx = 25
        if self.posty > 25:
            self.posty = 25

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

        # If the animal is blue (a herbivore), check for collision with plants
        if self.color == (0, 0, 255):
            hit_list = pygame.sprite.spritecollide(self, todos, False)
            for hit in hit_list:
                if isinstance(hit, Planta):
                    # Eat the plant and remove it from the game
                    self.tiempo_reproduccion -= 10  # Eating a plant decreases the reproduction time
                    todos.remove(hit)

    def reproducir(self, otro, todos):
        if (self.color == otro.color and otro not in self.hijos and self not in otro.hijos and
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

class Planta(Organismo):
    def __init__(self, vida, daño, energia, sed, movimiento, estado, genero, posicionx, posiciony, dieta, color):
        super().__init__(vida, daño, energia, sed, movimiento, estado, genero, posicionx, posiciony, dieta, color)
        self.cycles = 0

    def desidratacion(self):
        if self.water < 50 or self.cycles % 12 == 0:
            self.hp = self.hp - 10

    def death(self):
        if self.hp < 1 or self.cycles >= 60 or random.random() < 0.01: 
            self.estate = "Muerto"
        return super().death()

    def reproduction(self):
        if self.repcont >= 6:
            self.repcont = 0
            self.enrg = int(self.water) -1
            self.death()
            return [(self.postx + random.randint(-10, 10), self.posty + random.randint(-10, 10)) for _ in range(random.randint(0, 2))]
        else:
            self.repcont += 1
            return []
    def dibujar(self, ventana):
        pygame.draw.polygon(ventana, self.color, [(self.postx, self.posty), (self.postx + 5, self.posty + 5), (self.postx, self.posty + 5)])


pantalla = pygame.display.set_mode([ANCHO, ALTO])
todos = pygame.sprite.Group()

# Create four animals of different species
colores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
for color in colores:
    animal = Animal(color, random.randint(ANCHO // 2 - 50, ANCHO // 2 + 50), random.randint(ALTO // 2 - 50, ALTO // 2 + 50))
    todos.add(animal)
    animal = Animal(color, random.randint(ANCHO // 2 - 50, ANCHO // 2 + 50), random.randint(ALTO // 2 - 50, ALTO // 2 + 50))
    todos.add(animal)

ejecutando = True
reloj = pygame.time.Clock()

# Initialize cycle counter
# Initialize color counters
contadores_color = {color: 1 for color in colores}
def main():
    pygame.init()
    ventana = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Simulación de Organismos")

    colores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
    plantas = [Planta(10, 0, 50, 50, 0, "vivo", "planti", random.randint(0, 700), random.randint(0, 700), "fotosintetico", color) for color in colores for _ in range(3)]
    contador_colores = {color: 3 for color in colores}

    clock = pygame.time.Clock()

    corriendo = True
    while corriendo:
        clock.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
        for animal in todos:
            animal.mover()
            animal.actualizar()
            for otro in todos:
                if animal != otro and pygame.sprite.collide_rect(animal, otro):
                    hijo = animal.reproducir(otro, todos)
                    if hijo is not None:
                        todos.add(hijo)
                        contadores_color[hijo.color] += 1

        

        ventana.fill((0, 0, 0))
        nuevas_plantas = []
        for planta in plantas:
            planta.cycles += 1
            planta.dibujar(ventana)
            nuevas_posiciones = planta.reproduction()
            for pos in nuevas_posiciones:
                if contador_colores[planta.color] < 600:
                    nuevas_plantas.append(Planta(100, 0, 50, 50, 0, "vivo", "planti", pos[0], pos[1], "fotosintetico", planta.color))
                    contador_colores[planta.color] += 1
            planta.desidratacion()
            planta.death()
            if planta.estate == "Muerto":
                plantas.remove(planta)
                contador_colores[planta.color] -= 1
        plantas.extend(nuevas_plantas)
        todos.draw(pantalla)
        pygame.display.flip() 
    pygame.quit()
if __name__ == "__main__":
    main()