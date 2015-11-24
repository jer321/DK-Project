__Author__='Juan Fernando Otoya'
Description='''
en un futuro me gustaria agregar sonidos y mas niveles, ademas de cambiar la imagen de la princesa y el donkeykong y agregar animaciones.
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
from Powerup import *
from Princess import *
from Barril import *
import os
#Utilizo "os" para poder correrlo en otro sistema operativo. no se en cual lo vas a correr antal :D


def mapRender(screen,mapa,stairs,player,powerup,princess,barrelList,dkpos,mapimg):
	'renderiza el mapa, el personaje, los barriles y los proyectiles en la pantalla'
	for plataforma in mapa:
		pig.draw.polygon(screen,DARK_RED,((plataforma[0],plataforma[1]),(plataforma[2],plataforma[3]),\
			(plataforma[2],plataforma[3]+10),(plataforma[0],plataforma[1]+10)))

	#Pasto
	mapimg=pig.image.load(mapimg)
	screen.blit(mapimg,(0,0))
	#Escaleras
	for stair in stairs:
		imgEscalera=escaleraImg
		imgEscalera=pig.transform.scale(imgEscalera,(stair[2]-stair[0],stair[3]-stair[1]))
		screen.blit(imgEscalera,(stair[0],stair[1]))
	#Jugador
	screen.blit(player.img,(player.rect.left,player.rect.top))
	#Princesa
	screen.blit(princess.img,(princess.rect.left,princess.rect.top))
	#Mejora
	if powerup.show:
		screen.blit(powerup.img,(powerup.rect.left,powerup.rect.top))
	#DK imagen
	screen.blit(dkimg,dkpos)
	#Proyectiles
	for tiro in proyectiles:
		screen.blit(tiro.img,(tiro.rect.left,tiro.rect.top))
	#Barriles
	for barr in barrelList:#Update de todos los barriles
		screen.blit(barr.img,(barr.rect.left,barr.rect.top))

def update(screen,mapa,stairs,player,powerup,princess,entreBarriles,barrelInitPos=(0,0)):
	''
	global barrelTiming
	
	#Agregar barriles a la lista
	if time.time()>barrelTiming+entreBarriles:#cada barrelTiming segundos se agrega un barril
		b=barril(barrelInitPos,random.uniform(3,15))
		barriles.append(b)
		barrelTiming=time.time()


	player.update(mapa,stairs)#Adentro se pone el mapa para las colisiones
	powerup.update(player)
	princess.update(player)

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
				player.score+=300

		barr.update(mapa,stairs,player)

	if player.win:
		#Si toca a la princesa win=True
		playlevel=False
		player.score+=10000


def texto(player,name):
	'renderiza los textos en la pantalla'
	#El tiempo transcurrido del juego mostrado en pantalla
	fuenteDeTexto=pig.font.Font('freesansbold.ttf', 32)
	tiempoTranscurrido=120-int(pig.time.get_ticks()/1000)-gettime

	tiempo=fuenteDeTexto.render(str(tiempoTranscurrido), True, BLACK,)#el True es para el Anti-Aliased (alisado)
	txt1=fuenteDeTexto.render(str(name), True, BLACK,)
	txt2=fuenteDeTexto.render('Score:', True, BLACK,)
	txt3=fuenteDeTexto.render('Time:', True, BLACK,)
	score=fuenteDeTexto.render(str(player.score), True, BLACK,)#CAMBIAR!!!!!!

	screen.blit(txt1, (5,0))
	screen.blit(txt2, (5,32))
	screen.blit(txt2, (5,64))
	screen.blit(tiempo, (110,32))
	screen.blit(score, (110,64))


pig.init()

screensize=SCREEN_SIZE[0],SCREEN_SIZE[1]+10#Resolucionde Constantes
screen=pig.display.set_mode(screensize)

clock=pig.time.Clock()
pig.display.set_caption(CAPTION)#importar de Constantes

jugador2=Player2()
mejora=powerup()
princesa=princesa()

barriles=[]#Lista de los barriles en juego
barrelTiming=time.time()#tiempo para hacer cada cuanto se agregan barriles a la lista


running=True
background=pig.image.load(os.path.join('IMG','background.png')).convert_alpha()#utilizar Constantes
background=pig.transform.scale(background,(SCREEN_SIZE[0],screensize[1]))
grass=pig.image.load(os.path.join('IMG','Grass1_2.png')).convert_alpha()#utilizar Constantes
grass=pig.transform.scale(grass,(SCREEN_SIZE[0],screensize[1]))
dkimg=pig.image.load(os.path.join('IMG','donkeyKong2.png'))
dkimg=pig.transform.scale(dkimg,(128,128))


notname=True
txtname=''
while running:

	#Escoger nombre de personaje
	#dependiendo de la tecla que se unda se agrega la letra a "txtname"
	#para borrar txtname=txtname[:-1] lo que quiere decir que no toma el ultimo caracter. esto sucede cada vez que presionamos la tecla de borrar
	while notname:
		for event in pig.event.get():
			if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
				notname=False
				running=False
			if event.type==KEYDOWN:
				if event.key==K_q:
					txtname+='q'
				if event.key==K_w:
					txtname+='w'
				if event.key==K_e:
					txtname+='e'
				if event.key==K_r:
					txtname+='r'
				if event.key==K_t:
					txtname+='t'
				if event.key==K_y:
					txtname+='y'
				if event.key==K_u:
					txtname+='u'
				if event.key==K_i:
					txtname+='i'
				if event.key==K_o:
					txtname+='o'
				if event.key==K_p:
					txtname+='p'
				if event.key==K_a:
					txtname+='a'
				if event.key==K_s:
					txtname+='s'
				if event.key==K_d:
					txtname+='d'
				if event.key==K_f:
					txtname+='f'
				if event.key==K_g:
					txtname+='g'
				if event.key==K_h:
					txtname+='h'
				if event.key==K_j:
					txtname+='j'
				if event.key==K_k:
					txtname+='k'
				if event.key==K_l:
					txtname+='l'
				if event.key==K_z:
					txtname+='z'
				if event.key==K_x:
					txtname+='x'
				if event.key==K_c:
					txtname+='c'
				if event.key==K_v:
					txtname+='v'
				if event.key==K_b:
					txtname+='b'
				if event.key==K_n:
					txtname+='n'
				if event.key==K_m:
					txtname+='m'
				if event.key==K_SPACE:
					txtname+=' '

				if event.key==K_BACKSPACE:
					txtname=txtname[:-1]
				if event.key==K_RETURN:
					notname=False
				gettime=int(pig.time.get_ticks()/1000)*-1

		screen.fill(BLACK)
		fuenteDeTexto=pig.font.Font('freesansbold.ttf', 32)
		fuenteDeTexto2=pig.font.Font('freesansbold.ttf', 16)
		ask1=fuenteDeTexto.render('Ingresa tu Nombre:', True, WHITE,)
		ask2=fuenteDeTexto.render(txtname, True, WHITE,)
		txtcoso=fuenteDeTexto2.render('Para continuar presione "Enter" Luego de haber escrito el nombre del personaje', True, WHITE,)
		screen.blit(ask1, (100,150))
		screen.blit(ask2, (420,150))
		screen.blit(txtcoso, (100,128))

		pig.display.update()

	#Nivel 1
	jugador2.rect.left,jugador2.rect.centery=0,520
	mejora.rect.left,mejora.rect.centery=80,380
	princesa.rect.left,princesa.rect.bottom=270,120
	jugador2.win=True
	while not jugador2.win:
		for event in pig.event.get():
			if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
				running=False
				pig.quit()

		#Updates	
		update(screen,MapaDK1,escaleras1,jugador2,mejora,princesa,2,(120+80,50+100))
		
		#Fondo de Pantalla
		screen.blit(background,(0,0))
		#Mapa
		mapRender(screen,MapaDK1,escaleras1,jugador2,mejora,princesa,barriles,(120,50),os.path.join('IMG','Grass1_2.png'))
		#Textos
		texto(jugador2,txtname)

		#screen.blit(textoPantallaj, (0,0))
		pig.display.update()
		clock.tick(FPS)#Utilizar Constantes

		#GAME OVER
		while jugador2.dead:
			for event in pig.event.get():
				if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
					running=False
					pig.quit()


			screen.fill(BLACK)
			fuenteDeTexto=pig.font.Font('freesansbold.ttf', 128)
			fuenteDeTexto2=pig.font.Font('freesansbold.ttf', 32)
			ask1=fuenteDeTexto.render('GAME OVER', True, WHITE,)
			ask2=fuenteDeTexto2.render(txtname+' Has perdido', True, WHITE,)
			txtcoso=fuenteDeTexto2.render('Tu puntuacion es de:', True, WHITE,)
			txtcoso2=fuenteDeTexto2.render(str(jugador2.score), True, WHITE,)
			screen.blit(ask1, (120,140))
			screen.blit(ask2, (150,250))
			screen.blit(txtcoso, (100,300))
			screen.blit(txtcoso2, (500,300))
			pig.display.update()


	#Nivel 2
	jugador2.win=False#En el nivel 2 aun no ha ganado
	jugador2.upgraded=False
	mejora.show=True
	barriles=[]
	jugador2.rect.left,jugador2.rect.centery=0,520
	mejora.rect.left,mejora.rect.centery=80,270
	princesa.rect.left,princesa.rect.bottom=270+20,120+10
	while not jugador2.win:
		for event in pig.event.get():
			if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
				running=False
				pig.quit()

		#Updates	
		update(screen,MapaDK2,escaleras2,jugador2,mejora,princesa,2,(120+80,20+100))
		
		#Fondo de Pantalla
		screen.blit(background,(0,0))
		#Mapa
		mapRender(screen,MapaDK2,escaleras2,jugador2,mejora,princesa,barriles,(120,20),os.path.join('IMG','Mapa2.png'))
		#Textos
		texto(jugador2,txtname)

		#screen.blit(textoPantallaj, (0,0))
		pig.display.update()
		clock.tick(FPS)#Utilizar Constantes

		while jugador2.dead:
			for event in pig.event.get():
				if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
					running=False
					pig.quit()

			playlevel=False
			screen.fill(BLACK)
			fuenteDeTexto=pig.font.Font('freesansbold.ttf', 128)
			fuenteDeTexto2=pig.font.Font('freesansbold.ttf', 32)
			ask1=fuenteDeTexto.render('GAME OVER', True, WHITE,)
			ask2=fuenteDeTexto2.render(txtname+' Has perdido', True, WHITE,)
			txtcoso=fuenteDeTexto2.render('Tu puntuacion es de:', True, WHITE,)
			txtcoso2=fuenteDeTexto2.render(str(jugador2.score), True, WHITE,)
			screen.blit(ask1, (120,140))
			screen.blit(ask2, (150,250))
			screen.blit(txtcoso, (100,300))
			screen.blit(txtcoso2, (500,300))
			pig.display.update()


pig.quit()


print(__Author__)