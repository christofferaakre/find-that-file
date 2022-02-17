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

# start in player's home directory
directory = pathlib.Path(os.path.expanduser('~/coding'))

pygame.init()

clock = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GUI File Explorer")

player = Player(vec(WIDTH/2, HEIGHT-30))
InputManager.player = player

camera = Camera(Camera.SimpleCamera, WIDTH, HEIGHT)

sprites = pygame.sprite.Group()
sprites.add(player)

all_files = list(directory.glob('*'))
files = list(filter(lambda x: not x.stem.startswith('.'), all_files))

n_cols = math.ceil(math.sqrt(len(files)))

col = 0
row = 0

blocks = pygame.sprite.Group()

space_used = WIDTH / n_cols * (n_cols -1) + BLOCK_WIDTH
free_space = WIDTH - space_used
x_padding = free_space / 2
y_margin = 100

for file in files:
    if col == n_cols:
        col = 0
        row += 1

    x = WIDTH / n_cols * col + BLOCK_WIDTH / 2 + x_padding
    y = row * (BLOCK_HEIGHT + y_margin) + BLOCK_HEIGHT / 2
    position = vec(x,y)
    print(f"col: {col}, row: {row}, position: {position}")
    block = None
    if file.is_dir():
        block = Directory(position, name=file.stem)
    else:
        block = File(position, name=file.stem)

    sprites.add(block)
    blocks.add(block)
    col += 1

player.sprite_group = blocks

font = pygame.font.SysFont('Arial', 12)

while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

    display.fill(BACKGROUND_COLOR)
    camera.update(player)

    for sprite in sprites:
        display.blit(sprite.surf, camera.apply(sprite.rect))

    for block in blocks:
        text = font.render(block.name, True, block.color)
        text_rect = camera.apply(text.get_rect(center=block.rect.center))
        display.blit(text, text_rect)

    InputManager.handle_input()
    player.move()
    player.collide(blocks)

    pygame.display.update()
    clock.tick(FPS)
