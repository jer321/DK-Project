__Author__='Juan Fernando Otoya'
Description='''
'''
import pygame as pig
from pygame.locals import *
import time
import random
from Colors import *
from Constantes import *
from Mapas import *
from Escaleras import *
from Player import *
from Barril import *


def mapRender(screen,mapa,player,barrelList,shotslist):
	'renderiza el mapa, el personaje, los barriles y los proyectiles en la pantalla'
	for plataforma in mapa:
		pig.draw.polygon(screen,DARK_RED,((plataforma[0],plataforma[1]),(plataforma[2],plataforma[3]),\
			(plataforma[2],plataforma[3]+10),(plataforma[0],plataforma[1]+10)))

	#Pasto
	screen.blit(grass,(0,0))
	#Escaleras
	for escalera in escaleras:
		imgEscalera=escaleraImg
		imgEscalera=pig.transform.scale(imgEscalera,(escalera[2]-escalera[0],escalera[3]-escalera[1]))
		screen.blit(imgEscalera,(escalera[0],escalera[1]))
	#Jugador
	screen.blit(player.img,(player.rect.left,player.rect.top))
	#Proyectiles
	for tiro in proyectiles:
		screen.blit(tiro.img,(tiro.rect.left,tiro.rect.top))
	#Barriles
	for barr in barrelList:#Update de todos los barriles
		screen.blit(barr.img,(barr.rect.left,barr.rect.top))

def update(screen,mapa,player,entreBarriles,barrelInitPos=(0,0)):
	''
	global barrelTiming
	#Agregar barriles a la lista
	if time.time()>barrelTiming+entreBarriles:#cada barrelTiming segundos se agrega un barril
		b=barril(barrelInitPos,random.uniform(3,15))
		barriles.append(b)
		barrelTiming=time.time()

	jugador2.update(mapa)#Adentro se pone el mapa para las colisiones

	for tiro in proyectiles:
		if tiro.rect.centerx>SCREEN_SIZE[0] or tiro.rect.centerx<0:
			proyectiles.remove(tiro)
		tiro.update()

	for barr in barriles:#Update de todos los barriles
		if 0>=barr.rect.left and 510<barr.rect.centery<440:#Meter en fncion para cambiar esto para los niveles
			barriles.remove(barr)
		for tiro in proyectiles:
			if barr.rect.right>tiro.rect.centerx>barr.rect.left and barr.rect.bottom>tiro.rect.centery>barr.rect.top:
				barriles.remove(barr)
				proyectiles.remove(tiro)

		barr.update(MapaDK1)
		if barr.rect.right>=SCREEN_SIZE[0] and barr.rect.bottom>=SCREEN_SIZE[1]:
			barr.alive=False


pig.init()

screensize=SCREEN_SIZE[0],SCREEN_SIZE[1]+10#Resolucionde Constantes
screen=pig.display.set_mode(screensize)

clock=pig.time.Clock()
pig.display.set_caption(CAPTION)#importar de Constantes

jugador2=Player2()

barriles=[]
barrelTiming=time.time()

#__main__
running=True
background=pig.image.load('background.png').convert_alpha()#utilizar Constantes
background=pig.transform.scale(background,(SCREEN_SIZE[0],screensize[1]))
grass=pig.image.load('Grass1_2.png').convert_alpha()#utilizar Constantes
grass=pig.transform.scale(grass,(SCREEN_SIZE[0],screensize[1]))

while running:
	for event in pig.event.get():
		if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
			running=False

	#Updates	
	update(screen,MapaDK1,jugador2,2,(64,100))
	
	#Fondo de Pantalla
	screen.blit(background,(0,0))
	#Mapa
	mapRender(screen,MapaDK1,jugador2,barriles,None)
	

	#El tiempo transcurrido del juego mostrado en pantalla
	tiempoTranscurrido=pig.time.get_ticks()/1000
	fuenteDeTexto=pig.font.Font('freesansbold.ttf', 32)
	textoPantalla=fuenteDeTexto.render(str(tiempoTranscurrido), True, GREEN, BLUE)#el True es para el Anti-Aliased (alisado)
	screen.blit(textoPantalla, (300,0))
	textoPantallaj=fuenteDeTexto.render('Juan Come Mocos', True, BLACK, STEEL_BLUE)#CAMBIAR!!!!!!
	#screen.blit(textoPantallaj, (0,0))
	pig.display.update()
	clock.tick(30)#Utilizar Constantes

pig.quit()


print(__Author__)