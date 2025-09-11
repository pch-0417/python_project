import pygame

#pygame 기본 옵션 설정
background = pygame.image.load("game_background.jpg")
Screen_width_size = 800
Screen_height_size = 667
Screen = pygame.display.set_mode((Screen_width_size, Screen_height_size))
title_name = "Pac-Man game"
pygame.display.set_caption(title_name)
game_state = "Start Menu"
running = True

#pygame 내의 필요한 설정
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)