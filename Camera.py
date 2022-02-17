from typing import Callable
import pygame
from pygame import Rect
from constants import *

# Taken from here and adapted slightly
# https://stackoverflow.com/a/14357169/8304249
class Camera(object):
    def __init__(self, camera_func: Callable, width: int, height: int):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target: Rect):
        return target.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

    @classmethod
    def SimpleCamera(cls, state: Rect, target: Rect):
        left, top, _, _ = target
        _, _, width, height = state
        return Rect(-left + WIDTH / 2, -top + HEIGHT / 2, width, height)
