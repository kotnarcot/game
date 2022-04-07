import pygame
from gun import Gun
import controls
from pygame.sprite import Group
from bullet import Bullet
# from enemy import Enemy


def run():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("SnenegrBlack")
    bg_color = (0, 105, 60)
    gun = Gun(screen)
    bullets = Group()
    bg_color5 = pygame.image.load("image/1616963578_18-p-serii-fon-20.jpg")
    rect5 = bg_color5.get_rect()


    # enemy = Enemy(screen)

    while True:
        screen.blit(bg_color5, rect5)
        controls.events(screen,gun,bullets)
        gun.update_gun()
        controls.update(bg_color,screen,gun,bullets)
        controls.delete(bullets)

run()
