__Author__='Juan Fernando Otoya'
#BarrilTest.py
import pygame as pig
from pygame.locals import *
import random
from DATA.Constantes import *
from DATA.Escaleras import *
import os

class barril():
	def __init__(self,pos=(0,0),vel=5,size=(32,32)):
		'''pos es la posicion del barril, vel es el cambio en el eje x'''
		self.rect=pig.Rect(pos,size)#Se utiliza el onjeto "Rect" de pygame para llevar cuenta de la posicion de cada lado del rectangulo
		self.vel=vel
		self.onAir=True
		self.gravity=GRAVITY#Constante
		self.gravityvel=0#Variable que hace un cambio en el eje y. es 0 cuando toca alguna plataforma y se le va sumando GRAVITY cuando no toca plataformas

		self.canfall=None

		self.img = pig.image.load(os.path.join('IMG','Barrel.png')).convert_alpha()
		self.img = pig.transform.scale(self.img,size)

	def mover(self):
		'''Mueve al barril respecto a la velocidad dada. cuando toca alguna esquina del mapa la velocidad se multiplica por -1
			por lo que se movera hacia el otro lado'''
		self.rect.centerx+=self.vel

	def colisiones(self,mapa):
		'Detecta las colisiones con el mapa y afecta el vector de velocidad'
		#Colision con el lado izquierdo de la pantalla
		if self.rect.left<0:
			self.rect.left=0
			self.vel*=-1
		#Colision con el lado derecho de la pantalla
		elif self.rect.right>SCREEN_SIZE[0]:
			#SCREEN_SIZE[0] es el ancho de la pantalla. esta en 'Constantes.py'
			self.rect.right=SCREEN_SIZE[0]
			self.vel*=-1

		for i in mapa:
			pendiente=(i[3]-i[1])/(i[2]-i[0])#Le saca la pendiente a cada una de las lineas dadas en el mapa
			y=pendiente*(self.rect.centerx-i[0])+i[1]#En la recta, se ve el "y" de la linea del mapa respecto a la posicion en el eje x del jugador
			if y+12>self.rect.bottom>=y and i[2]+2>self.rect.centerx>i[0]-2:#+2 para que no valla traspasar bloques
				self.rect.bottom=y#Cuando toca el mapa. como a veces queda adentro porque se mueve mas pixeles, se pone el ese punto 'y' que se saca respecto al jugador
				self.onAir=False#Si toca el mapa, el personaje ya no se encuentra en el aire, por lo que ya no cae y no se le suma la gravedad a la posicion en y
				return None
		self.onAir=True

	def laddersColisiones(self,stairs):
		'Checkea las escaleras'
		Bool=True,False
		for i in stairs:
			#Detecta la parte arriba de las escaleras, no tocando la escalera, lo que hace que caiga desde la plataforma de arriba.
			if i[2]>self.rect.centerx>i[0] and i[3]-(i[3]-i[1])>self.rect.bottom>i[1]-(i[3]-i[1]):
				#Canfall toma un valor de (True,False,None)
				#si Canfall es None, entonces escoge un valor aleatorio entre (True,False), lo cual decide si cae por la escalera o no.
				if not self.canfall in Bool:
					self.canfall = random.randint(0,1)#Hace aleatoria la caida por las Escaleras
				#Si el Canfall es True se le suman 15 pixeles a la posicion de y, lo que hace que ya no toque el suelo y por lo tanto caiga.
				if self.canfall:
					self.rect.centery+=15
					#Cambiar imagen
				return None
			#una vez ya deja de tocar la escalera, canfall se vuelve none para que cuando toque la proxima escalera vuelva a escoger si cae o no.
			self.canfall=None

	def gravedad(self):
		'Hace caer el barril cuando no esta tocando ningun bloque del mapa u otros casos (cuando onAir=True)'
		if self.onAir:
			#MAX_Y_VEL es la velocidad maxima en el eje y que puede tener para que no traspase los bloques del mapa
			#Cuando gravityvel es mayor a la velocidad maxima que puede tener en y, gravityvel se vuelve la velocidad maxima.
			#estp evita que los barriles traspasen el mapa.
			if self.gravityvel>=MAX_Y_VEL:
				self.gravityvel=MAX_Y_VEL
			else:
				self.gravityvel+=self.gravity
			self.rect.centery+=self.gravityvel
			return None
		self.gravityvel=0
	def kill(self,player):
		'Si toca al jugador lo mata (player.dead=True), lo cual permite que se muestre la pantalla de "GAME OVER"'
		if (self.rect.right>player.rect.left>self.rect.left or self.rect.right>player.rect.right>self.rect.left)\
		 and (player.rect.bottom>self.rect.centery>player.rect.top):
			player.dead=True

	def update(self,mapa,stairs,player):
		'Llama las funciones de la clase para que se actualicen las posiciones y todos los checkeos'
		self.gravedad()
		self.mover()
		self.colisiones(mapa)
		self.laddersColisiones(stairs)
		self.kill(player)
