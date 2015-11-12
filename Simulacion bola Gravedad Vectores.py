#Barriles.py
__Author__='Juan Fernando Otoya'
import pygame as pig
from pygame.locals import *
import random
from Colors import *
from Mapa import *

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
		if self.vel[1]>10:#para que no se muevan mas pixeles que la diferencia para las colisiones y no traspasen
			self.vel[1]=10
		else:
			self.vel[1]+=self.gravityvel
		self.pos[0]+=self.vel[0]
		self.pos[1]+=self.vel[1]

		self.rect = pig.Rect(self.pos,self.size)
		self.checkBordes(mapa)
		screen.blit(self.img,self.pos)
	def checkBordes(self,mapa):

		for i in range(len(mapa)):
			y=pendientes[i]*(self.rect.centerx-mapa[i][0])+mapa[i][1]
			if y+10>self.rect.centery>=y and mapa[i][2]+2>self.rect.centerx>mapa[i][0]-2:#+2 para que no valla traspasar bloques
				self.pos[1]=y-self.size[1]
				self.vel[1]*=-1
				if pendientes[i]>0:
					self.vel[0]=abs(self.vel[0])*-1
				elif pendientes[i]<0:
					self.vel[0]=abs(self.vel[0])
				return

		if self.rect.left<0:
			self.pos[0]=0
			self.vel[0]*=-1

		elif self.rect.right>SCREEN_SIZE[0]:
			self.pos[0]=SCREEN_SIZE[0]-self.size[0]
			self.vel[0]*=-1

		if self.rect.bottom>SCREEN_SIZE[1]:
			self.pos[1]=SCREEN_SIZE[1]-self.size[1]
			self.gravityvel = 0
			self.vel[1]*=-1

		elif self.rect.top<0:
			self.pos[1]=1
		else:
			self.gravityvel+=self.grav
		
		
		
def mapRender(mapa):
	'renderiza el mapa en la pantalla'
	for plataforma in mapa:
		pig.draw.polygon(screen,DARK_RED,((plataforma[0],plataforma[1]),(plataforma[2],plataforma[3]),\
			(plataforma[2],plataforma[3]+10),(plataforma[0],plataforma[1]+10)))

barriles=[]

for x in range(10):
	name='barril {0}'.format(x)
	#b=barril([random.uniform(0,640),random.uniform(0,480)],[random.uniform(-10,10),random.uniform(-10,10)])
	b=barril([random.uniform(150,200),random.uniform(1,2)],[random.uniform(-10,10),random.uniform(-10,10)])
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
	mapRender(dimmapa)

	for i in barriles:
		i.update()
	

	pig.display.update()
	clock.tick(30)#Utilizar Constantes
	fps=clock.get_fps()
	pig.display.set_caption(str(fps))

pig.quit()