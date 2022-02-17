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

        n_cols = math.ceil(math.sqrt(len(files)))

        col = 0
        row = 0

        self.sprites = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()

        space_used = WIDTH / n_cols * (n_cols -1) + BLOCK_WIDTH
        free_space = WIDTH - space_used
        x_padding = free_space / 2
        y_margin = 100

        for file in files:
            if col == n_cols:
                col = 0
                row += 1

            x = WIDTH / n_cols * col + BLOCK_WIDTH / 2 + x_padding
            y = -row * (BLOCK_HEIGHT + y_margin) - BLOCK_HEIGHT / 2
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
