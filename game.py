#coding:gb2312
import pygame
import function as fu
from settings import Settings
from pygame.sprite import Group
from star import Star
def run_game():
	#��ʼ����Ļ
	pygame.init()
	al_setting = Settings()
	screen = pygame.display.set_mode((al_setting.screen_width,
	al_setting.screen_height))
	#���ñ���
	pygame.display.set_caption("start!!!!")
	#��������
	star = Star(al_setting,screen)
	stars = Group()
	#��������Ⱥ
	fu.creat_stars(al_setting,screen,stars)
	while True:
		#��������Ӧ
		fu.check_events()
		#������Ļ
		fu.update_screen(al_setting,stars,screen)
		#��������
		#fu.update_star()
run_game()
