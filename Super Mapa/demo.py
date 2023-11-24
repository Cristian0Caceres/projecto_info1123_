# By Alberto Caro S.
# Ing. Civil en Computacion
# Doctor(c) Cs. de la Computacion
# Pontificia Universidad Catolica de Chile
#-------------------------------------------
import pygame,time, random as RA, ctypes as ct
from pygame.locals import *

#---------------------------------------------------------------------
# Definicion de Constantes.-
#---------------------------------------------------------------------
nRES = (1200,700) ; nMAX_ROBOTS  =10 ;nMAX_NAVES = 2
nMIN_X = 0 ; nMAX_X = 2640 ; nMIN_Y = 0 ; nMAX_Y = 1760
nTRUE  = 1 ; nTIME1 = 400 ; nTIME2 = 400 ; lOK = True
nTILE_WX = 44 ; nTILE_HY = 44 ; nX0 = 232 ; nY0 = 14 ; nBTN_LEFT = 1
xd = 0 ; yd = 0

#---------------------------------------------------------------------
# Definicion de Estructura de Datos.-
#---------------------------------------------------------------------
class eRobot(ct.Structure):
 _fields_ = [
             ('nF',ct.c_short),('nX',ct.c_short),('nY',ct.c_short),
	         ('nR',ct.c_short),('dX',ct.c_short),('dY',ct.c_short),
	         ('nV',ct.c_short)
            ]

class eNaves(ct.Structure):
 _fields_ = [
             ('nF',ct.c_short),('nX',ct.c_short),('nY',ct.c_short),
	         ('nR',ct.c_short),('dX',ct.c_short),('dY',ct.c_short),
	         ('nV',ct.c_short)
            ]

#---------------------------------------------------------------------
# Carga imagenes y convierte formato PyGame
#---------------------------------------------------------------------
def Load_Image(sFile,transp = False):
    try: image = pygame.image.load(sFile)
    except pygame.error,message:
           raise SystemExit,message
    image = image.convert()
    if transp:
       color = image.get_at((0,0))
       image.set_colorkey(color,RLEACCEL)
    return image

#---------------------------------------------------------------------
# Inicializa PyGames.-
#---------------------------------------------------------------------
def PyGame_Init():
    pygame.init()
    pygame.time.set_timer(USEREVENT+1,nTIME1)
    pygame.time.set_timer(USEREVENT+2,nTIME2)
    pygame.mouse.set_visible(False)
    pygame.display.set_caption('Demo Robot en Mapa2D - By Alberto Caro - 2015()')
    return pygame.display.set_mode(nRES)

#---------------------------------------------------------------------
# Inicializa las Baldozas = Tiles del Super Extra Mega Mapa.-
#---------------------------------------------------------------------
def Tiles_Init():
    return [[RA.randint(0,9) for i in range(0,nMAX_X/nTILE_WX)] \
                             for i in range(0,nMAX_Y/nTILE_HY)]

#---------------------------------------------------------------------
# Inicializa Superficie del Super Extra Mega Mapa.-
#---------------------------------------------------------------------
def Mapa_Init(nAncho_X,nAlto_Y):
    return pygame.Surface((nAncho_X,nAlto_Y))

#---------------------------------------------------------------------
# Inicializa Array de Sprites.-
#---------------------------------------------------------------------
def Fig_Init():
    aImg = []
    aImg.append(Load_Image('f0.png',False )) # Baldosa 0               0
    aImg.append(Load_Image('f1.png',False )) # Baldosa 1               1
    aImg.append(Load_Image('f2.png',False )) # Baldosa 2               2
    aImg.append(Load_Image('f3.png',False )) # Baldosa 3               3
    aImg.append(Load_Image('f4.png',False )) # Baldosa 4               4
    aImg.append(Load_Image('f5.png',True  )) # Baldosa 5               5
    aImg.append(Load_Image('f6.png',True  )) # Baldosa 6               6
    aImg.append(Load_Image('f7.png',True  )) # Baldosa 7               7
    aImg.append(Load_Image('f8.png',True  )) # Baldosa 8               8
    aImg.append(Load_Image('f9.png',True  )) # Baldosa 9               9
    aImg.append(Load_Image('fa.png',True  )) # Nave 1                 10
    aImg.append(Load_Image('fb.png',True  )) # Nave 2                 11
    aImg.append(Load_Image('fc.png',True  )) # Robot 1 Led R-V        12
    aImg.append(Load_Image('fd.png',True  )) # Robot 2 Led V-R        13
    aImg.append(Load_Image('fe.png',True  )) # Robot 3 Timer          14
    aImg.append(Load_Image('ff.png',True  )) # Cursor Mouse 1 Normal  15
    aImg.append(Load_Image('pm.png',True  )) # Cursor Mouse 2 Mini    16
    aImg.append(Load_Image('bg.png',True  )) # Panel Main             17
    aImg.append(Load_Image('mm.png',False )) # Mini Mapa              18
    return aImg

