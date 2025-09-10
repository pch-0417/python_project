#메뉴 화면 만들기
import pygame
       
#기본 메뉴 설정
pygame.init()
Screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
running = True
title = "Pac-Man"

while running:
    pygame.display.flip()
    clock.tick(60)
pygame.quit()