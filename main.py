import pygame
from gun import Gun
import controls


def run():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("SnenegrBlack")
    bg_color = (0, 105, 60)
    gun = Gun(screen)

    while True:
        controls.events(screen,gun)
        gun.update_gun()
        controls.update(bg_color,screen,gun)

run()
