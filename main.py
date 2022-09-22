import pygame
from settings import *
from level import Level

# setup
pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('gAME') 

icon = pygame.image.load('assets/sprites/icon.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

level = Level(level_map,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('darkgrey')
    level.run()
    
    pygame.display.flip()
    clock.tick(60)