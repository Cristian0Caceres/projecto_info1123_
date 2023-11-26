
#---------------------------------------------------------------------
# Inicializa PGs.-
#---------------------------------------------------------------------
def PyGame_Init():
    PG.init()
    PG.mouse.set_visible(False) 
    PG.display.set_caption(' Mapa 2D Robotica - By Alberto Caro')
    return PG.display.set_mode(nRES) 

#---------------------------------------------------------------------
# Inicializa Relojes = Clock
#---------------------------------------------------------------------
def Clock_Init():
    PG.time.set_timer(USEREVENT + 1,nTIME_1)
    PG.time.set_timer(USEREVENT + 2,nTIME_2)
    return

#---------------------------------------------------------------------
# Inicilaiza parametros de los Robots
#---------------------------------------------------------------------
def Init_Robots():
    for i in range(0,nMAX_ROBOTS):
     aBoes[i].nF = RA.randint(5,6)    # 1:Robot,2:Robot
     aBoes[i].nX = RA.randint(0,6300) # nMAX_X-nTILE_WX)  # Pos. X Robot Mapa
     aBoes[i].nY = RA.randint(0,450)  # nMAX_Y-nTILE_HY)  # Pos. Y Robot Mapa
     aBoes[i].nR = RA.randint(0,500)  # Rango de Desplazamiento.-
     aBoes[i].dX = 0 # Sin movimiento por eje X
     aBoes[i].dY = 0 # Sin movimiento por eje Y
     aBoes[i].nV = RA.randint(0,5) # Velocidad Aleatoria entre [1,2,3]
    return

#---------------------------------------------------------------------
# Pinta los Robots en el Super Extra Mega Mapa.-
# Se pintan los Robots en Surface -> sMapa (6400 x 480)
#---------------------------------------------------------------------
def Pinta_Robots():
    for i in range(0,nMAX_ROBOTS):
     if aBoes[i].nF == 5: #  Robot Movi
        sMem.blit(aSprt[5],(aBoes[i].nX,aBoes[i].nY))
     if aBoes[i].nF == 6: #  Robot Delay
        sMem.blit(aSprt[6],(aBoes[i].nX,aBoes[i].nY))
    return

#---------------------------------------------------------------------
# Actualiza la estructura de datos de cada uno de los robots dentro del
# Mapa sMapa.
#---------------------------------------------------------------------
def Mueve_Robots():
    for i in range(0,nMAX_ROBOTS): # Recorrimos todos los Robots
     aBoes[i].nR -= 1    # Decrementamos en 1 el Rango del Robot
     if aBoes[i].nR < 0: # Si es negativo ->
        aBoes[i].nR = RA.randint(0,500) # Asignamos otro Rango aleatorio
        aBoes[i].nV = RA.randint(0,5)   # Asignamos otra velocidad 
        nDir = RA.randint(1,9)  # Generamos una Direccion de Movimiento Aleat.
        if nDir == 1: # Norte 
           aBoes[i].dX = +0 ; aBoes[i].dY = -1
        if nDir == 2: # Sur 
           aBoes[i].dX = +0 ; aBoes[i].dY = +1
        if nDir == 3: # Este 
           aBoes[i].dX = +1 ; aBoes[i].dY = +0
        if nDir == 4: # Oeste 
           aBoes[i].dX = -1 ; aBoes[i].dY = +0
        if nDir == 5: # Detenido 
           aBoes[i].dX = +0 ; aBoes[i].dY = +0
        if nDir == 6: # NE
           aBoes[i].dX = +1 ; aBoes[i].dY = -1
        if nDir == 7: # SE
           aBoes[i].dX = +1 ; aBoes[i].dY = +1
        if nDir == 8: # NO
           aBoes[i].dX = -1 ; aBoes[i].dY = -1
        if nDir == 9: # SO
           aBoes[i].dX = -1 ; aBoes[i].dY = +1

     #Actualizamos (Xs,Ys) de los Sprites en el Mapa 2D
     #--------------------------------------------------

     aBoes[i].nX += aBoes[i].dX*aBoes[i].nV # Posicion Robot[i] en eje X
     aBoes[i].nY += aBoes[i].dY*aBoes[i].nV # Posicion Robot[i] en eje Y

     if aBoes[i].nX < nMIN_X: # Check los bordes o limites
        aBoes[i].nX = nMIN_X ; aBoes[i].nR = 0 # Flag

     if aBoes[i].nX > (nMAX_X - nTW_X): # Check los bordes o limites
        aBoes[i].nX = nMAX_X - nTW_X ; aBoes[i].nR = 0 # Flag

     if aBoes[i].nY < nMIN_Y: # Check los bordes o limites
        aBoes[i].nY = nMIN_Y ; aBoes[i].nR = 0 # Flag

     if aBoes[i].nY > (nMAX_Y - nTH_Y): # Check los bordes o limites
        aBoes[i].nY = nMAX_Y - nTH_Y ; aBoes[i].nR = 0 # Flag

    return
    
#---------------------------------------------------------------------
# Inicializa las Baldozas = Tiles del Super Extra Mega Mapa.-
#---------------------------------------------------------------------
def Get_Tiles():      
    return [[ RA.randint(2,4) for i in range(0,nMW_X/nTW_X)] for i in range(0,nMH_Y/nTH_Y)]

#---------------------------------------------------------------------
# Inicializa Superficie del Super Extra Mega Mapa.-
#---------------------------------------------------------------------
def Get_Surface(nAncho_X,nAlto_Y):
    return PG.Surface((nAncho_X,nAlto_Y))

