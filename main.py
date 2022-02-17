#!/usr/bin/env python3
import pygame
import pygame.locals
import os
import sys
import pathlib
import math

from constants import *
from Player import Player
from Block import Block, Directory, File
from InputManager import InputManager
from Camera import Camera

from Game import Game
game = Game()

# start in player's home directory

pygame.init()

clock = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GUI File Explorer")


font = pygame.font.SysFont('Arial', 12)

game.directory = pathlib.Path(os.path.expanduser('~/coding'))
game.generate_blocks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

    display.fill(BACKGROUND_COLOR)
    game.camera.update(game.player)

    for sprite in game.sprites:
        display.blit(sprite.surf, game.camera.apply(sprite.rect))

    for block in game.blocks:
        text = font.render(block.name, True, block.color)
        text_rect = game.camera.apply(text.get_rect(center=block.rect.center))
        display.blit(text, text_rect)

    InputManager.handle_input()
    game.player.move()
    game.player.collide(game.blocks, game)

    pygame.display.update()
    clock.tick(FPS)
