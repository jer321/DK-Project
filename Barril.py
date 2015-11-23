__Author__='Juan Fernando Otoya'
#BarrilTest.py
import pygame as pig
from pygame.locals import *
import random
from Constantes import *
from Escaleras import *

class barril():
	def __init__(self,pos=(0,0),vel=5,size=(32,32)):
		''
		self.rect=pig.Rect(pos,size)#Se utiliza el onjeto "Rect" de pygame para llevar cuenta de la posicion de cada lado del rectangulo
		self.vel=vel
		self.onAir=True
		self.gravity=GRAVITY
		self.gravityvel=0

		self.canfall=None

		self.img = pig.image.load('Barrel.png').convert_alpha()
		self.img = pig.transform.scale(self.img,size)

	def mover(self):
		'Mueve al barril respecto a la velocidad dada'
		self.rect.centerx+=self.vel

	def colisiones(self,mapa):
		'Detecta las colisiones con el mapa y afecta el vector de velocidad'
		if self.rect.left<0:
			self.rect.left=0
			self.vel*=-1

		elif self.rect.right>SCREEN_SIZE[0]:
			self.rect.right=SCREEN_SIZE[0]
			self.vel*=-1

		for i in mapa:
			pendiente=(i[3]-i[1])/(i[2]-i[0])
			y=pendiente*(self.rect.centerx-i[0])+i[1]
			if y+12>self.rect.bottom>=y and i[2]+2>self.rect.centerx>i[0]-2:#+2 para que no valla traspasar bloques
				self.rect.bottom=y
				self.onAir=False
				return None
		self.onAir=True

	def laddersColisiones(self,stairs):
		'Checkea las escaleras'
		Bool=True,False
		for i in stairs:
			if i[2]>self.rect.centerx>i[0] and i[3]-(i[3]-i[1])>self.rect.bottom>i[1]-(i[3]-i[1]):
				if not self.canfall in Bool:
					self.canfall = random.randint(0,1)#Hace aleatoria la caida por las Escaleras
				if self.canfall:
					self.rect.centery+=15
					#Cambiar imagen
				return None
			self.canfall=8

	def gravedad(self):
		''
		if self.onAir:
			if self.gravityvel>MAX_Y_VEL:
				self.gravityvel=MAX_Y_VEL
			else:
				self.gravityvel+=self.gravity
			self.rect.centery+=self.gravityvel
			return None
		self.gravityvel=0
	def kill(self,player):
		'Si toca al jugador lo mata'
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
		#screen.blit(self.img,(self.rect.left,self.rect.top))