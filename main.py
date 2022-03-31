import pygame
from gun import Gun
import controls
from pygame.sprite import Group
from enemy import Enemy


def run():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("SnenegrBlack")
    bg_color = (0, 105, 60)
    gun = Gun(screen)
    bullets = Group()
    enemy = Enemy(screen)

    while True:
        controls.events(screen,gun,bullets,enemy)
        gun.update_gun()
        controls.update(bg_color,screen,gun, bullets , enemy)
        controls.delete(bullets)

run()
