__Author__='Juan Fernando Otoya'
#Mapa.py
import pygame as pig
from Constantes import *

heightdif=int(SCREEN_SIZE[1]/7)
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
(0,heightdif*2,SCREEN_SIZE[0]-500,heightdif*2),\

MapaDK1=\
(0,SCREEN_SIZE[1],SCREEN_SIZE[0],SCREEN_SIZE[1]),\
(380,90,580,90),\
(275,120,380,120),\
(0,170,890,180),\
(70,265,SCREEN_SIZE[0],245),\
(0,330,890,350),\
(70,440,SCREEN_SIZE[0],420),\
(0,510,890,530),\
(0,610,SCREEN_SIZE[0],600),\

MapaDK2=\
(0,SCREEN_SIZE[1],SCREEN_SIZE[0],SCREEN_SIZE[1]),\
(380,90,570,90),\
(290,120,380,120),\
(0,160,700,160),\
(860,210,930,210),\
(770,230,820,230),\
(670,250,730,250),\
(540,280,640,280),\
(250,300,380,300),\
(30,300,130,300),\
(770,320,920,320),\
(580,370,640,370),\
(670,390,730,390),\
(770,420,830,420),\
(860,450,920,450),\
(830,485,920,485),\
(730,500,800,500),\
(640,500,700,500),\
(510,550,610,550),\
(290,480,390,480),\
(30,300,130,300),\
(30,440,130,440),\
(30,550,130,550),\


