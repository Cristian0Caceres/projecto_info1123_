import pygame
import random

class Guerrero:
    def __init__(self, nombre, vida, x, y, equipo):
        self.nombre = nombre
        self.vida = vida
        self.x = x
        self.y = y
        self.equipo = equipo  # Nuevo atributo para el equipo
        self.vivo = True

    def mover(self):
        self.x += random.randint(-10, 10)
        self.y += random.randint(-10, 10)
        self.x = max(0, min(700, self.x))  # Asegurar que el guerrero se mantiene dentro del mapa
        self.y = max(0, min(700, self.y))  # Asegurar que el guerrero se mantiene dentro del mapa

    def atacar(self, otro_guerrero):
        if abs(self.x - otro_guerrero.x) < 10 and abs(self.y - otro_guerrero.y) < 10:
            if self.equipo != otro_guerrero.equipo:  # Solo atacar si el otro guerrero no es del mismo equipo
                otro_guerrero.vida -= 10
                if otro_guerrero.vida <= 0:  # Si la vida del guerrero cae a 0 o menos
                    otro_guerrero.vivo = False  # Cambiar el estado de vivo a False

# Inicializar Pygame
pygame.init()

# Crear una ventana de 700x700
ventana = pygame.display.set_mode((700, 700))

# Crear 10 guerreros en posiciones aleatorias y asignarles un equipo
guerreros = [Guerrero(f'Guerrero {i}', 200, random.randint(0, 700), random.randint(0, 700), i // 20) for i in range(100)]

# Definir los colores para los equipos
colores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255), (128, 0, 0), (0, 128, 0), (0, 0, 128)]

# Crear un objeto Clock
reloj = pygame.time.Clock()

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

    # Eliminar los guerreros muertos
    guerreros = [guerrero for guerrero in guerreros if guerrero.vivo]

    # Dibujar los guerreros
    ventana.fill((2, 2, 2))  # Llenar la ventana con blanco
    for guerrero in guerreros:
        if guerrero.vivo:  # Solo dibujar el guerrero si su estado es vivo
            color = colores[guerrero.equipo]  # Usar el color del equipo del guerrero
            pygame.draw.circle(ventana, color, (guerrero.x, guerrero.y), 10)  # Dibujar un círculo en la posición del guerrero

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar la tasa de fotogramas a 6 FPS
    reloj.tick(600)

# Salir de Pygame
pygame.quit()