#---------------------------------------------------------------------
# Inicializa Array de Sprites.-
#---------------------------------------------------------------------
def Img_Init():
    aImg = []
    aImg.append(Load_Image('T00.png',True  )) # Sonda 1-2
    aImg.append(Load_Image('T01.png',True  )) # Sonda 2-2
    aImg.append(Load_Image('T02.png',False )) # Tierra
    aImg.append(Load_Image('T03.png',False )) # Roca     
    aImg.append(Load_Image('T04.png',False )) # Marmol
    aImg.append(Load_Image('T05.png',True  )) # robot movi
    aImg.append(Load_Image('T06.png',True  )) # robot delay
    aImg.append(Load_Image('T07.png',False )) # Logo
    aImg.append(Load_Image('T08.png',False )) # Bandera
    aImg.append(Load_Image('T09.png',False )) # Caja
    aImg.append(Load_Image('T10.png',True  )) # Mouse
    return aImg

#---------------------------------------------------------------------
# Make Mapa 
#---------------------------------------------------------------------
def Make_Mapa():
    nPx = nPy = 0
    for f in range(0,nMH_Y/nTH_Y):
     for c in range(0,nMW_X/nTW_X):
      if aTiles[f][c] == 2: 
         sMap.blit(aSprt[2],(nPx,nPy)); nPx += nTW_X
      if aTiles[f][c] == 3: 
         sMap.blit(aSprt[3],(nPx,nPy)); nPx += nTW_X
      if aTiles[f][c] == 4: 
         sMap.blit(aSprt[4],(nPx,nPy)); nPx += nTW_X
     nPx = 0; nPy += nTH_Y
    sMap.blit(aSprt[8],(0500,140)) 
    sMap.blit(aSprt[8],(2000,140)) 
    sMap.blit(aSprt[8],(3000,140)) 
    sMap.blit(aSprt[8],(4000,140)) 
    sMap.blit(aSprt[8],(5000,140)) 
    return

#---------------------------------------------------------------------
# Make Mapa 
#---------------------------------------------------------------------
def Set_Mapa(nTile):
    nPx = nPy = 0
    for f in range(0,nMH_Y/nTH_Y):
     for c in range(0,nMW_X/nTW_X):
      if nTile == 2: 
         sMap.blit(aSprt[2],(nPx,nPy)); nPx += nTW_X
      if nTile == 3: 
         sMap.blit(aSprt[3],(nPx,nPy)); nPx += nTW_X
      if nTile == 4: 
         sMap.blit(aSprt[4],(nPx,nPy)); nPx += nTW_X
     nPx = 0; nPy += nTH_Y
    sMap.blit(aSprt[8],(0500,140)) 
    sMap.blit(aSprt[8],(2000,140)) 
    sMap.blit(aSprt[8],(3000,140)) 
    sMap.blit(aSprt[8],(4000,140)) 
    sMap.blit(aSprt[8],(5000,140)) 
    return

#---------------------------------------------------------------------
# Handle Mapa
#---------------------------------------------------------------------
def Pinta_Sonda():
    global nSx, nDs,sAux
    nSx += nDs
    if (nSx >= 450):
        nDs = -1*nDs
        sAux = aSprt[1]
    if (nSx <= 310):
        nDs = -1*nDs  
        sAux = aSprt[0]      
    sWin.blit(sAux,(nSx,nSY)) 
    return

#---------------------------------------------------------------------
# Pinta Mouse
#---------------------------------------------------------------------
def Pinta_Mouse():
    sWin.blit(aSprt[10],(nMx,nMy))
    return 

#---------------------------------------------------------------------
# Handle Mapa
#---------------------------------------------------------------------
def Handle_Mapa():
    global nXp,nYp
    sMem.blit(sMap,(0,0))
    Mueve_Robots()
    Pinta_Robots()    
    sWin.blit(sMem.subsurface((nXp,nYp,800,480)),(0,0))
    sWin.blit(aSprt[9],(300,440)) 
    Pinta_Sonda()
    if lFlag:
       sWin.blit(aSprt[7],(220,10)) 
    nXp += 1
    if nXp == (5600 - 1): 
       nXp = 0
    return

#--------------------------------------------------------------
# Handle de Pause.-
##--------------------------------------------------------------
def Pausa():
    while 1:
     e = PG.event.wait()
     if e.type in (PG.QUIT, PG.KEYDOWN):
        return

#---------------------------------------------------------------------
# While Principal del Demo.-
#---------------------------------------------------------------------

# Surfaces....
sWin = PyGame_Init(); Clock_Init()

sMap = Get_Surface(nMW_X,nMH_Y); sMem = Get_Surface(nMW_X,nMH_Y)

# Array....
aBoes = [ eRobots() for i in range(0,nMAX_ROBOTS) ] ; Init_Robots()  
aSprt = Img_Init() ; aTiles = Get_Tiles(); Make_Mapa() 
sAux  = aSprt[0]
MyClock = PG.time.Clock()

while lOK:
 lFlag = False   
 cKey = PG.key.get_pressed()
 if cKey[PG.K_ESCAPE] : lOK = False
 if cKey[PG.K_p]      : Pausa() 
 if cKey[PG.K_s]      : PG.image.save(sWin,'foto.png') 
 if cKey[PG.K_a]      : lFlag = True
 if cKey[PG.K_F1]     : Set_Mapa(2)
 if cKey[PG.K_F2]     : Set_Mapa(3)
 if cKey[PG.K_F3]     : Set_Mapa(4)

 ev = PG.event.get()
 for e in ev:
  if e.type == QUIT           : lOK = False
  if e.type == PG.MOUSEMOTION : nMx,nMy = e.pos  
  if e.type == USEREVENT + 1  : Handle_Mapa()

 Pinta_Mouse()
 PG.display.flip()
 MyClock.tick(100)

PG.quit






