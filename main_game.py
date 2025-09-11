import pygame, sys
from main_menu import draw_main_menu
from default import *


#메인 함수
running = True

while running:
    #FPS 설정
    clock.tick(60)
    # 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if game_state == "Start Menu":
            draw_main_menu()
            

    
    #화면 그리기
    Screen.fill(black)


    #업데이트
    pygame.display.flip()
