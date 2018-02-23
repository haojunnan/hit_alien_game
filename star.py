#coding:gb2312
import pygame
from pygame.sprite import Sprite
class Star(Sprite):
	def __init__(self,al_setting,screen):
		"""设置星星图案"""
		super(Star,self).__init__()
		self.screen = screen
		self.al_setting = al_setting
		self.image = pygame.image.load("xx.bmp")
		self.rect = self.image.get_rect()
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		#self.x = float(self.rect.x)
	def blitme():
		self.screen.blit(self.image,self.rect)
