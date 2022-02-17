#!/usr/bin/env python3
import pygame
import pygame.locals
import sys

from constants import *
from Player import Player
from InputManager import InputManager

pygame.init()

BACKGROUND_COLOR = (0, 0, 0)

clock = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GUI File Explorer")

player = Player(position=(vec(WIDTH/2, HEIGHT/2)))
InputManager.player = player

sprites = pygame.sprite.Group()

sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

    display.fill(BACKGROUND_COLOR)

    for sprite in sprites:
        display.blit(sprite.surf, sprite.rect)

    InputManager.handle_input()
    player.move()

    pygame.display.update()
    clock.tick(FPS)
