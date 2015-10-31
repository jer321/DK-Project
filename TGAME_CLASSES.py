#TGAME_CLASSES.py
import pygame as pig
from pygame.locals import *
from Colors import *
#cmd={
#	K_UP:up,
#	K_DOWN:down,
#	K_LEFT:left,
#	K_RIGHT:right,
#}
cmd={
	K_UP:'up',
	K_DOWN:'down',
	K_LEFT:'left',
	K_RIGHT:'right',
}

class control(object):
	def __init__(self,screensize=(600,480),map=None):
		'inicializa el ambiente grafico'
		pig.init()
		self.screen = pig.display.set_mode(screensize)
		self.running=True

	def CloseIf(self):
		for event in pig.event.get():
			if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
				self.running=False

	def detectCommand(self):
		key=pygame.key.get_pressed()
		for tecla in cmd:#Checkea cada uno de los comandos en para ver si estan siendo oprimidos
			if key[tecla]:#Si el comando esta siendo oprimido
				cmd[tecla]()#Hace el comando que esta siendo oprimido

class Player(pig.sprite.Sprite):
	def __init__(self,pos=(0,0),spriteShowing='donkeyKong2.png'):
		self.pos=pos
		self.posx,self.posy = self.pos
		self.spriteShowing = pig.image.load(spriteShowing)

		self.rectojo=pig.draw.rect(pantalla1.screen,STEEL_BLUE,(10,10,10,10))

	def update(self):
		'Actualiza todas las cosas del personaje'

	def commands(self):
		'Los comandos que son presionados para cambiar lo que hace el personaje'

pantalla1=control()
don=Player()


#Se haran varias pantallas para el Menu principal y los niveles, es decir varios loops de while 
#Main Loop
while pantalla1.running:
	pantalla1.CloseIf()
	pantalla1.screen.fill(WHITE)

	pig.display.update()

pig.quit()