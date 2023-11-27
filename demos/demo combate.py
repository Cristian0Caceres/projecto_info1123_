import pygame
import random

class Guerrero:
    def __init__(self, nombre, vida, x, y):
        self.nombre = nombre
        self.vida = vida
        self.x = x
        self.y = y

    def mover(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)
        self.x = max(0, min(700, self.x))  # Asegurar que el guerrero se mantiene dentro del mapa
        self.y = max(0, min(700, self.y))  # Asegurar que el guerrero se mantiene dentro del mapa

    def atacar(self, otro_guerrero):
        if abs(self.x - otro_guerrero.x) < 10 and abs(self.y - otro_guerrero.y) < 10:
            otro_guerrero.vida -= 10

# Inicializar Pygame
pygame.init()

# Crear una ventana de 700x700
ventana = pygame.display.set_mode((700, 700))

# Crear 10 guerreros en posiciones aleatorias
guerreros = [Guerrero(f'Guerrero {i}', 100, random.randint(0, 10), random.randint(0, 700)) for i in range(10)]

# Bucle principal del juego
corriendo = True
while corriendo:
    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Mover y atacar con los guerreros
    for guerrero in guerreros:
        guerrero.mover()
        for otro_guerrero in guerreros:
            if guerrero != otro_guerrero:
                guerrero.atacar(otro_guerrero)

    # Dibujar los guerreros
    ventana.fill((0, 0, 0))  # Llenar la ventana con blanco
    for guerrero in guerreros:
        if guerrero.vida > 0:  # Solo dibujar el guerrero si su vida es mayor que 0
            color = (255, 155 + guerrero.vida, 155 + guerrero.vida)  # El color se vuelve más rojo a medida que la vida disminuye
            pygame.draw.circle(ventana, color, (guerrero.x, guerrero.y), 10)  # Dibujar un círculo en la posición del guerrero

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
