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
		self.rect=pig.Rect(pos,size)
		self.vel=vel
		self.onAir=True
		self.gravity=GRAVITY
		self.gravityvel=0
		self.img = pig.image.load('Barrel.png').convert_alpha()
		self.img = pig.transform.scale(self.img,size)
	def mover(self):
		''
		self.rect.centerx+=self.vel

	def colisiones(self,mapa):
		''
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

	def laddersColisiones(self):
		'Checkea las escaleras'
		a=random.randint(0,1)
		for i in escaleras:
			if i[2]>self.rect.centerx>i[0] and i[3]-(i[3]-i[1])>self.rect.bottom>i[1]-(i[3]-i[1]):
				self.rect.centery+=15
				print('si')
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

	def update(self,mapa):
		''
		self.gravedad()
		self.mover()
		self.colisiones(mapa)
		self.laddersColisiones()
		#screen.blit(self.img,(self.rect.left,self.rect.top))