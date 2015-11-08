__Author__='Juan Fernando Otoya'
Description='''se implementa Prototipo grafico del primer nivel.

Todavia no se han implementado colisiones con el mapa.]
Se implementaran variables para las condiciones de las colisiones.'''
import pygame as pig
from pygame.locals import *
from Colors import *
from Constantes import *

class Player(pig.sprite.Sprite):
	def __init__(self,img='Character\der1.png',pos=(10,600),playerSize=(64,64),vel=(7,12)):
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

		self.img = None
		self.rect = pig.Rect(self.posx, self.posy, self.width, self.height)

	def update(self):
		''
		self.cmd()
		self.loadImg()
		self.gravity()
		self.rect = pig.Rect(self.posx,self.posy,self.width,self.height); #print(self.rect.left,self.rect.top)
		self.width,self.height = self.img.get_rect().size#actualizamos el tamano de la imagen para cuando cambia de sprite
		self.checkBordes()
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
			self.posx+=self.xvel
		elif self.keys[K_LEFT]:
			self.dir='W'
			self.posx-=self.xvel

	def loadImg(self):
		if self.onAir:
			if self.dir=='E':
				if self.gravityVel>abs(self.yvel):
					pass#self.img=pig.image.load('Sprites Player\derJD.png')
				else:
					self.img=pig.image.load('Character\c2\derJU.png')
			elif self.dir=='W':
				if self.gravityVel>abs(self.yvel):
					pass#self.img=pig.image.load('Sprites Player\izqJD.png')
				else:
					self.img=pig.image.load('Character\c2\izqJU.png')

		else:
			if self.dir=='E':
				self.img=pig.image.load('Character\c2\der1.png')
			elif self.dir=='W':
				self.img=pig.image.load('Character\c2\izq1.png')
		self.img=pig.transform.scale(self.img,(45,62))#Se Normaliza el tamano de la imagen escogida
		
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


		for i in range(len(dimmapa)-1): #f(x)=m(posx-x)+y
			y=pendientes[i]*(self.posx-dimmapa[i][0])+dimmapa[i][1]
			if self.rect.bottom>y and self.rect.bottom<y+10:
				self.posy=y-self.height
				self.onAir=False
		print(self.onAir)

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
background=pig.image.load('background.png').convert_alpha()#utilizar Constantes
background=pig.transform.scale(background,(SCREEN_SIZE[0],SCREEN_SIZE[1]))

difaltura=int(SCREEN_SIZE[1]/7)
#X0,  y0,        x1,          y1
dimmapa=\
(0,difaltura,SCREEN_SIZE[0],difaltura-30),\
(0,difaltura*3,SCREEN_SIZE[0],difaltura*3-30),\
(0,difaltura*5,SCREEN_SIZE[0],difaltura*5-30),\
(0,difaltura*6+40,SCREEN_SIZE[0],difaltura*6-30)

pendientes=[]
for i in dimmapa:
	'Saca las pendientes de todos los obstaculos del mapa'
	m=(i[3]-i[1])/(i[2]-i[0])#La pendiente. en dimmapa se dan todos los puntos del mapa
	pendientes.append(m)
print(pendientes)

while running:
	for event in pig.event.get():
		if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
			running=False

	#Fondo de Pantalla
	screen.blit(background,(0,0))

	#Mapa
	for plataforma in dimmapa:
		pig.draw.polygon(screen,DARK_RED,((plataforma[0],plataforma[1]),(plataforma[2],plataforma[3]),\
			(plataforma[2],plataforma[3]+10),(plataforma[0],plataforma[1]+10)))
	
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