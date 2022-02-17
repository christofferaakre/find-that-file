import pygame

from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position: vec):
        super().__init__()

        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center=position)

        self.position: vec = position
        self.velocity: vec = vec(0,0)
        self.acceleration: vec = vec(0,0)

        self.move_direction: vec = vec(0,0)

    def move(self):
        # friction
        self.acceleration = self.move_direction * ACC
        self.acceleration += self.velocity * FRIC

        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        self.rect.center = self.position
        self.acceleration = vec(0,0)
        self.move_direction = vec(0,0)
