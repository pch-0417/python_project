import pygame, sys
from main_menu import menu
from default import *

pygame.init()
pygame.font.init()
#메인 함수
def main():
    global running
    while running:
        #FPS 설정
        clock.tick(30)
        # 각종 입력 감지
        for event in pygame.event.get():
            if game_state == "Start Menu":
                menu()
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
    pygame.quit()
    sys.exit()

main()