#---------------------------------------------------------------------
# Inicilaiza parametros de los Robots
#---------------------------------------------------------------------
def Robots_Init():
    for i in range(0,nMAX_ROBOTS):
     aBoes[i].nF = RA.randint(1,3)    # Primary Key Nave.-
     aBoes[i].nX = RA.randint(0,2639) # nMAX_X-nTILE_WX)  # Pos. X Robot Mapa
     aBoes[i].nY = RA.randint(0,1759) # nMAX_Y-nTILE_HY)  # Pos. Y Robot Mapa
     aBoes[i].nR = RA.randint(0,500)  # Rango de Desplazamiento.-
     aBoes[i].dX = 0
     aBoes[i].dY = 0
     aBoes[i].nV = RA.randint(1,3)
    return

#---------------------------------------------------------------------
# Incializa parametros de las Naves.-
#---------------------------------------------------------------------
def Naves_Init():
    for i in range(0,nMAX_NAVES):
     aNave[i].nF = i   # Primary Key Nave.-
     aNave[i].nX = RA.randint(100,200) # Pos. X Robot Mapa
     aNave[i].nY = 600 # Pos. Y Robot Mapa
     aNave[i].nR = RA.randint(0,100)# Rango de Desplazamiento.-
     aNave[i].dX = 0
     aNave[i].dY = -1
     aNave[i].nV = RA.randint(1,2)
    return

#---------------------------------------------------------------------
# Pinta los Robots en el Super Extra Mega Mapa.-
#---------------------------------------------------------------------
def Pinta_Robots():
    for i in range(0,nMAX_ROBOTS):
     if aBoes[i].nF == 1: sMapa.blit(aSprt[12],(aBoes[i].nX,aBoes[i].nY))
     if aBoes[i].nF == 2: sMapa.blit(aSprt[13],(aBoes[i].nX,aBoes[i].nY))
     if aBoes[i].nF == 3: sMapa.blit(aSprt[14],(aBoes[i].nX,aBoes[i].nY))
    return

#---------------------------------------------------------------------
# Pinta las Naves en el Panel Izquierdo
#---------------------------------------------------------------------
def Pinta_Naves():
    Panta.blit(aSprt[10],(aNave[0].nX,aNave[0].nY))
    Panta.blit(aSprt[11],(aNave[1].nX,aNave[1].nY))
    return

#---------------------------------------------------------------------
# Pinta la Pantalla Principal de PyGames.-
#---------------------------------------------------------------------
def Pinta_Panel():
    Panta.blit(aSprt[17],(0,0))
    return

#---------------------------------------------------------------------
# Pinta el Super Extra Mega Mapa a Panta de PyGames.-
#---------------------------------------------------------------------
def Pinta_Mapa():
    Panta.blit(sMapa.subsurface((xd,yd,952,670)),(nX0,nY0))
    return

#---------------------------------------------------------------------
# Pinta el Mini Mapa del Super Extra Mega Mapa a Panta de PyGames.-
#---------------------------------------------------------------------
def Pinta_MMapa():
    xp = 0; yp = 0
    Panta.blit(aSprt[18],(1013,20))
    for i in range(0,nMAX_ROBOTS):
     xp = int(159/float(2640)*aBoes[i].nX) + 1017
     xy = int(112/float(1760)*aBoes[i].nY) + 0027
     Panta.blit(aSprt[16],(xp,xy))
    return

