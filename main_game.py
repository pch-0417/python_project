import pygame, sys
from main_menu import menu
from default import *

pygame.init()
#메인 함수
running = True
def main():
    while running:
        #FPS 설정
        clock.tick(30)
        # 각종 입력 감지
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if game_state == "Start Menu":
                menu()


        #업데이트
        pygame.display.flip()
main()

