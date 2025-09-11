from default import *
import pygame, sys
def menu():
    sysfont = pygame.font.SysFont('malgungothic', 72)
    text = sysfont.render("Game Start", True, (0, 0, 255))
    text_rect = text.get_rect()
    Screen.blit(background, (0, 0)) 
    Screen.blit(text, text_rect) 
    pygame.Rect(300, 300, 40, 40)   
    pygame.display.flip()