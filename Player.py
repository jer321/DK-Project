#Player.py
import pygame as pig
from pygame.locals import *
from Colors import *
from Constantes import *
from Mapa import *

class Player2:
	def __init__(self,pos=SCREEN_SIZE,vel=WALK_VEL,size=(45,62)):
		'pos=posicion del jugador, vel=velocidad en x, salto'
		self.jumpvel = 0
		self.walkvel = vel
		self.size = size
		self.gravityVel = 0

		self.state = None#Estado del jugador
		self.onAir = True
		self.canJump = False
		self.canShot = False
		self.dead = False

		self.rect = pig.Rect(SCREEN_SIZE[0]-self.size[0],SCREEN_SIZE[1]-self.size[1],self.size[0],self.size[1])
		self.dir = 'E'#Direccion del jugador(W,E)
		self.img = pig.image.load('Character\c2\der1.png') #None#La imagen que se muestra del jugador

	def cmd(self):
		'comandos'
		self.keys = pig.key.get_pressed()
		#Salto
		if self.keys[K_UP]:
			if self.canJump:
				self.jump()
		self.rect.centery+=self.jumpvel#Se suma too el tiempo la velocidad del salto. cuando se unde la tecla, esa velocidad cambia y cuando no se unde vale 0

		if self.keys[K_RIGHT]:
			self.dir='E'
			self.rect.centerx+=self.walkvel
		elif self.keys[K_LEFT]:
			self.dir='W'
			self.rect.centerx-=self.walkvel
		print(self.keys[K_UP])
	def jump(self):
		if self.onAir:
			return
		self.jumpvel=JUMP_VEL

	def grav(self):
		if self.onAir:
			self.gravityVel+=GRAVITY
		else:
			self.gravityVel=0
		if self.gravityVel+self.jumpvel>MAX_Y_VEL:
			self.gravityVel=MAX_Y_VEL-self.jumpvel#Velocidad Maxima de caida Para que no traspace bloques del mapa
		self.rect.centery+=self.gravityVel
	def colisiones(self):
		if self.rect.left<0:
			self.rect.left=0
		elif self.rect.right>SCREEN_SIZE[0]:
			self.rect.right=SCREEN_SIZE[0]
		if self.rect.bottom>SCREEN_SIZE[1]:
			self.rect.bottom=SCREEN_SIZE[1]

		for i in range(len(dimmapa)):
			y=pendientes[i]*(self.rect.centerx-dimmapa[i][0])+dimmapa[i][1]
			if y+10>self.rect.bottom>=y and dimmapa[i][2]>self.rect.centerx>dimmapa[i][0]:
				self.onAir=False
				self.canJump=True
				self.rect.bottom=y+2#+1 Para que siempre este adentro el rango y no genere problemas con si esta en el aire o no
				self.jumpvel=0
				return

		self.onAir=True
		self.canJump=False
	def loadImg(self):
		if self.onAir:
			if self.dir=='E':
				if self.gravityVel>abs(self.jumpvel) and self.onAir:
					pass#self.img=pig.image.load('Sprites Player\derJD.png')
				else:
					self.img=pig.image.load('Character\c2\derJU.png')
			elif self.dir=='W':
				if self.gravityVel>abs(self.jumpvel) and self.onAir:
					pass#self.img=pig.image.load('Sprites Player\izqJD.png')
				else:
					self.img=pig.image.load('Character\c2\izqJU.png')

		else:
			if self.dir=='E':
				self.img=pig.image.load('Character\c2\der1.png')
			elif self.dir=='W':
				self.img=pig.image.load('Character\c2\izq1.png')
		self.img=pig.transform.scale(self.img,(45,62))#Se Normaliza el tamano de la imagen escogida

	def update(self):
		self.cmd()
		self.grav()
		self.colisiones()
		self.loadImg()
		screen.blit(self.img,(self.rect.left,self.rect.top))

jonh=Player2()