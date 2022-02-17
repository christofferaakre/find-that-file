import pygame
from pygame.sprite import Group
from constants import *

from pathlib import Path
import math

from Player import Player
from Block import Directory, File
from InputManager import InputManager
from Camera import Camera


class Game():
    def generate_blocks(self):

        all_files = list(self.directory.glob('*'))
        files = list(filter(lambda x: not x.stem.startswith('.'), all_files))

        n_cols= math.floor(math.sqrt(len(files)))
        col = 0
        row = 0

        self.sprites = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()

        x_padding = BLOCK_WIDTH / 2
        margin = 75

        for file in files:
            if col == n_cols:
                col = 0
                row += 1

            x = x_padding + col * (BLOCK_WIDTH + margin)
            y = -row * (BLOCK_HEIGHT + margin) - BLOCK_HEIGHT / 2
            position = vec(x,y)
            print(f"col: {col}, row: {row}, position: {position}")
            block = None
            if file.is_dir():
                block = Directory(position, name=file.name)
            else:
                block = File(position, name=file.name)

            self.sprites.add(block)
            self.blocks.add(block)
            col += 1


        self.player = Player(vec(WIDTH/2, BLOCK_HEIGHT * 2))
        InputManager.player = self.player

        self.camera = Camera(Camera.SimpleCamera, WIDTH, HEIGHT)

        self.sprites.add(self.player)


        self.player.sprite_group = self.blocks
