__Author__='Juan Fernando Otoya'
Description='''se mejoro el sistema de imagenes.

Todavia no se han implementado colisiones con el mapa.'''
import pygame
import pygame as pig
from pygame.locals import *
from Colors import *

#y=int(mx+b)


class Player(pig.sprite.Sprite):
	def __init__(self,img='Sprites Player\der1.png',pos=(0,10),playerSize=(54,45),vel=(4,16)):
		''
		pig.sprite.Sprite.__init__(self)
		self.posx,self.posy = pos
		self.width,self.height = playerSize
		self.xvel,self.yvel = vel
		self.gravityVel = 0
		self.onAir=True
		self.dir = None#Direccion del personaje

		self.img = pig.image.load(img)
		self.img = pig.transform.scale(self.img,playerSize)
		self.rect = pig.Rect(self.posx, self.posy, self.width, self.height)


	def update(self):
		''
		self.cmd()
		self.rect = pig.Rect(self.posx,self.posy,self.width,self.height); #print(self.rect.left,self.rect.top)
		self.gravity()
		self.checkBordes()
		print(self.img.get_rect().size)
		screen.blit(self.img,(self.posx,self.posy))#Se pinta la imagen ya actualizada luego de la colision
	def cmd(self):
		'Los Comandos del Jugador'
		keys = pig.key.get_pressed()#Para la clase Player
		if keys[K_UP]:
			self.posy-=self.yvel
		elif keys[K_DOWN]:
			self.posy+=self.yvel
		if keys[K_RIGHT]:
			self.dir='E'
			self.img=pig.image.load('Sprites Player\der1.png')
			self.posx+=self.xvel
		elif keys[K_LEFT]:
			self.dir='W'
			self.img=pig.image.load('Sprites Player\izq1.png')
			self.posx-=self.xvel
	def checkBordes(self):
		'Detecta la colision con los bordes y actualiza la posicion del Player para que no sobrepase los bordes'
		if self.rect.top<0:#Borde superior de la pantalla
			self.posy=0
		if self.rect.bottom>=screenHeight:#Borde inferior de la pantalla
			self.posy=screenHeight-self.height
			self.onAir=False
		else:
			self.onAir=True

		if self.rect.left<0:#Borde izquierdo de la pantalla
			self.posx=0
		elif self.rect.right>screenWidth:#Borde derecho de la pantalla
			self.posx=screenWidth-self.width

		self.rect=pig.Rect(self.posx,self.posy,self.width,self.height)#Actualizamos las posiciones del personaje
	def checkMapCollision(self):
		''

	def gravity(self):
		''
		gravity=1#Utilizar de Constantes
		if self.onAir:
			if self.dir=='E':
				self.img=pig.image.load('Sprites Player\derJD.png')
			elif self.dir=='W':
				self.img=pig.image.load('Sprites Player\izqJD.png')
			self.gravityVel+=gravity#Poner limite a velocidad maxima de caida
		else:
			if self.dir=='E':
				self.img=pig.image.load('Sprites Player\der1.png')
			elif self.dir=='W':
				self.img=pig.image.load('Sprites Player\izq1.png')
			self.gravityVel=0
		self.posy+=self.gravityVel

suelosy=[]

pygame.init()

screenWidth=640#Utilizar de las Constantes
screenHeight=480#Utilizar de las Constantes

screensize=screenWidth,screenHeight
screen=pygame.display.set_mode(screensize)

clock=pygame.time.Clock()

jugador=Player()
#__main__
running=True
background=pig.image.load('background.jpg').convert_alpha()
background=pig.transform.scale(background,(screenWidth,screenHeight))
while running:
	for event in pygame.event.get():
		if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
			running=False

	#Fondo de Pantalla
	screen.blit(background,(0,0))
	#Mapa
	pig.draw.polygon(screen,SLATE_GRAY,((0,200),(0,170),(400,200),(400,230)))
	pig.draw.polygon(screen,BLACK,((640,200+128),(640,170+128),(200,185+128),(200,200+128)))
	#Los Dibujos
	jugador.update()
	#jugador.x += movex
	#jugador.y += movey

	#El tiempo transcurrido del juego mostrado en pantalla
	tiempoTranscurrido=pygame.time.get_ticks()/1000
	fuenteDeTexto=pygame.font.Font('freesansbold.ttf', 32)
	textoPantalla=fuenteDeTexto.render(str(tiempoTranscurrido), True, GREEN, BLUE)#el True es para el Anti-Aliased (alisado)
	screen.blit(textoPantalla, (300,0))

	pygame.display.update()
	clock.tick(60)#Utilizar Constantes

pygame.quit()
