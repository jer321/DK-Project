#Proyectil.py
__Author__='Juan Fernando Otoya'
import pygame as pig
from pygame.locals import *
from Constantes import *
class proyectil():
	def __init__(self,player=None,pos=(0,0),vel=20,size=(10,10)):
		self.img=pig.image.load(os.path.join('IMG','Character','Shot.png'))
		self.img=pig.transform.scale(self.img,size)
		self.rect=pig.Rect(pos,size)
		self.vel=vel
		if player.dir=='W':
			self.vel*=-1
		elif player.dir=='E':
			self.rect.right=player.rect.right
	def update(self):
		self.rect.centerx+=self.vel