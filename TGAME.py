__Author__='Juan Fernando Otoya'
Description='''se implementa Prototipo grafico del primer nivel.

Todavia no se han implementado colisiones con el mapa.]
Se implementaran variables para las condiciones de las colisiones.'''
import pygame as pig
from pygame.locals import *
from Colors import *
from Constantes import *



class Player(pig.sprite.Sprite):
	def __init__(self,img='Sprites Player\der1.png',pos=(10,600),playerSize=(54,45),vel=(7,12)):
		''
		pig.sprite.Sprite.__init__(self)
		self.posx,self.posy = pos
		self.width,self.height = playerSize
		self.xvel,self.yvel = vel
		self.gravityVel = 0
		self.difvel = self.yvel
		self.onAir=True
		self.keys = pig.key.get_pressed()
		self.dir = 'E'#Direccion del personaje

		self.img = pig.image.load(img)
		self.img = pig.transform.scale(self.img,playerSize)
		self.rect = pig.Rect(self.posx, self.posy, self.width, self.height)

	def update(self):
		''
		self.cmd()
		self.gravity()
		self.rect = pig.Rect(self.posx,self.posy,self.width,self.height); #print(self.rect.left,self.rect.top)
		self.width,self.height = self.img.get_rect().size#actualizamos el tamano de la imagen para cuando cambia de sprite
		self.checkBordes()
		self.loadImg()
		screen.blit(self.img,(self.posx,self.posy))#Se pinta la imagen ya actualizada luego de la colision
	def cmd(self):
		'Los Comandos del Jugador'
		self.keys = pig.key.get_pressed()
		#Salto
		if self.keys[K_UP]:
			self.posy-=self.yvel
		if self.onAir and not self.keys[K_UP]:#Normaliza la caida al soltar el boton en un salto
			self.posy-=self.yvel

		if self.keys[K_RIGHT]:
			self.dir='E'
			self.img=pig.image.load('Sprites Player\der1.png')
			self.posx+=self.xvel
		elif self.keys[K_LEFT]:
			self.dir='W'
			self.img=pig.image.load('Sprites Player\izq1.png')
			self.posx-=self.xvel

	def loadImg(self):
		if self.dir=='E' and self.onAir:
			if self.gravityVel>abs(self.yvel):# or not self.keys[K_UP]:
				self.img=pig.image.load('Sprites Player\derJD.png')
			else:
				self.img=pig.image.load('Sprites Player\derJU.png')
		elif self.dir=='W' and self.onAir:
			if self.gravityVel>abs(self.yvel):# or not self.keys[K_UP]:
				self.img=pig.image.load('Sprites Player\izqJD.png')
			else:
				self.img=pig.image.load('Sprites Player\izqJU.png')

		else:
			if self.dir=='E':
				self.img=pig.image.load('Sprites Player\der1.png')
			elif self.dir=='W':
				self.img=pig.image.load('Sprites Player\izq1.png')

	def checkBordes(self):
		'Detecta la colision con los bordes y actualiza la posicion del Player para que no sobrepase los bordes'
		if self.rect.top<0:#Borde superior de la pantalla
			self.posy=0
		if self.rect.bottom>=SCREEN_SIZE[1]:#Borde inferior de la pantalla
			self.posy=SCREEN_SIZE[1]-self.height
			self.jumpvel=0
			self.onAir=False
		else:
			self.onAir=True

		if self.rect.left<0:#Borde izquierdo de la pantalla
			self.posx=0
		elif self.rect.right>SCREEN_SIZE[0]:#Borde derecho de la pantalla
			self.posx=SCREEN_SIZE[0]-self.width

		self.rect=pig.Rect(self.posx,self.posy,self.width,self.height)#Actualizamos las posiciones del personaje
	def checkMapCollision(self):
		''
	def gravity(self):
		''
		gravity=GRAVITY#Utilizar de Constantes
		if self.onAir:
			self.gravityVel+=gravity#Poner limite a velocidad maxima de caida
		else:
			self.gravityVel=0
		self.posy+=self.gravityVel

pig.init()

screensize=SCREEN_SIZE[0],SCREEN_SIZE[1]#Resolucionde Constantes
screen=pig.display.set_mode(screensize)

clock=pig.time.Clock()
pig.display.set_caption(CAPTION)#importar de Constantes
jugador=Player()
#__main__
running=True
background=pig.image.load('background.jpg').convert_alpha()#utilizar Constantes
background=pig.transform.scale(background,(SCREEN_SIZE[0],SCREEN_SIZE[1]))
while running:
	for event in pig.event.get():
		if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
			running=False

	#Fondo de Pantalla
	screen.blit(background,(0,0))

	#Mapa
	pig.draw.polygon(screen,WOOD_BROWN,((0,390),(640-80,390),(640-80,385),(0,380)))#diferencia de 90 con los pies del jugador
	pig.draw.polygon(screen,WOOD_BROWN,((640,390-90),(80,390-90),(80,385-90),(640,380-90)))
	
	#Los Dibujos
	jugador.update()

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