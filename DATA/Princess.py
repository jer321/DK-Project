#Princesa
__Author__='Juan Fernando Otoya'

import pygame as pig
import os

class princesa():
	def __init__(self,pos=(0,0),size=(45,62)):
		self.rect=pig.Rect(pos,size)
		self.img=pig.image.load(os.path.join('IMG','princess.png'))
		self.img=pig.transform.scale(self.img,size)

	def update(self,player):
		if ((player.rect.right>self.rect.right>player.rect.left)\
		 or (player.rect.right>self.rect.left>player.rect.left))\
		 and player.rect.bottom>self.rect.centery>player.rect.top:
		 player.win=True