import pygame, sys
from main_menu import menu_draw
from default import *

pygame.init()
pygame.font.init()

#메인 함수
def main():
    global running
    while running:
        #FPS setting 
        clock.tick(30)
        # key event
        for event in pygame.event.get():
            if game_state == "Start Menu":
                menu_draw()
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
    pygame.quit()
    sys.exit()

main()

