import pygame
from constants import *

import sys
import pathlib

from utils import open_file

class Block(pygame.sprite.Sprite):
    def __init__(self, position: vec, name: str):
        super().__init__()

        self.position = position
        self.name = name

        self.surf = pygame.Surface((BLOCK_WIDTH, BLOCK_HEIGHT))
        self.surf.fill(BLOCK_COLOR)
        self.rect = self.surf.get_rect(center=position)

class Directory(Block):
    def __init__(self, position: vec, name: str):
        super().__init__(position, name)
        self.color = DIRECTORY_COLOR

    def interact(self, game):
        game.directory = game.directory / self.name
        game.generate_blocks()
        pass

class File(Block):
    def __init__(self, position: vec, name: str):
        super().__init__(position, name)
        self.color = FILE_COLOR

    def interact(self, game):
        path = game.directory / self.name
        open_file(path)
        sys.exit()
