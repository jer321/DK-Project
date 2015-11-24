__Author__='Juan Fernando Otoya'
import pygame as pig
from pygame.locals import *
from DATA.Constantes import *
from DATA.Proyectil import *
from DATA.Escaleras import *
import os

proyectiles=[]
class Player2:
	def __init__(self,pos=SCREEN_SIZE,vel=WALK_VEL,size=(45,62)):
		'''pos=posicion del jugador, vel=velocidad en x, salto'''
		self.jumpvel = 0
		self.walkvel = vel
		self.size = size
		self.gravityVel = 0
		self.score=0

		self.state = None#Estado del jugador
		self.onAir = True #Cuando esta callendo
		self.canJump = False #Cuando puede saltar
		self.upgraded = False #Permite al jugador disparar o no.Cambiar a False para la mejora
		self.canShot = True #Permite limitar los disparos.Cambiar a False para la mejora y para cada cuanto disparar
		self.canClimb= False #Cuando puede subir escaleras
		self.dead = False #Cuando Muere
		self.win = False #Cuando salva a la princesa

		self.rect = pig.Rect(SCREEN_SIZE[0]-self.size[0],SCREEN_SIZE[1]-self.size[1],self.size[0],self.size[1])
		self.dir = 'E'#Direccion del jugador(W,E)
		self.img = pig.image.load(os.path.join('IMG','Character','c2','der1.png')) #None#La imagen que se muestra del jugador

	def cmd(self):
		'comandos del teclado'
		self.keys = pig.key.get_pressed()
		#Salto
		if self.keys[K_SPACE]:
			if self.canJump:
				self.jump()
		self.rect.centery+=self.jumpvel#Se suma too el tiempo la velocidad del salto. cuando se unde la tecla, esa velocidad cambia y cuando no se unde vale 0

		if self.keys[K_DOWN]:# and self.laddersColisiones():
			self.rect.centery+=20


		if self.keys[K_b]:
			if self.upgraded:#Si ha conseguido la mejora
				self.shoot()
				self.canShot=False#El self.canShot hace que no se sigan disparando las balas cuando se deja undido el boton
		else:
			self.canShot=True

		if self.keys[K_RIGHT]:
			self.dir='E'
			self.rect.centerx+=self.walkvel
		elif self.keys[K_LEFT]:
			self.dir='W'
			self.rect.centerx-=self.walkvel
	def jump(self):
		'''Salto
			si se llama la funcion de salto si no esta en el aire, altera la velocidad de salto la cual siempre se esta sumando
			lo que hace que el jugador pueda "saltar". pero esta solo se incrementa si el jugador no esta en el aire (onAir=False)'''
		if self.onAir:
			return
		self.jumpvel=JUMP_VEL
	def shoot(self):
		'''Agrega una "bala" a la lista de proyectiles que ha lanzado el jugador
		 y los objetos en la lista se actualizan en la funcion update() en TGAME'''
		if self.canShot:
			proyectiles.append(proyectil(self,(self.rect.left,self.rect.top+32)))

	def grav(self):
		'''si el jugador se encuentra en el aire (esta en el aire cuando no toca ninguna plataforma o escalera)
		le suma a su posicion en y, gravityVel la cual se va incrementando con un limite de "MAX_Y_VEL" cuando el jugador esta en el aire.
		el limite para el cambio de posicion en y del personaje es para que no traspace bloques.'''
		if self.onAir:
			self.gravityVel+=GRAVITY
		else:
			self.gravityVel=0
		if self.gravityVel+self.jumpvel>MAX_Y_VEL:
			self.gravityVel=MAX_Y_VEL-self.jumpvel#Velocidad Maxima de caida Para que no traspace bloques del mapa
		self.rect.centery+=self.gravityVel
	def colisiones(self, mapa):
		'''si toca alguna plataforma cancela onAir por lo que el jugador no caera y acomoda la posicion en y 
		 respecto a la recta para que no quede metido en el bloque.'''
		if not self.state=='stair':
			if self.rect.left<0:
				self.rect.left=0
			elif self.rect.right>SCREEN_SIZE[0]:
				self.rect.right=SCREEN_SIZE[0]
			if self.rect.bottom>SCREEN_SIZE[1]:
				self.rect.bottom=SCREEN_SIZE[1]

			for i in mapa:
				pendiente=(i[3]-i[1])/(i[2]-i[0])
				y=pendiente*(self.rect.centerx-i[0])+i[1]
				if y+12>self.rect.bottom>=y and i[2]+2>self.rect.centerx>i[0]-2:#+2 para que no valla traspasar bloques
					self.onAir=False
					self.canJump=True
					self.rect.bottom=y+2#+2 Para que siempre este adentro del rango y no genere problemas con si esta en el aire o no
					self.jumpvel=0
					return

			self.onAir=True
			self.canJump=False
	def laddersColisiones(self,stairs):
		'''si toca una escalera. cancela las colisiones con el mapa para que pueda subir y bajar por las escaleras, pero tambien
			cancela onAir por lo que el jugador no caera.'''
		for i in stairs:
			if i[2]>self.rect.centerx>i[0] and i[3]>self.rect.bottom>i[1]:
				self.onAir=False
				self.canJump=True
				self.jumpvel=0
				self.canClimb=True#Cuando escala la escalera
				self.state='stair'
				return True
		self.canClimb=False
		self.state=None

	def loadImg(self):
		'''carga la imagen correspondiente para la accion del jugador.
		 si esta onAir carga la imagen de saltando.
		 si esta en una escalera carga la imagen de stair.
		 y si esta en el suelo carga la imagen en la que se encuentra normal.
		 Todas las imagenes tienen una direccion "dir" la cual indica hacia donde esta mirando el jugador
		 y "dir" es la que permite cargar uno de los lados de cada imagen dependiendo hacia que lado mira'''
		if self.onAir:
			if self.dir=='E':
				if self.gravityVel>abs(self.jumpvel) and self.onAir:
					pass#self.img=pig.image.load('Sprites Player\derJD.png')
				else:
					self.img=pig.image.load(os.path.join('IMG','Character','c2','derJU.png'))
			elif self.dir=='W':
				if self.gravityVel>abs(self.jumpvel) and self.onAir:
					pass#self.img=pig.image.load('Sprites Player\izqJD.png')
				else:
					self.img=pig.image.load(os.path.join('IMG','Character','c2','izqJU.png'))

		else:
			if self.dir=='E':
				self.img=pig.image.load(os.path.join('IMG','Character','c2','der1.png'))
			elif self.dir=='W':
				self.img=pig.image.load(os.path.join('IMG','Character','c2','izq1.png'))

		if self.canClimb==True:
			if self.dir=='E':
				self.img=pig.image.load(os.path.join('IMG','Character','c2','stair1.png'))
			elif self.dir=='W':
				self.img=pig.image.load(os.path.join('IMG','Character','c2','stair2.png'))
		self.img=pig.transform.scale(self.img,(45,62))#Se Normaliza el tamano de la imagen escogida

	def update(self, mapa, stairs):
		self.cmd()
		self.grav()
		self.colisiones(mapa)
		self.laddersColisiones(stairs)
		self.loadImg()
		#screen.blit(self.img,(self.rect.left,self.rect.top))
