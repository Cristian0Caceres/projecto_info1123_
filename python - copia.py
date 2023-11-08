import pygame as py 
import numpy as np

py.init()

ancho,largo=1000,1000
screen = py.display.set_mode((ancho,largo))

bg=25,25,25
screen.fill(bg)

nxc, nyc=25,25

dimCW = ancho / nxc
dimch = largo / nyc

while True:
    for y in range(0,nxc):
        for x in range(0,nyc):

            poly = [((x)  * dimCW, y     * dimch),
                    ((x+1)* dimCW, y     * dimch),
                    ((x+1)* dimCW, (y+1) * dimch),
                    ((x)  * dimCW, (y+1) * dimch)]

            py.draw.polygon(screen,(128,128,128),poly,1)
    py.display.flip()