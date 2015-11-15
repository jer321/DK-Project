#Barriles.py
__Author__='Juan Fernando Otoya'
import pygame as pig
from pygame.locals import *
import random
from Constantes import *
from Colors import *
from Mapas import *

pig.init()
screenWidth=640+64*3#Utilizar de las Constantes
screenHeight=480+64*3#Utilizar de las Constantes
SCREEN_SIZE=screenWidth,screenHeight
screensize=screenWidth,screenHeight
screen=pig.display.set_mode(screensize)
clock=pig.time.Clock()

class barril():#pig.sprite.Sprite):
	def __init__(self,pos,vel=[7,5],size=(32,32)):
		''
		#pig.sprite.Sprite.__init__(self)
		self.vel = vel
		self.pos = pos
		self.size = size
		self.grav = 1
		self.gravityvel = 0

		self.img = pig.image.load('Barrel.png').convert_alpha()
		self.img = pig.transform.scale(self.img,self.size)
		self.rect = pig.Rect(self.pos,self.size)
	def update(self,mapa):
		''
		if self.vel[1]>9:#para que no se muevan mas pixeles que la diferencia para las colisiones y no traspasen
			self.vel[1]=9
		else:
			self.vel[1]+=self.gravityvel
		self.pos[0]+=self.vel[0]
		self.pos[1]+=self.vel[1]

		self.rect = pig.Rect(self.pos,self.size)
		self.checkBordes(mapa)
		screen.blit(self.img,self.pos)
	def checkBordes(self,mapa):

		if self.rect.left<0:
			self.pos[0]=0
			self.vel[0]*=-1

		elif self.rect.right>SCREEN_SIZE[0]:
			self.pos[0]=SCREEN_SIZE[0]-self.size[0]
			self.vel[0]*=-1

		for i in mapa:
			pendiente=(i[3]-i[1])/(i[2]-i[0])
			y=pendiente*(self.rect.centerx-i[0])+i[1]
			if y+12>self.rect.bottom>=y and i[2]+2>self.rect.centerx>i[0]-2:#+2 para que no valla traspasar bloques
				self.rect.bottom=y+2#+2 Para que siempre este adentro del rango y no genere problemas con si esta en el aire o no
				self.pos[1]=y-self.size[1]
				self.vel[1]*=-1

				return None

		self.gravityvel+=self.grav
		
class barril():
	def __init__(self,pos=(0,0),vel=5,size=(32,32)):
		''
		self.rect=pig.Rect(pos,size)
		self.vel=vel
		self.gravity=GRAVITY
		self.gravityvel=0
		self.onAir=False
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
		self.mover()
		self.gravedad()
		self.colisiones(mapa)
		screen.blit(self.img,(self.rect.left,self.rect.top))

		
def mapRender(mapa):
	'renderiza el mapa en la pantalla'
	for plataforma in mapa:
		pig.draw.polygon(screen,DARK_RED,((plataforma[0],plataforma[1]),(plataforma[2],plataforma[3]),\
			(plataforma[2],plataforma[3]+10),(plataforma[0],plataforma[1]+10)))

barriles=[]

for x in range(10):
	name='barril {0}'.format(x)
	b=barril([random.uniform(150,200),random.uniform(10,15)],random.uniform(-20,20))
	barriles.append(b)

running=True
while running:
	for event in pig.event.get():
		if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
			running=False
	screen.fill(GRAY)

	#Update de todos los Barriles creados en el for loop de arriba
	mapRender(mapa2)

	for i in barriles:
		i.update(mapa2)
	

	pig.display.update()
	clock.tick(30)#Utilizar Constantes
	fps=clock.get_fps()
	pig.display.set_caption(str(fps))

pig.quit()