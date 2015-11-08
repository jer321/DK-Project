#Barriles.py
__Author__='Juan Fernando Otoya'
import pygame as pig
from pygame.locals import *
import random
from Colors import *
import time

pig.init()
screenWidth=640#Utilizar de las Constantes
screenHeight=480#Utilizar de las Constantes
screensize=screenWidth,screenHeight
screen=pig.display.set_mode(screensize)
clock=pig.time.Clock()

class barril(pig.sprite.Sprite):
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
	def update(self):
		''
		self.vel[1]+=grav
		self.pos[0]+=self.vel[0]
		self.pos[1]+=self.vel[1]
		self.rect = pig.Rect(self.pos,self.size)
		self.checkBordes()
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
		
		
barriles=[]
mapa=[]

dif=0
for x in range(3):
	if dif<640-80:
		dif+=120
	b=pig.Rect(random.uniform(0,100),dif,random.uniform(320,640),random.uniform(40,50))
	#mapa.append(b)

b=pig.Rect(0,100,160,20)
mapa.append(b)
b=pig.Rect(190,110,150,20)
mapa.append(b)
b=pig.Rect(380,120,150,20)
mapa.append(b)

b=pig.Rect(480,220,160,20)
mapa.append(b)
b=pig.Rect(480-200,220+20,160,20)
mapa.append(b)
b=pig.Rect(480-400,220+40,160,20)
mapa.append(b)


barrelTiming=time.time()
grav=1
running=True
while running:
	for event in pig.event.get():
		if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
			running=False
	screen.fill(GRAY)

	if time.time()>barrelTiming+1.5:#cada 0.5 segundos genera un barril
		#b=barril([random.uniform(0,640),random.uniform(0,480)],[random.uniform(-10,10),random.uniform(-10,10)])
		b=barril([32,32],[random.uniform(3,15),random.uniform(-10,10)])
		barriles.append(b)
		barrelTiming=time.time()
		print(barriles)

	for barr in range(len(barriles)-1):#Update de todos los barriles
	'se Cambio el loop for, para poder quitar los barriles cuando lleguen al borde de la pantalla'
		barriles[barr].update()
		if barriles[barr].rect.right>=screenWidth and barriles[barr].rect.bottom>=screenHeight:
			barriles.pop(barr)


	for i in mapa:
		pig.draw.rect(screen,RED,i)
	screen.blit(pig.transform.scale(pig.image.load('donkeyKong2.png'),(64,64)),(0,0))

	pig.display.update()
	clock.tick(30)#Utilizar Constantes

pig.quit()