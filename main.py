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
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()
        controls.events(gun)
        gun.update_gun()

run()
