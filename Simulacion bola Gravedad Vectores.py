#Barriles.py
__Author__='Juan Fernando Otoya'
import pygame as pig
from pygame.locals import *
import random
from Colors import *

pig.init()
screenWidth=640#Utilizar de las Constantes
screenHeight=480#Utilizar de las Constantes
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

		self.img = pig.image.load('Barrel.png').convert_alpha()
		self.img = pig.transform.scale(self.img,self.size)
		self.rect = pig.Rect(self.pos,self.size)
	def update(self):
		''
		if self.vel[1]>10:#para que no se muevan mas pixeles que la diferencia para las colisiones y no traspasen
			self.vel[1]=10
		else:
			self.vel[1]+=self.grav
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
			self.vel[1]*=-.851
			self.vel[0]*=.995#Coeficiente de friccion

		for coso in mapa:
			if coso.top+10>self.rect.bottom>=coso.top and coso.right>self.rect.centerx>coso.left:#Colision con top
				self.pos[1]=coso.top-self.size[1]
				self.vel[1]*=-.4851#Rebote
				#if time.time()>barrelTiming+1.5:
				#	self.vel[0]*=.14851#Friccion

			#elif coso.top<self.rect.top<=coso.bottom and coso.right>self.pos[0]>coso.left:#Colision con bottom
			#	self.pos[1]=coso.bottom
			#	self.vel[1]*=-.851

			elif (coso.bottom>=self.rect.top>=coso.top or coso.bottom+10>=self.rect.bottom>=coso.top)\
			 and coso.right-10>self.rect.left>=coso.right:#Colision con right
				self.pos[0]=coso.right
				self.vel[0]*=-.851

			elif (coso.bottom>=self.rect.top>=coso.top or coso.bottom>=self.rect.bottom>=coso.top+10)\
			 and coso.left+10>self.rect.right>coso.left:#Colision con left
				self.pos[0]=coso.left-self.size[0]
				self.vel[0]*=-.851
		
		

#barriles=pig.sprite.Group()

barriles=[]

for x in range(10):
	name='barril {0}'.format(x)
	#b=barril([random.uniform(0,640),random.uniform(0,480)],[random.uniform(-10,10),random.uniform(-10,10)])
	b=barril([random.uniform(0,640),random.uniform(1,2)],[random.uniform(-10,10),random.uniform(-10,10)])
	barriles.append(b)


mapa=[]
dif=0
for x in range(3):
	if dif<640-80:
		dif+=120
	b=pig.Rect(random.uniform(0,300),dif,random.uniform(200,300),random.uniform(32,80))
	mapa.append(b)
#b=pig.Rect(0,430,640,50)
#c=pig.Rect(screenWidth/2,screenHeight/2,80,80)
#mapa.append(b)
#mapa.append(c)
print(mapa)
running=True
while running:
	for event in pig.event.get():
		if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
			running=False
	screen.fill(GRAY)

	#Update de todos los Barriles creados en el for loop de arriba

	for i in mapa:
		pig.draw.rect(screen,RED,i)

	for i in barriles:
		i.update()
	

	pig.display.update()
	clock.tick(15)#Utilizar Constantes
	fps=clock.get_fps()
	pig.display.set_caption(str(fps))

pig.quit()