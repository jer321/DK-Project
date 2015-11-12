__Author__='Juan Fernando Otoya'
Description='''se implementa Prototipo grafico del primer nivel.
Todavia no se han implementado colisiones con el mapa.]
Se implementaran variables para las condiciones de las colisiones.'''
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
	def colisiones(self, mapa):
		if self.rect.left<0:
			self.rect.left=0
		elif self.rect.right>SCREEN_SIZE[0]:
			self.rect.right=SCREEN_SIZE[0]
		if self.rect.bottom>SCREEN_SIZE[1]:
			self.rect.bottom=SCREEN_SIZE[1]

		#for i in range(len(mapa)):
		for i in mapa:
			pendiente=(i[3]-i[1])/(i[2]-i[0])
			#y=pendientes[i]*(self.rect.centerx-mapa[i][0])+mapa[i][1]
			y=pendiente*(self.rect.centerx-i[0])+i[1]
			#if y+12>self.rect.bottom>=y and mapa[i][2]+2>self.rect.centerx>mapa[i][0]-2:#+2 para que no valla traspasar bloques
			if y+12>self.rect.bottom>=y and i[2]+2>self.rect.centerx>i[0]-2:#+2 para que no valla traspasar bloques
				self.onAir=False
				self.canJump=True
				self.rect.bottom=y+2#+2 Para que siempre este adentro del rango y no genere problemas con si esta en el aire o no
				self.jumpvel=0
				return

		self.onAir=True
		self.canJump=False
	def laddersColisiones(self):
		if 70+40>self.rect.centerx>70 and SCREEN_SIZE[1]>self.rect.bottom>SCREEN_SIZE[1]-75:
			self.onAir=False
			self.canJump=True
			self.jumpvel=0
			self.state='climbing'#Cuando escala la escalera
			return None
		self.state=None


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

		if self.state=='climbing':
			self.img=pig.image.load('Character\der1.png')
		self.img=pig.transform.scale(self.img,(45,62))#Se Normaliza el tamano de la imagen escogida

	def update(self, mapa):
		self.cmd()
		self.grav()
		self.colisiones(mapa)
		self.laddersColisiones()
		self.loadImg()
		screen.blit(self.img,(self.rect.left,self.rect.top))



def mapRender(mapa):
	'renderiza el mapa en la pantalla'
	for plataforma in mapa:
		pig.draw.polygon(screen,DARK_RED,((plataforma[0],plataforma[1]),(plataforma[2],plataforma[3]),\
			(plataforma[2],plataforma[3]+10),(plataforma[0],plataforma[1]+10)))


pig.init()

screensize=SCREEN_SIZE[0],SCREEN_SIZE[1]#Resolucionde Constantes
screen=pig.display.set_mode(screensize)

clock=pig.time.Clock()
pig.display.set_caption(CAPTION)#importar de Constantes
jugador2=Player2()
#__main__
running=True
background=pig.image.load('background.png').convert_alpha()#utilizar Constantes
background=pig.transform.scale(background,(SCREEN_SIZE[0],SCREEN_SIZE[1]))

while running:
	for event in pig.event.get():
		if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
			running=False

	#Fondo de Pantalla
	screen.blit(background,(0,0))

	#Mapa
	mapRender(dimmapa)
	#Escalera
	pig.draw.rect(screen,GREEN,(70,SCREEN_SIZE[1]-80,40,80))
	#Los Dibujos
	jugador2.update(dimmapa)#Adentro se pone el mapa para las colisiones

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
