cm = True
import os
import pygame
print(os.uname())
x = 800, 600
screen = pygame.display.set_mode(x)
while cm == True:
	sys = input('$ ')
	if sys == 'QUIT':
		break
	elif sys == 'cd':
		x = input('/')
		os.chdir(x)
	os.system(sys)

