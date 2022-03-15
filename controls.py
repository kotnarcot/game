import sys
import pygame

def events(gun):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.kright = True
            if event.key == pygame.K_a:
                gun.kleft = True
            if event.key == pygame.K_w:
                gun.kup = True
            if event.key == pygame.K_s:
                gun.kdown = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.kright = False
            if event.key == pygame.K_a:
                gun.kleft = False
            if event.key == pygame.K_w:
                gun.kup = False
            if event.key == pygame.K_s:
                gun.kdown = False
