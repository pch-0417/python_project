from default import *
import pygame, sys 

def menu_draw():
    sysfont = pygame.font.SysFont('malgungothic', 72)
    start_text = sysfont.render("Game Start", True, (0, 0, 255))
    optoins_text = sysfont.render("OPTOINS", True, (0, 0, 255))
    #text_font_size
    start_text_rect = start_text.get_rect()
    start_text_rect.center = (Screen_width_size // 2, Screen_height_size // 2)
    Screen.blit(background_img, (0, 0)) 
    Screen.blit(start_text, start_text_rect) 
    pygame.display.flip()


    
