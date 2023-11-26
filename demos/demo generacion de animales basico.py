import pygame
import random
import matplotlib.pyplot as plt

# Definir la clase Organismo
class Organismo:
    def __init__(self, vida, daño, energia, sed, movimiento, estado, genero, posicionx, posiciony, dieta):
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

# Definir la clase Animal que hereda de Organismo
class Animal(Organismo, pygame.sprite.Sprite):
    def __init__(self, color, vida, daño, energia, sed, movimiento, estado, genero, posicionx, posiciony, dieta):
        Organismo.__init__(self, vida, daño, energia, sed, movimiento, estado, genero, posicionx, posiciony, dieta)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(700)
        self.rect.y = random.randrange(700)

    def combat(self, target):
        if self.estate == "Vivo" and target.estate == "Vivo":
            target.hp -= self.dmg
            if target.hp <= 0:
                target.death()

    def update(self):
        self.rect.x += random.choice([-20, 20])
        self.rect.y += random.choice([-20, 20])
        if self.rect.x < 0 or self.rect.x > 690:
            self.rect.x = random.randrange(700)
        if self.rect.y < 0 or self.rect.y > 690:
            self.rect.y = random.randrange(700)

# Inicializar Pygame
pygame.init()

# Crear pantalla
screen = pygame.display.set_mode([700, 700])

# Crear grupo de sprites
all_sprites = pygame.sprite.Group()

# Crear 10 animales de colores aleatorios
for i in range(10):
    color = (random.randrange(256), random.randrange(256), random.randrange(256))
    vida = 100
    daño = 10 if i < 5 else 0  # Los primeros 5 animales son agresivos
    energia = 100
    sed = 100
    movimiento = 1
    estado = "Vivo"
    genero = "Macho" if i % 2 == 0 else "Hembra"
    posicionx = random.randrange(700)
    posiciony = random.randrange(700)
    dieta = "Carnívoro" if i < 5 else "Herbívoro"
    animal = Animal(color, vida, daño, energia, sed, movimiento, estado, genero, posicionx, posiciony, dieta)
    all_sprites.add(animal)

# Crear un objeto Clock
clock = pygame.time.Clock()

# Bucle principal del juego
running = True
dead_animals = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Contar el número de animales muertos
    for animal in all_sprites:
        if animal.estate == "Muerto":
            dead_animals += 1

    # Generar un gráfico cuando el número de animales muertos llega a 5
    if dead_animals == 5:
        plt.figure(figsize=(5, 5))
        plt.bar(["Vivos", "Muertos"], [10 - dead_animals, dead_animals])
        plt.title("Número de animales vivos y muertos")
        plt.show()
        break

    screen.fill((2, 2, 2))
    all_sprites.draw(screen)

    pygame.display.flip()

    # Limitar la tasa de fotogramas a 5 FPS
    clock.tick(5)

pygame.quit()
