import pygame
import pygame.locals

from constants import *
from Player import Player


class InputManager():
    player: Player
    @classmethod
    def handle_input(cls):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.locals.K_a]:
            cls.player.move_direction += vec(-1,0)
        if keys_pressed[pygame.locals.K_w]:
            cls.player.move_direction += vec(0,-1)
        if keys_pressed[pygame.locals.K_s]:
            cls.player.move_direction += vec(0,1)
        if keys_pressed[pygame.locals.K_d]:
            cls.player.move_direction += vec(1, 0)
