import pygame

# Tamaño de la pantalla
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Tamaño de las casillas
TILE_SIZE = 24

# Matriz del mapa
map_matrix = []  # Tu matriz aquí

class Objeto(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill((255, 0, 0))  # Cuadrado rojo
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

    def update(self):
        # Obtenemos la posición en la matriz
        matrix_x = int(self.rect.x // TILE_SIZE)-10
        matrix_y = int(self.rect.y // TILE_SIZE)-10

        # Comprobamos si la casilla es agua
        if map_matrix[matrix_y][matrix_x] == 'agua':
            self.kill()  # Eliminamos el objeto

# Inicializamos Pygame
pygame.init()

# Creamos la pantalla
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Creamos un objeto
objeto = Objeto(10, 10)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizamos el objeto
    objeto.update()

    # Dibujamos el mapa y el objeto
    screen.fill((0, 0, 0))
    for i in range(25-1):
        for j in range(32-1):
            if map_matrix[i][j] == 'agua':
                pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE))  # Casilla de agua azul
    screen.blit(objeto.image, objeto.rect)

    # Actualizamos la pantalla
    pygame.display.flip()

pygame.quit()
