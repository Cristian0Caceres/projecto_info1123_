import pygame
import random

# Dimensiones de la ventana
ANCHO = 700
ALTO = 700

# Tamaño de las casillas
TAM_CASILLA = ANCHO // 5

# Tipos de ambiente
TIPOS_AMBIENTE = ["arido", "humedo", "templado", "frio", "caluroso"]

class Ambiente:
    def __init__(self, agua, fertilidad, temperatura, humedad, condiciones_meteorologicas, sostenibilidad, tipo):
        self.h2o = agua
        self.fert = fertilidad
        self.temp = temperatura
        self.hume = humedad
        self.cm = condiciones_meteorologicas
        self.soste = sostenibilidad
        self.type = tipo

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))

    # Generar el mapa
    mapa = []
    for i in range(5):
        fila = []
        for j in range(5):
            agua = random.randint(0, 100)
            fertilidad = random.randint(0, 100)
            temperatura = random.randint(-30, 50)
            humedad = random.randint(0, 100)
            condiciones_meteorologicas = random.choice(["soleado", "nublado", "lluvioso", "nevado"])
            sostenibilidad = random.randint(0, 100)
            tipo = random.choice(TIPOS_AMBIENTE)
            fila.append(Ambiente(agua, fertilidad, temperatura, humedad, condiciones_meteorologicas, sostenibilidad, tipo))
        mapa.append(fila)

    # Dibujar el mapa
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            color = (0, mapa[i][j].fert, mapa[i][j].agua)  # Use fertility and water as color components
            pygame.draw.rect(pantalla, color, pygame.Rect(i*TAM_CASILLA, j*TAM_CASILLA, TAM_CASILLA, TAM_CASILLA))

    # Bucle principal
    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