#---------------------------------------------------------------------
# Pinta la Posicion de la Mouse en Panta de PyGame.-
#---------------------------------------------------------------------
def Pinta_Mouse():
    Panta.blit(aSprt[15],(nMx,nMy))
    return

#---------------------------------------------------------------------
# Acualiza Coordenadas Scroll Super Extra Mega Mapa.-
#---------------------------------------------------------------------
def UpDate_Scroll_Mapa(nMx,nMy):
    xd = 0 ; yd = 0
    if nMx in range(1018,1177):
       if nMy in range(25,137):
          xd = int(2640*(nMx-1018)/float(159))
          yd = int(1760*(nMy-25)/float(112))
          pygame.display.set_caption('[Coord Mapa]-> X: %d - Y: %d' %(xd,yd))
          if xd >= 1687: xd = 1687
          if yd >= 1090: yd = 1090
    return xd,yd

#---------------------------------------------------------------------
# Acualiza el Super Extra Mega Mapa.-
#---------------------------------------------------------------------
def UpDate_Mapa():
    nPx = nPy = 0
    for f in range(0,nMAX_Y/nTILE_HY):
     for c in range(0,nMAX_X/nTILE_WX):
      if aTile[f][c] == 0:
         sMapa.blit(aSprt[0],(nPx,nPy)); nPx += nTILE_WX
      if aTile[f][c] == 1:
         sMapa.blit(aSprt[1],(nPx,nPy)); nPx += nTILE_WX
      if aTile[f][c] == 2:
         sMapa.blit(aSprt[1],(nPx,nPy)); nPx += nTILE_WX
      if aTile[f][c] == 3:
         sMapa.blit(aSprt[3],(nPx,nPy)); nPx += nTILE_WX
      if aTile[f][c] == 4:
         sMapa.blit(aSprt[4],(nPx,nPy)); nPx += nTILE_WX
      if aTile[f][c] == 5:
         sMapa.blit(aSprt[1],(nPx,nPy)); nPx += nTILE_WX
      if aTile[f][c] == 6:
         sMapa.blit(aSprt[1],(nPx,nPy)); nPx += nTILE_WX
      if aTile[f][c] == 7:
         sMapa.blit(aSprt[1],(nPx,nPy)); nPx += nTILE_WX
      if aTile[f][c] == 8:
         sMapa.blit(aSprt[1],(nPx,nPy)); nPx += nTILE_WX
      if aTile[f][c] == 9:
         sMapa.blit(aSprt[4],(nPx,nPy)); nPx += nTILE_WX
     nPx = 0; nPy += nTILE_HY
    return

#---------------------------------------------------------------------
# Actualiza los Robots en el Super Extra Mega Mapa.-
#---------------------------------------------------------------------
def UpDate_Robots():
    for i in range(0,nMAX_ROBOTS):
     aBoes[i].nR -= 1
     if aBoes[i].nR < 0:
        aBoes[i].nR = RA.randint(0,500)
        aBoes[i].nV = RA.randint(1,3)
        nDir = RA.randint(1,9)
        if nDir == 1: # Norte ?
           aBoes[i].dX = +0 ; aBoes[i].dY = -1
        if nDir == 2: # Este ?
           aBoes[i].dX = +1 ; aBoes[i].dY = 0
        if nDir == 3: # Sur ?
           aBoes[i].dX = +0 ; aBoes[i].dY = +1
        if nDir == 4: # Oeste ?
           aBoes[i].dX = -1 ; aBoes[i].dY = +0
        if nDir == 5: # Detenido ?
	 aBoes[i].dX = +0 ; aBoes[i].dY = +0
        if nDir == 6: #
	 aBoes[i].dX = +1 ; aBoes[i].dY = -1
        if nDir == 7: #
	 aBoes[i].dX = -1 ; aBoes[i].dY = -1
        if nDir == 8: #
	 aBoes[i].dX = +1 ; aBoes[i].dY = +1
        if nDir == 9: #
	 aBoes[i].dX = -1 ; aBoes[i].dY = +1

     #Actualizamos (Xs,Ys) de los Sprites en el Mapa 2D
     #--------------------------------------------------

     aBoes[i].nX += aBoes[i].dX*aBoes[i].nV
     aBoes[i].nY += aBoes[i].dY*aBoes[i].nV

     if aBoes[i].nX < nMIN_X:
        aBoes[i].nX = nMIN_X ; aBoes[i].nR = 0

     if aBoes[i].nX > (nMAX_X - nTILE_WX):
        aBoes[i].nX = nMAX_X - nTILE_WX ; aBoes[i].nR = 0

     if aBoes[i].nY < nMIN_Y:
        aBoes[i].nY = nMIN_Y ; aBoes[i].nR = 0

     if aBoes[i].nY > (nMAX_Y - nTILE_HY):
        aBoes[i].nY = nMAX_Y - nTILE_HY ; aBoes[i].nR = 0

    return

