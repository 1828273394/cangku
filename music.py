import pygame

pygame.mixer.init()
pygame.mixer.music.load('./a.mp3')

pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
	pass

print('播放结束!')
pygame.mixer.music.stop()