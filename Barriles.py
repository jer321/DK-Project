#Barriles.py
__Author__='Juan Fernando Otoya'
import pygame as pig
from pygame.locals import *
import random
from Constantes import *
from Mapas import *
from Colors import *
import time

pig.init()
screenWidth=SCREEN_SIZE[0]#Utilizar de las Constantes
screenHeight=SCREEN_SIZE[1]#Utilizar de las Constantes
screen=pig.display.set_mode(SCREEN_SIZE)
clock=pig.time.Clock()

class barril1(pig.sprite.Sprite):
	def __init__(self,pos,vel=[7,5],size=(32,32)):
		''
		pig.sprite.Sprite.__init__(self)
		self.vel = vel
		self.pos = pos
		self.size = size
		self.state = None

		self.img = pig.image.load('Barrel.png').convert_alpha()
		self.img = pig.transform.scale(self.img,self.size)
		self.rect = pig.Rect(self.pos,self.size)

		self.alive = True#Estado del barril para cuando sean destruidos no se muestren
	def update(self):
		''
		self.vel[1]+=grav
		self.pos[0]+=self.vel[0]
		self.pos[1]+=self.vel[1]
		self.rect = pig.Rect(self.pos,self.size)
		self.checkBordes()
		if self.alive:
			screen.blit(self.img,self.pos)
	def checkBordes(self):
		if self.rect.left <=0:
			self.pos[0]=0
			self.vel[0]*=-.851
		elif self.rect.right>=screenWidth:
			self.pos[0]=screenWidth-self.size[0]
			self.vel[0]*=-.851

		if self.rect.top <=0:
			self.pos[1]=0
			self.vel[1]*=-1
		elif self.rect.bottom>=screenHeight:
			self.pos[1]=screenHeight-self.size[1]
			self.vel[1]*=-.2851
			#self.vel[0]*=.995#Coeficiente de friccion

		for coso in mapa:

			if coso.bottom>self.rect.bottom>=coso.top and coso.right>self.rect.centerx>coso.left:#Colision con top
				self.pos[1]=coso.top-self.size[1]
				self.vel[1]*=-.4851#Rebote
				if time.time()>barrelTiming+1.5:
					self.vel[0]*=.14851#Friccion

			#elif coso.top<self.rect.top<=coso.bottom and coso.right>self.pos[0]>coso.left:#Colision con bottom
			#	self.pos[1]=coso.bottom
			#	self.vel[1]*=-.851

			elif (coso.bottom>=self.rect.top>=coso.top or coso.bottom+10>=self.rect.bottom>=coso.top)\
			 and coso.centerx>self.rect.left>=coso.right:#Colision con right
				self.pos[0]=coso.right
				self.vel[0]*=-.851

			elif (coso.bottom>=self.rect.top>=coso.top or coso.bottom>=self.rect.bottom>=coso.top+10)\
			 and coso.centerx>self.rect.right>coso.left:#Colision con left
				self.pos[0]=coso.left-self.size[0]
				self.vel[0]*=-.851

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

barrelTiming=time.time()
running=True
while running:
	for event in pig.event.get():
		if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
			running=False
	screen.fill(GRAY)

	if time.time()>barrelTiming+1.5:#cada 0.5 segundos genera un barril
		#b=barril([random.uniform(0,640),random.uniform(0,480)],[random.uniform(-10,10),random.uniform(-10,10)])
		b=barril([32,32],random.uniform(3,15))
		barriles.append(b)
		barrelTiming=time.time()
		print(barriles)

	for barr in barriles:#Update de todos los barriles
		barr.update(MapaDK1)
		if barr.rect.right>=screenWidth and barr.rect.bottom>=screenHeight:
			barr.alive=False

	mapRender(MapaDK1)
	screen.blit(pig.transform.scale(pig.image.load('donkeyKong2.png'),(64,64)),(0,0))

	pig.display.update()
	clock.tick(30)#Utilizar Constantes

pig.quit()