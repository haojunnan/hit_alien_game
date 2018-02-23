#coding:gb2312
import pygame
import function as fu
from settings import Settings
from pygame.sprite import Group
from star import Star
def run_game():
	#初始化屏幕
	pygame.init()
	al_setting = Settings()
	screen = pygame.display.set_mode((al_setting.screen_width,
	al_setting.screen_height))
	#设置标题
	pygame.display.set_caption("start!!!!")
	#创建星星
	star = Star(al_setting,screen)
	stars = Group()
	#创建星星群
	fu.creat_stars(al_setting,screen,stars)
	while True:
		#鼠标键盘响应
		fu.check_events()
		#更新屏幕
		fu.update_screen(al_setting,stars,screen)
		#更新星星
		#fu.update_star()
run_game()