#---------------------------------------------------------------------
# Actualiza las Naves en el Panel Izquierdo.-
#---------------------------------------------------------------------
def UpDate_Naves():
    for i in range(0,nMAX_NAVES):
     aNave[i].nR -= 1
     if aNave[i].nR < 0:
        aNave[i].nR = RA.randint(0,100)
        aNave[i].nV = RA.randint(1,2)
        nDir = RA.randint(1,5)
        if nDir == 1: # Norte ?
           aNave[i].dX = +0 ; aNave[i].dY = -1
        if nDir == 2: # Este ?
           aNave[i].dX = +1 ; aNave[i].dY = 0
        if nDir == 3: # Sur ?
           aNave[i].dX = +0 ; aNave[i].dY = +1
        if nDir == 4: # Oeste ?
           aNave[i].dX = -1 ; aNave[i].dY = +0
        if nDir == 5: # Detenido ?
	 aNave[i].dX = +0 ; aNave[i].dY = +0

     #Actualizamos (Xs,Ys) de los Sprites en el Mapa 2D
     #--------------------------------------------------

     aNave[i].nX += aNave[i].dX*aNave[i].nV
     aNave[i].nY += aNave[i].dY*aNave[i].nV

     if aNave[i].nX < 017 : aNave[i].nX = 017 ; aNave[i].nR = 0
     if aNave[i].nX > 156 : aNave[i].nX = 156 ; aNave[i].nR = 0
     if aNave[i].nY < 052 : aNave[i].nY = 052 ; aNave[i].nR = 0
     if aNave[i].nY > 600 : aNave[i].nY = 600 ; aNave[i].nR = 0

    return

#--------------------------------------------------------------
# Handle de Pause.-
#--------------------------------------------------------------
def Pausa():
    while 1:
     e = pygame.event.wait()
     if e.type in (pygame.QUIT, pygame.KEYDOWN):
        return

#---------------------------------------------------------------------
# While Principal del Demo.-
#---------------------------------------------------------------------
Panta = PyGame_Init()
aSprt = Fig_Init()
aTile = Tiles_Init();
sMapa = Mapa_Init(2640,1760)
aBoes = [ eRobot() for i in range(0,nMAX_ROBOTS) ]
aNave = [ eNaves() for i in range(0,nMAX_NAVES) ]
Clok  = pygame.time.Clock(); nMx = 0; nMy = 0

Robots_Init()
Naves_Init()

while lOK:
 cKey = pygame.key.get_pressed()
 if cKey[pygame.K_ESCAPE] : lOK = False
 if cKey[pygame.K_p]      : Pausa()
 if cKey[pygame.K_s]      : pygame.image.save(Panta,'Capture.png')
 ev = pygame.event.get()
 for e in ev:
  if e.type == QUIT               : lOK = False
  if e.type == pygame.MOUSEMOTION : nMx,nMy = e.pos
  if e.type == pygame.MOUSEBUTTONDOWN and e.button == nBTN_LEFT:
               xd,yd = UpDate_Scroll_Mapa(nMx,nMy)
 Pinta_Panel()
 UpDate_Mapa()
 UpDate_Robots()
 Pinta_Robots()
 Pinta_Mapa()
 UpDate_Naves()
 Pinta_Naves()
 Pinta_MMapa()
 Pinta_Mouse()
 pygame.display.flip()

pygame.quit



