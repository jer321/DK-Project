#Powerup.py
__Author__='Juan Fernando Otoya'
import pygame as pig
class powerup():
	def __init__(self,pos=(0,0),size=(32,32)):
		''
		self.rect=pig.Rect(pos,size)
		self.img=pig.image.load('Character\c2\powerup.png')
		self.img=pig.transform.scale(self.img,(size))
		self.show=True
	def update(self,player):
		if ((player.rect.right>self.rect.right>player.rect.left)\
		 or (player.rect.right>self.rect.left>player.rect.left))\
		 and player.rect.bottom>self.rect.centery>player.rect.top:
		 player.upgraded=True
		 self.show=False