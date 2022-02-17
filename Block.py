import pygame
from constants import *

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

class File(Block):
    def __init__(self, position: vec, name: str):
        super().__init__(position, name)
        self.color = FILE_COLOR

