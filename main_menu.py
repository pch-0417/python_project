from default import *
import pygame, sys

class draw_main_menu:
  def menu():
    while True:
      Screen.fill(black)
      font = pygame.font.SysFont('arial', 80)
      title = font.render('Pac-Man Game', True, black)
      start_button = font.render('Start', True, black)
      Screen.blit(title, (Screen_width_size/2)-(title.get_width()/2), (Screen_height_size/2)-((title.get_height)/2))
      Screen.blit(start_button, (Screen_width_size/2)-(title.get_width()/2), (Screen_height_size/2)+((title.get_height)/2))
      pygame.display.update()
      
