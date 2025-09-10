from main_menu import draw_main_menu
import pygame, sys
       
#pygame 기본 초기화
pygame.init()

#pygame 기본 옵션 설정
Screen_width_size = 800
Screen_height_size = 600
Screen = pygame.display.set_mode((Screen_width_size, Screen_height_size))
title_name = "Pac-Man game"
pygame.display.set_caption(title_name)
game_state = "Start Menu"
#pygame 내의 필요한 설정

clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)

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
            darw_main_menu.menu()
            

    
    #화면 그리기
    Screen.fill(black)


    #업데이트
    pygame.display.flip()
