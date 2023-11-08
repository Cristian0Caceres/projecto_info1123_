import pygame as py 
import numpy as np

py.init()

#ancho y alto de nuestra pantalla que en este caso es de 1000 al cuadrado o 1000*1000
ancho,largo=1000,1000

#creacion de la pantalla usando los valores de ancho y largo 
screen = py.display.set_mode((ancho,largo))

#establecemos el color de fondo siendo este casi casi negro algo oscuro
bg=25,25,25

#pintamos el fondo 
screen.fill(bg)

#numero de celdas
nxc, nyc=25,25

#dimenciones de las celdas
dimCW = ancho / nxc
dimch = largo / nyc

#estado de las celdas vivo=1 muelto=0 diablo=???
gamestate= np.zeros((nxc,nyc))

#ciclo while el cual ejecuta el codigo 
while True:
    for y in range(0,nxc):
        for x in range(0,nyc):
            #calculamos la cantidad de vecinos a su alrededor
            n_neigh = gamestate[(x-1) % nxc ,(y-1) % nyc] + \
                      gamestate[(x)   % nxc ,(y-1) % nyc] + \
                      gamestate[(x+1) % nxc ,(y-1) % nyc] + \
                      gamestate[(x-1) % nxc ,(y)   % nyc] + \
                      gamestate[(x+1) % nxc ,(y)   % nyc] + \
                      gamestate[(x-1) % nxc ,(y+1) % nyc] + \
                      gamestate[(x)   % nxc ,(y+1) % nyc] + \
                      gamestate[(x+1) % nxc ,(y+1) % nyc]
            
            #regla 1 si es acompañada por 3 de su color vive
            if gamestate[x,y] == 0 and n_neigh == 3:
                gamestate[x,y] = 1
            #regla 2 si tas sola o te acompañamn muchos moriste pive
            if gamestate[x,y] == 1 and (n_neigh <2 or n_neigh > 3):
                gamestate[x,y] = 0
            #creacion del polygono que compondra cada una de nuestras celdas
            poly =    [((x)  * dimCW, y     * dimch),
                      ((x+1)* dimCW, y     * dimch),
                      ((x+1)* dimCW, (y+1) * dimch),
                      ((x)  * dimCW, (y+1) * dimch)]

            py.draw.polygon(screen,(128,128,128),poly,1)
    py.display.flip()