import pygame

#pygame background setting
background_img = pygame.image.load("game_background.jpg") 

#pygame tool
Screen_width_size = 800 
Screen_height_size = 667
Screen = pygame.display.set_mode((Screen_width_size, Screen_height_size)) # Screen setting
  #title setting
title_name = "Pac-Man game"
pygame.display.set_caption(title_name)
#pygame fps setting
clock = pygame.time.Clock()

# condition
game_state = "Start Menu"
running = True


#Color
black = (0, 0, 0)
white = (255, 255, 255)





