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

		self.img = pig.image.load('Barrel.png').convert_alpha()
		self.img = pig.transform.scale(self.img,self.size)
		self.rect = pig.Rect(self.pos,self.size)
	def update(self):
		''
		self.checkBordes()
		self.vel[1]+=grav
		self.pos[0]+=self.vel[0]
		self.pos[1]+=self.vel[1]
		self.rect = pig.Rect(self.pos,self.size)
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
			self.vel[1]*=-.851
			#self.vel[0]*=.995#Coeficiente de friccion
		
		

barriles=pig.sprite.Group()
#for x in range(10):
#	name='barril {0}'.format(x)
#	b=barril([random.uniform(0,640),random.uniform(0,480)],[random.uniform(1,10),random.uniform(1,10)])
#	barriles.add(b)

print(barriles)
barrelTiming=time.time()
grav=1
running=True
while running:
	for event in pig.event.get():
		if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
			running=False
	screen.fill(GRAY)
	if time.time()>barrelTiming+.51:
		#b=barril([random.uniform(0,640),random.uniform(0,480)],[random.uniform(-10,10),random.uniform(-10,10)])
		b=barril([32,32],[random.uniform(-10,10),random.uniform(-10,10)])
		barriles.add(b)
		barrelTiming=time.time()
	barriles.update()
	screen.blit(pig.transform.scale(pig.image.load('donkeyKong2.png'),(64,64)),(0,0))
	#for i in barriles:
	#	i.update()
	pig.display.update()
	clock.tick(60)#Utilizar Constantes

pig.quit()

