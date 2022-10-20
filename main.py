import pygame
from settings import *
from level import Level
from crosshair import Crosshair
from bullet import Bullet

# setup
pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Blaked Beans') 

icon = pygame.image.load('assets/sprites/icon.png').convert_alpha()
pygame.display.set_icon(icon)

pygame.mouse.set_visible(False)

bullet = Bullet('assets/sprites/bullet.png')
bullet_group = pygame.sprite.Group()
bullet_group.add(bullet)

crosshair = Crosshair('assets/sprites/crosshair.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

clock = pygame.time.Clock()

level = Level(level_map,screen)

shoot = False

while True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot = True
    if shoot == True:
        crosshair.shoot()

    screen.fill('blue')

    level.run()

    crosshair_group.draw(screen)
    crosshair_group.update()

    bullet_group.draw(screen)
    bullet_group.update()

    pygame.display.flip()

    clock.tick(60)