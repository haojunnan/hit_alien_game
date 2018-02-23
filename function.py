#coding:gb2312
import pygame
import sys
from star import Star
from random import randint
def check_events():
	"""鼠标相应事件"""
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
		elif event.type == pygame.QUIT:
			sys.exit()
def update_screen(al_setting,stars,screen):
	"""刷新界面"""
	screen.fill(al_setting.bg_color)
	stars.draw(screen)
	pygame.display.flip()
def creat_star(al_setting,screen,star_num,stars,row_number):
	"""创建星星"""
	a = randint(0,1)
	if a == 1:	
		star = Star(al_setting,screen)
		star.width = star.rect.width
		star.x =star.width + star.width * 2 * star_num
		star.rect.x = star.x
		star.y = star.rect.height + star.rect.height * 2 * row_number
		star.rect.y = star.y
		stars.add(star)
def star_rows(al_setting,screen):
	"""计算有多少行星星"""
	star = Star(al_setting,screen)
	rows = int(al_setting.screen_height / (star.rect.height * 2))
	return rows
def creat_stars(al_setting,screen,stars):
	star = Star(al_setting,screen)
	star_nums =int(al_setting.screen_width / (star.rect.width * 2))
	row_numbers = star_rows(al_setting,screen)
	for row_number in range(row_numbers):
		for star_num in range(star_nums):
			creat_star(al_setting,screen,star_num,stars,row_number)
