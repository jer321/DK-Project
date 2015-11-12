#Mapa.py
import pygame as pig
from Constantes import *

heightdif=int(SCREEN_SIZE[1]/8)
widthdif=int(SCREEN_SIZE[0]/8)

#X0,  y0,        x1,          y1
dimmapa=\
(0,SCREEN_SIZE[1],SCREEN_SIZE[0],SCREEN_SIZE[1]),\
(50,SCREEN_SIZE[1],150,SCREEN_SIZE[1]-120),\
(150,SCREEN_SIZE[1]-120,700,SCREEN_SIZE[1]-500),\
(0,heightdif*5,SCREEN_SIZE[0],heightdif*5-30),\
(0,heightdif,SCREEN_SIZE[0],heightdif-30),\
(0,heightdif*3,SCREEN_SIZE[0],heightdif*3-30),\
(0,heightdif*5,SCREEN_SIZE[0],heightdif*5-30),\
(0,heightdif*6+40,SCREEN_SIZE[0],heightdif*6-30+40)


mapa2=\
(0,SCREEN_SIZE[1],SCREEN_SIZE[0],SCREEN_SIZE[1]),\
(0,heightdif,100,heightdif),\
(0,heightdif*7-5,widthdif,heightdif*7+15),\
(widthdif*2,heightdif*6,widthdif*5,heightdif*6),\
(0,heightdif*5,350,heightdif*5),\
(widthdif*3,heightdif*3,widthdif*7,heightdif*4),\
(0,heightdif*4,widthdif*3,heightdif*4),\
(0,heightdif*2,SCREEN_SIZE[0],heightdif*2),\

#pendientes=[]
#for i in dimmapa:
#	'Saca las pendientes de todos los obstaculos del mapa'
#	try:
#		m=(i[3]-i[1])/(i[2]-i[0])#La pendiente. en dimmapa se dan todos los puntos del mapa
#	except ZeroDivisionError:
#		m=0
#	pendientes.append(m)
#print(pendientes)